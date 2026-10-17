# Tax controversy: governance and evidence (wave 2)

- **Archetype:** tax. **Module:** controversy (audits, notices, appeals and disputes, plus tax-authority AI). **Angle:** governance and evidence.
- **Prepared:** 2026-10-17. Sources were read with `curl`, `pdftotext` and the `r.jina.ai` mirror (five web searches were used). Each source below is marked `access: full` (opened and read) unless stated.

## 1. Summary

- **What the evidence shows.** Almost all published measurement in this module concerns tax authorities, not practitioners. Independent oversight reports exist for the IRS (GAO, TIGTA, the National Taxpayer Advocate) and for the ATO (the ANAO audit). They are more informative than any vendor or firm claim. For practitioner-side controversy work (notice response, audit defence, appeals drafting) there is no published error rate, override rate or parallel-run result in the sources found. The practitioner-side use cases are therefore mostly grade D.
- **Quality evidence that does exist.**
  - IRS voicebots: the National Taxpayer Advocate reports that in filing season 2026 the IRS counted 17% of voicebot volume as completed in the bot, with about 46% of callers transferred to a live assistor and about 14% disconnected (tax-controversy-04).
  - ATO: the ANAO found 74% of AI models in production had no completed data ethics assessment, and no evidence of ongoing performance monitoring for the 14 models deployed between 1 July 2023 and 14 May 2024 (tax-controversy-11).
  - IRS audit selection: TIGTA found the IRS has no process to evaluate whether AI selection beats earlier methods, and a pilot selection model raised both assessments per exam hour and the no-change rate (tax-controversy-01).
  - TIGTA's September 2026 report (read only through press coverage) found 4 of 5 sampled high-impact AI use cases lacked testing documentation (tax-controversy-02).
- **Constraints on practitioners converge on "existing duties apply".** IRS OPR Alert 2026-19 (24 June 2026), the Australian TPB Guidance Statement 55/2026 (22 July 2026) and the UK PCRT AI guidance (19 January 2026) all apply existing conduct rules to AI. The Tax Court's Clinco opinion (T.C. Memo. 2026-16) shows what failure looks like: three of four cited cases did not exist. The Tax Court has not adopted an AI rule, and the judge doubted that a blanket AI certification would make sense.
- **Open conflicts.** The OPR fee language (do not bill for time not spent; pass savings on) is contested by the AICPA, which asked the IRS for clarification and says the text does not appear to allow value pricing. Authority transparency is contested too: a UK tribunal rejected HMRC's refusal to confirm or deny whether it uses large language models on R&D compliance work.
- **Use cases:** 19 candidates (6 grade A, 4 grade B, 2 grade C, 7 grade D). Twelve describe AI used by tax authorities (the landscape recommended scoping tax-authority AI into this module), two are governance controls over authority models (02, 03), one is authority-oriented research (18), and four are practitioner-side or practitioner-governance ideas (14 to 17).

## 2. Use cases

