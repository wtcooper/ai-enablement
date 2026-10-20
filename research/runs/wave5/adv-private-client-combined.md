# AI in private client services: family-office accounting and reporting, succession and owner advisory, client experience

Run date: 2026-10-20. Archetype: advisory. Module: private-client. Angle: combined (practice, discourse, governance and evidence). Wave 5.

Conventions: every source has a ref in the form PUBLISHER-SHORT-YYYY, reusing the landscape file's refs where the same document appears there. `access: full` means opened and read in this run, directly or through the r.jina.ai mirror where a site blocked curl; `access: search-only` means seen only in search results. Quotations are under 25 words. Survey and vendor figures are as the publisher reports them.

## 1. Summary

**Evidence is thin, and almost all of it is vendor, bank or advisory-firm authored.** There is no independent measurement of AI in this module: no error rates, override rates, parallel-run results or inspection findings for family-office accounting, succession advisory or owner advisory. The only peer-reviewed item (STANFORD-JAR-2026) concerns SME bookkeeping, and the only academic literature review (FSR-FAULHABER-2024) concerns financial planning in general. This file grades no use case A.

**What is in use.** Named deployments are few and small: Masttro's Doc AI at Jefferson River Capital, a single family office with 200+ alternative investments (MASTTRO-JEFFERSON-2026); staff at two named family offices using general assistants for file conversion, Salesforce automation and LP-agreement comparison (FOPRO-AITODAY-2026); and Mercer Advisors' Aspen platform, which the firm says is deployed across 1,100+ wealth professionals (MERCER-ASPEN-2026; adjacent, because Mercer is a wealth platform). The one CPA-firm move found is PKF O'Connor Davies' announced collaboration with Asseta AI to run family-office accounting and reporting on an AI-driven platform (PKF-ASSETA-2026). Kaufman Rossin, Armanino and Wiss publish positioning, not deployments.

**Survey adoption figures are not comparable and one is routinely misread.** Citi reports 22% of family offices using AI for operational tasks or investment analysis, up from 13% (CITI-AIFO-2026). RBC and Campden report that half say AI is embedded and essential to their workflow (RBC-CAMPDEN-2026). Ocorian reports 86% using AI technology (OCORIAN-IFC-2026). The widely quoted J.P. Morgan "65% prioritise AI" is about AI as an investment theme, not operations, as Armanino and CIO both note (ARMANINO-FOTRENDS-2026; AICIO-FOOPTEST-2026). The RBC "85% AI is the top investment pick" is likewise an investment measure (RBC-CAMPDEN-2026).

**Where the field says it is heading.** Practitioners converge on three points: reporting and alternative-investment document intake are the first workable targets; data quality and a system of record come before tools; and people keep relationships, approvals and money movement. Discourse at the April 2026 Family Wealth Report forum described agents moving from answering to executing workflows (WISS-FOAI-2026).

**Governance is by analogy.** No regulator has issued family-office-specific AI guidance. The relevant texts are the IRS OPR guidance on Circular 230 duties (IRS-OPR-2026), FINRA's 2026 GenAI and agents section (FINRA-OVERSIGHT-2026), SEC FY2026 examination priorities on AI representations and supervision (SEC-EXAMPRI-FY2026), and private guidance from Northern Trust, Squire Patton Boggs and ArentFox Schiff.

**Succession and owner advisory:** only ideas. The sources are an FFI Practitioner article (2024), a CPA firm blog (2023) and an Exit Planning Institute webinar page; none reports a deployment or result.

## 2. Use cases

Counts: 16 use cases. Grade A: 0. Grade B: 4. Grade C: 9. Grade D: 3 (all labelled 'Idea').

