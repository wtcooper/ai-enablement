# Synthesis report: assurance / planning-risk-assessment

- **Prepared:** 2026-10-16
- **Inputs:** `landscape-assurance.md` (leads only, no YAML candidates), `assurance-planning-risk-assessment-practice.md`,
  `-discourse.md`, `-governance.md`
- **Outputs:**
  - module: `plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/assurance/modules/planning-risk-assessment.md` (299 lines)
  - use cases: `.../archetypes/assurance/use-cases/planning-risk-assessment.yaml` (25 entries)
- **Validator:** `python3 scripts/validate.py`: 0 errors. One warning for this file: 11 of 25 entries are graded A or
  B (44%), below the 50% target. Grades were not raised to clear it (see Grade mix).

## 1. Counts in and out

| Input | Candidates | A | B | C | D |
|---|---|---|---|---|---|
| practice | 24 | 0 | 13 | 7 | 4 |
| discourse | 22 | 0 | 6 | 10 | 6 |
| governance | 17 | 0 | 2 | 8 | 7 |
| **Total in** | **63** | 0 | 21 | 25 | 17 |
| **Out** | **25** | 0 | 11 | 9 | 5 |

Of the 63 candidates, 58 were merged into the 25 entries and 5 were not given their own entry because a
controls-testing pilot entry already covers the same change to the work (section 2b). Distinct source refs in the
YAML: 82 (vendor 21, press 18, regulator 12, professional-body 11, firm 7, academic 5, standard-setter 4, survey 3,
conference 1). The module's Sources section lists 13 more keys that are not in the YAML, with full details.

## 2. Duplicates merged

### 2a. Merge map (output id: input ids, P = practice, D = discourse, G = governance)

| Out | Title (short) | Merged from | Grade |
|---|---|---|---|
| 01 | Board-minutes and entity-document summaries | P01 (B), D01 (D), G01 (C) | B |
| 02 | Enterprise and grounded assistants for research and methodology | P13 (B), G17 (C), D02 (B) | B |
| 03 | Media-scanning agents (Deloitte) | P10 (B) | B |
| 04 | Audit-committee communications analysis (PwC) | P14, D05, G04 (all C) | C |
| 05 | Understanding the client's IT environment | G14 (C), P17 (C) | C |
| 06 | Idea: understanding the entity's own AI use | D18 (D), G13 (D) | D |
| 07 | ERP data ingestion (Grant Thornton gtap) | P15 (B) | B |
| 08 | Whole-population ledger analytics for risk identification | P06 (B), G05 (B), D10 (C), G07 (D) | B |
| 09 | Caseware Risk Suggestion Agent | P02 (B) | B |
| 10 | Agentic risk assessment linking evidence, assertions, materiality, procedures | P07 (C), D09 (C), D11 (D), G08 MindBridge part | C |
| 11 | Firm-platform agent frameworks for planning | P11 (B), D08 (C), G08 Deloitte/KPMG parts | B |
| 12 | Idea: chatbot drafts RMM (ICAEW test) | P20 (D), G09 (D) | D |
| 13 | Idea: multi-agent restatement-risk scoring (UMAR) | P22, D12, G06 (all D) | D |
| 14 | GenAI sounding board in fraud risk assessment | G11 (C), P18 (B) | C |
| 15 | Idea: AI-enabled fraud and evidence authenticity | D17 (D), G12 (D) | D |
| 16 | Idea: chatbot materiality (ICAEW test) | P21, D15, G10 (all D) | D |
| 17 | Scoping incl. group components | P24 (C), D06 (C), D16 (C), G08 PwC part | C |
| 18 | Prior-year planning document auto-population (PwC) | P04, D03, G03 (all B) | B |
| 19 | Planning-review gap check (Caseware demo) | P03 (C), G02 (C) | C |
| 20 | DAS methodology platform, mid-tier firms | P16 (B) | B |
| 21 | Engagement-level plan for AI and tool use | G15 (C) | C |
| 22 | Staffing and budget tool (RSM Luca Resourcing) | P12 (B), D13 (B) | B |
| 23 | AI savings negotiated into fees | D14 (C) | C |
| 24 | Continuous risk assessment and dynamic planning | P23 (D), G16 (D), D21 (C), D20 (C) | C |
| 25 | Internal audit work programs, risk considerations, scoping | D22 (B), P09 (C), P19 (B) | B |

### 2b. Placement decisions against the controls-testing pilot (referenced, not duplicated)

