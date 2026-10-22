# Portfolio review 1

<!-- One file per review: portfolio/reviews/<n>-review.md. Part A is the pack, prepared before the deciders meet; Part B records what they decided and is blank until then. Owners are roles, never names. DRAFT pack: scores and proposed outcomes come from the intake records; nothing here is a decision. -->

| | |
|---|---|
| Review number | 1 (previous: none) |
| Forum | Portfolio lead (head of AI office) and Risk lead, as the g0 deciders on the full path. The AI steering group has not yet met; it is asked only to set the live limit (see Actions) |
| Prepared by | Portfolio lead (head of AI office), drafted with ai-portfolio |
| Rebalance review? | No |

## Part A · Pack

### 1. Pipeline by stage

| Stage | Items | Change since review 0 |
|---|---|---|
| intake | 15 | +15 |
| discover | 1 | +1 (`ct-int-nonclient-drafting`, g0 Go on the light path) |
| prototype | 0 | |
| pilot | 0 | |
| production | 0 | |
| scale | 0 | |
| retire | 0 | |
| Live (prototype, pilot, scale) against the live limit | 0 / 3 (proposed; the steering group has not yet set it) | |

Of the 15 at intake: 11 are screened (7 SOX-only, of which 1 is on Hold, and 4 integrated-audit variants), 3 are outline stubs and 1 is an inventory entry (`firm-enterprise-assistant`). The 4 integrated-audit variants are provisional, not yet validated by the integrated-audit manager.

Enablement line (seat and licence roll-outs, tracked apart): none logged. The approved enterprise assistant is an inventory entry, not a roll-out.

### 2. Gate results since the last review

| Item | Gate | Outcome | Reason in one line |
|---|---|---|---|
| `sox-chase-assistant` | g0 | Hold | Low value (index 2.44, low end of the range is zero); the request template may remove most of the chasing. Decided by the portfolio lead, light path |
| `ct-int-nonclient-drafting` | g0 | Go | Validated by the integrated-audit manager; high readiness (4.73), low value (2.44); cost is a routine on the existing approved assistant. Manager's time released by the practice leader; practice leader consulted only. Decided by the portfolio lead, light path |

### 3. Decisions asked of the deciders

The ask on each is a `g0` decision on the full path: the portfolio lead and the risk lead decide together. The live limit is not `g0` evidence; where it matters, only the item's place in the queue is noted. Proposed outcomes are from the intake records' Screen results. Items are in the order of what blocks them.

#### `sox-prereview-checklist`: Written pre-review evidence checklist that captures the senior's unwritten checks

- **Ask:** Go to discover at g0 (full path).
- **Evidence for:** value index 4.33 and readiness index 4.45; weighted 4.40 (highest in the register); no AI needed (`ai_use: none`); value is a range with a grade D basis: 5-12 percentage points off the test-level review-note rate (30% today, reported from the tracking sheet) and 10-25 second-round senior reviews avoided a month. Senior review capacity is the plan's stated constraint.
- **Evidence against:** the baseline is reported, not from a record; hours per second-round review are unknown; data readiness is 3. It touches past client files for the back-test.
- **Kill criteria agreed at entry:** none yet; to be agreed at the Go.
- **Early warnings:** none yet.
- **Options:** (1) Go to discover; releases the SOX/ICFR practice lead's time for the checklist and the baseline. (2) Hold; releases nothing, and keeps `sox-client-data-approval` and the variant `ct-int-precheck-checklist` waiting, since both depend on it. 
- **Recommendation from the item owner:** not yet asked; the intake proposal is Go.
- **Blocker:** the co-decision. The risk lead should also say whether the back-test over past client files inside the firm is permitted (policy question 4); this would be a condition on the Go.

#### `sox-report-register`: One specialist validates each key report once; a register records it for reuse

- **Ask:** Go to discover at g0 (full path), with readiness work named as conditions.
- **Evidence for:** value index 4.11; capacity 25-63 staff hours a month net of one-off specialist effort of about 180-600 hours (user estimates), a quality overlap with the checklist (do not add), and 0-2 PCAOB ITGC evidence comments avoided per cycle (baseline 2 last cycle, reported). The integrated-audit line, where a specialist validates each report once, is the one case that shows the pattern (reported).
- **Evidence against:** readiness index 3.36, just under 3.5 (feasibility 3, data readiness 3). Grade D basis; the 0.25-0.5 h per test is capped until a time sample exists. The one-off specialist effort is the cost to carry.
- **Kill criteria agreed at entry:** none yet; to be agreed at the Go.
- **Early warnings:** none yet.
- **Options:** (1) Go with readiness work as conditions. (2) Hold until the checklist's baseline exists. 
- **Recommendation from the item owner:** not yet asked; the intake proposal is Go with conditions.
- **Blocker:** the co-decision. If it goes ahead, the variant `ct-int-validated-report-register` can follow once validated.

#### `sox-client-data-approval`: Take one controls-testing use through the client-data approval path

