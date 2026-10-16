# Module deep dive: assurance / planning-risk-assessment / discourse

- **Archetype:** assurance
- **Module:** planning-risk-assessment. Understanding the entity and its environment (including its IT and AI use), risk assessment procedures and analytics for risk identification, fraud risk assessment and brainstorming, materiality, scoping (including group audits), audit strategy and planning, budgeting and staffing the engagement.
- **Angle:** discourse. What practitioners are saying in the last 12 to 18 months about AI in audit planning and risk assessment: conference sessions, webinars, podcasts, practitioner articles; where it is heading (agentic and continuous risk assessment) and the worries.
- **Prepared:** 2026-10-16
- **Inputs read first:** `research/runs/wave1/landscape-assurance.md` (leads for this module) and `research/briefs/templates/vocabulary.md`.
- **Method note:** 62 sources opened and read for this angle with `curl` through the session proxy (`pdftotext` for PDFs), across 9 source types. Eight Wolters Kluwer pages that block `curl` were read through the r.jina.ai text mirror. Podcast and webinar pages were opened for show notes only; audio and recordings were not available. Web search was used for about eight queries before the shared budget ran out; everything after that came from links and the landscape's URLs. Figures from vendors and firms are marked as such in `outcomes[].provenance`. Quotations are paraphrased or under 25 words.

---

## 1. Summary

1. **Regulators describe planning and risk assessment as the place where AI already helps, and in the same breath warn about skepticism.** On 9 Dec 2025 the PCAOB acting chair said AI can already enhance risk assessment and evidence gathering by analysing entire populations "in certain scenarios", then warned that reliance on AI may erode critical thinking and skepticism and that junior auditors will need new routes to build those skills (ACCTODAY-BOTIC-2025; NYSSCPA-BOTIC-2025). IFIAR's 2024 member data say 55% of the 47 responding members frequently saw automated tools in risk assessment (IFIAR-TTF-2025).
2. **The firms' own account is qualitative.** PwC's U.S. assurance transformation leader said in Oct 2026 that AI is "particularly good" at pointing out where risks may lie, but time savings are "not that drastic yet" and the busy-season shift is modest (CFODIVE-PWC-2026). No firm published an error rate, override rate, parallel-run result or time saving for a planning or risk-assessment tool.
3. **Independent testing is thin and cautious.** ICAEW's single test of three chatbots on a fictional retailer found none performed risk assessment procedures as a human would, none separated financial-statement-level from assertion-level risk, and materiality benchmarks differed by model (ICAEW-PIERPOINT-2025). The FRC's worked example for summarising board minutes still has the auditor read the minutes (FRC-GENAI-2026, p.46). A research preprint reports AUROC 0.782 for a multi-agent restatement-risk scorer, but against restatement labels, not planning decisions (ARXIV-UMAR-2026). No inspection finding on AI risk-assessment tools was found.
4. **The stated destination is agent-built plans and continuous risk assessment, and every dated claim is a firm, vendor or consultancy claim.** PwC Australia says agents will assess risk and design audit plans, piloting with five clients and planning all audit clients by 2028 (PWCAU-2025). EY expects end-to-end audit support by 2028 (EY-CANVAS-2026). MindBridge (22 Sep 2026) and Optro (14 Oct 2026) launched agentic risk assessment products (MINDBRIDGE-ARA-2026; OPTRO-AGENTS-2026). Wolters Kluwer calls the full ecosystem a future-state vision and says analytics come first (WK-AGENTRA-2026). In internal audit, Deloitte and vendors push "continuous scoping" and dynamic plans (GRCREPORT-DELOITTE-2026; WK-DYNAMIC-2026).
5. **The worries cluster in five places:** automation bias and fluent-but-wrong output; erosion of skepticism and of the junior learning path; overselling ("we test everything") widening the expectation gap; "agent washing" and vendor dependence; and small firms lacking specialists to certify tools (ICAEW-FRCVIEW-2026; CPAPA-LEDGERLINE-2026; AUDITBOARD-AGENTICERA-2026).
6. **The scope of risk assessment is itself widening.** Clients' AI governance is immature (6% advanced in the CAQ Spring 2026 Pulse), and AI-enabled fraud is rated a moderate or high risk by 85% of 373 internal audit leaders while 62% say their function is unprepared or minimally prepared (CAQ-INSIDER-2026; IIAF-AIFRAUD-2026). Planning now includes understanding how the entity uses AI (JOFA-AIPA-2026; IFIAR-TTF-2026).
7. **Conference and podcast evidence is mostly agenda-level.** AAA (Jan 2026), KU/Deloitte (May 2026), ENGAGE (Jun 2026), WCARS (Nov 2025, May 2026) and three podcasts were found, but I could open only agendas and show notes, not session content. Planning-relevant spoken content exists only in the PCAOB acting chair's remarks, which I read as prepared remarks through press coverage. The web-search budget ran out before IIA GAM 2026 and ENGAGE recaps could be pursued.
8. **Use cases:** 22 candidates: 0 at grade A, 6 at B, 10 at C, 6 at D (labelled ideas). Six are in production or piloting at named organisations (PwC, PwC Australia, RSM, Helvetia Baloise, FJ Management); none has a published measurement.

---

## 2. Use cases

