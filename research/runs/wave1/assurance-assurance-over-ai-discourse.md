# Module deep dive: assurance / assurance-over-ai / discourse

- **Archetype:** assurance
- **Module:** assurance-over-ai. Two linked areas: (1) auditing AI the entity uses in financial reporting and internal control (AI-enabled controls, models and agents as in-scope systems; ITGCs over AI; COSO and AICPA guidance); (2) standalone assurance services over AI systems (AI governance and AI management system assurance, ISO/IEC 42001 certification and ISO/IEC 42006, ISAE 3000 AI assurance, algorithmic audits, AI audit taxonomies).
- **Angle:** discourse. What practitioners, CAEs, audit committees and commentators are saying in the last 12-18 months.
- **Prepared:** 2026-10-16
- **Method note.** About 60 pages, PDFs and show-note pages were opened with `curl` (and `pdftotext`) and read. Podcasts and conference sessions were read through show notes, programmes and written recaps only; no audio, video or transcripts were reached. The web-search quota ran out partway through (see Gaps), so some planned searches (ITGC over AI, ISACA AAIA, EU AI Act conformity-body capacity) were not run. Older items (2022 to Feb 2025) are used only as foundations and are flagged. Source refs follow `PUBLISHER-SHORT-YYYY` and reuse the landscape's keys where the document is the same. Every figure is attributed to its source; most are self-reported or vendor-published.

---

## 1. Summary

1. **Two conversations about "auditing AI" run side by side and rarely meet.**
   - *Conversation A: AI inside the entity's financial reporting and ICFR.* It is led by Big Four and mid-tier firms, COSO, the AICPA, the IIA and SOX-tech vendors. The message is that AI in the close is an in-scope system. Guidance is plentiful: COSO's generative-AI publication (23 Feb 2026, DART-COSOHU-2026) and the AICPA's first practice aid on AI for financial statement auditors (13 Oct 2026, JOFA-AIPA-2026). Public evidence of practice is thin. KPMG says SOX programs are still testing "around" AI and expects the first wave of AI-related material weaknesses in 2027 (KPMG-SOX-2026, p.7). That is a forecast. I found no disclosed material weakness attributed to AI (see Gaps).
   - *Conversation B: standalone assurance over AI systems.* It is led by certifiers (BSI, Schellman), the UK government and ICAEW, the Big Four and a few specialists. It is a market being built: ISO/IEC 42001 certification with accredited certifiers, AIUC-1 agent certification, CSA STAR for AI, and KPMG UK's ISAE (UK) 3000 opinion on AI governance. The open arguments are about criteria (no AI-specific standard in the US; ISO 42001 certifies a management system, not an individual AI system), independence (many providers are the AI developers themselves) and vocabulary ("audit", "assurance" and "evaluation" are used interchangeably, and "assurance" is a regulated term in some places).
2. **Readiness is the common worry, and audit partners and CAEs say it themselves.**
   - Only 6% of audit partners rate AI governance at their largest client as advanced (BOARDMEMBER-CAQ-2026).
   - In the Deloitte/CAQ audit committee survey, 75% of respondents named AI governance a top-three priority (35% the year before) and only 56% were confident in the committee's ability to oversee it (DELOITTE-ACPR-2026).
   - In an Optro/Panterra survey of internal audit leaders, 28% were confident in their teams' ability to audit AI risks (OPTRO-FOF-2025).
3. **Demand pull is real but uneven, and the regulatory push has slipped.**
   - Procurement, investors and insurers are described as asking for AI assurance (TECHUK-ROADMAP-2026; KPMGUK-GOVAI-2026).
   - The EU Digital Omnibus provisional agreement defers high-risk obligations to 2 Dec 2027 (stand-alone Annex III systems) and 2 Aug 2028 (Annex I products), pending formal adoption at the time of the source (GIBSON-OMNIBUS-2026).
   - The SEC's 19 May 2026 filer-status proposal would, if finalised, move roughly half of currently attested issuers out of SOX 404(b) auditor attestation (UNIQUS-FILER-2026). That shrinks one of the markets for auditing AI-enabled ICFR controls. I found no source that links the proposal to AI.
4. **There is no independent quality evidence.** No error rate, override rate, parallel-run result or inspection finding for assurance over AI was found. The one inspection-finding claim I saw (AI-related deficiencies in journal-entry testing, CALCPA-AI-2026) is unattributed and not corroborated by the landscape, so it is not used as evidence. The numbers in this file are surveys of readiness or practice, vendor claims, or market-size estimates.

---

## 2. Use cases

Notes on fields. In this module the AI is usually the *object* of assurance, not the tool doing the assurance work. `ladder` and `runtime_class` therefore describe the assurance team's own tooling and are set to defaults (`assist`, `personal-assistant`) unless the source describes AI doing the monitoring. Flagged for synthesis. `pattern: other` is used where no pattern fits; the pattern is described in `notes`.

