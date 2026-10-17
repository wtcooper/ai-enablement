# Verification report: assurance / sustainability-assurance

- **Verified:** 2026-10-17
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/sustainability-assurance.yaml` (13 entries)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/sustainability-assurance.md` (300 lines after edits)
- **Method:** every cited URL was opened with curl (PDFs through pdftotext). Five sites that block curl were read through
  the r.jina.ai text mirror. Two extra documents were opened: the ASE conference paper PDF, and a newer Hogan Lovells
  note (13 Oct 2026) on the California SB 253 regulation.
- **Validator:** `python3 scripts/validate.py` reports no ERROR for either file. The INFO/WARN lines on targets remain:
  13 use cases, 0% A/B. The 7 ERROR lines in the run are all in `assurance/ARCHETYPE.md` (broken links), which this
  pass did not touch.

## 1. Counts

| Action | Count | Entries |
|---|---|---|
| Kept | 7 | 02, 03, 05, 06, 07, 08, 09 |
| Fixed | 6 | 01, 04, 10, 11, 12, 13 |
| Rejected | 0 | |

Entry 06 also had a note edited to remove a reference to a research file. The wording did not change, so it counts as
kept.

## 2. Final grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 0 | |
| B | 0 | |
| C | 7 | 01, 02, 08, 09, 10, 11, 12 |
| D (idea) | 6 | 03, 04, 05, 06, 07, 13 |

No grade changed. The grades in the YAML were already conservative. B was considered and not given for 09 (Watershed
names Smiths Group and Harris Farm, but every figure comes from the vendor) and 11 (PwC Germany tool, no client named,
one trade article).

## 3. Fixes and rejections

### Use-case YAML

