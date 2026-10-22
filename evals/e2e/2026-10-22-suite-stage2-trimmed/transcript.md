### USER
The integrated-audit manager has validated `ct-int-nonclient-drafting`. Record `g0` as a Go into discover: the manager's time, released by the practice leader. Then take it to ai-solution-delivery: frame it, decide build versus buy, and open the brief as `g1` evidence.

### TOOLS
- Skill: ai-transformation:ai-portfolio Record g0 as a Go into discover for ct-int-nonclient-drafting: the integrated-audit manager validated it; the manager's time is released by the practice leader.
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md
- Edit: portfolio/portfolio.yaml
- Write: solutions/ct-int-nonclient-drafting/brief.md
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-nonclient-drafting.md

### ASSISTANT
`g0` is recorded as a Go into discover, and the brief is open as `g1` evidence. The brief is a draft: the baseline, the owner's metric and a sample test are still missing, so step 1 is not ticked and sourcing stays `undecided`.

I ran the ai-portfolio skill, then the ai-solution-delivery steps (frame, build or buy, open the brief), and checked that the YAML files parse.

**The g0 Go (`portfolio/portfolio.yaml`)**
- The item is now in `discover` and active. The provisional flag is gone because the manager validated it.
- **Resources:** the integrated-audit manager's time, released by the practice leader. No budget, since it runs on the existing approved assistant. Data is non-client templates and synthetic examples only.
- **Conditions:** no client data, and a senior approves templates before shared use.
- **Kill criteria:**
  - Client data turns up in prompts or drafts.
  - No baseline can be found from records.
  - The manager's time is withdrawn.
  - A template library alone does the job.
- **Next gate:** `g1`, with `g1` and `g2` combined on the light path. The intake record's evidence table is filled in.
- **Decider:** I recorded the portfolio lead, which is the light-path decider, and noted the practice leader as consulted. Correct that if someone else decided.

**The brief (`solutions/ct-int-nonclient-drafting/brief.md`)**
- **Framing:** the baseline is reported only, grade D, about 0–0.2 hours per control test. The owner hasn't confirmed the metric yet.
- **Build or buy (draft leaning):** configure the approved enterprise assistant with shared prompts and a share-and-review routine. A plain template library is the baseline it has to beat. A build has no owner and isn't warranted.
- **Tool catalog:** no catalog exists, so I recorded the leaning as a draft and requested a catalog entry through ai-governance.
- **Risk tier:** `tier-2` is provisional, copied from the draft policy. I left it null in the portfolio, as the policy asks.
- **Hand-back:** I set the item's `solution` field in the portfolio.

Value is still low (index 2.44). The Go holds only while the routine stays cheap, and the intake record says the quick-win category wouldn't survive a re-score. I left the category as it is. You may want to re-score it at `g1`.

**Question for the integrated-audit manager:** what number would they use to say this helped, and which record shows template and wording time today?

### USER
The portfolio lead decided it, so that's correct. The practice leader was consulted only. For the metric, the manager says they'd count hours per control test on template and wording work, taken from timesheet codes. I'll check what the codes cover. Go ahead and request the catalog entry, then re-score the category at `g1` so we know if it still counts as a quick win.

### TOOLS
- Skill: ai-transformation:ai-governance Request a tool-catalog entry for the approved enterprise AI assistant (non-client material only), with max_risk_tier, for solution ct-int-nonclient-drafting (brief at solutions/ct-int-nonclient-drafting/brief.md). Draft overlay/policy.md proposes tier-2 for this use and a ceiling of tier-2 for firm-enterprise-assistant; the risk lead has not yet confirmed.
- Write: overlay/tool-catalog.yaml
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-nonclient-drafting.md

### ASSISTANT
I wrote the catalog request as a draft entry and added the re-score to the `g1` evidence list. Nothing is approved yet. The register, the catalog and the brief all parse.

