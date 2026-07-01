# Knowledge Flow

How knowledge moves from ephemeral conversation into durable, layered project memory — and back into the next agent session. Full rules: `docs/KNOWLEDGE_SYSTEM.md` and `docs/CONTEXT_ENGINEERING.md`.

```mermaid
flowchart TB
  subgraph EPHEMERAL ["Ephemeral (dies with the session)"]
    CONV["Conversation:<br/>prompts, answers, debates"]
  end

  subgraph STATE ["Working memory (rewritten every session)"]
    CT["CURRENT_TASK.md"]
    NT["NEXT_TASK.md"]
    TH["CURRENT_THINKING.md"]
    LG["BACKLOG · BUGS_AND_RISKS · TECH_DEBT"]
  end

  subgraph DURABLE ["Durable long-form (append/revise deliberately)"]
    ARC["conversation-archive/<br/>raw + summaries"]
    SRS["REQUIREMENTS · SRS · ADRs ·<br/>QA specs · design artifacts"]
    DIA["diagrams/ (Mermaid)"]
  end

  subgraph MACHINE ["Machine-optimized (generated / compacted)"]
    OKF["knowledge/okf/<br/>one concept per file"]
    GR["knowledge/graph/<br/>code graphs (generated)"]
  end

  CONV -->|"Prime Rule:<br/>before session ends"| CT & NT & TH & LG
  CONV -->|"direction changed"| ARC
  CT & TH -->|"decisions mature"| SRS
  SRS --> DIA
  SRS -->|"compact summaries"| OKF
  SRC["Source code"] -->|"regenerate after<br/>big refactors"| GR

  OKF & CT & NT & TH -->|"fast orientation"| NEXT["Next agent session"]
  SRS & DIA & GR -->|"search on demand"| NEXT
```

**The one-way valve:** knowledge only flows *from* conversation *into* files — never the reverse. If a fact lives only in a chat transcript, the process treats it as lost. The Prime Rule (update state before ending work) is the valve's enforcement mechanism.
