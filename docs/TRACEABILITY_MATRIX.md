# Traceability Matrix

## Methodology Chain

Every feature traces:

```txt
Requirement -> Use Case -> Domain Concept -> Design Class/Operation -> SSD -> Contract -> Test
```

Artifacts: `docs/software-engineering/02..07_*.md`; tests: `docs/qa/`.

## Functional Requirement Coverage

<!-- One row per requirement. The docs validator flags FR/NFR IDs that appear in
REQUIREMENTS.md but not here. Populate from Phase 4 onward. -->

| Requirement | Use Case | Domain Concept | Design Class / Operation | Test Case |
|---|---|---|---|---|
| FR-EXAMPLE-001 | UC-001 | (concept) | (Class.operation) | TC-EXAMPLE-001 |

## Non-Functional Requirement Coverage

| Requirement | Verification method | Gate | Evidence location |
|---|---|---|---|
| NFR-EXAMPLE-001 | (benchmark / audit / test) | (CI gate # or release ring) | (path) |
