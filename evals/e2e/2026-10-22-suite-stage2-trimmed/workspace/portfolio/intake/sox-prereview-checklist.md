# Intake: Written pre-review evidence checklist that captures the senior's unwritten checks

| Field | Entry |
|---|---|
| Id | `sox-prereview-checklist` |
| Submitted by | SOX/ICFR practice lead (placeholder owner role), Audit: SOX-only outsourcing |
| Source | `units/sox-only-outsourcing/opportunities.yaml` → `sox-prereview-checklist` |
| Status | ready to screen |

## The problem in one sentence

Help SOX-only staff catch evidence-completeness gaps before senior review with a written self-check of the seniors' unwritten checks, so that the review-note rate (about 30% today, reported) falls.

## How often it happens

About 210 control tests last month, about 60 ITGC; about 42 tests (about 20% of all) drew an evidence-completeness or IPE note. From record: tracking sheet, as relayed. The advisor has not seen the sheet.

## Class

business-automation (the flow of review changes).

## Rules or AI

No AI needed. A written checklist does it. The advisor allows AI only to draft wording on non-client material. `ai_use: none`. Advisor values: `ladder: assist`, `runtime_class: shared-team-skills`.

## Data

| Data needed | Where it lives | Owner (role) | Seen in its real state? |
|---|---|---|---|
| Tracking sheet (tests, notes, note types) | Practice's tracking sheet | SOX/ICFR practice lead | Relayed; not seen by the advisor |
| Past files with known notes | Workpaper archive | Risk lead holds the PCAOB comment details | No |
| Seniors' unwritten checks | Seniors' heads | Seniors | Stated: listing from the system, full period, complete population |

## Owner and benefit

- Owner who would lead the work: SOX/ICFR practice lead (placeholder).
- Benefit owner in the business: not yet named.
- Lever and metric it would move: quality → review-note rate; capacity → second-round senior reviews avoided.

## Early read

