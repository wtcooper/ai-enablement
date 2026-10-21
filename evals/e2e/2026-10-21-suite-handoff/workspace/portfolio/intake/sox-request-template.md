# Intake: Request template naming the report and its parameters up front, plus a rule-based check when evidence arrives

| Field | Entry |
|---|---|
| Id | `sox-request-template` (the same id as in `portfolio.yaml`) |
| Submitted by | Practice lead, Audit, SOX-only outsourcing |
| Source | Advisor item: `units/sox-only-outsourcing/opportunities.yaml` → `sox-request-template` |
| Status | ready to screen (advisor category: park) |

## The problem in one sentence

Name the report and its parameters in the evidence request, with a rule check on arrival, so incomplete submissions bounce at once and waiting time falls.

## How often it happens

Up to about 42 tests a month could be affected (tracking sheet, as relayed; reported). Sample case: about 4 days waiting on the control owner plus about 2 days of rework (one case, reported). Last month's record not yet obtained.

## Class

business-automation. Proposed by the portfolio, to confirm at screen.

## Rules or AI

Templates first; a simple rule check on arrival. No AI needed. This is a process fix.

## Data

| Data needed | Where it lives | Owner (role) | Seen in its real state? |
|---|---|---|---|
| Per-client key-report list (does not exist yet; first step of `sox-report-register`) | Not yet recorded | Not yet named | no |

## Owner and benefit

- Owner who would lead the work: Practice lead
- Benefit owner in the business: not yet named
- Lever and metric it would move: quality → review-note rate; capacity → elapsed days per affected test (elapsed time, not staff hours)

## Early read

- Risk or regulatory exposure: control owners may ignore the template; the rule check may reject valid evidence.
- Build, buy or partner leaning: shared-team-skills; in-house
- Duplicates or near-duplicates elsewhere in the portfolio: none found as a pair. Overlaps `sox-prereview-checklist` and `sox-report-register` on the same evidence-completeness notes; do not add value. Depends on the report inventory from `sox-report-register`.
- Archetype evidence: assurance-controls-testing-03 (grade as recorded in the advisor's file)

## Screen result

Not yet screened. Revisit trigger carried from the advisor: the per-client key-report inventory exists. Link: `portfolio.yaml` → `sox-request-template`.
