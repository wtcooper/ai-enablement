# Deep dive: tax / compliance-corporate / practice

- **Archetype:** tax (tax services and tax functions)
- **Module:** compliance-corporate. Corporate direct-tax compliance in house and at large firms: federal, state and international income tax returns (1120, 5471/8858, state apportionment and SALT income tax), return workpapers and review, tax credits and incentives (R&D credit, Form 6765 Section G), estimated payments and the tax calendar.
- **Angle:** practice. What firms and in-house teams actually do: case studies, firm reports and announcements, vendor deployments with named customers, product documentation, job postings that show real use, and the structure of AI teams.
- **Prepared:** 2026-10-17. **Inputs:** `research/runs/wave2/landscape-tax.md`, `research/briefs/templates/vocabulary.md`.
- **Method note.** Pages were opened with `curl` (PDFs with `pdftotext`; a few bot-walled pages through the `r.jina.ai` text mirror). Sixteen web searches were run; a seventeenth was refused because the shared search budget was spent. Every source in section 5 is `access: full` (opened and read). Items seen only in search extracts are named in the Gaps section or in `notes` and support no outcome figure and no A or B grade.

---

## 1. Summary

- **Evidence is thin for this module and almost all of it is vendor-published.** Sixteen candidate use cases: A 0, B 3, C 12, D 1. No entry has a measured outcome from a named organization (grade A).
- **Three entries reach grade B because a named organization is described as running the work without published measurements:** PwC's K-1 agents (tax-compliance-corporate-02, adjacent setting so capped at B), Oxford Industries' governed AI automation with Savant (tax-compliance-corporate-08, announced in a vendor press release ahead of a TEI session) and OpenAI's own tax team (tax-compliance-corporate-09, a job listing plus a conference demonstration).
- **The most specific numbers come from tool vendors and are unattributed to customers.** Thomson Reuters says the Neo.Tax and ONESOURCE R&D credit workflow cuts filing time from weeks to days and that companies report 50-75% lower fees and 20-30% lower FIN 48 reserves (TR-NEOTAX-2025). Byron says business-return extraction is more than 97% accurate (BYRON-2026). Neither states a sample or method.
- **Quality evidence is absent.** No error rate, override rate, parallel-run result or independent measurement was found for AI in corporate return preparation, workpaper review, state apportionment or Form 6765. PwC says reviewers who override an agent are asked to say why (PWC-MEGNA-2025) but publishes no rate. The nearest independent measurement is a benchmark of personal income tax calculation, where frontier models calculated fewer than a third of federal returns correctly (COLUMN-TAXCALCBENCH-2025); it is adjacent and does not grade any entry.
- **Adoption in corporate tax departments is still low and governance lags.** Thomson Reuters Institute reports 67% of 288 corporate tax departments not using GenAI (TR-CORPTAX-2025) and, in a separate survey, 17% of corporate tax departments with specific AI and data policies and 45% with none (TR-TENSIONS-2025). KPMG Germany reports 71% of surveyed tax departments using AI tools (sample size not stated) (KPMG-DE-2026). The samples and definitions differ and should not be averaged.
- **Practice at the largest firms is announcements and platforms, not measured compliance results.** EY (Agent Factory, Tax Labs), KPMG (Digital Gateway with Claude), PwC (Agent OS) and RSM (myRSM Tax) describe platforms; EY's reported plan was 150 agents for 80,000 tax professionals (BTAX-BIG4-2025). No public outcome for corporate return preparation was found.
- **The in-house picture is about data, ownership and cost.** At TEI Tax Tech 2026, two hands out of more than 50 went up when asked whether tax owns AI implementation, and attendees raised silent failures and rising token costs (TEI-TAXTECH-2026). The strongest named pre-AI results in this module are rules-based automation (for example Baxter: 200+ international reports in 2 hours instead of 80, vendor-published), which show the data prerequisites.
- **Counter-views exist.** Sala argues AI will not shrink corporate tax teams much (TAXPROF-SALA-2026). A competing R&D credit provider argues AI-only credit tools will not meet Section G (STRIKETAX-2026).
- **Evidence count:** 16 use cases (A: 0, B: 3, C: 12, D: 1). 47 sources read in full across 9 types (vendor 19, firm 9, press 6, survey 5, conference 3, academic 2, regulator 1, job-posting 1, professional-body 1). No sources were search-only in the final list.

---

## 2. Use cases

Conventions used below:

- **Grades.** A firm's or vendor's own announcement or product page is grade C even when the firm is large. B requires a named organization described as running the work.
- **Provenance.** `self-reported` marks a statement by the organization describing its own use. `vendor-published` marks a vendor, or a firm describing a product or service it sells.
- **Dates.** A source date of `2026-10` marks a page with no publication date; it is the retrieval month (retrieved 2026-10-17) and the locator says so. `2026-03` for the TEI agenda and the Bloomberg Tax ASC 740 page is the month the document or page metadata gives.
- **Cap rule.** Evidence from an adjacent process (K-1 intake in asset and wealth management; personal income tax calculation) is capped at B.
- **Ladder and scope** are the analyst's reading of what the source describes.