```yaml
- id: advisory-private-client-01
  title: Family-office accounting and reporting delivered by a CPA firm on an AI-driven, multi-entity platform
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Multi-entity family offices keep accounting, investment reporting and financial operations in separate
    tools and spreadsheets, so closing and consolidating take manual effort and reporting is hard to trust.
  solution: 'A CPA firm adopts one cloud platform that combines the general ledger, bank and cash management, bill
    pay and financial reporting, with AI-powered workflows and automated intercompany reconciliation. Per its release,
    PKF O''Connor Davies plans to use the Asseta AI platform for family-office modernization from initial evaluation
    and implementation through ongoing financial operations. Firm type: large national accounting firm (PKF O''Connor
    Davies calls itself one of the nation''s largest; rank not verified here). Vendor: AI-native startup (Asseta
    AI).'
  outcomes:
  - lever: speed
    description: Vendor says most family offices go live in 8-12 weeks and publishes a 30/60/90-day implementation
      plan ending with reporting fully moved to the platform.
    figure: 8-12 weeks
    measures: Time to go live for 'most family offices', as stated in the vendor's FAQ; no sample or baseline given
    provenance: vendor-published
    source_ref: ASSETA-SITE-2026
  - lever: capacity
    description: Vendor homepage counters for scale of use.
    figure: $125B+ assets on platform; 50+ families onboarded
    measures: Counters on the vendor's homepage; definitions and dates not given
    provenance: vendor-published
    source_ref: ASSETA-SITE-2026
  - lever: speed
    description: Vendor markets closing 'in hours, not days'; no baseline or measurement is published.
    figure: none stated as a number
    measures: Marketing statement on the vendor site about close time; not a tracked metric
    provenance: vendor-published
    source_ref: ASSETA-SITE-2026
  prerequisites:
  - Import of chart of accounts and ownership structure into a sandbox, connection of bank and brokerage accounts,
    and historical data reconciliation (vendor's 30/60/90-day plan)
  - Team training on the new platform (same plan)
  risks_and_guardrails:
  - PKF's release announces a collaboration and says the firm 'plans' to use the platform; it reports no client
    results (PKF-ASSETA-2026).
  - All usage and speed figures are vendor claims; the vendor is a seed-stage company (CPAPA-ASSETASEED-2025).
  - 'Independence: outsourced accounting for a family''s operating company that the same firm audits is generally
    restricted under independence rules; none of the sources read addresses this for family offices (general background,
    unverified in this run).'
  human_checkpoints:
  - Historical data reconciliation is finished and the team trained before go-live (ASSETA-SITE-2026).
  - Armanino describes keeping posting to the books and moving money with people while AI handles lower-risk work
    (ARMANINO-FOTRENDS-2026).
  role_evolution: PKF's release says the platform needs 'experienced advisory support', so the firm's role is positioned
    as selecting, implementing and running the platform for the family office (PKF-ASSETA-2026). No headcount effect
    is reported.
  evidence_grade: C
  sources:
  - ref: PKF-ASSETA-2026
    title: PKF O'Connor Davies Announces Collaboration with Asseta AI to Support Family Office Modernization
    publisher: PKF O'Connor Davies / Business Wire
    type: firm
    url: https://www.businesswire.com/news/home/20260326796176/en/PKF-OConnor-Davies-Announces-Collaboration-with-Asseta-AI-to-Support-Family-Office-Modernization
    date: '2026-03-26'
    access: full
    locator: Release paragraphs 1-3 (collaboration, platform description, PKF plans)
  - ref: ASSETA-SITE-2026
    title: 'Asseta: Family Office General Ledger, Bill Pay, Investments Data, Reconciliations and Reporting (product
      site)'
    publisher: Asseta AI
    type: vendor
    url: https://www.asseta.ai/
    date: 2026-10
    access: full
    locator: Homepage counters; 30/60/90-day implementation panel; FAQ on inter-company activity and go-live
  - ref: CPAPA-ASSETASEED-2025
    title: Asseta AI Raises $4.2M Seed Round to Bolster Family Office Accounting Platform
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/?p=173630
    date: '2025-11-20'
    access: full
    locator: Paragraphs 1-3 (seed round, assets supported, adoption among larger offices)
  - ref: ARMANINO-FOTRENDS-2026
    title: 'Built to Last: The Family Office Trends Defining 2026'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/articles/family-office-trends/
    date: '2026-08-19'
    access: full
    locator: Section on AI as a governance decision
  notes: 'Grade C: one announced firm collaboration plus vendor claims. The vendor''s Nov 2025 release said the
    platform then supported more than $10 billion in assets, with nearly one-third of clients managing over $1 billion;
    the homepage now shows $125B+. The two figures are not reconciled by any source.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-02
  title: AI extraction of capital calls, distribution notices, K-1s and valuation statements into one system of
    record for alternative investments
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Capital calls, distributions, valuation statements and K-1s arrive in each fund manager's own format
    and portal, and staff re-key them into spreadsheets; unfunded commitments and stale marks are reconciled by
    hand.
  solution: 'A document-AI module ingests the PDFs, identifies the key data points and posts a reviewable draft
    to the family office''s reporting platform. At Jefferson River Capital, a single family office, Masttro''s Doc
    AI automated data capture for capital calls, distributions and valuations. Firm type: vendor (Masttro) with
    a named single-family-office customer; Armanino (mid-market firm) names document intake as the usual highest-return
    starting point.'
  outcomes:
  - lever: capacity
    description: Jefferson River Capital's implementation enabled tracking of 200+ alternative investments, per
      the vendor case summary; no time or error figures are published.
    figure: 200+ alternative investments tracked
    measures: Number of alternative investments tracked on the platform, per the vendor's case-study summary bullets
    provenance: vendor-published
    source_ref: MASTTRO-JEFFERSON-2026
  - lever: experience
    description: 'Context for the problem: in an audience poll at a family-office conference, collection of alts
      documents was named the major issue by 36% (extraction 27%, accuracy and consistency 9%).'
    figure: 36%
    measures: Share of the 70+ family offices polled that named collection as the major issue in processing alternative-investment
      documents and data; vendor-reported poll, wording as relayed by the vendor
    provenance: vendor-published
    source_ref: CANOE-FOALTS-2026
  prerequisites:
  - A defined intake process and one system of record for commitments, calls and valuations (ARMANINO-FOTRENDS-2026)
  - Clear view of where documents will live and who needs access (CANOE-FOALTS-2026)
  - Vendor diligence on whether client data trains models, where it is stored and who can access it (ARMANINO-FOTRENDS-2026)
  risks_and_guardrails:
  - Extraction is the step Armanino says puts a reviewable draft in front of a person; accuracy rates are not published
    by anyone in the sources read.
  - Fund managers' formats vary, so an unreviewed extraction can post wrong data to reporting; the Canoe write-up
    lists accuracy and consistency as a challenge (CANOE-FOALTS-2026).
  - FINRA's 2026 report names summarization and information extraction as the top GenAI use case among its member
    firms and lists hallucination and data-sensitivity risks (FINRA-OVERSIGHT-2026); the report addresses member
    firms, so applying it to family offices is by analogy.
  human_checkpoints:
  - A person reviews the extracted draft before it is posted (ARMANINO-FOTRENDS-2026).
  - Capital-call funding instructions are checked against procedure; Canoe cites flagging of wiring-information
    discrepancies as a feature (CANOE-FOALTS-2026).
  role_evolution: Staff move from copying data out of PDFs to reviewing drafts and exceptions. The 2022 Empaxis
    case describes an unnamed Northern California family office whose staff spent about an hour a day on manual
    statement work before bot-based extraction (EMPAXIS-FOSTMT-2022).
  evidence_grade: B
  sources:
  - ref: MASTTRO-JEFFERSON-2026
    title: Jefferson River Capital Single Family Office (case study)
    publisher: Masttro
    type: vendor
    url: https://masttro.com/resources/jefferson-river-capital
    date: '2026'
    access: full
    locator: 'Summary bullets: ''This Case Study Dives Into'''
  - ref: CANOE-FOALTS-2026
    title: 'The Future-Ready Family Office: Navigating alts data with AI-powered precision'
    publisher: Canoe Intelligence
    type: vendor
    url: https://canoeintelligence.com/the-future-ready-family-office-navigating-alts-data-with-ai-powered-precision/
    date: '2026-03-18'
    access: full
    locator: Sections on alts data challenges and the panel case study
  - ref: ARMANINO-FOTRENDS-2026
    title: 'Built to Last: The Family Office Trends Defining 2026'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/articles/family-office-trends/
    date: '2026-08-19'
    access: full
    locator: Section on alternative investments and AI document intake
  - ref: FINRA-OVERSIGHT-2026
    title: '2026 FINRA Annual Regulatory Oversight Report: GenAI: Continuing and Emerging Trends'
    publisher: FINRA
    type: regulator
    url: https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
    date: '2025-12-09'
    access: full
    locator: GenAI section, 'How FINRA Member Firms Use GenAI'
  - ref: EMPAXIS-FOSTMT-2022
    title: How Family Offices Automate Data Extraction for Investment Statements
    publisher: Empaxis
    type: vendor
    url: https://www.empaxis.com/blog/family-offices-automate-data-extraction
    date: '2022-06-30'
    access: full
    locator: Case paragraph on a Northern California family office
  - ref: FOX-MASTTRO-2024
    title: 'From archaic information to AI automation: A blue ocean opportunity for family offices'
    publisher: Family Office Exchange (familyoffice.com), content promoting Masttro Doc AI
    type: vendor
    url: https://familyoffice.com/insights/archaic-information-ai-automation-blue-ocean-opportunity-family-offices
    date: '2024-02-20'
    access: full
    locator: Sections on Doc AI (launched early 2023 per the piece)
  notes: 'Grade B: a named single-family-office customer, no published measurements. The Empaxis case is bot-based
    and unnamed, so it is context only. Vendor-voiced sources throughout.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-03
  title: AI-drafted reporting commentary and consolidated multi-entity reports for principals
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - data-reporting
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Investment reporting is still too manual, and families expect consolidated views across entities, investments
    and cash without waiting weeks for someone to stitch them together.
  solution: Staff use AI to draft reporting commentary, summarize documents and prepare meeting material for review;
    platforms consolidate entity-level numbers into one view. Armanino (mid-market and top-tier advisory firm; rank
    not verified) lists drafting reporting commentary among low-risk, high-leverage starting points where a person
    still signs off.
  outcomes:
  - lever: quality
    description: 'Survey: share of family offices using AI for investment performance reporting more than doubled
      in one year.'
    figure: 16%
    measures: Share of family offices in Citi's 2025 Global Family Office Report survey that use AI for investment
      performance reporting, as shown on Citi's May 2026 page; prior-year value not stated on the page
    provenance: vendor-published
    source_ref: CITI-AIFO-2026
  - lever: experience
    description: 'Survey: most respondents still find investment reporting too manual.'
    figure: 73%
    measures: Share of 2026 RBC/Campden respondents who 'still believe investment reporting is too manual', a top
      concern for three years running; sample size not captured
    provenance: vendor-published
    source_ref: RBC-CAMPDEN-2026
  - lever: capacity
    description: 'Survey: expectation of future use for financial reporting and data visualization.'
    figure: 69%
    measures: Share of 317 UBS family-office clients who think they are likely to use AI for financial reporting
      / data visualization in the next five years (intent, not use)
    provenance: vendor-published
    source_ref: UBS-GFO-2025
  prerequisites:
  - Clean, structured, reconciled data; speakers at a 2026 forum said the data, not the AI, is the bottleneck (WISS-FOAI-2026)
  - A defined process, owners and controls before technology (ARMANINO-FOTRENDS-2026)
  risks_and_guardrails:
  - Hallucination is often a data-governance problem, per a panel speaker (HUBBIS-ETON-2026).
  - Automation bias can turn a decision-support tool into an implicit decision driver (SQUIRE-FOAIRISK-2026).
  - Family offices are advised to define what data AI can access, what needs human review and what the audit trail
    is (ARMANINO-FOTRENDS-2026).
  human_checkpoints:
  - A person signs off on AI-drafted commentary and reports (ARMANINO-FOTRENDS-2026).
  - Final decisions, especially on investments, stay with experienced humans (CITI-AIFO-2026).
  role_evolution: Armanino and Citi both describe staff time shifting from assembling reports to review and strategy
    (ARMANINO-FOTRENDS-2026; CITI-AIFO-2026). The 2025 RBC and Campden report is quoted as predicting a significant
    reduction in staff doing basic accounting or administrative work (WSR-RBC-2025).
  evidence_grade: C
  sources:
  - ref: ARMANINO-FOTRENDS-2026
    title: 'Built to Last: The Family Office Trends Defining 2026'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/articles/family-office-trends/
    date: '2026-08-19'
    access: full
    locator: Sections on consolidated reporting and on AI as a governance decision
  - ref: CITI-AIFO-2026
    title: 'AI in the Family Office: Privacy, Efficiency and Institutional Rigor (Citi Institute)'
    publisher: Citi Institute / Citi Wealth
    type: survey
    url: https://www.citigroup.com/global/insights/ai-in-the-family-office
    date: '2026-05-11'
    access: full
    locator: Survey Highlights; Key Takeaways 3, 4 and 6
  - ref: RBC-CAMPDEN-2026
    title: '2026 RBC and Campden Wealth Report: North American family offices shift from caution to optimism amid
      Great Wealth Transfer, AI acceleration (press release)'
    publisher: RBC Wealth Management with Campden Wealth
    type: survey
    url: https://www.rbcwealthmanagement.com/en-us/newsroom/2026-10-01/2026-rbc-and-campden-wealth-report-north-american-family-offices-shift-from-caution-to-optimism-amid-great-wealth-transfer-ai-acceleration
    date: '2026-09-29'
    access: full
    locator: Section 'AI adoption up, cybersecurity becomes top operational concern'
  - ref: UBS-GFO-2025
    title: Global Family Office Report 2025
    publisher: UBS
    type: survey
    url: https://advisors.ubs.com/mediahandler/media/708870/Global%20Family%20Office%20Report%20_2025_.pdf
    date: '2025-05-21'
    access: full
    locator: Pp. 46-47 (chart and text on possible uses of AI over five years)
  - ref: WSR-RBC-2025
    title: 'Report: North American Family Offices Increasingly Embrace AI And Innovation'
    publisher: Wealth Solutions Report (on the RBC and Campden Wealth 2025 report)
    type: press
    url: https://wealthsolutionsreport.com/2025/10/16/report-north-american-family-offices-increasingly-embrace-ai-and-innovation/
    date: '2025-10-16'
    access: full
    locator: Paragraph quoting the report on staff reduction
  - ref: WISS-FOAI-2026
    title: AI for Family Offices Is Moving From Query to Command
    publisher: Wiss (Wiss Family Office)
    type: firm
    url: https://wiss.com/ai-for-family-offices/
    date: '2026-05-13'
    access: full
    locator: Key takeaways and the section on clean data first
  - ref: HUBBIS-ETON-2026
    title: 'Execution before ambition: Bryan Henning on AI discipline inside family offices'
    publisher: Hubbis (Independent Wealth Management Forum, Dubai 2026 panel)
    type: conference
    url: https://hubbis.com/article/execution-before-ambition-bryan-henning-on-ai-discipline-inside-family-offices
    date: '2026'
    access: full
    locator: Section on data quality
  - ref: SQUIRE-FOAIRISK-2026
    title: 'Family Office Insights: Managing Family Office AI Risk'
    publisher: Squire Patton Boggs
    type: firm
    url: https://www.squirepattonboggs.com/insights/publications/managing-family-office-ai-risk/
    date: 2026-07
    access: full
    locator: Risk section on hallucinations and automation bias
  notes: 'Grade C: survey shares and practitioner statements, no named deployment of this specific step. Survey
    provenance: every family-office survey cited here is published by a bank, administrator or advisory firm that
    sells to family offices, so none is independent in the vocabulary''s sense. Do not read the RBC ''half say AI
    is embedded'' or the Ocorian 86% as figures for reporting alone.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-04
  title: AI help with transaction coding, intercompany reconciliation and month-end close in family-office accounting
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - transaction-processing
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Lean teams code transactions, reconcile accounts across entities and banks, and run the close by hand
    across fragmented systems.
  solution: AI categorizes invoices and transactions, reconciles accounts across entities and banks, and flags anomalies;
    a person reviews the exceptions. Sources name this as where practitioners are trying AI, and one family office's
    controller posting asks the hire to assess AI-assisted tooling for coding, policy audits, allocation and AP
    workflow.
  outcomes:
  - lever: speed
    description: none published for family offices. A named adjacent peer-reviewed study of small-business accounting
      finds genAI adoption associated with productivity gains; no figure is available from the abstract.
    figure: none published
    measures: 'Adjacent evidence only: survey of 277 accountants plus platform data on 79 SMEs (200,000+ transaction
      records); not family offices'
    provenance: independent
    source_ref: STANFORD-JAR-2026
  prerequisites:
  - Clear workflow owners, system of record and bottlenecks mapped before tooling (ARMANINO-FOTRENDS-2026)
  - Defined end state and security and privacy policy before any system goes live (WISS-FOAI-2026)
  risks_and_guardrails:
  - Armanino says offices keep AI away from moving money, posting to the books and final decisions (ARMANINO-FOTRENDS-2026).
  - A written approval and audit trail for AI use is advised (AGILLINK-FOPRED-2026; ARMANINO-FOTRENDS-2026).
  human_checkpoints:
  - Armanino keeps moving money, posting to the books and final decisions in human hands (ARMANINO-FOTRENDS-2026).
  - A person still signs off on AI-prepared work (ARMANINO-FOTRENDS-2026).
  role_evolution: A family-office controller posting scopes AI-assisted tooling inside a role that also owns an
    outsourced-accounting relationship and the close calendar (JOB-FOCONTROLLER-2026). The 2025 RBC and Campden
    report is quoted as predicting fewer staff doing basic accounting (WSR-RBC-2025).
  evidence_grade: C
  sources:
  - ref: FOPRO-AITODAY-2026
    title: How Family Offices Are Using AI Today to Boost Efficiency
    publisher: The Family Office Professional (thefopro.com)
    type: press
    url: https://thefopro.com/how-family-offices-are-using-ai-today-to-boost-efficiency/
    date: '2026-06-08'
    access: full
    locator: Quote from Janet Arzt of Parere Advisory on layering AI into the month-end close
  - ref: WINGSPAN-FOREPORT-2026
    title: 'Reporting: The Family Office''s Easiest Win With AI'
    publisher: Wingspan Legacy Partners
    type: firm
    url: https://wingspanlegacy.com/?p=3770
    date: '2026-06-09'
    access: full
    locator: Paragraph on practitioners leaning on AI for the accounting function including month-end close
  - ref: JOB-FOCONTROLLER-2026
    title: Controller (private family office, Redwood City, California)
    publisher: 'A private family office (job board: Greenhouse)'
    type: job-posting
    url: https://job-boards.greenhouse.io/fo/jobs/5263749007
    date: '2026'
    access: full
    locator: '''What you''ll own'': Systems and process optimization bullet'
  - ref: AGILLINK-FOPRED-2026
    title: Family Office Predictions for 2026
    publisher: Agillink
    type: vendor
    url: https://www.agillink.com/insights/Blog/family-office-predictions-for-2026.html
    date: '2026-01-27'
    access: full
    locator: Section on AI and automation (invoice capture, multi-entity reconciliation, anomaly flagging)
  - ref: ARMANINO-FOTRENDS-2026
    title: 'Built to Last: The Family Office Trends Defining 2026'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/articles/family-office-trends/
    date: '2026-08-19'
    access: full
    locator: AI section
  - ref: STANFORD-JAR-2026
    title: 'Human + AI in Accounting: Early Evidence from the Field (Choi, Xie), Journal of Accounting Research
      64(3), pp. 1333-1373'
    publisher: Stanford GSB listing of the Journal of Accounting Research paper
    type: academic
    url: https://www.gsb.stanford.edu/index%2ephp/node/629989
    date: 2026-06
    access: full
    locator: Abstract
  notes: 'Grade C: interest and vendor/practitioner statements; no named family office reports a deployed close
    or coding workflow in the sources read. Measurements from an adjacent process (SME bookkeeping) would cap any
    grade at B.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-05
  title: General-purpose AI assistants for family-office staff on ad hoc operations tasks (file conversion, automation
    building, planning)
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - document-production
  - software-systems
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Small family-office teams lack specialist skills (for example Salesforce development) and lose time on
    low-value conversion and admin work.
  solution: 'Staff use AI assistants directly. Ford Estates LLC''s investment operations director says assistants
    got the office reasonably close to the code and structure needed for Salesforce automations; Placements Italcan
    Inc. uses AI to convert Excel files to the formats its software needs and to manage trips and travel costs.
    Pattern is ''other'': individual assistant use with no workflow around it.'
  outcomes:
  - lever: capacity
    description: 'Self-reported: the office built Salesforce automations without in-house deep Salesforce development
      experience; no time or cost figure given.'
    figure: none published
    measures: Interview statements by named office staff; no metric
    provenance: self-reported
    source_ref: FOPRO-AITODAY-2026
  prerequisites:
  - Approved tools and a short policy on what data may be entered (NT-FOAIPOLICY-2026)
  risks_and_guardrails:
  - Confidential family, financial, legal, tax, estate and security information should not go into tools outside
    the policy (NT-FOAIPOLICY-2026).
  - Public models may reuse submitted information (AFS-FOAI-2024).
  human_checkpoints:
  - Not described in the sources.
  role_evolution: Generalist staff cover technical work they could not do before; a Wingspan director describes
    picking one specific, tedious task and starting (WINGSPAN-FOREPORT-2026).
  evidence_grade: B
  sources:
  - ref: FOPRO-AITODAY-2026
    title: How Family Offices Are Using AI Today to Boost Efficiency
    publisher: The Family Office Professional (thefopro.com)
    type: press
    url: https://thefopro.com/how-family-offices-are-using-ai-today-to-boost-efficiency/
    date: '2026-06-08'
    access: full
    locator: Quotes from Matthew Espinosa (Ford Estates LLC) and Patricia Saputo (Placements Italcan Inc.)
  - ref: WINGSPAN-FOREPORT-2026
    title: 'Reporting: The Family Office''s Easiest Win With AI'
    publisher: Wingspan Legacy Partners
    type: firm
    url: https://wingspanlegacy.com/?p=3770
    date: '2026-06-09'
    access: full
    locator: Paragraphs on small concrete wins
  - ref: NT-FOAIPOLICY-2026
    title: How to Draft a Family Office AI Policy
    publisher: Northern Trust Institute
    type: firm
    url: https://www.northerntrust.com/united-states/institute/articles/how-to-draft-a-family-office-ai-policy
    date: '2026'
    access: full
    locator: 'Principle: Protect Sensitive Information'
  - ref: AFS-FOAI-2024
    title: 'AI in Family Offices: A Closer Look at Privacy, Confidentiality, and Fiduciary Responsibility'
    publisher: ArentFox Schiff
    type: firm
    url: https://www.afslaw.com/perspectives/ai-law-blog/ai-family-offices-closer-look-privacy-confidentiality-and-fiduciary
    date: '2024-06-24'
    access: full
    locator: Section on privacy and confidentiality
  notes: 'Grade B: two named family offices describe use, with no measurements. Self-reported through a trade interview.
    Pattern ''other'': individual use of a general assistant by one staff member, with no defined workflow.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-06
  title: AI comparison of LP-agreement language and support for fund due-diligence reading in the family office
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - review-assurance
  - research-synthesis
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Family-office staff read and compare long fund documents with little legal support.
  solution: Staff use AI to validate comparisons within LP agreements, compare standard against new language and
    support the due-diligence process. Placements Italcan Inc.'s CEO describes this use; Wingspan reports practitioners
    comparing contract language and pressure-testing LP agreements. Investment selection itself is out of scope
    (regulated advice); only the document-reading step is covered here.
  outcomes:
  - lever: quality
    description: none published; self-reported use only.
    figure: none published
    measures: Interview statement; no metric
    provenance: self-reported
    source_ref: FOPRO-AITODAY-2026
  prerequisites:
  - Approved AI tool that does not retain or train on family documents (ARMANINO-FOTRENDS-2026)
  risks_and_guardrails:
  - Hallucinated or oversimplified legal explanation is documented in an estate-planning example (AFS-FOAI-2024).
  - Legal interpretation should not rest on AI alone (NT-FOAIPOLICY-2026).
  human_checkpoints:
  - Counsel or the responsible executive reviews anything relied on (NT-FOAIPOLICY-2026).
  role_evolution: Family-office principals and staff take a first pass at document comparison before involving counsel;
    the sources do not say counsel's role changed.
  evidence_grade: B
  sources:
  - ref: FOPRO-AITODAY-2026
    title: How Family Offices Are Using AI Today to Boost Efficiency
    publisher: The Family Office Professional (thefopro.com)
    type: press
    url: https://thefopro.com/how-family-offices-are-using-ai-today-to-boost-efficiency/
    date: '2026-06-08'
    access: full
    locator: Quote from Patricia Saputo (Placements Italcan Inc.)
  - ref: WINGSPAN-FOREPORT-2026
    title: 'Reporting: The Family Office''s Easiest Win With AI'
    publisher: Wingspan Legacy Partners
    type: firm
    url: https://wingspanlegacy.com/?p=3770
    date: '2026-06-09'
    access: full
    locator: Paragraph listing contract comparison and LP-agreement pressure-testing
  - ref: NT-FOAIPOLICY-2026
    title: How to Draft a Family Office AI Policy
    publisher: Northern Trust Institute
    type: firm
    url: https://www.northerntrust.com/united-states/institute/articles/how-to-draft-a-family-office-ai-policy
    date: '2026'
    access: full
    locator: 'Principle: Appropriate Use'
  - ref: AFS-FOAI-2024
    title: 'AI in Family Offices: A Closer Look at Privacy, Confidentiality, and Fiduciary Responsibility'
    publisher: ArentFox Schiff
    type: firm
    url: https://www.afslaw.com/perspectives/ai-law-blog/ai-family-offices-closer-look-privacy-confidentiality-and-fiduciary
    date: '2024-06-24'
    access: full
    locator: Fiduciary section (rule against perpetuities example)
  notes: 'Grade B: one named family office, self-reported, no measurements.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-07
  title: AI flagging of payment anomalies and wire-instruction discrepancies alongside procedural controls against
    deepfake fraud
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - review-assurance
  - transaction-processing
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: AI-generated voice, video and writing make payment requests look authentic; family offices are lean,
    rely on informal channels and are likely targets.
  solution: Software flags anomalies in payments and approvals and discrepancies in wiring information, while the
    office adds procedural controls such as dual authorization and verification outside the request channel. Sources
    describe the controls as procedural rather than technical because detection tools lag attackers.
  outcomes:
  - lever: risk
    description: none published for AI flagging; Canoe lists proactive flagging of wiring-information discrepancies
      as a platform feature.
    figure: none published
    measures: Vendor feature description; no detection or false-positive rate given
    provenance: vendor-published
    source_ref: CANOE-FOALTS-2026
  prerequisites:
  - Approval workflows mapped to decision rights, signers and thresholds (AGILLINK-FOPRED-2026)
  - Staff aware that a single remote interaction should not authorize a significant payment (CFO-DEEPFAKE-2026)
  risks_and_guardrails:
  - A research professor quoted says defensive tools are behind and culture and procedure must carry the control
    (CFO-DEEPFAKE-2026).
  - SEC FY2026 priorities direct examiners at AI and polymorphic-malware risks in cybersecurity programs (SEC-EXAMPRI-FY2026).
  human_checkpoints:
  - Dual authorization and verified call-back for money movement (ARMANINO-FOTRENDS-2026; CFO-DEEPFAKE-2026).
  role_evolution: Approval authority stays with named people; offices replace informal email approvals with system
    workflows (AGILLINK-FOPRED-2026).
  evidence_grade: C
  sources:
  - ref: CANOE-FOALTS-2026
    title: 'The Future-Ready Family Office: Navigating alts data with AI-powered precision'
    publisher: Canoe Intelligence
    type: vendor
    url: https://canoeintelligence.com/the-future-ready-family-office-navigating-alts-data-with-ai-powered-precision/
    date: '2026-03-18'
    access: full
    locator: Panel section on proactive flagging of discrepancies in wiring information
  - ref: AGILLINK-FOPRED-2026
    title: Family Office Predictions for 2026
    publisher: Agillink
    type: vendor
    url: https://www.agillink.com/insights/Blog/family-office-predictions-for-2026.html
    date: '2026-01-27'
    access: full
    locator: Section on AI and automation; section on approval workflows
  - ref: ARMANINO-FOTRENDS-2026
    title: 'Built to Last: The Family Office Trends Defining 2026'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/articles/family-office-trends/
    date: '2026-08-19'
    access: full
    locator: Section on continuity and cyber (payment controls)
  - ref: CFO-DEEPFAKE-2026
    title: 'Seeing is no longer believing: deepfakes put a new face on cyber security risk for family offices'
    publisher: Canadian Family Offices
    type: press
    url: https://canadianfamilyoffices.com/special-reports/technology-sr/seeing-is-no-longer-believing-deepfakes-put-a-new-face-on-cyber-security-risk-for-family-offices/
    date: '2026-06-05'
    access: full
    locator: Quotes from Eugene Ng (MNP Digital) and Bruce Watson
  - ref: AJG-CYBER-2026
    title: When Cyber Risk Becomes Physical Risk
    publisher: Gallagher (Arthur J. Gallagher) Private Client
    type: firm
    url: https://www.ajg.com/news-and-insights/when-cyber-risk-becomes-physical-risk/
    date: 2026-09
    access: full
    locator: Page on deepfake exposure; cites a 2025 survey and a Deloitte report (not read)
  - ref: SEC-EXAMPRI-FY2026
    title: Examination Priorities for Fiscal Year 2026
    publisher: SEC Division of Examinations
    type: regulator
    url: https://www.sec.gov/files/2026-exam-priorities.pdf
    date: '2025-11-17'
    access: full
    locator: 'Cybersecurity section (pp. 11-12): AI and polymorphic malware'
  notes: 'Grade C: vendor feature claim plus guidance. Gallagher cites (secondarily) that 83% of family-office advisors
    in a 2025 survey were concerned about deepfakes and that 43% of family offices had a cyberattack in the prior
    12 to 24 months per a Deloitte report; neither original was read, so they are not used as outcomes. RBC''s 2026
    report says 59% name cybersecurity and data breaches the top near-term operational concern (up from 16%).'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-08
  title: AI-enabled platform that coordinates a multidisciplinary family-office service team across planning, tax
    preparation and portfolio work
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - coordination-scheduling
  - client-interaction
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Delivering the resources of a family office through individual advisors means coordinating many services,
    systems and specialists per family.
  solution: 'Mercer Advisors'' Aspen is described as a unified knowledge graph that maps relationships between clients,
    advisory teams and services, integrating with planning, custody and productivity systems. The second generation
    was unveiled in July 2026 and, per the company, is deployed across more than 1,100 wealth professionals. Firm
    type: large RIA and wealth platform (not an accounting firm); portfolio management is regulated advice and tax
    preparation belongs to tax, so only the coordination step is counted here.'
  outcomes:
  - lever: capacity
    description: 'Company statements on scale of use: Aspen deployed across 1,100+ wealth professionals; powers
      hundreds of thousands of discrete actions annually, from plan updates to portfolio management and tax preparation;
      42,000+ clients served.'
    figure: 1,100+ professionals; hundreds of thousands of actions a year
    measures: Company-reported count of wealth professionals with Aspen deployed, and actions per year (definition
      not given), as relayed by InvestmentNews
    provenance: self-reported
    source_ref: MERCER-ASPEN-2026
  prerequisites:
  - Integrations with planning, custodian, CRM and productivity systems (MERCER-ASPEN-2026)
  - An AI-native operating-system partner (Avantos credited in the article)
  risks_and_guardrails:
  - The same article says many wealth firms struggle to quantify what AI investment delivers (MERCER-ASPEN-2026).
  - FINRA and SEC expect supervision, accurate AI representations and logging for registered firms (FINRA-OVERSIGHT-2026;
    SEC-EXAMPRI-FY2026).
  human_checkpoints:
  - Fiduciary professionals remain the advisers to families (MERCER-ASPEN-2026 quote from the president).
  role_evolution: Company says the aim is for each of 450 advisors to deliver the capabilities of a $110B+ family
    office and spend more time with clients (MERCER-ASPEN-2026).
  evidence_grade: B
  sources:
  - ref: MERCER-ASPEN-2026
    title: Mercer Advisors and Compound Planning bet big on AI for family offices
    publisher: InvestmentNews
    type: press
    url: https://www.investmentnews.com/ria-news/mercer-advisors-and-compound-planning-bet-big-on-ai-for-family-offices/267616
    date: '2026-07-30'
    access: full
    locator: Paragraphs on Aspen second generation, knowledge graph, deployment, quotes from Daniel Gourvitch
  - ref: FINRA-OVERSIGHT-2026
    title: '2026 FINRA Annual Regulatory Oversight Report: GenAI: Continuing and Emerging Trends'
    publisher: FINRA
    type: regulator
    url: https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
    date: '2025-12-09'
    access: full
    locator: Regulatory Obligations and Monitoring paragraphs
  - ref: SEC-EXAMPRI-FY2026
    title: Examination Priorities for Fiscal Year 2026
    publisher: SEC Division of Examinations
    type: regulator
    url: https://www.sec.gov/files/2026-exam-priorities.pdf
    date: '2025-11-17'
    access: full
    locator: Emerging Financial Technology (p. 13)
  notes: 'Grade B, capped: a named deployment with company-reported figures, adjacent to this module because Mercer
    is a wealth platform, not an accounting or advisory firm, and its scope includes regulated portfolio work. No
    independent measurement.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-09
  title: 'AI agents that prepare advisor work from the client record: activity summaries, follow-up drafts, service-request
    tickets'
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - client-interaction
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Advisors serving complex families spend time on meeting follow-up and routine requests rather than on
    the relationship.
  solution: 'Compound Planning announced CompoundAI, agents built into its advisor operating system that draw on
    holdings, meeting transcripts and communication history to prepare work for advisor review. A General Assistant
    agent summarizes recent activity and drafts follow-up emails and agendas; a Service Request agent turns tasks
    such as a gift of appreciated stock to a donor-advised fund into a ticket for sign-off. A Hubbis panel also
    describes AI-enabled meeting capture and audit trails to close documentation gaps. Firm type: digital family-office
    and wealth firm (not an accounting firm).'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: Announcement only
    provenance: vendor-published
    source_ref: MERCER-ASPEN-2026
  prerequisites:
  - Full client record (holdings, transcripts, communications) available to the agents (MERCER-ASPEN-2026)
  - Structured capture embedded in redesigned workflows, not added as a tool (HUBBIS-ETON-2026)
  risks_and_guardrails:
  - 'FINRA names agent risks: autonomy without validation, acting beyond scope, auditability, sensitive data, limited
    domain knowledge (FINRA-OVERSIGHT-2026).'
  - The announcement says the agents prepare work for an advisor's review rather than only answering questions (MERCER-ASPEN-2026).
  human_checkpoints:
  - Advisor review and sign-off of drafts and tickets (MERCER-ASPEN-2026).
  role_evolution: Compound's chief executive says the technology is built to accelerate and augment the advisor-client
    relationship, not replace it (MERCER-ASPEN-2026).
  evidence_grade: C
  sources:
  - ref: MERCER-ASPEN-2026
    title: Mercer Advisors and Compound Planning bet big on AI for family offices
    publisher: InvestmentNews
    type: press
    url: https://www.investmentnews.com/ria-news/mercer-advisors-and-compound-planning-bet-big-on-ai-for-family-offices/267616
    date: '2026-07-30'
    access: full
    locator: Paragraphs on Compound Planning and CompoundAI
  - ref: HUBBIS-ETON-2026
    title: 'Execution before ambition: Bryan Henning on AI discipline inside family offices'
    publisher: Hubbis (Independent Wealth Management Forum, Dubai 2026 panel)
    type: conference
    url: https://hubbis.com/article/execution-before-ambition-bryan-henning-on-ai-discipline-inside-family-offices
    date: '2026'
    access: full
    locator: Section on documentation gaps and AI-enabled capture
  - ref: FINRA-OVERSIGHT-2026
    title: '2026 FINRA Annual Regulatory Oversight Report: GenAI: Continuing and Emerging Trends'
    publisher: FINRA
    type: regulator
    url: https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
    date: '2025-12-09'
    access: full
    locator: 'Emerging Trends in GenAI: Agents'
  notes: 'Grade C: product announcement with no use data. Adjacent to the module (wealth platform, not an accounting
    firm).'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-10
  title: Live consolidated family view with AI summaries and natural-language access for principals and the next
    generation
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - client-interaction
  - data-reporting
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Principals and heirs expect timely, app-like access to a single view of entities, investments and cash,
    not periodic static PDFs.
  solution: 'Platforms consolidate data across custodians and entities and add AI-driven summaries and assistants;
    advisors and CPA firms position live reporting as the replacement for periodic packages. Vendors: Masttro lists
    AI-powered wealth intelligence and a family communication portal; Asseta lists dashboard analytics and forecasting.'
  outcomes:
  - lever: experience
    description: 'none published; the case rests on expectations: a panel speaker says principals expect timely
      insights rather than periodic summaries.'
    figure: none published
    measures: Panel statement; no metric
    provenance: vendor-published
    source_ref: HUBBIS-ETON-2026
  prerequisites:
  - Open, structured data that the family office owns rather than data locked in a vendor system (WISS-FOAI-2026)
  - Entity map and a system of record per workflow (ARMANINO-FOTRENDS-2026)
  risks_and_guardrails:
  - Privacy is non-negotiable; solutions that cannot guarantee data security are unlikely to be adopted (CITI-AIFO-2026).
  - Agents connected through standard protocols can execute workflows but only on clean data (WISS-FOAI-2026).
  human_checkpoints:
  - Relationship managers keep judgment and client contact (HUBBIS-ETON-2026; KAUFMAN-FO-2026).
  role_evolution: Kaufman Rossin's family-office director says clients still want a human; AI should free staff
    time for deeper engagement (KAUFMAN-FO-2026).
  evidence_grade: C
  sources:
  - ref: ARMANINO-FOTRENDS-2026
    title: 'Built to Last: The Family Office Trends Defining 2026'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/articles/family-office-trends/
    date: '2026-08-19'
    access: full
    locator: Section 'Can you see what's happening across your office?' and consolidated reporting trend
  - ref: HUBBIS-ETON-2026
    title: 'Execution before ambition: Bryan Henning on AI discipline inside family offices'
    publisher: Hubbis (Independent Wealth Management Forum, Dubai 2026 panel)
    type: conference
    url: https://hubbis.com/article/execution-before-ambition-bryan-henning-on-ai-discipline-inside-family-offices
    date: '2026'
    access: full
    locator: Sections on principals' expectations and reporting cycles
  - ref: WISS-FOAI-2026
    title: AI for Family Offices Is Moving From Query to Command
    publisher: Wiss (Wiss Family Office)
    type: firm
    url: https://wiss.com/ai-for-family-offices/
    date: '2026-05-13'
    access: full
    locator: Sections on data ownership and agents executing workflows
  - ref: KAUFMAN-FO-2026
    title: 'Family Office Services: Insights from Chief Investment Officer on AI Adoption in Family Offices (news
      item featuring Jennifer Quent)'
    publisher: Kaufman Rossin
    type: firm
    url: https://kaufmanrossin.com/news/ai-adoption-in-family-offices/
    date: '2026-08-03'
    access: full
    locator: Quote from Jennifer Quent
  - ref: CITI-AIFO-2026
    title: 'AI in the Family Office: Privacy, Efficiency and Institutional Rigor (Citi Institute)'
    publisher: Citi Institute / Citi Wealth
    type: survey
    url: https://www.citigroup.com/global/insights/ai-in-the-family-office
    date: '2026-05-11'
    access: full
    locator: Key Takeaway 1
  - ref: FOX-MASTTRO-2024
    title: 'From archaic information to AI automation: A blue ocean opportunity for family offices'
    publisher: Family Office Exchange (familyoffice.com), content promoting Masttro Doc AI
    type: vendor
    url: https://familyoffice.com/insights/archaic-information-ai-automation-blue-ocean-opportunity-family-offices
    date: '2024-02-20'
    access: full
    locator: Section on next-generation expectations ($84 trillion transfer framing)
  notes: 'Grade C: vendor product descriptions and practitioner expectations. The client-experience claims in this
    area have no measured client-satisfaction data in the sources read.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-11
  title: 'Idea: AI that captures and surfaces institutional knowledge to reduce key-person risk in lean family offices'
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - research-synthesis
  - coordination-scheduling
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Much of how a family office runs lives in a few people's heads; reports run on who knows which entity
    owns what.
  solution: 'Idea (practitioners discuss it): AI helps capture and surface institutional knowledge, as a continuity
    tool as much as a productivity tool (Armanino). Idea only; no deployment found.'
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: Idea; no measure
    provenance: vendor-published
    source_ref: ARMANINO-FOTRENDS-2026
  prerequisites:
  - Documented decision rights, backups for key roles and an inventory of workflows (ARMANINO-FOTRENDS-2026)
  risks_and_guardrails:
  - Confidential family information entering AI tools needs a policy (NT-FOAIPOLICY-2026).
  human_checkpoints:
  - Not described.
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: ARMANINO-FOTRENDS-2026
    title: 'Built to Last: The Family Office Trends Defining 2026'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/articles/family-office-trends/
    date: '2026-08-19'
    access: full
    locator: AI section ('A lot of what makes a family office run lives in people's heads') and continuity section
  - ref: PULSE2-JPMFO-2026
    title: J.P. Morgan Private Bank's 2026 Family Office Report Finds AI Interest High And Portfolio Exposure Still
      Limited
    publisher: Pulse 2.0
    type: press
    url: https://pulse2.com/jpmorgan-global-family-office-report-2026/
    date: '2026-02-02'
    access: full
    locator: Paragraph on governance and succession (86% lack a clear succession plan for key decision makers, as
      summarized)
  notes: 'Idea. Context: the 86% figure is JPM''s, reported as lacking a clear succession plan for key decision
    makers; RBC''s 2026 release says half have an incomplete or non-existent plan; UBS''s 2025 report says 53% have
    a wealth succession plan. The definitions differ and are not comparable.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-12
  title: 'Idea: AI scenario modelling and successor assessment in family-enterprise succession advisory'
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - expert-judgment
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Succession in family businesses carries emotional and business risk, and many families have no plan;
    UBS found fewer than a third of family offices with a plan consulted the next generation at the outset.
  solution: 'Idea (practitioners discuss it): an advisor uses predictive analytics and simulation tools to model
    succession scenarios and assess candidates'' leadership potential from performance and feedback data, alongside
    governance and family-dynamics tools. The FFI Practitioner article names general commercial tools; no source
    shows them used in a family-succession engagement.'
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: Idea; no measure
    provenance: vendor-published
    source_ref: FFI-AIADVISORS-2024
  prerequisites:
  - Structured performance and feedback data on potential successors (FFI-AIADVISORS-2024)
  risks_and_guardrails:
  - Bias, hallucination and fiduciary-duty concerns for family-office AI use (AFS-FOAI-2024).
  - Succession documents can reveal inconsistent treatment of family members; confidentiality risk if uploaded to
    public tools (AFS-FOAI-2024).
  - Tax and estate technical content goes to tax.
  human_checkpoints:
  - Not described; the article assumes advisors remain responsible.
  role_evolution: FFI Practitioner argues advisors become more data-driven and multidisciplinary teams share one
    data set (FFI-AIADVISORS-2024).
  evidence_grade: D
  sources:
  - ref: FFI-AIADVISORS-2024
    title: 'Harnessing AI for Family Business Advisors: A Multidisciplinary Approach to Serving Family Enterprise
      Clients'
    publisher: FFI Practitioner (Family Firm Institute)
    type: professional-body
    url: https://ffipractitioner.org/harnessing-ai-for-family-business-advisors-a-multidisciplinary-approach-to-serving-family-enterprise-clients/
    date: '2024-10-22'
    access: full
    locator: 'Section ''Succession Planning: Data-Driven Scenario Modeling and Predictive Analytics'''
  - ref: HBK-EXITAI-2023
    title: You're Planning to Exit Your Business. Can AI Help?
    publisher: HBK CPAs & Consultants
    type: firm
    url: https://hbkcpa.com/insights/youre-planning-to-exit-your-business-can-ai-help/
    date: '2023-05-01'
    access: full
    locator: List of ten uses (chatbot-generated); the author also asked the bot why it may not outperform humans
  - ref: UBS-GFO-2025
    title: Global Family Office Report 2025
    publisher: UBS
    type: survey
    url: https://advisors.ubs.com/mediahandler/media/708870/Global%20Family%20Office%20Report%20_2025_.pdf
    date: '2025-05-21'
    access: full
    locator: Pp. 55-56 (succession key messages)
  notes: 'Idea only; both sources are opinion. HBK''s list was produced by a chatbot and is dated 2023. Pattern
    ''other'': an advisor-led modelling and assessment loop (scenario simulation plus candidate scoring), not a
    document or case pipeline.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-13
  title: 'Idea: AI-supported exit-readiness and value-building conversations with owner clients'
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Owner exits depend on leadership alignment, decision-making and institutional knowledge, and advisors
    want ways to start early AI conversations with owners.
  solution: 'Idea (practitioners discuss it): Certified Exit Planning Advisors guide owners in how AI affects enterprise
    value and exit readiness, using AI to make organizational gaps visible. An Exit Planning Institute webinar page
    frames the work as a people-side question and promises real-world examples and an advisor framework; no results
    are given.'
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: Idea; no measure
    provenance: vendor-published
    source_ref: EPI-AIWEBINAR-2026
  prerequisites:
  - Not described.
  risks_and_guardrails:
  - Valuation and tax technical work routes to other modules; owner data confidentiality applies (AFS-FOAI-2024).
  human_checkpoints:
  - Not described.
  role_evolution: EPI presents advisors as guides for early AI conversations with owners (EPI-AIWEBINAR-2026).
  evidence_grade: D
  sources:
  - ref: EPI-AIWEBINAR-2026
    title: How Advisors Are Using AI to Accelerate Business Value and Exit Readiness (webinar page)
    publisher: Exit Planning Institute
    type: professional-body
    url: https://exit-planning-institute.org/events/webinar-epi-2026-how-advisors-use-AI-accelerate-business-value-and-exit-readiness
    date: '2026'
    access: full
    locator: Session description and learning points
  - ref: HBK-EXITAI-2023
    title: You're Planning to Exit Your Business. Can AI Help?
    publisher: HBK CPAs & Consultants
    type: firm
    url: https://hbkcpa.com/insights/youre-planning-to-exit-your-business-can-ai-help/
    date: '2023-05-01'
    access: full
    locator: List of ten uses; valuation and successor identification
  notes: 'Idea only. The session date for the EPI webinar was not clear on the page, so it is a signal of discussion,
    not scheduled or delivered content. Other EPI chapter events on AI in 2026 were seen only in search snippets.
    Pattern ''other'': advisor-led diagnostic conversation supported by AI, no pipeline.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-14
  title: Advising families on AI policy, data limits and vendor diligence as a service
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - expert-judgment
  - document-production
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: announced
  problem: Family offices handle the most sensitive data of any client and adopt AI tools without a policy; leaks
    can occur through ordinary use with no breach event.
  solution: 'Banks, law firms and CPA firms publish policy frameworks and templates and advise offices to inventory
    AI use cases, tier them by risk, approve tools, vet vendors and train staff. Northern Trust gives ten principles
    and a risk-tiered template; Squire Patton Boggs gives a six-part governance response; Armanino and Wiss advise
    setting data and review rules before adoption. Firm type: law firm, bank and mid-market CPA firms. Whether any
    firm sells this as a paid service is not shown.'
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: Guidance only
    provenance: vendor-published
    source_ref: NT-FOAIPOLICY-2026
  prerequisites:
  - Inventory of AI use cases by risk level (SQUIRE-FOAIRISK-2026)
  - Short list of approved tools and named owner (NT-FOAIPOLICY-2026)
  risks_and_guardrails:
  - Higher-risk uses (investment advice, tax positions, financial modelling, legal interpretation) get enhanced
    review under the Northern Trust template (NT-AIPOLICYTEMPLATE-2026).
  - Vendors should be asked whether client data trains models and where it is stored (ARMANINO-FOTRENDS-2026).
  human_checkpoints:
  - AI output reviewed before reliance, especially on investment, legal, tax and estate matters (NT-FOAIPOLICY-2026).
  - Policy reviewed at least annually (NT-FOAIPOLICY-2026).
  role_evolution: Squire says responsibility must remain attributable to identified individuals or functions (SQUIRE-FOAIRISK-2026).
  evidence_grade: C
  sources:
  - ref: NT-FOAIPOLICY-2026
    title: How to Draft a Family Office AI Policy
    publisher: Northern Trust Institute
    type: firm
    url: https://www.northerntrust.com/united-states/institute/articles/how-to-draft-a-family-office-ai-policy
    date: '2026'
    access: full
    locator: Ten principles; Continuous Evolution
  - ref: NT-AIPOLICYTEMPLATE-2026
    title: Artificial Intelligence Responsible Use Policy for Family Office (template, noting it is a generalized
      template by Andersen Consulting, LLC)
    publisher: Northern Trust (hosting an Andersen Consulting template)
    type: firm
    url: https://www.northerntrust.com/content/dam/northerntrust/wealth-management/global/en/documents/ai-responsible-use-policy-for-family-office.pdf
    date: '2026'
    access: full
    locator: AI Risk Classification Framework; Confidential Family and Firm Data
  - ref: SQUIRE-FOAIRISK-2026
    title: 'Family Office Insights: Managing Family Office AI Risk'
    publisher: Squire Patton Boggs
    type: firm
    url: https://www.squirepattonboggs.com/insights/publications/managing-family-office-ai-risk/
    date: 2026-07
    access: full
    locator: Key risks; six-part governance response
  - ref: ARMANINO-FOTRENDS-2026
    title: 'Built to Last: The Family Office Trends Defining 2026'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/articles/family-office-trends/
    date: '2026-08-19'
    access: full
    locator: AI section
  - ref: WISS-FOAI-2026
    title: AI for Family Offices Is Moving From Query to Command
    publisher: Wiss (Wiss Family Office)
    type: firm
    url: https://wiss.com/ai-for-family-offices/
    date: '2026-05-13'
    access: full
    locator: Practical guidance paragraph (policy before go-live, vet vendors)
  - ref: AFS-FOAI-2024
    title: 'AI in Family Offices: A Closer Look at Privacy, Confidentiality, and Fiduciary Responsibility'
    publisher: ArentFox Schiff
    type: firm
    url: https://www.afslaw.com/perspectives/ai-law-blog/ai-family-offices-closer-look-privacy-confidentiality-and-fiduciary
    date: '2024-06-24'
    access: full
    locator: Sections on confidentiality and fiduciary duty
  notes: 'Grade C: published guidance with no evidence of clients adopting it. Routed overlap with risk-controls.
    Pattern ''other'': advisory deliverable (policy, inventory, vendor review) produced with AI help; no recurring
    agentic loop.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-15
  title: 'Hybrid family-office model: outsourced accounting, reporting and AI enablement with strategy and relationships
    kept in-house'
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: workflow-automation
  maturity: announced
  problem: Lean offices lack bandwidth to build and maintain a bench for each of accounting, reporting, technology,
    AI and security.
  solution: Offices keep strategy, family relationships and decision-making in-house and move accounting operations,
    reporting, reconciliations, technology, AI enablement and cybersecurity to outside providers. Armanino describes
    this as the trend; PKF's Asseta collaboration is the nearest named example of a CPA firm running family-office
    financial operations on a platform. GenTrust's CIO says family offices have asked it to find staff who can find
    AI technology to automate bill pay, concierge and similar work.
  outcomes:
  - lever: cost
    description: Armanino, citing Campden Wealth and AlTi Tiedemann Global (2025), says 80% of family offices outsource
      primarily to access specialized expertise while only 31% cite cost savings as a main driver.
    figure: 80% and 31%
    measures: As worded by Armanino about family offices that outsource; denominators and the underlying report
      not read
    provenance: vendor-published
    source_ref: ARMANINO-FOTRENDS-2026
  prerequisites:
  - Defined decision rights and named backups for critical roles (ARMANINO-FOTRENDS-2026)
  risks_and_guardrails:
  - Vendor opacity and concentration risk (SQUIRE-FOAIRISK-2026).
  - 'Independence: an audit firm selling this to an attest client faces restrictions (general background, unverified
    in this run).'
  human_checkpoints:
  - Principals and in-house staff keep decisions and the relationship (ARMANINO-FOTRENDS-2026).
  role_evolution: In-house roles narrow toward strategy and relationships; GenTrust's CIO reports demand for staff
    who can select and run AI automation (AICIO-FOOPTEST-2026).
  evidence_grade: C
  sources:
  - ref: ARMANINO-FOTRENDS-2026
    title: 'Built to Last: The Family Office Trends Defining 2026'
    publisher: Armanino
    type: firm
    url: https://www.armanino.com/articles/family-office-trends/
    date: '2026-08-19'
    access: full
    locator: Section on hybrid models
  - ref: PKF-ASSETA-2026
    title: PKF O'Connor Davies Announces Collaboration with Asseta AI to Support Family Office Modernization
    publisher: PKF O'Connor Davies / Business Wire
    type: firm
    url: https://www.businesswire.com/news/home/20260326796176/en/PKF-OConnor-Davies-Announces-Collaboration-with-Asseta-AI-to-Support-Family-Office-Modernization
    date: '2026-03-26'
    access: full
    locator: Release paragraphs 2-3
  - ref: AICIO-FOOPTEST-2026
    title: For Family Offices, AI Is Both an Investment Theme and an Operational Test
    publisher: Chief Investment Officer (ai-cio.com)
    type: press
    url: https://www.ai-cio.com/news/for-family-offices-ai-is-both-an-investment-theme-and-an-operational-test/
    date: '2026'
    access: full
    locator: Quote from Jim Besaw (GenTrust); cybersecurity outsourcing
  - ref: PULSE2-JPMFO-2026
    title: J.P. Morgan Private Bank's 2026 Family Office Report Finds AI Interest High And Portfolio Exposure Still
      Limited
    publisher: Pulse 2.0
    type: press
    url: https://pulse2.com/jpmorgan-global-family-office-report-2026/
    date: '2026-02-02'
    access: full
    locator: Operational paragraph (80% outsource some aspect of portfolio management; cybersecurity most-needed
      service at 32%, as summarized)
  notes: 'Grade C: firm positioning and surveys. JPM''s 80% is about outsourcing some aspect of portfolio management,
    a different measure from Armanino''s 80%. Pattern ''other'': an operating-model split (what is outsourced versus
    kept), not an agent pattern.'
  last_reviewed: '2026-10-20'
- id: advisory-private-client-16
  title: AI-assisted cash-flow forecasting and scenario modelling from family-office ledger history
  archetype: advisory
  module: private-client
  function: service-delivery
  work_types:
  - data-reporting
  - research-synthesis
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Forecasting cash needs for families with multiple entities is manual work in spreadsheets.
  solution: One family office fed years of profit-and-loss statements into an enterprise AI tool to model future
    cash flow, turning hours of work into a fraction of the time (an unnamed office as told to Wingspan). Asseta
    lists a forecasting module and says it will add planning and performance modules.
  outcomes:
  - lever: speed
    description: 'Practitioner recollection, unnamed office: hours of work turned into a fraction of the time; no
      figure.'
    figure: none published
    measures: Recollection relayed by a Wingspan director; no baseline
    provenance: self-reported
    source_ref: WINGSPAN-FOREPORT-2026
  prerequisites:
  - Clean multi-year ledger data (WISS-FOAI-2026)
  risks_and_guardrails:
  - Forecast assumptions and formulas need independent validation (IRS-OPR-2026 on AI-generated projections in written
    tax advice; analogy only).
  - Models are trained to please; prompts should say what the AI should not do (WISS-FOAI-2026).
  human_checkpoints:
  - Finance lead validates inputs and assumptions (IRS-OPR-2026, by analogy).
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: WINGSPAN-FOREPORT-2026
    title: 'Reporting: The Family Office''s Easiest Win With AI'
    publisher: Wingspan Legacy Partners
    type: firm
    url: https://wingspanlegacy.com/?p=3770
    date: '2026-06-09'
    access: full
    locator: Paragraph on feeding profit-and-loss statements into an enterprise tool
  - ref: ASSETA-SITE-2026
    title: 'Asseta: Family Office General Ledger, Bill Pay, Investments Data, Reconciliations and Reporting (product
      site)'
    publisher: Asseta AI
    type: vendor
    url: https://www.asseta.ai/
    date: 2026-10
    access: full
    locator: 'Platform menu: Forecasting product'
  - ref: CPAPA-ASSETASEED-2025
    title: Asseta AI Raises $4.2M Seed Round to Bolster Family Office Accounting Platform
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/?p=173630
    date: '2025-11-20'
    access: full
    locator: Paragraph on planned forecasting, planning and performance modules
  - ref: IRS-OPR-2026
    title: 'Issue Number 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice'
    publisher: IRS Office of Professional Responsibility
    type: regulator
    url: https://www.irs.gov/pub/opr-taxpros/issue-number-2026-19-introductory-guidelines-for-responsible-ai-use-in-federal-tax-practice.pdf
    date: '2026-06-24'
    access: full
    locator: Section on Circular 230 section 10.37 (written advice)
  - ref: WISS-FOAI-2026
    title: AI for Family Offices Is Moving From Query to Command
    publisher: Wiss (Wiss Family Office)
    type: firm
    url: https://wiss.com/ai-for-family-offices/
    date: '2026-05-13'
    access: full
    locator: Forum warning about AI bias
  notes: 'Grade C: an unnamed practitioner example and a vendor product listing. IRS guidance is cited only as an
    analogy for validating projections. Pattern ''other'': one-off modelling session by a finance lead using an
    enterprise AI tool.'
  last_reviewed: '2026-10-20'
```

