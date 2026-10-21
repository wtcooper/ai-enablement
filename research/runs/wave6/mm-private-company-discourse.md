# Discourse: private-company assurance at mid-market firms

Module: `private-company` (assurance archetype, mid-market extension). Angle: discourse. Researched 2026-10-21. Read first: the wave 6 landscape file, the research vocabulary, and the existing assurance archetype and its module and use-case files, so that this file adds only what they lack.

## 1. Summary

- **What was read.** 45 distinct sources, all opened and read (community 3; conference 3; firm 1; podcast 1; press 5; professional-body 17; regulator 1; survey 4; vendor 10). Practitioner discourse on private-company audits, reviews and compilations is concentrated in four channels: AICPA-linked material (Journal of Accountancy, A&A Focus webcasts, the small-firm advocate column), Caseware's own releases and event recaps (the audit file at Citrin Cooperman, EisnerAmper and PKF O'Connor Davies), CPA.com surveys, and a handful of firm and state-body statements. Reddit and r/auditing returned 403 and could not be read; Going Concern could be read through a mirror.
- **Use cases.** 11 candidate entries; by grade A: 0, B: 1, C: 9, D: 1. The existing assurance archetype already holds the main firm and vendor deployments (DAS adoption at Citrin Cooperman, EisnerAmper and PKF O'Connor Davies; the Caseware disclosure checklist agent; gtap; Ask Luca; Oberlander on Thomson Reuters), so entries here are limited to changes it lacks, and the rest is cross-linked in section 4. Nothing reaches grade A: no firm in this module has published a tracked measure of an AI effect.
- **What is different at mid-market scale.** (1) The binding constraint is compliance load, not tooling: the AICPA's Small Firm Advocate says quality management and peer review effort now rivals the time spent on the audit for many small firms (JOFA-SMALLFIRM-2026). (2) Methodology and platform choice is a firm-level decision that practitioners discuss openly and that no source evaluates (GRF-ENGAGE-2026). (3) Client data quality and access, not model quality, is what firms further along say blocks them (CPACOM-ATR-2025). (4) Clients' finance leaders are now asking where AI savings go (FEIDAILY-FERF-2026).
- **Quality evidence is absent, and the baseline is thin.** None of the five 2025 state peer review reports read mentions AI. Their tables give a non-AI baseline: across four states, 135 of 1,485 reviewed engagements (9%) were nonconforming, 43 of 295 reviews (15%) and 14 of 482 compilations that omit disclosures (3%).
- **SSARS is a near-total gap.** No AI guidance, firm case or measured result was found for preparation, compilation or review engagements. The only live SSARS change is SSARS 27 (effective for periods ending on or after 15 December 2026), which is about consulting-engagement scope, not AI (CPACOM-SSARS27-2025).
- **Dated frontier.** AICPA practice aid on AI for financial statement auditors, 13 October 2026 (AICPA-AIPA-2026); Caseware Verity for Excel generally available 9 September 2026 (CASEWARE-VERITYXL-2026); Texas State Board statement on AI in attest work, August 2026 (TSBPA-2026).

## 2. Use cases

```yaml
- id: assurance-private-company-01
  title: Engagement-aware AI inside the Excel workpaper for workpaper generation and audit test automation (Caseware
    Verity for Excel)
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Auditors move information by hand between the audit file, client submissions and Excel workpapers. Caseware
    describes the aim as less time searching for and transferring information.
  solution: Caseware says Verity for Excel reasons across the connected engagement (client-submitted information,
    procedures, trial balance data, materiality, samples and supporting documents) and keeps live connections between
    the engagement and Excel. It can run multi-step workflows inside Excel covering workpaper generation and test
    automation across tests of controls, substantive analytics and tests of details, through to reporting. Suggestions
    can be reviewed and approved before changes are applied.
  outcomes:
  - {lever: capacity, description: Average time saved in Caseware's own testing to date, figure: 9 hours per engagement;
      75% per task, measures: 'Caseware''s wording: ''in testing to date'' the product ''has saved on average nine
      hours per engagement and 75% per task''. The release does not say how many engagements, firms or tasks, what
      the baseline was, or what ''75% per task'' is a percentage of.', provenance: vendor-published, source_ref: CASEWARE-VERITYXL-2026}
  prerequisites:
  - Caseware Verity access; the release says Verity for Excel is included at no additional licensing for firms that
    already have Verity (CASEWARE-VERITYXL-2026)
  - A Caseware engagement with the connected client information, trial balance, materiality and sample data the
    agent reads (CASEWARE-VERITYXL-2026)
  risks_and_guardrails:
  - Caseware says practitioners remain in control and can review and approve suggestions before changes are applied
    (CASEWARE-VERITYXL-2026)
  - Caseware describes Verity outputs as designed to be traceable and explainable, with AI reasoning and artifacts
    kept under firm control (CASEWARE-CWX-2026)
  human_checkpoints:
  - The practitioner approves each suggested change before it is applied (CASEWARE-VERITYXL-2026)
  role_evolution: Caseware says the intent is that teams spend less time searching for and moving information and
    more time on professional judgment (CASEWARE-VERITYXL-2026).
  evidence_grade: C
  sources:
  - {ref: CASEWARE-VERITYXL-2026, title: 'Caseware Verity for Excel: Agentic AI Connects Client Requests to Audit
      Workpapers', publisher: Caseware, type: vendor, url: 'https://www.caseware.com/news/caseware-puts-agentic-ai-inside-the-audit-connecting-client-requests-to-the-workpaper-with-caseware-verity-for-excel',
    date: '2026-09-09', access: full, locator: 'opening paragraphs; section on Verity for Excel (general availability,
      nine hours and 75% figure)'}
  - {ref: CASEWARE-CWX-2026, title: 'How Agentic AI Is Transforming Audit: Inside Caseware Verity (CwX 2026 session
      recap)', publisher: Caseware, type: vendor, url: 'https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance',
    date: '2026-06-17', access: full, locator: governance paragraphs}
  last_reviewed: '2026-10-21'
  notes: 'Graded C: the only evidence is Caseware''s own release; no firm is named as using the Excel product. Overlaps
    the Excel-agent entries in substantive-testing (07, 11, 12); cross-link rather than count twice. The 9-hour
    and 75% figures are vendor testing results with no stated method.'
- id: assurance-private-company-02
  title: Client request collection with an agent that validates submissions and feeds the workpaper
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - coordination-scheduling
  - review-assurance
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Client information arrives late, incomplete or in poor shape. In CPA.com's survey of 54 U.S. firms, 60%
    ranked poor-quality client data and 53% ranked lack of access to client information and systems among the top
    blockers to audit transformation (CPACOM-ATR-2025).
  solution: Caseware introduced Client Requests, which lets auditors and clients collaborate through the engagement
    and sends client-submitted information into the Excel workpaper. A Verity Response Validation Agent checks client
    submissions. Caseware calls this the first step toward automating the path from client request to a populated
    workpaper. It is offered through a limited early-access program with reference customers, ahead of a broader
    rollout.
  outcomes:
  - {lever: speed, description: none published, figure: none published, measures: No figures published for Client
      Requests or the Response Validation Agent., provenance: vendor-published, source_ref: CASEWARE-VERITYXL-2026}
  prerequisites:
  - Membership of Caseware's early-access program during the limited rollout (CASEWARE-VERITYXL-2026)
  risks_and_guardrails:
  - Caseware says the agent's findings inform the review, but the decision to accept a submission always rests with
    the auditor (CASEWARE-VERITYXL-2026)
  - In the CPA.com survey the firms furthest along said access to client data was their biggest obstacle (CPACOM-ATR-2025)
  human_checkpoints:
  - The auditor decides whether to accept each client submission (CASEWARE-VERITYXL-2026)
  role_evolution: Caseware says auditors gain confidence in the completeness and accuracy of what clients return
    (CASEWARE-VERITYXL-2026).
  evidence_grade: C
  sources:
  - {ref: CASEWARE-VERITYXL-2026, title: 'Caseware Verity for Excel: Agentic AI Connects Client Requests to Audit
      Workpapers', publisher: Caseware, type: vendor, url: 'https://www.caseware.com/news/caseware-puts-agentic-ai-inside-the-audit-connecting-client-requests-to-the-workpaper-with-caseware-verity-for-excel',
    date: '2026-09-09', access: full, locator: section on Client Requests and the Response Validation Agent}
  - {ref: CPACOM-ATR-2025, title: '2025 Audit Transformation Report (Audit Benchmark Survey, 54 U.S. firms)', publisher: CPA.com
      (AICPA), type: survey, url: 'https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf',
    date: 2025-12, access: full, locator: '''Barriers to overcome'' chart and text (PDF page 8)'}
  last_reviewed: '2026-10-21'
  notes: Early access only; no named customer and no measurement. The release does not say how the agent copes with
    clients on small-business systems such as spreadsheets or QuickBooks; no source found on non-ERP data handling
    for this feature. The 60% and 53% figures are shares of responding firms in a non-representative survey of 54
    firms.
- id: assurance-private-company-03
  title: Extraction of source-document data into workpapers (Caseware Verity Document Intelligence Agent, beta)
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - transaction-processing
  - document-production
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Staff key information from client source documents into workpapers by hand during engagement execution.
  solution: Caseware describes a Document Intelligence Agent, still in beta in June 2026, that automates extraction
    of information from source documents into workpapers to reduce manual data entry.
  outcomes:
  - {lever: capacity, description: none published, figure: none published, measures: No figures published for this
      agent in the CwX 2026 recap., provenance: vendor-published, source_ref: CASEWARE-CWX-2026}
  prerequisites:
  - Caseware Cloud and beta access (CASEWARE-CWX-2026)
  risks_and_guardrails:
  - Caseware says Verity outputs are designed to be traceable and explainable, with engagement boundaries enforced
    (CASEWARE-CWX-2026)
  - The recap says the agent is still in beta (CASEWARE-CWX-2026)
  human_checkpoints:
  - Not described for this agent in the recap; Caseware's general statement is that review points remain the auditor's
    call (CASEWARE-CWX-2026)
  role_evolution: Not described for this agent.
  evidence_grade: C
  sources:
  - {ref: CASEWARE-CWX-2026, title: 'How Agentic AI Is Transforming Audit: Inside Caseware Verity (CwX 2026 session
      recap)', publisher: Caseware, type: vendor, url: 'https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance',
    date: '2026-06-17', access: full, locator: section on the Verity Agentic Suites (Document Intelligence Agent
      paragraph)}
  last_reviewed: '2026-10-21'
  notes: 'Thin entry: one sentence of vendor description. Related extraction tools (DataSnipper, Thomson Reuters)
    are in substantive-testing. Kept because Caseware''s file is the one named for small and mid-sized firms in
    the landscape file.'
- id: assurance-private-company-04
  title: Firm-built audit research and insight agent on a cloud AI platform, run alongside a vendor audit file (EisnerAI
    Audit Design Agent)
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - research-synthesis
  - review-assurance
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: EisnerAmper's national office head says removing the work of assembling and sorting data lets auditors
    do more meaningful work, which implies auditors spend material time on it today.
  solution: EisnerAmper announced on 9 March 2026 a collaboration with Microsoft to develop the EisnerAI Audit Design
    Agent on Microsoft Foundry. The firm describes it as a research and insight partner that helps auditors synthesize
    information across systems and spot patterns, and says it can speed risk assessment and reduce errors or discrepancies.
    On 25 June 2026 the same firm announced it had adopted Caseware's DAS suite across its assurance practice and
    would keep evaluating AI tools on Caseware's platform, so it is both building and buying.
  outcomes:
  - {lever: quality, description: none published, figure: none published, measures: 'Neither announcement publishes
      accuracy, time or review-note figures for the agent.', provenance: self-reported, source_ref: EISNER-AUDITAGENT-2026}
  prerequisites:
  - Collaboration with Microsoft and use of Microsoft Foundry (EISNER-AUDITAGENT-2026)
  - A separate audit file and methodology (DAS) that the agent sits alongside (CASEWARE-EISNERAMPER-2026)
  risks_and_guardrails:
  - The trade-press coverage names no controls, accuracy checks or review design for the agent (EISNER-AUDITAGENT-2026)
  human_checkpoints:
  - Not described in the announcement coverage (EISNER-AUDITAGENT-2026)
  role_evolution: EisnerAmper's national office head says removing the work of assembling and sorting data lets
    auditors do more meaningful work (EISNER-AUDITAGENT-2026).
  evidence_grade: C
  sources:
  - {ref: EISNER-AUDITAGENT-2026, title: EisnerAmper Rolls Out In-House AI Audit Design Agent, publisher: CPA Practice
      Advisor, type: press, url: 'https://www.cpapracticeadvisor.com/2026/03/20/eisneramper-rolls-out-in-house-ai-audit-design-agent/180020/',
    date: '2026-03-20', access: full, locator: first four paragraphs and executive quotes}
  - {ref: CASEWARE-EISNERAMPER-2026, title: EisnerAmper Adopts Caseware DAS Suite to Unify Audit Methodology Across
      Multi-Vertical Practice, publisher: Caseware, type: vendor, url: 'https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice',
    date: '2026-06-25', access: full, locator: 'paragraphs on 1,100 professionals and on future AI tools'}
  last_reviewed: '2026-10-21'
  notes: 'Announced, not in production, as far as public sources show. Mid-tier build-versus-buy pattern: a firm
    that standardizes on a vendor methodology and still builds its own agent. Compare the larger-firm platforms
    already in planning-risk-assessment (11).'
- id: assurance-private-company-05
  title: Firm-run, hands-on evaluation of audit methodology and AI tools before committing
  archetype: assurance
  module: private-company
  function: technology-it
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Choosing an audit methodology or vendor is high-stakes, and the ENGAGE 2026 panel abstract frames it
    as something firms with an audit department face whether they are exploring or ready to change.
  solution: The GRF-hosted ENGAGE 2026 panel, 'Methodology for Selecting a Methodology', was billed as practitioner-led
    and free of vendor pitches, with each panelist having chosen a different methodology or vendor and covering
    considerations beyond cost, ROI and stakeholder strategy. A Thomson Reuters interview (vendor-run) says leading
    firms build the capability to test systems themselves by using standardized use-case tests to compare systems
    side by side and by running AI solutions in parallel on live engagements, with partners judging performance
    on the firm's own work.
  outcomes:
  - {lever: risk, description: none published, figure: none published, measures: Neither source reports a result
      from a firm-run evaluation., provenance: vendor-published, source_ref: TR-STATEAUDIT-2026}
  prerequisites:
  - Partner and managing-partner time to test tools on the firm's own files (TR-STATEAUDIT-2026)
  - A set of standard test tasks so tools can be compared on the same work (TR-STATEAUDIT-2026)
  - A live engagement that can carry a parallel run without risking quality (TR-STATEAUDIT-2026)
  risks_and_guardrails:
  - The Thomson Reuters interviewees are vendor executives selling audit software, so the advice to test directly
    is also a sales context (TR-STATEAUDIT-2026)
  - The GRF page is an abstract; the panel's content was not read
  human_checkpoints:
  - Partners decide whether the evidence from their own testing is enough to scale adoption (TR-STATEAUDIT-2026)
  role_evolution: Partners and managing partners take on the job of building their own trust in tool performance
    instead of relying on demonstrations (TR-STATEAUDIT-2026).
  evidence_grade: C
  sources:
  - {ref: GRF-ENGAGE-2026, title: 2026 AICPA & CIMA Engage Conference (GRF CPAs & Advisors event page), publisher: GRF
      CPAs & Advisors, type: conference, url: 'https://www.grfcpa.com/?p=9081', date: 2026-06, access: full, locator: 'ENGAGE
      2026 session listing: ''Methodology for Selecting a Methodology'' abstract'}
  - {ref: TR-STATEAUDIT-2026, title: 'The state of AI in audit in 2026: Interview with experts', publisher: Thomson
      Reuters Tax & Accounting, type: vendor, url: 'https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/',
    date: '2026-03-30', access: full, locator: section on evaluating AI solutions (apples-to-apples tests and parallel
      runs)}
  last_reviewed: '2026-10-21'
  notes: Methodology and tool choice is the live decision in this module. No source publishes the outcome of a bake-off
    or the criteria a firm used. The Thomson Reuters description of parallel runs is a claim about what leading
    firms do; no firm is named.
- id: assurance-private-company-06
  title: Tool-assisted gap flagging and cross-referencing in engagement files to ease peer review at small firms
  archetype: assurance
  module: private-company
  function: risk-compliance-legal
  work_types:
  - review-assurance
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: The AICPA's Small Firm Advocate wrote in August 2026 that for many small firms the effort to comply with
    quality management standards and peer review now rivals the time spent performing the audit, and that peer review
    has become more focused on several areas including risk assessment.
  solution: The AICPA column advises standardizing templates, checklists and engagement files through the year and
    says audit-specific, AI-enabled technologies can help firms identify gaps, cross-reference requirements and
    flag inconsistencies earlier, so reviewers and partners spend time on judgment and supervision. A Thomson Reuters
    blog (vendor) says purpose-built audit AI embeds research with links to standards, standardizes work papers
    and builds audit trails.
  outcomes:
  - {lever: quality, description: none published, figure: none published, measures: 'No source reports a peer review
      result, finding rate or hours saved from using such a tool.', provenance: vendor-published, source_ref: TR-PEERREVIEW-2026}
  prerequisites:
  - Standardized templates, checklists and engagement files kept up through the year (JOFA-SMALLFIRM-2026)
  - A regular flow of audit work; the column says firms that audit regularly develop more repeatable processes (JOFA-SMALLFIRM-2026)
  - A system of quality management in place; the AICPA says firms had to have one by 15 December 2025 and should
    operate it in 2026 (AICPA-QMPR-2026)
  risks_and_guardrails:
  - The AICPA column says technology will not remove the need for peer review (JOFA-SMALLFIRM-2026)
  - None of five 2025 state peer review reports read for this module mentions AI, so how reviewers treat AI-assisted
    files is not documented in them (TSCPA-PEERREVIEW-2025; CTCPA-PR-2026; MNCPA-PR-2026; MOCPA-PR-2026; OSCPA-PR-2026)
  - The Thomson Reuters piece is marketing for its own product (TR-PEERREVIEW-2026)
  human_checkpoints:
  - Reviewers and partners keep judgment and supervision; the tool flags gaps (JOFA-SMALLFIRM-2026)
  role_evolution: The column suggests some small firms use independent contractors or consultants, often retired
    practitioners, for engagement work and remediation during peak periods (JOFA-SMALLFIRM-2026).
  evidence_grade: C
  sources:
  - {ref: JOFA-SMALLFIRM-2026, title: 'What small firm CPAs need to know (Small Firm Q&A, Stephanie Otero)', publisher: Journal
      of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/aug/what-small-firm-cpas-need-to-know/',
    date: '2026-08-01', access: full, locator: first two Q&As (audit viability; peer review efficiency)}
  - {ref: TR-PEERREVIEW-2026, title: How to pass audit peer review with AI, publisher: Thomson Reuters Tax & Accounting,
    type: vendor, url: 'https://tax.thomsonreuters.com/blog/passing-peer-review-with-ai/', date: '2026-01-23', access: full,
    locator: opening summary and section on what reviewers look for}
  - {ref: AICPA-QMPR-2026, title: 'New QM Peer Review Checklists: What Firms Need to Know (CPEA Report, August 2026;
      landing page only)', publisher: AICPA & CIMA, type: professional-body, url: 'https://www.aicpa-cima.com/resources/article/new-qm-peer-review-checklists-what-firms-need-to-know',
    date: 2026-08, access: full, locator: opening paragraph (15 December 2025 requirement)}
  - {ref: TSCPA-PEERREVIEW-2025, title: Annual Report on Peer Review Activities 2025 (Tennessee), publisher: Tennessee
      Society of CPAs, type: professional-body, url: 'https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf',
    date: '2026-03-31', access: full, locator: whole report (no mention of AI)}
  - {ref: CTCPA-PR-2026, title: 'Annual Report on Peer Review Activities, 2025 (Connecticut)', publisher: Connecticut
      Society of CPAs, type: professional-body, url: 'https://www.ctcpas.org/storage/assets/PDFs/Annual%20Report%20on%20PR%20Activities.pdf',
    date: '2026-01-12', access: full, locator: whole report (no mention of AI)}
  - {ref: MNCPA-PR-2026, title: 2025 Annual Report on Peer Review Activities (Minnesota and North Dakota), publisher: Minnesota
      Society of CPAs, type: professional-body, url: 'https://www.mncpa.org/mncpa/media/Documents-Shared/peer-review/2025-MNCPA-annual-report-on-peer-review-activities.pdf',
    date: 2026-01, access: full, locator: whole report (no mention of AI)}
  - {ref: MOCPA-PR-2026, title: 2025 Annual Report on Peer Review Activities (Missouri), publisher: Missouri Society
      of CPAs, type: professional-body, url: 'https://www.mocpa.org/storage/assets/MOCPA/Peer%20Review%20Annual%20Report%202025.pdf',
    date: '2026-02-25', access: full, locator: whole report (no mention of AI)}
  - {ref: OSCPA-PR-2026, title: Annual Report on Peer Review Activities for 2025 (Oregon administering entity),
    publisher: Oregon Society of CPAs, type: professional-body, url: 'https://www.orcpa.org/storage/assets/Pages/About/Peer%20Review/Annual%20Report%202025.pdf',
    date: '2026-03-01', access: full, locator: whole report (no mention of AI)}
  last_reviewed: '2026-10-21'
  notes: 'Graded C: advice and vendor claims only, no named firm. This is where the quality-management module''s
    system of quality management meets small-firm scale; see quality-management (14, 21, 23) for the firm-level
    and file-level AI controls. Baseline peer review data are in the module notes.'
- id: assurance-private-company-07
  title: Preparation, compilation and review engagements run on the same AI-enabled platform as audits
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: 'Firms serving private companies run audits, reviews, compilations and preparations, and in 2025 state
    peer review reports the review engagement was among the more often nonconforming types: 43 of 295 reviews across
    four states (this report''s arithmetic from per-state tables).'
  solution: Citrin Cooperman (which describes itself as serving private, middle-market businesses) adopted Caseware's
    AI-enabled DAS suite including DAS Audit, DAS PCR and DAS EBP. EisnerAmper's adoption of DAS includes modules
    for preparation, compilation and review engagements and for employee benefit plan audits. Neither release says
    what AI does inside the preparation, compilation and review module.
  outcomes:
  - {lever: capacity, description: 'Adoption counts for the whole DAS suite, not an AI effect or a result for compilations
      and reviews', figure: 'more than 1,100 professionals; over 1,500 client engagements', measures: 'Caseware''s
      wording for EisnerAmper: ''more than 1,100 EisnerAmper professionals are now using the DAS suite to execute
      audits'' and ''over 1,500 client engagements'' completed ''using the new system'', as of 25 June 2026; not
      split by engagement type', provenance: vendor-published, source_ref: CASEWARE-EISNERAMPER-2026}
  prerequisites:
  - Data migration, training and change management; CPA.com acted as implementation partner for Citrin Cooperman
    and EisnerAmper (CITRIN-DAS-2026; CASEWARE-EISNERAMPER-2026)
  - A phased rollout; EisnerAmper says it put professional readiness ahead of speed (CASEWARE-EISNERAMPER-2026)
  risks_and_guardrails:
  - No source describes AI in the preparation, compilation and review module; the grade is capped for that reason
  - A 2026 CPE webcast on preparation, compilation and review lists SSARS 22 to 27 and fraud-related and going-concern
    responsibilities, with no AI item in its objectives (NYSSCPA-PCR-2026)
  human_checkpoints:
  - Not described for the preparation, compilation and review module
  role_evolution: Citrin Cooperman's assurance innovation leader says seeing the reasoning behind procedures helps
    professionals build technical knowledge and judgment (CITRIN-DAS-2026).
  evidence_grade: C
  sources:
  - {ref: CITRIN-DAS-2026, title: 'Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware',
    publisher: Caseware, type: vendor, url: 'https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth',
    date: '2026-07-13', access: full, locator: 'first two paragraphs (DAS Audit, DAS PCR, DAS EBP) and CPA.com implementation
      paragraph'}
  - {ref: CASEWARE-EISNERAMPER-2026, title: EisnerAmper Adopts Caseware DAS Suite to Unify Audit Methodology Across
      Multi-Vertical Practice, publisher: Caseware, type: vendor, url: 'https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice',
    date: '2026-06-25', access: full, locator: 'first paragraph (modules, 1,100 professionals, 1,500 engagements)'}
  - {ref: TSCPA-PEERREVIEW-2025, title: Annual Report on Peer Review Activities 2025 (Tennessee), publisher: Tennessee
      Society of CPAs, type: professional-body, url: 'https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf',
    date: '2026-03-31', access: full, locator: 'section II.2.c, reviews row: 13 of 99'}
  - {ref: CTCPA-PR-2026, title: 'Annual Report on Peer Review Activities, 2025 (Connecticut)', publisher: Connecticut
      Society of CPAs, type: professional-body, url: 'https://www.ctcpas.org/storage/assets/PDFs/Annual%20Report%20on%20PR%20Activities.pdf',
    date: '2026-01-12', access: full, locator: 'nonconforming engagements table, reviews row: 5 of 63'}
  - {ref: MNCPA-PR-2026, title: 2025 Annual Report on Peer Review Activities (Minnesota and North Dakota), publisher: Minnesota
      Society of CPAs, type: professional-body, url: 'https://www.mncpa.org/mncpa/media/Documents-Shared/peer-review/2025-MNCPA-annual-report-on-peer-review-activities.pdf',
    date: 2026-01, access: full, locator: 'nonconforming engagements table, reviews row: 14 of 75'}
  - {ref: MOCPA-PR-2026, title: 2025 Annual Report on Peer Review Activities (Missouri), publisher: Missouri Society
      of CPAs, type: professional-body, url: 'https://www.mocpa.org/storage/assets/MOCPA/Peer%20Review%20Annual%20Report%202025.pdf',
    date: '2026-02-25', access: full, locator: 'nonconforming engagements table, reviews row: 11 of 58'}
  - {ref: NYSSCPA-PCR-2026, title: 'Annual Update and Practice Issues for Preparation, Compilation and Review Engagements
      (webcast listing)', publisher: NYSSCPA, type: conference, url: 'https://nysscpa.org/catalog/events/1020413-annual-update-and-practice-issues-for-preparation-compilation-and-review-engagements-webcast-2026-23-07',
    date: '2026-07-23', access: full, locator: course objectives}
  last_reviewed: '2026-10-21'
  notes: This is the only entry that reaches SSARS work, and it shows platform adoption rather than AI. No AICPA,
    ARSC or state-board source found that addresses AI in preparation, compilation or review. SSARS 27, which takes
    preparation out of AR-C 70 when financial statements are a by-product of a consulting engagement, applies to
    periods ending on or after 15 December 2026 (CPACOM-SSARS27-2025); route the advisory-service side to the future
    accounting and client advisory archetype. The 43 of 295 baseline is a sum of four states' tables and a different
    mix of firms than any AI adopter.
- id: assurance-private-company-08
  title: Standardize workpaper layouts, functionality and the firm knowledge base before layering AI
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - document-production
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Caseware's AI and analytics lead told the Journal of Accountancy that audit variability made it hard
    for auditors to benefit from tools that need consistent execution.
  solution: Citrin Cooperman's audit innovation leader describes a firm project, running more than a year, with
    a team just for developing the standardized workpaper, layout and functionality. Technologists, subject matter
    experts, managers and the quality and standards teams all take part. She says a standardized knowledge base
    and process makes it easier for AI to surface the right information and for automation to scale across varied
    engagements.
  outcomes:
  - {lever: quality, description: 'The article reports the effort''s length, not results', figure: more than a year,
    measures: 'How long the standardization effort ''has stretched'', in the Journal of Accountancy''s words; no
      result is reported', provenance: self-reported, source_ref: JOFA-AUDITAI-2026}
  prerequisites:
  - A dedicated project team that includes technologists, subject matter experts, managers and the quality and standards
    teams (JOFA-AUDITAI-2026)
  - Client data access; in a CPA.com survey of audit firms, lack of access to client data was one of the top obstacles
    to implementing AI (JOFA-AUDITAI-2026)
  risks_and_guardrails:
  - Kanter calls the work a 'huge' undertaking (JOFA-AUDITAI-2026)
  - A customized AI tool is only as good as the data it can reach (JOFA-AUDITAI-2026)
  human_checkpoints:
  - The firm's quality and standards teams help define the standardized workpaper (JOFA-AUDITAI-2026)
  role_evolution: The firm's quality and standards teams take part in building the standardized workpaper (JOFA-AUDITAI-2026).
  evidence_grade: B
  sources:
  - {ref: JOFA-AUDITAI-2026, title: How AI is transforming the audit - and what it means for CPAs, publisher: Journal
      of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/feb/how-ai-is-transforming-the-audit-and-what-it-means-for-cpas/',
    date: '2026-02-01', access: full, locator: section on how a firm starts implementing AI (Kanter quotes)}
  - {ref: JOFA-SMALLFIRM-2026, title: 'What small firm CPAs need to know (Small Firm Q&A, Stephanie Otero)', publisher: Journal
      of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/issues/2026/aug/what-small-firm-cpas-need-to-know/',
    date: '2026-08-01', access: full, locator: 'peer review answer: standardizing templates, checklists and engagement
      files'}
  - {ref: CITRIN-DAS-2026, title: 'Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware',
    publisher: Caseware, type: vendor, url: 'https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth',
    date: '2026-07-13', access: full, locator: Citrin Cooperman description of its clients}
  last_reviewed: '2026-10-21'
  notes: 'Graded B: a named mid-tier firm and a described real project, with no published measurement. The article
    is dated February 2026 and Citrin''s DAS adoption release July 2026; no source links the two. Unlike a platform
    adoption, this is a content and methodology change that precedes tool choice.'
- id: assurance-private-company-09
  title: 'Show clients where AI-driven efficiency goes: value reporting to CFOs and audit committees'
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - client-interaction
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: In the FERF survey of 95 finance leaders, opinion was evenly split on whether the auditor's AI has improved
    audit quality, and some respondents described faster processing without more insight. The lead researcher says
    CFOs are asking where the savings go.
  solution: The FERF researcher says firms that can answer clearly and with data will have an advantage. CPA.com's
    2025 survey of 54 firms found 66% tell clients about their technology and methodology as a differentiator, while
    83% name staff efficiency as a top return on technology and 6% do not measure the return at all.
  outcomes:
  - {lever: experience, description: CFO opinion on whether the auditor's AI has improved audit quality, figure: evenly
      split, measures: 'FERF 16th annual audit fee survey, 95 FEI member respondents (September 2025 to January
      2026); the page gives no counts for this question', provenance: independent, source_ref: FEIDAILY-FERF-2026}
  - {lever: growth, description: Firms that communicate their technology use to clients as a value differentiator,
    figure: 66%, measures: '''Two-thirds of the firms (66%)'' of the 54 surveyed U.S. firms ''communicate their
      use of technology and methodology'' to clients; survey is not representative', provenance: self-reported,
    source_ref: CPACOM-ATR-2025}
  prerequisites:
  - 'A way to measure what the technology changed beyond hours: 54% of surveyed firms prioritize audit quality or
    accuracy as a return, 37% cost savings (CPACOM-ATR-2025)'
  risks_and_guardrails:
  - FERF's respondents span private companies, nonprofits, public entities and government agencies, and its fee
    benchmark covers about 470 S&P 500 companies, so the large-company figures do not describe mid-market fees (FEIDAILY-FERF-2026)
  - One respondent who ran a formal competitive review reported fee reductions of 25 to 30 percent (FEIDAILY-FERF-2026)
  human_checkpoints:
  - The engagement partner owns the conversation with the CFO or audit committee (FEIDAILY-FERF-2026)
  role_evolution: Partners are expected to explain value and insight, not only compliance execution; some respondents
    see audit relationships as more transactional over time (FEIDAILY-FERF-2026).
  evidence_grade: C
  sources:
  - {ref: FEIDAILY-FERF-2026, title: 'Audit Fees Hold Firm, Relationships Are Evolving, and Financial Leaders See
      Room for More (FERF 16th annual audit fee survey)', publisher: FEI Daily (Financial Executives International),
    type: survey, url: 'https://daily.financialexecutives.org/FEI-Daily/April-2026/audit-fees-stable-ai-audit-trends-ferf-2024-survey.aspx',
    date: 2026-04, access: full, locator: paragraphs on AI in audit workflows and the value perception gap}
  - {ref: CPACOM-ATR-2025, title: '2025 Audit Transformation Report (Audit Benchmark Survey, 54 U.S. firms)', publisher: CPA.com
      (AICPA), type: survey, url: 'https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf',
    date: 2025-12, access: full, locator: '''Technology ROI'' table and the sentence on communicating technology
      use to clients (PDF page 12)'}
  last_reviewed: '2026-10-21'
  notes: 'Overlaps planning-risk-assessment (23) on negotiating AI efficiency into fees and economics.md; this entry
    is the reporting step. Graded C: survey evidence of intent and client opinion, no named firm showing the practice.'
- id: assurance-private-company-10
  title: Start with low-risk drafting and documentation tasks chosen with staff, before analytics
  archetype: assurance
  module: private-company
  function: service-delivery
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Firms exploring AI risk being overwhelmed, and the analytics and data-driven testing that attract attention
    are conceptually hard to validate.
  solution: At the AICPA's A&A Focus webcast on 10 September 2025, a Caseware senior vice president advised starting
    with easy-win tasks such as summarizing board minutes, editing long memos or automating routine documentation,
    picked with staff, and not starting with analytics. She advised respecting firm policy and quality management
    requirements, reading licence terms (smaller firms lack large firms' leverage to negotiate), and learning to
    write prompts using a situation-task-appearance-refine structure. An ENGAGE 2026 session by an AAFCPAs consultant
    and the same Caseware executive was billed as covering use cases, benefits and limits, governance, prompting
    and bias.
  outcomes:
  - {lever: capacity, description: none published, figure: none published, measures: The webcast recap reports no
      measurements., provenance: vendor-published, source_ref: JOFA-AAFOCUS-2025-09}
  prerequisites:
  - A firm policy and an approved tool; data privacy and confidentiality checked, especially for open or free tools
    (JOFA-AAFOCUS-2025-09)
  - Staff involved in picking the tedious tasks to automate (JOFA-AAFOCUS-2025-09)
  risks_and_guardrails:
  - The speaker warned that with a free tool 'you are the product' (JOFA-AAFOCUS-2025-09)
  - Due care and professional skepticism are unchanged; the practitioner stays responsible for accuracy and judgment
    (JOFA-AAFOCUS-2025-09)
  human_checkpoints:
  - The practitioner reviews every AI draft and remains responsible for it (JOFA-AAFOCUS-2025-09)
  role_evolution: The speaker said easy-win uses help younger staff perform at a higher level sooner (JOFA-AAFOCUS-2025-09).
  evidence_grade: C
  sources:
  - {ref: JOFA-AAFOCUS-2025-09, title: 'A&A Focus recap: AI considerations in A&A, GASB updates, and practical lease
      accounting challenges', publisher: Journal of Accountancy (AICPA), type: professional-body, url: 'https://www.journalofaccountancy.com/newsletters/a-a-focus/aa-focus-recap-ai-considerations-in-aa-gasb-updates-and-practical-lease-accounting-challenges',
    date: '2025-09-19', access: full, locator: paragraphs on Danielle Supkis-Cheek's AI segment}
  - {ref: AAFCPAS-ENGAGE-2026, title: AAFCPAs Takes the Stage at AICPA ENGAGE 2026, publisher: AAFCPAs, type: conference,
    url: 'https://www.aafcpa.com/?p=29733', date: '2026-05-20', access: full, locator: ENGAGE 2026 session description
      (Ryan Wolff with Danielle Cheek)}
  last_reviewed: '2026-10-21'
  notes: The speaker is a vendor executive speaking on an AICPA webcast, which is advice, not evidence of results.
    Board-minute summaries and memo drafting are covered as tool uses in planning-risk-assessment (01) and completion-reporting
    (13); this entry is the adoption sequence. The ENGAGE 2026 session text is an abstract; the session content
    was not read.
- id: assurance-private-company-11
  title: 'Idea: continuous, AI-powered audits sold by start-ups as a challenge to hours-based audit fees'
  archetype: assurance
  module: private-company
  function: strategy-planning
  work_types:
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: model
  runtime_class: background-agent
  maturity: emerging
  problem: Audit fees and delivery models are built on labor-intensive procedures.
  solution: 'Idea: new entrants run continuous, AI-driven audits that undercut the hours-based model. An episode
    summary of The Accounting Podcast (25 September 2026) says start-ups such as Oath Verified are pioneering continuous,
    AI-powered audits that challenge traditional fee structures. The summary is machine-written and does not say
    whether any private-company audit has been signed under this model.'
  outcomes:
  - {lever: cost, description: none published, figure: none published, measures: none published; a podcast summary
      page makes the point and gives no data, provenance: independent, source_ref: ACCOUNTINGPODCAST-2026}
  prerequisites:
  - Not stated in the summary
  risks_and_guardrails:
  - A Going Concern commentator argues a firm could be forced to retract an audit report if AI hallucinated evidence
    or its agents were not properly supervised; this is opinion, not a finding (GOINGCONCERN-2026-08-03)
  human_checkpoints:
  - Not stated in the summary
  role_evolution: The summary says smaller firms can use technology to compete with larger entities (ACCOUNTINGPODCAST-2026).
  evidence_grade: D
  sources:
  - {ref: ACCOUNTINGPODCAST-2026, title: 'Tips to Roll Out AI In Your Firm, AI Squeezing Audit Fees (The Accounting
      Podcast, episode summary page)', publisher: Podwise (The Accounting Podcast), type: podcast, url: 'https://podwise.ai/episodes/8995231',
    date: '2026-09-25', access: full, locator: 'episode summary, second sentence'}
  - {ref: GOINGCONCERN-2026-08-03, title: 'Monday Morning Accounting News Brief: Chief Purpose Officer dips out
      of KPMG; EY teases a new quantum computer (8.3.26)', publisher: Going Concern, type: community, url: 'https://www.goingconcern.com/monday-morning-accounting-news-brief-chief-purpose-officer-dips-out-of-kpmg-dumpster-fire-ey-teases-a-new-quantum-computer-8-3-26/',
    date: '2026-08-03', access: full, locator: section 'Give the PCAOB a Piece of Your Mind on AI Standards' (Castonguay
      quote)}
  last_reviewed: '2026-10-21'
  notes: Idea only. The only source is an AI-written summary page of a podcast episode, so even the company name
    is second-hand; the episode audio and transcript were not available. AI-native audit models are covered more
    fully in the archetype's disruption and frontier files.
```

## 3. Module notes

### 3.1 Processes and key steps (work types)

Cross-links point to existing assurance modules; this file does not restate them.

- **Acceptance, continuance and independence for smaller private clients** (review-assurance). See acceptance-independence. New at this scale: AI-related non-attest services to an attest client raise independence concerns under existing rules (JOFA-ETHICS-2026).
- **Planning and risk assessment** (review-assurance, document-production). See planning-risk-assessment. At this scale the planning file is often built from a prior-year file and a trial balance, and vendors target that start point with risk-suggestion agents (CASEWARE-RISKAGENT-2026).
- **Collecting client data and documents (the PBC list)** (coordination-scheduling, data-reporting). This is the step with least coverage elsewhere in the archetype: Caseware's Client Requests, Response Validation Agent and Document Intelligence Agent target it (use cases 02, 03). Grant Thornton says gtap works with data from any ERP and will go to private company audits first (GT-GTAP-2026). No source describes AI handling of non-ERP client records (QuickBooks files, spreadsheets, bank exports).
- **Fieldwork: tests of controls and details** (review-assurance, transaction-processing). See controls-testing and substantive-testing. The Excel-embedded agent in use case 01 adds a Caseware-specific route.
- **Completion: disclosure checklist, draft statements, review, report** (document-production, review-assurance). See completion-reporting. The Caseware checklist agent's beta result is recorded there; it is repeated under metrics below only for scale.
- **Preparation, compilation and review engagements under SSARS** (document-production, review-assurance). Practitioner CPE for these engagements covers the SSARS hierarchy, going concern, subsequent events, fraud-related risk and documentation, and the 2026 listing read has no AI objective (NYSSCPA-PCR-2026).
- **Firm quality management and peer review** (review-assurance). See quality-management. Firms had to have a system of quality management by 15 December 2025 and peer reviewers now use checklists for it (AICPA-QMPR-2026).

### 3.2 Common pain points

- **Compliance load rivals the audit itself.** The AICPA small-firm column says the effort to manage standards, particularly quality management and peer review, now rivals the time spent performing the audit for many small firms. Firms that audit only occasionally find each engagement feels like starting over (JOFA-SMALLFIRM-2026).
- **Staff capability.** In CPA.com's survey of 54 firms, 66% ranked staff not trained in advanced approaches among the top blockers, 60% poor-quality client data, 53% lack of access to client information and systems, and 53% budget (CPACOM-ATR-2025).
- **Choosing a methodology.** A June 2026 ENGAGE panel was built around how to choose one, with panelists who had each chosen differently (GRF-ENGAGE-2026).
- **Hiring and capacity.** In the AICPA's 2026 top-issues survey (629 respondents) hiring experienced staff ranked first for firms with 11 to 30 employees, and staff workload ranked in the top four for the four larger size groups (JOFA-TOPISSUES-2026).
- **Data protection with free tools.** Caseware's senior vice president warned small firms to read licence terms because large firms can negotiate and small ones cannot (JOFA-AAFOCUS-2025-09).

### 3.3 Metrics and benchmarks

Peer review baseline (non-AI), engagements found nonconforming over engagements reviewed, peer reviews accepted in 2025. Source: each state's annual report, section on nonconforming engagements. The right-hand column is this report's own addition of the four state columns.

| Engagement type | Tennessee | Connecticut | Minnesota | Missouri | Four-state sum |
|---|---|---|---|---|---|
| Single audit | 2 of 11 | 3 of 9 | 3 of 15 | 8 of 22 | 16 of 57 (28%) |
| Other audits under SAS | 8 of 53 | 3 of 39 | 6 of 78 | 6 of 60 | 23 of 230 (10%) |
| Reviews | 13 of 99 | 5 of 63 | 14 of 75 | 11 of 58 | 43 of 295 (15%) |
| Compilations with disclosures | 2 of 44 | 4 of 47 | 5 of 51 | 1 of 20 | 12 of 162 (7%) |
| Compilations omitting disclosures | 5 of 175 | 2 of 67 | 4 of 138 | 3 of 102 | 14 of 482 (3%) |
| All engagement types | 34 of 448 | 18 of 256 | 38 of 418 | 45 of 363 | 135 of 1,485 (9%) |

(TSCPA-PEERREVIEW-2025; CTCPA-PR-2026; MNCPA-PR-2026; MOCPA-PR-2026.) Provenance: independent (state administering entities), but not an AI measure and not a sample of AI users. In the same reports 164 of 191 system reviews passed across these four states plus Oregon (86%): Tennessee 40 of 46, Connecticut 28 of 34, Minnesota 41 of 44, Missouri 23 of 31, Oregon 32 of 36 (OSCPA-PR-2026). Tennessee's 16 system review deficiency reasons were led by engagement performance (6) and monitoring (5); in Missouri human resources, engagement performance and monitoring had 6 each (TSCPA-PEERREVIEW-2025; MOCPA-PR-2026). Oregon's table splits reviews across two rows and is not summed here.

Adoption and attitude benchmarks:

- CPA.com audit survey of 54 firms (not representative): 75% have no formally documented transformation plan; nearly one quarter use no AI or advanced automation; 22% have no automated solution; 89% are not using technology for substantive analytics, and Excel/Power BI is the most common analytics tool. On return on technology, 83% name staff efficiency among their top two outcomes, 54% audit quality or accuracy, 37% cost savings, and 6% do not measure it (CPACOM-ATR-2025, PDF pages 3, 4, 12 and 20).
- AICPA 2026 top-issues survey, 629 respondents: technology and AI change management ranked first for five-year impact in all six size groups, and bolstering quality management made the five-year top five in four of six groups (JOFA-TOPISSUES-2026; AICPA-TOPISSUES-2026).
- ICAEW (UK mid-tier, 35 firms surveyed February and March 2026): 86% have a technology strategy that includes AI; most are not yet sure of the workforce impact (ICAEW-MIDTIER-2026). Adjacent: non-US.
- Caseware beta result for the disclosure checklist agent: 2.7 hours saved per checklist run on average, results varying (vendor-published; CASEWARE-CWX-2026). Verity for Excel: nine hours per engagement and 75% per task in Caseware's testing to date (vendor-published; CASEWARE-VERITYXL-2026).
- CPA.com's 2025 report says some firms report LLM research tools cut document analysis time by 50% or more within audit and advisory; no firm is named (vendor-published; CPACOM-AIACC-2025, executive summary).
- Adjacent (internal audit, not external audit): a Gartner webinar poll of 743 audit professionals found 93% report some AI use and 38% have an AI strategy; Going Concern notes the sample probably leans toward AI enthusiasts (GOINGCONCERN-2026-08-11).
- A Caseware blog cites a survey (not identified) in which 28% of senior audit leaders called their firms very or extremely prepared to reskill staff for AI (vendor-cited; CASEWARE-READINESS-2026).

### 3.4 Guardrails and regulatory points

- **AICPA practice aid, 13 October 2026.** Two parts: a client's use of AI in reporting and controls, and the firm's own use of AI in the audit, including quality management, supervision, review, competence of the team and partner responsibility to know and approve the tools. More content on risk assessment and evidence is planned (AICPA-AIPA-2026; JOFA-AIPA-2026). Its Q&A says AICPA auditing standards do not require telling the client about AI use, but laws, contracts or firm policy may, and some states require licensed professionals to give advance notice of certain AI uses, which can go in the engagement letter (CFODIVE-AIPA-2026).
- **Confidentiality.** Public-practice members face the Confidential Client Information Rule (ET 1.700.001) before pasting client data into an AI system, and consent may be required (JOFA-ETHICS-2026).
- **Texas State Board, August 2026.** Existing rules apply although the Texas rules do not mention generative AI; AI analyses are not audit evidence and do not replace required procedures; audits, reviews and compilations are named; the board suggests documenting how AI was used and what validation was done, without logging every interaction; it lists policy elements (approved tools, confidential-data limits, review and approval, documentation, training, cybersecurity, monitoring of guidance) (TSBPA-2026). One state board only; other boards were not checked.
- **Quality management.** System of quality management required by 15 December 2025 and operating in 2026; peer review checklists test it (AICPA-QMPR-2026).
- **SSARS.** SSARS 27 lets financial statements prepared as part of a consulting engagement fall outside AR-C 70; effective for periods ending on or after 15 December 2026, early adoption allowed. It was prompted by differing readings of SSARS in client advisory practices and does not mention AI (CPACOM-SSARS27-2025; JOFA-AAFOCUS-2025-03).
- **Independence.** Developing or hosting an AI system for an attest client can raise independence concerns under existing non-attest service rules (JOFA-ETHICS-2026).
- **No AI-specific peer review guidance found.** The only peer review item read is the August 2026 QM checklist page (AICPA-QMPR-2026); the checklist report itself is member content and was not read.

### 3.5 Frontier signals (dated, sourced)

1. 2026-10-13: AICPA practice aid on AI for financial statement auditors, with risk-assessment and evidence content to follow (AICPA-AIPA-2026).
2. 2026-10-08: PKF O'Connor Davies, a Top 25 firm, adopts the DAS suite and joins Caseware's Agentic Pioneer Program to co-develop proprietary agents (CASEWARE-PKF-2026).
3. 2026-10-06: Caseware's Risk Suggestion Agent launches worldwide, included at no extra cost in a firm's existing Verity subscription, with a GRF partner quoted (CASEWARE-RISKAGENT-2026).
4. 2026-09-09: Verity for Excel generally available; Client Requests and Response Validation Agent in limited early access (CASEWARE-VERITYXL-2026).
5. 2026-08: AICPA column frames technology and AI as one of several ways small firms keep audit work viable, alongside niche focus, regular audit volume and shared resources (JOFA-SMALLFIRM-2026).
6. 2026-06-25: EisnerAmper reports more than 1,100 professionals on DAS and over 1,500 engagements completed (CASEWARE-EISNERAMPER-2026).
7. 2026-06-17: Caseware states a goal of automating up to 50% of the engagement workflow across the lifecycle; it is a roadmap statement, not a result (CASEWARE-CWX-2026).
8. 2026-05-08: Grant Thornton says gtap goes to private company audits first and public company audits next year (GT-GTAP-2026).
9. 2026-04: FERF finds respondents evenly split on whether auditor AI improved quality and CFOs asking where savings go (FEIDAILY-FERF-2026).
10. 2026-03-09: EisnerAmper announces the in-house EisnerAI Audit Design Agent with Microsoft (EISNER-AUDITAGENT-2026).
11. 2025-10-15: Wolters Kluwer previews its first audit agent inside CCH Axcess Engagement (WK-EXPERTAI-2025). 2025-11-05: Thomson Reuters announces an AI grid for CoCounsel Audit and Audit Intelligence Test with early-adopter claims of up to 70% faster preparation and workpaper review (vendor-published; TR-AGENTIC-2025). Both are the main alternatives to Caseware for small and mid-sized firms.
12. 2026-12-15 (upcoming): SSARS 27 effective for periods ending on or after that date (CPACOM-SSARS27-2025).

### 3.6 Workforce and role effects

- **Informal training is eroding.** A September 2026 trade-press piece says the first two years used to be learned by chasing documents, rekeying data and reconciling across systems, and that AI is absorbing this work without a replacement development model. It proposes structured teaching of source-document literacy and engagement context (CPAPA-STOPTRAIN-2026). Opinion, not data.
- **Juniors supervise, seniors review differently.** A Caseware blog says juniors must understand why a procedure exists in order to supervise an agent running it, and senior reviewers ask what the tool was asked to do and whether the rationale holds. It also reports that at Citrin Cooperman firm-level AI governance sits with the Risk Management Officer and domain policies sit with practice leaders (vendor-published; CASEWARE-READINESS-2026).
- **AI as a teaching aid.** A Withum partner who used Verity in beta likened it to a partner walking a junior through a checklist line by line (CASEWARE-CWX-2026). Citrin Cooperman's assurance innovation leader says seeing the reasoning behind procedures builds judgment (CITRIN-DAS-2026).
- **Capacity framing.** A Thomson Reuters executive says 75% of audit partners are scheduled to retire within ten years, entry-level interest is low, and AI investment is now judged as a workforce solution (vendor interview; TR-STATEAUDIT-2026).
- **Non-traditional skills.** About a third of surveyed firms said they need at least one non-traditional skill and about 20% had hired such staff (CPACOM-ATR-2025, PDF page 20).
- **Small-firm capacity.** The AICPA column suggests contractors, often retired practitioners, for peak periods and shared resources with other small firms, and says stepping away from audit work may be right for a firm that accumulated engagements without building a practice (JOFA-SMALLFIRM-2026).
- **Large-firm counterpoint.** KPMG's US chair and CEO says he sees no significant workforce reduction (reported by Going Concern from Fortune; GOINGCONCERN-2026-10-19). Larger-firm voice; shown only for what is reaching mid-market conversations.

### 3.7 Objections and concerns practitioners raise

- **Hallucinated evidence and supervision failure.** A Bloomberg Tax columnist, quoted by Going Concern, says a firm will eventually have to retract an audit report if AI hallucinated evidence or agents were not supervised. Opinion, and about large-firm and public-company practice (GOINGCONCERN-2026-08-03).
- **Automation bias.** Caseware's senior vice president told the Journal of Accountancy auditors must fight the instinct to trust the output, and not to subordinate their judgment (JOFA-AUDITAI-2026).
- **Client confidentiality and free tools.** See guardrails above (JOFA-AAFOCUS-2025-09; JOFA-ETHICS-2026; TSBPA-2026).
- **Where do the savings go?** CFOs ask this; opinion on whether AI improved audit quality is evenly split; one respondent reported 25 to 30 percent fee cuts after a competitive review (FEIDAILY-FERF-2026). No mid-market data on AI-driven fee cuts found.
- **Vendor claims without method.** Every time-saving figure in this module comes from a vendor or from an unnamed-firm survey (CASEWARE-CWX-2026; CASEWARE-VERITYXL-2026; TR-AGENTIC-2025; CPACOM-AIACC-2025).
- **Viability of small-firm audit practice.** The AICPA column says some small firms should consider leaving audit work (JOFA-SMALLFIRM-2026).
- **Readiness.** Vendor-cited: few senior audit leaders feel ready to reskill (CASEWARE-READINESS-2026).

### 3.8 Interview probes

1. Which audit file and methodology do your private-company engagements run in, who chose it, did you test alternatives side by side, and what would make you change?
2. How does client data actually reach you (ERP export, QuickBooks, spreadsheets, emailed PBC items)? Which step takes most hours before any tool can help, and what do you do when the client's data is poor?
3. Where do you record AI use on the engagement file, and what has your peer reviewer or your quality management monitoring asked about it so far?
4. For preparation, compilation and review engagements, who drafts the statements and disclosures, does anyone use AI there, and how do you keep the independence and no-assurance lines clear?
5. What have clients or audit committees asked about fees or AI since you adopted a tool, and what do you show them?

## 4. Routed to other modules

- **planning-risk-assessment:** Caseware Risk Suggestion Agent worldwide launch and the GRF partner quote (CASEWARE-RISKAGENT-2026); the AICPA practice aid's start-of-engagement question about how far the client relies on AI in reporting, which turns the existing idea entry (06) into one with a published source (AICPA-AIPA-2026); gtap and any-ERP data ingestion (07) (GT-GTAP-2026).
- **completion-reporting:** the 2.7 hours per checklist beta figure and the use of the agent as a quality check on completed checklists are already in entry 01 there (CASEWARE-CWX-2026).
- **quality-management:** Texas board policy elements and documentation advice (TSBPA-2026); Citrin Cooperman's split of firm-level and practice-level AI governance (CASEWARE-READINESS-2026); the AICPA QM peer review checklists (AICPA-QMPR-2026); junior development after AI absorbs rote work (CPAPA-STOPTRAIN-2026, entry 25 there); AI-use disclosure to clients in the engagement letter, now with a practice aid Q&A (CFODIVE-AIPA-2026, entry 24 there).
- **acceptance-independence:** AI-related non-attest services for attest clients (JOFA-ETHICS-2026).
- **substantive-testing:** Verity for Excel overlaps the Excel-agent entries (07, 11, 12); Thomson Reuters Audit Intelligence Test and the Oberlander small-firm quote are already there (TR-AGENTIC-2025).
- **assurance-over-ai and soc-attestation:** the AICPA and AIUC joint SOC 2 plus AIUC-1 offering of 19 October 2026 was seen only as quoted by Going Concern (GOINGCONCERN-2026-10-19); not opened at the source.
- **Future accounting and client advisory archetype (not yet built):** SSARS 27 and AI-prepared statements in outsourced CFO and client advisory work; small-firm tax and bookkeeping AI examples (CPACOM-SSARS27-2025; JOFA-REALLIFE-2026; JOFA-AAFOCUS-2025-03).
- **Internal audit (controls-testing):** the Gartner internal audit poll (GOINGCONCERN-2026-08-11).
- **Economics and disruption files:** the FERF value-perception finding and the KPMG and Grant Thornton UK fee episode (FEIDAILY-FERF-2026).

## 5. Sources

45 sources, all opened and read in full or in the part cited. Types: community 3; conference 3; firm 1; podcast 1; press 5; professional-body 17; regulator 1; survey 4; vendor 10. Going Concern and FEI Daily were read through the r.jina.ai text mirror; all other pages were fetched directly. Sources of type community and podcast are weak: the podcast entry is a machine-written summary page, and Going Concern is commentary.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| AAFCPAS-ENGAGE-2026 | AAFCPAs Takes the Stage at AICPA ENGAGE 2026 | AAFCPAs | conference | https://www.aafcpa.com/?p=29733 | 2026-05-20 | full |
| ACCOUNTINGPODCAST-2026 | Tips to Roll Out AI In Your Firm, AI Squeezing Audit Fees (The Accounting Podcast, episode summary page) | Podwise (The Accounting Podcast) | podcast | https://podwise.ai/episodes/8995231 | 2026-09-25 | full |
| AICPA-AIPA-2026 | AICPA releases guidance to help auditors address the use of AI in financial reporting and auditing | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full |
| AICPA-QMPR-2026 | New QM Peer Review Checklists: What Firms Need to Know (CPEA Report, August 2026; landing page only) | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/resources/article/new-qm-peer-review-checklists-what-firms-need-to-know | 2026-08 | full |
| AICPA-TOPISSUES-2026 | AICPA Survey Cites Change Management for Technology and AI as Top Long-Term Issue Facing Accounting Firms | CPA Practice Advisor | survey | https://www.cpapracticeadvisor.com/2026/06/23/aicpa-survey-cites-change-management-for-technology-and-ai-as-top-long-term-issue-facing-accounting-firms/185547/ | 2026-06-23 | full |
| CASEWARE-CWX-2026 | How Agentic AI Is Transforming Audit: Inside Caseware Verity (CwX 2026 session recap) | Caseware | vendor | https://www.caseware.com/resources/blog/cwx-2026-how-agentic-ai-is-transforming-audit-and-assurance | 2026-06-17 | full |
| CASEWARE-EISNERAMPER-2026 | EisnerAmper Adopts Caseware DAS Suite to Unify Audit Methodology Across Multi-Vertical Practice | Caseware | vendor | https://www.caseware.com/news/eisneramper-leverages-das-powered-by-caseware-to-unify-audit-and-build-an-agentic-future-across-its-multi-vertical-practice | 2026-06-25 | full |
| CASEWARE-PKF-2026 | PKF O'Connor Davies Adopts AI-Enabled DAS Suite Powered by Caseware Verity, and Joins the Caseware Agentic Pioneer Program | Caseware | vendor | https://www.caseware.com/news/pkf-oconnor-davies-adopts-ai-enabled-das-suite-powered-by-caseware-verity-and-joins-the-caseware-agentic-pioneer-program | 2026-10-08 | full |
| CASEWARE-READINESS-2026 | The AI Readiness Gap: Why Audit Firms Aren't Seeing ROI on AI | Caseware | vendor | https://www.caseware.com/resources/blog/the-ai-readiness-gap-why-audit-and-accounting-leaders-arent-seeing-the-value-they-expect | 2026-09-03 | full |
| CASEWARE-RISKAGENT-2026 | Caseware Verity-Powered Risk Suggestion Agent launches to Help Auditors Identify Engagement-Specific Risks | Caseware | vendor | https://www.caseware.com/news/caseware-verity-powered-risk-suggestion-agent-launches-to-help-auditors-identify-engagement-specific-risks | 2026-10-06 | full |
| CASEWARE-VERITYXL-2026 | Caseware Verity for Excel: Agentic AI Connects Client Requests to Audit Workpapers | Caseware | vendor | https://www.caseware.com/news/caseware-puts-agentic-ai-inside-the-audit-connecting-client-requests-to-the-workpaper-with-caseware-verity-for-excel | 2026-09-09 | full |
| CFODIVE-AIPA-2026 | AICPA issues guidance for AI-assisted auditing | CFO Dive | press | https://www.cfodive.com/news/aicpa-issues-guidance-ai-assisted-auditing/832907/ | 2026-10-13 | full |
| CITRIN-DAS-2026 | Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware | Caseware | vendor | https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth | 2026-07-13 | full |
| CPACOM-AIACC-2025 | 2025 AI in Accounting Report | CPA.com | professional-body | https://www.cpa.com/sites/cpa/files/2025-06/2025_AI_in_Accounting_Report.pdf | 2025-06 | full |
| CPACOM-ATR-2025 | 2025 Audit Transformation Report (Audit Benchmark Survey, 54 U.S. firms) | CPA.com (AICPA) | survey | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full |
| CPACOM-SSARS27-2025 | SSARS standard clarification: frequently asked questions (SSARS 27) | CPA.com (AICPA) | professional-body | https://www.cpa.com/sites/cpa/files/2025-08/SSARS_Standard_Clarification_FAQ.pdf | 2025-08 | full |
| CPAPA-STOPTRAIN-2026 | Stop Training CPAs for Yesterday's Work | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/09/02/stop-training-cpas-for-yesterdays-work/189548/ | 2026-09-02 | full |
| CTCPA-PR-2026 | Annual Report on Peer Review Activities, 2025 (Connecticut) | Connecticut Society of CPAs | professional-body | https://www.ctcpas.org/storage/assets/PDFs/Annual%20Report%20on%20PR%20Activities.pdf | 2026-01-12 | full |
| EISNER-AUDITAGENT-2026 | EisnerAmper Rolls Out In-House AI Audit Design Agent | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/20/eisneramper-rolls-out-in-house-ai-audit-design-agent/180020/ | 2026-03-20 | full |
| FEIDAILY-FERF-2026 | Audit Fees Hold Firm, Relationships Are Evolving, and Financial Leaders See Room for More (FERF 16th annual audit fee survey) | FEI Daily (Financial Executives International) | survey | https://daily.financialexecutives.org/FEI-Daily/April-2026/audit-fees-stable-ai-audit-trends-ferf-2024-survey.aspx | 2026-04 | full |
| GOINGCONCERN-2026-08-03 | Monday Morning Accounting News Brief: Chief Purpose Officer dips out of KPMG; EY teases a new quantum computer (8.3.26) | Going Concern | community | https://www.goingconcern.com/monday-morning-accounting-news-brief-chief-purpose-officer-dips-out-of-kpmg-dumpster-fire-ey-teases-a-new-quantum-computer-8-3-26/ | 2026-08-03 | full |
| GOINGCONCERN-2026-08-11 | Audit Leaders Currently in the "Throw AI at the Wall and See What Sticks" Phase | Going Concern | community | https://www.goingconcern.com/audit-leaders-currently-in-the-throw-ai-at-the-wall-and-see-what-sticks-phase/ | 2026-08-11 | full |
| GOINGCONCERN-2026-10-19 | Monday Morning Accounting News Brief: Deloitte Starts the Week With Layoffs; AI Agent Audits Are Here (10.19.26) | Going Concern | community | https://www.goingconcern.com/monday-morning-accounting-news-brief-deloitte-starts-the-week-with-layoffs-ai-agent-audits-are-here-10-19-26/ | 2026-10-19 | full |
| GRF-ENGAGE-2026 | 2026 AICPA & CIMA Engage Conference (GRF CPAs & Advisors event page) | GRF CPAs & Advisors | conference | https://www.grfcpa.com/?p=9081 | 2026-06 | full |
| GT-GTAP-2026 | Grant Thornton U.S. Launches In-House Audit Transformation Platform | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/05/08/grant-thornton-u-s-launches-in-house-audit-transformation-platform/183107/ | 2026-05-08 | full |
| ICAEW-MIDTIER-2026 | Mid-tier firms focused on AI and consolidation | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/mid-tier-firms-focused-on-ai-and-consolidation | 2026-05 | full |
| JOFA-AAFOCUS-2025-03 | A&A Focus recap: Rev rec, AICPA standard setting update, and stablecoins | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/newsletters/a-a-focus/a-a-focus-recap-rev-rec-aicpa-standard-setting-update-and-stablecoins/ | 2025-03-17 | full |
| JOFA-AAFOCUS-2025-09 | A&A Focus recap: AI considerations in A&A, GASB updates, and practical lease accounting challenges | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/newsletters/a-a-focus/aa-focus-recap-ai-considerations-in-aa-gasb-updates-and-practical-lease-accounting-challenges | 2025-09-19 | full |
| JOFA-AIPA-2026 | AI and the audit: AICPA publishes practice aid to assist auditors | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 | full |
| JOFA-AUDITAI-2026 | How AI is transforming the audit - and what it means for CPAs | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/feb/how-ai-is-transforming-the-audit-and-what-it-means-for-cpas/ | 2026-02-01 | full |
| JOFA-ETHICS-2026 | Accounting ethics in the age of AI | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/ | 2026-08-05 | full |
| JOFA-REALLIFE-2026 | Real-life ways small firms are using AI | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/aug/real-life-ways-small-firms-use-ai/ | 2026-08-01 | full |
| JOFA-SMALLFIRM-2026 | What small firm CPAs need to know (Small Firm Q&A, Stephanie Otero) | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/aug/what-small-firm-cpas-need-to-know/ | 2026-08-01 | full |
| JOFA-TOPISSUES-2026 | AICPA Top Issues Survey: Firms' focus on technology rises | Journal of Accountancy (AICPA) | survey | https://www.journalofaccountancy.com/news/2026/jun/aicpa-top-issues-survey-firms-focus-on-technology-rises/ | 2026-06-23 | full |
| MNCPA-PR-2026 | 2025 Annual Report on Peer Review Activities (Minnesota and North Dakota) | Minnesota Society of CPAs | professional-body | https://www.mncpa.org/mncpa/media/Documents-Shared/peer-review/2025-MNCPA-annual-report-on-peer-review-activities.pdf | 2026-01 | full |
| MOCPA-PR-2026 | 2025 Annual Report on Peer Review Activities (Missouri) | Missouri Society of CPAs | professional-body | https://www.mocpa.org/storage/assets/MOCPA/Peer%20Review%20Annual%20Report%202025.pdf | 2026-02-25 | full |
| NYSSCPA-PCR-2026 | Annual Update and Practice Issues for Preparation, Compilation and Review Engagements (webcast listing) | NYSSCPA | conference | https://nysscpa.org/catalog/events/1020413-annual-update-and-practice-issues-for-preparation-compilation-and-review-engagements-webcast-2026-23-07 | 2026-07-23 | full |
| OSCPA-PR-2026 | Annual Report on Peer Review Activities for 2025 (Oregon administering entity) | Oregon Society of CPAs | professional-body | https://www.orcpa.org/storage/assets/Pages/About/Peer%20Review/Annual%20Report%202025.pdf | 2026-03-01 | full |
| RSM-ASKLUCA-2026 | RSM US Launches Ask Luca, Expanding AI Capabilities in the Audit | RSM US LLP | firm | https://rsmus.com/newsroom/2026/rsm-launches-ask-luca.html | 2026-01-08 | full |
| TR-AGENTIC-2025 | Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows | 2025-11-05 | full |
| TR-PEERREVIEW-2026 | How to pass audit peer review with AI | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/passing-peer-review-with-ai/ | 2026-01-23 | full |
| TR-STATEAUDIT-2026 | The state of AI in audit in 2026: Interview with experts | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/state-of-ai-in-audit/ | 2026-03-30 | full |
| TSBPA-2026 | Texas State Board Report, August 2026 (generative AI article), Vol. 168 | Texas State Board of Public Accountancy | regulator | https://www.tsbpa.texas.gov/wp-content/uploads/2026/08/br_082026_web_final.pdf | 2026-08 | full |
| TSCPA-PEERREVIEW-2025 | Annual Report on Peer Review Activities 2025 (Tennessee) | Tennessee Society of CPAs | professional-body | https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf | 2026-03-31 | full |
| WK-EXPERTAI-2025 | Wolters Kluwer Unveils Expert AI for CCH Axcess | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/10/15/wolters-kluwer-unveils-expert-ai-for-cch-axcess/171011/ | 2025-10-15 | full |

Reference-key notes: CITRIN-DAS-2026 and GT-GTAP-2026 reuse the landscape file's keys (GT-GTAP-2026 here is the CPA Practice Advisor article; the landscape key also covers Grant Thornton's own release). CASEWARE-EISNERAMPER-2026, CASEWARE-PKF-2026, CASEWARE-CWX-2026, OSCPA-PR-2026, JOFA-AIPA-2026, AICPA-AIPA-2026, TR-AGENTIC-2025 and CPACOM-ATR-2025 follow the keys the existing assurance archetype uses. TSCPA-PEERREVIEW-2025, AICPA-TOPISSUES-2026, ICAEW-MIDTIER-2026, RSM-ASKLUCA-2026, EISNER-AUDITAGENT-2026, TR-STATEAUDIT-2026, WK-EXPERTAI-2025, ACCOUNTINGPODCAST-2026, CPACOM-AIACC-2025 and AICPA-QMPR-2026 follow the landscape file.