| Input candidates | Pilot entry used instead | Why |
|---|---|---|
| P05, D04 (walkthrough documentation: KPMG Copilot, PwC Advanced Walkthrough Assistant) | `assurance-controls-testing-01` | Same tools and same change. The module's §2 and §3 point to CT-01 for walkthroughs as part of understanding the entity. |
| P08, D19 (Optro Agentic Risk Assessment Scoring for internal audit planning) | `assurance-controls-testing-04` | CT-04 already names Optro's scoring alongside Microsoft's coverage targeting. Entry 25 notes the cross-reference. |
| D07 (PwC Australia AI-native platform: agents assess risk and design plans) | `assurance-controls-testing-17` | Same pilot. The module cites CT-17 under delegate. Date note: the pilot dates the Accounting Times article 2025-10-28 and the discourse file dates it 2025-10-27. |

Other cross-references, not duplicates: entry 11 uses the same platforms as CT-16 but covers planning, not tests of
controls. Entry 24 is the planning counterpart of CT-09 (continuous control testing). FJ Management's AI secondary
review is CT-10 and is mentioned only in entry 25's notes.

### 2c. Grade changes made in merging

- 14: practice graded the City of Charlotte slides B. The merged entry is C because the presenter speaks in a
  personal capacity, the setting is local-government internal audit, and the slides do not show the output was used
  on an engagement. The AFM observation names no firm.
- 01: kept at B (practice), above discourse (D) and governance (C). The grade rests on KPMG's present-tense statement;
  the notes record the disagreement.
- 08 and 24: an idea entry (G07, D) was folded into 08 (B). Entries graded D (P23, G16) were folded into 24, which is
  graded C because its only figure is a vendor claim.

### 2d. Source-ref reconciliation (where inputs disagreed)

| Chosen ref | Conflict resolved |
|---|---|
| EY-CANVAS-2026 = EY's own release (ey.com, 2026-04-07) | Discourse used the same ref for the CPA Practice Advisor article. Claims were checked against the EY release as the practice file read it. |
| KPMG-CLARA-2025 = kpmg.com release, 2025-04-22 | Practice read the Newsfile copy dated 2025-04-23. Noted in entry 01. |
| CASEWARE-VERITY-2026 = "CwX 2026" blog (2026-06-17); CASEWARE-AIDA-2026 = "From AiDA to agentic" (2026-07-28) | Governance used CASEWARE-VERITY-2026 for the AiDA blog. Practice's split was kept and governance's claims were re-keyed. |
| IFIAR-TTF-2026 URL `fsa.go.jp/ifiar/2026TTFReport.pdf` | Discourse gave the IFIAR news page and governance gave a different fsa.go.jp path. Both PDF URLs resolve (checked 2026-10-16). |
| OPTRO-CRX-2026 (not used in the YAML after the CT-04 decision) | Discourse called the same release OPTRO-AGENTS-2026. |
| IIAF-AIFRAUD-2026 | Governance called it IAF-AIFRAUD-2026. |
| CAQ-RSM-2026 date 2026-08-25 | Discourse gave 2026-08. |
| AICPA-PA-2026 and JOFA-AIPA-2026 typed professional-body | Practice typed AICPA-PA-2026 standard-setter and JOFA-AIPA-2026 press. The pilot lists AICPA and JofA under professional bodies. |

**Pilot key mapping.** The pilot used short keys without years. Equivalents: FRC-GENAI-2026 = FRC-GENAI;
IFIAR-TTF-2025 = IFIAR-TTF25; IFIAR-TTF-2026 = IFIAR-TTF26; IFIAR-SURVEY-2026 = IFIAR-2025F; PCAOB-TAA-2024 =
PCAOB-2024-007; PWC-AT-2025 = AT-PWC; CFODIVE-PWC-2026 = CFODIVE-PWC; KPMG-CLARA-2025 = K-CLARA; DELOITTE-OMNIA-2026 =
DELOITTE-OMNIA; CPACOM-ATR-2025 = CPACOM-ATR; TRI-FOP-2026 = TRI-FOP; AFM-12BB-2025 = AFM-12; NFRA-CAALLEY-2026 =
NFRA-CAALLEY; CPAB-AI-2024 = CPAB-AI; FRC-ATT-2025 = FRC-THEMATIC; FRC-SANDBOX-2026 = FRC-SANDBOX; PETERS-2022 =
PETERS; HOLMSTROM-2024 = HOLMSTROM; IIAF-AIFRAUD-2026 = IIAF-FRAUD; AICPA-PA-2026 = AICPA-PA; WCARS-2026 = WCARS75.

## 3. Coverage by ladder and change scope

| Ladder \ scope | step | process | model |
|---|---|---|---|
| assist | 02, 06, 12, 14, 15, 16, 21 | — | 23 |
| augment | 01, 03, 04, 05, 09, 10, 13, 17, 18, 19, 22, 25 | 08, 20 | — |
| automate | — | 07 | — |
| delegate | — | 11, 24 | (CT-17 in the pilot) |

