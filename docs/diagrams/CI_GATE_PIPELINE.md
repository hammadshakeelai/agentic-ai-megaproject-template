# CI Gate Pipeline

The five-gate ladder from `docs/GOVERNANCE_AND_GATES.md`, and what a change passes through on its way to production.

```mermaid
flowchart LR
  subgraph DEV ["Local (agent session)"]
    L1["validators +<br/>module tests"]
  end
  subgraph CI ["Continuous Integration"]
    G1["Gate 1 · Docs CI<br/>links, state files,<br/>file sizes, secrets"]
    G2["Gate 2 · Code CI<br/>build, unit tests,<br/>lint, contracts"]
    G3["Gate 3 · Security CI<br/>dep audit, DTO scan,<br/>authz negatives"]
    G4["Gate 4 · Benchmark CI<br/>goldsets, snapshots,<br/>cost counters"]
  end
  subgraph REL ["Release"]
    G5["Gate 5 · Release CI<br/>build, signing dry-run,<br/>telemetry smoke"]
    RING["Ring gates<br/>internal → alpha →<br/>beta → production"]
  end
  L1 --> G1 --> G2 --> G3 --> G4 --> G5 --> RING
```

Gates activate progressively — Gate 1 from day one; each later gate turns on when its prerequisites exist. **Local/CI parity is mandatory:** every CI check has a documented local command, so agents never discover a gate for the first time in CI.

## Merge Decision

```mermaid
flowchart TB
  PR["Change (PR / merge request)"] --> P0{"Any P0 gate failure?"}
  P0 -- yes --> BLOCK["Blocked. No exceptions."]
  P0 -- no --> P1{"P1 failure?"}
  P1 -- yes --> WV{"Recorded waiver with<br/>owner + expiry?"}
  WV -- no --> BLOCK
  WV -- yes --> WARN["Merge allowed;<br/>release builds blocked<br/>until resolved"]
  P1 -- no --> FLK{"Flaky test involved?"}
  FLK -- yes --> Q["Fix or quarantine with<br/>owner + expiry, then re-run"]
  Q --> P0
  FLK -- no --> MERGE["Merge + state-doc<br/>update in same burst"]
```
