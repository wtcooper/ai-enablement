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

### USER
Take it as drafted. Go ahead and append the `g0` entry, set the stage to discover and fill in the sponsor, tier, path and next gate. Keep the tier-1 as provisional and flag the sponsor and gate path as assumptions until the forum agrees them.

### ASSISTANT
I've recorded the `g0` Go for `sox-prereview-checklist` in `portfolio/portfolio.yaml`, and the item is now at stage `discover`, status `active`. I couldn't run a parser on the YAML, so the edits are checked by eye only. I also updated the "Screen result" in its intake record to show the decision was taken, by the Head of AI on 2026-10-21.

**What the entry now holds**
- **Decision:** `g0`, Go, decided outside a review, with the reasons and evidence from the draft.
- **Resources:** two seniors, the ITGC senior manager and the methodology owner, released by the sponsor, with no spend beyond staff time.
- **Conditions:**
  1. The review-note rate by engagement is the success metric, with the SOX/ICFR practice leader as benefit owner. The baseline comes from the tracking-sheet record, not the reported 30%.
  2. The integrated-audit line's note rate is a second measure, with `ct-int-precheck-checklist` staying a draft to validate and its value not added.
  3. The sponsor and the full gate path are assumptions until the forum agrees them.
  4. Tier-1 is provisional until ai-governance confirms it.
- **Kill criteria:** a blind back-test would have caught under 25% of the evidence-completeness notes, or the half-days can't be released or the seniors can't state the checks in writing.
- **Next gate:** `g1`, with the practice leaders and the risk and quality partner as proposed gatekeepers. The evidence list includes baselines from records for both lines and the blind back-test.

The sponsor, risk tier and gate path are filled in, each with a YAML comment flagging it as an assumption or provisional. Nothing outside this item changed.

**Still open from set-up**
- **Forum:** it isn't agreed, so the gatekeepers, sponsor and full path stay proposals.
- **Live limit:** the number is not set.
- **Other practices:** tax and advisory aren't in yet.
- **AI inventory:** no inventory of AI already in use.
- **Policy:** no `overlay/policy.md` exists.
- **Portfolio file:** it stays `setting-up`.

**Next step** is discover, led by the sponsor: two or three protected senior half-days to co-write the checklist, then the blind back-test on past files. Pull the baselines from the tracking-sheet record first, for both the SOX-only and integrated-audit lines. Tell me when you want to hold the `g1` gate, and I'll prepare the evidence pack for the gatekeepers.

I haven't screened the other 11 items. Do you want me to draft `g0` options for the next strongest, or bring the whole set to a first portfolio review?

### USER
Let's bring the whole set to a first portfolio review, not draft more `g0` options one by one. Please prepare the review pack. Show the remaining 11 items alongside `sox-prereview-checklist` and flag which ones need a screen decision from me.

### ASSISTANT
I've written the review 1 pack to `portfolio/reviews/1-review.md`. Part A is complete. Part B is blank until you report the decisions. I haven't recorded any decision, and `state.last_review` stays at 0 until you do.

Nothing in the register meets a rule for a stop, redirect or scale decision. No item has a kill criterion that could be met, an early warning, a due gate or a benefit under review. So this review is a first screen of the register.

**Where the 12 items stand**
- 11 are at intake and 1 is in discover (`sox-prereview-checklist`, decided).
- Nothing is live.
- The live limit is still unset.

**What needs a `g0` decision from you (4 items)**

| Item | Value / readiness | Draft recommendation (mine, for you to change) |
|---|---|---|
| `sox-report-register` | 4.11 / 3.36 | Go into discover, limited to stage 1. Named validator and sign-off role as conditions |
| `sox-client-data-approval` | 2.56 / 3.36 | Go into discover, scoped to one narrow request |
| `sox-request-template` | 3.44 / 4.45 | Hold until the per-client report inventory exists |
| `sox-listing-tool` | 2.11 / 2.36 | Hold, and merge with its integrated-audit twin once that is confirmed |

Each has its options, evidence for and against, and proposed kill criteria in section 3 of the pack.

**What you need to settle before the other 7 can be screened**
- **Owners:** `sox-junior-development` and `sox-chase-assistant` have no owner. Name one for each, or leave them as outlines.
- **Draft to validate:** the five integrated-audit items stay outlines until the integrated-audit manager confirms them.
  - **Register:** the manager's confirmation is the advisor's next step for `ct-int-validated-report-register`, which should be screened with `sox-report-register`.

