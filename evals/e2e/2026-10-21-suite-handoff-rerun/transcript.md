### USER
I'm head of AI at our firm. The audit practice already has a transformation plan in this folder. Set up a firm-wide AI portfolio and bring the audit opportunities into it so we can compare and prioritise them.

### TOOLS
- Skill: ai-transformation:ai-portfolio
- Write: /tmp/claude-0/-home-user-ai-enablement-evals-e2e-2026-10-21-suite-handoff-rerun-workspace/807fbf4d-3850-5c6c-82b1-8d3750715cd5/scratchpad/check.py

### ASSISTANT
I've read the audit plan and both units' opportunity files. I haven't written anything yet.

**What I found**
- **Plan settings:** the plan gives me the value levers and weights (capacity, quality, risk, staff experience, margin), a redeploy stance and the guardrails. I'll inherit these as a starting point for the firm portfolio, and you can change them.
- **Integrated-audit file:** it parses, but it's an unvalidated desk review. Those items will come in as outlines marked "draft to validate".
- **SOX-only file:** `units/sox-only-outsourcing/opportunities.yaml` doesn't parse. An unquoted colon in an item title on line 106 breaks it: "Named junior-development workstream: juniors keep…". The portfolio skill doesn't fix advisor files, so I won't touch it. The transformation-advisor skill can fix that title. I'll import from it only once you've agreed how to handle it. My options are to wait for the fix, or to import the other items now and add that one after the fix.

Reminder: please keep client-confidential and personal data out of anything we write here.

**First step: setting up the portfolio.** Next we log the audit ideas, then score them side by side.

**Question 1:** Which practices and functions should the firm-wide portfolio cover (for example audit, tax, advisory and the internal functions), and should it hold ideas only, or pilots and live AI systems too?