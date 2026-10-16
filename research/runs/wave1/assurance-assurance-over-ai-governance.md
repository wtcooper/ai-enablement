# Deep dive: assurance-over-ai, governance & evidence angle

- **Archetype:** assurance
- **Module:** assurance-over-ai (auditing AI the entity uses in financial reporting and internal control; standalone assurance over AI systems)
- **Angle:** governance & evidence
- **Prepared:** 2026-10-16 (research run wave 1)
- **Landscape input:** `research/runs/wave1/landscape-assurance.md`

Method note: pages were fetched with `curl` through the session proxy (`pdftotext` for PDFs). `access: full` means the page or PDF was opened and the relevant parts read. Where a figure is attributed to a secondary report of a document that was not opened, this is stated. Web search was rationed and ran out before follow-up searches on SEC statements, NIST revision details, further academic work and national standard-setters, so those are listed under Gaps. Quotations are under 25 words.

---

## 1. Summary

- **Scale of the evidence.** 21 candidate use cases: 0 at grade A, 2 at B, 5 at C and 14 at D (labelled 'idea'). 45 sources were opened across 8 source types. No community or job-posting sources were found.
- **Evidence quality is thin on both sides of the module.** No error rates, override rates, parallel-run results or inspection findings were found for audits of entity AI, or for AI assurance engagements. The only independent measurements are academic (a 435-tool landscape and 35 practitioner interviews, OJEWALE-2024; a count of 617 security findings across six open-source agent projects, NIAN-AUDITABLE-2026) and the UK government's market sizing (DSIT-ASSURANCE-2025).
- **Area 1, auditing entity AI, is guidance-rich and practice-poor.**
  - COSO published *Achieving Effective Internal Control Over Generative AI* on 23 Feb 2026, with eight capability types, five components, 17 principles and a six-step roadmap (COSO-GENAI-2026; DART-COSO-2026).
  - The AICPA followed on 13 Oct 2026 with a 51-page practice aid whose part one covers the entity's AI use, AI-operated controls and service-organisation evidence (AICPA-PA-2026; CFODIVE-AICPAPA-2026).
  - BDO's 20 Jul 2026 article turns COSO's reliance test into ITGC scoping across the model, data pipelines, orchestration and agents (BDO-ITGC-2026).
  - No named audit engagement, regulator inspection result or measured outcome was found.
- **A reliance test is the pivot.** COSO's working definition says reliance exists when management depends on AI outputs as part of the evidence for an ICFR control; then ICFR-grade evidence applies (prompt, configuration and model version, sampling rationale, retained evidence) (COSO-GENAI-2026, p. 13).
- **Area 2, standalone assurance, has real named activity but no measurements.**
  - ISO/IEC 42001 certification audits by BSI have named clients (Umony, Accelleo) (BSI-UMONY-2026; BSI-ACCELLEO-2026).
  - BSI announced triple accreditation (ANAB, UKAS, RvA) on 10 Mar 2026 (BSI-ANAB-2026).
  - KPMG UK describes an ISAE (UK) 3000 AI governance opinion on SOC 2+ criteria (KPMGUK-GOVAI-2026; KPMGUK-CONTROLS-2026), and KPMG Nederland added AI Assurance in Sep 2025 (KPMGNL-AI-2025).
  - No issued report or named client was found for either KPMG service.
- **The standard-setters are watching, not yet setting.** The IAASB's July 2026 Technology Catalog lists "AI assurance" as a newly added matter at further-information-gathering stage, medium priority, and asks whether ISAE 3000 (Revised) is enough (IAASB-CATALOG-2026, p. 14).
- **The assurers' quality is the live concern.** ISO/IEC 42006 arrived about two years after ISO/IEC 42001, and the CSA note and the UK roadmap both stress accreditation and competence gaps (EVS-42006-2025; CSA-AIASSURE-2026; DSIT-ASSURANCE-2025).
- **EU AI Act conformity is delayed.** The AI Omnibus moved Annex III high-risk obligations to 2 Dec 2027 and Annex I to 2 Aug 2028, and harmonised standards are expected by end of 2026 at the earliest (AG-OMNIBUS-2026; SIG-AIACT-2026; DQS-OMNIBUS-2026).
- **A classification caveat.** In most entries the AI is the audited object, not the actor, so `ladder` is `assist` and `runtime_class` is nominal; the real change is in scoping, evidence standards and service models.

---

## 2. Use cases

Notes on fields: `provenance: n/a` appears only where the outcome description is "none published". Sources marked `access: search-only` are not used to support any outcome.