```yaml
- id: assurance-planning-risk-assessment-01
  archetype: assurance
  module: planning-risk-assessment
  title: 'Idea: LLM summarisation of board minutes and entity documents to focus the auditor''s understanding of
    the entity'
  function: service-delivery
  work_types:
  - research-synthesis
  - review-assurance
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Auditors read the entity's board minutes as part of risk assessment to understand the entity and spot
    risk indicators. The FRC describes this as a review where a tool could help the auditor concentrate on the most
    relevant parts (FRC-GENAI-2026, Illustrative example 1, p.43). Reading it all is slow, and relevant items can
    be missed.
  solution: A tool segments the minutes and gives each segment a stable identifier. It summarises each meeting,
    reviews all meetings together for themes that only show across the period, then writes a final summary in which
    every statement cites the minute section it comes from. The auditor documents that the tool was used and how
    the output shaped further work (FRC-GENAI-2026, pp.43-45). The FRC presents this as an illustrative example
    for a hypothetical firm, not as a reported deployment (FRC-GENAI-2026, p.42).
  outcomes:
  - lever: quality
    description: No outcome published. The FRC example sets no figures and names no firm.
    figure: none published
    measures: no measurement in the source
    source_ref: FRC-GENAI-2026
  prerequisites:
  - Minutes available in digital, readable form
  - A central library of pre-written prompts that specialists have tested (FRC-GENAI-2026, pp.45-46)
  - Certification testing across entities of different sizes and sectors, with prompts refined from observed deficiencies
    (FRC-GENAI-2026, p.45)
  - Staff training on how to review output (FRC-GENAI-2026, p.46)
  risks_and_guardrails:
  - Omitted, distorted or invented content is the named risk set (FRC-GENAI-2026, p.44)
  - Training warns about automation bias and the tendency of the tool to sound fluent and confident when wrong (FRC-GENAI-2026,
    p.46)
  - The example sets the tolerance for output deficiencies by the design of the human review; the tolerance would
    be lower if the reviewer did not read the minutes (FRC-GENAI-2026, p.47)
  human_checkpoints:
  - Auditor reads the board minutes to confirm the summary is complete and accurate (FRC-GENAI-2026, p.46)
  - Closer reading of the cited sections where output conflicts with prior understanding or affects the risk assessment
    (FRC-GENAI-2026, p.46)
  - Review by an engagement-team member who understands the entity (FRC-GENAI-2026, p.46)
  role_evolution: Training centres on reviewing the tool's output because auditors use pre-written prompts and do
    not prompt the tool themselves (FRC-GENAI-2026, p.46).
  evidence_grade: D
  sources:
  - ref: FRC-GENAI-2026
    title: 'Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples'
    publisher: Financial Reporting Council
    type: regulator
    url: https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf
    date: '2026-03-30'
    access: full
    locator: Illustrative example 1, pp.42-47
  - ref: ICAEW-PIERPOINT-2025
    title: 'Testing Gen AI platforms: can they do audit work? (Helen Pierpoint)'
    publisher: ICAEW
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work
    date: '2025-09-24'
    access: full
    locator: 'Introduction: chatbots used for research on entities and environments'
  last_reviewed: '2026-10-16'
  notes: 'Idea only: a regulator-authored example for a hypothetical firm. Pierpoint reports that simple chatbots
    are already used by auditors to improve their understanding of entities and their environments through research,
    with no firm named (ICAEW-PIERPOINT-2025, introduction). No error rate, override rate or time saving found.'
- id: assurance-planning-risk-assessment-02
  archetype: assurance
  module: planning-risk-assessment
  title: Grounded guidance copilots for methodology and standards questions during audit planning and documentation
  function: service-delivery
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Auditors need firm-approved methodology and technical guidance at each step and spend time finding it
    and applying it consistently (CAQ-RSM-2026).
  solution: A generative AI assistant answers questions from the firm's own manuals, practice aids and technical
    guides. RSM describes Ask Luca this way and says it is grounded in firm-approved guidance (CAQ-RSM-2026). PwC
    describes ChatNational as a generative AI chatbot and research tool in use for a year that connects to PwC's
    global research platform for accounting, auditing and reporting guidance (CFOBREW-PWC-2025).
  outcomes:
  - lever: speed
    description: RSM says Ask Luca helps auditors reduce research time and apply guidance more consistently. No
      figure given.
    figure: none published
    measures: no figure given
    provenance: self-reported
    source_ref: CAQ-RSM-2026
  prerequisites:
  - Curated corpus of firm-approved guidance
  - Enterprise-licensed model
  - AI training for staff; PwC says practitioners had training and model access for pre-approved work before its
    enterprise rollout (CFODIVE-PWC-2026)
  risks_and_guardrails:
  - RSM says grounding in firm-approved guidance and experienced human review are vital for comparable tools (CAQ-RSM-2026)
  human_checkpoints:
  - Experienced human review of answers before they inform audit judgments (CAQ-RSM-2026)
  role_evolution: RSM says less research time lets auditors spend more attention on analysis, skepticism and judgment
    (CAQ-RSM-2026).
  evidence_grade: B
  sources:
  - ref: CAQ-RSM-2026
    title: 'Shaping the future of assurance: Advancing AI in the audit (RSM, CAQ Audit in Action blog)'
    publisher: Center for Audit Quality (blog by RSM)
    type: professional-body
    url: https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit
    date: 2026-08
    access: full
    locator: 'Section ''Ask Luca: trusted guidance where auditors work'''
  - ref: CFOBREW-PWC-2025
    title: A look at PwC's 'next generation' audit
    publisher: CFO Brew
    type: press
    url: https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit
    date: '2025-11-05'
    access: full
    locator: Description of ChatNational
  - ref: CFODIVE-PWC-2026
    title: PwC exec ushers in AI-assisted audits, awaits bigger time savings
    publisher: CFO Dive
    type: press
    url: https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/
    date: '2026-10-07'
    access: full
    locator: Paragraph on training and pre-approved use before 2025 launch
  last_reviewed: '2026-10-16'
  notes: Cross-phase tool. Neither source ties it to planning specifically, so the grade is capped at B and the
    entry is kept because planning and risk-assessment methodology questions are a natural use. No measurements
    published.
- id: assurance-planning-risk-assessment-03
  archetype: assurance
  module: planning-risk-assessment
  title: Prior-year-informed planning document auto-population (PwC Simplified Audit for Private Business)
  function: service-delivery
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Planning documents are rebuilt each year from last year's information, and auditors need to see what
    changed in the business since the last audit (PWC-AT-2025).
  solution: The tool ingests prior-year information and auto-populates a planning document that serves as a base
    for considering compliance with AICPA standards. It is designed for private-company clients audited under AICPA
    standards (PWC-AT-2025).
  outcomes:
  - lever: speed
    description: PwC's Shawn Panson said the tool saves time and lets auditors ask better questions by showing what
      changed since last year. No figure given.
    figure: none published
    measures: no figure given
    provenance: self-reported
    source_ref: PWC-AT-2025
  prerequisites:
  - Prior-year audit information in a form the tool can ingest
  - Private-company engagements under AICPA standards (PWC-AT-2025)
  risks_and_guardrails:
  - A risk rating should reflect the current engagement's circumstances and not carry forward the prior-year conclusion
    (WK-SAS145-2024, section on SAS 145 documentation). This is the obvious failure mode of a carry-forward tool;
    PwC does not discuss it in the source.
  human_checkpoints:
  - Auditors review and complete the populated planning document (inferred from the description of the document
    as a 'foundation'; PWC-AT-2025)
  role_evolution: Auditors are expected to ask better questions because they see what changed (PWC-AT-2025).
  evidence_grade: B
  sources:
  - ref: PWC-AT-2025
    title: PwC expects end-to-end AI audit automation within 2026
    publisher: Accounting Today
    type: press
    url: https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026
    date: '2025-10-28'
    access: full
    locator: Paragraph on Simplified Audit for Private Business
  - ref: WK-SAS145-2024
    title: 'SAS 145 risk assessment: How technology strengthens audit quality'
    publisher: Wolters Kluwer
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/auditing-reimagined-sas-145-and-the-rise-of-technology-enabled-risk-management
    date: '2024-03-19'
    access: full
    locator: SAS 145 section on documenting the risk assessment
  last_reviewed: '2026-10-16'
  notes: Panson said this was the first year PwC auditors used the tool in planning (PWC-AT-2025, Oct 2025). The
    human-review checkpoint is inferred from the word 'foundation' and is not stated in the source. No measurements.
- id: assurance-planning-risk-assessment-04
  archetype: assurance
  module: planning-risk-assessment
  title: Walkthrough assistant that builds a tailored work plan and process documentation from prior-year and current-year
    material
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Documenting walkthroughs and controls has traditionally been one of the more tedious parts of the audit,
    according to PwC's Jennifer Kosar (PWC-AT-2025).
  solution: PwC's Advanced Walkthrough Assistant takes in prior-year walkthroughs and current-year documentation,
    then produces a tailored work plan, flags what is missing or changed since last year, captures key documentation
    of controls and risk, and generates documentation for review (PWC-AT-2025). In October 2026 PwC listed it among
    tools for 2026 year-end audits, describing it as documenting business processes to help auditors prepare for
    discussions (CFODIVE-PWC-2026).
  outcomes:
  - lever: speed
    description: No figure published. Kosar's comment is qualitative.
    figure: none published
    measures: no figure given
    provenance: self-reported
    source_ref: PWC-AT-2025
  prerequisites:
  - Prior-year walkthrough files and current-year process documentation in readable form (PWC-AT-2025)
  risks_and_guardrails:
  - The sources describe no tool-specific guardrails. PwC says in general that AI systems need significant expertise
    to build, test and monitor over time (CFOBREW-PWC-2025).
  human_checkpoints:
  - Documentation is generated 'for review' by the audit team (PWC-AT-2025)
  role_evolution: PwC says it is hiring engineers it would not have hired into assurance before, and wants more
    dual-track staff who can serve both roles (CFOBREW-PWC-2025).
  evidence_grade: B
  sources:
  - ref: PWC-AT-2025
    title: PwC expects end-to-end AI audit automation within 2026
    publisher: Accounting Today
    type: press
    url: https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026
    date: '2025-10-28'
    access: full
    locator: Paragraph on Advanced Walkthrough Assistant
  - ref: CFODIVE-PWC-2026
    title: PwC exec ushers in AI-assisted audits, awaits bigger time savings
    publisher: CFO Dive
    type: press
    url: https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/
    date: '2026-10-07'
    access: full
    locator: Paragraph listing tools for 2026 year-end audits
  - ref: CFOBREW-PWC-2025
    title: A look at PwC's 'next generation' audit
    publisher: CFO Brew
    type: press
    url: https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit
    date: '2025-11-05'
    access: full
    locator: Roundtable remarks on skills and hiring
  last_reviewed: '2026-10-16'
  notes: Straddles planning (understanding processes for risk assessment) and controls-testing (walkthroughs). Listed
    here because it is an input to risk assessment; the controls-testing module may also hold it.
- id: assurance-planning-risk-assessment-05
  archetype: assurance
  module: planning-risk-assessment
  title: Analysis of audit committee communications to surface issues earlier in audit preparation (PwC)
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Issues raised in audit committee communications can reach the audit team late in the preparation cycle
    (CFODIVE-PWC-2026).
  solution: PwC says a tool analyses audit committee communications to surface issues that need handling sooner
    in the audit preparation cycle, as one of the AI uses for 2026 year-end audits (CFODIVE-PWC-2026).
  outcomes:
  - lever: speed
    description: No figure published.
    figure: none published
    measures: no figure given
    source_ref: CFODIVE-PWC-2026
  prerequisites:
  - Access to audit committee papers and communications in digital form (inferred)
  risks_and_guardrails:
  - No guardrails described for this tool in the source. PwC's general position is that the final audit product
    and regulatory obligations are unchanged (CFODIVE-PWC-2026).
  human_checkpoints:
  - Not described in the source
  role_evolution: Not described in the source.
  evidence_grade: C
  sources:
  - ref: CFODIVE-PWC-2026
    title: PwC exec ushers in AI-assisted audits, awaits bigger time savings
    publisher: CFO Dive
    type: press
    url: https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/
    date: '2026-10-07'
    access: full
    locator: Paragraph listing tools for 2026 year-end audits
  last_reviewed: '2026-10-16'
  notes: One sentence in one trade article. 'Will be using AI' is a plan, not evidence of use. Also relevant to
    completion-reporting.
- id: assurance-planning-risk-assessment-06
  archetype: assurance
  module: planning-risk-assessment
  title: AI-assisted risk assessment tool to support scoping decisions (PwC, announced)
  function: service-delivery
  work_types:
  - expert-judgment
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Deciding what is and is not in scope of the audit rests on the risk assessment (PWC-AT-2025).
  solution: In October 2025 PwC's Shawn Panson said the firm planned to 'soon' have a risk-assessment tool to help
    people make smarter decisions about what is scoped into the audit (PWC-AT-2025). The October 2026 follow-up
    article did not mention this tool (CFODIVE-PWC-2026).
  outcomes:
  - lever: quality
    description: No outcome published.
    figure: none published
    measures: no figure given
    source_ref: PWC-AT-2025
  prerequisites:
  - Not described
  risks_and_guardrails:
  - Not described. See the module notes for regulators' general expectations.
  human_checkpoints:
  - The tool 'helps people make decisions', so a person decides scope (PWC-AT-2025)
  role_evolution: Not described in the source.
  evidence_grade: C
  sources:
  - ref: PWC-AT-2025
    title: PwC expects end-to-end AI audit automation within 2026
    publisher: Accounting Today
    type: press
    url: https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026
    date: '2025-10-28'
    access: full
    locator: Paragraph on the planned risk-assessment tool
  - ref: CFODIVE-PWC-2026
    title: PwC exec ushers in AI-assisted audits, awaits bigger time savings
    publisher: CFO Dive
    type: press
    url: https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/
    date: '2026-10-07'
    access: full
    locator: Absence of the tool in the Oct 2026 list
  last_reviewed: '2026-10-16'
  notes: 'Forward-looking statement from Oct 2025. Status a year later is unknown: the Oct 2026 article neither
    confirms nor withdraws it. Interview probe.'
- id: assurance-planning-risk-assessment-07
  archetype: assurance
  module: planning-risk-assessment
  title: AI agents assess risk and design audit plans and workflows on an AI-native platform (PwC Australia pilot)
  function: service-delivery
  work_types:
  - expert-judgment
  - coordination-scheduling
  - data-reporting
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: Auditors spend time on data gathering and documentation before they reach analysis (PWCAU-2025).
  solution: PwC Australia's assurance leader Sue Horlin said an 'AI-native' platform will have AI agents assess
    risk, design audit plans and workflows, and test balances and controls, with auditors in the loop for context,
    analysis and decisions. She said it works in real time on full populations, including against trusted third-party
    data (PWCAU-2025).
  outcomes:
  - lever: capacity
    description: 'PwC says the platform lets its 1,600 Australian auditors spend less time on data gathering and
      documentation and more on analysis. No measurement published. Pilot scale: five Australian audit clients at
      first, with a plan to cover all audit clients by 2028.'
    figure: 5 clients initially; all audit clients planned by 2028
    measures: number of audit clients in the initial pilot, and the stated roll-out plan
    provenance: self-reported
    source_ref: PWCAU-2025
  prerequisites:
  - Real-time, full-population client data access (PWCAU-2025)
  - Trusted third-party data sources (PWCAU-2025)
  risks_and_guardrails:
  - RSM audit partner Matthew Beevers (commenting on AI in audit generally, not on this platform) warned that over-reliance
    on AI over professional judgement could introduce errors and poorer audit quality, and raise data security and
    client confidentiality risks (PWCAU-2025)
  - PwC says its systems are designed for accuracy, transparency and accountability with human oversight and validation
    (PWCAU-2025)
  human_checkpoints:
  - Human auditors keep context, communication and final judgments (PWCAU-2025)
  role_evolution: PwC Australia says auditors move from data gathering and documentation toward insight and analysis
    (PWCAU-2025).
  evidence_grade: B
  sources:
  - ref: PWCAU-2025
    title: PwC Australia rolls out pilot program for AI-assisted full audits
    publisher: Accounting Times
    type: press
    url: https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits
    date: '2025-10-27'
    access: full
    locator: Paragraphs quoting Sue Horlin on agents, pilot scope and 2028 roll-out
  last_reviewed: '2026-10-16'
  notes: Strongest named planning-stage agent deployment found. It is a pilot, announced 27 Oct 2025, with no published
    quality or time measurement. Whether the agents' risk assessments are reviewed against a human baseline is not
    stated. Note the article's wording 'global pilot program'.
- id: assurance-planning-risk-assessment-08
  archetype: assurance
  module: planning-risk-assessment
  title: Big Four platform agents that identify potential risk factors during audit planning (EY, Deloitte, KPMG)
  function: service-delivery
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: research-brief
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Risk identification depends on what the team can read and analyse in the time available; firms say agents
    can widen what is considered (EY-CANVAS-2026; CPAPA-DELOITTE-2026).
  solution: EY says it has embedded agentic AI in all phases of the audit on EY Canvas, will tailor workflows to
    engagements and expects end-to-end support by 2028 (EY-CANVAS-2026). Deloitte says Omnia's agent network can
    analyse information to identify potential risk factors (CPAPA-DELOITTE-2026). KPMG said in July 2024 that GenAI
    in KPMG Clara interacts with engagement documentation and methodology and helps teams refine risk assessments
    (KPMG-CLARA-2025).
  outcomes:
  - lever: quality
    description: No outcome published for risk identification. EY states the deployment covers 130,000 assurance
      professionals and 160,000 audit engagements in 150-plus countries.
    figure: none published
    measures: EY's stated number of assurance professionals, audit engagements and countries covered; not an outcome
      measure
    provenance: self-reported
    source_ref: EY-CANVAS-2026
  prerequisites:
  - Firm-wide platform and data foundation (EY with Microsoft; Deloitte's own engineering teams) (EY-CANVAS-2026;
    CPAPA-DELOITTE-2026)
  - 'Training: EY describes a global programme to upskill audit and technology risk professionals (EY-CANVAS-2026)'
  risks_and_guardrails:
  - EY says human judgment, skepticism and insight remain fundamental (EY-CANVAS-2026)
  - Deloitte says its AI capabilities follow its Trustworthy AI framework (CPAPA-DELOITTE-2026)
  - KPMG says it maintains a high level of professional skepticism while deploying agents (KPMG-CLARA-2025)
  human_checkpoints:
  - Not specified for risk identification in these sources
  role_evolution: EY says it will train all global audit and technology risk professionals this year (EY-CANVAS-2026).
    Deloitte says the agents give its nearly 85,000 audit and assurance practitioners deeper risk analysis (CPAPA-DELOITTE-2026).
  evidence_grade: C
  sources:
  - ref: EY-CANVAS-2026
    title: EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/
    date: '2026-04-07'
    access: full
    locator: Paragraphs on 'all phases', 2028 and risk assessments
  - ref: CPAPA-DELOITTE-2026
    title: Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia to Advance Audit and Assurance
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/06/24/deloitte-unveils-connected-agentic-intelligence-in-deloitte-omnia-to-advance-audit-assurance/185652/
    date: '2026-06-24'
    access: full
    locator: List of what Omnia agents can do
  - ref: KPMG-CLARA-2025
    title: KPMG advances AI integration in KPMG Clara smart audit platform
    publisher: KPMG
    type: firm
    url: https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html
    date: 2025-04
    access: full
    locator: Text on GenAI in Clara from July 2024
  last_reviewed: '2026-10-16'
  notes: 'Firm announcements through trade press. The risk-identification claim is one phrase in each. KPMG''s July
    2024 item is outside the 18-month window and is kept as the earliest firm statement. Treat ''embedded in all
    phases'' (EY) and ''by 2028'' (EY) as distinct tenses: now versus expected.'
- id: assurance-planning-risk-assessment-09
  archetype: assurance
  module: planning-risk-assessment
  title: Evidence-linked agentic risk assessment tied to assertions, materiality and methodology (MindBridge)
  function: service-delivery
  work_types:
  - review-assurance
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Planning decisions need to be supported by evidence and aligned with methodology; MindBridge says ARA
    makes them 'faster, better supported and more defensible' (MINDBRIDGE-ARA-2026).
  solution: MindBridge's Agentic Risk Assessment connects evidence, analytics, assertions, materiality and methodology.
    It is designed to plug into customer-built and third-party workpaper tools and agentic workflows. A separate
    MCP server lets users query MindBridge results from compatible AI assistants (MINDBRIDGE-ARA-2026).
  outcomes:
  - lever: quality
    description: Vendor claim of faster, better supported, more defensible planning decisions. No figure and no
      named customer.
    figure: none published
    measures: no figure given
    provenance: vendor-published
    source_ref: MINDBRIDGE-ARA-2026
  prerequisites:
  - Transaction and ledger data loaded into MindBridge
  - Firm methodology configured so assertions and materiality can be mapped (inferred from the feature description)
  risks_and_guardrails:
  - Vendor says the capability preserves auditor judgment and control (MINDBRIDGE-ARA-2026)
  - Practitioner warning that models can name ISA risks without separating financial-statement-level from assertion-level
    risk (ICAEW-PIERPOINT-2025)
  human_checkpoints:
  - Auditor retains judgment and control (MINDBRIDGE-ARA-2026)
  role_evolution: Not described in the source.
  evidence_grade: C
  sources:
  - ref: MINDBRIDGE-ARA-2026
    title: MindBridge Advances Financial Oversight for the Agentic Era with New Platform Capabilities (press release)
    publisher: MindBridge
    type: vendor
    url: https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/
    date: '2026-09-22'
    access: full
    locator: Item 'Agentic Risk Assessment for audit & assurance'
  - ref: ICAEW-PIERPOINT-2025
    title: 'Testing Gen AI platforms: can they do audit work? (Helen Pierpoint)'
    publisher: ICAEW
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work
    date: '2025-09-24'
    access: full
    locator: Findings on risk assessment
  last_reviewed: '2026-10-16'
  notes: Press release of 22 Sep 2026. Unlike the finance products in the same release, the ARA item is not described
    as a preview, but no customers or availability dates are given.
- id: assurance-planning-risk-assessment-10
  archetype: assurance
  module: planning-risk-assessment
  title: Full-population analytics run at the start of the engagement to inform risk assessment (Wolters Kluwer
    CCH Axcess Engagement)
  function: service-delivery
  work_types:
  - data-reporting
  - review-assurance
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Planning often starts from a trial balance, a few comparative schedules, last year's file and judgment,
    with limited analytics. Anomalies may not surface until substantive testing, when they cost more (WK-AGENTRA-2026).
  solution: Embedded analytics give full-population views of journal entries (for example round-dollar, late-period
    or unusual account-combination entries), trend and ratio analysis, and subledger analysis (being expanded) early
    in the engagement. Wolters Kluwer says these are not agentic themselves but give structured signals that agents
    can use later (WK-AGENTRA-2026).
  outcomes:
  - lever: quality
    description: Vendor claim that earlier visibility improves risk assessment and procedure design. No figure.
    figure: none published
    measures: no figure given
    provenance: vendor-published
    source_ref: WK-AGENTRA-2026
  prerequisites:
  - Client ledger and subledger data available at planning time
  - Staff able to interpret analytics output; the same vendor says analytics only help if data is reliable and auditors
    apply skepticism (WK-SAS145-2024)
  risks_and_guardrails:
  - Wolters Kluwer says technology does not make the risk assessment; value depends on reliable data, analysis,
    skepticism and judgment (WK-SAS145-2024)
  - The same vendor says AI is a poor fit for precise calculations and repeatable procedures on structured data,
    and cites hallucination, variability and opacity as audit risks (WK-AIDATA-2026)
  human_checkpoints:
  - Auditor decides what the pattern means and how it affects the risk assessment (WK-SAS145-2024)
  role_evolution: Auditors start planning with a more complete data picture and spend time interpreting it (WK-AGENTRA-2026).
  evidence_grade: C
  sources:
  - ref: WK-AGENTRA-2026
    title: The evolving role of agentic risk assessment in audit planning
    publisher: Wolters Kluwer
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/the-evolving-role-of-agentic-risk-assessment-in-audit-planning
    date: '2026-03-02'
    access: full
    locator: Section on data analytics in CCH Axcess Engagement
  - ref: WK-SAS145-2024
    title: 'SAS 145 risk assessment: How technology strengthens audit quality'
    publisher: Wolters Kluwer
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/auditing-reimagined-sas-145-and-the-rise-of-technology-enabled-risk-management
    date: '2024-03-19'
    access: full
    locator: Text on technology and risk assessment
  - ref: WK-AIDATA-2026
    title: 'AI in audit data analysis: Risks, limitations, and best practices'
    publisher: Wolters Kluwer (TeamMate)
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/ai-audit-data-analysis-risks-limitations-best-practices
    date: '2026-06-10'
    access: full
    locator: Key takeaways
  last_reviewed: '2026-10-16'
  notes: Vendor thought leadership, 2 Mar 2026, no named customer. IFIAR reports that 55% of responding members
    frequently observed automated tools and techniques in risk assessment in 2024, up from 49% in 2023 (IFIAR-TTF-2025,
    table of ATT use). That regulator figure (55% of the 47 members that answered) shows tools are in risk assessment
    in general; it says nothing about this product.
- id: assurance-planning-risk-assessment-11
  archetype: assurance
  module: planning-risk-assessment
  title: 'Idea: risk-assessment agent that drafts a cited risk narrative and a second agent that maps risks to procedures'
  function: service-delivery
  work_types:
  - document-production
  - expert-judgment
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: Risk narratives vary in clarity and completeness by preparer, and linking risks to procedures is manual
    (WK-AGENTRA-2026).
  solution: 'Wolters Kluwer''s future-state scenario: an analytics engine flags late-period entries, margin compression
    and receivables aging shifts. A risk-assessment agent synthesises them into a draft narrative with citations
    and evidence links. A second agent maps risks to relevant procedures or flags areas needing enhanced testing.
    The auditor reviews and refines (WK-AGENTRA-2026). The CPA Journal outlines a comparable framework where ML
    models classify inherent and control risk and GenAI turns results into documentation-ready language, with illustrative,
    uncalibrated thresholds (CPAJ-AIPLAN-2026).'
  outcomes:
  - lever: quality
    description: none published (idea)
    figure: none published
    measures: no measurement in either source
    source_ref: WK-AGENTRA-2026
  prerequisites:
  - Connected data and APIs so analytics, workpapers and documents are not in silos (WK-CONNECTED-2026)
  - Approval gates, exception logs and evidence links on every agent step (WK-CONNECTED-2026)
  - Readiness assessment of data, IT, staff skills and governance before piloting (CPAJ-AIPLAN-2026)
  risks_and_guardrails:
  - Wolters Kluwer calls agentic audits assistive, not autonomous, with human approval at each step (WK-CONNECTED-2026)
  - The CPA Journal authors list black-box outputs, biased or stale training data and over-dependence among the
    risks, and say the auditor keeps full responsibility (CPAJ-AIPLAN-2026)
  - ICAEW's test found chatbots do not separate financial-statement-level from assertion-level risk (ICAEW-PIERPOINT-2025)
  human_checkpoints:
  - Auditor reviews and refines the draft narrative and the risk-to-procedure mapping (WK-AGENTRA-2026)
  role_evolution: Wolters Kluwer expects analytics to create signals, agents to interpret them and auditors to apply
    judgment and finalise conclusions (WK-AGENTRA-2026).
  evidence_grade: D
  sources:
  - ref: WK-AGENTRA-2026
    title: The evolving role of agentic risk assessment in audit planning
    publisher: Wolters Kluwer
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/the-evolving-role-of-agentic-risk-assessment-in-audit-planning
    date: '2026-03-02'
    access: full
    locator: Section on the next wave of agentic capabilities and the hypothetical scenario
  - ref: WK-CONNECTED-2026
    title: 'The connected audit: A strategic framework for agentic workflows'
    publisher: Wolters Kluwer
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/a-strategic-framework-for-agentic-audit-workflows
    date: '2026-03-02'
    access: full
    locator: Key takeaways and sections on governance and integration
  - ref: CPAJ-AIPLAN-2026
    title: Leveraging Artificial Intelligence in Audit Planning (Kasztelnik and Jermakowicz)
    publisher: The CPA Journal
    type: academic
    url: https://www.cpajournal.com/2026/08/19/leveraging-artificial-intelligence-in-audit-planning/
    date: '2026-08-19'
    access: full
    locator: Framework, Exhibits 1-3 and 'Ethical and Professional Considerations'
  - ref: ICAEW-PIERPOINT-2025
    title: 'Testing Gen AI platforms: can they do audit work? (Helen Pierpoint)'
    publisher: ICAEW
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work
    date: '2025-09-24'
    access: full
    locator: Findings on risk assessment
  last_reviewed: '2026-10-16'
  notes: 'Idea, labelled as such: a vendor describes it as a future state (''still a future-state vision''), and
    the CPA Journal piece is a conceptual framework with illustrative exhibits and no testing on real engagements.'
- id: assurance-planning-risk-assessment-12
  archetype: assurance
  module: planning-risk-assessment
  title: 'Idea: multi-agent restatement-risk scoring that fuses text, ratio and critical-audit-matter signals (UMAR
    research prototype)'
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Risk-scoring approaches usually give a point prediction without showing how far different evidence sources
    agree (ARXIV-UMAR-2026).
  solution: Three agents (MD&A text, financial ratios, critical audit matters) each give a risk score with calibrated
    uncertainty. An aggregator based on Dempster-Shafer evidence theory fuses the scores and measures conflict between
    agents. The authors say it offers auditors potentially actionable and interpretable risk signals (ARXIV-UMAR-2026).
  outcomes:
  - lever: quality
    description: Authors report the framework beat logistic regression, XGBoost, FinBERT and single- and dual-agent
      LLM baselines on restatement prediction.
    figure: AUROC 0.782; PR-AUC 0.341; expected calibration error 0.052
    measures: 3,200 US 10-K firm-year observations (2019-2023), with financial restatement as the label
    provenance: independent
    source_ref: ARXIV-UMAR-2026
  prerequisites:
  - Filing text and financial data for the entity
  - Evaluation against the firm's own risk assessments (not done in the paper)
  risks_and_guardrails:
  - Preprint, not peer reviewed, with author-run evaluation (ARXIV-UMAR-2026)
  - The label is a later restatement, not an auditor's planning judgment, so results do not show better planning
    decisions (ARXIV-UMAR-2026, abstract)
  human_checkpoints:
  - Not specified; the abstract frames outputs as signals for auditors (ARXIV-UMAR-2026)
  role_evolution: Not discussed.
  evidence_grade: D
  sources:
  - ref: ARXIV-UMAR-2026
    title: Multi-Agent Framework for Audit Risk Assessment with Explicit Uncertainty and Evidence Conflict Modeling
      (UMAR)
    publisher: arXiv (Wang et al.)
    type: academic
    url: https://arxiv.org/abs/2606.15640
    date: '2026-06-14'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-16'
  notes: Idea from a research preprint (14 Jun 2026). Included because researchers are discussing multi-agent risk
    scoring for planning. No deployment found. Provenance marked independent because the authors are not a vendor
    or deploying firm; the evaluation is still theirs.
- id: assurance-planning-risk-assessment-13
  archetype: assurance
  module: planning-risk-assessment
  title: AI-supported engagement staffing requests, budget planning and engagement-leader review (RSM Luca Resourcing)
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Staffing requests and budgets for audit engagements were handled by manual processes, limiting visibility
    into engagement planning (CAQ-RSM-2026).
  solution: RSM says Luca Resourcing replaces manual processes with a connected collaboration tool. It supports
    initial staffing requests, budget planning and engagement-leader review, and helps teams align the right resources
    to the right work at the right time. RSM presents it as a benefit of its AI investment (CAQ-RSM-2026). The CAQ
    newsletter describes it as a workforce planning tool that uses technology to align talent and engagement needs
    (CAQ-INSIDER-2026).
  outcomes:
  - lever: capacity
    description: RSM says the tool improves visibility into engagement planning and speeds staffing decisions. No
      figure.
    figure: none published
    measures: no figure given
    provenance: self-reported
    source_ref: CAQ-RSM-2026
  prerequisites:
  - Engagement and talent data in one system
  - Engagement leaders using the tool for review (CAQ-RSM-2026)
  risks_and_guardrails:
  - The source describes no tool-specific guardrails; engagement-leader review is the only control named (CAQ-RSM-2026)
  human_checkpoints:
  - Engagement-leader review of staffing and budget (CAQ-RSM-2026)
  role_evolution: RSM says leaders get better insights to make faster, more informed staffing decisions (CAQ-RSM-2026).
  evidence_grade: B
  sources:
  - ref: CAQ-RSM-2026
    title: 'Shaping the future of assurance: Advancing AI in the audit (RSM, CAQ Audit in Action blog)'
    publisher: Center for Audit Quality (blog by RSM)
    type: professional-body
    url: https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit
    date: 2026-08
    access: full
    locator: Section 'RSM Luca Resourcing'
  - ref: CAQ-INSIDER-2026
    title: Audit Insider, July/August 2026
    publisher: Center for Audit Quality
    type: professional-body
    url: https://www.thecaq.org/audit-insider-july-august-2026
    date: '2026-09-01'
    access: full
    locator: Description of RSM's three tools
  last_reviewed: '2026-10-16'
  notes: Named, live deployment (added within the past year, per RSM) with no measurement. What the AI component
    does inside the tool is not specified; RSM attributes the benefit to 'AI technology' generally.
- id: assurance-planning-risk-assessment-14
  archetype: assurance
  module: planning-risk-assessment
  title: AI efficiency gains negotiated into audit fees and engagement budgets
  function: service-delivery
  work_types:
  - coordination-scheduling
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: If firms tell clients AI cuts hours, clients may ask why fees do not fall (FINSTORY-KPMGFEE-2026).
  solution: 'Reported case: KPMG International pressed its auditor, Grant Thornton UK, for a lower fee on the argument
    that AI should lower the cost of the audit, and the fee fell (FINSTORY-KPMGFEE-2026). The same article quotes
    PwC from 2025: clients know AI saves hours and are asking for discounts. Practitioners disagree on whether higher
    quality should instead support higher fees (FINSTORY-KPMGFEE-2026).'
  outcomes:
  - lever: cost
    description: 'Reported audit fee paid by KPMG International to its auditor fell from $416,000 in 2024 to $357,000
      in 2025, about 14%. Second-hand: the article cites the Financial Times, which was not opened.'
    figure: $416,000 to $357,000
    measures: audit fee paid by KPMG International to Grant Thornton UK, per a secondary report of the FT
    provenance: independent
    source_ref: FINSTORY-KPMGFEE-2026
  prerequisites:
  - A fee and budget model that is not purely billable-hour (implied by the debate in the source)
  risks_and_guardrails:
  - The PCAOB acting chair cited an Accountancy Europe study warning that profit pressure at private-equity-backed
    firms could bring cost-cutting and aggressive fee negotiation that strain staff and judgment (ACCTODAY-BOTIC-2025)
  - AI investment itself costs firms heavily, so fee cuts and build costs pull in opposite directions (FINSTORY-KPMGFEE-2026)
  human_checkpoints:
  - Partner pricing decisions (inferred)
  role_evolution: The article raises whether the billable hour survives; it offers no firm decision (FINSTORY-KPMGFEE-2026).
  evidence_grade: C
  sources:
  - ref: FINSTORY-KPMGFEE-2026
    title: KPMG forced Auditor for a 14% AI Discount...Will the Billable Hour die?
    publisher: The Finance Story
    type: press
    url: https://thefinancestory.com/kpmg-forced-auditor-for-a-14-ai-discount-will-the-billable-hour-die
    date: '2026-02-12'
    access: full
    locator: Sections 'KPMG asked its auditor for an AI discount' and 'Paradox facing the profession'
  - ref: ACCTODAY-BOTIC-2025
    title: PCAOB warns auditors about AI and PE
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe
    date: '2025-12-09'
    access: full
    locator: Botic remarks on profitability pressure
  last_reviewed: '2026-10-16'
  notes: 'Not a tool but a change in how engagement budgets and fees are set (module scope: budgeting). The landscape
    could not confirm these fee figures on the Verdantix page; this article states them but cites the FT. Treat
    as unconfirmed. Also touches acceptance-independence (client-auditor pricing pressure).'
- id: assurance-planning-risk-assessment-15
  archetype: assurance
  module: planning-risk-assessment
  title: 'Idea: LLM-proposed materiality benchmark and percentage'
  function: service-delivery
  work_types:
  - expert-judgment
  - data-reporting
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Materiality needs a benchmark, a percentage and supporting rationale under ISA 320 (ICAEW-PIERPOINT-2025).
  solution: ICAEW tested three general chatbots (Copilot, Grok, Claude) on a fictional, AI-generated retailer. Claude
    chose profit before tax with a 5% factor and anchored its reasoning in ISA 320. Copilot chose revenue at 0.75%
    with a vague rationale that the author says may be a hallucination (ICAEW-PIERPOINT-2025).
  outcomes:
  - lever: quality
    description: The three models gave different benchmarks and factors for the same facts; the author concludes
      human judgement is needed to interpret and choose thresholds.
    figure: PBT at 5% (Claude); revenue at 0.75% (Copilot)
    measures: benchmark and percentage each model proposed for one fictional retailer, in a single test
    provenance: independent
    source_ref: ICAEW-PIERPOINT-2025
  prerequisites:
  - Entity financials and context; a prompt specifying format and rationale (the author had to add detail on rationale
    and output format) (ICAEW-PIERPOINT-2025)
  risks_and_guardrails:
  - Percentages were not rounded consistently; Copilot omitted considerations such as whether the entity is a public
    interest entity (ICAEW-PIERPOINT-2025)
  - Results differ by model and prompt wording, and the test predates a newer Grok release (ICAEW-PIERPOINT-2025)
  human_checkpoints:
  - Auditor interprets the output and decides the materiality thresholds (ICAEW-PIERPOINT-2025)
  role_evolution: Not discussed beyond the need for human judgement (ICAEW-PIERPOINT-2025).
  evidence_grade: D
  sources:
  - ref: ICAEW-PIERPOINT-2025
    title: 'Testing Gen AI platforms: can they do audit work? (Helen Pierpoint)'
    publisher: ICAEW
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work
    date: '2025-09-24'
    access: full
    locator: Sections on materiality and performance materiality
  last_reviewed: '2026-10-16'
  notes: 'Idea, tested once by ICAEW''s technical manager. Author''s conclusion: the case for using chatbots to
    identify risks of material misstatement or calculate materiality has not been made. Not a benchmark: one fictional
    entity, three models, no repeat runs. The article''s performance-materiality paragraph attributes a 60% figure
    to Claude and then says Claude proposed the highest percentage (75%), so per-model figures are not used here.'
- id: assurance-planning-risk-assessment-16
  archetype: assurance
  module: planning-risk-assessment
  title: Cross-entity analytics and AI to scope and assess risk in group audits
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Group audits span entities, jurisdictions and systems; assessing risk and fraud across many entities
    with large data volumes is among the hardest parts (WK-GROUP-2025).
  solution: Wolters Kluwer says automation can extract and consolidate data from many systems, connected platforms
    can give engagement teams a central view across the group, analytics can show patterns and anomalies, and AI
    can help prioritise exceptions and review unstructured documents so auditors can focus on higher-risk areas
    (WK-GROUP-2025).
  outcomes:
  - lever: quality
    description: Vendor claim of earlier risk identification and better focus on higher-risk areas. No figure.
    figure: none published
    measures: no figure given
    provenance: vendor-published
    source_ref: WK-GROUP-2025
  prerequisites:
  - Timely access to reliable data across components (WK-GROUP-2025)
  - Coordination across component teams (WK-GROUP-2025)
  risks_and_guardrails:
  - Auditors remain responsible for evaluating results and deciding responses (WK-GROUP-2025)
  human_checkpoints:
  - Group engagement team decides scoping and responses (WK-GROUP-2025)
  role_evolution: Vendor says tools let auditors spend more time on analysis, investigation and insight (WK-GROUP-2025).
  evidence_grade: C
  sources:
  - ref: WK-GROUP-2025
    title: 'The future of group audits: How AI and technology are transforming audit quality'
    publisher: Wolters Kluwer
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/group-audits-embracing-technology-and-adapting-to-change
    date: '2025-04-03'
    access: full
    locator: Sections on data management and on assessing risk and detecting fraud across entities
  last_reviewed: '2026-10-16'
  notes: Generic vendor content; no component-scoping method is described, no customer is named. No other source
    found on AI-assisted group scoping, so this is the thinnest entry in the set.
- id: assurance-planning-risk-assessment-17
  archetype: assurance
  module: planning-risk-assessment
  title: 'Idea: fraud risk assessment and brainstorming extended to AI-enabled fraud, including deepfakes and fabricated
    documents'
  function: risk-compliance-legal
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: 'Internal audit leaders see AI-enabled fraud as a rising risk but feel unready: in a survey of 373 senior
    leaders, 85% rated it a moderate to high risk and 62% (n=372) said their function was unprepared or minimally
    prepared to detect it (IIAF-AIFRAUD-2026, executive summary and Figure 7).'
  solution: Auditors would add AI-enabled fraud (deepfake impersonation in wire authorisations, fabricated invoices,
    attempts to deceive auditors in confirmation procedures) to fraud risk factors and brainstorming, and use AI
    themselves to build the skills needed to spot misuse. The Anti-Fraud Collaboration, of which the CAQ is a member,
    had published a deepfake resource by April 2026 (CAQ-INSIDERAPR-2026; IIAF-AIFRAUD-2026).
  outcomes:
  - lever: risk
    description: 'none published (idea): no deployed method or detection result found'
    figure: none published
    measures: no measurement of detection or of changed procedures
    source_ref: IIAF-AIFRAUD-2026
  prerequisites:
  - Updated fraud risk factor lists and brainstorming agendas
  - 'Tools and skills: respondents cited lack of tools (57%) and skills (55%) as the biggest obstacles (IIAF-AIFRAUD-2026,
    Figure 7 text)'
  risks_and_guardrails:
  - Concern centres on visible threats such as phishing; synthetic identity fraud is less widely recognised (IIAF-AIFRAUD-2026,
    executive summary)
  - IFIAR says auditors should be alert to deliberate misuse of AI within audited entities, including manipulated
    data and documents (IFIAR-TTF-2026, section on advanced technologies in financial reporting)
  human_checkpoints:
  - Engagement team's fraud brainstorming and partner challenge (inferred from ordinary practice, not stated in
    these sources)
  role_evolution: Respondents asked for continuous training and closer work with technology, cyber and risk teams
    (IIAF-AIFRAUD-2026, priority actions).
  evidence_grade: D
  sources:
  - ref: IIAF-AIFRAUD-2026
    title: Internal Audit and AI-Enabled Fraud (survey report)
    publisher: IIA Internal Audit Foundation with Optro
    type: survey
    url: https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf
    date: '2026'
    access: full
    locator: Executive summary; Figure 7 text; priority actions
  - ref: CAQ-INSIDERAPR-2026
    title: Audit Insider, April 2026
    publisher: Center for Audit Quality
    type: professional-body
    url: https://www.thecaq.org/audit-insider-april-2026
    date: 2026-04
    access: full
    locator: 'Item ''Fraud and Emerging Tech: The Deepfake Threat'''
  - ref: IFIAR-TTF-2026
    title: 'Use of technology in audits: Innovation and audit quality'
    publisher: IFIAR Technology Task Force
    type: regulator
    url: https://www.ifiar.org/latest-news/ifiar-releases-2026-report-on-the-use-of-technology-in-audits/
    date: '2026-04-20'
    access: full
    locator: Section 'The Use of Advanced Technologies in the Financial Reporting Process'
  last_reviewed: '2026-10-16'
  notes: Idea. The survey is of internal audit leaders (mostly in-house), not external audit teams. No source describes
    AI used inside a fraud brainstorming session; that step has no public discourse found.
- id: assurance-planning-risk-assessment-18
  archetype: assurance
  module: planning-risk-assessment
  title: 'Idea: understanding the entity''s own use of AI in financial reporting as a standard risk assessment procedure'
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: intake-triage
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Clients are adopting AI faster than they govern it. Audit partners rated only 6% of their largest clients'
    AI governance as advanced, and nearly 90% as developing or early stage (CAQ-INSIDER-2026, Spring 2026 Pulse
    item).
  solution: Planning adds inquiry into how the entity uses AI in financial reporting and controls, the governance
    around it, and whether AI-generated documents feed audit evidence. The AICPA practice aid (13 Oct 2026) covers
    AI-related risks, effects on controls and audit responses, with more on assessing risk of material misstatement
    and evaluating evidence to follow (JOFA-AIPA-2026). SEC accounting staff say they ask auditors what they see
    at clients (KPMG-HOHL-2026).
  outcomes:
  - lever: risk
    description: 'none published (idea): no firm has published results of this procedure'
    figure: none published
    measures: no measurement
    source_ref: JOFA-AIPA-2026
  prerequisites:
  - Auditors able to evaluate AI governance and agent oversight; the CAQ says the EY survey's agentic findings are
    ones to put in front of an engagement team (CAQ-INSIDERSEP-2026)
  - Entity access to documentation of its AI systems and governance
  risks_and_guardrails:
  - 'EY''s survey of 202 senior AI decision-makers at public companies with $1bn or more revenue: 47% bypassed AI
    governance for urgent deployments and 36% reported an AI incident with material impact (CAQ-INSIDERSEP-2026)'
  - Among organisations using agentic AI in that survey, 85% said agents act without real-time human oversight and
    26% said they cannot detect unauthorised agents (CAQ-INSIDERSEP-2026)
  - IFIAR says AI-generated source documents may be used as evidence and that auditors need to understand how advanced
    technologies are used across the organisation (IFIAR-TTF-2026)
  human_checkpoints:
  - Engagement partner and team decide how the entity's AI affects risk of material misstatement (JOFA-AIPA-2026)
  role_evolution: At the Dec 2025 conference SEC accounting staff said existing auditing standards were not written
    with today's technology or AI in mind, and, on preparers' AI governance, that the foundations of risk assessment
    remain the same even if AI needs different responses (DART-SECPCAOB-2025, 'Emerging issues').
  evidence_grade: D
  sources:
  - ref: JOFA-AIPA-2026
    title: 'AI and the audit: AICPA publishes practice aid to assist auditors'
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/
    date: '2026-10-13'
    access: full
    locator: Whole article
  - ref: CAQ-INSIDER-2026
    title: Audit Insider, July/August 2026
    publisher: Center for Audit Quality
    type: professional-body
    url: https://www.thecaq.org/audit-insider-july-august-2026
    date: '2026-09-01'
    access: full
    locator: Item on Spring 2026 Audit Partner Pulse
  - ref: CAQ-INSIDERSEP-2026
    title: Audit Insider, September 2026
    publisher: Center for Audit Quality
    type: professional-body
    url: https://www.thecaq.org/audit-insider-september-2026
    date: 2026-09
    access: full
    locator: Item 'EY Survey Finds Autonomous AI Outpacing Oversight'
  - ref: KPMG-HOHL-2026
    title: Q&A with Kurt Hohl, SEC Chief Accountant (Women Corporate Directors peer exchange)
    publisher: KPMG Board Leadership Center
    type: firm
    url: https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html
    date: '2026-05-27'
    access: full
    locator: Answer on AI and auditors
  - ref: IFIAR-TTF-2026
    title: 'Use of technology in audits: Innovation and audit quality'
    publisher: IFIAR Technology Task Force
    type: regulator
    url: https://www.ifiar.org/latest-news/ifiar-releases-2026-report-on-the-use-of-technology-in-audits/
    date: '2026-04-20'
    access: full
    locator: Section on advanced technologies in the financial reporting process
  - ref: DART-SECPCAOB-2025
    title: 'AICPA & CIMA Conference on Current SEC and PCAOB Developments: key takeaways (Heads Up)'
    publisher: Deloitte DART
    type: firm
    url: https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways
    date: '2025-12-12'
    access: full
    locator: Section 'Emerging issues'
  last_reviewed: '2026-10-16'
  notes: 'Idea in the sense that no named firm reports performing and measuring it; guidance does exist. The practice
    aid''s own text was not opened (only the JofA summary). Survey denominators: CAQ Pulse figures are partner ratings
    of their largest client; EY figures are respondent organisations, and the agentic percentages apply to the subset
    using agentic AI.'
- id: assurance-planning-risk-assessment-19
  archetype: assurance
  module: planning-risk-assessment
  title: Agentic risk-assessment scoring for internal audit planning and prioritisation (Optro)
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Scoring risk across the audit universe takes manual analysis and can be inconsistent (OPTRO-AGENTS-2026).
  solution: Optro's Agentic Risk Assessment Scoring analyses selected Optro data and recommends starting scores
    with supporting evidence, which Optro says gives a faster, more consistent view of risk for planning and prioritisation
    (OPTRO-AGENTS-2026).
  outcomes:
  - lever: speed
    description: Vendor claim that audit teams spend less time on manual analysis. No figure.
    figure: none published
    measures: no figure given
    provenance: vendor-published
    source_ref: OPTRO-AGENTS-2026
  prerequisites:
  - Audit universe and risk data held in the Optro platform (OPTRO-AGENTS-2026)
  - Structured audit data; FJ Management says AI works better with structured fields (OPTRO-FJ-2026)
  risks_and_guardrails:
  - Agents recommend 'starting' scores, which implies the audit team sets final scores (OPTRO-AGENTS-2026, inferred)
  - Chambers warns about 'agent washing', where basic AI features are rebranded as agents, and says to demand evidence
    such as live demos on new inputs (AUDITBOARD-AGENTICERA-2026)
  human_checkpoints:
  - Audit team reviews scores and evidence before the plan is set (inferred from 'starting scores')
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: OPTRO-AGENTS-2026
    title: Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance
    publisher: Optro
    type: vendor
    url: https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance
    date: '2026-10-14'
    access: full
    locator: Product list, 'Agentic Risk Assessment Scoring'
  - ref: AUDITBOARD-AGENTICERA-2026
    title: 'The agentic audit era: What CAEs must rethink now (Richard Chambers)'
    publisher: AuditBoard (now Optro)
    type: vendor
    url: https://auditboard.com/blog/agentic-audit-era-what-caes-must-rethink
    date: '2026-08-12'
    access: full
    locator: Section on agent washing
  - ref: OPTRO-FJ-2026
    title: FJ Management advances its agentic audit strategy with Optro (customer story)
    publisher: Optro
    type: vendor
    url: https://auditboard.com/blog/fj-management-success-story
    date: '2026-09-22'
    access: full
    locator: Section on structured data
  last_reviewed: '2026-10-16'
  notes: Launched 14 Oct 2026, two days before this run. Internal audit, not external audit. No customer results.
- id: assurance-planning-risk-assessment-20
  archetype: assurance
  module: planning-risk-assessment
  title: 'Dynamic internal audit planning: continuous risk assessment, continuous scoping and micro audits triggered
    by live signals'
  function: service-delivery
  work_types:
  - coordination-scheduling
  - expert-judgment
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: Annual plans age quickly. Only 9% of CAEs reported adequate audit coverage for digital disruption, and
    23% rated their risk governance maturity for it as managed or optimised (AUDITBOARD-RIF-2026, section 4, summarising
    the Risk in Focus North America 2026/2027 report).
  solution: Internal audit keeps a living risk register, holds more frequent risk reviews and updates the plan as
    risks move (AUDITBOARD-RTRA-2025). Deloitte describes functions experimenting with AI for continuous auditing,
    anomaly detection and dynamic planning, and agents scanning internal and external data for emerging risks to
    trigger adaptive responses, with 'continuous scoping' as a method (GRCREPORT-DELOITTE-2026). Wolters Kluwer
    adds AI risk scoring, reserved surge capacity for micro audits and a rolling multi-year plan, and notes IIA
    Standard 9.4 requires plans based on ongoing risk assessment (WK-DYNAMIC-2026; WK-MICRO-2026; WK-MULTIYEAR-2026).
  outcomes:
  - lever: risk
    description: No measured outcome. Consultancy and vendor descriptions only.
    figure: none published
    measures: no figure given
    provenance: vendor-published
    source_ref: WK-DYNAMIC-2026
  prerequisites:
  - Data feeds and KRIs for the main risks (AUDITBOARD-RTRA-2025)
  - Flexible resourcing and board approval of significant plan changes under the IIA Standards (WK-MULTIYEAR-2026)
  - Governance for the agents themselves (GRCREPORT-DELOITTE-2026)
  risks_and_guardrails:
  - AuditBoard says automation is a tool and skepticism must stay central (AUDITBOARD-RTRA-2025)
  - Deloitte stresses transparency, accountability and ethical use in AI governance for audit (GRCREPORT-DELOITTE-2026)
  - Wolters Kluwer says automation helps with repeated calculations but cannot judge an acquisition's risk or the
    right time to review a process (WK-MULTIYEAR-2026)
  human_checkpoints:
  - CAE and board approve significant changes to the approved plan (WK-MULTIYEAR-2026)
  role_evolution: Deloitte recommends rotational staffing, co-sourcing and digital specialists to close capability
    gaps (GRCREPORT-DELOITTE-2026). Chambers says AI is central to solving the coverage problems it helps create
    (AUDITBOARD-RIF-2026).
  evidence_grade: C
  sources:
  - ref: AUDITBOARD-RTRA-2025
    title: 'Embracing real-time risk assessment: A practitioner''s guide for internal audit teams in 2026'
    publisher: AuditBoard (now Optro)
    type: vendor
    url: https://auditboard.com/blog/embracing-real-time-risk-assessment-a-practitioners-guide-for-internal-audit-teams-in-2026
    date: '2025-09-04'
    access: full
    locator: Practical steps section
  - ref: GRCREPORT-DELOITTE-2026
    title: Deloitte Sees Internal Audit Moving Closer to the Center of Enterprise Risk in 2026
    publisher: GRC Report
    type: press
    url: https://www.grcreport.com/post/deloitte-sees-internal-audit-moving-closer-to-the-center-of-enterprise-risk-in-2026
    date: '2026-05-19'
    access: full
    locator: Paragraphs on continuous scoping and agentic AI
  - ref: WK-DYNAMIC-2026
    title: 'Static to strategic: unlocking the benefits of dynamic audit planning'
    publisher: Wolters Kluwer (TeamMate)
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/static-strategic-unlocking-benefits-dynamic-audit-planning
    date: '2026-09-23'
    access: full
    locator: Key takeaways
  - ref: WK-MICRO-2026
    title: 'Real-time risk intelligence: How micro audits are redefining internal audit'
    publisher: Wolters Kluwer (TeamMate)
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/risk-intelligence-micro-audits-redefining-internal-audit
    date: '2026-07-29'
    access: full
    locator: Key takeaways
  - ref: WK-MULTIYEAR-2026
    title: 'Multi-year audit planning: Keeping an eye on tomorrow''s risks'
    publisher: Wolters Kluwer (TeamMate)
    type: vendor
    url: https://wolterskluwer.com/en/expert-insights/multi-year-audit-planning
    date: '2026-10-14'
    access: full
    locator: Opening and assumptions sections
  - ref: AUDITBOARD-RIF-2026
    title: 'Converging risks, competing priorities: Top takeaways from Risk in Focus, North America 2026/2027 (Richard
      Chambers)'
    publisher: AuditBoard (now Optro)
    type: vendor
    url: https://auditboard.com/blog/top-takeaways-from-risk-in-focus-north-america-2026-2027
    date: '2026-09-15'
    access: full
    locator: Section 4 and closing sections
  last_reviewed: '2026-10-16'
  notes: Mostly vendor and consultancy framing. The Deloitte item is a secondary summary (GRC Report, 19 May 2026).
    PwC's internal audit outlook describes agents sensing risks with plans flexing daily, but that page returned
    403 and was seen only in a search extract, so it is not used as evidence.
- id: assurance-planning-risk-assessment-21
  archetype: assurance
  module: planning-risk-assessment
  title: Continuous, year-round external audit with risk assessment updated as client data flows in
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: Year-end audit rush leaves planning and risk assessment as a point-in-time exercise (TR-CHALLENGES-2026).
  solution: Thomson Reuters says client transactions flow continuously into AI-driven engines, which flag issues
    as they occur and give earlier risk identification (TR-CHALLENGES-2026). The CPA Journal authors expect AI-driven
    continuous auditing to update risk assessments dynamically during the period, if data integrity, exception thresholds
    and intervention protocols are in place (CPAJ-AIPLAN-2026). PwC Australia says its platform works in real time
    on full populations (PWCAU-2025). Rutgers' WCARS programmes track the research (WCARS-2025; WCARS70-2026).
  outcomes:
  - lever: speed
    description: Thomson Reuters claims 80-90% complete deliverables by year-end with minimal human intervention.
      The claim is unsourced.
    figure: 80-90% complete deliverables by year-end
    measures: share of deliverables complete at year-end as stated by the vendor; no denominator, sample or method
      given
    provenance: vendor-published
    source_ref: TR-CHALLENGES-2026
  prerequisites:
  - Real-time client data feeds and system access (CPAJ-AIPLAN-2026)
  - Well-designed exception thresholds and protocols for auditor intervention (CPAJ-AIPLAN-2026)
  risks_and_guardrails:
  - Testing more data surfaces more exceptions and can widen the expectation gap if sold as certainty (CPAPA-LEDGERLINE-2026)
  - Firms should run new automation in shadow mode on completed engagements and ramp gradually (CPAPA-LEDGERLINE-2026)
  human_checkpoints:
  - Auditor intervention protocols when anomalies appear (CPAJ-AIPLAN-2026)
  role_evolution: Thomson Reuters expects auditors to turn data anomalies into risk narratives and work on judgment-heavy
    procedures (TR-CHALLENGES-2026).
  evidence_grade: C
  sources:
  - ref: TR-CHALLENGES-2026
    title: Audit challenges and changes in 2026
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/challenges-and-changes-within-the-audit-industry/
    date: '2026-02-02'
    access: full
    locator: Section 'Continuous assurance and real-time auditing'
  - ref: CPAJ-AIPLAN-2026
    title: Leveraging Artificial Intelligence in Audit Planning (Kasztelnik and Jermakowicz)
    publisher: The CPA Journal
    type: academic
    url: https://www.cpajournal.com/2026/08/19/leveraging-artificial-intelligence-in-audit-planning/
    date: '2026-08-19'
    access: full
    locator: Section 'Future Directions for AI-Enabled Auditing'
  - ref: PWCAU-2025
    title: PwC Australia rolls out pilot program for AI-assisted full audits
    publisher: Accounting Times
    type: press
    url: https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits
    date: '2025-10-27'
    access: full
    locator: Real-time claim
  - ref: CPAPA-LEDGERLINE-2026
    title: 'Testing Every Transaction Changes the Audit: Here''s What Firms Should Know Before They Sell It (Tunde
      Adewole, Ledgerline)'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/
    date: '2026-10-15'
    access: full
    locator: Sections 'The trap' and 'How to roll it out safely'
  - ref: WCARS-2025
    title: 69th World Continuous Auditing & Reporting Symposium (programme)
    publisher: Rutgers Accounting Web
    type: conference
    url: https://raw.rutgers.edu/69wcars.html
    date: '2025-11-07'
    access: full
    locator: Programme
  - ref: WCARS70-2026
    title: 70th World Continuous Auditing & Reporting Symposium, Seville (programme PDF)
    publisher: Rutgers / Universidad Pablo de Olavide
    type: conference
    url: https://raw.rutgers.edu/70wcars/70%20WCARS%20Programa_4as.pdf
    date: '2026-05-21'
    access: full
    locator: Programme
  last_reviewed: '2026-10-16'
  notes: Direction of travel, not practice. No firm describes live continuous risk assessment on external audits.
    The 'end-to-end integration by late 2026' line in the Thomson Reuters piece is a prediction with no source.
- id: assurance-planning-risk-assessment-22
  archetype: assurance
  module: planning-risk-assessment
  title: AI-drafted audit work programs and agent-planned procedures in internal audit (Helvetia Baloise, FJ Management)
  function: service-delivery
  work_types:
  - document-production
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Internal audit teams plan and execute many diverse audits with limited staff and want broader coverage
    without matching headcount growth (OPTRO-FJ-2026).
  solution: Helvetia Baloise's group chief audit executive says the team uses AI to support audit work programs,
    summarise reports and policies, and assist selected fieldwork such as anomaly identification (OPTRO-HELVETIA-2026).
    FJ Management's head of internal audit uses AI for secondary workpaper review and aims for a state where an
    auditor sets the audit objective and an agent plans procedures, pulls evidence, runs tests and drafts workpapers
    for human review (OPTRO-FJ-2026).
  outcomes:
  - lever: capacity
    description: No figure. FJ Management plans to move from reviewing selected workpapers to a secondary review
      of every workpaper.
    figure: none published
    measures: no figure given
    provenance: vendor-published
    source_ref: OPTRO-FJ-2026
  prerequisites:
  - Audit record organised as structured 'atomic units' (risks, entities, processes, controls, observations, test
    procedures) that agents can use (OPTRO-FJ-2026)
  - A GRC platform as system of record, connected to AI tools through MCP (OPTRO-FJ-2026)
  risks_and_guardrails:
  - 'FJ''s rule: AI drafts and detects, people decide (OPTRO-FJ-2026)'
  - FJ uses several models to review the same work independently and treats disagreement as a signal for the auditor
    to investigate (OPTRO-FJ-2026)
  - FJ advises starting with one high-leverage, low-risk use case (OPTRO-FJ-2026)
  human_checkpoints:
  - Auditor sets the audit objective and signs off; severity ratings, materiality calls and final sign-off stay
    with people (OPTRO-FJ-2026)
  role_evolution: FJ's head of internal audit says his focus shifted from executing procedures to designing how
    the work is done (OPTRO-FJ-2026).
  evidence_grade: B
  sources:
  - ref: OPTRO-HELVETIA-2026
    title: How Helvetia Baloise gave internal audit room to focus on risk (customer story)
    publisher: Optro
    type: vendor
    url: https://auditboard.com/blog/helvetia-baloise-success-story
    date: '2026-09-10'
    access: full
    locator: Results section, AI paragraph
  - ref: OPTRO-FJ-2026
    title: FJ Management advances its agentic audit strategy with Optro (customer story)
    publisher: Optro
    type: vendor
    url: https://auditboard.com/blog/fj-management-success-story
    date: '2026-09-22'
    access: full
    locator: Sections on audit coverage and agentic auditing
  last_reviewed: '2026-10-16'
  notes: Both are vendor-published customer stories (Sep 2026), so the claims are the customer's own words as chosen
    by the vendor. Helvetia's AI use is a brief mention; FJ's agent-planned audits are a stated vision, not a running
    system.
```

