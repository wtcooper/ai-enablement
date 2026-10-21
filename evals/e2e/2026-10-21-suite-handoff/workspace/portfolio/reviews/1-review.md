# Portfolio review 1

| | |
|---|---|
| Review number | 1 (previous: none) |
| Forum | Proposed, not yet agreed: Managing partner or chief operating officer, Practice leaders, Risk and quality partner, Head of IT, Finance lead, People lead, Head of AI |
| Prepared by | Head of AI (portfolio owner), drafted with the portfolio skill |
| Rebalance review? | No (first review; rebalance is proposed for every third review) |

**Status of this pack:** Part A is a draft for the portfolio owner to confirm. The recommendations are the portfolio office's drafts, labelled as such. The forum and the gatekeepers decide. Part B is empty until decisions are reported.

## At a glance: what needs a decision from you

| Group | Items | What is needed |
|---|---|---|
| **A. Ready to screen: a `g0` decision from you** | `sox-report-register`, `sox-client-data-approval`, `sox-request-template`, `sox-listing-tool` | Go, Hold, Kill or Recycle into discover. Options and a draft recommendation are in section 3 |
| **B. Cannot be screened yet: a precondition from you** | `sox-chase-assistant`, `sox-junior-development` (no owner) | Name an owner role, or leave in outline |
| **C. Cannot be screened yet: waiting on validation** | `ct-int-validated-report-register`, `ct-int-precheck-checklist`, `ct-int-nonclient-drafting`, `ct-int-listing-compare-draft`, `ct-int-ai-secondary-review` | The integrated-audit manager confirms the desk review; until then they stay outlines |
| **Already decided** | `sox-prereview-checklist` | `g0` Go taken on 2026-10-21; in discover; next gate `g1`, not yet due |

Nothing meets a surfacing rule for a stop, redirect or scale decision. No item has a kill criterion that can be met, an early warning, a due gate or a benefit under review. So this review is a first screen of the register, not a status hearing.

## Part A · Pack

### 1. Pipeline by stage

| Stage | Items | Change since review 0 |
|---|---|---|
| intake | 11 | +11 (imported from the two audit units) |
| discover | 1 | +1 (`sox-prereview-checklist`) |
| prototype | 0 | |
| pilot | 0 | |
| production | 0 | |
| scale | 0 | |
| retire | 0 | |
| Live (prototype, pilot, scale) against the live limit | 0 / not set | Live limit still to be agreed |

Of the 11 at intake: 4 are ready to screen and 7 are outlines (2 without an owner, 5 draft to validate). Enablement line (seat and licence roll-outs, tracked apart): none logged.

### 2. Gate results since the last review

| Item | Gate | Outcome | Reason in one line |
|---|---|---|---|
| `sox-prereview-checklist` | g0 | go | Value 4.33 and readiness 4.45 indexes; a process fix with no client data; the review-note rate is agreed with its benefit owner. Decided by the Head of AI outside a review. Sponsor and full gate path are assumptions; tier-1 is provisional |

### 3. Decisions asked of the forum

All four are `g0` screens (the item is ready but has not been screened). Scores are the advisor's, carried under the portfolio's weights; indexes use the default threshold of 3.5 on each axis (a proposed default, not a standard). Value ranges are the advisor's estimates on reported figures. Savings from the checklist, request template and register draw on the same pool of evidence-completeness notes: do not add them (combined ceiling about 20 points of the 30% note rate, per the advisor).

#### sox-report-register: One specialist validates each key report once; a register records it for reuse across tests

