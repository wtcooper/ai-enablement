# Intake: One specialist validates each key report once; a register records it for reuse across tests

| Field | Entry |
|---|---|
| Id | `sox-report-register` |
| Submitted by | ITGC senior manager (placeholder owner role), Audit: SOX-only outsourcing |
| Source | `units/sox-only-outsourcing/opportunities.yaml` → `sox-report-register` |
| Status | ready to screen |

## The problem in one sentence

Validate each key report once per client and record it for reuse, so that per-test re-proving of report completeness stops and evidence-completeness notes fall.

## How often it happens

About 100-126 of 210 tests a month rely on a system report (control share used as a proxy; reported). About 60 ITGC tests a month (tracking sheet, as relayed). About 8 distinct key reports and about 25 key controls per client, 15 clients (user estimates).

## Class

business-automation.

## Rules or AI

No AI is required (the plan says so). It is standardisation and a register. `ai_use: none`. Advisor values: `ladder: assist`, `runtime_class: shared-team-skills`. Kept because it is a big bet on the evidence-completeness notes and feeds `sox-listing-tool`.

## Data

| Data needed | Where it lives | Owner (role) | Seen in its real state? |
|---|---|---|---|
| Key reports per client | Client systems; not inventoried yet | ITGC senior manager with control owners | No |
| Validation records | Do not exist for this line; one integrated-audit case where the specialist validates once | ITGC senior manager | Reported, one case |
| A shared place for the register | To decide (no tool catalogue exists) | IT/security lead | No |

## Owner and benefit

- Owner who would lead the work: ITGC senior manager (the register owner and validator in the plan; a placeholder role).
- Benefit owner: not yet named.
- Lever and metric: capacity → staff hours per test; quality → note rate; risk → PCAOB ITGC comments.

## Early read

- Risk or regulatory exposure: AS 1215 documentation; AS 1105 reliability when reusing a validation across periods; AS 2605 notice to the clients' external auditors. Risk and quality must confirm that a senior manager on the ITGC side can sign a validation record.
- Build, buy or partner leaning: build in-house.
- Duplicates or near-duplicates elsewhere in the portfolio: `ct-int-validated-report-register` (integrated line, draft to validate) is the same pattern and is expected to be merged at roll-up. Overlaps `sox-prereview-checklist` and `sox-request-template` on the same notes.
- Archetype evidence: none recorded. The case rests on the integrated-audit contrast case (reported, n=1). Use case 06 (grade A) is context only.
- Human checkpoints: specialist signs each validation; senior confirms the listing is the validated report.
- AI use: none.
- Capacity choice: redeploy (advisor's); firm stance undecided.

## From the plan

- Process and prerequisites: reliability of information (IPE); validation capacity of one senior manager at about 4 h a week outside peak; a named owner for the register and re-validation triggers; methodology agreement on what must be recorded; a shared place for the register.
- Cost lines and who carries them (Case A): first-time validation 192-248 h for all 15 clients (first client 24 h, later 12-16 h each; reuse untested), at a blended USD 210 an hour = USD 40,320-52,080, counted as real cost because it displaces billable work. Stage 1 (4-5 clients) is 60-88 h = USD 12,600-18,480, about 15-22 weeks at 4 h a week. Re-validation cost not yet known. Register hosting: existing tools, to confirm. Case A total about 270-448 h.
- Comparison and go/no-go: stage 2 only if measured hours per later client are within 12-16 (or explained), the evidence-completeness note rate falls in these clients against their prior period with no rise in other notes or in re-performance disagreement, and risk and quality accept the records and the validator role.
- Assumptions to test first: key reports per client and hours per report; whether the integrated pattern is structural; whether the specialist group can supply 180-600 h.
- Steps: Now step 4, inventory key reports for the 4-5 stage-1 clients, validate the first and time it (ITGC senior manager). Next step 9, validate the others. Later step 16, remaining clients and a second validator. `next_step`: inventory, agree with risk and quality what a validation record must contain, validate the first client and time it.
- Control-plan rows: validation hours per client (24 first, 12-16 later); validations stale after a report or system change (zero relied on after a change without re-validation); monthly; ITGC senior manager.
- People steps: as `sox-prereview-checklist`. Concentration check: this owner also back-tests the checklist (about 6 h a week for the first 8 weeks).

## Screen result

Scores (value 4, feasibility 3, data readiness 3, risk 4, time to value 3, strategic fit 5) kept. Weighted 3.70; **value index 4.11, readiness index 3.36**. Category big bet (staged). Horizon medium. Full path. Risk tier: none (`ai_use: none`). Sponsor: Managing partner for assurance (placeholder). **Primary** for its merged idea; `ct-int-validated-report-register` is its variant.

**Proposed g0: pending the deciders (portfolio lead and risk lead).** Quadrant: high value, readiness just under 3.5, so Go with readiness work named as conditions.
- Resources a Go would name: ITGC senior manager about 4 h a week outside peak; stage 1 (4-5 clients) is 60-88 h, USD 12,600-18,480 at USD 210 an hour, counted as real cost because it displaces billable work. Released by the practice leader (time); finance lead to confirm that treatment and supply the staff rate; risk lead and IT/security lead release access to client reports.
- Conditions: risk and quality confirm that a senior manager on the ITGC side can sign a validation record and what a record contains; a named register owner and re-validation triggers; validate one client first and time it.
- Kill criteria (from Case A's stage 2 go/no-go): measured hours per later client outside 12-16 with no explanation; the evidence-completeness rate does not fall in the stage-1 clients against their prior period, or other notes or re-performance disagreement rise; risk and quality do not accept the records or the validator role.
- Open before any Go: live limit unset; the same person also runs the checklist back-test (about 6 h a week for 8 weeks).

## Next gate evidence

Filled after a Go.
