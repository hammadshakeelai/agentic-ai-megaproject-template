# Work Package Lifecycle

Packet states from proposal to completion. Board: `docs/WORK_PACKAGE_BOARD.md`.

```mermaid
stateDiagram-v2
    [*] --> Proposed: packet drafted from<br/>sprint plan / backlog
    Proposed --> Ready: passes Definition of Ready<br/>(owned/forbidden files, tests, rollback)
    Proposed --> Rejected: not needed / merged<br/>into another packet
    Ready --> InProgress: claimed by exactly<br/>one agent session
    InProgress --> Blocked: dependency or human<br/>decision needed
    Blocked --> Ready: unblocked (record<br/>what unblocked it)
    InProgress --> InReview: implementation done,<br/>evidence attached
    InReview --> InProgress: reviewer rejects<br/>(findings handed back)
    InReview --> Complete: acceptance criteria met,<br/>state docs updated
    InProgress --> Ready: session ended early<br/>(clean stop + handoff)
    Complete --> [*]
    Rejected --> [*]
```

## Rules

- **Ready** is a real gate, not a label — see `docs/GOVERNANCE_AND_GATES.md`.
- **InProgress** implies exactly one owner; two agents on one packet is a process violation.
- **Blocked** packets record what unblocks them; a blocked packet with no unblock condition is a planning bug.
- A packet that returns to Ready twice gets split or re-planned — the packet, not the agent, is at fault.
- **Complete** requires evidence, not assertion.
