# Assurance consistency pass: report

Date: 2026-10-17. Scope: the 10 module files (`modules/*.md`) and 10 use-case files (`use-cases/*.yaml`) under
`plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/`. I did not touch the
archetype-level files (ARCHETYPE.md, interview-guide.md, value-chain.md, economics.md, state-of-ai.md, frontier.md,
guardrails.md, workforce.md, disruption.md, objections.md, sources.md).

Result: `python3 scripts/validate.py` reports 0 errors (8 warnings, all the existing evidence-target warnings). Every
module is at or under 300 lines: acceptance-independence 299, assurance-over-ai 292, completion-reporting 288,
controls-testing 294, planning-risk-assessment 300, quality-management 300, soc-attestation 299, specialists 277,
substantive-testing 300, sustainability-assurance 300.

Note on commits: the archetype verifiers committed while I was working (ca00ec1, 4198256, 0175f0e), and their
commits picked up some of my in-progress YAML edits. The working tree holds the final state; nothing was lost.

## 1. Build-process references removed

**YAML notes, automated pass (108 entries).** I removed the leading "Merged from practice-NN, discourse-NN and
governance-NN" / "From practice-NN" sentences: assurance-over-ai 22 entries, controls-testing 25,
planning-risk-assessment 25, soc-attestation 12, substantive-testing 24. The remaining note text was rewrapped.