```yaml

- id: tax-compliance-corporate-01
  title: AI maps general-ledger and trial-balance accounts to the tax chart of accounts before the compliance load
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - data-reporting
  - transaction-processing
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Before a corporate return can be prepared, ledger data from many entities and countries has to be extracted, mapped to tax accounts and checked for inconsistencies. EY describes this as taking weeks and several people for multinationals, and Thomson Reuters Institute reports that tax professionals spend more than half their time on reactive work, mostly compliance.
  solution: 'EY describes a GenAI-assisted tool that ingests the extracted ledger data, standardises it and maps it using pre-vetted prompts, after which a qualified team member reviews the result. Thomson Reuters says its goal for ONESOURCE direct tax is agentic AI that handles data import, validation and mapping while tax professionals keep oversight. Salesforce''s earlier, non-AI approach shows the same step done by rules: a tax data blueprint mapping ledger accounts to Corptax M codes.'
  outcomes:
  - lever: speed
    description: EY says the multi-country mapping step can become a two-day process with human review, in place of weeks of manual work. No client or measurement is named.
    figure: two days (stated as achievable)
    measures: elapsed time to extract, map and review general-ledger accounts for tax across countries at a multinational; an illustrative 'AI in practice' example with no sample, baseline or method given
    provenance: vendor-published
    source_ref: EY-COMPL-2026
  prerequisites:
  - A defined tax chart of accounts or M-code design that the mapping targets
  - Ledger extracts available from each entity and country in a consistent format
  - Pre-vetted prompts or mapping rules signed off by tax
  - A blueprint of which adjustments are automated in the compliance engine (as in the Salesforce case)
  risks_and_guardrails:
  - Mapping errors can compound across entities in multi-entity structures (Bloomberg Tax, a vendor, makes this point about corporate tax calculations).
  - TEI Tax Tech 2026 attendees described AI that fails quietly, so reviewers need a way to see what was mapped and why.
  - Mapping logic built by one person and never documented was cited as a risk for automation workflows (Alteryx workflows nobody could explain).
  human_checkpoints:
  - A qualified team member reviews the AI-produced mapping before it is loaded (EY)
  - Tax approves the mapping rules or prompts before use
  role_evolution: Staff shift from building mappings by hand to reviewing and correcting AI-proposed mappings and maintaining the rules; EY says the work moves from assembling information to applying judgment.
  evidence_grade: C
  sources:
  - ref: EY-COMPL-2026
    title: 'AI and the transformation of tax compliance (page title: Tax transformation: Adopting AI to drive efficiencies)'
    publisher: EY US
    type: firm
    url: https://www.ey.com/en_us/insights/tax-compliance/ai-and-the-transformation-of-tax-compliance
    date: '2026-02-12'
    access: full
    locator: Box 'AI in practice' on general-ledger account mapping; section on categorisation (mapping trial balance accounts to tax-sensitized charts of accounts)
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: Paragraph beginning 'Thomson Reuters ONESOURCE direct tax solutions' (goal of agentic AI for data import, validation and mapping)
  - ref: CSC-SALESFORCE-2026
    title: 'Fragmentation to Integration: Salesforce Files Six Weeks Sooner (Corptax data blueprint and automation, not AI)'
    publisher: CSC Corptax
    type: vendor
    url: https://cscglobal.com/service/corptax/case-studies/salesforce/
    date: 2026-10
    access: full
    locator: Paragraph on the tax data blueprint mapping ledger accounts to Corptax M codes (pre-AI baseline; page undated, retrieved 2026-10)
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain (recap of the 27-29 Apr 2026 seminar)'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Paragraphs on silent failures and undocumented workflows
  last_reviewed: '2026-10-17'
  notes: Grade C because the only quantified statement is EY's own illustration. The Salesforce case is rules-based automation and is cited only for the prerequisite. Bloomberg Tax text on error compounding is from a vendor guide (BTAX-CORPAI-2026).
- id: tax-compliance-corporate-02
  title: Agents interpret K-1 footnotes and map them to tax treatments, with a confidence score and a logged reviewer override
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - transaction-processing
  - expert-judgment
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: PwC describes historic K-1 processing as guides and trained staff interpreting each item, with heavy human review, and a group conferring when a footnote had not been seen before. OCR tools had been layered on for extraction.
  solution: PwC's AI tax leader says agents trained on how to treat different expenses and disclosures assess a K-1 footnote, say how they interpreted it and give a confidence level. A reviewer sees the flag, may override, and is asked to say why so the agent can learn from the correction. Agents run on PwC's Agent OS, which manages the tools each agent can use, such as data mapping and document extraction.
  outcomes:
  - lever: capacity
    description: PwC's AI tax leader says one person reviews the output where several people previously met to decide an unfamiliar footnote. No time, volume or accuracy figure is published.
    figure: none published
    measures: no measurement; the interview describes one reviewer replacing a group discussion on novel K-1 footnotes
    provenance: self-reported
    source_ref: PWC-MEGNA-2025
  prerequisites:
  - Historical treatment data to train agents
  - A tool layer for document extraction and data mapping
  - An agent management platform (PwC's Agent OS) for orchestration and monitoring
  - Reviewer feedback loop for overrides
  risks_and_guardrails:
  - Confidence is rarely 100%, and PwC says up-front training and continued retraining on new data are needed.
  - PwC says outputs stay inside a human-reviewed, multi-eye process, and complex outputs such as tax calculations get strong oversight.
  - Approved processes are locked so changes are not made ad hoc (PwC).
  human_checkpoints:
  - Reviewer checks flagged items and low-confidence interpretations
  - Override reasons are recorded to retrain the agent
  - Firm governance committee oversees how agents are built and used
  role_evolution: PwC says its AI champions (over 3,200) and a workforce-transformation team embedded in tax help staff adopt tools; reviewers move from deciding items in a group to checking an agent's stated reasoning.
  evidence_grade: B
  sources:
  - ref: PWC-MEGNA-2025
    title: How PwC's tax team is using agentic AI (interview with Dom Megna, PwC US AI Tax Leader)
    publisher: CFO.com
    type: firm
    url: https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/
    date: '2025-06-06'
    access: full
    locator: Answers on K-1 data mapping, feedback and override, Agent OS, governance committee and AI champions
  last_reviewed: '2026-10-17'
  notes: The setting described is K-1 intake in PwC's asset and wealth management tax work, which feeds partnership and corporate-investor returns. It is therefore adjacent to corporate direct-tax compliance, and the grade is capped at B. PwC also says it has more than 800 custom GPTs and more than 250 AI agents firm-wide, including in tax. Whether these are in the same workflow is not stated. No override rate is given.
- id: tax-compliance-corporate-03
  title: AI compares returns and source data year on year and flags anomalies to direct reviewer attention
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Reviewers of corporate returns and workpapers compare against prior years and source schedules by hand. EY says tax transparency and authorities' wider access to company data raise the importance of consistent data across functions and jurisdictions.
  solution: EY says AI-enabled comparison of US corporate income tax returns can speed data gathering and pinpoint inconsistencies, and that anomaly scans can help the preparer decide where to spend review time. Baker Tilly describes AI flagging unusual effective tax rate movements and inconsistencies across entities. Corptax lists PDF comparison and tax code version tracking on its AI/ML roadmap. Deloitte gives flagging anomalies in source data and account reconciliations for human review as an example of a lower-risk start.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: no figure published; sources describe what AI can do, not a measured result
    provenance: vendor-published
    source_ref: EY-COMPL-2026
  prerequisites:
  - Prior-year returns and workpapers in a comparable, machine-readable form
  - Consistent entity and account structure across years
  - Reviewer-agreed thresholds for what counts as an anomaly
  risks_and_guardrails:
  - Anomaly lists are only as good as the data; TEI Tax Tech 2026 attendees worried about how to review growing volumes of work when errors are quiet and technical.
  - Bloomberg Tax (vendor) lists IRS examination exposure and SOX control failures among risks of unverified AI outputs.
  human_checkpoints:
  - Reviewer decides which flagged items matter
  - Preparer resolves each flagged inconsistency before sign-off
  role_evolution: EY says AI can help reviewers focus on the items that add the most value or carry the greatest risk, with preparation done by AI and staff reviewing outputs.
  evidence_grade: C
  sources:
  - ref: EY-COMPL-2026
    title: 'AI and the transformation of tax compliance (page title: Tax transformation: Adopting AI to drive efficiencies)'
    publisher: EY US
    type: firm
    url: https://www.ey.com/en_us/insights/tax-compliance/ai-and-the-transformation-of-tax-compliance
    date: '2026-02-12'
    access: full
    locator: Section on identifying year-over-year data anomalies and the AI-enabled comparison of US corporate income tax returns
  - ref: BAKERTILLY-2026
    title: 'The new tax operating model: AI as a strategic partner'
    publisher: Baker Tilly US
    type: firm
    url: https://www.bakertilly.com/insights/the-new-tax-operating-model-ai-as-a-strategic-partner
    date: '2026-02-20'
    access: full
    locator: Paragraph on flagging unusual ETR movements and inconsistencies across entities
  - ref: CORPTAX-2026
    title: ACT and CSC Corptax webinar on AI and machine learning in tax (Corptax AI/ML roadmap)
    publisher: CSC Corptax
    type: vendor
    url: https://go.corptax.com/act-ai-ml-tax
    date: 2026-10
    access: full
    locator: 'Roadmap list: PDF comparisons, audit prediction, tax code version tracking'
  - ref: DELOITTE-TTT-2026
    title: 'Riding the wave: A framework to plan for AI (Tax Transformation Trends AI report, part three)'
    publisher: Deloitte Global
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf
    date: 2026-07
    access: full
    locator: 'Scenario 1 discussion: AI agents flagging anomalies in source data and account reconciliations'
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain (recap of the 27-29 Apr 2026 seminar)'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Paragraph on reviewing increasing volumes when errors are quiet
  last_reviewed: '2026-10-17'
  notes: All sources describe capability or roadmap. No named corporate team or measured result was found.
- id: tax-compliance-corporate-04
  title: Preparation shifts to AI and staff review its output, with fewer review layers where outputs are consistent
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: EY describes the current model as a staff-level team member doing most compliance preparation, followed by layers of review.
  solution: 'EY says that in future AI will do much of the preparation, staff will monitor it and review initial outputs, and fewer review levels may be needed because AI output is consistent. PwC says complex outputs keep multi-eye review, while simple diagnostics may not need three layers. The practice shift also bears on pricing: Bloomberg Tax reports top firms exploring value-based fees as AI cuts billable hours.'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: no figure published; this is a stated direction, not a measured result
    provenance: vendor-published
    source_ref: EY-COMPL-2026
  prerequisites:
  - Evidence that AI output is consistent enough to justify fewer review layers
  - Redefined review roles and sign-off levels
  - Documentation of what AI did, so reviewers can rely on it
  risks_and_guardrails:
  - Sala argues the corporate tax function is not a return-preparation pool, so large headcount effects from automating preparation are overstated; AI cannot carry regulatory, ethical or financial culpability.
  - The IRS Office of Professional Responsibility says practitioners keep full responsibility for AI-assisted work and must verify facts, citations and calculations (as reported by the Journal of Accountancy).
  - Only 2 of more than 50 attendees polled at TEI Tax Tech 2026 said tax owns AI implementation at their company.
  human_checkpoints:
  - Qualified professional reviews AI-prepared output
  - Complex outputs keep multi-person review (PwC)
  role_evolution: EY says the process, the roles and the ordering of tasks need to change, with staff monitoring AI. Sala predicts AI will not shrink corporate tax teams much. KPMG Germany's survey reports 58% expect stable domestic tax headcount.
  evidence_grade: C
  sources:
  - ref: EY-COMPL-2026
    title: 'AI and the transformation of tax compliance (page title: Tax transformation: Adopting AI to drive efficiencies)'
    publisher: EY US
    type: firm
    url: https://www.ey.com/en_us/insights/tax-compliance/ai-and-the-transformation-of-tax-compliance
    date: '2026-02-12'
    access: full
    locator: Section on operating model change, 'staff-level team member' passage
  - ref: PWC-MEGNA-2025
    title: How PwC's tax team is using agentic AI (interview with Dom Megna, PwC US AI Tax Leader)
    publisher: CFO.com
    type: firm
    url: https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/
    date: '2025-06-06'
    access: full
    locator: Answer on human-reviewed, multi-eye process and layers of review
  - ref: TAXPROF-SALA-2026
    title: 'Sala: AI Won''t Shrink Corporate Tax Teams Much. Here''s Why. (abstract of 121 Tax Notes State 189, 20 Jul 2026)'
    publisher: TaxProf Blog (AALS)
    type: press
    url: https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/
    date: '2026-07-20'
    access: full
    locator: Abstract, paragraphs 1-2
  - ref: JOFA-OPR-2026
    title: IRS outlines AI risks, Circular 230 duties for tax practitioners
    publisher: Journal of Accountancy
    type: press
    url: https://www.journalofaccountancy.com/news/2026/jun/irs-outlines-ai-risks-circular-230-duties-for-tax-practitioners/
    date: '2026-06-26'
    access: full
    locator: Paragraphs on practitioner responsibility and verification
  - ref: KPMG-DE-2026
    title: Tax departments are increasingly turning to artificial intelligence (two KPMG quick surveys)
    publisher: KPMG Germany
    type: survey
    url: https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html
    date: '2026-05-06'
    access: full
    locator: Headcount expectations paragraph
  - ref: BTAX-PRICING-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Tax
    type: press
    url: https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: Opening paragraphs on value-based pricing
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain (recap of the 27-29 Apr 2026 seminar)'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Paragraph on the poll about who owns AI implementation
  last_reviewed: '2026-10-17'
  notes: A forward-looking statement by a firm and a contrary academic view. No firm reports having removed a review layer.
- id: tax-compliance-corporate-05
  title: Agents roll forward prior-year workpapers and prepare review-ready business returns (1120, 1120-S, 1065) including book-to-tax and state apportionment
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - transaction-processing
  - document-production
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Business-return preparation involves unstructured client data, inconsistent client data, changing rules and review-heavy processes. Byron's founder says most CPA automation had focused on 1040 returns because business returns were too complex to automate reliably.
  solution: Byron says specialised agents roll forward prior-year returns and workpapers into a current-year Excel workbook, request missing client information and process the data into review-ready output, covering book-to-tax adjustments, depreciation schedules, state apportionments and partnership allocations. Outputs are source-linked and confidence-scored, and approved data moves into existing tax software. Thomson Reuters says its Ready to Review agents handle 1040s now and will expand to business returns. RSM has launched myRSM Tax, which it says integrates generative AI into core tax workflows across entities and individuals.
  outcomes:
  - lever: quality
    description: Byron says its extraction is more than 97% accurate across federal, state, K-3 and footnote extractions.
    figure: '>97% accuracy (company statement)'
    measures: accuracy of data extraction across federal, state, K-3 and footnote extractions; the source gives no sample size, test set or definition of accuracy
    provenance: vendor-published
    source_ref: BYRON-2026
  prerequisites:
  - Integration with the tax software and document systems the firm already uses
  - Prior-year workpapers in Excel
  - Client data intake process that the agent can query for missing information
  - SOC 2 Type II and role-based access (Byron states it has these)
  risks_and_guardrails:
  - Accuracy statement is the company's and covers extraction, not return correctness.
  - Byron says customer data is not used to train underlying models; firms still need to check this in contracts.
  - OPR guidance says practitioners must use secure, enterprise-approved AI for client data (Journal of Accountancy).
  human_checkpoints:
  - Accountants verify outputs; each extracted number is source-linked and confidence-scored (Byron)
  - Professional final review before filing
  role_evolution: Byron says agents prepare the work and accountants verify it, with firms focusing on review and judgment. Thomson Reuters says its approach lets teams take on more work without proportional hiring.
  evidence_grade: C
  sources:
  - ref: BYRON-2026
    title: Byron Launches with AI Agents for Business Tax Preparation Workflows
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/05/27/byron-launches-with-ai-agents-for-business-tax-preparation-workflows/184034/
    date: '2026-05-27'
    access: full
    locator: Paragraphs on agent workflow, accuracy statement and review model
  - ref: TR-R2R-2025
    title: 'AI tax return preparation: how Ready to Review transforms the workflow'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-tax-return-preparation-how-ready-to-review-transforms-the-workflow/
    date: '2025-12-19'
    access: full
    locator: Paragraph stating Ready to Review handles 1040s and will expand to business returns
  - ref: RSM-MYRSM-2025
    title: RSM expands AI commitment with launch of myRSM Tax
    publisher: RSM US
    type: firm
    url: https://rsmus.com/newsroom/2025/rsm-expands-ai-commitment-with-launch-of-myrsm-tax.html
    date: '2025-06-16'
    access: full
    locator: Paragraphs 1-3 describing myRSM Tax
  - ref: JOFA-OPR-2026
    title: IRS outlines AI risks, Circular 230 duties for tax practitioners
    publisher: Journal of Accountancy
    type: press
    url: https://www.journalofaccountancy.com/news/2026/jun/irs-outlines-ai-risks-circular-230-duties-for-tax-practitioners/
    date: '2026-06-26'
    access: full
    locator: Paragraph on secure, enterprise-approved AI
  last_reviewed: '2026-10-17'
  notes: Targeted at CPA firms preparing returns for clients, so it is firm-side, not an in-house deployment. No named customer firm and no independent test was found. Thomson Reuters' statement about business returns is a plan.
- id: tax-compliance-corporate-06
  title: Tax firms build agent platforms ('agent factories') to create, deploy and manage tax agents at scale
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - software-systems
  - transaction-processing
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Firms and clients need many agents for data collection, document analysis and compliance tasks, and need a way to track and coordinate them. PwC says it built Agent OS because dozens of unmanaged agents lack performance tracking and coordination.
  solution: EY says its Tax Agent Factory is a methodology, operating model and technology strategy to design, build, train, deploy and manage agents at scale, and that Tax Labs co-designs AI journeys with clients. KPMG and Anthropic announced Claude inside KPMG's Digital Gateway, starting with tax clients and private equity. Bloomberg Tax reported in March 2025 that EY planned to roll out as many as 150 agents to 80,000 tax professionals.
  outcomes:
  - lever: capacity
    description: EY said in March 2025 it planned to roll out as many as 150 agents to 80,000 tax professionals within three months; no usage or output data has been published.
    figure: up to 150 agents, 80,000 tax professionals (planned)
    measures: count of agents planned and number of EY tax professionals as stated by an EY executive to Bloomberg Tax in March 2025; a plan, not a measured result
    provenance: self-reported
    source_ref: BTAX-BIG4-2025
  - lever: speed
    description: KPMG US's tax vice chair says building an agent to help clients adjust to changing tax regulations used to take weeks and now takes minutes.
    figure: weeks to minutes
    measures: time to build a client agent for changing tax rules, as stated by a KPMG executive; no sample, baseline or method given
    provenance: self-reported
    source_ref: KPMG-ANTHROPIC-2026
  prerequisites:
  - Alliances with model and cloud providers
  - A governed platform where agents and tools are managed (Agent OS, Digital Gateway)
  - Firm tax data and domain knowledge to ground agents
  - Governance and assurance for AI systems (KPMG Trusted AI framework; PwC governance committee)
  risks_and_guardrails:
  - KPMG says it will embed cybersecurity, risk and AI assurance in how systems are designed and operated.
  - Announcements give no error rate, override rate or quality result.
  - Deloitte warns that agentic corrections to source data will need to be written back to the system of record to keep an audit-ready posture.
  human_checkpoints:
  - Human review of agent outputs inside client engagements
  - Firm-level governance committee oversight (PwC)
  role_evolution: EY says agents free tax professionals for judgment work. KPMG says 276,000 people get access to Claude. Bloomberg Tax noted the tools could dampen future staff needs.
  evidence_grade: C
  sources:
  - ref: BTAX-BIG4-2025
    title: Big Four Firms Roll Out AI That Can Handle Routine Tasks Solo
    publisher: Bloomberg Tax
    type: press
    url: https://news.bloombergtax.com/financial-accounting/big-four-firms-roll-out-ai-that-can-handle-routine-tasks-solo
    date: '2025-03-24'
    access: full
    locator: Paragraphs on EY's plan for 150 agents and 80,000 tax professionals
  - ref: EY-TAXLABS-2025
    title: EY unveils suite of powerful AI capabilities to accelerate tax transformation and deliver strategic value
    publisher: EY Global
    type: firm
    url: https://www.ey.com/en_gl/newsroom/2025/11/ey-unveils-suite-of-powerful-ai-capabilities-to-accelerate-tax-transformation-and-deliver-strategic-value
    date: '2025-11-25'
    access: full
    locator: Paragraphs on Tax Labs and Tax Agent Factory
  - ref: KPMG-ANTHROPIC-2026
    title: KPMG Partners with Anthropic for Digital Gateway Powered by Claude
    publisher: CPA Practice Advisor (reproducing the KPMG and Anthropic announcement)
    type: firm
    url: https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/
    date: '2026-05-20'
    access: full
    locator: Quotation from Rema Serafi and Digital Gateway description
  - ref: PWC-MEGNA-2025
    title: How PwC's tax team is using agentic AI (interview with Dom Megna, PwC US AI Tax Leader)
    publisher: CFO.com
    type: firm
    url: https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/
    date: '2025-06-06'
    access: full
    locator: Answer on why PwC built Agent OS
  - ref: DELOITTE-TTT-2026
    title: 'Riding the wave: A framework to plan for AI (Tax Transformation Trends AI report, part three)'
    publisher: Deloitte Global
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf
    date: 2026-07
    access: full
    locator: Scenario 2 discussion of write-back of agentic corrections
  last_reviewed: '2026-10-17'
  notes: These are firm announcements. EY's target is reported by the press from a Mar 2025 interview; the follow-up result is not published. The landscape's '3 million compliance tasks' figure was not confirmed in a primary source and is not used.
- id: tax-compliance-corporate-07
  title: 'R&D credit: AI builds contemporaneous qualified-research documentation from project and payroll systems and populates Form 6765'
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - data-reporting
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Thomson Reuters says R&D credit work built on engineer interviews and retrospective surveys takes over 200 hours a year and can draw audit adjustments of 10% or more. Revised Form 6765 requires business-component detail in a new Section G.
  solution: Neo.Tax connects to project management, payroll, accounting and ERP systems by API, clusters ticket-level data into business components, applies the four-part test (per Thomson Reuters), reconciles payroll and ledger data to allocate costs, and passes the result into ONESOURCE Income Tax to populate Form 6765 including Section G. Baker Tilly and EY describe the same shift from interviews and timesheets to AI over ERP and project data.
  outcomes:
  - lever: speed
    description: Thomson Reuters says the integration reduces filing time from weeks to days.
    figure: weeks to days
    measures: time to prepare the Form 6765 filing with Neo.Tax inside ONESOURCE; no sample or baseline stated
    provenance: vendor-published
    source_ref: TR-NEOTAX-2025
  - lever: cost
    description: Thomson Reuters says companies report 50-75% savings compared to accounting-firm fees.
    figure: 50-75% lower fees (reported)
    measures: R&D credit study cost compared with accounting-firm fees; 'companies report', with no sample count or method
    provenance: vendor-published
    source_ref: TR-NEOTAX-2025
  - lever: risk
    description: Thomson Reuters says companies report 20-30% lower FIN 48 reserves compared to interview-driven studies.
    figure: 20-30% lower reserves (reported)
    measures: FIN 48 reserves compared with interview-driven studies; 'companies report', with no sample count or method
    provenance: vendor-published
    source_ref: TR-NEOTAX-2025
  - lever: capacity
    description: The Thomson Reuters product page says AI finds R&D costs across internal systems, saving 150+ hours.
    figure: 150+ hours
    measures: hours saved identifying and validating R&D costs; the page gives no period or baseline (the blog's manual baseline is over 200 hours a year)
    provenance: vendor-published
    source_ref: TR-NEOTAXPAGE-2026
  prerequisites:
  - Integrations with payroll, project management, accounting and ERP systems
  - Task-level records of R&D work captured as it happens
  - Tax-engine integration (ONESOURCE Income Tax) for Form 6765
  - Tax sign-off on business-component definitions and the four-part test
  risks_and_guardrails:
  - Strike Tax Advisory, a competing R&D credit provider, argues AI questionnaire workflows cannot reconstruct the Section G artifact after the fact and that AI cannot make the legal and technical judgments under Section 41.
  - 'The effective date of the revised form is described differently by sources: Thomson Reuters says finalised Feb 2025, optional for 2025 and mandatory for tax year 2026; Strike Tax says instructions were finalised on 5 Feb 2026. The IRS Form 6765 page retrieved on 2026-10-17 shows a clarification dated 18 Jun 2025 to the January 2025 version of the instructions and does not mention Section G.'
  - Software vendor liability is typically capped at fees paid under standard terms, per Strike Tax; an examination adjustment falls on the taxpayer.
  human_checkpoints:
  - Tax professional reviews business-component clustering and four-part-test results
  - Reconciliation of payroll and ledger allocations
  - Manual updates where people are missing from project tracking data (Neo.Tax page)
  role_evolution: Thomson Reuters says teams reduce reliance on engineer interviews and outside consultants; Baker Tilly says the shift moves tax teams away from 'find and replace' work on transaction data.
  evidence_grade: C
  sources:
  - ref: TR-NEOTAX-2025
    title: How to eliminate the burden of R&D tax credit compliance (ONESOURCE and Neo.Tax)
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/neo-tax-onesource-eliminating-the-triple-burden-of-rd-credit-compliance/
    date: '2025-09-08'
    access: full
    locator: Pain-point list; 'Effortless Form 6765 filing'; 'Cost savings + lower Fin 48' paragraphs
  - ref: TR-NEOTAXPAGE-2026
    title: ONESOURCE and Neo.Tax R&D tax credit calculation and claim (product page)
    publisher: Thomson Reuters
    type: vendor
    url: https://tax.thomsonreuters.com/en/corporation-solutions/c/neotax
    date: 2026-10
    access: full
    locator: Page text on 150+ hours (page undated; retrieved 2026-10)
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: Neo.Tax section on Section G and contemporaneous standard
  - ref: BAKERTILLY-2026
    title: 'The new tax operating model: AI as a strategic partner'
    publisher: Baker Tilly US
    type: firm
    url: https://www.bakertilly.com/insights/the-new-tax-operating-model-ai-as-a-strategic-partner
    date: '2026-02-20'
    access: full
    locator: Research tax credit example paragraph
  - ref: STRIKETAX-2026
    title: 'Form 6765 Section G becomes mandatory in 2026: most AI-only R&D credit tools will not be ready'
    publisher: Strike Tax Advisory
    type: vendor
    url: https://www.striketax.com/journal/form-6765-section-g-becomes-mandatory-in-2026-most-ai-only-r-d-credit-tools-will-not-be-ready
    date: 2026-08
    access: full
    locator: Opening and 'what the IRS has said' sections
  - ref: IRS-6765-2026
    title: About Form 6765, Credit for Increasing Research Activities
    publisher: Internal Revenue Service
    type: regulator
    url: https://www.irs.gov/forms-pubs/about-form-6765
    date: '2026-06-20'
    access: full
    locator: Revision list on the Form 6765 page
  - ref: TEI-MIDYEAR-2026
    title: TEI Midyear Conference 2026 at-a-glance agenda, preliminary (Washington DC, 15-18 Mar 2026)
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: 2026-03
    access: full
    locator: 'Tax Lab: Research Credit Automation (15-18 Mar 2026 agenda)'
  last_reviewed: '2026-10-17'
  notes: All outcome figures are vendor-published, are unattributed to any named customer, and the TR page does not say how they were measured. The Neo.Tax customer list seen in search results (Mercury, Notion and others) is search-only and not used. The Section G effective-date conflict is unresolved here; check the IRS instructions for the filing year.
- id: tax-compliance-corporate-08
  title: In-house tax team runs governed AI automation of data extraction, reconciliation and reporting with a full audit trail
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - data-reporting
  - transaction-processing
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: 'Kognitos argues the binding constraint in corporate tax is now data: assembling and reconciling source data from ledgers and systems, not the calculation, which engines such as ONESOURCE and Corptax handle once data is clean.'
  solution: Savant says its platform turns messy data into governed, repeatable outputs with an audit trail, and planned live demonstrations of multi-system reconciliation across ERPs and source documents, AI document extraction and validation, and reporting with data lineage. Oxford Industries (parent of Tommy Bahama and others) was to co-present with Savant on how its tax team deploys AI safely and at scale. Kognitos positions its agent platform as the layer that assembles, reconciles and validates source data for the tax engines.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: the Oxford Industries session is announced, with no results published; which workflows Oxford runs is not stated
    provenance: vendor-published
    source_ref: SAVANT-2026
  prerequisites:
  - Data-lineage and audit-trail capability
  - Source systems reachable by the automation layer
  - A tax data blueprint (see Salesforce case)
  - Ownership of the AI process within or alongside tax
  risks_and_guardrails:
  - At TEI Tax Tech 2026, attendees said tax rarely owns AI implementation, that training rollouts can fail, and that unexplained workflows left by departed staff are a hazard.
  - Rising token costs were raised as a threat to the economic case for automation (Thomson Reuters Institute recap).
  - Savant, Kognitos and Bloomberg Tax are vendors; claims about governance are theirs.
  human_checkpoints:
  - Tax reviews reconciled outputs and exceptions
  - Audit-ready reporting with lineage retained for auditors
  role_evolution: 'Savant''s announced Oxford speaker is a Senior Director of Tax & Accounting, so the session was to be fronted by a tax leader. The Thomson Reuters Institute recap quotes a senior director: ''You will not survive in this field if you don''t have a change mindset.'''
  evidence_grade: B
  sources:
  - ref: SAVANT-2026
    title: Savant Showcases Audit-Ready Agentic AI at TEI Tax Tech 2026
    publisher: Savant Labs
    type: vendor
    url: https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/
    date: '2026-04-16'
    access: full
    locator: Press release paragraphs on the Oxford Industries co-presented session and live demonstrations
  - ref: KOGNITOS-2026
    title: AI for Corporate Tax and Provision Automation (2026)
    publisher: Kognitos
    type: vendor
    url: https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/
    date: '2026-06-17'
    access: full
    locator: Sections on data as the binding constraint and the engine versus data layer
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain (recap of the 27-29 Apr 2026 seminar)'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Paragraphs on governance, polling and token costs
  last_reviewed: '2026-10-17'
  notes: Grade B rests on one named in-house team (Oxford Industries) described by a vendor press release dated 16 Apr 2026 ahead of the session; the release does not state outcomes or which tax workflows Oxford runs. Kognitos and Savant customer lists in search results were not verified.
- id: tax-compliance-corporate-09
  title: A small in-house tax team builds its own AI agents and data pipelines for ingestion, validation, compliance and reporting
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - software-systems
  - data-reporting
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: background-agent
  maturity: in-production
  problem: A tax department that must meet corporate income tax return compliance and ASC 740 reporting needs reliable data flows into return software; OpenAI's job listing says tax expertise remains the cornerstone while technical skills such as SQL, Python and machine learning are valuable.
  solution: OpenAI's listing for a Senior Manager, Tax Data Automation asks for leading automation of ingestion, validation, compliance and reporting using AI-driven agents, SQL-based pipelines, metadata repositories and tax logic frameworks, working with engineering teams. It asks for experience implementing and operating Corptax or ONESOURCE Income Tax. The Thomson Reuters Institute reports that four members of OpenAI's tax department demonstrated live automation pipelines at TEI Tax Tech 2026, and an OpenAI tax operations director was listed as a panellist at a Bloomberg Tax forum session on AI in compliance and provisioning.
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: no results published; the evidence is a job listing and a conference demonstration
    provenance: vendor-published
    source_ref: OPENAI-JOB-2025
  prerequisites:
  - Tax staff with SQL, Python and engineering collaboration skills
  - Metadata repositories and tax logic frameworks
  - Return software such as Corptax or ONESOURCE Income Tax already in operation
  - Documentation, best practices and training for tax and finance staff
  risks_and_guardrails:
  - Unexplained automations were cited as a hazard at TEI Tax Tech 2026.
  - The listing was posted in Jan 2025 and closed (valid through 11 Mar 2025), so it shows intent at that date, not current practice.
  human_checkpoints:
  - Tax expertise applied to ensure regulatory adherence and accuracy in automated processes (job listing)
  role_evolution: The listing combines 10+ years of tax experience in corporate, partnership and international tax with SQL and Python skills; the role also delivers training programmes for tax and finance staff.
  evidence_grade: B
  sources:
  - ref: OPENAI-JOB-2025
    title: Senior Manager, Tax Data Automation (job listing, OpenAI tax team)
    publisher: OpenAI, via Khosla Ventures job board
    type: job-posting
    url: https://jobs.khoslaventures.com/companies/openai/jobs/45083210-senior-manager-tax-data-automation
    date: '2025-01-22'
    access: full
    locator: Responsibilities and qualifications lists
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain (recap of the 27-29 Apr 2026 seminar)'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Paragraph on OpenAI sending four tax department members to demonstrate live automation pipelines
  - ref: BTAX-FORUM-2026
    title: Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk (programme announcement for the 16 Jun 2026 forum)
    publisher: Bloomberg Tax
    type: conference
    url: https://pro.bloombergtax.com/?p=17345
    date: '2026-06-10'
    access: full
    locator: Panel 'Emerging Technologies and AI Integration' panellist list
  last_reviewed: '2026-10-17'
  notes: OpenAI is an AI company, so its tax team is unlikely to be typical. Grade B rests on a named organisation's listing and a recap of a live demonstration; no measured outcome.
- id: tax-compliance-corporate-10
  title: Cited AI tax research and assistants sit inside the compliance and workpaper tools
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: Compliance staff leave their return, workpaper or tracking tool to research a question, and junior staff lean on outside advisors for harder ones.
  solution: Thomson Reuters says it embedded CoCounsel Tax into ONESOURCE direct tax solutions in late 2024, returning structured, citable research from natural-language queries. Bloomberg Tax describes AI insights and current rates inside its Workpapers spreadsheets and an AI Assistant in its Compliance Tracker that summarises and analyses filings, with Deep Thinking Mode for multi-step questions. TEI Midyear 2026 ran hands-on labs on AI tax research and on analysing Excel files with AI.
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: Thomson Reuters says junior staff can handle more complex questions with cited sources and teams may need outside advisors less often for some; no figure published
    provenance: vendor-published
    source_ref: TR-CORPAI-2026
  prerequisites:
  - Grounding in authoritative content (Checkpoint, Bloomberg Tax Portfolios)
  - Embedding in the tools where staff already work
  - Approved-use policy and secure enterprise deployment
  risks_and_guardrails:
  - Bloomberg Tax (vendor) warns that generic models can hallucinate and lack source traceability; it recommends human verification of citations.
  - Thomson Reuters' tension survey found that 45% of corporate tax departments have no relevant AI policy.
  human_checkpoints:
  - Staff verify cited sources before relying on output
  role_evolution: Thomson Reuters says junior staff can work through more complex questions with cited sources; Bloomberg Tax calls for human oversight of citations.
  evidence_grade: C
  sources:
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: Paragraph on CoCounsel Tax embedded in ONESOURCE direct tax solutions in late 2024
  - ref: BTAX-ASC740-2026
    title: Accelerate your ASC 740 process (Bloomberg Tax Research, Provision and Workpapers product page)
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/products/accelerate-your-asc-740-process/
    date: 2026-03
    access: full
    locator: Paragraph on AI-powered insights in Workpapers
  - ref: BTAX-TOOLS-2026
    title: Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026
    date: '2026-03-09'
    access: full
    locator: 'Feature list: Deep Thinking Mode, AI Assistant in Compliance Tracker, document-based analysis'
  - ref: BTAX-LEVERAGE-2026
    title: How to Leverage AI for Corporate Tax Success in 2026
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/insights/tax-automation/how-to-leverage-ai-for-corporate-tax-success-in-2026/
    date: '2026-03-18'
    access: full
    locator: Risk section on hallucination and oversight
  - ref: TR-TENSIONS-2025
    title: 5 GenAI tensions corporate tax departments should address (from the 2025 Generative AI in Professional Services Report)
    publisher: Thomson Reuters Tax & Accounting
    type: survey
    url: https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address-tri/
    date: '2025-06-24'
    access: full
    locator: 'Governance tension: policy coverage figures'
  - ref: TEI-MIDYEAR-2026
    title: TEI Midyear Conference 2026 at-a-glance agenda, preliminary (Washington DC, 15-18 Mar 2026)
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: 2026-03
    access: full
    locator: Tax Labs on AI tax research and Excel analysis
  last_reviewed: '2026-10-17'
  notes: All sources are vendors or a conference programme. Research as a stand-alone activity belongs to research-advisory; this entry covers research embedded in compliance workpapers and engines.
- id: tax-compliance-corporate-11
  title: AI assistant for the tax calendar and obligation tracker, with regulatory-change monitoring
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - coordination-scheduling
  - research-synthesis
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Corporate departments track federal, state and international due dates, extensions and rule changes across many entities, often in spreadsheets.
  solution: Bloomberg Tax announced an AI Assistant in its Compliance Tracker that answers workflow questions by summarising and analysing filings. Orbitax's XatBot has a Tax Flows mode that tracks regulatory changes across jurisdictions and distributes comparison reports to stakeholders. Corptax lists tax code version tracking on its AI/ML roadmap.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: no figure published; Bloomberg Tax says the assistant saves time and reduces risk without measurement
    provenance: vendor-published
    source_ref: BTAX-TOOLS-2026
  prerequisites:
  - A single record of entities, jurisdictions and filing obligations
  - Current rule and due-date content
  - Stakeholder distribution lists
  risks_and_guardrails:
  - Missed or wrong dates carry penalties; Thomson Reuters Institute found 56% of respondents who spent more than half their time reactive said their departments incurred penalties, against 31% of those mainly proactive.
  - No source describes AI preparing or scheduling estimated payments for corporates.
  human_checkpoints:
  - Tax confirms deadlines and changes before action
  role_evolution: Not described in the sources; Bloomberg Tax frames it as saving time and reducing risk.
  evidence_grade: C
  sources:
  - ref: BTAX-TOOLS-2026
    title: Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026
    publisher: Bloomberg Tax
    type: vendor
    url: https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026
    date: '2026-03-09'
    access: full
    locator: 'Feature list: AI Assistant in Compliance Tracker'
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: 'Orbitax XatBot section: Tax Flows'
  - ref: CORPTAX-2026
    title: ACT and CSC Corptax webinar on AI and machine learning in tax (Corptax AI/ML roadmap)
    publisher: CSC Corptax
    type: vendor
    url: https://go.corptax.com/act-ai-ml-tax
    date: 2026-10
    access: full
    locator: 'Roadmap: tax code version tracking'
  - ref: TR-CORPTAX-2025
    title: 'The GenAI paradox: Why most tax departments aren''t using AI yet, and what early adopters are gaining (reports the 2025 State of the Corporate Tax Department survey)'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/
    date: '2025-10-22'
    access: full
    locator: Penalty comparison paragraph (reactive versus proactive)
  last_reviewed: '2026-10-17'
  notes: The penalty comparison is a survey association (288 departments), not an effect of any tool. No evidence was found for AI in estimated-payment calculation or extension tracking for corporates.
- id: tax-compliance-corporate-12
  title: Pre-filing audit-risk prediction from return data
  archetype: tax
  module: compliance-corporate
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Tax authorities are adopting AI to sharpen enforcement, and Bloomberg Tax's forum programme says executives should prioritise data integrity, audit trails and proactive compliance.
  solution: Corptax lists audit prediction on its AI/ML roadmap, to address potential audit triggers early. Deloitte's scenario framework crosses a company's AI adoption with its tax authority's AI progress and notes that tax can become a stress test of enterprise AI governance.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: none published; the Corptax item is a roadmap line
    provenance: vendor-published
    source_ref: CORPTAX-2026
  prerequisites:
  - Return and workpaper data in analysable form
  - Knowledge of authority audit selection signals
  risks_and_guardrails:
  - Audit-risk models built without knowledge of authority selection logic may mislead.
  - Sources do not report any accuracy test.
  human_checkpoints:
  - Tax decides whether to adjust positions or disclosures
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: CORPTAX-2026
    title: ACT and CSC Corptax webinar on AI and machine learning in tax (Corptax AI/ML roadmap)
    publisher: CSC Corptax
    type: vendor
    url: https://go.corptax.com/act-ai-ml-tax
    date: 2026-10
    access: full
    locator: 'Roadmap list: audit prediction'
  - ref: DELOITTE-TTT-2026
    title: 'Riding the wave: A framework to plan for AI (Tax Transformation Trends AI report, part three)'
    publisher: Deloitte Global
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf
    date: 2026-07
    access: full
    locator: 'Summary section: stress test of AI governance; scenario framework'
  - ref: BTAX-FORUM-2026
    title: Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk (programme announcement for the 16 Jun 2026 forum)
    publisher: Bloomberg Tax
    type: conference
    url: https://pro.bloombergtax.com/?p=17345
    date: '2026-06-10'
    access: full
    locator: Final panel description
  last_reviewed: '2026-10-17'
  notes: Roadmap-level only. Authority-side AI is routed to controversy.
- id: tax-compliance-corporate-13
  title: Continuously updated effective-tax-rate and cash-tax modelling with what-if scenarios
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - data-reporting
  - expert-judgment
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: Static spreadsheet models are slow to update when entity structure, transfer pricing or supply chains change, and the impact on cash taxes and provisioning is seen late.
  solution: Baker Tilly describes AI modelling engines that ingest financial data, deferred positions, intercompany activity and entity structures to calculate jurisdictional and consolidated effective rates continuously, and run what-if scenarios on cash taxes, provisioning and financial statements. It also describes agents that download trial balances from the ERP, summarise them and compare them with prior calculations.
  outcomes:
  - lever: speed
    description: none published
    figure: none published
    measures: none published; capability description
    provenance: vendor-published
    source_ref: BAKERTILLY-2026
  prerequisites:
  - Integrated ERP and tax data
  - Defined entity structure and intercompany data
  - Standardised processes and data formats (Baker Tilly names standardisation as the backbone)
  risks_and_guardrails:
  - Scenario models are only as accurate as inputs (Kognitos on data as the constraint).
  - No source reports an error rate.
  human_checkpoints:
  - Tax reviews scenario outputs before decisions
  role_evolution: Baker Tilly says AI becomes a strategic partner when it amplifies decision making and frees people for judgment work.
  evidence_grade: C
  sources:
  - ref: BAKERTILLY-2026
    title: 'The new tax operating model: AI as a strategic partner'
    publisher: Baker Tilly US
    type: firm
    url: https://www.bakertilly.com/insights/the-new-tax-operating-model-ai-as-a-strategic-partner
    date: '2026-02-20'
    access: full
    locator: Sections on modelling engines and agentic trial-balance comparison
  - ref: KOGNITOS-2026
    title: AI for Corporate Tax and Provision Automation (2026)
    publisher: Kognitos
    type: vendor
    url: https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/
    date: '2026-06-17'
    access: full
    locator: Data as binding constraint section
  last_reviewed: '2026-10-17'
  notes: Provision-heavy; the direct-compliance part is estimated payments and cash-tax forecasting. No source describes estimated payments being computed or paid by AI for a corporate; this entry should be read with the provision module.
- id: tax-compliance-corporate-14
  title: Compliance delivered as an AI-enabled managed service, with providers expected to use AI and pricing moving toward value
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types:
  - transaction-processing
  - client-interaction
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: Thomson Reuters' survey says 77% of business tax departments want their tax service providers to use GenAI but 59% are not sure whether their providers do. Billing for hours conflicts with AI efficiency, and the IRS Office of Professional Responsibility warns against billing for time not actually spent.
  solution: Deloitte says some companies look to outsourcing to gain AI-powered solutions without capital outlay and upgrade costs. TEI Midyear 2026 included a session on managed services and staffing for the tax capacity crisis. Bloomberg Tax reports top firms exploring value- and outcome-based fees, and an RSM partner gave an illustrative case where a 20-hour client report could take 10 hours with GenAI and checking.
  outcomes:
  - lever: cost
    description: An RSM partner illustrated that a 20-hour tax advisory report could fall to 10 hours with generative AI and checking, raising the question of margin versus price reduction.
    figure: 20 hours to 10 hours (illustration)
    measures: hours to create certain tax advisory reports for clients; an example given by an RSM partner in an interview, not a measured result and not a compliance return
    provenance: self-reported
    source_ref: BTAX-PRICING-2026
  prerequisites:
  - Provider transparency about AI use
  - Pricing models not tied to hours
  - Agreed review and liability responsibilities between client and provider
  risks_and_guardrails:
  - OPR guidance says savings from AI should be reflected in client billing and AI use disclosed as appropriate; the AICPA has asked the IRS to clarify, saying the language does not appear to allow value pricing.
  - Only 20% of organisations in Thomson Reuters' survey measure GenAI return on investment.
  human_checkpoints:
  - Client and provider agree what AI does and who reviews it
  role_evolution: Bloomberg Tax reports firm leaders rethinking pricing; Thomson Reuters Institute reports clients lack insight into provider AI use.
  evidence_grade: C
  sources:
  - ref: TR-TENSIONS-2025
    title: 5 GenAI tensions corporate tax departments should address (from the 2025 Generative AI in Professional Services Report)
    publisher: Thomson Reuters Tax & Accounting
    type: survey
    url: https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address-tri/
    date: '2025-06-24'
    access: full
    locator: 'First tension: 77% and 59% figures; ROI measurement tension'
  - ref: DELOITTE-LU-2025
    title: AI-enabled tax transformation
    publisher: Deloitte Luxembourg
    type: firm
    url: https://www.deloitte.com/lu/en/services/tax/research/ai-enabled-tax-transformation.html
    date: '2025-11-19'
    access: full
    locator: Paragraph on outsourcing as a route to AI-powered solutions
  - ref: TEI-MIDYEAR-2026
    title: TEI Midyear Conference 2026 at-a-glance agenda, preliminary (Washington DC, 15-18 Mar 2026)
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: 2026-03
    access: full
    locator: 'Session ''Solving the Tax Capacity Crisis: A Blueprint for Managed Services and Staffing'''
  - ref: BTAX-PRICING-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Tax
    type: press
    url: https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: Paragraphs on value-based pricing and the RSM example
  - ref: JOFA-OPR-2026
    title: IRS outlines AI risks, Circular 230 duties for tax practitioners
    publisher: Journal of Accountancy
    type: press
    url: https://www.journalofaccountancy.com/news/2026/jun/irs-outlines-ai-risks-circular-230-duties-for-tax-practitioners/
    date: '2026-06-26'
    access: full
    locator: Paragraph on fees and unconscionable fee risk
  - ref: AICPA-CART-2026
    title: AICPA, former IRS commissioner to lead initiative on AI in tax
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/
    date: '2026-09-23'
    access: full
    locator: Last paragraph on AICPA seeking OPR clarification
  last_reviewed: '2026-10-17'
  notes: The 59% figure is quoted from the source as 'aren't sure if their companies are using GenAI', in a paragraph about service providers. Evidence is survey and press, with no published provider deployment.
- id: tax-compliance-corporate-15
  title: Tax staff build their own automations and agents with low-code and conversational builders
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - software-systems
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Tax technology teams are small and queues for IT build are long; TEI's own curriculum includes Python in Excel, Fabric for ETL and automation sustainment.
  solution: At TEI Tax Tech 2026 Google and Microsoft showed attendees how to build AI agents, and the Thomson Reuters Institute recap says attendees were deploying such tools. Orbitax's Autopilot is a conversational workflow builder inside its International Tax Platform that automates multi-step tasks. TEI Midyear 2026 offered hands-on labs on analysing Excel files with AI.
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: none published
    provenance: vendor-published
    source_ref: TEI-TAXTECH-2026
  prerequisites:
  - Approved enterprise tools
  - Training for tax staff
  - Documentation standards and automation sustainment so workflows outlive their builders
  risks_and_guardrails:
  - A tool meant to save two hours consumed a day when the intended users had not been consulted; Alteryx workflows could not be explained after the builder left (TEI Tax Tech 2026).
  - Only two of more than 50 polled said tax owns AI implementation.
  human_checkpoints:
  - Documented logic and owner for each automation
  role_evolution: 'Tax professionals act as builders; a senior director said: ''You will not survive in this field if you don''t have a change mindset.'' (TEI recap)'
  evidence_grade: C
  sources:
  - ref: TEI-TAXTECH-2026
    title: '2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain (recap of the 27-29 Apr 2026 seminar)'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain
    date: '2026-05-04'
    access: full
    locator: Paragraphs on Google and Microsoft demonstrations, failed training and undocumented workflows
  - ref: TR-CORPAI-2026
    title: 'AI in corporate tax: 2026 key trends and use cases'
    publisher: Thomson Reuters Tax & Accounting
    type: vendor
    url: https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/
    date: '2026-07-01'
    access: full
    locator: Orbitax XatBot Autopilot description
  - ref: TEI-MIDYEAR-2026
    title: TEI Midyear Conference 2026 at-a-glance agenda, preliminary (Washington DC, 15-18 Mar 2026)
    publisher: Tax Executives Institute
    type: conference
    url: https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf
    date: 2026-03
    access: full
    locator: 'Tax Lab: Escaping Excel'
  last_reviewed: '2026-10-17'
  notes: One conference recap plus a vendor feature. No named department outcome.
- id: tax-compliance-corporate-16
  title: Continuous 'always-on' compliance monitoring replaces periodic batch preparation (idea)
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: model
  runtime_class: background-agent
  maturity: emerging
  problem: Compliance is prepared in periodic batches; issues surface at deadlines.
  solution: EY practitioners write that AI agents could analyse compliance metrics continuously, raising alerts or remediations before deadlines; Deloitte describes compliance shifting toward continuous or near real-time as tax authorities adopt AI.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: idea only; no deployment found
    provenance: vendor-published
    source_ref: BLAW-EY-2025
  prerequisites:
  - Near-real-time data from ERP and finance systems
  - Mature data governance
  risks_and_guardrails:
  - Deloitte notes a patchwork where some authorities are not ready for real-time interaction, creating hybrid compliance burdens.
  human_checkpoints:
  - Human review of alerts and remediations
  role_evolution: EY authors say tax professionals shift to judgment, exception management, model tuning and strategic insight.
  evidence_grade: D
  sources:
  - ref: BLAW-EY-2025
    title: AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way (by Daren R. Campbell and Randy Carpenter of EY)
    publisher: Bloomberg Law / Bloomberg Tax
    type: firm
    url: https://news.bloomberglaw.com/business-and-practice/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way
    date: '2025-11-21'
    access: full
    locator: 'Use-case list: continuous audit and ''always-on'' monitoring'
  - ref: DELOITTE-TTT-2026
    title: 'Riding the wave: A framework to plan for AI (Tax Transformation Trends AI report, part three)'
    publisher: Deloitte Global
    type: firm
    url: https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf
    date: 2026-07
    access: full
    locator: Scenario discussion on continuous or near real-time compliance
  last_reviewed: '2026-10-17'
  notes: Idea. Labelled D because it is discussed by practitioners (EY authors; Deloitte scenario) with no deployment found.

```

