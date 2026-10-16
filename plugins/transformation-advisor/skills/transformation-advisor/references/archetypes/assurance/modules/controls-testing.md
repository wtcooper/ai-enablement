# Controls testing (assurance)

Last reviewed 2026-10-16. Use cases live in `../use-cases/controls-testing.yaml` (25 entries). Ids are shortened
here: `#05` means `assurance-controls-testing-05`. Source keys in brackets, such as [K-SOX30], are listed in §10
and given in full in the YAML. Almost every outcome figure is self-reported by the deploying organisation or its
vendor; no independent measure of AI test quality exists yet. Say so when you quote one.

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

Testing whether internal controls are well designed and actually operate, in three settings: external audits of
internal control over financial reporting (ICFR; SOX 404 integrated audits under PCAOB AS 2201/AS 2301 and ISA
330), internal audit and management SOX programmes, and SOC 1/SOC 2 examinations (an auditor's report on a service
organisation's controls). It runs from walkthroughs and IT general controls (ITGCs: access, change management,
operations) through sampling, evidence and tick-marking (marking on the evidence what was checked) to deficiency
evaluation and documentation, and now includes testing controls that AI itself performs. Internal audit and SOX
teams are ahead of external auditors on agents; external audit voices are more cautious.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Scoping and RCM | Pick key controls, link them to risks in the risk and control matrix (RCM), set test attributes, decide reliance | expert-judgment | Vague criteria, sampling logic and exception rules; KPMG advises a "controls clean-up" before AI |
| Walkthrough and test of design | Trace one transaction end to end; confirm the control is designed to prevent or detect misstatement | document-production, research-synthesis | Repeated yearly even when nothing changed; same architecture redrawn each time |
| Reliability of information (IPE) | Test controls over the reports a control uses (information produced by the entity) | review-assurance, data-reporting | 43 IPE/data findings at the six largest networks in 2025 [IFIAR-2025F] |
| Evidence request (PBC) | Request, chase and validate items "provided by client" | coordination-scheduling, client-interaction | ~1 in 5 requests wrong first time (practitioner estimate); owners spread over 20+ systems |
| Sample selection | Statistical, judgmental, or full population | data-reporting, expert-judgment | Static lists; 24 "insufficient" and 11 "biased" sample findings in 2025 |
| Test of operating effectiveness | Check each attribute per sample, tick-mark, conclude | review-assurance, transaction-processing | 16 hours per control (FY2024, up from 12 in FY2022); PDFs, screenshots, exports in every format |
| ITGC testing | Access, change, operations; now also over AI components | review-assurance | Longest to test; 39 ITGC findings in 2025 |
| Deviation and deficiency evaluation | Exception vs missing support; severity (deficiency, significant deficiency, material weakness); aggregation | expert-judgment | Missing support is not always a failure; 11 severity-evaluation findings in 2025 |
| Documentation and review | Workpapers, secondary review, sign-off | document-production, review-assurance | Manager/CAE review bottleneck; errors slip through on "the fiftieth workpaper" |
| Reliance on others | SOC 1 reports and CUECs (controls the customer must run); internal audit's work (AS 2605, ISA 610) | review-assurance, research-synthesis | Many reports to read; reliance standards predate AI |
| SOC examinations | Section 3 system description, tests, deviations, management responses | review-assurance, document-production | KPMG UK: demand nearly doubled in a year; 90% of exceptions on manual controls |

Inspection context: internal control testing is the largest single source of engagement findings at the six
largest networks (213 in 2025 listed public-interest audits; 69 on insufficient evidence for manual controls)
[IFIAR-2025F]. Those are exactly the steps AI tools target.

## 3. Where AI is changing the work

Lens key: improve (assist a step), automate (no person on the normal path), delegate (an agent owns a multi-step
outcome), reinvent (the process or service model changes). All four lenses have evidence; automate and delegate are
thin, and no entry reaches the top "reinvent" rung of the ladder (see the synthesis report).

