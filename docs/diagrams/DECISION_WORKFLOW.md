# Decision Workflow (ADR Lifecycle)

Every major decision runs this loop, including the adversarial challenge and the reversal path. Template: `docs/templates/ADR_TEMPLATE.md`.

```mermaid
flowchart TB
  T["Decision trigger:<br/>framework / data store / provider /<br/>core algorithm / security model / structure"] --> DR["Draft ADR:<br/>context, options with pros/cons"]
  DR --> CH["ADVERSARIAL CHALLENGE:<br/>write the strongest argument<br/>AGAINST the preferred option"]
  CH --> SURV{"Preference survives<br/>the challenge?"}
  SURV -- no --> RE["Switch preference or<br/>gather more evidence (spike)"]
  RE --> DR
  SURV -- yes --> DEC["Record: decision, consequences<br/>(positive/negative/operational),<br/>REVERSAL CONDITIONS"]
  DEC --> ACC{"Human acceptance pass"}
  ACC -- accept --> A["Status: Accepted"]
  ACC -- revise --> DR
  ACC -- defer --> DEF["Status: Deferred<br/>+ what unblocks it"]
  A --> LIVE["Decision in force:<br/>code cites ADR-### in comments"]
  DEF -.->|"unblocking evidence arrives"| DR

  LIVE --> MON["Operations: watch<br/>reversal conditions"]
  MON --> RC{"Reversal condition<br/>triggered?"}
  RC -- no --> MON
  RC -- yes --> REOPEN["Reopen: new ADR supersedes,<br/>old one marked Superseded<br/>(never edited away)"]
  REOPEN --> DR
```

## Rules

- An ADR without reversal conditions is not acceptable — every decision must state what evidence would reopen it.
- Deferring is legitimate; deferring without an unblock condition is not.
- Superseded ADRs stay in the repo forever: they are the project's institutional memory of *why not*.
- Agents cite ADR IDs in code comments where the decision shapes the implementation.