**YAML file headers rewritten** (references to "wave 1 landscape scan", "deep dives", `research/runs/...`, "synthesis
report", "input files' refs", "verification report", "the pilot's key"): assurance-over-ai, controls-testing,
planning-risk-assessment, soc-attestation, substantive-testing. Review stamps were normalised to "Sources checked
<date>" in acceptance-independence, completion-reporting, quality-management, specialists and sustainability-assurance
(YAML), and in the completion-reporting, quality-management, specialists and controls-testing modules.

**YAML notes and fields fixed by hand:**
- acceptance-independence-18: "independence angle" changed to "independence side".
- assurance-over-ai: 01 (dropped "cited in discourse-01"); 06 (bare "-10" changed to `assurance-controls-testing-10`);
  07, 08, 14 ("routed to" changed to "covered in" / "in the ... module"; 14 now names `assurance-controls-testing-11`);
  09, 20 ("Graded C at verification (was B)" changed to "Graded C"); 10, 19 (dropped "(discourse had ...)"); 12
  ("opened in full at verification" changed to "read in full"); 13, 16 (dropped "From practice/governance-NN, with
  ..."; "re-opened" changed to "checked"); 20 ("dates differ between inputs" changed to "has two version dates");
  guardrails in 01, 13, 14, 18 ("routed to acceptance-independence" changed to "see/covered in the
  acceptance-independence module"); 22 ("practice-angle reading" changed to "as interpreted here").
- planning-risk-assessment: 01, 02, 07, 14, 15, 16, 22, 23, 25 (removed "practice/discourse/governance file",
  "landscape", "routes/routed", research ids; 07 now cites `assurance-acceptance-independence-18`; 23 refers to the
  archetype's economics file instead of "the cross-cutting business-model lens").
- soc-attestation: 04, 05, 11, 12, 13, 14, 15, 16 (removed "discourse said / governance said / three of four said"
  reasoning, research ids and "at verification"; 13 now names `assurance-controls-testing-14`).
- substantive-testing: 01, 04, 16 (dropped "two of three angles" choice notes); 02, 19, 22 (dropped "landscape" and
  "any angle"; 22 now gives Grant Thornton's own 7 May 2026 release date); 05, 11, 17 (dropped research ids, "routed",
  "two angles chose"); 10 (rewritten cross-reference, see section 3).
- specialists-10: "from other angles" / "specialists angle" reworded.
- sustainability-assurance: 05 ("routed to other modules" changed to `assurance-substantive-testing-22`); 08
  ("deep-dive candidates 08 and 15" removed); 13 ("routed to" changed to `assurance-controls-testing-15` and
  `assurance-specialists-10`).
- controls-testing notes: 02, 03, 04, 06, 09, 11, 13, 14, 17, 18, 20 (removed "Verifier ...", "landscape", "deep
  dive(s)", "practice said / governance said", "Lens set (two of three deep dives)", "as given in the input"; kept
  "search-only source" labels).

**Modules:**
- controls-testing.md: §10 dropped "the synthesis report maps keys to input refs" and "added at verification"; §9
  "before the pilot" changed to "before piloting" (it meant the reader's own pilot).
- completion-reporting.md §2: "Not described in the inputs" changed to "No public source describes it".
- Kept as business usage: PwC Australia's pilot, PwC's fund-audit pilot, FGMK's pilot group, "during the pilot" in
  quality-management-04, "Baker Tilly's synthesis", "routed virtually all customers" (Delve), "verification gate",
  "identity verification".

## 2. Routed items (all six confirmed against the source and placed)

Downloads were kept in a private folder made with `mktemp -d` in the session scratchpad.

| Item | Source opened | What it says | Placed in |
|---|---|---|---|
| CPAB finding | CPAB, *The evolving use of technology in the audit*, Dec 2025, p. 1 (PDF) | 2025 inspections: tools as primary evidence for a class of transactions; in some instances limited validation of input completeness and accuracy; one tool's substantive testing limited to flagged high-risk/outlier items, low-risk items not tested | substantive-testing-08: new guardrail, new human checkpoint, source CPAB-EVOLVING-2025; substantive-testing.md §7 (IFIAR and others) and §11 |
| AT-C 325/330 | CPA Practice Advisor, 27 Feb 2026 | ASB exposure draft adds AT-C 325 (examination) and 330 (review) of sustainability information; effective for engagements beginning on or after 15 Jun 2029; comments closed 30 Jun 2026 | sustainability-assurance.md §2 adoption bullet and §12 (CPAPA-ASB-2026). Not a use case: it is a standard |
| IESSA lines | IESBA IESSA final pronouncement (Aug 2025), 5400.20 A3 (p. 85), 5606.4 A3 and R5606.6 (p. 173) | Implementing sustainability reporting software is a self-review threat when it affects the client's records or controls, whether or not the firm built it; no IT systems services to PIE clients if a self-review threat might arise; designing or implementing software to collect or produce sustainability data is a management responsibility | acceptance-independence-15: new guardrail and source IESBA-IESSA-2025; acceptance-independence.md §6 IESBA bullet and §10 |
| Deloitte impairment case | Deloitte UK 2025 Transparency Report, Appendix 7 (PDF p. 111), quality overview (PDF pp. 21-22), Appendix 5 (PDF p. 102) | Automated impairment modelling across its largest audits (recalculation and sensitivity analysis); across ten consumer entities it found several calculation inaccuracies; an audit manager calls it an "AI impairment tool"; plan to extend to going concern and viability | New use case `assurance-specialists-14` (grade B, adjacent: the report does not say specialists run it); specialists.md §3 and §5; specialists.yaml header |
| CAQ "shadow AI" | CAQ Audit Committee Insights, Aug 2026 ("AI and ICFR") and Mar 2026 (six questions) | "Invisible AI" in ERP tools influencing reporting, routing, review and evidence; "shadow AI" outside approved channels; FEI AI Framework for ICFR; six audit-committee questions | controls-testing-15: new guardrail, new human checkpoint, sources CAQ-ACI-2026-08 and CAQ-ACI-2026-03; controls-testing.md §4 probe 9 and §10 |
| Board Agenda conflict | Board Agenda, 31 Mar 2026; FRC thematic review, June 2025, exec summary and p. 20 | Board Agenda: none of six firms monitored impact on quality. FRC: monitoring mainly counted teams using tools; no formal monitoring to quantify quality impact; firms developing capabilities to monitor usage and impact | quality-management-07 notes and source BOARDAGENDA-FRC-2026; quality-management.md §5 line after the FRC figures and §10. Conclusion: the module's "0 of 6 quantified" matches the FRC; the press wording overstates it |

None was skipped.

## 3. controls-testing-07 and -08 trimmed against substantive-testing

- **controls-testing-07** rewritten to controls-specific claims: removed the Oberlander, Sanville (realisation, zero
  comment forms) and CoCounsel outcomes, the Sanville guardrail and role note, and the FG-SANVILLE source. It now
  keeps PwC's October 2025 statement that controls-testing automation would follow Evidence Match, RMF's controls use
  (its ~50% figure labelled as tests of details) and KPMG UK's DataSnipper use on IT change tickets
  (`assurance-controls-testing-11`), and points to `assurance-substantive-testing-10` for the measured figures and
  `assurance-substantive-testing-14` for the CoCounsel figure. Grade stays B. TR-AGENTIC kept as a source because the
  module's §5 cites it.
- **controls-testing-08**: its figures (Armanino, Microsoft) are controls/internal-audit figures and do not duplicate
  substantive entries, so nothing was removed. Added cross-references to `assurance-substantive-testing-24`, `-25`
  and `-01` in the notes, and noted that its CPAPA-ADEWOLE source is the same article as LEDGERLINE-CPAPA-2026.
- **controls-testing-17** notes now point to `assurance-substantive-testing-24` (same PwC Australia programme).
- Matching updates elsewhere: substantive-testing-10 notes and the substantive-testing.yaml header (CT-07 no longer
  quotes Oberlander/Sanville); quality-management.yaml (Sanville entry) now points to `assurance-substantive-testing-10`
  instead of controls-testing-07; controls-testing.md §3, §5, §7 and §10 updated the same way (§5 Oberlander/RMF/Sanville
  bullet replaced with a pointer; FG-SANVILLE removed from §10).

## 4. controls-testing.yaml schema upgrade

- `provenance` added to 40 of 46 outcomes. Left out where unclear: #12 and #13 (EY conference poll and EY/KPMG
  description), #20 first outcome (mixes RSM's own positioning with Andera's customer claim), #22, #24, #25 (ideas with
  no figure). Convention matches sibling files (arXiv prototype = independent; IIAF survey = independent; vendor
  customer stories = vendor-published; firm's own statements = self-reported).
- `access` added to 152 of 154 sources: `search-only` for PWC-DCT and FG-FRAZIER (as the notes and the module say),
  `full` for all others, based on the controls-testing verification report ("88 of the 90 distinct URLs opened
  directly"). Left out for IAASB-ED (the page was opened but the exposure-draft texts are login-gated).
- New CAQ sources carry `access` and `locator`. `last_reviewed` set to 2026-10-17 for #07, #08, #15, #17.

## 5. Cross-references normalised to full ids

All cross-module references now use the existing full id form `assurance-<module>-NN` (the ids in the files carry the
`assurance-` prefix, so `controls-testing-11` alone would not resolve). Each was checked to exist and match content.
- planning-risk-assessment.md: CT-01, CT-04, CT-17 (header and 6 body uses) changed to `assurance-controls-testing-NN`.
- soc-attestation.md: CT-01, -02, -11, -12, -13, -14, -15, -23 (header and 12 body uses).
- substantive-testing.md: `CT#07`, `CT#08`, `CT#10`, `CT#15`.
- completion-reporting.md: ST-13 (3 uses). assurance-over-ai.md: `CT#15` (3 uses). quality-management.md: `ct-#10`.
- Module headers now say "other modules' ids are in full" instead of defining CT-/ST- shorthands.
- YAML: soc-attestation.yaml header "-12, -13, -14, -23" and assurance-over-ai-06 "-10" expanded to full ids. All
  other bare `-NN` references point within their own module and were checked against the target titles.
- A script check of every `assurance-<module>-NN` reference across modules and YAML found no missing ids.

## 6. Files changed

Modules: all ten. Use cases: acceptance-independence, assurance-over-ai, completion-reporting, controls-testing,
planning-risk-assessment, quality-management, soc-attestation, specialists (new entry 14), substantive-testing,
sustainability-assurance.