```yaml
- id: assurance-assurance-over-ai-01
  title: Scope the entity's AI use cases to financial-reporting processes, assertions and key controls
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: intake-triage
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Entities adopt generative AI through embedded features, vendor tools and unsanctioned use, so an auditor cannot tell which
    AI touches financial reporting. COSO names rapid change and uncontrolled adoption (shadow AI) as core risks (DART-COSO-2026).
    The AICPA says one early question is how far the company relies on AI in financial reporting (AICPA-PA-2026).
  solution: >-
    Work from a use-case inventory in which each use case is classified by capability type, given an owner, and described
    by objective, data sources, model, deployment model and criticality (COSO-GENAI-2026). Then map in-scope use cases to
    financial reporting processes, assertions and key controls, including controls over spreadsheets, tools, upstream data
    and interfaces (DART-COSO-2026). BDO says an effective IT audit starts with the entity's AI use cases, the related systems
    and service providers, and the governance around them (BDO-ITGC-2026). Deloitte adds that management should coordinate
    early with internal and external auditors on what counts as sufficient, appropriate evidence for GenAI-enabled controls
    (DART-COSO-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: COSO-GENAI-2026
  prerequisites:
  - A cross-functional AI governance structure that owns the inventory (COSO-GENAI-2026)
  - Periodic scans or surveys to find shadow AI (COSO-GENAI-2026)
  - A process to identify AI used by vendors and other third parties (AT-AICPAPA-2026)
  risks_and_guardrails:
  - >-
    COSO frames inventory as a repeating cycle, so a one-off list goes stale as models, prompts and vendors change (COSO-GENAI-2026).
  - Deloitte warns the guidance is not a prescriptive rulebook and builds on the 2013 framework (DART-COSO-2026).
  human_checkpoints:
  - Management signs off ownership and criticality per use case (COSO-GENAI-2026)
  - Auditor judges whether a use case is financially relevant (DART-COSO-2026)
  role_evolution: >-
    The AICPA says the audit team may need a blend of audit expertise, AI knowledge, data skills, professional skepticism
    and specialist support (AICPA-PA-2026). BDO places understanding of the entity's AI use first in the IT audit approach
    (BDO-ITGC-2026).
  evidence_grade: D
  sources:
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: pp. 18-19, roadmap steps 1-2 and example inventory entry
  - ref: DART-COSO-2026
    title: 'Heads Up: COSO Releases Publication on Internal Controls Related to Generative AI (Vol. 33, Issue 3)'
    publisher: Deloitte (DART)
    type: firm
    url: https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai
    date: '2026-04-03'
    access: full
    locator: section on six actions, items 1, 2 and 6
  - ref: AICPA-PA-2026
    title: >-
      AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing (news release on
      the practice aid Artificial Intelligence (AI) Considerations for Financial Statement Auditors)
    publisher: AICPA & CIMA
    type: professional-body
    url: >-
      https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing
    date: '2026-10-13'
    access: full
    locator: section 'Considering an organization's use of AI'
  - ref: BDO-ITGC-2026
    title: >-
      Artificial Intelligence: IT Audit Considerations with Focus on Information Technology General Controls (web article
      and PDF)
    publisher: BDO USA
    type: firm
    url: >-
      https://www.bdo.com/insights/assurance/artificial-intelligence-it-audit-considerations-with-focus-on-information-technology-general-control
    date: '2026-07-20'
    access: full
    locator: opening section 'Start with understanding'
  - ref: AT-AICPAPA-2026
    title: AICPA releases practice guide for auditors dealing with AI (12-minute read quoting the practice aid at length)
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai
    date: '2026-10-14'
    access: full
    locator: section on understanding the entity and its system of internal control
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): published guidance from COSO, the AICPA and firms; no named engagement or measured outcome found. The
    AI is the audited object here, so ladder and runtime_class are nominal. COSO's integrated case examples are illustrative
    and unnamed, so they are not counted as deployments.
- id: assurance-assurance-over-ai-02
  title: Classify AI-enabled controls as reliance or non-reliance to set the evidence standard
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Some AI-assisted controls are re-performed by a person and some are accepted on the AI output alone, yet both are called
    AI controls. Treating them alike makes evidence demands either too heavy or too light (COSO-GENAI-2026).
  solution: >-
    COSO adopts a working definition: reliance occurs when management depends on AI-generated outputs as part of the evidence
    supporting an ICFR control's design or operating effectiveness. Its reliance example is AI matching journal entries to
    support with management approving on the AI output alone; its non-reliance example is a control owner re-performing the
    match on all or a sample of items (COSO-GENAI-2026). Where reliance exists, COSO expects the same evidence standards as
    for ICFR: documented prompt, configuration and model version, a clear sampling rationale and exception resolution, and
    retained evidence of design and operation. For non-reliance cases evidence expectations may be proportionately lower (COSO-GENAI-2026).
    BDO applies the test to ITGC scoping and says ITGCs matter significantly more under reliance (BDO-ITGC-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: COSO-GENAI-2026
  prerequisites:
  - Use-case inventory mapped to key controls (DART-COSO-2026)
  - >-
    Logs that can support an AI 'bill of materials': prompts, outputs, system messages, model version, parameters and plugins
    (COSO-GENAI-2026)
  risks_and_guardrails:
  - >-
    COSO labels the definition a working definition drawn from emerging industry views, so it is not part of the 2013 framework
    (COSO-GENAI-2026).
  - >-
    BDO's paraphrase of the definition (re-performing or independently validating) is worded differently from COSO's text,
    so the two should not be treated as identical (BDO-ITGC-2026; COSO-GENAI-2026).
  human_checkpoints:
  - Control owner re-performs and documents review in non-reliance patterns (COSO-GENAI-2026)
  - Auditor decides which pattern applies to each control (BDO-ITGC-2026)
  role_evolution: >-
    Inference from the definition: control owners must show re-performance evidence and auditors must decide which pattern
    applies, which adds a classification step to controls scoping (COSO-GENAI-2026; BDO-ITGC-2026).
  evidence_grade: D
  sources:
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: p. 13, working definition of AI reliance and evidence list
  - ref: BDO-ITGC-2026
    title: >-
      Artificial Intelligence: IT Audit Considerations with Focus on Information Technology General Controls (web article
      and PDF)
    publisher: BDO USA
    type: firm
    url: >-
      https://www.bdo.com/insights/assurance/artificial-intelligence-it-audit-considerations-with-focus-on-information-technology-general-control
    date: '2026-07-20'
    access: full
    locator: section 'Control activities' (reliance example and ITGC importance)
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): guidance only; no engagement or measured outcome found. BDO states COSO's definition as depending on outputs
    'without sufficiently re-performing'; the COSO PDF read in this run words it differently (see Gaps).
- id: assurance-assurance-over-ai-03
  title: Extend ITGC scoping and testing to AI models, data pipelines, orchestration and agents
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - software-systems
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    ITGC testing was designed around applications, databases and operating systems, but AI-enabled processes add models, pipelines,
    orchestration software and agents that can read from and act on ERP systems (BDO-ITGC-2026). The AICPA notes traditional
    general IT controls may not address all AI-specific risks (AT-AICPAPA-2026).
  solution: >-
    BDO keeps the four ITGC domains (user access, program change, computer operations, program development) and extends them
    to AI components in scope: the model (foundation or fine-tuned), data pipelines, orchestration software, AI agents and
    enterprise AI platforms. Each component gets its own risk assessment and scoping that weighs the nature of the component,
    the degree of reliance and whether the entity or a service provider performs the control (BDO-ITGC-2026). BDO also asks
    whether ERP user-access reviews cover AI agents, and separates agents native to the ERP, external agents working through
    the user interface and headless agents using an API (BDO-ITGC-2026). The AICPA says AI-related IT controls may need testing,
    and that purchased AI may limit what the auditor can do (AT-AICPAPA-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: BDO-ITGC-2026
  prerequisites:
  - Component-level inventory of the AI ecosystem behind each in-scope use case (BDO-ITGC-2026)
  - Reliance classification per use case (BDO-ITGC-2026)
  - Access to service-provider controls or reports where components are hosted by vendors (BDO-ITGC-2026)
  risks_and_guardrails:
  - >-
    BDO says the key difference is the extension of existing ITGC categories to AI components, not new categories (BDO-ITGC-2026).
  - COSO says it does not repeat established ITGC guidance, which remains necessary (COSO-GENAI-2026).
  - >-
    The PCAOB's technology-assisted analysis amendments require testing of relevant ITGCs where applicable when testing controls
    over electronic information, but CalCPA stresses they are not AI-specific (CALCPA-AIREG-2026).
  human_checkpoints:
  - IT audit specialist scopes components per use case (BDO-ITGC-2026)
  - Engagement team decides how far ITGC testing must extend under reliance (BDO-ITGC-2026)
  role_evolution: >-
    BDO has auditors scope ITGCs component by component, which implies, by inference, that IT audit specialists need to understand
    model, pipeline and agent architectures (BDO-ITGC-2026).
  evidence_grade: C
  sources:
  - ref: BDO-ITGC-2026
    title: >-
      Artificial Intelligence: IT Audit Considerations with Focus on Information Technology General Controls (web article
      and PDF)
    publisher: BDO USA
    type: firm
    url: >-
      https://www.bdo.com/insights/assurance/artificial-intelligence-it-audit-considerations-with-focus-on-information-technology-general-control
    date: '2026-07-20'
    access: full
    locator: sections 'IT General Controls' and 'AI-related components'; PDF edition
  - ref: AT-AICPAPA-2026
    title: AICPA releases practice guide for auditors dealing with AI (12-minute read quoting the practice aid at length)
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai
    date: '2026-10-14'
    access: full
    locator: paragraph on traditional general IT controls and purchased AI
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: p. 6, scope and boundaries
  - ref: CALCPA-AIREG-2026
    title: 'AI Standard Setting, Regulation in Audit: Part 1'
    publisher: California Society of CPAs (CalCPA)
    type: professional-body
    url: https://www.calcpa.org/whats-happening/articles/ai-standard-setting-regulation-in-audit-part-1
    date: '2026-08-12'
    access: full
    locator: 'section ''PCAOB: The U.S. Issuer Landscape'', AS 1105 paragraph'
  last_reviewed: '2026-10-16'
  notes: >-
    Grade C: firm-published approach with an offer of services; no named engagement or measured outcome found. The CalCPA
    article is secondary; the PCAOB's own pages returned HTTP 403.
- id: assurance-assurance-over-ai-04
  title: >-
    Design audit responses for controls operated by AI by combining tests of AI outputs and tests of AI-related controls
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Some AI models continuously learn, drift and give probabilistic outcomes, so the testing strategy that works for deterministic
    automated controls may not carry over (AT-AICPAPA-2026). The less insight an auditor has into how an output was produced,
    the harder it is to become comfortable with it (AT-AICPAPA-2026).
  solution: >-
    The AICPA practice aid, as reported by Accounting Today, says the auditor may be able to test AI outputs substantively.
    If that alone cannot give sufficient appropriate evidence, the auditor designs tests of controls on operating effectiveness.
    In some cases traditional controls such as human review or monitoring can bring AI-related risk to an acceptable level;
    in others controls over data quality, model performance and safeguards need testing (AT-AICPAPA-2026). The aid also says
    the auditor cannot rely on tests of controls alone, and may need to establish relationships between inputs and outputs,
    and look to non-traditional information sources (AT-AICPAPA-2026). Further sections on assessing the risk of material
    misstatement and evaluating audit evidence when a company uses AI are promised (AICPA-PA-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: AT-AICPAPA-2026
  prerequisites:
  - >-
    Understanding of the AI mechanism under the control, including whether it is deterministic or probabilistic (AT-AICPAPA-2026)
  - Reliance classification and evidence set from entity (COSO-GENAI-2026)
  risks_and_guardrails:
  - >-
    The AICPA says risks vary with AI type, use case, whether the AI was built internally or bought, and whether an agentic
    layer sits on top (AT-AICPAPA-2026).
  - >-
    A simple one-to-one translation of existing risk guidance does not always work, because AI can change risks inherent to
    a class of transaction (AT-AICPAPA-2026).
  - >-
    The AICPA's chief auditor says the auditor's focus stays on material misstatement and control deficiencies relevant to
    the opinion (CFODIVE-AICPAPA-2026).
  human_checkpoints:
  - The reviewer in a human-in-the-loop control must have the knowledge to judge AI reliability (AT-AICPAPA-2026)
  - Auditor judges where evidence comes from when the process is opaque (AT-AICPAPA-2026)
  role_evolution: >-
    Auditors need to understand the AI mechanism behind a control as well as the control activity itself (AT-AICPAPA-2026).
  evidence_grade: D
  sources:
  - ref: AT-AICPAPA-2026
    title: AICPA releases practice guide for auditors dealing with AI (12-minute read quoting the practice aid at length)
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai
    date: '2026-10-14'
    access: full
    locator: sections on control activities, audit responses and audit evidence
  - ref: AICPA-PA-2026
    title: >-
      AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing (news release on
      the practice aid Artificial Intelligence (AI) Considerations for Financial Statement Auditors)
    publisher: AICPA & CIMA
    type: professional-body
    url: >-
      https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing
    date: '2026-10-13'
    access: full
    locator: paragraph on future additions to section one
  - ref: CFODIVE-AICPAPA-2026
    title: AICPA issues guidance for AI-assisted auditing
    publisher: CFO Dive
    type: press
    url: https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/
    date: '2026-10-13'
    access: full
    locator: interview paragraphs with Jennifer Burns
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: p. 13
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): non-authoritative guidance. The 51-page practice aid itself was not opened (member login); its content
    is read through Accounting Today, the AICPA release and CFO Dive. No auditor has published results of applying the approach.
- id: assurance-assurance-over-ai-05
  title: >-
    Use management's AI monitoring metrics, separate evaluations and remediation logs as audit evidence of control operation
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Point-in-time testing misses gradual model drift and vendor-driven changes, and 'set-and-forget' does not work when AI
    is used in financial reporting (DART-COSO-2026). COSO notes some risks such as gradual accuracy degradation are hard to
    detect through ongoing monitoring alone (COSO-GENAI-2026).
  solution: >-
    COSO expects continuous monitoring of indicators such as accuracy, precision and recall, coverage, latency and exception
    volumes, plus separate evaluations: periodic model effectiveness audits on historical and hypothetical data, independent
    challenge sessions and simulated adversarial exercises (COSO-GENAI-2026). It also expects a remediation log of issue,
    root cause, action and follow-up testing, and an agreed deficiency playbook (COSO-GENAI-2026). Deloitte lists transaction
    volume, transaction size and override percentages as indicators of drift, and calls for root-cause review of prompt design,
    retrieval issues and vendor changes (DART-COSO-2026). COSO says its illustrative metrics serve both operational monitoring
    and audit evidence collection (COSO-GENAI-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: COSO-GENAI-2026
  prerequisites:
  - >-
    Monitoring dashboards with thresholds linked to retraining, reconfiguration or rollback triggers (COSO-GENAI-2026)
  - Retained remediation logs with owner sign-offs (COSO-GENAI-2026)
  risks_and_guardrails:
  - >-
    COSO notes monitoring systems themselves need monitoring so their detection logic stays accurate (COSO-GENAI-2026).
  - >-
    Deficiencies from GenAI may be safety and reliability failures such as hallucinations in regulated disclosures, not only
    control gaps (COSO-GENAI-2026).
  human_checkpoints:
  - Human-in-the-loop quality reviews of a sample of transactions against a rubric (COSO-GENAI-2026)
  - Escalation to governance bodies when deficiencies are material (COSO-GENAI-2026)
  role_evolution: >-
    Inference: assurance providers would review metric trends and remediation history alongside samples, since both sources
    stress ongoing monitoring (DART-COSO-2026; COSO-GENAI-2026).
  evidence_grade: D
  sources:
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: pp. 16-17, monitoring activities; p. 4, audit-ready control mapping
  - ref: DART-COSO-2026
    title: 'Heads Up: COSO Releases Publication on Internal Controls Related to Generative AI (Vol. 33, Issue 3)'
    publisher: Deloitte (DART)
    type: firm
    url: https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai
    date: '2026-04-03'
    access: full
    locator: paragraph beginning 'Monitoring plays a key role'
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): the example in COSO (an expense-monitoring model retrained when monthly precision or recall drops below
    a threshold) is illustrative and unnamed. No published override rates, drift rates or parallel-run results from a named
    entity were found.
- id: assurance-assurance-over-ai-06
  title: Define control effectiveness for probabilistic AI through multi-metric tolerance ranges instead of pass/fail
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    A deviation-based pass/fail view of control failure fits deterministic automation, but GenAI outputs are probabilistic,
    so the definition of a control failure may need to change (COSO-GENAI-2026).
  solution: >-
    COSO's 'looking ahead' passage says organizations will increasingly rely on multi-metric AI tolerances. Performance would
    be defined by acceptable error or risk thresholds across dimensions such as task accuracy, data leakage tolerance, bias
    levels, explainability minimums, cybersecurity posture and model change velocity (COSO-GENAI-2026). COSO says such ranges
    may give a more realistic view of control effectiveness in dynamic GenAI environments (COSO-GENAI-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: COSO-GENAI-2026
  prerequisites:
  - Agreed tolerance ranges per use case, approved by control owners and risk (COSO-GENAI-2026)
  risks_and_guardrails:
  - >-
    The passage is forward-looking and phrased with 'may', so no assurance standard yet accepts multi-metric tolerance as
    a deviation definition (COSO-GENAI-2026).
  human_checkpoints:
  - Control owner and reviewers sign off tolerance changes (COSO-GENAI-2026)
  role_evolution: >-
    Inference: assurance providers would need statistical and model-evaluation skills to judge whether a tolerance range is
    credible (based on the dimensions in COSO-GENAI-2026).
  evidence_grade: D
  sources:
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: p. 16, 'Looking ahead' box under Principle 16
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): discussed by COSO's authors as a direction. The role_evolution sentence is an inference from the dimensions
    listed, not a statement in the source.
- id: assurance-assurance-over-ai-07
  title: >-
    Obtain evidence over vendor-supplied AI through service-auditor reports and AI-specific management representations
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Auditors have limited ability to run procedures on AI bought from a third party, and any vendor-supplied GenAI limits
    visibility into training data, model updates and underlying controls (AT-AICPAPA-2026; COSO-GENAI-2026).
  solution: >-
    The AICPA practice aid says that when an entity uses a service organization that provides AI services, or one that uses
    AI within its system, a service auditor's report often becomes important audit evidence. If that is not sufficient, additional
    procedures may include AI-related management representations, such as identification of the AI the entity uses (AT-AICPAPA-2026).
    It also asks whether the entity has a process to identify AI used by vendors and other third parties and to evaluate the
    effect on financial reporting (AT-AICPAPA-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: AT-AICPAPA-2026
  prerequisites:
  - Service-auditor reports whose scope covers the AI components (AT-AICPAPA-2026)
  - Entity process for identifying third-party AI (AT-AICPAPA-2026)
  risks_and_guardrails:
  - Third-party AI limits visibility into training data, model updates and change cadence (COSO-GENAI-2026).
  - >-
    The AICPA says the auditor's ability to perform certain procedures may be limited when the AI is bought from a third party
    (AT-AICPAPA-2026).
  human_checkpoints:
  - Auditor evaluates whether the service-auditor report covers the relevant AI controls (AT-AICPAPA-2026)
  role_evolution: >-
    User auditors must read service-auditor reports for AI scope and ask for representations that name the AI in use (AT-AICPAPA-2026).
  evidence_grade: D
  sources:
  - ref: AT-AICPAPA-2026
    title: AICPA releases practice guide for auditors dealing with AI (12-minute read quoting the practice aid at length)
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai
    date: '2026-10-14'
    access: full
    locator: paragraphs on service organizations and purchased AI
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: p. 6, third-party and vendor risk
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): guidance only. AICPA TQA 9561 on AI in SOC 1 and SOC 2 engagements (landscape item R21) was not reachable
    and is routed to the SOC module. Landscape item P14 (CSA note on SOC 2 and AI controls gaps) was not re-opened this run.
- id: assurance-assurance-over-ai-08
  title: Extend fraud-risk assessment to AI-specific manipulation and synthetic evidence
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    AI creates new routes for fraud: deepfakes, synthetic records and model manipulation through crafted prompts, and agents
    that bring authorization and interface risks (COSO-GENAI-2026).
  solution: >-
    COSO Principle 8 asks fraud risk assessment to identify how these threats could be used inside or outside the entity and
    whether existing fraud controls would catch them, and to expand preventive programs where needed (COSO-GENAI-2026). The
    AICPA practice aid adds examples: personnel altering training data or the algorithm to create bias, editing model attributes
    so fraudulent transactions classify as legitimate, and generating fictitious supporting documents (AT-AICPAPA-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: COSO-GENAI-2026
  prerequisites:
  - Use-case inventory including agents and their permissions (COSO-GENAI-2026)
  risks_and_guardrails:
  - COSO says agents can add authorization risk, excessive agency and insecure interfaces (COSO-GENAI-2026).
  human_checkpoints:
  - Fraud-risk discussion in the engagement team covers AI-enabled schemes (AT-AICPAPA-2026)
  role_evolution: >-
    Inference: specialist support in fraud-risk discussions grows where AI is in the reporting process; the aid says teams
    may need specialist support generally (AICPA-PA-2026).
  evidence_grade: D
  sources:
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: p. 11, Principle 8
  - ref: AT-AICPAPA-2026
    title: AICPA releases practice guide for auditors dealing with AI (12-minute read quoting the practice aid at length)
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai
    date: '2026-10-14'
    access: full
    locator: paragraph on AI-enabled fraud risk
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): guidance only. The planning-side treatment sits in planning-risk-assessment (see Routed). The role_evolution
    sentence is an inference; the aid says auditors need specialist support generally (AICPA-PA-2026).
- id: assurance-assurance-over-ai-09
  title: Re-perform AI-operated control outputs with independent test populations or challenger models
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    An auditor cannot inspect the reasoning of a probabilistic model, so confidence has to come from testing outputs against
    something independent (AT-AICPAPA-2026).
  solution: >-
    COSO lists methods now discussed by the assurance and risk community: human review ranging from full re-performance to
    risk-based sampling of exceptions; performance testing on test populations to check accuracy and completeness and stress-test
    edge cases; multi-model validation comparing outputs across independent AI models or deterministic benchmark algorithms;
    analytics monitoring of drift; and third-party validation or certification of models (COSO-GENAI-2026). COSO says these
    support management's assurance and auditor expectations of sufficient appropriate evidence (COSO-GENAI-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: COSO-GENAI-2026
  prerequisites:
  - Representative test populations and benchmark algorithms (COSO-GENAI-2026)
  - A second model or deterministic benchmark independent of the first (COSO-GENAI-2026)
  risks_and_guardrails:
  - >-
    For auditors' own tools the AICPA says a second AI tool checking the first does not reduce the auditor's supervision and
    review duties; this is an adjacent context (AT-AICPAPA-2026).
  human_checkpoints:
  - Human reviewers handle disagreements between model and challenger (COSO-GENAI-2026)
  role_evolution: >-
    Inference: assurance teams would need to build or buy challenger tooling and test sets to use the methods listed in COSO-GENAI-2026.
  evidence_grade: D
  sources:
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: p. 14, five leading approaches
  - ref: AT-AICPAPA-2026
    title: AICPA releases practice guide for auditors dealing with AI (12-minute read quoting the practice aid at length)
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai
    date: '2026-10-14'
    access: full
    locator: paragraph on one AI tool evaluating another
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): COSO calls the methods emerging industry practice but names no deployment. The AICPA statement concerns
    auditors' own tools, so it is adjacent and caps the grade. role_evolution is an inference.
- id: assurance-assurance-over-ai-10
  title: Require agent systems to produce tamper-evident, reconstructable action records
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - software-systems
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: >-
    Once an agent can call tools and trigger side effects, the question becomes whether its actions stay answerable after
    deployment, and an auditor needs trustworthy evidence to reconstruct behavior (NIAN-AUDITABLE-2026).
  solution: >-
    The paper separates accountability, auditability (the system property that makes accountability possible) and auditing
    (reconstructing behavior from trustworthy evidence). It defines five auditability dimensions: action recoverability, lifecycle
    coverage, policy checkability, responsibility attribution and evidence integrity, and proposes an Auditability Card for
    agent systems (NIAN-AUDITABLE-2026). COSO separately says that for significant-impact GenAI processes an AI 'bill of materials'
    should hold logs of prompts, outputs, system messages, model version, parameters and plugins (COSO-GENAI-2026).
  outcomes:
  - lever: risk
    description: Lower-bound ecosystem measurement suggests basic security prerequisites for auditability are widely unmet
    figure: '617'
    measures: security findings across six prominent open-source agent projects, as counted by the authors
    provenance: independent
    source_ref: NIAN-AUDITABLE-2026
  - lever: speed
    description: >-
      Pre-execution mediation with tamper-evident records added little runtime cost in the authors' feasibility tests
    figure: 8.3 ms
    measures: >-
      median overhead of pre-execution mediation with tamper-evident records in the authors' runtime feasibility results
    provenance: independent
    source_ref: NIAN-AUDITABLE-2026
  prerequisites:
  - Agent runtime that can mediate actions before execution (NIAN-AUDITABLE-2026)
  - Retained logs and configuration history (COSO-GENAI-2026)
  risks_and_guardrails:
  - >-
    The authors say no single mechanism suffices and describe detect, enforce and recover classes (NIAN-AUDITABLE-2026).
  - >-
    The results come from research prototypes and open-source projects, not audited enterprise deployments (NIAN-AUDITABLE-2026).
  human_checkpoints:
  - Responsibility attribution ties actions back to accountable people (NIAN-AUDITABLE-2026)
  role_evolution: >-
    Inference: assurance providers would need to evaluate logging design and evidence integrity as part of AI control testing
    (based on NIAN-AUDITABLE-2026 and COSO-GENAI-2026).
  evidence_grade: D
  sources:
  - ref: NIAN-AUDITABLE-2026
    title: Auditable Agents (arXiv 2604.05485, v4)
    publisher: Nian et al. (arXiv; condensed version accepted to ACM AI Summit 2026)
    type: academic
    url: https://arxiv.org/abs/2604.05485
    date: '2026-04-07'
    access: full
    locator: abstract (v4, last revised 2026-09-27)
  - ref: COSO-GENAI-2026
    title: Achieving Effective Internal Control Over Generative AI (32-page publication)
    publisher: COSO
    type: standard-setter
    url: https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf
    date: '2026-02-23'
    access: full
    locator: p. 13, general controls and AI bill of materials
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): academic position paper with prototype measurements; no named audited deployment. Figures describe the
    paper's own experiments and cap the grade. role_evolution is an inference.
- id: assurance-assurance-over-ai-11
  title: 'Audit GenAI in three layers: provider governance, model, and application'
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Existing audit procedures do not address the governance challenges of generative systems, which show emergent capabilities
    and adapt to many downstream tasks (MOKANDER-LLM-2023; MOKANDER-BLUEPRINT-2024).
  solution: >-
    The authors propose three complementary audit layers: governance audits of the providers that design and release the system,
    model audits after pre-training and before release, and application audits of products built on the model, coordinated
    so each informs the others (MOKANDER-LLM-2023; MOKANDER-BLUEPRINT-2024). Independent assessments of how AI audits have
    worked in practice found that only a subset of audit studies translate into the desired accountability outcomes (BIRHANE-2024).
    Interviews with 35 AI audit practitioners and a review of 435 tools found tools often fall short in supporting accountability
    (OJEWALE-2024).
  outcomes:
  - lever: quality
    description: Only some AI audit studies lead to accountability outcomes
    figure: subset (no count stated in the abstract)
    measures: >-
      audit studies that translate to desired accountability outcomes, per the authors' assessment of audits by regulators,
      law firms, civil society, journalism, academia and consultancies
    provenance: independent
    source_ref: BIRHANE-2024
  - lever: quality
    description: AI audit tools fall short on accountability
    figure: '435'
    measures: AI audit tools in the authors' landscape analysis, compared with needs voiced in 35 practitioner interviews
    provenance: independent
    source_ref: OJEWALE-2024
  prerequisites:
  - Cooperation of model providers for governance and model audits (MOKANDER-LLM-2023)
  - Tools that support accountability, not only evaluation (OJEWALE-2024)
  risks_and_guardrails:
  - >-
    The authors say audits cannot by themselves solve the risks and must be conducted in a structured, coordinated way (MOKANDER-LLM-2023).
  - The audit ecosystem is described as muddled and imprecise, which hampers mapping stakeholders (BIRHANE-2024).
  human_checkpoints:
  - Auditors at each layer feed findings to the others (MOKANDER-BLUEPRINT-2024)
  role_evolution: >-
    The Birhane paper taxonomizes AI audits done by regulators, law firms, civil society, journalism, academia and consultancies,
    so by inference AI audit work is spread across several kinds of provider (BIRHANE-2024).
  evidence_grade: D
  sources:
  - ref: MOKANDER-LLM-2023
    title: 'Auditing large language models: a three-layered approach (arXiv 2302.08500)'
    publisher: Mokander, Schuett, Kirk and Floridi (arXiv)
    type: academic
    url: https://arxiv.org/abs/2302.08500
    date: '2023-02-16'
    access: full
    locator: abstract
  - ref: MOKANDER-BLUEPRINT-2024
    title: A Blueprint for Auditing Generative AI (arXiv 2407.05338)
    publisher: Mokander, Curl and Kshirsagar (arXiv)
    type: academic
    url: https://arxiv.org/abs/2407.05338
    date: '2024-07-07'
    access: full
    locator: abstract
  - ref: BIRHANE-2024
    title: 'AI auditing: The Broken Bus on the Road to AI Accountability (arXiv 2401.14462)'
    publisher: Birhane, Steed, Ojewale, Vecchione and Raji (arXiv; IEEE SaTML 2024)
    type: academic
    url: https://arxiv.org/abs/2401.14462
    date: '2024-01-25'
    access: full
    locator: abstract
  - ref: OJEWALE-2024
    title: 'Towards AI Accountability Infrastructure: Gaps and Opportunities in AI Audit Tooling (arXiv 2402.17861, v3)'
    publisher: Ojewale et al. (arXiv)
    type: academic
    url: https://arxiv.org/abs/2402.17861
    date: '2024-02-27'
    access: full
    locator: abstract
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): academic frameworks; the two empirical papers (Birhane, Ojewale) measure the audit ecosystem, not a layered
    audit. Only abstracts were read for all four papers.
- id: assurance-assurance-over-ai-12
  title: Run an end-to-end internal algorithmic audit that produces a document set at each development stage
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Practitioners find it hard to identify harms in their own systems before deployment, and emergent issues after deployment
    are difficult to trace to their source (RAJI-2020).
  solution: >-
    The authors introduce a framework for internal algorithmic auditing applied throughout the development lifecycle. Each
    audit stage yields documents that together form the audit report, drawing on the organization's values or principles to
    assess decisions made along the way (RAJI-2020).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: RAJI-2020
  prerequisites:
  - Organization-level principles to audit against (RAJI-2020)
  risks_and_guardrails:
  - It is an internal audit by the developing organization, so it does not replace external assurance (RAJI-2020).
  human_checkpoints:
  - Audit documents are reviewed at each lifecycle stage (RAJI-2020)
  role_evolution: >-
    The framework is applied inside the developing organization throughout its development lifecycle, so the audit work sits
    with that organization's own teams (RAJI-2020).
  evidence_grade: D
  sources:
  - ref: RAJI-2020
    title: >-
      Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing (arXiv 2001.00973)
    publisher: Raji et al. (arXiv)
    type: academic
    url: https://arxiv.org/abs/2001.00973
    date: '2020-01-03'
    access: full
    locator: abstract
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): 2020 academic framework by authors including industry researchers; pre-generative-AI and not tested here.
    Older than the 12-18 month window; kept as a foundation. Abstract only.
- id: assurance-assurance-over-ai-13
  title: >-
    Assess AI strategy, governance maturity and controls through internal audit using the IIA AI Auditing Framework
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Organizations look to internal audit for guidance on AI as adoption grows, while many internal auditors are not AI experts
    (IIA-AIFRAMEWORK-2024).
  solution: >-
    The IIA framework gives internal auditors structured, principles-based guidance to assess AI risks, governance, management
    and control processes, linked to the Three Lines Model. Auditors can use it to assess AI strategy and governance maturity,
    identify AI risks, evaluate controls over data, algorithms and cybersecurity, and provide assurance over AI-enabled processes;
    it includes a practitioner checklist and states it emphasizes reasonable assurance (IIA-AIFRAMEWORK-2024). The Portuguese
    edition says the auditor may act as adviser to management or as assurance provider, and that outside technical resources
    may be needed (IIA-AIFRAMEWORK-2024). The 2024 update added coverage of generative AI and large language models (IIA-AIFRAMEWORK-2024).
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: IIA-AIFRAMEWORK-2024
  prerequisites:
  - AI inventory and strategy to audit against (IIA-AIFRAMEWORK-2024)
  risks_and_guardrails:
  - >-
    The checklist is a quick-start guide that should be customised to organizational maturity (IIA-AIFRAMEWORK-2024).
  - Internal auditors are not expected to master every technical aspect of AI (IIA-AIFRAMEWORK-2024).
  human_checkpoints:
  - Chief audit executive decides advisory versus assurance posture (IIA-AIFRAMEWORK-2024)
  role_evolution: >-
    The framework treats AI auditing as a progression rather than a destination and encourages building a trusted-adviser
    relationship with the audit committee on AI (IIA-AIFRAMEWORK-2024).
  evidence_grade: D
  sources:
  - ref: IIA-AIFRAMEWORK-2024
    title: >-
      The IIA's Artificial Intelligence Auditing Framework (public page and Portuguese-language PDF edition, updated Sep 2024)
    publisher: The IIA
    type: professional-body
    url: https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/
    date: '2024-09-13'
    access: full
    locator: public page; Portuguese PDF Parts 1-4, pp. 11-12 and 21
  - ref: IIA-COSO-2026
    title: COSO Issues GenAI Guidance
    publisher: Internal Auditor (The IIA)
    type: professional-body
    url: https://internalauditor.theiia.org/en/articles/2026/march/coso-issues-genai-guidance/
    date: '2026-03-11'
    access: full
    locator: paragraph on intended audience
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): published guidance; no named internal audit function's results found. The first version dates from 2017
    per the PDF; the Sep 2024 update is the current one. The IIA's English framework text is member-only; the Portuguese edition
    was read.
- id: assurance-assurance-over-ai-14
  title: Certify an AI management system to ISO/IEC 42001 through a two-stage accredited audit
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Customers, banks and defence buyers want evidence that an AI developer's governance works, but cannot inspect the vendor's
    models or pipelines directly (CSA-AIASSURE-2026; BSI-UMONY-2026).
  solution: >-
    A certification body audits the organization's AI management system against ISO/IEC 42001. BSI's Umony case describes
    rigorous scoping, a specialist pre-assessment by AI-experienced auditors, targeted training, and a two-stage audit focused
    on risk assessment, impact assessment, controls and evidence (BSI-UMONY-2026). BSI's Accelleo case describes achieving
    ISO/IEC 27001 and 42001 together under the Annex SL structure (BSI-ACCELLEO-2026). The CSA note describes a two-stage
    initial audit followed by annual surveillance audits over a three-year certificate cycle (CSA-AIASSURE-2026).
  outcomes:
  - lever: growth
    description: Umony reports enhanced credibility in enterprise sales and supply-chain assurance
    figure: none
    measures: qualitative claim on the certifier's own case study page; no figure given
    provenance: vendor-published
    source_ref: BSI-UMONY-2026
  - lever: risk
    description: Accelleo reports a harmonized approach to risk and governance and clients adopting AI with confidence
    figure: none
    measures: qualitative claim on the certifier's case study page; no figure given
    provenance: vendor-published
    source_ref: BSI-ACCELLEO-2026
  prerequisites:
  - Defined AIMS scope, objectives and interfaces (BSI-UMONY-2026)
  - Policies, roles, controls and KPIs across the AI lifecycle (BSI-UMONY-2026)
  - An accredited certification body (CSA-AIASSURE-2026)
  risks_and_guardrails:
  - >-
    The CSA note advises buyers to check the certifying body's accreditation, not only that a certificate exists (CSA-AIASSURE-2026).
  - >-
    The UK roadmap says the standards that could underpin certification are limited in number and scope, which curbs near-term
    quality gains (DSIT-ASSURANCE-2025).
  - >-
    ISO/IEC 42006 followed ISO/IEC 42001 by about two years, so earlier certificates were issued without an AI-specific certifier
    competence standard (CSA-AIASSURE-2026).
  human_checkpoints:
  - Certification body auditors decide stage 1 and stage 2 outcomes (BSI-UMONY-2026)
  - Annual surveillance audits re-check the system (CSA-AIASSURE-2026)
  role_evolution: >-
    Certifiers use AI-experienced auditors for pre-assessment and audit, and ISO/IEC 42006 sets competence rules for them
    (BSI-UMONY-2026; EVS-42006-2025).
  evidence_grade: B
  sources:
  - ref: BSI-UMONY-2026
    title: Umony achieves ISO/IEC 42001 certification for responsible AI (case study)
    publisher: BSI
    type: vendor
    url: >-
      https://www.bsigroup.com/en-GB/insights-and-media/insights/case-studies/umony-achieves-isoiec-42001-certification-for-responsible-ai/
    date: '2026'
    access: full
    locator: case study, sections 'The Challenge' and 'The Solution' (page undated; retrieved 2026-10-16)
  - ref: BSI-ACCELLEO-2026
    title: Accelleo builds trusted defence AI with ISO/IEC 42001 (case study)
    publisher: BSI
    type: vendor
    url: >-
      https://www.bsigroup.com/en-GB/insights-and-media/insights/case-studies/accelleo-builds-trusted-defence-ai-with-iso-iec-42001/
    date: '2026'
    access: full
    locator: case study, section 'The Solution' (page undated; retrieved 2026-10-16)
  - ref: CSA-AIASSURE-2026
    title: Who Assures the Assurers? Third-Party AI Assessment Standards (research note)
    publisher: Cloud Security Alliance, AI Safety Initiative
    type: professional-body
    url: https://labs.cloudsecurityalliance.org/research/csa-research-note-third-party-ai-assurance-standards-2026092/
    date: '2026-09-27'
    access: full
    locator: '''Background'' section on certification cycle'
  - ref: DSIT-ASSURANCE-2025
    title: Trusted third-party AI assurance roadmap
    publisher: UK Department for Science, Innovation and Technology (GOV.UK)
    type: regulator
    url: >-
      https://www.gov.uk/government/publications/trusted-third-party-ai-assurance-roadmap/trusted-third-party-ai-assurance-roadmap
    date: '2025-09-03'
    access: full
    locator: section on accreditation, limitations paragraph
  last_reviewed: '2026-10-16'
  notes: >-
    Grade B: named certifications without published measurements; both case studies are written by the certifier. CSA cites
    vendor-side market data of six to twelve months and tens of thousands of dollars in audit fees, four to six months with
    an existing ISO/IEC 27001 certificate; this run did not open that source, so it stays out of outcomes. BSI's release also
    gives 26% of organizations taking steps to align with ISO/IEC 42001 (BSI-ANAB-2026), with no stated denominator.
- id: assurance-assurance-over-ai-15
  title: Accredit and oversee AI management system certifiers against ISO/IEC 42006
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Certification is only as trustworthy as the body that issues it, and the CSA note assesses that the AI assurance supplier
    base is growing faster than accreditation can vet entrants (CSA-AIASSURE-2026).
  solution: >-
    ISO/IEC 42006 sets additional requirements, on top of ISO/IEC 17021-1, for bodies that audit and certify AI management
    systems, and is aimed at certification bodies and the accreditation bodies that assess them (EVS-42006-2025). BSI announced
    ANAB accreditation for ISO/IEC 42001 on 10 March 2026, adding to UKAS and RvA accreditations, and describes itself as
    the first certifier holding all three (BSI-ANAB-2026). The UK roadmap says UKAS was piloting accreditation for ISO/IEC
    42001 certification and that accredited management system certification may be the most feasible near-term quality route
    (DSIT-ASSURANCE-2025).
  outcomes:
  - lever: risk
    description: BSI holds accreditation for ISO/IEC 42001 certification from three national accreditation bodies
    figure: '3'
    measures: national accreditation bodies (ANAB, UKAS, RvA) that BSI says have accredited it to certify ISO/IEC 42001
    provenance: self-reported
    source_ref: BSI-ANAB-2026
  prerequisites:
  - ISO/IEC 17021-1 certification body foundations (EVS-42006-2025)
  - Auditor competence in AI-specific areas such as data quality and transparency (EVS-42006-2025)
  risks_and_guardrails:
  - >-
    The CSA note says accreditation against the older general baseline alone does not guarantee AI-specific auditor competence
    (CSA-AIASSURE-2026).
  - >-
    Schellman also describes itself as the first ANAB-accredited certification body for ISO 42001, while BSI claims the first
    UKAS accreditation, so 'first' claims are self-described (SCHELLMAN-AIUC1-2026; BSI-ANAB-2026).
  human_checkpoints:
  - Accreditation bodies assess certifiers' competence, impartiality and consistency (BSI-ANAB-2026)
  role_evolution: >-
    Certification bodies need auditors trained for AI and accreditation assessors who can judge them (EVS-42006-2025).
  evidence_grade: B
  sources:
  - ref: EVS-42006-2025
    title: New international standard sets rules for auditing AI management systems (news item on ISO/IEC 42006)
    publisher: EVS (Estonian Centre for Standardisation and Accreditation), crediting IEC
    type: standard-setter
    url: https://www.evs.ee/en/auditing-ai-management-systems
    date: '2025-08-05'
    access: full
    locator: whole news item
  - ref: BSI-ANAB-2026
    title: BSI secures ANAB accreditation to certify ISO/IEC 42001
    publisher: BSI
    type: vendor
    url: >-
      https://www.bsigroup.com/en-AU/insights-and-media/media-centre/press-releases/2026/march/bsi-secures-anab-accreditation-to-certify-isoiec-42001/
    date: '2026-03-10'
    access: full
    locator: first two paragraphs
  - ref: DSIT-ASSURANCE-2025
    title: Trusted third-party AI assurance roadmap
    publisher: UK Department for Science, Innovation and Technology (GOV.UK)
    type: regulator
    url: >-
      https://www.gov.uk/government/publications/trusted-third-party-ai-assurance-roadmap/trusted-third-party-ai-assurance-roadmap
    date: '2025-09-03'
    access: full
    locator: accreditation section
  - ref: CSA-AIASSURE-2026
    title: Who Assures the Assurers? Third-Party AI Assessment Standards (research note)
    publisher: Cloud Security Alliance, AI Safety Initiative
    type: professional-body
    url: https://labs.cloudsecurityalliance.org/research/csa-research-note-third-party-ai-assurance-standards-2026092/
    date: '2026-09-27'
    access: full
    locator: '''Key Takeaways'' and ''Security Analysis'''
  - ref: SCHELLMAN-AIUC1-2026
    title: Schellman Becomes the First Accredited Auditor for AIUC-1, the Security Standard for AI Agents
    publisher: Schellman
    type: firm
    url: https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1
    date: '2026-02-03'
    access: full
    locator: quote by Avani Desai
  last_reviewed: '2026-10-16'
  notes: >-
    Grade B: named accreditations announced by the accredited body itself; no measurements. The CSA note's disclaimer on AI
    assistance, noted in the landscape file, was not found on the page text this run, so its claims are used only where another
    source agrees. BSI-ANAB-2026 is the certifier's own press release.
- id: assurance-assurance-over-ai-16
  title: Issue a reasonable-assurance opinion on AI governance and controls under ISAE (UK) 3000 using SOC 2+ criteria
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Organizations need more than internal confidence that AI governance works in practice, and customers, regulators and procurement
    teams ask for a defensible explanation of accountability and controls (KPMGUK-GOVAI-2026).
  solution: >-
    KPMG UK describes an AI Governance Assurance product that combines its Trusted AI framework, controls assurance skills
    and SOC principles to give independent assurance over AI governance and controls in accordance with ISAE (UK) 3000. It
    tests whether controls are clearly defined, suitably designed against the Trust Services Criteria and informed by its
    Trusted AI framework (which it says incorporates relevant EU AI Act and ISO/IEC 42001 requirements), and operating effectively,
    and provides a report shareable with customers (KPMGUK-GOVAI-2026). KPMG's January 2026 paper calls this a reasonable-assurance
    opinion via a 'SOC 2+' approach, and says the work scopes the AI estate, tests controls, examines evidence and reports
    on management's process, controls and claims (KPMGUK-CONTROLS-2026).
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: KPMGUK-GOVAI-2026
  prerequisites:
  - An AI inventory so systems are traceable and monitored (KPMGUK-CONTROLS-2026)
  - An AI strategy and governance framework as the basis for criteria (KPMGUK-CONTROLS-2026)
  risks_and_guardrails:
  - >-
    KPMG's paper states there is currently no prescriptive regulatory framework mandating external AI assurance (KPMGUK-CONTROLS-2026).
  - >-
    The IAASB says questions remain about subject matter and suitable criteria for AI assurance and whether ISAE 3000 (Revised)
    suffices, and is only gathering information (IAASB-CATALOG-2026).
  - >-
    KPMG notes key risks in AI-enabled services often sit at application, workflow, oversight and third-party layers, not
    only the model (KPMGUK-GOVAI-2026).
  human_checkpoints:
  - The practitioner tests controls and examines evidence before a formal assurance opinion (KPMGUK-CONTROLS-2026)
  role_evolution: Controls assurance and SOC teams extend into AI governance engagements (KPMGUK-GOVAI-2026).
  evidence_grade: C
  sources:
  - ref: KPMGUK-GOVAI-2026
    title: Independent confidence in how you govern AI (AI Governance Assurance)
    publisher: KPMG UK
    type: firm
    url: https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html
    date: '2026-09-22'
    access: full
    locator: sections 'Make AI Trust Stand Up to Scrutiny' and 'Regulation'
  - ref: KPMGUK-CONTROLS-2026
    title: 'Reimagining Controls Assurance with AI: Latest Insights for Leaders'
    publisher: KPMG UK
    type: firm
    url: >-
      https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf
    date: 2026-01
    access: full
    locator: p. 2 partner note ('introducing a reasonable-assurance opinion'); p. 7-8 'Assurance of AI'
  - ref: IAASB-CATALOG-2026
    title: Technology Catalog of Issues and Possible Actions, Version 3 (28-page PDF)
    publisher: IAASB
    type: standard-setter
    url: >-
      https://ifacweb.blob.core.windows.net/publicfiles/2026-07/IAASB-Technology-Catalog-of-Issues-Proposed-Actions.pdf
    date: '2026-07-09'
    access: full
    locator: p. 14, matter 10(b) AI assurance
  last_reviewed: '2026-10-16'
  notes: "Grade C: firm service description. KPMG's January 2026 paper says it is 'introducing' the opinion, and no issued\
    \ report or named client was found, so maturity is announced. The 18% testing-time reduction in the same paper concerns\
    \ AI used to perform controls assurance, an adjacent process, and is routed (see Routed). "
- id: assurance-assurance-over-ai-17
  title: Independently check AI systems, algorithms and data analytics against recognised standards
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    The impact of AI failure grows as AI moves into daily operations, and incidents from bias, privacy problems and unforeseen
    errors can cause reputational damage and lost revenue (KPMGNL-AI-2025).
  solution: >-
    KPMG Nederland added AI Assurance to its Responsible AI services in September 2025 to provide independent checks of AI
    systems, algorithms and data analytics an organization uses or offers. The service builds on the Trusted AI Framework
    and integrates the AI Act, ISO 42001 and the NIST AI RMF into its methods, and sits beside AI governance support and gap
    analyses and readiness scans with technical checks such as robustness tests (KPMGNL-AI-2025). The ACCA and EY paper separates
    performance assessments (measuring systems against predefined quality and performance metrics) from governance and conformity
    assessments (CFOTECH-ACCAEY-2025).
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: KPMGNL-AI-2025
  prerequisites:
  - Defined criteria drawn from recognised standards (KPMGNL-AI-2025)
  risks_and_guardrails:
  - >-
    The ACCA and EY paper says current assessment frameworks lack robustness and calls for well-specified objectives, defined
    methods and criteria, and competent, objective and accountable providers (CFOTECH-ACCAEY-2025).
  human_checkpoints:
  - KPMG says it can give an independent opinion in the AI domain based on recognised standards (KPMGNL-AI-2025)
  role_evolution: >-
    KPMG presents the service as an extension of decades of assurance over financial figures to AI systems (KPMGNL-AI-2025).
  evidence_grade: C
  sources:
  - ref: KPMGNL-AI-2025
    title: KPMG Nederland voegt AI Assurance toe aan haar Responsible AI-aanbod (press release, Dutch)
    publisher: KPMG Nederland
    type: firm
    url: >-
      https://kpmg.com/nl/nl/home/media/press-releases/2025/09/kpmg-start-met-onafhankelijke-controles-van-ai-systemen.html
    date: '2025-09-23'
    access: full
    locator: press release, sections on AI Assurance and components (event date 23 Sep 2025 on page)
  - ref: CFOTECH-ACCAEY-2025
    title: EY & ACCA urge trustworthy AI with robust assessment frameworks
    publisher: CFOtech UK
    type: press
    url: https://cfotech.co.uk/story/ey-acca-urge-trustworthy-ai-with-robust-assessment-frameworks
    date: '2025-08-05'
    access: full
    locator: section 'Types of assessments'
  last_reviewed: '2026-10-16'
  notes: >-
    Grade C: firm announcement in Dutch; no client or report named. The page's metadata date (2026-10-13) differs from the
    23-09-2025 event date shown in the text, so the earlier date is used.
- id: assurance-assurance-over-ai-18
  title: Scope an AI assessment engagement as governance, conformity or performance assessment
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    The word 'audit' is used for very different third-party evaluations of AI, which blurs what a report does and does not
    tell a user (SFN-ACCAEY-2025; landscape note on ACCA-EY-2025).
  solution: >-
    The ACCA and EY policy paper describes three types: governance assessments of internal oversight, conformity assessments
    against laws and standards, and performance assessments against predefined metrics, ranging from technical evaluations
    to traditional assurance and audits (CPAPA-ACCAEY-2025; SFN-ACCAEY-2025). EY's global assurance vice-chair links the work
    to EY's existing capabilities in assessments, readiness evaluations and compliance (CFOTECH-ACCAEY-2025).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: CFOTECH-ACCAEY-2025
  prerequisites:
  - Clear purpose and criteria for each assessment (CFOTECH-ACCAEY-2025)
  risks_and_guardrails:
  - >-
    The paper recommends policymakers define assessment purposes and criteria and align standards internationally (CFOTECH-ACCAEY-2025).
  human_checkpoints:
  - Not described in the sources; the paper asks for clear purposes, methods and criteria (CFOTECH-ACCAEY-2025)
  role_evolution: The paper calls for competent, objective and professionally accountable providers (SFN-ACCAEY-2025).
  evidence_grade: C
  sources:
  - ref: CPAPA-ACCAEY-2025
    title: EY and ACCA Share New Guidance on AI Assessments to Boost Confidence in AI Systems
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/?p=166602
    date: '2025-08-04'
    access: full
    locator: article body
  - ref: CFOTECH-ACCAEY-2025
    title: EY & ACCA urge trustworthy AI with robust assessment frameworks
    publisher: CFOtech UK
    type: press
    url: https://cfotech.co.uk/story/ey-acca-urge-trustworthy-ai-with-robust-assessment-frameworks
    date: '2025-08-05'
    access: full
    locator: article body, EY quote
  - ref: SFN-ACCAEY-2025
    title: ACCA and EY share new guidance to help businesses boost confidence in AI
    publisher: Scottish Financial News
    type: press
    url: >-
      https://www.scottishfinancialnews.com/articles/acca-and-ey-share-new-guidance-to-help-businesses-boost-confidence-in-ai
    date: '2025-08-05'
    access: full
    locator: article body
  - ref: ACCA-EY-2025
    title: >-
      AI Assessments: Enhancing Confidence in AI (policy paper; not opened, DNS failure on accaglobal.com; carried from landscape
      and press copies)
    publisher: ACCA and EY
    type: professional-body
    url: https://www.accaglobal.com/policy-and-insights/reports/2025/ai-enhancing-confidence
    date: 2025-08
    access: search-only
    locator: policy paper (not opened)
  last_reviewed: '2026-10-16'
  notes: >-
    Grade C: a taxonomy from a professional body and a firm that sells assessments. The paper itself was not opened (DNS failure);
    press copies agree on the three types. The 'audit' labelling issue comes from the landscape's reading of the paper and
    is not independently confirmed here.
- id: assurance-assurance-over-ai-19
  title: Certify AI agents through quarterly technical testing, a named auditor and insurance backing (AIUC-1)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - software-systems
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    Procurement teams face bespoke risk assessments of AI agents, and legal teams face uncertain liability (SCHELLMAN-AIUC1-2026).
  solution: >-
    AIUC-1 is a security, safety and reliability standard for AI agents; certification involves thousands of adversarial scenarios
    and quarterly testing of agent behavior. In the Schellman arrangement the Artificial Intelligence Underwriting Company
    runs technical evaluations and issues certification while Schellman provides audit evidence collection, reporting and
    guidance (SCHELLMAN-AIUC1-2026). CSA let STAR Registry listings carry an AIUC-1 trustmark from June 2026 (CSA-STAR-AIUC1-2026).
    The CSA note says AIUC-1 pairs certification with underwriting, citing insurance up to $50 million behind one certified
    agent (CSA-AIASSURE-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: SCHELLMAN-AIUC1-2026
  prerequisites:
  - An agent system that can be tested against adversarial scenarios (SCHELLMAN-AIUC1-2026)
  risks_and_guardrails:
  - >-
    Schellman's release says it is the first 'authorized' auditor while the CSA note says first 'accredited'; the difference
    matters when judging a badge (SCHELLMAN-AIUC1-2026; CSA-AIASSURE-2026).
  - >-
    The CSA note says buyers should ask for the specific policy terms and limits behind insurance-backed claims (CSA-AIASSURE-2026).
  human_checkpoints:
  - >-
    AIUC issues certification after its technical evaluations and Schellman's evidence collection and reporting (SCHELLMAN-AIUC1-2026)
  role_evolution: A CPA-firm auditor combines audit evidence work with another party's technical testing (SCHELLMAN-AIUC1-2026).
  evidence_grade: C
  sources:
  - ref: SCHELLMAN-AIUC1-2026
    title: Schellman Becomes the First Accredited Auditor for AIUC-1, the Security Standard for AI Agents
    publisher: Schellman
    type: firm
    url: https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1
    date: '2026-02-03'
    access: full
    locator: release body, 'AIUC-1 Certification Overview' (first published 2026-02-03; page updated 2026-09-29)
  - ref: CSA-STAR-AIUC1-2026
    title: >-
      Cloud Security Alliance Extends AI Assurance Leadership Into Agentic AI With Addition of AIUC-1 Certification to STAR
      Registry
    publisher: Cloud Security Alliance
    type: professional-body
    url: >-
      https://cloudsecurityalliance.org/press-releases/2026/06/30/csa-extends-leadership-into-agentic-ai-with-addition-of-aiuc-1-certification-to-star-registry
    date: '2026-06-30'
    access: full
    locator: release body
  - ref: CSA-AIASSURE-2026
    title: Who Assures the Assurers? Third-Party AI Assessment Standards (research note)
    publisher: Cloud Security Alliance, AI Safety Initiative
    type: professional-body
    url: https://labs.cloudsecurityalliance.org/research/csa-research-note-third-party-ai-assurance-standards-2026092/
    date: '2026-09-27'
    access: full
    locator: '''Background'' and ''Security Analysis'''
  last_reviewed: '2026-10-16'
  notes: >-
    Grade C: vendor claims; no primary certificate seen. The $50 million insurance example and the ElevenLabs reference come
    from the CSA note quoting a trade press report (Forkast News, 16 Sep 2026) not opened here, so they stay out of outcomes.
    The 'accredited' versus 'authorized' wording differs between sources.
- id: assurance-assurance-over-ai-20
  title: Demonstrate high-risk AI conformity under the EU AI Act through internal-control or notified-body assessment
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    High-risk AI providers must show conformity with the Act's requirements, but harmonised standards and conformity-assessment
    capacity are not ready (DQS-OMNIBUS-2026; CSA-AIASSURE-2026).
  solution: >-
    For Annex III point 1 systems where the provider has applied harmonised standards, Article 43(1) lets the provider opt
    for conformity assessment based on internal control (Annex VI) or assessment of the quality management system and technical
    documentation with a notified body (Annex VII). For Annex III points 2 to 8, providers follow the internal control procedure
    (EU-AIACT-ART43-2024). The Commission has asked CEN and CENELEC for standards in ten areas including quality management
    and conformity assessment, and the first harmonised AI standard, prEN 18286 on quality management, entered public enquiry
    on 30 October 2025 (EC-AISTANDARDS-2025). The AI Omnibus (Regulation (EU) 2026/1744) moved Annex III obligations to 2
    December 2027 and Annex I obligations to 2 August 2028 (AG-OMNIBUS-2026; SIG-AIACT-2026).
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: EU-AIACT-ART43-2024
  prerequisites:
  - Published and cited harmonised standards for presumption of conformity (EC-AISTANDARDS-2025)
  - Designated notified bodies where that route applies (CSA-AIASSURE-2026)
  risks_and_guardrails:
  - >-
    DQS reports CEN and CENELEC missed an autumn 2025 target and expect delivery by end of 2026 at the earliest (DQS-OMNIBUS-2026).
  - >-
    DQS counts 8 of 27 member states with fully designated competent authorities as of March 2026, while the CSA note cites
    a report that only three had designated both notifying and market-surveillance authorities; the two figures measure different
    things (DQS-OMNIBUS-2026; CSA-AIASSURE-2026).
  - >-
    Application of harmonised standards is voluntary, and providers may use other frameworks (EC-AISTANDARDS-2025).
  human_checkpoints:
  - Provider or notified body signs off conformity (EU-AIACT-ART43-2024)
  role_evolution: >-
    Conformity-assessment bodies must be designated and independent of providers; supply is tight (CSA-AIASSURE-2026).
  evidence_grade: D
  sources:
  - ref: EU-AIACT-ART43-2024
    title: 'Article 43: Conformity Assessment, Regulation (EU) 2024/1689 (third-party reproduction of the Act''s text)'
    publisher: artificialintelligenceact.eu (text of the Regulation published in the EU Official Journal)
    type: regulator
    url: https://artificialintelligenceact.eu/article/43/
    date: '2024-07-12'
    access: full
    locator: paragraphs 1-2 (page reproduces Article 43; its 'comes into force 2 August 2026' note pre-dates the Omnibus)
  - ref: EC-AISTANDARDS-2025
    title: Standardisation of the AI Act
    publisher: European Commission (Shaping Europe's digital future)
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation
    date: 2025-10
    access: full
    locator: sections 'How are standards developed' and prEN 18286 paragraph
  - ref: DQS-OMNIBUS-2026
    title: 'EU AI Act: Parliament and Council Align on Postponing High-Risk AI Obligations'
    publisher: DQS Global (blog)
    type: vendor
    url: >-
      https://www.dqsglobal.com/en/about/newsroom/eu-ai-act-parliament-and-council-align-on-postponing-high-risk-ai-obligations
    date: '2026-04-27'
    access: full
    locator: section 'Why the Delay?'
  - ref: HL-OMNIBUS-2026
    title: EU legislators agree to delay for high-risk AI rules
    publisher: Hogan Lovells (via JD Supra)
    type: press
    url: https://www.jdsupra.com/legalnews/eu-legislators-agree-to-delay-for-high-5617765/
    date: '2026-05-08'
    access: full
    locator: sections on extended timelines and next steps
  - ref: AG-OMNIBUS-2026
    title: 'EU AI Act: AI Omnibus formally adopted'
    publisher: Addleshaw Goddard
    type: press
    url: >-
      https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/
    date: '2026-07-01'
    access: full
    locator: first two paragraphs
  - ref: SIG-AIACT-2026
    title: A comprehensive EU AI Act Summary [August 2026 update]
    publisher: Software Improvement Group
    type: vendor
    url: https://www.softwareimprovementgroup.com/eu-ai-act-summary/
    date: '2026-08-14'
    access: full
    locator: '''What''s new in this August 2026 update'''
  - ref: CSA-AIASSURE-2026
    title: Who Assures the Assurers? Third-Party AI Assessment Standards (research note)
    publisher: Cloud Security Alliance, AI Safety Initiative
    type: professional-body
    url: https://labs.cloudsecurityalliance.org/research/csa-research-note-third-party-ai-assurance-standards-2026092/
    date: '2026-09-27'
    access: full
    locator: '''Security Analysis'' on notified-body capacity'
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): a legal requirement with no completed assessment found. Sources differ on approval dates: SIG gives Parliament
    16 Jun, Council 29 Jun, signature 8 Jul, publication 24 Jul and entry into force 27 Jul 2026; AG reports adoption on 1
    Jul 2026. The Official Journal was not opened. Only paragraphs 1-2 of Article 43 were checked; paragraphs on Annex I products
    were not.
- id: assurance-assurance-over-ai-21
  title: Agree structured information access between AI developers and assurance providers
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Assurance providers often struggle to obtain the information they need, ranging from white-box access to minimal documentation,
    while firms worry about exposing confidential training data or giving more than needed (DSIT-ASSURANCE-2025).
  solution: >-
    DSIT asked a consortium to map information access requirements for AI assurance providers, alongside a voluntary code
    of ethics and a skills and competencies framework (DSIT-ASSURANCE-2025). A techUK summit page dated 28 September 2026
    says that work is underway and lists information and data access as a workstream (TECHUK-ASSURANCE-2026).
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: no outcome figure published in the source
    provenance: n/a
    source_ref: DSIT-ASSURANCE-2025
  prerequisites:
  - Agreed access tiers between developers and assurance providers (DSIT-ASSURANCE-2025)
  risks_and_guardrails:
  - Firms using assurance may lack practices to share information safely (DSIT-ASSURANCE-2025).
  human_checkpoints:
  - >-
    Not described; the information-access mapping was still in progress at the techUK page date (TECHUK-ASSURANCE-2026)
  role_evolution: >-
    DSIT suggests AI auditing could be the first specialism for a professional certification scheme (DSIT-ASSURANCE-2025).
  evidence_grade: D
  sources:
  - ref: DSIT-ASSURANCE-2025
    title: Trusted third-party AI assurance roadmap
    publisher: UK Department for Science, Innovation and Technology (GOV.UK)
    type: regulator
    url: >-
      https://www.gov.uk/government/publications/trusted-third-party-ai-assurance-roadmap/trusted-third-party-ai-assurance-roadmap
    date: '2025-09-03'
    access: full
    locator: sections on professionalisation and information access
  - ref: TECHUK-ASSURANCE-2026
    title: 'One year on: the Trusted Third-Party AI Assurance Roadmap (summit page)'
    publisher: techUK
    type: conference
    url: https://www.techuk.org/events/one-year-on-the-trusted-third-party-ai-assurance-roadmap
    date: '2026-09-28'
    access: full
    locator: paragraphs on consortium progress and 'What we'll cover'
  last_reviewed: '2026-10-16'
  notes: >-
    Grade D (idea): UK policy workstream; no published output found. The techUK page also reports over 12,000 people employed
    in the UK AI assurance ecosystem and no agreed competency framework.
```