```yaml
- id: assurance-assurance-over-ai-01
  title: AI-system inventory as the scoping step for ICFR and audit planning
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    SOX teams and auditors cannot scope controls over AI until they know where AI touches financial reporting.
    Audit partners most often name lack of in-house AI expertise and control capability (33%), data quality
    (27%), missing governance frameworks and oversight structures (27%) and thin documentation of models,
    assumptions and decision logic (26%) as the main AI-related internal-control challenges at their largest
    client [BOARDMEMBER-CAQ-2026]. Unsanctioned "shadow AI" sits outside formal IT governance [UNIQUS-GENAI-2026].
  solution: >
    Start with a living inventory of AI use cases, with owners and escalation paths, and use it to scope risk
    assessment and testing. Deloitte describes COSO's six-step roadmap (govern, inventory, assess, design,
    implement, monitor) as a tool management, boards, risk functions and external auditors can use to
    understand how AI has been implemented [DART-COSOHU-2026]. EY leaders advise organisations just starting
    out to begin with governance and an AI inventory [EY-SOC-2026]. A summary of a Genpact CAE forum lists a
    complete inventory of material AI systems with assigned accountability as a first action [GENPACT-CAE-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: DART-COSOHU-2026
  prerequisites:
    - Cross-functional governance with named owners for each AI capability [DART-COSOHU-2026]
    - A way to detect shadow AI, such as acceptable-use policy and discovery [UNIQUS-GENAI-2026]
  risks_and_guardrails:
    - COSO-aligned commentary stresses ongoing inventories, because AI use cases change quickly and are adopted outside formal channels [DART-COSOHU-2026].
  human_checkpoints:
    - Control owner and IT sign-off on what is in or out of scope [DART-COSOHU-2026]
  role_evolution: >
    EY's AI assurance leaders position the inventory as the first thing an organisation should build
    before it seeks assurance [EY-SOC-2026].
  evidence_grade: D
  sources:
    - {ref: DART-COSOHU-2026, title: "Heads Up: COSO releases publication on internal controls related to generative AI", publisher: Deloitte DART, type: firm, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai", date: 2026-04-03, access: full, locator: "paragraphs 1-3 (roadmap, inventory, shadow AI)"}
    - {ref: BOARDMEMBER-CAQ-2026, title: "What audit partners are seeing on AI and what it means for audit committees", publisher: Corporate Board Member (CAQ author), type: press, url: "https://boardmember.com/?p=50023", date: 2026-07-15, access: full, locator: "section on operational control gaps"}
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "section 'How AI improves SOC reporting', closing quote"}
    - {ref: GENPACT-CAE-2026, title: "Evolving AI governance demands new oversight and audit strategies", publisher: welcome.ai (summary of Genpact CAE Forum, 2026-03-26), type: press, url: "https://www.welcome.ai/content/evolving-ai-governance-demands-new-oversight-and-audit-strategies", date: 2026-09-11, access: full, locator: "paragraph on actions for CAEs"}
    - {ref: UNIQUS-GENAI-2026, title: "Internal controls over generative AI", publisher: Uniqus, type: firm, url: "https://uniqus.com/internal-controls-over-generative-ai/", date: 2026-04-07, access: full, locator: "section 1 (shadow AI)"}
  last_reviewed: 2026-10-16
  notes: >
    Idea, as practitioners discuss it; no named organisation reports having run it or measured it. The Genpact
    source is an AI-generated aggregator summary of a forum, so low authority. The COSO capability list differs
    between sources: IIA lists eight types including "regulatory intelligence" [IIA-COSO-2026]; EisnerAmper lists
    eight including "knowledge retrieval and summarization" [EISNER-COSO-2026]. The COSO document itself was not opened.

- id: assurance-assurance-over-ai-02
  title: Classifying AI-touched controls by the AI's role to set ITGC and test scope
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    When a control uses AI, the type of control and the scope of IT general control testing are unclear. Vendor
    commentary says over-scoping and presenting a monitoring activity as a key control are both likely errors
    [FINREP-JE-2026].
  solution: >
    A finance-technology vendor, citing PwC's 2025 guidance (not opened here), describes three classes: AI makes
    and executes the decision (ITGC testing of the AI system itself comes into scope); AI flags and a human reviews
    and decides (an IT-dependent manual control, where human sign-off is the primary operating evidence); and AI
    supplements a key control without replacing it [FINREP-JE-2026]. Another vendor lists twelve questions it says
    external auditors ask about AI-touched controls, ending with whether the AI behaves like a control or like a
    tool [KOGNITOS-SOXQ-2026].
  outcomes:
    - lever: quality
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: FINREP-JE-2026
  prerequisites:
    - A control matrix that records, for each control, what the AI does and what the human does [FINREP-JE-2026]
  risks_and_guardrails:
    - Both sources are vendors with a product to sell; the PwC original and the auditors' actual questions were not seen [FINREP-JE-2026] [KOGNITOS-SOXQ-2026].
  human_checkpoints:
    - Human reviewer disposition of AI flags, evidenced by sign-off and reviewer identity [FINREP-JE-2026]
  role_evolution: >
    The sources do not discuss role change; they say controllers and SOX leads need to explain AI controls in
    auditor-ready terms [KOGNITOS-SOXQ-2026].
  evidence_grade: C
  sources:
    - {ref: FINREP-JE-2026, title: "AI journal entry testing and SOX 404 controls: a 2026 practitioner walkthrough", publisher: Finrep, type: vendor, url: "https://www.finrep.ai/blog/ai-journal-entry-testing-and-sox-404-controls-a-2026-practitioner-walkthrough", date: 2026-08-03, access: full, locator: "section 'How to classify an AI journal entry control in your control matrix'"}
    - {ref: KOGNITOS-SOXQ-2026, title: "What your SOX auditor will ask about your AI automation", publisher: Kognitos, type: vendor, url: "https://www.kognitos.com/blog/sox-auditor-questions-ai-automation/", date: 2026-05-15, access: full, locator: "TL;DR and section 'The 12 questions'"}
  last_reviewed: 2026-10-16
  notes: >
    Vendor claims. The Kognitos post says the PCAOB's amended AS 2201 and AS 2101 take effect for fiscal years
    beginning on or after 2026-12-15 and that Big Four firms now train staff to scrutinise AI-touched controls; neither
    is confirmed by the landscape (which lists QC 1000 with that date) and neither is used as a finding here.

- id: assurance-assurance-over-ai-03
  title: Extending ITGCs and access controls to AI components and agents
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    GenAI can let a user retrieve information they could not reach directly and lets one system configure rules,
    execute transactions and generate review reports, which strains access and segregation-of-duties controls
    [UNIQUS-GENAI-2026]. In an Optro survey of over 400 GRC and audit leaders, respondents said they authorise agents
    to approve or reject transactions (38%), modify controls or policies (34%) and change user permissions or
    access rights (27%) [OPTRO-AGENTIC-2026].
  solution: >
    Treat prompts, system prompts, retrieval connectors and transformation rules as governed configurations with
    version history, approval workflows and rollback [AT-COSO-2026]. Apply least privilege, logging and human
    override to autonomous agents, manage API keys and tokens like privileged credentials, and re-examine
    segregation of duties where AI can configure, execute and review [UNIQUS-GENAI-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: UNIQUS-GENAI-2026
  prerequisites:
    - An AI inventory and an agent identity and permission register [UNIQUS-GENAI-2026]
  risks_and_guardrails:
    - In the same Optro survey, 25% reported a control failure involving an agent and 30% an unintended agent action [OPTRO-AGENTIC-2026]. Vendor-published; sample of over 400 respondents; the figures say how many reported these events, not how severe.
  human_checkpoints:
    - Human override capability on agent actions [UNIQUS-GENAI-2026]
  role_evolution: >
    KPMG says the auditor of the future must be as comfortable in a system configuration log as in a transaction
    ledger [KPMG-SOX-2026].
  evidence_grade: C
  sources:
    - {ref: UNIQUS-GENAI-2026, title: "Internal controls over generative AI", publisher: Uniqus, type: firm, url: "https://uniqus.com/internal-controls-over-generative-ai/", date: 2026-04-07, access: full, locator: "sections on access controls and segregation of duties"}
    - {ref: AT-COSO-2026, title: "COSO releases guidance on internal controls for AI", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/coso-releases-guidance-on-applying-internal-controls-to-ai", date: 2026-02-24, access: full, locator: "paragraph on control environment"}
    - {ref: OPTRO-AGENTIC-2026, title: "One in three organizations say they have acted on wrong decisions made by AI agents", publisher: Optro, type: vendor, url: "https://optro.ai/blog/one-in-three-organizations-say-they-have-acted-on-wrong-decisions-made-by-ai-agents-optro-research-finds", date: 2026-10-08, access: full, locator: "paragraphs 2-4"}
    - {ref: KPMG-SOX-2026, title: "The Future of SOX: a point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24, access: full, locator: "POV 2, 'self-healing controls' (p.8)"}
  last_reviewed: 2026-10-16
  notes: >
    Uniqus is an advisory firm point of view, not a deployment report. It also says the PCAOB signalled attention to
    ITGCs over AI in "2026 inspection priorities"; that statement was not confirmed from a PCAOB source and is not used
    as a finding. The landscape cites a BDO paper on ITGCs over AI (BDO-ITGC-2026); it was not re-opened here.

- id: assurance-assurance-over-ai-04
  title: Continuous monitoring of AI-operated controls (volumes, override rates, drift) instead of point-in-time testing
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >
    Generative AI outputs vary, so a test of one sample at one date says little about how the control behaves next
    month. Deloitte says "set-and-forget" does not work when GenAI is used in financial reporting [DART-COSOHU-2026].
  solution: >
    Monitor key indicators such as transaction volume, transaction size and override percentages to detect model
    drift, evaluate accuracy and reliability, and look for root causes such as prompt design, retrieval issues and
    vendor changes [DART-COSOHU-2026]. COSO's guidance, as summarised, asks for risk assessment, change control and
    monitoring that are continuous or moving toward continuous [AT-COSO-2026].
  outcomes:
    - lever: quality
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: DART-COSOHU-2026
  prerequisites:
    - Baselines for the chosen indicators and an owner for each [DART-COSOHU-2026]
    - Living risk registers that update when models, corpora or configurations change [AT-COSO-2026]
  risks_and_guardrails:
    - Deloitte says the COSO guidance is best treated as building on the 2013 framework, not as a prescriptive rulebook [DART-COSOHU-2026].
  human_checkpoints:
    - Review of drift alerts and root-cause assessment by the control owner [DART-COSOHU-2026]
  role_evolution: >
    Deloitte says GenAI requires a shift in mindset for management and auditors, from static point-in-time
    assurance to continuous monitoring of model performance and risk [DART-COSOHU-2026].
  evidence_grade: D
  sources:
    - {ref: DART-COSOHU-2026, title: "Heads Up: COSO releases publication on internal controls related to generative AI", publisher: Deloitte DART, type: firm, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai", date: 2026-04-03, access: full, locator: "paragraph 3 (monitoring indicators)"}
    - {ref: AT-COSO-2026, title: "COSO releases guidance on internal controls for AI", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/coso-releases-guidance-on-applying-internal-controls-to-ai", date: 2026-02-24, access: full, locator: "paragraphs on risk assessment and the five foundational principles"}
  last_reviewed: 2026-10-16
  notes: >
    Idea: described as guidance; no named organisation reports measured results.

- id: assurance-assurance-over-ai-05
  title: Treating AI output as a claim to validate, with an evidence package for each AI-touched control
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Because GenAI is probabilistic, a control that relies on its output cannot be evidenced by the output alone.
    COSO's guidance, as summarised, says outputs should be treated as claims requiring validation rather than facts
    to accept by default [AT-COSO-2026]; EisnerAmper says outputs should be treated as assertions requiring validation [EISNER-COSO-2026].
  solution: >
    Retain prompts, system prompts and configurations with version history [AT-COSO-2026]. Advisers add that
    inputs, outputs, model versions and human-review records should be kept so the control can be shown to have
    operated [UNIQUS-GENAI-2026] [KOGNITOS-SOXQ-2026]. Another vendor adds a crosswalk table in the control matrix that
    maps each AI detection rule to the audit risk factor it addresses (for journal entries, AS 2401) [FINREP-JE-2026].
  outcomes:
    - lever: quality
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: AT-COSO-2026
  prerequisites:
    - Logging and retention of prompts, outputs and reviewer decisions [KOGNITOS-SOXQ-2026]
  risks_and_guardrails:
    - COSO, as summarised, names data extraction and ingestion as a high-risk capability because weak controls there pass compromised data to every downstream process [AT-COSO-2026].
  human_checkpoints:
    - A named reviewer who documents what the AI concluded and why they agreed or disagreed [BAKERTILLY-IA-2026]
  role_evolution: >
    Baker Tilly says finding accuracy and coverage, not efficiency, become the indicators of a reliable audit
    function, because boards ask who made the call when AI is involved [BAKERTILLY-IA-2026].
  evidence_grade: C
  sources:
    - {ref: AT-COSO-2026, title: "COSO releases guidance on internal controls for AI", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/coso-releases-guidance-on-applying-internal-controls-to-ai", date: 2026-02-24, access: full, locator: "five foundational principles; control environment paragraph"}
    - {ref: EISNER-COSO-2026, title: "COSO released GenAI governance guidance: what it means for your organization", publisher: EisnerAmper, type: firm, url: "https://www.eisneramper.com/insights/artificial-intelligence-insights/coso-ai-governance-internal-control-framework-0526/", date: 2026-05-13, access: full, locator: "Key takeaways"}
    - {ref: UNIQUS-GENAI-2026, title: "Internal controls over generative AI", publisher: Uniqus, type: firm, url: "https://uniqus.com/internal-controls-over-generative-ai/", date: 2026-04-07, access: full, locator: "section 1"}
    - {ref: KOGNITOS-SOXQ-2026, title: "What your SOX auditor will ask about your AI automation", publisher: Kognitos, type: vendor, url: "https://www.kognitos.com/blog/sox-auditor-questions-ai-automation/", date: 2026-05-15, access: full, locator: "questions 3, 4 and 8"}
    - {ref: FINREP-JE-2026, title: "AI journal entry testing and SOX 404 controls: a 2026 practitioner walkthrough", publisher: Finrep, type: vendor, url: "https://www.finrep.ai/blog/ai-journal-entry-testing-and-sox-404-controls-a-2026-practitioner-walkthrough", date: 2026-08-03, access: full, locator: "section 'What PCAOB AS 2401 actually requires'"}
    - {ref: BAKERTILLY-IA-2026, title: "Strategy in motion: internal audit's 2026 execution mandate", publisher: Baker Tilly, type: firm, url: "https://www.bakertilly.com/insights/internal-audit-2026-execution-mandate", date: 2026-04-10, access: full, locator: "section 3"}
  last_reviewed: 2026-10-16
  notes: >
    The Baker Tilly article also says the EU AI Act (2026) "explicitly classifies audit AI as high risk". I could not
    confirm that; Gibson Dunn's description of Annex III lists recruitment, credit scoring, law enforcement, education
    and border control "among others" and does not mention audit [GIBSON-OMNIBUS-2026]. Not used.

- id: assurance-assurance-over-ai-06
  title: Moving from testing around AI to relying on AI-operated controls, with test of design first
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    KPMG says SOX programs have not yet fully started relying on AI-operated controls and are still testing
    "around" the AI, using manual and other automated controls [KPMG-SOX-2026]. That is expected to change.
  solution: >
    KPMG expects it to become unavoidable to work AI considerations into the control environment, "likely during this next year",
    and expects the first wave of AI-related material weaknesses in 2027; it gives an illustrative failure: an AI system in a delegation-of-authority
    workflow approves outside policy thresholds repeatedly [KPMG-SOX-2026]. In a separate paper, KPMG says external
    auditors are placing greater emphasis on test of design as organisations adopt automated controls, AI-enabled
    processes and continuous monitoring [KPMG-404A-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: KPMG-SOX-2026
  prerequisites:
    - Controls designed to be testable: documented logic, explainability, evidence of operation [KPMG-404A-2026]
  risks_and_guardrails:
    - KPMG's forecast of material weaknesses is a firm prediction, not an observed event. Its own wording is that the industry has largely avoided AI-related material weaknesses to date [KPMG-SOX-2026].
  human_checkpoints:
    - Deficiency evaluation, including probing management's explanation for "why it's not a material weakness" [KPMG-ACAGENDA-2025]
  role_evolution: >
    KPMG describes a new mandate for auditors to provide assurance over the AI systems themselves, extending the
    ICFR perimeter to the models that generate, transform and validate financial data [KPMG-SOX-2026].
  evidence_grade: C
  sources:
    - {ref: KPMG-SOX-2026, title: "The Future of SOX: a point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24, access: full, locator: "p.6 ('Auditing AI itself') and p.7 ('The first AI-related material weaknesses')"}
    - {ref: KPMG-404A-2026, title: "The 404(a) opportunity: turning a compliance shift into a strategic catalyst", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/404-opportunity.pdf", date: 2026-08, access: full, locator: "section on renewed focus on Test of Design"}
    - {ref: KPMG-ACAGENDA-2025, title: "On the 2026 audit committee agenda", publisher: KPMG Board Leadership Center, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/boardleadership/pdf/2026/on-the-2026-audit-committee-agenda.pdf", date: 2025-12-05, access: full, locator: "p.2, section 'ICOFR and probing control deficiencies'"}
  last_reviewed: 2026-10-16
  notes: >
    The PDF has no printed date; the date is the landscape's (24 Sep 2026). A single firm's view. No other firm
    or regulator source forecasting AI-related material weaknesses was found.

- id: assurance-assurance-over-ai-07
  title: Audit committee and external auditor dialogue on AI in financial reporting and controls
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [client-interaction, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >
    Audit committees are taking on AI oversight faster than they feel able to carry it. In the Deloitte/CAQ survey of
    close to 250 audit committee chairs and members, 75% named AI governance a top-three priority (35% the year before)
    but only 56% were confident in the committee's ability to oversee it [DELOITTE-ACPR-2026].
  solution: >
    KPMG's board leadership centre tells committees to discuss with the external auditor how the audit plan
    assesses risks from the company's use of GenAI and AI agents in financial reporting and related controls, and
    how the auditor itself uses AI [KPMG-ACAGENDA-2025]. Audit partners report that two-thirds say the committee
    proactively raised the use of AI in operations or financial reporting in the past 12 months, the most frequent
    topic [BOARDMEMBER-CAQ-2026].
  outcomes:
    - lever: risk
      description: Share of audit committees with primary responsibility for AI governance
      figure: "20% to 29%"
      measures: "share of Deloitte/CAQ survey respondents (audit committee chairs and members; 248 respondents per Accounting Today) saying the audit committee has primary responsibility for AI governance, prior year to current year"
      provenance: independent
      source_ref: AT-ACPR-2026
    - lever: risk
      description: Share of committees overseeing AI governance who describe their oversight as emerging or limited
      figure: "82%"
      measures: "committees overseeing AI governance describing oversight as emerging or limited, as reported by Accounting Today from the Deloitte/CAQ survey"
      provenance: independent
      source_ref: AT-ACPR-2026
  prerequisites:
    - Committee skills: 70% of respondents named technology, including AI, as the skill that would most enhance committee effectiveness [DELOITTE-ACPR-2026]
  risks_and_guardrails:
    - The Deloitte/CAQ survey measures committees' own views; the 57% "AI governance is the biggest committee challenge" figure comes from audit partners, a different group [BOARDMEMBER-CAQ-2026].
  human_checkpoints:
    - Committee challenge of management's explanation of control deficiencies [KPMG-ACAGENDA-2025]
  role_evolution: >
    KPMG says internal audit's focus on AI governance and risk will likely grow, and asks whether internal audit
    keeps a human on the loop at critical stages of agent workflows [KPMG-ACAGENDA-2025].
  evidence_grade: B
  sources:
    - {ref: DELOITTE-ACPR-2026, title: "Audit Committee Practices Report, fifth edition (media alert)", publisher: Deloitte US with Center for Audit Quality, type: survey, url: "https://www.deloitte.com/us/en/about/press-room/deloitte-caq-announce-2026-audit-committee-practices-report.html", date: 2026-09-22, access: full, locator: "highlights: 'A gap between AI responsibility and readiness'"}
    - {ref: AT-ACPR-2026, title: "Audit committees focusing on emerging risks like AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/audit-committees-focusing-on-emerging-risks-like-ai", date: 2026-09-22, access: full, locator: "paragraph 2"}
    - {ref: KPMG-ACAGENDA-2025, title: "On the 2026 audit committee agenda", publisher: KPMG Board Leadership Center, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/boardleadership/pdf/2026/on-the-2026-audit-committee-agenda.pdf", date: 2025-12-05, access: full, locator: "pp.4-6, 'Clarify the role of the audit committee in the oversight of AI'; external auditor and internal audit sections"}
    - {ref: BOARDMEMBER-CAQ-2026, title: "What audit partners are seeing on AI and what it means for audit committees", publisher: Corporate Board Member (CAQ author), type: press, url: "https://boardmember.com/?p=50023", date: 2026-07-15, access: full, locator: "paragraphs 3-6"}
  last_reviewed: 2026-10-16
  notes: >
    Grade B: the measurements describe committee practice, not an outcome of the dialogue (adjacent evidence, so capped at B).
    Page numbers for the KPMG PDF are approximate (the text was extracted from a multi-column PDF).

- id: assurance-assurance-over-ai-08
  title: Disclosure controls over statements about the company's AI use, risks and governance
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Companies disclose how they use and govern AI, and those disclosures need controls behind them. KPMG says audit
    committees should consider tasking management with reassessing whether internal controls and disclosure controls
    support disclosures about the company's use of AI, the associated risks and its governance of the technology
    [KPMG-ACAGENDA-2025].
  solution: >
    The audit committee asks management to reassess disclosure controls and procedures for AI statements, and the
    auditor and internal audit test them [KPMG-ACAGENDA-2025]. An advisory firm adds that "AI washing" (overstating AI
    capabilities in public disclosures) has drawn SEC enforcement scrutiny [UNIQUS-GENAI-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: KPMG-ACAGENDA-2025
  prerequisites:
    - Inventory and governance evidence that can support the disclosure [KPMG-ACAGENDA-2025]
  risks_and_guardrails:
    - The SEC enforcement statement is from an advisory firm and was not confirmed from an SEC source [UNIQUS-GENAI-2026].
  human_checkpoints:
    - Audit committee review of management's reassessment [KPMG-ACAGENDA-2025]
  role_evolution: >
    SEC staff at a 2026 accountants' liability conference said consultations increasingly involve the use and
    implementation of AI in accounting tools and business relationships [JDSUPRA-ALI-2026].
  evidence_grade: C
  sources:
    - {ref: KPMG-ACAGENDA-2025, title: "On the 2026 audit committee agenda", publisher: KPMG Board Leadership Center, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/boardleadership/pdf/2026/on-the-2026-audit-committee-agenda.pdf", date: 2025-12-05, access: full, locator: "p.2, 'Climate, AI, and cybersecurity disclosures'"}
    - {ref: UNIQUS-GENAI-2026, title: "Internal controls over generative AI", publisher: Uniqus, type: firm, url: "https://uniqus.com/internal-controls-over-generative-ai/", date: 2026-04-07, access: full, locator: "section 1.1, SEC enforcement posture"}
    - {ref: JDSUPRA-ALI-2026, title: "Highlights from American Law Institute's Accountants' Liability Conference 2026", publisher: Vedder via JD Supra, type: press, url: "https://www.jdsupra.com/legalnews/highlights-from-american-law-institute-6955525/", date: 2026-05-22, access: full, locator: "SEC enforcement panel summary"}
  last_reviewed: 2026-10-16
  notes: The ALI item is about AI in accounting tools and business relationships generally; the link to AI-disclosure controls is mine, not the source's. Treat as weak support.

- id: assurance-assurance-over-ai-09
  title: Internal audit assurance over AI governance, using the IIA AI Auditing Framework
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >
    Organisations expect assurance over their AI, but internal audit is not ready. In the Optro/Panterra survey of
    internal audit leaders, 63% of surveyed organisations had not defined formal risk appetites or governance
    frameworks for AI and only 28% of respondents were confident in their teams' ability to audit AI risks
    [OPTRO-FOF-2025].
  solution: >
    The IIA's framework gives internal auditors a structure (strategy, governance, human factor; a practitioner's
    checklist) to assess AI strategy and governance maturity, identify AI-related risks, evaluate controls over data,
    algorithms and cybersecurity, and provide assurance over AI-enabled processes [IIA-AIFRAMEWORK-2024]. A Cherry
    Bekaert podcast covers what an AI audit scope should include, from training data to cybersecurity and user behaviour [CBH-POD-2025].
  outcomes:
    - lever: risk
      description: Internal audit leaders confident in their teams' ability to audit AI risks
      figure: "28%"
      measures: "respondents to the 2026 Focus on the Future survey of internal audit leaders (US, Canada, Germany, UK, EU) who are confident in their teams' ability to audit AI risks; sample size not stated on the page read"
      provenance: vendor-published
      source_ref: OPTRO-FOF-2025
  prerequisites:
    - An AI inventory and an understanding of board-level strategy alignment [IIA-AIFRAMEWORK-2024]
  risks_and_guardrails:
    - The IIA framework emphasises reasonable assurance given the complexity and evolving nature of AI [IIA-AIFRAMEWORK-2024]. It is guidance, not a mandatory standard; no AI-specific IIA Topical Requirement appears in Baker Tilly's list of those issued or planned [BAKERTILLY-IA-2026].
  human_checkpoints:
    - Named human reviewer for AI-assisted audit work [BAKERTILLY-IA-2026]
  role_evolution: >
    Richard Chambers writes that internal auditors who cannot use or understand AI will struggle to advise on its
    risks, and calls this an emerging AI credibility gap [OPTRO-FOF-2025].
  evidence_grade: C
  sources:
    - {ref: IIA-AIFRAMEWORK-2024, title: "The IIA's Artificial Intelligence Auditing Framework", publisher: The IIA, type: professional-body, url: "https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/", date: 2024-09-13, access: full, locator: "sections 'How internal auditors audit AI using this framework' and 'What's new in the 2024 framework'"}
    - {ref: OPTRO-FOF-2025, title: "Top takeaways from 2026 Focus on the Future", publisher: Optro (Richard Chambers), type: vendor, url: "https://optro.ai/blog/top-takeaways-from-2026-focus-on-the-future", date: 2025-11-12, access: full, locator: "section 2, 'The gap grows between AI assurance expectations and internal audit readiness'"}
    - {ref: CBH-POD-2025, title: "Auditing AI: the role of internal audit", publisher: Cherry Bekaert, type: podcast, url: "https://www.cbh.com/insights/podcasts/auditing-ai-internal-audits-expanding-role", date: 2025-05-30, access: full, locator: "show notes (audio not heard)"}
    - {ref: BAKERTILLY-IA-2026, title: "Strategy in motion: internal audit's 2026 execution mandate", publisher: Baker Tilly, type: firm, url: "https://www.bakertilly.com/insights/internal-audit-2026-execution-mandate", date: 2026-04-10, access: full, locator: "sections 3 and 4"}
  last_reviewed: 2026-10-16
  notes: >
    Grade C: the survey is vendor-published and measures readiness, not assurance quality. The IIA page URL contains
    "2023" but the page shows a 13 Sep 2024 date; treat as a foundation document. Baker Tilly describes the March 2026
    IIA Great Audit Minds conference as a tipping point from AI experiments to execution [BAKERTILLY-IA-2026].

- id: assurance-assurance-over-ai-10
  title: ISO/IEC 42001 AI management system certification by accredited certification bodies
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: >
    Customers want proof that an AI developer or deployer governs AI responsibly. ISO/IEC 42001 certifies a
    management system, not individual AI systems, and the standard for certifying bodies (ISO/IEC 42006) was
    published about nineteen months after ISO 42001 itself [HUMANITIX-BABL-2026] [CASRAI-42006-2026].
  solution: >
    Accredited certification bodies audit an organisation's AI management system against ISO/IEC 42001. BSI says it
    holds accreditation from UKAS, RvA and, since 10 Mar 2026, ANAB [BSI-ANAB-2026]. A secondary guide records ANAB
    accrediting its first certification body in Sep 2024 [CASRAI-42006-2026]; Schellman says it was the first ANAB-accredited body for ISO 42001 [SCHELLMAN-AIUC1-2026]. Anthropic, Sierra and Zendesk posted
    ISO 42001 certificates in the CSA STAR Registry [CSA-STARAI-2025]; Fieldguide says it holds ISO 42001 certification [FIELDGUIDE-AIUC1-2026].
  outcomes:
    - lever: growth
      description: Organisations reporting steps to align with ISO/IEC 42001
      figure: "26%"
      measures: "share of organisations reporting they are taking steps to align with ISO/IEC 42001, per BSI-commissioned research quoted in BSI's press release; sample not stated"
      provenance: vendor-published
      source_ref: BSI-ANAB-2026
  prerequisites:
    - An accredited certification body; buyers are advised to check the accreditation body's register and scope, not just the certificate [CASRAI-42006-2026]
  risks_and_guardrails:
    - One guide notes that the number of accredited certification bodies named in a single vendor tally (roughly a dozen) is far smaller than the number of organisations advertising certification services; the guide could not verify the roster itself [CASRAI-42006-2026].
    - A webinar listing says ISO 42001 certifies management systems without giving assurance over individual AI systems [HUMANITIX-BABL-2026].
  human_checkpoints:
    - Certification decision by the accredited body after audit [CASRAI-42006-2026]
  role_evolution: >
    ISO/IEC 42006 assesses competence at the audit-team level rather than the individual auditor, according to
    secondary reporting summarised by CASRAI, which says it could not read the standard [CASRAI-42006-2026].
  evidence_grade: B
  sources:
    - {ref: BSI-ANAB-2026, title: "BSI secures ANAB accreditation to certify ISO/IEC 42001", publisher: BSI, type: firm, url: "https://www.bsigroup.com/en-IE/insights-and-media/media-centre/press-releases/2026/march/bsi-secures-anab-accreditation-to-certify-isoiec-42001/", date: 2026-03-10, access: full, locator: "paragraphs 1-3"}
    - {ref: CASRAI-42006-2026, title: "ISO/IEC 42006 explained: who is allowed to certify ISO 42001", publisher: CASRAI, type: community, url: "https://casrai.org/guides/iso-42006-explained-who-can-certify-iso-42001", date: 2026-09-25, access: full, locator: "sections 'The 2024-2026 accreditation record' and 'The BSI claims, kept separate'"}
    - {ref: CSA-STARAI-2025, title: "Cloud Security Alliance launches STAR for AI", publisher: Cloud Security Alliance, type: professional-body, url: "https://cloudsecurityalliance.org/press-releases/2025/10/23/cloud-security-alliance-launches-star-for-ai-establishing-the-global-framework-for-responsible-and-auditable-artificial-intelligence", date: 2025-10-23, access: full, locator: "paragraph 'STAR for AI Level 2'"}
    - {ref: FIELDGUIDE-AIUC1-2026, title: "Fieldguide becomes first AI platform for audit and advisory to achieve AIUC-1 certification", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/blog/fieldguide-first-aiuc-1-certification", date: 2026-05-06, access: full, locator: "final paragraph before quotes"}
    - {ref: SCHELLMAN-AIUC1-2026, title: "Schellman becomes the first accredited auditor for AIUC-1", publisher: Schellman, type: firm, url: "https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1", date: 2026-02-03, access: full, locator: "CEO quote, paragraph 2"}
    - {ref: HUMANITIX-BABL-2026, title: "AI Assurance in Practice: providing trust beyond AI governance certifications", publisher: ISACA Melbourne Chapter, type: conference, url: "https://events.humanitix.com/july-2026-emerging-technologies-working-group", date: 2026-07-16, access: full, locator: "event description"}
  last_reviewed: 2026-10-16
  notes: >
    Dates conflict: CASRAI gives 7 Jul 2025 for ISO/IEC 42006; the landscape's BSI-42006-2025 source is dated 21 Jul 2025
    (probably the national adoption date). BSI's Nov 2025 and Mar 2026 accreditation claims are different events
    [CASRAI-42006-2026]. No certificate counts were found. Grade B (named certifiers and certified organisations, no measured outcomes).

- id: assurance-assurance-over-ai-11
  title: Buyer-side verification of AI assurance evidence in procurement and third-party risk
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Procurement teams receive certificates and reports whose meaning depends on who issued them and against what
    criteria [CASRAI-42006-2026]. SOC 2 is described as the default trust signal that enterprise buyers demand from AI
    vendors, yet the AICPA has not published AI-specific Trust Services Criteria, so two clean reports can cover different control sets [CSA-SOC2-2026].
  solution: >
    A five-minute register check (who accredited the certifier, and is the scope right) is recommended for ISO 42001
    certificates [CASRAI-42006-2026]. KPMG UK says it finds AI assurance increasingly requested and assessed by
    procurement and supplier risk teams [KPMGUK-GOVAI-2026]. techUK says investors, insurers and procurement teams are
    increasingly asking for assurance evidence [TECHUK-ROADMAP-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: CASRAI-42006-2026
  prerequisites:
    - Accreditation registers that can be searched by certificate or body [CASRAI-42006-2026]
  risks_and_guardrails:
    - CASRAI says IAF CertSearch does not allow listing certificates by certification body, which makes a supplier's track record hard to check; I did not verify this against IAF [CASRAI-42006-2026].
  human_checkpoints:
    - Procurement or risk reviewer confirms the scope covers the AI system being bought [CASRAI-42006-2026]
  role_evolution: >
    The sources do not describe role change; they describe a new due-diligence step for procurement and third-party risk teams [KPMGUK-GOVAI-2026].
  evidence_grade: C
  sources:
    - {ref: CASRAI-42006-2026, title: "ISO/IEC 42006 explained: who is allowed to certify ISO 42001", publisher: CASRAI, type: community, url: "https://casrai.org/guides/iso-42006-explained-who-can-certify-iso-42001", date: 2026-09-25, access: full, locator: "section 'How to check an ISO 42001 certificate'"}
    - {ref: CSA-SOC2-2026, title: "The SOC 2 AI gap: auditors improvise where AICPA has not acted", publisher: CSA Labs, type: professional-body, url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/", date: 2026-08-30, access: full, locator: "Key Takeaways"}
    - {ref: KPMGUK-GOVAI-2026, title: "Independent confidence in how you govern AI", publisher: KPMG UK, type: firm, url: "https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html", date: 2026-09-22, access: full, locator: "section 'Benefits', 'Differentiate in the market'"}
    - {ref: TECHUK-ROADMAP-2026, title: "One year on: the Trusted Third-Party AI Assurance Roadmap", publisher: techUK, type: conference, url: "https://www.techuk.org/events/one-year-on-the-trusted-third-party-ai-assurance-roadmap", date: 2026-09-28, access: full, locator: "'Why this matters now'"}
  last_reviewed: 2026-10-16
  notes: >
    The techUK text is an event description written beforehand. CSA is an industry body that publishes related frameworks
    (AICM, STAR for AI), so its note on the SOC 2 gap is not neutral. Grade C: commentary and a vendor-style claim from KPMG; no deployment data.

- id: assurance-assurance-over-ai-12
  title: SOC-style attestation and ISAE 3000 assurance opinions over AI governance and controls
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: announced
  problem: >
    Customers, boards and regulators want a recognisable report showing that AI governance is operating, not just documented.
    EY's SOC conference says "trust me" is not enough and customers want tested evidence [EY-SOC-2026].
  solution: >
    KPMG UK combines its Trusted AI framework, controls assurance and SOC principles to give an independent opinion on AI
    governance and controls under ISAE (UK) 3000, assessing whether controls are clearly defined, suitably designed
    (against the Trust Services Criteria, informed by the EU AI Act and ISO/IEC 42001) and operating effectively
    [KPMGUK-GOVAI-2026]. CSA has launched STAR for AI, including a Level 2 route built on ISO/IEC 42001, and in Mar 2026
    published guidelines for CPAs doing SOC 2+ attestation for STAR for AI [CSA-STARAI-2025] [CSA-CPAGUIDE-2026]. Baker
    Tilly shows how AI controls can map to each element of the SOC 2 Trust Services Criteria [BAKERTILLY-SOC2-2025].
  outcomes:
    - lever: growth
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: KPMGUK-GOVAI-2026
  prerequisites:
    - An AI governance control framework with ownership, escalation and lifecycle management [KPMGUK-GOVAI-2026]
    - Criteria: the AICPA has published no AI-specific Trust Services Criteria, so auditors build ad hoc evidence requests [CSA-SOC2-2026]
  risks_and_guardrails:
    - EY says attestation is harder for AI because AI is not a series of control points: it spans data, models, platforms, applications and operations [EY-SOC-2026].
    - AICPA leaders have warned that "fast and easy" SOC tooling risks quality and objectivity [JOFA-SOCFAST-2026].
  human_checkpoints:
    - Practitioner judgement in scoping and criteria selection ("scope negotiation") [JOFA-EVAL-2025]
  role_evolution: >
    EY's Americas assurance chief technology officer describes a "two-in-the-box" model where an AI auditor and an IT professional
    assess risk together [JOFA-EVAL-2025].
  evidence_grade: C
  sources:
    - {ref: KPMGUK-GOVAI-2026, title: "Independent confidence in how you govern AI", publisher: KPMG UK, type: firm, url: "https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html", date: 2026-09-22, access: full, locator: "section 'Make AI trust stand up to scrutiny'"}
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "section 'How attestation and certification strengthen AI assurance'"}
    - {ref: CSA-STARAI-2025, title: "Cloud Security Alliance launches STAR for AI", publisher: Cloud Security Alliance, type: professional-body, url: "https://cloudsecurityalliance.org/press-releases/2025/10/23/cloud-security-alliance-launches-star-for-ai-establishing-the-global-framework-for-responsible-and-auditable-artificial-intelligence", date: 2025-10-23, access: full, locator: "paragraphs 'Two foundational components'"}
    - {ref: CSA-CPAGUIDE-2026, title: "Guidelines for CPAs providing CSA STAR or STAR for AI attestation program", publisher: Cloud Security Alliance, type: professional-body, url: "https://cloudsecurityalliance.org/artifacts/guidelines-for-cpas-providing-csa-star-or-star-for-ai-attestation-program", date: 2026-03-05, access: full, locator: "landing page description (document not downloaded)"}
    - {ref: BAKERTILLY-SOC2-2025, title: "Representing AI controls in your SOC 2 report", publisher: Baker Tilly, type: firm, url: "https://www.bakertilly.com/insights/ai-controls-for-soc-2-reports", date: 2025-12-18, access: full, locator: "sections on risk categories and TSC mapping"}
    - {ref: CSA-SOC2-2026, title: "The SOC 2 AI gap: auditors improvise where AICPA has not acted", publisher: CSA Labs, type: professional-body, url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/", date: 2026-08-30, access: full, locator: "Key Takeaways"}
    - {ref: JOFA-SOCFAST-2026, title: "Promises of 'fast and easy' threaten SOC credibility", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/", date: 2026-02-01, access: full, locator: "opening quotes"}
    - {ref: JOFA-EVAL-2025, title: "A new frontier: CPAs as AI system evaluators", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/issues/2025/nov/a-new-frontier-cpas-as-ai-system-evaluators/", date: 2025-11-01, access: full, locator: "sections 'What's an AI audit?' and 'Risk profiles in AI evaluations'"}
  last_reviewed: 2026-10-16
  notes: >
    Announced: KPMG UK describes a product with no named client or issued opinion on the page read. The KPMG UK
    opinion type is stated as reasonable assurance in the landscape's summary of the controls paper; the web page itself
    says "independent assurance opinion" under ISAE (UK) 3000. The AICPA TQA 9561 (SOC 1 and SOC 2 effects of AI, 11 Sep 2026) is in the landscape and was not re-opened.

- id: assurance-assurance-over-ai-13
  title: System-level technical AI assurance engagements (bias audits, LLM testing, risk-management engagements)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: >
    Governance certification does not tell a buyer whether an individual AI system performs as claimed [HUMANITIX-BABL-2026].
    Much existing AI assurance in the UK is supplied by AI developers themselves, which raises independence questions [CONSULTANCY-BIG4-2025].
  solution: >
    An engagement borrows the practitioner, responsible party and intended-user model from financial audit, including
    ISAE 3000-style reasonable and limited assurance: select a normative framework and criteria, then gather evidence by
    inspection, inquiry, reperformance and analytical testing. A 16 Jul 2026 ISACA Melbourne session by Babl AI's CEO used
    NYC Local Law 144 bias audits, LLM testing against the NIST AI RMF Generative AI Profile, and EU AI Act risk-management engagements as examples
    [HUMANITIX-BABL-2026]. BSI offers an Algorithm Auditing and Dataset Testing service that verifies an AI system performs as intended by assessing algorithms, models and datasets [DSIT-ROADMAP-2025]. An AICPA assurance and advisory innovation senior manager expects functionality
    engagements to be likelier at the developer and governance engagements at the deployer [JOFA-EVAL-2025].
  outcomes:
    - lever: growth
      description: Size of the UK AI assurance market
      figure: "about GBP 1.01 billion GVA in 2024; over 524 companies"
      measures: "approximate value (gross value added) of the UK AI assurance market in 2024 and number of companies operating in it, per the ministerial foreword of the DSIT roadmap"
      provenance: independent
      source_ref: DSIT-ROADMAP-2025
  prerequisites:
    - Access to the system, data and documentation; the roadmap says mapping best practice for information access between assurers and those they assess is a priority action [TECHUK-ROADMAP-2026]
    - Criteria; AICPA and Caseware voices say scope and criteria are negotiated because no comprehensive framework exists [JOFA-EVAL-2025]
  risks_and_guardrails:
    - DSIT cites a World Privacy Forum report suggesting up to 38% of AI governance tools may use metrics that could result in harm [DSIT-ROADMAP-2025].
    - A Caseware executive says her firm calls its output an "evaluation report" because misusing the term "assurance" can be a problem in some jurisdictions [JOFA-EVAL-2025].
  human_checkpoints:
    - Practitioner scoping, criteria selection and opinion [JOFA-EVAL-2025]
  role_evolution: >
    Deloitte, Grant Thornton UK, KPMG and Forvis Mazars staff were scheduled to speak at ICAEW's AI Assurance Conference
    (6 Jul 2026), and a Deloitte partner leads a Global Algorithm and AI Assurance team and chairs an ICAEW AI Assurance Working Group, per the programme biographies [ICAEW-AIAC-2026].
  evidence_grade: B
  sources:
    - {ref: HUMANITIX-BABL-2026, title: "AI Assurance in Practice: providing trust beyond AI governance certifications", publisher: ISACA Melbourne Chapter, type: conference, url: "https://events.humanitix.com/july-2026-emerging-technologies-working-group", date: 2026-07-16, access: full, locator: "event description"}
    - {ref: DSIT-ROADMAP-2025, title: "Trusted third-party AI assurance roadmap", publisher: UK Department for Science, Innovation and Technology, type: regulator, url: "https://www.gov.uk/government/publications/trusted-third-party-ai-assurance-roadmap/trusted-third-party-ai-assurance-roadmap", date: 2025-09-03, access: full, locator: "ministerial foreword; sections on process certification (BSI AA&DT) and quality of tools"}
    - {ref: JOFA-EVAL-2025, title: "A new frontier: CPAs as AI system evaluators", publisher: Journal of Accountancy, type: professional-body, url: "https://www.journalofaccountancy.com/issues/2025/nov/a-new-frontier-cpas-as-ai-system-evaluators/", date: 2025-11-01, access: full, locator: "sections 'What's an AI audit?' and 'Safeguards against AI failures'"}
    - {ref: ICAEW-AIAC-2026, title: "AI Assurance Conference 2026 (programme and speakers)", publisher: ICAEW, type: conference, url: "https://www.icaew.com/learning-and-development/events/ai-assurance-conference", date: 2026-07-06, access: full, locator: "'Our speakers' (names not in the extracted text)"}
    - {ref: CONSULTANCY-BIG4-2025, title: "Big Four weighing up new AI audit offerings", publisher: Consultancy.uk, type: press, url: "https://www.consultancy.uk/news/40424/big-four-weighing-up-new-ai-audit-offerings", date: 2025-06-10, access: full, locator: "paragraphs 4-6"}
    - {ref: TECHUK-ROADMAP-2026, title: "One year on: the Trusted Third-Party AI Assurance Roadmap", publisher: techUK, type: conference, url: "https://www.techuk.org/events/one-year-on-the-trusted-third-party-ai-assurance-roadmap", date: 2026-09-28, access: full, locator: "first paragraph (four workstreams)"}
  last_reviewed: 2026-10-16
  notes: >
    Grade B: named providers (BSI, Babl AI, Deloitte and others) and a measured market size, but no measured assurance outcomes.
    The webinar page says these are worked examples; it does not say Babl AI delivered each one. The market-size figure
    is a government estimate (provenance independent); an earlier DSIT figure quoted by ICAEW in Feb 2025 gave 524 firms (84 specialised) and a 2035 potential above GBP 6.53 billion [ICAEW-WHERE-2025],
    versus GBP 18.8 billion in the 2025 roadmap; the reason for the difference was not found.

- id: assurance-assurance-over-ai-14
  title: AIUC-1 certification of AI agents (technical evaluation plus audit evidence, re-tested quarterly)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: >
    Enterprise security, legal and procurement teams run bespoke risk assessments of AI agents, and agent behaviour
    changes after a point-in-time audit [SCHELLMAN-AIUC1-2026].
  solution: >
    The Artificial Intelligence Underwriting Company (AIUC) runs technical evaluations (adversarial scenarios derived from
    real incidents) and issues the certificate; Schellman, named first authorised auditor on 3 Feb 2026, collects independent
    audit evidence and reports [SCHELLMAN-AIUC1-2026]. Agent behaviour is tested at least quarterly [FIELDGUIDE-AIUC1-2026].
    Fieldguide (audit software, certified 6 May 2026) and Sierra (customer-service agents, announced 17 Sep 2026) say they hold the certification [FIELDGUIDE-AIUC1-2026] [SIERRA-AIUC1-2026].
  outcomes:
    - lever: risk
      description: Certification maintained by technical re-testing at least quarterly and a full audit each year
      figure: "quarterly re-test; annual audit"
      measures: "cadence of re-evaluation stated in Sierra's announcement and Schellman's release, not a measured result"
      provenance: vendor-published
      source_ref: SIERRA-AIUC1-2026
  prerequisites:
    - Controls reviewed by the auditor across technical, legal, operational and governance areas [SIERRA-AIUC1-2026]
  risks_and_guardrails:
    - The standard covers six principles: security, safety, reliability, accountability, data and privacy, and societal impact; it operationalises ISO 42001, NIST AI RMF, MITRE ATLAS and OWASP Top 10 for LLMs [SCHELLMAN-AIUC1-2026].
    - Every account read is a certifier's or certified company's own announcement.
  human_checkpoints:
    - Annual full audit and auditor review of governance controls [SIERRA-AIUC1-2026]
  role_evolution: >
    Schellman's AI practice leader says AIUC-1 complements risk-management frameworks such as ISO 42001 with agent-specific
    technical controls, and that leading AI companies adopt both [SCHELLMAN-AIUC1-2026].
  evidence_grade: B
  sources:
    - {ref: SCHELLMAN-AIUC1-2026, title: "Schellman becomes the first accredited auditor for AIUC-1", publisher: Schellman, type: firm, url: "https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1", date: 2026-02-03, access: full, locator: "paragraphs 1-4 and 'AIUC-1 certification overview'"}
    - {ref: FIELDGUIDE-AIUC1-2026, title: "Fieldguide becomes first AI platform for audit and advisory to achieve AIUC-1 certification", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/blog/fieldguide-first-aiuc-1-certification", date: 2026-05-06, access: full, locator: "paragraphs 1-4"}
    - {ref: SIERRA-AIUC1-2026, title: "Sierra earns AIUC-1 certification after independent audit", publisher: Unite.AI, type: press, url: "https://www.unite.ai/es/sierra-earns-aiuc-1-certification-after-independent-audit/", date: 2026-09-17, access: full, locator: "paragraphs 1-2 and 'Alcance de las pruebas'"}
  last_reviewed: 2026-10-16
  notes: >
    Search results also named ElevenLabs, Intercom's Fin and UiPath (Mar 2026, [UIPATH-AIUC1-2026]) as certified; those are search-only and not used in outcomes.
    Schellman is described in its own release as "first authorized auditor"; the headline says "accredited". Accreditation status should be checked with AIUC.
    The standard was reported revised on 15 Jul 2026 (search-only). Sierra also posted an ISO 42001 certificate [CSA-STARAI-2025].

- id: assurance-assurance-over-ai-15
  title: Continuous assurance over AI risk instead of an annual audit cycle
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >
    A summary of Genpact's CAE Forum (26 Mar 2026) says annual audit plans cannot keep pace with continuously changing AI systems
    and that boards want ongoing assessments [GENPACT-CAE-2026]. EY's SOC conference says risk assessment cannot be a static
    or annual exercise [EY-SOC-2026].
  solution: >
    Move from point-in-time assessment to continuous monitoring with real-time dashboards and dynamic audit planning
    [GENPACT-CAE-2026]. AIUC-1's quarterly agent re-testing is one live example of the cadence [FIELDGUIDE-AIUC1-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: GENPACT-CAE-2026
  prerequisites:
    - An AI inventory and agreed risk indicators [GENPACT-CAE-2026]
  risks_and_guardrails:
    - In an EY conference poll, 71% of participants rated their risk management maturity 7 or lower out of 10 [EY-SOC-2026]; poll size not stated.
  human_checkpoints:
    - Human oversight of AI-generated outputs, which EY says are still required even as accuracy improves [EY-SOC-2026]
  role_evolution: >
    The Genpact forum summary says CAEs need data scientists and AI ethics specialists on their teams [GENPACT-CAE-2026].
  evidence_grade: D
  sources:
    - {ref: GENPACT-CAE-2026, title: "Evolving AI governance demands new oversight and audit strategies", publisher: welcome.ai (summary of Genpact CAE Forum, 2026-03-26), type: press, url: "https://www.welcome.ai/content/evolving-ai-governance-demands-new-oversight-and-audit-strategies", date: 2026-09-11, access: full, locator: "paragraphs on continuous assurance"}
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "section 'Managing AI risks through continuous assurance'"}
    - {ref: FIELDGUIDE-AIUC1-2026, title: "Fieldguide becomes first AI platform for audit and advisory to achieve AIUC-1 certification", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/blog/fieldguide-first-aiuc-1-certification", date: 2026-05-06, access: full, locator: "paragraph 3"}
  last_reviewed: 2026-10-16
  notes: >
    Idea as discussed by practitioners. The Genpact summary is an AI-generated aggregator page; the original Genpact material was not reached.

- id: assurance-assurance-over-ai-16
  title: Quality infrastructure for AI assurers (professional certification, code of ethics, accreditation)
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [coordination-scheduling, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: piloting
  problem: >
    The UK government says it is difficult to judge the quality of existing AI assurance certifications and that none are
    issued by UKAS-accredited organisations [DSIT-ROADMAP-2025]. techUK says the sector lacks an agreed competency framework,
    clear career pathways and a professional body to set and uphold standards [TECHUK-ROADMAP-2026].
  solution: >
    DSIT's Sep 2025 roadmap set four immediate actions: a consortium to professionalise the market, a skills and competencies
    framework, a map of information access, and an AI Assurance Innovation Fund [TECHUK-ROADMAP-2026]. It suggests AI auditing could be a starting
    point for professional certification [DSIT-ROADMAP-2025]. It judged process certification and accreditation of assurers premature, while noting
    UKAS is piloting accreditation of ISO/IEC 42001 certification bodies [DSIT-ROADMAP-2025]. ICAEW's conference included a session on what an AI
    assurance profession could look like [ICAEW-AIAC-2026].
  outcomes:
    - lever: quality
      description: Consortium workstreams reported under way at the one-year point
      figure: "three workstreams under way (code of ethics, skills framework, information-access map)"
      measures: "work items techUK's event description says are underway; no deliverable seen"
      provenance: self-reported
      source_ref: TECHUK-ROADMAP-2026
  prerequisites:
    - A consortium chaired by BCS and supported by DSIT, with techUK leading its industry advisory group [TECHUK-ROADMAP-2026]
  risks_and_guardrails:
    - ICAEW reports the government judged it premature to put a regulated body and professional standard in place [ICAEW-ROADMAP-2025].
    - A commentator notes the roadmap has no binding audit mandate, thresholds or standard report template [SUBSTACK-JAIN-2025]. Low-authority opinion.
  human_checkpoints:
    - Accreditation or registration decision by a recognised authority, if introduced [ICAEW-ROADMAP-2025]
  role_evolution: >
    The roadmap treats AI auditing as one specialism within a wider assurance profession, with pathways from internal audit,
    cybersecurity, data science and privacy [DSIT-ROADMAP-2025].
  evidence_grade: B
  sources:
    - {ref: DSIT-ROADMAP-2025, title: "Trusted third-party AI assurance roadmap", publisher: UK DSIT, type: regulator, url: "https://www.gov.uk/government/publications/trusted-third-party-ai-assurance-roadmap/trusted-third-party-ai-assurance-roadmap", date: 2025-09-03, access: full, locator: "sections on professionalisation, process certification and accreditation"}
    - {ref: ICAEW-ROADMAP-2025, title: "Trusted AI assurance roadmap outlines three quality assurance models", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/trusted-ai-assurance-roadmap-outlines-three-quality-assurance-models", date: 2025-09, access: full, locator: "sections 'Professionalisation' and 'Process certification'"}
    - {ref: TECHUK-ROADMAP-2026, title: "One year on: the Trusted Third-Party AI Assurance Roadmap", publisher: techUK, type: conference, url: "https://www.techuk.org/events/one-year-on-the-trusted-third-party-ai-assurance-roadmap", date: 2026-09-28, access: full, locator: "first paragraph and 'Why this matters now'"}
    - {ref: ICAEW-AIAC-2026, title: "AI Assurance Conference 2026", publisher: ICAEW, type: conference, url: "https://www.icaew.com/learning-and-development/events/ai-assurance-conference", date: 2026-07-06, access: full, locator: "'Explore professionalisation'"}
    - {ref: SUBSTACK-JAIN-2025, title: "Auditing AI without illusions", publisher: Soumya Jain (Substack), type: community, url: "https://wildandempty.substack.com/p/auditing-ai-without-illusions", date: 2025-09-13, access: full, locator: "list of what the roadmap lacks"}
  last_reviewed: 2026-10-16
  notes: >
    UK-specific. Grade B: named programme and bodies, work in progress, no measured results. The Centre for AI Measurement (led by NPL) is described by techUK as launched to underpin assurance with metrology [TECHUK-ROADMAP-2026].

- id: assurance-assurance-over-ai-17
  title: AI assurance linked to insurance underwriting
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: announced
  problem: >
    Liability for AI failures is unclear. Consultancy.uk, summarising the FT, notes that some insurers offer policies covering
    losses from malfunctioning AI services [CONSULTANCY-BIG4-2025].
  solution: >
    AIUC describes itself as building "confidence infrastructure" through certification, auditing and insurance for AI agents
    [SCHELLMAN-AIUC1-2026]. techUK's listing includes an "AI insurance in practice" workshop on risk, assurance and underwriting [TECHUK-ROADMAP-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: SCHELLMAN-AIUC1-2026
  prerequisites:
    - A certification standard and evidence an underwriter accepts [SCHELLMAN-AIUC1-2026]
  risks_and_guardrails:
    - The sources do not say whether certification changes underwriting terms; no policy terms or loss data were found.
  human_checkpoints:
    - Underwriter decision (not described in the sources)
  role_evolution: >
    Not described in the sources.
  evidence_grade: C
  sources:
    - {ref: SCHELLMAN-AIUC1-2026, title: "Schellman becomes the first accredited auditor for AIUC-1", publisher: Schellman, type: firm, url: "https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1", date: 2026-02-03, access: full, locator: "'About AIUC'"}
    - {ref: CONSULTANCY-BIG4-2025, title: "Big Four weighing up new AI audit offerings", publisher: Consultancy.uk, type: press, url: "https://www.consultancy.uk/news/40424/big-four-weighing-up-new-ai-audit-offerings", date: 2025-06-10, access: full, locator: "paragraph 4"}
    - {ref: TECHUK-ROADMAP-2026, title: "One year on: the Trusted Third-Party AI Assurance Roadmap", publisher: techUK, type: conference, url: "https://www.techuk.org/events/one-year-on-the-trusted-third-party-ai-assurance-roadmap", date: 2026-09-28, access: full, locator: "related events list"}
  last_reviewed: 2026-10-16
  notes: Vendor claim and an event title. Included because insurers appear in techUK's list of parties demanding assurance evidence.

- id: assurance-assurance-over-ai-18
  title: Audit firms building AI assurance as a new service line
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [expert-judgment, client-interaction]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: announced
  problem: >
    Realtid, summarising the Financial Times, reports that AI assurance has no clear standards and quality ranges from
    superficial advice to technical reviews focused on single legal requirements; many providers are the developers
    themselves [REALTID-FT-2025].
  solution: >
    In June 2025 press reports, Deloitte, EY, PwC and KPMG were said to be positioning to offer AI assurance, in the way
    they entered ESG assurance, and PwC UK's chief technology officer for audit said the firm already checks chatbot accuracy and bias
    [REALTID-FT-2025] [CONSULTANCY-BIG4-2025]. By Sep 2026 KPMG UK was marketing an AI governance assurance product [KPMGUK-GOVAI-2026], KPMG US
    framed assurance over AI systems as a "new mandate" for SOX [KPMG-SOX-2026], and EY named AI assurance leaders in its SOC conference [EY-SOC-2026].
  outcomes:
    - lever: growth
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: REALTID-FT-2025
  prerequisites:
    - Skills in data science and model testing alongside audit [ICAEW-AIAC-2026]
  risks_and_guardrails:
    - Press commentary raises liability if an assured system later causes harm, which slows even well-resourced firms [REALTID-FT-2025].
    - Consultancy.uk says the Big Four's partnerships with AI tool providers could raise independence questions [CONSULTANCY-BIG4-2025].
  human_checkpoints:
    - Partner sign-off on opinions (not described in the sources)
  role_evolution: >
    Deloitte's audit partner told the FT that AI assurance is critical for wide AI adoption, as quoted by Realtid [REALTID-FT-2025].
  evidence_grade: B
  sources:
    - {ref: REALTID-FT-2025, title: "Revisionsjattarna ser nasta kassako i AI-granskning (reporting the Financial Times)", publisher: Realtid, type: press, url: "https://www.realtid.se/it-tech/revisionsjattarna-ser-nasta-kassako-i-ai-granskning/", date: 2025-06-04, access: full, locator: "sections 'Saknas tydliga standarder' and 'Processen med assurance gar langsamt'"}
    - {ref: CONSULTANCY-BIG4-2025, title: "Big Four weighing up new AI audit offerings", publisher: Consultancy.uk, type: press, url: "https://www.consultancy.uk/news/40424/big-four-weighing-up-new-ai-audit-offerings", date: 2025-06-10, access: full, locator: "paragraphs 3-7"}
    - {ref: KPMGUK-GOVAI-2026, title: "Independent confidence in how you govern AI", publisher: KPMG UK, type: firm, url: "https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html", date: 2026-09-22, access: full, locator: "page overview"}
    - {ref: KPMG-SOX-2026, title: "The Future of SOX: a point of view for 2030 and beyond", publisher: KPMG LLP, type: firm, url: "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf", date: 2026-09-24, access: full, locator: "p.6"}
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "opening section"}
    - {ref: ICAEW-AIAC-2026, title: "AI Assurance Conference 2026", publisher: ICAEW, type: conference, url: "https://www.icaew.com/learning-and-development/events/ai-assurance-conference", date: 2026-07-06, access: full, locator: "speaker biographies"}
  last_reviewed: 2026-10-16
  notes: >
    The Realtid article is a Swedish-language report of an FT piece (the FT original was not reached). A search summary said EY's
    UK technology risk leader cautioned about liabilities; that was not in the text opened and is not used. Landscape item F4/F6 describe KPMG UK and Deloitte offers from other pages.
    Grade B: named firms with offers or teams; no measurements or named client opinions.

- id: assurance-assurance-over-ai-19
  title: EU AI Act-aligned risk-management assurance engagements, and the effect of delayed deadlines
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >
    Assurance providers cite the EU AI Act as a driver of demand [KPMGUK-GOVAI-2026]. The provisional Digital Omnibus agreement
    would defer high-risk obligations for stand-alone Annex III systems to 2 Dec 2027 and for AI in regulated products (Annex I) to 2 Aug 2028 [GIBSON-OMNIBUS-2026].
  solution: >
    Risk-management engagements aligned to the Act are used as worked examples in practitioner training [HUMANITIX-BABL-2026]. KPMG UK's
    framework incorporates relevant Act requirements and ISO/IEC 42001 [KPMGUK-GOVAI-2026]. A 2025 academic paper argues the Act gives no
    data access to researchers and civil society and calls for third-party audit and model access for high-risk systems [ARXIV-HARTMANN-2025].
  outcomes:
    - lever: growth
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: GIBSON-OMNIBUS-2026
  prerequisites:
    - Formal adoption of the Omnibus; at 27 May 2026 it awaited adoption and publication, expected before 2 Aug 2026 [GIBSON-OMNIBUS-2026]
  risks_and_guardrails:
    - Gibson Dunn says implementation was visibly off track by late 2025, which prompted the Commission's Digital Omnibus proposal of 19 Nov 2025 [GIBSON-OMNIBUS-2026].
    - Whether the Omnibus was formally adopted could not be confirmed from the sources opened.
  human_checkpoints:
    - Not described in the sources
  role_evolution: >
    Not described in the sources.
  evidence_grade: C
  sources:
    - {ref: GIBSON-OMNIBUS-2026, title: "EU AI Act omnibus agreement: postponed high-risk deadlines and other key changes", publisher: Gibson Dunn, type: press, url: "https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines/", date: 2026-05-27, access: full, locator: "Key Takeaways; section 2"}
    - {ref: KPMGUK-GOVAI-2026, title: "Independent confidence in how you govern AI", publisher: KPMG UK, type: firm, url: "https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html", date: 2026-09-22, access: full, locator: "sections 'Regulation' and 'Make AI trust stand up to scrutiny'"}
    - {ref: HUMANITIX-BABL-2026, title: "AI Assurance in Practice: providing trust beyond AI governance certifications", publisher: ISACA Melbourne Chapter, type: conference, url: "https://events.humanitix.com/july-2026-emerging-technologies-working-group", date: 2026-07-16, access: full, locator: "worked examples"}
    - {ref: ARXIV-HARTMANN-2025, title: "Addressing the regulatory gap: moving towards an EU AI audit ecosystem beyond the AI Act by including civil society", publisher: Hartmann et al., arXiv 2403.07904v3, type: academic, url: "https://arxiv.org/pdf/2403.07904", date: 2025-02-19, access: full, locator: "abstract"}
  last_reviewed: 2026-10-16
  notes: >
    Demand-timing signal rather than a use case in operation. No source gave counts of engagements. The Omnibus status at the date of
    this file is unconfirmed (a search result said Parliament voted 16 Jun 2026 [SIDLEY-OMNIBUS-2026], search-only).

- id: assurance-assurance-over-ai-20
  title: Using AI to monitor AI performance inside SOC and attestation work
  archetype: assurance
  module: assurance-over-ai
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: >
    AI systems drift, and agents may rewrite themselves and change behaviour to work around anomalies, according to EY's
    SOC conference summary [EY-SOC-2026].
  solution: >
    EY conference speakers said AI can monitor AI system performance and detect problems such as model drift at an early stage,
    and that organisations should start with simple automations in controlled environments before multi-agent set-ups under close oversight [EY-SOC-2026].
  outcomes:
    - lever: risk
      description: none published
      figure: n/a
      measures: n/a
      provenance: n/a
      source_ref: EY-SOC-2026
  prerequisites:
    - Governance in place before multi-agent automation [EY-SOC-2026]
  risks_and_guardrails:
    - EY leaders say AI may invent details and fill in blanks even when told not to, so human oversight stays necessary [EY-SOC-2026].
  human_checkpoints:
    - Human oversight of AI-generated outputs and processes [EY-SOC-2026]
  role_evolution: >
    Not described beyond oversight of AI outputs [EY-SOC-2026].
  evidence_grade: D
  sources:
    - {ref: EY-SOC-2026, title: "How AI assurance builds trust with SOC, attestation and certification", publisher: EY, type: firm, url: "https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf", date: 2026-09, access: full, locator: "section 'How AI improves SOC reporting' (framework and control mapping paragraph)"}
  last_reviewed: 2026-10-16
  notes: Idea as discussed at the conference; no measured use found. The conference's own live poll on AI uses in SOC work (63% evidence collection) is in the landscape (S8) and is about AI used by the assurance provider, not about assurance over AI.
```

