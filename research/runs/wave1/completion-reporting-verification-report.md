# Verification report: assurance / completion-reporting

- **Date:** 2026-10-17
- **Files checked and edited:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/completion-reporting.yaml`
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/completion-reporting.md` (288 lines)
- **Validator:** `INFO .../completion-reporting.yaml: 18 use cases, 3 graded A/B (17%)` plus the matching WARN for the
  A/B target. 0 errors overall.

## 1. Counts

| Outcome | Count | Entries |
|---|---|---|
| Kept | 10 | 02, 03, 04, 09, 12, 14, 15, 16, 17, 18 |
| Fixed | 8 | 01, 05, 06, 07, 08, 10, 11, 13 |
| Rejected | 0 | |

All 18 entries also had build-process notes removed: merge provenance ("merged from practice-NN…"), angle-versus-angle
choices, references to search-only leads, and the "flag for the verifier" note. The YAML header no longer points at
research paths. References to other modules' use-case ids (ST-13) remain.

**Sources:** 84 unique URLs cited across both files. All 84 were opened:
- 73 directly with curl;
- 8 through the r.jina.ai text mirror (7 PCAOB pages that return 403, and one Fieldguide article that reset the
  connection);
- 2 DOI pages (AAA journals, 403): abstracts read from the Crossref API;
- 1 (ISA 570 PDF) returned 404 at the cited URL. The correct URL was found on the IAASB landing page and opened, and
  the YAML URL was fixed.

AS 3101 was also opened (via the mirror) to confirm the module's keyword check. No source was unreachable. Every
claim was traced except the dating limits listed in §4.

## 2. Final grade mix

| Grade | Before | After |
|---|---|---|
| A | 1 (06) | 1 (06) |
| B | 3 (05, 10, 14) | 2 (10, 14) |
| C | 8 | 9 (01, 02, 03, 04, 05, 07, 08, 09, 13) |
| D (idea) | 6 | 6 (11, 12, 15, 16, 17, 18) |

**A/B share: 17%** (3 of 18).

**Flagged calls:**
- **#05 → C** (applying the rule). The vocabulary requires a "named organization" for A and B, and the study's
  firm is "a Big 4 audit firm in Germany". For the same reason, maturity moved from in-production to piloting
  (in-production also requires a named organization). The note records that the peer-reviewed study does describe
  real use.
- **#10 kept at B.** Every figure was confirmed against the thesis:
  - model 85%, control group 77%, LLM-assisted group 78%;
  - 18.4 organisations per participant in both groups;
  - edge cases 67% versus 60%;
  - two groups of five BDO accountants; 20 cases; 82-organisation sample; COPRO 79% in cross-validation.

  The thesis meets the letter of A, since BDO is named and the outcome is measured. But it is a controlled student
  experiment on historical cases, not deployed work, and it found no gain in accuracy or speed. B is a downgrade for
  overstatement, not an inflation.

## 3. Fixes and rejections