---

## 3. Module notes

### Processes and key steps (with work types)

**Area 1: auditing AI the entity uses in financial reporting and internal control**

- Understand the entity's AI use, its effect on reporting, and who owns it: research-synthesis, review-assurance (AICPA-PA-2026; BDO-ITGC-2026).
- Management's six-step cycle that the auditor tests against: establish governance, inventory use cases, assess risks by COSO component, design and map controls, implement and communicate, monitor and adapt (COSO-GENAI-2026, pp. 18-19).
- Identify AI-operated controls and controls that use AI-generated information; assess fraud risk including AI manipulation: review-assurance (AT-AICPAPA-2026; COSO-GENAI-2026, p. 11).
- Classify each AI-enabled control as reliance or non-reliance: review-assurance (COSO-GENAI-2026, p. 13).
- Scope ITGCs to AI components (model, pipelines, orchestration, agents, platforms): review-assurance, software-systems (BDO-ITGC-2026).
- Design responses: substantive tests of AI outputs and/or tests of AI-related controls; use service-auditor reports where AI is bought: review-assurance (AT-AICPAPA-2026).
- Evaluate deficiencies and root causes (configuration errors, retrieval issues, prompt design, data quality, model changes outside change control, vendor changes) and communicate them: review-assurance, document-production (COSO-GENAI-2026, p. 16).

