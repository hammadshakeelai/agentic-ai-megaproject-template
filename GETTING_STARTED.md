# Getting Started

How to turn this template into a live project. Total time: one focused session for bootstrap, then Phase 0 begins.

## 1. Copy And Rename

1. Copy the template directory to a new location and rename it to your project name.
2. Run `git init` inside it.
3. Configure the commit template: `git config commit.template .gitmessage.txt`.

## 2. Replace Placeholders

Search the whole tree for `{{` and replace:

| Placeholder | Meaning | Example |
|---|---|---|
| `{{PROJECT_NAME}}` | Product/project name | `Atlas` |
| `{{PROJECT_ONE_LINER}}` | One sentence describing the product | `A privacy-first team wiki` |
| `{{DOMAIN}}` | Problem domain | `knowledge management` |
| `{{PRIMARY_PLATFORM}}` | First delivery target | `web app`, `Android APK`, `CLI` |
| `{{TECH_DIRECTION}}` | Initial (not final) technology direction | `Next.js + Postgres` |
| `{{SENSITIVE_DATA_CLASSES}}` | What must never leak or be committed | `user documents, access logs` |
| `{{TEAM_OR_OWNER}}` | Human owner(s) | `@yourhandle` |

Placeholders you cannot fill yet are fine — Phase 0 exists to fill them. Leave them as `{{...}}` so validators can flag them later.

## 3. The Bootstrap Ritual (Phase 0 Kickoff)

Give your AI agent this exact prompt (adapt bracketed parts):

```txt
Read AGENTS.md, docs/PROCESS.md, and docs/LIFECYCLE_PHASES.md in this repository.

We are starting Phase 0 (Inception & Discovery) for [rough product idea in 2-5 sentences].

Your tasks, in order:
1. Interview me: ask the clarifying questions Phase 0 requires (mob elaboration).
   Ask in batches of at most 5. Challenge my assumptions where they look weak.
2. From my answers, write docs/PURIFIED_PROMPT.md: a clean, complete, testable
   statement of what we are building, with all decisions I have already made and
   all decisions still open clearly separated.
3. Write docs/DISCOVERY.md: product shape, users, core questions, constraints,
   initial technology direction, and Phase 0 exit criteria status.
4. Fill docs/software-engineering/00_INCEPTION.md.
5. Update docs/CURRENT_TASK.md, docs/NEXT_TASK.md, docs/CURRENT_THINKING.md.
6. Commit in short semantic bursts per docs/COMMIT_POLICY.md.

Do not write any production code. Do not skip the interview.
```

The two artifacts that matter most from Phase 0:

- **`docs/PURIFIED_PROMPT.md`** — the original messy idea rewritten as a precise product statement. Every future agent reads this instead of the original conversation. Keep it under two pages.
- **`docs/DISCOVERY.md`** — what is known, unknown, constrained, and risky.

## 4. Configure The Guardrails

1. Edit `.github/CODEOWNERS` with real owners (even if it is just you).
2. Run the validators once to confirm they pass on the clean template:

   ```bash
   python tools/qa/validate_docs.py
   python tools/qa/scan_secrets.py
   ```

3. Push to your host, let the docs-validation workflow run once, then make it a **required status check** on `main` so Gate 1 cannot be bypassed. On a public GitHub repo (branch protection is free) this is one call — the context name is the workflow's job id (`docs-validation`) and `15368` is GitHub's global Actions app id:

   ```bash
   # confirm the exact check name from a completed run first
   gh api repos/OWNER/REPO/commits/main/check-runs --jq '.check_runs[].name'

   gh api --method PUT repos/OWNER/REPO/branches/main/protection --input - <<'JSON'
   {
     "required_status_checks": { "strict": false, "checks": [ { "context": "docs-validation", "app_id": 15368 } ] },
     "enforce_admins": false,
     "required_pull_request_reviews": null,
     "restrictions": null
   }
   JSON
   ```

   `enforce_admins: false` keeps an owner escape hatch for direct pushes; set it to `true` once you move to a strict PR-only flow. `strict: false` avoids forcing every branch to be rebased before merge — flip to `true` if you want that.

## 5. Proceed Through Phases

Follow `docs/LIFECYCLE_PHASES.md`. The short version:

```txt
Phase 0  Inception & Discovery        -> purified prompt accepted
Phase 1  Research & Requirements      -> requirement catalogue with IDs
Phase 2  Specification (SRS)          -> SRS accepted
Phase 3  Architecture & ADRs          -> ADR pack accepted (adversarially challenged)
Phase 4  Design Artifacts             -> use cases, domain model, contracts, UX flows
Phase 5  QA & Gate Design             -> test strategy, traceability matrix, ready/done
Phase 6  Scaffold & Toolchain         -> repo skeleton, CI phase 1, sprint-0 packets
Phase 7+ Construction Loop            -> vertical slices, one work packet at a time
...      Hardening -> Release Rings -> Operations
```

**The single most important rule:** no production feature code before Phase 6's gate. Everything before that is thinking made durable — and it is what makes the construction loop fast, parallel, and safe later.

## 6. Daily Rhythm Once Construction Starts

Every agent session follows the loop in `docs/diagrams/AGENT_SESSION_LOOP.md`:

```txt
Orient (read state files) -> Claim packet -> Explore -> Plan -> Implement in bursts
-> Verify with evidence -> Commit -> Update state files -> Write handoff
```

If a session ends mid-task for any reason, the state files are the recovery path. That is the whole point.

## 7. Scaling Up

When one agent is not enough, read `docs/MULTI_AGENT_ORCHESTRATION.md` before spawning more. The non-negotiable rule: **two agents never edit the same files in the same time window.** Partition by owned folders, coordinate through state files and packets.
