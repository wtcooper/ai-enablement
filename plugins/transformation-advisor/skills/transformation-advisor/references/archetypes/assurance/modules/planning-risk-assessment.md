# Planning and risk assessment (assurance)

Last reviewed 2026-10-16. Use cases live in `../use-cases/planning-risk-assessment.yaml` (25 entries). Ids are
shortened: `#05` means `assurance-planning-risk-assessment-05`; `CT-04` means `assurance-controls-testing-04` in the
pilot, which holds walkthroughs (CT-01), risk-scored coverage targeting (CT-04) and the PwC Australia AI-native pilot
(CT-17). Source keys in brackets are in the YAML or §10. No entry reaches grade A: no named organisation has published a
measured outcome for AI in planning; every figure is self-reported, vendor-claimed or a prevalence count. Say so.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

The start of an audit: understanding the entity and its environment (including its IT and its own AI use), risk
assessment procedures and analytics, identifying and assessing risks of material misstatement (RMM: the risk the
financial statements are materially wrong, assessed at statement and assertion level), fraud risk assessment and
team brainstorming, materiality, scoping (including group components), strategy and planning documents, and
budgeting and staffing. It also covers internal audit's risk assessment and audit planning. Standards: ISA 315
(Revised 2019) and AS 2110 for risk assessment, ISA 240 for fraud, ISA 320 for materiality. AI here is mostly first
drafts for a person to review; the standards are permissive, and the main risk is the tool's output becoming the
conclusion.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Understand the entity and its IT | Read minutes and documents, research industry, inquire, walk through processes | research-synthesis, review-assurance | Reading is slow and items are missed; walkthroughs redone yearly (CT-01) |
| Understand the entity's own AI | Ask where AI touches reporting and controls, and how it is governed | review-assurance, expert-judgment | Partners rate only 6% of largest clients' AI governance advanced [CAQ-INSIDER-2026]; AS 2110 has no AI wording |
| Risk assessment procedures and analytics | Inquiry, analytical procedures, observation, inspection; ledger analytics | data-reporting | Poor client data (60%) and no system access (53%) block analytics [CPACOM-ATR-2025] |
| Identify and assess RMM | Inherent and control risk by assertion; significant risks; rationale | expert-judgment | 60% of US firms prioritise carrying forward last year's risk assessment [CPACOM-ATR-2025] |
| Fraud risk and team discussion | Fraud risk factors, the presumed revenue risk, brainstorming with the partner | expert-judgment | Bias and blind spots; AI-enabled fraud new: 62% of IA leaders unprepared [IIAF-AIFRAUD-2026] |
| Materiality | Benchmark, percentage, performance materiality, rationale | expert-judgment, data-reporting | Inspectors check year-on-year rises driven by fee pressure [PCAOB-PRIORITIES-2024] |
| Scoping, incl. group components | Which accounts, locations and components are in scope | expert-judgment | Built from prior-year files; multi-location scoping is an inspection focus |
| Strategy, plan, planning review | Planning memo, risks linked to procedures, planned tool use, review | document-production, coordination-scheduling | 85% of US firms prioritise rolling binders forward [CPACOM-ATR-2025]; unclear where GenAI was used [AFM-12BB-2025] |
| Budget, staffing, fees | Staffing requests, hours budget, fee | coordination-scheduling, client-interaction | Manual processes (RSM); clients asking for AI discounts |
| Ongoing reassessment | Revise risks when evidence contradicts them (AS 2110 .74) | expert-judgment | Set at planning; revised only when the team notices contradicting evidence |
| Internal audit planning | Audit universe, annual and multi-year plan, engagement scoping | expert-judgment, coordination-scheduling | Plans age in-year; 9% of CAEs report adequate coverage of digital disruption [AUDITBOARD-RIF-2026] |

Inspection context: IFIAR's 2025 survey found a risk-assessment finding in 44 of 770 inspected listed audits (6%;
53 findings), versus 14% for internal control testing [IFIAR-SURVEY-2026]. These are findings on risk assessment
generally; no inspection finding specific to an AI risk-assessment tool was found.