**Area 2: standalone assurance over AI systems**

- Scope the engagement as a governance, conformity or performance assessment: expert-judgment (CPAPA-ACCAEY-2025; SFN-ACCAEY-2025).
- Readiness or gap analysis and pre-assessment: research-synthesis, review-assurance (KPMGNL-AI-2025; BSI-UMONY-2026).
- ISO/IEC 42001 stage 1 and stage 2 audit, then annual surveillance over a three-year cycle: review-assurance (BSI-UMONY-2026; CSA-AIASSURE-2026).
- ISAE (UK) 3000 reasonable-assurance opinion on AI governance and controls: review-assurance, document-production (KPMGUK-GOVAI-2026).
- Technical testing such as robustness tests and quarterly adversarial testing of agents: review-assurance, software-systems (KPMGNL-AI-2025; SCHELLMAN-AIUC1-2026).
- Certifier accreditation against ISO/IEC 42006: review-assurance (EVS-42006-2025; BSI-ANAB-2026).
- EU AI Act conformity assessment, by internal control or notified body: review-assurance (EU-AIACT-ART43-2024).

### Common pain points

- Black-box limits: the less insight an auditor has into how an output was produced, the harder it is to become comfortable with it (AT-AICPAPA-2026). The IAASB notes technologies that are hard to understand, explain or interrogate challenge risk identification (IAASB-CATALOG-2026, p. 19).
- Purchased AI restricts the auditor's procedures, so reports from service auditors become central (AT-AICPAPA-2026).
- Standards assume human experts: the IAASB catalog flags that experts are presumed to be humans in the standards (IAASB-CATALOG-2026, p. 3, matter 7(c)).
- No agreed criteria for AI assurance: the IAASB asks what subject matter and suitable criteria apply (IAASB-CATALOG-2026, p. 14).
- Information access: providers often cannot get the information they need, from white-box access down to minimal documentation (DSIT-ASSURANCE-2025).
- Unclear and inconsistent labelling of third-party evaluations (landscape note on ACCA-EY-2025; the paper was not opened).
- Shortage of qualified certifiers and notified bodies (CSA-AIASSURE-2026; DQS-OMNIBUS-2026).
- COSO says ITGC guidance is not repeated and remains necessary, so teams must combine AI-specific and traditional controls (COSO-GENAI-2026, p. 6).

