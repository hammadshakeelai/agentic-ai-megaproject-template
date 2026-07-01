# Repository Guidelines — The Agent Contract

Every AI agent (and human) working in this repository follows this contract. It exists so the project survives context-window limits, session ends, model rotations, and handoffs between many agents over a long timeline.

## Mandatory Session Start (Read Order)

Before meaningful work, read in this order and stop as soon as you have enough context for your task:

1. `AGENTS.md` (this file)
2. `docs/CURRENT_TASK.md` — where the project is right now
3. `docs/NEXT_TASK.md` — the exact next step and why
4. `docs/CURRENT_THINKING.md` — live decisions, debates, and baseline
5. `docs/PROCESS.md` — the rules in force
6. The relevant work packet, ADRs, and module README for your task
7. Only then: source files

Never start from the source tree. Start from the state files.

## Mandatory Session End (Update Order)

Before ending meaningful work:

1. Update changed artifact docs, and `docs/TRACEABILITY_MATRIX.md` if requirements/use cases/contracts/tests changed.
2. Update `docs/CURRENT_TASK.md` (what happened this session).
3. Update `docs/NEXT_TASK.md` (the exact next step a fresh agent should take).
4. Update `docs/CURRENT_THINKING.md` (new decisions, resolved/opened debates).
5. Update `docs/BACKLOG.md`, `docs/BUGS_AND_RISKS.md`, `docs/TECH_DEBT.md` as needed.
6. Update `docs/conversation-archive/` if the conversation changed direction, requirements, architecture, process, or risks.
7. Commit in short semantic bursts with AI trailers (`docs/COMMIT_POLICY.md`).

## Phase Gate Rule

Do not start production feature code before the SRS and the architecture ADR pack are accepted (see `docs/LIFECYCLE_PHASES.md`). Do not skip a phase without an ADR explaining why.

## Work Packet Rule

Every coding task must be defined as a work packet before implementation (`docs/templates/WORK_PACKAGE_TEMPLATE.md`): goal, requirement IDs, **owned files**, **forbidden files**, acceptance criteria, test plan, rollback, and handoff notes. If no packet exists for your task, write one first.

## Traceability Rule

Every real feature maintains the chain:

```txt
Requirement -> Use Case -> Domain Concept -> Design Class/Operation -> Contract -> Test
```

New requirements get IDs (`FR-<AREA>-###`, `NFR-<AREA>-###`) and a row in `docs/TRACEABILITY_MATRIX.md`.

## Decision Rule

Major decisions (frameworks, data stores, providers, core algorithms, security/privacy model, repo structure) require an ADR in `docs/adr/` with: options, the **strongest argument against** the preferred choice, consequences, and reversal conditions. A decision is not strong until it survives a serious challenge.

## Code Rules

- Keep source files around 200–300 lines; split by feature/domain before files get hard to test or hand off. Log exceptions in `docs/TECH_DEBT.md`.
- Keep public interfaces small and explicit; do not bypass module boundaries.
- Comments preserve durable context (`// REQ FR-XXX-001, ADR-004: why this exists`), never restate syntax.
- Prefer many focused tests over one broad test file. Read the relevant `docs/qa/` spec before coding a module.

## Evidence Rule

Never assert success — show it. Every claim of "tests pass" or "it works" must be backed by pasted command output, and every skipped verification must be recorded with a reason and follow-up in the task closeout.

## Parallel Agent Rule

Two agents must never edit the same files in the same time window. Parallel work is partitioned by owned folders in the work packets. See `docs/MULTI_AGENT_ORCHESTRATION.md`.

## Conversation Preservation Rule

When a user prompt or an AI answer changes product direction, requirements, architecture, process, or risks, save it (raw or summarized) in `docs/conversation-archive/`. Never store secrets, credentials, private user data, or hidden system instructions.

## Security Rule

Never commit secrets, API keys, credentials, `.env` files, or `{{SENSITIVE_DATA_CLASSES}}`. Run `python tools/qa/scan_secrets.py` before committing when in doubt.

## Final Response Checklist

Every meaningful session ends with a report that states: what changed, files changed, tests/validation run (with evidence), what was NOT done, the next exact task, and commit hashes if any.
