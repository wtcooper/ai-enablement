# Tax data technology: practice angle

Archetype: tax. Module: tax-data-technology (in-house tax operations and data architecture). Angle: practice. Prepared 2026-10-17 (wave 2). Working folder was a private temporary directory.

## 1. Summary

- 16 candidate use cases: grade A 0, B 7, C 8, D 1. No use case reaches grade A: the only named in-house figures (Rover, 80% and 50%) are vendor-published and come from an adjacent indirect-tax reconciliation, so that entry is capped at B.
- 45 distinct sources read or seen (43 opened, 2 search-only). By type: conference 2, firm 6, job-posting 7, press 2, professional-body 1, survey 6, vendor 21.
- Practice is clearest in three places. (1) Job postings from OpenAI, Snowflake, Fortive, Apple and EY show tax functions staffing for a tax data layer, light coding and review of automated pipelines. (2) Vendors are exposing tax platforms to customers' own agents through MCP (Avalara shipped, Kintsugi read-only, Sovos developing) but no customer use is published. (3) Real-time reporting (France's September 2026 mandate) turns master-data quality into a legal-validity issue, and conference accounts say regulators are ahead of the companies they audit.
- Evidence is thin where it matters. Outcomes are vendor-published or anecdotal; there is no independent error-rate, override-rate or parallel-run evidence. The strongest governance signals are survey and event findings: 57.4% of surveyed indirect tax leaders are not confident they could defend AI-assisted decisions to an authority (vendor-sponsored survey), and only two of more than 50 TEI attendees polled said tax owns AI implementation.
- Four landscape statements were not confirmed on the pages opened (see Gaps).

## 2. Use cases