---

## 3. Module notes

### Processes and key steps, with work types

Steps follow the module description. The AI references show where a source describes AI at that step.

- **Data collection and tax-sensitising of ledger and trial-balance data** (`data-reporting`). AI: GL-to-tax mapping (EY-COMPL-2026); agentic import, validation and mapping (TR-CORPAI-2026).
- **Book-to-tax adjustments, depreciation and M-1/M-3 schedules** (`transaction-processing`). AI: Byron lists book-to-tax adjustments and depreciation schedules among its agents (BYRON-2026). Baxter's Corptax BOTS post Ms and E&P adjustments by rule (CSC-BAXTER-2026).
- **Federal corporate return and workpaper preparation** (`document-production`). AI: roll-forward of prior-year workpapers (BYRON-2026); myRSM Tax (RSM-MYRSM-2025).
- **International information returns (5471, 8858) and foreign tax credit forms** (`transaction-processing`, `data-reporting`). Baxter reports 200+ international reports printed in 2 hours versus 80 with rules-based bots (CSC-BAXTER-2026). No AI-specific case was found (see Gaps).
- **State apportionment and state income tax returns** (`transaction-processing`). Byron lists state apportionments among its agents (BYRON-2026). No other source describes AI in this step.
- **Credits and incentives, including R&D credit and Form 6765 Section G** (`data-reporting`, `document-production`). AI: Neo.Tax inside ONESOURCE (TR-NEOTAX-2025). NextEra reports clean-energy credit forms with 700,000+ data points loaded in minutes via an Alteryx pipeline and a Corptax import template, not AI (CSC-NEXTERA-2026).
- **Preparer and reviewer sign-off, analytics review** (`review-assurance`). AI: year-on-year comparison and anomaly flags (EY-COMPL-2026).
- **Return-to-provision true-up** (`data-reporting`). Belongs mainly to the provision module; Neo.Tax says real-time credit data can reduce return-to-provision adjustments (TR-CORPAI-2026).
- **Estimated payments, extensions and tax calendar** (`coordination-scheduling`). AI: Bloomberg Tax Compliance Tracker assistant (BTAX-TOOLS-2026).