**Planning, walkthroughs and design**
- Improve: `#01` walkthrough assistants draft narratives from prior-year files and flag changes (PwC, KPMG UK).
  `#02` agents draft test plans and score control wording (KPMG UK, Fieldguide, Petual). `#04` risk-scored sample
  and coverage selection, weeks to one day (Microsoft IA), plus predictive targeting (KPMG, Optro).

**Evidence and sampling**
- Improve: `#03` agents clarify PBC requests and check submissions before testing (Optro, RSM; collection agents announced).
- Reinvent: `#08` full-population tests replace samples (Armanino tests 100% of vendor master changes).

**Testing operating effectiveness and ITGCs**
- Delegate: `#05` agents read unstructured evidence, test attributes, cite sources and draft workpapers; Reddit
  automated 175 controls in 90 days, -60% time per control (vendor-published, CAE-confirmed).
- Automate: `#06` Microsoft's two-agent ITGC change-management tester (850 h and $185K a year). `#07` agents match
  client documents to samples (Oberlander 16 h to 5-6 h; mostly substantive work so far).
- Reinvent: `#09` continuous, year-round testing; internal audit tests the first line's monitoring (Klaviyo, Snowflake).
- Ideas: `#23` screen evidence for fabrication and hidden instructions; `#25` synthetic data to stress-test controls pre-go-live.

**Deviations, documentation and review**
- Improve: `#10` AI secondary review with several models cross-checking a workpaper (FJ Management); `#22` idea:
  deficiency classification grounded in a log of past deviations.

**SOC examinations and reliance on others**
- Improve: `#11` KPMG UK SOC engagements ~18% less testing time; `#12` drafting Section 3 and deviation responses;
  `#13` reading vendor SOC reports for scope, exceptions and CUECs.
- Automate: `#14` compliance platforms pull evidence for SOC 2 examiners; contested (peer-review alert, Delve allegations).
- Reinvent (idea): `#24` external auditor relying on management's AI-tested work; no public case yet.

**Testing AI-performed controls (new test object)**
- Reinvent: `#15` scope AI components, extend ITGCs to prompts, models and agent identities, apply COSO "reliance".

**Operating and service model**
- Delegate: `#16` Big Four platform agents (EY, Deloitte, KPMG, PwC, GT); controls-testing use announced, not evidenced.
  `#18` PayPal's agent "swarms".
- Reinvent: `#17` PwC Australia AI-native audit pilot; `#19` in-sourcing co-sourced testing to agents (Havertys);
  `#20` firms selling agent-delivered testing (RSM Beacon with Andera, Riveron, Arden).
- Improve: `#21` SOX practitioners hired to build agent evaluation sets (new role).

## 4. Interview probes

Ask in the person's own setting (audit firm, internal audit, SOX programme or SOC practice).

1. **"Walk me through one key control from evidence request to sign-off. Where do the hours go?"** Reveals the
   baseline against 16 hours per control, and whether the pain is chasing (`#03`), testing (`#05`-`#07`) or review (`#10`).
2. **"Which control types have you moved to AI or agent testing, and which did you try and pull back from?"**
   Reveals maturity. Bounded ITGCs and three-way matches go first; teams plateau on management review controls.
3. **"Does each control have written attributes, evidence requirements and exception rules?"** Reveals readiness.
   Vague criteria such as "approval is required" break agents; a controls clean-up may come first.
4. **"When an agent marks a sample 'pass', what does the reviewer actually look at? Do you track override rates?"**
   Reveals rubber-stamp risk and automation bias, and whether review is designed or improvised.
5. **"Did you run old and new testing in parallel on the same controls, and did both catch the same exceptions?"**
   Reveals whether any quality evidence exists. Most teams have only hours saved.
6. **CAE: "Has your external auditor agreed in advance whether they will rely on agent-produced workpapers, and
   what they need to see?" Partner: "If a client hands you agent-tested work, what would you need under AS 2605?"**
   Reveals the biggest open risk: no public case of reliance exists.
7. **"How was the tool approved for this specific use: edge-case tests, parallel running, recertification
   triggers? Who monitors its effect on quality?"** Reveals ISQM 1 / QC 1000 readiness (firm quality-management
   standards) and the gaps the FRC found.
