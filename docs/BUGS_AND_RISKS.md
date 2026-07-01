# Bugs And Risks

<!--
Two ledgers in one file. Nothing gets deleted — closed items move to the bottom
with resolution notes, because "we already tried that" is valuable memory.
-->

## Open Bugs

| ID | Severity | Area | Description | Found by | Status |
|---|---|---|---|---|---|
| | | | | | |

Severity: P0 blocks everything · P1 blocks release · P2 fix soon · P3 recorded.

## Open Risks

| ID | Likelihood | Impact | Description | Mitigation | Trigger to act |
|---|---|---|---|---|---|
| RISK-001 | medium | high | State files go stale if sessions skip the Prime Rule | Validator checks freshness; handoff review | A session finds stale state files |

## Closed / Resolved

| ID | Resolution | Date | Notes |
|---|---|---|---|
| | | | |