**Findings in the pack**
- **Approval request:** the advisor's file contradicts itself on `sox-client-data-approval`. It lists the checklist as a dependency, but its next step says to open the request now.
  - **Duplicate request:** `ct-int-listing-compare-draft` also says it opens the approval request. There should be one request.
- **Duplicates:** the register is 12 items but about 9 distinct ideas, because of the three pairs.
- **Levers:** margin (weight 0.10) has no item, and one item uses a `speed` lever that isn't one of the firm's five.
- **No-AI items:** about 5 items need no AI. Decide whether process fixes belong in the AI register.
- **Scope:** the register is audit only. Compare tax and advisory ideas before treating this ranking as firm-wide.
- **Costs:** no tool has a run-cost range. Only staff time is recorded.

I didn't use the prepare-review-item subagent brief. It applies to items that meet a surfacing rule, and none do.

**Question:** Which of these four `g0` decisions would you least like to take, and why?

### USER
I'd least like to take `sox-listing-tool`, because holding it only makes sense once the integrated-audit twin is confirmed, and that confirmation isn't mine to give. I'll take the other three as drafted: Go on `sox-report-register` limited to stage 1, Go on `sox-client-data-approval` scoped to one narrow request, and Hold on `sox-request-template`. For `sox-client-data-approval`, make sure there's only one approval request, not the duplicate from `ct-int-listing-compare-draft`.

### ASSISTANT
I've recorded three of the four `g0` decisions from review 1 in `portfolio/portfolio.yaml` and in Part B of `portfolio/reviews/1-review.md`. I left `sox-listing-tool` open, as you asked. I couldn't run a parser on the YAML, so the edits are checked by eye only.

**Recorded, each decided by the Head of AI, in review 1**
- **`sox-report-register`:** Go into discover, limited to stage 1.
  - **Moved to discover:** the item is now at stage `discover`.
  - **Stage 1 scope:** inventory the key reports for 4-5 clients, agree the record content with the risk and quality partner, then validate and time the first client.
  - **Resources:** the ITGC-side senior manager at about 4 hours a week outside peak, with the practice lead's approval. There is no tool spend.
  - **Conditions:**
    - A named validator and register owner, and risk and quality confirming that role can sign a validation record.
    - AS 1215 record content agreed, and a shared place for the register.
    - The remaining clients need a new decision at `g1`.
  - **Kill criteria:** first-client validation takes more than 32 hours, or risk and quality won't accept the signing role.
  - **Next gate:** `g1`.
- **`sox-client-data-approval`:** Go into discover, scoped to one narrow request.
  - **Single request:** there is one approval request, owned by this item. `ct-int-listing-compare-draft` and `sox-listing-tool` attach to it and don't open their own.
  - **Where it's written:** the condition is in the decision entry, in a comment on `ct-int-listing-compare-draft`, and in that item's intake record. I couldn't edit the advisor's file, which still tells that item to start the request.
  - **Check needed:** whether a request without the checklist's written attributes is acceptable. The advisor's file is inconsistent on that.
  - **Next gate:** `g1`.
- **`sox-request-template`:** Hold at intake, to revisit when the per-client key-report inventory exists.

**Left open: `sox-listing-tool`.** No decision is recorded, and the item stays at intake. You hesitated because the Hold depends on the twin. The Hold I drafted rests on the advisor's own trigger and doesn't need the twin; only the proposed merge does. So you could take the Hold on its own, or wait for the integrated-audit manager to confirm `ct-int-listing-compare-draft`. It's in the open questions either way.

**What I filled in without being told**
- **Sponsors:** the SOX/ICFR practice leader for the register and the template, and the managing partner for assurance for the approval, as the plan names them.
- **Risk tiers:** tier-2 for the register, because validation records feed audit evidence, and tier-1 for the approval and the template. The tiers are provisional.
- **Gate path:** the full path for all three.
- **Status:** all of these are flagged as assumptions until the forum agrees them and ai-governance confirms the tiers.

I set `state.last_review` to 1, `step_completed` to 5 and `next_step` to 3. The portfolio file is still `setting-up`, because the forum, live limit and gate paths aren't agreed.