8. **"What does the file show: tool and version, criteria for use, what it produced, the checkpoint, the
   reviewer's own work? Would it survive an AS 1215 or FRC-style review?"** Reveals documentation risk; "an AI
   tool was used" is not enough.
9. **"Which in-scope controls (yours or your clients') now depend on AI output? Are you testing around the AI or
   relying on it, and what do you keep: prompts, model versions, logs?"** Reveals exposure to the new test object
   (`#15`); KPMG expects the first AI-related material weaknesses in 2027.
10. **"Has full-population or continuous testing changed your exception volumes? Who works them, and are
    investigation thresholds set before you see results?"** Reveals capacity and expectation-gap risk (`#08`, `#09`).
11. **"How has co-source spend, or your hours-based testing revenue, changed? What came in-house first?"**
    Reveals business-model pressure on both sides (`#19`, `#20`).
12. **"What stops a control owner planting instructions in evidence, or submitting an AI-fabricated screenshot?"**
    Reveals adversarial readiness; 62% of internal audit leaders say they are unprepared or minimally prepared for AI-enabled fraud.

## 5. Metrics and benchmarks

**Baselines to ask for first**
- Testing hours per control: 16 (FY2024), up from 12 (FY2022); SOX control cost +45% between KPMG's 2023 and 2025
  surveys; 52% of internal audit departments spend over 40% of hours on SOX [K-SOX30].
- Average SOX programme ~$2.3M and 15,000+ hours a year, ~40% on testing (cited by Zanin; survey not named) [CPAPA-ZANIN].
- Co-source share: 58% say outsourced providers exceed 20% of SOX budget [K-SOX30].
- PBC first-time-right: ~1 in 5 requests wrong first time (practitioner estimate) [CPAPA-ZANIN].

**Named outcomes (self-reported or vendor-published; effort, not quality)**
- Reddit IA: 175 controls (>40% of SOX scope) in 90 days; -60% testing time per control; later >75% of SOX controls (Optro only) `#05`.
- Microsoft IA: 850 h and $185K a year from one ITGC agent, built in 1-3 months `#06`; sample selection weeks to
  one day `#04`; whole function: quality-review effort ~-50%, reports 3 to 2 weeks `#08`.
- KPMG UK SOC engagements: ~18% less testing time; ~15% from DataSnipper alone `#11`.
- Oberlander: sample-to-evidence 16 h to 5-6 h; RMF: ~50% on 60+ invoice samples; Sanville: realisation
  $150-200 to $250+ an hour and zero PCAOB comment forms (after a full methodology overhaul) `#07`.
- PwC (external audit, year one): savings "not that drastic yet" [CFODIVE-PWC].

**Vendor claims (grade C; ask for named, measured cases)**: Petual 68-80% efficiency [FTG-PETUAL]; Andera "save 70%
of time on any control" [ANDERA-HOME]; Fieldguide up to 70% of financial audit testing automated [FG-FINAUDIT];
Midship 16 hours to under 15 minutes per test, up to 85% of SOX controls automatable [SRA-16H]; Thomson Reuters up
to 70% faster preparation and review [TR-AGENTIC].

**Adoption and quality benchmarks**
- Gartner poll (743, Aug 2026): 93% of audit teams use some AI; 30% use GenAI for testing vs 60% for drafting
  issues and reports; 38% have a strategy [AT-GARTNER].
- Regulators seeing automated tools "frequently" in controls testing: 43% vs 88% for journal-entry testing; 31% of
  IFIAR members found tools "not used as intended" (2024) [IFIAR-TTF25].
- Listed-PIE audits with a controls-testing finding where inspected: 14% in 2025 (11% in 2021) [IFIAR-2025F].
- Agent risk: 34% acted on an inaccurate agent output; 46% spend more time validating AI; 9% redesigned workflows
  for agents (Optro survey of 417) [OPTRO-SURVEY].