---

## 3. Module notes

### 3.1 Where the discourse was found

| Venue and date | What was said or listed | Sources | Access limit |
|---|---|---|---|
| AICPA & CIMA Conference on Current SEC and PCAOB Developments, 8-10 Dec 2025 | PCAOB acting chair Botic (9 Dec): AI can already enhance risk assessment by analysing entire populations in certain scenarios; risks to skepticism and junior skill-building. SEC accounting staff: AI governance, explainability, emerging fraud risk; existing standards were not written with AI in mind. Deloitte, RSM and BDO recaps are preparer-heavy. | ACCTODAY-BOTIC-2025; NYSSCPA-BOTIC-2025; DART-SECPCAOB-2025; RSM-SECPCAOB-2025 | Prepared remarks and recaps read; no transcript of Q&A |
| PCAOB Standards and Emerging Issues Advisory Group, 5 Nov 2025 | Botic and Board members Ho and Stein on AI: regulatory clarity, agile standard-setting, a 'human-in-the-lead' model; firms testing full populations of journal entries. | KSLAW-SEIAG-2025; CAQ-INSIDERNOV-2025 | Secondary summaries only |
| AAA Auditing Section Midyear Meeting, Excellence in Auditing Education Workshop, 15 Jan 2026 | Panel on how technology, AI in particular, is changing the audit environment (CBIZ, KPMG, PwC). Panel on how junior auditors use GenAI across phases of fieldwork, planning included (PwC, Grant Thornton, EY). CAQ staff moderated both. | AAA-MIDYEAR-2026; CAQ-INSIDERFEB-2026 | Agenda only; no session content |
| Deloitte/University of Kansas Auditing Symposium, 7-9 May 2026 | Day 2 (8 May): 'The Future of AI in Auditing' (PwC) and panel 'Artificial Intelligence in the Audit'. | KU-SYMPOSIUM-2026 | Agenda only |
| AICPA & CIMA ENGAGE, 8-11 Jun 2026 | 'Methodology for Selecting a Methodology' (8 Jun), 'The Modern Audit Practice' (9 Jun), 'AI Ethics & Oversight: What's in the Black Box?' (10 Jun); AAFCPAs and Caseware session on AI and analytics for audit quality, with limitations and skepticism. | GRF-ENGAGE-2026; AAFCPA-ENGAGE-2026 | Session blurbs only; no recap found; official agenda blocked (landscape) |
| Rutgers WCARS: 69th (7-8 Nov 2025), 70th Seville (21-22 May 2026), 75th (6-7 Nov 2026) | 69th research papers include 'Enhanced AI Risk Assessment' and 'LLM and RAG for Business Risk Analysis'; professional day included 'Supervised Agents and Auditing'. 70th: 'From Generative AI to agentic audit: the rapid evolution of tooling for continuous auditing and reporting' and a paper on humanising AI and auditor reliance. 75th theme: 'Taming the Autonomous Frontier'. | WCARS-2025; WCARS70-2026; WCARS-2026 | Programmes only |
| CAQ webinar, 26 Mar 2026 | AI in financial reporting and audit for audit committees, with an EY partner and a Marsh chief accounting officer. | CAQ-WEBINAR-2026 | Listing only; recording not viewed |
| Podcast: ICAEW Beyond Finance, 11 Nov 2025 | FRC, Grant Thornton and Deloitte guests on AI in audit: smaller-firm use cases, explainability and human oversight, third-party providers, whether off-the-shelf tools suffice. | ICAEW-POD-2025 | Show notes only |
| Podcast: Speaking of Risk and Audit, 27 Apr 2026 | Richard Chambers with KPMG's Charles King: practical AI use cases for audit planning, testing and reporting; skepticism with agentic AI. | SRA-KING-2026 | Show notes only |
| Podcast: Risk Management Show, 11 Jan 2026 | Chambers on AI readiness, governance gaps and using AI against resource limits. | RMS-CHAMBERS-2026 | Show notes only |

