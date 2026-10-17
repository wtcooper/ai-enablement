# Grade A recheck (measured-outcome rule), 2026-10-17

Rule: A = a figure a named organisation reports as measured (tracked metric, study, data), or an independent
measurement of its deployment. A practitioner's recollection or rough estimate quoted in a vendor or press piece is B.
Scope: every `evidence_grade: A` entry in `archetypes/assurance/use-cases/` and `archetypes/tax/use-cases/`.
Sources re-opened: Caseware HLB and MHA, Microsoft Internal Audit and SOX change-management PDFs, KPMG UK controls
assurance PDF, Reddit post mirror, Optro launch, DataSnipper Armanino and FGMK stories, Alwin launch, Fieldguide
Sanville, Aibidia Trivium and Fortum.

| id | decision | reason |
|---|---|---|
| assurance-completion-reporting-06 | keep A | MHA ran a "data-driven, head-to-head pilot" with identical tests on the same accounts and reports average times (casting 25 to 12 min) and zero false positives: a trial measurement. HLB's ~600 h is the manager's estimate (B-level) but is not needed for A. |
| assurance-controls-testing-04 | keep A (borderline) | Microsoft's own publication states 2K hours saved a year as a result; not a quoted recollection. "Weeks to a single day" alone would be B. |
| assurance-controls-testing-05 | keep A | Reddit's CAE, on Reddit's own engineering blog: 175 controls automated (a count) and testing time down "on average" 60% per control. |
| assurance-controls-testing-06 | keep A | Microsoft's own innovation story reports 850 h and $185K a year as key results. |
| assurance-controls-testing-08 | keep A | Microsoft's own report of tracked function metrics (median report issuance 3 to 2 weeks; services automated under 30 to nearly 100). Armanino's "I estimate ... 25-plus hours" is B-level. |
| assurance-controls-testing-11 | keep A | KPMG UK's own publication says recent engagements "evidenced" ~18% less testing time (~15% on one engagement). |
| assurance-substantive-testing-10 | **change to B** | Oberlander ("two full days" to 5-6 h) and Sanville ("hours to minutes", "roughly $150-200" realisation) are recollections quoted by vendors; zero PCAOB comment forms is one inspection relayed via the vendor, not published by the PCAOB, and not a measure of matching. |
| assurance-substantive-testing-11 | **change to B** | FGMK "30-45 minutes to ~5 minutes" and CROP "around 80% faster" are approximate vendor-stated before-and-after figures with no measurement described. |
| tax-compliance-individual-business-05 | keep A | Crete pilot: 7,000 returns, field-completion accuracy measured against filed returns (published by co-developer OpenAI). Boulay "maybe 15 or 20 hours" is B-level. |
| tax-controversy-15 | keep A | HMRC annual report and Austrian Ministry of Finance figures are the organisations' own reported data (method unpublished). |
| tax-controversy-18 | keep A | Taxpayer Advocate Service measurements of IRS voicebots and chatbots (independent of the programme). |
| tax-controversy-19 | keep A | ATO-reported prompt counts and revenue (via OECD) plus ANAO's independent audit counts. |
| tax-indirect-tax-01 | keep A | Dell's test-set study (16,000 records; precision, recall, F1). |
| tax-indirect-tax-06 | keep A | Academic study on 74 textbook and 20 real ICON client cases. |
| tax-transfer-pricing-09 | **change to B** | Trivium's 80% saving rests on its manager's recollected baseline (2-5 days, up to six weeks); Fortum's 65% automation rate and "over 8,000" transactions are a quoted manager's statements with no denominator or method. |

## Counts

| archetype | A entries checked | kept A | changed to B |
|---|---|---|---|
| assurance | 8 | 6 | 2 |
| tax | 7 | 6 | 1 |

## Follow-on edits

- Each changed entry: `evidence_grade` set to B and one sentence appended to `notes` (substantive-testing-10 notes also
  say "quantified" instead of "measured" matching figures). Outcomes unchanged; provenance already labelled.
- Assurance ARCHETYPE.md module counts: unchanged and confirmed against the YAML (substantive-testing still 13 of 25
  A/B, strong).
- `assurance/modules/substantive-testing.md`: "home of these measured figures" became "named (estimated, grade B) figures".
- `assurance/modules/controls-testing.md`: "the measured cases are tests of details" became "the named cases".
- `tax/modules/transfer-pricing.md`: `#09` is now described as grade B (managers' estimates); "the only measured cases"
  became "the only named-customer figures (grade B estimates)".
- `validate.py`: 0 errors (15 warnings are about A/B share targets and were there before).

## Open points (not changed, outside the rule's edit scope)

- completion-reporting-06 notes and `assurance/modules/completion-reporting.md` (table row and objection) still call
  HLB "measured"; under the rule HLB's 600 h is an estimate and only MHA's trial is measured.
- controls-testing-04 is the weakest A kept: one rounded first-party figure (2K hours) from a vendor-style overview.