**Catalog entry (`overlay/tool-catalog.yaml`, new file)**
- One entry, `enterprise-assistant`, at status `under-review`.
- **Proposed `max_risk_tier`:** `tier-2`, as the draft policy proposes. The risk lead hasn't confirmed it.
- **Left for the IT/security lead:** the vendor, contract, underlying model, regions, user groups, retention and exit plan. I marked these "to be confirmed" rather than guess.
- **Assumptions I flagged:**
  - Tool tier is `commercial`.
  - Data classes are `public` and `firm-internal`, because the policy hasn't defined data classes yet.
- **Not written:** the vendor evaluation, so `vendor_file` points at a file that doesn't exist yet. The request path is also still unset (governance step 7).
- **Retention matters for this item.** The brief needs a prompt log or retention setting to notice client data pasted by mistake.

**Metric**
- The brief now records the manager's metric as confirmed: hours per control test on template and wording work, from timesheet codes. The baseline stays reported-only, grade D, until you've checked the codes.
- If no code isolates template and wording time, we'll need a short time sample instead.

**Category re-score**
- It's now a `g1` evidence line on the item and a row in the intake record's evidence table.
- Value stays 2 until the baseline exists. If the baseline doesn't lift it, the screening rules park the item rather than call it a quick win. That would be a recorded Recycle or Hold at `g1`, not a quiet re-label.

**Open items**
- **Timesheet codes:** whether any code isolates template and wording time (yours).
- **Catalog entry:** vendor, contract, retention and user-group details for the IT/security lead to fill in.
- **Tier:** `tier-2` still needs the risk lead's confirmation.

### USER
Timesheet codes: there's one code for "engagement administration" and nothing that isolates template and wording work, so the manager's metric can't come from the codes. Plan on a short time sample instead: five control tests over two weeks, with the manager logging template and wording time by hand. Update the brief's baseline to say that, and tell me what the sample needs to look like to move it from grade D to something we can use at `g1`.

### TOOLS
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: portfolio/intake/ct-int-nonclient-drafting.md

### ASSISTANT
I updated the brief's baseline and the intake record's evidence table with the new plan. The brief now says the codes can't isolate the time, and that the baseline will come from a hand-logged sample of five control tests over two weeks. The sample rules are in its Open questions.

**On grade D**

The item's "grade D" is the no-measure tag on the value range. It isn't a scale I can re-grade by running a sample. What the sample changes is the basis label, from "reported" to "observed". It also gives a measured range to replace the 0–15% guess. At `g1` I'd present it as "observed, self-logged, n=5", not as a higher grade, and let the gatekeepers weigh it.

**What the sample needs to be usable at `g1`**
- **One written definition** of "template and wording work", with two or three examples inside and outside it, agreed before logging starts. Without it, five tests will measure five different things.
- **The same unit as the existing figure:** staff hours per control test, against the 1.5 h hands-on number. Log minutes on template and wording and total hands-on minutes for each test, so the share can be checked against the 0–15% guess.
- **Pre-change only.** Record whether the assistant was used on each test. A mix of assisted and unassisted tests wouldn't be a baseline.
- **Level of the person doing the work, not their name,** plus a note on any unusual test.
- **The range across all five tests, not only the mean.** With n=5, a spread from 3% to 25% tells you more than an average.
- **A cross-check if you can manage it.** The manager is logging their own time, which is self-reported. Having a second person time one or two tests is a cheap way to see whether the logging is off.

**What the result decides**
- If template and wording time comes out near the top of the range, say 10–15% of hands-on time, value probably moves above 2. The category can stand as a quick win, and I'd re-score it from the measured range.
- If it comes out near zero, the item parks. The kill criterion "no saving can be shown" would also be in play.
- Either way, the re-score and the category call happen at `g1` with the sample in hand. Five tests is thin, so the portfolio decision should say so.

The two-week window is your call. I'd rather you close the sample on five logged tests than on the date, so a slow fortnight doesn't leave you short.

### USER
Good, that's clear. Write the sample protocol into the brief as a short checklist the manager can follow, including the written definition of template and wording work with a few in and out examples. Draft those examples from non-client material only. Then tell me what the portfolio needs from me at `g1`, and whether the other audit opportunities in the plan should come into the firm-wide portfolio now or wait until this one clears.