### Common pain points

- **Under-resourcing and reactive work.** 58% of 288 corporate tax departments say they are under-resourced (51% the year before), and respondents report spending more than half their time on reactive work, mostly compliance (TR-CORPTAX-2025).
- **Manual data gathering and spreadsheets.** EY states that 63% of departments still gather ERP/GL data manually and 76% rely heavily on Excel; the page does not name the survey (EY-COMPL-2026).
- **Upgrade priority and budget.** In the 2026 survey of 170 tax leaders, fewer than half said their department received a budget increase last year, and a majority said upgrading tax technology is a relatively low priority at their company (TR-CORPTECH-2026).
- **Talent.** Bloomberg Tax (a vendor) says a survey it conducted found three out of four tax departments struggle to attract and retain staff (BTAX-LEVERAGE-2026).
- **New form and filing demands.** Form 6765 Section G, and the first GloBE Information Return on 30 Jun 2026, are cited as compressing the direct-tax calendar (TR-CORPAI-2026).
- **Data quality is the binding constraint.** Kognitos argues assembling and reconciling source data, not calculation, is the hard part (KOGNITOS-2026). Deloitte lists data quality concerns and talent gaps (DELOITTE-LU-2025).

### Metrics and benchmarks

All are survey or vendor figures; measures are as the source states.