## 3. Module notes

### Processes and key steps (with work types)

- **Family-office accounting and close** (transaction-processing, data-reporting): multi-entity general ledger, bank and brokerage feeds, bill pay and AP, intercompany entries, month-end close (ASSETA-SITE-2026; ARMANINO-FOTRENDS-2026; JOB-FOCONTROLLER-2026).
- **Alternative-investment administration** (transaction-processing, data-reporting): collecting capital calls, distribution notices, valuation statements and K-1s from each manager's portal, then entering them in one system (ARMANINO-FOTRENDS-2026; CANOE-FOALTS-2026).
- **Consolidated reporting to principals, family councils and advisors** (data-reporting, document-production): entity roll-up, commentary, dashboards (ARMANINO-FOTRENDS-2026; AGILLINK-FOPRED-2026).
- **Controls and payment approval** (review-assurance): approval hierarchies, dual authorization, vendor access reviews (ARMANINO-FOTRENDS-2026; AGILLINK-FOPRED-2026).
- **Succession and governance advisory** (expert-judgment, client-interaction): succession plans, next-generation involvement, decision rights (UBS-GFO-2025 pp. 55-56; PWC-USFB-2025; FFI-AIADVISORS-2024).
- **Owner advisory and exit readiness** (expert-judgment): value-building and readiness conversations with business owners (EPI-AIWEBINAR-2026).
- **Client experience** (client-interaction, coordination-scheduling): meetings, follow-up, service requests, portals and live views (MERCER-ASPEN-2026; HUBBIS-ETON-2026).