### TOOLS
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md

### ASSISTANT
The brief now has a "Baseline sample protocol" under Open questions, written for the manager. It has a draft definition of template and wording work, a six-row in/out table drawn from generic non-client material, and an eleven-item checklist. The "unsure" column handles edge cases without anyone ruling on them during logging. The manager should correct the definition and examples before logging starts.

**What the portfolio needs from you at `g1`**

Gatekeepers for this stage are the practice leader, the risk lead and the IT/security lead. On the light path `g1` and `g2` combine, so one decision covers both. You'll need:

1. **Baseline written in:** the observed sample, labelled as such, with the range and the share of hands-on time.
2. **Value re-scored and the category re-checked:** this is the "still a quick win, or park" call.
3. **Benefit owner named.** The metric is agreed, but nobody is recorded as the benefit owner yet.
4. **Data seen in its real state:** the manager looks at the actual non-client templates and synthetic examples.
5. **Strategic fit and feasibility assessed**, plus the build or buy leaning. The leaning is a draft until a sample test of the assistant against a template-library baseline has run. That test is separate from the time baseline.
6. **Combined `g2` evidence:**
   - A prototype run on real non-client material.
   - Controls defined. The catalog entry's retention and logging need to be settled so client data pasted by mistake can be noticed.
   - The business case still holds.
   - A skills check.
7. **Catalog entry and tier moving:** IT/security fills in the entry and the risk lead confirms `tier-2`. The tier stays provisional until the policy is approved.
8. **Live limit, which is still unset.** A Go at `g1` enters prototype or pilot, and the limit binds there. The steering group has to set a number first, or the Go gets held. That's the one thing only you can unblock.

I'd also write the decision criteria down before the sample comes in, so the number doesn't set the bar after the fact.

**The other audit opportunities**

They're already in the register. The SOX-only items and the integrated-audit variants were imported at intake, and the `sox-chase-assistant` is on Hold. So the question is about `g0` decisions.

- **Don't hold them for this item.** It has no dependencies on them, and it's a light-path, non-client item. They are mostly full-path, client-data items that need the risk lead's co-decision, so this item clearing tells you little about them.
- **Highest-priority AI item:** I haven't checked the scores for that, so I wouldn't name one. By weighted score, `sox-prereview-checklist` (4.40) is the top item overall, but it's `ai_use: none`, so it isn't an AI item. The AI items with the shortest path to a decision are the ones that don't need client data. Everything in that group sits behind the unset live limit and the pending risk-lead decisions.
- **The integrated-audit variants** (`ct-int-validated-report-register`, `ct-int-precheck-checklist` and the listing and secondary-review variants) can't pass `g0` until the manager validates them and the SOX primary passes. Putting the same validation request to the manager now is cheap.
- **What this item does give you** is a worked run through the light path, the catalog request and the baseline sample. That's useful practice, but it isn't a gate the others depend on.

If you want, I can set out the `g0` queue as a proposal for the portfolio lead and risk lead, ordered by what blocks each item.

### USER
Yes, set out the `g0` queue as a proposal for the portfolio lead and risk lead, ordered by what blocks each item. Put the validation request to the integrated-audit manager for the variants at the same time. I'll take the live limit to the steering group myself. Suggest a number and a short rationale I can bring, and write the `g1` decision criteria into the brief now, before the sample comes in.

### TOOLS
- Edit: solutions/ct-int-nonclient-drafting/brief.md
- Edit: solutions/ct-int-nonclient-drafting/brief.md

### ASSISTANT
I wrote the `g1` decision criteria into the brief. The `g0` queue, the validation request and the live-limit suggestion are below, since pre-reads and drafted messages go in chat. I haven't changed any other portfolio file.

## `g1` criteria (now in the brief, drafted before the sample)