**Count by evidence grade:** A 0, B 6 (07, 10, 13, 14, 16, 18), C 10 (02, 03, 05, 06, 08, 09, 11, 12, 17, 19), D 4 (01, 04, 15, 20). Total 20.

---

## 3. Module notes

**Processes and key steps (with work types)**

*Area 1: auditing AI the entity uses in financial reporting and ICFR*
- Identify and inventory AI touching financial reporting, including shadow AI (`research-synthesis`, `review-assurance`) [DART-COSOHU-2026] [UNIQUS-GENAI-2026].
- Assess risk of material misstatement and fraud risk where AI is used (`review-assurance`, `expert-judgment`) [KPMG-ACAGENDA-2025].
- Classify AI-touched controls, understand design, test design (`review-assurance`) [FINREP-JE-2026] [KPMG-404A-2026].
- Test ITGCs, access, change management and segregation of duties over AI components and agents (`review-assurance`, `software-systems`) [UNIQUS-GENAI-2026].
- Test or monitor operating effectiveness; evaluate deficiencies, including whether a deficiency is a material weakness (`data-reporting`, `expert-judgment`) [DART-COSOHU-2026] [KPMG-ACAGENDA-2025].
- Communicate with the audit committee about AI risks and the auditor's own AI use (`client-interaction`) [KPMG-ACAGENDA-2025].