### Common pain points

- Investment reporting is too manual: 73% of 2026 RBC and Campden respondents say so, a top concern for three years running (RBC-CAMPDEN-2026).
- Alternative-investment documents arrive on each manager's schedule and format; K-1s arrive late by design and push returns onto extension (ARMANINO-FOTRENDS-2026).
- Fragmented, unstructured data across custodians, managers and spreadsheets is called the bottleneck for AI (WISS-FOAI-2026; HUBBIS-ETON-2026).
- Key-person dependency and informal knowledge (ARMANINO-FOTRENDS-2026).
- Lack of internal expertise: 57% of family offices cite it as the biggest barrier to AI (CITI-AIFO-2026).
- Many offices lack a succession plan, but sources define it differently (see metrics).

### Metrics and benchmarks (what each figure counts)

All are publisher-reported; every family-office survey here is published by a bank, administrator or advisory firm that sells to family offices.

- **22%** of family offices have automated operational tasks or use AI for investment analysis, up from 13% in 2024; **16%** use AI for investment performance reporting; **57%** cite lack of internal expertise as the biggest barrier (Citi Wealth 2025 Global Family Office Report, as shown on CITI-AIFO-2026; sample size not on the page).
- **Half** of offices say AI is embedded and essential to their workflow; **73%** say investment reporting is too manual; **59%** name cybersecurity and data breaches the top near-term operational concern, up from 16% (RBC-CAMPDEN-2026; sample size not captured). The 2025 edition reported three times more family offices using AI to improve operations than in 2024, on 317 responses (WSR-RBC-2025).
- **86%** of family offices say they already use AI technology to improve efficiency, decision-making and data insights; only **7%** are seeking opportunities in the AI sector (OCORIAN-IFC-2026; family members and senior executives from 16 jurisdictions; sample size not stated).
- **69%** of 317 UBS family-office clients think they are likely to use AI for financial reporting or data visualization in the next five years; 64% text analysis; 62% portfolio analysis; 6% do not expect to use AI (UBS-GFO-2025, pp. 46-47). This is intent, not use.
- **50%** of family offices polled at a 2025 conference said they are currently exploring or frequently using AI; 36% said collecting alts documents was the main problem (CANOE-FOALTS-2026; vendor-reported poll of 70+ attendees).
- **65%** of US family businesses see AI and generative AI as growth opportunities; **28%** take a cautious approach; most firms remain in exploration or pilot stages (PWC-USFB-2025). **73%** of 900+ NextGen leaders see genAI as a powerful force for transformation (CIO-PWCNEXTGEN-2024).
- **J.P. Morgan 2026 (n=333, 30 countries; secondary):** 65% plan to prioritise AI investments (an investment measure); 86% lack a clear succession plan for key decision makers; 80% outsource some aspect of portfolio management (PULSE2-JPMFO-2026).
- **Succession plans:** 53% of UBS clients have a wealth succession plan, up from 47% (UBS-GFO-2025, p. 56); half of RBC respondents have an incomplete or non-existent plan (RBC-CAMPDEN-2026); 86% lack a clear plan for key decision makers in JPM's survey (PULSE2-JPMFO-2026). The three questions differ and should not be compared.
- **Armanino's suggested metrics to watch** (suggestions, not measured benchmarks): days to close; share of reports that are system-generated; share of K-1s received before the filing deadline; number of approved AI use cases with documented review controls; rework hours per month (ARMANINO-FOTRENDS-2026).
- **Quality evidence: none found.** No source reports extraction accuracy, override rate, parallel-run result or inspection finding for this module. Mercer's article says many wealth firms struggle to quantify what AI investment delivers (MERCER-ASPEN-2026). The only independent adjacent measure is the Stanford JAR study on SME bookkeeping, which reports productivity gains without a figure in the abstract (STANFORD-JAR-2026).

