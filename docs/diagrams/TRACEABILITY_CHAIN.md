# Traceability Chain

Every feature traces from requirement to test. Coverage is one row per requirement in `docs/TRACEABILITY_MATRIX.md`.

```mermaid
flowchart LR
  R["Requirement<br/>FR-AREA-###<br/>(docs/REQUIREMENTS.md)"]
  U["Use Case UC-###<br/>(02_USE_CASES)"]
  D["Domain Concept<br/>(03_DOMAIN_MODEL)"]
  C["Design Class / Operation<br/>(05_DESIGN_CLASS_DIAGRAM)"]
  S["SSD Event<br/>(06_SYSTEM_SEQUENCE_DIAGRAMS)"]
  O["Operation Contract<br/>(07_OPERATION_CONTRACTS)"]
  T["Test Case TC-AREA-###<br/>(docs/qa/)"]
  CODE["Implementation<br/>(comments cite REQ + ADR)"]

  R --> U --> D --> C --> S --> O --> T
  T -.->|verifies| CODE
  C -.->|shapes| CODE
  R -.->|cited in| CODE
```

## Change Impact Flows Both Ways

```mermaid
flowchart TB
  CH["Proposed change"] --> Q1{"New behavior?"}
  Q1 -- yes --> NR["New/updated requirement ID<br/>+ matrix row + planned test ID"]
  Q1 -- no --> Q2{"Changes existing behavior?"}
  Q2 -- yes --> TR["Walk the chain backward:<br/>which tests, contracts, use cases<br/>does this touch?"]
  Q2 -- "no (pure refactor)" --> RF["No matrix change;<br/>existing tests must stay green"]
  NR --> IMPL["Implement with tests"]
  TR --> IMPL
  RF --> IMPL
```

The chain is what lets any agent answer, in seconds: *why does this code exist, and what breaks if I change it?*