### 3.2 Processes and key steps (with work types)

| Step | What happens | Work types | Where AI discourse sits |
|---|---|---|---|
| Understand the entity, environment, IT and AI use | Inquiry, board minutes and documents, industry research, walkthroughs, understanding the entity's IT and AI | `research-synthesis`, `review-assurance` | Minutes summarisation (UC01), grounded copilots (UC02), walkthrough assistant (UC04), entity AI use (UC18) |
| Preliminary analytics and risk identification | Trend, ratio and journal-entry analytics; unstructured document analysis | `data-reporting` | Planning analytics (UC10), agentic risk assessment (UC08, UC09, UC11, UC12) |
| Fraud risk assessment and brainstorming | Identify fraud risk factors; team discussion | `expert-judgment` | AI-enabled fraud as a new factor (UC17); no source on AI inside the brainstorm itself |
| Materiality and performance materiality | Pick benchmark and percentage, document rationale | `expert-judgment`, `data-reporting` | Chatbot test (UC15) |
| Assess risks of material misstatement, document | Inherent and control risk at assertion level; significant risks; rationale | `expert-judgment`, `document-production` | Draft risk narratives (UC11); carry-forward risk (UC03) |
| Scoping, including group components | Decide which accounts, locations and components are in scope | `expert-judgment` | Scoping tool announced (UC06); group audits (UC16) |
| Strategy, plan, planning memo | Convert risks to procedures; planning documents | `document-production`, `coordination-scheduling` | Auto-populated planning document (UC03); agent-designed plans (UC07) |
| Budget, staffing, timeline, fee | Staffing requests, hours budget, fees | `coordination-scheduling` | Resourcing tool (UC13); fee pressure (UC14) |
| Internal audit: universe, annual and multi-year plan | Risk assessment, plan, re-planning | `expert-judgment`, `coordination-scheduling` | Scoring (UC19), dynamic planning (UC20), work programs (UC22) |