```yaml
- id: tax-controversy-01
  title: Machine-learning return classification and selection for examination (authority side)
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Tax authorities with too few examiners must decide which returns and which issues to examine. The IRS's older scoring approach depended on past examination studies, and examination no-change rates (the share of audits that end with no adjustment) are high, especially for partnerships and corporations. That burdens compliant taxpayers and wastes examiner time."
  solution: "The IRS runs statistical and machine-learning models on current return data, trained without relying on historical exam results. The LB&I Line Anomaly Recommender scores Form 1120 returns of mid-size corporations, with human classifiers reviewing output. The SB/SE Form 1040 classification model recommends the top three issues per return, and examiners and managers can add or remove issues. A Form 1040 return-selection model was still in pilot, and a Large Partnership Compliance model feeds partnership selection. For a taxpayer or representative, this changes how exposure arises: the first contact is a model-driven selection that is not disclosed."
  outcomes:
    - lever: quality
      description: "TIGTA reports that pilot tests of the Form 1040 return-selection model found a higher dollar assessment per examination hour but also higher no-change rates, and that management had made no deployment decision. TIGTA also reports that the IRS has not set up processes to evaluate whether the AI models perform better than prior methods, and LB&I had no specific examination-result data for the Line Anomaly Recommender."
      figure: "none published (figures redacted in the public report)"
      measures: "Pilot comparison of the Form 1040 selection model: dollar assessment per examination hour and no-change rate, as described qualitatively by TIGTA"
      provenance: independent
      source_ref: TIGTA-2025
  prerequisites:
    - "Large structured return datasets and a research function (the IRS's RAAS group) to build and maintain models"
    - "Contractor support: TIGTA reports $3.9 million on two contracts for the Line Anomaly Recommender (Sept 2018 to Sept 2021) and $7.9 million on two contracts for the Form 1040 classification model (July 2019 to Sept 2024)"
    - "Human classifiers and examiners to review model output"
  risks_and_guardrails:
    - "Models trained on current return data do not learn from exam outcomes, so they may miss new noncompliance and cannot be tuned on exam productivity (TIGTA-2025)"
    - "No performance-evaluation process comparing AI selection with prior methods; TIGTA recommended a measurement plan and the IRS agreed, subject to staffing and expected Treasury AI governance guidance (TIGTA-2025)"
    - "GAO reports the IRS may lack audit-outcome data to retrain models if fewer audits are conducted after staff reductions (GAO-2026)"
  human_checkpoints:
    - "Human classifiers review Line Anomaly Recommender output before returns are made available to the field (TIGTA-2025)"
    - "Examiner and manager can add or remove the issues the Form 1040 classification model suggests (TIGTA-2025)"
  role_evolution: "Examiners and classifiers shift from choosing cases by scoring formulas to reviewing model-suggested returns and issues and overriding them (TIGTA-2025). Representatives should expect that selection reasons are not visible to them, which GAO flagged for audit-selection documentation generally (GAO-TAXGAP-2024)."
  evidence_grade: B
  sources:
    - { ref: TIGTA-2025, title: "The IRS Could Leverage Examination Results in Artificial Intelligence Examination Case Selection Models and Improve Processes to Evaluate Performance (2025-308-022)", publisher: "Treasury Inspector General for Tax Administration", type: regulator, url: "https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf", date: "2025-05-19", access: full, locator: "Highlights; pp. 5-8 (models, LAR human review, Form 1040 pilot result); p. 14 (Recommendation 3, performance evaluation)" }
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: "U.S. Government Accountability Office", type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: "2026-03-24", access: full, locator: "p. 26 (audit-outcome data after staffing reductions)" }
    - { ref: GAO-TAXGAP-2024, title: "Tax Gap: IRS Should Take Steps to Ensure Continued Improvement in Estimates (GAO-24-106449)", publisher: "U.S. Government Accountability Office", type: regulator, url: "https://www.gao.gov/products/gao-24-106449", date: "2024-05-06", access: full, locator: "Fast Facts and What GAO Found (documentation of the AI sample-selection pilot)" }
  last_reviewed: "2026-10-17"
  notes: "The TIGTA text is partly redacted, so no effect sizes are available. The no-change rate is the IRS's own effectiveness metric, and GAO notes it counts default audits (taxpayer non-response) as changes (GAO-EQUITY-2024). The TIGTA review covers the SB/SE and LB&I models only, not every IRS selection tool."

- id: tax-controversy-02
  title: Feedback loop and performance monitoring for AI audit-selection models
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "The IRS selects returns with models that are trained on current return data, but exam results are not routinely fed back to tune the models, and the IRS cannot readily show whether the AI models beat the earlier methods. With fewer audits, there is also less outcome data to retrain on."
  solution: "Compare model-suggested issues with issues examiners actually pursued, review closed-case adjustment data (the exam change report data held on closed cases) for productivity by issue, track no-change rates and model drift, and use a governance process to refine models. This is the control TIGTA recommended, not a deployed use of AI."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "TIGTA recommended a measurement plan with metrics to monitor AI models and correct drift; the IRS agreed with all three recommendations, two subject to staffing constraints and expected Treasury AI governance guidance"
      provenance: independent
      source_ref: TIGTA-2025
  prerequisites:
    - "Closed-case exam data linked back to the model's suggested issues"
    - "Staff to run the governance process (IRS agreed to two recommendations subject to staffing constraints)"
    - "Enough ongoing audits to generate outcome data (GAO-2026)"
  risks_and_guardrails:
    - "Feedback from exam outcomes can entrench past enforcement patterns; GAO found the IRS's refundable-credit selection reviews did not consider unintended bias in data and assumptions (GAO-EQUITY-2024)"
    - "TIGTA's 2026 sample found documentation gaps for high-impact AI: 4 of 5 sampled use cases lacked testing documentation (ACCTODAY-TIGTA-2026)"
  human_checkpoints:
    - "Governance process in which division leaders review exam performance results as part of model refinement (TIGTA-2025, Recommendation 1)"
  role_evolution: "Data scientists and examination leaders would share ownership of model quality, with exam outcomes as the evaluation signal (TIGTA-2025)."
  evidence_grade: D
  sources:
    - { ref: TIGTA-2025, title: "The IRS Could Leverage Examination Results in Artificial Intelligence Examination Case Selection Models and Improve Processes to Evaluate Performance (2025-308-022)", publisher: "Treasury Inspector General for Tax Administration", type: regulator, url: "https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf", date: "2025-05-19", access: full, locator: "Highlights; pp. 9-14 (Recommendations 1-3 and management responses)" }
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: "U.S. Government Accountability Office", type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: "2026-03-24", access: full, locator: "p. 26 (fewer audits means less outcome data for training)" }
    - { ref: GAO-EQUITY-2024, title: "Tax Enforcement: IRS Audit Selection Processes for Returns Claiming Refundable Credits Could Better Address Equity (GAO-24-106126)", publisher: "U.S. Government Accountability Office", type: regulator, url: "https://www.gao.gov/products/gao-24-106126", date: "2024-04-25", access: full, locator: "Fast Facts; What GAO Found" }
    - { ref: ACCTODAY-TIGTA-2026, title: "IRS's AI risk management needs to be improved", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/irs-ai-risk-management-needs-to-be-improved", date: "2026-09-28", access: full, locator: "paragraphs 4-8 (TIGTA sample of five high-impact use cases)" }
  last_reviewed: "2026-10-17"
  notes: "Idea. Graded D because it is a recommended control with no published implementation. The TIGTA 2026 report (2026208059fr.pdf) returned 403 from tigta.gov and the mirror, so the figures come from the Accounting Today article."

- id: tax-controversy-03
  title: Disparity and fairness testing of AI audit-selection models
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: "Race-blind audit selection can still produce disparate audit rates. Independent researchers estimated that Black taxpayers were audited at 2.9 to 4.7 times the rate of non-Black taxpayers, driven mainly by EITC claimants. GAO found the IRS's refundable-credit selection reviews did not consider demographic equity in the data and assumptions behind the system."
  solution: "Test selection models and their performance targets (such as minimizing the no-change rate) against demographic and other group outcomes before and after deployment, using partial-identification or third-party data where the authority does not hold the variables. This pattern is described by researchers, GAO and Werfel's risk register, not shown as a deployed control."
  outcomes:
    - lever: risk
      description: "none published for the testing control itself. The disparity estimate below measures the audit process, not a fairness test."
      figure: "2.9 to 4.7 times"
      measures: "Audit rate of Black taxpayers relative to non-Black taxpayers, estimated by partial identification because neither the IRS nor the authors observe race (working paper, January 2023)"
      provenance: independent
      source_ref: SIEPR-AUDIT-2023
  prerequisites:
    - "Demographic or proxy data to test against; Werfel notes tax data systems may not collect the needed variables"
    - "Willingness to change selection objectives, since the study finds that minimizing the no-change rate and targeting erroneously claimed refundable credits raise the audit rate of Black taxpayers"
  risks_and_guardrails:
    - "Performance and fairness trade off in model design (SIEPR-AUDIT-2023)"
    - "Disclosure of model details to improve transparency can raise the risk of adversarial manipulation (AICPA-WERFELART-2026)"
  human_checkpoints:
    - "Werfel's register calls for human review of high-impact audit-selection decisions and periodic bias audits with documented findings (AICPA-WERFEL-2026, risk 7)"
  role_evolution: "Model owners and oversight bodies would add disparity metrics to the model's performance indicators; the register also lists workforce expertise erosion as a risk to the ability to do this (AICPA-WERFEL-2026, risks 7 and 15)."
  evidence_grade: D
  sources:
    - { ref: SIEPR-AUDIT-2023, title: "Measuring and Mitigating Racial Disparities in Tax Audits", publisher: "Stanford Institute for Economic Policy Research (Elzayn, Smith, Hertz, Ramesh, Fisher, Ho, Goldin)", type: academic, url: "https://siepr.stanford.edu/publications/working-paper/measuring-and-mitigating-racial-disparities-tax-audits", date: "2023-01", access: full, locator: "Abstract" }
    - { ref: GAO-EQUITY-2024, title: "Tax Enforcement: IRS Audit Selection Processes for Returns Claiming Refundable Credits Could Better Address Equity (GAO-24-106126)", publisher: "U.S. Government Accountability Office", type: regulator, url: "https://www.gao.gov/products/gao-24-106126", date: "2024-04-25", access: full, locator: "Fast Facts; What GAO Found (Dependent Database program, no-change rate)" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendix A: AI Risk Register for Tax Authorities", publisher: "AICPA (Danny Werfel)", type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: "2026-06", access: full, locator: "Appendix A, risk 7 (Audit Targeting), pp. 5-6" }
    - { ref: AICPA-WERFELART-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: "The Tax Adviser (AICPA)", type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: "2026-08-31", access: full, locator: "section 'AI risk register for tax authorities'" }
  last_reviewed: "2026-10-17"
  notes: "Pattern 'other': model audit and disparity testing of a scoring system. Idea, graded D. The disparity estimate is about IRS audits in general and predates the 2025 AI expansion; it is a measurement of an adjacent process. The SIEPR date is the page's 'January, 2023' publication field. The Werfel appendices PDF is dated 2026-06 from its upload path; the PDF metadata creation date is May 2026."

- id: tax-controversy-04
  title: Voicebots and chatbots answering taxpayer calls and questions (tax authority)
  archetype: tax
  module: controversy
  function: customer-service
  work_types: [client-interaction]
  pattern: service-agent-escalation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Phone demand at the IRS far exceeds live-assistor capacity, and notice-related or balance-due calls from taxpayers and practitioners wait a long time."
  solution: "The IRS answers a share of calls with voicebots (11 voicebots and two chatbots listed in its June 2025 inventory) and routes callers to live assistors when the bot cannot complete the request. Callbacks are offered when expected waits are long."
  outcomes:
    - lever: experience
      description: "In filing season 2026 (through April 18), the IRS considered only 17% of voicebot volume as completed by the voicebot; about 46% of callers transferred to a live assistor and about 14% disconnected, according to the National Taxpayer Advocate, using IRS data. On the enterprise lines CSR level of service fell from 70% to 56% and time on hold rose from 8 to 14 minutes."
      figure: "17% completed by voicebot; about 46% transferred; about 14% disconnected"
      measures: "Share of voicebot call volume completed in the voicebot, transferred to a live assistor, or disconnected, enterprise phone lines, filing season 2026 through April 18, 2026 (NTA, from IRS Voice Bot Report)"
      provenance: independent
      source_ref: NTA-OBJ-2026
    - lever: capacity
      description: "IRS reported over 5 million sessions with its taxpayer-service bots in the 2024 filing season and nearly 25 million in the 2025 filing season."
      figure: "over 5 million; nearly 25 million sessions"
      measures: "Sessions with IRS voicebots and chatbots in the 2024 and 2025 filing seasons, as reported by the IRS to GAO"
      provenance: self-reported
      source_ref: GAO-2026
  prerequisites:
    - "Authenticated and unauthenticated call flows, transfer paths to live assistors, and callback capacity"
    - "Voicebot data reporting by phone line (NTA notes it was unavailable for some lines)"
  risks_and_guardrails:
    - "Wrong answers can create reliance claims; Werfel's register lists hallucination, drift, over-trust and estoppel-type claims for authority chatbots (AICPA-WERFEL-2026, risks 1-5)"
    - "NTA says voicebot technology could help only if it accurately addresses the issues taxpayers need handled, and that the high transfer rate shows more work is needed (NTA-OBJ-2026)"
  human_checkpoints:
    - "Transfer to a live assistor; the IRS offered callbacks and connected over 85% of callers who elected the callback service to an assistor in filing season 2026 (NTA-OBJ-2026)"
  role_evolution: "Assistors receive fewer, harder calls. Calls answered by assistors on enterprise lines fell 20% (from 12.4 million to 9.9 million) while voicebot volume rose 4% (NTA-OBJ-2026)."
  evidence_grade: A
  sources:
    - { ref: NTA-OBJ-2026, title: "National Taxpayer Advocate Fiscal Year 2027 Objectives Report to Congress, Review of the 2026 Filing Season", publisher: "Taxpayer Advocate Service (IRS)", type: regulator, url: "https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/06/JRC27_FullReport.pdf", date: "2026-06", access: full, locator: "Review of the 2026 Filing Season, Figure 2.7 and the paragraph that follows it" }
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: "U.S. Government Accountability Office", type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: "2026-03-24", access: full, locator: "p. 20 (taxpayer services use cases)" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendix A: AI Risk Register for Tax Authorities", publisher: "AICPA (Danny Werfel)", type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: "2026-06", access: full, locator: "Appendix A, risks 1-5, pp. 1-4" }
  last_reviewed: "2026-10-17"
  notes: "Voicebot and CSR metrics cover the IRS enterprise phone lines only through April 18 each year. The NTA report does not say the rise in hold time was caused by voicebots; staffing also changed. The NTA report states its text was partly developed with AI assistance and reviewed by staff."

- id: tax-controversy-05
  title: AI and automation to speed amended-return processing (tax authority)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [transaction-processing]
  pattern: document-to-decision
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Amended returns and refund claims wait weeks or months in the IRS, and backlog of this kind pushes taxpayers into correspondence, follow-up calls and disputes. The IRS receives about 5 million amended returns each year."
  solution: "The IRS says it uses AI and automation to speed processing of amended returns, so far for hundreds of thousands of them."
  outcomes:
    - lever: speed
      description: "The IRS CIO told employees that an amended individual return could take 12, 14 or 16 weeks on average before, and that AI and automation brought that to under three days for the returns affected."
      figure: "from 12 to 16 weeks to under three days"
      measures: "Average processing time for amended returns, before and after AI and automation, as stated by the IRS CIO at an all-staff meeting; applied to 'hundreds of thousands' of about 5 million amended returns a year; no methodology published"
      provenance: self-reported
      source_ref: IRS-AIFIRST-2026
  prerequisites:
    - "Digitized amended-return data; the IRS also put about 1,500 IT and HR employees on involuntary details to frontline taxpayer service in February 2026, with duties that included reducing the amended-return backlog (IRS-AIFIRST-2026)"
  risks_and_guardrails:
    - "Unpublished methodology: it is unclear which returns were included and whether the under-three-day figure covers the complex cases"
    - "GAO identifies automated decisions without human review in other IRS fraud use cases (GAO-2026); a comparable check for this use case is not reported"
  human_checkpoints:
    - "Not described in the source"
  role_evolution: "The IRS says AI will not eliminate jobs and aims to make each employee more productive; headcount started and ends 2026 at about 74,000 (IRS-AIFIRST-2026)."
  evidence_grade: A
  sources:
    - { ref: IRS-AIFIRST-2026, title: "Tax chief pushes 'AI-first IRS' to get more out of agency's workforce", publisher: "Nextgov/FCW (Jory Heckman)", type: press, url: "https://www.nextgov.com/artificial-intelligence/2026/10/tax-chief-pushes-ai-first-irs-get-more-out-agencys-workforce/416389/", date: "2026-10-02", access: full, locator: "paragraphs on CIO Kaschit Pandya's remarks (amended returns) and CHCO Kweskin (headcount)" }
  last_reviewed: "2026-10-17"
  notes: "The all-staff meeting was Wednesday 30 September 2026. Figures come from a transcript and audio obtained by Government Executive, as reported by Nextgov. Treat the speed figure as a spoken, unaudited claim. The IRS CEO's aim of a mid-90s compliance rate in five years (from about 85%) is a stated vision, not a result."

- id: tax-controversy-06
  title: AI fraud and identity-theft screening that holds refunds, with human release (tax authority)
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance, transaction-processing]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Refund fraud and identity theft at scale cannot be screened manually. A held refund, though, creates a taxpayer problem that often ends in calls, identity-verification steps and correspondence."
  solution: "IRS models score returns for fraud or noncompliance risk. In most compliance and fraud use cases the AI gives a risk score or recommendation and an IRS official reviews it. GAO found two fraud use cases that automate a decision without human review: one decides relief for taxpayers whose accounts were flagged for identity-theft risk, and one pauses refund issuance when a return looks like identity theft, after which an employee reviews the risk factors and decides whether to release the refund. A separate IRS tool compares the output of several machine-learning models against a confidence threshold to flag possible fraud for human review (FedScoop)."
  outcomes:
    - lever: risk
      description: "GAO counted the use cases rather than measuring detection accuracy: 18 of 43 IRS tax-compliance and fraud-focused AI use cases were operational as of June 2025."
      figure: "18 of 43"
      measures: "IRS AI use cases in the tax compliance and fraud detection category that were operational (not in development) as of June 2025, from the IRS internal inventory"
      provenance: independent
      source_ref: GAO-2026
    - lever: experience
      description: "The Taxpayer Protection Program line, which handles identity-theft verification, received nearly 2.4 million calls in filing season 2026 (through April 18); 19% were answered by an assistor and hold time was 20 minutes, per the National Taxpayer Advocate."
      figure: "19% of calls answered by a CSR; 20 minutes on hold"
      measures: "Calls answered by a customer service representative divided by calls received on the TPP line, filing season 2026 through April 18; the report does not isolate the effect of AI screening"
      provenance: independent
      source_ref: NTA-OBJ-2026
  prerequisites:
    - "Identity-verification process and phone capacity for taxpayers whose refunds are paused"
    - "Inventory and governance record for the use case; GAO found IRS inventory omissions, including contracted tools used to help build criminal cases"
  risks_and_guardrails:
    - "Two use cases act without a human decision; GAO says in the IRS case that an employee reviews after a refund is paused (GAO-2026)"
    - "Over 25% of inventory entries did not describe the expected benefit, and some tools were missing from the inventory (GAO-2026)"
    - "Werfel's register lists adversarial manipulation of detection models, agentic irreversible action and control dilution as risks (AICPA-WERFEL-2026, risks 13, 14, 17)"
  human_checkpoints:
    - "An IRS official reviews AI risk scores and recommendations before audits or investigations proceed in most use cases (GAO-2026, p. 19)"
    - "Employee reviews identity-theft risk factors and decides whether a paused refund should be issued (GAO-2026, p. 19)"
  role_evolution: "Reviewers move from finding suspect returns to handling model flags and the taxpayer verification work that follows."
  evidence_grade: B
  sources:
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: "U.S. Government Accountability Office", type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: "2026-03-24", access: full, locator: "pp. 19-20 (Tax compliance and fraud detection); Highlights (inventory quality)" }
    - { ref: TREAS-AIINV-2026, title: "IRS ramps up AI use amid staff cuts, Treasury inventory shows", publisher: "FedScoop", type: press, url: "https://fedscoop.com/treasury-irs-ai-use-case-inventory/", date: "2026-01-29", access: full, locator: "paragraphs on deployed tools (confidence threshold fraud tool, synthetic data engine)" }
    - { ref: NTA-OBJ-2026, title: "National Taxpayer Advocate Fiscal Year 2027 Objectives Report to Congress, Review of the 2026 Filing Season", publisher: "Taxpayer Advocate Service (IRS)", type: regulator, url: "https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/06/JRC27_FullReport.pdf", date: "2026-06", access: full, locator: "Figure 2.8 and the paragraph that follows it" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendix A: AI Risk Register for Tax Authorities", publisher: "AICPA (Danny Werfel)", type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: "2026-06", access: full, locator: "Appendix A, risks 13, 14 and 17" }
  last_reviewed: "2026-10-17"
  notes: "No published error, false-positive or release-time rates for IRS fraud models were found. The TPP-line figures are context, not evidence of AI performance. FedScoop reports the IRS list shows no 'collections' or 'enforcement' use cases in its public inventory, although a 2024 inventory listed a collections chatbot."

- id: tax-controversy-07
  title: AI case search and summaries for IRS Chief Counsel, Appeals and Taxpayer Advocate staff
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [research-synthesis, document-production]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Appeals, Chief Counsel and the Taxpayer Advocate Service handle document-heavy disputes with reduced staff. Appeals lost 29% of its workforce in 2025 according to a law-firm commentary, and practitioners report growing case backlogs."
  solution: "According to a practitioner article, the IRS rolled out an AI program (named Agentforce in that article) across the Office of Chief Counsel, the Taxpayer Advocate Service and the Office of Appeals in late 2025, to search documents and provide case summaries so staff can spend more time on taxpayer interaction. Search-only coverage adds that the agents cannot make final decisions or disburse funds."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "No usage or outcome figures were found in any source"
      provenance: self-reported
      source_ref: EISNER-IRSAI-2026
  prerequisites:
    - "Access to case files and document repositories; a vendor platform"
  risks_and_guardrails:
    - "No public statement was found on how case summaries are checked, logged or disclosed to taxpayers and representatives. Werfel's register flags explainability and lack of auditability as risks for appeals of AI-assisted determinations (AICPA-WERFEL-2026, risks 3 and 18)."
    - "The practitioner commentary on Appeals (staffing, independence, underdeveloped cases) does not mention AI; do not read it as evidence about this tool (CPAPA-APPEALS-2026)"
  human_checkpoints:
    - "Not described in the sources opened. Search-only coverage says agents cannot make final decisions."
  role_evolution: "Staff are expected to spend less time on document search and more on direct taxpayer interaction, per the EisnerAmper article. No staffing-effect evidence."
  evidence_grade: C
  sources:
    - { ref: EISNER-IRSAI-2026, title: "AI at the IRS: Transforming Tax Enforcement and the Future of Taxpayer Services", publisher: "EisnerAmper (Kristen De Noia)", type: firm, url: "https://eisneramper.com/insights/tax/ai-irs-transforming-0126", date: "2026-01-27", access: full, locator: "section 'AI in Taxpayer Services'" }
    - { ref: CPAPA-APPEALS-2026, title: "A Matter of Balance: IRS Appeals Processes, Staffing Create Growing Concerns for Practitioners, Taxpayers", publisher: "CPA Practice Advisor (Frost Law authors)", type: press, url: "https://www.cpapracticeadvisor.com/2026/07/21/a-matter-of-balance-irs-appeals-processes-staffing-create-growing-concerns-for-practitioners-taxpayers/187095/", date: "2026-07-21", access: full, locator: "paragraphs on staffing and case backlog" }
  last_reviewed: "2026-10-17"
  notes: "Single secondary source. The Axios exclusive of 2025-11-21 (https://www.axios.com/2025/11/21/irs-deploys-ai-agents), listed in the landscape as search-only, was not opened; the 'cannot make final decisions' statement comes from that search coverage and is not used for grading. The Appeals-staffing figure is from a law-firm commentary, not an IRS source."

- id: tax-controversy-08
  title: Generative AI drafting of information document requests and exam reports for revenue agents
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [document-production, research-synthesis]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Revenue agents spend time on routine drafting (information document requests, exam reports) and on extracting facts from large volumes of taxpayer data."
  solution: "EisnerAmper reports that revenue agents are beginning to have access to generative AI programs for routine drafting such as IDRs and exam reports, with agents reviewing and finalizing, and that AI is being used to integrate and summarize large volumes of data for agents. The article does not name an IRS source for this."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "The article says only that use could lead to quicker audits"
      provenance: self-reported
      source_ref: EISNER-IRSAI-2026
  prerequisites:
    - "Approved generative AI tools inside IRS systems; training and data-handling rules for taxpayer information (none described in the source)"
  risks_and_guardrails:
    - "For representatives: AI-drafted IDRs may be broader or less targeted; no source tests this. Note the Tax Court raised the possibility of IRS attorneys using AI-generated false cases (BLAW-TAXCT-2026)"
  human_checkpoints:
    - "Revenue agents review and finalize first drafts (EISNER-IRSAI-2026)"
  role_evolution: "Agents are expected to focus on complex audit areas while AI handles routine drafting (EISNER-IRSAI-2026)."
  evidence_grade: C
  sources:
    - { ref: EISNER-IRSAI-2026, title: "AI at the IRS: Transforming Tax Enforcement and the Future of Taxpayer Services", publisher: "EisnerAmper (Kristen De Noia)", type: firm, url: "https://eisneramper.com/insights/tax/ai-irs-transforming-0126", date: "2026-01-27", access: full, locator: "section 'AI in Audits'" }
    - { ref: BLAW-TAXCT-2026, title: "Tax Court Navigates AI Misuse Rules for Self-Represented Filers", publisher: "Bloomberg Law (Daily Tax Report)", type: press, url: "https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers", date: "2026-03-20", access: full, locator: "final paragraph" }
  last_reviewed: "2026-10-17"
  notes: "Unverified: the claim is from a firm article without a cited IRS source; it is graded C. The same article says AI has been incorporated into the DIF scoring system, which TIGTA's report does not state (TIGTA describes DIF as a separate statistical model that relies on the National Research Program). Do not rely on that sentence."

- id: tax-controversy-09
  title: HMRC AI-enabled risk targeting and document analysis for compliance casework
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "HMRC needs to find inaccuracies across a very large return population and handle document-heavy complex cases, while growing its compliance workforce."
  solution: "HMRC says it uses AI and advanced analytics to highlight where tax returns may contain inaccuracies, which it calls one of the main ways it identifies cases for further investigation, and uses Natural Language Processing to help caseworkers scan large volumes of documents in complex cases. It is trialling Copilot for caseworkers to summarize information and designing AI tools to give rapid case summaries and query large datasets. It ran a data competition with two finalists piloting evasion-detection ideas."
  outcomes:
    - lever: capacity
      description: "HMRC reports that AI and advanced analytical tools supported the protection and recovery of GBP 10 billion in tax in 2025-26."
      figure: "GBP 10 billion"
      measures: "Tax protected and recovered from compliance interventions that HMRC says were directly enabled by the use of AI and advanced analytical tools and techniques, 2025 to 2026; method not published"
      provenance: self-reported
      source_ref: HMRC-ARA-2026
  prerequisites:
    - "HMRC's Connect data platform and third-party data; its first Chief AI Officer was appointed in April 2026 (HMRC-ARA-2026)"
    - "Responsible-AI controls aligned with the HMRC Charter and government AI frameworks (HMRC-ROADMAP-2025)"
  risks_and_guardrails:
    - "Transparency: in Elsbury v Information Commissioner the First-tier Tribunal rejected HMRC's refusal to confirm or deny whether it holds information on large language model use in its R&D tax credit compliance team, finding the claimed fraud risk unsubstantiated (ELSBURY-ICO-2025). The panel accepted the appellant's argument that HMRC correspondence indicators suggested AI use, possibly unauthorised, undermining trust."
    - "ICAS reports that the FT saw HMRC's eventual FOI response, which said the R&D compliance team did not use generative AI on R&D claims and that the technology was not approved for generating taxpayer letters; the FT also reported suggestions that individual caseworkers may have used it without authorisation, which ICAS says raises confidentiality concerns (ICAS-HMRC-2025)"
    - "HMRC states it will adopt AI responsibly under its established ethical and safety controls and the HMRC Charter; no independent audit of HMRC's AI controls was found (HMRC-UPDATE-2026)"
  human_checkpoints:
    - "Caseworkers decide on investigations; the HMRC Permanent Secretary says AI augments agents (CSW-HMRC-2026)"
  role_evolution: "The HMRC Permanent Secretary told MPs he expects HMRC to be broadly the same size in 2030, with AI assisting officials rather than replacing them (CSW-HMRC-2026). HMRC is also recruiting 5,500 additional compliance officers by 2030 (OUTLAW-HMRC-2026)."
  evidence_grade: A
  sources:
    - { ref: HMRC-ARA-2026, title: "HM Revenue and Customs Annual Report and Accounts 2025 to 2026", publisher: "HM Revenue and Customs", type: regulator, url: "https://assets.publishing.service.gov.uk/media/6a4f66c406e7256c331df8a2/HMRC_annual_report_and_accounts_2025_to_2026.pdf", date: "2026-07", access: full, locator: "Chief Executive's foreword; 'AI focus - close the tax gap' box in the closing-the-tax-gap section (around printed p. 21)" }
    - { ref: ELSBURY-ICO-2025, title: "Thomas Elsbury v The Information Commissioner [2025] UKFTT 915 (GRC)", publisher: "First-tier Tribunal (General Regulatory Chamber)", type: regulator, url: "https://caselaw.nationalarchives.gov.uk/ukftt/grc/2025/915", date: "2025-07-31", access: full, locator: "paragraphs 34-48" }
    - { ref: ICAS-HMRC-2025, title: "HMRC's plans for AI", publisher: "ICAS (Susan Cattell)", type: professional-body, url: "https://www.icas.com/news-insights-events/news/tax/hmrc-s-plans-for-ai", date: "2025-10-29", access: full, locator: "closing section on the FOI case" }
    - { ref: CSW-HMRC-2026, title: "HMRC perm sec says AI adoption won't reduce staff numbers", publisher: "Civil Service World", type: press, url: "https://www.civilserviceworld.com/news/article/hmrc-perm-sec-says-ai-adoption-wont-reduce-staff-numbers", date: "2026-01-15", access: full, locator: "paragraphs 2-8" }
    - { ref: OUTLAW-HMRC-2026, title: "UK firms warned following HMRC AI-powered tax crackdown", publisher: "Pinsent Masons (Out-Law)", type: firm, url: "https://www.pinsentmasons.com/out-law/news/uk-firms-warned-following-hmrc-ai-powered-tax-crackdown", date: "2026-07-14", access: full, locator: "opening paragraphs" }
    - { ref: HMRC-UPDATE-2026, title: "HMRC Transformation Roadmap: update 2026", publisher: "HM Revenue and Customs", type: regulator, url: "https://www.gov.uk/government/publications/hmrc-transformation-roadmap-progress-update-2026/hmrc-transformation-roadmap-update-2026", date: "2026-07-02", access: full, locator: "section 'HMRC's progress with AI'" }
    - { ref: HMRC-ROADMAP-2025, title: "HMRC's Transformation Roadmap", publisher: "HM Revenue and Customs", type: regulator, url: "https://www.gov.uk/government/publications/hmrc-transformation-roadmap", date: "2025-07-21", access: full, locator: "Section 6 (as quoted by ICAS-HMRC-2025)" }
  last_reviewed: "2026-10-17"
  notes: "The GBP 10 billion figure is HMRC's own attribution, with no published method, comparison or error rate. Out-Law reports a record GBP 50.2 billion compliance yield in the same year; the source does not say how the two figures relate, so they should not be compared. The Elsbury panel's confidential annex was not public. HMRC Roadmap 2025 was read through the ICAS summary and the gov.uk landing text."

- id: tax-controversy-10
  title: AI call summaries and complaint triage for tax-authority advisers (HMRC)
  archetype: tax
  module: controversy
  function: customer-service
  work_types: [client-interaction, document-production]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Advisers spend time on after-call notes, and complaints must reach the right team quickly. Inconsistent call notes also make later disputes harder to reconstruct."
  solution: "HMRC says it is piloting AI call summarisation that drafts notes from customer calls while a human reviews them, and testing tools to triage customer complaints. The HMRC Permanent Secretary described telephony summarisation as being tested, with the agent still leading the call and the system summarising the outcome and next-best step. HMRC also reports more than 28,000 Copilot licences issued by March 2026, with plans to scale to 50,000 during 2026."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "No time-saving or accuracy figures for call summarisation were found; HMRC says only that it helps advisers save time and improve consistency"
      provenance: self-reported
      source_ref: HMRC-UPDATE-2026
  prerequisites:
    - "Telephony platform with embedded AI (HMRC plans a new contact-centre platform with AI capability delivered incrementally, per the 2026 update)"
    - "Synthetic-data test environments to test AI tools without risking customer data (HMRC-UPDATE-2026)"
  risks_and_guardrails:
    - "Summaries become part of the record of a taxpayer interaction; Werfel's register lists hallucination and control dilution among the risks of AI-enabled correspondence tools (AICPA-WERFEL-2026, risks 1 and 17)"
  human_checkpoints:
    - "A human reviews AI-drafted call notes (HMRC-UPDATE-2026)"
  role_evolution: "The Permanent Secretary expects broadly the same HMRC headcount in 2030, using AI to augment adviser experience (CSW-HMRC-2026)."
  evidence_grade: B
  sources:
    - { ref: HMRC-UPDATE-2026, title: "HMRC Transformation Roadmap: update 2026", publisher: "HM Revenue and Customs", type: regulator, url: "https://www.gov.uk/government/publications/hmrc-transformation-roadmap-progress-update-2026/hmrc-transformation-roadmap-update-2026", date: "2026-07-02", access: full, locator: "foreword (complaint triage, call summaries); section 'HMRC's progress with AI'" }
    - { ref: CSW-HMRC-2026, title: "HMRC perm sec says AI adoption won't reduce staff numbers", publisher: "Civil Service World", type: press, url: "https://www.civilserviceworld.com/news/article/hmrc-perm-sec-says-ai-adoption-wont-reduce-staff-numbers", date: "2026-01-15", access: full, locator: "paragraphs 6-8 (telephony summarisation example)" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendix A: AI Risk Register for Tax Authorities", publisher: "AICPA (Danny Werfel)", type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: "2026-06", access: full, locator: "Appendix A, risks 1 and 17" }
  last_reviewed: "2026-10-17"
  notes: "Named deployment (pilot) without measurements, so grade B. Copilot licence counts measure rollout, not use or benefit."

- id: tax-controversy-11
  title: Real-time AI prompts during online return filing to prevent errors and later notices (ATO)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [client-interaction, review-assurance]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Errors in lodged returns later become reviews, amendments and disputes. Catching them at lodgment is cheaper for both sides."
  solution: "The ATO uses AI models inside myTax that compare amounts a taxpayer enters with expectations from similar taxpayers or prior years and prompt the taxpayer to check specific labels before lodging; the taxpayer can review and amend. Pre-filled data from employers, banks and others is also provided and must be confirmed. Separately, the ATO uses AI risk models to identify potential non-compliance or fraud for human review, and says decisions adversely affecting taxpayer rights are always made by a human."
  outcomes:
    - lever: risk
      description: "The OECD reports that the ATO issued more than 636,000 prompts to individuals in 2023-24, helping to protect approximately AUD 78.9 million in revenue."
      figure: "AUD 78.9 million; more than 636,000 prompts"
      measures: "Prompts issued to individuals during return submission in 2023-24, and the revenue the ATO reported the prompts helped protect; the OECD relays the ATO's figures and the method is not published"
      provenance: self-reported
      source_ref: OECD-GOVAI-2025
  prerequisites:
    - "Pre-filled third-party data and historical return data for the models to compare against"
    - "Chief Data Officer as the accountable official under the Australian government's AI policy (ATO-AI-2026)"
  risks_and_guardrails:
    - "ANAO audit (tabled 28 February 2025) found the ATO's AI governance only partly effective: 74% of AI models in production had no completed data ethics assessment, and for the 14 models deployed between 1 July 2023 and 14 May 2024 there was no evidence of ongoing performance monitoring and reporting (ANAO-ATO-2025, paras 15 and 19)"
    - "For the work-related-expenses models, ANAO found gaps in assessing ethical, privacy and legal considerations (ANAO-ATO-2025, para 16)"
  human_checkpoints:
    - "Taxpayer reviews prompts and decides what to amend before lodging (ATO-AI-2026)"
    - "ATO staff review risk-model output; adverse decisions made by a human, with a right of review (ATO-AI-2026)"
  role_evolution: "ATO says AI frees staff to focus on work needing human judgment (ATO-AI-2026). ANAO notes that an enterprise-wide approach to monitoring AI model performance was due by December 2026 (ANAO-ATO-2025, para 20)."
  evidence_grade: A
  sources:
    - { ref: OECD-GOVAI-2025, title: "Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions", publisher: "OECD", type: regulator, url: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf", date: "2025-09", access: full, locator: "Chapter 5, 'AI in tax administration', Box 5.5" }
    - { ref: ATO-AI-2026, title: "ATO AI transparency statement", publisher: "Australian Taxation Office", type: regulator, url: "https://ato.gov.au/about-ato/commitments-and-reporting/information-and-privacy/ato-ai-transparency-statement", date: "2026-02", access: full, locator: "sections 'AI governance' and 'Examples of how we use AI'" }
    - { ref: ANAO-ATO-2025, title: "Governance of Artificial Intelligence at the Australian Taxation Office (Auditor-General Report No. 22 2024-25)", publisher: "Australian National Audit Office", type: regulator, url: "https://www.anao.gov.au/work/performance-audit/governance-of-artificial-intelligence-the-australian-taxation-office", date: "2025-02-28", access: full, locator: "Summary, paragraphs 8-20" }
  last_reviewed: "2026-10-17"
  notes: "The ATO statement's date (27 February 2026) comes from the landscape scan's search result; the page text read through the mirror shows no date but refers to AI policy version 2.0 from 15 December 2025. The ATO is an Australian authority, and Australian law differs from US law on review rights. The OECD publication carries a 5 September 2025 approval date; the landscape lists 18 September 2025."

- id: tax-controversy-12
  title: Machine-learning clustering and routing of administrative tax-appeal files (Brazil)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [transaction-processing, research-synthesis]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Brazil had around USD 140 billion in assessed taxes waiting for decisions in administrative tax appeals, and an appeal ruling took about six years."
  solution: "Under the AI Litigation Project, supervised machine learning groups similar appeal files so they go to the same officers, which is meant to increase the speed of handling and decisions. Clustering algorithms were used to complete files in full or in part, and a web-based report assistant tool was being developed to help officers reuse blocks of text. Officers label files and paragraphs to improve later suggestions."
  outcomes:
    - lever: speed
      description: "First trials on a sample of 2,000 manually labelled files found that the supervised algorithms can attain sensitivity and specificity of over 80%."
      figure: "over 80% sensitivity and specificity"
      measures: "Sensitivity and specificity of supervised classification of similar-file groups, in first trials on a sample of 2,000 manually labelled appeal files; no throughput or ruling-time result reported"
      provenance: self-reported
      source_ref: OECD-GOVAI-2025
  prerequisites:
    - "Manually labelled historical files for training and testing"
    - "Officer feedback loop (labelling) to improve suggestions"
  risks_and_guardrails:
    - "OECD says taxpayer rights to challenge decisions require AI-assisted decision processes to be explainable, transparent and accountable (OECD-GOVAI-2025, Managing risks and challenges)"
  human_checkpoints:
    - "Appeal officers handle the files and rulings; the tool groups files and suggests text (OECD-GOVAI-2025, Box 5.2)"
  role_evolution: "Officers specialise on grouped sets of similar files and reuse text blocks (OECD-GOVAI-2025, Box 5.2)."
  evidence_grade: A
  sources:
    - { ref: OECD-GOVAI-2025, title: "Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions", publisher: "OECD", type: regulator, url: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf", date: "2025-09", access: full, locator: "Chapter 5, 'AI in tax administration', Box 5.2 and 'Managing risks and challenges'" }
  last_reviewed: "2026-10-17"
  notes: "The OECD box cites a 2022 OECD source for this project, so the trial result may predate 2025. The OECD text names the project and country, not the implementing agency. Trial metrics are classification measures, not dispute outcomes. Graded A on the measured trial result; the project's current status is not stated."

- id: tax-controversy-13
  title: Predictive risk models for audit selection and fraud detection (Austria PACC)
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Austrian tax and customs authorities need to target limited audit resources across income, corporate and VAT tax and customs transactions."
  solution: "Since 2014 the Austrian Federal Ministry of Finance's Predictive Analytics Competence Centre has applied machine-learning risk models, using decision trees, regression models and text mining, to retrospective and real-time audits and fraud detection, with projects underway to add generative models."
  outcomes:
    - lever: risk
      description: "In 2023 the risk models analysed about 6.5 million cases and the Ministry reports additional tax revenues of approximately EUR 185 million; nearly 27.5 million cases were also examined for compliance, with 375,000 flagged for further review for implausible risk profiles."
      figure: "approximately EUR 185 million; 6.5 million cases"
      measures: "Additional tax revenues the Ministry attributes to the PACC risk models across income, corporate and VAT taxes and customs in 2023, from about 6.5 million cases analysed; method not published"
      provenance: self-reported
      source_ref: OECD-GOVAI-2025
  prerequisites:
    - "A specialised analytics unit organised by subject area (predictive, advanced, tax and customs analytics)"
    - "Accurate training data: OECD stresses that risk-model reliability depends on accurate training data (OECD-GOVAI-2025)"
  risks_and_guardrails:
    - "Skewed data and algorithmic errors in tax administration can cause serious harm: OECD cites the Dutch childcare benefits scandal, in which about 26,000 families were wrongly accused of fraud (OECD-GOVAI-2025, Box 5.6)"
  human_checkpoints:
    - "Cases flagged for further review (375,000 in 2023) go to staff; the source does not describe the review step in detail (OECD-GOVAI-2025, Box 5.3)"
  role_evolution: "Not described in the source."
  evidence_grade: A
  sources:
    - { ref: OECD-GOVAI-2025, title: "Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions", publisher: "OECD", type: regulator, url: "https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf", date: "2025-09", access: full, locator: "Chapter 5, Box 5.3 and Box 5.6" }
  last_reviewed: "2026-10-17"
  notes: "The OECD box cites an Austrian Ministry press release of August 2024 that was not opened. No information about false-positive or no-change rates in Austria. Revenue figures are attributed, not audited."

- id: tax-controversy-14
  title: Authority and citation verification step for AI-assisted submissions to the IRS and the Tax Court
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "In Clinco v. Commissioner, T.C. Memo. 2026-16, three of four cases the taxpayer's counsel cited for a signature argument were found not to exist, apparently generated by a large language model, and counsel repeated one after the IRS pointed out the error. A fabricated authority in a protest, IDR response, brief or opinion exposes the practitioner under Circular 230 and court rules."
  solution: "Treat every AI-assisted draft as a draft, and add a documented verification step: check each cited authority in an authoritative database, read the case, confirm calculations, and log the check. Firms discussed in the Journal of Accountancy use citation-verification logs or a second reviewer for briefs."
  outcomes:
    - lever: risk
      description: "none published. The Tax Court judge said he had seen fewer than a dozen instances of hallucinated cases and had issued no sanctions."
      figure: "fewer than a dozen instances"
      measures: "Instances of hallucinated case citations that Judge Holmes had seen in the Tax Court, as stated in an interview reported by Bloomberg Law (March 2026)"
      provenance: independent
      source_ref: BLAW-TAXCT-2026
  prerequisites:
    - "Written firm AI policy with permitted and prohibited uses, approved tools, training, vendor vetting and documentation (IRS-OPR-2026; TAXCT-CLINCO-2026)"
    - "Access to authoritative research platforms to check citations against"
  risks_and_guardrails:
    - "Circular 230 sections 10.22 (due diligence), 10.35 (competence), 10.36 (firm procedures) and 10.37 (written advice) apply to AI use, per IRS OPR Alert 2026-19 (IRS-OPR-2026)"
    - "AICPA Statements on Standards for Tax Services section 1.4 permits reliance on tools but keeps responsibility with the member (TAXCT-CLINCO-2026)"
    - "Sanction routes: IRC section 6673 allows penalties up to $25,000 for frivolous or groundless arguments; lawyers before the Tax Court are bound by the ABA Model Rules under Tax Court Rule 201(a). Judge Holmes said a rule requiring a certification that AI was not used might make no sense because some AI use is legitimate (BLAW-TAXCT-2026; TAXCT-CLINCO-2026)"
    - "Most Tax Court cases (over three-quarters) are pro se, which complicates any disciplinary rule (BLAW-TAXCT-2026)"
  human_checkpoints:
    - "The signing practitioner independently verifies facts, authorities, citations and calculations before delivery or filing (IRS-OPR-2026)"
    - "Second reviewer or citation log for briefs (TAXCT-CLINCO-2026, firm policy section)"
  role_evolution: "Practitioners keep full responsibility for accuracy, and AI use shifts time from drafting toward verification (IRS-OPR-2026; TAXCT-CLINCO-2026)."
  evidence_grade: D
  sources:
    - { ref: IRS-OPR-2026, title: "Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "sections 'Regulatory Framework: Circular 230 Provisions' (1-6) and 'Best Practices'" }
    - { ref: TAXCT-CLINCO-2026, title: "A recipe for sanctions: AI-hallucinated citations in tax", publisher: "Journal of Accountancy (Newkirk and Webber)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/", date: "2026-09-01", access: full, locator: "sections 'A recipe for sanctions', 'Circular 230, SSTSs...' and 'Firm AI use policies'" }
    - { ref: BLAW-TAXCT-2026, title: "Tax Court Navigates AI Misuse Rules for Self-Represented Filers", publisher: "Bloomberg Law (Daily Tax Report)", type: press, url: "https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers", date: "2026-03-20", access: full, locator: "paragraphs 1-12" }
  last_reviewed: "2026-10-17"
  notes: "Idea (D). The step is required by existing duties, but no source reports firm-level error rates or adoption of verification tooling. Clinco is described by the JoA article as apparently the first Tax Court case to address potential AI hallucinations; the court stopped short of formal sanctions."

- id: tax-controversy-15
  title: AI risk register and readiness assessment for tax authorities and preparers
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Tax authorities and practitioners say they do not know which questions to ask to assess readiness for AI or to put to AI vendors in due diligence, and the Tax Court, the IRS and professional bodies have each issued separate, narrower guidance."
  solution: "Danny Werfel's framework, published through the AICPA, gives a 20-risk register for tax authorities (four categories) and a 15-risk register for preparers (a five-layer stack), with five risks shared, a three-tier priority scheme and an eight-step methodology (scope, relevance, prioritisation, governance and vendor controls). It recommends starting with limited-scope pilots. In September 2026 the AICPA launched a Council on AI Risk in Tax to test and refine the framework."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "No use of the register by a named organisation was found"
      provenance: self-reported
      source_ref: AICPA-WERFELART-2026
  prerequisites:
    - "Inventory of AI use cases and defined scope for each deployment"
    - "Risk owner or governance function; Werfel's register flags the lack of an enterprise governance function as a risk"
  risks_and_guardrails:
    - "The author states the views are his and not official AICPA policy (AICPA-WERFELART-2026)"
    - "Transparency measures can conflict with security: disclosing how detection models work could help bad actors evade them (AICPA-WERFELART-2026)"
  human_checkpoints:
    - "Tier 1 risks must be addressed before a deployment launches; mandatory human approval for irreversible, financial or rights-affecting agent actions is an illustrative control (AICPA-WERFELART-2026; AICPA-WERFEL-2026, risk 14)"
  role_evolution: "Chief AI officers or governance owners, and preparer firms' risk owners, run the register; the framework lists skill erosion and workforce expertise erosion as risks (AICPA-WERFELART-2026)."
  evidence_grade: D
  sources:
    - { ref: AICPA-WERFELART-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: "The Tax Adviser (AICPA)", type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: "2026-08-31", access: full, locator: "sections 'Risk registers for the use of AI in tax' to 'Innovate, but responsibly'" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendix A: AI Risk Register for Tax Authorities", publisher: "AICPA (Danny Werfel)", type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: "2026-06", access: full, locator: "Appendices A and B" }
    - { ref: AICPA-CART-2026, title: "AICPA, former IRS commissioner to lead initiative on AI in tax", publisher: "The Tax Adviser (AICPA)", type: professional-body, url: "https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/", date: "2026-09-23", access: full, locator: "paragraphs 2-6" }
  last_reviewed: "2026-10-17"
  notes: "Pattern 'other': structured risk-register assessment before and during deployment. Graded D because the register is a proposed framework with no named adopter. The AICPA Tax Adviser items are published by the same body that backs the framework (self-published). The landscape records 'Stack Model' and 'Quadrant Model' as the two registers' names; the article uses a stack view for preparers and a quadrant view for authorities."

- id: tax-controversy-16
  title: AI triage and first-draft response for tax notices
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [transaction-processing, document-production]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Corporate tax departments and practices receive many authority notices and queries, each with a response deadline. Reading, classifying, assembling support and drafting replies is repetitive. Authority-side automation is expected to raise notice volume faster than live resolution capacity, according to practitioner commentary."
  solution: "AI reads each notice, classifies it, pulls the relevant account and return data, drafts a response and routes it to a reviewer. Practitioner events show the topic is under discussion, but no named deployment was found."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "No measures found"
      provenance: self-reported
      source_ref: TEI-MIDYEAR-2026
  prerequisites:
    - "Clean intake of notices with tracked deadlines; access to returns and account transcripts"
    - "Confidentiality and section 7216 controls for any tax-return information sent to an AI tool (IRS-OPR-2026)"
  risks_and_guardrails:
    - "Written responses to the IRS fall under Circular 230 due diligence and competence duties (IRS-OPR-2026)"
    - "Client permission before client information is entered into AI tools is expected in Australia (TPB-GS-2026)"
  human_checkpoints:
    - "Practitioner reviews and signs every response (IRS-OPR-2026)"
  role_evolution: "Not evidenced for this use case."
  evidence_grade: D
  sources:
    - { ref: TEI-MIDYEAR-2026, title: "2026 Midyear Conference Program At A Glance (TEI Tax Lab: Managing Tax Notices with AI)", publisher: "Tax Executives Institute", type: conference, url: "https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf", date: "2026-03", access: full, locator: "Technology track, Tax Lab listing 'Managing Tax Notices with AI'" }
    - { ref: MILLER-CLE-2025, title: "Leveraging AI, Big Data, IRS Online Services & Emerging Technology for Tax Controversy Professionals", publisher: "Miller & Chevalier (free CLE panel)", type: conference, url: "https://www.millerchevalier.com/event/leveraging-ai-big-data-irs-online-services-emerging-technology-tax-controversy-professionals", date: "2025-06-25", access: full, locator: "event description" }
    - { ref: IRS-OPR-2026, title: "Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Circular 230 provisions 1 and 6" }
    - { ref: TPB-GS-2026, title: "TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct", publisher: "Tax Practitioners Board (Australia)", type: regulator, url: "https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct", date: "2026-07-22", access: full, locator: "Confidentiality section, paragraphs 2-6" }
  last_reviewed: "2026-10-17"
  notes: "Idea (D): conference titles only. A Wolters Kluwer CCH Expert AI notice-triage item appears in search results (July 2026) but the page was not opened, so it is not used. The TEI agenda is a program-at-a-glance dated February 2026 (PDF metadata); topics and times are subject to change."

- id: tax-controversy-17
  title: Pre-filing audit-exposure review against authority-style anomaly checks
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Authorities use anomaly and cross-matching models whose criteria they do not publish, so a return that looks plausible to a human reviewer can still stand out to a model."
  solution: "Practitioners run their own checks before filing: year-over-year consistency, round-number patterns, income against asset indicators, and third-party reporting matches, and they raise the documentation standard for mixed-use items and digital-asset basis. AI can run these checks across a client portfolio. The idea is argued in practitioner commentary; the ATO already prompts individuals at lodgment (tax-controversy-11)."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "No measured outcome found for practitioner-side exposure checks"
      provenance: self-reported
      source_ref: ACCTODAY-2026
  prerequisites:
    - "Client data in structured form across years; contemporaneous records"
  risks_and_guardrails:
    - "The cited commentary asserts several facts about IRS AI that could not be verified from primary sources (see notes); do not use it as evidence of how IRS models work"
    - "Confidentiality duties apply to client data entered into AI tools (IRS-OPR-2026; TPB-GS-2026)"
  human_checkpoints:
    - "Preparer decides which flags to act on and what substantiation to request from the client"
  role_evolution: "The commentary argues that interpretation, explanation and restructuring advice remain with the practitioner as AI handles matching and anomaly detection (ACCTODAY-2026). Unevidenced opinion."
  evidence_grade: D
  sources:
    - { ref: ACCTODAY-2026, title: "What does an AI-driven IRS mean for small accounting firms?", publisher: "Accounting Today (Allison Rinehimer, AT Think opinion)", type: press, url: "https://www.accountingtoday.com/opinion/what-does-the-new-ai-driven-irs-mean-for-small-accounting-firms", date: "2026-07-02", access: full, locator: "sections 'Fraud detection and automated cross-data matching', 'Documentation standards have effectively increased'" }
    - { ref: IRS-OPR-2026, title: "Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Circular 230 provision 6 (sections 6713, 7216)" }
    - { ref: TPB-GS-2026, title: "TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct", publisher: "Tax Practitioners Board (Australia)", type: regulator, url: "https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct", date: "2026-07-22", access: full, locator: "Confidentiality section" }
  last_reviewed: "2026-10-17"
  notes: "Verification flags on ACCTODAY-2026: (1) it cites IRM 10.24.1 (effective 10 February 2026) as the first IRM section governing AI in audit selection; irs.gov/irm/part10/irm_10-024-001 returned a 404 when fetched, so this is unconfirmed. (2) It says GAO flagged the IRS for not ensuring AI models are documented, independently validated or explainable; the GAO documents opened say IRS had not documented elements of an AI sampling pilot (GAO-24-106449) and examined inventory quality (GAO-26-107522), not that wording. (3) It attributes TIGTA workforce figures (25% loss from about 103,000 to about 77,000) that were not checked against the TIGTA report. The IRS CEO's meeting reported headcount of 74,000 (IRS-AIFIRST-2026)."

- id: tax-controversy-18
  title: LLM reasoning to detect and analyse abusive tax strategies (authority research)
  archetype: tax
  module: controversy
  function: risk-compliance-legal
  work_types: [research-synthesis, expert-judgment]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Well-advised taxpayers design tax-minimisation strategies that are hard for authorities to find and analyse across statutes, case law and administrative guidance."
  solution: "Researchers (Blair-Stanek, Holzenberger and Van Durme) tested advanced LLMs on interpreting and verifying strategies, filling gaps in partly specified ones, and generating full strategies. They report that LLM-based reasoning found an apparently novel strategy and position LLMs as a tool for tax agencies. Another paper with overlapping authors pairs LLMs with a symbolic solver to improve auditability."
  outcomes:
    - lever: quality
      description: "The authors report that LLM-based reasoning identified an entirely novel tax strategy. No rates or accuracy figures are in the abstract."
      figure: "none published"
      measures: "Qualitative result in the abstract of 'Can LLMs Identify Tax Abuse?'; no accuracy measure"
      provenance: independent
      source_ref: JHU-TAXABUSE-2025
  prerequisites:
    - "Expert review of generated strategies"
  risks_and_guardrails:
    - "The authors of the second paper argue LLMs alone are poorly suited to tax calculation because errors incur penalties and any system needs high accuracy and auditability (JHU-TAXREASON-2025)"
    - "Models that find avoidance strategies could also help taxpayers generate them (dual use); the abstract frames the use for agencies"
  human_checkpoints:
    - "Not described; academic experiment"
  role_evolution: "Not evidenced."
  evidence_grade: D
  sources:
    - { ref: JHU-TAXABUSE-2025, title: "Can LLMs Identify Tax Abuse?", publisher: "arXiv (Blair-Stanek, Holzenberger, Van Durme)", type: academic, url: "https://arxiv.org/abs/2508.20097", date: "2025-08-10", access: full, locator: "Abstract; v2 of 21 January 2026" }
    - { ref: JHU-TAXREASON-2025, title: "Language Models and Logic Programs for Trustworthy Tax Reasoning", publisher: "arXiv (Jurayj, Holzenberger, Van Durme)", type: academic, url: "https://arxiv.org/abs/2508.21051", date: "2025-08-28", access: full, locator: "Abstract" }
  last_reviewed: "2026-10-17"
  notes: "Idea (D): research paper, not a deployment. The tax-abuse paper was first submitted on 10 August 2025 and revised on 21 January 2026."

- id: tax-controversy-19
  title: AI-enabled IRM research assistant for IRS customer service representatives
  archetype: tax
  module: controversy
  function: customer-service
  work_types: [research-synthesis, client-interaction]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "IRS phone staff need to find the right Internal Revenue Manual guidance while a caller waits, and the IRS aims for first-contact resolution."
  solution: "The IRS rolled out 'Archie', an AI-enabled tool that helps customer service representatives research the Internal Revenue Manual. The National Taxpayer Advocate says it was available to about 12,000 CSRs and part of the Taxpayer 360 project, which had not yet reached the goal of a single integrated taxpayer view as of the 2026 filing season."
  outcomes:
    - lever: experience
      description: "none published. The Advocate calls the new tools promising steps and Taxpayer 360 a work in progress."
      figure: "about 12,000 CSRs with access"
      measures: "Number of customer service representatives to whom the tool was available, per the NTA; no usage, accuracy or resolution data"
      provenance: independent
      source_ref: NTA-OBJ-2026
  prerequisites:
    - "Searchable IRM content; Taxpayer 360 data integration (incomplete)"
  risks_and_guardrails:
    - "Reps' answers shape taxpayer reliance; Werfel's register lists over-trust and unauthorized reliance for authority AI (AICPA-WERFEL-2026, risk 4)"
  human_checkpoints:
    - "The CSR remains the person answering the caller (NTA-OBJ-2026)"
  role_evolution: "CSRs are expected to resolve issues accurately at first contact, aided by research tools (NTA-OBJ-2026)."
  evidence_grade: B
  sources:
    - { ref: NTA-OBJ-2026, title: "National Taxpayer Advocate Fiscal Year 2027 Objectives Report to Congress, Review of the 2026 Filing Season", publisher: "Taxpayer Advocate Service (IRS)", type: regulator, url: "https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/06/JRC27_FullReport.pdf", date: "2026-06", access: full, locator: "Review of the 2026 Filing Season, Taxpayer 360 paragraph" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendix A: AI Risk Register for Tax Authorities", publisher: "AICPA (Danny Werfel)", type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: "2026-06", access: full, locator: "Appendix A, risk 4" }
  last_reviewed: "2026-10-17"
  notes: "The word 'rolled out' and the 12,000 figure come from the NTA; the underlying IRS description was not opened."
```

