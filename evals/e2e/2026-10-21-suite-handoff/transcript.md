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

### USER
Write the files directly instead, please. I'd rather not approve a script I haven't read. Your choices on the left-out items and the draft outlines are fine, so go ahead on that basis. Leave the firm-level capacity stance as undecided for now.

### ASSISTANT
I've written `portfolio/portfolio.yaml` and 12 intake records in `portfolio/intake/`, one per imported audit item. I couldn't run a parser on the YAML, so the file is checked by eye only.

**What's in the portfolio**
- **Settings:** the five common levers (capacity, quality, risk, staff experience and margin), with weights equal to the audit plan's. The capacity stance is `undecided` at firm level, and each item's capacity use is also `undecided`.
- **Imported items:** 12 of the 15 audit items, each with a back-link to its source file. I changed nothing in the advisor's files.
- **Status:** 5 items are ready to screen. The 5 integrated-audit items are outlines marked "Draft to validate", and `sox-chase-assistant` and `sox-junior-development` are outlines because they have no owner.
- **Left out:** `sox-ai-secondary-review`, `sox-agent-testing` and `sox-platform-plus-review`.

**First comparison**

Scores and ranges are the advisor's. The indexes are my arithmetic under the shared weights. The advisor's weighted scores all re-checked correctly.

| Item | Category | Weighted | Value | Readiness |
|---|---|---|---|---|
| `sox-prereview-checklist` | foundation | 4.40 | 4.33 | 4.45 |
| `ct-int-precheck-checklist` | quick-win | 4.15 | 3.44 | 4.73 |
| `sox-request-template` | park | 4.00 | 3.44 | 4.45 |
| `ct-int-validated-report-register` | quick-win | 3.90 | 4.11 | 3.73 |
| `sox-report-register` | big-bet | 3.70 | 4.11 | 3.36 |
| `ct-int-nonclient-drafting` | quick-win | 3.70 | 2.44 | 4.73 |
| `sox-junior-development` | foundation | 3.35 | 2.56 | 4.00 |
| `sox-chase-assistant` | park | 3.15 | 2.44 | 3.73 |
| `sox-client-data-approval` | foundation | 3.00 | 2.56 | 3.36 |
| `ct-int-listing-compare-draft` | foundation | 2.95 | 3.67 | 2.36 |
| `ct-int-ai-secondary-review` | park | 2.35 | 2.78 | 2.00 |
| `sox-listing-tool` | park | 2.25 | 2.11 | 2.36 |

**Things to know before you rely on that table**
- **Duplicates:** the three pairs are flagged in the file and in the intake records, and their value must not be added. The checklist, request template and register also share one pool of evidence-completeness notes, which the advisor puts at about 20 points of the 30% note rate.
- **One approval for both tools:** `sox-client-data-approval` and `ct-int-listing-compare-draft` would each open the same client-data approval request. Only one should.
- **Value units:** the units differ across items (percentage points, hours a month, hours per test, days), so the ranges can't be compared until step 3 puts them on a common basis.
- **Process fixes:** several items need no AI (the checklists, request template and registers). You may want to decide whether the portfolio holds process fixes alongside AI items.
- **Speed lever:** `ct-int-ai-secondary-review` uses a `speed` lever that isn't among the firm's five. Map it to capacity or drop it at screen.
- **Not yet agreed (step 1):**
  - Gatekeepers, review forum, rhythm, gate paths and live limit are my proposals. They're marked as proposed in the file.
  - No AI inventory exists, and tax and advisory aren't in yet.
- **Status:** the file stays `setting-up` until those are confirmed.

**Next question:** Who releases people and budget for an audit pilot, and would they sit at the gate: the practice leaders, the risk and quality partner, or someone else?

### USER
The practice leaders release people and budget for pilots, so they should sit at the gate. I'd also add the risk and quality partner, because independence and client-data approval are gate conditions and not just a sign-off. Please add both as proposed gatekeepers. Then let's move on and take the strongest audit opportunity toward a prototype.

