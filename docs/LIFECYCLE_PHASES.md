# Lifecycle Phases — The Playbook

Each phase has **entry criteria, activities, artifacts, and an exit gate**. A phase is not done because time passed; it is done when its gate is satisfied and the state files say so. The master flowchart is `docs/diagrams/MASTER_LIFECYCLE.md`.

Phases 0–6 are deliberately front-loaded: with AI agents, planning artifacts are cheap to produce and enormously valuable, because they become the durable context every future session runs on. The cost balance of software engineering has shifted — exploit it.

---

## Phase 0 — Inception & Discovery

**Entry:** a rough product idea exists.

**Activities**
- **Mob elaboration**: the agent interviews the human(s) in small question batches, challenging weak assumptions (adapted from AWS AI-DLC).
- Rewrite the raw idea as a **purified prompt**: complete, precise, testable, with settled vs. open decisions separated.
- Record product shape, users, core questions, constraints, initial technology direction.

**Artifacts:** `docs/PURIFIED_PROMPT.md`, `docs/DISCOVERY.md`, `docs/software-engineering/00_INCEPTION.md`.

**Exit gate:** the human accepts the purified prompt as "this is what we are building"; major assumptions and open questions are recorded.

---

## Phase 1 — Research & Requirements

**Entry:** purified prompt accepted.

**Activities**
- Research the domain: competitors, prior art, platform constraints, legal/compliance issues, cost drivers. Store findings with sources.
- Derive a full requirement catalogue with stable IDs: `FR-<AREA>-###` (functional) and `NFR-<AREA>-###` (non-functional, measurable).
- Classify requirements by release ring (which slice/ring first needs it).

**Artifacts:** `docs/RESEARCH_BASELINE.md`, `docs/REQUIREMENTS.md`.

**Exit gate:** requirement catalogue reviewed by the human; every requirement has an ID, a priority, and a release ring.

---

## Phase 2 — Specification (SRS)

**Entry:** requirement catalogue exists.

**Activities**
- Write an Agile SRS: scope per release ring, acceptance criteria, explicit out-of-scope list, quality attributes.
- The out-of-scope list is as important as the in-scope list — it is what stops agents from gold-plating.

**Artifacts:** `docs/SRS.md`.

**Exit gate:** SRS accepted by the human. This acceptance is a hard prerequisite for production code.

---

## Phase 3 — Architecture & Decisions

**Entry:** SRS accepted.

**Activities**
- Draft ADRs for every major decision: platform, framework, data store, providers, core algorithms, privacy/security model, deployment, release process, repo structure.
- Each ADR records options, the **strongest argument against** the preferred option, consequences, and reversal conditions.
- Run an explicit **ADR acceptance pass**: accept / revise / defer each one. Deferring is legitimate — record what unblocks it.
- Draw system context and container diagrams; write the threat model for sensitive data classes.

**Artifacts:** `docs/adr/ADR-*.md`, `docs/ARCHITECTURE.md`, `docs/security/THREAT_MODEL.md`, diagrams in `docs/diagrams/`.

**Exit gate:** ADR pack reviewed with disposition recorded for every ADR; no accepted ADR lacks reversal conditions.

---

## Phase 4 — Design Artifacts & Spikes

**Entry:** ADR pack accepted.

**Activities**
- Produce the methodology chain artifacts (see `docs/METHODOLOGY.md`): use cases, domain model, data-flow diagrams, design classes, system sequence diagrams, operation contracts, package/CRC structure.
- Draft external contracts first: API spec (e.g. OpenAPI), data model/ERD, data dictionary, UX flow spec.
- Run **prototype spikes** for the highest-risk mechanisms. Spike code is throwaway by default; promoting it to production requires passing normal gates.

**Artifacts:** `docs/software-engineering/02..08_*.md`, `docs/api/`, `docs/data/`, `docs/ux/`.

**Exit gate:** every P0 requirement traces to a use case, domain concept, design element, and contract; spike results recorded in `docs/CURRENT_THINKING.md`.

---

## Phase 5 — QA & Gate Design

**Entry:** design artifacts exist.

**Activities**
- Write the testing master plan and the requirement-to-test matrix (every requirement gets planned test IDs `TC-<AREA>-###`).
- Define Definition of Ready / Definition of Done.
- Design the phased CI gates (docs CI now; code CI, security CI, benchmark CI, release CI later).
- Identify **launch-blocking test areas** — the invariants that halt feature exposure when violated (e.g. data-leak prevention, integrity of core domain state).
- For AI/ML features: define goldset/benchmark datasets and thresholds before implementation.

