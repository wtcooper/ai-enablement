# Synthesis report: professional-services / scoping-pricing

- **Date:** 2026-10-19
- **Inputs:** `landscape-professional-services.md`, `ps-scoping-pricing-practice.md`, `ps-scoping-pricing-discourse.md`,
  `ps-scoping-pricing-governance.md`, plus the "Routed to other modules" sections of every other `ps-*.md` file in
  `research/runs/wave3/` (items routed to scoping-pricing).
- **Outputs:** `plugins/.../archetypes/professional-services/modules/scoping-pricing.md` (290 lines, contents list at
  top) and `plugins/.../archetypes/professional-services/use-cases/scoping-pricing.yaml` (23 entries).
- **Validator:** `python3 scripts/validate.py` gives 0 errors for these files; 23 entries, 61% graded A/B (meets the
  15-25 and 50% targets). A script check confirmed every source key cited in the module is in the YAML or in the
  module's Sources list (4 keys marked *), and every inline key in a YAML entry is in that entry's sources.
- No downloads were needed; all facts come from the input files.

## 1. Counts in and out

| | Practice | Discourse | Governance | Routed from other modules | Total |
|---|---|---|---|---|---|
| Candidates in | 17 (0 A, 8 B, 6 C, 3 D) | 16 (0 A, 5 B, 7 C, 4 D) | 18 (0 A, 6 B, 5 C, 7 D) | 3 entries (2 B, 1 D) plus evidence items | 51 + 3 |
| Out | | | | | **23 (0 A, 14 B, 8 C, 1 D)** |

No candidate was dropped outright; every one was merged into an output entry. Routed entries used: firm-finance-02
(Norton Rose Fulbright hourly billing, B), client-development-12 (firm-built AI tools licensed to clients, B) and
pursuit-proposals-10 (fee scenarios in RFP responses, idea). Routed evidence items used: ACC-Everlaw release
(ACCEVERLAW-2025), AL-CLIENT-2026, ICAEW-EXPECT-2026, TRI-LAWYERDEV-2026, IRS-OPR-2026, ABA-OP512-2024 (read in
full by two other governance angles), BLOOMBERG-AICOST-2026 (module metrics only).

## 2. Duplicates merged

P = practice, D = discourse, G = governance.

| Out | Merged from | Grade decision |
|---|---|---|
| 01 Scoping and solution-architecture drafts (Spaulding Ridge, Diabsolut) | P13 | B kept |
| 02 PSA estimating agents (Certinia) | P11, D02 (estimate part), G18 (estimate part) | C |
| 03 Fee proposals from comparable past matters (Ayora, Narrative, August, job postings) | D01, P03, P04, pursuit-proposals-10 (D) | C |
| 04 Fixed-fee benchmarking (Goodwin, PERSUIT; in-house buyer side) | P01, P02 | B (Goodwin) |
| 05 SOW drafting agent (Neocol) | P12, D02 and G18 (SOW parts) | B kept |
| 06 Hourly matters on actual AI-assisted time | G01 (D), firm-finance-02 (B) | **B, raised from G01's D** by the routed Norton Rose statement; notes say no firm describes re-basing estimates |
| 07 AI use, approval and cost terms in fee agreements | G14 (C), D12 (D), G15 (D) | C; consumption-cost part labelled idea |
| 08 Budget-overrun alerts | D10 | C |
| 09 Matter-level AI value evidence (Legora-Laurel) | D09, G10, P15 (D) | C |
| 10 Partner-led AI-value conversation | G16 (C), D16 (D) | C |
| 11 Clients press for AI savings (in-house; KPMG-Grant Thornton) | D03, G11, D11 (B) + routed ICAEW, AL, TRI-LAWYERDEV, ACC release | B, resting on the KPMG case, consistent with assurance-acceptance-independence-21 (B) |
| 12 Public-sector buyer recourse and AI declarations | G12 (B), G13 (D) | B (Deloitte refund); APS part is announced policy |
| 13 Staff metrics off billed hours (Wipfli) | G07 + discourse role notes | B |
| 14 Idea: observability map and outcome-fee baselines | P17, D08, G08, G09 (all D) | D, labelled idea |
| 15 Flat fees and AFAs with AI savings priced in (law) | D04 (C), G02 (D), D15 (D), P16 (D) | C |
| 16 Accounting and tax value, tiered and subscription pricing | P10, D13, G06 (all B) | B |
| 17 Where the AI time dividend goes | P14 (C), D14 (C), G17 (D) | C |
| 18 Kopka Law KPI retainer | D05, G03 | B |
| 19 McKinsey outcome-linked fees | P07, D06, G04 | B |
| 20 IT services outcome contracts and savings splits | P08 (B), P09 (C) | B |
| 21 AI-native law firms, flat or per-document prices | P05 | B |
| 22 PwC One | P06, D07, G05 | B |
| 23 Law firms license firm-built AI tools | client-development-12 (routed) | B |

