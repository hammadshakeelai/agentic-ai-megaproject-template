# Testing Master Plan

## Strategy

<!-- Which levels exist, what each protects, and who runs it where. -->

| Level | Scope | Runs | Gate |
|---|---|---|---|
| Unit | pure logic, domain rules | every session + CI gate 2 | merge |
| Integration | module boundaries, contracts | CI gate 2/3 | merge |
| Contract/DTO | public schemas, forbidden fields | CI gate 3 | merge |
| Benchmark/goldset | AI/algorithmic quality | CI gate 4 | exposure |
| E2E / acceptance | user-visible flows (BDD) | pre-release | ring |
| Manual | device/platform behavior | per checklist | ring |

## Launch-Blocking Areas

<!-- Define in Phase 5: the invariants that stop feature exposure when red, regardless of schedule.
Examples: data-leak prevention on public outputs, core domain state integrity, idempotent writes,
abuse/moderation paths, payment correctness. -->

| Area | Why blocking | Test IDs |
|---|---|---|
| | | |

## Test Data Governance

<!-- Fixtures, seeds, goldsets: where they live, how they change, who approves threshold changes. -->

## Tooling

<!-- Test frameworks per module, decided by ADR. Local commands MUST match CI commands. -->

## Exit Criteria (Phase 5)

- Every requirement has a planned test ID in `REQUIREMENT_TO_TEST_MATRIX.md`.
- Launch-blocking areas are listed with owners.
- Ready/Done definitions are in force.