- SOC work (EY conference poll): AI for evidence collection 63%, Section 3 45%, deviation responses 41% [EY-SOC].
- US CPA firms (54 surveyed): 75% have no documented transformation plan; 41% expect technology to reduce the need
  for sampling [CPACOM-ATR].

**What to measure (recommend these, not hours alone)**: hours per control before and after; reviewer override and
disagreement rate; whether parallel runs catch the same exceptions; rework and review notes; PBC follow-up rate;
time to a final workpaper; exception-detection rate; accuracy for binary matching tools; inspection and internal
quality-review findings. Research reference: an LLM prototype matched assessor-only control conclusions 91.7% of
the time on 14 controls, with every judge revision stricter [INTELLIAUDIT].

## 6. Guardrails

**Standards and regulators (no body prohibits AI; none has AI-specific requirements yet)**
- **Accountability is universal.** The auditor owns the opinion. NFRA: there is "no separate, lower evidentiary bar
  for technology generated information" [NFRA-CAALLEY]. FRC, AICPA, AFM, IFIAR and CPAB say the same.
- **PCAOB (US public companies).** AS 1105/AS 2301 technology-assisted-analysis amendments apply to fiscal years
  beginning on or after 15 Dec 2025; they stress ITGCs for electronic information but expressly exclude AI
  [PCAOB-2024-007]. QC 1000 takes effect 15 Dec 2026 (date not re-verified on the primary source). AS 1215
  (documentation) is the de facto bar; AS 2605 governs using internal audit's work.
- **IAASB (ISA).** Exposure drafts of ISA 330/500/520 (5 Aug 2026; comments due 15 Dec 2026) would allow "tests of
  controls alone" in narrow cases, clarify IT general controls, and require evaluating, not just considering,
  reliability of information [IAASB-ED].
- **FRC (UK).** Generative and agentic AI guidance (30 Mar 2026): risks are deficient output, misuse of output and
  non-compliant methodology; define human "control points"; certify per use case; do not overstate the
  persuasiveness of population-level AI outputs [FRC-GENAI]. 2025 thematic: certification policies incomplete [FRC-THEMATIC].
- **US private companies and SOC.** AICPA practice aid (13 Oct 2026) [AICPA-PA]; TQA 9561 (11 Sep 2026): no new SOC
  criteria, scope follows the system boundary, AI providers treated as subservice organisations [SD-TQA]. Peer Review
  Board alert (effective 1 Jun 2026): templated SOC 2 work is nonconforming [JOFA-PRB].
- **Management side.** COSO GenAI guidance (23 Feb 2026) defines when management "relies" on AI and the evidence that
  triggers: prompt, configuration and model version, sampling rationale [COSO-GENAI].
- **Elsewhere.** NFRA ten principles (Jul 2026) cover agentic tools that select and test samples; AFM's 12 building
  blocks (Dec 2025) require verifiable outputs [AFM-12].

**Design guardrails seen in deployments**
- Auditor approves the test plan before an agent runs; review at set stages (plan, extraction, conclusion).
- Every attribute linked to a location in the source; prompts and models versioned.
- Deterministic code for calculations and pass/fail rules; LLMs for reading documents.
- Back-test on completed engagements and run in parallel before relying; ramp gradually.
- Written criteria for when AI may auto-clear an item and when it must route to a person.
- Agent credentials governed with segregation of duties; defences against instructions hidden in evidence.
- A log of previously accepted deviations; reviewers form their own expectation before reading AI output.

**Steps that stay with a person**: the walkthrough inquiry and observation; deciding evidence is sufficient; telling
missing support from a true exception; classifying severity and aggregating deficiencies; reliance decisions (on
SOC reports, internal audit, or AI-performed controls); investigation thresholds for full-population runs; sign-off.

## 7. Roles and how they evolve

- **Testers become reviewers.** Hours move from tick-and-tie to exceptions, remediation and control design;
  practitioners say review is now where most auditor time goes. Reviewer-to-preparer ratios rise.
- **The bottleneck moves to review.** 46% report more time validating AI output; a rubber-stamp approval "provides no
  real control value" (KPMG) [K-SOX30].