### Metrics and benchmarks (with sources)

- UK AI assurance market: over 524 companies and about £1.01 billion gross value added in 2024, with a potential £18.8 billion by 2035 if adoption barriers are addressed (DSIT-ASSURANCE-2025, introduction). Government estimate.
- UK AI assurance ecosystem employs over 12,000 people (TECHUK-ASSURANCE-2026, 'Why this matters now'). Trade association figure; source not stated on the page.
- The UK roadmap quotes a World Privacy Forum report suggesting as much as 38% of AI governance tools may use metrics that could result in harm (DSIT-ASSURANCE-2025, footnote 1). Secondary quote; the World Privacy Forum report was not opened.
- AI audit tooling: interviews with 35 AI audit practitioners and a landscape of 435 tools (OJEWALE-2024, abstract). Academic, independent.
- Agent auditability: 617 security findings across six prominent open-source projects; 8.3 ms median overhead of pre-execution mediation with tamper-evident records (NIAN-AUDITABLE-2026, abstract). Academic; research prototypes.
- BSI-published: 26% of organizations report taking steps to align with ISO/IEC 42001, and 62% of global business leaders expect to increase AI investment; the page gives no denominator or sample (BSI-ANAB-2026). Vendor-published.
- CSA note on market-supplied data: six to twelve months and tens of thousands of dollars in certification-body fees for a first ISO/IEC 42001 certification, four to six months with an existing ISO/IEC 27001 certificate (CSA-AIASSURE-2026, citing a consultancy blog not opened here). Low confidence; not used in outcomes.
- KPMG UK: testing-time reductions of about 18% from using AI in controls assurance engagements (KPMGUK-CONTROLS-2026, p. 2). Firm figure for an adjacent process (AI used to perform assurance), routed.
- Carried from the landscape and not re-opened this run (treat as leads): CAQ Audit Partner Pulse, Spring 2026, in which 6% of audit partners rated AI governance at their largest client as advanced, 40% as developed but incomplete or inconsistent and 46% as early-stage or reactive, and 57% called AI governance the top audit-committee challenge (CAQ-PULSE-2026); ISACA's 2026 poll, in which 38% of 3,400+ digital-trust professionals had a formal, comprehensive AI policy (ISACA-PULSE-2026); IFIAR's 2024 observation that automated tools were frequently seen in 39% of members' IT application and security configuration reviews (IFIAR-TTF-2025).