### 3.3 Common pain points

- **Planning starts from thin inputs.** Wolters Kluwer describes planning that starts from a trial balance, a few comparative schedules, last year's file and judgment, with anomalies surfacing only in substantive testing (WK-AGENTRA-2026). Vendor view.
- **Understanding the entity and documenting walkthroughs are slow.** PwC calls walkthroughs one of the more tedious parts of the audit (PWC-AT-2025).
- **Staffing and budgets run on manual processes** at least at RSM before Luca Resourcing (CAQ-RSM-2026).
- **Data access and quality** limit analytics at planning. The AICPA/CPA.com benchmark found poor client data (60%) and no access to client systems (53%) among top blockers across 54 firms; carried from the landscape (CPACOM-ATR-2025), not re-opened.
- **Annual plans age in-year.** CAEs report low coverage of the fastest-growing risks: 9% adequate coverage for digital disruption, 23% managed or optimised risk governance maturity for it (AUDITBOARD-RIF-2026, section 4).
- **Carrying forward last year's conclusions.** Wolters Kluwer says ratings must reflect current-engagement circumstances (WK-SAS145-2024).

### 3.4 Metrics and benchmarks (with what each figure counts)

- **IFIAR, 2024 member survey:** 55% of the 47 members that answered frequently observed automated tools and techniques in risk assessment (13% never, 32% infrequently). 2023: 49% of 45. For comparison, journal-entry testing 88% of 48, substantive procedures 55% of 47, controls testing 43% of 46, IT applications 39% of 44 (IFIAR-TTF-2025, table of ATT use). The 2026 report says use is continuing in journal entries, internal controls and risk assessment; its chart values were not extractable (IFIAR-TTF-2026, p.9).
- **Adoption among US firms:** 22% of 54 complete-response firms had an automated risk assessment solution (CPACOM-ATR-2025, via landscape; not re-opened).
- **Client AI governance (CAQ Spring 2026 Pulse, released 15 Jul 2026):** 6% of audit partners rated their largest client's AI governance advanced; nearly 90% said developing or early stage; AI governance topped audit committee challenges at 57% (CAQ-INSIDER-2026).
- **EY AI Governance and Risk Survey (reported Sep 2026; n=202 senior AI decision-makers at public companies with at least $1bn revenue):** 98% have a formal AI governance policy, 47% bypassed it for urgent deployments, 36% reported an AI incident with material impact; among agentic AI users, 85% say agents act without real-time human oversight and 26% cannot detect unauthorised agents (CAQ-INSIDERSEP-2026).
- **AI-enabled fraud (IIA Foundation with Optro, n=373 senior internal audit leaders):** 85% rate it a moderate to high risk; 62% (n=372) say their function is unprepared or minimally prepared; barriers: no suitable tools 57%, skills 55%, budget 46%; 83% plan to use more AI in the next year (IIAF-AIFRAUD-2026, executive summary and Figures 7 and 9 text).
- **Fraud and AI more broadly (ACFE benchmarking via CAQ):** 7% of organisations feel more than moderately prepared to detect AI-powered fraud; 16% use GenAI in anti-fraud programmes; 75% call bias a key factor in adopting AI tools but 18% test their models for it (CAQ-INSIDERMAY-2026).
- **Practitioner poll (ISACA 2026 Tech Trends Pulse, via a practitioner article):** 62% of respondents put AI and machine learning in their top three technology priorities for 2026; 41% say keeping pace with AI-driven change is their biggest professional concern. Respondent count not given in the article (CPAPA-ISACA-2025).
- **Investor view (CAQ, Mar 2026):** nearly 90% of investors say it is very important for auditors to keep integrating new technologies such as AI; the newsletter does not describe the survey sample (CAQ-INSIDERMAR-2026).
- **Chatbot test timings (ICAEW):** Copilot under 20 seconds, Grok about 1 minute 15, Claude about 3.5 minutes for the risk and materiality report on one fictional retailer. Not a quality measure (ICAEW-PIERPOINT-2025).
- **Research prototype:** AUROC 0.782, PR-AUC 0.341, ECE 0.052 on 3,200 firm-years with restatement labels (ARXIV-UMAR-2026).
- **Scale claims, not outcomes:** EY 130,000 assurance professionals, 160,000 engagements (EY-CANVAS-2026); Deloitte nearly 85,000 (CPAPA-DELOITTE-2026); PwC Australia 1,600 auditors, five pilot clients (PWCAU-2025).
- **Quality evidence:** none published for planning tools: no error rates, override rates, parallel-run results or inspection findings. The FRC says a tool need not be perfectly accurate to be certified; the tolerance depends on how much human review sits behind it (FRC-GENAI-2026, pp.45 and 47).

