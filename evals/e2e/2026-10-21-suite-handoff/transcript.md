### USER
I'm head of AI at our firm. The audit practice already has a transformation plan in this folder. Set up a firm-wide AI portfolio and bring the audit opportunities into it so we can compare and prioritise them.

### ASSISTANT
I've read the SOX/ICFR practice plan and the two units' opportunity files. Before I write anything, I need one decision from you.

**What I found**
- There is no `opportunities.yaml` at the top level. The opportunities are in two unit files:
  - `units/sox-only-outsourcing`: 10 items, validated through the plan.
  - `units/integrated-audit`: 5 items, all labelled `draft-to-validate` (desk review only).
- No `portfolio/` or `overlay/` folder exists yet, so there are no firm-wide policy, risk tiers or tool catalog to draw on.
- The plan's levers and weights belong to this one practice, not the firm:
  - **Levers:** capacity, quality, risk, staff experience and margin.
  - **Weights:** value 0.30, feasibility 0.20, data readiness 0.15, risk 0.20, time to value 0.05, strategic fit 0.10.
  - **Capacity stance:** redeploy.

**How I'd import the audit items**
- Each item keeps a back-link to its source file, and I won't edit the advisor's files.
- The 5 integrated-audit items stay as outlines until someone who does the work validates them.
- Several items overlap, so I'd flag them as duplicate-check pairs rather than add their value together:
  - The two pre-review checklists (`sox-prereview-checklist` and `ct-int-precheck-checklist`).
  - The two report registers (`sox-report-register` and `ct-int-validated-report-register`).
  - The two listing-comparison tools (`sox-listing-tool` and `ct-int-listing-compare-draft`).
- The SOX items' value ranges already warn that the checklist, request-template and report-register quality gains overlap, so they can't be summed.

**Question:** Should the firm-wide portfolio use this audit plan's levers, weights and redeploy stance as they stand, or do you want firm-level ones that other practices, such as tax and advisory, can also score against?

Please don't share any client-confidential or personal data in this session.

### USER
Firm-level, please. The audit plan's levers and weights are fine as a starting point for audit, but tax and advisory need to score against the same scale. Use a common set of levers (capacity, quality, risk, margin, staff experience), keep the weights close to the audit ones, and make the capacity stance a firm-level choice rather than assuming redeploy. Go ahead and import the audit items with back-links and the duplicate-check pairs as you described.

### ASSISTANT
I couldn't run the build script. The environment asks for approval before it will run, and I haven't been given that approval. So I'm stopping here, and nothing has been written to `portfolio/` yet.

The script is saved at `/tmp/claude-0/-home-user-ai-enablement-evals-e2e-2026-10-21-suite-handoff-workspace/807fbf4d-3850-5c6c-82b1-8d3750715cd5/scratchpad/build.py`. When you run it, it:
- creates `portfolio/portfolio.yaml`;
- creates 12 intake records in `portfolio/intake/`;
- imports 12 of the 15 audit items, each with its back-link to the source file;
- prints any arithmetic errors it finds in the advisor's weighted scores.

**What the script will set up, as you directed**
- **Levers:** capacity, quality, risk, staff experience and margin. Margin uses the shared id `cost`.
  - **Metrics:** I rewrote them so tax and advisory can use them, with each item stating its own unit.
- **Weights:** I kept the audit plan's weights exactly rather than moving them slightly. You can adjust them.
- **Capacity stance:** `undecided` at firm level. Each imported item's capacity choice is also `undecided`, even though the audit plan said redeploy.
- **Duplicate-check pairs:** the checklists, the report registers and the listing-comparison tools.
  - **Value:** their value is not added together.
- **Related items:** the client-data approval, the listing tools and the two non-client assistant items.

**Choices I made that you should check**
- **Items left out:** I did not import `sox-ai-secondary-review`, `sox-agent-testing` or `sox-platform-plus-review`. They are target pictures with no value or scores in the advisor file.
- **Draft items:** the 5 integrated-audit items stay as outlines marked "Draft to validate".
- **Owner not named:** `sox-chase-assistant` and `sox-junior-development` also stay as outlines.
- **Item classes:** the portfolio's classing of items is mine and needs your confirmation at screen.
  - **Process fixes:** the checklists, request template, registers and approval are process fixes that need no AI. Whether they belong in an AI register is a screening question.
- **Value units:** units differ across items (percentage points, hours a month, hours per test, days), so ranges aren't comparable until step 3 puts them on a common basis.
- **Open set-up items:** gatekeepers, forum, live limit, rhythm and gate paths are my proposals, not agreed. The file stays `setting-up` until you confirm them. There is also no inventory of AI already in use.

Please either approve running the script, or tell me to write the files directly instead.