## 3. Where AI is changing the work

Lenses: improve (assist/augment a step), automate (no person on the normal path), delegate (an agent owns a multi-step
outcome), reinvent (model changes). Improve dominates; automate has one entry; delegate is stated design only.

**Understanding the entity and its environment**
- Improve: `#01` cited summaries of board minutes (KPMG Clara; FRC worked example; the reviewer still reads the
  minutes). `#02` enterprise and grounded assistants for entity research and methodology (KPMG 2.175M Audit Chat
  conversations; RSM Ask Luca; PwC ChatNational). `#03` Deloitte agents scan media for emerging threats and draft
  staff memos. `#04` PwC tool analyses audit-committee communications (announced). `#05` access-rights analytics
  and guided IT-risk identification (AFM good practice; vendor viewpoint). Walkthrough narratives: see CT-01.
- New planning topic (idea): `#06` understanding the client's own AI use (AICPA practice aid Part 1, ISA 315
  Appendix 5). No firm has published results; AICPA RMM guidance for AI-using clients is still to come.

**Analytics and risk identification**
- Automate: `#07` Grant Thornton gtap standardises ERP data ingestion (private-company audits first).
- Improve: `#08` whole-population ledger analytics (RSM, KPMG Transaction Scoring; ISA 315 A203); IFIAR members see
  tools in risk assessment frequently in 55% of responses. `#09` Caseware Risk Suggestion Agent drafts
  engagement-specific risks (launched 6 Oct 2026). `#10` agentic risk assessment linking evidence, assertions and
  materiality (MindBridge, announced) and risk-to-procedure agents (Wolters Kluwer future state).
- Delegate: `#11` firm-platform agent frameworks (EY Canvas "all phases", Deloitte Omnia, KPMG orchestration pilots);
  planning-specific agents are not itemised. CT-17: PwC Australia says agents will assess risk and design plans
  (5 pilot clients, all by 2028).
- Ideas and tests: `#12` chatbot RMM drafting failed ICAEW's test; `#13` multi-agent restatement-risk scoring
  (research prototype, AUROC 0.782).

**Fraud risk assessment**
- Improve: `#14` GenAI as a sounding board after the team's own assessment (AFM, unnamed firms; one practitioner demo).
- New topic (idea): `#15` AI-enabled fraud schemes and fabricated evidence in fraud risk factors (ISA (UK) 240 A101, A36).

**Materiality and scoping**
- Ideas: `#16` chatbot materiality (models disagreed). `#17` scoping tools: PwC's planned tool not seen since Oct 2025;
  group audits have one generic vendor article.

**Plan, review and governance of the plan**
- Improve: `#18` PwC auto-populates the planning document from prior-year information. `#19` in-file agent checks
  the planning file for gaps (Caseware demo). `#20` DAS methodology platform at EisnerAmper, Citrin Cooperman,
  PKF O'Connor Davies (process change). `#21` the audit plan states which tools are used and for which risks (AFM, IFIAR).

**Budget, staffing and fees**
- Improve: `#22` RSM Luca Resourcing for staffing requests and budgets (AI content unspecified).
- Reinvent: `#23` clients negotiating AI savings into fees (KPMG and its auditor; figures second-hand).

**Continuous risk assessment and internal audit**
- Delegate (direction of travel): `#24` continuous risk assessment and dynamic plans; no live external-audit case.
- Improve: `#25` internal audit work programs, risk considerations and risk-to-control scoping (Helvetia Baloise,
  Fieldguide, FJ Management vision). Audit-universe risk scoring (Optro): see CT-04.

**Open questions: steps with no evidence of AI use in practice.** Materiality (`#16`: one ICAEW test, no deployment),
group-audit scoping (`#17`: no source on AI component scoping beyond one vendor article), and fraud brainstorming
in external audit (`#14`: no firm named; no source on AI inside a live brainstorm). Also: risk-assessment agents with
override or acceptance data, and any parallel run against a human risk assessment. Probe these; do not assume.