### 3.5 Guardrails and regulatory points

- **FRC (UK), 30 Mar 2026:** risk of deficient output, mitigated by system design, certification with testing, staff education and human review; the example expects the reviewer to read the minutes and cites automation bias (FRC-GENAI-2026, pp.43-47). ICAEW's technology faculty chair welcomed it but said automation bias gets one paragraph (on p.35) and vendor questions are thin; ICAEW's data analytics head said small firms lack the specialist teams the guidance assumes (ICAEW-FRCVIEW-2026).
- **PCAOB:** the acting chair wants a "human-in-the-lead" model with skepticism and accountability non-negotiable (KSLAW-SEIAG-2025). SEC accounting staff said existing auditing standards were not written with AI in mind (DART-SECPCAOB-2025, 'Emerging issues'). The SEC Chief Accountant says the SEC asks auditors how they use AI for audit quality and quality-control monitoring (KPMG-HOHL-2026).
- **IFIAR, Apr 2026:** firms should run a defined and improved governance system for technology; risks include weak oversight and over-reliance without challenge; entity AI can change the scope and nature of procedures (IFIAR-TTF-2026, executive summary and p.10).
- **AICPA practice aid, 13 Oct 2026:** covers entity AI use and the firm's own use, including supervision and review; guidance on risk of material misstatement and evidence is promised (JOFA-AIPA-2026).
- **Standards text:** the risk-assessment standards require separate inherent and control risk assessment, with rationale tied to the response (WK-SAS145-2024). The CPA Journal authors map AU-C 220, 230 and 500 to AI-tool use; that is their reading, not a standard-setter's (CPAJ-AIPLAN-2026).
- **Internal audit:** IIA Standard 9.4 requires plans based on ongoing risk assessment and updated for change; significant plan changes need board approval (WK-DYNAMIC-2026; WK-MULTIYEAR-2026).
- **SEC/PCAOB conference reminder:** auditors were reminded to understand and document an AI model's design and to keep human oversight of AI-driven internal controls (CAQ-INSIDERDEC-2025).
- **Practitioner controls:** approval gates, exception logs and evidence links on every agent step (WK-CONNECTED-2026); shadow-mode runs on completed engagements, then a gradual ramp (CPAPA-LEDGERLINE-2026); several models reviewing the same work with disagreement as a signal (OPTRO-FJ-2026).

### 3.6 Frontier signals (dated and sourced)

