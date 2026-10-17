# Synthesis report: assurance / quality-management

- **Prepared:** 2026-10-16
- **Inputs:** `landscape-assurance.md` (leads, journey markers and frontier only; no YAML entries of its own),
  `assurance-quality-management-practice.md` (23 candidates), `assurance-quality-management-discourse.md` (19),
  `assurance-quality-management-governance.md` (22)
- **Outputs:**
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/quality-management.md` (297 lines, table of contents)
  - `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/use-cases/quality-management.yaml` (25 entries, 70 distinct source keys)
- **Validator:** `INFO ... quality-management.yaml: 25 use cases, 11 graded A/B (44%)`; 0 errors in these files. One
  expected warning on this file (below the 50% A/B target; see §4). At the time of the run the validator also reported
  an ERROR in `modules/sustainability-assurance.md` (310 lines), a file another agent is writing; it was not touched.
- **Structure:** as instructed, Part A (entries 01-16) is firm-level AI tool governance along the ISQM 1 / QC 1000
  lifecycle (certify, control, monitor, recertify, govern, resource, train, deal with inspectors); Part B (17-25) is
  engagement-level supervision, review and documentation of AI output. `assurance-controls-testing-10` (AI secondary
  review) is referenced from `#21` and `#22`, not duplicated.

## 1. Counts in and out

| | Practice | Discourse | Governance | Total |
|---|---|---|---|---|
| Candidates in | 23 | 19 | 22 | 64 |
| Carried into an output entry | 23 | 19 | 22 | 64 |
| Dropped | 0 | 0 | 0 | 0 |

**Out:** 25 entries. 20 are merges of two to five candidates; 5 come from a single candidate (05, 09, 15, 16, 24).
Every source of every merged candidate is kept in the merged entry (checked by script against the inputs' YAML, after
mapping refs to canonical keys).

## 2. Duplicates merged

P = practice, D = discourse, G = governance (candidate numbers in each file).

| Out | Title (short) | Merged from | Notes |
|---|---|---|---|
| 01 | Certify per use case, central board, recertify | P01, P04, D01, G01 | P04 (recertification triggers) folded in: D01 and G01 already covered triggers |
| 02 | Risk-tiered permitted-use policy, prompt library | P03, G02, D19 | D19 (idea) kept as a design option |
| 03 | Tool inventory, preventive controls | P02, D02, G20 | P02's Deloitte board and preprint material belongs to approval, carried in 01/08 |
| 04 | Evaluation sets, parallel running | G03, P19 | G03 was an idea |
| 06 | Vendor due diligence, scaled for small firms | P11, G06, D16 | D16 (small-firm idea) folded in |
| 07 | Quality-impact monitoring, network/member ownership | P05, P06, D03, G04, G05 | network allocation merged into monitoring to stay within 25 |
| 08 | Board oversight, AI committee, escalation | G07, P07, D04 | escalation pieces remain unadopted regulator suggestions (said in notes) |
| 10 | Role-based training, access gating, tutor mode | P13, G08, D07, P14 | tutor mode is announced only |
| 11 | Connected resourcing (RSM Luca Resourcing) | P10, D06, G10 | P10's search-only CAQ ref replaced by the opened post |
| 12 | Firm-approved guidance assistant | D05, G09 | |
| 13 | Regulator engagement, inspection-ready file | P21, D09, G19 | |
| 14 | Idea: AI in firm's own monitoring and RCA | P09, D18, G17 | all three D |
| 17 | Idea: partner plans AI use; senior stand-back | P18, D13, G11 | all three D |
| 18 | Human control points in agentic workflows | P15, D11, G12 | |
| 19 | Review mechanics: citations, tie-back, gates | G13, P16 | |
| 20 | Idea: structured scepticism | P23, G14, D12 | |
| 21 | AI review of engagement files | P08, G16 | overlaps ct-#10, referenced |
| 22 | Idea: model or rules engine cross-checks AI | P20, D14, G15 | named deployment lives in ct-#10 |
| 23 | Two-place documentation of AI use | P17, D10, G18 | |
| 25 | Supervision and junior development redesign | D08, G22 | |