Two things remain on your list. The live limit is still unset. The first two `g1` gates now depend on the SOX/ICFR practice leader and the practice lead naming the validator and preparing the request.

**Question:** Should the Hold on `sox-listing-tool` wait for the integrated-audit manager's confirmation, or do you want me to draft the Hold for you to take on its own?

### USER
Draft the Hold on `sox-listing-tool` for me to take on its own, resting on the advisor's trigger. Leave the merge with the integrated-audit twin as an open question until that manager confirms it. Then tell me what's left before I can call the first portfolio review done.

### ASSISTANT
I've drafted the Hold on `sox-listing-tool` in the "Screen result" of `portfolio/intake/sox-listing-tool.md`. I haven't added it to `decisions` in `portfolio.yaml`, so the item stays open at intake until you take it.

**Draft Hold**
- **Reason:** it depends on four items that aren't in place yet (the checklist, the register, the client-data approval and the junior-development workstream).
  - **Speeds the wrong step:** it speeds the staff step and not the senior-review constraint.
  - **Client data:** no AI tool is approved for client data.
- **Trigger:** the advisor's own trigger, unchanged. The checklist and register are in place with baselines, and the client-data approval is granted.
- **Resources:** none. The merge with `ct-int-listing-compare-draft` is not part of the decision.
- **Open question:** the merge stays open until the integrated-audit manager confirms the twin. The two items stay separate in the meantime, and their value isn't added.
- **My proposals:**
  - **Risk tier:** tier-4, provisional. It would produce attest evidence from client data, which ai-governance's default tiers place at the top. ai-governance should confirm it.
  - **Horizon:** long.
  - **Gate path and sponsor:** the full path, and the SOX/ICFR practice leader as sponsor. Both stay assumptions.
- **Check before revisiting:** whether simple rules could do the listing match, which the advisor's file doesn't record.

**What's left before you can call review 1 done**

*To close the review itself*
1. **Take or change the `sox-listing-tool` Hold.** Once you say so, I'll append the entry as `g0`, review 1, Hold, with the trigger as `revisit_when`.
2. **Agree the forum and rhythm.** Review 1 so far has your decisions only. The forum membership, the monthly rhythm, the live limit and the gate paths are still proposals.
   - **Portfolio file:** `portfolio.yaml` stays `setting-up` until they're agreed.
   - **Gatekeepers:** the practice leaders and the risk and quality partner are only proposed gatekeepers.
3. **Report the forum's view.** If the forum has to ratify the three Go/Hold decisions, tell me what it changes. I'd record any change as a new entry, since decisions are appended and never edited.

*Not needed to close it, but they hold up the next steps*
- **Seven items can't be screened yet:**
  - **No owner:** `sox-junior-development` and `sox-chase-assistant` need an owner role named.
  - **Desk review only:** the five integrated-audit items wait for the integrated-audit manager to confirm them.
- **Provisional entries:** these stay flagged until ai-governance confirms the risk tiers and the forum agrees the sponsors and gate paths.
- **Conditions on the Go decisions:**
  - **Validator and signer:** the register still needs a named validator and risk and quality's view on who can sign a validation record.
  - **Approval request:** the single approval request needs preparing, and risk and quality need to say whether it can go ahead before the checklist's attributes are written.
- **Baselines:** the review-note rate for both audit lines should come from the tracking-sheet record, not the reported figures.
- **Firm-wide gaps:** no tax or advisory ideas are logged, there's no inventory of AI already in use, and no `overlay/policy.md` exists.

Items 1 and 2 are what stand between you and calling review 1 done. Everything else is follow-up.

**Question:** Do you want to take the Hold on `sox-listing-tool` as drafted, or change anything first?

### USER
Let's take the highest-priority audit opportunity in the portfolio into prototype. Help me decide build versus buy and set up the solution brief.

### ASSISTANT
I've opened `solutions/sox-prereview-checklist/brief.md` and drafted the problem frame in section 1. The build-or-buy decision isn't made yet, and I don't expect it to be a product choice.

**The highest-priority audit item is `sox-prereview-checklist`.** It is the top-ranked audit item in the register (4.40) and the only audit item in discover.