- **2025-10-27/28:** PwC says a tool for every audit step should exist in calendar 2026, with a risk-assessment tool 'soon' (PWC-AT-2025); PwC Australia announces an AI-native platform where agents assess risk and design plans, five clients first, all by 2028 (PWCAU-2025).
- **2025-12-09:** PCAOB acting chair on AI and risk assessment (ACCTODAY-BOTIC-2025).
- **2026-03-02:** Wolters Kluwer sets out an agentic risk-assessment path starting from analytics (WK-AGENTRA-2026).
- **2026-03-30:** FRC publishes generative and agentic AI guidance with the minutes example (FRC-GENAI-2026).
- **2026-04-07:** EY says agentic AI is embedded in all phases on EY Canvas, with end-to-end support expected by 2028 (EY-CANVAS-2026).
- **2026-04-20:** IFIAR's technology report says use continues in risk assessment (IFIAR-TTF-2026).
- **2026-05-19:** Deloitte's internal audit outlook (as summarised) calls agentic AI the 'mega hot topic' and promotes continuous scoping and dynamic planning (GRCREPORT-DELOITTE-2026).
- **2026-06-24:** Deloitte unifies agents in Omnia (CPAPA-DELOITTE-2026).
- **2026-09-22:** MindBridge announces Agentic Risk Assessment (MINDBRIDGE-ARA-2026).
- **2026-10-07:** PwC says AI savings are 'not that drastic yet' (CFODIVE-PWC-2026).
- **2026-10-13:** AICPA practice aid, with risk of material misstatement guidance to follow (JOFA-AIPA-2026).
- **2026-10-14:** Optro launches Agentic Risk Assessment Scoring (OPTRO-AGENTS-2026).
- **2026-11-06/07 (scheduled):** 75th WCARS on AI governance and agentic systems (WCARS-2026).
- **Direction in practitioner writing:** risk assessment moves from periodic and point-in-time to continuous, with agents interpreting analytics signals and auditors reviewing (WK-AGENTRA-2026; CPAJ-AIPLAN-2026; TR-CHALLENGES-2026).

### 3.7 Workforce and role effects

- **Junior skill-building is the loudest role worry.** Botic said AI may erode critical thinking and skepticism and that new paths will be needed for junior auditors to gain those skills (ACCTODAY-BOTIC-2025). AAA put a panel on how juniors use GenAI in planning, internal control analysis and substantive testing (AAA-MIDYEAR-2026).
- **New hires.** PwC says it is hiring engineers it would not previously have hired into assurance and wants more dual-track people (CFOBREW-PWC-2025).
- **Review becomes the core skill.** FRC training focuses on reviewing output, not prompting (FRC-GENAI-2026, p.46). ICAEW says staff need training in judgement and skepticism over AI output, not just tool mechanics (ICAEW-FRCVIEW-2026).
- **Planning shifts to review of suggested priorities** where scoring agents are used (OPTRO-AGENTS-2026; OPTRO-FJ-2026).
- **Resourcing.** Staffing and budgeting move into a connected tool with engagement-leader review (CAQ-RSM-2026). Deloitte recommends rotational staffing, co-sourcing and digital specialists for internal audit (GRCREPORT-DELOITTE-2026).
- **Fees and pricing.** Clients ask for discounts as firms advertise AI efficiency (FINSTORY-KPMGFEE-2026, quoting PwC; second-hand).

### 3.8 Objections and concerns practitioners raise

- **"Chatbots cannot do risk assessment."** They cannot add management inquiry, observation and inspection; they did not separate financial-statement from assertion level; one omitted the presumed fraud risk in revenue; materiality benchmarks varied (ICAEW-PIERPOINT-2025).
- **Automation bias.** AI output is confident even when wrong (ICAEW-FRCVIEW-2026; FRC-GENAI-2026, p.46). Botic cites studies on over-trust in agentic AI (ACCTODAY-BOTIC-2025).
- **Black boxes.** Standards require auditors to understand and justify their risk assessments (CPAJ-AIPLAN-2026).
- **Overselling certainty.** Testing everything yields more exceptions and, if marketed as "nothing can be wrong", widens the expectation gap (CPAPA-LEDGERLINE-2026).
- **Agent washing.** Chambers, citing a mid-2025 Gartner estimate, says only about 130 of thousands of vendors claiming agentic capability offered true agentic AI; the figure is as reported in his post, not checked (AUDITBOARD-AGENTICERA-2026, section 2).
- **Vendor dependence.** Most AI in audit is features added to existing products, so firms need better vendor questions (ICAEW-FRCVIEW-2026). ENGAGE ran a session on choosing a methodology vendor (GRF-ENGAGE-2026).
- **Small firms.** Guidance assumes technology and methodology teams that small firms lack (ICAEW-FRCVIEW-2026). The ICAEW podcast raised the same smaller-firm question (ICAEW-POD-2025).
- **Modest savings.** PwC concedes time savings are not yet dramatic (CFODIVE-PWC-2026); vendor claims of 80-90% complete deliverables by year-end are unsourced (TR-CHALLENGES-2026).
- **Client-side risk.** Client AI governance is immature and agentic AI often runs without real-time oversight (CAQ-INSIDER-2026; CAQ-INSIDERSEP-2026).

### 3.9 Interview probes for an advisor

1. Walk me through the last engagement's risk assessment. Which inputs did AI touch (minutes, prior-year file, analytics, entity research), and what does the reviewer do with the output? Do they re-read the source?
2. How did you certify your planning tools? What errors did testing show, what tolerance did you accept, and who recertifies when the model changes?
3. When AI flags a risk or fails to, where is it documented under your risk assessment standard, and have inspectors or quality reviewers asked about it?
4. If summaries replace reading, how do juniors still learn the entity and the business? What changed in your first-year curriculum?
5. Did AI change your hours budgets, staffing or fees on any engagement, and who kept the savings (firm, client, staff)?

---

## 4. Routed to other modules

- **substantive-testing:** full-population testing and how to sell it (CPAPA-LEDGERLINE-2026); LLM journal-entry anomaly detection beating rule-based tests (AuditCopilot, arXiv 2512.02726, abstract opened but not otherwise used); PwC 'Simplified Audit - Execute' reading supporting documents and flagging gaps, and Evidence Match for cash, receivables and payables (CFODIVE-PWC-2026; CFOBREW-PWC-2025); deepfakes used against auditors in confirmation procedures (CAQ-INSIDERAPR-2026).
- **controls-testing:** SOX agent adoption questions (CPA Practice Advisor, 18 Aug 2026; not read beyond a snippet); ISACA AAIA credential for IT auditors (CPAPA-ISACA-2025).
- **quality-management:** FRC certification, monitoring and human-review expectations (FRC-GENAI-2026); IFIAR governance expectation (IFIAR-TTF-2026); PCAOB Inspections Modernization Council and QC 1000 amendments (CAQ-INSIDER-2026; CAQ-INSIDERSEP-2026); junior-skill erosion as a supervision issue (ACCTODAY-BOTIC-2025).
- **acceptance-independence:** SEC Chief Accountant on independence rules being fit for purpose when AI is integrated into audit delivery (KPMG-HOHL-2026); private-equity and fee pressure (ACCTODAY-BOTIC-2025; FINSTORY-KPMGFEE-2026).
- **completion-reporting:** audit committee communications analysis (CFODIVE-PWC-2026); FJ Management's secondary review of every workpaper (OPTRO-FJ-2026); CAQ audit committee webinar (CAQ-WEBINAR-2026).
- **other-assurance (assurance over AI):** EY AI governance survey (CAQ-INSIDERSEP-2026); AICPA practice aid Part 1 on entity AI and controls (JOFA-AIPA-2026); EY says it offers assurance over AI diagnostics, governance and controls (EY-CANVAS-2026).
- **specialists:** none found specific to planning.

---

## 5. Sources

62 distinct sources cited, all opened (`access: full`) unless noted; none is search-only. By type: conference 8, regulator 3, professional-body 13, firm 4, vendor 16, academic 2, survey 1, press 12, podcast 3, community 0, job-posting 0. Refs follow `PUBLISHER-SHORT-YYYY`; the same document keeps the landscape's ref where one exists. Sources read but not cited in any use case or note are not listed. Items seen only in search extracts or blocked are in section 6.

