# Research Foundations

Where this template's ideas come from, and what each source contributed. Keep this file honest: when you change the methodology, record what you changed, why, and what evidence prompted it.

## Origin

The template was distilled from a real large-scale agentic project that reached implementation readiness with: persistent state files, a 20-phase gated roadmap, a 196-requirement catalogue with full traceability, an adversarially-reviewed ADR pack, phased CI gates, work packets with owned/forbidden files, and AI-attributed short-burst commits. The generalization removed the product domain and kept the process skeleton.

## Community Methodologies

| Source | What it is | What this template adopted |
|---|---|---|
| [GitHub Spec Kit](https://github.com/github/spec-kit) ([docs](https://github.github.com/spec-kit/), [GitHub blog](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)) | Spec-Driven Development toolkit: Specify → Plan → Tasks → Implement, agent-agnostic | Hard separation of spec/plan/tasks from implementation; human checkpoints between phases; the "constitution" idea folded into `AGENTS.md` as the agent contract |
| [BMAD Method](https://docs.bmad-method.org/) ([overview](https://bmadcodes.com/bmad-method/)) | Agentic-agile framework with role agents (Analyst, PM, Architect, Dev, QA) and story-file sharding | The role table in `MULTI_AGENT_ORCHESTRATION.md`; sharding plans into session-sized packets with embedded context |
| [AWS AI-DLC](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/) ([workflows](https://aws.amazon.com/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/)) | AI-native lifecycle: Inception/Construction/Operations, mob elaboration, units of work | The Phase 0 interview ritual (mob elaboration); AI proposes / human disposes posture; units-of-work sizing |
| [Cline Memory Bank](https://docs.cline.bot/features/memory-bank) ([pattern](https://cline.bot/blog/memory-bank-how-to-make-cline-an-ai-agent-that-never-forgets)) | Structured markdown memory hierarchy read at every session start | The L1–L4 memory hierarchy in `CONTEXT_ENGINEERING.md`; activeContext ≈ `CURRENT_THINKING.md` |
| [Anthropic — Claude Code best practices](https://code.claude.com/docs/en/best-practices) ([context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)) | Explore→Plan→Code→Commit; plan mode; subagents for wide reads; writer/reviewer; evidence over assertion | The session loop; the Evidence Rule; subagent delegation guidance; keeping the always-loaded contract small |
| [12-Factor Agents](https://paddo.dev/blog/12-factor-agents/) ([overview](https://www.ikangai.com/12-factor-agents-a-blueprint-for-reliable-llm-applications/)) | Production principles: own your context window, small composable agents, pause points | Context budget discipline; small-agents-one-job; human pause points for irreversible actions |

## Research Papers

| Paper | Contribution used here |
|---|---|
| [ChatDev: Communicative Agents for Software Development](https://arxiv.org/pdf/2307.07924) | Phase-structured agent communication; multi-role cooperation outperforming single-agent orchestration |
| MetaGPT (SOP-encoded multi-agent framework; see the [multi-vocal literature review](https://arxiv.org/html/2604.16321v1)) | Encoding standard operating procedures into roles — the insight that process structure, not model cleverness, drives output quality |
| [Agentic Software Engineering: Foundational Pillars and a Research Roadmap (SE 3.0)](https://arxiv.org/abs/2509.06216) | The command/execution environment split (humans orchestrate, agents execute, structured handoff between them); verification and trust as first-class concerns |
| [LLM-Based Multi-Agent Systems for Code Generation: A Multi-Vocal Literature Review](https://arxiv.org/html/2604.16321v1) | Survey evidence on which multi-agent topologies actually help (reviewer/tester roles) vs. add overhead |
| [CodePori](https://arxiv.org/pdf/2402.01411) | Large-scale autonomous multi-agent development: the necessity of bounded task decomposition at scale |

## Design Positions Taken (and why)

1. **Docs-first over code-first.** With agents, planning artifacts are cheap and compounding; unplanned code is cheap and corrosive. The gate before production code is the template's spine.
2. **Repo as memory over tool-specific memory.** Vendor memory features change; Markdown in git survives model rotations and tool switches.
3. **Traceability over velocity theater.** The chain looks bureaucratic until the tenth agent asks "why does this exist and what breaks if I change it" — then it is the fastest thing in the repo.
4. **Adversarial ADRs over consensus ADRs.** Agents agree too easily. Forcing the strongest counter-argument produces decisions that survive contact with reality.
5. **Short bursts over big merges.** Reviewability, revertability, and crash recovery all fall out of one habit.
6. **Evidence over assertion.** LLMs report success optimistically; requiring pasted output changes agent behavior more than any exhortation to "be careful".
7. **Repeated self-audit before the coding gate.** *(Added 2026-07-02, from the origin project's session archive.)* The origin project did not close pre-code planning with one checklist — the human repeatedly asked "what else can be done before coding?" across multiple sessions, and each pass surfaced a genuinely different lens (test architecture, then concrete tests/CI, then governance/templates/ownership) until a final multi-pass audit came back clean. One audit pass finds what it is looking for; repeated passes with fresh framing find what the previous pass assumed. Codified as the audit ritual in `LIFECYCLE_PHASES.md` Phase 5 and `docs/templates/PRECODE_AUDIT_TEMPLATE.md`, with the counter-pressure recorded too: code-dependent work is deferred explicitly, so the ritual cannot become planning forever.

## Maintaining This File

When you adopt, modify, or drop a practice: add a row or position here with the date, the trigger, and the evidence. The methodology itself follows the ADR spirit — decisions with reversal conditions, not dogma.
