# Sprint N Plan: (theme)

<!--
A sprint here is a batch of work packets serving one theme (e.g. "toolchain and
contract foundation", "first vertical slice"). Duration is packet-driven, not
calendar-driven — the sprint ends when its packets are Complete, and with agents
that may be hours or days, not weeks.
-->

## Theme And Goal

<!-- One paragraph: what is true at sprint end that is not true now. -->

## In This Sprint

| Packet | Title | Requirements | Depends on | Status |
|---|---|---|---|---|
| S<N>-001 | | | — | Proposed |
| S<N>-002 | | | S<N>-001 | Proposed |

Packet files live in `docs/sprints/sprint-<N>/S<N>-###_slug.md`, each from
`docs/templates/WORK_PACKAGE_TEMPLATE.md`, each sized to one agent session.

## Explicitly NOT In This Sprint

<!-- The fence. Name the tempting adjacent work agents must not start. -->

-

## Parallelization Map

<!-- Which packets may run in parallel (disjoint owned files) and which are serialized. -->

| Track | Packets | Owned area |
|---|---|---|
| A | | |
| B | | |

## Sprint Gates

- Entry: previous phase/sprint gate satisfied; all packets pass Definition of Ready.
- Exit: all packets Complete with evidence; state docs current; retro notes added
  to `docs/CURRENT_THINKING.md`; next sprint plan drafted or backlogged.

## Verification Commands

<!-- The exact commands that must be green at sprint end. -->

```bash
python tools/qa/validate_docs.py
python tools/qa/scan_secrets.py
```
