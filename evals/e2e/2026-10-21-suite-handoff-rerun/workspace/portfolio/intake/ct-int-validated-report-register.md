# Intake: Register of specialist-validated reports, reusable across engagements and lent to the SOX-only line

| Field | Entry |
|---|---|
| Id | `ct-int-validated-report-register` |
| Submitted by | Integrated-audit manager (placeholder owner role), Audit: integrated audit ICFR testing |
| Source | `units/integrated-audit/opportunities.yaml` → `ct-int-validated-report-register` |
| Status | **Draft to validate.** Outline until an integrated-audit manager has reviewed it. |

## The problem in one sentence

Record the reports a specialist has already validated, with parameters and re-validation triggers, so that staff reuse them across engagements and the SOX-only line, and per-test re-proving of report completeness stops.

## How often it happens

Not known. One reported case (about 1.5 h hands-on, no notes, 2-day senior queue). The desk review's validation list asks for the number of ITGC tests a year and the share covered by a validated report.

## Class

business-automation.

## Rules or AI

No AI needed; it is standardisation. AI use limited to drafting the form on non-client material. `ai_use: none`. Advisor values: `ladder: assist`, `runtime_class: shared-team-skills`.

## Data

| Data needed | Where it lives | Owner (role) | Seen in its real state? |
|---|---|---|---|
| How validation is recorded today and what triggers re-validation | The IT audit specialist's practice | Integrated-audit manager | No |
| Tests per year and share with a validated report | Resourcing or operations tracking | Integrated-audit manager | No |

## Owner and benefit

- Owner: Integrated-audit manager (placeholder; the desk review says the manager is still to be named). Benefit owner: not yet named.
- Lever: capacity → staff hours per SOX-only ITGC test; risk → PCAOB comments.

## Early read

- Risk or regulatory exposure: AS 1215 documentation; independence of evidence if reuse across clients or lines is poorly scoped. Full route if it spans two lines.
- Duplicates: **`sox-report-register` is the same pattern.** The plan expects a roll-up into a single parent with `rolled_up_from`. Until then do not add the two items' values.
- Archetype evidence: assurance-controls-testing-06 (grade A); assurance-controls-testing-07 (grade B); assurance-controls-testing-03 (grade C).
- Human checkpoints: IT audit specialist signs each validation; senior confirms the listing is system-generated and in scope.
- Capacity choice: redeploy (advisor's); firm stance undecided.

## From the plan

Not a case in the plan; a desk review only (`units/integrated-audit/desk-review.md`, a draft written from the archetype and one reported case, not validated by anyone who does the work). Its two assumptions most likely wrong: that the validated-once pattern is typical and inspector-ready (one case, may depend on one specialist), and that hours released survive added review and documentation. Plan, Prioritize: merged with option 4 at roll-up, still to do. Next step: ask the specialist how validation is recorded and what triggers re-validation (integrated-audit manager).

## Screen result

**Provisional variant of `sox-report-register`.** Counted once, under the primary; its value is not added. Cannot pass g0 until the integrated-audit manager has validated it. No g0 outcome is proposed. Scores kept for reference: weighted 3.90, value index 4.11, readiness index 3.73; category quick win as the advisor drafted it (provisional). Its useful contribution is evidence for the primary: whether the validated-once pattern is structural and how validation is recorded. Full path. Sponsor placeholder: Managing partner for assurance.

## Next gate evidence

Filled after a Go.
