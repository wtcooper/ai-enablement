# Synthesis report: professional-services / pursuit-proposals

- **Date:** 2026-10-19
- **Inputs:** `landscape-professional-services.md`, `ps-pursuit-proposals-practice.md`, `ps-pursuit-proposals-discourse.md`,
  `ps-pursuit-proposals-governance.md`; the "Routed to other modules" sections of every other `ps-*.md` file and the
  routing tables of the finished synthesis reports (client-development, knowledge-management, scoping-pricing,
  acceptance-risk, talent-learning, work-production); the finished client-development, scoping-pricing,
  knowledge-management, acceptance-risk, work-production and talent-learning YAML files for cross-references.
- **Outputs:** `plugins/.../archetypes/professional-services/modules/pursuit-proposals.md` (297 lines, contents list at
  top) and `plugins/.../archetypes/professional-services/use-cases/pursuit-proposals.yaml` (20 entries).
- **Validator:** `python3 scripts/validate.py` reports 0 errors; 20 entries, 50% graded A/B (meets 15-25 and 50%, just).
  A script check confirmed every outcome `source_ref` is in its entry's sources, every inline key in an entry is in that
  entry's sources, each source key has one URL, date and type across the file, and every key cited in the module is in
  the YAML or in the module's §10 (module-only keys marked *).
- No downloads were needed; all facts come from the input files.

## 1. Counts in and out

| | Practice | Discourse | Governance | Routed from other modules | Total |
|---|---|---|---|---|---|
| Candidates in | 14 (0 A, 7 B, 5 C, 2 D) | 16 (0 A, 4 B, 8 C, 4 D) | 17 (0 A, 1 B, 7 C, 9 D) | evidence items only | 47 |
| Out | | | | | **20 (0 A, 10 B, 7 C, 3 D)** |

Not carried as entries (no evidence lost; each is cross-referenced or noted):
- practice-10 (fee scenarios in proposals, D): already absorbed into professional-services-scoping-pricing-03.
- governance-14 (junior bid-writer development, D): evidence is the NBER patent-drafting trial, already held in
  talent-learning (professional-services-talent-learning-06, -07, -11); cross-referenced in module §3 and §7.
- discourse-16 (auto-populate team diversity data, D idea): a single item in an ABA list with no deployment and no
  discussion of accuracy or privacy; mentioned here only. Dropping it was a judgement on value, and it also kept the
  file at the 50% A/B line; reinstate it if the verifier prefers.

## 2. Duplicates merged

P = practice, D = discourse, G = governance.

| Out | Merged from | Grade decision |
|---|---|---|
| 01 First drafts from an approved library (Cherry Bekaert, Versent, Serco, unnamed Big 4) | P01, P08, G01, D05 | B (P01, P08 named deployments); G01 and D05 were C |
| 02 Archive search and chat (Ballard Spahr X-Ray; Benesch; Woodard & Curran) | D01, P02 | B kept |
| 03 Pitchbooks, proposals and CVs from structured data (GRSM, Stinson, Gowling, Neudesic, Arup) | P03, G17 | B (P03); G17 was C |
| 04 Bios regenerated from time records (Baker Botts) | D04 | B kept |
| 05 Record reconciliation before retrieval | D02 | C kept |
| 06 Requirement extraction, compliance matrix and red flags (Benesch) | P04, D06, G11 | B (P04); D06 C, G11 D |
| 07 Go/no-go from experience and win/loss data (Stinson) | P05, D07, G05 + DAYSHAPE routed | B (P05); D07 C, G05 D |
| 08 Pitch research brief (Baker Botts) | D03, G12, D14 | B (D03); G12 C, D14 D |
| 09 Urgent partner-drafted responses (Lynn Pinker Hurst & Schwegmann via Harvey) | P06 + HARVEY-LPHS-2025 routed | B kept (vendor anecdote, named firm) |
| 10 Executive summaries, win themes, one voice | G15, voice part of D09 | C |
| 11 Pre-submission accuracy and quality check | P09, G03, review part of D09 | C |
| 12 Firm-approved assistants instead of personal chatbots (Ballard Spahr Ask Ellis) | G02, D13 | B (D13 named deployment); G02 was C |
| 13 Tailoring vs signal loss | G10 | B kept (adjacent independent studies; capped) |
| 14 Proposal agents in PSA and experience platforms (Certinia, Kantata, Intapp) | P14, G04 + KM and delivery-management routed items | C |
| 15 Agentic pursuit workflows | D12, P07 | C; ladder delegate describes what sources discuss |
| 16 Win/loss and proposal-performance analytics | D08, G06, P11 | C; AI-moderated interviews (P11) cross-referenced to professional-services-client-development-18 |
| 17 Idea: answer bank for clients' AI questions, backed by matter evidence | G09, D11, G08 + LAWFUEL-2025 routed | D |
| 18 Idea: AI-use register for bid disclosure | G07 + CANBERRATIMES-APSAI-2025 routed | D |
| 19 Idea: bid-stage OCG and RFP terms flagging | P13, D15, G16 | D (routed back here by acceptance-risk) |
| 20 In-house buyers compare proposals (Priori Scout) | P12, D10, G13 | C |