| Outcome | When |
|---|---|
| **Go** | Median template and wording share is 10% or more, and at least 3 of 5 tests are at 5% or more |
| **Recycle** to a smaller scope | Median is 5% to under 10%, or only one or two tests drive it |
| **Kill** or Hold | Median is under 5%, or the sample can't be completed |

- **Conditions for a Go:** the same non-numeric conditions apply: benefit owner named, routine time estimated at under half the saving, assistant tested against a template library, catalog retention filled, live limit set, and value re-scored above 2. Category still stands as a quick win only on that last one.
- **Numbers are my proposals.** The gatekeepers confirm or change them before logging starts, and the confirmation goes in the decisions log.
- **Someone has to count the integrated line's monthly control tests from records.** Without that count the routine-cost test can't be run.

## `g0` queue (proposal for the portfolio lead and risk lead)

Ordered by what blocks each item. These are proposed outcomes from the intake records, and the deciders decide.

**A. Ready for the deciders now (full path, needs the risk lead)**

| # | Item | Proposed | What blocks it |
|---|---|---|---|
| 1 | `sox-prereview-checklist` (weighted 4.40) | Go to discover | Only the co-decision. The risk lead should confirm that the back-test over past client files inside the firm is permitted (policy question 4). |
| 2 | `sox-report-register` (3.70) | Go, with readiness work as conditions | The co-decision. Readiness index is just under 3.5. |
| 3 | `sox-client-data-approval` (3.00) | Choose: Hold, or Go for stage 0 only | The deciders' choice. Stage 0 is about 40–80 h of practice-lead time (placeholder), and the 3–4 month approval lead time applies to every client-data tool. The approval itself is decided by the risk lead, IT/security lead and counsel, not this gate. |

**B. Decide as a Hold, with a trigger**

| # | Item | Proposed | Trigger or blocker |
|---|---|---|---|
| 4 | `sox-request-template` (4.00) | Hold | Revisit once a client's key-report inventory exists. |
| 5 | `sox-listing-tool` (2.25) | Hold | Needs the checklist, the register and the approval first. `sox-junior-development` isn't in the register because its title breaks the YAML. |

**C. Waiting on the manager's validation, then on their primary**

A variant's `g0` follows its primary, and they are counted once under it.

| # | Item | Waits for |
|---|---|---|
| 6 | `ct-int-precheck-checklist` | Validation, and `sox-prereview-checklist` passing `g0` |
| 7 | `ct-int-validated-report-register` | Validation, and `sox-report-register` passing `g0` |
| 8 | `ct-int-listing-compare-draft` | Validation, and `sox-listing-tool` passing `g0` (proposed Hold, so this lands on Hold too) |
| 9 | `ct-int-ai-secondary-review` | Validation, and `sox-ai-secondary-review` leaving outline |

**D. Not queued**
- `sox-chase-assistant` is already on Hold.
- `sox-ai-secondary-review`, `sox-agent-testing` and `sox-platform-plus-review` are outline stubs with no scores.
- `firm-enterprise-assistant` is an inventory entry that needs an owner and a use list.

One inconsistency to fix: `ct-int-listing-compare-draft` lists the SOX/ICFR practice lead as owner. The other integrated-audit items list the integrated-audit manager.

## Validation request to the integrated-audit manager (draft)

> Four integrated-audit items in the AI portfolio were drafted from a desk review, and nobody who does the work has checked them yet. Could you read each and tell us what's wrong or missing?
> - Written pre-review checklist for evidence gaps
> - Register of specialist-validated reports
> - Tool to compare listings to active users and draft the workpaper
> - AI secondary review of ITGC workpapers
>
> For each: does it describe how integrated-audit testing actually works? Are the figures right (about 1.5 h hands-on per test, one reported case with zero review notes, about 2 days in the senior queue)? Are they distinct from the SOX-only versions, or the same item? Which would you own? Please don't send any client names or content.

Their answers decide whether each variant stays a distinct item or merges into its primary.

## Live limit: suggest 3

Today the count is 0, since nothing is in prototype, pilot or scale.