- **Ask:** `g0`. Go into discover, or Hold. Quadrant: value 4.11, readiness 3.36. The usual outcome is Go with the readiness work named as conditions.
- **Evidence for:**
  - Capacity: 25-63 staff hours a month, net of one-off specialist effort of about 180-600 hours; quality 3-10 points of the note rate (not additive); risk 0-2 PCAOB ITGC evidence comments avoided per cycle (advisor's file, `value`; Grade D).
  - About 100-126 of 210 tests a month rely on a system report (reported, control share as a proxy).
  - The integrated-audit line shows the pattern in one reported case; `ct-int-validated-report-register` would feed this register.
  - Unblocks `sox-request-template` and is a dependency of `sox-listing-tool`.
- **Evidence against:**
  - The 1.0 h gap between the 2.5 h and 1.5 h cases rests on two single cases, so the high end is capped at 0.5 h per test.
  - No archetype evidence is recorded (`evidence: []`).
  - Readiness is held down by feasibility 3, data readiness 3 and time to value 3.
  - Validation goes stale when a report or system changes.
  - Reuse across clients is untested.
- **Readiness work if Go (conditions):**
  - A named validator: the ITGC senior manager at about 4 hours a week outside peak, approved by the practice lead.
  - The risk and quality partner confirms that role can sign validation records.
  - A named owner for the register and for re-validation triggers.
  - Methodology agreement on what must be recorded under AS 1215.
  - A shared place for the register.
- **Kill criteria (proposed):**
  - Validating the first client takes more than 32 hours (top of the advisor's 16-32 h range).
  - The risk and quality partner will not accept a validation record signed by the ITGC senior manager role.
- **Resources if Go (to be released by the sponsor):** the validator's time and the practice lead's approval, with no tool spend. Stage 1 is scoped to inventorying the key reports for the 4-5 clients behind the ITGC controls and the two PCAOB comments, then validating the first client and timing it. Cost is real staff time: 24 h for the first client and 12-16 h for each later client as reports are reused (reuse untested), at a blended USD 210 an hour (advisor's file).
- **Early warnings:** none.
- **Options:**
  - Go into discover with the conditions above. This costs senior-manager time in the shoulder weeks and releases the report inventory that `sox-request-template` needs.
  - Hold until the checklist reaches `g1`, so one scarce senior group is not asked for two things at once. This releases that time and delays the inventory.
  - Recycle: merge with `ct-int-validated-report-register` into one firm-level register once the integrated line's manager confirms it.
- **Recommendation (portfolio office draft):** Go into discover, limited to stage 1, with the named validator and sign-off role as conditions. The seniors needed for the checklist are not the ITGC senior manager, so the two can run together. Check this with the practice lead before deciding.

#### sox-client-data-approval: Take one controls-testing use through the client-data approval path

- **Ask:** `g0`. Go into discover, Hold or Kill. Quadrant: value 2.56, readiness 3.36. The usual outcome is Kill or Hold with a revisit trigger. The advisor kept it as a foundation by the user's decision because it is the lead-time item for any client-data tool.
- **Evidence for:**
  - No controls-testing case has gone through the 3-4 month path (security review, retention assessment, independence check) (advisor's file, `description`).
  - Every client-data tool option depends on it.
  - No standalone value: the advisor records `low: 0, high: 0` as an enabler.
- **Evidence against:**
  - Value 2: nothing is delivered until a tool exists.
  - Approval may take longer than 3-4 months, or the scope may be too broad to approve.
  - The practice lead cannot decide it alone: risk and quality, the CIO and general counsel sign off.
  - `depends_on` lists `sox-prereview-checklist` and the prerequisite is written test attributes, but the advisor's `next_step` has no dependency and says to open the request now. **The advisor's file is inconsistent on whether this must wait for the checklist.**
- **Kill criteria (proposed):** the CIO, general counsel or risk and quality will not accept a narrow scope (access recertification listing comparison, one or two clients) for a request.
- **Resources if Go:** the practice lead's time to prepare the request pack, plus sponsor support from the managing partner for assurance. No spend recorded.
- **Early warnings:** none.
- **Options:**
  - Go into discover now, preparing the narrow request pack while the checklist is co-written, because the lead time is long. This costs practice-lead time and releases the approval clock.
  - Hold behind the checklist's `g1`, so the request carries real written attributes. This saves effort and adds to the lead time.
  - Kill: choose not to pursue client-data tools. This releases the effort and closes the path to `sox-listing-tool` and `ct-int-listing-compare-draft`.
- **Recommendation (portfolio office draft):** Go into discover, scoped to the narrow request. Open one request only: `ct-int-listing-compare-draft` also lists "start the approval request" as its next step. Confirm with the risk and quality partner whether a request without written attributes would be accepted.

#### sox-request-template: Request template naming the report and its parameters, plus a rule check on arrival

- **Ask:** `g0`. Quadrant: value 3.44, readiness 4.45. The usual outcome for lower-value but cheap items is Go only on the light path, otherwise Hold. The advisor parked it because the per-client report list does not exist yet.
- **Evidence for:** quality 2-6 points (a subset of the same notes; not additive) and 0-2 elapsed days saved per affected test (about 4 days waiting plus 2 days of rework on the sample case: reported, one case). Needs no AI; templates first.
- **Evidence against:** it needs the report inventory from `sox-report-register` first. It overlaps the checklist and the register on the same notes. Value 3 (Grade D).
- **Kill criteria:** none proposed; it is on hold.
- **Early warnings:** none.
- **Options:**
  - Hold, with the advisor's trigger: the per-client key-report inventory exists. This costs nothing and releases no effort.
  - Go into discover now. It could only start for a client whose inventory is complete, which is none yet.
- **Recommendation (portfolio office draft):** Hold with `revisit_when` set to the advisor's trigger.

#### sox-listing-tool: Certified tool for portal pull, listing comparison and workpaper first pass

- **Ask:** `g0`. Quadrant: value 2.11, readiness 2.36. The usual outcome is Kill, or Hold with a revisit trigger. The advisor parked it.
- **Evidence for:** capacity 24-126 staff hours a month at full coverage (a guess; near zero for the first approved scope). The pattern evidence is self-reported by the deploying teams (advisor's file, Grade C for this practice).
- **Evidence against:**
  - It depends on four items: the checklist, the register, the client-data approval and the junior-development workstream.
  - It speeds the staff step, not the senior-review constraint (seniors are 90-95% booked), so its value counts only when the checklist and register are in place.
  - Client data is not approved for any AI tool.
  - Rules-or-AI check not recorded: a rule-based comparison may do the listing match.
  - Added review lands on seniors and is not netted.
- **Kill criteria:** none proposed; it is on hold.
- **Early warnings:** none.
- **Options:**
  - Hold with the advisor's trigger: the checklist and register are in place with baselines and the client-data approval is granted.
  - Kill: a rules-first approach may remove the need for it. This releases effort and leaves the integrated-audit twin on its own.
  - Recycle: merge with `ct-int-listing-compare-draft` into one firm-level listing-comparison item, so the two are scored once.
- **Recommendation (portfolio office draft):** Hold with the advisor's trigger, and merge with its integrated-audit twin when that is confirmed.

### Not ready to screen (no decision asked, but a precondition from you)

| Item | Scores (weighted, value, readiness) | What blocks screening | What is needed |
|---|---|---|---|
| `sox-junior-development` | 3.35, 2.56, 4.00 | No owner (a senior manager role "to be named") | Name an owner role. `sox-listing-tool` and the checklist's follow-on work depend on it. The advisor kept it as a foundation by the user's decision; under its own rules it would be park (value 2) |
| `sox-chase-assistant` | 3.15, 2.44, 3.73 | No owner; no measure of chasing time | Name an owner or leave it in outline. It depends on `sox-request-template`, which is on hold |
| `ct-int-validated-report-register` | 3.90, 4.11, 3.73 | Draft to validate (desk review only) | The integrated-audit manager confirms; the advisor's next step is to ask the specialist how validation is recorded today. Screen together with `sox-report-register` |
| `ct-int-precheck-checklist` | 4.15, 3.44, 4.73 | Draft to validate | Same confirmation. Its note rate is already a second measure on the checklist's `g0` |
| `ct-int-nonclient-drafting` | 3.70, 2.44, 4.73 | Draft to validate | Same confirmation. Value 2.44 is below the line; this is an assistant routine on non-client material |
| `ct-int-listing-compare-draft` | 2.95, 3.67, 2.36 | Draft to validate | Same confirmation. Pair with `sox-listing-tool` |
| `ct-int-ai-secondary-review` | 2.35, 2.78, 2.00 | Draft to validate | Same confirmation. Lowest readiness in the register. Its `speed` lever is not one of the firm's five levers |

### 4. Early-warning flags

None. No item has a next gate due or a kill criterion that can be met yet.

### 5. Balance

| View | Now | Comment |
|---|---|---|
| Horizon: near, medium, long | near 1; the other 11 unset | Horizon is set at screen. Not a finding yet |
| Class: individual-productivity, business-automation, new-value | 3 / 9 / 0 | No new-value item. The classes are the portfolio's proposals, to confirm at screen |
| Category: quick win, foundation, big bet, park | 3 / 4 / 1 / 4 | Advisor's categories, carried as they stand. Foundations are a third of the register |
| Levers covered | capacity, quality, risk, experience | **Margin (weight 0.10) has no item.** `ct-int-ai-secondary-review` uses `speed`, which the firm does not use |
| Units and functions | Audit only: SOX-only 7, integrated 5; service delivery 11, risk and compliance 1 | **Three duplicate pairs** (checklists, registers, listing tools). Counted as 12 items but about 9 distinct ideas. Tax and advisory not yet in |
| Run cost and cost constraints | Not recorded for any tool | No tool has a run-cost range. The only cost recorded is staff time: specialist validation of about 180-600 hours one-off (user estimate), 24 h for the first client and 12-16 h for each later client (advisor's file) |

Two other points. Roughly 5 of the 12 items need no AI at all (the checklists, the request template, the registers and the approval). And the register as it stands is audit only, so the comparison is of audit items against each other, not against the firm's other practices.

### 6. Benefits: forecast versus realised

No benefit rows exist yet. They are due before `g3`, and no item is near it. The forecasts below are item-level ranges, not realised value.

| Item | Benefit | Forecast (range) | Realised so far | Status | Counterfactual |
|---|---|---|---|---|---|
| `sox-prereview-checklist` | Review-note rate | 5-12 points off a 30% rate (Grade D; the 30% is reported and must be replaced by a record) | none | forecast | Not yet set |
| `sox-prereview-checklist` | Second-round senior reviews | 10-25 avoided a month | none | forecast | Not yet set |
| `sox-report-register` | Staff hours | 25-63 a month net of one-off effort (Grade D) | none | forecast | Not yet set |

Portfolio measures: items with a benefit owner 1 of 12; items reviewed after go-live 0 of 0; benefit success rate not applicable. Use-case effects only; no enterprise P&L effect is claimed. The capacity choice (redeploy or reduce) is `undecided` at firm level, so none of these hours has a recorded destination.

### 7. Capacity and dependencies

- **Scarce reviewers.** Seniors are 90-95% booked in busy season. The checklist, the register, the junior workstream and the listing tools all draw on the same seniors and the ITGC senior manager. The live limit is still unset.
- **Order of dependencies.**
  1. The checklist.
  2. The register and the approval.
  3. The request template.
  4. The junior workstream.
  5. The listing tools.
  6. Secondary review.
- **One approval, two requests.** `sox-client-data-approval` and `ct-int-listing-compare-draft` both say they open the approval request. It should be one.
- **Inventory and decommissioning.** No inventory of AI already in use and no decommissioning route exist yet. Needed before anything reaches production.

## Part B · Decisions

Recorded as reported by the Head of AI. Three of four `g0` decisions taken; one left open.

| Item | Decision | Reason | Resources or conditions | Next gate | Decided by |
|---|---|---|---|---|---|
| `sox-report-register` | Go into discover, limited to stage 1 | Value index 4.11, readiness 3.36: a Go with readiness work as conditions; unblocks the request template and the listing tools | ITGC-side senior manager (role to be named) at about 4 h a week outside peak, approved by the practice lead; no tool spend. Conditions: named validator and register owner; risk and quality confirms who can sign a validation record; AS 1215 record content agreed; shared place for the register; stage 1 only | g1 (practice leaders, risk and quality partner, proposed) | Head of AI |
| `sox-client-data-approval` | Go into discover, scoped to one narrow request | Foundation and lead-time item; every client-data tool depends on it | Practice lead's time, sponsor the managing partner for assurance (assumed); the request itself is decided by risk and quality, the CIO and general counsel. Conditions: **one approval request only**, owned by this item (the integrated-audit listing tool and the SOX-only listing tool attach to it and do not open their own); check with risk and quality whether a request without the checklist's written attributes is acceptable | g1 (same gatekeepers, proposed) | Head of AI |
| `sox-request-template` | Hold | Report list does not exist; depends on the register's inventory | None. Revisit when the per-client key-report inventory exists | none until revisited | Head of AI |
| `sox-listing-tool` | **No decision taken** | The portfolio owner will not decide until the integrated-audit twin is confirmed, and that confirmation is not theirs to give | Open question below. Stays at intake, status active | g0 | n/a |

All three decisions carry these caveats: sponsor and full gate path are assumptions until the forum agrees them, and the risk tiers (tier-2 for the register, tier-1 for the approval and the template) are provisional until ai-governance confirms them.

Rebalance changes (weights, live limit, stage definitions): none.

## Actions

| Action | Owner (role) | Depends on |
|---|---|---|
| ~~Take the four `g0` decisions above~~ Three taken; `sox-listing-tool` remains open | Head of AI | The integrated-audit twin's confirmation |
| Name the ITGC-side validator and the register owner; get the risk and quality partner's view on who can sign a validation record | SOX/ICFR practice leader | `sox-report-register` at `g1` |
| Prepare the single narrow approval request; ask risk and quality whether it can go ahead before the checklist's attributes are written | Practice lead | `sox-client-data-approval` at `g1` |
| Tell the integrated-audit manager that `ct-int-listing-compare-draft` does not open its own approval request | Head of AI | |
| Name an owner role for `sox-junior-development` and `sox-chase-assistant`, or leave them in outline | Head of AI with the SOX/ICFR practice leader | |
| Ask the integrated-audit manager to confirm or correct the five desk-review items | Head of AI | |
| Agree the live limit, the forum membership, the gate paths and the gatekeepers | Head of AI with the managing partner or chief operating officer | |
| Replace the reported 30% note rate and the 42-a-month figure with tracking-sheet records, for both lines | SOX/ICFR practice leader | `sox-prereview-checklist` at `g1` |
| Confirm the provisional risk tier and whether the independence check applies to the checklist | Risk and quality partner, with ai-governance | `sox-prereview-checklist` at `g1` |
| Settle the firm-level capacity stance | Managing partner or chief operating officer, with the Head of AI | Any item approaching `g3` |
| Bring tax and advisory ideas through intake so audit is not the whole portfolio | Head of AI | |

## Open questions

- **`sox-listing-tool`: who confirms the integrated-audit twin?** The Hold I drafted is on the advisor's trigger and does not itself depend on the twin; only the proposed merge does. The owner chose not to take the decision until the twin is confirmed. Needs the integrated-audit manager (or the practice lead) to confirm `ct-int-listing-compare-draft`, or the owner to take the Hold on its own.
- Does the register measure the same thing across the SOX-only and integrated lines? Value is in different units (percentage points, hours a month, hours per test, days).
- Does a request without written attributes get accepted by the CIO, general counsel and risk and quality?
- Can a rule-based comparison do the listing match, making the AI tool unnecessary?
- Should process fixes that need no AI stay in the firm's AI register?
- Who decides `g0` on the full path? The light path (where the portfolio owner decides alone) is not yet agreed.
- Is the 25% kill criterion on the checklist the right line? It is the low end of the advisor's own assumption, not a tested figure.
