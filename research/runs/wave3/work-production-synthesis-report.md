# Synthesis report: professional-services / work-production

Prepared 2026-10-19. Outputs:
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/modules/work-production.md` (294 lines, table of contents)
- `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/use-cases/work-production.yaml` (25 entries)

`scripts/validate.py`: 0 errors; the work-production YAML reports 25 use cases, 18 graded A/B (72%). Every source key
in the module is in the YAML or in the module's Sources section (checked by script). No downloads were needed.

## 1. Counts in and out

| Input | Candidates |
|---|---|
| ps-work-production-practice.md | 21 (A 5, B 11, C 4, D 1; its own grades) |
| ps-work-production-discourse.md | 17 (A 5, B 4, C 4, D 4) |
| ps-work-production-governance.md | 16 (A 4, B 3, C 5, D 4) |
| Routed in from other deep dives | 5 items (see §6) |
| **Total in** | **54 candidates + 5 routed items** |
| **Out** | **25 use cases** (A 3, B 15, C 5, D 2) |

No candidate was dropped outright; every one was merged into an output entry.

## 2. Duplicates merged

| Out | Title (short) | Merged from (P = practice, D = discourse, G = governance) |
|---|---|---|
| 01 | Cited research, verified | P04, D11, G03 |
| 02 | Summaries, chronologies, transcripts, translation | P03, P11, D12, summarisation parts of D02 and G04 |
| 03 | Extraction and cited Q&A | P02, D02, G04; HARVEY-INDEMNITY-2026 routed from knowledge-management |
| 04 | Regulatory horizon scanning | P16 |
| 05 | First drafts from precedent | P05, D17; LEGORA-BMW-2026 and LAWSITES-MSFT-2026 routed from knowledge-management; LAWSITES-LITERA-2026 routed from quality-review |
| 06 | Drafting trial and skill effects (NBER) | P06, D01, G01 |
| 07 | Consulting analysis and deliverables; task allocation | P17, D08, G07, D16 |
| 08 | Playbook review and redlining in Word | P01, D03, G06 |
| 09 | AI red-teams a draft | P07 |
| 10 | Idea: challenger role | D14 |
| 11 | Pre-release check of citations, references, consistency | D10, G02, G13, P12 |
| 12 | Diligence over whole document sets | P08 |
| 13 | PwC task agents (extraction and mapping) | P18 |
| 14 | Data-room agent writes the memo | P09 |
| 15 | Matter templates with agent tasks and review gates | P10, D04, G09 |
| 16 | General-purpose agent workspaces; checkpoints and matter-scoped access | P21, D13, G16 |
| 17 | Legal engineers build playbooks, vaults, agents | P19, D07 |
| 18 | In-house lawyer-built workflow agents (DPIA) | P14 |
| 19 | In-house AI-first default and insourcing | P15, D06 |
| 20 | Shared AI workspaces with clients | P13 |
| 21 | Firm expertise packaged as agents for others | D05; Kirkland, A&O Shearman, Fried Frank detail routed from firm-finance (BLOOMBERGLAW-KIRKLAND-2026) |
| 22 | Gated rollout (policy, tools, training, review rule) | D09, G10, G11 |
| 23 | Test tools on own work, re-test | G14, G05, P20; EDRM-EMORY-2025 routed from quality-review |
| 24 | Idea: log edits and overrides | D15, G15 |
| 25 | AI-use records, disclosure, client AI terms | G08, G12 |

Source-key harmonisation inside the YAML: CHARLOTIN-HALLUCINATIONS-2026 and CHARLOTIN-HALLUC-2026 became
CHARLOTIN-DB-2026 (the key already used in the tax archetype); VALS-LEGALRESEARCH-2025 became VALS-VLAIRRES-2025;
LAWSITES-VALS-2025 became LAWSITES-VALSRESEARCH-2025; LAWSITES-ASTRA-2026 became LAWSITES-OPENAI-2026; EDT-ILTACON-2026
became EDISCOVERYTODAY-ILTACON-2026 (landscape key). NBER URL set to nber.org; Vals Feb 2025 URL set to the dated
report page. CALBAR-GENAI-2026 dated 2026-05-14 (board approval date found by the governance dive; the PDF is undated).

## 3. Coverage by ladder and change scope

| | step | process | model | total |
|---|---|---|---|---|
| assist | 3 (09, 10, 25) | 3 (22, 23, 24) | 0 | 6 |
| augment | 9 (01-03, 04-08, 11) | 5 (12, 17, 18, 19, 20) | 0 | 14 |
| automate | 1 (13) | 0 | 0 | 1 |
| delegate | 0 | 3 (14, 15, 16) | 1 (21) | 4 |
| total | 13 | 11 | 1 | 25 |

- **Automate** has one firm example (PwC, March 2025, outside the 18-month window). No evidence for automate at
  process scope.
- **Delegate** entries are all grade C (announcements or vendor benchmarks). No named firm reports delegating a
  whole workstream to an agent; the Law Society reports very limited autonomous use.
- **Model** scope has one entry (21), built on plans and an April 2025 announcement. Productised services without a
  professional in the loop (PwC One) were routed to scoping-pricing by the inputs; Kirkland's platform investment
  is in firm-finance. No entry was invented to fill these cells.

## 4. Grade mix and grading decisions

Final: A 3 (06, 07, 08), B 15, C 5 (04, 14, 15, 16, 21), D 2 (10, 24; both labelled "Idea"). A/B share 72%.

Decisions that differ from at least one input:
- **Vals and Stanford tool benchmarks are not grade A on their own.** Practice graded its extraction, summaries
  and research entries A; discourse graded extraction, research and chronology A; governance graded research and
  extraction A. All rest on tests of tools in isolation, not on a named organization's deployment, so they are B
  here (named firm deployments without measures). This matches the tax archetype, which graded Vals-only entries C.
- **Playbook review (08) is A** on Microsoft's tracked telemetry (about 70% of suggestions kept by 1,800+ users),
  labelled vendor-published and noted as an acceptance measure, not an error rate. Inputs graded it A, B and C.
- **Consulting (07) is A** on the HBS/BCG field experiment (two inputs A, practice B). Notes flag the 2023 model and
  researcher-designed tasks.
- **NBER (06) provenance is vendor-published** (Google built the assistant, ran and funded the study; two inputs
  said independent, one vendor-published). Grade stays A (preregistered trial, blinded scoring).
- **Merged ideas rose with their merges:** G05 and P20 (D) sit inside 23 (B, Vals consortium firms and Covington);
  G13 (D) sits inside 11 (B, Grant Thornton named); G10 and G11 (C) sit inside 22 (B, on Reed Smith's associate
  certification requirement). The C/D components are described as such in each entry's notes.

## 5. Routed to other modules (from the three work-production inputs)

- **delivery-management:** Harvey Legal Work Orchestration task, status and review-gate mechanics (HARVEY-ORCH-2026); Certinia PMO Quality, Project Manager, Sales-to-Delivery Handoff agents (CERTINIA-VEDA-2026).
- **pursuit-proposals / scoping-pricing:** Certinia RFP Responder and SOW Drafter agents (CERTINIA-VEDA-2026).
- **scoping-pricing:** PwC One and subscription tools without a person in the loop (CPAPA-PWC-2026); pricing for judgment rather than hours in tax and accounting (TRI-CHARGING-2026); consumption-based AI pricing worries (EDT-ILTACON-2026 = EDISCOVERYTODAY-ILTACON-2026); pricing models and observability of AI-reduced effort (STANFORD-DEL-2026); flat fees may build in AI savings (CALBAR-GENAI-2026 p. 8); about 60% of in-house respondents saw no savings (BLOOMBERGLAW-ACC-2025).
- **billing-collections:** client demands for AI line items and refusal to pay for AI-done work (TRI-LEGALWEEK-2026); hourly billing must reflect time spent, AI costs overhead unless matter-specific and disclosed without markup (ABA-OP512-2024 Part II.F; CALBAR-GENAI-2026 p. 8); IRS OPR on billing for unspent manual time (IRS-OPR-2026 item 2).
- **acceptance-risk:** Harvey Intake and Legora Intake for routing legal requests; Dentsu non-compete checks on new customers (HARVEY-DENTSU-2026); confidentiality, client consent and conflicts exposure from connected tools (ABA-OP512-2024 Part II.B; CALBAR-GENAI-2026 pp. 5-6); employment-related AI screening and bias (CALBAR-GENAI-2026 p. 9); shadow AI at 34% of professionals (TR-FOP-2026) and 54% of consultants (LEXISNEXIS-FOW-2026); firm policies by size (ILTA-TECHSURVEY-2026).
- **quality-review:** Deloitte Australia reference errors and disclosure (CTV-DELOITTE-2025); court-decision hallucination database (CHARLOTIN-DB-2026); ILTA human-review and verification policy rates (ILTA-TECHSURVEY-2026); deeper review-gate design overlapping work-production 11, 22 and 23.
- **talent-learning:** MinterEllison accelerator and legal-engineer cohort (LEGORA-MINTERELLISON-2026); Blank Rome Trial Academy practicums and 300-associate hackathon (HARVEY-BLANKROME-2026); NBER junior-skill findings (NBER-AUTOR-2026); 48% fear harm to judgment development (TR-FOP-2026); Duane Morris onboarding redesign (TRI-ONBOARD-2026); pyramid and hiring data (VAULT-PYRAMID-2026); Allens supervision (ALLENS-XEXAM-2026); legal writing pedagogy (TRI-CLARITYWRITE-2026); junior consultant learning (STRATEGYCASE-JUNIOR-2026); Choi, Monahan and Schwarcz on limiting first-year law students' AI use (LEGALFUTURES-CHOI-2023); ICMCI assessment-integrity rules, sections 5.2 and 6 (ICMCI-AICODE-2026).
- **client-relationship-development:** RSGI finding that 61% of law firms proactively discussed Harvey efficiencies with clients while 4% of in-house teams say their firms approached them (LEGALIT-RSGI-2026); Reed Smith's claim that partners win work through AI-enabled delivery (HARVEY-REEDSMITH-2026); about one-third of embedded-AI partners have discussed AI with 60%+ of clients (TRI-STANDOUT-2026).
- **knowledge-management:** Hogan Lovells Cadwalader knowledge-management agents and shared playbooks (HARVEY-HLC-2026); Harvey Horizon Scanning; Blank Rome brief bank; firms extracting lawyers' knowledge into workflows (VAULT-PYRAMID-2026). Work-production 04 and 17 overlap.
- **firm-finance:** Harvey Command Center analytics (named on the platform menu, not read); ROI measurement and strategy gaps (TRI-LEGALWEEK-2026; TRI-STANDOUT-2026: 25% strongly agree their firm has a plan for monetising AI usage); platform market concentration (LAWSITES-PEAK-2026; EDISCOVERYTODAY-ILTACON-2026).
- **staffing-resourcing:** EU AI Act high-risk employment rules extended to 2027-12-02 (EC-AIACT-2026).
- **Tax archetype:** more than 70% of tax firms automate up to a quarter or more of tax workflows (TRI-CHARGING-2026); EY and KPMG agent platforms (ICAEW-AI2026-2026); Circular 230 and AICPA tax-section material (IRS-OPR-2026; AICPA-TAXAI-2026).
- **Assurance archetype:** EY, KPMG and Deloitte audit-agent announcements; FRC audit-quality findings on AI monitoring (landscape lead, not read); PCAOB and IAASB material; PwC and Legora tax and audit legal-engineer roles seen in job feeds.
- **Legal-practice extension (litigation, e-discovery), if one is built:** AI document review products and validation derived from technology-assisted review (LAWSITES-ILTACONROUND-2026; EDT-CROWD2-2026); Thomson Reuters Institute and ILTA AI Guide for Litigators (TRI-AIGUIDELIT-2026).

## 6. Picked up from other modules' "Routed to" sections

| From | Item | Where used |
|---|---|---|
| ps-knowledge-management-practice | Microsoft precedent drafting (LAWSITES-MSFT-2026); BMW first drafts from approved standards (LEGORA-BMW-2026); Harvey review tables (HARVEY-INDEMNITY-2026); Vals benchmarks | 05, 03 |
| ps-firm-finance-practice | Kirkland fund formation engine; A&O Shearman and Fried Frank plans (BLOOMBERGLAW-KIRKLAND-2026) | 21 |
| ps-quality-review-practice | Microsoft Legal Agent and Litera Lito drafting (LAWSITES-LITERA-2026); Covington e-discovery test-set validation (EDRM-EMORY-2025) | 05, 08, 23 |
| ps-quality-review-governance | Vals task benchmarks and HBS productivity figures | 02, 03, 07, 08, 23 |

The firm-finance discourse, client-development, pursuit-proposals, scoping-pricing, talent-learning and
knowledge-management discourse and governance files route nothing to work-production.

## 7. Gaps

- **No deployer quality data.** No firm, in-house team or consultancy publishes error, override, recall or
  parallel-run rates for AI-assisted drafting, extraction, research or review. Measured evidence is tool benchmarks
  (Vals, Stanford), two trials (NBER, HBS/BCG), vendor telemetry (Microsoft) and incident records.
- **Consulting and accounting thin.** McKinsey, BCG, Bain, Deloitte, EY and KPMG primary pages were blocked or empty.
  Consulting rests on HBS/BCG (2023), Deloitte incidents, a LexisNexis blog summary and a coaching site. Accounting
  rests on Grant Thornton UK forensic and PwC Agent OS (2025). Engineering and architecture: nothing.
- **Vendor-hosted case studies.** Nearly every named legal example sits on Harvey or Legora pages.
- **Delegate and model levels** have no named deployment (see §3).
- **In-house beyond legal** (finance, HR, shared services working like firms): none found.
- **Dates:** Legora customer pages show a "joined" month, not a publication date (Goodwin, Grant Thornton,
  MinterEllison, Crowell); TR Future of Professionals and the Law Society pages are undated; the Ivo release is undated.
- **Conflicting counts:** Vals research questions 200 (Vals page) vs 210 (LawSites); Vals redlining Harvey 59.4%
  (text) vs 65.0% (table). Both are shown with their source.

## 8. Suggested improvements to the briefs

1. **Publish a shared source-key registry per wave.** The same document carries different keys across files:
   Charlotin database (CHARLOTIN-DB-2026 in tax; CHARLOTIN-HALLUCINATIONS-2026 and CHARLOTIN-HALLUC-2026 in PS
   inputs); Stanford hallucination paper (STANFORD-HALLUC-2024 in tax; STANFORD-MAGESH-2024 here, kept to match
   every PS input). **Collision:** tax `research-advisory.yaml` uses VALS-VLAIR-2025 for the October 2025 Vals
   research report (vlair-10-14-25), while every PS file uses VALS-VLAIR-2025 for the February 2025 report; this
   file uses VALS-VLAIRRES-2025 for October. The tax key should be renamed.
2. **Fix field values for recurring documents in one place.** Within professional services, the scoping-pricing
   YAML gives CALBAR-GENAI-2026 as 2026-05 (this file: 2026-05-14), ILTA-TECHSURVEY-2026 as professional-body (this
   file: survey) and TR-FOP-2026 as 2026-09 (this file: 2026). EC-AIACT-2026 and CHARLOTIN-DB-2026 carry read
   dates that differ by file. The coordinator should pick one value each.
3. **State the A-grade rule for tool benchmarks and trials explicitly.** The deep dives split on whether an
   independent benchmark of tools (Vals) or a field trial (NBER, HBS) meets "measured outcome from a named
   organization". A one-line rule (benchmarks of tools in isolation are B at most, and only with a named deployment;
   trials with practising professionals can be A) would remove most regrading.
4. **Ask deep dives to record provenance for sponsored studies consistently** (NBER was run and funded by Google;
   two dives said independent).
5. **Give the work-production brief a consulting- and accounting-first search budget.** Three dives ran out of
   shared search budget, and all three ended legal-heavy.
6. **Ask for the firm type tag in each use case's notes** (law firm, in-house, consulting, accounting, Big Four), so
   synthesis does not have to reconstruct it.