**This item needs no AI.**
- The advisor's own description says the checklist is the solution: a written staff self-check, co-written with seniors and tested on past files. AI may only draft wording on non-client material.
- So the choice is probably not build versus buy. It is closer to configure: the firm's existing audit platform and templates, owned by the methodology owner.
- No tool in the catalog is involved, and there is no `overlay/` folder, so I describe it by runtime class (shared team skills).

**Prototype still needs `g1`.**
- The brief doesn't move the item. `g1` is not held, and its evidence isn't in yet: baselines from the tracking-sheet record for both lines, and the blind back-test on past files.
- I didn't touch the portfolio item's `solution` field. ai-portfolio writes that when `g1` is a Go.
- Treat the brief as `g1` evidence. Its leaning is to solve this without a model, which strengthens the case for a light prototype: co-write the checklist, then back-test it.

**What is still unconfirmed in the brief**
- The practice leader's own confirmation of the metric. You agreed it on their behalf.
- The 30% note rate and the 42-a-month figure are reported, not from the record.
- The last real instance hasn't been walked through.
- Risk tier is blank, because there is no policy file. The portfolio's tier-1 is provisional.

**Question:** Do you want any tool to check client evidence against the checklist automatically, or is the written checklist the whole solution? (A checking tool would be `sox-listing-tool` territory, which is on hold.)

### USER
The written checklist is the whole solution. I don't want a checking tool, since that's `sox-listing-tool` territory and it stays on hold. Set the brief to "configure, no AI" and put it in the practice leader's existing audit templates. Then list what I need to do to get the `g1` evidence in: the baselines from the tracking sheet and the blind back-test on past files.

### ASSISTANT
I've updated `solutions/sox-prereview-checklist/brief.md`: sourcing is `configure`, with no AI model and no new tool. The checklist goes in the practice's existing audit templates, and I recorded both decisions in the log. `sox-listing-tool` stays on hold, and the brief says that no checking tool is part of this solution.

Two points to check:
- **Brief left open:** the method says to stop a brief when the answer is "solve without AI". I kept this one open on your instruction, because it holds the checklist's design and back-test as `g1` evidence, and the log says so.
- **Template assumption:** you said "the practice leader's existing audit templates". I read that as the practice's existing workpaper templates and haven't named which ones. It's an open question in the brief.

Step 2 isn't fully closed, because the post-launch owner is still unnamed. I proposed the methodology owner, who approves the checklist anyway.

**What you need to do to get the `g1` evidence in**

The order follows dependencies.

1. **Secure the people (you and the SOX/ICFR practice leader):**
   - Get the practice leader to release two or three protected senior half-days in the shoulder weeks, outside peak.
   - Name the two seniors who will co-write the checklist.
   - Name the ITGC senior manager who will run the back-test, and the methodology owner who approves it.
2. **Pull the baselines from the tracking sheet (practice leader):** for both lines, replace the reported figures with records.
   - **SOX-only line:** the test-level review-note rate (reported at about 30%) and the evidence-completeness notes (reported at about 42 of 210 tests a month). Include the cause of each note, so the checklist can be tested against it.
   - **Integrated-audit line:** its note rate, which the `g0` Go condition counts as a second measure. No baseline exists. The one reported case had zero notes, so the integrated-audit manager needs to supply it.
3. **Walk through one real instance (you, with a senior):** the last test where a senior caught a completeness gap. Capture which check it was, what happened next and how long the second round took. This also fills the "work today" gap in the brief.
4. **Show the data in its real state (practice lead):** confirm where the past workpapers and the tracking sheet live, and that the back-test files can be read. Cases stay in the firm's approved systems.
5. **Co-write the checklist (the two seniors):** it covers the listing straight from the system, the full period, a complete comparison population, the sign-off date against policy, and the trace from each exception to its ticket. The methodology owner approves it.
6. **Run the blind back-test (ITGC senior manager):**
   - **Files:** past SOX-only files with known review notes.
   - **Blind condition:** the tester must not see the PCAOB comment text.
   - **Kill criterion:** the checklist would have caught at least 25% of the evidence-completeness notes. Under 25% triggers the kill criterion. Use the back-test protocol cited in the advisor's file.