- **GenAI use in corporate tax:** 67% of departments not using GenAI; 57% of departments implementing new technologies plan to include GenAI, 36% machine learning, 17% to explore agentic AI; 288 departments surveyed (TR-CORPTAX-2025).
- **Belief versus action:** 92% of corporate tax professionals think GenAI can be used in their work, 75% think it should be, 20% use it across the company; 20% of organisations measure ROI; 95% believe GenAI will become central within five years; 24% treat GenAI skills as nice to have in new hires and 2% require them (TR-TENSIONS-2025; sample not stated on the page).
- **Policies:** 17% have specific AI and data policies, 21% cover GenAI under general technology policies, 45% have none (TR-TENSIONS-2025).
- **Expectations of timing:** the 2026 survey of 170 tax leaders reports that respondents now expect AI to be central to their workflow within one to two years; 67% say technology investment enabled a shift to proactive work (TR-CORPTECH-2026).
- **German tax departments (KPMG, sample size not stated):** 71% use AI tools and 19% are preparing; 89% use company-wide standard tools and 29% specialised tax applications; 66% of AI users report noticeable time savings; hurdles are IT approvals (47%), data protection (41%) and lack of knowledge (41%) (KPMG-DE-2026).
- **Deloitte's Tax Transformation Trends figures (sample not stated on the page):** 21% prioritise AI for routine data tasks, 10% for tax planning, 8% for identifying risks and opportunities; 77% of tax leaders require 90% or higher accuracy before trusting AI with tax processes; barriers are budget (45%), limited AI expertise (36%), no clear AI strategy (33%), data security and privacy (30%), leadership support (28%) (DELOITTE-LU-2025).
- **Vendor outcome claims:** Neo.Tax figures in tax-compliance-corporate-07; Byron's 97% in tax-compliance-corporate-05.
- **Baselines from rules-based automation (vendor-published):** Baxter, 200+ international reports in 2 hours versus 80 (CSC-BAXTER-2026); NextEra, 800 hours to minutes on credit forms (CSC-NEXTERA-2026, headline of the case study; the text states 700,000+ data points).
- **Independent, adjacent:** frontier models calculated fewer than a third of federal personal income tax returns correctly on a simplified sample (COLUMN-TAXCALCBENCH-2025); a neuro-symbolic design is proposed as more reliable (JHU-TAXREASON-2025).
- **Not found:** error rates, override rates, parallel-run results or inspection findings for corporate return preparation with AI.