| Entry / section | Fix | Reason |
|---|---|---|
| #01 role_evolution | The Withum comment is now attributed to Verity's learning value in general, not to "the agent" | The CwX blog says McElgunn described the learning value of Verity; it does not tie his remark to the checklist agent (embellished attribution) |
| #01 risks | "Segment comments kept rising" replaced with "rose from 16% to 23% of reviews with comment letters (a Deloitte review Fieldguide cites)" | Embellished qualifier; the source gives one rise between two figures |
| #01 notes | Rewritten: Caseware names partners who used Verity, not the checklist agent | Accuracy; build references removed |
| #05 | Grade B → C; maturity in-production → piloting | The firm is anonymised; the vocabulary requires a named organization |
| #06 | "40-50%" → "up to 40-50%" on subsequent drafts | The case-study body says "up to" |
| #06 / module §3, §6 | MHA "pilot" → "head-to-head trial" | Same meaning, clearer wording; the baseline caveat (tool versus tool) is kept |
| #07 human_checkpoints | "Not specified" replaced with the CEO's statement that practitioners stay in the reviewer's seat | The release does state a checkpoint |
| #08 problem | "EQR deficiencies at 42% of inspected firms" → share of inspected firms with at least one EQR-deficiency comment | Statistic described as something it doesn't measure (firms with a comment form, not a deficiency rate) |
| #10, #11 sources | ISA 570 URL corrected (`IAASB-ISA570-…` → `IAASB-ISA-570-…`) | The cited URL returns 404 |
| #10 notes | Rewritten with verified details | Build references removed |
| #13 problem | EY Canada item: "consulting report" → "a published research report on loyalty-programme fraud" | Big4News describes a thought-leadership report, not a consulting engagement |
| Module header | "not yet source-verified" → verified date | Status |
| Module §2 | "in one methodology" → "in one product's checklist" | TR describes its Guided Assurance product |
| Module §2 | EQR row reworded as above | Same reason as #08 |
| Module §2 | KAM row: "usefulness contested" now cites PCAOB-AGENDA-2026 | Claim attributed to the wrong document (the PIR page gives CAM counts; the agenda page gives the usefulness debate) |
| Module §2 | Audit committee row: "11% of listed audits where inspected in 2025, 4% in 2024" | Denominator made explicit; figures match IFIAR Table B.2 (79/725; 24/593) |
| Module §3 | #05 described as "an unnamed German Big 4 firm" | Consistency with the grade |
| Module §4 | AICPA representations point limited to the service-organisation context | Overgeneralised: the source ties it to an insufficient service auditor's report |
| Module §4 | "A vendor says its agents are not writing opinions" removed | No cited source (it came from an undated page that was never cited) |
| Module §6 | PCAOB EQR hours: "a 2018 baseline" → "per the 2018 post-implementation review" | The data predate 2018; the release date is not the measurement period |
| Module §6 | AI-investment findings attributed to Fedyk et al. 2022 | Names the original study behind the secondary figure |
| Module §7 | AICPA aid "non-authoritative" removed | Not stated in any opened source (AICPA release, JofA, Accounting Today) |
| Module §7 | IFIAR "keep audits human-led" reworded | IFIAR reports that firms say audits stay human-led and asks them to show it; it is not IFIAR's own instruction |
| Module §8 | "Committees raised AI unprompted" → "proactively raised the company's use of AI" | The CAQ pulse is about the company's AI use, not the auditor's |
| Module §8 | CAQ question qualified as being about the company's AI | Same reason |
| Module §10 | 2026-12-15: ISA 570 applies to periods beginning on or after this date; amended AS 1220 takes effect | ISA 570's effective date is period-based |
| Module §11 | "year-one savings" → "savings so far" | Embellished qualifier; CFO Dive gives no year count |
| Module §12 | KPMG-HOHL-2026 date 2026-05-27 → 2026-05-26; ICAEW-REPLETTER-2026 2026-05 → 2026-05-14 | Corrected from the pages' display dates |
| Module §4 intro, §12 | "Deep dive" wording removed | Build reference |

**Confirmed without change (spot list):**
- Caseware: 2.7 h "per disclosure checklist run" (CwX) versus "per workflow" (launch); the reasoning and citations
  do not persist after lock (docs); US GAAP and PDF only at GA.
- TR: 1,200-1,500 requirements; 30% of eligible customers and about 300 analyses a month; "No"/"N/A" calls on the
  roadmap.
- HLB: 300+ sets; 3-4 h per first review; 1,200 h; about 600 h saved.
- MHA: 25 → 12 min casting; 58 → 42 min first pass; zero false positives.
- CPA.com: 39% and 17% of 54 firms.
- IFIAR inspection-theme figures (all six); IFIAR TTF: 30% growth in AI-enabled tools; agentic AI "may evolve".
- PCAOB: EQR 37% → 42%; reviewer hours 1% and 3%; AC chairs 90% CAMs and fee questions.
- Deloitte/CAQ: 75% / 35% / 56% (248 respondents); CAQ partner pulse 57%; DataSnipper 73%, 13%, 80% and 38%.
- ISA 220 A34-A35; ISA 570 paras 21, A13, A42, A46 and effective date; AS 1220 .02 and .12; ISQM 2 para 8.
- FRC guidance: three risk categories, the critic role, rules-based mitigations, board-minutes and contract
  examples.
