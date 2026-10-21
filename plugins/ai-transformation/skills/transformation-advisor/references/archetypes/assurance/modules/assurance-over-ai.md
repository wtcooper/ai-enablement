# Assurance over AI (assurance)

Last reviewed 2026-10-21 (mid-market firms added). Use cases live in `../use-cases/assurance-over-ai.yaml` (27 entries). Ids are shortened
here: `#05` means `assurance-assurance-over-ai-05`; other modules' ids are in full. Source keys in
brackets are listed in §11 and given in full in the YAML. **Read this first:** in most entries the AI is the *object*
of the assurance work, not the tool doing it. No measured quality outcome exists anywhere in this module: no error
rate, override rate, parallel run, inspection finding, fee or certificate count. The figures are readiness surveys,
market sizing, vendor counts and one firm's forecast. Say so when you quote them.

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
10. [Mid-market firms](#10-mid-market-firms)
11. [Sources](#11-sources)

## 1. What this module covers

Two linked areas. **Area 1: auditing the AI an entity uses in financial reporting and internal control over
financial reporting (ICFR)**: finding the AI, deciding whether management relies on it, extending IT general controls
(ITGCs: access, change, operations and development controls) to models, data pipelines and agents, and choosing
evidence. **Area 2: standalone assurance over AI systems**: readiness work, ISO/IEC 42001 certification (an audit of an
organisation's AI management system, meaning its policies, roles and controls for AI), ISAE (UK) 3000 opinions,
AIUC-1 agent certification, technical and bias testing, EU AI Act conformity, and the accreditation and skills of the
assurers themselves. Area 1 is guidance-rich and practice-poor. Area 2 has named certifications but no issued Big Four
client report was found. Testing AI-performed controls inside a SOX programme is covered in controls-testing (`assurance-controls-testing-15`).

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| **Area 1** Inventory and understand AI use | List AI use cases (including unsanctioned "shadow AI"), owners and criticality; map them to processes, assertions and key controls | research-synthesis, review-assurance | Partners cite lack of in-house AI expertise (33%) and thin model documentation (26%) at their largest client [BOARDMEMBER-CAQ-2026] |
| Classify AI-enabled controls | Decide whether management relies on the AI output or re-performs it (COSO's "reliance" test) | review-assurance, expert-judgment | A working definition only; BDO's paraphrase differs from COSO's text [COSO-GENAI, BDO-ITGC] |
| Scope ITGCs to AI components | Extend access, change, operations and development controls to the model, pipelines, orchestration, agents and platforms | review-assurance, software-systems | Agents approve transactions and change access; components hosted by vendors [OPTRO-SURVEY, BDO-ITGC] |
| Choose evidence | Test AI outputs substantively, test AI-related controls, use SOC reports and representations, or test around the AI | review-assurance | Probabilistic, drifting models; no widely accepted method for black-box systems [KPMG-SOX-2026] |
| Monitor and evaluate deficiencies | Drift and override metrics, remediation logs; decide severity, including material weakness | data-reporting, expert-judgment | COSO says the definition of a control failure may need to move beyond pass/fail for GenAI [COSO-GENAI] |
| Fraud risk | Consider training-data tampering, model manipulation, fictitious documents | review-assurance | New schemes such as altered training data and fictitious documents [AT-AICPAPA-2026] |
| Communicate | Audit committee dialogue; disclosure controls over AI statements | client-interaction | Only 56% of committee members confident in the committee's AI oversight [DELOITTE-ACPR-2026] |
| **Area 2** Scope and criteria | Pick assessment type (governance, conformity, performance) and criteria (ISO 42001, Trust Services Criteria plus AI, AIUC-1, bespoke) | expert-judgment | No AI-specific criteria; "scope negotiation" [JOFA-EVAL, CSA-SOC2] |
| Readiness and gap work | AI inventory, risk register, policies against ISO 42001 or NIST AI RMF | review-assurance, document-production | BSI will not certify a system another part of BSI consulted on [BSI-ANAB-2026] |
| Certification audit or attestation testing | Two-stage audit then annual surveillance; or design and operating tests for an ISAE 3000 opinion | review-assurance | Access to models, data and documentation [JOFA-EVAL, DSIT-ROADMAP-2025] |
| Technical testing | Adversarial, performance, robustness and bias tests | review-assurance, software-systems | Developers rarely grant access; quarterly re-testing for agents [JOFA-EVAL, FIELDGUIDE-AIUC1-2026] |
| Report, certificate or opinion | Certificate, opinion, or "evaluation report" | document-production | "Assurance" can be a regulated term; report types differ [JOFA-EVAL, EY-AIASSESS-2025] |
| Accreditation of assurers | Accreditation bodies witness audits and assess certifiers against ISO/IEC 42006 | review-assurance | Supplier base growing faster than accreditation, per CSA [CSA-AIASSURE-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate or redesign the flow (process scope), delegate (an agent owns an
outcome), reinvent (`change_scope: model`, new services and roles). Here "changing the work" mostly means AI as a new
audit object and new services. Only six entries have AI doing assurance work (augment: `#05`, `#06`, `#11`, `#19`,
`#25`; delegate, as an idea: `#27`). **No evidence was found for automate or delegate**; do not invent it.

**Inventory, scoping and classification (Area 1)**
- Improve: `#01` idea: a living AI inventory mapped to assertions and key controls (COSO, AICPA, BDO). `#02` reliance
  versus non-reliance, plus a three-class view of the AI's role (decides, flags, supplements) from a vendor citing PwC.

**ITGCs and evidence for AI-operated controls**
- Redesign: `#03` extend ITGCs to models, pipelines and agents (native, UI-driven, headless) and choose between testing
  outputs, testing AI controls or testing around (AICPA aid); builds on `assurance-controls-testing-15`. `#04` evidence trail: retained prompts,
  model versions, reviewer records; research on tamper-evident agent records. `#05` idea: monitoring metrics,
  multi-metric tolerance ranges and remediation logs as evidence.
- Improve: `#06` idea: re-perform outputs with test populations or challenger models. `#07` idea: SOC reports and
  AI-specific representations for vendor AI. `#08` idea: AI-enabled fraud schemes in the fraud-risk assessment.
- Redesign: `#25` a third-party agent-evaluation attestation (about 1,400 tests) goes to the client's external
  auditors as input to a SOX audit, with assurance tiered by agent risk (MSCI, a larger public company; vendor case study).

**Governance oversight**
- Improve: `#09` audit committee dialogue with the auditor and disclosure controls over AI statements (survey-backed).
  `#10` internal audit using the IIA AI Auditing Framework and COSO's capability taxonomy.
- Redesign: `#11` idea: continuous, AI-assisted assurance over AI instead of an annual cycle.

**Standalone assurance services (Area 2)**
- Improve: `#12` scope each engagement as governance, conformity or performance assessment and say which. `#26`
  scope agent engagements with AIUC's developer-versus-deployer matrix (78 core controls: 33, 40, 5).
- Reinvent: `#13` readiness and gap assessments (Deloitte, KPMG NL). `#14` ISAE (UK) 3000 "SOC 2+" reasonable-assurance
  opinion over AI governance (KPMG UK; announced). `#15` ISO/IEC 42001 certification (BSI clients Umony and Accelleo;
  Schellman). `#19` AIUC-1 agent certification with insurance (KPMG aIQ Capture, Fieldguide, Sierra). `#20` system-level
  technical assurance (BSI, Deloitte, KPMG NL). `#21` New York City bias audits (independent study: regime not
  effective). `#22` EU AI Act conformity (deadlines moved to 2027 and 2028).
- Redesign: `#23` buyer-side register checks and the CSA STAR for AI registry. For the AICPA and AIUC joint SOC 2
  plus AIUC-1 engagement (19 Oct 2026) see `assurance-soc-attestation-17`.
- Reinvent (idea): `#27` CPAs build an "audit package" so reviewers can verify AI-generated analysis (a CPA-developer's maths case).

**Market and quality infrastructure**
- Reinvent: `#16` accrediting certifiers against ISO/IEC 42006. `#17` firms certify their own AI management systems
  (KPMG, PwC Taiwan, EY Italy). `#18` new service lines (EY suite, EY CertifyPoint, PwC Canada). `#24` professionalising
  assurers (UK consortium, ISACA AAIA credential).

Coverage: ladder assist 21, augment 5, automate 0, delegate 1 (idea); scope step 9, process 6, model 12. Grades: B 7,
C 13, D (ideas) 7, A 0.

## 4. Interview probes

Ask in the person's setting: external auditor, SOX or internal audit lead, CFO or audit committee, or AI assurance provider.

1. **"Which AI touches your close, key controls or reports? Who keeps the inventory, and when was it last refreshed?"** Reveals whether `#01` exists and how much shadow AI there is. Only 6% of partners rate their largest client's AI governance advanced.
2. **"For each AI-touched control, does management rely on the output or re-perform it?"** Reveals the evidence standard owed (`#02`). Under reliance COSO expects prompt, configuration, model version and sampling rationale.
3. **"Are you testing around the AI or relying on it? What evidence did you take?"** Reveals exposure to KPMG's forecast of first AI-related material weaknesses in 2027 (`#03`, `#07`).
4. **"Do access reviews cover AI agents (ERP-native, UI-driven, headless)? Are prompts, retrieval connectors and thresholds under change control?"** Reveals the ITGC gap (`#03`). 38% let agents approve or reject transactions.
5. **"When AI flags or decides, what do you keep? Could you reconstruct what an agent did last quarter?"** Reveals evidence-trail readiness (`#04`).
6. **"How would you define a deviation for a probabilistic control? Do you track overrides and drift?"** Reveals whether monitoring exists or point-in-time testing is all there is (`#05`).
7. **"What has your external auditor asked about AI, and what do you bring the audit committee that is not a policy list?"** Reveals dialogue maturity (`#09`); about two-thirds of audit partners say their committee raised AI.
8. **Provider: "Who buys AI assurance from you (procurement, board, regulator, insurer) and what triggered it?"** Reveals demand pull; no general mandate exists, and EU high-risk dates have moved (`#14`, `#22`, `#23`).
9. **Provider: "Which shape do you sell: readiness, ISO 42001 certification, ISAE 3000 opinion, agent certification, technical testing? How do you keep consulting apart from certification, and what can you sell to audit clients?"** Reveals impartiality and independence exposure (`#13`-`#19`).
10. **"What criteria and assurance level do you use, and how do you get access to models, data and documentation?"** Reveals scope negotiation and the access problem (`#12`, `#20`).
11. **"Who staffs the work (IT audit, controls assurance, data science), with which credentials?"** Reveals competence against ISO/IEC 42006 team rules and AAIA uptake (`#16`, `#24`).
12. **"How do you price it against a SOC 2, and have you issued a report yet?"** Reveals commercial maturity. No fee or issued Big Four report was found publicly.

## 5. Metrics and benchmarks

**Client readiness (surveys; self-reported views, not outcomes)**
- CAQ Audit Partner Pulse (Spring 2026): largest client's AI governance 6% advanced, 40% developed but incomplete,
  46% early-stage; 57% call AI governance the top audit-committee challenge [BOARDMEMBER-CAQ-2026].
- Deloitte/CAQ committees (248 respondents): AI governance in the top three for 75% (35% a year earlier); 56%
  confident; primary responsibility 20% to 29%; 82% of overseeing committees call oversight emerging or limited; 70%
  want technology skills [DELOITTE-ACPR-2026, AT-ACPR-2026].
- Internal audit leaders: 63% of organisations without formal AI risk appetite or governance; 28% confident they can
  audit AI risks (vendor-published) [OPTRO-FOF-2025].
- Agents (Optro, 400+ GRC and audit leaders, vendor-published): agents approve or reject transactions 38%, modify
  controls 34%, change access 27%; 25% report a control failure involving an agent, 30% an unintended action [OPTRO-SURVEY].

**Market (government estimates and provider counts)**
- UK AI assurance: about GBP 1.01bn gross value added in 2024, 524+ companies [DSIT-ROADMAP-2025]; 84 specialised
  firms (17 in a 2023 government study), 12,572 employees [DSIT-ASSURANCE-2024]. 2035 potential: GBP 6.53bn (2024 report) versus
  GBP 18.8bn (2025 roadmap); the reason for the gap was not found.
- Schellman: 26 signed ISO 42001 clients in Oct 2024; ANAB accreditation took about eight months [SCHELLMAN-AT-2024].
- BSI research: 26% of organisations taking steps to align with ISO/IEC 42001; no sample stated [BSI-ANAB-2026].
- AIUC-1: 78 core controls (Q4 2026), typically 33 met by the developer, 40 by the deployer, 5 by the independent
  evaluator [AIUC-Q4-2026]; about 1,400 tests across 112 privileged roles on one MSCI agent [AIUC-MSCI-2026]; 900+ tests before KPMG's aIQ Capture certification; first AIUC-1-backed policy (ElevenLabs) $50M cover; quarterly re-tests
  [AIUC-KPMG-2026, FORKAST-AIUC-2026, SIERRA-AIUC1-2026].

**Independent research (the only independent quality evidence)**
- 435 AI audit tools and 35 practitioner interviews: tools support evaluation more than accountability [OJEWALE-2024].
- Only a subset of AI audit studies lead to accountability outcomes [BIRHANE-2024].
- New York City bias audits: 16 interviews; the law has not created an effective audit regime [GROVES-2024].
- Agent auditability: 617 security findings across six open-source agent projects; tamper-evident mediation
  costs a median 8.3 ms (prototype) [NIAN-AUDITABLE-2026].

**Not found**: fees or margins (the CSA note cites six to twelve months and tens of thousands of dollars for a first
ISO 42001 certification from a consultancy source not checked here; low confidence) [CSA-AIASSURE-2026]; certificate counts; issued
AI assurance opinions; disclosed AI-caused material weaknesses; inspection findings.

**What to measure (suggest these)**: share of AI-touched controls inventoried and classified; agent identities covered
by access reviews; COSO's monitoring indicators (accuracy, precision and recall, coverage, latency, exception volumes)
plus override rates [COSO-GENAI, DART-COSO-2026]; time to reconstruct an agent action; for providers, engagements by
shape, report types issued, access obtained and re-test findings.

## 6. Guardrails

**Standards and regulators (no general mandate for external AI assurance) [K-UKCA]**
- **COSO** (23 Feb 2026): GenAI guidance building on the 2013 framework, not a new framework; eight capability types; a
  working "reliance" definition and the evidence it triggers [COSO-GENAI, DART-COSO-2026, KPMG-COSO-2026].
- **AICPA practice aid** (13 Oct 2026; 51 pages [CFODIVE-AICPAPA-2026]): the entity's AI use, AI-operated controls,
  service organisations; the auditor cannot rely on tests of controls alone where models drift or are probabilistic; sections on
  risk of material misstatement and audit evidence to follow [AICPA-PA-2026, AT-AICPAPA-2026].
- **PCAOB**: technology-assisted-analysis amendments (AS 1105, AS 2301) include testing relevant ITGCs but are not
  AI-specific (secondary source) [CALCPA-AISTD-2026].
- **IAASB**: Technology Catalog v3 (9 Jul 2026) lists AI assurance as a matter for information gathering and asks
  whether ISAE 3000 (Revised) suffices [IAASB-CATALOG-2026]. ISAE (UK) 3000 is the basis KPMG UK cites [KPMGUK-GOVAI-2026].
- **ISO**: 42001 certifies a management system, not an AI system's performance [HUMANITIX-BABL-2026]; 42006 adds
  certifier rules on top of ISO/IEC 17021-1 [EVS-42006-2025]. BSI, an accredited body, does not certify what another
  part of BSI consulted on [BSI-ANAB-2026].
- **EU AI Act**: Article 43 puts Annex III points 2-8 on internal control; Omnibus moves high-risk dates to 2 Dec 2027
  and 2 Aug 2028 [EU-AIACT-ART43-2024, AG-OMNIBUS-2026].
- **UK**: accredited management-system certification is the most feasible near-term quality route; a regulated
  profession judged premature [DSIT-ROADMAP-2025, ICAEW-ROADMAP-2025]. **New York City**: annual independent bias
  audits of hiring tools [GROVES-2024]. "Assurance" can be a regulated term [JOFA-EVAL].

**Design guardrails from the sources**
- Classify reliance before choosing evidence; under reliance keep the AI "bill of materials" (prompts, outputs,
  system messages, model version, parameters, plugins) [COSO-GENAI].
- Extend existing ITGC categories to AI components and agent identities rather than inventing new ones [BDO-ITGC].
- A review step that rubber-stamps AI output "provides no real control value" [KPMG-SOX-2026]; reviewers need the knowledge
  to judge AI reliability [AT-AICPAPA-2026].
- Check a certifier's accreditation and scope, not just the certificate; ask for insurance policy terms behind
  insured badges [CASRAI-42006-2026, CSA-AIASSURE-2026].
- Keep readiness consulting apart from certification, and test independence before selling to audit clients
  [BSI-ANAB-2026, KPMGUS-ISO-2025].
- State the assessment type and whether an opinion is given [EY-AIASSESS-2025].

**Steps that stay with a person**: the reliance decision; whether a use case is financially relevant; deficiency
severity, including material weakness; criteria and scope; tolerance sign-off; the opinion or certification decision;
accreditation decisions.

## 7. Roles and how they evolve

- **IT auditors** must be as comfortable in a configuration log as in a ledger and scope ITGCs component by component
  [KPMG-SOX-2026, BDO-ITGC].
- **Audit teams** need a blend of audit, AI and data skills, skepticism and specialist support [AICPA-PA-2026]; EY describes
  a "two-in-the-box" AI auditor and IT professional [JOFA-EVAL].
- **Internal audit** faces an "AI credibility gap", in Richard Chambers' phrase [OPTRO-FOF-2025]; the IIA says
  auditors need not be experts on every topic and may use outside technical resources [IIA-AIFRAMEWORK-2024].
- **SOC and controls-assurance teams** extend into AI governance opinions [K-UKCA]; Schellman, which began as a
  SOC audit firm, moved into AI certification [SCHELLMAN-AT-2024, SCHELLMAN-AIUC1-2026].
- **Certifiers** use AI-experienced auditors; ISO/IEC 42006 judges competence at team level (secondary report)
  [BSI-UMONY-2026, CASRAI-42006-2026].
- **New entrants**: Deloitte Singapore hires AI assurance consultants (2-4 years), expects AI-regulation knowledge to
  grow on the job and treats ISO/IEC 42001 familiarity as an advantage [DELOITTE-JOB-SG-2026]; ISACA's AAIA opens to
  CISA, CIA, CPA, ACCA and ICAEW holders [ISACA-AAIA-2026]; DSIT sees AI auditing as a possible starting point for
  professional certification [DSIT-ROADMAP-2025].
- **Audit committees**: 70% want technology skills [DELOITTE-ACPR-2026]. **Procurement** gains a due-diligence step
  [KPMGUK-GOVAI-2026]. **CISOs** run tiered assurance programmes for agents (`#25`). **CPAs** are pitched as
  verifiers of machine output [JOFA-MATHEX-2026] (`#27`).

## 8. Frontier

- **2024-09** Schellman becomes the first ANAB-accredited ISO 42001 certifier [SCHELLMAN-AT-2024].
- **2025-07-07** ISO/IEC 42006 published [CASRAI-42006-2026, BRIGHT-42006-2026].
- **2025-09-03** UK trusted third-party AI assurance roadmap [DSIT-ROADMAP-2025]. **2025-09-23** KPMG NL adds AI Assurance [KPMGNL-AI-2025]. **2025-10-23** CSA launches STAR for AI [CSA-STARAI-2025].
- **2025-10-30** prEN 18286, first harmonised AI Act standard, enters public enquiry [EC-AISTANDARDS-2025].
- **2025-11 to 12** KPMG US and KPMG International certified to ISO 42001 [KPMGUS-ISO-2025, KPMGINTL-ISO-2025].
- **2025-11-20** European accreditation decision to make ISO/IEC 42006 mandatory (vendor report) [BRIGHT-42006-2026].
- **2026-02-03** Schellman named authorised AIUC-1 auditor [SCHELLMAN-AIUC1-2026]. **2026-02-16** PwC Canada ISO 42001 offer [CONSULTINGCA-PWC-2026]. **2026-02-23** COSO GenAI guidance [COSO-GENAI].
- **2026-03-10** BSI holds ANAB, UKAS and RvA accreditation [BSI-ANAB-2026].
- **2026-04-07** EY announces an AI assurance suite for audit and non-audit clients [EY-CANVAS-2026].
- **2026-05-19** SEC filer-status proposal would move about half of attested issuers out of 404(b) if adopted [UNIQUS].
- **2026-06-30** AIUC-1 trustmark on the STAR Registry [CSA-STAR-AIUC1-2026].
- **2026-07** AI Omnibus adopted and published (dates differ by source) [AG-OMNIBUS-2026, SIG-AIACT-2026]; IAASB adds AI assurance to its Technology Catalog [IAASB-CATALOG-2026].
- **2026-08-27** KPMG aIQ Capture is the first Big Four AIUC-1 certification [AIUC-KPMG-2026].
- **2026-09-22 / 24** KPMG UK markets AI governance assurance [KPMGUK-GOVAI-2026]; KPMG US sees a "new mandate" to assure AI systems [KPMG-SOX-2026].
- **2026-09-24** AIUC publishes the MSCI case (`#25`) [AIUC-MSCI-2026].
- **2026-09-28** UK consortium working on code of ethics, skills framework, information-access map [TECHUK-ROADMAP-2026].
- **2026-10-13** AICPA practice aid; more sections promised [AICPA-PA-2026]. **2026-10-15** AIUC developer-deployer guidance [AIUC-Q4-2026]. **2026-10-19** AICPA and AIUC joint SOC 2 plus AIUC-1 offering (`assurance-soc-attestation-17`).
- **End 2026 at the earliest** harmonised AI Act standards [DQS-OMNIBUS-2026]. **2027** first AI-related material weaknesses expected (KPMG forecast) [KPMG-SOX-2026]. **2027-12-02 / 2028-08-02** EU high-risk obligations apply [AG-OMNIBUS-2026].

## 9. Common objections

- **"Our auditor tests around the AI, so this doesn't apply yet."** KPMG says weaknesses have been avoided so far partly because programmes still test around the AI, expects working AI into the control environment to become unavoidable, and forecasts the first wave in 2027 [KPMG-SOX-2026]. Start with `#01` and `#02`; they cost little.
- **"There are no standards, so AI assurance is meaningless."** Partly fair: no AI-specific Trust Services Criteria [CSA-SOC2] and the IAASB is still gathering information [IAASB-CATALOG-2026]. But ISO 42001 with accredited certifiers and ISAE 3000 engagements exist; state the criteria and report type (`#12`).
- **"An ISO 42001 certificate proves the AI works."** No. It certifies a management system [HUMANITIX-BABL-2026]. Pair it with technical testing (`#19`, `#20`) and check the certifier's accreditation (`#16`, `#23`).
- **"The EU AI Act will force everyone to buy third-party assurance."** Most Annex III categories use internal control [EU-AIACT-ART43-2024] and dates moved to Dec 2027 and Aug 2028 [AG-OMNIBUS-2026]. Today's pull is procurement, investors and insurers [KPMGUK-GOVAI-2026, TECHUK-ROADMAP-2026].
- **"A person approves every AI output, so the control works."** Rubber-stamp review adds no control value [KPMG-SOX-2026]; the reviewer must be able to judge AI reliability [AT-AICPAPA-2026].
- **"We can't get access to the model."** Common [JOFA-EVAL, GROVES-2024, SCHELLMAN-AT-2024]. Test outputs, use SOC reports and representations (`#03`, `#07`); the UK consortium is mapping access rules (`#24`).
- **"Insurance-backed certification removes the risk."** Test counts measure activity, and payout behaviour in a systemic failure is unknown [FORKAST-AIUC-2026]; ask for policy terms [CSA-AIASSURE-2026].
- **"Our firm can do the readiness work, the certificate and the audit."** Impartiality rules and auditor independence limit that [BSI-ANAB-2026, KPMGUS-ISO-2025, CONSULTANCY-BIG4-2025].
- **"AI cannot audit itself."** A Prager Metis not-for-profit partner (Top 100 firm) says auditors test the information management gives them, whatever tool produced it [ATODAY-DAVIS-2026]. **"AI risk is just old risk."** A practitioner says reperformance and common-mode failure are where AI tests existing methods [AT-AUDITRISK-2026].
- **"Our ISO 42001 work and SOC 2 cover the agent."** MSCI's CISO says neither answered whether the agent "does what the policy says" (his statement as published by AIUC) [AIUC-MSCI-2026] (`#25`).
- **"AI audits create accountability."** Independent research finds only some do, tools fall short, and New York City's mandated audits have not worked well [BIRHANE-2024, OJEWALE-2024, GROVES-2024].

## 10. Mid-market firms

This section covers auditors of private, mid-market companies and the regional firms that might sell AI assurance.
- **Area 1 is the near-term work.** The practice aid's first part (nonauthoritative) guides financial-statement auditors, including those of private companies, to understand the client's AI in reporting and controls, consider it at acceptance and continuance, assess AI-specific risks (data, model, hallucination, explainability, bias, drift, AI-enabled fraud) and respond by testing outputs, AI controls or AI-related IT controls, with a service auditor's report and AI-related representations when AI is bought [AICPA-PA-2026, AT-AICPAPA-2026] (`#01`-`#08`). The ASB sets private-company audit standards and peer review monitors compliance [CFODIVE-AICPAPA-2026]; no ASB AI standard was found.
- **Evidence arrives from outside.** Clients may hand their auditor a third-party agent evaluation (`#25`, larger-company example) or an AIUC-1 report; the developer-deployer matrix shows what a deploying client must evidence itself (`#26`).
- **Area 2 at regional firms.** No mid-market CPA firm is named delivering the joint SOC 2 plus AIUC-1 offering (`assurance-soc-attestation-17`); one regional firm's job posting pairs ISO 42001 advisory with SOC work (`assurance-soc-attestation-18`).
- **Probes:** "On your last private-company audit where the client used AI in close or controls, what did you do at acceptance and risk assessment, and what did you ask for beyond a SOC report?" "How would you decide whether to test an AI-operated control's outputs or the control itself, and who reviews that choice?"

## 11. Sources

Full details (title, publisher, type, URL, date, access, locator) are in the YAML. Keys shared with controls-testing
keep that file's keys.
- **Standard-setters and regulators:** COSO-GENAI (COSO, 2026-02-23); IAASB-CATALOG-2026; EVS-42006-2025;
  DSIT-ROADMAP-2025; DSIT-ASSURANCE-2024; EU-AIACT-ART43-2024; EC-AISTANDARDS-2025.
- **Professional bodies:** AICPA-PA-2026 (2026-10-13); JOFA-EVAL; JOFA-FAST; IIA-AIFRAMEWORK-2024; ISACA-AAIA-2026;
  ICAEW-ROADMAP-2025; ICAEW-AIASSURE-2025; CALCPA-AISTD-2026; CSA-SOC2; CSA-AIASSURE-2026; CSA-STARAI-2025; CSA-CPAGUIDE-2026;
  CSA-STAR-AIUC1-2026; ACCA-EY-2025.
- **Firms:** KPMG-SOX-2026, K-404A, K-UKCA, KPMG-COSO-2026, KPMG-ACAGENDA-2025, KPMGUK-GOVAI-2026, KPMGUS-ISO-2025,
  KPMGINTL-ISO-2025, KPMGNL-AI-2025; DART-COSO-2026, DELOITTE-42001-2025, DELOITTE-AIA-UK-2026; EY-SOC-2026, EY-CANVAS-2026,
  EY-AIASSESS-2025, EY-COSO-2026, EYJP-CERTIFYPOINT-2026, EYIT-CERT-2025, EYIT-CERT-2026; BDO-ITGC; UNIQUS-GENAI-2026;
  EISNER-COSO-2026; BAKERTILLY-IA-2026; BAKERTILLY-SOC2-2025; SCHELLMAN-AIUC1-2026.
- **Vendors:** BSI-ANAB-2026, BSI-UMONY-2026, BSI-ACCELLEO-2026, SGS-PWCTW-2026, BRIGHT-42006-2026, AIUC-KPMG-2026,
  AIUC1-SITE-2026, AIUC-SERIES-A-2026, FIELDGUIDE-AIUC1-2026, COALFIRE-STAR-2025, OPTRO-SURVEY, OPTRO-FOF-2025,
  FINREP-JE-2026, KOGNITOS-SOXQ-2026, SIG-AIACT-2026, DQS-OMNIBUS-2026, AIUC-MSCI-2026, AIUC-Q3-2026, AIUC-Q4-2026.
- **Press:** AT-AICPAPA-2026, AT-COSO-2026, AT-ACPR-2026, BOARDMEMBER-CAQ-2026, SCHELLMAN-AT-2024, CONSULTINGCA-PWC-2026,
  REALTID-FT-2025, CONSULTANCY-BIG4-2025, FORKAST-AIUC-2026, SIERRA-AIUC1-2026, GIBSON-OMNIBUS-2026, AG-OMNIBUS-2026,
  TCC-ICFR-2026, CPAPA-ACCAEY-2025, CFOTECH-ACCAEY-2025, SFN-ACCAEY-2025, GENPACT-CAE-2026 (AI-generated summary;
  low authority), JOFA-MATHEX-2026, AT-AUDITRISK-2026, AT-PEEC-2026.
- **Surveys, academic, conferences, podcasts, community, jobs:** DELOITTE-ACPR-2026; GROVES-2024, BIRHANE-2024,
  OJEWALE-2024, MOKANDER-LLM-2023, MOKANDER-BLUEPRINT-2024, NIAN-AUDITABLE-2026, ARXIV-HARTMANN-2025;
  HUMANITIX-BABL-2026, ICAEW-AIAC-2026, TECHUK-ROADMAP-2026; CBH-POD-2025; CASRAI-42006-2026, SUBSTACK-JAIN-2025;
  DELOITTE-JOB-SG-2026.
- **Not in the YAML:** UNIQUS (Uniqus, *What the SEC's filer status overhaul means for ICFR governance*,
  2026-06-04, https://uniqus.com/what-the-secs-filer-status-overhaul-means-for-icfr-governance/; opened; the same
  document is UNIQUS in controls-testing.yaml).
- **Not in the YAML (added 2026-10-21, opened):** ATODAY-DAVIS-2026 (Accounting Today, *"AI cannot audit itself" - a
  response*, Scott Davis, Prager Metis, 2026-06-05, https://www.accountingtoday.com/opinion/ai-cannot-audit-itself-a-response);
  CFODIVE-AICPAPA-2026 (CFO Dive, *AICPA issues guidance for AI-assisted auditing*, 2026-10-13,
  https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/; in acceptance-independence YAML).