### Guardrails and regulatory points

- **Existing practitioner duties apply.** IRS OPR guidance says practitioners keep full responsibility for AI-assisted work, must verify facts, citations and calculations, must use secure, enterprise-approved AI for client data, and should reflect AI cost savings in billing (JOFA-OPR-2026).
- **Risk framework.** The AICPA-led Council on AI Risk in Tax (CART) builds on a 20-risk framework in four categories: information integrity, fairness and legitimacy, security and data, and institutional capacity (AICPA-CART-2026).
- **Form 6765 Section G timing is reported differently** by Thomson Reuters (final Feb 2025; mandatory for tax year 2026), Strike Tax (instructions final 5 Feb 2026) and the IRS page, which did not mention Section G when retrieved (TR-CORPAI-2026; STRIKETAX-2026; IRS-6765-2026). Verify with the instructions for the filing year.
- **Audit trail and write-back.** Deloitte says agentic corrections to source data will need to be stored back to the system of record to maintain an audit-ready posture (DELOITTE-TTT-2026).
- **Traceability.** PwC says its agents are trained to explain inputs, outputs and assumptions, and approved processes are locked (PWC-MEGNA-2025). Bloomberg Tax (vendor) lists restatement, IRS examination, SOX control failure and professional responsibility among the risks of unverified AI output (BTAX-CORPAI-2026).
- **Data protection.** KPMG Germany respondents cited IT approvals and data protection among the biggest hurdles (KPMG-DE-2026).