- **Rule:** no more live items than there are named owners and review capacity to carry them.
- **Owners:** the audit plan names three owner roles: the integrated-audit manager, the SOX/ICFR practice lead and the ITGC senior manager. Three is one live item each.
- **The real constraint is review capacity.** Seniors are about 90–95% booked in busy season (reported), and any live item adds review load on them. That argues against going above 3, and I would not count the limit as a target to fill.
- **Candidates:** the three items most likely to reach `g1` first are `ct-int-nonclient-drafting`, `sox-prereview-checklist` and `sox-report-register`. A fourth, such as `sox-client-data-approval` stage 0, would sit behind them.
- **Assumptions to say out loud:**
  - The limit counts every item in prototype, pilot or scale, including ones with no AI.
  - The portfolio is audit-only at the moment. Other practices will need the number revisited as they log items.
  - I don't have the owners' actual capacity, so the steering group should confirm that each can carry one.
- **Check at the first rebalance,** which is every third review.

I can write the queue into a review pack or the register once the steering group sets the number.

### USER
Three works as the live limit, and I'll take it to the steering group with the review-capacity rationale. Please write the `g0` queue into a review pack for the portfolio lead and risk lead, with the validation request attached. Fix the `ct-int-listing-compare-draft` owner while you're there so it matches the other integrated-audit items.

### TOOLS
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/ct-int-listing-compare-draft.md
- Edit: portfolio/intake/ct-int-listing-compare-draft.md
- Write: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md

### ASSISTANT
The review pack is written at `portfolio/reviews/1-review.md`, with the validation request attached as Attachment A. The `ct-int-listing-compare-draft` owner is fixed. The register still parses, and the pack's stage, horizon, class, category and no-AI counts match it.

**The pack**
- **Part A:**
  - Pipeline: 14 at intake and 1 in discover.
  - Live items: 0 of 3, with 3 shown as proposed because the steering group hasn't set it.
  - Gate results: the two `g0` decisions already made, the Hold on `sox-chase-assistant` and the Go on `ct-int-nonclient-drafting`.
- **Decision blocks:** five items for the portfolio lead and risk lead, in order of what blocks them.
  - `sox-prereview-checklist`: proposed Go. The risk lead should also confirm the back-test over past client files is permitted.
  - `sox-report-register`: proposed Go, with readiness work as conditions.
  - `sox-client-data-approval`: Hold, or a Go for stage 0 only. The intake record proposes neither, so it's the deciders' choice.
  - `sox-request-template`: proposed Hold.
  - `sox-listing-tool`: proposed Hold.
- **Not asked:** the four integrated-audit variants wait on the manager's validation and their SOX-only primaries.
- **Evidence labels:** every figure keeps its basis (reported, estimate, placeholder). I left the item owners' recommendation as "not yet asked" instead of writing one for them.
- **Part B** is a blank table for the deciders' outcomes. I did not set `state.last_review`, because no review has been held.
- **Actions table:**
  - Taking the live limit to the steering group, which is yours.
  - The five `g0` decisions.
  - The validation request.
  - The back-test question for the risk lead.
  - The `sox-junior-development` title fix.
  - The catalog entry and the tier confirmation.

**Owner fix**
- `ct-int-listing-compare-draft` now lists the integrated-audit manager as owner, in both `portfolio.yaml` and its intake record.
- I didn't touch the advisor file. It names the "Practice lead" in the next step, so the two now differ until the advisor skill is re-run.

**Decisions for you**
- The pack leaves the live limit unrecorded. Once the steering group sets the number, I'll write it into `settings.live_limit` and update the pack.
- I added the attachment as its own section after the template's open questions, because the template has no attachment slot. Say if you'd rather have it moved into the Actions table.
- The pack records the live limit as counting every item in prototype, pilot or scale, including ones with no AI. It's listed under Open questions, so correct it there if the steering group counts differently.

### USER
Move the attachment into the Actions table instead of its own section, so the pack follows the template. The live limit counting every item in prototype, pilot or scale, including non-AI ones, is fine as written, so leave it. Next, run the `sox-junior-development` title fix so it imports into the register, and tell me what the portfolio looks like once it's in.