## 3. Module notes

### 3.1 Processes, steps and work types

- **Selection and notice generation (authority side).** Return classification and issue selection (`review-assurance`, `data-reporting`); third-party data matching and fraud screening that generate notices or refund holds (`transaction-processing`). Taxpayers meet this as an unexplained notice or exam letter. Sources: TIGTA-2025, GAO-2026.
- **Notice intake, triage and response (practitioner and in-house).** Read the notice, classify, assemble support, draft, route for review (`transaction-processing`, `document-production`). Practitioner discussion is limited to conference titles (TEI-MIDYEAR-2026, MILLER-CLE-2025).
- **Examination and audit defence.** Information document requests, substantiation, interviews, exam report (`research-synthesis`, `document-production`, `expert-judgment`). IRS revenue agents reportedly get generative AI for drafting (EISNER-IRSAI-2026, single secondary source).
- **Appeals, Fast Track and ADR.** Protests, case summaries, settlement (`expert-judgment`, `document-production`). TEI's Midyear program listed a session on expanded use of Fast Track and ADR at IRS Appeals (TEI-MIDYEAR-2026). IRS Appeals, Chief Counsel and the Taxpayer Advocate Service reportedly received an AI case-summary tool in late 2025 (EISNER-IRSAI-2026).
- **Litigation.** Research, briefing and citation checking for Tax Court filings (`research-synthesis`, `document-production`). Clinco is the reference case (TAXCT-CLINCO-2026, BLAW-TAXCT-2026).
- **Taxpayer service (authority side).** Calls and chat (`client-interaction`): IRS voicebots, an IRM research assistant for phone staff, HMRC call summaries (NTA-OBJ-2026, HMRC-UPDATE-2026).
- **AI governance of the above.** Inventory, impact assessment, testing documentation and monitoring (`review-assurance`). Sources: GAO-2026, ACCTODAY-TIGTA-2026, ANAO-ATO-2025, AICPA-WERFELART-2026.