*Area 2: standalone assurance over AI systems*
- Agree scope and criteria (called "scope negotiation" by one Caseware executive) (`expert-judgment`) [JOFA-EVAL-2025].
- Readiness and gap work, then evidence gathering by inspection, inquiry, reperformance, analytical testing or technical evaluation (`review-assurance`) [HUMANITIX-BABL-2026] [SCHELLMAN-AIUC1-2026].
- Report, certificate or opinion (`document-production`) [KPMGUK-GOVAI-2026] [BSI-ANAB-2026].
- Surveillance and re-testing (quarterly for AIUC-1) (`data-reporting`) [FIELDGUIDE-AIUC1-2026].
- Verification of assurers (accreditation, registers, professional credentials) by buyers and regulators (`coordination-scheduling`) [CASRAI-42006-2026] [DSIT-ROADMAP-2025].

**Common pain points**
- No AI-specific criteria. The AICPA has published no AI-specific Trust Services Criteria, so auditors improvise [CSA-SOC2-2026]; "scope negotiation" is manual and varies [JOFA-EVAL-2025].
- Internal capability is thin: 33% of audit partners cite lack of in-house AI expertise and control capability at their largest client [BOARDMEMBER-CAQ-2026]; 28% of internal audit leaders are confident in their teams' ability to audit AI [OPTRO-FOF-2025]; 70% of audit committee respondents want technology skills [DELOITTE-ACPR-2026].
- Weak client data and documentation: 27% cite data quality and 26% thin documentation of models, assumptions and decision logic [BOARDMEMBER-CAQ-2026].
- Access: AI developers rarely grant access to check reliability, security or bias [JOFA-EVAL-2025]; the UK roadmap lists information access as a blocker [TECHUK-ROADMAP-2026].
- Certificate quality: accredited bodies are fewer than organisations advertising certification, per one vendor tally cited by CASRAI [CASRAI-42006-2026].