- **Automate** has one entry (07, data ingestion). No source describes a planning step running with no person on the
  normal path. Entries were not invented to fill this.
- **Delegate** has two entries. 11 rests on platform announcements where planning-specific agents are not itemised.
  24 is a stated direction with no live external-audit case. PwC Australia's agent-built plans are CT-17.
- **Model** has one entry (23, fees), and its figures are second-hand. Structural model changes (AI-native firms,
  private-equity ownership) sit in acceptance-independence and the business-model lens.
- **Maturity:** 11 in-production, 4 piloting, 3 announced, 7 emerging.
- **Patterns:** six entries use `other`: 06 and 15 (procedures about the client's AI or AI-enabled fraud), 13
  (multi-agent risk-score fusion), 21 (plan for tool use), 22 (resourcing workflow) and 23 (pricing). See section 6.

## 4. Grade mix

- Out: A 0, B 11, C 9, D 5 (44% A/B). In: A 0, B 21, C 25, D 17.
- **No grade A.** No named organisation has published a measured outcome for AI in planning or risk assessment.
  Every B is a named deployment without measurement: KPMG, PwC, Deloitte, RSM, Grant Thornton, Caseware customers,
  EY and Helvetia Baloise.
- Five D entries were kept because each adds something the others do not:
  - 06 and 15: new planning topics created by client AI. The user asked for these.
  - 12 and 16: the only independent test of AI on RMM and materiality.
  - 13: the only quantitative research result.
- The share stays below 50% because the evidence base is thin, not because B entries were dropped. Raising 14 back
  to B would give 48%; the reasons for C are in 2c.

## 5. Gaps

- **Unevidenced steps (flagged as open questions in the module §3 and the probes):**
  - Materiality: one ICAEW test, no deployment.
  - Group-audit scoping: one generic vendor article and no AI-specific source. IFIAR shows three group-plan findings a year, unrelated to AI.
  - Fraud brainstorming in external audit: no firm named and no source on AI inside a live brainstorm.
- **No quality evidence.** No error rate, override rate, parallel run or inspection finding for any AI
  risk-assessment tool. The FRC found no firm quantified tools' quality impact.
- **Primary texts not read:**
  - AICPA practice aid (member-gated).
  - IAASB ED-520 and ED-330 (login-gated; read via the AUASB summary).
  - International ISA 315 (the UK adoption was read).
  - AS 2110 as amended for QC 1000.
  - The NFRA staff paper (press report only).
  - The FRC 2026 annual review (commentary only).
- **Named cases not retrieved:**
  - MindBridge customers (site 403).
  - PwC's promised risk-assessment tool (unconfirmed since Oct 2025).
  - KPMG's April 2026 orchestration announcement (Bloomberg Law opening only).
  - PayPal, Uniper and Microsoft internal audit planning cases.
- **Session content.** Conference and podcast material is at agenda level only (AAA, KU/Deloitte, ENGAGE, WCARS,
  ICAEW and SRA podcasts).
- **Budgeting and staffing** rest on one RSM tool whose AI content is unspecified.
- **Data conflicts left open:**
  - The ICAEW article's performance-materiality figures are internally inconsistent (practice reported Claude at
    60%; not used).
  - The KPMG fee figures are unconfirmed (landscape could not find them on Verdantix; FINSTORY cites the FT).
  - The PwC Australia article date (27 vs 28 Oct 2025).

## 6. Routed to other modules (collected from the inputs)

- **controls-testing:** walkthrough assistants (PwC, KPMG Copilot), already CT-01. AI-operated controls, COSO
  reliance and GITCs for AI components (AT-AICPAPA-2026, COSO-GENAI-2026). KPMG controls-testing agents
  (KPMG-CLARA-2025). Reddit's 175 controls and Klaviyo and FJ quotes (OPTRO-CRX-2026). SOX agent adoption article (CPA
  Practice Advisor, 18 Aug 2026, snippet only). ISACA AAIA credential (CPAPA-ISACA-2025). Multi-agent IT-audit evidence
  paper (arXiv 2608.07688, pilot abstract).