### 3.2 Common pain points

- Notice volumes and automation outpace human resolution capacity. IRS assistor-answered calls fell 20% (12.4 million to 9.9 million) between filing seasons 2025 and 2026 on the enterprise lines, and hold time rose from 8 to 14 minutes (NTA-OBJ-2026).
- IRS staff reductions limited AI capability. GAO reports the research group lost 63 employees who worked full or part time on AI, and the IRS had no plan to address AI skill gaps (GAO-2026). IRS headcount ended 2026 at about 74,000, flat for the year after the 2025 reduction (IRS-AIFIRST-2026).
- Selection criteria are not visible to representatives. GAO found the IRS had not completed documentation of an AI sampling pilot's key components (GAO-TAXGAP-2024). Authorities decline to disclose AI use in some cases (ELSBURY-ICO-2025).
- Disparate audit outcomes from selection design. See tax-controversy-03.
- Appeals capacity: a law-firm commentary says 29% of Appeals' workforce left in 2025 and cases are stacking up (CPAPA-APPEALS-2026). It does not discuss AI.
- Fabricated authorities in filings (Clinco).

### 3.3 Metrics and benchmarks

| Metric | Value | What it measures | Provenance | Source |
|---|---|---|---|---|
| IRS AI use cases | 126 active (June 2025), up from 10 (Aug 2022); 65 withheld from public reporting as sensitive or exempt research | Active use cases in the IRS internal inventory | independent (GAO audit of IRS inventory) | GAO-2026, Highlights |
| IRS AI use cases, other counts | 61 (Treasury public inventory, Jan 2026); 225 as of December 2025 (TIGTA, via press) | Different scope and date; not comparable with 126 | independent / press | TREAS-AIINV-2026; ACCTODAY-TIGTA-2026 |
| Inventory quality | over 25% of use cases lacked a stated benefit; some contracted law-enforcement tools missing | Share of inventory entries without benefit information | independent | GAO-2026, Highlights |
| IRS compliance/fraud use cases operational | 18 of 43 (June 2025) | Operational vs in development | independent | GAO-2026, p. 20 |
| High-impact AI documentation | 2 of 5 sampled lacked a documented impact assessment; 4 of 5 lacked testing documentation | TIGTA sample of five presumed high-impact use cases | independent (via press) | ACCTODAY-TIGTA-2026 |
| IRS voicebot outcomes (FS2026) | 17% completed in bot; about 46% transferred; about 14% disconnected | Share of voicebot volume | independent (NTA, IRS data) | NTA-OBJ-2026 |
| IRS bot sessions | over 5 million (FS2024); nearly 25 million (FS2025) | Sessions with voice bots and chatbots | self-reported to GAO | GAO-2026, p. 20 |
| Audit selection pilot (Form 1040) | higher dollar assessment per exam hour, higher no-change rate; no deployment decision | Pilot comparison, no figures | independent | TIGTA-2025, p. 7 |
| Audit rate disparity | 2.9 to 4.7 times (Black vs non-Black taxpayers) | Partial-identification estimate, older data | independent (academic) | SIEPR-AUDIT-2023 |
| ATO AI governance | 74% of models in production without completed data ethics assessment; no ongoing monitoring evidence for 14 models | ANAO audit, data to May 2024 | independent | ANAO-ATO-2025, paras 15, 19 |
| ATO myTax prompts | over 636,000 prompts; approx. AUD 78.9 million protected (2023-24) | Prompts issued, revenue ATO reports protected | self-reported via OECD | OECD-GOVAI-2025, Box 5.5 |
| HMRC AI-enabled compliance | GBP 10 billion protected and recovered (2025-26) | Interventions HMRC says were directly enabled by AI and analytics | self-reported | HMRC-ARA-2026 |
| Austria PACC | EUR 185 million additional revenue; 6.5 million cases analysed (2023) | Ministry-attributed | self-reported via OECD | OECD-GOVAI-2025, Box 5.3 |
| Brazil appeals file classification | sensitivity and specificity over 80% on 2,000 labelled files | First trials | self-reported via OECD | OECD-GOVAI-2025, Box 5.2 |
| FTA members using AI | 70% of 54 FTA members (2024 data) | Share of Forum on Tax Administration members using AI tools | independent (OECD, via Bloomberg Tax) | BTAX-OECDFTA-2025 |
| LLM tax accuracy | models calculated fewer than one third of simplified federal returns correctly; ChatGPT 39 to 47% of common tax questions correct | Benchmarks of tax tasks, not controversy | independent / company-authored (Column Tax) | COLUMN-TAXCALCBENCH-2025; ANTINOZZI-2024 |
| Practitioner AI use | 81% of tax and audit professionals use AI regularly; more than one-third use unauthorised tools | Vendor-owned survey, sample size not stated on the page | vendor-published | TR-FOP-2026 |
| Corporate tax departments | 71% use AI tools, 19% preparing (Germany; sample size not stated) | Adoption | self-reported (firm survey) | KPMG-DE-2026 |