**Metrics and benchmarks (all readiness, practice or market size; none measure assurance quality)**
- 6% advanced / 40% developed but incomplete or inconsistent / 46% early-stage or reactive AI governance at audit partners' largest client; 57% say AI governance is the biggest audit committee challenge; two-thirds say committees raised AI use in operations or reporting [BOARDMEMBER-CAQ-2026]. Survey of audit partners; sample size not on the page read.
- 75% of audit committee respondents list AI governance as a top-three priority (35% prior year); 56% confident; primary responsibility 20% to 29%; 82% of committees overseeing AI describe oversight as emerging or limited; 248 respondents [DELOITTE-ACPR-2026] [AT-ACPR-2026].
- 63% of surveyed organisations lack formal AI risk appetite or governance; 28% of IA leaders confident to audit AI; 39% expect AI to transform their work significantly by 2030 (32% the year before) [OPTRO-FOF-2025].
- Optro agentic report (400+ GRC and audit leaders): 34% acted on an inaccurate agent output; 38% let agents approve or reject transactions; 34% modify controls or policies; 27% change access; 30% saw an unintended agent action; 25% had a control failure involving an agent; 96% agree workflows should adapt, 9% have redesigned them [OPTRO-AGENTIC-2026]. Vendor-published.
- Genpact research quoted by a summary: nearly 50% of executives think governance is lagging AI [GENPACT-CAE-2026]. Low authority.
- UK AI assurance market: about GBP 1.01 billion GVA (2024), 524 companies, over 12,000 employed (techUK), potential GBP 18.8 billion by 2035 [DSIT-ROADMAP-2025] [TECHUK-ROADMAP-2026].
- BSI research: 26% of organisations taking steps to align with ISO/IEC 42001 [BSI-ANAB-2026].
- Not used: a vendor blog's claim that a Deloitte 2025 survey found 67% of large accelerated filers piloting or deploying AI in a SOX process and 23% having updated control documentation [FINREP-JE-2026]. The Deloitte survey was not seen.

