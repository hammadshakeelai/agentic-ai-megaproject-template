# Commit Policy

## Purpose

The project moves in short, reviewable bursts so humans and AI agents can understand exactly what changed, why it changed, and who changed it. Commit history is a first-class handoff artifact.

## Short-Burst Rule

Prefer small semantic commits after each coherent unit of work:

- one planning-doc update
- one scaffold folder/package addition
- one module skeleton
- one contract group
- one domain rule plus its tests
- one bug fix plus its regression test

Avoid giant mixed commits. If a change touches multiple domains, split by intent unless the files must land together to keep the repo working.

## Commit Message Format

Concise semantic subjects, imperative mood:

```txt
docs(process): add short-burst commit policy
scaffold(api): add submissions module shell
test(domain): cover ranking cap rule
fix(upload): make completion idempotent
```

Types: `docs` `scaffold` `feat` `fix` `test` `refactor` `chore` `security` `perf`

## Required Trailers For AI Work

Every AI-authored commit includes:

```txt
AI-Agent: <model/tool name, plainly>
AI-Work-Mode: autonomous|pairing|review
AI-Commit-Time: <local ISO 8601 with timezone>
Work-Package: WP-###
Requirements: FR-XXX-001, NFR-YYY-002
Process-Docs-Updated: yes|no
```

The commit template in `.gitmessage.txt` scaffolds these. Why they matter: they make it possible to audit which agent produced what, correlate defects with work modes, and verify the Prime Rule was followed — per commit, forever.

## Before-Commit Checklist

- Work packet or task state is clear.
- Changes are scoped to one semantic purpose.
- Requirement IDs referenced where useful.
- Tests or verification were run, or the reason is recorded.
- State docs updated if the task changed them.
- No secrets, sensitive data, or generated build artifacts staged.

## Cadence

Commit after each stable mini-milestone. Do not commit broken code unless it is an intentional WIP checkpoint on a private branch with the recovery path written in `docs/NEXT_TASK.md` and in the commit message.

Short bursts are also the crash-recovery mechanism: when a session dies, the blast radius is one burst.