No independent head-to-head benchmark of AI tools for notice response, audit defence or appeals was found. No published override or error rate exists for IRS, HMRC or ATO selection models.

### 3.4 Guardrails and regulatory points

- **IRS OPR Alert 2026-19 (24 Jun 2026).** Applies Circular 230 sections 10.22 (due diligence), 10.27 (fees), 10.35 (competence), 10.36 (firm procedures) and 10.37 (written advice), plus IRC sections 6713 and 7216 (disclosure of return information). Says practitioners must review AI output, and that billing manual time not spent may violate section 10.27 (IRS-OPR-2026).
- **AICPA reaction.** The AICPA asked the IRS to clarify the fee language, saying it does not appear to allow a value-pricing model and overlooks implementation costs and risks (AICPA-CART-2026).
- **AICPA SSTS section 1.4 (Reliance on Tools).** Members may rely on tools, with responsibility retained, per the JoA summary (TAXCT-CLINCO-2026).
- **Australia.** TPB(GS) 55/2026 (final 22 Jul 2026, exposure draft 24 Mar 2026): practitioners stay responsible; verify and review AI content at each step; document verification; obtain client permission before entering client information into AI tools; quality-management system (TPB-GS-2026). ATO says decisions adversely affecting taxpayer rights are always made by a human (ATO-AI-2026).
- **UK.** PCRT topical guidance on AI from seven bodies (19 Jan 2026): integrity, bias and due care, confidentiality, limits of AI (PCRT-AI-2026).
- **Courts.** Tax Court Rule 201(a) binds lawyers to the ABA Model Rules; IRC section 6673 allows penalties up to $25,000 for frivolous or groundless arguments; no AI-specific rule adopted (TAXCT-CLINCO-2026, BLAW-TAXCT-2026).
- **Federal AI governance.** OMB Memorandum M-25-21 requires minimum risk practices for high-impact AI by April 2026; TIGTA reported in September 2026 that Treasury had not issued minimum-practice guidance as of July 2026 and that the IRS has its own policy (ACCTODAY-TIGTA-2026). IRS AI policy of March 2025 requires inventory entries (GAO-2026).
- **EU AI Act (Regulation 2024/1689).** Recital 59 says AI systems intended for administrative proceedings by tax and customs authorities should not be classified as high-risk law-enforcement AI (EU-AIACT). Hadwick argues this leaves tax-authority systems without a category of their own (HADWICK-EUAIACT). The landscape cited Recital 38 for this; the text is in Recital 59.
- **OECD.** Tax administration needs explainability and transparency because taxpayers must be able to challenge decisions; privacy and trust are named as particular constraints (OECD-GOVAI-2025).
- **Transparency law.** In Elsbury v Information Commissioner (31 Jul 2025) the First-tier Tribunal found HMRC's refusal to confirm or deny LLM use in R&D compliance untenable (ELSBURY-ICO-2025).