### Guardrails and regulatory points

- COSO and the AICPA practice aid are non-regulatory guidance; Deloitte says COSO's guidance builds on the 2013 framework and is not a prescriptive rulebook (DART-COSO-2026). KPMG states there is currently no prescriptive regulatory framework mandating external AI assurance (KPMGUK-CONTROLS-2026, p. 8).
- NIST's AI RMF 1.0 is voluntary; the NIST page says it is being revised as part of the White House AI Action Plan, and records a Generative AI Profile (26 Jul 2024 per the page) and an April 2026 concept note for a critical-infrastructure profile (NIST-AIRMF-2023). The CSA note says the RMF declined to define a certification process (CSA-AIASSURE-2026).
- PCAOB: technology-assisted analysis amendments to AS 1105 and AS 2301 are effective for 2026 audits and require testing relevant ITGCs where applicable, but are not AI-specific, per a state CPA society article (CALCPA-AIREG-2026). The PCAOB's own pages were not reachable.
- FRC: the human auditor remains accountable, and firms should consider AI tool use within ISQM (UK) 1 (FRC-GENAINEWS-2026). That guidance concerns auditors' own tools, so it is routed.
- IAASB: ED ISA 330 proposals address how an entity's use of technology affects responses to assessed risks and tests of controls; the post-implementation review of ISA 315 (Revised 2019) is expected to start in Q3 2026 (IAASB-CATALOG-2026, p. 19).
- ISO/IEC 42006 supplements ISO/IEC 17021-1 for bodies certifying AI management systems, and can sit inside ISO/IEC 17065 schemes (EVS-42006-2025).
- EU AI Act: Article 43 sets internal-control and notified-body routes (EU-AIACT-ART43-2024); the Omnibus delays high-risk dates (AG-OMNIBUS-2026; SIG-AIACT-2026).
- UK: DSIT's roadmap says accredited management system certification may be the most feasible near-term quality route and notes UKAS was piloting 42001 accreditation (DSIT-ASSURANCE-2025).

