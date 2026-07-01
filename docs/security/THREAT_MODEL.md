# Threat Model

<!--
PHASE 3 DELIVERABLE. Model threats per trust boundary before code exists;
revisit at Phase 8 (hardening) and whenever a new public surface appears.
-->

## Assets

<!-- What is worth attacking/protecting. Start from {{SENSITIVE_DATA_CLASSES}}. -->

| Asset | Sensitivity | Where it lives |
|---|---|---|
| | | |

## Trust Boundaries

<!-- Where data crosses ownership/privilege lines. Each boundary gets a diagram
in docs/diagrams/THREAT_MODEL.md and a Level 2 DFD if sensitive data crosses it. -->

-

## Threats (STRIDE per boundary)

| Boundary | Threat (S/T/R/I/D/E) | Scenario | Control | Verified by |
|---|---|---|---|---|
| | | | | TC-SEC-### |

## Abuse Cases

<!-- How legitimate features get weaponized: spam, farming, harassment, scraping,
resource exhaustion. Each abuse case needs a control and a test or monitor. -->

-

## Residual Risks

<!-- Accepted risks with owner and review date — mirror into docs/BUGS_AND_RISKS.md. -->

-

## Exit Criteria

- Every trust boundary has STRIDE coverage with named controls.
- Every control is verified by a test ID or an explicit monitor.
- Launch-blocking security areas are registered in `docs/qa/TESTING_MASTER_PLAN.md`.