**Guardrails and regulatory points**
- COSO, *Achieving Effective Internal Control Over Generative AI* (23 Feb 2026), builds on the 2013 framework: eight capability types, minimum control expectations, six-step roadmap [DART-COSOHU-2026] [IIA-COSO-2026]. Authors include academics, EY and Meta staff [IIA-COSO-2026].
- AICPA practice aid, *AI Considerations for Financial Statement Auditors* (13 Oct 2026), Part 1 on the entity's AI use; more guidance on risk of material misstatement and audit evidence is promised [JOFA-AIPA-2026].
- PCAOB AS 1105 and AS 2301 technology-assisted-analysis amendments do not specifically address AI; where auditors test controls over electronic information, testing includes relevant ITGCs [CALCPA-AI-2026].
- ISAE (UK) 3000 is the engagement standard KPMG UK cites for its AI governance opinion [KPMGUK-GOVAI-2026]. ISO/IEC 42006 governs certifiers of ISO 42001 [CASRAI-42006-2026]. "Assurance" can be a regulated term [JOFA-EVAL-2025].
- EU AI Act high-risk dates: see use case 19 [GIBSON-OMNIBUS-2026]. The IIA AI Auditing Framework is guidance [IIA-AIFRAMEWORK-2024].

**Frontier signals (dated, sourced)**
- 2026-02-23: COSO releases its generative-AI internal control guidance [DART-COSOHU-2026].
- 2026-03-10: BSI announces ANAB accreditation for ISO/IEC 42001 certification, completing UKAS, RvA and ANAB accreditation [BSI-ANAB-2026].
- 2026-02-03 to 2026-09-17: AIUC-1 gains Schellman as authorised auditor and certified companies including Fieldguide (6 May) and Sierra (17 Sep) [SCHELLMAN-AIUC1-2026] [FIELDGUIDE-AIUC1-2026] [SIERRA-AIUC1-2026].
- 2026-05-19: SEC proposes filer-status changes that would move about half of attested issuers out of 404(b), per Uniqus summarising SEC fact-sheet figures; comments were due 20 Jul 2026; not final [UNIQUS-FILER-2026].
- 2026-05-27: provisional EU deal delays high-risk AI Act dates to Dec 2027 and Aug 2028 [GIBSON-OMNIBUS-2026].
- 2026-09-22: KPMG UK publishes its AI governance assurance product page [KPMGUK-GOVAI-2026]; Deloitte/CAQ survey shows AI governance in 75% of committees' top three [DELOITTE-ACPR-2026].
- 2026-09-24: KPMG says it expects the first wave of AI-related material weaknesses in 2027 and sees a new mandate to assure AI systems [KPMG-SOX-2026].
- 2026-09-28: UK AI assurance consortium (chaired by BCS) reported working on a voluntary code of ethics, a skills framework and an information-access map [TECHUK-ROADMAP-2026].
- 2026-10-13: AICPA's first AI practice aid for auditors, with more sections promised [JOFA-AIPA-2026].

