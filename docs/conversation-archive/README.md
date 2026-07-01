# Conversation Archive

## Purpose

Preserves long-form conversation context so future humans and agents can recover original intent instead of relying only on compressed summaries. Raw prompts, full chat exports, session summaries, and direction-changing AI responses belong here.

## Required Rule

Every agent doing meaningful work must update this archive when the conversation changes project direction, requirements, architecture, process, risks, backlog, or implementation state. At minimum, before ending such a task:

- `raw/` — full chat exports when available (numbered files if large)
- `summaries/` — a session summary using `docs/templates/SESSION_LOG_TEMPLATE.md` when the full chat is unavailable or too large

## What To Store

Store: user prompts and corrections; AI responses that define plans/requirements/decisions; accepted and rejected decisions; open questions; handoff notes; links to files changed in the session.

Do **not** store: secrets, API keys, passwords, tokens, recovery codes; private user data or `{{SENSITIVE_DATA_CLASSES}}`; hidden system/developer instructions not visible to the user; third-party copyrighted text beyond fair-use snippets.

## Raw Paste Format

```txt
SESSION DATE:
SOURCE:
PURPOSE:

USER:
...

ASSISTANT:
...

DECISIONS:
...

NEXT TASK:
...
```