Field disagreements: majority value used; on a tie, the value supported by the strongest-evidence candidate. Notable
choices: governance gates set to `ladder: assist`, `pattern: other` (discourse used `augment` to describe the governed
tool); 02 `pattern: other` (G02 had `intake-triage`); 18 `draft-review-loop` (D11 had `end-to-end-case-agent`); 25
`change_scope: model` (G22 had `process`). Each choice is in the entry's `notes`.

## 3. Coverage by ladder and change scope

| Ladder | Count | Ids |
|---|---|---|
| assist | 17 | 01-13, 17, 20, 23, 24 |
| augment | 7 | 14, 15, 16, 19, 21, 22, 25 |
| automate | 0 | none |
| delegate | 1 | 18 |

| Change scope | Count | Ids |
|---|---|---|
| step | 16 | 02, 03, 04, 06, 09, 10, 11, 12, 13, 17, 19, 20, 21, 22, 23, 24 |
| process | 7 | 01, 05, 07, 08, 14, 16, 18 |
| model | 2 | 15 (idea), 25 |

- **Assist dominates because most of this module is governance of AI, not AI doing the work.** Firm-level entries are
  human-run gates. That follows the inputs; nothing was invented to move entries up the ladder.
- **Automate: no evidence.** No input describes an AI-run quality-management step with people only on exceptions.
- **Delegate: one entry (18),** the governed agentic workflows at Deloitte and KPMG, described as design intent.
- **Model scope is thin:** one idea (third-party validation of firms' tools) and one announced workforce shift (PwC).
- **Maturity:** 16 in production (mostly self-described governance), 3 piloting, 1 announced, 5 emerging.
- **Patterns:** 16 `other` (governance gates). Recurring unmet patterns are proposed in §6.

## 4. Grade mix

| Grade | In (64) | Out (25) |
|---|---|---|
| A | 0 | 0 |
| B | 22 | 11 (01, 02, 08, 09, 10, 12, 16, 18, 21, 23, 24) |
| C | 22 | 9 (03, 04, 05, 06, 07, 11, 13, 19, 25) |
| D (idea) | 20 | 5 (14, 15, 17, 20, 22) |

**A/B share is 44%, below the 50% target. It cannot be met honestly:**
- No input found a measured outcome of AI tool governance or AI-output review at a named organisation, so no entry
  is A. The only measured named figures (Sanville, `#16`) are vendor-published and concern an adjacent change, as the
  practice angle judged.
- Most evidence is regulator guidance (FRC, IFIAR, IAASB, NFRA, AICPA) or regulator observation of firms that are not
  named per finding. Under the vocabulary that is C (or D where only recommended).
- Two entries were graded **below** what some angles gave: `#03` inventory (practice and discourse said B on the FRC's
  collective review and on Deloitte's board, which belongs to `#01`) and `#11` resourcing (discourse and governance said
  B, but the source does not say what AI does in the tool). Upgrading both would reach 52%; I judged that inflation.
- Dropping three C/D entries would also reach 50% (11/22), but every C/D entry covers a lifecycle step or frontier
  idea no B entry covers (monitoring, recertification testing, vendor diligence, inspectors, resourcing, automation-bias
  countermeasures, engagement planning). The brief allows C/D entries that add something; these do.
- **Caveat on the Bs:** all eleven rest on firms' own descriptions (transparency reports, releases, podcast remarks,
  a vendor case study), several second-hand through an academic reading of 2024 transparency reports (PwC, KPMG, EY).

## 5. Gaps

- **No quality evidence.** No error rate, override rate, false-positive rate, seeded-error test or parallel-run result
  for any firm's AI tools or reviewers. The FRC found no large UK firm quantifying quality impact; IFIAR suggests
  metrics and publishes no values.
- **No AI-specific inspection findings** for 2025-26 (PCAOB, FRC, CPAB counts). CalCPA's claim of AI-related findings is
  unverified and not used.
- **Firms:** governance evidence is almost all Deloitte UK, plus KPMG, RSM, PwC US and Grant Thornton UK fragments. EY,
  PwC UK, BDO, Grant Thornton US, Forvis Mazars and mid-tier firms are absent or second-hand. Small firms: CPA.com
  benchmark, ICAEW comment and Sanville only.