**Workforce and role effects**
- "Two-in-the-box": EY's Americas assurance chief technology officer says AI auditors and IT professionals assess risk together; CPA licensure requires subject-matter expertise on the team, including code, data security and testing and monitoring [JOFA-EVAL-2025].
- Internal audit leaders are told to build skills (a 70/20/10 training model is suggested) and to put named human reviewers in the trail [BAKERTILLY-IA-2026].
- Professional credentials are forming: the UK roadmap suggests AI auditing as the first professional certification [DSIT-ROADMAP-2025]; ISACA promotes an AAIA credential (listed on its own page) [ISACA-5Q-2026].
- The chair of ICAEW's Technology Faculty Board stresses staff training on judgement, not only tool mechanics, in the FRC guidance context [ICAEW-FRCVIEW-2026]; this is firm-side AI use (routed below).

**Objections and concerns practitioners raise**
- Independence and conflicts: many assurers are the developers; Big Four tool partnerships may raise questions [CONSULTANCY-BIG4-2025] [REALTID-FT-2025].
- Audit-washing: inadequate or unstandardised audits can give false assurance (2022 foundation) [GMF-AUDITWASH-2022]; there is no binding audit mandate or template in the UK roadmap [SUBSTACK-JAIN-2025].
- ISO 42001 certifies a management system, not a system's performance [HUMANITIX-BABL-2026]; certifier accreditation lagged the standard [CASRAI-42006-2026].
- Terminology: "audit", "assurance", "evaluation report" [JOFA-EVAL-2025].
- Quality of SOC-type reports: AICPA leaders warn about templated, fast-turn reports [JOFA-SOCFAST-2026] [JOFA-PEER-2026].
- Liability for assured AI that later fails [REALTID-FT-2025].
- Vendor-driven narrative: much of the SOX-and-AI "what auditors will ask" material is written by tool vendors [KOGNITOS-SOXQ-2026] [FINREP-JE-2026].

**Interview probes for an advisor**
1. "Which AI systems touch your close or key controls today, who keeps the inventory, and do you test around them or rely on them?"
2. "When AI flags or decides in a control, what do you keep (prompts, model version, reviewer decision), and what has your external auditor actually asked for?"
3. "Where there is no AI-specific criteria set, who chooses the criteria and the opinion type, and how do you document that choice?"
4. "Who assures the AI your customers buy from you: you, the developer, or an accredited certifier? How do you handle independence and liability?"
5. "What does your audit committee ask first about AI, and what do you bring them that is not a policy list?"

---

## 4. Routed to other modules

