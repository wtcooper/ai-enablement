# Verification report: assurance / assurance-over-ai

Wave 1 · Verifier · 2026-10-17

**Files checked**
- Use cases: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/assurance-over-ai.yaml` (24 entries)
- Module: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/assurance-over-ai.md` (292 lines, has a table of contents)

**Method.** Every distinct cited source was opened with `curl` (`pdftotext` for PDFs). Where a page loaded its text with JavaScript or hid it,
another route was used: the `r.jina.ai` mirror (Deloitte DART, the ICAEW roadmap article, the ISACA AAIA page), the linked PDF (the ACCA/EY
paper, the IIA framework in English), or a linked subpage (the ISACA exam content outline for the AAIA domains). Dates were checked against
the byline, `article:published_time`, JSON-LD and PDF metadata. Each figure, attribution, regulatory statement and frontier date was matched
to the text. Claims were also traced back to the raw research files to find where wording drifted.

`python3 scripts/validate.py`: **0 errors** in these two files. One warning: 24 use cases, 6 graded A/B (25%), below the 50% target.

## 1. Counts

| Use-case entries | Count |
|---|---|
| Kept as written (06, 07, 08, 11, 17, 19, 21) | 7 |
| Fixed (wording, figure, date, attribution, grade or source) | 17 |
| Rejected | 0 |
| **Total** | **24** |