**No grade was raised by merging.** Each merged entry carries the highest grade an input already gave a named
deployment. Overlaps are cross-referenced, not duplicated: client-development-05, -06, -07, -10, -12, -14 to -19;
scoping-pricing-02, -03, -05, -09, -10, -12; knowledge-management-04, -07; acceptance-risk-10, -11;
work-production-11, -22, -25; talent-learning-06, -07, -11. No assurance, tax or security entry covers pursuit.

**Source-key canonicalisation**

| Canonical key | Input keys or variants |
|---|---|
| HARVEY-BD-2026 | HARVEY-BDBLOG-2026 (practice); same URL; matches client-development |
| LAWSITES-CELESTE-2026 | LAWNEXT-CELESTE-2026 (practice); matches client-development and acceptance-risk |
| PPN-0224-2024 | UKGOV-PPN0224-2024 (practice, dated 2024-03); governance date 2024-03-25 used |
| SOURCE-PRECISION-2026 | SOURCE-INSIGHTS-2026 (client-development practice, routed); matches the client-development module |
| INTROHIVE-LAWSITES-2026 | typed `press` (governance typed it `survey`); matches client-development |
| CERTINIA-VEDA-2026 | dated 2026-10 (knowledge-management YAML uses 2026-10-19 for the same undated page) |
| ACCEVERLAW-2025 / EVERLAW-ACC-2025 | governance's in-house figures were not needed in this module; not carried |

**Provenance and field fixes.** Governance outcomes with `figure: null` and no provenance were rewritten as "none
published" with a vocabulary provenance. Benesch's qualitative compliance statement was relabelled `vendor-published`
(it appears in a Kantiv case study). Maturity for 10 and 11 was set to `emerging` (governance had `in-production` on
survey evidence alone) because the vocabulary requires a named organisation.

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 4 (07, 12, 17, 18) | 0 | 0 | 4 |
| augment | 11 (01, 02, 04, 06, 08, 09, 10, 11, 13, 14, 19) | 2 (16, 20) | 0 | 13 |
| automate | 1 (05) | 1 (03) | 0 | 2 |
| delegate | 0 | 1 (15) | 0 | 1 |
| **Total** | 16 | 4 | 0 | 20 |

- **Automate:** one in-production entry (03, B, template assembly from structured data) and one with no named
  customer (05, C).
- **Delegate:** one entry (15, C), resting on a vendor summary of the SMPS Q2 report, survey shares and Intapp's claim.
  No firm runs pursuit end to end through an agent.
- **Model scope: no evidence.** No source shows a new service, pricing or sourcing model arising from pursuit work.
  The nearest signals (partners and technical staff drafting, buyers reading bids with AI, Priori recommending a
  sourcing path) are recorded in 02, 09, 13 and 20 but do not meet the vocabulary's model definition. None was invented.
- **Process scope** is thin (4); most evidence is step-level help with drafting, retrieval and review.

## 4. Grade mix and maturity

- Grades: A 0, B 10, C 7, D 3. **No A is possible:** every firm figure is a recollection, estimate or projection
  (Cherry Bekaert, GRSM, Ballard Spahr, Baker Botts, Benesch, Woodard & Curran, Versent) or an undefined vendor figure
  (Serco, Neudesic, Arup, Certinia). Independent measurements exist only for adjacent processes (Ohio IT supplier bids,
  labour-platform cover letters, legal research hallucination, 2023 writing experiment).
- B grades rest on named deployments without measurement (01-04, 06-09, 12) and, for 13, adjacent independent studies.
- Maturity: in-production 10, announced 4, emerging 6.
- Firm kinds: law (Ballard Spahr, Baker Botts, GRSM, Stinson, Gowling WLG, Lynn Pinker Hurst & Schwegmann), engineering
  and AEC (Benesch, Woodard & Curran, Arup), accounting (Cherry Bekaert only), IT services and consulting (Versent,
  Neudesic, FOIL via Kantata, an unnamed Big 4 firm), government services (Serco, adjacent). In-house: 20 (entry) and
  parts of 17.

## 5. Items routed to pursuit-proposals from other modules