- **EQR and consultation with AI:** nothing public.
- **Resourcing:** RSM's tool is named but its AI role is unstated; no other case.
- **Primary texts not read:** PCAOB QC 1000 and amendment text (pcaobus.org 403); SEC approval status (secondary
  sources to 8 Oct 2026); AICPA practice aid (login); NFRA staff series (press reports only); IAASB September 2026
  meeting outcome on Guides 1-2; FRC 2026 audit quality review; PwC UK 2025 transparency report; ACRA's guidance
  (announcement only).
- **Not searched or blocked:** job postings, community forums, conference recordings; SSRN field experiment on LLMs and
  audit quality; Swedish junior-auditor study; MindBridge PCAOB letter. All three angles hit the web-search quota.
- **Lens gaps:** automate empty; delegate and model thin (see §3).

## 6. Suggested improvements to the briefs

1. **Grade rule for collective regulator observations.** Angles split on whether the FRC's review of six named firms,
   reported collectively, is B or C. Write the rule into the vocabulary (I applied C).
2. **"AI element unspecified" rule.** A named deployment whose source does not say what AI does should cap at C. Add it.
3. **Ladder for governance use cases.** Say whether `ladder` describes the governance process or the governed tool;
   the angles disagreed. Consider a field such as `subject: governs-ai | uses-ai`.
4. **New patterns.** Four recurring `other` shapes: *governance gate / tool certification*, *evaluation harness and
   parallel run*, *human control point in an agent workflow*, *use documentation and audit trail*.
5. **Canonical keys before the deep dives.** The angles still produced different keys and URLs for the same document
   (Deloitte UK transparency reports, RSM release, CPAB 2025 paper, IFIAR 2026 report, FRC thematic review) and the same
   key for two different NFRA articles. The landscape should issue a key table the deep dives must reuse.
