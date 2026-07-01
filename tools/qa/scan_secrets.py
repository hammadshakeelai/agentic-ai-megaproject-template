#!/usr/bin/env python3
"""Obvious-secret scanner: cheap last line of defense, not a real secret manager.

Flags common credential patterns in tracked-looking files. Pair with a proper
scanner (gitleaks, trufflehog) at CI gate 3.

Exit code 0 = clean, 1 = findings.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "build", "dist", "__pycache__"}
SKIP_FILES = {"scan_secrets.py"}
TEXT_SUFFIXES = {".md", ".txt", ".py", ".ts", ".js", ".dart", ".go", ".rs", ".java",
                 ".yml", ".yaml", ".json", ".toml", ".ini", ".cfg", ".env", ".sh",
                 ".ps1", ".xml", ".gradle", ".properties"}

PATTERNS = [
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[0-9A-Za-z]{36,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[0-9A-Za-z\-]{10,}\b")),
    ("private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("generic assignment", re.compile(
        r"(?i)\b(?:api[_-]?key|secret|password|token)\b\s*[:=]\s*['\"][^'\"\s]{16,}['\"]")),
    ("bearer header", re.compile(r"(?i)authorization:\s*bearer\s+[0-9a-z._\-]{20,}")),
]

ALLOW_HINTS = ("example", "placeholder", "your-", "xxxx", "<", "{{", "changeme", "dummy", "sample")


def main() -> int:
    findings: list[str] = []
    for path in ROOT.rglob("*"):
        if path.is_dir() or set(path.parts) & SKIP_DIRS:
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES or path.name in SKIP_FILES:
            continue
        if path.name == ".env.example":
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            lowered = line.lower()
            if any(hint in lowered for hint in ALLOW_HINTS):
                continue
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path.relative_to(ROOT)}:{lineno}: possible {label}")

    for finding in findings:
        print(f"FAIL: {finding}")
    if findings:
        print(f"\nsecret scan FAILED: {len(findings)} finding(s)")
        return 1
    print("secret scan clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