### Frontier signals (dated)

- 2025-09-03: UK DSIT publishes the trusted third-party AI assurance roadmap; four immediate actions: a consortium, a skills framework, an information-access map and a £11 million AI Assurance Innovation Fund (DSIT-ASSURANCE-2025).
- 2025-09-23: KPMG Nederland adds AI Assurance to its Responsible AI services (KPMGNL-AI-2025).
- 2025-10-30: prEN 18286 on quality management for the AI Act enters public enquiry as the first harmonised AI standard (EC-AISTANDARDS-2025).
- 2026-02-03: Schellman announced as authorised auditor for AIUC-1 (SCHELLMAN-AIUC1-2026).
- 2026-02-23: COSO publishes generative AI internal control guidance (COSO-PRESS-2026).
- 2026-03-10: BSI announces ANAB accreditation for ISO/IEC 42001 (BSI-ANAB-2026).
- 2026-04-07 (v1) to 2026-09-27 (v4): "Auditable Agents" proposes an Auditability Card for agent systems (NIAN-AUDITABLE-2026).
- 2026-06-30: CSA lets STAR listings carry an AIUC-1 trustmark (CSA-STAR-AIUC1-2026).
- 2026-07: IAASB Technology Catalog version 3 adds AI assurance as a matter under information gathering (IAASB-CATALOG-2026, p. 14).
- 2026-07-24: AI Omnibus published in the Official Journal per SIG (SIG-AIACT-2026); AG reported formal adoption on 1 Jul 2026 (AG-OMNIBUS-2026).
- 2026-09-28: techUK summit on the roadmap one year on; consortium chaired by BCS working on a code of ethics, skills framework and information-access map; a Centre for AI Measurement led by NPL has launched (TECHUK-ASSURANCE-2026).
- 2026-10-13: AICPA practice aid issued; guidance on risk of material misstatement and audit evidence with AI to be added later (AICPA-PA-2026).
- By end of 2026 at the earliest: harmonised standards for the AI Act (DQS-OMNIBUS-2026).

### Workforce and role effects

- The AICPA says the audit team may need a blend of auditing expertise, AI knowledge, data skills, professional skepticism and specialist support (AICPA-PA-2026).
- For AI inside the reporting process, the human reviewer needs the right knowledge and expertise to judge reliability (AT-AICPAPA-2026).
- The IIA's framework says internal auditors are not expected to master every technical aspect of AI, and may use external technical resources (IIA-AIFRAMEWORK-2024, Portuguese PDF, p. 21).
- ISO/IEC 42006 sets competence requirements for AI management system auditors (EVS-42006-2025). DSIT's roadmap proposes a skills and competencies framework and says AI auditing could be the first specialism for professional certification (DSIT-ASSURANCE-2025).
- techUK states there is no agreed competency framework, unclear career pathways and no professional body to set and uphold standards (TECHUK-ASSURANCE-2026).
- ISACA's AI audit certification (AAIA) is open to holders of CISA and, with an IT audit or advisory focus, CIA, CPA, ACCA and equivalent designations, which, by inference, shows IT audit, internal audit and accounting credentials converging on AI audit (ISACA AAIA page opened this run; undated, so not listed in section 5).
- COSO's authors include practitioners from EY and Meta and academics, which, by inference, signals who shapes the criteria auditors will test against (JOFA-COSO-2026).

### Objections and concerns practitioners raise

- Black-box reasoning and the difficulty of evaluating inputs and outputs (AT-AICPAPA-2026; IAASB-CATALOG-2026, p. 19).
- Certificate quality: a certificate is only as trustworthy as the certifying body, and accreditation lags the standards (CSA-AIASSURE-2026).
- Whether an assurance service delivers accountability: only a subset of AI audit studies translate into the desired outcomes (BIRHANE-2024); tooling falls short on accountability (OJEWALE-2024).
- The IAASB asks whether existing ISAE 3000 (Revised), alone or with non-authoritative material, suffices or a subject-specific ISAE is needed (IAASB-CATALOG-2026, p. 15).
- Burden of evidence: a CalCPA article reports a PCAOB board member warning inspectors might ask firms to "turn over every rock" on AI model documentation, making AI-assisted procedures costlier to defend than sampling; this is secondhand and not verified against a PCAOB source (CALCPA-AIREG-2026).
- Definition risk: COSO's reliance definition is a working definition, and BDO paraphrases it differently (COSO-GENAI-2026, p. 13; BDO-ITGC-2026).
- Independence of AI assurance providers and tool vendors is a live question in the wider module set (routed, see section 4).

### Interview probes for an advisor

1. For the AI-enabled controls you have seen at clients, which did you treat as reliance and which as non-reliance, and what evidence did you ask for (prompt, configuration and model version, logs, sampling rationale)?
2. When an AI-operated control drifts, how do you define a deviation and a deficiency, and has anyone moved beyond pass/fail?
3. For standalone AI assurance, what criteria do you use (ISO/IEC 42001, Trust Services Criteria plus, NIST, bespoke), what level of assurance do you give, and how do you get access to models, data and documentation?
4. How do you show that your own certification or assurance work meets ISO/IEC 42006 or equivalent competence rules, and who does the technical testing?
5. Who staffs these engagements (IT audit, controls assurance, data science), what credentials do you require, and how do you price work with no stable scope?

---

## 4. Routed to other modules

| Item | Target module | Source ref and why |
|---|---|---|
| FRC guidance on generative and agentic AI in audit: three risk categories, certification, human-in-the-loop control points, two worked examples | quality-management (engagement-level supervision and review; firm-level tool governance) | FRC-GENAI-2026, FRC-GENAINEWS-2026: concerns the auditor's own tools, not the entity's AI. |
| AICPA practice aid part two: the firm's own AI use, quality management, one AI tool checking another, engagement-letter disclosure and state laws | quality-management; acceptance-independence | AT-AICPAPA-2026, CFODIVE-AICPAPA-2026: auditor's own use. |
| AICPA acceptance and continuance considerations when the client relies heavily on AI (comparison to complex valuation models; untraceable agent workflows) | acceptance-independence | AT-AICPAPA-2026. |
| AI-enabled fraud risk in planning; understanding the entity's use of IT and AI in risk assessment | planning-risk-assessment | AT-AICPAPA-2026; COSO-GENAI-2026, p. 11. |
| KPMG UK controls assurance with AI: about 18% testing-time reduction; AI in SOC 1, SOC 2, ISAE 3402 and ISAE (UK) 3000 engagements | controls-testing; other-assurance (SOC) | KPMGUK-CONTROLS-2026, p. 2: AI used to perform assurance, an adjacent process. |
| PCAOB AS 1105 and AS 2301 technology-assisted analysis amendments | substantive-testing; controls-testing | CALCPA-AIREG-2026 (secondary). |
| IAASB catalog matters 6(a) to 6(h) on technological tools, explainability, outliers and documentation | substantive-testing | IAASB-CATALOG-2026, p. 3. |
| IAASB catalog matters 7(b) and 7(c): management's expert and experts presumed to be humans | specialists | IAASB-CATALOG-2026, p. 3. |
| IAASB catalog matter 10(a) and ISSA 5000 | other-assurance (sustainability) | IAASB-CATALOG-2026, p. 14. |
| IAASB Technology Quality Management initiative (240+ participants, non-authoritative material approved Dec 2025) | quality-management | IAASB-TECH-2026. |
| AICPA TQA 9561 on AI in SOC 1 and SOC 2, and AI-specific Trust Services Criteria gaps | other-assurance (SOC) | Landscape items R21 and P14; not opened this run. |
| Independence of AI-assurance providers, tool vendors and private-equity-backed firms | acceptance-independence | Landscape items R22, R23; Schellman describes itself as a CPA firm and ISO certification body (SCHELLMAN-AIUC1-2026). |

---

## 5. Sources