| Entry | Field | Change | Reason |
|---|---|---|---|
| 01 | outcomes[0].measures | The note now says Verdantix places the Omnia ESG tool "as part of the sustainability assurance process" but names no engagement or client | The old note said the source did not frame it as assurance. The Verdantix release does, in one sentence |
| 04 | sources ISSA5000-2024 locator; notes | Added A228 (p. 110); notes now give A228's actual content | Missing page; the paraphrase of A228 is now exact |
| 10 | risks_and_guardrails; EU-ESRS-2026 locator | Estimates citation changed from ESRS 1 paras 65–66 to para 65. Para 91 now includes "without undue cost or effort". Locator names Art. 3 | Para 66 is about the value-chain cap, not estimates (wrong attribution). The para 91 condition had been left out |
| 11 | risks_and_guardrails; IESBA locator | 5606.4 A3 now includes its condition (the service forms part of or affects the client's sustainability records or controls). R5606.6 now reads "might create". 5400.20 A3 is now "taking responsibility for designing or implementing software...". Page corrected to p. 173 | The rules were embellished: the IESSA lists *taking responsibility for* software design as a management responsibility, not the design itself, and the self-review threat is conditional |
| 12 | outcomes[0].description; TRI-SUSTAIN-2025 date | Added that materiality-assessment AI is less popular than in the prior year's study and that practitioners see the technology as immature. Date 2025-06 changed to 2025-06-12 | A qualifier in the source had been left out; the byline gives the exact date |
| 13 | solution | "Practitioners and vendors suggest..." changed to "A vendor suggests..." | Only Watershed (a vendor) says this. No practitioner source |
| 13 | risks_and_guardrails[0] | "The IAASB expects questions..." changed to "says questions may arise...; it does not name AI" | The qualifier was embellished. Theme 10(a) is about technology generally, not AI |
| 13 | human_checkpoints[0] | Replaced a checkpoint attributed to IAASB-CATALOG-2026 with ISSA 5000 A262 (integrity of information through the entity's systems) | Wrong document: the Catalog contains no such checkpoint |
| Header | comments | Removed research-file paths and deep-dive candidate numbering | Build-only material |

### Module file

| Section | Change | Reason |
|---|---|---|
| §2 ISSA 5000 | "under any framework" changed to "any suitable framework". ISAE 3000/3410 bullet rewritten: ISAE 3000 (Revised) no longer applies internationally; ISAE 3410 withdrawn (approved Mar 2025); a jurisdiction that has not adopted may keep the old standard but then cannot claim IAASB compliance | The old wording mixed up the two FAQ cases (IAASB-ISSA5000FAQ-2025 Q1–Q4) |
| §2 adoption | "France, Spain and the Netherlands are listed as dependent" changed to "The Netherlands, France, Spain and several other EU states are marked as subject to the delegated act" | The Netherlands is listed as "in progress" and France and Spain as "under consideration". All carry the delegated-act footnote, as do Austria, Portugal and others |
| §2 Omnibus | Recital 31 applies to first-wave companies; exemption covers financial years *starting* in 2025–2026 | The scope was too broad |
| §2 CEAOB | CEAOB advice adopted 25 Sep 2026 and published 30 Sep; "expected to consult" changed to "will launch a public consultation this autumn" | Two dates exist (CEAOB PDF and ACCA page) |
| §2 ESRS | Transitional choice now cited to EU-ESRS-2026 Art. 2 as well as WPK; application to Art. 3; ESRS 1 "paras 65–66" changed to "paras 65, 91" | Primary source added; para 66 was misattributed |
| §2 ESRS / A131 | "A supplier's own assurance report" changed to "Another practitioner's assurance report on a value-chain entity" | A131 is about one-to-many reports from another practitioner |
| §2 US | SB 253 bullet rewritten: the Office of Administrative Law approved CARB's initial regulation on 12 Oct 2026, confirming the 10 Nov 2026 deadline. The regulation has no assurance requirement, and CARB accepts reports with or without assurance (new source HL-CARB-OAL-2026). CARB workshop dated 21 Jul 2026; Q4 2026 rulemaking package | The deadline was still pending approval in the July sources. A newer primary-quality note settles it. HL-CARB-ROADMAP-2026 was superseded and removed |
| §2 IESSA | Same three corrections as YAML 11 | Embellished rule text |
| §3 table | "CARB timing unsettled" changed to "CARB assurance timing unsettled" | The reporting deadline is now final |
| §4 #13 | "The IAASB lists the question" changed to "lists related technology questions (complex systems, external data; AI not named)" | Wrong framing: Theme 10(a) does not mention AI |
| §5 probe 9; §8 | "ICAEW expects more work with non-accountant specialists" changed to "ICAEW's audit director says firms *may* need more specialists, including non-accountants". The source is about audits generally, with sustainability as an example | Embellished qualifier; attributed to the named speaker (Alex Russell) |
| §6 | CAQ row: "with assurance" changed to "with assurance or verification" | The statistic was reported as something it does not measure |
| §6 | "if a team pilots AI" changed to "if a team tries AI" | Build-only wording ("pilot") |
| §7 | Human-steps list now cites MDPI-SUSAI-2026 ss. 6.2–7.2 | The citation location was unclear |
| §9 | ICAEW 2026-07 changed to 2026-07-14; CARB preview 2026-07 changed to 2026-07-21; "CEAOB advice delivered" changed to "adopted"; added 2026-10-12 OAL approval; SB 253 deadline now cited to HL-CARB-OAL-2026; TQM guide noted as being on AI-enabled tools | Exact dates; the CARB status was out of date |
| §10 | The AI-evidence question no longer attributes AI framing to the IAASB | Wrong attribution |
| §11 | IESSA objection now gives the conditional self-review rule | Embellished |
| §12 | Removed "opened by the deep-dive analyst". ICAEW date 2026-07-14. ACCA-EUPA date 2026-10 changed to 2026-09 (the page is titled "EU update - September 2026"). WINSTON publisher noted as now Winston Taylor (the page is on winstontaylor.com and says it was first published before the 1 Jun 2026 merger). Added HL-CARB-OAL-2026. Entries merged onto shared lines to stay within 300 lines | Build-only reference; dates; publisher accuracy; length |

### Claims confirmed exactly (selected)

- ISSA 5000 para 15: effective for periods beginning on or after 15 Dec 2026, or as at a date on or after it; early
  application permitted. IESSA aligned to the same date; value-chain-component independence provisions 1 Jul 2028.
- ISSA 5000 A91 (overreliance on automated tools, p. 79), A96–A98 (p. 81), A231, A249 (p. 114), A262 (p. 117), and
  IESSA R5320.11, 5320.11 A1 (p. 45) and 5120.12 A2 (automation bias): wording matches.
- Directive (EU) 2026/470: OJ 26.2.2026; thresholds EUR 450m and 1,000 employees; reasonable-assurance empowerment
  removed (recital); limited-assurance delegated act by 1 Jul 2027 (Art. 1(3), Audit Directive Art. 26a(3));
  transposition 19 Mar 2027 (Art. 5); Art. 2(12)(a) opinion covers the identification process and mark-up; Art. 2(10)
  inserts Art. 29f (technology report by 19 Mar 2028, no mention of AI).
- Delegated Regulation (EU) 2026/1563: OJ 21.9.2026; in force 10 Nov 2026; applies to financial years from 1 Jan 2027.
- None of ISSA 5000, the IESSA, the Omnibus, the revised ESRS, the CEAOB advice or the IAASB FAQs contains
  "artificial intelligence" or "AI". The module's opening claim holds.
- All figures in §6 (IFAC p. 3, Leeds snapshot, IFIAR factsheet, TRI survey, ASE-CIKE n = 77, Watershed) match the
  sources.

## 4. Sources that could not be reached

- **Unreachable after retries: none.** 49 documents were opened: the 47 unique cited URLs, the ASE conference PDF and
  the new Hogan Lovells OAL note.
- **Needed the text mirror** (curl returned 403): KnowESG (PwC tool), IFIAR TTF 2026 and IFIAR SATF factsheet, MDPI
  Sustainability systematic review, Preprints.org MDPI-SUSAI preprint. All were read in full this way.
- **Cited only through a secondary source, not opened:** the Gu, Dai and Vasarhelyi 2023 satellite-GHG study (described
  in the MDPI systematic review; ScienceDirect blocked); the Verdantix full Green Quadrant report (paywalled); the CIO
  article that KnowESG summarises. None supports a grade above C or D.

## 5. Targets

| Target | Result |
|---|---|
| 15–25 use cases | **Not met.** 13 entries. No entry was rejected; the shortfall is in the evidence, not in the verification |
| At least 50% graded A or B | **Not met.** 0%. No named assurance provider has published AI use on a sustainability engagement |
| Every source dated | **Met.** Every YAML source and every §12 entry has an ISO date |
| Ids unique; values from the vocabulary; quotations under 25 words | **Met** (validator plus manual check; the longest quotation is 7 words) |
| Module ≤300 lines; no build-only references | **Met** (300 lines; "pilot", "deep-dive" and research paths removed from the module) |

## 6. Error patterns found, for the briefs

1. **Embellished rule text from standards.** Conditional or scoped provisions became unconditional. IESSA 5606.4 A3
   lost its "when it forms part of or affects" condition, and 5400.20 A3 lost "taking responsibility for". Briefs
   should require quoting the operative words of any rule and keeping its conditions.
2. **Framing attributed to the wrong document.** The IAASB Technology Catalog was cited for AI-specific questions and
   for a practitioner checkpoint it does not contain. Briefs should ask: "Does the source use the word you are
   attributing to it (AI, expects, requires)?"
3. **Paragraph ranges cited too broadly.** "ESRS 1 paras 65–66" included a paragraph on a different topic. Cite single
   paragraphs and check each one.
4. **Dates on pending regulatory events.** The SB 253 deadline was stated as settled when the sources still called it
   proposed. A later source (12 Oct 2026) confirmed it. For any date within 60 days of the run, briefs should require a
   search for a newer status update.
5. **Sweeping speaker paraphrase.** The ICAEW director's "might need to engage more with specialists" became "expects
   more work with non-accountant specialists". Keep modal verbs (may, might, could).
6. **"Practitioners and vendors" when only one vendor said it.** Count the sources behind each plural.
7. **Publication versus adoption dates.** The CEAOB advice was adopted on 25 Sep and published on 30 Sep. Live pages
   (ACCA EU update) need the date shown on the page, not the month of the run.
8. **Not found here:** search-only figures inside A or B entries (none; there are no A or B entries), and grades
   inflated by adjacent-process evidence (the Moldova financial-audit survey was correctly kept out of grade support).