**Artifacts:** `docs/qa/*`, `docs/TRACEABILITY_MATRIX.md`, `docs/PRECODE_COMPLETION_AUDIT.md`.

**Exit gate — the pre-code audit ritual.** Do not close this phase with a single checklist glance. Run the ritual the way it works in practice:

```txt
1. Ask the agent: "What useful pre-code work remains before implementation?"
2. It surveys planning, QA, and governance artifacts and recommends work.
3. Human approves; agent executes and archives the session.
4. Repeat from 1 — until a full pass surfaces nothing new that is not code-dependent.
5. Record every pass in docs/PRECODE_COMPLETION_AUDIT.md
   (from docs/templates/PRECODE_AUDIT_TEMPLATE.md), with evidence per claim.
```

Each pass audits a different lens (planning artifacts → test/QA readiness → collaboration/governance), and later passes re-check earlier ones. Work that genuinely requires code goes in the audit's "Must Wait For Code" list — deferred, not forgotten, and not an excuse to keep planning. The gate is satisfied when the final pass is clean, validators run green (pasted into the audit), and the human signs the Final Decision naming the first work packet.

---

## Phase 6 — Scaffold & Toolchain

**Entry:** the pre-code completion audit is signed (Phase 5 exit).

**Activities**
- Scaffold the monorepo skeleton with module boundaries, placeholder folders, and module READMEs (boundaries first, code later).
- Verify local toolchain readiness; wire CI phase 1 (docs validation, secret scan).
- Cut the first sprint plan into **individual task packets** small enough for one agent session each.

**Artifacts:** repo skeleton, `.github/workflows/`, `docs/sprints/SPRINT_0_PLAN.md`, `docs/sprints/sprint-0/S0-###_*.md` packets.

**Exit gate:** validators pass in CI; sprint-0 packets satisfy Definition of Ready. **This gate opens production coding.**

---

## Phase 7 — Construction Loop (repeat per vertical slice)

**Entry:** Phase 6 gate passed.

The unit of work is a **vertical slice**: the thinnest end-to-end path through the system that proves the architecture (one flow, UI to storage and back). Each slice decomposes into work packets executed with the session loop (`docs/diagrams/AGENT_SESSION_LOOP.md`):

```txt
Orient -> Claim packet -> Explore -> Plan -> Implement in bursts
-> Verify with evidence -> Commit -> Update state -> Handoff
```

**Rules**
- One packet per agent session where possible; split packets that don't fit.
- Tests land with (or before) the behavior they protect, per the requirement-to-test matrix.
- New CI gates activate as their prerequisites exist (see `docs/GOVERNANCE_AND_GATES.md`).
- Slice review at each slice end: demo evidence, traceability updated, retro notes into `docs/CURRENT_THINKING.md`.

**Exit gate (per slice):** acceptance criteria met with evidence; state docs updated; no orphaned debt (undocumented).

---

## Phase 8 — Hardening

**Entry:** enough slices exist for a coherent pre-release build.

**Activities:** security test checklist, dependency audit, performance profiling against NFR targets, failure-mode matrix review, benchmark/goldset runs for AI features, chaos/abuse testing for public surfaces.

**Exit gate:** all launch-blocking areas green; P0/P1 bugs closed or explicitly waived with owner and expiry.

---

## Phase 9 — Release Rings

**Entry:** hardening gate passed.

Release progressively: **internal → private alpha → closed beta → production**, with a release-gate checklist per ring (`docs/templates/RELEASE_GATE_EVIDENCE_TEMPLATE.md`). Each ring widens exposure and adds required evidence (crash/error telemetry, rollback rehearsal, store/compliance checks where relevant).

**Exit gate (per ring):** evidence template completed; rollback path tested; next-ring criteria defined.

---

## Phase 10 — Operations & Evolution

**Entry:** first production release.

**Activities:** observability review cadence, incident → bug/risk ledger flow, feedback intake into backlog, periodic knowledge-system maintenance (stale doc sweep, diagram refresh, code-graph regeneration after large refactors), periodic ADR review (are reversal conditions triggered?).

This phase never exits; it loops back into Phase 7 for each new increment and into Phase 3 when an ADR's reversal condition fires.

---

## The Spiral Escape Hatch

At any phase, if a subsystem shows repeated safety, correctness, cost, or legal failures across two consecutive iterations: pause feature delivery for that subsystem and run a spiral cycle — identify risk, prototype, evaluate, decide (ADR), resume. Record entry and exit in `docs/CURRENT_THINKING.md`.