### Frontier signals (dated)

- **2025-03-24:** EY reported as planning up to 150 agents for 80,000 tax professionals within three months (BTAX-BIG4-2025).
- **2025-11-05:** Thomson Reuters launches ONESOURCE+, positioned as an AI-powered compliance network across tax, trade, legal and risk (TR-ONESOURCEPLUS-2025).
- **2025-11-25:** EY announces Tax Labs and Tax Agent Factory (EY-TAXLABS-2025).
- **2026-03-09:** Bloomberg Tax shows an AI Assistant in its Compliance Tracker at TEI Midyear (BTAX-TOOLS-2026).
- **2026-03-16:** TEI and Thomson Reuters report corporate tax leaders expect AI to be central to their workflow within one to two years (TR-CORPTECH-2026).
- **2026-05-04 (recap of the 27-29 Apr seminar):** TEI Tax Tech attendees say capability is no longer the question; governance, training failures and token costs are (TEI-TAXTECH-2026).
- **2026-05-20:** KPMG and Anthropic announce Digital Gateway with Claude, initially for tax clients and private equity (KPMG-ANTHROPIC-2026).
- **2026-05-27:** Byron launches agents for 1065, 1120 and 1120-S returns (BYRON-2026).
- **2026-07-01:** Thomson Reuters links Section G and the first GloBE Information Return to AI adoption in direct tax (TR-CORPAI-2026).
- **2026-07-20:** Sala argues AI will not shrink corporate tax teams much (TAXPROF-SALA-2026).
- **2026-09-23:** AICPA and former IRS commissioner launch CART (AICPA-CART-2026).

### Workforce and role effects

- **Reviewer role.** EY says staff will monitor AI and review initial outputs, possibly with fewer review levels (EY-COMPL-2026). PwC says one reviewer replaces a group huddle on novel items and agents learn from logged overrides (PWC-MEGNA-2025).
- **AI teams.** PwC reports over 3,200 AI champions, a workforce-transformation team embedded in tax, over 350,000 US training hours and about 80% of staff trained (PWC-MEGNA-2025). EY pairs Tax Labs with an Agent Factory operating model (EY-TAXLABS-2025). OpenAI's tax team is small (four members presented) and its listed role requires 10+ years of tax experience plus SQL and Python (TEI-TAXTECH-2026; OPENAI-JOB-2025). Panel titles at the Bloomberg Tax forum include a Global Tax Technology Leader (EisnerAmper), a Director of Tax Technology (Home Depot) and a Tax Knowledge Management Practice Leader (KPMG) (BTAX-FORUM-2026).
- **Ownership.** Two of more than 50 TEI attendees polled said tax owns AI implementation (TEI-TAXTECH-2026).
- **Skills.** Deloitte reports 45% of respondents name AI-related skills as their greatest need over one to two years, 94% believe AI skills will be essential within four to five years, and 53% are recruiting digitally native talent (DELOITTE-LU-2025). Thomson Reuters finds few departments make GenAI skills a hiring requirement (2%) (TR-TENSIONS-2025).
- **Headcount.** 58% of KPMG Germany respondents expect stable domestic tax headcount and 72% abroad (KPMG-DE-2026). Sala expects limited shrinkage (TAXPROF-SALA-2026).
- **Pricing.** Firms are exploring value-based fees; OPR cautions against billing time not spent (BTAX-PRICING-2026; JOFA-OPR-2026).

### Objections and concerns raised

- **Silent failure.** An attendee described an agent that admitted it could not open a file and had been telling the user what they wanted to hear; the recap says errors are increasingly polite, quiet and technical (TEI-TAXTECH-2026).
- **Accountability.** Sala argues AI cannot shoulder regulatory, ethical or financial consequences of culpability (TAXPROF-SALA-2026).
- **Judgment on credits.** Strike Tax says an AI questionnaire can produce a number but not a defensible R&D credit claim, and notes vendor liability is typically capped at fees (STRIKETAX-2026). Competing-vendor view.
- **Trust threshold.** 77% of tax leaders require 90% or higher accuracy (DELOITTE-LU-2025).
- **Cost.** Rising token costs could change the economics of automation (TEI-TAXTECH-2026).
- **Governance gap.** 45% have no relevant AI policy (TR-TENSIONS-2025).
- **Training that fails.** A tool meant to save two hours consumed a day because the users had not been consulted (TEI-TAXTECH-2026).

### Interview probes for an advisor

1. Walk me through how ledger data reaches your return software. Which steps are rules, which are a person, and which (if any) are an AI model? What do you check on AI-mapped accounts, and how do you record it?
2. Who owns AI in tax: tax, finance or IT? How do you document AI-assisted workpapers for your auditors and for an IRS examination?
3. What review layers apply to AI-prepared work? Do you record when reviewers override, and do you know the rate?
4. For R&D credits: where does project data come from today, what changes with Section G, and who signs off the business-component and four-part-test judgments?
5. Do your outsourced compliance providers use AI, and has that changed what you pay or what you expect to receive?

---

## 4. Routed to other modules

- **Tax notices and IRS correspondence** (EY authors list notice reading, summarising and draft responses as an emerging use case; TEI Midyear ran a lab on managing notices with AI): controversy (BLAW-EY-2025; TEI-MIDYEAR-2026).
- **Sales and use tax and VAT compliance:** ONESOURCE Sales and Use Tax AI (up to 65% less time on routine reporting; cycle from 30 to 11 days for large enterprises, company claims) and the EY sales-and-use lookback example: indirect-tax (TR-SUTAI-2026; TR-ONESOURCEPLUS-2025; EY-COMPL-2026).
- **1040 and individual return preparation:** Ready to Review and the CLH CPAs quote of about an hour saved per simple 1040: compliance (individual and small-business lens) (TR-COCOUNSEL-2025; TR-R2R-2025). TaxCalcBench belongs here as well (COLUMN-TAXCALCBENCH-2025).
- **GloBE Information Return and Pillar Two data:** Orbitax XatBot modes and the first GIR on 30 Jun 2026: international-pillar-two (TR-CORPAI-2026; KOGNITOS-2026).
- **ASC 740 provision automation:** Bloomberg Workpapers pushing to Provision; Neo.Tax and return-to-provision effects: provision (BTAX-ASC740-2026; TR-CORPAI-2026).
- **Transfer pricing Tax Skills in Orbitax:** transfer-pricing (TR-CORPAI-2026).
- **Complex planning opinions versus AI:** Sala's question whether tax AI could displace Big Four opinions on planning: research-advisory (TAXPROF-SALA-2026).
- **R&D credit for clients' own AI projects:** a planning topic for research-advisory (CPAPA-RD-2026).
- **Tax-authority AI and audit selection:** controversy (DELOITTE-TTT-2026; BTAX-FORUM-2026).
- **Practitioner AI governance (OPR, CART):** cross-cutting professional-responsibility module (JOFA-OPR-2026; AICPA-CART-2026).

---

## 5. Sources