## 4. Interview probes

Ask in the person's own setting (audit firm partner or manager, methodology lead, CAE).

1. **"Walk me through the last risk assessment. Which inputs did AI touch (minutes, prior-year file, analytics,
   research), and what did the reviewer do with the output: re-read the source or accept it?"** Reveals whether review
   is designed (FRC pattern, `#01`) or improvised, and the automation-bias exposure.
2. **"Which planning outputs now start from an AI draft, and do you record how often reviewers change or reject
   it?"** Reveals whether any quality evidence exists. No vendor or firm has published override rates (`#09`, `#19`).
3. **"On the file, does it say the tool's output was used to focus your work or to reach a conclusion?"** Reveals the
   FRC's key misuse risk and inspection readiness.
4. **"When a tool rates an account or entity low risk, who tests that rating, how often, and what happens when the
   model or vendor changes?"** Reveals whether the NFRA expectation of periodic testing is met (`#08`, `#10`).
5. **"How much of last year's risk assessment carries forward? What would make the team challenge it?"** Reveals
   roll-forward bias (85% roll binders forward) and whether `#18`-type tools amplify it.
6. **"What client data do you actually get at planning, and how often does lack of access stop analytics?"** Reveals
   readiness for `#07`/`#08`; 60% cite poor data and 53% no access.
7. **"How do you find out how the client uses AI in reporting and controls? What happens when management cannot
   explain it?"** Reveals readiness for `#06` and team-competence gaps; ties to acceptance.
8. **"Has fraud brainstorming changed? Do you add AI-enabled schemes or fabricated documents? Does anyone use AI in
   the discussion, and after or before forming their own view?"** Reveals `#14`/`#15` practice; an open question.
9. **"Has any tool proposed materiality or scoping? Who decided, and how is a change from last year justified?"**
   Reveals unevidenced steps (`#16`, `#17`) and fee-pressure risk inspectors already watch.
10. **"Did AI change hours budgets, staffing mix or fees on any engagement? Who kept the savings?"** Reveals
    business-model pressure (`#22`, `#23`); PwC calls savings "not that drastic yet".
11. **"If summaries replace reading, how do juniors still learn the entity? What changed in first-year training?"**
    Reveals the skill-building risk the PCAOB acting chair raised.
12. **CAE: "Is the audit plan still annual? What signals would trigger a re-plan, and who approves it?"** Reveals
    whether dynamic planning (`#24`) is real; significant changes need board approval under IIA Standards.

## 5. Metrics and benchmarks

**Baselines and prevalence (independent unless noted)**
- IFIAR members "frequently" seeing automated tools in risk assessment: 55% of 47 (2024), 49% of 45 (2023); journal
  entries 88%; 31% reported a tool "not used as intended", mostly misread results and thin outlier testing [IFIAR-TTF-2025].
- Six large networks: about 30% year-on-year growth in AI-enabled tools in 2025, inconsistently reported [IFIAR-TTF-2026].
- Dutch PIE firms: risk assessment 28% of average tool use (tests of details 51%); AI is 3% of tool types available to
  staff (data analytics 32%) [AFM-12BB-2025].
- US firms (54 with complete data): 22% have automated risk assessment, 11% substantive analytics, 22% no automated
  solution; 85% prioritise rolling binders forward, 60% carrying forward the prior risk assessment [CPACOM-ATR-2025].
- The FRC found no formal monitoring quantifying the audit-quality impact of tools at the six largest UK firms [FRC-ATT-2025].
- Pre-GenAI observational study: one standard deviation of audit-firm AI investment associated with a 5.0% lower
  likelihood of restatement (36 largest firms) [FEDYK-2022]. Adjacent; all audit AI, not planning.

**Named outcomes (none measured)**
- PwC: AI time savings "more of a shift" and "not that drastic yet" (Oct 2026); AI "particularly good" at pointing to
  where risks may lie [CFODIVE-PWC-2026].