### Guardrails and regulatory points

- **IRS OPR (Circular 230):** diligence (section 10.22) requires verifying AI-created facts, citations and calculations before delivery; section 10.27 on fees says cost savings from AI should be passed on and billing should reflect efficiencies; section 10.36 expects firm procedures, training and vendor vetting; section 10.37 says written advice cannot rely on AI projections without verification; IRC 6713 and 7216 and Circular 230 section 10.51 apply to unauthorized use or disclosure of tax return information, so client data should go only to secure, enterprise-approved AI (IRS-OPR-2026). Applies to tax practitioners; family-office accountants handling return information are touched by it.
- **FINRA 2026 report:** rules are technology-neutral; supervision, communications, recordkeeping and fair dealing apply to GenAI; the top use case among member firms is summarization and information extraction; agent risks listed are autonomy, scope and authority, auditability, data sensitivity, domain knowledge and misaligned rewards; monitoring may include prompt and output logs and model-version tracking (FINRA-OVERSIGHT-2026). It addresses member firms; family offices are covered only by analogy.
- **SEC FY2026 priorities:** examiners will review the accuracy of registrants' AI representations and whether policies exist to supervise AI use, including back-office operations; cybersecurity reviews include AI and polymorphic malware risks (SEC-EXAMPRI-FY2026). Relevant to RIA affiliates of accounting firms (the landscape's lead).
- **Private guidance:** Northern Trust's ten principles (protect sensitive information, human oversight, appropriate use, access controls, vendor governance and others) and a risk-tiered template (NT-FOAIPOLICY-2026; NT-AIPOLICYTEMPLATE-2026); Squire Patton Boggs lists model, data-exposure, vendor-opacity and AI-enabled-fraud risks and a six-part governance response (SQUIRE-FOAIRISK-2026); ArentFox Schiff argues public models may reuse submitted data and fiduciary duties are not displaced by AI (AFS-FOAI-2024).
- **Payments:** controls against deepfake-enabled fraud are procedural (dual authorization, verification outside the request channel) because detection tools lag (CFO-DEEPFAKE-2026; ARMANINO-FOTRENDS-2026).
- **Independence:** none of the sources addresses independence for family-office accounting sold to the firm's own audit clients. General background, unverified in this run: outsourced accounting and some valuation services are commonly restricted for attest clients (see the landscape's independence note).