6. **Shared search budget.** All three angles ran out of web search; give each angle its own quota or a fetch list.
7. **Cross-module overlap.** Tell synthesis agents which pilot entries overlap (as done here for ct-#10) in the brief.
8. **Size of `function` list.** A quality-management function value would help; the angles used four functions.

## 7. Conflicts resolved, and items for the verifier

- **QC 1000 amendments:** the landscape said "approved 9 Sep 2026, effective 15 Dec 2026"; governance read DART and
  EisnerAmper: adopted 9 Sep, effective with QC 1000 on 15 Dec 2026 only if the SEC approves, approval pending as of
  8 Oct 2026. Used governance's wording. QC 1000's own 15 Dec 2026 date rests on secondary sources.
- **IFIAR 2025 survey unit:** landscape "35% of engagements"; the report says audits (listed PIE audits inspected).
  Used "audits".
- **Luca Resourcing:** landscape "AI staffing tool"; the opened CAQ post does not say what AI does. Used the post.
- **NFRA:** two different CAalley articles shared the key `NFRA-CAALLEY-2026`. Split into NFRA-CAALLEY-2026 (ten
  principles) and NFRA-CAALLEY-BIAS-2026 (automation bias).
- **FRC thematic review:** practice/governance read the AI-converted HTML; discourse read the PDF. Canonical URL is the
  PDF (official), date 2025-06-26; locators use section names that work for both. Verifier: check FRC counts on the PDF.
- **FRC sandbox:** two documents (news release 2026-06-04; programme page 2026-06) now have two keys.
- **IAASB roundtable summary:** governance opened only the publication page; discourse read the PDF. Canonical URL is
  the PDF, date 2026-02-10 from the page.
- **Persuasiveness of AI output (`#05` guardrail):** taken from the landscape's reading of the FRC guidance (R1), no page given.
- **HOLMSTROM-2024** dated 2024-06 from PDF metadata (the pilot YAML dated it to a 2025 conference).
- **KPMG "first Big Four" ISO 42001 claim** is KPMG's; Fieldguide (a vendor) says it also holds ISO 42001.
- **CAQ pulse on audit committees raising AI** ("nearly one quarter" vs "about two-thirds") is routed to planning; unresolved.
- **Dates inferred:** FIELDGUIDE-SANVILLE-2026 (undated page), TRI-FOP-2026 (2026-07 per landscape), Deloitte UK reports
  (PDF metadata), IAASB workstream page (`2026`, not in the YAML).

## 8. Canonical keys mapped to input refs and pilot keys

| Canonical key | Input refs | Pilot key |
|---|---|---|
| FRC-GENAI-2026 | all angles (two URLs: media.frc.org.uk used) | FRC-GENAI |
| FRC-ATT-2025 | all angles (HTML and PDF URLs) | FRC-THEMATIC |
| FRC-GENAINEWS-2026 | P: FRC-NEWS-2026; D, G | — |
| FRC-AIAUDITNEWS-2025 (report only) | P: FRC-NEWS-2025; G | — |
| IFIAR-TTF-2025 / IFIAR-TTF-2026 | all angles (D used ifiar.org URL for 2026) | IFIAR-TTF25 / IFIAR-TTF26 |
| IFIAR-SURVEY-2026 | P, G | IFIAR-2025F |
| DELOITTE-UKTR-2025 / -2026 | P: DELUK-TR-2025 / -2026; G | — |
| RSM-ASKLUCA-2026 | D: RSM-LUCA-2026; G | — |
| CAQ-RSM-2026 | P (search-only listing page); D, G (opened post) | — |
| CPAB-EVOLVING-2025 | P: CPAB-TECH-2025; G | — |
| CPAB-AI-2024 | G | CPAB-AI |
| PCAOB-PRIORITIES-2024 | P: PCAOB-PRIORITIES-2024; G: PCAOB-PRIORITIES-2025 | — |
| IAASB-TQMWS-2026 (report only) | P, G; D: IAASB-TQMPAGE-2026 | — |
| NFRA-CAALLEY-2026 / NFRA-CAALLEY-BIAS-2026 | P, G / D (same key, different article) | NFRA-CAALLEY |
| AFM-2025 / AFM-12BB-2025 | P (press release) / G (report) | AFM-12 |
| PWC-AT-2025, CFODIVE-PWC-2026 | P, D | AT-PWC, CFODIVE-PWC |
| KPMG-SOX-2026 | D | K-SOX30 |
| DELOITTE-OMNIA-2026 | P, D | DELOITTE-OMNIA |
| AICPA-PA-2026 | all angles | AICPA-PA |
| ICAEW-FRCVIEW-2026 | D, G (dates 2026-05-06 / 2026-05; day used) | ICAEW-FRC |
| FIELDGUIDE-SANVILLE-2026, FIELDGUIDE-PCAOB-2026 | P, D | FG-SANVILLE, FG-PCAOB |
| CPAPRACTICE-RSMANDERA-2026 | P | CPAPA-RSM |
| HOLMSTROM-2024, PETERS-2022, TRI-FOP-2026, CPACOM-ATR-2025 | P, G | HOLMSTROM, PETERS, TRI-FOP, CPACOM-ATR |
| FRC-SANDBOX-2026 / FRC-SANDBOXPAGE-2026 | G (release) / P: FRC-SANDBOX-2026 (page) | FRC-SANDBOX (release) |
| JOFA-AIPA-2026 | D (professional-body), G (press); typed professional-body | — |

All other keys appear in only one input, or identically in several, and are unchanged.

## 9. Routed to other modules (collected from the three deep dives)

| Item | Target module | Source keys | From |
|---|---|---|---|
| PwC Evidence Match; KPMG agents for expense vouching and unrecorded liabilities; KPMG AI transaction scoring and agents designing substantive tests | substantive-testing | PWC-AT-2025; ATKPMG-CLARA-2025; KPMG-TR-2025 | P, G |
| CPAB 2025: a tool as primary evidence source, testing limited to flagged items, limited input validation | substantive-testing (also planning-risk-assessment) | CPAB-EVOLVING-2025 | P, G |
| FRC illustrative example 2 (contract review to select revenue samples) | substantive-testing | FRC-GENAI-2026, pp. 49-54 | P |
| IFIAR 2026: AI-originated audit evidence and adversarial misuse of AI by audited entities | planning-risk-assessment; substantive-testing | IFIAR-TTF-2026, p. 10 | G |
| IFIAR frequency of tool use by audit area (journal entries 88%, controls 43%, risk assessment 55%) | substantive-testing; controls-testing; planning-risk-assessment | IFIAR-TTF-2025 | G |
| Deloitte UK automated impairment modelling found calculation inaccuracies across ten consumer entities | specialists; substantive-testing | DELOITTE-UKTR-2025 | G |
| PwC advanced walkthrough assistant and Simplified Audit - Execute | controls-testing | CFODIVE-PWC-2026 | P |
| KPMG on human-in-the-loop for AI controls, model drift and prompt injection | controls-testing | KPMG-SOX-2026, p. 14 | D |
| IFIAR's repeated finding on insufficient ITGC testing | specialists (IT audit) / controls-testing | IFIAR-TTF-2025 | P |
| FRC illustrative example 1 (board-minutes summary for risk assessment) | planning-risk-assessment | FRC-GENAI-2026, pp. 43-48 | P |
| ICAEW test of three chatbots on risk assessment and materiality | planning-risk-assessment | ICAEW-PIERPOINT-2025 | D |
| CAQ Spring 2026 Audit Partner Pulse: client AI governance (6% advanced, 40% incomplete, 46% early); audit committees raising AI (quarter vs two-thirds conflict) | planning-risk-assessment | BOARDMEMBER-CAQ-2026; CAQ-TRENDS-2026 | D, G |
| AICPA practice aid Part 1 (entity AI use, acceptance, AI-operated controls, SOC reliance) | planning-risk-assessment; acceptance-independence; controls-testing | AICPA-PA-2026; AT-AICPAPA-2026; JOFA-AIPA-2026 | G |
| Deloitte UK GenAI plans for disclosure assessment, tie-through, going concern | completion-reporting | DELOITTE-UKTR-2025, p. 94 | P |
| KPMG Financial Report Analyzer; PwC audit-committee communications tool; Foley's five audit-committee questions; IFIAR on transparency with those charged with governance | completion-reporting | ATKPMG-CLARA-2025; CFODIVE-PWC-2026; FOLEY-PCAOB-2026; IFIAR-TTF-2026 | P, D, G |
| Fabian and Ratzinger-Sakel: AI platform for auditing management reports | completion-reporting | FABIAN-2026 | G |
| IFIAR 2025 findings on acceptance (18% of firms) and ethics (30%); PCAOB focus on private equity and independence; PE deal counts and staffing warnings; SEC OCA independence review | acceptance-independence | IFIAR-SURVEY-2026; DART-SECPCAOB-2025; CAALLEY-PCAOBPE-2025; PCAOB-BOTICNEB-2026; TR-HOHL-2026; CAQ-HOHLWEBINAR-2026; STARLING-HOHL-2026; KPMG-HOHL-2026; PCAOB-PRIORITIES-2024 | P, D, G |
| IRBA example of AI analysing non-traditional sources for client acceptance | acceptance-independence | IRBA-SPA11-2025 | P |
| Fee and junior-hours pressure; KPMG's AI fee argument; client acceptance of AI terms (also `#24`) | acceptance-independence | ICAEW-EXPECT-2026; VERDANTIX-KPMGFEE-2026; ICAEW-POD-2025 | D |
| Deloitte and KPMG AI assurance services; KPMG ISO 42001 as precursor; fragmented market for assurance over AI tools; EY AI assurance | assurance-over-ai (other-assurance) | DELOITTE-OMNIA-2026; DELOITTE-UKTR-2026; AT-KPMGISO-2025; ICAEW-POD-2025; EY-CANVAS-2026 | P, D, G |
| FRC: some AI reviews may need specialist reviewers | specialists | FRC-GENAI-2026, p. 37 | D |
| PwC Australia AI-native audit pilot (five clients, all by 2028, 1,600 auditors); PwC hiring engineers and dual-track staff; graduate intake cuts; lean senior teams; small firms building audit operations around AI | cross-cutting (business model and workforce) | ACCTIMES-PWCAU-2025; PWC-AT-2025; ICAEW-EXPECT-2026; BI-PWC-2025; PODWISE-ACCTPOD-2026; PCAOB-BOTICNEB-2026 | P, D |