- Reach figures, not effects: EY 130,000 professionals, 160,000 engagements (`#11`); KPMG 2.175M Audit Chat
  conversations (`#02`); EisnerAmper 1,100+ users, 1,500+ engagements on DAS (`#20`).

**Vendor claims (grade C; ask for named, measured cases)**: Caseware 94% accuracy on golden-dataset items and 15-20
minutes to under 2 for indicative workflows, neither planning-specific (`#19`); Thomson Reuters 80-90% of deliverables
complete by year-end, unsourced (`#24`).

**Independent tests of AI on planning work**
- ICAEW, three chatbots, one fictional retailer: 0 of 3 separated statement-level from assertion-level risk; materiality
  benchmarks differed by model (`#12`, `#16`). A single test, not a benchmark.
- UMAR prototype: AUROC 0.782, PR-AUC 0.341 on 3,200 10-K firm-years, label is restatement, not a planning decision (`#13`).
- Fraud-rating experiment with ChatGPT (66 auditors, one vignette): weak evidence, design inconsistencies (`#14`).

**Client-side context**: 6% of largest clients have advanced AI governance [CAQ-INSIDER-2026]; 47% of 202 large companies
bypassed AI governance and 36% had a material AI incident [CAQ-INSIDERSEP-2026]; see also `#15`.

**What to measure (recommend these)**: IFIAR's suggested metrics: engagement coverage, false-positive and
false-negative rates against a manual sample, rework rates, escalation incidence, and benchmarking against traditional
methods [IFIAR-TTF-2026]. Add: reviewer override rate on AI-suggested risks; risks found later in fieldwork that
planning missed; planning hours and senior review time; internal and external inspection findings.

## 6. Guardrails

**Standards and regulators (none prohibits AI in planning; none sets AI-specific requirements)**
- **ISA 315 (Revised 2019)** (read in its UK adoption): automated tools may analyse large data volumes (A21) and whole
  populations to find significant classes (A203); procedures must not be biased toward corroborative evidence (para
  13); AI is named once, in Appendix 5, with auditor responsibilities "unchanged" [ISAUK315-2025].
- **AS 2110** has no AI wording. Hooks: understanding the company and changes since prior periods (.07-.08), analytics
  with expectations and limited precision (.46-.48), fraud discussion with the partner (.49-.53), inquiries of the audit
  committee and others (.54), revising the assessment (.74) [AS2110-PCAOB-2026].
- **PCAOB.** Release 2024-007: a procedure's purpose decides its category, and a multi-purpose procedure must meet each
  objective; reliability evaluation for risk-assessment information takes less effort; it does not address AI
  [PCAOB-TAA-2024]. Staff (2024): standards not seen as an impediment; some firms bar GenAI on procedures [PCAOB-GENAI-2024].
  The acting chair wants a "human-in-the-lead" model [KSLAW-SEIAG-2025].
- **ISA (UK) 240 (Revised March 2026, effective periods from 15 Dec 2026):** tools may support fraud brainstorming
  (A56); AI or ML that initiates entries may heighten fraud risk (A101); authenticity technology where documents are
  doubtful (A36); tools do not replace scepticism (A9) [ISAUK240-2026].
- **IAASB exposure drafts (5 Aug 2026; comments due 15 Dec 2026):** ED-520 would require considering inconsistent
  results of risk-assessment analytics; ED-330 would remove the always-substantive requirement [AUASB-CPED-2026].
- **FRC (30 Mar 2026):** risks of deficient output, misuse (an auditor may not see the output was meant to inform
  judgement, not conclude), and non-compliant methodology; certification, prompt libraries, review at control points;
  worked example on board minutes [FRC-GENAI-2026].
- **AICPA practice aid (13 Oct 2026):** Part 1 on the entity's AI use; Part 2 on firm use under quality management;
  RMM and evidence guidance to follow; AI tools need not be named in the engagement letter under AU-C 210, though state
  law or firm policy may require it [AICPA-PA-2026, CFODIVE-AICPA-2026].