Across both files: 35 YAML changes (34 fixes plus one claim replaced; one entry can have several) and 11 module fixes. One claim was removed because the source no longer
supports it (#23, the CASRAI CertSearch statement), and a supported statement from the same page took its place. Two grades went down (B to C).
No grade went up.

## 2. Final grade mix

| Grade | Before | After | Entries after |
|---|---|---|---|
| A | 0 | 0 | none |
| B | 8 | **6** | 15, 16, 17, 19, 21, 24 |
| C | 10 | **12** | 02, 03, 04, 09, 10, 12, 13, 14, 18, 20, 22, 23 |
| D (idea) | 6 | 6 | 01, 05, 06, 07, 08, 11 |

A/B share: 33% before, **25% after**.

## 3. Fixes and rejections

### Use cases (YAML)

| # | Entry | Before | Action | Reason |
|---|---|---|---|---|
| 1 | header | Cited `research/runs/wave1/` | Fix | Build-only path removed |
| 2 | 01 | AICPA practice aid "(13 Oct 2026, non-authoritative)" | Fix | Unsourced qualifier. Neither the AICPA release nor Accounting Today says "non-authoritative" |
| 3 | 01 | "Auditor judges whether a use case is financially relevant (DART)" | Fix | Wrong actor. Deloitte says management applies extra rigour to financially relevant use cases and agrees with auditors what evidence is enough |
| 4 | 01 | Note: COSO's "eighth" capability type named differently | Fix | In the COSO PDF, knowledge retrieval and summarization is type 7 |
| 5 | 02 | "PwC 2025 guidance the researchers did not see" | Fix | Build wording. Now "could not be checked" |
| 6 | 03 | KPMG: weaknesses avoided "because they still test around the AI" | Fix | Embellished cause. KPMG credits strong AI governance and also timing (still testing around) |
| 7 | 03 | "Advisers add: treat prompts… as governed configurations" (AT-COSO) | Fix | Wrong speaker. Accounting Today is reporting COSO's guidance |
| 8 | 03 | "KPMG expects reliance on AI-operated controls to become unavoidable" | Fix | Misreported. KPMG says working AI into the control environment will "likely during this next year" become unavoidable |
| 9 | 03 | Prerequisite "testable controls: documented logic, explainability" (K-404A) | Fix | Not in the source. KPMG says design, rationalization and documentation should come before using AI |
| 10 | 03 | Protiviti: workforce cuts "weaken controls such as segregation of duties" | Fix | The link to segregation of duties is the blog's, not Protiviti's |
| 11 | 03 | K-SOX30 locator | Fix | The configuration-log quotation is on p. 8, not p. 6 |
| 12 | 04 | Baker Tilly: accuracy and coverage matter "because boards ask who made the call" | Fix | Embellished cause. The source puts the two points side by side and does not link them |
| 13 | 05 | COSO: "deviation-based pass/fail view fits deterministic automation better" | Fix | Paraphrase drift. COSO says the definition of "control failure" may need to move beyond a single pass/fail indicator |
| 14 | 09 | Grade B; "close to 250" respondents | Fix | **Grade inflated.** The evidence is surveys of unnamed committees and one firm's advice, with no named deployment, so C. The respondent count is 248 |
| 15 | 10 | IIA: auditors need not "master every technical aspect"; AI auditing "a progression" | Fix | The English PDF (now opened) says auditors "are not expected to be experts on every audit topic" and may need outside technical resources. "Progression" was not found |
| 16 | 12 | "The market uses 'AI audit' and 'AI assurance' loosely" (EY) | Fix | Rewritten to the ACCA/EY paper (terms "at times used interchangeably") and EY ("number and variety of approaches is challenging") |
| 17 | 12 | ACCA-EY-2025 `access: search-only` | Fix | Better source. The paper's PDF opened; now `full`, with PDF URL and locator. EY-AIASSESS date set to 2025-08-27 (JSON-LD) |
| 18 | 13 | Deloitte SG: "deepen ISO/IEC 42001 expertise on the job"; 42001 as a staffing prerequisite | Fix | Misread posting. On-the-job learning is for AI regulations and frameworks. ISO/IEC 42001 familiarity is "an advantage, not a requirement". The requirements ask for 2-3 years, the title says 2-4 |
| 19 | 13, 20, 22 | DELOITTE-AIA-UK-2026 date "2026" (undated) | Fix | Missing date. JSON-LD gives 2026-07-02 |
| 20 | 14 | "AICPA leaders have warned 'fast and easy' SOC tooling risks quality" | Fix | The speaker is the chair of an AICPA SOC working group, and the warning is about SOC services pushed by tool-vendor marketing |
| 21 | 15 | "ISO/IEC 42006 followed ISO/IEC 42001 by about two years" | Fix | Publication gap is about 19 months (CASRAI); the CSA's "two years" runs to accreditation in 2026. Both sources now cited |
| 21b | 15 | ANAB "witnessed audits of two start-ups" | Fix | Embellished. The article calls Evisort and StackAware an AI contract-management company and an AI risk solutions provider; now "two AI companies" |
| 22 | 15 | "Schellman, a SOC audit firm" cited to Accounting Today | Fix | Wrong document. Accounting Today does not say it; Schellman's own site does ("began as a SOC audit firm"). Source added |
| 23 | 16 | Witness audits cited to BSI's release | Fix | Wrong document. Witnessing is described in Accounting Today's Schellman article. Source added |
| 24 | 16 | Note: ISO/IEC 42006 date conflict (7 Jul / 21 Jul / 5 Aug 2025); build references | Fix | Resolved. Published 7 Jul 2025 (CASRAI, Bright Defense); EVS is a later news item. CSA page re-checked: no AI-drafting disclaimer found |
| 25 | 18 | Prerequisite "skills in data science and model testing" (ICAEW conference) | Fix | Connective claim, not on the page. Replaced with EY's "two-in-the-box" model (JOFA-EVAL, added) |
| 26 | 18 | Deloitte partner: AI assurance "critical for wide AI adoption" | Fix | Embellished. Tedder says companies and consumers will want assurance over AI used in critical functions |
| 27 | 20 | Grade B | Fix | **Grade inflated.** Evidence is service offers (the same kind graded C in #18). The UK market figures measure the whole AI assurance market, an adjacent scope, so C |
| 28 | 20 | "84 specialised firms (17 a year earlier)" | Fix | DSIT says 17 in the 2023 AI Sector Study, "in the space of 2 years" |
| 29 | 20 | Mökander: audits "cannot by themselves solve the risks" | Fix | Embellished. The abstract says audits must be coordinated and urges realism about what auditing can achieve |
| 30 | 22 | EC-AISTANDARDS-2025 date "2025-10"; Babl session called "practitioner training" | Fix | The page's "Last update" is 2026-08-03. The Babl item is one ISACA chapter session |
| 31 | 23 | "CASRAI says IAF CertSearch does not list certificates by certification body" | Reject (claim) | Not on the CASRAI page (updated 2026-09-25). Replaced with that page's supported note: IAF ceased on 1 Jan 2026 and was replaced by Global Accreditation Cooperation |
| 32 | 24 | DSIT "judged process certification and accreditation of assurers premature"; AI auditing "the first specialism" | Fix | Misread. DSIT judged a regulated body premature, found general process-certification requirements hard to develop, and saw accredited management-system certification as the most feasible route. It calls AI auditing "a useful starting point" |
| 33 | 24 | ICAEW-ROADMAP date "2025-09"; ISACA domains locator; notes citing "governance angle" and "input" | Fix | Date 2025-09-16. Domains confirmed on ISACA's exam content outline page. Build references removed |
| 34 | all | `last_reviewed: 2026-10-16` | Fix | Set to 2026-10-17 |

### Module

| # | Section | Before | Action | Reason |
|---|---|---|---|---|
| M1 | Header | Last reviewed 2026-10-16 | Fix | 2026-10-17 |
| M2 | §2 Monitor row | "Pass/fail deviations fit deterministic controls, not GenAI" | Fix | Same drift as YAML #13 |
| M3 | §2 Fraud row | "specialist support needed" [AT-AICPAPA] | Fix | Connective claim; the source's fraud passage does not say it. Now names the example schemes |
| M4 | §2 Readiness row; §6 ISO | "Advisory work cannot be certified by the same body"; "Accredited bodies do not certify what an affiliate consulted on" | Fix | Overgeneralised. This is BSI's own impartiality rule |
| M5 | §3 Coverage | Grades B 8, C 10 | Fix | B 6, C 12 |
| M6 | §5 | "about 248"; "17 a year earlier"; "first insured agent $50M"; "a source nobody opened" | Fix | 248; 17 in a 2023 government study; first AIUC-1-backed policy (ElevenLabs); build wording removed |
| M7 | §6 | AICPA aid "non-authoritative" | Fix | Unsourced qualifier |
| M8 | §7 | "AI credibility gap" unattributed; IIA "master every technical aspect"; "SOC firm Schellman" [AT only]; Deloitte SG "trains 42001 on the job"; DSIT "first specialism" | Fix | Attributed to Chambers; IIA wording; Schellman source added; posting misread corrected; "possible starting point" |
| M9 | §8 | "2025-07/08 ISO/IEC 42006 published (dates differ)" | Fix | 2025-07-07 [CASRAI, Bright Defense] |
| M10 | §9 | KPMG: testing around is "exactly how" weaknesses were avoided; "reliance to become unavoidable" | Fix | Embellished cause and misquoted forecast (as YAML #6, #8) |
| M11 | §10 | "ACCA-EY-2025 (search only)" | Fix | Opened in full |

Checked and confirmed without change (examples): COSO reliance definition and evidence list (p. 13), five approaches (p. 14), monitoring and
"Looking ahead" tolerances (p. 16), Principle 8 (p. 11); every CAQ, Deloitte/CAQ and Optro percentage; KPMG 2027 forecast (p. 7) and rubber-stamp
line (p. 14); BDO four ITGC domains and agent types; AICPA aid content via the release and Accounting Today; UK GVA £1.01bn, 524 firms, £18.8bn
vs £6.53bn; Schellman 26 contracts and eight-month ANAB process; BSI triple accreditation, 26% figure and impartiality rule; KPMG, PwC Taiwan and EY
Italy certificates and dates; AIUC-1 900+ tests, $50M ElevenLabs policy, quarterly re-tests, consortium 60+ vs 250+; Article 43; Omnibus dates
(Reg. 2026/1744, 2 Dec 2027, 2 Aug 2028); prEN 18286 (30 Oct 2025); IAASB matter 10(b) (PDF created 9 Jul 2026); arXiv abstracts and dates; SEC
filer-status proposal (19 May 2026, Uniqus).

## 4. Sources that couldn't be reached

**None of the 95 distinct cited sources were unreachable** (94 in the YAML plus UNIQUS, which only the module cites). Five needed another route:

| Source | Route |
|---|---|
| DART-COSO-2026 | Static HTML had no body text; read through `r.jina.ai` |
| ICAEW-ROADMAP-2025 | Body loaded by script; read through `r.jina.ai` |
| ISACA-AAIA-2026 | Eligibility through `r.jina.ai`; domains from the linked exam content outline page |
| ACCA-EY-2025 | Previously "search-only (DNS failure)". The landing page and the 22-page PDF both opened |
| IIA-AIFRAMEWORK-2024 | English PDF linked from the public page opened (previously Portuguese only) |

Primary texts that remain unread are not cited directly: the AICPA practice aid (member login), ISO/IEC 42001 and 42006, the EU Official Journal
Omnibus text, PwC Canada's own release, and the Financial Times original behind Realtid and Consultancy.uk. Claims resting on them are worded as
"as reported".

## 5. Targets

| Target | Status |
|---|---|
| 15–25 use cases | **Met** (24) |
| At least 50% graded A or B | **Not met** (6 of 24, 25%). Grades were not raised to reach the target. Area 1 has no named engagement. Area 2's offers have no named client |
| Every source has a URL and a date | **Met.** Five pages have no date anywhere, so they carry the year only and the locator says so (BSI case studies ×2, AIUC-1 site, EY Japan, ISACA) |
| Vocabulary values, unique ids, quotations under 25 words | **Met** (validator clean; no quotation over 25 words) |
| No build-only references in the module | **Met.** The YAML notes still record merge provenance ("merged from practice-14…"), as the brief allows |

## 6. Error patterns to fix in the briefs

1. **Invented causes.** "Because" was added where the source only put two points side by side (Baker Tilly, KPMG on material weaknesses). Brief rule: state a cause only if the source does.
2. **Press summary credited to the wrong speaker.** Accounting Today reporting COSO became "advisers"; a press article was cited for a fact that appears only on the firm's own site. Brief rule: cite the document where the sentence appears, and name the original speaker.
3. **One organisation's rule turned into a general rule.** BSI's impartiality policy became "accredited bodies do not…". Brief rule: keep the subject of the source's sentence.
4. **Job postings over-read.** "Deepen 42001 expertise on the job" was wrong on both the subject and the requirement. Brief rule: quote the posting's own requirement line.
5. **Grade B given without a named deployment.** Surveys of unnamed committees and service offers were graded B, and a market-wide figure supported one service. Brief rule: B needs a named organisation doing the use case; aggregate surveys and offers are C.
6. **Dates marked "undated" without checking JSON-LD or "Last update".** Two pages had machine-readable dates. Brief rule: check JSON-LD, `article:published_time`, page "Last update" and PDF metadata before writing the year only.
7. **Unsourced qualifiers carried forward.** For example "non-authoritative", "loosely", "start-ups", "critical for adoption". Brief rule: every adjective about a document's status needs the source's own word.
8. **Search-only labels not retried.** The ACCA paper and the IIA English PDF were reachable through PDF links on the landing page. Brief rule: try the linked PDF and `r.jina.ai` before recording search-only.
9. **Pages change after they are read.** The CASRAI guide no longer carries the CertSearch claim. Brief rule: record the retrieval date for each claim from a page that is updated over time, and re-check before verification.