All rows below were opened (`full`) unless marked `search-only`; the three search-only rows at the end are carried from the landscape file and used only in the metrics list. One ref per document; refs follow `PUBLISHER-SHORT-YYYY` and reuse the landscape file's ref where the document is the same (COSO-GENAI-2026, AICPA-PA-2026, JOFA-AIPA-2026, AT-AICPAPA-2026, KPMGUK-GOVAI-2026, KPMGUK-CONTROLS-2026, KPMGNL-AI-2025, ACCA-EY-2025, IAASB-TECH-2026, BDO-ITGC-2026, FRC-GENAI-2026).

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| COSO-GENAI-2026 | Achieving Effective Internal Control Over Generative AI (32-page publication) | COSO | standard-setter | https://www.coso.org/_files/ugd/719ba0_ef4dbc255331406e95faf46e7a9e3a1c.pdf | 2026-02-23 | full |
| COSO-PRESS-2026 | COSO release page and press release: Practical Roadmap for Managing Generative AI Risks and Controls | COSO | standard-setter | https://www.coso.org/generative-ai | 2026-02-23 | full |
| DART-COSO-2026 | Heads Up: COSO Releases Publication on Internal Controls Related to Generative AI (Vol. 33, Issue 3) | Deloitte (DART) | firm | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai | 2026-04-03 | full |
| JOFA-COSO-2026 | COSO creates audit-ready guidance for governing generative AI | Journal of Accountancy (AICPA) | press | https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ | 2026-02-26 | full |
| IIA-COSO-2026 | COSO Issues GenAI Guidance | Internal Auditor (The IIA) | professional-body | https://internalauditor.theiia.org/en/articles/2026/march/coso-issues-genai-guidance/ | 2026-03-11 | full |
| AICPA-PA-2026 | AICPA Releases Guidance to Help Auditors Address the Use of AI in Financial Reporting and Auditing (news release on the practice aid Artificial Intelligence (AI) Considerations for Financial Statement Auditors) | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy (AICPA) | press | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 | full |
| AT-AICPAPA-2026 | AICPA releases practice guide for auditors dealing with AI (12-minute read quoting the practice aid at length) | Accounting Today | press | https://www.accountingtoday.com/news/aicpa-releases-practice-guide-for-auditors-dealing-with-ai | 2026-10-14 | full |
| CFODIVE-AICPAPA-2026 | AICPA issues guidance for AI-assisted auditing | CFO Dive | press | https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/ | 2026-10-13 | full |
| DSIT-ASSURANCE-2025 | Trusted third-party AI assurance roadmap | UK Department for Science, Innovation and Technology (GOV.UK) | regulator | https://www.gov.uk/government/publications/trusted-third-party-ai-assurance-roadmap/trusted-third-party-ai-assurance-roadmap | 2025-09-03 | full |
| TECHUK-ASSURANCE-2026 | One year on: the Trusted Third-Party AI Assurance Roadmap (summit page) | techUK | conference | https://www.techuk.org/events/one-year-on-the-trusted-third-party-ai-assurance-roadmap | 2026-09-28 | full |
| EVS-42006-2025 | New international standard sets rules for auditing AI management systems (news item on ISO/IEC 42006) | EVS (Estonian Centre for Standardisation and Accreditation), crediting IEC | standard-setter | https://www.evs.ee/en/auditing-ai-management-systems | 2025-08-05 | full |
| KPMGUK-GOVAI-2026 | Independent confidence in how you govern AI (AI Governance Assurance) | KPMG UK | firm | https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html | 2026-09-22 | full |
| KPMGUK-CONTROLS-2026 | Reimagining Controls Assurance with AI: Latest Insights for Leaders | KPMG UK | firm | https://assets.kpmg.com/content/dam/kpmgsites/uk/pdf/2026/01/reimagining-controls-assurance-with-ai.pdf.coredownload.inline.pdf | 2026-01 | full |
| KPMGNL-AI-2025 | KPMG Nederland voegt AI Assurance toe aan haar Responsible AI-aanbod (press release, Dutch) | KPMG Nederland | firm | https://kpmg.com/nl/nl/home/media/press-releases/2025/09/kpmg-start-met-onafhankelijke-controles-van-ai-systemen.html | 2025-09-23 | full |
| IIA-AIFRAMEWORK-2024 | The IIA's Artificial Intelligence Auditing Framework (public page and Portuguese-language PDF edition, updated Sep 2024) | The IIA | professional-body | https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/ | 2024-09-13 | full |
| EC-AISTANDARDS-2025 | Standardisation of the AI Act | European Commission (Shaping Europe's digital future) | regulator | https://digital-strategy.ec.europa.eu/en/policies/ai-act-standardisation | 2025-10 | full |
| DQS-OMNIBUS-2026 | EU AI Act: Parliament and Council Align on Postponing High-Risk AI Obligations | DQS Global (blog) | vendor | https://www.dqsglobal.com/en/about/newsroom/eu-ai-act-parliament-and-council-align-on-postponing-high-risk-ai-obligations | 2026-04-27 | full |
| HL-OMNIBUS-2026 | EU legislators agree to delay for high-risk AI rules | Hogan Lovells (via JD Supra) | press | https://www.jdsupra.com/legalnews/eu-legislators-agree-to-delay-for-high-5617765/ | 2026-05-08 | full |
| AG-OMNIBUS-2026 | EU AI Act: AI Omnibus formally adopted | Addleshaw Goddard | press | https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/ | 2026-07-01 | full |
| SIG-AIACT-2026 | A comprehensive EU AI Act Summary [August 2026 update] | Software Improvement Group | vendor | https://www.softwareimprovementgroup.com/eu-ai-act-summary/ | 2026-08-14 | full |
| EU-AIACT-ART43-2024 | Article 43: Conformity Assessment, Regulation (EU) 2024/1689 (third-party reproduction of the Act's text) | artificialintelligenceact.eu (text of the Regulation published in the EU Official Journal) | regulator | https://artificialintelligenceact.eu/article/43/ | 2024-07-12 | full |
| CALCPA-AIREG-2026 | AI Standard Setting, Regulation in Audit: Part 1 | California Society of CPAs (CalCPA) | professional-body | https://www.calcpa.org/whats-happening/articles/ai-standard-setting-regulation-in-audit-part-1 | 2026-08-12 | full |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance: Risks, mitigations and illustrative examples (60 pages) | Financial Reporting Council | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 | full |
| FRC-GENAINEWS-2026 | Innovative new guidance supports audit firm adoption of emerging AI technologies | Financial Reporting Council | regulator | https://www.frc.org.uk/news-and-events/news/2026/03/innovative-new-guidance-supports-audit-firm-adoption-of-emerging-ai-technologies/ | 2026-03-30 | full |
| BDO-ITGC-2026 | Artificial Intelligence: IT Audit Considerations with Focus on Information Technology General Controls (web article and PDF) | BDO USA | firm | https://www.bdo.com/insights/assurance/artificial-intelligence-it-audit-considerations-with-focus-on-information-technology-general-control | 2026-07-20 | full |
| UNIQUS-GENAI-2026 | Internal Controls Over Generative AI: A Uniqus Point of View for Boards, Audit Committees and the C-Suite | Uniqus Consultech | vendor | https://uniqus.com/wp-content/uploads/2026/04/Internal-Controls-Over-Generative-AI.pdf | 2026-04 | full |
| MOKANDER-BLUEPRINT-2024 | A Blueprint for Auditing Generative AI (arXiv 2407.05338) | Mokander, Curl and Kshirsagar (arXiv) | academic | https://arxiv.org/abs/2407.05338 | 2024-07-07 | full |
| MOKANDER-LLM-2023 | Auditing large language models: a three-layered approach (arXiv 2302.08500) | Mokander, Schuett, Kirk and Floridi (arXiv) | academic | https://arxiv.org/abs/2302.08500 | 2023-02-16 | full |
| NIAN-AUDITABLE-2026 | Auditable Agents (arXiv 2604.05485, v4) | Nian et al. (arXiv; condensed version accepted to ACM AI Summit 2026) | academic | https://arxiv.org/abs/2604.05485 | 2026-04-07 | full |
| RAJI-2020 | Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing (arXiv 2001.00973) | Raji et al. (arXiv) | academic | https://arxiv.org/abs/2001.00973 | 2020-01-03 | full |
| BIRHANE-2024 | AI auditing: The Broken Bus on the Road to AI Accountability (arXiv 2401.14462) | Birhane, Steed, Ojewale, Vecchione and Raji (arXiv; IEEE SaTML 2024) | academic | https://arxiv.org/abs/2401.14462 | 2024-01-25 | full |
| OJEWALE-2024 | Towards AI Accountability Infrastructure: Gaps and Opportunities in AI Audit Tooling (arXiv 2402.17861, v3) | Ojewale et al. (arXiv) | academic | https://arxiv.org/abs/2402.17861 | 2024-02-27 | full |
| NIST-AIRMF-2023 | AI Risk Management Framework (program page: AI RMF 1.0, Generative AI Profile, revision notice) | NIST | regulator | https://www.nist.gov/itl/ai-risk-management-framework | 2023-01-26 | full |
| IAASB-TECH-2026 | Technology and the Future of Audit and Assurance (focus-area page) | IAASB | standard-setter | https://www.iaasb.org/focus-areas/technology | 2026-07 | full |
| IAASB-CATALOG-2026 | Technology Catalog of Issues and Possible Actions, Version 3 (28-page PDF) | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-07/IAASB-Technology-Catalog-of-Issues-Proposed-Actions.pdf | 2026-07-09 | full |
| BSI-ANAB-2026 | BSI secures ANAB accreditation to certify ISO/IEC 42001 | BSI | vendor | https://www.bsigroup.com/en-AU/insights-and-media/media-centre/press-releases/2026/march/bsi-secures-anab-accreditation-to-certify-isoiec-42001/ | 2026-03-10 | full |
| BSI-UMONY-2026 | Umony achieves ISO/IEC 42001 certification for responsible AI (case study) | BSI | vendor | https://www.bsigroup.com/en-GB/insights-and-media/insights/case-studies/umony-achieves-isoiec-42001-certification-for-responsible-ai/ | 2026 | full |
| BSI-ACCELLEO-2026 | Accelleo builds trusted defence AI with ISO/IEC 42001 (case study) | BSI | vendor | https://www.bsigroup.com/en-GB/insights-and-media/insights/case-studies/accelleo-builds-trusted-defence-ai-with-iso-iec-42001/ | 2026 | full |
| CSA-AIASSURE-2026 | Who Assures the Assurers? Third-Party AI Assessment Standards (research note) | Cloud Security Alliance, AI Safety Initiative | professional-body | https://labs.cloudsecurityalliance.org/research/csa-research-note-third-party-ai-assurance-standards-2026092/ | 2026-09-27 | full |
| SCHELLMAN-AIUC1-2026 | Schellman Becomes the First Accredited Auditor for AIUC-1, the Security Standard for AI Agents | Schellman | firm | https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1 | 2026-02-03 | full |
| CSA-STAR-AIUC1-2026 | Cloud Security Alliance Extends AI Assurance Leadership Into Agentic AI With Addition of AIUC-1 Certification to STAR Registry | Cloud Security Alliance | professional-body | https://cloudsecurityalliance.org/press-releases/2026/06/30/csa-extends-leadership-into-agentic-ai-with-addition-of-aiuc-1-certification-to-star-registry | 2026-06-30 | full |
| CPAPA-ACCAEY-2025 | EY and ACCA Share New Guidance on AI Assessments to Boost Confidence in AI Systems | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=166602 | 2025-08-04 | full |
| CFOTECH-ACCAEY-2025 | EY & ACCA urge trustworthy AI with robust assessment frameworks | CFOtech UK | press | https://cfotech.co.uk/story/ey-acca-urge-trustworthy-ai-with-robust-assessment-frameworks | 2025-08-05 | full |
| SFN-ACCAEY-2025 | ACCA and EY share new guidance to help businesses boost confidence in AI | Scottish Financial News | press | https://www.scottishfinancialnews.com/articles/acca-and-ey-share-new-guidance-to-help-businesses-boost-confidence-in-ai | 2025-08-05 | full |
| ACCA-EY-2025 | AI Assessments: Enhancing Confidence in AI (policy paper; not opened, DNS failure on accaglobal.com; carried from landscape and press copies) | ACCA and EY | professional-body | https://www.accaglobal.com/policy-and-insights/reports/2025/ai-enhancing-confidence | 2025-08 | search-only |
| CAQ-PULSE-2026 | CAQ Audit Partner Pulse, Spring 2026 (carried from landscape-assurance.md, which read it via a secondary article; not opened this run) | Center for Audit Quality | professional-body | URL not recorded in the landscape file | 2026-07-15 | search-only |
| ISACA-PULSE-2026 | ISACA AI Pulse Poll 2026 (carried from landscape-assurance.md; not opened this run) | ISACA | survey | URL not recorded in the landscape file | 2026 | search-only |
| IFIAR-TTF-2025 | Use of technology in audits: observations, risks and further evolution (carried from landscape-assurance.md; not opened this run) | IFIAR | regulator | URL not recorded in the landscape file | 2025-03-27 | search-only |

**Source count by type (all rows):** academic 6, conference 1, firm 6, press 9, professional-body 8, regulator 7, standard-setter 5, survey 1, vendor 6. Opened (`full`): 45; search-only: 4.

**Date notes.** BSI-UMONY-2026 and BSI-ACCELLEO-2026 carry no publication date on the page, so the year is the retrieval year; EC-AISTANDARDS-2025 is dated to the latest item it mentions (30 Oct 2025); IAASB-TECH-2026 is dated to the catalog edition it describes; KPMGNL-AI-2025 uses the 23-09-2025 event date shown in the text, not the page metadata (2026-10-13); EU-AIACT-ART43-2024 uses the Official Journal publication date of Regulation (EU) 2024/1689 (12 Jul 2024) from general knowledge, since the reproduction page is undated and this was not confirmed on it. Pages were also opened but not cited in the use cases: the ISACA AAIA page (undated) and BSI's ISO/IEC 42001 product page (undated).

---

## 6. Gaps

- **PCAOB and SEC statements.** The PCAOB's own pages (standard-setting projects, staff spotlight, release pages) returned 403 or 404. SEC Office of the Chief Accountant remarks were not re-opened. The only PCAOB view in this file comes from a state CPA society article (CALCPA-AIREG-2026), including an unverified claim of AI-related inspection deficiencies in journal-entry testing that the landscape did not find in any primary source.
- **Web search ran out** before searches on SEC statements, NIST revision details, further academic work on auditability of AI, and national standard-setter work (AUASB, IDW, NBA, CPA Canada, ICAEW) on AI assurance. No national standard-setter statement on AI assurance engagements was found.
- **AICPA practice aid and IIA English framework full text** are behind member logins; the practice aid is read through Accounting Today, the AICPA release, the Journal of Accountancy and CFO Dive. TQA 9561 was not reachable.
- **ISO texts.** ISO/IEC 42001 and 42006 pages on iso.org returned 403; ISO/IEC 42006's content comes from a standards body news item (EVS-42006-2025) and a certifier's release. The publication date of ISO/IEC 42006 is given only as 2025 here (EVS item dated 5 Aug 2025).
- **The ACCA/EY paper** could not be opened (DNS failure); three press copies were read.
- **IIA AI Auditing Framework**: only the Portuguese PDF edition of the Sep 2024 update was readable; the English text is member-only.
- **EU AI Act**: the Official Journal text of the Omnibus was not opened; sources differ on approval dates (SIG: Parliament 16 Jun, Council 29 Jun, signed 8 Jul, published 24 Jul, in force 27 Jul 2026; AG: formal adoption reported 1 Jul 2026). Only paragraphs 1 and 2 of Article 43 were checked. Designation counts differ (8 of 27 member states with fully designated competent authorities, DQS; three with both notifying and market-surveillance authorities, CSA citing a compliance vendor).
- **COSO text discrepancy.** The COSO PDF read here lists the eighth capability type as "knowledge retrieval" in its executive summary, while COSO's release page and the AICPA's press coverage name "regulatory intelligence"; the PDF file metadata shows a later creation date (1 Sep 2026) than the 23 Feb 2026 release, so a revised version may be posted. Use the PDF's wording when quoting the taxonomy.
- **BDO versus COSO on reliance.** BDO's paraphrase of COSO's reliance definition differs from the wording on COSO's p. 13 (BDO-ITGC-2026; COSO-GENAI-2026).
- **No outcomes with real measurement.** No error rates, override rates, parallel-run results or inspection findings were found for AI controls testing or for AI assurance engagements. COSO's case examples are illustrative and unnamed. KPMG's and BSI's service descriptions give no client results beyond qualitative claims.
- **No issued AI assurance reports** (ISAE (UK) 3000, SOC 2+, AIUC-1) or named client for the KPMG services were found. ElevenLabs's AIUC-1 certification was mentioned only in the CSA note via a trade press report not opened.
- **CSA note reliability.** The landscape says the note was generated with AI assistance and not CSA-reviewed; that disclaimer was not found in the page text this run. Its claims are used only with attribution and are not placed in outcomes.
- **Source types not found:** community discussions, job postings, podcasts and conference proceedings specific to this module (the techUK summit page is an agenda description, not proceedings).
- **Practitioner voices** on AI-enabled control testing are almost entirely firm publications; no practitioner survey of audits of entity AI was found.

