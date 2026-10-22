# Intake: Certified tool for portal pull, listing comparison and workpaper first pass

| Field | Entry |
|---|---|
| Id | `sox-listing-tool` |
| Submitted by | SOX/ICFR practice lead (placeholder owner role), Audit: SOX-only outsourcing |
| Source | `units/sox-only-outsourcing/opportunities.yaml` → `sox-listing-tool` |
| Status | ready to screen (advisor category: park until its dependencies are met) |

## The problem in one sentence

Have an approved tool pull listings, compare them to the active-user population and draft the workpaper first pass, with every flagged exception and a sample of unflagged items going to a person, so that staff hands-on time per ITGC test (about 2.5 h on the sample case) falls.

## How often it happens

About 60 ITGC tests a month of about 210 (tracking sheet, as relayed); coverage of 30-60% of tests is a guess, not measured.

## Class

business-automation.

## Rules or AI

Part of this is deterministic matching that a scripted workflow could do. The advisor chose `workflow-automation` with an AI draft. The rules-or-AI split should be tested again at discover.

## Data

| Data needed | Where it lives | Owner (role) | Seen in its real state? |
|---|---|---|---|
| Client user listings and reviewer sign-offs | Client portals | Client control owners; IT/security lead for access | No; needs the client-data approval |
| Past tests with planted exceptions for shadow mode | Workpaper archive | SOX/ICFR practice lead | No |

## Owner and benefit

- Owner who would lead the work: SOX/ICFR practice lead (placeholder); ITGC senior manager owns shadow results.
- Benefit owner: not yet named.
- Lever and metric: capacity → staff hours per test.

## Early read

- Risk or regulatory exposure: high. Client data, AS 1215 documentation, AS 2605 reliance, automation bias. Full route.
- Build, buy or partner leaning: not decided; no tool catalogue, so described by runtime class.
- Duplicates or near-duplicates elsewhere in the portfolio: `ct-int-listing-compare-draft` is the same tool for the integrated line. One tool should serve both, so evaluate once. Values must not be added. Overlaps `sox-report-register` on the same tests.
- Archetype evidence: assurance-controls-testing-06 (grade A); assurance-controls-testing-07 (grade B); assurance-controls-testing-05 (grade A). Use case 06 is one company's in-house internal audit agent with self-reported effort figures; it is not access recertification at an audit firm. Case 05 is a target picture only.
- Human checkpoints: as in the register entry.
- AI use: AI in scope.
- Capacity choice: redeploy (advisor's); firm stance undecided.

## From the plan

- Process and prerequisites: written attributes and exception rules; parallel run and old-versus-new comparison; AS 1215 documentation; external auditor told in advance.
- Cost lines and who carries them (Case C): known cost about 80-180 h [placeholder]; licence, consumption and firm-side review effort unknown, so no payback range is given.
- Comparison and go/no-go: shadow mode on past tests with planted exceptions, then old-versus-new on the same controls. Each stage's go/no-go is set with risk and quality first (proposed: no missed planted exception that a person would have caught).
- Assumptions to test first: approval time and scope; control types covered; hours saved net of review; whether clients' external auditors accept the work.
- Steps: Later step 18, shadow mode only once approval is granted and the checklist, register and junior workstream are in place. `next_step` as in the advisor file.
- Control-plan row: see `sox-client-data-approval`.
- People steps: as `sox-prereview-checklist`; juniors keep a rotating manual sample.
- **Dependency:** the plan also depends on `sox-junior-development`, now in the register (imported 2026-10-22 after the advisor skill quoted its title; screen result pending the deciders).

## Screen result

Scores (value 2, feasibility 2, data readiness 2, risk 3, time to value 1, strategic fit 3) kept. Weighted 2.25; **value index 2.11, readiness index 2.36**. Category park (the constraint gate caps value: it speeds a staff step, not the senior queue). Horizon long. Full path. Risk tier: not set (ai-governance). Sponsor: Managing partner for assurance (placeholder). **Primary** for its merged idea; `ct-int-listing-compare-draft` is its variant.

**Proposed g0: pending the deciders (portfolio lead and risk lead).** Quadrant: both indexes low. Proposed **Hold**, `revisit_when`: `sox-prereview-checklist` and `sox-report-register` are in place with baselines and `sox-client-data-approval` is granted. Depends on `sox-junior-development`, now in the register.

## Next gate evidence

Filled after a Go.
