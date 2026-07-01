# QA Artifact Set

Read the relevant spec **before** coding a module; add or update test IDs before implementing behavior they should protect.

## Index

- `TESTING_MASTER_PLAN.md` — strategy, levels, launch-blocking areas, tooling.
- `REQUIREMENT_TO_TEST_MATRIX.md` — every requirement → planned test IDs.
- `LOCAL_PR_CHECKLIST.md` — the pre-commit/PR checklist agents run locally.
- `../GOVERNANCE_AND_GATES.md` — Ready/Done definitions and the CI gate ladder.
- `../TRACEABILITY_MATRIX.md` — full chain coverage.

Add as the project matures: a concrete test-case catalogue (`TC-` IDs with steps), BDD acceptance scenarios, focused specs per launch-blocking area, goldset/benchmark governance for AI features, failure-mode matrix, coverage & flaky-test policy, architecture fitness rules, release gate checklist, and manual QA checklists for device/platform behavior.

## Principles

- Tests trace to requirements; orphan tests and untested requirements are both findings.
- Launch-blocking areas are defined in Phase 5 and never weakened to make a release date.
- A flaky test is fixed or quarantined with owner + expiry — never deleted quietly.
- Benchmark thresholds change only with a report artifact and a state-doc update.