| Ref | Title | Publisher | Type | URL | Date | Access | Note |
|---|---|---|---|---|---|---|---|
| AAA-MIDYEAR-2026 | Excellence in Auditing Education Workshop, AAA Auditing Section Midyear Meeting (agenda) | American Accounting Association | conference | https://aaahq.org/Meetings/2026/Auditing-Section-Midyear-Meeting/Workshop | 2026-01-15 | full | Workshop held Thursday 15 January 2026, 1:00-5:00 pm. Agenda only; no session content. |
| AAFCPA-ENGAGE-2026 | AAFCPAs Takes the Stage at AICPA ENGAGE 2026 | AAFCPAs | conference | https://aafcpa.com/2026/05/20/aafcpas-takes-the-stage-at-aicpa-engage-2026/ | 2026-05-20 | full | Session announcement; no recap. |
| CAQ-WEBINAR-2026 | AI in Financial Reporting and Audit: What Audit Committees Need to Know (webinar) | Center for Audit Quality | conference | https://www.thecaq.org/event/event-ai-in-financial-reporting-and-audit | 2026-03-26 | full | Event listing opened; recording not viewed. |
| GRF-ENGAGE-2026 | 2026 AICPA & CIMA Engage Conference (GRF session listing) | GRF CPAs & Advisors | conference | https://www.grfcpa.com/?p=9081 | 2026-06 | full | Sessions listed for 8-11 Jun 2026; page published 2025-11-17, last modified 2026-07-14. |
| KU-SYMPOSIUM-2026 | 2026 Deloitte/University of Kansas Auditing Symposium (agenda) | University of Kansas School of Business | conference | https://business.ku.edu/research-and-faculty/accounting/deloitte-ku-auditing-symposium | 2026-05-08 | full | Symposium ran 7-9 May 2026; AI sessions on Day 2 (8 May). Agenda only. |
| WCARS-2025 | 69th World Continuous Auditing & Reporting Symposium (programme) | Rutgers Accounting Web | conference | https://raw.rutgers.edu/69wcars.html | 2025-11-07 | full | Professional day 7 Nov 2025, research day 8 Nov 2025. |
| WCARS-2026 | 75th World Continuous Auditing & Reporting Symposium (page) | Rutgers Accounting Web | conference | https://raw.rutgers.edu/75wcars.html | 2026-11-06 | full | Event scheduled 6-7 Nov 2026; no session list posted on the page I opened. |
| WCARS70-2026 | 70th World Continuous Auditing & Reporting Symposium, Seville (programme PDF) | Rutgers / Universidad Pablo de Olavide | conference | https://raw.rutgers.edu/70wcars/70%20WCARS%20Programa_4as.pdf | 2026-05-21 | full | Programme dated by event, 21-22 May 2026. |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance: Risks, Mitigations and Illustrative Examples | Financial Reporting Council | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03-30 | full |  |
| IFIAR-TTF-2025 | Use of technology in audits: observations, risks and further evolution | IFIAR Technology Task Force | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 2025-03-27 | full | Read from a copy of the PDF already downloaded by a parallel analyst (public document). |
| IFIAR-TTF-2026 | Use of technology in audits: Innovation and audit quality | IFIAR Technology Task Force | regulator | https://www.ifiar.org/latest-news/ifiar-releases-2026-report-on-the-use-of-technology-in-audits/ | 2026-04-20 | full | URL is the IFIAR news page that links the report; report text read from a copy downloaded by a parallel analyst. Frequency chart values are graphics and were not extractable. |
| CAQ-INSIDER-2026 | Audit Insider, July/August 2026 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-insider-july-august-2026 | 2026-09-01 | full | Page text carries 1 September 2026; reports the Spring 2026 Audit Partner Pulse released 15 July 2026. |
| CAQ-INSIDERAPR-2026 | Audit Insider, April 2026 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-insider-april-2026 | 2026-04 | full | Day of month not shown. |
| CAQ-INSIDERDEC-2025 | Audit Insider, December 2025 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-insider-december-2025 | 2025-12-19 | full |  |
| CAQ-INSIDERFEB-2026 | Audit Insider, January/February 2026 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-insider-january-february-2026 | 2026-02 | full | Day of month not shown. |
| CAQ-INSIDERMAR-2026 | Audit Insider, March 2026 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-insider-march-2026 | 2026-03 | full | Day of month not shown. |
| CAQ-INSIDERMAY-2026 | Audit Insider, May 2026 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-insider-may-2026 | 2026-05 | full | Day of month not shown. |
| CAQ-INSIDERNOV-2025 | Audit Insider, November 2025 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-insider-november-2025 | 2025-12 | full | Newsletter sent in early December 2025 (search listing showed 4 Dec); page text refers to the post-Thanksgiving period. |
| CAQ-INSIDERSEP-2026 | Audit Insider, September 2026 | Center for Audit Quality | professional-body | https://www.thecaq.org/audit-insider-september-2026 | 2026-09 | full | Day of month not shown. |
| CAQ-RSM-2026 | Shaping the future of assurance: Advancing AI in the audit (RSM, CAQ Audit in Action blog) | Center for Audit Quality (blog by RSM) | professional-body | https://www.thecaq.org/aia-shaping-the-future-of-assurance-advancing-ai-in-the-audit | 2026-08 | full | Blog date inferred from the CAQ July/August 2026 newsletter, which links it. |
| ICAEW-FRCVIEW-2026 | How helpful is FRC's guidance on generative and agentic AI? | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/how-helpful-is-frc-guidance-on-generative-and-agentic-ai | 2026-05-06 | full |  |
| ICAEW-PIERPOINT-2025 | Testing Gen AI platforms: can they do audit work? (Helen Pierpoint) | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2025/sep-2025/testing-gen-ai-platforms-can-they-do-audit-work | 2025-09-24 | full |  |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 | full | Practice aid itself not opened. |
| NYSSCPA-BOTIC-2025 | PCAOB's Botic Flags Opportunities and Risks in AI | NYSSCPA | professional-body | https://nysscpa.org/news/1051584-pcaobs-botic-flags-opportunities-and-risks-in-ai-2025-12-10 | 2025-12-10 | full |  |
| DART-SECPCAOB-2025 | AICPA & CIMA Conference on Current SEC and PCAOB Developments: key takeaways (Heads Up) | Deloitte DART | firm | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2025/aicpa-cima-conference-sec-pcaob-developments-2025-key-takeaways | 2025-12-12 | full |  |
| KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 2025-04 | full | Day taken from the landscape (22 April 2025); the page text I opened does not show it. |
| KPMG-HOHL-2026 | Q&A with Kurt Hohl, SEC Chief Accountant (Women Corporate Directors peer exchange) | KPMG Board Leadership Center | firm | https://kpmg.com/us/en/board-leadership/articles/2026/qa-kurt-hohl-sec-chief-accountant.html | 2026-05-27 | full |  |
| RSM-SECPCAOB-2025 | Insights from the 2025 AICPA Conference on Current SEC and PCAOB Developments | RSM US | firm | https://rsmus.com/content/dam/rsm/insights/financial-reporting/1pdf/insights-from-the-2025-aicpa-conference-on-current-sec-and-pcaob-developments-12-25.pdf | 2025-12 | full |  |
| AUDITBOARD-AGENTICERA-2026 | The agentic audit era: What CAEs must rethink now (Richard Chambers) | AuditBoard (now Optro) | vendor | https://auditboard.com/blog/agentic-audit-era-what-caes-must-rethink | 2026-08-12 | full |  |
| AUDITBOARD-RIF-2026 | Converging risks, competing priorities: Top takeaways from Risk in Focus, North America 2026/2027 (Richard Chambers) | AuditBoard (now Optro) | vendor | https://auditboard.com/blog/top-takeaways-from-risk-in-focus-north-america-2026-2027 | 2026-09-15 | full |  |
| AUDITBOARD-RTRA-2025 | Embracing real-time risk assessment: A practitioner's guide for internal audit teams in 2026 | AuditBoard (now Optro) | vendor | https://auditboard.com/blog/embracing-real-time-risk-assessment-a-practitioners-guide-for-internal-audit-teams-in-2026 | 2025-09-04 | full |  |
| MINDBRIDGE-ARA-2026 | MindBridge Advances Financial Oversight for the Agentic Era with New Platform Capabilities (press release) | MindBridge | vendor | https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/ | 2026-09-22 | full |  |
| OPTRO-AGENTS-2026 | Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance | Optro | vendor | https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance | 2026-10-14 | full |  |
| OPTRO-FJ-2026 | FJ Management advances its agentic audit strategy with Optro (customer story) | Optro | vendor | https://auditboard.com/blog/fj-management-success-story | 2026-09-22 | full |  |
| OPTRO-HELVETIA-2026 | How Helvetia Baloise gave internal audit room to focus on risk (customer story) | Optro | vendor | https://auditboard.com/blog/helvetia-baloise-success-story | 2026-09-10 | full |  |
| TR-CHALLENGES-2026 | Audit challenges and changes in 2026 | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/challenges-and-changes-within-the-audit-industry/ | 2026-02-02 | full |  |
| WK-AGENTRA-2026 | The evolving role of agentic risk assessment in audit planning | Wolters Kluwer | vendor | https://wolterskluwer.com/en/expert-insights/the-evolving-role-of-agentic-risk-assessment-in-audit-planning | 2026-03-02 | full | Site blocks curl; read through the r.jina.ai text mirror. |
| WK-AIDATA-2026 | AI in audit data analysis: Risks, limitations, and best practices | Wolters Kluwer (TeamMate) | vendor | https://wolterskluwer.com/en/expert-insights/ai-audit-data-analysis-risks-limitations-best-practices | 2026-06-10 | full | Read through the r.jina.ai text mirror. |
| WK-CONNECTED-2026 | The connected audit: A strategic framework for agentic workflows | Wolters Kluwer | vendor | https://wolterskluwer.com/en/expert-insights/a-strategic-framework-for-agentic-audit-workflows | 2026-03-02 | full | Read through the r.jina.ai text mirror. |
| WK-DYNAMIC-2026 | Static to strategic: unlocking the benefits of dynamic audit planning | Wolters Kluwer (TeamMate) | vendor | https://wolterskluwer.com/en/expert-insights/static-strategic-unlocking-benefits-dynamic-audit-planning | 2026-09-23 | full | Read through the r.jina.ai text mirror. |
| WK-GROUP-2025 | The future of group audits: How AI and technology are transforming audit quality | Wolters Kluwer | vendor | https://wolterskluwer.com/en/expert-insights/group-audits-embracing-technology-and-adapting-to-change | 2025-04-03 | full | Mirror shows 2025-04-03 as published time but the text links to 2026 articles, so it was revised later. Read through the r.jina.ai text mirror. |
| WK-MICRO-2026 | Real-time risk intelligence: How micro audits are redefining internal audit | Wolters Kluwer (TeamMate) | vendor | https://wolterskluwer.com/en/expert-insights/risk-intelligence-micro-audits-redefining-internal-audit | 2026-07-29 | full | Read through the r.jina.ai text mirror. |
| WK-MULTIYEAR-2026 | Multi-year audit planning: Keeping an eye on tomorrow's risks | Wolters Kluwer (TeamMate) | vendor | https://wolterskluwer.com/en/expert-insights/multi-year-audit-planning | 2026-10-14 | full | Read through the r.jina.ai text mirror. |
| WK-SAS145-2024 | SAS 145 risk assessment: How technology strengthens audit quality | Wolters Kluwer | vendor | https://wolterskluwer.com/en/expert-insights/auditing-reimagined-sas-145-and-the-rise-of-technology-enabled-risk-management | 2024-03-19 | full | Outside the 18-month window; used as a foundation only. Read through the r.jina.ai text mirror. |
| ARXIV-UMAR-2026 | Multi-Agent Framework for Audit Risk Assessment with Explicit Uncertainty and Evidence Conflict Modeling (UMAR) | arXiv (Wang et al.) | academic | https://arxiv.org/abs/2606.15640 | 2026-06-14 | full | Abstract page; preprint, not peer reviewed. |
| CPAJ-AIPLAN-2026 | Leveraging Artificial Intelligence in Audit Planning (Kasztelnik and Jermakowicz) | The CPA Journal | academic | https://www.cpajournal.com/2026/08/19/leveraging-artificial-intelligence-in-audit-planning/ | 2026-08-19 | full |  |
| IIAF-AIFRAUD-2026 | Internal Audit and AI-Enabled Fraud (survey report) | IIA Internal Audit Foundation with Optro | survey | https://www.theiia.org/globalassets/site/content/research/foundation/2026/internal-audit-and-ai-enabled-fraud/ia-and-ai-enabled-fraud-report-en.pdf | 2026 | full | Survey fielded Q4 2025; the document shows no release day (PDF creation date 2026-07-28; a search extract said February 2026). |
| ACCTODAY-BOTIC-2025 | PCAOB warns auditors about AI and PE | Accounting Today | press | https://www.accountingtoday.com/news/pcaob-warns-auditors-about-ai-and-pe | 2025-12-09 | full |  |
| CFOBREW-PWC-2025 | A look at PwC's 'next generation' audit | CFO Brew | press | https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit | 2025-11-05 | full | Reports a PwC roundtable held 27 October 2025. |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 | full |  |
| CPAPA-DELOITTE-2026 | Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia to Advance Audit and Assurance | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/06/24/deloitte-unveils-connected-agentic-intelligence-in-deloitte-omnia-to-advance-audit-assurance/185652/ | 2026-06-24 | full |  |
| CPAPA-ISACA-2025 | AI Isn't a Threat to Auditors: It's the Key to Elevating the Profession (Sampa David Sampa, ISACA working group) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/12/02/ai-isnt-a-threat-to-auditors-its-the-key-to-elevating-the-profession/174120/ | 2025-12-02 | full |  |
| CPAPA-LEDGERLINE-2026 | Testing Every Transaction Changes the Audit: Here's What Firms Should Know Before They Sell It (Tunde Adewole, Ledgerline) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/ | 2026-10-15 | full |  |
| EY-CANVAS-2026 | EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/ | 2026-04-07 | full |  |
| FINSTORY-KPMGFEE-2026 | KPMG forced Auditor for a 14% AI Discount...Will the Billable Hour die? | The Finance Story | press | https://thefinancestory.com/kpmg-forced-auditor-for-a-14-ai-discount-will-the-billable-hour-die | 2026-02-12 | full | Secondary report of a Financial Times story; the FT article was not opened. |
| GRCREPORT-DELOITTE-2026 | Deloitte Sees Internal Audit Moving Closer to the Center of Enterprise Risk in 2026 | GRC Report | press | https://www.grcreport.com/post/deloitte-sees-internal-audit-moving-closer-to-the-center-of-enterprise-risk-in-2026 | 2026-05-19 | full | Secondary summary of Deloitte's Internal Audit Hot Topics for 2026; Deloitte's report not opened. |
| KSLAW-SEIAG-2025 | PCAOB SEIAG Meeting Highlights: AI and Crypto take Center Stage | King & Spalding | press | https://www.kslaw.com/blog-posts/pcaob-seiag-meeting-highlights-ai-and-crypto-take-center-stage | 2025-11 | full | Meeting held 2025-11-05; blog post date not shown on page. |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 | full |  |
| PWCAU-2025 | PwC Australia rolls out pilot program for AI-assisted full audits | Accounting Times | press | https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits | 2025-10-27 | full |  |
| ICAEW-POD-2025 | Beyond Finance podcast: How should audit firms use AI? | ICAEW | podcast | https://www.icaew.com/insights/podcast/beyond-finance/how-should-audit-firms-use-ai | 2025-11-11 | full | Show notes opened; audio not heard. |
| RMS-CHAMBERS-2026 | Risk Management Show: Evaluating Governance Gaps and AI Readiness in 2026 with Richard Chambers | Global Risk Community | podcast | https://globalriskcommunity.libsyn.com/evaluating-governance-gaps-and-ai-readiness-in-2026-with-richard-chambers | 2026-01-11 | full | Show notes opened; audio not heard. |
| SRA-KING-2026 | Speaking of Risk and Audit: Auditing in the Age of AI: Risks, Rewards, and Practical Steps (Richard Chambers with Charles King, KPMG) | Optro (Speaking of Risk and Audit) | podcast | https://srapodcast.podbean.com/e/auditing-in-the-age-of-ai-risks-rewards-and-practical-steps/ | 2026-04-27 | full | Show notes opened; audio not heard. |

Carried from the landscape and not re-opened (cited once, in notes): CPACOM-ATR-2025 (AICPA and CPA.com, 2025 Audit Transformation Report, Dec 2025; the landscape read it in full).

---

## 6. Gaps

- **Search budget.** The shared web-search budget ran out after about eight searches, before searches on IIA Great Audit Minds 2026 sessions, ENGAGE 2026 recaps, group-audit scoping and AI scheduling tools. After that I followed links and the landscape's URLs with `curl` only.
- **Session content.** For the AAA workshop, KU symposium, ENGAGE, WCARS and the CAQ webinar I found agendas and listings, not what was said. IIA GAM 2026 and ISACA North America 2026 were not reopened (landscape has them).
- **Podcasts.** Show notes only (ICAEW Beyond Finance, Speaking of Risk and Audit, Risk Management Show). No audio or transcript. What the KPMG guest said about audit planning use cases is unknown beyond one sentence.
- **Community.** No community discussion read: Reddit and LinkedIn were blocked or not used. No job postings found for this module.
- **Blocked or unreachable:** pwc.com pages ('Risk assessment, reimagined' and the internal audit AI page; 403), gartner.com ('4 AI risks impacting audit plans'; 403), mindbridge.ai (403), trullion.com (403), pcaobus.org (403, so Botic's remarks were read through press and law-firm coverage, not the PCAOB text), learnsignal.com (429), Wolters Kluwer direct (Cloudflare; read via the r.jina.ai text mirror), Gartner press release (404), Uniper case page (404).
- **No quality evidence for planning tools.** Nothing on error, miss or override rates, parallel runs against a human risk assessment, or inspection findings on AI-assisted risk assessment. The only independent measures are one ICAEW chatbot test and one preprint on restatement labels.
- **No evidence found** for AI inside the fraud brainstorming session, for AI-assisted group component scoping beyond one vendor article, or for measured outcomes from staffing and budgeting tools.
- **Partial reads.** AICPA practice aid read only through the JofA summary; Deloitte internal audit outlook read through a secondary summary; IFIAR 2026 chart values not extractable; BDO conference recap page was a landing page (download required) with no auditor-AI content.
- **Fee figures.** The KPMG/Grant Thornton fee figures come from a secondary article citing the Financial Times and remain unconfirmed.
- **Outside the window.** KPMG's July 2024 GenAI statement (inside KPMG-CLARA-2025) and the March 2024 Wolters Kluwer SAS 145 article are older than 18 months and are used as foundations only.
- **Updates to the landscape.**
  - The AAA event is the Excellence in Auditing Education Workshop, held 15 Jan 2026 (the landscape gave no date). Both panels were moderated by CAQ staff; PwC's Tim Persons sat on the first panel (AAA-MIDYEAR-2026).
  - Botic's remark was that AI can enhance risk assessment and evidence gathering by analysing entire populations "in certain scenarios"; the qualifier matters (ACCTODAY-BOTIC-2025).
  - FRC Illustrative example 1 is for a hypothetical firm, not a deployment (FRC-GENAI-2026, p.42).
  - IFIAR issued a newer technology report on 20 Apr 2026; the landscape cites only the 2025 report (IFIAR-TTF-2026).