- **substantive-testing:**
  - KPMG expense-vouching and unrecorded-liability agents; KPMG orchestration pilots on asset valuation and revenue testing (BBL-KPMG-2026).
  - PwC Evidence Match, Audit Innovation Hub and Simplified Audit - Execute (CFODIVE-PWC-2026, CFOBREW-PWC-2025).
  - AuditCopilot journal-entry anomaly detection (ARXIV-AUDITCOPILOT-2025).
  - Journal-entry testing prevalence: 88% (IFIAR-TTF-2025).
  - Full-population testing and how to sell it (CPAPA-LEDGERLINE-2026).
  - Deepfakes used against auditors in confirmations (CAQ-INSIDERAPR-2026).
  - LLM document irregularity detection: 167 items, 74-96% correct at basic prompts (PL-YOAA-2025).
  - Benchmarks: ARXIV-FAB-2026, ARXIV-FINAUDITING-2025, ARXIV-LLMAUDIT-2025.
- **completion-reporting:** Caseware Disclosure Checklist Agent (2.7 hours per run, beta, vendor; UK availability 6
  Oct 2026). KPMG Financial Report Analyzer. FinancialAuditBench. PwC audit-committee communications tool (also entry
  04). FJ Management's secondary review of every workpaper. CAQ audit-committee webinar (CAQ-WEBINAR-2026).
- **quality-management:**
  - Firm level: RSM Ask Luca, a guidance copilot with 4,000+ users (CPAPA-ASKLUCA-2026; also in entry 02).
    IFIAR's unclear network versus member-firm monitoring responsibility. FRC certification, recertification and
    monitoring (FRC-ATT-2025, FRC-GENAI-2026). IFIAR governance and metrics. PCAOB Inspections Modernization Council
    and QC 1000 amendments. FRC sandbox. ACRA guidance.
  - Engagement level: supervision and review of AI output; automation-bias training; algorithm aversion and
    motivation effects (PETERS-2022, COMMERFORD-2022, HOLMSTROM-2024, FABIAN-2026); junior skill erosion as a
    supervision issue (ACCTODAY-BOTIC-2025).
- **acceptance-independence:**
  - Heavy client AI reliance treated like complex valuation models in acceptance and continuance (AT-AICPAPA-2026).
  - SEC Chief Accountant on independence when AI is part of audit delivery (KPMG-HOHL-2026).
  - Private-equity and fee pressure (ACCTODAY-BOTIC-2025, FINSTORY-KPMGFEE-2026).
  - Clark's claim of AI fieldwork for 35+ CPA firms (CLARK-JOB-2026).
  - Fieldguide funding and the BDO tie-up; Grant Thornton gtap under an alternative practice structure.
- **other-assurance / assurance over AI:** EY AI governance survey (CAQ-INSIDERSEP-2026). AICPA practice aid Part 1
  on entity AI and controls. EY's assurance over AI diagnostics, governance and controls (EY-CANVAS-2026). Reliance on
  SOC reports where the provider uses AI (AT-AICPAPA-2026).
- **specialists:** nothing specific to planning. The ISA 315 IT-risk viewpoint (ICAEW-315-2025) is kept here as
  entry 05, and practice also routes it to IT-audit specialists.
- **cross-cutting (business model and workforce):** AI investment, restatements and headcount (FEDYK-2022);
  workforce survey (TRI-FOP-2026); fee debate (entry 23).

## 7. Suggested improvements to the briefs

1. **Publish a canonical source-key registry per archetype**, seeded from the pilot and the landscape. Three deep
   dives working in parallel produced five ref conflicts: the same ref used for different documents (EY-CANVAS-2026,
   CASEWARE-VERITY-2026), different refs for one document (OPTRO-CRX/AGENTS, IIAF/IAF) and different URLs and dates.
   The pilot's year-less keys also break the PUBLISHER-SHORT-YYYY rule.
2. **Give deep dives the list of pilot use cases in adjacent modules.** Five candidates duplicated controls-testing
   entries (walkthroughs, Optro scoring, PwC Australia). A "check these ids first" list would save merge work and
   keep each change in one place.
3. **Agree one grading convention for regulator-observed, unnamed-firm use.** Governance graded this C (and maturity
   piloting); practice graded similar evidence B. Write the rule into the vocabulary.
4. **Ask deep dives to flag unevidenced module steps explicitly.** All three did this for materiality, group scoping
   and fraud brainstorming, which made the open-questions list easy to build. A required "steps with no evidence"
   field would make it consistent across modules.
5. **Propose new patterns.** Six of 25 entries needed `other`. Candidates:
   - `client-ai-procedure`: audit procedures about the client's own AI or AI-enabled fraud.
   - `risk-signal-scoring`: models or agents that score entity or account risk for a person to use.
   - `resourcing-pricing`: staffing, budgeting and fee setting.
6. **Ask for override and acceptance data by name.** No input found any. Interview briefs for this module should
   collect reviewer change rates on AI-suggested risks as a first-class metric.
7. **Shared search quota.** All three deep dives ran out of web-search quota part-way. Stagger the angles or raise
   the budget for modules rated High density.