**No grade was raised by merging alone.** Entry 06 went from D to B because a routed named deployment (Norton Rose) is
the same change at the billing end; this is flagged in its notes. Entry 11 keeps D11's B.

**Source-key canonicalisation**

| Canonical key | Input keys or variants |
|---|---|
| BLOOMBERGTAX-PRICING-2026 | BLOOMBERGLAW-ACCTPRICING-2026 (practice), BLAW-ACCT-2026 (discourse); bloombergtax.com URL used |
| AIWEEKLY-MCK-2026 | AIWEEKLY-MCK-2025 (discourse, landscape); page dated 2026-06-29 |
| TRI-KOPKA-2026 | TRI-BILLING-2026 (governance); same URL |
| BLOOMBERGLAW-ACC-2025 | ACCEVERLAW-BL-2025 (discourse); typed press. The ACC-Everlaw press release is a separate document (ACCEVERLAW-2025) |
| FORRESTER-TECHSVCS-2026 | FORRESTER-SOTS-2026 (discourse) |
| BI-MCKINSEY-2025 | Yahoo Finance syndication URL used: practice found the Business Insider URL not found; governance cited it as read |
| EDISCOVERYTODAY-ILTACON-2026 | typed conference (discourse typed press); EDT-ILTACON-2026 in work-production is the same post |
| TRI-LFFI-Q1-2026, TRI-SOTLM-2026 | typed survey (practice typed press) |

Date choices: CALBAR-GENAI-2026 `2026-05` (inputs gave 2026, 2026-05 and 2026-05-14); TR-FOP-2026 `2026-09` (page
metadata per governance); SPI-AI-2026 `2026-10` (practice and discourse read a 2026-07-14 page timestamp; the page lists
the report as published October 2026) - unresolved; undated vendor pages dated by read month `2026-10`.

## 3. Coverage by ladder and change scope

| | step | process | model | Total |
|---|---|---|---|---|
| assist | 04, 06, 07, 12 | 10, 11, 13, 14 | 15, 16, 17, 18, 19, 20 | 14 |
| augment | 01, 02, 03, 05 | 08, 09 | 23 | 7 |
| automate | none | none | none | 0 |
| delegate | none | none | 21, 22 | 2 |
| Total | 8 | 6 | 9 | 23 |

- **Automate: no evidence.** No source describes a scoping, estimating or pricing step with no person on the normal
  path. The nearest are draft time entries (09) and budget alerts (08), both reviewed by people.
- **Delegate: only inside new service models** (AI-native law firms, PwC One). No agent is shown owning a scope,
  estimate or price.
- **Ladder is nominal for pricing-model entries** (15-20, 13, 14): AI changes delivery effort, not the pricing step.
  The YAML notes say so.

## 4. Grade mix

0 A, 14 B (61%), 8 C, 1 D. **No A is possible:** no named organisation publishes a tracked metric for AI in scoping or
pricing. The figures that exist are executives' approximate statements to reporters (McKinsey about 25%, TCS about
80%), vendor-published customer stories (Certinia), vendor surveys (BigHand, ACC-Everlaw, TRI) or one fee change reported
via the FT (KPMG). Under the 2026-10-17 rule these are B at most. Most B entries are named **pricing-model** changes;
only 01, 04 and 05 are named **AI tools** in the pricing workflow, all vendor-published.

## 5. Gaps

- **No quality evidence:** no estimate-versus-actual, override, win-rate, margin or parallel-run data for AI-built
  estimates, scopes or fee proposals, from any source.
- **No automate entries; delegate only at model level** (see §3).
- **Primary documents not reached:** FT and WSJ originals (PwC, KPMG, McKinsey figures are secondary), McKinsey's own
  pages, Forrester Wave Q2 2026 (search snippet only, so not used as evidence), SPI report body, AICPA 2025 pricing
  survey, Kantata's "Fact or fiction" outcome-pricing post (404).
- **Sector skew:** governance is mostly US legal ethics. No SRA, Law Society, ICAEW, IESBA or MCA guidance on passing
  AI savings to clients; no consulting fee rule found; architecture and engineering only via Deltek; no in-house
  shared-service examples outside legal.
- **Conflicts kept visible:** McKinsey share (25% vs 20% vs "about a third"); ACC-Everlaw sample (657 vs about 650);
  KPMG entity (KPMG International vs other); the 22% TRI figure used two ways; SPI date.
