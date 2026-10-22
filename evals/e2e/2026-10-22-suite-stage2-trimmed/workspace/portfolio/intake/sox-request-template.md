# Intake: Request template naming the report and its parameters up front, plus a rule-based check when evidence arrives

| Field | Entry |
|---|---|
| Id | `sox-request-template` |
| Submitted by | SOX/ICFR practice lead (placeholder owner role), Audit: SOX-only outsourcing |
| Source | `units/sox-only-outsourcing/opportunities.yaml` → `sox-request-template` |
| Status | ready to screen (advisor category: park, with a revisit trigger) |

## The problem in one sentence

Help staff get the right report with the right parameters from control owners on the first request, so that days waiting and later review notes fall.

## How often it happens

Affected tests up to about 42 a month (of about 210; tracking sheet, as relayed). In the sample case, about 4 days waiting on the control owner plus about 2 days rework (reported, one case).

## Class

business-automation.

## Rules or AI

No AI needed: a template and a simple rule check on arrival (date range, report type, system-generated format). `ai_use: none`. Advisor values: `ladder: assist`, `runtime_class: shared-team-skills`.

## Data

| Data needed | Where it lives | Owner (role) | Seen in its real state? |
|---|---|---|---|
| Per-client list of key reports | Does not exist yet | SOX/ICFR practice lead with the client's control owner | No |
| Request-list wording | Practice's current request lists | SOX/ICFR practice lead | Not seen by the advisor |

## Owner and benefit

- Owner who would lead the work: SOX/ICFR practice lead (placeholder).
- Benefit owner in the business: not yet named.
- Lever and metric it would move: quality → review-note rate; capacity → elapsed days.

## Early read

- Risk or regulatory exposure: client-facing wording needs risk and quality approval; no client data in the template.
- Build, buy or partner leaning: build in-house.
- Duplicates or near-duplicates elsewhere in the portfolio: overlaps `sox-prereview-checklist` and `sox-report-register` on the same evidence notes. Do not add values. It depends on the report inventory that starts `sox-report-register`.
- Archetype evidence: assurance-controls-testing-03 (grade C).
- Human checkpoints: staff confirm every bounced item before chasing.
- AI use: none.
- Capacity choice: redeploy (advisor's); firm stance undecided, confirmed at `g3`.

## From the plan

- Process and prerequisites: evidence request (PBC) for report-based controls; agree the report list per client with the control owner; update request-list wording.
- Cost lines and who carries them (Case A): practice lead 16-40 h [placeholder; probably lower now that the back-test is separate].
- Comparison and go/no-go: staged start client by client; pilot compared with the same clients' prior period; the Case A go/no-go applies.
- Assumptions to test first: hours per note; share of notes that are request-driven.
- Steps: Next step 10, draft client by client as each inventory completes, test on the next two requests per client (practice lead; depends on the report inventory). `next_step`: once the inventory exists, draft revised wording for the access recertification control and test it on the next two requests; depends on `sox-report-register`.
- Control-plan row: wrong-first-time requests and days waiting (about 4 days baseline, one case); monthly; practice lead. If out of range: revise wording; check the report list with the control owner.
- People steps: as `sox-prereview-checklist`.

## Screen result

Scores (value 3, feasibility 5, data readiness 3, risk 5, time to value 5, strategic fit 4) kept. Weighted 4.00; **value index 3.44, readiness index 4.45**. Category park. Horizon near. Full path (client-facing wording). Sponsor: Managing partner for assurance (placeholder).

**Proposed g0: pending the deciders (portfolio lead and risk lead).** Quadrant: value below 3.5 with readiness above it; on the full path the default is Hold. Proposed **Hold**, `revisit_when`: the per-client key-report inventory exists for a client (the first step of `sox-report-register`). Not a stop: the plan starts it client by client as each inventory completes. Overlaps the checklist and the register on the same notes; do not add values.

## Next gate evidence

Filled after a Go.
