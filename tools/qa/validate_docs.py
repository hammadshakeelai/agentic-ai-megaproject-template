#!/usr/bin/env python3
"""Docs validator: the always-on Gate 1 check.

Validates the process guarantees this template depends on:
  1. Required state files exist and are non-empty.
  2. Relative Markdown links resolve.
  3. Files in docs/diagrams/ contain at least one Mermaid block.
  4. Source files respect the hard file-size guardrail.
  5. Leftover template placeholders ({{...}}) are reported (warning only).
  6. Requirement IDs in REQUIREMENTS.md appear in the traceability matrix
     (activates automatically once REQUIREMENTS.md exists).

Exit code 0 = pass, 1 = failures found. Warnings never fail the build.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

REQUIRED_STATE_FILES = [
    "AGENTS.md",
    "docs/PROCESS.md",
    "docs/CURRENT_TASK.md",
    "docs/NEXT_TASK.md",
    "docs/CURRENT_THINKING.md",
    "docs/BACKLOG.md",
    "docs/BUGS_AND_RISKS.md",
    "docs/TECH_DEBT.md",
]

# Hard cap: soft target is 200-300 lines (docs/PROCESS.md); the validator only
# fails clear violations so generated/vendored exceptions stay manageable.
MAX_SOURCE_LINES = 500
SOURCE_SUFFIXES = {".py", ".ts", ".tsx", ".js", ".jsx", ".dart", ".go", ".rs",
                   ".java", ".kt", ".swift", ".rb", ".cs", ".cpp", ".c", ".h"}
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "build", "dist",
             "__pycache__", ".dart_tool", "target", "knowledge"}

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)")
REQ_ID_RE = re.compile(r"\b(?:FR|NFR)-[A-Z]+-\d{3}\b")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)


def iter_files(suffixes: set[str]) -> list[Path]:
    out = []
    for path in ROOT.rglob("*"):
        if path.is_dir() or set(path.parts) & SKIP_DIRS:
            continue
        if path.suffix.lower() in suffixes:
            out.append(path)
    return out


def check_state_files(errors: list[str]) -> None:
    for rel in REQUIRED_STATE_FILES:
        path = ROOT / rel
        if not path.is_file():
            errors.append(f"missing required state file: {rel}")
        elif len(path.read_text(encoding="utf-8", errors="replace").strip()) < 20:
            errors.append(f"required state file is effectively empty: {rel}")


def check_links(errors: list[str]) -> None:
    for md in iter_files({".md"}):
        text = md.read_text(encoding="utf-8", errors="replace")
        for match in LINK_RE.finditer(text):
            target = match.group(1)
            if target.startswith(("http://", "https://", "mailto:", "{{")):
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                rel = md.relative_to(ROOT)
                errors.append(f"broken link in {rel}: {target}")


def check_mermaid(errors: list[str]) -> None:
    diagrams = ROOT / "docs" / "diagrams"
    if not diagrams.is_dir():
        return
    for md in diagrams.glob("*.md"):
        if md.name == "README.md":
            continue
        if "```mermaid" not in md.read_text(encoding="utf-8", errors="replace"):
            errors.append(f"diagram file has no mermaid block: {md.relative_to(ROOT)}")


def check_file_sizes(errors: list[str]) -> None:
    for src in iter_files(SOURCE_SUFFIXES):
        lines = len(src.read_text(encoding="utf-8", errors="replace").splitlines())
        if lines > MAX_SOURCE_LINES:
            errors.append(
                f"source file exceeds hard {MAX_SOURCE_LINES}-line cap "
                f"({lines} lines): {src.relative_to(ROOT)} "
                f"- split it or record a TD entry in docs/TECH_DEBT.md"
            )


def check_placeholders(warnings: list[str]) -> None:
    for md in iter_files({".md"}):
        if "templates" in md.parts or md.name == "GETTING_STARTED.md":
            continue
        for token in sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", md.read_text(encoding="utf-8", errors="replace")))):
            warnings.append(f"unfilled placeholder {token} in {md.relative_to(ROOT)}")


def check_traceability(errors: list[str]) -> None:
    req = ROOT / "docs" / "REQUIREMENTS.md"
    matrix = ROOT / "docs" / "TRACEABILITY_MATRIX.md"
    if not (req.is_file() and matrix.is_file()):
        return
    # Commented-out text is guidance, not requirements.
    req_text = HTML_COMMENT_RE.sub("", req.read_text(encoding="utf-8", errors="replace"))
    matrix_text = HTML_COMMENT_RE.sub("", matrix.read_text(encoding="utf-8", errors="replace"))
    req_ids = set(REQ_ID_RE.findall(req_text))
    matrix_ids = set(REQ_ID_RE.findall(matrix_text))
    for missing in sorted(req_ids - matrix_ids):
        errors.append(f"requirement {missing} has no row in TRACEABILITY_MATRIX.md")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    check_state_files(errors)
    check_links(errors)
    check_mermaid(errors)
    check_file_sizes(errors)
    check_placeholders(warnings)
    check_traceability(errors)

    for warning in warnings:
        print(f"WARN: {warning}")
    for error in errors:
        print(f"FAIL: {error}")

    if errors:
        print(f"\ndocs validation FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"docs validation passed ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