- **Others.** IFIAR: govern GenAI, keep humans in control, explain key judgements [IFIAR-TTF-2026]. AFM: foundation,
  input data and controlled implementation before GenAI [AFM-12BB-2025]. NFRA (as reported): no lower evidentiary bar;
  periodically test a tool's low-risk classifications [NFRA-CAALLEY-2026]. Internal audit: IIA Standard 9.4 requires
  plans based on ongoing risk assessment [WK-DYNAMIC-2026].

**Design guardrails seen in sources**
- Cited output linked to source sections; pre-written, tested prompt libraries; certification before use (`#01`).
- The auditor forms their own view before reading AI output (AFM, `#14`); nothing enters the file without an explicit
  accept, edit or reject (`#09`, `#19`).
- Approval gates, exception logs and evidence links on every agent step [WK-CONNECTED-2026]; shadow runs on completed
  engagements, then a gradual ramp [CPAPA-LEDGERLINE-2026]; several models review the same work (`#25`).
- The audit plan records which tools address which risks, and the file shows where AI was used and how it was reviewed (`#21`).

**Steps that stay with a person**: inquiry, observation and inspection; the fraud discussion with the engagement
partner; the assessment of RMM and significant risks; materiality and scoping decisions; judgement on the client's
AI use; revising the assessment; partner sign-off of the plan. The chatbots ICAEW tested could not perform inquiry,
observation or inspection.

## 7. Roles and how they evolve

- **Preparers become reviewers of cited drafts.** The FRC example moves training to reviewing outputs and resisting
  automation bias (`#01`); ICAEW's faculty chair wants training in judgement and scepticism, not tool mechanics [ICAEW-FRCVIEW-2026].
- **Juniors.** The PCAOB acting chair warned AI may erode critical thinking and that juniors need new routes to build
  those skills [ACCTODAY-BOTIC-2025]; an AAA panel examined how juniors use GenAI in planning [AAA-MIDYEAR-2026].
  Caseware and Citrin Cooperman say visible reasoning helps juniors learn (`#20`); Deloitte adds a tutor mode (`#03`).
- **Evidence on judgement is mixed.** Automation reduced scepticism in one study [PETERS-2022]; auditors discounted
  contradicting AI advice more than human advice [COMMERFORD-2022]; a registered report proposes testing GenAI's effect
  on motivation [HOLMSTROM-2024].
- **New roles.** PwC hires engineers and dual-track CPA and data-science staff (`#18`); vendors hire audit practitioners
  as agent architects and audit engineers [FIELDGUIDE-JOB-2026]; the AFM saw "tool ambassadors" at planning meetings (`#05`).
- **Engagement partners** take on knowing which tools are used and checking they are approved (`#21`).
- **Internal audit.** FJ Management's head moved from executing procedures to designing the work (`#25`).
- **Workforce size.** Pre-GenAI, AI investment correlated with 7.1% fewer accounting staff after four years [FEDYK-2022].

## 8. Frontier

- **2025-10-27/28** PwC targets a tool for every audit step in 2026, a risk-assessment tool "soon" (not seen since)
  [PWC-AT-2025]; PwC Australia pilots agents that assess risk and design plans (CT-17).
- **2025-12-09** PCAOB acting chair: AI can already enhance risk assessment "in certain scenarios"; warns on scepticism [ACCTODAY-BOTIC-2025].
- **2026-03-30** FRC generative and agentic AI guidance, with the board-minutes example [FRC-GENAI-2026].
- **2026-04-07** EY embeds agents in all audit phases; end-to-end by 2028 [EY-CANVAS-2026].
- **2026-04-20** IFIAR flags agentic AI moving toward orchestration; suggests quality metrics [IFIAR-TTF-2026].
- **2026-06-04** FRC opens an Audit Tech & AI Sandbox [FRC-SANDBOX-2026].
- **2026-06-24** Deloitte unifies agents in Omnia, including risk-factor identification [DELOITTE-OMNIA-2026].
- **2026-07-24** NFRA principles cover planning and risk assessment [NFRA-CAALLEY-2026].
- **2026-08-05** IAASB EDs on ISA 330, 500 and 520; comments due 15 Dec 2026 [IAASB-EDPAGE-2026].
- **2026-09-22 / 10-06 / 10-14** MindBridge, Caseware and Optro launch risk-assessment agents (`#10`, `#09`, CT-04).
- **2026-10-13** AICPA practice aid; RMM guidance for AI-using clients to follow [AICPA-PA-2026].
- **2026-11-06/07** WCARS: "Taming the Autonomous Frontier" (scheduled) [WCARS-2026].
- **2026-12-15** ISA (UK) 240 (revised 2026-04-30) effective [ISAUK240-2026]; IAASB comment deadline. Watch for AICPA RMM guidance and FRC sandbox output.

