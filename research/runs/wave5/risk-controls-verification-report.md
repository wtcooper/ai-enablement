# Verification report: advisory / risk-controls

Checked 2026-10-21 against the sources themselves. Files changed:

- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/use-cases/risk-controls.yaml`
- `plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/modules/risk-controls.md`

Method: I downloaded all 94 distinct sources (79 in the YAML and 15 cited only in the module) to a private folder. I
used curl, pdftotext and the r.jina.ai mirror, plus three extra fetches: the KPMG 2030 PDF, the IESBA pronouncement PDF
and a Cuatrecasas note on the EU AI Omnibus. No web search was used. For each source I checked that it exists, its date
(byline, `article:published_time`, JSON-LD, PDF metadata), every figure, and who said what. I also checked every
cross-reference to another archetype: all 23 exist and their titles match what the text says about them.
`scripts/validate.py` reports 0 errors. The module is now 300 lines, which is the limit.

## Counts

| Action | Entries |
|---|---|
| Kept | 8 (01, 03, 06, 10, 11, 13, 21, 24) |
| Fixed | 16 (02, 04, 05, 07, 08, 09, 12, 14, 15, 16, 17, 18, 19, 20, 22, 23) |
| Rejected | 0 |

Entry 06 is counted as kept. Its only change is a note that the PwC page returned 403 and was read through the mirror.

## Final grade mix

| Grade | Count | Entries |
|---|---|---|
| A | 0 | none |
| B | 12 | 03, 04, 05, 06, 07, 08, 10, 11, 13, 14, 15, 19 |
| C | 9 | 01, 02, 09, 12, 16, 17, 18, 20, 22 |
| D | 3 | 21, 23, 24 (all labelled "Idea") |

No entry qualifies for A under the 2026-10-17 rule. Every figure is either vendor-published or a practitioner's
recollection, or it counts scope rather than outcome (the Grant Thornton bank counts). The new Crown Castle "more than
half" figure is a recollection quoted in a vendor launch, so it supports B, not A.

## Fixes and rejections

| Entry / section | What was wrong | Fix | Pattern |
|---|---|---|---|
| 02 | It said there was "no named customer". The CFOtech launch names Crown Castle, with a quote. | Corrected. The Crown Castle quote is about evidence chasing, not the board-signal link, so the entry stays C and "announced". | Source under-read |
| 04 | It said Diligent's customers were not named, and missed the Crown Castle figure. It put the request agent's completeness check inside the Baker Tilly billing audit, but that detail comes from Romano in the IIA article. | Added the Crown Castle outcome ("more than half" less evidence chasing; recollection, vendor-published). Reattributed the request agent to IIA-UPSKILL-2026 and fixed the locator. | Wrong document or speaker |
| 05 | "Reddit's internal audit team reports …": the figures are Optro's own statement, with no Reddit quote. | Reworded as "Optro's release says …". Confirmed that Optro is AuditBoard's current name. | Wrong speaker |
| 05, 08, 09, 14, 16, 17, 19, 20 | KPMG-SOX2030-2026 pointed to the HTML summary. That page holds none of the cited survey figures (45%, 12 to 16 hours, 52%, 28%, 58%), and it numbers the POVs differently from the PDF. | URL changed to the 20-page PDF. Locators now follow the PDF numbering. | Locator and document mismatch |
| 08, 09 | The first-line/third-line split was cited to POV 5 (entry 08) and POV 2 (entry 09). In the PDF it is POV 3, p. 10. | Locators corrected. | Wrong locator |
| 07, 09, 16 | KPMG-REVCONTROLS-2026 (the "-new" PDF) is byte-identical to KPMG-FUTURESOX-2026. The note claimed "pagination differs". | Merged into one ref, KPMG-FUTURESOX-2026. Slide numbers replaced with PDF page numbers. The false note was removed. | Same document under two refs |
| 12 | The KPMG agentic-SOX article was dated "2025-07". | Now 2025-07-31, from the page's publishDate. The locator records the 2025-08-06 display date and a 2026-05-15 JSON-LD refresh. | Imprecise date |
| 14 | The title said Havertys "replaces" its outsourced testers. The source describes a first goal with no result yet. | Title now says it "starts moving" testing to agents. | Embellished qualifier |
| 15 | "Customers achieve 68-80%": the source says customers "can achieve". The $2.3M figure is unsourced in Midship's release, and another vendor CEO attributes $2.3M to KPMG as average SOX *program* cost. | Wording corrected and a caution added on the $2.3M figure. Andera's 70% is now located in the page's meta description. Added ACCTODAY-RSMBEACON-2026 for Andera's production use. | Statistic reported as something it doesn't measure |
| 16 | "External-auditor reliance on management testing 'is going to go away'" paraphrased inside the quotation marks. | Replaced with the verbatim quote ("the concept of auditor reliance is going to go away"). | Embellished qualifier |
| 17 | GT-AIIMPACT-2026 was dated 2026-03-18, which is the end of fieldwork. The RSM sample was described as "all of them AI users", which the cited source does not say. "Not a prescriptive rulebook" was attributed to COSO, but it is Deloitte's view. | Date set to "2026" with the fieldwork window noted. The unsupported qualifier was removed. The two claims are now attributed separately to COSO and Deloitte. | Wrong date; unsourced qualifier; wrong speaker |
| 18 | role_evolution said finance staff who build automations "become owners of the controls" (COSO p. 8). Page 8 says only that controls should govern who can build, deploy and interact with GenAI. | Rewritten to match p. 8. | Unsourced connective in role_evolution |
| 19 | "Sikich finds AI the hardest skill (41%)": cybersecurity is hardest (42%) and AI is second. The claim also had no source ref. | Corrected, with a p. 23 ref. | Statistic misreported |
| 20 | KPMG source URL. | Moved to the PDF, as above. | Locator and document mismatch |
| 22 | Graded B and "in-production". The field data comes from an unnamed vendor's bookkeeping platform, which is an adjacent process, and no advisory deployment was found. | Downgraded to C, maturity set to emerging, note rewritten. | Grade inflated by an adjacent process |
| 23 | DOJ paraphrased as asking "whether human decision-making is the baseline". The text asks "what baseline of human decision-making is used to assess AI". | Now quoted exactly. | Embellished wording |
| Module §4, probe 5 | "Most external auditors are undecided": uncertainty was the largest single answer (48%), not a majority. | Corrected. | Statistic misreported |
| Module §5 | Microsoft was described as "one … agent"; the source describes two agents. Petual "68-80%" lacked "can". Diligent's named customer was missing. The Gartner 38% strategy figure has two different bases in the press reports. RSM was described as "1,030 … AI users". The Vals benchmark was called "537-question", but that count is not on the source page. The $2.3M figure was labelled audit fees. | All corrected or qualified. | Several |
| Module §6, AICPA | The practice aid was called "non-authoritative", which neither source says. | Removed. | Unsourced qualifier |
| Module §6, SEC | The "unless not subject to audit procedures" exception was applied to (c)(4)(vi), management functions. That exception applies only to (ii) and (v). | Corrected. | Regulatory misstatement |
| Module §6, EU | "Provisional deal … adoption unconfirmed" was out of date. Regulation (EU) 2026/1744 was published in the Official Journal on 2026-07-24. | Updated, citing CUATRECASAS-AIOMNIBUS-2026, which replaces GIBSONDUNN-EUOMNIBUS-2026. | Stale regulatory status |
| Module §6, independence | Crowe was named as a PE-backed alternative practice structure without a source. | Replaced with Baker Tilly (APS stated on its own page) and Grant Thornton (GT-CBIZ-2026). | Unsourced claim |
| Module §7 | The staffing-cut figures sat beside AI without context. The Pulse attributes the cuts to budget pressure. | Added the measure, the private-company n = 29 and the report's own cause. | Unsourced connective |
| Module §8 | "ACFE Canada session … 2026-11-15 to 17": those are the conference dates. The AI ethics and compliance session is on 2026-11-16. | Corrected. | Wrong date |
| Module §9 | "The real risk is rubber-stamp review: 34% acted on a wrong agent output" linked a survey figure to a cause the survey does not give. "RSM says" quoted text that is the Accounting Today reporter's description. | The cause is now attributed to KPMG and the survey figure is kept separate. The quote is attributed to Accounting Today. | Embellished cause; wrong speaker |
| Module §10 | It listed KPMG-REVCONTROLS-2026 and GIBSONDUNN-EUOMNIBUS-2026. ICAEW was dated "2026-06". | Both refs removed and CUATRECASAS added. ICAEW is now 2026-06-10, and the TR-FOP page is noted. | Refs |

## Sources that couldn't be reached, or were only partly reached

- **PWC-DYNTEST-2026**: direct requests returned 403. I read it in full through the r.jina.ai mirror, and it supports
  the 30-40% claim.
- **LEXISNEXIS-CONSULTING-2026**: the direct page was a thin shell. The mirror confirmed the 54% figure.
- **AICPA TQA 9561 text**: behind the AICPA login. I relied on the Deloitte DART summary and the Journal of Accountancy,
  as the YAML already says.
- **IIA-CAEBULLETIN-2026**: partly member-restricted. The RSM summary it is cited for is readable.
- **IAC-SOXRELIANCE-2026**: the full poll results are in a paid eBook. The 95% and 48% figures are confirmed from the
  article text.
- **VALS-FAB-2026**: the 537-question count is not on the page, so I removed it.
- **TR-FOP-2026**: the 34% "shadow AI" figure is on the report page, not in the press release.

## Targets

| Target | Result |
|---|---|
| 15-25 use cases | 24: met |
| At least 50% graded A or B | 12 of 24 (50%): met, but only just |
| Every source dated | Met. ISO dates throughout; undated pages carry "2026" with the reason in the locator or notes. |

## Patterns of error to fix in the briefs

1. **Read the primary document, not its summary.** The KPMG HTML page has none of the survey figures, and the PDF numbers
   the POVs differently. The briefs should require the locator to point at the file that actually holds the passage.
2. **Use one ref per document.** Two KPMG URLs served identical files, and the note invented a pagination difference.
   Before giving a near-duplicate URL its own ref, compare the files (size or hash).
3. **Don't use fieldwork dates as publication dates.** GT-AIIMPACT-2026 used the end of fieldwork. If no publication
   date is shown, use the year and record the fieldwork window.
4. **Read the whole source for named users.** The Diligent launch named Crown Castle, but the entries said "no named
   customer". Missing a named user can understate the evidence as easily as other errors overstate it.
5. **Copy quantifiers exactly.** "Can achieve" became "achieve", 48% became "most", second-hardest became "hardest", and
   "replaces" was used for a plan. Hedges and rankings should be copied word for word.
6. **Attribute to the right speaker.** Vendor statements about a customer, a reporter's description and a quote from a
   different article were each assigned to the wrong party. State the speaker and the document.
7. **Don't add qualifiers the source lacks.** "Non-authoritative", "all of them AI users", "537-question" and Crowe as an
   APS had no source. Every qualifier needs one.
8. **Check legal exceptions clause by clause.** The SEC exception was extended to (c)(4)(vi). Rule text should be checked
   paragraph by paragraph.
9. **Re-check regulatory status near the run date.** The EU Omnibus had been adopted three months before this file
   called it provisional.
10. **Don't connect a survey figure to a cause.** "Rubber-stamp review" was offered as the reason for the 34%, and
    staffing cuts were placed next to AI. The briefs should forbid linking a figure to a cause unless the source makes
    the link.
11. **Don't grade from adjacent evidence.** Strong academic data from an unnamed bookkeeping platform was graded B for an
    advisory use case. The briefs should state that an unnamed deployment, or evidence from another process, caps an
    entry at C.

## Issue outside these files (not edited)

`GT-AIIMPACT-2026` names two different documents. In this module it is Grant Thornton's cross-industry 2026 AI Impact
Survey (950 leaders). In `ai-portfolio/references/method/acquired-firms.md`, `ai-portfolio/references/method/stage-gates.md`
and `transformation-advisor/references/method/acquisitions.md` it is the private-equity report, which this module cites
as GT-PEAI-2026. One of the two keys should be renamed.
