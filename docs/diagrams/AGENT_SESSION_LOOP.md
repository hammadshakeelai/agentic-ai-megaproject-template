# Agent Session Loop

The inner loop every agent session runs, from orientation to handoff. This is the operational heart of the whole methodology.

```mermaid
flowchart TB
  S(["Session start"]) --> O["ORIENT<br/>read AGENTS.md → CURRENT_TASK →<br/>NEXT_TASK → CURRENT_THINKING"]
  O --> CL["CLAIM<br/>take one work packet<br/>(write one if missing)"]
  CL --> RD{"Packet passes<br/>Definition of Ready?"}
  RD -- no --> FIX["Fix the packet or escalate<br/>to human — do not start"]
  FIX --> CL
  RD -- yes --> EX["EXPLORE<br/>packet-named ADRs, specs,<br/>module README, then source"]
  EX --> PL["PLAN<br/>written plan: files, tests,<br/>commit bursts, risks"]
  PL --> HP{"Plan needs human<br/>decision or is irreversible?"}
  HP -- yes --> PAUSE["Pause point:<br/>ask, wait, record answer"]
  PAUSE --> PL
  HP -- no --> IM["IMPLEMENT<br/>one short burst:<br/>code + tests together"]
  IM --> V["VERIFY<br/>run tests/validators,<br/>capture output as evidence"]
  V --> OK{"Green?"}
  OK -- no --> DBG["Diagnose; if scope grows,<br/>split packet / record risk"]
  DBG --> IM
  OK -- yes --> CM["COMMIT<br/>semantic subject + AI trailers"]
  CM --> MORE{"Packet finished?"}
  MORE -- "no, and context healthy" --> IM
  MORE -- "no, context low" --> WIND["Wind down early:<br/>clean stop beats truncated work"]
  MORE -- yes --> UP
  WIND --> UP["UPDATE STATE<br/>CURRENT_TASK, NEXT_TASK,<br/>CURRENT_THINKING, ledgers"]
  UP --> AR{"Direction changed<br/>this session?"}
  AR -- yes --> CA["Archive conversation<br/>(raw or summary)"]
  AR -- no --> HO
  CA --> HO["HANDOFF REPORT<br/>changed files, evidence,<br/>not-done list, next exact task"]
  HO --> E(["Session end"])
```

**Invariants:**
- Never skip ORIENT, even for "quick" tasks — stale context is how agents undo prior decisions.
- One packet per session; splitting mid-flight is a planning failure to record.
- Every VERIFY produces pasted evidence; every skipped check produces a reason + follow-up.
- The session may end early at any time *if* UPDATE STATE and HANDOFF happen. The only unacceptable ending is a silent one.