### Frontier signals (dated, sourced)

1. **2025-11-17.** SEC FY2026 priorities direct examiners at AI representations and supervision of AI use, including back-office tasks (SEC-EXAMPRI-FY2026).
2. **2025-11-20.** Asseta AI announced a $4.2M seed round and said it supports more than $10 billion in assets (CPAPA-ASSETASEED-2025).
3. **2025-12-09.** FINRA added AI agents to its oversight report as an emerging risk (FINRA-OVERSIGHT-2026).
4. **2026-03-26.** PKF O'Connor Davies announced its collaboration with Asseta AI (PKF-ASSETA-2026).
5. **2026-04-10.** Ocorian survey: 72% expect AI's most significant effects on operating models over two to five years; 26% strongly agree AI will reshape how family offices operate within the next year (OCORIAN-IFC-2026).
6. **2026-04 (forum), reported 2026-05-13.** Forum speakers said AI had moved from answering questions to executing workflows through connected data, with clean data a precondition (WISS-FOAI-2026).
7. **2026-05-11.** Citi: adoption slow but accelerating; younger generations and junior staff are the biggest advocates; some family offices expect analysts to move to managing agentic workflows (CITI-AIFO-2026; AICIO-FOOPTEST-2026).
8. **2026-07-30.** Mercer Advisors unveiled Aspen's second generation; Compound Planning announced CompoundAI agents (MERCER-ASPEN-2026).
9. **2026-09-29.** RBC and Campden: half of offices say AI is embedded and essential; cybersecurity is the top near-term concern (RBC-CAMPDEN-2026).

### Workforce and role effects

- The 2025 RBC and Campden report is quoted as predicting AI will likely cause a significant reduction in the number of family-office staff doing basic accounting or administrative work (WSR-RBC-2025). This is a prediction, not a measurement.
- GenTrust's CIO says several family offices asked it, over 12 months, to help find staff who can find AI technology to automate bill pay, concierge and similar work (AICIO-FOOPTEST-2026).
- Citi reports some family offices expect analysts to be replaced by AI agents, with staff moving to managing AI processes (AICIO-FOOPTEST-2026, citing Citi).
- A family-office controller posting scopes AI-assisted tooling inside a senior close-ownership role (JOB-FOCONTROLLER-2026).
- Kaufman Rossin's family-office director says the human connection cannot be automated and AI should free staff time for client engagement (KAUFMAN-FO-2026).
- A panel speaker says tools lift morale when they remove low-value tasks and hurt it when poorly implemented (HUBBIS-ETON-2026).

### Objections and concerns practitioners raise