### TOOLS
- Skill: ai-transformation:transformation-advisor Fix the YAML in units/sox-only-outsourcing/opportunities.yaml: the title of option sox-junior-development breaks the file (unquoted colon or similar). Quote the title, change nothing else, then confirm the file parses so ai-portfolio can import the item.
- Edit: units/sox-only-outsourcing/opportunities.yaml
- Edit: portfolio/portfolio.yaml
- Write: portfolio/intake/sox-junior-development.md
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/intake/sox-listing-tool.md
- Edit: portfolio/intake/sox-listing-tool.md
- Edit: portfolio/portfolio.yaml
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md
- Edit: portfolio/reviews/1-review.md

### ASSISTANT
`sox-junior-development` is now in the register, and the review pack has the attachment folded into its Actions table. The register parses with 16 items, no duplicate ids, and every `depends_on` resolves. The pack's counts match it.

**Pack**
- The validation message is now a row in the Actions table, and "Attachment A" is gone.
- The pack now has a seventh decision block for `sox-junior-development`, and the Actions table says "six items" for `g0`.
- **Counts updated:** intake is 15, medium-horizon items 4, business-automation items 12, foundations 4.
- **Actions changes:** the "fix the title" row is replaced with one for naming the holder of the junior-workstream owner role, assigned to the SOX/ICFR practice lead.

**Title fix and import**
- The advisor skill quoted the title in `units/sox-only-outsourcing/opportunities.yaml`, and nothing else changed. The title had an unquoted colon, which broke the file at line 106.
- I imported the item with its intake record, copying the advisor's value line, scores, grade B evidence id, plan case and steps as they stand. I added the owner role to `roles.other`. I updated the `sox-listing-tool` intake record, which said this item wasn't in the register yet.
- **Computed against the portfolio weights:** weighted 3.35, value index 2.56, readiness index 4.00, horizon medium. Category is foundation as the advisor and you decided it. Value 2 would park it under the category rules.

**Judgement calls I made, for you to confirm**
- **Gate path is `full`, proposed.** The readiness and judgment-time measures concern staff, and the draft policy treats monitoring or evaluating staff as a risk-lead matter. I recorded that the measures must stay aggregate, with no individual ratings.
- **Class is `business-automation`.** Only the synthetic practice cases use AI, so it could instead be read as a no-AI process item.
- **No `g0` decision is recorded.** The quadrant default is Hold. A Go to discover is defensible once the owner role has a holder, since the plan's first step is to name the owner and take baselines.
- **Owner is a role with no holder yet,** which is the plan's own placeholder. If you'd rather it sit at `outline` until someone is named, say so and I'll change the status.

**What the portfolio looks like now**

| | |
|---|---|
| Items | 16: 1 in discover (`ct-int-nonclient-drafting`), 15 at intake |
| Live against the limit | 0 of 3 (3 is proposed, not yet set) |
| `g0` decided | 2: one Go (`ct-int-nonclient-drafting`), one Hold (`sox-chase-assistant`) |
| Queued for the deciders | 6: checklist, register, client-data approval, request template, listing tool and junior development |
| Waiting on validation | 4 integrated-audit variants, each also waiting on its primary |
| Not queued | 3 outline stubs, and the enterprise-assistant inventory entry |
| Categories | 3 quick wins (all integrated-audit variants), 4 foundations, 1 big bet, 7 parked |
| No-AI items | 5. The checklist, request template and register depend on none, and the listing tool and secondary review depend on them |

The dependency chain is now complete in the register. The checklist comes first, then the register, the client-data approval and junior development. The listing tool sits behind all four, and `sox-ai-secondary-review` is an outline stub parked behind the listing tool. The checklist is the item most of them wait on.

Two things I have not done. I haven't recorded any `g0` decision beyond the two already made. I also haven't written the live limit into `settings.live_limit`, since the steering group hasn't set it.

### END
session 807fbf4d-3850-5c6c-82b1-8d3750715cd5