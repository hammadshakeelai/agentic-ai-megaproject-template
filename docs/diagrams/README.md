# Mermaid Diagram Pack

Canonical process diagrams. One concept per file; diagrams are source code (rendered images are build artifacts). If a diagram change alters a decision or requirement, update ADRs, the traceability matrix, and state docs in the same burst.

## Process Diagrams (template-provided)

- `MASTER_LIFECYCLE.md` — the full phase-gated lifecycle with gates and loops.
- `AGENT_SESSION_LOOP.md` — the per-session inner loop every agent runs.
- `HANDOFF_SEQUENCE.md` — agent-to-agent handoff through repo state.
- `TRACEABILITY_CHAIN.md` — the requirement-to-test artifact chain.
- `WORK_PACKAGE_LIFECYCLE.md` — packet states from Proposed to Complete.
- `DECISION_WORKFLOW.md` — ADR lifecycle including adversarial challenge and reversal.
- `CI_GATE_PIPELINE.md` — the five-gate CI ladder and merge policy.
- `KNOWLEDGE_FLOW.md` — how knowledge moves from conversation to durable memory.
- `ORCHESTRATION_TOPOLOGIES.md` — single agent → pair → parallel → swarm.

## Product Diagrams (create during Phases 3–4)

Add as the project takes shape: `SYSTEM_CONTEXT.md`, `C4_CONTAINERS.md`, `DOMAIN_MODEL.md`, `DATA_FLOW.md`, `DATABASE_ERD.md`, `API_SEQUENCES.md`, `THREAT_MODEL.md`, `UX_FLOWS.md`, `PACKAGE_DEPENDENCIES.md`, `DEPLOYMENT_VIEW.md`, `RELEASE_PROCESS.md`.

## Rules

- Keep diagrams source-controlled as Mermaid in Markdown.
- One concept per file; prefer several small diagrams over one dense one.
- Add figure captions when diagrams are copied into reports.
- The docs validator checks that files here contain Mermaid blocks.