## 6. Gaps

- **Reddit, TaxProTalk and other practitioner forums** could not be read (Reddit returned 403 through the mirror). No community-forum voice from working auditors in this module.
- **No AI in peer review.** None of the five 2025 state reports read (Tennessee, Connecticut, Minnesota, Missouri, Oregon) mentions AI; the AICPA Peer Review Board's QM checklist report (August 2026) is member content and was not read. No finding about AI-assisted files or AI-related deficiencies was found anywhere.
- **No SSARS AI material.** No ARSC, AICPA, state board or firm source on AI in preparation, compilation or review; the CPE listings read have no AI objective. The one commercial guide found that mentions it (analytics on trial balances in compilations and reviews) was not opened and is not used.
- **No measured outcome** for any AI use in a private-company audit, from any named firm. All time-saving figures are vendor-published or from unnamed firms.
- **Non-ERP client data.** No source describes AI handling of QuickBooks files, spreadsheets or other non-ERP records; only generic "any ERP" and poor-data statements.
- **Firm-size breakdown** of the CPA.com audit survey and of the AICPA top-issues survey was not extracted by size group beyond the ranking statements cited.
- **Not reached or not opened at source:** AICPA practice aid text (member-only; read via news release, Journal of Accountancy and CFO Dive); the Caseware beta-results document behind the 2.7-hour figure; the original survey behind the 28% reskilling figure; the AICPA and AIUC release; the Bloomberg Tax column quoted by Going Concern; the podcast audio and transcript; Fieldguide and Jescpa blog pieces on peer review (no publication date could be established, so not used); the VSCPA 2026 AI survey (403).
- **Conference coverage is thin.** ENGAGE 2026 session recaps were not found; only abstracts and one panel listing (GRF-ENGAGE-2026; AAFCPAS-ENGAGE-2026). Other state-society conference sessions and the AICPA Peer Review Conference were not checked beyond the landscape file.
- **Mid-market fee data.** Only large-company fee data and one UK episode; no data on mid-market audit fee changes tied to AI.
