# Intake: Certified tool for portal pull, listing-to-active-user comparison and workpaper first pass; every flagged exception and a sample of unflagged items go to a person

| Field | Entry |
|---|---|
| Id | `sox-listing-tool` (the same id as in `portfolio.yaml`) |
| Submitted by | Practice lead, Audit, SOX-only outsourcing |
| Source | Advisor item: `units/sox-only-outsourcing/opportunities.yaml` → `sox-listing-tool` |
| Status | ready to screen (advisor category: park) |

## The problem in one sentence

Use a certified tool for portal pull, listing-to-active-user comparison and workpaper first pass, so staff hours per report-based test fall while a person reviews every flagged exception.

## How often it happens

About 210 tests a month; 30-60% coverage (63-126 tests) is a guess, not measured. The sample case took about 2.5 hours of hand work (reported, one case). Last month's record not yet obtained.

## Class

business-automation. Proposed by the portfolio, to confirm at screen.

## Rules or AI

Not recorded as checked in the advisor's file. A rule-based comparison may cover much of the listing match; test this before treating it as an AI item.

## Data

| Data needed | Where it lives | Owner (role) | Seen in its real state? |
|---|---|---|---|
| Client listings and active-user lists via the client portal | Client systems | Not yet named | no. Client data is not yet approved for any AI tool |

## Owner and benefit

- Owner who would lead the work: Practice lead (approval); ITGC senior manager (shadow results)
- Benefit owner in the business: not yet named
- Lever and metric it would move: capacity → staff hours per month (value near zero for the first approved scope until widened)

## Early read

- Risk or regulatory exposure: automation bias and rubber-stamp review; non-repeatable outputs; documentation not defensible to the PCAOB (AS 1215); added review lands on seniors, who are the constraint. Reliance on others' work (AS 2605) needs early notice.
- Build, buy or partner leaning: workflow-automation class; not decided
- Duplicates or near-duplicates elsewhere in the portfolio: `ct-int-listing-compare-draft`, the same comparison tool in the integrated-audit line; both wait on the same approval (`sox-client-data-approval`). Do not add the two items' value. Depends on `sox-prereview-checklist`, `sox-report-register`, `sox-client-data-approval` and `sox-junior-development`.
- Archetype evidence: assurance-controls-testing-06, assurance-controls-testing-07, assurance-controls-testing-05 (grades as recorded in the advisor's file; pattern evidence is self-reported by the deploying teams)

## Screen result

**DRAFT g0 Hold for the portfolio owner to take on its own. Not a recorded decision; nothing in `decisions` yet.** Review 1 left this item open.

Scores carried from the advisor's file under the portfolio's weights: weighted 2.25, value index 2.11, readiness index 2.36. Quadrant: both axes below 3.5, so the usual outcome is Kill or Hold with a revisit trigger.

| Field | Draft |
|---|---|
| Category / horizon | park (advisor's category) / long (proposed; time to value is scored 1 and four items come first) |
| Risk tier | tier-4, provisional: it would produce attest evidence from client data on a delegated-to-tool first pass. ai-governance to confirm |
| Gate path | full (assumption until the forum agrees the gate paths) |
| Sponsor | SOX/ICFR practice leader (assumption until the forum agrees). Not needed to hold |

**Draft decision: Hold**, resting on the advisor's trigger only.
- **Reason:** it depends on four items that are not yet in place (the checklist, the register, the client-data approval and the junior-development workstream). It speeds the staff step, not the senior-review constraint, so its value counts only once the checklist and register are in place. Client data is not approved for any AI tool.
- **Evidence:** advisor's file for the item (capacity 24-126 staff hours a month at full coverage, a guess; near zero for the first approved scope; pattern evidence self-reported by the deploying teams; Grade C for this practice); review 1 pack, decision block for `sox-listing-tool`.
- **Resources:** none; a Hold releases nothing.
- **`revisit_when`:** "Options 1 and 4 are in place with baselines, and the client-data approval (sox-client-data-approval) is granted" (the advisor's trigger, unchanged).
- **Next gate:** none while held.
- **Recycle or kill:** not proposed.

**Open question, not part of this decision:** whether to merge this item with `ct-int-listing-compare-draft` into one firm-level listing-comparison item. That waits for the integrated-audit manager to confirm the twin. Until then the two stay separate and their value is not added.

**Rules-or-AI check still to do** before it is revisited: a rule-based comparison may cover much of the listing match.

Link: `portfolio.yaml` → `sox-listing-tool`.