| Item | From | Used in |
|---|---|---|
| Lynn Pinker Hurst & Schwegmann won after an under-48-hour response (HARVEY-LPHS-2025, HARVEY-BD-2026) | client-development practice and discourse | 09 |
| Clients add AI clauses to RFPs and guidelines; few firms give hard data (LAWFUEL-2025) | client-development discourse | 17 |
| Latham role supports panels, pitches and RFPs (LATHAM-INNOVATIONATTY-2026) | client-development practice | 09; module §7 |
| Source Global Research buyer segmentation (SOURCE-PRECISION-2026) | client-development practice | 08 notes |
| Florida and ICMCI limits on AI claims in proposals (FLBAR-OP241-2024; ICMCI-AICODE-2026) | client-development governance | 17; module §6 |
| Certinia "8 hours to 1" headline (CERTINIA-VEDA-2026); 15-times-more-RFPs claim (CERTINIA-SOA-2026) | delivery-management practice and governance | 14 (headline as outcome; 15x in notes only, not checked) |
| Kantata Sales Accelerator and FOIL quote (KANTATA-ENGINE-2025); Intapp experience pitch generation (INTAPP-EXPERIENCE-2026) | knowledge-management practice and discourse | 14 |
| Legora posting: 90% of technical RFP content automated in six months (LEGORA-JOB-RFP-2026) | quality-review practice | module §8 only (*); Legora is a vendor |
| Reverse-auction win rates (TRI-ILTACON-2025) | scoping-pricing discourse | module §5 only (*) |
| APS planned-AI-use declaration in quote responses (CANBERRATIMES-APSAI-2025) | scoping-pricing governance | 18; module §6 |
| Capacity-aware bid/no-bid: 55% miss, delay or turn down work (DAYSHAPE-ONREC-2026) | staffing-resourcing governance | 07 |
| OCG and RFP terms flagged during a bid (idea) | acceptance-risk synthesis | 19 |
| Partner discomfort 35% (BIGHAND-LF-2026) | scoping-pricing discourse | Not used: client conversation, held by client-development-14 |
| Tailored CV and proposal generation from profiles (CINODE-2026) | staffing-resourcing practice | Not used: only a routing line; no pursuit detail read |
| Kantata Expertise Engine at FOIL via Consultancy.uk (KANTATA-CONSULTANCYUK-2025) | delivery-management practice | Not used separately: same quote taken from KANTATA-ENGINE-2025 |
| RFP buyers ask how firms use AI to cut cost (UNITEAI-KANTATA-2026); Narrative's RFP claims | staffing-resourcing discourse; scoping-pricing discourse | Not used: no pursuit passage or source row in the inputs |
| Legalweek "RFP 3.0" session (LEGALWEEK-RFP3-2026, search-only); Deloitte "Proposal Studio" posting (search-only) | pursuit practice and discourse | Not used: search-only |

## 6. Routed out from pursuit-proposals inputs (for the target modules' synthesis)

- **client-development:** Introhive partner survey and MCP server (INTROHIVE-LAWSITES-2026, INTROHIVE-MCP-2026); TRI
  Stand-out finding on partners discussing AI with clients (TRI-STANDOUT-2026); DealCloud relationship management
  (INTAPP-DEALCLOUD-2026); AI-search visibility and agent-to-agent discovery sessions (TRI-CMBDO34-2027, scheduled;
  LMA-RECORDINGS-2026); Projectworks' unsourced claim that over half of proposals are for existing clients
  (PROJECTWORKS-BD-2026).
- **scoping-pricing:** fee-scenario modelling (practice-10; ABA-LPMAI-2026 item 8; ABA-LPMRFP-2026); Certinia Estimate
  Creation, Estimation and SOW Drafter agents (CERTINIA-VEDA-2026); Priori pricing guidance (PRIORI-SCOUT-2026); GSK
  savings questions (TRI-LEGALWEEK-2026); LMA26 "Priced to Win" session (LMA-PRICED-2026); LLMs swayed by discount
  framing (UPPEREDGE-PROPTRAP-2026); Stanford pricing framework (STANFORD-DEL-2026).
- **billing-collections:** California fee rules on AI time and costs (CALBAR-GENAI-2026, p.8); ABA 512 fee guidance
  (ABA-OP512-2024); client line-item AI billing demands (TRI-LEGALWEEK-2026).
- **acceptance-risk:** BakerHostetler's Celeste use on intake and conflicts (LAWSITES-CELESTE-2026); OCG review (now
  entry 19 here); conflict risk when one matter's information informs another (ABA-OP512-2024, p.2 n.4); GSA draft
  LLM clause (FEDREG-GSA-2026); California GenAI deliverable disclosure (CALDGS-SCM2302-2025); Litera's AI-disclosure
  questions for vendor RFPs (LITERA-GCRFP-2026).
- **knowledge-management:** experience, CV and matter databases (IKAUN-ARUP-2026, IKAUN-GOWLING-2026, IKAUN-GRSM-2026);
  records reconciliation layer (entry 05).
- **staffing-resourcing:** Arup expert finder and Neudesic consultant matching (IKAUN-ARUP-2026, IKAUN-NEUDESIC-2026);
  matching team members to bids (STINSON-LAW360-2026; PROJECTWORKS-BD-2026).
