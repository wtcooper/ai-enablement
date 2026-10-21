# Synthesis report: assurance / benefit-plans

Synthesised 2026-10-21. Outputs:
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/benefit-plans.md` (280 lines, table of contents)
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/use-cases/benefit-plans.yaml` (15 entries; passes `scripts/validate.py` with the expected below-target warning: 47% A/B)

## 1. Counts in and out

| | Count |
|---|---|
| Candidate entries in `mm-benefit-plans-combined.md` | 17 (0 A, 8 B, 6 C, 3 D) |
| Items routed to benefit-plans from other `mm-*.md` files and the landscape | 7 (see section 6) |
| Entries out | 15 (0 A, 7 B, 6 C, 2 D) |
| Merged | 1 pair (old 06 + old 16) |
| Dropped as duplicate of a sibling module | 1 (old 14) |
| New entries created from routed items | 0 (routed items were added to existing entries or cross-referenced) |

Id map (research file → final): 01→01, 02→02, 03→03, 04→04, 05→05, 06+16→06, 07→07, 08→08, 09→09, 10→10,
11→11, 12→12, 13→13, 14→dropped, 15→14, 17→15.

## 2. Duplicates merged and other changes

- **Old 06 (plan-document reading) + old 16 (citation-backed technical Q&A for trainees) → 06.** Same tool (CoCounsel
  Audit), same firms (Kimberlin, Sensiba), same two case studies. Kept both outcome lines and all sources (TR-KIMBERLIN-2026,
  TR-SENSIBA-2026, LEDGERLINE-CPAPA-2026, ICPAS-EBPQ-2024).
- **Old 14 (idea: firm-level governance and documentation of AI in plan audits) dropped**, because it duplicates
  `assurance-quality-management-17` and `-23`. Its plan-specific points (CalCPA AI session, the Forvis Mazars
  documentation remark, AuditMiner's prediction on documenting judgment) moved to the module's Guardrails and Frontier.
  SIKICH-WEBINAR-2025 stays in the module's Sources list. CALCPA-EBP-2025 is no longer cited.
- **09 widened with routed adoptions.** Withum, EisnerAmper and PKF O'Connor Davies DAS adoptions were added. I re-opened
  the three Caseware releases on 2026-10-21 to check their wording about plan audits: Withum "deployed the DAS Suite,
  including DAS, DAS PCR and DAS EBP"; EisnerAmper's platform includes "modules for ... employee benefit plan audits";
  PKF's release describes the suite as including DAS EBP. Citrin's PE ownership (New Mountain Capital, controlling,
  April 2022) was added from BORYSOFF-PE-2024, which came from the mm-widen-assurance routing.
- **01: MECPA-TECHSURVEY-2025 added to the notes** (open-text answers naming Autire for EBP work; re-checked in the PDF).
- **Ladder normalised:** 04 (trust reconciliation) and 08 (generated risk assessment) moved from automate to augment,
  because a person reviews or concludes on the output on the normal path.
- **Drift removed:** sentences in the research file that made claims no source supports were reworded as stated gaps:
  02 (grouping "can hide" an exception), 04, 06 (misreads flow into tests), 09 and 11 ("consistency is not quality",
  "membership and tools do not guarantee quality"), 11's role line ("moves inspection preparation to the vendor"), 13
  and 15. The module's capacity line keeps "without adding headcount" only as Autire's home-page statement.
- **Firm kind added** to each solution (regional, Top 100, Top 75, specialist, mid-market APS, PE-backed, Top 20/25,
  vendor).

**Source-key reconciliation** (same document, same key):
- AICPA-AIPA-2026 (research file) → **AICPA-PA-2026** (the key the archetype already uses for that URL). I kept the
  research file's type `professional-body`; the archetype files use `standard-setter` for that key.
- OATH-SITE-2026 (mm-widen-assurance) → **OATH-2026** (the archetype key, used in `assurance-acceptance-independence-20`).
- CITRIN-DAS-2026 is kept. The archetype also uses CASEWARE-CITRIN-2026 for the same release in another file; the
  coordinator should pick one.
- Withum: CASEWARE-WITHUM-2026 (private-company-practice) is used here; private-company-governance calls the same release
  WITHUM-DAS-2026. EisnerAmper: CASEWARE-EISNERAMPER-2026 (the archetype key), which the practice pass calls CASEWARE-EISNERDAS-2026
  and the governance pass calls EISNER-DAS-2026.

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 06, 13, 14 | | | 3 |
| augment | 02, 04, 07, 08 | 09, 11, 15 | 12 | 8 |
| automate | 05, 10 | 01, 03 | | 4 |
| delegate | | | | 0 |
| Total | 9 | 5 | 1 | 15 |

- **Delegate: no evidence.** No source describes an agent owning a multi-step plan-audit outcome. The nearest is
  Ledgerline's CEO describing agents plus deterministic code in general terms, already recorded as
  `assurance-substantive-testing-25` (automate/model, C). No entry was invented to fill the gap.
- **Model: thin.** It has one grade-C entry (12, Metz), plus cross-references to `assurance-substantive-testing-25`
  (Ledgerline) and `assurance-acceptance-independence-20` (Oath lists employee benefit plans among its client types).
- **Automate at process scope** rests on rules-based automation (01's tests are hard-coded logic; 03 is data
  integration), not on AI in the narrow sense.

## 4. Grade mix

- Out: A 0, B 7 (47%), C 6, D 2. The share is below the validator's 50% A/B target. That reflects the evidence, not a
  synthesis choice.
- No A: every figure is in a vendor-authored case study or press release, and none states how it was measured. Under
  the 2026-10-17 rule, Belfint's 80 to 54 hours and Rea's 40% cannot be A.
- B rests on named firm deployments: Belfint, Rea, Sikich, Anders, Kimberlin, Sensiba, Citrin, Withum, EisnerAmper and
  PKF. Seven of the ten are known only through vendor-hosted pages. Sikich's brochure and Belfint's blog are the only
  firm-authored sources.
- By provenance, every outcome is vendor-published or self-reported. None is independent.

## 5. Gaps

- **Primary DOL study unread.** dol.gov returned 403. All deficiency figures come from Belfint, AAFCPAs, ICPAS, the
  AICPA's EBPAQC page and Jones & Roth. Belfint's text gives 307 plans but its table totals 308, and the by-area rates
  have no denominator. Check the primary PDF before quoting any of these figures to a client.
- **No regulator or peer-review view of AI** in plan audits (DOL EBSA, AICPA Peer Review Board, EBPAQC).
- **No independent quality measure**: no error, override, miss or parallel-run rates, and no inspection outcome
  linked to a tool.
- **No firm-authored account of AI results** outside vendor-hosted pages.
- **Plan types without AI evidence**: defined benefit (actuarial), health and welfare, multiemployer, ESOP, and
  full-scope investment testing.
- **Conference content**: the AICPA EBP 2026 agenda (loaded by JavaScript) and the CalCPA AI session's content were
  not read; only an abstract is public. There are no podcasts, community threads, job postings or academic studies.
- **Pricing and fee effects** of faster plan audits are not published, apart from vendor profitability claims.
- **Unverified items left out**: PSCA-AIRK-2026 (search-only; used only in idea 15), PKF-DAS-2026 (search-only; the
  Caseware release was used instead), the 2024 ERISA Advisory Council recommendation on disclosing AI in benefit
  determinations (search summary only), and undated pages from DataSnipper/Whitley Penn and Stax.ai.

## 6. Routed to other modules

**From the benefit-plans research, for other modules' synthesis:**
- `substantive-testing`: Ledgerline's whole-population specialist-firm model is already `assurance-substantive-testing-25`.
  DataSnipper evidence snipping for eligible-compensation validation (an undated Whitley Penn case page) belongs to
  `assurance-substantive-testing-14`.
- `controls-testing`: EBP-specific SOC 1 reading (benefit-plans 07) overlaps `assurance-controls-testing-13`.
- `soc-attestation`: AuditMiner SOC toolkits and AICPA TQA 9561 (11 Sep 2026) on a service organisation's AI in SOC 1
  and SOC 2 [AICPA-TQA9561-2026; AUDITMINER-SOC-2026].
- `quality-management`: plan-audit AI governance and documentation (the dropped old 14): the CalCPA 2026 session, the
  Forvis Mazars remark at a 2024 AICPA webcast, and AuditMiner's 2026 predictions [CALCPA-EBP-2026; JOFA-AAFOCUS-2024;
  AUDITMINER-PREDICT-2026; AICPA-PA-2026].