```yaml
- id: tax-data-technology-01
  title: Central tax data layer fed from multiple ERPs, built and run by the tax function
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - data-reporting
  - software-systems
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Tax teams pull data by hand from several ERPs, document stores and third parties, often in unusable formats
    or with missing attributes, before any tax work starts. EY's 2025 survey reports 51% of tax and finance functions
    in the early stages of data management maturity.
  solution: The tax function owns a central tax data lake or warehouse that ingests from multiple ERP and financial
    systems, with data models, ingestion pipelines and reconciled datasets that analytics and AI tools then use.
    Snowflake's own tax analytics team describes building a unified data and knowledge layer as the single source
    of truth for tax. Fortive and Apple advertise roles to architect or oversee the same thing (Fortive names Power
    Platform and Alteryx as automation tools; Apple names pipelines, models and governance standards).
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: null
    source_ref: SNOWFLAKE-JOB-2026
  prerequisites:
  - Tax is included in finance transformation and ERP upgrade decisions (KPMG-SNOWFLAKE-2023).
  - A named owner for data models, versioning and a verified-query or reconciliation library (SNOWFLAKE-JOB-2026).
  - Source-system integrity work so the tax layer is a single source of truth (APPLE-JOB-2026).
  risks_and_guardrails:
  - Fortive's posting requires solutions to be SOX-compliant and auditable (FORTIVE-JOB-2026).
  - Apple's posting requires solutions to comply with internal controls and data security policies and to be documented
    (APPLE-JOB-2026).
  - In the 2026 TR Institute report, fewer than half of surveyed departments got a budget increase, so the build
    competes for scarce funding (TR-CORPTECH-2026).
  human_checkpoints:
  - Tax staff review reconciliations and the results of automated filings and reporting cycles (SNOWFLAKE-JOB-2026).
  - IT and tax agree ERP changes, upgrades and configurations (APPLE-JOB-2026).
  role_evolution: Tax roles in these postings combine tax knowledge with data modelling, SQL or Python and ERP knowledge;
    the Snowflake posting asks the candidate to act as the translation layer between what models can do and what
    the tax function needs (SNOWFLAKE-JOB-2026). EY's survey reports 73% of respondents prioritising the hiring
    of data scientists and tax technology experts (EY-TFO-2025).
  evidence_grade: B
  sources:
  - ref: SNOWFLAKE-JOB-2026
    title: Senior / Staff Analyst, Tax - Finance Analytics & AI
    publisher: Snowflake (via Built In)
    type: job-posting
    url: https://www.builtinla.com/job/senior-staff-analyst-tax-finance-analytics-ai/10335973
    date: '2026-08-18'
    access: full
    locator: 'Role description: ''Tax Intelligence & Unification'' and ''Finance analytics'' sections'
  - ref: FORTIVE-JOB-2026
    title: Director, Global Tax Technology Architect (listed as 'Tax M20')
    publisher: Fortive (via The Ladders)
    type: job-posting
    url: https://www.theladders.com/job/tax-m20-fortive-everett-wa_87489329
    date: '2026'
    access: full
    locator: Key Responsibilities, bullets 3-5 and 7
  - ref: APPLE-JOB-2026
    title: Tax Technology Lead
    publisher: Apple (via AnitaB.org job board)
    type: job-posting
    url: https://jobs.anitab.org/companies/apple/jobs/84254724-tax-technology-lead
    date: '2026-06-25'
    access: full
    locator: Responsibilities, bullets 1-5 and 8
  - ref: EY-TFO-2025
    title: EY report indicates CFOs and tax leaders innovating with AI (EY Tax and Finance Operations Survey)
    publisher: EY
    type: survey
    url: https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments
    date: '2025-11-18'
    access: full
    locator: Section 'The AI and data imperative' and talent section
  - ref: KPMG-SNOWFLAKE-2023
    title: 'Driving Tax value with good data: Leveraging Snowflake solutions with KPMG LLP'
    publisher: KPMG US
    type: firm
    url: https://frv.kpmg.us/kpmg-us/content/dam/kpmg/pdf/2023/driving-tax-value-good-data.pdf
    date: '2023'
    access: full
    locator: 'Opening page: ''Data is everywhere'' and Snowflake approach'
  - ref: TR-CORPTECH-2026
    title: Corporate tax teams eager for AI, but frustrated by pace of change (2026 Corporate Tax Department Technology
      Report)
    publisher: Thomson Reuters Institute with Tax Executives Institute
    type: survey
    url: https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026
    date: '2026-03-16'
    access: full
    locator: Paragraph on budgets
  - ref: OPENAI-JOB-TAXDATA-2025
    title: Senior Manager, Tax Data Automation
    publisher: OpenAI (via Khosla Ventures job board)
    type: job-posting
    url: https://jobs.khoslaventures.com/companies/openai/jobs/45083210-senior-manager-tax-data-automation
    date: '2025-01-22'
    access: full
    locator: 'Responsibilities: SQL-based data pipelines, metadata repositories'
  last_reviewed: '2026-10-17'
  notes: Evidence is job postings and one aggregator copy of Snowflake's posting. The Snowflake posting describes
    a team that already runs this way; Fortive and Apple describe roles to build or oversee it, not completed builds.
    No outcome figure is published for any of the three. OpenAI's 2025 posting for a Senior Manager, Tax Data Automation
    also lists SQL data pipelines and metadata repositories. The Apple posting does not mention AI.
- id: tax-data-technology-02
  title: Plain-language analytics and tax agents over a semantic layer on the tax data
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - data-reporting
  - software-systems
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Tax analysts and directors work in spreadsheets and filings, and refreshing dashboards or spreadsheets
    by hand takes time that could go to analysis and exception handling.
  solution: Snowflake's tax analytics team says it replaced traditional BI workflows with AI agents that encode
    repeatable tax processes, semantic models that let analysts query complex data in plain English, Streamlit apps
    for real-time insight, and workflow automations. The posting names Snowflake's CoCo coding assistant and SnowWork
    as the build environment and asks for verified-query coverage and accuracy iteration based on evaluation metrics.
  outcomes:
  - lever: speed
    description: none published
    figure: null
    measures: null
    source_ref: SNOWFLAKE-JOB-2026
  prerequisites:
  - A reconciled gold-layer data model the semantic layer can sit on (SNOWFLAKE-JOB-2026).
  - A verified query library and evaluation metrics for SQL generation accuracy, iterated with tax analyst feedback
    (SNOWFLAKE-JOB-2026).
  risks_and_guardrails:
  - The posting makes the owner responsible for the contract between the model and its consumers across each tax
    cycle, including versioning (SNOWFLAKE-JOB-2026).
  - At the 2026 TEI seminar attendees described AI errors that fail quietly and politely, which makes review harder
    as volume rises (TEI-TAXTECH-2026).
  human_checkpoints:
  - The posting describes the builder as designing the workflow, writing the prompt and validating the output (SNOWFLAKE-JOB-2026).
  - Tax leadership receives stakeholder summaries and owns exception handling (SNOWFLAKE-JOB-2026).
  role_evolution: The posting expects the engineer to turn work done twice into a reusable agent and to set the
    standard for how agents are built on the team, with tax staff shifting from data preparation to decision-making
    and exception handling (SNOWFLAKE-JOB-2026).
  evidence_grade: B
  sources:
  - ref: SNOWFLAKE-JOB-2026
    title: Senior / Staff Analyst, Tax - Finance Analytics & AI
    publisher: Snowflake (via Built In)
    type: job-posting
    url: https://www.builtinla.com/job/senior-staff-analyst-tax-finance-analytics-ai/10335973
    date: '2026-08-18'
    access: full
    locator: '''About the role'' paragraphs; ''Semantic Layer & Application development''; ''Finance analytics'''
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (event report on the Tax Executives Institute seminar)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Section 'A very bad wizard', paragraphs on silent failure
  last_reviewed: '2026-10-17'
  notes: Single named employer, self-description in a job posting; not independently confirmed. The 'AI-first' framing
    is the employer's own.
- id: tax-data-technology-03
  title: AI-first tax operating model with tax staff who build and review database-driven workflows
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - data-reporting
  - review-assurance
  - software-systems
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Recurring income tax work (compliance, provision, close and reporting) runs on spreadsheets, trackers
    and hand-offs that are slow to review and hard to scale.
  solution: 'OpenAI''s tax team postings describe a move from a traditional compliance and provision function to
    a data-driven, AI-first model in which preparation is increasingly automated in database-driven workflows and
    staff focus on review, validation and improvement of tax outputs, build data models and light automation, and
    use AI tools for analysis, documentation and mappings. The team also wants a leader who defines when AI can
    safely speed up work and when human review or extra controls are needed. This is a pattern not covered by the
    controlled list, so it is recorded as ''other'': tax staff become builders and first-level reviewers of automated
    pipelines.'
  outcomes:
  - lever: capacity
    description: none published
    figure: null
    measures: null
    source_ref: OPENAI-JOB-USTAXOPS-2026
  prerequisites:
  - Tax, finance, data and technical teams partner on data quality and system integration (OPENAI-JOB-USTAXOPS-2026).
  - Staff comfortable with SQL or databases and with working outside Excel-heavy workflows (OPENAI-JOB-USTAXOPS-2026).
  - Experience operating a corporate income tax compliance or provision engine such as Corptax or OneSource Income
    Tax is asked for in the 2025 posting (OPENAI-JOB-TAXDATA-2025).
  risks_and_guardrails:
  - The March 2026 posting asks for familiarity with process design, controls and audit-sensitive environments (OPENAI-JOB-DIRECTTAX-2026).
  - A TEI poll found two hands up out of more than 50 when asked whether the tax function owns AI implementation
    at their company (TEI-TAXTECH-2026).
  human_checkpoints:
  - First-level review and validation of automated provision outputs and data pipelines (OPENAI-JOB-USTAXOPS-2026).
  - Defined points where human review, escalation or added controls are required (OPENAI-JOB-DIRECTTAX-2026).
  role_evolution: 'The April 2026 posting says the role is ''not a traditional tax role'': less return preparation
    and managing external advisors, more review, validation and building data models and AI-assisted processes (OPENAI-JOB-USTAXOPS-2026).
    EY''s survey reports 89% of respondents investing in upskilling and reskilling existing staff (EY-TFO-2025).'
  evidence_grade: B
  sources:
  - ref: OPENAI-JOB-USTAXOPS-2026
    title: Manager, US Tax Operations
    publisher: OpenAI (via Glynn Capital job board)
    type: job-posting
    url: https://jobs.glynncapital.com/companies/openai/jobs/74040402-manager-us-tax-operations
    date: '2026-04-11'
    access: full
    locator: Intro paragraph; 'you will' bullets
  - ref: OPENAI-JOB-DIRECTTAX-2026
    title: Senior Manager, Direct Tax AI Systems and Operations
    publisher: OpenAI (via Glynn Capital job board)
    type: job-posting
    url: https://jobs.glynncapital.com/companies/openai/jobs/72240291-senior-manager-direct-tax-ai-systems-and-operations
    date: '2026-03-26'
    access: full
    locator: Team description and responsibilities bullets 1-6
  - ref: OPENAI-JOB-TAXDATA-2025
    title: Senior Manager, Tax Data Automation
    publisher: OpenAI (via Khosla Ventures job board)
    type: job-posting
    url: https://jobs.khoslaventures.com/companies/openai/jobs/45083210-senior-manager-tax-data-automation
    date: '2025-01-22'
    access: full
    locator: Responsibilities and qualifications
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (event report on the Tax Executives Institute seminar)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Section 'A very bad wizard' (poll) and section 'A very good man' (OpenAI demonstration)
  - ref: EY-TFO-2025
    title: EY report indicates CFOs and tax leaders innovating with AI (EY Tax and Finance Operations Survey)
    publisher: EY
    type: survey
    url: https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments
    date: '2025-11-18'
    access: full
    locator: Talent and reskilling paragraph
  last_reviewed: '2026-10-17'
  notes: Three OpenAI postings (Jan 2025, Mar 2026, Apr 2026) show the direction; no outcome measures. The TR Institute
    recap says OpenAI sent four members of its tax department to demonstrate live automation pipelines; it does
    not give the size of the department, so the landscape's '(four people)' shorthand is not supported. Postings
    state intent and self-description, not independently observed practice.
- id: tax-data-technology-04
  title: Tax-analyst-built data pipelines and automations using AI coding tools
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - software-systems
  - data-reporting
  pattern: bulk-transformation
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Data integrations that tax needs can wait weeks or months in an IT queue, and the Excel-based alternatives
    are fragile.
  solution: At the April 2026 TEI seminar attendees reported building data-integration pipelines with AI coding
    tools in about 15 minutes that would previously have waited about two months in an IT queue, on platforms such
    as Alteryx, Power Platform, Snowflake, Databricks, Microsoft Fabric and Palantir Foundry. Reported uses include
    agentic systems run against historical filings, validation agents that critique their own output, and image-to-text
    extraction from state tax notices. Google and Microsoft showed agent building at the event (TEI-TAXTECH-2026).
  outcomes:
  - lever: speed
    description: Pipeline build time reported as about 15 minutes against about two months in an IT queue; anecdotal,
      no method given
    figure: 15 minutes vs about two months
    measures: Time to build a data-integration pipeline versus the queue wait, as described by the event author
      about attendees; not a measured study
    provenance: self-reported
    source_ref: TR-AUDITOR-2026
  prerequisites:
  - A tooling stack the tax team may use (the poll listed Alteryx, Power Platform, Snowflake, Databricks, Microsoft
    Fabric, Palantir Foundry) (TR-AUDITOR-2026).
  - Light scripting skills in tax staff (OPENAI-JOB-DIRECTTAX-2026).
  risks_and_guardrails:
  - The same recap warns that analysts can deploy pipelines nobody else has reviewed, documented or knows how to
    maintain, and an OpenAI panelist agreed that vibe coding has security implications (TR-AUDITOR-2026).
  - Attendees described Alteryx workflows nobody could explain after the builder left without documenting the logic
    (TEI-TAXTECH-2026).
  - Rising token costs were raised as something that could change the economic case for automation (TEI-TAXTECH-2026).
  human_checkpoints:
  - Review of builder output before deployment is the missing control the recap calls out (TR-AUDITOR-2026).
  - Light 'runbooks and validation checks' are listed in OpenAI's posting (OPENAI-JOB-DIRECTTAX-2026).
  role_evolution: Tax analysts become pipeline builders without an IT hand-off; the recap's speaker says that, at
    the high end, the job has become as much a data science problem as an accounting one (TR-AUDITOR-2026).
  evidence_grade: C
  sources:
  - ref: TR-AUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: Paragraphs beginning 'Attendees ... polled themselves on tooling' and 'The first is to outrun your
      own controls'
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (event report on the Tax Executives Institute seminar)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Sections 'A very good man' and 'A very bad wizard'
  - ref: OPENAI-JOB-DIRECTTAX-2026
    title: Senior Manager, Direct Tax AI Systems and Operations
    publisher: OpenAI (via Glynn Capital job board)
    type: job-posting
    url: https://jobs.glynncapital.com/companies/openai/jobs/72240291-senior-manager-direct-tax-ai-systems-and-operations
    date: '2026-03-26'
    access: full
    locator: Responsibilities bullets 1 and 3
  last_reviewed: '2026-10-17'
  notes: 'Graded C: a secondary event recap with unnamed practitioners, and one named participant (OpenAI) who did
    not give figures. The 15-minute claim is anecdotal and was not verified.'
- id: tax-data-technology-05
  title: 'Governance layer for tax automation: version control, sign-off and evidence logs'
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - software-systems
  - review-assurance
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Under SOX and internal-control frameworks, finance and tax teams must document what an automated process
    ran, when it changed and who approved it; most workflow tools do not keep native run history or version records,
    and key-person risk grows when builders leave.
  solution: 'Savant''s Spring 2026 release added version controls with timestamped snapshots, a sign-off and approval
    step between development and production that enforces segregation of duties, and evidence logs with report templates
    for SOX and ICFR documentation that can be exported to GRC tools. Oxford Industries'' senior director of tax
    and accounting is quoted as saying Savant provided the governance controls and audit documentation to meet that
    standard. The pattern is ''other'': it is a control framework around automations rather than an agentic task
    pattern.'
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: null
    source_ref: SAVANT-SPRING-2026
  prerequisites:
  - Separate development and production environments and named control owners (SAVANT-SPRING-2026).
  - Documented logic so a departing builder does not leave unexplained workflows (TEI-TAXTECH-2026).
  risks_and_guardrails:
  - At the 2026 TEI seminar, a Savant and Oxford Industries session was billed as showing how Oxford's tax team
    deploys AI safely and at scale; no recap of the session was found (SAVANT-TEI-2026).
  - Vendor release; the control claims have not been tested by an auditor in any source found (SAVANT-SPRING-2026).
  human_checkpoints:
  - A designated manager or control owner must approve before a workflow goes live (SAVANT-SPRING-2026).
  - Exceptions are routed for human review before results move downstream (SAVANT-CLAUDE-2026).
  role_evolution: Analysts build and modify workflows in development; managers or control owners approve promotion
    to production, which makes tax automation owners part of the internal control environment (SAVANT-SPRING-2026).
  evidence_grade: B
  sources:
  - ref: SAVANT-SPRING-2026
    title: Savant Spring 2026 Release Delivers SOX Compliance Automation, 5x Faster Processing, and Expanded Enterprise
      Integrations
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/spring-2026-release/
    date: '2026-04-23'
    access: full
    locator: Paragraphs on Version Controls, Sign-off Approvals, Evidence Logs; Oxford quote
  - ref: SAVANT-TEI-2026
    title: Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/
    date: '2026-04-16'
    access: full
    locator: Session description and booth demonstration list
  - ref: SAVANT-CLAUDE-2026
    title: Savant Labs Extends Claude and Copilot into Governed Finance Workflows
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/claude-copilot-finance-workflows/
    date: '2026-06-16'
    access: full
    locator: Paragraph on exceptions routed for human review
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (event report on the Tax Executives Institute seminar)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Section 'A very bad wizard' (undocumented Alteryx workflows; poll)
  - ref: TEI-TECHTAX-2025
    title: '2025 TechTAXcelerate: Unleashing the Future of Tax Technology (webinar series page)'
    publisher: Tax Executives Institute
    type: professional-body
    url: https://www.tei.org/events-education/events/2025-techtaxcelerate-unleashing-future-tax-technology-webinar-series
    date: 2025-11
    access: full
    locator: 'Preliminary agenda: ''Automation Sustainment: Ensuring Deployed Automation Continues to Deliver'''
  last_reviewed: '2026-10-17'
  notes: Named customer (Oxford Industries) is quoted by the vendor; no measurements. The tax function's sustainment
    concern is also a TEI curriculum topic (session listed 17-20 Nov 2025). Savant's release also lists new connectors
    (Oracle Fusion, Microsoft Fabric Lakehouse, SAP HANA / S/4HANA) and the vendor's claim of about five times faster
    processing 'compared to other tools in the market'; that comparison is unsourced and not used as an outcome.
- id: tax-data-technology-06
  title: Scheduled multi-system reconciliation of sales-tax data between the tax engine and the ledger
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - data-reporting
  - review-assurance
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Month-end sales tax reconciliation between source transactions, tax-engine output and returns is done
    in manual spreadsheets.
  solution: 'Rover (pet-care marketplace) rebuilt its monthly sales tax reconciliation in Savant: the workflow pulls
    data from systems including Avalara, reviews taxability, sourcing and tax-rate reasonability, matches transactions,
    reconciles and produces audit-ready outputs on a schedule. Savant also lists multi-system reconciliation across
    ERPs and source documents with data lineage among its TEI demos.'
  outcomes:
  - lever: speed
    description: Rover reduced month-end close time by 80% after replacing manual spreadsheets with the governed
      workflow
    figure: 80%
    measures: Reduction in 'month-end close time' per the release's figure line; the same release's text says the
      company 'reduced its month-end sales tax reconciliation time', so what exactly was timed is not clear; no
      baseline given
    provenance: vendor-published
    source_ref: SAVANT-ROVER-2026
  - lever: cost
    description: Lower data handling costs
    figure: 50%
    measures: Reduction in data handling costs per the release; basis and period not stated
    provenance: vendor-published
    source_ref: SAVANT-ROVER-2026
  prerequisites:
  - Access to the ERP, tax engine and transaction data across systems (SAVANT-ROVER-2026).
  - A reconciliation logic the tax accountant can maintain (SAVANT-ROVER-2026).
  risks_and_guardrails:
  - Figures come from a vendor press release announcing a webinar, not a published study (SAVANT-ROVER-2026).
  - 'Indirect-tax adjacency: the measured process is sales tax reconciliation, so the grade is capped at B for this
    module.'
  human_checkpoints:
  - Outputs are audit-ready on a schedule and reviewed by the tax accountant; exceptions are handled by staff (SAVANT-ROVER-2026;
    SAVANT-CLAUDE-2026).
  role_evolution: Rover's senior tax accountant describes the workflow as running on a schedule and matching transactions
    automatically, so the monthly rebuild of the process is no longer manual work (SAVANT-ROVER-2026).
  evidence_grade: B
  sources:
  - ref: SAVANT-ROVER-2026
    title: Savant and Rover Host Webinar on Accelerating Tax Workflows with AI Automation
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/rover-tax-automation-webinar/
    date: '2026-03-04'
    access: full
    locator: Opening bullets and the paragraph with the Foelber quote and the 80 percent / 50 percent line
  - ref: SAVANT-TEI-2026
    title: Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/
    date: '2026-04-16'
    access: full
    locator: Paragraph listing booth demonstrations
  - ref: SAVANT-CLAUDE-2026
    title: Savant Labs Extends Claude and Copilot into Governed Finance Workflows
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/claude-copilot-finance-workflows/
    date: '2026-06-16'
    access: full
    locator: Paragraph on out-of-the-box agents for bank reconciliation, sales tax automation and close support
  last_reviewed: '2026-10-17'
  notes: 'Named customer, vendor-published figures. The webinar was announced for 2026-03-19; no recording or independent
    check was found. Related and routed: sales tax filing agents (indirect-tax).'
- id: tax-data-technology-07
  title: Agent keeps tax-engine configuration in sync with ERP master data
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - software-systems
  - transaction-processing
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: New legal entities, registrations, warehouse locations, products and customer exemptions set up in the
    ERP must also be set up in the tax engine; manual duplicate maintenance causes mismatches and delays tax collection
    in new locations.
  solution: Vertex Configuration Agent for Microsoft Dynamics 365 monitors master-data changes (business events)
    in Dynamics 365 Finance and Supply Chain and triggers matching configuration updates in the Vertex O Series
    tax engine; it generates notices for each change and uses alerts and review checkpoints for high-impact changes.
    Vertex says it was built with Azure AI Foundry, Copilot Studio, MCP servers and various LLMs. Avalara describes
    a browser agent that guides users through ERP configurations.
  outcomes:
  - lever: speed
    description: none published (data sheet lists faster onboarding and reduced manual synchronisation as benefits,
      without figures)
    figure: null
    measures: null
    source_ref: VERTEX-DATASHEET-2025
  prerequisites:
  - Microsoft Dynamics 365 Finance and Supply Chain and the Vertex O Series tax engine (VERTEX-DATASHEET-2025).
  - 'Clean master data for the five covered areas: legal entities, registrations, warehouse locations, products,
    customer exemptions (VERTEX-DATASHEET-2025).'
  risks_and_guardrails:
  - Human-in-the-loop alerts and review checkpoints validate high-impact changes before they take effect in the
    tax engine (VERTEX-DATASHEET-2025).
  - The data sheet lists a traceable log of tax-impacting changes for audit readiness (VERTEX-DATASHEET-2025).
  human_checkpoints:
  - Tax team validates high-impact configuration changes before they reach the engine (VERTEX-DATASHEET-2025).
  role_evolution: Not stated in the sources; the vendor frames it as reduced manual oversight of configuration (VERTEX-DATASHEET-2025).
  evidence_grade: C
  sources:
  - ref: VERTEX-CONFIGAGENT-2025
    title: Vertex Configuration Agent for Microsoft Dynamics 365 Now Available in the Microsoft Marketplace
    publisher: Vertex Inc.
    type: vendor
    url: https://www.vertexinc.com/sites/default/files/2025-11/press-release-vertex-configuration-agent-for-microsoft-dynamics-365.pdf
    date: '2025-11-18'
    access: full
    locator: Paragraphs 1-2 (availability on 2025-11-18 and function)
  - ref: VERTEX-DATASHEET-2025
    title: Vertex Configuration Agent for Microsoft Dynamics 365 (data sheet)
    publisher: Vertex Inc.
    type: vendor
    url: https://www.vertexinc.com/sites/default/files/2025-11/202511-data-sheet-ai-agent-microsoft-d365.pdf
    date: 2025-11
    access: full
    locator: '''Real-Time Sync'', key features list, ''Human-in-the-Loop to Ensure Governance'''
  - ref: AVALARA-AGENTIC-2025
    title: Avalara Extends AI Leadership with Avi Everywhere, MCP Servers, and Global Compliance Innovations
    publisher: Avalara (PR Newswire)
    type: vendor
    url: https://tools.prnewswire.com/en-us/live/20813/release/20251006EN90727
    date: '2025-10-06'
    access: full
    locator: Section 'Avi Everywhere', browser extension bullet
  last_reviewed: '2026-10-17'
  notes: No named customer or figures in either vendor document. The engine is an indirect-tax determination engine,
    so the engine itself belongs to indirect-tax; the ERP-to-engine data flow is the part recorded here.
- id: tax-data-technology-08
  title: Regulatory-change impact on tax configuration, with proposed fixes executed after approval
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - research-synthesis
  - software-systems
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Rule and format changes must be mapped to each company's entities, registrations and settings, and finding
    and fixing configuration errors depends on support tickets and hand-offs.
  solution: Sovos's March 2026 announcement describes Sovi AI diagnosing root causes of compliance errors, proposing
    fixes and executing corrections once approved, surfacing problems before filing deadlines, and assessing how
    rule changes affect each customer's configuration. Avalara's October 2025 release adds natural-language creation
    and visualisation of compliance rules.
  outcomes:
  - lever: speed
    description: none published
    figure: null
    measures: null
    source_ref: SOVOS-SOVI-2026
  prerequisites:
  - The customer's entity structure, tax registrations and filing history held in the vendor platform (SOVOS-SOVI-2026).
  risks_and_guardrails:
  - Sovos states every recommendation, approval and action is documented, that customer data is kept inside its
    security perimeter and not used to train external models, and that workflows are designed with human oversight
    (SOVOS-SOVI-2026).
  - Capabilities are described as available now or rolling out; no customer use is named (SOVOS-SOVI-2026).
  human_checkpoints:
  - Corrections are executed only after approval by the Sovos user (SOVOS-SOVI-2026).
  role_evolution: Sovos says it plans to extend Ask Sovi into guided, human-approved actions inside the platform
    over time (SOVOS-SOVI-2026).
  evidence_grade: C
  sources:
  - ref: SOVOS-SOVI-2026
    title: Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability
    publisher: Sovos
    type: vendor
    url: https://sovos.com/press-releases/sovos-expands-sovi-ai/
    date: '2026-03-24'
    access: full
    locator: Bullets 'Problem-to-Resolution Guidance' to 'Full Audit Transparency' and closing paragraph on security
      perimeter
  - ref: AVALARA-AGENTIC-2025
    title: Avalara Extends AI Leadership with Avi Everywhere, MCP Servers, and Global Compliance Innovations
    publisher: Avalara (PR Newswire)
    type: vendor
    url: https://tools.prnewswire.com/en-us/live/20813/release/20251006EN90727
    date: '2025-10-06'
    access: full
    locator: '''Advanced Rules with AI Visualization'' paragraph'
  last_reviewed: '2026-10-17'
  notes: Vendor announcements only; no named customer, figure or independent test.
- id: tax-data-technology-09
  title: AI-assisted mapping and error remediation for e-invoicing and real-time reporting interfaces
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - transaction-processing
  - software-systems
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: In clearance and continuous-transaction-control regimes an invoice has no legal force until the authority
    returns its identifier, so a wrong VAT ID, malformed schema or mismatched master data can stop shipments and
    payment and attract penalties. More than 60 jurisdictions have moved or are moving to such regimes, according
    to a 2026 TEI recap.
  solution: Avalara says it uses AI to map standardised invoice fields to country-specific compliance requirements,
    with visual mapping tools and minimal customisation; Sovos describes AI-powered mappings for tax determination
    and filing and error diagnosis and remediation. Sovos reports running France's September 2026 mandate in production,
    with a 1.6% invoice rejection rate; its documents do not say how much of that is due to AI.
  outcomes:
  - lever: quality
    description: Sovos reports a 1.6% invoice rejection rate in live production in France against an estimated market-wide
      rate of about 20%
    figure: 1.6% vs about 20% (estimate)
    measures: Invoice rejection rate during live production, three weeks into France's mandate, per Sovos; the 20%
      is described as an estimated market-wide rate with no source, and the release does not attribute the difference
      to AI
    provenance: vendor-published
    source_ref: SOVOS-FRANCE-2026
  prerequisites:
  - 'Clean master data: the recap lists wrong VAT ID, malformed schema and mismatched master data as rejection causes
    (TR-AUDITOR-2026).'
  - ERP-side reporting layer such as SAP Document and Reporting Compliance, which Roedl describes as generating,
    validating and transmitting e-documents (ROEDL-DRC-2026).
  risks_and_guardrails:
  - Italy's penalty is described as 70% of the disputed VAT for such failures; France's penalties start at 10% of
    VAT due for late submissions (TR-AUDITOR-2026; SOVOS-FRANCE-GOLIVE-2026).
  - The AI contribution is not isolated in any source, so the outcome cannot be credited to AI (SOVOS-FRANCE-2026).
  human_checkpoints:
  - Approval of proposed fixes before execution (SOVOS-SOVI-2026).
  - Review steps for the AI-generated field mappings are not described in the Avalara release (AVALARA-AGENTIC-2025).
  role_evolution: The TEI recap quotes a panelist describing a shift from preparing returns to answering notices
    on data already shared with the authority (TR-AUDITOR-2026).
  evidence_grade: C
  sources:
  - ref: AVALARA-AGENTIC-2025
    title: Avalara Extends AI Leadership with Avi Everywhere, MCP Servers, and Global Compliance Innovations
    publisher: Avalara (PR Newswire)
    type: vendor
    url: https://tools.prnewswire.com/en-us/live/20813/release/20251006EN90727
    date: '2025-10-06'
    access: full
    locator: '''AI-Driven Global E-Invoicing'' bullet'
  - ref: SOVOS-SOVI-2026
    title: Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability
    publisher: Sovos
    type: vendor
    url: https://sovos.com/press-releases/sovos-expands-sovi-ai/
    date: '2026-03-24'
    access: full
    locator: Intro paragraph and error diagnosis bullets
  - ref: SOVOS-FRANCE-2026
    title: 'Three Weeks into France E-Invoicing Mandate: Sovos Hits Unparalleled Production Scale'
    publisher: Sovos
    type: vendor
    url: https://sovos.com/press-releases/three-weeks-into-france-e-invoicing-mandate-sovos-hits-unparalleled-production-scale/
    date: '2026-09-23'
    access: full
    locator: Paragraphs 1-2 (170,000 registrants, 1.6% rejection rate)
  - ref: SOVOS-FRANCE-GOLIVE-2026
    title: Sovos Brings Global 2000 Clients Live in France Ahead of the World's Most Complex E-Invoicing Mandate
    publisher: Sovos
    type: vendor
    url: https://sovos.com/press-releases/sovos-brings-global-2000-clients-live-in-france-ahead-of-the-worlds-most-complex-e-invoicing-mandate/
    date: '2026-08-18'
    access: full
    locator: Paragraphs 2-3 (mandate scope and penalties)
  - ref: TR-AUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: Paragraphs on continuous transaction controls and clearance regimes
  - ref: ROEDL-DRC-2026
    title: Neue Grundarchitektur fuer moderne steuerliche Compliance - SAP DRC
    publisher: Roedl & Partner
    type: firm
    url: https://www.roedl.com/insights/neue-grundarchitektur-fuer-moderne-steuerliche-compliance-sap-drc/
    date: '2026-06-25'
    access: full
    locator: Paragraphs 2-4
  last_reviewed: '2026-10-17'
  notes: The e-invoicing engines themselves fall under indirect-tax; this entry records the interface and data-quality
    step. Sovos also reports 170,000 registrants on its network in France (vendor-published, counts organisations
    registered on Sovos-powered services). The landscape reported SAP DRC agents from a LinkedIn recap; that was
    not reachable here and is not used.
- id: tax-data-technology-10
  title: Digital tax analyst agent that monitors invoice and source data and routes exceptions (idea)
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: Where tax authorities receive structured transaction data in near real time and run analytics before
    audits, the company can no longer prepare at the end of the quarter; the TEI recap quotes panelists saying authorities
    arrive knowing more about transactions than the company's team.
  solution: 'Idea (label: idea). Deloitte''s 2026 scenario paper describes, for a department with advanced AI adoption,
    an agent acting as a digital tax analyst that extracts, validates and cross-checks invoice data, continuously
    monitors transactions and routes exceptions to the right reviewer; for a lower-maturity department it suggests
    using agents to flag common anomalies in source data and account reconciliations for human review. It adds that
    agentic corrections to source data would need to be stored back in the system of record.'
  outcomes:
  - lever: risk
    description: none published
    figure: null
    measures: null
    source_ref: DELOITTE-TTT-2026
  prerequisites:
  - Data integrity and common data models, listed as a decision that applies across all four scenarios (DELOITTE-TTT-2026).
  - Explainability and audit trails, and clear ownership of AI-driven tax outcomes (DELOITTE-TTT-2026).
  risks_and_guardrails:
  - Accountability becomes harder to trace in AI-driven processes, so tax would need to engage earlier in governance
    (DELOITTE-TTT-2026).
  - Some firms are reported to have given up on compliance in favour of a safety margin; a panelist said 'Do not
    do this' (TR-AUDITOR-2026).
  human_checkpoints:
  - Exceptions go to the appropriate human reviewer (DELOITTE-TTT-2026).
  role_evolution: Deloitte describes the department's role shifting from preparation to oversight and interpretation
    in the high-adoption scenarios (DELOITTE-TTT-2026).
  evidence_grade: D
  sources:
  - ref: DELOITTE-TTT-2026
    title: 'Tax Transformation Trends AI report, part three: Riding the wave: A framework to plan for AI'
    publisher: Deloitte Global
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf
    date: 2026-07
    access: full
    locator: Scenario 1 'Limited progress' (recommended response) and Scenario 2 'Advanced automation and systems
      integration' (indirect tax example); 'A combination of scenarios'
  - ref: TR-AUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: Paragraphs on authorities arriving at audits with processed data
  last_reviewed: '2026-10-17'
  notes: 'Idea: a scenario framework, not a deployment. Included because both a Big Four paper and conference panelists
    discuss it. No deployment found.'
- id: tax-data-technology-11
  title: Read-only MCP access to tax-compliance data from general AI assistants
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - data-reporting
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Finance and tax staff must log in to a compliance portal to see nexus, filings and registrations, and
    generic assistants answer from general knowledge rather than the company's numbers.
  solution: Kintsugi's MCP server (from September 2026) gives Claude or ChatGPT read-only access to a customer's
    nexus, transactions, filings, registrations, products, connections and account data through 46 tools in nine
    areas, so users can ask questions such as which filings are due this month. Anrok is also reported to offer
    an MCP server (search extract only; the vendor page was blocked). Avalara's 2025 blog describes an agent answering
    the status of a sales tax return through its MCP servers.
  outcomes:
  - lever: experience
    description: none published
    figure: null
    measures: null
    source_ref: KINTSUGI-MCP-2026
  prerequisites:
  - A login on the vendor platform and an MCP-capable AI client (KINTSUGI-MCP-2026).
  - OAuth 2.1 sign-in and scoped permissions (AVALARA-MCP-2026).
  risks_and_guardrails:
  - Kintsugi says every tool is read-only so the assistant cannot change anything or take action, and that human
    experts verify the numbers behind every filing (KINTSUGI-MCP-2026).
  - Avalara advises least-privilege scopes, periodic consent audits and logging of every tool call, since agents
    are nondeterministic (AVALARA-MCP-2026).
  human_checkpoints:
  - The assistant answers questions only; filings remain checked by the vendor's experts (KINTSUGI-MCP-2026).
  role_evolution: Not stated beyond partners and founders being able to query their own compliance picture without
    portal navigation (KINTSUGI-MCP-2026).
  evidence_grade: C
  sources:
  - ref: KINTSUGI-MCP-2026
    title: 'Kintsugi MCP Server: Ask AI About Your Tax Data'
    publisher: Kintsugi
    type: vendor
    url: https://trykintsugi.com/blog/kintsugi-announces-mcp-server
    date: '2026-09-18'
    access: full
    locator: Paragraphs 2-5 (read-only scope, 46 tools, September 2026)
  - ref: AVALARA-MCP-2025
    title: 'Connecting AI to Tax Automation: How Avalara''s Model Context Protocol Servers Enable Smarter Compliance'
    publisher: Avalara
    type: vendor
    url: https://www.avalara.com/us/en/blog/model-context-protocol-servers-bridge-the-gap.html
    date: '2025-11-06'
    access: full
    locator: Paragraph with the Florida return status example
  - ref: AVALARA-MCP-2026
    title: 'Inside Avalara MCP servers: A developer''s primer for agentic tax and compliance'
    publisher: Avalara
    type: vendor
    url: https://www.avalara.com/us/en/blog/avalara-mcp-servers.html
    date: '2026-05-27'
    access: full
    locator: '''Operational realities'' section'
  - ref: ANROK-MCP-2026
    title: Anrok MCP server (product page)
    publisher: Anrok
    type: vendor
    url: https://www.anrok.com/product/mcp
    date: '2026'
    access: search-only
    locator: Search extract only
  last_reviewed: '2026-10-17'
  notes: Vendor announcements; no customer use. Anrok figures and behaviour (including write actions) are from a
    search extract only and are not relied on.
- id: tax-data-technology-12
  title: Customers' own agents act on tax platforms through vendor-hosted MCP servers
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - transaction-processing
  - software-systems
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Each AI model and each tax system needs custom glue code; tax teams that build their own agents cannot
    call a compliance platform without bespoke integration.
  solution: Avalara says it ships MCP servers for AvaTax, Returns, E-Invoicing and Live Reporting, registrations
    and licence management, exemption certificates, tax content, item classification and cross-border; its examples
    include an accounts-payable agent that validates a vendor invoice, checks for an exemption certificate and files
    the resulting use tax. Sovos says it is developing a Sovos MCP Gateway and expects over time to support agent-to-agent
    orchestration. Vertex says its Dynamics 365 agent was built with MCP servers, and PwC's Agent OS integrates
    agents with internal data through APIs or MCP.
  outcomes:
  - lever: speed
    description: none published (Avalara's CEO says customers are cutting filing times from days to hours, without
      a named customer or method)
    figure: null
    measures: null
    source_ref: AVALARA-AGENTIC-2025
  prerequisites:
  - Active vendor subscription with entitlements to the services called (AVALARA-MCP-2026).
  - An MCP-capable client supporting OAuth 2.1 (AVALARA-MCP-2026).
  - Retry-safe (idempotent) agent flows for tools that file returns or commit transactions (AVALARA-MCP-2026).
  risks_and_guardrails:
  - Least-privilege OAuth scopes, rate-limit handling, and logging every tool call with inputs and response status
    (AVALARA-MCP-2026).
  - Sovos describes governed access with full audit transparency and says the gateway is a foundation under development,
    not a shipped product (SOVOS-SOVI-2026).
  - Vertex's agent keeps human review checkpoints for high-impact changes (VERTEX-DATASHEET-2025).
  human_checkpoints:
  - Not specified for Avalara's write tools beyond the advice on scopes and idempotency (AVALARA-MCP-2026).
  - 'Sovos: governed, human-approved actions are planned over time (SOVOS-SOVI-2026).'
  role_evolution: Avalara frames developers and partners as the audience; tax staff would consume compliance through
    their own agents rather than the vendor application (AVALARA-MCP-2026; SOVOS-SOVI-2026).
  evidence_grade: C
  sources:
  - ref: AVALARA-AGENTIC-2025
    title: Avalara Extends AI Leadership with Avi Everywhere, MCP Servers, and Global Compliance Innovations
    publisher: Avalara (PR Newswire)
    type: vendor
    url: https://tools.prnewswire.com/en-us/live/20813/release/20251006EN90727
    date: '2025-10-06'
    access: full
    locator: '''MCP Servers: The Backbone of Intelligent Interoperable Compliance'' and CEO quote'
  - ref: AVALARA-MCP-2026
    title: 'Inside Avalara MCP servers: A developer''s primer for agentic tax and compliance'
    publisher: Avalara
    type: vendor
    url: https://www.avalara.com/us/en/blog/avalara-mcp-servers.html
    date: '2026-05-27'
    access: full
    locator: Sections 'What's available today', 'What you can build', 'Operational realities'
  - ref: SOVOS-SOVI-2026
    title: Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability
    publisher: Sovos
    type: vendor
    url: https://sovos.com/press-releases/sovos-expands-sovi-ai/
    date: '2026-03-24'
    access: full
    locator: Paragraph on the Sovos MCP Gateway
  - ref: VERTEX-DATASHEET-2025
    title: Vertex Configuration Agent for Microsoft Dynamics 365 (data sheet)
    publisher: Vertex Inc.
    type: vendor
    url: https://www.vertexinc.com/sites/default/files/2025-11/202511-data-sheet-ai-agent-microsoft-d365.pdf
    date: 2025-11
    access: full
    locator: '''Microsoft Tools'' paragraph'
  - ref: PWC-MEGNA-2025
    title: How PwC's tax team is using agentic AI (interview with Dom Megna, US AI Tax Leader)
    publisher: CFO.com
    type: press
    url: https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/
    date: '2025-06-06'
    access: full
    locator: Answer on Agent OS and integration with internal data
  last_reviewed: '2026-10-17'
  notes: Avalara documents the servers and operating practice; no named customer or outcome. The landscape stated
    that Sovos 'added MCP and A2A interoperability'; the opened release says the Sovos MCP Gateway is being developed
    and A2A support is expected over time. Thomson Reuters ONESOURCE MCP support was not found. An unofficial community
    AvaTax MCP server also exists (search extract only; not used).
- id: tax-data-technology-13
  title: Agentic mapping of inbound client data into tax platforms with confidence scores and learning from overrides
  archetype: tax
  module: tax-data-technology
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: Data arrives from clients and third parties in different formats, sometimes unmapped or missing metadata.
    PwC describes K-1 footnotes that staff historically interpreted with guides and training, then reviewed, with
    OCR added for extraction.
  solution: PwC's US AI tax leader says agents trained on how to treat items assess each K-1 footnote, state how
    they interpreted it and give a confidence level. A reviewer sees flagged items, and an override must be explained
    so the agent can learn from it. PwC's Agent OS manages which tools (data mapping, document extraction) each
    agent uses.
  outcomes:
  - lever: capacity
    description: Interviewee says one person reviews where three people used to gather to decide; no measured figures
    figure: null
    measures: null
    provenance: self-reported
    source_ref: PWC-MEGNA-2025
  prerequisites:
  - Historical data to train the agents, plus continuing feedback (PWC-MEGNA-2025).
  - An orchestration layer such as Agent OS to manage tools and monitor agents (PWC-MEGNA-2025).
  risks_and_guardrails:
  - The interviewee says full hand-off is not the model and that 100% confidence is rare (PWC-MEGNA-2025).
  - Policy interpretation and high-touch consulting stay largely human (PWC-MEGNA-2025).
  human_checkpoints:
  - Human review of flagged low-confidence items; overrides must carry a reason (PWC-MEGNA-2025).
  role_evolution: Three people reviewing together become one reviewer plus a learning agent, per the interviewee
    (PWC-MEGNA-2025). PwC also says it keeps legacy tax employees engaged and upskilled (PWC-MEGNA-2025).
  evidence_grade: B
  sources:
  - ref: PWC-MEGNA-2025
    title: How PwC's tax team is using agentic AI (interview with Dom Megna, US AI Tax Leader)
    publisher: CFO.com
    type: press
    url: https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/
    date: '2025-06-06'
    access: full
    locator: Answers 1-3 (data mapping example, confidence and overrides, Agent OS)
  last_reviewed: '2026-10-17'
  notes: 'Firm-side practice (data ingestion into tax platforms) and interview, not a published study. PwC says
    it has over 800 custom GPTs and over 250 agents, including in tax; scope of those counts is the interviewee''s.
    The 70% confidence value in the interview is an illustration, not a measure. Adjacent quality evidence from
    the routed OpenAI and Thrive tax-return pilot: at launch a quarter of returns reached 75% correct field completion,
    and 86% within six weeks (self-reported, vendor-published; this is return preparation, so not used as an outcome
    here).'
- id: tax-data-technology-14
  title: Extraction of unstructured documents and notices into structured tax data
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - transaction-processing
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: State tax notices never arrive in the same format twice, and financial statements, leases and contracts
    need extraction before they feed tax data.
  solution: TEI seminar attendees reported using AI image-to-text solutions to pull structured data out of state
    tax notices. Savant's Spring 2026 release includes more than ten prebuilt document-extraction skills for finance
    document types, and Avalara's Outlook agent scans inbound invoices, validates them for taxes, duties and certificates,
    and passes results to ERP systems.
  outcomes:
  - lever: speed
    description: none published
    figure: null
    measures: null
    source_ref: TR-AUDITOR-2026
  prerequisites:
  - Documents available digitally with source systems to receive the result (AVALARA-AGENTIC-2025).
  - Extraction prompts or skills tuned to document types (SAVANT-SPRING-2026).
  risks_and_guardrails:
  - At the same seminar, someone described an agent admitting it could not open the file and had told the user what
    they wanted to hear (TEI-TAXTECH-2026).
  - Savant states that extraction normally needs custom prompt engineering to deploy effectively (SAVANT-SPRING-2026).
  human_checkpoints:
  - Review of extracted values before they enter tax data (TEI-TAXTECH-2026).
  role_evolution: Not described beyond staff reviewing extracted data (TEI-TAXTECH-2026).
  evidence_grade: C
  sources:
  - ref: TR-AUDITOR-2026
    title: '2026 TEI Tax Technology Seminar: What the auditor already knows'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows
    date: '2026-05-12'
    access: full
    locator: 'Paragraph on tooling poll: image-to-text solutions for state tax notices'
  - ref: SAVANT-SPRING-2026
    title: Savant Spring 2026 Release Delivers SOX Compliance Automation, 5x Faster Processing, and Expanded Enterprise
      Integrations
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/spring-2026-release/
    date: '2026-04-23'
    access: full
    locator: Paragraph on Vision Agent Skills
  - ref: AVALARA-AGENTIC-2025
    title: Avalara Extends AI Leadership with Avi Everywhere, MCP Servers, and Global Compliance Innovations
    publisher: Avalara (PR Newswire)
    type: vendor
    url: https://tools.prnewswire.com/en-us/live/20813/release/20251006EN90727
    date: '2025-10-06'
    access: full
    locator: '''Avi in Outlook'' bullet'
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (event report on the Tax Executives Institute seminar)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Section 'A very bad wizard', first anecdote
  last_reviewed: '2026-10-17'
  notes: The state notice example is unnamed attendees via a vendor-affiliated recap. Notice response itself belongs
    to controversy; return-document extraction (W-2, K-1) belongs to compliance.
- id: tax-data-technology-15
  title: Source-data assembly and reconciliation layer between the close and the tax engines
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - data-reporting
  - review-assurance
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: The close-to-tax handoff is a manual junction; vendors argue that data assembly and reconciliation, not
    the tax calculation, is the binding constraint, and that a provision engine fed unreconciled data needs extensive
    cleanup.
  solution: Kognitos positions an agentic layer beneath the provision and compliance engines that pulls data from
    ledgers and financial statements across entities, reconciles and validates it, and hands clean data to the engines
    with an audit trail. It states that it is not a tax engine. Savant's Spring 2026 release adds connectors to
    Oracle Fusion, SAP S/4HANA and Microsoft Fabric Lakehouse for similar data work.
  outcomes:
  - lever: quality
    description: none published
    figure: null
    measures: null
    source_ref: KOGNITOS-2026
  prerequisites:
  - An established tax engine for calculation, as the vendor says its layer sits beneath it (KOGNITOS-2026).
  - Access to ERP and ledger data across entities (KOGNITOS-2026; SAVANT-SPRING-2026).
  risks_and_guardrails:
  - The source is a vendor blog and cites the 58% under-resourced figure from the 2025 TR Institute survey (KOGNITOS-2026;
    TR-CORPTAX-2025).
  - Audit trails for data preparation matter when the provision feeds audited financial statements (KOGNITOS-2026).
  human_checkpoints:
  - The agent reasons about exceptions and inconsistencies; the vendor does not describe the human review step in
    detail (KOGNITOS-2026).
  role_evolution: 'Vendor claim: tax teams spend less time on data assembly and more on forecasting, modelling and
    advisory work (KOGNITOS-2026).'
  evidence_grade: C
  sources:
  - ref: KOGNITOS-2026
    title: AI for Corporate Tax and Provision Automation (2026)
    publisher: Kognitos
    type: vendor
    url: https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/
    date: '2026-06-17'
    access: full
    locator: Sections on the engine versus data-layer split and the close-to-tax handoff
  - ref: TR-CORPTAX-2025
    title: 'The GenAI paradox: why most tax departments aren''t using AI yet (2025 State of the Corporate Tax Department)'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/
    date: '2025-10-22'
    access: full
    locator: Key insights bullet on 58% under-resourced
  - ref: SAVANT-SPRING-2026
    title: Savant Spring 2026 Release Delivers SOX Compliance Automation, 5x Faster Processing, and Expanded Enterprise
      Integrations
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/spring-2026-release/
    date: '2026-04-23'
    access: full
    locator: Integration enhancements list
  - ref: DELOITTE-TTT-2026
    title: 'Tax Transformation Trends AI report, part three: Riding the wave: A framework to plan for AI'
    publisher: Deloitte Global
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf
    date: 2026-07
    access: full
    locator: 'Scenario 1: agents to flag source-data anomalies and reconciliations'
  last_reviewed: '2026-10-17'
  notes: No named customer. Provision and Pillar Two parts of the blog are routed to their own modules.
- id: tax-data-technology-16
  title: Low-code data preparation and consolidation for tax (the pre-LLM baseline)
  archetype: tax
  module: tax-data-technology
  function: finance-accounting
  work_types:
  - data-reporting
  - transaction-processing
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Large tax departments aggregate data from dozens of templates and sources by hand before provision and
    return work can begin, with errors and key-person dependency.
  solution: Not generative AI. Tools such as Alteryx and Microsoft Power Query consolidate and reconcile data, document
    themselves visually and feed tax engines. DuPont's global tax accounting manager described combining Alteryx
    with ONESOURCE to get one source of information during a stalled ERP upgrade and heavy M&A. An RGP client built
    over 100 process streams (BEAT, state NOL reporting, apportionment) with controls; a telecom and media client
    trained over 100 staff across more than 80 workstreams.
  outcomes:
  - lever: capacity
    description: Over 1,100 man-hours removed by automating routine tax processes at an automotive client
    figure: 1,100+ hours
    measures: Reduction in man-hours from automating tax processes, per RGP; client unnamed; period and baseline
      not stated
    provenance: vendor-published
    source_ref: RGP-2024
  - lever: capacity
    description: More than 500 hours a year saved at a telecom and media client
    figure: 500+ hours per year
    measures: Annual time savings from automating manual tax processes, per Concentrix; client unnamed; measurement
      method not stated
    provenance: vendor-published
    source_ref: CONCENTRIX-2020
  prerequisites:
  - Training for tax staff and ongoing support when source data changes (RGP-2024).
  - A planned path when tax engines or ERPs are upgraded; RGP's client plans to migrate the flows for planned Vertex
    and ONESOURCE upgrades (RGP-2024).
  risks_and_guardrails:
  - RGP designed controls inside the Alteryx processes to protect data integrity (RGP-2024).
  - Concentrix says visual workflows self-document, but TEI attendees in 2026 still described unexplained workflows
    left by departed builders (CONCENTRIX-2020; TEI-TAXTECH-2026).
  human_checkpoints:
  - Tax reviewers verify the visual workflows and outputs (CONCENTRIX-2020).
  role_evolution: Concentrix says it trained business users and teams to build on the new capability themselves
    (CONCENTRIX-2020).
  evidence_grade: B
  sources:
  - ref: DUPONT-TR-2021
    title: How Alteryx and ONESOURCE streamline tax data management and strengthen the tax provision process (Tonya
      Cicconi, DuPont)
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/videos/how-alteryx-and-onesource-helps-company-streamline-and-strengthen
    date: 2021-04
    access: full
    locator: 'Article body: first six paragraphs'
  - ref: RGP-2024
    title: Optimizing Automotive Tax Processes with Alteryx
    publisher: RGP
    type: firm
    url: https://rgp.com/?p=12146
    date: '2024-06-03'
    access: full
    locator: Key aspects list and impact list
  - ref: CONCENTRIX-2020
    title: Workflow Optimization Automates Taxes for Telecom Giant
    publisher: Concentrix
    type: firm
    url: https://www.concentrix.com/insights/case-studies/taxing-process-automated-for-telecom-giant/
    date: 2020-02
    access: full
    locator: Paragraph beginning 'We facilitated the adoption'
  - ref: NUCLEUS-2024
    title: Automate 67 percent of tax processes with Alteryx
    publisher: Nucleus Research
    type: firm
    url: https://nucleusresearch.com/?p=38578
    date: '2024-09-04'
    access: full
    locator: Summary paragraph
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain'
    publisher: Thomson Reuters Institute (event report on the Tax Executives Institute seminar)
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Section 'A very bad wizard'
  last_reviewed: '2026-10-17'
  notes: 'Baseline, not AI: it shows what the AI-built pipelines in UC04 replace and what they inherit (sustainment,
    key-person risk). Capped at B: only DuPont is named and gives no figures; the hours figures are from anonymised
    clients. Nucleus Research reports 67% of tax tasks automated, 5% revenue growth in 18 months and 25,000 hours
    saved in a three-week proof of concept across organisations it interviewed; how those figures were calculated
    and who commissioned them is not stated on the page, so they are not used as outcomes. A BDO case study (32%
    overtime reduction; apportionment results from over a week to hours) was read but has no publication date and
    is excluded.'
```

