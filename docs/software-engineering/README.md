# Software Engineering Artifact Set

This folder holds the methodology chain artifacts (see `docs/METHODOLOGY.md`):

```txt
Inception -> Requirements/SRS -> Process Model -> Use Cases -> Domain Model
-> DFDs -> Design Class Diagram -> SSDs -> Operation Contracts
-> Packages & CRC -> Final Report
```

## Artifact Index

- `00_INCEPTION.md` — problem, vision, scope, actors, technology direction, repo setup. *(Phase 0)*
- `01_PROCESS_MODEL.md` — selected process model, loop, fallback + switch trigger. *(Phase 2)*
- `02_USE_CASES.md` — use case diagram, high-level + expanded use cases. *(Phase 4)*
- `03_DOMAIN_MODEL.md` — conceptual domain classes, attributes, relationships. *(Phase 4)*
- `04_DATA_FLOW_DIAGRAMS.md` — DFD level 0/1, key level 2 flows. *(Phase 4)*
- `05_DESIGN_CLASS_DIAGRAM.md` — software classes, operations, interfaces, boundaries. *(Phase 4)*
- `06_SYSTEM_SEQUENCE_DIAGRAMS.md` — SSDs for essential use cases. *(Phase 4)*
- `07_OPERATION_CONTRACTS.md` — pre/postcondition contracts for system operations. *(Phase 4)*
- `08_PACKAGES_CRC.md` — package dependencies and CRC cards. *(Phase 4)*
- `09_FINAL_REPORT_PLAN.md` — assembled report order and build plan. *(any time after Phase 5)*

Each file contains its own section skeleton and **exit criteria**. An artifact is done when its exit criteria are met, not when it looks long enough.

## Traceability Rule

Every feature must trace:

```txt
FR -> Use Case -> Domain Concept -> Design Class/Operation -> SSD Event -> Operation Contract -> Test Case
```

Coverage table: `docs/TRACEABILITY_MATRIX.md`.