All sources were opened and read (`access: full`). Refs reuse the landscape file's keys where the document is the same.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| TR-CORPAI-2026 | AI in corporate tax: 2026 key trends and use cases | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/ | 2026-07-01 |
| TR-CORPTAX-2025 | The GenAI paradox: Why most tax departments aren't using AI yet, and what early adopters are gaining (reports the 2025 State of the Corporate Tax Department survey) | Thomson Reuters Institute | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 |
| TR-TENSIONS-2025 | 5 GenAI tensions corporate tax departments should address (from the 2025 Generative AI in Professional Services Report) | Thomson Reuters Tax & Accounting | survey | https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address-tri/ | 2025-06-24 |
| TR-TECHREPORT-2025 | Corporate tax departments take the first steps towards a tech-enabled future, new report shows (2025 Corporate Tax Technology Report) | Thomson Reuters Institute with Tax Executives Institute | survey | https://www.thomsonreuters.com/en/institute/reports/corporate-tax-tech-report-2025 | 2025-01-29 |
| TR-CORPTECH-2026 | Corporate tax teams eager for AI, but frustrated by pace of change, new report shows (2026 Corporate Tax Department Technology Report) | Thomson Reuters Institute with Tax Executives Institute | survey | https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026 | 2026-03-16 |
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain (recap of the 27-29 Apr 2026 seminar) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 |
| SAVANT-2026 | Savant Showcases Audit-Ready Agentic AI at TEI Tax Tech 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 |
| PWC-MEGNA-2025 | How PwC's tax team is using agentic AI (interview with Dom Megna, PwC US AI Tax Leader) | CFO.com | firm | https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/ | 2025-06-06 |
| KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence (two KPMG quick surveys) | KPMG Germany | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-06 |
| CORPTAX-2026 | ACT and CSC Corptax webinar on AI and machine learning in tax (Corptax AI/ML roadmap) | CSC Corptax | vendor | https://go.corptax.com/act-ai-ml-tax | 2026-10 |
| CORPTAX-AIREADY-2026 | Corptax Professional Services AI Data Readiness package (info-sheet page) | CSC Corptax | vendor | https://go.corptax.com/ai-readiness-info-sheet.html | 2026-10 |
| KOGNITOS-2026 | AI for Corporate Tax and Provision Automation (2026) | Kognitos | vendor | https://www.kognitos.com/blog/ai-corporate-tax-provision-automation-2026/ | 2026-06-17 |
| TAXPROF-SALA-2026 | Sala: AI Won't Shrink Corporate Tax Teams Much. Here's Why. (abstract of 121 Tax Notes State 189, 20 Jul 2026) | TaxProf Blog (AALS) | press | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 |
| EY-TAXLABS-2025 | EY unveils suite of powerful AI capabilities to accelerate tax transformation and deliver strategic value | EY Global | firm | https://www.ey.com/en_gl/newsroom/2025/11/ey-unveils-suite-of-powerful-ai-capabilities-to-accelerate-tax-transformation-and-deliver-strategic-value | 2025-11-25 |
| KPMG-ANTHROPIC-2026 | KPMG Partners with Anthropic for Digital Gateway Powered by Claude | CPA Practice Advisor (reproducing the KPMG and Anthropic announcement) | firm | https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/ | 2026-05-20 |
| BTAX-FORUM-2026 | Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk (programme announcement for the 16 Jun 2026 forum) | Bloomberg Tax | conference | https://pro.bloombergtax.com/?p=17345 | 2026-06-10 |
| DELOITTE-TTT-2026 | Riding the wave: A framework to plan for AI (Tax Transformation Trends AI report, part three) | Deloitte Global | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf | 2026-07 |
| DELOITTE-LU-2025 | AI-enabled tax transformation | Deloitte Luxembourg | firm | https://www.deloitte.com/lu/en/services/tax/research/ai-enabled-tax-transformation.html | 2025-11-19 |
| TR-NEOTAX-2025 | How to eliminate the burden of R&D tax credit compliance (ONESOURCE and Neo.Tax) | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/neo-tax-onesource-eliminating-the-triple-burden-of-rd-credit-compliance/ | 2025-09-08 |
| TR-NEOTAXPAGE-2026 | ONESOURCE and Neo.Tax R&D tax credit calculation and claim (product page) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/corporation-solutions/c/neotax | 2026-10 |
| STRIKETAX-2026 | Form 6765 Section G becomes mandatory in 2026: most AI-only R&D credit tools will not be ready | Strike Tax Advisory | vendor | https://www.striketax.com/journal/form-6765-section-g-becomes-mandatory-in-2026-most-ai-only-r-d-credit-tools-will-not-be-ready | 2026-08 |
| CPAPA-RD-2026 | Spotting R&D Tax Credit Opportunities in Clients' Custom AI Projects | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/10/spotting-rd-tax-credit-opportunities-in-clients-custom-ai-projects/188227/ | 2026-08-10 |
| IRS-6765-2026 | About Form 6765, Credit for Increasing Research Activities | Internal Revenue Service | regulator | https://www.irs.gov/forms-pubs/about-form-6765 | 2026-06-20 |
| BTAX-CORPAI-2026 | AI for Corporate Tax: Verified Intelligence That Stands Up to Scrutiny | Bloomberg Tax | vendor | https://pro.bloombergtax.com/insights/artificial-intelligence/ai-for-corporate-tax-verified-intelligence-for-complex-calculations-and-compliance/ | 2026-05-18 |
| BTAX-LEVERAGE-2026 | How to Leverage AI for Corporate Tax Success in 2026 | Bloomberg Tax | vendor | https://pro.bloombergtax.com/insights/tax-automation/how-to-leverage-ai-for-corporate-tax-success-in-2026/ | 2026-03-18 |
| BTAX-TOOLS-2026 | Bloomberg Tax Showcases Industry-Leading AI-Powered Tools at TEI Midyear 2026 | Bloomberg Tax | vendor | https://pro.bloombergtax.com/insights/company-news/bloomberg-tax-showcases-industry-leading-ai-powered-tools-at-tei-midyear-2026 | 2026-03-09 |
| BTAX-ASC740-2026 | Accelerate your ASC 740 process (Bloomberg Tax Research, Provision and Workpapers product page) | Bloomberg Tax | vendor | https://pro.bloombergtax.com/products/accelerate-your-asc-740-process/ | 2026-03 |
| EY-COMPL-2026 | AI and the transformation of tax compliance (page title: Tax transformation: Adopting AI to drive efficiencies) | EY US | firm | https://www.ey.com/en_us/insights/tax-compliance/ai-and-the-transformation-of-tax-compliance | 2026-02-12 |
| BAKERTILLY-2026 | The new tax operating model: AI as a strategic partner | Baker Tilly US | firm | https://www.bakertilly.com/insights/the-new-tax-operating-model-ai-as-a-strategic-partner | 2026-02-20 |
| BLAW-EY-2025 | AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way (by Daren R. Campbell and Randy Carpenter of EY) | Bloomberg Law / Bloomberg Tax | firm | https://news.bloomberglaw.com/business-and-practice/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way | 2025-11-21 |
| CSC-BAXTER-2026 | Baxter International case study (Corptax BOTS; rules-based automation, not AI) | CSC Corptax | vendor | https://cscglobal.com/service/corptax/case-studies/baxter/ | 2026-10 |
| CSC-NEXTERA-2026 | From 800 Hours to Minutes: NextEra Collaborates with Corptax to Power through New Credit Rules (rules-based import automation, not AI) | CSC Corptax | vendor | https://cscglobal.com/service/corptax/case-studies/nextera/ | 2026-10 |
| CSC-SALESFORCE-2026 | Fragmentation to Integration: Salesforce Files Six Weeks Sooner (Corptax data blueprint and automation, not AI) | CSC Corptax | vendor | https://cscglobal.com/service/corptax/case-studies/salesforce/ | 2026-10 |
| OPENAI-JOB-2025 | Senior Manager, Tax Data Automation (job listing, OpenAI tax team) | OpenAI, via Khosla Ventures job board | job-posting | https://jobs.khoslaventures.com/companies/openai/jobs/45083210-senior-manager-tax-data-automation | 2025-01-22 |
| TEI-MIDYEAR-2026 | TEI Midyear Conference 2026 at-a-glance agenda, preliminary (Washington DC, 15-18 Mar 2026) | Tax Executives Institute | conference | https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf | 2026-03 |
| BYRON-2026 | Byron Launches with AI Agents for Business Tax Preparation Workflows | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/05/27/byron-launches-with-ai-agents-for-business-tax-preparation-workflows/184034/ | 2026-05-27 |
| BTAX-BIG4-2025 | Big Four Firms Roll Out AI That Can Handle Routine Tasks Solo | Bloomberg Tax | press | https://news.bloombergtax.com/financial-accounting/big-four-firms-roll-out-ai-that-can-handle-routine-tasks-solo | 2025-03-24 |
| RSM-MYRSM-2025 | RSM expands AI commitment with launch of myRSM Tax | RSM US | firm | https://rsmus.com/newsroom/2025/rsm-expands-ai-commitment-with-launch-of-myrsm-tax.html | 2025-06-16 |
| BTAX-PRICING-2026 | AI Efficiency Gains Push Accounting Firms to Reimagine Pricing | Bloomberg Tax | press | https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing | 2026-03-05 |
| JOFA-OPR-2026 | IRS outlines AI risks, Circular 230 duties for tax practitioners | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/jun/irs-outlines-ai-risks-circular-230-duties-for-tax-practitioners/ | 2026-06-26 |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 |
| TR-R2R-2025 | AI tax return preparation: how Ready to Review transforms the workflow | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/ai-tax-return-preparation-how-ready-to-review-transforms-the-workflow/ | 2025-12-19 |
| TR-COCOUNSEL-2025 | Thomson Reuters launches agentic AI solutions to transform tax, audit and accounting workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows | 2025-11-05 |
| TR-ONESOURCEPLUS-2025 | Thomson Reuters launches ONESOURCE+, the AI-powered intelligent compliance network | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-onesource-plus-the-ai-powered-intelligent-compliance-network | 2025-11-05 |
| TR-SUTAI-2026 | Thomson Reuters launches AI tax compliance solution that saves time and reduces risk (ONESOURCE Sales and Use Tax AI) | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk | 2026-01-15 |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task | arXiv (Bock and three co-authors; Column Tax) | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 |
| JHU-TAXREASON-2025 | Language Models and Logic Programs for Trustworthy Tax Reasoning | arXiv (Jurayj and two co-authors) | academic | https://arxiv.org/abs/2508.21051 | 2025-08-28 |

Type counts: vendor 19, firm 9, press 6, survey 5, conference 3, academic 2, regulator 1, job-posting 1, professional-body 1. No `podcast`, `community` or `standard-setter` sources were used. Sources with date `2026-10` carry no publication date; the date is the retrieval month.

---

## 6. Gaps

- **Web search budget.** Sixteen searches were used; the seventeenth (a check for practitioner coverage of Form 6765 Section G and AI tools) was refused because the shared budget was spent.
- **No measured outcomes.** No named in-house corporate tax department published error rates, override rates, parallel-run results, review-time or fee data for AI in return preparation, workpaper review, state apportionment or credits. Oxford Industries, Home Depot, Amazon and Walmart appear only as named participants.
- **Search-only material, not used for outcomes or grades:** Neo.Tax customer list (Mercury, Notion and others, via a case-study directory); Unstract and Instafill claims on Form 5471 extraction; ONESOURCE help pages on automated Form 5471 preparation; a Chatfin summary citing a Vertex benchmark on nexus monitoring time (47 days to under 8 hours); a StealthAgents page with unsourced provision-cycle figures; Alteryx's Global Tax Management customer story (50% fewer manual compliance processes; blocked when fetched); a Concentrix telecom tax-return workflow case study. Savant's marketing percentages (50-70% productivity gain, >98% accuracy) were not opened on the vendor's site.
- **Form 5471/8858 and international forms:** no AI-specific deployment found; only rules-based Corptax automation and vendor extraction claims.
- **State apportionment and SALT income tax:** only Byron's agent description (BYRON-2026). No state-specific case, error rate or state conformity evidence found.
- **Estimated payments and extensions for corporates:** no source describes AI doing this.
- **Wolters Kluwer CCH, Longview and Vertex corporate income tax AI:** no customer stories surfaced; the landscape reports Wolters Kluwer pages behind a bot wall.
- **Job postings:** one in-house posting found (OpenAI, Jan 2025, closed). No 2026 postings for corporate tax technology or AI roles were reached.
- **Closed communities:** TEI chapters, Tax Labs and member sessions are not public; r/taxpros and TaxProTalk were not reached. TEI Annual Conference 2026 (starts 17-18 Oct) has no recaps yet.
- **Dates unresolved:** the Corptax webinar and info-sheet pages, Neo.Tax product page and CSC case-study pages carry no publication date (retrieval month used). Strike Tax's page carries conflicting date metadata (Aug 2026 used). The TEI Tax Tech recap date (2026-05-04) is taken from a date in the page text. The EY compliance article is dated 2026-02-12 by page metadata but cites a January 2024 survey, so it may be a republished older piece.
- **Unverified items from the landscape not used:** EY-NVIDIA '3 million compliance tasks' target; Basis '30% of top 25 firms'; Black Ore customer shares; Deloitte 'Pillar Two Agent'.
- **Sample sizes** are not stated on the pages for the Deloitte, KPMG Germany and Thomson Reuters generative AI report figures quoted.