- Uniper 50-80%; Guo ~37%; FinancialAuditBench 90 tasks, 6 engagements, ~179 files, 11 models; FinAuditing 1,102
  instances and 13 models.
- Logothetis and Botic quotations; DAC Beachcroft negligence point; CCAB section 10.
- All quotations are under 25 words.

## 4. Sources not fully reachable or verifiable

- **Not reachable:** none.
- **Abstract only (403 on the publisher page):**
  - FABIAN-2026 (J. Information Systems): read via Crossref. Online publication date 2026-03-03 confirmed.
  - EULERICH-2025 (Accounting Horizons): read via Crossref.
- **Undated pages; Wayback Machine unreachable from this environment** (the dates in the YAML come from earlier
  archive checks and could not be re-confirmed):
  - DATASNIPPER-RISKS-2025 ("2025");
  - DATASNIPPER-AGENTS-2025 ("2025-10");
  - DATASNIPPER-CONNECT-2026 and DATASNIPPER-AIREPORT-2026 (month approximate);
  - CASEWARE-DCA-DOCS-2026, IDEAGEN-DISCLOSE-2026, FIELDGUIDE-QR-2026 and PCAOB-AGENDA-2026 (retrieval-dated).
- **Behind a login:** the AICPA practice aid itself. Its content is taken from the AICPA release, JofA and Accounting
  Today, all opened.

## 5. Targets

| Target | Met? |
|---|---|
| 15-25 use cases | Yes (18) |
| At least 50% graded A or B | **No: 17%.** The evidence does not support more; no grade was raised. The disclosure checklist (the busiest step) has only vendor figures with unnamed customers, and most other completion steps have no public AI evidence at all |
| Every source dated | Yes. Every source has an ISO date; seven undated web pages carry retrieval or archive dates (see §4) |
| Ids unique; vocabulary values valid | Yes (validator: 0 errors) |
| Module ≤ 300 lines | Yes (288) |

## 6. Error patterns to fix in the briefs

1. **Statistic described as something it doesn't measure.** The PCAOB EQR figure counts firms with a comment form,
   not engagements or a deficiency rate. The IFIAR percentages need the "where inspected" denominator. Ask the
   deep-dive briefs to copy the source's own unit phrase into `measures`, and the module brief to reuse it in tables.
2. **Attribution drift from a platform to a feature.** Beta-partner comments about Caseware Verity became comments
   about the checklist agent. Briefs should require that the named product in a claim match the product in the
   source sentence.
3. **Embellished qualifiers in module prose** ("kept rising", "year-one", "non-authoritative", "keep audits
   human-led" as an IFIAR instruction). The module brief should say: no qualifier or status label that isn't in the
   cited text.
4. **Uncited carry-overs.** "A vendor says its agents are not writing opinions" survived from a deep-dive aside whose
   source was never cited. The synthesis brief should forbid module sentences whose only support is an uncited
   research note.
5. **Company AI versus auditor AI.** Two committee-survey findings about the company's own AI were framed as being
   about the auditor. Add a check: whose AI does the source mean?
6. **"Named organization" applied inconsistently.** The rule was relaxed for an anonymised peer-reviewed study. The
   vocabulary should say explicitly whether anonymised field studies can reach B, and that maturity
   "in-production" follows the same naming rule.
7. **Broken canonical URLs.** The ISA 570 PDF URL was mistyped (hyphen missing) and 404s. Synthesis should re-open
   each canonical URL after key consolidation, not rely on a deep dive's copy.
8. **Build notes in shipped files.** Merge provenance and angle comparisons were written into `notes`. The synthesis
   brief should keep them in the synthesis report only.