- `assurance-over-ai`: assessing recordkeepers' and TPAs' own AI (benefit-plans 14), and any audit of AI used by plans
  for claims or benefit decisions.
- `acceptance-independence`: prospecting and acceptance from Form 5500 data (benefit-plans 13).
- Archetype `workforce.md` and `economics.md`: outsourced and offshore plan-audit capacity [AUDITMINER-PREDICT-2026;
  AUDENZA-EBP-2026]; Serent Capital's investment in Autire [SERENT-AUTIRE-2026].
- No module yet: Form 5500 preparation, compliance testing and census scrubbing by TPAs and plan administrators (an
  undated Stax.ai page, not cited). This could become a future plan-administration or tax compliance module.

**Picked up here from other files:**
- mm-private-company-practice: DAS EBP in the Withum, EisnerAmper and PKF suites (→ 09); the MECPA survey naming Autire (→ 01 notes).
- mm-widen-assurance: Citrin and PKF DAS adoptions (→ 09); TSCPA ERISA 2 of 21 (already in 11 and the module metrics);
  Oath's EBP service line (→ cross-reference to `assurance-acceptance-independence-20` and OATH-2026 in 12).
- mm-private-company-governance: EBSA findings, the firm-size link, EBPAQC membership, DAS EBP and the CalCPA session
  (already in the research file; used in the module metrics, guardrails and 09).
- mm-nonprofit-government: the Citrin DAS EBP adoption (→ 09); the PKF item via CASEWARE-PKF-2026, not the search-only PKF-DAS-2026.
- landscape: the low-evidence verdict and the AICPA EBP and CalCPA conference rows (→ Frontier).

## 7. Suggested improvements to the briefs

- **Give researchers the archetype's canonical source keys up front** (a key list or lookup for sources.md). In this
  wave, the same Caseware releases had three keys each across four files, and the AICPA practice-aid release had two.
- **Ask researchers to tag each entry "AI", "rules-based automation" or "workflow tooling".** In this module, about half
  the entries are not AI by the sources' own description. A field would stop the advisor from overstating AI adoption.
- **Tell module researchers to check sibling-module ids before writing ideas.** Old 14 duplicated quality-management
  entries, and old 15 sits close to assurance-over-ai.
- **State the ladder rule for audit review in the vocabulary:** if a person reviews every output (not only exceptions),
  the entry is augment, not automate. Two entries needed that correction here.
- **Lower or waive the 15-entry and 50% A/B validator targets for modules the landscape marked low-evidence.** The
  brief's own target here is 12-20, so the warning is expected and not actionable.
- **Name the DOL's primary study as a must-read and give a fallback route** (for example, an archived copy), because
  every quality benchmark in this module depends on it.
