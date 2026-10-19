# Synthesis report: professional-services / quality-review

Run 2026-10-19. Outputs:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/quality-review.md` (274 lines, table of contents at the top)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/quality-review.yaml` (18 entries)

`scripts/validate.py` reports 0 errors for both files (18 use cases, 61% graded A/B). Every source key in the module is in the YAML or in the module's §10. Every key named inside a YAML entry is in that entry's `sources`.

## 1. Counts in and out

| Input | Candidates | Grades in |
|---|---|---|
| ps-quality-review-practice.md | 19 | A 1, B 9, C 9, D 0 |
| ps-quality-review-discourse.md | 17 | A 0, B 7, C 7, D 3 |
| ps-quality-review-governance.md | 17 | A 1, B 7, C 3, D 6 |
| **Total** | **53** | **A 2, B 23, C 19, D 9** |

The landscape file added no candidates. Its quality-review leads were already covered by the deep dives. Routed items picked up from other `ps-*.md` files are listed in §4.

**Out: 18 use cases (A 0, B 11, C 6, D 1).**

## 2. Duplicates merged (P = practice, D = discourse, G = governance)

| Out | Merged from |
|---|---|
| 01 Enforced review policy and attestation | P01, P12 (training part), D06, G04, G17 (unsanctioned-use part), plus routed LAW360-GA-2026 |
| 02 Automated cite, quote and proposition check | P02, D01 (checker part), G02, plus the Thomson Reuters Verify part of D02 |
| 03 Verification record on the file | P03, D01 (audit-trail part), G08 |
| 04 Pre-issue reference audit, consulting and advisory reports | D03, G06 (incident facts shared with P10) |
| 05 Benchmark tools and set review depth by task | P04, P08, P19, D07, G03, G13 |
| 06 In-matter test-set validation and sampling | P06, plus routed LAWSOC-AGENTIC-2026 |
| 07 Evaluation suites and change control (legal engineers) | P05 |
| 08 Review gates with a named reviewer | P07, D05, plus routed TRI-PREMORTEM-2026 |
| 09 Oversight tiered by agent autonomy | D10, G07 |
| 10 AI layer on the firm's quality management system | D04, G09, D13 |
| 11 Track acceptance and overrides | P09, D15, plus routed TRI-STANDARDS-2026 |
| 12 Idea: cut the verification tax | D08, plus routed KANTATA-SOPSI-2026 |
| 13 Machine cross-check before human review | D16, P15 |
| 14 Incident response and look-back | P10, D11, G10 |
| 15 Check incoming work | P13, D12, G15, G16 |
| 16 Client disclosure and tool vetting | P18, D09, G05 |
| 17 In-house: bounded workflows and evidence from firms | P16, D17 |
| 18 Insurance-ready AI governance | G14, plus insurer comments from D06 and a Law Society point routed via acceptance-risk |

**Not kept as separate entries. Each is cross-referenced by id instead:**
- P11 and G11 (verification-first onboarding, unaided practice): talent-learning-02 and -09.
- G12 (blinded expert scoring, NBER): talent-learning-11 and work-production-06.
- D14 (BYU preparer self-review tool): talent-learning-06.
- P17 and D02 (source-linked research tools): work-production-01. The Verify feature moved into 02.
- P14 (Certinia PMO Quality agent): delivery-management, following routing in all three angles.

## 3. Coverage

| Ladder | n | Change scope | n |
|---|---|---|---|
| assist | 7 | step | 10 |
| augment | 9 | process | 8 |
| automate | 1 (`#13`, C, emerging) | model | **0** |
| delegate | 1 (`#09`, C, emerging) | | |