- **Ask:** Choose between Hold and a Go for stage 0 only, at g0 (full path).
- **Evidence for a stage 0 Go:** it carries the 3-4 month lead time for every client-data tool; stage 0 costs the practice lead about 40-80 hours to prepare the pack (placeholder). It has no standalone value, so it is an enabler.
- **Evidence against:** both indexes under 3.5 (value 2.56, readiness 3.36), so the quadrant default is Hold or Kill. It depends on `sox-prereview-checklist`.
- **Kill criteria if Go:** the approval scope is refused or cannot be narrowed to one use.
- **Early warnings:** none yet.
- **Options:** (1) Hold, with `revisit_when` the checklist's written attributes exist. (2) Go for stage 0 only, as an exception to the quadrant default; releases about 40-80 hours of practice-lead time (placeholder).
- **Recommendation from the item owner:** not yet asked; the intake record offers the two options and proposes neither.
- **Blocker:** the deciders' choice. The approval itself is decided by the risk lead, IT/security lead and general counsel, not by this gate.

#### `sox-request-template`: Request template naming the report and its parameters up front

- **Ask:** Hold at g0 (full path).
- **Evidence for a Hold:** value index 3.44, readiness 4.45; the full-path default for value under 3.5 is Hold. Overlaps the checklist and the register on the same evidence-completeness notes (do not add the values).
- **Evidence against:** readiness is high and the idea is cheap; the plan starts it client by client as each inventory completes.
- **Options:** (1) Hold, `revisit_when` a client's key-report inventory exists (the first step of the register). (2) Go to discover now; this releases practice-lead time ahead of the inventory.
- **Recommendation from the item owner:** not yet asked; the intake proposal is Hold.
- **Blocker:** none except the decision.

#### `sox-listing-tool`: Certified tool for portal pull, listing comparison and workpaper first pass

- **Ask:** Hold at g0 (full path).
- **Evidence for a Hold:** value index 2.11, readiness 2.36; weighted 2.25. Depends on the checklist, the register, the client-data approval and `sox-junior-development`. The coverage figure (30-60%) is a guess, not a measure. Pattern evidence is self-reported by the deploying teams.
- **Evidence against:** capacity of 24-126 staff hours a month at full coverage is the largest forecast in the audit set, but near zero for the first approved scope.
- **Options:** (1) Hold, `revisit_when` the checklist and register are in place with baselines and the approval is granted. (2) Kill; not proposed.
- **Recommendation from the item owner:** not yet asked; the intake proposal is Hold.
- **Blocker:** none beyond the decision and its dependencies. `sox-junior-development`, which it also depends on, is now in the register (imported after the advisor skill quoted its title).

#### `sox-junior-development`: Named junior-development workstream: juniors keep the completeness check and the timing-difference call

- **Ask:** Hold or Go to discover at g0 (full path, proposed).
- **Evidence for:** readiness index 4.00; weighted 3.35. A stated design requirement and the guard on the junior pipeline; `sox-listing-tool` depends on it. The plan's go/no-go is that the owner and protected coaching time exist before any tool goes live in shadow mode. Turnover is about 25% (reported, practice-level).
- **Evidence against:** value index 2.56 and value score 2 (the low end of the range is zero); the category is foundation by the user's decision, and under the category rules value 2 would park it. Feasibility and time to value are 3 because protected coaching time is not secured while seniors are 90-95% booked (reported). Evidence is mixed: one vendor customer story (grade B, one 20-person firm, not SOX testing) and a PCAOB research proposal that warns of reduced skill-building. Not a forecast; baselines are unmeasured.
- **Kill criteria if Go:** protected coaching time cannot be secured.
- **Early warnings:** none yet.
- **Options:** (1) Hold, `revisit_when` a holder for the owner role is named and the checklist's written checks exist; releases nothing. (2) Go to discover; releases the owner's time (2-4 h a week, placeholder) to take baselines, which the plan lists as a Now step.
- **Recommendation from the item owner:** not asked; the owner role has no holder yet. The intake proposal is Hold by the quadrant default, with Go defensible once the owner role is filled.
- **Blocker:** the owner role has no holder; the risk lead should look at the staff measures (aggregate only, no individual ratings).

#### Not asked at this pack

- **Waiting on validation and their primary (4 integrated-audit variants):** `ct-int-precheck-checklist`, `ct-int-validated-report-register`, `ct-int-listing-compare-draft`, `ct-int-ai-secondary-review`. Their `g0` follows their primary's, and they are counted once under it. The validation request is in the Actions table.
- **Already decided:** `sox-chase-assistant` (Hold), `ct-int-nonclient-drafting` (Go).
- **Outline stubs, no scores:** `sox-ai-secondary-review`, `sox-agent-testing`, `sox-platform-plus-review`.
- **Inventory entry:** `firm-enterprise-assistant` needs an owner and a use list.

### 4. Early-warning flags

None. No item is past a gate yet.

### 5. Balance