### ASSISTANT
I've added the practice leaders and the risk and quality partner as proposed gatekeepers, at the discover, prototype and pilot gates. The risk and quality partner is on discover too, because the independence check is part of that gate's exit evidence. The finance lead is on the production gate. I still count those as proposals until the forum agrees them.

**The strongest audit opportunity is `sox-prereview-checklist`.**
- **Scores:** it has the highest weighted score (4.40), a value index of 4.33 and a readiness index of 4.45. It sits in the "value and readiness both at least 3.5" quadrant, whose usual `g0` outcome is Go into discover.
- **Weakest evidence:** its range rests on a Grade D estimate, and data readiness is a 3 because the seniors' criteria are still unwritten.
- **Paired item:** `ct-int-precheck-checklist` is the same checklist in the integrated-audit line. It's still a draft, so I'd screen the two together and not score them as separate wins.

**It can't go straight to a prototype.** Every item needs a recorded `g0` screen decision and then a `g1` discover gate first. Those decisions are for you and the gatekeepers to take. On the light path, which is still only my proposal, `g0` is yours alone.

**This item needs no AI.** Its "prototype" is the advisor's own next step: two seniors co-write the checklist in protected half-days, then the ITGC senior manager back-tests it blind on past files. The build-or-buy handoff to the **ai-solution-delivery** skill would only open at a Go at `g1`.

Two things would have to be true before I draft a `g0` Go for you to take or change:
- A sponsor releases the protected senior half-days.
- The metric the team improves is the one the benefit owner watches.

**Question:** Who in the business owns the review-note rate, so they can be named as the benefit owner and agree it as the success metric?

### USER
The audit practice's SOX/ICFR leader owns the review-note rate. They already track it by engagement, so I'm happy to name them as benefit owner and agree it as the success metric. We'd also count the integrated-audit line's note rate, since the paired checklist sits there. Draft the `g0` Go for me to take, with those two conditions written in.

### ASSISTANT
I've drafted the `g0` Go for `sox-prereview-checklist`. It's in the "Screen result" section of `portfolio/intake/sox-prereview-checklist.md`, marked as a draft.

I haven't recorded it as a decision, so `decisions` in `portfolio.yaml` is still empty. The only change I made there is naming the SOX/ICFR practice leader as benefit owner, which you told me.

**Draft decision: Go into discover**
- **Condition 1:** the review-note rate by engagement is the success metric, with the SOX/ICFR practice leader as benefit owner. The baseline comes from the tracking-sheet record, not the reported 30%.
- **Condition 2:** the integrated-audit line's note rate is counted as a second measure, with its own baseline from record.
  - **Baseline:** none exists today, because the one reported case had zero notes.
  - **Paired item:** `ct-int-precheck-checklist` stays a draft to validate until its manager confirms it.
  - **Value:** it is not added to this item's value.
- **Resources:** two seniors give two or three protected half-days in the shoulder weeks, and none in peak. The ITGC senior manager runs the blind back-test, and the methodology owner approves the checklist. There is no budget beyond staff time.
- **Data:** past SOX-only workpapers and the tracking sheet, plus three past integrated-audit files.
- **Proposed kill criteria:**
  - A blind back-test shows the checklist would have caught under 25% of the evidence-completeness notes. That is the low end of the advisor's own assumption.
  - The half-days can't be released, or the seniors can't state the checks in writing.
- **Next gate:** `g1`, with the practice leaders and the risk and quality partner as proposed gatekeepers.

**Please check these assumptions of mine**
- **Sponsor:** I named the SOX/ICFR practice leader as sponsor, on the plan's wording that the practice lead holds the protected half-days.
- **Gate path:** I drafted the full path, because the light path isn't agreed. That also puts the risk and quality partner at `g1`.
- **Risk tier:** `tier-1` is provisional. No policy file exists yet to set it, so ai-governance should confirm it.
- **Independence:** the checklist doesn't touch client data, but I've asked the risk and quality partner to confirm at `g1` whether the independence check applies.
- **Worth-a-year check:** that check is written for large items. This one costs a few half-days plus a back-test.

If you take it as drafted, I'll append the `g0` entry, set the stage to discover and fill the sponsor, tier, path and next gate. Say so, or tell me what to change.