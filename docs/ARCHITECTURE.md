# Architecture

<!--
PHASE 3 DELIVERABLE. The narrative view that ties the accepted ADRs together.
Decisions live in docs/adr/ — this file explains how they compose. Keep it a map,
not a novel; link to ADRs and diagrams rather than restating them.
-->

## System Context

<!-- Who/what talks to the system. Diagram: docs/diagrams/SYSTEM_CONTEXT.md (create in Phase 3). -->

## Containers And Modules

<!-- The major deployable/buildable units and their protected boundaries.
Diagram: docs/diagrams/C4_CONTAINERS.md. Every external provider sits behind an adapter
(see docs/software-engineering/05_DESIGN_CLASS_DIAGRAM.md boundaries table). -->

| Unit | Responsibility | Protected boundary | Key ADRs |
|---|---|---|---|
| | | | |

## Data Architecture

<!-- Canonical stores, data classes (mark sensitive ones), migration approach. -->

## Cross-Cutting Concerns

<!-- Auth, observability, error handling, idempotency, configuration — one paragraph
each with the owning ADR. -->

## Architecture Invariants

<!-- The rules agents must never violate, e.g. "all writes to X are server-side",
"module A never imports module B". These feed architecture-fitness checks. -->

-

## Exit Criteria

- Every accepted ADR is reflected here or explicitly out of scope.
- Every invariant is testable (or has a fitness-check plan).