- **New roles:** SOX practitioners hired by vendors as AI evaluators (`#21`); data-science managers inside internal
  audit (PayPal); engineers and dual-track CPA/data-science hires at PwC; Reddit's "AI-first" internal audit role.
- **IT auditors** must read configuration and model logs as fluently as a ledger; KPMG says these skills are not
  core to the CPA curriculum.
- **Juniors.** Upside: Sanville's first-years now do complex revenue testing under guidance. Risk: moving from
  preparing to reviewing may erode autonomy and skill-building (Holmstrom & Peters proposal); Thomson Reuters urges
  protecting structured development. NFRA wants role-specific training: safe use, critical review, governance.
- **Co-source economics.** Clients redirect testing spend to advisory (Havertys); firms repackage testing as
  platform plus review (RSM, Riveron); hourly pricing is under pressure.

## 8. Frontier

- **2025-10-28** PwC promises a tool for every audit step in 2026, with controls-testing automation modelled on
  Evidence Match; PwC Australia pilots an AI-native audit (5 clients, all by 2028) [AT-PWC, AT-PWCAU].
- **2026-01** KPMG UK introduces a reasonable-assurance "SOC 2+" opinion over AI governance and controls [K-UKCA].
- **2026-02-23** COSO GenAI guidance makes AI-touched controls an ICFR test object [COSO-GENAI].
- **2026-02 to 05** SOC 2 credibility crisis: AICPA warning, Peer Review Board alert, Delve allegations [JOFA-FAST].
- **2026-03-30** FRC issues the first regulator guidance on generative and agentic AI in audit [FRC-GENAI].
- **2026-02 to 06** Funding and consolidation: Fieldguide $75M, Petual $20M, Optro buys Midship (6 May), Andera $37M.
- **2026-04-20** IFIAR asks firms to define what "human-led" means as agents orchestrate audit work [IFIAR-TTF26].
- **2026-05-19** SEC filer-status proposal would remove 404(b) attestation for ~80.8% of reporters if adopted [UNIQUS].
- **2026-06-23 to 08-07** PCAOB asks about AI in its standard-setting agenda; the IIA urges modernising AS 2605 [IIA-PCAOB].
- **2026-07** NFRA (India) principles explicitly cover agentic tools that select and test samples [NFRA-CAALLEY].
- **2026-08-05** IAASB exposure drafts reshape tests of controls; comments due 15 Dec 2026 [IAASB-ED].
- **2026-08-26 / 09-15** RSM Beacon with Andera launches; Workiva ships evidence, attribute and testing agents.
- **2026-09-24** KPMG *Future of SOX 2030*: continuous 100% testing; first AI-related material weaknesses expected 2027.
- **2026-10-14** Optro extends autonomous testing beyond SOX to operational audit; evidence collection "upcoming".
- **2026-11-06/07** WCARS: "Taming the Autonomous Frontier: AI Governance and Continuous Auditing" (scheduled).
- **2026-12-15** QC 1000 effective; IAASB comment deadline. Watch for the first sandbox outputs from the FRC.

## 9. Common objections

- **"AI isn't reliable; reruns give different answers."** True of LLMs alone. Deployments pair them with rules:
  Microsoft's pass/fail logic is rule-based; the FRC recommends output schemas and deterministic rules; vendors
  build evaluation sets so the same evidence gives the same conclusion (`#06`, `#21`). Ask for override rates.
- **"Our external auditor won't rely on it."** Fair: no public case exists. Involve them before the pilot, agree the
  workpaper format, run in parallel. The IIA is pressing the PCAOB to modernise AS 2605 (`#24`).
- **"Review time will eat the savings."** 46% report more validation time and PwC calls savings modest, yet Reddit
  reports 60% less testing time per control. Design the review: cited evidence, risk-based re-performance, secondary AI review (`#10`).
- **"Regulators will penalise us."** No regulator prohibits AI; the FRC opened a sandbox. The risk is
  documentation: show tool, version, criteria, output and reviewer work. MindBridge says inspection uncertainty
  makes firms run AI and manual procedures in parallel, so budget for that at first.