- **Not used:** Ron Baker and ABA Business Law podcasts, Kerbis and Furlong podcast show notes (summaries only); Litera
  webinar promotion; Narrative's 18% write-off claim and Certinia's 11-23% margin claim (unattributed).

## 6. Routed to other modules (collected from the inputs)

| Item | Target | Sources |
|---|---|---|
| Laurel-Legora draft time entries; AI line items and single "services rendered" bills; billing rules after the fee is agreed; Intapp Time | billing-collections | LEGORA-LAUREL-2026, TRI-LEGALWEEK-2026, CALBAR-GENAI-2026, TXETHICS-OP705-2025, DCBAR-OP388-2024 |
| Rate growth, realisation, LFFI, AI-bubble warning, Citi H1 2026, SPI time-versus-revenue gap, AI vendor seat vs consumption cost, Norton Rose policy, PE and outside capital | firm-finance | TRI-LFFI-Q1-2026, TRI-LFFI-Q2-2026, TRI-SOTLM-2026, TRI-RATES-2025, BESTLAWFIRMS-CITI-2026, SPI-AI-2026, EDISCOVERYTODAY-ILTACON-2026, BLOOMBERGLAW-TEXAS-2026 |
| Harvey Legal Work Orchestration; Certinia PMO Quality scope scans; budget-overrun alerts (also here as 08) | delivery-management | HARVEY-ORCH-2026, CERTINIA-VEDA-2026, AYORA-LTH-2026 |
| Certinia Staffing Agent (Nextview); hybrid human-agent teams; outcome data in staffing | staffing-resourcing | CERTINIA-CUSTOMERS-2026, KANTATA-RMI-2026 |
| Partner AI conversations; 32% of clients reconsidering; conversation playbook | client-development | TRI-STANDOUT-2026, TR-FOP-2026 |
| RFP pricing analytics, reverse-auction win rates, Certinia RFP Responder and Deal Coach, AI-use declarations in quote responses, Priori Scout | pursuit-proposals | TRI-ILTACON-2025, CERTINIA-VEDA-2026, CANBERRATIMES-APSAI-2025, PRIORI-SCOUT-2026 |
| Junior training under AFAs; NBER patent trial; Wipfli metrics; early-career development | talent-learning | ILTA-PULSE-2025, NBER-AUTOR-2026, BLOOMBERGTAX-PRICING-2026, TR-FOP-2026 |
| Deloitte Australia and Newfoundland errors; hallucination and Vals benchmarks; supervision duties | quality-review | CTV-DELOITTE-2025, BNN-DELOITTE-2025, STANFORD-MAGESH-2024, VALS-VLAIR-2025, CALBAR-GENAI-2026 |
| Confidentiality, agentic access, client-approval policies | acceptance-risk | CALBAR-GENAI-2026, ILTA-TECHSURVEY-2026 |
| AICPA contingent-fee and attest-fee rules; KPMG audit-fee case; tax fee guidance | assurance and tax archetypes (cross-referenced by id, not duplicated) | AICPA-CODE-2026, YAHOO-KPMG-2026, IRS-OPR-2026 |

## 7. Suggested improvements to the briefs

1. **Share a canonical source-key list before the deep dives.** Five documents arrived under two or three keys (Bloomberg Tax
   article, AI Weekly, Kopka, ACC-Everlaw, Forrester), and others had conflicting types, dates or URLs (eDiscovery Today,
   LFFI, SOTLM, Business Insider, SPI).
2. **Say whether routed entries may raise a grade.** Entry 06 moved from D to B on evidence another module holds; a
   one-line rule (allowed, with a note, when the routed item shows the same change) would keep modules consistent.
3. **Add a marker for pricing-model entries.** Over half of this module describes a pricing or business-model change
   where AI is the cause, not the tool. A field such as `ai_role: tool-in-step | cause-of-change` would make the
   ladder coverage table honest.
4. **Give a provenance rule for co-published surveys** (a professional body with a vendor, e.g. ACC with Everlaw).
   Angles labelled the same survey `independent` and `vendor-published`.
5. **Fix the date convention for undated live pages** (read month vs read day); inputs used both.
6. **Budget searches per angle and protect one for primary documents.** Practice and governance ran out after eight
   searches, before reaching FT/WSJ originals, consulting-firm pages and non-US regulators.
7. **Ask governance angles for non-US and non-legal fee rules explicitly** (SRA, ICAEW, IESBA, MCA, professional
   indemnity insurers), since US legal ethics dominated.
