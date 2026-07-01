# Orchestration Topologies

The four adoption stages of multi-agent work. Adopt in order; each stage amplifies the process quality of the previous one. Full rules: `docs/MULTI_AGENT_ORCHESTRATION.md`.

## Stage 1 — Single Agent, Role-Sequenced (default)

```mermaid
flowchart LR
  H["Human"] --> AN["Analyst<br/>session"] --> AR["Architect<br/>session"] --> PL["Planner<br/>session"] --> IM["Implementer<br/>session(s)"] --> RV["Reviewer<br/>session"]
  RV -->|findings| IM
```

## Stage 2 — Writer / Reviewer Pair

```mermaid
flowchart LR
  P["Work packet"] --> W["Writer agent<br/>code + tests + evidence"]
  W -->|"diff + packet only<br/>(no reasoning transcript)"| R["Reviewer agent<br/>fresh context, adversarial"]
  R -->|accept| M["Merge"]
  R -->|findings| W
```

## Stage 3 — Parallel Implementers, Folder Ownership

```mermaid
flowchart TB
  O["Orchestrator<br/>(human or agent)"] --> A["Agent A<br/>owns: services/api/"]
  O --> B["Agent B<br/>owns: apps/client/"]
  O --> C["Agent C<br/>owns: docs/qa/"]
  A & B & C --> Q["Merge queue<br/>Reviewer + CI gates"]
  Q --> S["State files<br/>(single writer per window)"]
```

## Stage 4 — Swarm With Merge Queue (advanced)

```mermaid
flowchart TB
  BOARD["Work package board<br/>(Ready packets)"] --> S1["agent"] & S2["agent"] & S3["agent"] & S4["agent"]
  S1 & S2 & S3 & S4 --> MQ["Merge queue"]
  MQ --> RV["Reviewer agents"] --> CI["CI gate ladder"] --> INT["Integration"]
  INT --> BOARD
  HUM["Human: priorities,<br/>pause points, waivers"] -.-> BOARD & MQ
```

## Choosing A Stage

| Signal | Move to |
|---|---|
| Solo project, phases still early | Stage 1 |
| Defects slipping through self-review | Stage 2 |
| Ready packets queuing faster than one agent clears them | Stage 3 |
| Stages 1–3 running smoothly for multiple slices | Stage 4 (maybe) |

Never jump a stage to feel fast — a swarm running a weak process produces weak output at swarm speed.