- **"Testing everything means drowning in exceptions."** It does surface more. Set thresholds before running,
  staff the follow-up, and never sell it as certainty: reasonable assurance still applies (`#08`).
- **"Our evidence is too messy."** Mixed formats are why RPA failed and agents are used (Reddit). But field
  discipline decides success; start with bounded ITGCs and clean attributes.
- **"The savings figures are vendor hype."** Mostly true: all are self- or vendor-reported. Bring your "ugliest
  evidence" to demos (Zanin) and do not rely on vendor accuracy claims without your own evaluation (NFRA).
- **"Internal audit sharing agents with the business breaks independence."** PayPal hands ownership to the first
  and second lines; KPMG says internal audit should test monitoring, not run it.

## 10. Sources

Full details (title, publisher, type, URL, date) are in the YAML; the synthesis report maps keys to input refs.
- **Regulators and standard-setters:** FRC-GENAI (FRC, 2026-03-30); FRC-THEMATIC (FRC, 2025-06-26); IFIAR-2025F
  (2026-04-01); IFIAR-TTF25 (IFIAR, *Use of technology in audits*, 2025-03-27,
  https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf); IFIAR-TTF26 (2026-04-20); PCAOB-2024-007; IAASB-ED
  (2026-08-05); COSO-GENAI (2026-02-23); AFM-12 (2025-12-11); IRBA (2024-09-19).
- **Professional bodies:** AICPA-PA, JOFA-PRB, JOFA-FAST, JOFA-COSO, JOFA-EVAL, CSA-SOC2, IIA-PCAOB, ICAEW-FRC, CALCPA.
- **Firms and in-house teams:** K-SOX30, K-404A, K-AGENTIC, K-UKCA, K-CLARA (KPMG); MSFT-CM, MSFT-IA (Microsoft);
  DELOITTE-OMNIA; RSM-BEACON; RIVERON; GT-SOX; BDO-ITGC; SD-TQA; UNIQUS; FOLEY-BOTIC; PWC-DCT (search only).
- **Vendors:** OPTRO-LAUNCH, OPTRO-ACT, OPTRO-FIRST, OPTRO-MIDSHIP, OPTRO-HAVERTYS, OPTRO-FJM, OPTRO-SNOW,
  AUDITBOARD-ACC; FG-AGENTS, FG-SANVILLE, FG-PCAOB, FG-FRAZIER (search only); DS-ARMANINO, DS-RMF; TR-AGENTIC;
  PETUAL-HOME, A16Z-PETUAL; MINDBRIDGE-PCAOB; YC-ARDEN, YC-MIDSHIP. Not in the YAML: ANDERA-HOME (Andera homepage,
  accessed 2026-10-16, https://www.andera.ai/); FG-FINAUDIT (Fieldguide, *Increase Capacity and Audit Quality with Field
  Agents for Financial Audit*, 2025-06, https://www.fieldguide.io/blog/increase-capacity-and-audit-quality-with-field-agents-for-financial-audit).
- **Press:** AT-PWC, CFODIVE-PWC, CFOBREW-PWC, AT-PWCAU, CPAPA-EY, CPAPA-RSM, CPAPA-WORKIVA, CPAPA-ZANIN,
  CPAPA-ADEWOLE, CONS-GT, FTG-PETUAL, NFRA-CAALLEY, AT-GARTNER, IANS-DELVE, CCI-DELVE, VERDANTIX.
- **Surveys, academic, podcasts, community, jobs:** OPTRO-SURVEY (2026-10-08); IIAF-FRAUD (2026-02-17); EY-SOC
  (2026-09); CPACOM-ATR (CPA.com/AICPA, *2025 Audit Transformation Report*, 2025-12,
  https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf); INTELLIAUDIT; PETERS; KOKINA;
  SRA-16H, SRA-SWARM, IIA-SWARM, AUDITPOD-296, JOFA-PODSOC; REDDIT-POST; JOB-FG-SOX, JOB-FG-SWE, JOB-NACE, JOB-REDDIT.
