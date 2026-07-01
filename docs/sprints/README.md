# Sprints

One folder per sprint, one plan per sprint, one file per packet:

```txt
docs/sprints/
├── README.md                  (this file)
├── SPRINT_0_PLAN.md           (from docs/templates/SPRINT_PLAN_TEMPLATE.md)
└── sprint-0/
    ├── S0-001_first_packet.md (from docs/templates/WORK_PACKAGE_TEMPLATE.md)
    └── S0-002_...
```

Rules:

- Sprint 0 is created at the Phase 6 gate and contains scaffold/toolchain packets only.
- Every packet is sized to one agent session and passes Definition of Ready before claim.
- Packet status changes are mirrored on `docs/WORK_PACKAGE_BOARD.md`.
- A sprint ends when its packets are Complete — then retro notes go to `docs/CURRENT_THINKING.md` and the next plan is cut.