## 3. Module notes

### Processes and key steps (with work types)

| Step | Work type | What AI changes (sources) |
|---|---|---|
| Extract and ingest ERP and ledger data into a tax data layer | data-reporting, software-systems | Tax-owned warehouse or lake, pipelines built partly with AI coding tools (UC01, UC04) |
| Map and normalise inbound data (trial balance, chart of accounts, entity hierarchy, K-1 items) | transaction-processing, data-reporting | Agents propose mappings with confidence scores; reviewers override (UC13; EY-JOB-2026 lists these structures as the consultant's work) |
| Keep ERP master data and the tax engine in sync (entities, registrations, locations, products, exemptions) | software-systems | Event-driven agent with review checkpoints (UC07) |
| Reconcile ledger, tax engine and returns | review-assurance, data-reporting | Scheduled multi-system reconciliation (UC06, UC15) |
| Build, document, approve and sustain automations | software-systems, review-assurance | Version control, sign-off, evidence logs (UC05); TEI ran an "Automation Sustainment" session in Nov 2025 (TEI-TECHTAX-2025) |
| Send and validate real-time reports and e-invoices; handle rejections | transaction-processing | AI-assisted mapping and error remediation (UC09) |
| Query and report on tax data | data-reporting | Semantic layer, plain-language queries (UC02); read-only MCP access (UC11) |
| Let agents call tax platforms | software-systems | Vendor-hosted MCP servers (UC12) |

### Common pain points

- Fragmented data: 51% of tax and finance functions are in the early stages of data management maturity, and 44% name the inability to execute a sustainable plan for data, AI and technology as their biggest barrier (EY-TFO-2025, survey of 1,600 CFOs and senior finance and tax leaders in 30 jurisdictions).
- Under-resourcing: 58% of corporate tax departments call themselves under-resourced, up from 51% a year earlier; more than half of time goes to reactive work (TR-CORPTAX-2025).
- Slow investment: fewer than half of 170 surveyed tax leaders got a budget increase last year, and most say upgrading tax technology is a relatively low priority at their company (TR-CORPTECH-2026).
- Undocumented automation: Alteryx workflows nobody could explain once the builder left (TEI-TAXTECH-2026). Savant's release notes that most workflow tools lack native run history for SOX (SAVANT-SPRING-2026).
- Governance vacuum: two hands out of more than 50 when asked if tax owns AI implementation (TEI-TAXTECH-2026).
- Adoption hurdles in Germany: IT approvals (47%), data protection requirements (41%) and lack of knowledge (41%) (KPMG-DE-2026; sample size not stated).
- Clearance regimes make bad master data costly: a rejected invoice may carry no legal force until the authority returns an identifier (TR-AUDITOR-2026).

### Metrics and benchmarks (what each figure measures)

| Figure | What it measures, in the source's words | Provenance | Ref |
|---|---|---|---|
| 51% | Tax and finance functions still in the early stages of data management maturity | survey (EY) | EY-TFO-2025 |
| 73% / 89% | Respondents prioritising the hiring of data scientists and tax technology experts / investing in upskilling and reskilling existing staff | survey (EY) | EY-TFO-2025 |
| 53% to 21% | Time tax professional respondents spend on routine activities now, and the level they would like | survey (EY) | EY-TFO-2025 |
| 67% not using GenAI; 57% / 36% / 17% | Corporate tax departments not using GenAI; of departments implementing new technology, shares whose plans include GenAI, machine learning, and exploring agentic AI | survey (TR Institute; sample size not on the page) | TR-CORPTAX-2025 |
| 15.4% | Average share of a tax department's total budget spent on tax technologies and software | survey (TR Institute) | TR-CORPTAX-2025 |
| 67% | Tax professionals who said their company's technology investment enabled a shift toward more proactive tax work | survey, 170 tax leaders | TR-CORPTECH-2026 |
| 71% / 19% | Tax departments using AI tools / actively preparing to implement them; 66% of users report noticeable time savings | survey (KPMG Germany; sample size not stated) | KPMG-DE-2026 |
| 92%; 12.5%; 57.4% | Tax functions using AI in some form; those with specific AI targets or KPIs; those not confident they could defend AI-assisted decisions to a tax authority (176 indirect tax leaders, vendor-sponsored) | survey (Fonoa) | FONOA-2026 |
| 4-6x | Top-quartile "tax readiness" organisations, versus the bottom quartile, more likely to outperform peers on innovation, resilience, workforce capability and enterprise value (2,084 leaders, 25 countries) | survey (KPMG) | KPMG-READINESS-2026 |
| 1.6% vs about 20% | Sovos invoice rejection rate in France production vs an unsourced market estimate | vendor-published | SOVOS-FRANCE-2026 |
| 80% / 50% | Rover: reduction in month-end close time / data handling costs after rebuilding reconciliation | vendor-published | SAVANT-ROVER-2026 |
| 1,100+ hours; 500+ hours per year | Anonymised automaker and telecom clients, hours saved by automating tax processes | vendor-published | RGP-2024; CONCENTRIX-2020 |

**Quality evidence.** None independent for this module. There is no published error rate, override rate, parallel-run result or inspection finding for AI-built tax data pipelines, mappings or agent reconciliations. The nearest items are: PwC's description of a confidence-and-override loop with no figures (PWC-MEGNA-2025); Fonoa's survey that finds most respondents cannot confidently defend AI-assisted decisions (FONOA-2026); the TEI recap's anecdote of an agent that said it could not open a file and had told the user what they wanted to hear (TEI-TAXTECH-2026); and an adjacent tax-return pilot (routed to compliance) that reports field-completion rates (OPENAI-CODEX-2026).

### Guardrails and regulatory points

- SOX and internal controls: Fortive requires SOX-compliant, auditable solutions (FORTIVE-JOB-2026); Apple requires compliance with internal controls and documentation (APPLE-JOB-2026); Savant sells segregation of duties between development and production (SAVANT-SPRING-2026).
- Continuous transaction controls: over 60 jurisdictions are on or moving to them; the EU has a 2030 target for cross-border real-time digital reporting (TR-AUDITOR-2026). France required receipt of e-invoices from 1 Sep 2026, with issuing and near-real-time reporting for large and medium-sized companies; penalties start at 10% of VAT due for late submissions and per-invoice penalties are capped at 25% of the invoice (SOVOS-FRANCE-GOLIVE-2026).
- Defending AI-assisted outputs: a BDO indirect tax partner is quoted in the Fonoa report saying the task is demonstrating a process rather than defending a technology, and a KPMG tax technology leader is quoted separating tool exploration from production-ready, enterprise-wide builds (FONOA-2026).
- Agent access to tax systems: OAuth 2.1, least-privilege scopes, idempotent writes and tool-call logging (AVALARA-MCP-2026); read-only scope by design at Kintsugi (KINTSUGI-MCP-2026).
- Data protection and IT approval are top German adoption hurdles (KPMG-DE-2026).
- Corrections made by agents should be written back to the system of record to keep an audit-ready posture (DELOITTE-TTT-2026).

### Frontier signals (dated)

- 2025-10-06: Avalara announces MCP servers so third-party agents can discover and call its APIs (AVALARA-AGENTIC-2025); by 2026-05-27 it lists servers across the core product stack (AVALARA-MCP-2026).
- 2025-11-18: Vertex Configuration Agent for Dynamics 365 listed in the Microsoft Marketplace (VERTEX-CONFIGAGENT-2025).
- 2026-03-24: Sovos says it is developing a Sovos MCP Gateway, with agent-to-agent orchestration expected over time (SOVOS-SOVI-2026).
- 2026-04 (seminar 27-29 Apr; recap 2026-05-12): TEI attendees describe regulators moving ahead of companies and multinationals compressing multi-year roadmaps into 12- and 18-month cycles (TR-AUDITOR-2026).
- 2026-03-16: Tax professionals expect AI to become central to workflow within one to two years, faster than a year earlier (TR-CORPTECH-2026).
- 2026-06-16: Savant lets conversations in Claude and Copilot run as governed deterministic workflows with human review checkpoints (SAVANT-CLAUDE-2026).
- 2026-08-18: Snowflake's tax analytics posting describes replacing BI workflows with agents and a semantic layer (SNOWFLAKE-JOB-2026).
- 2026-09-18: Kintsugi's read-only MCP server (KINTSUGI-MCP-2026).
- 2026-10-01: Sovos announces the acquisition of Flowie, whose agents run finance and procurement processes on top of ERP systems and would draw on Sovos tax data (SOVOS-FLOWIE-2026). Announced only.

### Workforce and role effects

- Tax teams hire or ask for builders: OpenAI, Fortive, Apple and Snowflake postings combine tax knowledge with SQL, Python or data architecture (OPENAI-JOB-USTAXOPS-2026; FORTIVE-JOB-2026; APPLE-JOB-2026; SNOWFLAKE-JOB-2026).
- Staff shift from preparing to reviewing and validating automated outputs (OPENAI-JOB-USTAXOPS-2026).
- Headcount: 58% of German respondents expect domestic tax headcount to stay constant, 72% abroad (KPMG-DE-2026). 61% of EY respondents expect senior retirements to affect their function significantly (EY-TFO-2025).
- A senior director at TEI is quoted: "You will not survive in this field if you don't have a change mindset" (TEI-TAXTECH-2026).
- Reskilling: 89% invest in upskilling existing staff (EY-TFO-2025).
- Training rollouts can fail when users are not consulted: a tool meant to save two hours took a day (TEI-TAXTECH-2026).

### Objections and concerns practitioners raise

- Silent, polite failures that are hard to review at volume (TEI-TAXTECH-2026).
- Tax rarely owns AI implementation (TEI-TAXTECH-2026).
- Rising token costs could change the economics of automation (TEI-TAXTECH-2026).
- Vibe-coded pipelines with no review, documentation or security thinking (TR-AUDITOR-2026).
- No KPIs: nearly nine in ten under pressure to adopt AI, 12.5% with specific targets (FONOA-2026).
- Giving up on compliance in favour of a safety margin and accepting the audit; the panel rejected it (TR-AUDITOR-2026).
- Vendor governance claims are untested (SAVANT-SPRING-2026).

### Interview probes for an advisor

1. Which system holds the tax team's single source of financial data, who owns its models and mappings, and what happens to them when the ERP is upgraded or replaced?
2. Of the automations (Alteryx, Power Platform, scripts, agents) your team runs, how many have a named owner, documentation, version history and a review step? What happened the last time a builder left?
3. When an agent or pipeline changes a number or a mapping, where is the change logged, who approves it, and is the correction written back to the source system?
4. If you operate in a clearance or continuous-transaction-control country, how often are invoices rejected for master-data reasons, and who fixes them and how fast?
5. Who in the company decides which AI tools tax may use, and how long do IT approval and data protection review take?

## 4. Routed to other modules

| Item | Target module | Source and note |
|---|---|---|
| Tax AI for 1040 and 1041 preparation by 30+ Crete firms: 7,000 returns in the pilot; OpenAI's post says it saves practitioners about a third of preparation time, drafts returns with up to 97% accuracy and raises throughput by about 50% (vendor-published, return preparation) | compliance | OPENAI-CODEX-2026; RUNTIMEWIRE-2026 (dated 2026-08-20) |
| ONESOURCE Sales and Use Tax AI: touchless data import, validation, return mapping and filing; company claims of up to 65% less routine reporting time, 30 to 11 day cycles and up to 75% lower audit exposure | indirect-tax | TR-SUTAI-2026; TR-ONESOURCEPLUS-2025 (also claims 40-60% less preparation time) |
| Exemption certificate validation, HS classification, and Global Classification AI that normalises product data into one product master | indirect-tax | AVALARA-AGENTIC-2025; TR-ONESOURCEPLUS-2025 |
| Avalara AI-powered tax research (one AP user quoted as cutting research time by more than 80%) | research-advisory | AVALARA-AGENTIC-2025 |
| Provision and Pillar Two parts of the data-layer argument (58% under-resourced, close-to-provision handoff) | provision; international-pillar-two | KOGNITOS-2026; EY-TFO-2025 (81% name Pillar Two the most significant regulatory change); APPLE-JOB-2026 (preferred knowledge of Pillar Two reporting) |
| GIR XML as a data-engineering problem (LUCANET-2025, FGS-GIR-2026 from the landscape; not re-opened here) | international-pillar-two | Landscape section 13 |
| State tax notice response and authority-side analytics | controversy | TR-AUDITOR-2026 |
| Tax authority real-time information sharing pilots | governance and evidence angle | Landscape OECD-FTA-2025 (not re-opened here) |
| Microsoft Fabric tax data hub of a Brazilian tax firm (BMTax): figures seen in a search extract only | tax-data-technology (search-only, not used) | BMTAX-MS-2026 |

## 5. Sources

One list. Ref follows PUBLISHER-SHORT-YYYY. Access: full = opened and read; search-only = seen only in search results.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute (event report on the Tax Executives Institute seminar) | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| TR-AUDITOR-2026 | 2026 TEI Tax Technology Seminar: What the auditor already knows | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-auditor-already-knows | 2026-05-12 | full |
| TEI-TECHTAX-2025 | 2025 TechTAXcelerate: Unleashing the Future of Tax Technology (webinar series page) | Tax Executives Institute | professional-body | https://www.tei.org/events-education/events/2025-techtaxcelerate-unleashing-future-tax-technology-webinar-series | 2025-11 | full |
| SAVANT-TEI-2026 | Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 | full |
| SAVANT-SPRING-2026 | Savant Spring 2026 Release Delivers SOX Compliance Automation, 5x Faster Processing, and Expanded Enterprise Integrations | Savant Labs | vendor | https://savantlabs.io/press/spring-2026-release/ | 2026-04-23 | full |
| SAVANT-CLAUDE-2026 | Savant Labs Extends Claude and Copilot into Governed Finance Workflows | Savant Labs | vendor | https://savantlabs.io/press/claude-copilot-finance-workflows/ | 2026-06-16 | full |
| SAVANT-ROVER-2026 | Savant and Rover Host Webinar on Accelerating Tax Workflows with AI Automation | Savant Labs | vendor | https://savantlabs.io/press/rover-tax-automation-webinar/ | 2026-03-04 | full |
| KOGNITOS-2026 | AI for Corporate Tax and Provision Automation (2026) | Kognitos | vendor | https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/ | 2026-06-17 | full |
| KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence (KPMG Germany quick surveys) | KPMG Germany | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-07 | full |
| TR-CORPTAX-2025 | The GenAI paradox: why most tax departments aren't using AI yet (2025 State of the Corporate Tax Department) | Thomson Reuters Institute | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 | full |
| TR-CORPTECH-2026 | Corporate tax teams eager for AI, but frustrated by pace of change (2026 Corporate Tax Department Technology Report) | Thomson Reuters Institute with Tax Executives Institute | survey | https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026 | 2026-03-16 | full |
| EY-TFO-2025 | EY report indicates CFOs and tax leaders innovating with AI (EY Tax and Finance Operations Survey) | EY | survey | https://ey.com/en_gl/newsroom/2025/11/ey-report-indicates-cfos-and-tax-leaders-innovating-with-ai-to-manage-mounting-geopolitical-turbulence-talent-shortages-and-regulatory-developments | 2025-11-18 | full |
| FONOA-2026 | State of Indirect Tax in the AI Era 2026 | Fonoa | survey | https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026 | 2026-06-17 | full |
| KPMG-READINESS-2026 | 2026 KPMG Global Tax Readiness Dividend | KPMG | survey | https://kpmg.com/xx/en/our-insights/transformation/global-tax-readiness-dividend.html | 2026-06-22 | full |
| DELOITTE-TTT-2026 | Tax Transformation Trends AI report, part three: Riding the wave: A framework to plan for AI | Deloitte Global | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf | 2026-07 | full |
| PWC-MEGNA-2025 | How PwC's tax team is using agentic AI (interview with Dom Megna, US AI Tax Leader) | CFO.com | press | https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/ | 2025-06-06 | full |
| OPENAI-JOB-DIRECTTAX-2026 | Senior Manager, Direct Tax AI Systems and Operations | OpenAI (via Glynn Capital job board) | job-posting | https://jobs.glynncapital.com/companies/openai/jobs/72240291-senior-manager-direct-tax-ai-systems-and-operations | 2026-03-26 | full |
| OPENAI-JOB-USTAXOPS-2026 | Manager, US Tax Operations | OpenAI (via Glynn Capital job board) | job-posting | https://jobs.glynncapital.com/companies/openai/jobs/74040402-manager-us-tax-operations | 2026-04-11 | full |
| OPENAI-JOB-TAXDATA-2025 | Senior Manager, Tax Data Automation | OpenAI (via Khosla Ventures job board) | job-posting | https://jobs.khoslaventures.com/companies/openai/jobs/45083210-senior-manager-tax-data-automation | 2025-01-22 | full |
| SNOWFLAKE-JOB-2026 | Senior / Staff Analyst, Tax - Finance Analytics & AI | Snowflake (via Built In) | job-posting | https://www.builtinla.com/job/senior-staff-analyst-tax-finance-analytics-ai/10335973 | 2026-08-18 | full |
| APPLE-JOB-2026 | Tax Technology Lead | Apple (via AnitaB.org job board) | job-posting | https://jobs.anitab.org/companies/apple/jobs/84254724-tax-technology-lead | 2026-06-25 | full |
| FORTIVE-JOB-2026 | Director, Global Tax Technology Architect (listed as 'Tax M20') | Fortive (via The Ladders) | job-posting | https://www.theladders.com/job/tax-m20-fortive-everett-wa_87489329 | 2026 | full |
| EY-JOB-2026 | Toronto - Manager - Tax Technology Transformation | EY Canada careers | job-posting | https://careers.ey.com/ey/job/Toronto-Toronto-Manager-Tax-Technology-Transformation-ON-M5H-0B3/1389659033/ | 2026-09-23 | full |
| AVALARA-AGENTIC-2025 | Avalara Extends AI Leadership with Avi Everywhere, MCP Servers, and Global Compliance Innovations | Avalara (PR Newswire) | vendor | https://tools.prnewswire.com/en-us/live/20813/release/20251006EN90727 | 2025-10-06 | full |
| AVALARA-MCP-2025 | Connecting AI to Tax Automation: How Avalara's Model Context Protocol Servers Enable Smarter Compliance | Avalara | vendor | https://www.avalara.com/us/en/blog/model-context-protocol-servers-bridge-the-gap.html | 2025-11-06 | full |
| AVALARA-MCP-2026 | Inside Avalara MCP servers: A developer's primer for agentic tax and compliance | Avalara | vendor | https://www.avalara.com/us/en/blog/avalara-mcp-servers.html | 2026-05-27 | full |
| SOVOS-SOVI-2026 | Sovos Expands Sovi AI with New Capabilities for Tax Guidance, Intelligent Automation and Agent Interoperability | Sovos | vendor | https://sovos.com/press-releases/sovos-expands-sovi-ai/ | 2026-03-24 | full |
| SOVOS-FRANCE-GOLIVE-2026 | Sovos Brings Global 2000 Clients Live in France Ahead of the World's Most Complex E-Invoicing Mandate | Sovos | vendor | https://sovos.com/press-releases/sovos-brings-global-2000-clients-live-in-france-ahead-of-the-worlds-most-complex-e-invoicing-mandate/ | 2026-08-18 | full |
| SOVOS-FRANCE-2026 | Three Weeks into France E-Invoicing Mandate: Sovos Hits Unparalleled Production Scale | Sovos | vendor | https://sovos.com/press-releases/three-weeks-into-france-e-invoicing-mandate-sovos-hits-unparalleled-production-scale/ | 2026-09-23 | full |
| SOVOS-FLOWIE-2026 | Sovos Acquires Flowie, Launching the Industry's First Agentic Compliant Finance Orchestration Platform | Sovos | vendor | https://sovos.com/press-releases/sovos-acquires-flowie-launching-the-industrys-first-agentic-compliant-finance-orchestration-platform/ | 2026-10-01 | full |
| VERTEX-CONFIGAGENT-2025 | Vertex Configuration Agent for Microsoft Dynamics 365 Now Available in the Microsoft Marketplace | Vertex Inc. | vendor | https://www.vertexinc.com/sites/default/files/2025-11/press-release-vertex-configuration-agent-for-microsoft-dynamics-365.pdf | 2025-11-18 | full |
| VERTEX-DATASHEET-2025 | Vertex Configuration Agent for Microsoft Dynamics 365 (data sheet) | Vertex Inc. | vendor | https://www.vertexinc.com/sites/default/files/2025-11/202511-data-sheet-ai-agent-microsoft-d365.pdf | 2025-11 | full |
| KINTSUGI-MCP-2026 | Kintsugi MCP Server: Ask AI About Your Tax Data | Kintsugi | vendor | https://trykintsugi.com/blog/kintsugi-announces-mcp-server | 2026-09-18 | full |
| ANROK-MCP-2026 | Anrok MCP server (product page) | Anrok | vendor | https://www.anrok.com/product/mcp | 2026 | search-only |
| TR-ONESOURCEPLUS-2025 | Thomson Reuters launches ONESOURCE+, the AI-powered intelligent compliance network | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-onesource-plus-the-ai-powered-intelligent-compliance-network | 2025-11-05 | full |
| TR-SUTAI-2026 | Thomson Reuters launches AI tax compliance solution (ONESOURCE Sales and Use Tax AI) | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk | 2026-01-15 | full |
| DUPONT-TR-2021 | How Alteryx and ONESOURCE streamline tax data management and strengthen the tax provision process (Tonya Cicconi, DuPont) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/videos/how-alteryx-and-onesource-helps-company-streamline-and-strengthen | 2021-04 | full |
| RGP-2024 | Optimizing Automotive Tax Processes with Alteryx | RGP | firm | https://rgp.com/?p=12146 | 2024-06-03 | full |
| CONCENTRIX-2020 | Workflow Optimization Automates Taxes for Telecom Giant | Concentrix | firm | https://www.concentrix.com/insights/case-studies/taxing-process-automated-for-telecom-giant/ | 2020-02 | full |
| NUCLEUS-2024 | Automate 67 percent of tax processes with Alteryx | Nucleus Research | firm | https://nucleusresearch.com/?p=38578 | 2024-09-04 | full |
| KPMG-SNOWFLAKE-2023 | Driving Tax value with good data: Leveraging Snowflake solutions with KPMG LLP | KPMG US | firm | https://frv.kpmg.us/kpmg-us/content/dam/kpmg/pdf/2023/driving-tax-value-good-data.pdf | 2023 | full |
| ROEDL-DRC-2026 | Neue Grundarchitektur fuer moderne steuerliche Compliance - SAP DRC | Roedl & Partner | firm | https://www.roedl.com/insights/neue-grundarchitektur-fuer-moderne-steuerliche-compliance-sap-drc/ | 2026-06-25 | full |
| RUNTIMEWIRE-2026 | OpenAI pitches Codex for tax prep after a 7,000-return pilot | Runtime Wire | press | https://runtimewire.com/article/openai-codex-tax-prep-7000-return-pilot | 2026-08-20 | full |
| OPENAI-CODEX-2026 | Building self-improving tax agents with Codex | OpenAI | vendor | https://openai.com/index/building-self-improving-tax-agents-with-codex/ | 2026 | full |
| BMTAX-MS-2026 | BMTax customer story (Microsoft Fabric tax data hub, Brazil) | Microsoft | vendor | https://www.microsoft.com/en/customers/story/26420-bmtax-azure-openai-in-foundry-models | 2026-04 | search-only |

Notes on individual sources:
- TEI-TAXTECH-2026: Vendor-affiliated recap; author attended, no sample sizes beyond one room poll.
- TR-AUDITOR-2026: Vendor-affiliated recap; panel remarks are paraphrased by the author.
- TEI-TECHTAX-2025: Event held 17-20 Nov 2025; page carries no publication date, so the event month is used.
- KOGNITOS-2026: Vendor blog; page states Kognitos is not a tax engine.
- KPMG-DE-2026: Sample size not stated in the release.
- TR-CORPTAX-2025: Vendor-owned research arm; sample size not stated on the page.
- TR-CORPTECH-2026: 170 tax leaders; full report not opened.
- EY-TFO-2025: 1,600 CFOs and senior finance and tax leaders, 30 jurisdictions, 22 industries; press release only.
- FONOA-2026: Vendor-sponsored; 176 indirect tax leaders.
- KPMG-READINESS-2026: 2,084 senior leaders, 25 countries; landing page only.
- DELOITTE-TTT-2026: Date taken from the PDF creation metadata (2 Jul 2026); the document itself shows no date. Scenario framework, not a survey.
- OPENAI-JOB-DIRECTTAX-2026: Posting no longer accepting applications when read; datePosted from page metadata.
- OPENAI-JOB-USTAXOPS-2026: Posting no longer accepting applications when read.
- OPENAI-JOB-TAXDATA-2025: Posting no longer accepting applications when read.
- SNOWFLAKE-JOB-2026: Removed 2026-09-15 per the aggregator; datePosted from page metadata. Aggregator copy, not Snowflake's own careers page.
- APPLE-JOB-2026: Posting text does not mention AI or agents.
- FORTIVE-JOB-2026: Opened through the r.jina.ai text mirror; the aggregator shows 'More than 3 months ago' on 2026-10-17 and a 404 status, so the exact posting date and year are not confirmed.
- EY-JOB-2026: Consulting (client-facing) role, not an in-house role.
- VERTEX-DATASHEET-2025: Date from the PDF creation metadata (13 Nov 2025) and the file path.
- ANROK-MCP-2026: Page blocked by a bot wall; description known only from a search extract. No date seen.
- DUPONT-TR-2021: Page shows 2021-04-21/22 timestamps; pre-generative-AI baseline.
- RGP-2024: Anonymised client; pre-generative-AI baseline.
- CONCENTRIX-2020: Anonymised client; first published 2020-02-15, page modified 2026-07-22; pre-generative-AI baseline.
- NUCLEUS-2024: Analyst ROI case study; sponsorship not stated on the page opened.
- KPMG-SNOWFLAKE-2023: Older; used for the foundation of the tax data layer only. Year from the file path.
- ROEDL-DRC-2026: German; does not discuss AI.
- OPENAI-CODEX-2026: Opened through the r.jina.ai mirror; page shows no date, so the year only is given. Tax preparation, routed to the compliance module.
- BMTAX-MS-2026: Page returned 403. Figures (45 TB consolidated, 15-25% efficiency, 5 million documents per minute) are search-extract only and are not used in any outcome.

## 6. Gaps

- **Search budget.** The shared web-search allowance ran out after 15 searches, before a planned search for LLM account-mapping accuracy studies and one for independent e-invoice rejection data. Both remain open.
- **No independent quality evidence** (error rates, override rates, parallel runs, inspection findings) for AI in tax data pipelines, mappings, reconciliations or e-invoicing interfaces.
- **No in-house case study with named metrics.** Named in-house organisations (OpenAI, Snowflake, Fortive, Apple, Oxford Industries, Rover, DuPont) appear through job postings, a conference billing, a vendor quote or an old vendor video. The Savant and Oxford Industries TEI session (billed for 28 Apr 2026) has no recap or slides.
- **Postings, not practice.** Job postings show intent and self-description. Fortive's posting date and year are not confirmed (the aggregator shows "more than 3 months ago"). Several postings were closed when read.
- **Blocked or unreachable.** Anrok MCP page (Cloudflare), PwC tax-agent pages, the Microsoft BMTax story (403), the Avalara 9 Apr 2026 release body (prnewswire body did not load), Wolters Kluwer, Bloomberg Tax, ITR (paywalled), the TEI member sessions, OECD Tax Administration 2025. The SAP DRC agent claims (Tax and Compliance Assistant, Sapphire session) are only in a LinkedIn recap seen in a search result and are not used; a SAPinsider benchmark (AI 42%, mandates 35%) is also search-only.
- **Landscape corrections.** (1) The landscape's EY survey figures "80% struggle with foundational data" and "75% in earliest stages of GenAI" are not on the EY press release opened here; the release says 51% are in early stages of data management maturity and 44% name an unsustainable plan for data, AI and technology as the biggest barrier. (2) The landscape's "OpenAI's tax department (four people)" is not supported: the recap says OpenAI sent four members of its tax department. (3) Sovos "added MCP and A2A interoperability" overstates the release, which says a Sovos MCP Gateway is being developed and agent-to-agent support is expected over time. (4) The landscape's Fonoa "8x" is attributed in the page to the small cohort that closed the measurement, governance and defensibility gap, with no more precise cohort definition on the page opened.
- **Dates inferred.** DELOITTE-TTT-2026 (from PDF metadata), VERTEX-DATASHEET-2025 (metadata and file path), TEI-TECHTAX-2025 (event month), DUPONT-TR-2021 (page timestamps), FORTIVE-JOB-2026 (year only), OPENAI-CODEX-2026 (year only). A BDO tax-automation case study with figures was read but has no visible date and was excluded.
- **Not covered:** Oracle's tax agents (none found), Thomson Reuters ONESOURCE MCP support (none found), Corptax, Longview and OneStream data-layer products, Workiva, e-invoicing practice in Poland, Germany, India and Brazil, and customs/payroll data flows.