### 3.5 Frontier signals (dated)

- 2026-10-02 (meeting 2026-09-30): IRS leadership describes an "AI-first IRS" and says AI will not eliminate jobs; stated aim of a mid-90s compliance rate in five years versus about 85% now (IRS-AIFIRST-2026).
- 2026-09-28: TIGTA report on IRS AI risk management, reported as finding documentation gaps for high-impact AI and recommending completion of impact assessments and standard data-quality evaluation (ACCTODAY-TIGTA-2026).
- 2026-09-23: AICPA launches the Council on AI Risk in Tax with Werfel, including NAEA and the Federation of Tax Administrators (AICPA-CART-2026).
- 2026-08-31: Werfel's risk framework published in The Tax Adviser (AICPA-WERFELART-2026).
- 2026-07-22: TPB final AI guidance (TPB-GS-2026). 2026-07-02: HMRC roadmap update with AI call summaries and complaint triage in pilot (HMRC-UPDATE-2026).
- 2026-07: HMRC annual report credits AI and analytics with GBP 10 billion protected; HMRC appoints its first Chief AI Officer in April 2026 (HMRC-ARA-2026).
- 2026-06-24: IRS OPR Alert 2026-19 (IRS-OPR-2026).
- 2026-03-24: GAO report on IRS AI skills, inventory quality and strategy; eight recommendations accepted by the IRS (GAO-2026). 2026-03-20: Tax Court judge says the court is feeling its way on AI guardrails (BLAW-TAXCT-2026).
- 2026-12 (planned): ATO enterprise-wide monitoring of AI model performance, per ANAO (ANAO-ATO-2025, para 20).
- Not yet moved: Tax Court rule on AI; Treasury minimum risk guidance; EU treatment of tax-authority AI.

