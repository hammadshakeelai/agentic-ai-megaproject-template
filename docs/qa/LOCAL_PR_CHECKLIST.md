# Local PR / Commit Checklist

Run before every commit burst and before opening a PR. CI enforces the same checks — finding failures locally is always cheaper.

## Every Burst

- [ ] `python tools/qa/validate_docs.py` passes
- [ ] `python tools/qa/scan_secrets.py` passes
- [ ] Module tests for changed code pass (paste evidence into closeout)
- [ ] Commit is one semantic purpose with AI trailers
- [ ] No forbidden files from the packet were touched (`git status` review)

## Every PR / Packet Completion

- [ ] Acceptance criteria checked one by one against evidence
- [ ] Requirement IDs referenced in description
- [ ] Traceability matrix updated if requirements/tests changed
- [ ] State docs updated (CURRENT_TASK, NEXT_TASK, CURRENT_THINKING)
- [ ] New bugs/risks/debt recorded in ledgers
- [ ] File-size guardrails respected or debt-logged
- [ ] Screenshots/recordings attached for UI changes
- [ ] Security/privacy notes from the packet addressed
