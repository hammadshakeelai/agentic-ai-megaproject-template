# Architecture Decision Records

One decision per file: `ADR-###-short-slug.md`, from `docs/templates/ADR_TEMPLATE.md`. Lifecycle: `docs/diagrams/DECISION_WORKFLOW.md`.

Rules:

- Every ADR contains an **Internal Challenge** (strongest argument against) and **Reversal Conditions**. Both are mandatory.
- Statuses: Proposed → Accepted / Deferred (+ unblock condition) / Superseded by ADR-###.
- Superseded ADRs are never deleted or edited away — they are institutional memory.
- Run an explicit acceptance pass before the Phase 3 gate: disposition every ADR.
- Decisions that need ADRs: platform/framework, data store, external providers, core algorithms, security/privacy model, deployment, release process, repo structure — and anything an agent would otherwise silently re-decide.

Index (maintain as ADRs land):

| ID | Title | Status |
|---|---|---|
| | | |