7. **Check the three integrated-audit past files (integrated-audit manager):** test the draft integrated checklist on them, as the `g0` resources promised. Its value stays separate.
8. **Name the post-launch owner and the template it lives in (you):** this closes brief step 2.
9. **Get three confirmations before the gate (you, ai-governance and the risk and quality partner):**
   - **Risk tier:** tier-1 is still provisional and no `overlay/policy.md` exists. The brief's tier stays blank until ai-governance sets it.
   - **Independence check:** whether it applies to this checklist.
   - **Counterfactual:** a counterfactual idea and the leaning, which is configure, no AI.
10. **Take it to `g1`:** the gatekeepers (proposed) are the practice leaders and the risk and quality partner. I can prepare the evidence pack once steps 2 to 6 are in.

**Question:** Which audit templates should hold the checklist, and who owns them after launch?

### USER
Use the practice's existing SOX workpaper templates, the ones the seniors already fill in for control testing. The methodology owner owns the checklist after launch and approves any change to it. Record both in the brief, close step 2, and then prepare the `g1` evidence pack outline so I can see which pieces are still missing.

### ASSISTANT
I've closed step 2 in `solutions/sox-prereview-checklist/brief.md` and written the `g1` pack outline to `portfolio/gates/g1-sox-prereview-checklist.md`. The outline holds the status of each piece of evidence and lists which are still missing.

**Recorded in the brief**
- **Sourcing:** configure, no AI. The checklist goes in the practice's existing SOX workpaper templates that the seniors already fill in for control testing.
- **Support:** the methodology owner owns the checklist after launch and approves any change.
- **State:** steps 1 and 2 are done and `next_step` is 3. The decisions are in the log, which now has an entry for each of the two decisions you gave.
- **Open point:** the templates are the ones seniors fill in, but the checklist is a staff self-check. Step 3 needs to say which field staff reach before they submit.

**Where the `g1` evidence stands**

The outline covers 11 pieces of evidence: 1 is met, 2 are partly met, and 8 are not presented or not met.

| Status | Pieces |
|---|---|
| Met | The build/buy leaning: configure, no AI, with an owner named. |
| Partly met | The success metric: the practice leader's own confirmation isn't recorded. Feasibility: the scores are on file, but data readiness stays at 3 until the checks are written. |
| Not presented | Baselines from records for both lines, data seen in its real state, a counterfactual idea, the drafted and back-tested checklist, release of the people, and the independence view. |
| Not met | Risk tier: tier-1 is provisional and no policy file exists. |

Neither kill criterion can be tested until the checklist is written, and neither is met. The outline also lists the gatekeepers' options and a draft recommendation: don't hold `g1` until the baselines, the data check, the back-test and the people release have evidence.

**What stands in the way of holding the gate**
- **Proposals, not agreements:** the gatekeepers, the sponsor and the full gate path. Agree them, or record that `g1` is held on that basis.
- **Left unchanged:** the portfolio item's `solution` field, which gets set when `g1` is a Go. I also didn't touch `portfolio.yaml`.

**Question:** Do you want to agree the gatekeepers and sponsor with the forum before the evidence is in, or hold `g1` on the proposed basis and record that?

### USER
Hold `g1` on the proposed basis and record that. I'll agree the gatekeepers and sponsor with the forum in parallel, but I don't want to wait on them before the evidence work starts. Then draft the ask to the SOX/ICFR practice leader for the protected senior half-days and the two named seniors, since everything else depends on that.

### ASSISTANT
I've recorded the basis for `g1` and drafted the ask to the SOX/ICFR practice leader. Nothing has been sent.

**Basis for holding `g1`**
- **Where recorded:** it is in `portfolio/gates/g1-sox-prereview-checklist.md` and as a comment on the item's `next_gate` in `portfolio.yaml`.
- **Proposed basis:** `g1` will be held on the proposed gatekeepers (the practice leaders and the risk and quality partner), the proposed sponsor and the full gate path.
- **Forum agreement in parallel:** you're agreeing the gatekeepers and sponsor with the forum while the evidence work starts. If the forum changes any of them, I'll update the outline. I won't edit the `g0` entry.
- **Caveat on the outcome:** `g1` will carry a note that it was taken by gatekeepers the forum had not yet agreed, unless the forum has agreed them by then.
- **Not held yet:** the evidence is still missing, so the gate itself isn't held.