- **talent-learning:** onboarding with AI (KANTIV-ROBINS-2026; Loopio 15%); NBER patent-drafting trial
  (NBER-AUTOR-2026); TR-FOP pipeline concerns (TR-FOP-2026); proposal-professional skills (NYREJ-SMPSNY-2026;
  VT-OPTIMIZE26-2026).
- **quality-review:** evaluator-side AI use and protest risk (NATLAW-BRADLEY-2026); scoring volatility
  (JBL-MCKINLEY-2026); Deloitte Australia refund (CTV-DELOITTE-2025, search-only in governance); Stanford hallucination
  study (STANFORD-MAGESH-2024); SRA and BSB notices (JMW-SRA-2026; MONDAQ-BSB-2026).
- **firm-finance:** AI ROI measurement (TR-AIPS-2026; LAWSITES-LITERA-2026; PATTERN-ALVAREZ-2025).
- **In-house flag (not a module):** ACC/Everlaw findings that 64% expect less reliance on outside counsel and that 9% of
  US respondents report policies prohibiting GenAI, down from 29% (EVERLAW-ACC-2025 / ACCEVERLAW-2025).

## 7. Judgment calls and corrections

- Serco (government services) and Robins & Morton (construction) are adjacent; Serco's figures are kept as undefined
  vendor outcomes and Robins & Morton's award-entry figure is not used.
- AutogenAI's customer page says Serco's revenue rose 5%; the Serco PDF says win rates rose 5%. The PDF is used.
- Loopio's blog says 47% expect better results; the report says 42%. The report is used.
- GRSM's headline says 50% in four months; the quote says over 50% in the first quarter after go-live. The quote is used.
- ikaun's release headline says over 25% of RFPs go unpursued; the body says 30% of the 76% that skipped RFPs cite
  lack of time or resources. Neither is used as a headline figure.
- The ABA column's "70-80% complete first draft" and Tribble's accuracy claims (search-only) are not used as outcomes.
- Baker Botts's 24-hour figure may refer to attorney onboarding rather than client preparation; the ambiguity is noted.
- The module's "Most surveyed teams are not cutting people" line reports survey answers only and sets no staffing view.

## 8. Gaps

- **No measured outcome:** no error, override, rework, parallel-run, inspection or win-rate measure for AI-assisted
  bids. Independent evidence is adjacent only.
- **Consulting and accounting:** one accounting firm (Cherry Bekaert) and no Big Four, MBB or mid-tier consultancy
  primary source; the Big 4 example is unnamed. Practice and governance ran out of searches before these queries.
- **Model scope and delegate rung:** no evidence of a pursuit-driven service or operating-model change, and no firm
  running an end-to-end pursuit agent.
- **Win/loss:** no named firm using AI for win/loss analysis; only vendor product documentation.
- **Client AI terms in RFPs:** no survey of how many RFPs or OCGs carry AI questions or restrictions; anecdotes and an
  ABA description only. No firm describes its answer bank or AI-use register.
- **Not opened or gated:** SMPS Foundation Q2 2026 report (vendor summary only), Loopio/Responsive/ikaun/QorusDocs full
  reports, Legalweek "RFP 3.0" session, SRA notice (secondary reports), LMA recordings, podcast audio, Intapp case
  studies, AutogenAI Jacobs and Kyndryl stories.
- **Dates:** ikaun, Versent, Certinia, DealCloud and AutogenAI customer pages are undated; years or read months are used.

## 9. Suggested improvements to the briefs

1. **Ship a shared source registry per wave** (key, title, URL, date, type). This module reconciled six key variants
   (Harvey, Celeste, PPN 02/24, Source, ACC-Everlaw, Introhive type) that other synthesis files had already settled.
2. **Define maturity for survey-only evidence.** Governance marked entries `in-production` because a survey shows wide
   use with no named organisation; the vocabulary says a named organisation is required. Say which wins.
3. **Forbid `figure: null` and missing provenance in outcomes.** Require "none published" with a real `source_ref`.
4. **Give consulting and accounting their own search budget** and name target sources (Big Four proposal studios,
   AICPA ENGAGE, MCA). The module is skewed to law and AEC firms.
5. **Fix the client-development / pursuit-proposals boundary in the brief:** client-development owns value
   conversations, matter evidence and win/loss interviews; pursuit owns RFP answers to AI questions and bid-level
   analytics. Three angles collected the same Legalweek, Stand-out and Introhive material.
6. **Require a source row for every routed key** (Cinode, UniteAI-Kantata, Narrative and Certinia's 15x claim arrived
   as one-line notes the target module cannot verify).
7. **Ask governance angles to point to the practice id** for named deployments, so merges do not have to rediscover
   which firm stands behind a rule-based entry.