| View | Now | Comment |
|---|---|---|
| Horizon: near, medium, long | 5 / 4 / 3 (counts of scored items, variants included) | 3 outline stubs and the inventory entry are unscored |
| Class: individual-productivity, business-automation, new-value | 3 / 12 / 1 | Variants are counted once under their primaries in the value totals |
| Category: quick win, foundation, big bet | 3 / 4 / 1 | The other scored items are parked. The 3 quick wins are all integrated-audit items; `ct-int-nonclient-drafting` is to be re-checked at g1 |
| No-AI items (`ai_use: none`), counted apart from AI items | 5 | The checklist, the request template, the register and two of their variants; the AI items (listing tool, secondary review) depend on them |
| Levers covered | capacity, quality, risk, experience | Margin (cost) has no item. Experience is qualitative only |
| Units and functions | Audit only (SOX-only outsourcing and integrated audit) | No other practice or function has logged an item; the live-limit rationale assumes this |
| Run cost and cost constraints | Not estimated | The one cost figure is the specialist validation effort (180-600 hours, user estimate) and the 40-80 hours of pack preparation (placeholder) |

### 6. Benefits: forecast versus realised

No benefit rows yet; none are due before `g3`.

Portfolio measures: items with a benefit owner 0 of 16; items reviewed after go-live 0 of 0; benefit success rate not applicable. Use-case effects and enterprise P&L effects are not yet separated, because nothing has been measured.

### 7. Capacity and dependencies

- **Live limit:** 0 live, with 3 proposed. Candidates to reach `g1` first are `ct-int-nonclient-drafting`, `sox-prereview-checklist` and `sox-report-register`, one per named owner role. A fourth, `sox-client-data-approval` stage 0, would wait. Review capacity is the real constraint: seniors are about 90-95% booked in busy season (reported).
- **Owner load:** the integrated-audit manager is the placeholder owner of five items (one in discover) and the validator of the four variants; the SOX/ICFR practice lead owns most of the SOX-only items.
- **Foundations other items wait on:** the checklist and the register are needed by the client-data approval, the listing tool and their variants.
- **Catalog:** an `enterprise-assistant` entry is requested (`overlay/tool-catalog.yaml`, `under-review`) and the risk tier is provisional. The policy is a draft.

## Part B · Decisions

To be recorded after the deciders meet. The deciders decide; this file records.

| Item | Decision | Reason | Resources or conditions | Next gate | Decided by |
|---|---|---|---|---|---|
| `sox-prereview-checklist` | | | | | |
| `sox-report-register` | | | | | |
| `sox-client-data-approval` | | | | | |
| `sox-request-template` | | | | | |
| `sox-listing-tool` | | | | | |
| `sox-junior-development` | | | | | |

Rebalance changes (weights, live limit, stage definitions): none yet. The live limit goes to the AI steering group.

## Actions

| Action | Owner (role) | Depends on |
|---|---|---|
| Take the live limit (proposed 3, with the review-capacity rationale) to the AI steering group; record the number in `settings.live_limit` once set | Portfolio lead (head of AI office) | Steering group meeting |
| Decide g0 on the six items above | Portfolio lead and Risk lead | This pack |
| Send this validation request to the integrated-audit manager (draft message): "Four integrated-audit items in the AI portfolio were drafted from a desk review, and nobody who does the work has checked them yet. Could you read each and tell us what is wrong or missing? (1) Written pre-review checklist for evidence gaps, `ct-int-precheck-checklist`. (2) Register of specialist-validated reports, `ct-int-validated-report-register`. (3) Tool to compare listings to active users and draft the workpaper, `ct-int-listing-compare-draft`. (4) AI secondary review of ITGC workpapers, `ct-int-ai-secondary-review`. For each one: does it describe how integrated-audit testing really works? Are the figures right (about 1.5 h hands-on per control test, one reported case with zero review notes, about 2 days in the senior queue)? Is it a distinct item, or the same as the SOX-only version? Which would you own? Please do not send client names or content. Your answers decide whether each item stays on its own or merges into its SOX-only counterpart." | Portfolio lead (head of AI office) | None |
| Confirm the back-test over past client files is permitted, as a condition on `sox-prereview-checklist` | Risk lead | `sox-prereview-checklist` g0 |
| Name the holder of the junior-workstream owner role (a senior manager) | SOX/ICFR practice lead | `sox-junior-development` g0 |
| Check the template, wording and time sample, and confirm the g1 criteria thresholds | Integrated-audit manager; gatekeepers | `ct-int-nonclient-drafting` g1 |
| Complete the `enterprise-assistant` catalog entry; confirm `tier-2` | IT/security lead; Risk lead | `ct-int-nonclient-drafting` g1 |

## Open questions

- Does the live limit count items with no AI? Assumed yes (all items in prototype, pilot or scale).
- Are the proposed outcomes for the SOX-only items still right once the risk lead has reviewed the draft policy's tiers?
- The integrated-audit variants may merge into their primaries after validation; if so, the register counts change.
- All value figures are ranges with a grade D basis (no published measure) except where an intake record says otherwise; none is measured.