**The ask is in `portfolio/gates/g1-ask-sox-icfr-practice-leader.md`**
- **Request 1:** two or three protected senior half-days in the shoulder weeks, none in peak, to write down the seniors' unwritten checks.
- **Request 2:** two named seniors, chosen by the leader, with the methodology owner approving the checklist.
- **Costs and next steps:** the draft says plainly that the cost is time, with no spend and no AI. The back-test follows and the 25% kill line applies.
- **Two questions for the leader:** whether the sponsor role is right for them, and whether the ITGC senior manager can also run the back-test.
- **Also asked for:** the tracking-sheet records of review notes by cause, for the baseline.

**One conflict to settle.**
- **Overlap:** the ITGC senior manager is also the proposed validator for `sox-report-register` stage 1, at about four hours a week.
- **Options:** either the back-test waits for that stage, or another role runs it. That's for you and the leader to settle.

**Check before sending**
- **Kill line:** the 25% line is the low end of the advisor's own assumption, not a tested figure.
- **Roles only:** the draft uses roles, not names.
- **No performance wording:** I removed a line that hinted at choosing seniors by how often they catch gaps. It read as a judgment about individuals.

**Question:** Do you want me to add the baseline request for the integrated-audit line as a separate note to the integrated-audit manager, or keep the ask to the practice leader only?

### USER
Keep the ask to the practice leader only for now. I'll speak to the integrated-audit manager myself, so add a short separate note to them for the integrated-audit baseline, and keep it in roles only. On the ITGC senior manager overlap, have the back-test wait for the `sox-report-register` stage 1 workload rather than pull in another role, and record that as a dependency in the `g1` outline.

### ASSISTANT
The three changes are made, and nothing has been sent.

**Ask to the practice leader (`portfolio/gates/g1-ask-sox-icfr-practice-leader.md`)**
- It now covers only the SOX/ICFR practice leader. The two requests stay the same: protected senior half-days and two named seniors.
- The ITGC senior manager point is now a timing statement, not a question: the back-test waits for the register's first-stage workload, and no second role is pulled in. Writing the checklist does not wait.
- The baseline request is limited to the SOX-only line.
- Your decision on the overlap is recorded in the drafting notes.

**Note to the integrated-audit manager (`portfolio/gates/g1-note-integrated-audit-manager.md`)**
- It uses roles only and asks for counts and shares, with no client or engagement detail.
- It asks for four things:
  - The share of tests that drew a review note, over the same period as the SOX-only figure if possible.
  - How many tests that covers.
  - How many of those notes were about evidence completeness, if the records allow it.
  - How they count a note.
- It asks which figures come from a record and which are estimates. It also says their line's own checklist stays a draft and its value isn't added to the SOX-only one.
- It asks for nothing else: no confirmation of the five desk-review items, and not the three past files that the `g0` resources assumed. Those are still separate asks.

**Dependency in the `g1` outline (`portfolio/gates/g1-sox-prereview-checklist.md`)**
- The blind back-test (item 7) now waits for the `sox-report-register` stage 1 workload. I added it to the item's "needs first" column and to a new Dependencies section.
- **Consequence for the gate:** register stage 1 has its own open conditions, a named validator and the risk and quality partner's view on who can sign. If stage 1 slips, the back-test slips, and so does `g1`.
- **Open question:** what counts as the workload leaving room: the first client validated and timed, or only the key-report inventory finished? Nobody has defined this, and the back-test can't be scheduled without it.

I left `portfolio.yaml` alone, since the dependency is recorded in the `g1` outline.

**Question:** What should count as the ITGC senior manager's stage 1 workload leaving room: the first client validated and timed, or the key-report inventory finished?

### USER
The first client validated and timed. The key-report inventory alone doesn't free the ITGC senior manager's time, because the validation is the heavy part. Record that as the definition in the `g1` outline, and tell me what that implies for the earliest realistic back-test date so I can decide whether it's worth raising with the practice leader.

### ASSISTANT
I've recorded your definition in the Dependencies section of the `g1` outline. The ITGC senior manager's stage 1 workload has left room when the first client has been validated and timed, and finishing the key-report inventory alone doesn't count.

**I can't give you a calendar date.** I don't have the firm's peak and shoulder weeks, and the plans I write are sequenced by steps, not dates. What I can give is the earliest the back-test can start, counted in weeks of the validator's time.