### 3.6 Workforce and role effects

- IRS: headcount flat at about 74,000 after a loss of more than a quarter of the workforce in 2025; leadership says AI is not designed to eliminate jobs (IRS-AIFIRST-2026). GAO reports that probationary AI experts were let go and that the IRS lacks a workforce plan for AI skills (GAO-2026).
- HMRC: Permanent Secretary expects broadly the same headcount in 2030; AI augments agents (CSW-HMRC-2026). 5,500 extra compliance officers are being recruited (OUTLAW-HMRC-2026).
- Werfel's register lists workforce and expertise erosion as a risk for authorities and skill erosion for preparers (AICPA-WERFELART-2026).
- Practitioners: responsibility stays with the signer (IRS-OPR-2026, TPB-GS-2026). One academic argues AI cannot hold culpability, so corporate tax practice headcount will shrink less than predicted (SALA-TAXNOTES-2026). Vendor-owned survey: over a quarter of tax and audit professionals would not take a job at a firm without professional-grade AI (TR-FOP-2026).

### 3.7 Objections and concerns practitioners and others raise

- Bias in audit selection, and the difficulty of testing without demographic data (SIEPR-AUDIT-2023, GAO-EQUITY-2024, AICPA-WERFEL-2026).
- Opacity and the right to challenge: OECD says authorities' AI decisions need to be explainable so taxpayers can contest them (OECD-GOVAI-2025). Werfel's register says an authority that cannot reconstruct an AI output cannot answer an appeal (AICPA-WERFEL-2026, risk 18).
- Chatbot reliance: a wrong answer from an authority chatbot may create claims of good-faith reliance (AICPA-WERFEL-2026, risk 4).
- Fee pass-through (AICPA objection to OPR) and the cost of implementing AI safely (AICPA-CART-2026).
- A blanket AI-use certification may not make sense because there are legitimate uses (BLAW-TAXCT-2026).
- Possible unauthorised use of AI by authority staff (ELSBURY-ICO-2025, ICAS-HMRC-2025).
- Staff cuts raise error and oversight risk at the same time as AI use expands (GAO-2026).

### 3.8 Interview probes

1. When you last received an IRS or state notice or audit letter, did anyone on the team ask whether the selection or the letter itself came from a model? What would you do differently if the authority published its selection criteria?
2. Walk me through what happens to an AI-assisted draft (protest, IDR response, brief) between the first draft and the signature. Where is the citation check logged, and who else sees it?
3. Does your engagement letter say whether AI tools are used on client data, and does your fee approach change when AI saves time? How are you reading the OPR fee language?
4. What data would you need to show whether AI shortens your notice-response cycle or reduces re-work? Do you measure either today?
5. If an authority uses AI against your client, what record would you request, and what has an authority actually given you?

## 4. Routed to other modules

| Item | Target module | Why | Source |
|---|---|---|---|
| IRS LB&I remarks (29 Jul 2026): AI can support but not replace judgment; transfer pricing expert witnesses must explain inputs, assumptions, methods and AI tools; IRS wants to see formulas to test them | transfer-pricing | TP documentation and expert practice | IRS-LBI-TP-2026 |
| TaxCalcBench: frontier models calculate fewer than one third of simplified federal returns correctly | compliance | Return calculation, not controversy | COLUMN-TAXCALCBENCH-2025 |
| ChatGPT correct on 39-47% of common tax questions (2023-24 tax seasons) | research-advisory | Research quality | ANTINOZZI-2024 |
| LLM plus symbolic solver for auditable tax reasoning | research-advisory | Research and calculation auditability | JHU-TAXREASON-2025 |
| In-house adoption surveys (Thomson Reuters, KPMG Germany) and the argument that corporate tax headcount will shrink less than predicted | tax-data-technology | In-house department adoption and staffing | TR-FOP-2026, TR-CORPTAX-2025, KPMG-DE-2026, SALA-TAXNOTES-2026 |
| IRS Zero Paper AI routing tool (pre-deployment) and paper return digitisation | compliance | Paper-return intake | TREAS-AIINV-2026 |
| Bloomberg Tax Leadership Forum panel on AI in compliance, provisioning and risk (16 Jun 2026) | compliance; provision | Corporate practice, announcement only | BTAX-FORUM-2026 |
| Quality of AI in tax calculation (Column Tax) is company-authored | compliance | See above | COLUMN-TAXCALCBENCH-2025 |


## 5. Sources

