# Handoff Sequence

Agent-to-agent handoff flows through repository state, never through shared conversation. The test of a good handoff: the incoming agent never needs the outgoing agent's chat transcript.

```mermaid
sequenceDiagram
    autonumber
    participant H as Human / Orchestrator
    participant A as Agent A (outgoing)
    participant R as Repo (state files + commits)
    participant B as Agent B (incoming)

    H->>A: Assign work packet WP-042
    A->>R: Read state files, packet, ADRs
    loop short bursts
        A->>A: implement + verify
        A->>R: semantic commit (AI trailers)
    end
    A->>R: Update CURRENT_TASK / NEXT_TASK / CURRENT_THINKING
    A->>R: Archive conversation if direction changed
    A-->>H: Final report: changes, evidence, not-done, next task
    H->>B: Continue with next packet
    B->>R: ORIENT: read state files
    B->>R: git log / git status (verify clean baseline)
    Note over B,R: Uncommitted leftovers are untrusted:<br/>re-verify before building on them
    B->>B: proceed with session loop
```

## Failure Path: Interrupted Session

```mermaid
sequenceDiagram
    autonumber
    participant A as Agent A (died mid-task)
    participant R as Repo
    participant B as Agent B (recovery)

    A--xR: session ends silently (context/crash/stop)
    B->>R: read NEXT_TASK.md + git status/log
    alt last commit is stable burst
        B->>R: discard/stash untrusted uncommitted changes
        B->>B: resume packet from last green state
    else last commit is marked WIP checkpoint
        B->>R: read recovery path from commit message + NEXT_TASK
        B->>B: verify, then continue or revert
    else state files stale
        B->>B: reconstruct from git history, then FIX STATE FILES FIRST
        Note over B: record the staleness as a process bug in BUGS_AND_RISKS.md
    end
```