- Risk or regulatory exposure: PCAOB-facing documentation; the methodology owner approves the checklist. No client data.
- Build, buy or partner leaning: build in-house (a document).
- Duplicates or near-duplicates elsewhere in the portfolio: `ct-int-precheck-checklist` is the same idea for the integrated line (draft to validate). The advisor plan intends to merge them into one parent with `rolled_up_from` at roll-up. Overlap with `sox-request-template` and `sox-report-register`: do not add their quality values.
- Archetype evidence: assurance-controls-testing-03 (grade C); assurance-controls-testing-10 (grade B).
- Human checkpoints: senior samples checklist completions and reviews every exception.
- AI use: none (rules or a template are enough).
- Capacity choice: redeploy (advisor's). The firm's `capacity_stance` is still undecided; the choice is confirmed at `g3`.

## From the plan

- Process and prerequisites (Prioritize, item list): test of operating effectiveness; two seniors articulate the checks; methodology owner approves.
- Cost lines and who carries them (Case A): senior time to write and test, 6-24 h (practice lead holds the half-days); checklist back-test by the ITGC senior manager, 2 h a week for 8 weeks = 16 h, budgeted separately; training 20-60 h [placeholder]; parallel run 20-60 h [placeholder]. Case A total about 270-448 h for the whole package, mostly report validation.
- Comparison and go/no-go (Case A, How we will know): a blind back-test on past files, then a staggered start against other clients. Proposed: back-test catches at least half of the evidence notes on at least ten past files; the evidence-completeness rate falls at least 5 points with no rise in other note types or in re-performance disagreement.
- Assumptions to test first: share of notes the checklist catches; hours per note and per second-round review; which notes count as completeness.
- Steps (Plan, Now / Next): Now step 1, schedule and hold 2-3 protected senior half-days in the shoulder weeks and co-write the checklist with two seniors (practice lead); Next step 8, freeze it and run the blind back-test (ITGC senior manager); step 11 pilot on stage-1 clients. `next_step`: schedule the half-days and co-write the checklist, then the ITGC senior manager back-tests on past files, blind to the PCAOB comment text. Depends on nothing.
- Control-plan row: evidence-completeness note rate (about 20% baseline; range set after four weeks; monthly; practice lead); back-test catch rate (gate: at least half on at least ten files). If out of range: check use on a sample, revise wording, do not widen.
- People steps: managers align on one answer to "Is my job safe?", then the practice lead's note goes to all 40 people the week before the checklist work starts. No headcount reduction and no change in junior hiring pace is planned (user); this is not a commitment on fees.

## Screen result

Scores (value 4, feasibility 5, data readiness 3, risk 5, time to value 5, strategic fit 5) copied from the advisor and kept: the portfolio weights equal the plan's. Weighted 4.40; **value index 4.33, readiness index 4.45**. Category foundation (checklist is a dependency of `sox-client-data-approval`, `sox-listing-tool` and the not-yet-imported junior workstream). Horizon near. Full path (back-test uses past client files; risk and quality approve it). Risk tier: none (`ai_use: none`). Sponsor: Managing partner for assurance (placeholder). **Primary** for its merged idea; `ct-int-precheck-checklist` is its variant.

**Proposed g0: pending the deciders (portfolio lead and risk lead).** Quadrant: Go to discover.
- Resources a Go would name: SOX/ICFR practice lead holds 2-3 protected senior half-days in the shoulder weeks (6-24 h); ITGC senior manager 16 h for the blind back-test; risk lead releases past files and holds the PCAOB comment details. No budget line beyond time. Released by the practice leader (time) and the risk lead (files).
- Kill criteria (from Case A's go/no-go): the back-test would have caught fewer than half of the evidence notes on at least ten past files; or, in the pilot, the evidence-completeness rate falls by less than 5 points, or other note types or re-performance disagreement rise. The plan says revise before widening; the forum may prefer a stop after one revision.
- Open before any Go: the live limit is unset; seniors are 90-95% booked in busy season and the same ITGC senior manager also carries the report register.

## Next gate evidence

Filled after a Go.

## Build-or-buy framing (DRAFT pre-read for the g0 meeting)

**Draft, 2026-10-21. Not a solution brief; no `solutions/` folder is opened.** This is for the portfolio lead and the risk lead to react to. It records options and a leaning; the deciders decide. Figures are the practice lead's reported ones, relayed, and the advisor has not seen the tracking sheet.

**What the g0 meeting decides.** Whether to release discover resources for this item (people's time and access to past files). It is not a decision to buy or build software, because the item needs no AI (`ai_use: none`).

**Options**

| Option | What it is | For | Against |
|---|---|---|---|
| A. Build in-house | Seniors and the practice lead write the checklist in their protected half-days; the ITGC senior manager back-tests it blind on past files | Fits the practice's own unwritten checks; cheapest (6-24 h of senior time plus 16 h back-test); no client-data tool, no vendor approval; moves the note rate fastest | Uses scarce senior time; may go stale; the criteria are still tacit (data readiness 3) |
| B. Configure the existing audit platform to carry it | Host the checklist as a workpaper step or template in the platform the practice already uses | Staff meet it where they work; completion can be counted | Whether the platform can do this is unknown; may need a configuration approval; the platform's analytics module is used mainly for sampling today (reported) |
| C. Use the enterprise assistant to draft wording | Draft or tidy checklist wording on non-client material only | Saves some drafting time | Small gain; the senior judgment is the work, not the wording; keep to non-client material |
| D. Buy an external checklist or methodology pack | A generic third-party checklist | Quick to obtain | Cannot hold this practice's unwritten checks, which is the point; no catalogue entry exists; named products are for the firm's tool catalogue, not this document |
| E. Do nothing | Senior review continues to catch gaps late | No cost | The 30% note rate, second-round reviews and the PCAOB exposure continue |

**Leaning (for the deciders to confirm or change): A, with B as a later question and C only as an optional aid.** Reason: the value sits in writing down tacit checks, which only the seniors can do; a bought pack would miss them. Runtime class: none; if option C is used, `personal-assistant` under the existing usage rule.

**What discover would settle**
- the written definitions of control test, review-note rate, hands-on time and elapsed time, tested by two people classifying the same ten notes
- a timed sample of about ten tests (hands-on hours, senior review hours per file and per second-round review) to replace the placeholders
- the back-test protocol agreed with the risk lead, frozen before anyone reads the PCAOB comment text
- where the checklist will live (document or platform) and who approves it (methodology owner)
- the benefit owner and the metric they watch

**Evidence so far.** No controls-specific published measure of a checklist effect exists. Related archetype use cases: assurance-controls-testing-03 (evidence_grade C) and assurance-controls-testing-10 (evidence_grade B); neither is a measure of this checklist. The value range (5-12 points off the note rate) is the plan's illustrative arithmetic, grade D, on reported figures. The note pool of about 42 tests a month is the tracking sheet as relayed.

**Governance (assumptions for the risk lead to correct).** No AI tool touches client data, so no vendor or client-data approval is needed for A. The back-test reads past client files inside the firm; the risk lead should confirm that is permitted under the engagement terms and how the PCAOB comment details are kept apart. Proposed risk tier: none for A, `tier-2` at most for C (see the draft policy, `overlay/policy.md`).

**Resources a Go would name** (from the screen result): SOX/ICFR practice lead holds 2-3 protected senior half-days (6-24 h); ITGC senior manager 16 h for the back-test; risk lead releases past files. No budget line beyond time. The same ITGC senior manager also carries the report register, and seniors are 90-95% booked in busy season.

**Questions for the meeting**
1. What is the live limit, given the owners and review capacity in the room?
2. Who is the benefit owner, and is the review-note rate the measure they watch?
3. Can the practice lead hold the protected half-days, and is a stop after one failed revision acceptable, or should the plan's "revise before widening" stand?
4. Does the risk lead accept the back-test protocol and the handling of the PCAOB comment details?
5. The integrated-audit variant (`ct-int-precheck-checklist`) is provisional: should the integrated-audit manager validate it before or alongside this item's discover stage?
6. Capacity: redeploy is the advisor's choice for this item; the firm-wide stance is still open.

## Draft agenda for the g0 meeting (portfolio lead and risk lead)

**Draft.** Order follows dependency: the live limit and the tiers come first because they bound what the checklist decision can be. Each topic ends in a recorded outcome or a named open question. Papers: `portfolio/portfolio.yaml`, this record, `overlay/policy.md` (draft risk tiers, section 4).

1. **Live limit.** Set `settings.live_limit` as a number from real figures: how many owners and how much review capacity exist. Note that the ITGC senior manager and the seniors are shared by the checklist and the report register. *Outcome: a number, or a named open question.*
2. **Draft risk tiers.** The risk lead corrects the four assumed regimes (attest independence and PCAOB, US tax-return consent, client engagement-letter restrictions, personal-data law), the tier definitions, the not-permitted list and the proposed tier per portfolio item. Open questions 1 to 6 in the policy draft are the starting list; the engagement-letter list and counsel's view on consent are the likely follow-ups. *Outcome: corrections recorded; tiers then written into the portfolio items' `risk_tier`.*
   > **Note: the draft is not settled.** The regimes and the policy, catalog and other owners in `overlay/policy.md` are assumptions supplied by the portfolio lead, not confirmed by the risk lead or counsel. The risk lead is asked to correct them. Until then the tiers are a starting point only, and no portfolio item carries a `risk_tier`.
3. **Checklist decision (`sox-prereview-checklist`, `g0`).** Walk the build-or-buy pre-read above, then the six questions. Deciders: portfolio lead and risk lead. Options: Go to discover (with the named resources, conditions and kill criteria), Hold, Recycle or Kill. *Outcome: one recorded outcome with reason, evidence and, for a Go, resources and the next gate's evidence.*
4. **Chase assistant Hold (`sox-chase-assistant`).** Note the `g0` Hold recorded by the portfolio lead (light path) and its revisit trigger. Confirm the proposed `tier-3` for client-facing drafts, and whether the sender counts as the named reviewer. *Outcome: noted; tier confirmed or changed.*

If time allows, the other full-route items still pending `g0`: `sox-report-register` (proposed Go with conditions), `sox-request-template`, `sox-client-data-approval` and `sox-listing-tool` (proposed Holds, with the stage 0 exception for the approval request). The integrated-audit items stay provisional until the integrated-audit manager has validated them.