## 9. Common objections

- **"Chatbots can't do risk assessment."** Correct for general chatbots: ICAEW found no inquiry, observation or
  statement-versus-assertion split, and answers varied (`#12`). Deployed tools are narrower: cited summaries, drafted
  risk lists, analytics, all reviewed (`#01`, `#08`, `#09`).
- **"The AI becomes the conclusion."** The FRC's central misuse risk. Record that output informed judgement; form your
  own view first; periodically test low-risk ratings (§6).
- **"It just rolls last year forward faster."** A real risk (`#18`). ISA 315 para 13 bars bias toward corroboration;
  ask the tool to show what changed, and document challenge.
- **"Savings are small."** PwC agrees so far [CFODIVE-PWC-2026]. Vendor figures are unmeasured or not
  planning-specific. Measure before claiming.
- **"Agent washing."** Richard Chambers warns that basic features are rebranded as agents; ask for live demos on new
  inputs [AUDITBOARD-AGENTICERA-2026].
- **"Small firms can't certify tools."** ICAEW says guidance assumes specialist teams small firms lack [ICAEW-FRCVIEW-2026];
  methodology platforms (`#20`) and the FRC sandbox are routes.
- **"Client data won't support it."** 60% cite poor data, 53% no access [CPACOM-ATR-2025]; standardised ingestion (`#07`) comes first.
- **"Continuous risk assessment oversells certainty."** More data means more exceptions and a wider expectation gap if
  sold as certainty [CPAPA-LEDGERLINE-2026].

## 10. Sources

Full details are in the YAML except for keys listed as not in it; the synthesis report maps keys to the inputs and pilot.
- **Regulators and standard-setters:** FRC-GENAI-2026, AFM-12BB-2025, IFIAR-TTF-2025, IFIAR-TTF-2026, IFIAR-SURVEY-2026,
  PCAOB-TAA-2024, PCAOB-GENAI-2024, PCAOB-PRIORITIES-2024, ISAUK315-2025, ISAUK240-2026, AS2110-PCAOB-2026,
  AUASB-CPED-2026, ACRA-APG1-2025, FSA-DP-2025, IRBA-AIUPDATE-2024, CPAB-AI-2024.
- **Professional bodies:** AICPA-PA-2026, JOFA-AIPA-2026, CAQ-GENAI-2024, CAQ-RSM-2026, CAQ-INSIDER-2026,
  CAQ-INSIDERSEP-2026, CAQ-INSIDERAPR-2026, CAQ-INSIDERMAY-2026, ICAEW-PIERPOINT-2025, ICAEW-315-2025, ICAEW-GROUP-2025.
- **Firms:** KPMG-CLARA-2024, KPMG-CLARA-2025, KPMG-HOHL-2026, EY-CANVAS-2026, DELOITTE-OMNIA-2026, DART-SECPCAOB-2025,
  GT-GTAP-2026. **Vendors:** CASEWARE-RSA-2026, CASEWARE-LAUNCH-2026, CASEWARE-VERITY-2026, CASEWARE-AIDA-2026, CASEWARE-EISNERAMPER-2026,
  CASEWARE-CITRIN-2026, CASEWARE-PKF-2026, MINDBRIDGE-ARA-2026, WK-AGENTRA-2026, WK-CONNECTED-2026, WK-SAS145-2024,
  WK-GROUP-2025, WK-DYNAMIC-2026, WK-MICRO-2026, WK-MULTIYEAR-2026, TR-CHALLENGES-2026, OPTRO-HELVETIA-2026, OPTRO-FJ-2026,
  FIELDGUIDE-DEMO-2026, AUDITBOARD-RTRA-2025, AUDITBOARD-RIF-2026.
