# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**The full agent contract lives in `AGENTS.md` — read it first.** This file only adds Claude-Code-specific notes.

## Session Protocol

- Start every session by reading `docs/CURRENT_TASK.md`, `docs/NEXT_TASK.md`, and `docs/CURRENT_THINKING.md`. They are the project's working memory; the conversation is not.
- Use plan mode (or an explicit written plan) before any multi-file change. Separate exploration from execution.
- Use subagents for wide read-only exploration so the main context stays focused on the task.
- End every session by updating the state files and writing the next exact task — even if the session was cut short.

## Commands

```bash
python tools/qa/validate_docs.py     # link/state-file/placeholder/file-size checks
python tools/qa/scan_secrets.py      # obvious committed secrets
```

Add project build/test/lint commands here as toolchains land (and mirror them in `AGENTS.md` and `README.md`).

## Hard Rules (summary — full versions in AGENTS.md)

- No production feature code before the SRS + ADR gate (Phase 6 in `docs/LIFECYCLE_PHASES.md`).
- Every coding task needs a work packet with owned/forbidden files first.
- Short-burst semantic commits with AI trailers (`docs/COMMIT_POLICY.md`).
- Show evidence for every "it works" claim; record every skipped check.
- Source files target 200–300 lines; exceptions go in `docs/TECH_DEBT.md`.