- **Model scope: no evidence.** No source shows a firm selling review as a service or changing its operating model around review. The nearest signal is a CPA Practice Advisor blurb about an AICPA and AIUC assurance certification for AI systems. It was routed to assurance, was not opened, and was not used.
- **Automate and delegate:** each has one entry, and both are ideas or announcements. No firm describes AI review with no person on the normal path.
- **Firm kinds:** law firms and courts dominate. The accounting and advisory entries are Armanino, Forvis Mazars, Schellman, CPA insurers and the FRC's six audit firms. Consulting enters through the Big Four incidents and the ICMCI code. The in-house entries are Microsoft, Starbucks, GSK and CLOC.

## 4. Routed items

**Picked up from other deep dives:** LAW360-GA-2026 (talent-learning practice; 85% manual checks), TRI-STANDARDS-2026 (talent-learning discourse; override tracking), KANTATA-SOPSI-2026 (delivery-management discourse; 89% verifying), TRI-PREMORTEM-2026 (delivery-management discourse; review as theatre), LAWSOC-AGENTIC-2026 (knowledge-management governance, sampling; also cited for the Law Society PI-insurance finding), LAWSOCIE-SRAWARN-2026 (staffing-resourcing governance; 42 SRA reports, module guardrails only), and PCAOB QC 1000 and the Deloitte Australia refund (acceptance-risk; Deloitte is used, QC 1000 is left to assurance).

**Not used:**
- TRI-MIDSIZE-2026, BLOOMBERGLAW-GCXAI-2026 and CONSULTANCYUK-BONE-2026: the routing notes give no quotable quality-review content. They belong to firm-finance.
- JBL-MCKINLEY-2026 and NATLAW-BRADLEY-2026: buyer-side evaluation of bids. They belong to pursuit-proposals.
- BOERSEN-LILLI-2024 and AL-DIDOMENICO-2026: not opened in a form that supports a claim.
- LAWSITES-IMANAGE-2026 and LAWSITES-SIMPLEDOCS-2026: playbook review is already work-production-08.
- DWF-SRA-2026 (Cork v Smith, 67 UK cases): talent-learning already holds it.
- DCBAR-OP388-2024: about billing.
- JMW-SRA-2026, MONDAQ-BSB-2026 and LEXISNEXIS-FOW-2026: already in other modules, so they are not repeated.

**Routed out from the three quality-review inputs**, for the target modules' syntheses:
- **billing-collections and scoping-pricing:** client requests for AI line items and "won't pay for AI work" guidelines (TRI-LEGALWEEK-2026); Cal Bar billing rules, p.8; ABA 512 Part II.F fees; ACC/Everlaw in-house survey (ACCEVERLAW-2025: 59% see no GenAI savings from firms).
- **acceptance-risk:** client terms on outside counsel and vendor AI use (Starbucks, "unbiased model" warranties); confidentiality and agent data access (CALBAR-GENAI-2026 pp.5-6); client consent to input data (ABA 512 Part II.B); privilege and discoverability of client AI chats (ABA podcast, Heppner v. Warner); PI insurance exclusions.
- **talent-learning:** NBER-AUTOR-2026; Duane Morris onboarding (TRI-ONBOARD-2026); Blank Rome (HARVEY-BLANKROME-2026); TR-FOP-2026 early-career data; JOA-LEARN-2026; TRI "Trust by Verify" for early-career lawyers; ABA podcast "Developing Lawyers in the Age of AI" (2026-10-13).
- **delivery-management:** Certinia PMO Quality and Retrospective Drafter agents (CERTINIA-VEDA-2026); Harvey orchestration beyond review gates (HARVEY-ORCH-2026).
- **client-development:** Reed Smith's claim that AI-enabled delivery wins work (HARVEY-REEDSMITH-2026); partners not discussing AI with clients; client reconsideration data (TRI-STANDOUT-2026; TR-FOP-2026).
- **pursuit-proposals:** Legora's RFP-automation posting (LEGORA-JOB-RFP-2026).
- **firm-finance:** tool sprawl, token costs and no firm-wide ROI proof (TRI-ILTACON-2026; BESTLAWFIRMS-VTAX-2026).
- **knowledge-management:** citator and corpus quality as knowledge assets (LAWSITES-FILEVINE-2026).
- **work-production:** Vals task benchmarks and HBS productivity figures; substantive drafting, redlining and e-discovery methods.
- **assurance archetype:** FRC thematic review, SQMS 1, IAASB quality management, PCAOB, the CPA Newfoundland and Labrador investigation of Deloitte, and AICPA/AIUC AI assurance certification (blurb only).
- **out of archetype:** hallucination management inside courts (TRI-COURTS-2026).