- **Press:** PWC-AT-2025, CFODIVE-PWC-2026, CFOBREW-PWC-2025, BBL-DELOITTE-2026, BBL-KPMG-2026, CPAPA-ASKLUCA-2026,
  CPAPA-GT-2026, CPAPA-MINDBRIDGE-2026, CPAPA-LEDGERLINE-2026, ITBRIEF-CASEWARE-2026, BDO-FIELDGUIDE-2026, NFRA-CAALLEY-2026,
  CPIA-ARAQ-2026, BOARDAGENDA-FRC-2026, AT-AICPAPA-2026, ACCTODAY-BOTIC-2025, FINSTORY-KPMGFEE-2026, GRCREPORT-DELOITTE-2026.
- **Surveys, academic, conference:** CPACOM-ATR-2025, TRI-FOP-2026, IIAF-AIFRAUD-2026, ARXIV-UMAR-2026, ARXIV-FAB-2026,
  CPAJ-AIPLAN-2026, INDO-ICOBUSS-2025, PETERS-2022, VLGAA-NUCCIO-2026.
- **Not in the YAML (all opened by the deep dives):** FRC-ATT-2025 (FRC, *Thematic Review: Certification of Automated
  Tools and Techniques*, 2025-06-26, https://www.frc.org.uk/docs/8383/html/); FRC-SANDBOX-2026 (FRC sandbox release,
  2026-06-04, https://www.frc.org.uk/news-and-events/news/2026/06/frc-invites-firms-and-companies-to-experiment-innovate-and-reduce-burdens-through-new-sandbox-programmes/);
  IAASB-EDPAGE-2026 (IAASB, ISA 330/500/520 proposals, 2026-08-05, https://www.iaasb.org/publications/proposed-revisions-audit-evidence-risk-response-isa-330-isa-500-isa-520);
  CFODIVE-AICPA-2026 (CFO Dive, 2026-10-13, https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/);
  KSLAW-SEIAG-2025 (King & Spalding, PCAOB SEIAG highlights, 2025-11, https://www.kslaw.com/blog-posts/pcaob-seiag-meeting-highlights-ai-and-crypto-take-center-stage);
  ICAEW-FRCVIEW-2026 (ICAEW, 2026-05-06, https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai);
  AUDITBOARD-AGENTICERA-2026 (Optro blog, R. Chambers, 2026-08-12, https://auditboard.com/blog/agentic-audit-era-what-caes-must-rethink);
  AAA-MIDYEAR-2026 (AAA workshop agenda, 2026-01-15, https://aaahq.org/Meetings/2026/Auditing-Section-Midyear-Meeting/Workshop);
  WCARS-2026 (Rutgers, 75th WCARS, 2026-11-06, https://raw.rutgers.edu/75wcars.html);
  FEDYK-2022 (*Review of Accounting Studies* 27(3), 2022-09, https://ideas.repec.org/a/spr/reaccs/v27y2022i3d10.1007_s11142-022-09697-x.html);
  COMMERFORD-2022 (*Journal of Accounting Research* 60(1), 2022-03, https://ideas.repec.org/a/bla/joares/v60y2022i1p171-201.html);
  HOLMSTROM-2024 (PCAOB registered report proposal, 2024-06, https://assets.pcaobus.org/pcaob-dev/docs/default-source/economicandriskanalysis/conference/conference---spring/session_5_holmstrom_peters.pdf);
  FIELDGUIDE-JOB-2026 (Fieldguide Agent Architect posting, accessed 2026-10-16, https://www.builtinboston.com/job/agent-architect-audit/10693122).