**What the earliest back-test implies**
- **Validation effort:** the advisor's figures put the first client at about 24 hours, in a range of 16 to 32. Those are your estimates, not records.
- **Allowance:** the validator's allowance is about 4 hours a week outside peak.
- **Result:** that is roughly 4 to 8 weeks of the allowance, with 6 as the middle. Peak weeks don't count. If you give me the weeks outside peak, I can turn that into a count of calendar weeks.
- **Not included:** the key-report inventory comes first, and the advisor's file doesn't estimate its hours. The back-test's own hours aren't estimated either. So the real figure is longer.
- **Start conditions:** stage 1 hasn't started, and it needs three things first:
  - A named validator.
  - The risk and quality partner's view on who can sign a validation record.
  - AS 1215 record content agreed.

The back-test can't come earlier than this, and it's the last major piece of `g1` evidence. The half-days to write the checklist don't wait.

**Whether to raise it with the practice leader**

I think it's worth raising, because `g1` effectively waits on a stage nobody has started. The practice leader already controls the validator's hours. You could ask them about:
- **More hours:** whether more than about 4 hours a week is possible for stage 1.
- **Start order:** whether stage 1 can start before the half-days are fixed.
- **Accepting the wait:** treating the dependency as accepted, and noting it as a capacity constraint on that role at the next review.

Whether to ask for more than 4 hours a week, or to accept the wait, is your call. You've already ruled out pulling in another role.

I haven't changed the ask to the practice leader or the note to the integrated-audit manager.

**Question:** Do you want me to add the options above to the ask to the practice leader, or will you raise them in conversation?

### USER
I'll raise those options with the practice leader in conversation, so leave the ask as it is. Please add a line to the `g1` outline that the back-test timing is a capacity constraint on the ITGC senior manager role, to be raised at the next review. Then tell me what the next step in the brief is and whether anything else can move ahead without the back-test.

### ASSISTANT
I've added the line to the `g1` outline (`portfolio/gates/g1-sox-prereview-checklist.md`, Dependencies section). It says the back-test timing is a capacity constraint on the ITGC senior manager role, to be raised at the next portfolio review. It also notes that you're raising the options with the practice leader in conversation. The ask to the practice leader is unchanged.

**The next step in the brief is step 3, solution design.**

The step is short here because no model runs. It has to cover:
- **Placement:** purpose and non-goals, and where the self-check sits in the SOX workpaper template. The open point is which field staff reach before they submit, since the template is the one seniors fill in.
- **Flow:** staff complete the self-check, a senior reviews every exception and samples the completions, and the methodology owner approves any change.
- **Permissions:** the permission table is essentially read/write on the template, with no system access beyond what staff already have.
- **Failure behaviour:** what happens when the checklist can't be completed or conflicts with a senior's call, and what staff do when evidence doesn't fit. Logging is the completed checklist itself. This step also covers cost, which is staff time only, and role evolution.
- **Tier:** the risk tier stays blank for ai-governance.
- **Role evolution:** the capacity choice is still undecided at firm level.

**What can move ahead without the back-test**

| Piece | Why it can proceed |
|---|---|
| Co-writing the checklist | It needs the half-days, not the validator. |
| SOX-only baseline from the tracking sheet | It needs only the practice leader's records. |
| Integrated-audit baseline | It needs the manager's records. |
| Data seen in its real state | It needs only confirmation of where past workpapers live and that they can be read. |
| Counterfactual idea | It can be drafted now. |
| Independence view and risk tier | They need the risk and quality partner and ai-governance, not the back-test. |
| Forum agreement on gatekeepers and sponsor | It's already running in parallel. |
| Brief steps 3 and 4 | Step 4, the evaluation plan, is the back-test protocol: the case inventory, gold answers from the notes' causes and the 25% line. It can be drafted before the back-test runs. |
| Register stage 1 start conditions | The named validator, the risk and quality view on who can sign and AS 1215 record content. Settling them starts the clock on the back-test. |

**What cannot proceed without the back-test:** the drafted-and-tested checklist (item 7), the kill-criterion check and the strategic-fit confirmation that depends on the written criteria. Those are the last items to arrive.

**Question:** Which field in the SOX workpaper template do staff reach before they submit, so the self-check sits where they will see it?

### END
session 807fbf4d-3850-5c6c-82b1-8d3750715cd5