## 5. Grade decisions and conflicts

- **No A.** The practice angle graded Linklaters' own benchmark A, and the governance angle graded Vals and Stanford A. Both are graded B here because the figures measure tools in isolation, not an outcome of people working with AI. This matches the work-production header and the tax archetype. If the coordinator reads the 2026-10-17 rule more literally, `#05` could go to A on Linklaters.
- **Same document, different keys.** One key was chosen for each document, in line with existing archetype files:
  - TRI-ACCOUNT-2026 became TRI-STANDARDS-2026.
  - CANLAWMAG-SC-2026 became CANLAWYER-SC-2026.
  - CHARLOTIN-HALLUC-2026 became CHARLOTIN-DB-2026.
  - VALS-VLAIR-LR-2025 and VALS-LEGALRESEARCH-2025 became VALS-VLAIRRES-2025.
  - JOA-LEARN-2026 became JOA-TRAINING-2026.
  - AYINDE-EWHC-2025 became EWHC-AYINDE-2025.
  - CTV-DELOITTENL-2025 became CTV-DELOITTE-NL-2025.
  - TRI-TBV-2026, TRI-TRUSTBYVERIFY-2026 and TRI-BEYONDHITL-2026 became TRI-EVENTS-2026.
- **Dates that conflict:**
  - CALBAR-GENAI-2026: the PDF shows 2026-05; the Board approval date is 2026-05-14, which is the date used.
  - ILTA: the file name suggests 2026-06 and the metadata says 2026-08; 2026-06 is used, as in work-production.
  - TR-FOP-2026: the inputs give 2026-06-22, 2026-09-30 and "2026"; "2026" is used.
  - The Q3.18 table is cited at p.4 by one input and p.5 by another.
  - VALS-VLAIR-2025 is typed as vendor here; the inputs used academic, survey and vendor.

## 6. Gaps

- No reviewer catch rate, override rate, parallel-run result, review-time measure or inspection finding for AI-assisted deliverables at any named firm or in-house team. This is the central evidence gap.
- No consulting or Big Four primary description of how AI-assisted deliverables are reviewed. Those pages were blocked, and the evidence is incidents only.
- Engineering and architecture quality review, non-legal in-house shared services, and mid-size consulting are not covered.
- Several primary texts were not opened: the SRA and BSB notices, the Sullivan & Cromwell letter, the Johnson v. Dunn order, the full NBER and Stanford papers, the Casepoint report and the Filevine evaluation paper.
- Court AI-certification and disclosure orders (for example the Florida 11th Judicial Circuit's administrative order 26-04) were seen only through secondary sources.

## 7. Suggested improvements to the briefs

1. **Publish a shared key register before the deep dives run.** Nine documents arrived under two or three keys across the three angles and the sibling modules.
2. **State the grade-A test for tool benchmarks in the vocabulary.** This covers a firm's own benchmark of a tool and third-party benchmarks. Angles graded the same evidence A and B.
3. **Give the deep dives the sibling modules' finished id lists.** Work-production and talent-learning already held about a third of these candidates (tool testing, policy gate, onboarding, override logging, disclosure), so much of the merge effort went into de-duplication.
4. **Ask each angle for one consulting or accounting primary source on review practice.** If none is reachable, the angle should say so early rather than at the end. Search budgets ran out before the Big Four searches in all three angles.
5. **Ask the governance angle to tag each idea (D) with the regulator text that motivates it.** Several D entries merged cleanly into B entries once that link was explicit.