| Item | Target module | Source |
|---|---|---|
| Agentic testing of SOX controls (Optro/Midship: SOX test from about 16 hours to under 15 minutes, up to 85% of controls, vendor claim; PayPal "swarm auditing" episode) | controls-testing | SRA-POD-2026 (episodes 2026-05-28, 2026-02-11) |
| FRC guidance coverage; FRC said firms "encouraged" to set metrics for tool impact; reported by Board Agenda that none of six firms monitored impact on audit quality (landscape wording differs: firms were "building ways to monitor") | quality-management | BOARDAGENDA-FRC-2026 |
| PCAOB Acting Chair Botic (9 Dec 2025): AI enhances risk assessment, overreliance may undermine skepticism; PE shifting incentives | quality-management; acceptance-independence | KSLAW-BOTIC-2025 |
| AICPA practice aid Part 2 (firm's own AI use, supervision and review) | quality-management | JOFA-AIPA-2026 |
| ICAEW view on FRC guidance: three risk categories; misinterpretation and misuse hardest | quality-management | ICAEW-FRCVIEW-2026 |
| ICAEW podcast with FRC, Grant Thornton, Deloitte on firms' AI use (11 Nov 2025) | quality-management | ICAEW-POD-2025 |
| CalCPA article: unattributed claim of PCAOB inspection deficiencies in AI-assisted journal-entry testing (unverified) | quality-management; substantive-testing | CALCPA-AI-2026 |
| SOC quality: "fast and easy" tools; AICPA Peer Review Board action (14 May 2026); CSA note | other-assurance (SOC) | JOFA-SOCFAST-2026; JOFA-PEER-2026; CSA-SOC2-2026 |
| SEC staff say consultations include AI in accounting tools and business relationships, PE, partner rotation | acceptance-independence | JDSUPRA-ALI-2026 |
| SEC filer-status proposal (about half of attested issuers leave 404(b), if final) | cross-cutting audit firm business model; controls-testing | UNIQUS-FILER-2026 |
| "Two-in-the-box" AI auditor and IT professional | specialists | JOFA-EVAL-2025 |
| ISACA AAIA credential and 2026 audit questions | specialists | ISACA-5Q-2026 |
| EY SOC poll on AI use by SOC providers (63% evidence collection) | other-assurance (SOC) | EY-SOC-2026 |

---

## 5. Sources

Type counts (61 documents in the table; 59 opened, 2 search-only): professional-body 15, firm 13, press 13, vendor 6, podcast 4, conference 4, community 2, academic 2, survey 1, regulator 1. Access: 59 `full`, 2 `search-only`. There are no `standard-setter` sources, because the COSO publication and ISO standards were not opened; they were read through secondary reports.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| KPMG-SOX-2026 | The Future of SOX: a point of view for 2030 and beyond | KPMG LLP | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/future-sox-point-view-2030-beyond-new.pdf | 2026-09-24 (landscape date; PDF undated) | full |
| KPMG-404A-2026 | The 404(a) opportunity | KPMG LLP | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/404-opportunity.pdf | 2026-08 | full |
| KPMG-ACAGENDA-2025 | On the 2026 audit committee agenda | KPMG Board Leadership Center | firm | https://kpmg.com/kpmg-us/content/dam/kpmg/boardleadership/pdf/2026/on-the-2026-audit-committee-agenda.pdf | 2025-12-05 | full |
| KPMGUK-GOVAI-2026 | Independent confidence in how you govern AI | KPMG UK | firm | https://kpmg.com/uk/en/insights/audit/independent-confidence-in-how-you-govern-ai.html | 2026-09-22 | full |
| DART-COSOHU-2026 | Heads Up: COSO releases publication on internal controls related to generative AI | Deloitte DART | firm | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai | 2026-04-03 | full |
| IIA-COSO-2026 | COSO issues generative AI guidance | The IIA, Internal Auditor | professional-body | https://internalauditor.theiia.org/en/articles/2026/march/coso-issues-genai-guidance/ | 2026-03-11 | full |
| EISNER-COSO-2026 | COSO released GenAI governance guidance | EisnerAmper | firm | https://www.eisneramper.com/insights/artificial-intelligence-insights/coso-ai-governance-internal-control-framework-0526/ | 2026-05-13 | full |
| AT-COSO-2026 | COSO releases guidance on internal controls for AI | Accounting Today | press | https://accountingtoday.com/news/coso-releases-guidance-on-applying-internal-controls-to-ai | 2026-02-24 | full |
| UNIQUS-GENAI-2026 | Internal controls over generative AI | Uniqus | firm | https://uniqus.com/internal-controls-over-generative-ai/ | 2026-04-07 | full |
| UNIQUS-FILER-2026 | What the SEC's filer status overhaul means for ICFR governance | Uniqus | firm | https://uniqus.com/what-the-secs-filer-status-overhaul-means-for-icfr-governance/ | 2026-06-04 | full |
| KOGNITOS-SOXQ-2026 | What your SOX auditor will ask about your AI automation | Kognitos | vendor | https://www.kognitos.com/blog/sox-auditor-questions-ai-automation/ | 2026-05-15 | full |
| FINREP-JE-2026 | AI journal entry testing and SOX 404 controls | Finrep | vendor | https://www.finrep.ai/blog/ai-journal-entry-testing-and-sox-404-controls-a-2026-practitioner-walkthrough | 2026-08-03 | full |
| BOARDMEMBER-CAQ-2026 | What audit partners are seeing on AI and what it means for audit committees | Corporate Board Member | press | https://boardmember.com/?p=50023 | 2026-07-15 | full |
| CAQ-PULSE-2026 | Spring 2026 Audit Partner Pulse Survey release | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-partners-see-companies-moving-forward-with-greater-intent-as-evolving-risks-reshape-strategy-caq-survey-finds | 2026-07-15 | full |
| AT-PULSE-2026 | Audit partners concerned about AI risks | Accounting Today | press | https://www.accountingtoday.com/news/audit-partners-concerned-about-ai-risks | 2026-07-15 | full |
| DELOITTE-ACPR-2026 | Audit Committee Practices Report, fifth edition (media alert) | Deloitte US with CAQ | survey | https://www.deloitte.com/us/en/about/press-room/deloitte-caq-announce-2026-audit-committee-practices-report.html | 2026-09-22 | full |
| AT-ACPR-2026 | Audit committees focusing on emerging risks like AI | Accounting Today | press | https://www.accountingtoday.com/news/audit-committees-focusing-on-emerging-risks-like-ai | 2026-09-22 | full |
| OPTRO-FOF-2025 | Top takeaways from 2026 Focus on the Future | Optro (R. Chambers) | vendor | https://optro.ai/blog/top-takeaways-from-2026-focus-on-the-future | 2025-11-12 | full |
| OPTRO-AGENTIC-2026 | One in three organizations say they have acted on wrong decisions made by AI agents | Optro | vendor | https://optro.ai/blog/one-in-three-organizations-say-they-have-acted-on-wrong-decisions-made-by-ai-agents-optro-research-finds | 2026-10-08 | full |
| SRA-POD-2026 | Speaking of Risk and Audit (episode list, show notes) | AuditBoard/Optro; host R. Chambers | podcast | https://srapodcast.podbean.com/ | 2026-08-31 | full |
| CBH-POD-2025 | Auditing AI: the role of internal audit | Cherry Bekaert | podcast | https://www.cbh.com/insights/podcasts/auditing-ai-internal-audits-expanding-role | 2025-05-30 | full |
| BAKERTILLY-IA-2026 | Strategy in motion: internal audit's 2026 execution mandate | Baker Tilly | firm | https://www.bakertilly.com/insights/internal-audit-2026-execution-mandate | 2026-04-10 | full |
| BAKERTILLY-SOC2-2025 | Representing AI controls in your SOC 2 report | Baker Tilly | firm | https://www.bakertilly.com/insights/ai-controls-for-soc-2-reports | 2025-12-18 | full |
| GENPACT-CAE-2026 | Evolving AI governance demands new oversight and audit strategies (Genpact CAE Forum, 2026-03-26) | welcome.ai | press | https://www.welcome.ai/content/evolving-ai-governance-demands-new-oversight-and-audit-strategies | 2026-09-11 | full |
| IIA-AIFRAMEWORK-2024 | The IIA's Artificial Intelligence Auditing Framework | The IIA | professional-body | https://www.theiia.org/en/content/tools/professional/2023/the-iias-updated-ai-auditing-framework/ | 2024-09-13 | full |
| ISACA-5Q-2026 | Five questions that audit professionals will need to answer in 2026 | ISACA | professional-body | https://www.isaca.org/resources/news-and-trends/isaca-now-blog/2026/five-questions-that-audit-professionals-will-need-to-answer-in-2026 | 2026-01-05 | full |
| DSIT-ROADMAP-2025 | Trusted third-party AI assurance roadmap | UK DSIT | regulator | https://www.gov.uk/government/publications/trusted-third-party-ai-assurance-roadmap/trusted-third-party-ai-assurance-roadmap | 2025-09-03 | full |
| ICAEW-ROADMAP-2025 | Trusted AI assurance roadmap outlines three quality assurance models | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/trusted-ai-assurance-roadmap-outlines-three-quality-assurance-models | 2025-09 | full |
| TECHUK-ROADMAP-2026 | One year on: the Trusted Third-Party AI Assurance Roadmap (event) | techUK | conference | https://www.techuk.org/events/one-year-on-the-trusted-third-party-ai-assurance-roadmap | 2026-09-28 | full |
| ICAEW-AIAC-2026 | AI Assurance Conference 2026 | ICAEW | conference | https://www.icaew.com/learning-and-development/events/ai-assurance-conference | 2026-07-06 | full |
| ICAEW-WHERE-2025 | Where are we now with AI assurance? | ICAEW | professional-body | https://icaew.com/insights/viewpoints-on-the-news/2025/feb-2025/where-are-we-now-with-ai-assurance | 2025-02 | full |
| ICAEW-FRCVIEW-2026 | How helpful is FRC's guidance on generative and agentic AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai | 2026-05 | full |
| ICAEW-POD-2025 | How should audit firms use AI? | ICAEW Beyond Finance podcast | podcast | https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai | 2025-11-11 | full |
| SUBSTACK-JAIN-2025 | Auditing AI without illusions | Soumya Jain (Substack) | community | https://wildandempty.substack.com/p/auditing-ai-without-illusions | 2025-09-13 | full |
| REALTID-FT-2025 | Revisionsjattarna ser nasta kassako i AI-granskning | Realtid | press | https://www.realtid.se/it-tech/revisionsjattarna-ser-nasta-kassako-i-ai-granskning/ | 2025-06-04 | full |
| CONSULTANCY-BIG4-2025 | Big Four weighing up new AI audit offerings | Consultancy.uk | press | https://www.consultancy.uk/news/40424/big-four-weighing-up-new-ai-audit-offerings | 2025-06-10 | full |
| JOFA-EVAL-2025 | A new frontier: CPAs as AI system evaluators | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2025/nov/a-new-frontier-cpas-as-ai-system-evaluators/ | 2025-11-01 | full |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 | full |
| JOFA-SOCFAST-2026 | Promises of 'fast and easy' threaten SOC credibility | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/feb/promises-of-fast-and-easy-threaten-soc-credibility/ | 2026-02-01 | full |
| JOFA-PEER-2026 | AICPA guides peer reviewers to address SOC 2 risks | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/may/aicpa-guides-peer-reviewers-to-address-soc-2-risks/ | 2026-05-14 | full |
| HUMANITIX-BABL-2026 | AI Assurance in Practice: providing trust beyond AI governance certifications | ISACA Melbourne Chapter | conference | https://events.humanitix.com/july-2026-emerging-technologies-working-group | 2026-07-16 | full |
| PJR-POD-2026 | Beyond the hype: building responsible AI with ISO/IEC 42001 certification | Perry Johnson Registrars | podcast | https://perryjohnsonregistrars.podbean.com/e/beyond-the-hype-building-responsible-ai-with-isoiec-42001-certification/ | 2026-05-20 | full |
| INFOSEC-DRATA-2026 | Ask an auditor: ISO 42001 | Drata (listing on infosec-conferences.com) | conference | https://infosec-conferences.com/event/20260513-ask-an-auditor-iso-42001-proving-your/ | 2026-05 | full |
| BSI-ANAB-2026 | BSI secures ANAB accreditation to certify ISO/IEC 42001 | BSI | firm | https://www.bsigroup.com/en-IE/insights-and-media/media-centre/press-releases/2026/march/bsi-secures-anab-accreditation-to-certify-isoiec-42001/ | 2026-03-10 | full |
| CASRAI-42006-2026 | ISO/IEC 42006 explained: who is allowed to certify ISO 42001 | CASRAI | community | https://casrai.org/guides/iso-42006-explained-who-can-certify-iso-42001 | 2026-09-25 | full |
| SCHELLMAN-AIUC1-2026 | Schellman becomes the first accredited auditor for AIUC-1 | Schellman | firm | https://www.schellman.com/blog/news/schellman-becomes-the-first-accredited-auditor-for-aiuc-1 | 2026-02-03 | full |
| FIELDGUIDE-AIUC1-2026 | Fieldguide becomes first AI platform for audit and advisory to achieve AIUC-1 | Fieldguide | vendor | https://www.fieldguide.io/blog/fieldguide-first-aiuc-1-certification | 2026-05-06 | full |
| SIERRA-AIUC1-2026 | Sierra earns AIUC-1 certification after independent audit | Unite.AI | press | https://www.unite.ai/es/sierra-earns-aiuc-1-certification-after-independent-audit/ | 2026-09-17 | full |
| CSA-STARAI-2025 | Cloud Security Alliance launches STAR for AI | Cloud Security Alliance | professional-body | https://cloudsecurityalliance.org/press-releases/2025/10/23/cloud-security-alliance-launches-star-for-ai-establishing-the-global-framework-for-responsible-and-auditable-artificial-intelligence | 2025-10-23 | full |
| CSA-CPAGUIDE-2026 | Guidelines for CPAs providing CSA STAR or STAR for AI attestation | Cloud Security Alliance | professional-body | https://cloudsecurityalliance.org/artifacts/guidelines-for-cpas-providing-csa-star-or-star-for-ai-attestation-program | 2026-03-05 | full (landing page) |
| CSA-SOC2-2026 | The SOC 2 AI gap: auditors improvise where AICPA has not acted | CSA Labs | professional-body | https://labs.cloudsecurityalliance.org/research/csa-research-note-soc2-ai-controls-gap-20260830-csa-styled/ | 2026-08-30 | full |
| EY-SOC-2026 | How AI assurance builds trust with SOC, attestation and certification | EY | firm | https://www.ey.com/content/dam/ey-unified-site/ey-com/en-gl/services/technology-risk/documents/ey-gl-soc-reporting-attestation-conference-highlights-09-2026.pdf | 2026-09 | full |
| GIBSON-OMNIBUS-2026 | EU AI Act omnibus agreement: postponed high-risk deadlines | Gibson Dunn | press | https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines/ | 2026-05-27 | full |
| KSLAW-BOTIC-2025 | PCAOB Acting Chair Botic delivers remarks at the AICPA conference | King & Spalding | press | https://www.kslaw.com/blog-posts/pcaob-acting-chair-botic-delivers-remarks-at-the-aicpa-conference | 2025-12 (remarks 2025-12-09) | full |
| BOARDAGENDA-FRC-2026 | Auditors warned they remain accountable despite use of AI | Board Agenda | press | https://boardagenda.com/2026/03/31/auditors-warned-they-remain-accountable-despite-use-of-ai/ | 2026-03-31 | full |
| CALCPA-AI-2026 | AI standard setting, regulation in audit: part 1 | CalCPA | professional-body | https://www.calcpa.org/whats-happening/articles/ai-standard-setting-regulation-in-audit-part-1 | 2026-08-12 | full |
| JDSUPRA-ALI-2026 | Highlights from ALI Accountants' Liability Conference 2026 | Vedder via JD Supra | press | https://www.jdsupra.com/legalnews/highlights-from-american-law-institute-6955525/ | 2026-05-22 | full |
| GMF-AUDITWASH-2022 | AI audit-washing and accountability | German Marshall Fund of the United States | academic | https://gmfus.org/news/ai-audit-washing-and-accountability | 2022-11-15 | full |
| ARXIV-HARTMANN-2025 | Addressing the regulatory gap: moving towards an EU AI audit ecosystem beyond the AI Act by including civil society | Hartmann et al., arXiv 2403.07904v3 | academic | https://arxiv.org/pdf/2403.07904 | 2025-02-19 | full |
| SIDLEY-OMNIBUS-2026 | EU lawmakers reach provisional agreement to delay key EU AI Act obligations | Sidley Austin | press | https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/ | 2026-06-22 | search-only (403) |
| UIPATH-AIUC1-2026 | UiPath achieves AIUC-1 certification | UiPath | vendor | https://www.uipath.com/newsroom/uipath-achieves-aiuc-1-certification | 2026-03 | search-only |

Listed but not cited by ref in the use cases or notes: CAQ-PULSE-2026 and AT-PULSE-2026 (same survey release as BOARDMEMBER-CAQ-2026, 2026-07-15; they confirm "nearly 90%" of partners rate largest-client AI governance as developing or early stage); PJR-POD-2026 and INFOSEC-DRATA-2026 (ISO 42001 webinar and podcast listings that add little). Also opened and not used: a Schellman on-demand ISO 42001 webinar page (no date shown) and a Diligent assurance-reporting page.

---

## 6. Gaps

**Not found, stated plainly**
- **No quality evidence for assurance over AI.** No error rate, override rate, parallel-run result, inspection finding or independent measurement of an AI assurance engagement or of an AI-enabled control test was found. The numbers available are surveys of readiness, vendor claims, and market size.
- **No disclosed AI-caused material weakness.** Two web searches and three EDGAR full-text phrase queries (two returned zero hits; one returned loose matches on AI-named companies) found none. KPMG says the first wave is expected in 2027 [KPMG-SOX-2026]. The absence may be because disclosures do not name AI.
- **No AI-specific PCAOB or SEC inspection or enforcement item** on auditing AI-enabled controls was found. Two secondary claims (PCAOB 2026 inspection priorities in [UNIQUS-GENAI-2026]; AI-related deficiencies in journal-entry testing in [CALCPA-AI-2026]) are unverified and not used as evidence.
- No named client case of an issued AI governance assurance opinion; no ISO 42001 certificate counts; no US AI-specific attestation criteria beyond CSA's STAR for AI.
- No small-practice or non-Big-Four voice on AI assurance beyond Baker Tilly, Cherry Bekaert, Schellman, Uniqus and Fieldguide.

**Not reachable or not completed**
- **Web-search quota ran out** partway through. Planned searches not run: BDO's ITGC-over-AI paper and AI-agent ITGC discourse, ISACA AAIA demand and holder counts, EU AI Act notified-body capacity, a Deloitte/PwC/EY AI assurance product launch in 2026, and AI audit taxonomies (ACCA/EY assessment types are in the landscape and not re-opened here).
- Blocked or error pages (403 or similar): Babl AI site, MindBridge events, ICAEW events site (a different ICAEW page was read), Foley, Goodwin, Sidley, University at Buffalo (Botic lecture of 7 Apr 2026), and an EY press release (error page). The FT original was not reached (read through Realtid and Consultancy.uk).
- Not opened: the COSO publication itself, the AICPA practice aid full text, AICPA TQA 9561, ISO/IEC 42001 and 42006 text (paywalled), ACCA/EY *AI assessments*, the Deloitte/CAQ report PDF, the Optro report PDFs, and the CAQ pulse PDF. Figures come from press releases and secondary articles.
- Podcasts and conference sessions: only show notes, programmes and recaps were read. No transcripts or recordings. ICAEW's AI Assurance Conference page is a programme, not proceedings; speaker names were not in the extracted text. The Cherry Bekaert podcast (2025-05-30) and ICAEW podcast (2025-11-11) are within the 18-month window but older than most items.
- Community discussion (Reddit, LinkedIn, IIA AuditSphere, ISACA chapters) was not reached.
- A Risk Management Show episode with Richard Chambers could not be dated and is not cited.

**Data conflicts and cautions**
- COSO's eight capability types are listed differently by IIA ("regulatory intelligence") and EisnerAmper ("knowledge retrieval and summarization"); the landscape follows the IIA list.
- ISO/IEC 42006 publication date: 7 Jul 2025 (CASRAI) versus 21 Jul 2025 for the BSI edition (landscape).
- UK AI assurance market potential: GBP 6.53 billion by 2035 (DSIT figure quoted by ICAEW, Feb 2025) versus GBP 18.8 billion (DSIT roadmap, Sep 2025).
- Baker Tilly's statement that the EU AI Act explicitly classes audit AI as high risk is not supported by the Annex III categories named by Gibson Dunn; not used.
- Board Agenda says none of six firms monitored the impact of automated tools on audit quality; the landscape's summary of the FRC review says firms were building ways to monitor. Routed to quality-management for resolution.
- The Realtid article is dated 2025-06-04, not 2026 as a search summary suggested.
- Several sources are vendors or advisers who sell AI governance, controls or certification services (Kognitos, Finrep, Uniqus, Optro, Fieldguide, Schellman, BSI, KPMG, EY, Deloitte); their claims about what auditors will ask or what the market needs are marketing-adjacent.