- Privacy and confidentiality are non-negotiable; solutions that cannot guarantee data security are unlikely to be adopted (CITI-AIFO-2026). Exposure can occur through ordinary use with no breach event (SQUIRE-FOAIRISK-2026).
- Hallucination as a data-governance problem (HUBBIS-ETON-2026); models trained to please the user (WISS-FOAI-2026); automation bias (SQUIRE-FOAIRISK-2026).
- Buying AI before fixing the data (WISS-FOAI-2026).
- Vendor opacity and a crowded vendor market that drives wait-and-see (SQUIRE-FOAIRISK-2026; AICIO-FOOPTEST-2026, citing PwC).
- Fiduciary duty is not displaced by AI (AFS-FOAI-2024).
- Most AI projects fail to produce meaningful outcomes, with the panel unsure whether the share is 70% or 95% (HUBBIS-ETON-2026; the figure is the speaker's, unsourced).
- AI-enabled fraud and impersonation (CFO-DEEPFAKE-2026; AJG-CYBER-2026).
- Conflation of AI as an investment theme with AI use in operations (ARMANINO-FOTRENDS-2026).

### Interview probes for an advisor

1. Which steps in your family-office accounting (document intake, intercompany, coding, close, consolidation) does an AI tool touch today, who reviews the output, and what share of extracted or coded items gets corrected?
2. Which client data may go into which AI tool, who approved the list, and has any principal or family member asked for a ban or an opt-in?
3. When a principal wants a live consolidated view, what must be true of the data and the system of record before you trust AI summaries, and who owns that system?
4. In succession or exit engagements, where do you use AI and where do you refuse, and how do you keep one family member's information from reaching another?
5. How have roles on family-office engagements changed: who now reviews machine-prepared work, who talks to the principals, and what are you hiring for?

## 4. Routed to other modules

- **Estate and trust technical work (tax archetype):** Wealth.com's AI estate and tax planning platform, its Series B of $65M, claims of 100,000+ estate documents processed in 2025 and approvals from the three largest broker-dealers (WEALTHCOM-SERIESB-2026), and the CEO's argument that AI makes estate planning routine with attorneys in a collaborating role (WEALTHCOM-INVNEWS-2025). Vendor claims, not verified.
- **Tax (tax archetype):** K-1 compliance calendars, IRC 7216 and Circular 230 duties (IRS-OPR-2026); Mercer's tax-preparation actions inside Aspen (MERCER-ASPEN-2026).
- **Regulated investment advice (out of scope):** portfolio management and manager selection inside Aspen and the RBC, JPM and UBS allocation findings (MERCER-ASPEN-2026; RBC-CAMPDEN-2026; PULSE2-JPMFO-2026); the FSR literature review on AI in financial planning (FSR-FAULHABER-2024).
- **Client accounting services:** the Stanford JAR study on SME bookkeeping and the general ledger, close and reconciliation tooling used by smaller businesses (STANFORD-JAR-2026).
- **Valuation:** Masttro's claimed AI valuation of private equity and venture holdings (MASTTRO-JEFFERSON-2026 platform pages; vendor claim, not read in detail).
- **Risk-controls:** AI governance and policy advisory (SQUIRE-FOAIRISK-2026; NT-FOAIPOLICY-2026); AI-enabled fraud and control design (CFO-DEEPFAKE-2026; AJG-CYBER-2026).
- **Forensic-disputes:** deepfake impersonation and payment-fraud investigation (CFO-DEEPFAKE-2026).
- **Professional-services (firm operations):** how firms staff and price family-office work; PE ownership of firms; firms' own AI policies for staff.

## 5. Sources

Type counts below are of all 45 listed sources (41 opened, 4 search-only).

By type: firm 12; press 11; vendor 6; survey 5; regulator 3; conference 3; professional-body 2; academic 2; job-posting 1. No podcast, community-forum or standard-setter source was found for this module.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| AFS-FOAI-2024 | AI in Family Offices: A Closer Look at Privacy, Confidentiality, and Fiduciary Responsibility | ArentFox Schiff | firm | https://www.afslaw.com/perspectives/ai-law-blog/ai-family-offices-closer-look-privacy-confidentiality-and-fiduciary | 2024-06-24 | full |
| AGILLINK-FOPRED-2026 | Family Office Predictions for 2026 | Agillink | vendor | https://www.agillink.com/insights/Blog/family-office-predictions-for-2026.html | 2026-01-27 | full |
| AICIO-FOOPTEST-2026 | For Family Offices, AI Is Both an Investment Theme and an Operational Test | Chief Investment Officer (ai-cio.com) | press | https://www.ai-cio.com/news/for-family-offices-ai-is-both-an-investment-theme-and-an-operational-test/ | 2026 | full |
| AJG-CYBER-2026 | When Cyber Risk Becomes Physical Risk | Gallagher (Arthur J. Gallagher) Private Client | firm | https://www.ajg.com/news-and-insights/when-cyber-risk-becomes-physical-risk/ | 2026-09 | full |
| ARMANINO-FOTRENDS-2026 | Built to Last: The Family Office Trends Defining 2026 | Armanino | firm | https://www.armanino.com/articles/family-office-trends/ | 2026-08-19 | full |
| ASSETA-SITE-2026 | Asseta: Family Office General Ledger, Bill Pay, Investments Data, Reconciliations and Reporting (product site) | Asseta AI | vendor | https://www.asseta.ai/ | 2026-10 | full |
| CANOE-FOALTS-2026 | The Future-Ready Family Office: Navigating alts data with AI-powered precision | Canoe Intelligence | vendor | https://canoeintelligence.com/the-future-ready-family-office-navigating-alts-data-with-ai-powered-precision/ | 2026-03-18 | full |
| CFO-DEEPFAKE-2026 | Seeing is no longer believing: deepfakes put a new face on cyber security risk for family offices | Canadian Family Offices | press | https://canadianfamilyoffices.com/special-reports/technology-sr/seeing-is-no-longer-believing-deepfakes-put-a-new-face-on-cyber-security-risk-for-family-offices/ | 2026-06-05 | full |
| CIO-PWCNEXTGEN-2024 | Generative AI sparks family business renaissance: PwC report (on PwC's 'Success and Succession in an AI World', NextGen Survey 2024) | CIO.com | press | https://www.cio.com/article/2091956/generative-ai-sparks-family-business-renaissance-pwc-report.html | 2024-04-16 | full |
| CITI-AIFO-2026 | AI in the Family Office: Privacy, Efficiency and Institutional Rigor (Citi Institute) | Citi Institute / Citi Wealth | survey | https://www.citigroup.com/global/insights/ai-in-the-family-office | 2026-05-11 | full |
| CPAPA-ASSETASEED-2025 | Asseta AI Raises $4.2M Seed Round to Bolster Family Office Accounting Platform | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=173630 | 2025-11-20 | full |
| EMPAXIS-FOSTMT-2022 | How Family Offices Automate Data Extraction for Investment Statements | Empaxis | vendor | https://www.empaxis.com/blog/family-offices-automate-data-extraction | 2022-06-30 | full |
| EPI-AIWEBINAR-2026 | How Advisors Are Using AI to Accelerate Business Value and Exit Readiness (webinar page) | Exit Planning Institute | professional-body | https://exit-planning-institute.org/events/webinar-epi-2026-how-advisors-use-AI-accelerate-business-value-and-exit-readiness | 2026 | full |
| FFI-AIADVISORS-2024 | Harnessing AI for Family Business Advisors: A Multidisciplinary Approach to Serving Family Enterprise Clients | FFI Practitioner (Family Firm Institute) | professional-body | https://ffipractitioner.org/harnessing-ai-for-family-business-advisors-a-multidisciplinary-approach-to-serving-family-enterprise-clients/ | 2024-10-22 | full |
| FINRA-OVERSIGHT-2026 | 2026 FINRA Annual Regulatory Oversight Report: GenAI: Continuing and Emerging Trends | FINRA | regulator | https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai | 2025-12-09 | full |
| FOPRO-AITODAY-2026 | How Family Offices Are Using AI Today to Boost Efficiency | The Family Office Professional (thefopro.com) | press | https://thefopro.com/how-family-offices-are-using-ai-today-to-boost-efficiency/ | 2026-06-08 | full |
| FOX-MASTTRO-2024 | From archaic information to AI automation: A blue ocean opportunity for family offices | Family Office Exchange (familyoffice.com), content promoting Masttro Doc AI | vendor | https://familyoffice.com/insights/archaic-information-ai-automation-blue-ocean-opportunity-family-offices | 2024-02-20 | full |
| FSR-FAULHABER-2024 | Artificial Intelligence in Accounting, Medicine, and Law with Potential Implications for Financial Planning: A Review of Literature | Financial Services Review 32(4), Iowa State University authors | academic | https://openjournals.libs.uga.edu/fsr/article/download/4017/3449/11845 | 2024 | full |
| FWR-DATAFIRST-2026 | The State Of AI In Family Offices: Why You Need To Fix Your Data Before You Buy AI (forum keynote write-up) | Family Wealth Report | conference | https://www.familywealthreport.com//article.php/The-State-Of-AI-In-Family-Offices-%E2%80%93-Why-You-Need-To-Fix-Your-Data-Before-You-Buy-AI-?id=207578 | 2026-04-30 | search-only |
| FWR-QUERYCOMMAND-2026 | From Query To Command: AI's Rapid Evolution (Family Wealth Report Fintech Forum coverage) | Family Wealth Report | conference | https://www.familywealthreport.com/article.php/From-Query-To-Command%3A-AI%E2%80%99s-Rapid-Evolution-%E2%80%93-Family-Wealth-Report-Fintech-Forum?id=207424 | 2026-04-13 | search-only |
| HBK-EXITAI-2023 | You're Planning to Exit Your Business. Can AI Help? | HBK CPAs & Consultants | firm | https://hbkcpa.com/insights/youre-planning-to-exit-your-business-can-ai-help/ | 2023-05-01 | full |
| HK-PRINCIPALS-2026 | When Principals Ask AI Instead of Their Advisors | Holland & Knight | firm | https://www.hklaw.com/en/insights/publications/2026/04/when-principals-ask-ai-instead-of-their-advisors | 2026-04-20 | search-only |
| HUBBIS-ETON-2026 | Execution before ambition: Bryan Henning on AI discipline inside family offices | Hubbis (Independent Wealth Management Forum, Dubai 2026 panel) | conference | https://hubbis.com/article/execution-before-ambition-bryan-henning-on-ai-discipline-inside-family-offices | 2026 | full |
| IRS-OPR-2026 | Issue Number 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice | IRS Office of Professional Responsibility | regulator | https://www.irs.gov/pub/opr-taxpros/issue-number-2026-19-introductory-guidelines-for-responsible-ai-use-in-federal-tax-practice.pdf | 2026-06-24 | full |
| JOB-FOCONTROLLER-2026 | Controller (private family office, Redwood City, California) | A private family office (job board: Greenhouse) | job-posting | https://job-boards.greenhouse.io/fo/jobs/5263749007 | 2026 | full |
| JPM-FAMILYOFFICE-2026 | J.P. Morgan Private Bank 2026 Global Family Office Report | J.P. Morgan Private Bank | survey | https://privatebank.jpmorgan.com/nam/en/insights/reports/2026-family-office-report-download | 2026-02 | search-only |
| KAUFMAN-FO-2026 | Family Office Services: Insights from Chief Investment Officer on AI Adoption in Family Offices (news item featuring Jennifer Quent) | Kaufman Rossin | firm | https://kaufmanrossin.com/news/ai-adoption-in-family-offices/ | 2026-08-03 | full |
| MASTTRO-JEFFERSON-2026 | Jefferson River Capital Single Family Office (case study) | Masttro | vendor | https://masttro.com/resources/jefferson-river-capital | 2026 | full |
| MERCER-ASPEN-2026 | Mercer Advisors and Compound Planning bet big on AI for family offices | InvestmentNews | press | https://www.investmentnews.com/ria-news/mercer-advisors-and-compound-planning-bet-big-on-ai-for-family-offices/267616 | 2026-07-30 | full |
| NT-AIPOLICYTEMPLATE-2026 | Artificial Intelligence Responsible Use Policy for Family Office (template, noting it is a generalized template by Andersen Consulting, LLC) | Northern Trust (hosting an Andersen Consulting template) | firm | https://www.northerntrust.com/content/dam/northerntrust/wealth-management/global/en/documents/ai-responsible-use-policy-for-family-office.pdf | 2026 | full |
| NT-FOAIPOLICY-2026 | How to Draft a Family Office AI Policy | Northern Trust Institute | firm | https://www.northerntrust.com/united-states/institute/articles/how-to-draft-a-family-office-ai-policy | 2026 | full |
| OCORIAN-IFC-2026 | FAMILY OFFICES: Family offices embrace AI for operations but hold back on investment (reports an Ocorian study) | IFC Review | press | https://www.ifcreview.com/?p=17434 | 2026-04-10 | full |
| PKF-ASSETA-2026 | PKF O'Connor Davies Announces Collaboration with Asseta AI to Support Family Office Modernization | PKF O'Connor Davies / Business Wire | firm | https://www.businesswire.com/news/home/20260326796176/en/PKF-OConnor-Davies-Announces-Collaboration-with-Asseta-AI-to-Support-Family-Office-Modernization | 2026-03-26 | full |
| PULSE2-JPMFO-2026 | J.P. Morgan Private Bank's 2026 Family Office Report Finds AI Interest High And Portfolio Exposure Still Limited | Pulse 2.0 | press | https://pulse2.com/jpmorgan-global-family-office-report-2026/ | 2026-02-02 | full |
| PWC-USFB-2025 | PwC 2025 US Family Business Survey: Navigating slower growth amid opportunity and change | PwC US | survey | https://www.pwc.com/us/en/services/audit-assurance/private-company-services/library/family-business-survey.html | 2026-03-16 | full |
| RBC-CAMPDEN-2026 | 2026 RBC and Campden Wealth Report: North American family offices shift from caution to optimism amid Great Wealth Transfer, AI acceleration (press release) | RBC Wealth Management with Campden Wealth | survey | https://www.rbcwealthmanagement.com/en-us/newsroom/2026-10-01/2026-rbc-and-campden-wealth-report-north-american-family-offices-shift-from-caution-to-optimism-amid-great-wealth-transfer-ai-acceleration | 2026-09-29 | full |
| SEC-EXAMPRI-FY2026 | Examination Priorities for Fiscal Year 2026 | SEC Division of Examinations | regulator | https://www.sec.gov/files/2026-exam-priorities.pdf | 2025-11-17 | full |
| SQUIRE-FOAIRISK-2026 | Family Office Insights: Managing Family Office AI Risk | Squire Patton Boggs | firm | https://www.squirepattonboggs.com/insights/publications/managing-family-office-ai-risk/ | 2026-07 | full |
| STANFORD-JAR-2026 | Human + AI in Accounting: Early Evidence from the Field (Choi, Xie), Journal of Accounting Research 64(3), pp. 1333-1373 | Stanford GSB listing of the Journal of Accounting Research paper | academic | https://www.gsb.stanford.edu/index%2ephp/node/629989 | 2026-06 | full |
| UBS-GFO-2025 | Global Family Office Report 2025 | UBS | survey | https://advisors.ubs.com/mediahandler/media/708870/Global%20Family%20Office%20Report%20_2025_.pdf | 2025-05-21 | full |
| WEALTHCOM-INVNEWS-2025 | AI is transforming estate planning into a mainstream financial essential, says Wealth.com CEO | InvestmentNews | press | https://www.investmentnews.com/retirement-planning/ai-is-transforming-estate-planning-into-a-mainstream-financial-essential-says-wealthcom-ceo/263123 | 2025-11-19 | full |
| WEALTHCOM-SERIESB-2026 | Wealth.com: $65 Million Series B Raised To Accelerate AI-Powered Estate And Tax Planning Platform | Pulse 2.0 | press | https://pulse2.com/wealth-com-65-million-series-b-raised-to-accelerate-ai-powered-estate-and-tax-planning-platform/ | 2026-04-16 | full |
| WINGSPAN-FOREPORT-2026 | Reporting: The Family Office's Easiest Win With AI | Wingspan Legacy Partners | firm | https://wingspanlegacy.com/?p=3770 | 2026-06-09 | full |
| WISS-FOAI-2026 | AI for Family Offices Is Moving From Query to Command | Wiss (Wiss Family Office) | firm | https://wiss.com/ai-for-family-offices/ | 2026-05-13 | full |
| WSR-RBC-2025 | Report: North American Family Offices Increasingly Embrace AI And Innovation | Wealth Solutions Report (on the RBC and Campden Wealth 2025 report) | press | https://wealthsolutionsreport.com/2025/10/16/report-north-american-family-offices-increasingly-embrace-ai-and-innovation/ | 2025-10-16 | full |

Source notes (access method, date basis, caveats):

- **AFS-FOAI-2024:** Older than the window; foundation for the confidentiality and fiduciary arguments.
- **AGILLINK-FOPRED-2026:** Publisher type is inferred (it describes serving teams that manage bill pay, accounting and reporting); not verified.
- **AICIO-FOOPTEST-2026:** Read through the r.jina.ai mirror (site blocks curl). Exact day not shown: image upload path is 2026/07 and the Kaufman Rossin page of 2026-08-03 calls it recent, so it sits between late July and early August 2026.
- **AJG-CYBER-2026:** Month from the PDF path (2026/sep). Its family-office statistics are cited from other sources (a 2025 survey via WealthManagement.com and a Deloitte Family Office Cybersecurity Report), which were not read.
- **ARMANINO-FOTRENDS-2026:** Blocked to curl; read through the r.jina.ai mirror, which gave the publication timestamp.
- **ASSETA-SITE-2026:** Undated live page, read 2026-10-20. All figures on it are vendor claims; counter definitions are not given.
- **CANOE-FOALTS-2026:** Read through the mirror. Vendor write-up of a breakfast panel and audience poll at Institutional Investor's East Coast Family Office Wealth Conference 'late last year' (so late 2025).
- **CIO-PWCNEXTGEN-2024:** Older than the 18-month window; kept as a foundation for the succession angle. The PwC PDF itself was blocked.
- **CITI-AIFO-2026:** Page read in full; survey figures are credited on the page to the Citi Wealth 2025 Global Family Office Report. The Citi PDF download was not read. CIO (AICIO-FOOPTEST-2026) quotes 14% for 2024; Citi's own page says 13%, which this file uses.
- **EMPAXIS-FOSTMT-2022:** Older than the window; describes bot-based extraction, not an LLM, for an unnamed family office.
- **EPI-AIWEBINAR-2026:** Event page; the session date was not clearly stated for this webinar, so this is a signal of discussion, not evidence of use.
- **FFI-AIADVISORS-2024:** Read through the mirror. Older than the window; a single author's argument, not a deployment report.
- **FINRA-OVERSIGHT-2026:** The section page shows no date; 2025-12-09 is the release date given in law-firm summaries seen in search results.
- **FOX-MASTTRO-2024:** Vendor-voiced piece; older than the window.
- **FSR-FAULHABER-2024:** The landscape listed this as FSR-FAULHABER-2025 with journal and year unconfirmed. The PDF's own citation line gives Financial Services Review, 32(4), 2024, pp. 1-11, so the ref year is corrected here.
- **FWR-DATAFIRST-2026:** Paywalled; only the abstract was visible.
- **FWR-QUERYCOMMAND-2026:** Paywalled; only the abstract was visible. Its content is known here through the Wiss recap (WISS-FOAI-2026).
- **HBK-EXITAI-2023:** Older than the window. The article lists ten uses as generated by a chatbot, so it shows what is being discussed, not what is deployed.
- **HK-PRINCIPALS-2026:** Title and date seen in a search listing only; the URL returned 404 when opened. A lead on principals using AI in place of advisors.
- **HUBBIS-ETON-2026:** Panel write-up; the page shows no publication date and the forum date was not retrieved.
- **JOB-FOCONTROLLER-2026:** Undated live posting read 2026-10-20; year is the read year, not a publication date.
- **JPM-FAMILYOFFICE-2026:** Primary report not opened. Figures come from the secondary pages PULSE2-JPMFO-2026 and the Let's Data Science summary. Release date is reported as 2026-02-04 by one summary; Pulse 2.0 is stamped 2026-02-02, so only the month is used.
- **MASTTRO-JEFFERSON-2026:** Page is undated; related items on it are dated 2026-10-14. Only the summary bullets are public.
- **NT-AIPOLICYTEMPLATE-2026:** Undated PDF; treated as 2026.
- **NT-FOAIPOLICY-2026:** Publication date not shown on the page (page footer is 2026); treated as 2026.
- **OCORIAN-IFC-2026:** News item on an Ocorian survey of family members and senior executives from 16 jurisdictions; sample size not stated in the item; the Ocorian report itself was not read.
- **PKF-ASSETA-2026:** Business Wire and pkfod.com pages were blocked; the full release text was read on a syndicated copy at https://aijourn.com/?p=509847. The date is in the Business Wire URL and the search listing.
- **PULSE2-JPMFO-2026:** Secondary summary of JPM-FAMILYOFFICE-2026.
- **PWC-USFB-2025:** Read through the mirror (the pwc.com page returns Access Denied to curl). Page is dated 2026-03-16 and covers the 2025 survey.
- **RBC-CAMPDEN-2026:** Press release read in full; the release text read did not state the 2026 sample size. Full report not read.
- **SEC-EXAMPRI-FY2026:** sec.gov blocked curl; read through the mirror. Release date 2025-11-17 is taken from the landscape file; the PDF text itself shows no date. The landscape listed this item as snippet-only; it is now opened.
- **STANFORD-JAR-2026:** Abstract page read through the mirror. Adjacent evidence only: accountants and SMEs on an AI-enabled accounting platform, not family offices.
- **UBS-GFO-2025:** Primary PDF read with pdftotext. Date is the UBS media-page date (URL ends fr-20250521) seen in search results; survey fielded 2025-01-22 to 2025-04-04.
- **WISS-FOAI-2026:** Read through the mirror. It is a recap of a Family Wealth Report article of 2026-04-13 about the April 2026 Family Wealth Report Family Office Fintech Forum in New York.
- **WSR-RBC-2025:** Secondary coverage of the RBC and Campden Wealth North America Family Office Report 2025; the report itself was not read.

## 6. Gaps

**Not found or not reachable**
- Any independent measurement of AI in family-office accounting, succession or owner advisory: error rates, override rates, parallel runs, client-satisfaction data, inspection findings. None found.
- Named CPA or advisory firm case studies with figures. PKF O'Connor Davies and Kaufman Rossin are the only accounting firms in the landscape with family-office AI items; the PKF item is an announcement with no results, and the Kaufman item is a quote on relationships (PKF-ASSETA-2026; KAUFMAN-FO-2026). Armanino, Wiss and Wingspan publish advice. Baker Tilly, EisnerAmper, Citrin Cooperman, Marcum, Withum and Cherry Bekaert family-office AI pages were not searched or found (a combined search for them returned none).
- Primary reports not opened: J.P. Morgan 2026 Global Family Office Report (figures are from secondary summaries), the Citi PDF, the RBC 2026 full report and sample size, the Ocorian report, Campden Wealth and AlTi Tiedemann's 2025 Operational Excellence Report (cited via Armanino), PwC's 2024 NextGen PDF (blocked), the Deloitte Family Office Cybersecurity Report (cited via Gallagher).
- Paywalled or blocked: Family Wealth Report forum articles (abstracts only); Holland & Knight's April 2026 piece on principals asking AI instead of their advisors (404 when opened; title seen in search). The H&K topic, principals using AI in place of advisors, is a client-experience signal this file could not substantiate.
- No podcast, community discussion or conference proceedings with session-level detail were found. Discourse evidence is trade-press and firm-blog recaps (WISS-FOAI-2026; HUBBIS-ETON-2026; CANOE-FOALTS-2026). The Hubbis panel and Northern Trust pages show no publication date.
- No AICPA PFP, CFP Board, STEP or similar professional-body guidance on AI in this module was found; the web-search budget ran out before these could be searched. The FFI Practitioner and Exit Planning Institute items are the only professional-body material.
- Job-posting evidence is a single undated family-office controller posting (JOB-FOCONTROLLER-2026). A PKF O'Connor Davies posting mentioning Asseta experience appeared in a search summary only and was not opened.
- Succession and owner-advisory AI: only ideas (FFI-AIADVISORS-2024; HBK-EXITAI-2023; EPI-AIWEBINAR-2026). Exit Planning Institute chapter events on AI were seen only as search snippets.
- Wealth-advisor adoption surveys (for example Advisor360, J.D. Power, Schwab) surfaced only through an aggregator snippet and were not opened, so none is used.

**Corrections to the landscape**
- FSR-FAULHABER-2025 is dated 2024 in the PDF's own citation line (Financial Services Review 32(4), 2024); this file uses FSR-FAULHABER-2024.
- JPM-FAMILYOFFICE-2026's "65% plan to prioritise AI investments" measures AI as an investment theme, not use in operations; the landscape summary line did not make that distinction.
- SEC-EXAMPRI-FY2026 was snippet-only in the landscape; the PDF was read here (through the mirror) and it confirms attention to AI representations and supervision.
- PKF-ASSETA-2026 was snippet-only in the landscape; the release text was read on a syndicated copy.
- Citi's page gives 13% for 2024 where CIO's relay says 14%; this file uses Citi's own page.

**Date uncertainty:** the RBC release is dated 2026-09-29 although its URL path says 2026-10-01; the J.P. Morgan release date is reported as 2026-02-04 by one summary while Pulse 2.0 is stamped 2026-02-02; the CIO article's day, the Northern Trust pages, the Hubbis panel, the Masttro case study and the EPI webinar are undated or ambiguous and carry a year or month only.
