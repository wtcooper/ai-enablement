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

Not yet screened. Revisit trigger carried from the advisor: the checklist and register are in place with baselines and the client-data approval is granted. Link: `portfolio.yaml` → `sox-listing-tool`.