Refs follow `PUBLISHER-SHORT-YYYY` and match the landscape file where the same document appears there. Where the landscape combined two documents under one ref (TAXCT-CLINCO-2026, AICPA-WERFEL-2026), the ref is kept for the main document and a new ref is added for the second. Access is `full` for every source below unless stated. Notes on access are in the Gaps section.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| ANAO-ATO-2025 | Governance of Artificial Intelligence at the Australian Taxation Office (Auditor-General Report No. 22 2024-25) | Australian National Audit Office | regulator | https://www.anao.gov.au/work/performance-audit/governance-of-artificial-intelligence-the-australian-taxation-office | 2025-02-28 |
| ATO-AI-2026 | ATO AI transparency statement | Australian Taxation Office | regulator | https://ato.gov.au/about-ato/commitments-and-reporting/information-and-privacy/ato-ai-transparency-statement | 2026-02 |
| ELSBURY-ICO-2025 | Thomas Elsbury v The Information Commissioner [2025] UKFTT 915 (GRC) | First-tier Tribunal (General Regulatory Chamber) | regulator | https://caselaw.nationalarchives.gov.uk/ukftt/grc/2025/915 | 2025-07-31 |
| GAO-2026 | Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522) | U.S. Government Accountability Office | regulator | https://www.gao.gov/products/gao-26-107522 | 2026-03-24 |
| GAO-EQUITY-2024 | Tax Enforcement: IRS Audit Selection Processes for Returns Claiming Refundable Credits Could Better Address Equity (GAO-24-106126) | U.S. Government Accountability Office | regulator | https://www.gao.gov/products/gao-24-106126 | 2024-04-25 |
| GAO-TAXGAP-2024 | Tax Gap: IRS Should Take Steps to Ensure Continued Improvement in Estimates (GAO-24-106449) | U.S. Government Accountability Office | regulator | https://www.gao.gov/products/gao-24-106449 | 2024-05-06 |
| HMRC-ARA-2026 | HM Revenue and Customs Annual Report and Accounts 2025 to 2026 | HM Revenue and Customs | regulator | https://assets.publishing.service.gov.uk/media/6a4f66c406e7256c331df8a2/HMRC_annual_report_and_accounts_2025_to_2026.pdf | 2026-07 |
| HMRC-ROADMAP-2025 | HMRC's Transformation Roadmap | HM Revenue and Customs | regulator | https://www.gov.uk/government/publications/hmrc-transformation-roadmap | 2025-07-21 |
| HMRC-UPDATE-2026 | HMRC Transformation Roadmap: update 2026 | HM Revenue and Customs | regulator | https://www.gov.uk/government/publications/hmrc-transformation-roadmap-progress-update-2026/hmrc-transformation-roadmap-update-2026 | 2026-07-02 |
| IRS-OPR-2026 | Alert 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 |
| NTA-OBJ-2026 | National Taxpayer Advocate Fiscal Year 2027 Objectives Report to Congress, Review of the 2026 Filing Season | Taxpayer Advocate Service (IRS) | regulator | https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/06/JRC27_FullReport.pdf | 2026-06 |
| OECD-GOVAI-2025 | Governing with Artificial Intelligence: The State of Play and Way Forward in Core Government Functions | OECD | regulator | https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/06/governing-with-artificial-intelligence_398fa287/795de142-en.pdf | 2025-09 |
| TIGTA-2025 | The IRS Could Leverage Examination Results in Artificial Intelligence Examination Case Selection Models and Improve Processes to Evaluate Performance (2025-308-022) | Treasury Inspector General for Tax Administration | regulator | https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf | 2025-05-19 |
| TPB-GS-2026 | TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct | Tax Practitioners Board (Australia) | regulator | https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct | 2026-07-22 |
| EU-AIACT | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Recital 59 | European Parliament and Council (Official Journal) | standard-setter | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689 | 2024-07-12 |
| PCRT-AI-2026 | Professional bodies issue AI advice to members (PCRT topical guidance on AI) | Association of Taxation Technicians (for the seven PCRT bodies) | standard-setter | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 2026-01-19 |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 |
| AICPA-WERFEL-2026 | A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendix A: AI Risk Register for Tax Authorities | AICPA (Danny Werfel) | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-06 |
| AICPA-WERFELART-2026 | A risk framework for AI use in tax administration and preparation | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/ | 2026-08-31 |
| ICAS-HMRC-2025 | HMRC's plans for AI | ICAS (Susan Cattell) | professional-body | https://www.icas.com/news-insights-events/news/tax/hmrc-s-plans-for-ai | 2025-10-29 |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax | Journal of Accountancy (Newkirk and Webber) | professional-body | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 |
| ANTINOZZI-2024 | Is ChatGPT an Accurate Source of Information for Uninformed Taxpayers? (abstract via Wealth Strategies Journal) | Antinozzi and Cooper (working paper) | academic | https://wealthstrategiesjournal.com/2024/06/30/hannah-smith-antinozzi-lauren-cooper-is-chatgpt-an-accurate-source-of-information-for-uninformed-taxpayers-june-18-2024/ | 2024-06-18 |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task | arXiv (Bock, Molisee, Ozer, Shah; Column Tax authors) | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 |
| HADWICK-EUAIACT | Slipping Through the Cracks, the Carve-outs for AI Tax Enforcement Systems in the EU AI Act | European Papers, Vol. 9 No. 3, pp. 936-955 (David Hadwick) | academic | https://www.europeanpapers.eu/e-journal/slipping-through-cracks-carve-outs-ai-tax-enforcement-systems-eu-ai-act | 2024-12-30 |
| JHU-TAXABUSE-2025 | Can LLMs Identify Tax Abuse? | arXiv (Blair-Stanek, Holzenberger, Van Durme) | academic | https://arxiv.org/abs/2508.20097 | 2025-08-10 |
| JHU-TAXREASON-2025 | Language Models and Logic Programs for Trustworthy Tax Reasoning | arXiv (Jurayj, Holzenberger, Van Durme) | academic | https://arxiv.org/abs/2508.21051 | 2025-08-28 |
| SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Tax Notes State 121:189; abstract via TaxProf Blog) | Tax Notes (Michael V. Sala) | academic | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 |
| SIEPR-AUDIT-2023 | Measuring and Mitigating Racial Disparities in Tax Audits | Stanford Institute for Economic Policy Research (Elzayn, Smith, Hertz, Ramesh, Fisher, Ho, Goldin) | academic | https://siepr.stanford.edu/publications/working-paper/measuring-and-mitigating-racial-disparities-tax-audits | 2023-01 |
| KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence (quick surveys) | KPMG Germany | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-06 |
| TR-CORPTAX-2025 | The GenAI paradox (State of the Corporate Tax Department 2025) | Thomson Reuters | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 |
| TR-FOP-2026 | Future of Professionals Report 2026, tax and audit paper | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 |
| BTAX-FORUM-2026 | Bloomberg Tax Leadership Forum to Examine AI, Policy Shifts, and Global Tax Risk | Bloomberg Tax | conference | https://pro.bloombergtax.com/?p=17345 | 2026-06-10 |
| MILLER-CLE-2025 | Leveraging AI, Big Data, IRS Online Services & Emerging Technology for Tax Controversy Professionals | Miller & Chevalier (free CLE panel) | conference | https://www.millerchevalier.com/event/leveraging-ai-big-data-irs-online-services-emerging-technology-tax-controversy-professionals | 2025-06-25 |
| TEI-MIDYEAR-2026 | 2026 Midyear Conference Program At A Glance (TEI Tax Lab: Managing Tax Notices with AI) | Tax Executives Institute | conference | https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf | 2026-03 |
| EISNER-IRSAI-2026 | AI at the IRS: Transforming Tax Enforcement and the Future of Taxpayer Services | EisnerAmper (Kristen De Noia) | firm | https://eisneramper.com/insights/tax/ai-irs-transforming-0126 | 2026-01-27 |
| GT-OECD-2025 | Governing with AI: tax authorities (factsheet summarising the OECD report) | Grant Thornton Ireland | firm | https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/ | 2025-09-19 |
| IRS-LBI-TP-2026 | Report on recent US international tax developments, 31 July 2026 (IRS LB&I remarks of 29 July 2026) | EY Tax News | firm | https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026 | 2026-07-31 |
| OUTLAW-HMRC-2026 | UK firms warned following HMRC AI-powered tax crackdown | Pinsent Masons (Out-Law) | firm | https://www.pinsentmasons.com/out-law/news/uk-firms-warned-following-hmrc-ai-powered-tax-crackdown | 2026-07-14 |
| ACCTODAY-2026 | What does an AI-driven IRS mean for small accounting firms? | Accounting Today (Allison Rinehimer, AT Think opinion) | press | https://www.accountingtoday.com/opinion/what-does-the-new-ai-driven-irs-mean-for-small-accounting-firms | 2026-07-02 |
| ACCTODAY-TIGTA-2026 | IRS's AI risk management needs to be improved | Accounting Today | press | https://www.accountingtoday.com/news/irs-ai-risk-management-needs-to-be-improved | 2026-09-28 |
| BLAW-TAXCT-2026 | Tax Court Navigates AI Misuse Rules for Self-Represented Filers | Bloomberg Law (Daily Tax Report) | press | https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers | 2026-03-20 |
| BTAX-OECDFTA-2025 | Tax Authorities Increasingly Use AI in Audits, OECD Report Finds (on the OECD tax administration digitalisation report) | Bloomberg Tax | press | https://news.bloombergtax.com/daily-tax-report/tax-authorities-increasingly-use-ai-in-audits-oecd-report-finds | 2025-06-17 |
| CPAPA-APPEALS-2026 | A Matter of Balance: IRS Appeals Processes, Staffing Create Growing Concerns for Practitioners, Taxpayers | CPA Practice Advisor (Frost Law authors) | press | https://www.cpapracticeadvisor.com/2026/07/21/a-matter-of-balance-irs-appeals-processes-staffing-create-growing-concerns-for-practitioners-taxpayers/187095/ | 2026-07-21 |
| CSW-HMRC-2026 | HMRC perm sec says AI adoption won't reduce staff numbers | Civil Service World | press | https://www.civilserviceworld.com/news/article/hmrc-perm-sec-says-ai-adoption-wont-reduce-staff-numbers | 2026-01-15 |
| IRS-AIFIRST-2026 | Tax chief pushes 'AI-first IRS' to get more out of agency's workforce | Nextgov/FCW (Jory Heckman) | press | https://www.nextgov.com/artificial-intelligence/2026/10/tax-chief-pushes-ai-first-irs-get-more-out-agencys-workforce/416389/ | 2026-10-02 |
| TREAS-AIINV-2026 | IRS ramps up AI use amid staff cuts, Treasury inventory shows | FedScoop | press | https://fedscoop.com/treasury-irs-ai-use-case-inventory/ | 2026-01-29 |

Source count: 46 distinct sources. By type: regulator 14, press 8, academic 7, professional-body 5, firm 4, survey 3, conference 3, standard-setter 2.

## 6. Gaps

**Not found or not reachable**
- No published error rate, override rate, parallel-run result or inspection outcome for AI used by practitioners in notice response, audit defence, appeals or litigation drafting. All practitioner-side use cases are grade D.
- No published false-positive, no-change or override rates for IRS, HMRC or ATO selection models after deployment. TIGTA's report is redacted where results would be; LB&I had no examination-result data for its Line Anomaly Recommender (TIGTA-2025).
- TIGTA's September 2026 report on IRS AI risk management (2026208059fr.pdf) returned 403 from tigta.gov and the mirror. Its figures are from Accounting Today only. The TIGTA FY2026 management challenges report was not opened.
- Axios coverage of the IRS Agentforce rollout (21 Nov 2025) is blocked; the deployment rests on one EisnerAmper article. The Tax Notes Talk 2026 episodes (Tax Court Chief Judge on AI, state audit-selection bias) and the IMF technical note on generative AI for compliance risk analysis were not opened.
- The HMRC and ATO annual-report and ANAO detail beyond the pages cited was not read in full. HMRC's AI algorithmic transparency records and any NAO review were not found in one search. The OECD Tax Administration 2025 and the FTA's AI governance framework were not reached (the OECD page opened only as a short stub).
- The Elsbury confidential annex is not public. The Austrian Ministry press release and the 2022 OECD source for Brazil were not opened.
- NTU's questions for the Chief Counsel nominee (which raise AI and the term 'symplexity') carry no readable date on the page, so it is not cited.
- State tax agencies (California CDTFA chatbot, FTA briefing paper) and state tribunals were not covered beyond the landscape. No source on US Appeals or Chief Counsel guidance for AI-generated documents.
- Closed communities (TEI, r/taxpros) not reached.

**Corrections to the landscape file**
- The EU AI Act carve-out for tax authorities is in Recital 59, not Recital 38.
- OECD Governing with Artificial Intelligence: the primary report says the ATO issued more than 636,000 prompts that helped protect approximately AUD 78.9 million; the Grant Thornton Ireland summary (19 Sep 2025) rounds these to 600,000 and close to AUD 80 million and says tax administration is among the areas showing concrete results. The OECD text itself says tax administration shows relatively less use by total number of use cases than some other functions, and attributes this partly to regulatory constraints. The report was approved on 5 Sep 2025.
- The landscape says the Tax Court judge floated an AI certification rule. In the Bloomberg Law interview Judge Holmes said the rules committee might amend rules to require a certification that AI has not been used, but he was not sure that would make sense, and said the court is "feeling our way in the dark".
- The landscape dates the framework's publication as Sep 2026; The Tax Adviser article is dated 2026-08-31, and the CART announcement (2026-09-23) calls it published "earlier this month" while the Journal of Accountancy article of 2026-09-01 already cites the August issue.
- Counts of IRS AI use cases differ by source and date (126 internal inventory June 2025, 61 Treasury public inventory January 2026, 225 as of December 2025 per TIGTA via press). They are not comparable.

**Unverified claims in sources (not used as evidence)**
- Accounting Today opinion (2 Jul 2026) cites IRM 10.24.1 (effective 10 Feb 2026) as the IRS's first IRM section on AI in audit selection. The IRM URL returned 404 when fetched. Its statement that GAO found the IRS lacked controls to ensure AI models are documented, independently validated or explainable is not worded that way in the GAO texts opened. Its TIGTA workforce figures were not checked.
- EisnerAmper's statement that AI is incorporated in the DIF system is not supported by TIGTA's description of DIF.
- The HMRC GBP 10 billion AI attribution, the ATO AUD 78.9 million, Austria EUR 185 million and Brazil's 80% sensitivity/specificity are all self-reported; method not published.
