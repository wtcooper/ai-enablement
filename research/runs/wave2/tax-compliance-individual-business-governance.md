# Governance and evidence: individual, trust, partnership and small-business return preparation

- **Archetype:** tax
- **Module:** compliance-individual-business
- **Angle:** governance (what constrains and measures the work)
- **Prepared:** 2026-10-17 (wave 2)
- **Working method:** sources downloaded with `curl` into a private temporary folder, PDFs read with `pdftotext`, bot-walled pages through the `r.jina.ai` mirror where the brief allows. Web search was rationed; four searches returned results before the shared budget ran out. Every source below was opened and read (`access: full`); none rests on a search extract alone. Reading depth differs and is stated in the locators and notes.

## 1. Summary

- **The rules are "existing duties apply", and they now exist in writing in three jurisdictions.** The IRS Office of Professional Responsibility (OPR) issued Alert 2026-19 on 2026-06-24, mapping generative AI onto Circular 230 sections 10.22 (due diligence), 10.27(a) (fees), 10.35 (competence), 10.36 (firm procedures), 10.37 (written advice) and 10.51(a)(15), plus IRC sections 6713 and 7216. The UK PCRT bodies published topical AI guidance on 2026-01-19, and Australia's Tax Practitioners Board issued guidance statement TPB(GS) 55/2026 on 2026-07-22 after an exposure draft on 2026-03-24. None creates a new rule; all keep the signing practitioner responsible.
- **The IRS operational documents that govern the return workflow do not mention AI.** Publication 1345 (Rev. 12-2025, e-file providers), Publication 4557 and Publication 5708 (security), the 7216 regulations, Rev. Proc. 2013-14 (consent wording) and the Form 8867 instructions (Rev. November 2025, preparer due diligence) contain no reference to AI. Firms must read AI into duties written for a different workflow: interview and document the client, obtain written consent before disclosure, protect data under the FTC Safeguards Rule, and have the taxpayer review the return before signing.
- **The most specific governance artefact for this module is Danny Werfel's preparer risk register** (The Tax Adviser, 2026-08-31, with appendices). It has 15 risks in five layers (technical, practice, legal and regulatory, business, workforce and strategic), an eight-step deployment method, a worked case study of a tool that extracts documents, suggests deductions and drafts positions, and illustrative gates and thresholds. It is a proposal, not a standard. The AICPA launched a Council on AI Risk in Tax on 2026-09-23 to test and refine it. The landscape file's "20 risks" belong to the separate tax-authority register.
- **Measured quality evidence is thin, vendor-sourced or adjacent.** Black Ore says its agentic preparer reached accuracy above 99 percent across tens of thousands of pilot returns (company claim, no definition of accuracy). Thomson Reuters's early-adopter partner estimates about an hour saved per simple 1040. Against that, the only measurement of models on return calculation found (TaxCalcBench, mid-2025 models, authors from a deterministic-engine vendor) found the best model strictly correct on 32.35% of 51 simplified returns. No error rates, override rates, parallel-run results or inspection outcomes for AI-prepared returns were found. The only human-preparer error baseline found dates from 2014.
- **The live friction is fees.** OPR says not to bill for manual time AI saved and to credit cost reductions; the AICPA (2026-09-08) is asking the IRS to clarify, says the language does not appear to allow value pricing, and its CEO called it non-authoritative. No IRS response was found.
- **Adoption is broad in research and communication, thin in preparation.** In the AICPA 2026 tax software survey (1,808 members who prepared 2025 returns for a fee), 65% use AI in tax research, 32% for client communication, and 16% have no plans to use AI (24.3% a year earlier).
- **Enforcement is not yet visible.** The Tax Court's *Clinco* opinion (hallucinated citations, no sanctions) is the first Tax Court case of its kind according to the Journal of Accountancy. No OPR, TPB or state-board disciplinary action for AI-assisted return preparation was found.
- **Evidence mix of the 15 candidate use cases:** grade A: 0; B: 2; C: 4; D (ideas): 9.

## 2. Use cases

```yaml
- id: tax-compliance-individual-business-01
  archetype: tax
  module: compliance-individual-business
  title: Agent prepares the 1040 from source documents and prior-year return, then hands it to a CPA for review
  function: service-delivery
  work_types:
  - transaction-processing
  - document-production
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: Individual-return preparation is a seasonal, document-heavy flow (collect W-2s, 1099s and K-1s, key or
    import the data, prepare, review). Firms strain to keep pace with peak-season volume, and the signing preparer
    carries full responsibility for every position on the return whoever or whatever drafted it.
  solution: Thomson Reuters announced Ready to Review on 2025-11-05, an agentic workflow on its CoCounsel platform
    that uses agents to process source documents and prior-year returns, extract and categorise data and generate
    returns for professional review; it was in an early-adopter program, with general availability stated for December
    2025. Black Ore opened its Tax Autopilot to CPA firms on 2026-04-29 after a two-year invitation-only pilot;
    the company says it ingests source documents, applies federal and state logic, generates workpapers and routes
    the finished return into the firm's existing tax software for human sign-off.
  outcomes:
  - lever: speed
    description: A partner at one early-adopter firm (CLH CPAs and Consultants) estimates a saving of about an hour
      on each simple 1040
    figure: approximately 1 hour per simple 1040
    measures: reduction in preparation time per simple 1040, as estimated by a CLH partner in a vendor press release;
      not a time study and no baseline given
    provenance: vendor-published
    source_ref: TR-COCOUNSEL-2025
  - lever: quality
    description: Black Ore says Tax Autopilot achieved accuracy above 99 percent across tens of thousands of returns
      in its pilot
    figure: above 99%
    measures: company-stated accuracy across pilot returns; the press report does not define what counts as accurate
      (field, return, or after review) or how it was measured
    provenance: vendor-published
    source_ref: BLACKORE-2026
  - lever: speed
    description: Black Ore says time savings of up to 98 percent on complex filings
    figure: up to 98%
    measures: company-stated maximum time saving on complex filings; baseline and sample not given
    provenance: vendor-published
    source_ref: BLACKORE-2026
  prerequisites:
  - Digitised source documents and prior-year returns in a form the agent can read
  - Integration with the firm's existing tax software, where the return is reviewed and signed (BLACKORE-2026)
  - A documented verification policy and logging before any client return is processed (AICPA-WERFELAPP-2026, Appendix
    D, Step 5)
  - Engagement letters updated for AI use and responsibility allocation (AICPA-WERFELAPP-2026, Appendix D, Step
    5)
  risks_and_guardrails:
  - The signing preparer remains responsible for every position on the return; a vendor contract cannot transfer
    that responsibility (AICPA-WERFELAPP-2026, Appendix D, Step 6 note).
  - OPR says Circular 230 section 10.22 due diligence requires verifying the facts, citations and calculations AI
    produces; practitioners cannot rely solely on AI (IRS-OPR-2026, Regulatory Framework item 1).
  - 'Werfel''s preparer register names control dilution: faster preparation can leave partner review less rigorous
    in practice even if unchanged on paper (AICPA-WERFELAPP-2026, Appendix C, risk 6).'
  - 'Independent measurement of unaided models on the calculation step is poor: the best of four mid-2025 models
    computed 32.35% of 51 simplified federal-only returns strictly correctly (COLUMN-TAXCALCBENCH-2025, results
    table). That test does not measure the vendors'' products.'
  - No independent error rate, override rate or parallel-run result for either product was found.
  human_checkpoints:
  - Signing preparer confirms every AI-drafted position before filing (AICPA-WERFELAPP-2026, Appendix D, Step 5)
  - Review and sign-off in the firm's tax software (BLACKORE-2026)
  - Taxpayer reviews the return before signing the e-file authorisation (IRS-PUB1345-2025, taxpayer signature section)
  role_evolution: Vendors frame the accountant as the reviewer and signer of agent-prepared returns (BLACKORE-2026).
    Werfel warns that staff may learn to operate tools rather than the underlying law, and that junior-level work
    is where judgment is built (AICPA-WERFELAPP-2026, Appendix C, risk 13). Thomson Reuters Institute's paper advises
    firms to define the early-career role and keep supervision in place before automation erodes development (TR-FOP-2026,
    universal priorities).
  evidence_grade: B
  sources:
  - ref: TR-COCOUNSEL-2025
    title: Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows
    publisher: Thomson Reuters
    type: vendor
    url: https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows
    date: '2025-11-05'
    access: full
    locator: Section 'Transforming Tax Preparation with Agentic AI'; availability note at end
  - ref: BLACKORE-2026
    title: AI Tax Startup Black Ore Opens Platform to CPA Firms
    publisher: Sovereign Magazine
    type: press
    url: https://www.sovereignmagazine.com/article/ai-tax-startup-black-ore-opens-platform-to-cpa-firms
    date: '2026-04-29'
    access: full
    locator: 'Paragraphs 2-4 (''How Tax Autopilot Works''); customer named: Maxwell Locke and Ritter'
  - ref: COLUMN-TAXCALCBENCH-2025
    title: 'TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126)'
    publisher: Column Tax authors (Bock, Molisee, Ozer, Shah), arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2507.16126
    date: '2025-07-22'
    access: full
    locator: Section 4 results table; abstract
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix C risks 6 and 13; Appendix D Steps 5 and 6
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework, item 1 (section 10.22)
  - ref: IRS-PUB1345-2025
    title: 'Publication 1345: Handbook for Authorized IRS e-file Providers of Individual Income Tax Returns (Rev.
      12-2025)'
    publisher: Internal Revenue Service
    type: regulator
    url: https://www.irs.gov/pub/irs-pdf/p1345.pdf
    date: 2025-12
    access: full
    locator: Form 8878/8879 signature authorisation section
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026'
    access: full
    locator: 'Universal priorities: ''Define the role of early-career professionals'''
  notes: 'Grade B: named customers (CLH CPAs and Consultants for Thomson Reuters; Maxwell Locke and Ritter for Black
    Ore) but only vendor-published figures with undefined measures. Thomson Reuters''s release also says early-adopter
    customers ''saw up to 70% faster preparation and workpaper review''; that sentence sits in the audit section
    and does not say which product or step it covers, so it is not used as an outcome. Black Ore holds SOC 2 Type
    II certification per the same report (company statement). Whether Ready to Review reached general availability
    in December 2025 was not confirmed. Basis (agent completing a 1065) and PwC K-1 agents are in the landscape
    file but were not read here.'
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-02
  archetype: tax
  module: compliance-individual-business
  title: AI extraction of W-2, 1099 and K-1 data, checked against the source document before it reaches the return
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Keying or importing client documents is slow, and an extraction error can flow into a return without
    any flag. In the 2026 AICPA tax software survey, importing data and integration with other software were the
    lowest-rated software attributes.
  solution: AI classifies uploaded documents and extracts figures into the preparation system (Black Ore describes
    ingesting W-2s, 1099s, K-1s and brokerage statements; Thomson Reuters describes extraction and categorisation
    inside Ready to Review). The governance control proposed in Werfel's preparer register is independent verification
    of AI-extracted figures against source documents for all returns, spot-check audits of extraction accuracy,
    and an escalation protocol for complex or ambiguous documents.
  outcomes:
  - lever: quality
    description: Black Ore reports accuracy above 99 percent across pilot returns; no extraction-specific figure
      was published
    figure: above 99%
    measures: company-stated accuracy across pilot returns, definition not given (same claim as in tax-compliance-individual-business-01)
    provenance: vendor-published
    source_ref: BLACKORE-2026
  prerequisites:
  - Source documents retained and linkable to each extracted figure so a reviewer can compare
  - A sampling or full-verification procedure for extracted data defined before go-live
  - Escalation route for complex or ambiguous documents (AICPA-WERFELAPP-2026, Appendix C, risk 3 controls)
  risks_and_guardrails:
  - 'Werfel''s illustrative scenario: a W-2 box 12 code is misclassified, a pre-tax health premium is treated as
    taxable wages, and the error is found only when the taxpayer receives a notice (AICPA-WERFELAPP-2026, Appendix
    C, risk 3). This is a hypothetical scenario, not an observed incident.'
  - Client data sent to an AI vendor raises section 7216 and 6713 exposure; OPR says to use only secure, enterprise-approved
    AI (IRS-OPR-2026, Regulatory Framework item 6).
  - Under the 7216 regulations, a person who develops software used to prepare or file a return is itself a tax
    return preparer, and contractors who receive return information for software work must receive written notice
    of sections 6713 and 7216 (TREAS-7216-2008, 301.7216-1(b)(2)(i)(B) and 301.7216-2(d)(2)). Whether a given AI
    vendor falls within those provisions is a legal question the sources reviewed do not answer.
  human_checkpoints:
  - Preparer or reviewer compares extracted figures to source documents (verification policy)
  - Escalation to senior review when a source document is complex or ambiguous
  role_evolution: Data entry becomes verification work. Werfel's register warns that junior staff can end up operating
    the tool without building the tax-law understanding needed to catch its errors (AICPA-WERFELAPP-2026, Appendix
    C, risk 13).
  evidence_grade: C
  sources:
  - ref: BLACKORE-2026
    title: AI Tax Startup Black Ore Opens Platform to CPA Firms
    publisher: Sovereign Magazine
    type: press
    url: https://www.sovereignmagazine.com/article/ai-tax-startup-black-ore-opens-platform-to-cpa-firms
    date: '2026-04-29'
    access: full
    locator: Paragraph 'How Tax Autopilot Works'
  - ref: TR-COCOUNSEL-2025
    title: Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows
    publisher: Thomson Reuters
    type: vendor
    url: https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows
    date: '2025-11-05'
    access: full
    locator: Ready to Review description
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix C, risk 3 (Incorrect Document Extraction)
  - ref: AICPA-TAXSW-2026
    title: 2026 tax software survey (1,808 AICPA members; AI adoption questions)
    publisher: The Tax Adviser and Journal of Accountancy (AICPA)
    type: survey
    url: https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/
    date: '2026-08-31'
    access: full
    locator: 'Section ''Ratings'': importing data and integration'
  - ref: TREAS-7216-2008
    title: '26 CFR 301.7216-1, 301.7216-2 and 301.7216-3: disclosure or use of tax return information by tax return
      preparers'
    publisher: U.S. Treasury (T.D. 9375, as amended 2008), text read from eCFR
    type: regulator
    url: https://www.ecfr.gov/current/title-26/section-301.7216-3
    date: 2008-01
    access: full
    locator: 301.7216-1(b)(2)(i)(B); 301.7216-2(d)(2)
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework, item 6
  notes: 'Survey figure for context: respondents rated importing data 3.4 on average across the seven major products
    (5 is best), with integration also lowest; this is a rating of software, not of AI. WK CCH Axcess Expert AI
    Scan (document intelligence for W-2, 1099, K-1) is in the landscape file as search-only; its pages were bot-blocked
    here and no figure is used. No independent extraction accuracy measure for tax documents was found.'
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-03
  archetype: tax
  module: compliance-individual-business
  title: 'Gate-controlled rollout: research and summarisation first, then deduction suggestions, then position drafting'
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Vendors package document extraction, deduction suggestion and position drafting together. In Werfel's
    preparer case study the proposed tool had no scope restriction, no oversight requirement and no phase boundary,
    and the signing preparer would still carry full responsibility.
  solution: 'Idea (a published framework, no deployment found): authorise the tool in phases. Phase 1 is document
    summarisation, data extraction and research support only; Phase 2 adds AI-suggested deductions and credits under
    mandatory independent verification; Phase 3 allows AI-drafted positions. Expansion depends on gate conditions
    rather than dates. The case study''s illustrative gates include: independent testing showing a hallucination
    rate of 2% or less on the firm''s return types; hallucination rate held at 2% or less for 60 consecutive days;
    Phase 2 error rate at 1% or less for 90 consecutive days; and automatic suspension if the error rate exceeds
    1% in any 30-day window. A per-preparer override rate below 5% triggers mandatory review because it suggests
    approval rather than analysis.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no figure published
    source_ref: AICPA-WERFELAPP-2026
  prerequisites:
  - A named owner with authority to restrict or suspend the tool (AICPA-WERFELAPP-2026, Appendix D, Step 6)
  - 'Items the case study lists as Phase 1 gate conditions: a documented, trained and tested independent-verification
    policy, confirmed 100% logging, engagement letters updated and approved by counsel, and an executed vendor contract
    with accuracy SLA and data protection terms (AICPA-WERFELAPP-2026, Appendix D, Step 7)'
  - Measurement of hallucination, error and override rates on the firm's own client return types
  risks_and_guardrails:
  - The thresholds are illustrative figures in a hypothetical case study, not evidence-based standards or regulator
    requirements. Werfel's article says the framework is not a standard and was written for the AICPA, and the AICPA
    says views are the author's (AICPA-WERFEL-2026, author note).
  - Werfel's article advises piloting or deploying with limited scope and testing thoroughly before scaling, noting
    that incremental deployments can still yield large returns (AICPA-WERFEL-2026, 'Innovate, but responsibly').
  - A tool restricted to summarisation would not trigger malpractice exposure at meaningful intensity because no
    filed position is involved (AICPA-WERFEL-2026, preparers register discussion).
  human_checkpoints:
  - 'Sign-offs in the case study: managing partner for Phase 1; senior partner and counsel for Phase 2; managing
    partner and general counsel for Phase 3 (AICPA-WERFELAPP-2026, Appendix D, Step 7)'
  - Signing preparer verifies every AI-drafted position before filing
  role_evolution: Adoption becomes a governed programme owned by a partner or general counsel rather than a tool
    a preparer starts using. Phase 3 gates include an annual check that staff can perform AI-assisted tasks without
    the tool (AICPA-WERFELAPP-2026, Appendix D, Step 7).
  evidence_grade: D
  sources:
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix D, Steps 1, 5, 6 and 7 (phased rollout slide)
  - ref: AICPA-WERFEL-2026
    title: A risk framework for AI use in tax administration and preparation (Danny Werfel)
    publisher: The Tax Adviser (AICPA), August 2026 issue
    type: professional-body
    url: https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/
    date: '2026-08-31'
    access: full
    locator: Section 'Innovate, but responsibly'; preparers risk register discussion
  - ref: AICPA-CART-2026
    title: AICPA, former IRS commissioner to lead initiative on AI in tax
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/
    date: '2026-09-23'
    access: full
    locator: Paragraphs on CART's purpose (testing and refining the framework)
  notes: 'Idea: discussed by a former IRS commissioner and adopted as the starting point for the AICPA''s new Council
    on AI Risk in Tax (CART, 2026-09-23), which will test and refine the framework. No firm has published using
    the phase gates. Correction to the landscape file: the ''20 risks'' belong to the tax authorities register;
    the preparers register has 15 risks in five categories (technical, practice, legal and regulatory, business,
    workforce and strategic).'
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-04
  archetype: tax
  module: compliance-individual-business
  title: Log every AI suggestion and the preparer's decision, and monitor override and error rates
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: When an AI-assisted position is challenged, a firm with no record cannot show what the tool suggested
    and what the preparer verified. Werfel's register lists this as a transparency and malpractice risk.
  solution: 'Idea (published guidance, no deployment found): keep a full log of every AI suggestion and the preparer''s
    decision (accept, modify, reject) with override rationale, retained for 7 years at the highest control level,
    and review override rates by preparer monthly. Australia''s TPB tells practitioners to verify AI content at
    each step of the workflow, establish processes to contest AI outputs, and document each step to meet record-keeping
    and quality-management obligations. OPR''s best-practice list includes documenting AI usage and verification
    processes.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no figure published
    source_ref: AICPA-WERFELAPP-2026
  prerequisites:
  - Tool or workflow that records suggestions and user decisions in a retrievable form
  - 'Retention period set (Werfel''s high-intensity column: 7 years; medium: 5 years)'
  - Someone assigned to review the logs and act on error patterns
  risks_and_guardrails:
  - Logs are firm records that may be produced in an IRS examination or client dispute (AICPA-WERFELAPP-2026, Appendix
    D, Step 6 organisational questions).
  - Logs hold client return information and fall under the firm's information-security duties (IRS-PUB5708-2024,
    Requirements).
  - Override-rate monitoring is a proposal in the register, with no published evidence of what rate indicates good
    practice.
  human_checkpoints:
  - Monthly review of override rates by preparer and error patterns
  - Management escalation when an error pattern is confirmed
  role_evolution: Reviewers' decisions become auditable data. The same documentation is what the TPB expects to
    see under Determination sections 30 and 40 (TPB-GS55-2026, paragraph 10).
  evidence_grade: D
  sources:
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix C risks 1, 7 and 12 (controls); Appendix D Step 5 (documentation and audit trail)
  - ref: TPB-GS55-2026
    title: TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct
    publisher: Tax Practitioners Board (Australia)
    type: regulator
    url: https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct
    date: '2026-07-22'
    access: full
    locator: Competency section, paragraph 10 and Table 1
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Best Practices for Responsible AI Use
  notes: Idea. The TPB paragraph is a regulator's expectation (Australia), not a US requirement; the Werfel retention
    periods are illustrative.
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-05
  archetype: tax
  module: compliance-individual-business
  title: 'Firm-level AI governance programme: written policy, named owner, training and vendor vetting, documented
    against Circular 230 section 10.36'
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Staff use AI tools whether or not the firm has sanctioned them. In the Thomson Reuters 2026 survey, more
    than one-third of tax and audit professionals admit using unauthorised AI tools. In Wolters Kluwer's January
    2025 survey, only 25% of firms had established AI policies.
  solution: Regulators ask principals to put adequate procedures in place. OPR says firms should deploy policies
    for AI use covering staff training, secure data handling, AI accuracy monitoring and vetting of outsourced or
    third-party tools, with the steps documented to show adherence to section 10.36. The Journal of Accountancy's
    recommended policy elements include permitted and prohibited uses, human verification of all cited authorities,
    facts, calculations and legal conclusions, supervisory review and documentation of AI use. Australia's TPB ties
    the same expectations to its quality-management and supervision determinations.
  outcomes:
  - lever: risk
    description: Wolters Kluwer's survey found only a quarter of firms had AI policies; it also reports that firms
      with policies viewed AI more positively than those without
    figure: 25% of firms with policies; 84% vs 44% positive
    measures: share of surveyed firms that had established AI policies; and share viewing AI positively among firms
      with and without policies (survey of over 2,300 global participants; the correlation is the report's, not
      a measured effect of policies)
    provenance: vendor-published
    source_ref: WK-FRA-2025
  prerequisites:
  - A named principal responsible for AI use across the practice
  - An approved-tools list and a vendor review checklist (security, confidentiality, data-use terms)
  - Training on hallucination, bias and confidentiality risks
  risks_and_guardrails:
  - Section 10.36 discipline requires willfulness, recklessness or gross incompetence plus a pattern or practice
    of non-compliance; the section does not make every AI error a principal's violation (IRS-OPR-2026, item 4 quotes
    the text).
  - Competence under section 10.35 includes understanding how AI systems work, their limits and risks (IRS-OPR-2026,
    item 3).
  - OPR's alert is described as introductory guidelines; the AICPA's chief executive said the fee language in it
    is not authoritative (AICPA-FEES-2026).
  - For AICPA members, SSTS section 1.4 (Reliance on Tools) says tools may be relied on reasonably but do not absolve
    professional responsibility (as summarised in TAXCT-CLINCO-2026).
  human_checkpoints:
  - Principal approval of tools before use on client work
  - Periodic review of AI use practices against evolving guidance
  role_evolution: Partners and principals take on an explicit AI oversight duty. Thomson Reuters's paper recommends
    that firms govern the tools being used, approve secure tools and give usage guidance (TR-FOP-2026, universal
    priorities).
  evidence_grade: C
  sources:
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework, items 3, 4 and 6; Best Practices
  - ref: TAXCT-CLINCO-2026
    title: 'A recipe for sanctions: AI-hallucinated citations in tax (analysis of Clinco v. Commissioner, T.C. Memo.
      2026-16)'
    publisher: Journal of Accountancy (AICPA)
    type: press
    url: https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/
    date: '2026-09-01'
    access: full
    locator: Sections on Circular 230 and SSTS; sidebar 'Firm policies for responsible AI use in tax practice'
  - ref: TPB-GS55-2026
    title: TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct
    publisher: Tax Practitioners Board (Australia)
    type: regulator
    url: https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct
    date: '2026-07-22'
    access: full
    locator: Table 1 (Determination sections 30, 35 and 40) and paragraphs 8-12
  - ref: PCRT-AI-2026
    title: Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax
    publisher: ICAEW Insights (news item on the seven-body PCRT guidance)
    type: professional-body
    url: https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax
    date: '2026-01-19'
    access: full
    locator: 'Fundamental principles: professional competence and due care'
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026'
    access: full
    locator: 'Universal priorities: ''Govern the tools being used'''
  - ref: WK-FRA-2025
    title: Wolters Kluwer releases inaugural report, the Future Ready Accountant
    publisher: Wolters Kluwer
    type: survey
    url: https://www.wolterskluwer.com/en/news/wolters-kluwer-releases-inaugural-report-the-future-ready-accountant
    date: '2025-01-14'
    access: full
    locator: Key findings bullets on adoption and barriers
  - ref: AICPA-FEES-2026
    title: AICPA seeks IRS clarity on AI guidelines, CPA fees
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/news/2026/sep/aicpa-seeks-irs-clarity-on-ai-guidelines-cpa-fees/
    date: '2026-09-08'
    access: full
    locator: Paragraph quoting AICPA president and CEO
  notes: 'Grade C because the only measured prevalence figures are vendor-published surveys with different samples
    (WK: over 2,300 global participants in accounting and tax, January 2025; TR: tax and audit professionals, 2026).
    The AICPA small-firm AI policy template (April 2026) is in the landscape file as search-only and was not opened.
    UK: the seven PCRT bodies'' guidance, effective as topical guidance from 2026-01-19, says members may need to
    consult an AI specialist if unfamiliar with AI, and should perform risk-based due diligence on outputs (PCRT-AI-2026);
    only the news items about the guidance were read, not the guidance itself.'
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-06
  archetype: tax
  module: compliance-individual-business
  title: 'Revise engagement letters and consent forms for AI use: disclosure, section 7216 consent, and responsibility
    allocation'
  function: risk-compliance-legal
  work_types:
  - document-production
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Return information shared with an AI vendor may be a disclosure or use that needs taxpayer consent, and
    clients who learn after an error that AI drafted a position may dispute the fee or leave. No rule requiring
    disclosure of AI use was found in the sources reviewed.
  solution: 'Idea (guidance, not a deployment): update the engagement letter and consent step. Under the section
    7216 regulations a preparer may not disclose or use return information without written consent unless an exception
    applies; consent must be knowing and voluntary, signed and dated, identify the purpose and recipient, and cannot
    be conditioned on the service except for disclosure to another preparer; for Form 1040 series filers Rev. Proc.
    2013-14 sets mandatory wording and format. Australia''s TPB says permission to put client information into AI
    tools may be given by a signed engagement letter and recommends telling the client to whom and where data goes,
    where it is stored and whether AI tools may be used. Werfel''s register recommends engagement-letter language
    on AI use and responsibility allocation and a client disclosure policy.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no figure published
    source_ref: TREAS-7216-2008
  prerequisites:
  - Counsel review of consent and engagement language
  - A list of AI vendors that receive return information, with their data-retention and training terms
  - A decision on which uses are covered by a regulatory exception and which need consent
  risks_and_guardrails:
  - Unauthorised disclosure or use carries criminal exposure under section 7216 (a misdemeanor, up to one year or
    a fine of $1,000 or both, per Rev. Proc. 2013-14) and a civil penalty under section 6713 ($250 per disclosure,
    $10,000 a year cap, per the same document); amounts are as stated in the 2013 revenue procedure and were not
    checked for later change.
  - A single consent document cannot authorise both uses and disclosures for Form 1040 filers, and consent cannot
    be obtained retroactively (TREAS-7216-2008, 301.7216-3(b)(1) and (c)(1)).
  - A consent to disclosure to a preparer outside the United States is required, and consent to disclose a Form
    1040 filer's SSN abroad is restricted (TREAS-7216-2008, 301.7216-3(a)(3)(i)(D) and (b)(4)).
  - The regulations and revenue procedure reviewed do not mention AI; how they apply to a given LLM vendor is not
    answered by the sources read. OPR cites sections 6713 and 7216(a) and Circular 230 section 10.51(a)(15) for
    unauthorised disclosure through AI platforms (IRS-OPR-2026, item 6).
  - UK PCRT guidance says inputting client data into a publicly available AI model without consent is likely to
    breach confidentiality and suggests anonymised, generic data (PCRT-AI-2026, Confidentiality).
  human_checkpoints:
  - Client signs and dates the consent before any disclosure or use
  - Counsel review of language before the tool is used on any client matter (AICPA-WERFELAPP-2026, Appendix D, Step
    6)
  role_evolution: Client onboarding gains a technology-disclosure conversation. The Journal of Accountancy notes
    practitioners are beginning to weigh when to disclose AI use and that no universal rule requires it in most
    tax matters (TAXCT-CLINCO-2026, 'Disclosure considerations').
  evidence_grade: D
  sources:
  - ref: TREAS-7216-2008
    title: '26 CFR 301.7216-1, 301.7216-2 and 301.7216-3: disclosure or use of tax return information by tax return
      preparers'
    publisher: U.S. Treasury (T.D. 9375, as amended 2008), text read from eCFR
    type: regulator
    url: https://www.ecfr.gov/current/title-26/section-301.7216-3
    date: 2008-01
    access: full
    locator: 301.7216-3(a)(1), (a)(3)(i), (b), (c); 301.7216-2(d)(1)-(2); 301.7216-1(b)(2)(i)(B)
  - ref: IRS-RP201314-2013
    title: 'Rev. Proc. 2013-14: format and content of taxpayer consents under section 301.7216-3 (Form 1040 series)'
    publisher: Internal Revenue Service
    type: regulator
    url: https://www.irs.gov/pub/irs-drop/rp-13-14.pdf
    date: 2013-01
    access: full
    locator: Sections 3.01-3.02 (penalties) and 5.01-5.04 (form and mandatory wording)
  - ref: TPB-GS55-2026
    title: TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct
    publisher: Tax Practitioners Board (Australia)
    type: regulator
    url: https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct
    date: '2026-07-22'
    access: full
    locator: Confidentiality section, paragraphs on client permission and engagement letters
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework, item 6
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix C risks 7, 8, 10 and 12 (controls)
  - ref: PCRT-AI-2026
    title: Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax
    publisher: ICAEW Insights (news item on the seven-body PCRT guidance)
    type: professional-body
    url: https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax
    date: '2026-01-19'
    access: full
    locator: 'Fundamental principles: confidentiality'
  - ref: TAXCT-CLINCO-2026
    title: 'A recipe for sanctions: AI-hallucinated citations in tax (analysis of Clinco v. Commissioner, T.C. Memo.
      2026-16)'
    publisher: Journal of Accountancy (AICPA)
    type: press
    url: https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/
    date: '2026-09-01'
    access: full
    locator: '''Disclosure considerations'''
  notes: 'Idea: practitioner-facing guidance and an NYSSCPA webinar on section 7216 and AI vendors (landscape, search-only)
    discuss it; no firm has published its AI consent wording. Treat the legal interpretation as unresolved and take
    advice.'
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-07
  archetype: tax
  module: compliance-individual-business
  title: Move client work from public chatbots to approved tools covered by the firm's written information security
    plan
  function: technology-it
  work_types:
  - software-systems
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Preparers use whichever AI tool is at hand. Return information is among the most sensitive data a firm
    holds, and the IRS and FTC already require a written security programme that covers service providers.
  solution: 'Restrict client data to enterprise-approved AI under the firm''s written information security plan
    (WISP). OPR says practitioners must use only secure, enterprise-approved AI and never upload sensitive data
    to unsecured sites. IRS Publication 5708 lists the FTC Safeguards Rule elements that apply to tax preparers
    as financial institutions: a qualified individual, risk assessment, service-provider contracts that require
    safeguards, multi-factor authentication and reporting of a security event affecting 500 or more people to the
    FTC within 30 days.'
  outcomes:
  - lever: risk
    description: Thomson Reuters Institute reports that more than one-third of tax and audit professionals admit
      using unauthorised AI tools
    figure: more than one-third
    measures: share of surveyed tax and audit professionals who said they use unauthorised AI tools (2026 Future
      of Professionals Report; sample size not stated on the page read)
    provenance: vendor-published
    source_ref: TR-FOP-2026
  prerequisites:
  - An approved-tools list and a process to vet new tools
  - A current WISP with a named qualified individual (IRS-PUB5708-2024)
  - Contracts with AI providers that bind them to safeguards, bar training on client data without explicit written
    consent, and require incident notification (AICPA-WERFELAPP-2026, Appendix D contract terms)
  risks_and_guardrails:
  - Where client data goes into a model that retains it or trains on it, the firm may face section 7216 and 6713
    questions (IRS-OPR-2026, item 6).
  - Werfel's illustrative contract terms include vendor notice 60 days before a material model change, notice within
    24 hours of a systematic output error or data incident, and a right to commission independent accuracy testing;
    these are proposals, not market practice evidence.
  - None of the IRS operational publications read (Publications 1345, 4557 and 5708, Form 8867 instructions) mention
    AI.
  human_checkpoints:
  - Qualified individual approves tools and reviews security testing results
  - Staff acknowledge the acceptable-use rules
  role_evolution: Practice administrators or IT leads take on AI vendor oversight alongside the traditional data-security
    role.
  evidence_grade: C
  sources:
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework item 6; Best Practices
  - ref: IRS-PUB5708-2024
    title: 'Publication 5708: Creating a Written Information Security Plan for your Tax and Accounting Practice
      (Rev. 8-2024)'
    publisher: Internal Revenue Service
    type: regulator
    url: https://www.irs.gov/pub/irs-pdf/p5708.pdf
    date: 2024-08
    access: full
    locator: '''Requirements'' (page 2): FTC Safeguards Rule elements'
  - ref: IRS-PUB4557-2024
    title: 'Publication 4557: Safeguarding Taxpayer Data (Rev. 5-2024; footer reads 6-2024)'
    publisher: Internal Revenue Service
    type: regulator
    url: https://www.irs.gov/pub/irs-pdf/p4557.pdf
    date: 2024-06
    access: full
    locator: 'Safeguards program section: select service providers'
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026'
    access: full
    locator: 'Universal priorities: ''Govern the tools being used'''
  - ref: PCRT-AI-2026
    title: Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax
    publisher: ICAEW Insights (news item on the seven-body PCRT guidance)
    type: professional-body
    url: https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax
    date: '2026-01-19'
    access: full
    locator: 'Fundamental principles: confidentiality'
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix D, Step 6 (contract requirements)
  notes: Pub 5708 text is from the Rev. 8-2024 edition; the FTC rule detail should be checked against current FTC
    text before use.
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-08
  archetype: tax
  module: compliance-individual-business
  title: AI-assisted tax research for return positions, with every cited authority verified before use
  function: service-delivery
  work_types:
  - research-synthesis
  - expert-judgment
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Preparers and reviewers research positions for Schedule C, partnership and S corporation returns. General
    models can invent authorities. In Clinco v. Commissioner, T.C. Memo. 2026-16, the court said three of four cases
    cited by taxpayer's counsel on a signature argument appeared to be hallucinations from a large language model,
    and counsel left one in a later table of authorities after the IRS pointed it out.
  solution: Practitioners use tax research assistants and general tools to find and summarise authority, then verify.
    In the 2026 AICPA tax software survey, 65% of respondents said they use AI in tax research. H&R Block and OpenAI
    announced on 2025-04-15 a tool for H&R Block tax professionals, grounded in vetted data from H&R Block's Tax
    Institute, aimed at keeping them current on code changes and handling complicated questions, targeted for the
    2026 season; they also said they would study the return on investment from AI tools qualitatively.
  outcomes:
  - lever: capacity
    description: 'Adoption benchmark (not an outcome): most surveyed CPA preparers report using AI for tax research'
    figure: 65%
    measures: share of respondents (1,808 AICPA members who prepared 2025 returns for a fee; survey fielded June
      1-19, 2026) who said they use AI in tax research; 16% said no plans to use AI, down from 24.3% a year earlier
    provenance: independent
    source_ref: AICPA-TAXSW-2026
  - lever: quality
    description: 'Adjacent-domain measurement: two vendors'' retrieval-based legal research tools hallucinated between
      17% and 33% of the time in a preregistered evaluation'
    figure: 17% to 33%
    measures: share of evaluation queries in which Lexis+ AI and Thomson Reuters's AI research tools produced hallucinated
      content, per the paper's abstract; legal research queries, not tax queries; query count not read
    provenance: independent
    source_ref: MAGESH-HALLUC-2024
  prerequisites:
  - Research tool grounded in authoritative tax content, with source links the reviewer can open
  - A rule that every cited authority is opened and read before it reaches a client memo, return position or filing
  - A firm policy on which tools may be used (see tax-compliance-individual-business-05)
  risks_and_guardrails:
  - 'Clinco: the court stopped short of sanctions but wrote that submitting a brief with fictitious caselaw is ''a
    recipe for sanctions''; the article says it appears to be the first Tax Court case on possible AI hallucinations
    (TAXCT-CLINCO-2026).'
  - OPR's alert says practitioners must verify the accuracy of facts, citations and calculations produced by AI,
    and notes that courts have sanctioned lawyers for fabricated citations (IRS-OPR-2026, introductory section;
    item 1).
  - Circular 230 section 10.34(a) bars signing a return the practitioner knows or should know contains a position
    lacking a reasonable basis (TREAS-C230-2014, 10.34(a)(1)); the alert does not cite this section.
  - No independent accuracy measurement of tax-specific research assistants was found; the Stanford result concerns
    legal research tools and caps this entry's grade.
  human_checkpoints:
  - Reviewer opens and reads each cited authority
  - Second reviewer cross-checks authorities for litigation filings (TAXCT-CLINCO-2026, 'Litigation safeguards')
  role_evolution: Research shifts from searching to verifying. Werfel's register warns that junior staff may accept
    confident, well-formatted AI lists without checking authorities (AICPA-WERFELAPP-2026, Appendix C, risk 4).
  evidence_grade: B
  sources:
  - ref: AICPA-TAXSW-2026
    title: 2026 tax software survey (1,808 AICPA members; AI adoption questions)
    publisher: The Tax Adviser and Journal of Accountancy (AICPA)
    type: survey
    url: https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/
    date: '2026-08-31'
    access: full
    locator: Section 'Use of AI and other technical tools'
  - ref: TAXCT-CLINCO-2026
    title: 'A recipe for sanctions: AI-hallucinated citations in tax (analysis of Clinco v. Commissioner, T.C. Memo.
      2026-16)'
    publisher: Journal of Accountancy (AICPA)
    type: press
    url: https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/
    date: '2026-09-01'
    access: full
    locator: '''The apparitions in the briefing''; ''A recipe for sanctions''; ''Judicial scrutiny'''
  - ref: CNBC-HRB-2025
    title: ChatGPT for taxes? OpenAI and H&R Block have a plan for tax pros
    publisher: CNBC (via NBC 7 San Diego)
    type: press
    url: https://www.nbcsandiego.com/news/business/money-report/chatgpt-for-taxes-openai-and-hr-block-have-a-plan-for-tax-pros/3804532/?amp=1
    date: '2025-04-15'
    access: full
    locator: Paragraphs on the joint project, Tax Institute data and the ROI study
  - ref: MAGESH-HALLUC-2024
    title: Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362)
    publisher: Magesh, Surani, Dahl, Suzgun, Manning and Ho (Stanford)
    type: academic
    url: https://arxiv.org/abs/2405.20362
    date: '2024-05-30'
    access: full
    locator: Abstract
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Real-World Consequences; Regulatory Framework item 1
  - ref: TREAS-C230-2014
    title: 31 CFR 10.34, Circular 230 standards with respect to tax returns and documents
    publisher: U.S. Treasury (Circular 230, Rev. 6-2014), text read from eCFR
    type: regulator
    url: https://www.ecfr.gov/current/title-31/section-10.34
    date: 2014-06
    access: full
    locator: 10.34(a)(1)
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix C risk 4
  notes: 'Grade B: a named real use (counsel in Clinco, a failure case; AICPA prevalence data) without published
    accuracy measurements for tax-specific tools; the 17-33% figure is an adjacent legal-research measurement. The
    H&R Block and OpenAI tool was announced; whether it launched for the 2026 season and any ROI findings were not
    found. Research-advisory is the home module for the research product landscape; this entry covers the return-position
    use only.'
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-09
  archetype: tax
  module: compliance-individual-business
  title: Route calculation to a deterministic tax engine and keep the language model for intake, explanation and
    orchestration
  function: technology-it
  work_types:
  - software-systems
  - transaction-processing
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: Unaided language models calculate returns unreliably, yet agentic preparers promise return drafts. Calculation
    errors, wrong tax tables and eligibility mistakes are costly and hard to audit.
  solution: 'Idea (researchers'' recommendation; no deployment described in the sources): pair the model with a
    deterministic calculation engine or a symbolic solver. The TaxCalcBench authors conclude that their findings
    point to a continued need for deterministic tax calculation engines and for added infrastructure and orchestration
    around models. A Johns Hopkins team accepted to AAAI 2026 proposes translating rules into logic programs for
    a symbolic solver and reports reduced cost, estimated from real-world penalties for tax errors, on a statutory
    reasoning dataset.'
  outcomes:
  - lever: quality
    description: On 51 hand-built simplified federal-only tax year 2024 test cases, the best of four tested models
      (Gemini 2.5 Pro) computed 32.35% of returns correctly under the strict criterion; the others scored 27.45%
      (Claude Opus 4), 25.98% (Gemini 2.5 Flash) and 23.04% (Claude Sonnet 4)
    figure: 32.35% best; 23.04% lowest
    measures: share of test cases where every evaluated line matched the output of a traditional tax engine exactly,
      with the document-collection and preparation steps assumed correct; lenient (within $5 per line) scores were
      51.96%, 42.65%, 41.18% and 38.24%
    provenance: vendor-published
    source_ref: COLUMN-TAXCALCBENCH-2025
  prerequisites:
  - A deterministic engine whose outputs the firm already trusts (the firm's tax software)
  - Interfaces that let the model supply inputs and read results rather than compute them
  - A benchmark of the firm's own return types to test the combined system
  risks_and_guardrails:
  - The benchmark authors work for a company that sells a deterministic tax engine, which is why provenance is marked
    vendor-published; the test used models from mid-2025 and calculation only.
  - 'The authors'' error analysis: models misused tax tables, made calculation errors and misjudged eligibility
    (COLUMN-TAXCALCBENCH-2025, abstract).'
  - Columbia's TaxBench, still in development, will score field-by-field against reviewed reference returns and
    test asking for missing information and rule precedence; no results yet (COLUMBIA-TAXBENCH-2026).
  human_checkpoints:
  - Preparer reviews the engine-calculated return and any model-supplied inputs
  role_evolution: Preparers review inputs and eligibility judgments more than arithmetic. No source describes a
    role change in detail.
  evidence_grade: D
  sources:
  - ref: COLUMN-TAXCALCBENCH-2025
    title: 'TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126)'
    publisher: Column Tax authors (Bock, Molisee, Ozer, Shah), arXiv preprint
    type: academic
    url: https://arxiv.org/abs/2507.16126
    date: '2025-07-22'
    access: full
    locator: Abstract; Section 4 results table; error analysis
  - ref: JHU-TAXREASON-2025
    title: Language Models and Logic Programs for Trustworthy Tax Reasoning (arXiv 2508.21051; accepted to AAAI
      2026)
    publisher: Jurayj, Holzenberger and Van Durme, Johns Hopkins University
    type: academic
    url: https://arxiv.org/abs/2508.21051
    date: '2025-08-28'
    access: full
    locator: Abstract
  - ref: COLUMBIA-TAXBENCH-2026
    title: TaxBench (benchmark in development)
    publisher: Columbia University DAP Lab
    type: academic
    url: https://daplab.cs.columbia.edu/benchmarks/taxbench/
    date: '2026'
    access: full
    locator: '''What it evaluates''; ''Release status'''
  notes: 'Idea labelled as such: the measurement exists but is of unaided models on one step; no firm describes
    the hybrid design in production. Column Tax was reported as acquired by Aiwyn in 2025 (BLACKORE-2026), which
    is relevant to the benchmark authors'' affiliation. Later models than those tested in July 2025 were not covered;
    a refresh of the benchmark was not found.'
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-10
  archetype: tax
  module: compliance-individual-business
  title: 'Vendor diligence and contract terms for AI preparation tools: documented error rates, accuracy commitments,
    model-change notice and independent testing'
  function: procurement-supply-chain
  work_types:
  - review-assurance
  - research-synthesis
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Firms asked to buy agentic preparers have few independent figures to rely on. Werfel's account of the
    tax community is that practitioners do not know what to ask AI vendors to check their products are deployed
    responsibly.
  solution: 'Idea (published framework): ask the vendor for a documented error rate for tax-specific deduction and
    position suggestions on the firm''s return complexity, citation to a specific code section or ruling for every
    suggestion, behaviour outside its training scope, notice before model updates with a re-validation window, liability
    and indemnification terms, data storage and retention, and how it handles degraded context in long sessions.
    Illustrative contract terms include an accuracy SLA with a financial remedy and termination right, 60 days''
    notice of material model change, 24-hour incident notification, and the firm''s right to commission independent
    accuracy testing on 30 days'' notice.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no figure published
    source_ref: AICPA-WERFELAPP-2026
  prerequisites:
  - Firm's own test set of anonymised return types to run before purchase
  - Counsel to negotiate liability and data terms
  - An exit plan so the firm can work without the tool (AICPA-WERFELAPP-2026, Appendix C risk 14)
  risks_and_guardrails:
  - A vendor contract reduces exposure and creates remedies but does not change who bears responsibility for positions
    filed (AICPA-WERFELAPP-2026, Appendix D, contract requirements note).
  - 'Werfel''s scenario: a vendor''s terms disclaim liability for tax advice while the signing preparer faces penalties
    (Appendix C, risks 7 and 8); illustrative, not an observed case.'
  - 'Public benchmarks cannot substitute for firm-specific testing: TaxCalcBench covers simplified federal-only
    returns and calculation only; TaxBench is unreleased.'
  human_checkpoints:
  - Managing partner and counsel sign-off before contract
  - Annual vendor-dependency review
  role_evolution: Practice leaders become buyers of validated capability. Werfel names vendor dependence, where
    a vendor discontinues a product and the firm has no manual workflow, as a risk (AICPA-WERFELAPP-2026, Appendix
    C risk 14).
  evidence_grade: D
  sources:
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix D, Step 6 (questions and illustrative contract terms); Appendix C risks 7, 8 and 14
  - ref: AICPA-WERFEL-2026
    title: A risk framework for AI use in tax administration and preparation (Danny Werfel)
    publisher: The Tax Adviser (AICPA), August 2026 issue
    type: professional-body
    url: https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/
    date: '2026-08-31'
    access: full
    locator: 'Introduction: readiness self-assessment and vendor due diligence'
  - ref: IRS-PUB5708-2024
    title: 'Publication 5708: Creating a Written Information Security Plan for your Tax and Accounting Practice
      (Rev. 8-2024)'
    publisher: Internal Revenue Service
    type: regulator
    url: https://www.irs.gov/pub/irs-pdf/p5708.pdf
    date: 2024-08
    access: full
    locator: 'Requirements: service providers'
  - ref: TPB-GS55-2026
    title: TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct
    publisher: Tax Practitioners Board (Australia)
    type: regulator
    url: https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct
    date: '2026-07-22'
    access: full
    locator: 'Confidentiality section: due diligence on commercial and internally developed AI tools'
  notes: Idea. No procurement checklists or contracts from actual firms were found; the contract terms are Werfel's
    illustrations.
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-11
  archetype: tax
  module: compliance-individual-business
  title: Redesign preparer and partner review so faster, AI-assisted preparation does not mean thinner review
  function: service-delivery
  work_types:
  - review-assurance
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: 'AI-assisted preparation raises volume. Werfel''s register describes control dilution: partners spend
    less time per return reviewing AI-assisted work, so more returns are processed with less scrutiny even though
    the review process is unchanged on paper.'
  solution: 'Idea (published framework): require sign-off that evidences real analysis rather than approval, scale
    sampling and spot checks to volume, set workload thresholds, escalate novel or uncertain positions to senior
    review regardless of the AI''s confidence, and, at the highest control level, a weekly quality review of AI-assisted
    returns plus real-time error-flag monitoring during busy season. The register also recommends reviewing every
    audit finding on AI-assisted returns individually.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no figure published
    source_ref: AICPA-WERFELAPP-2026
  prerequisites:
  - Baseline review time and error data for pre-AI returns to compare against
  - A defined definition of 'novel or uncertain' positions for escalation
  risks_and_guardrails:
  - 'Without a baseline the firm cannot tell whether review quality fell; the only published human-error baseline
    found is old: a 2014 GAO study of 19 undercover visits found only 2 of 19 preparers computed the correct refund,
    and GAO''s analysis of IRS audit data for tax years 2006-2009 estimated errors (changes to tax due or refund)
    in 60% of preparer-prepared returns against 50% of self-prepared ones (GAO-14467T-2014). The sample cannot be
    generalised and the data are over a decade old.'
  - Circular 230 section 10.36 expects principals to take reasonable steps to ensure firm procedures are followed
    (IRS-OPR-2026, item 4).
  human_checkpoints:
  - Senior review of novel positions
  - Reviewer documents the analysis behind sign-off
  role_evolution: Reviewers' work shifts from catching keying errors to testing positions and auditing the tool.
    Werfel warns of a hollowing out of experienced staff as AI reduces demand for their expertise (AICPA-WERFELAPP-2026,
    Appendix C, risk 15).
  evidence_grade: D
  sources:
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix C risks 4-6 and 15; Appendix D Step 5 (human oversight, review frequency, escalation)
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework item 4
  - ref: GAO-14467T-2014
    title: 'Paid Tax Return Preparers: In a Limited Study, Preparers Made Significant Errors (GAO-14-467T)'
    publisher: U.S. Government Accountability Office
    type: regulator
    url: https://www.gao.gov/products/gao-14-467t
    date: 2014-04
    access: full
    locator: 'Highlights: What GAO Found'
  notes: Idea. No measurement of review quality in AI-assisted tax preparation was found. The GAO baseline is foundational
    only.
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-12
  archetype: tax
  module: compliance-individual-business
  title: AI-prompted due-diligence questions and missing-information requests at client intake
  function: service-delivery
  work_types:
  - client-interaction
  - expert-judgment
  pattern: intake-triage
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: For returns claiming the earned income credit, child tax credit, American opportunity credit or head
    of household status, the preparer must interview the client, ask adequate questions, document the questions
    and answers at the time, and file Form 8867; failures carry a per-credit penalty ($650 per credit, $2,600 across
    four credits, for a return filed in 2026, per the instructions). Missing information is also where agent-prepared
    returns are likely to go wrong.
  solution: 'Idea (researchers'' benchmark design; no deployment found): an assistant that reads the client''s initial
    materials, identifies what is missing or inconsistent and drafts the follow-up questions, which the preparer
    asks and records. Columbia''s TaxBench is built to test whether an agent asks only for the information it needs,
    distinguishing information given initially from information the agent must request.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no figure published
    source_ref: COLUMBIA-TAXBENCH-2026
  prerequisites:
  - Intake materials in digital form
  - Preparer interview and contemporaneous notes remain the record of due diligence (IRS-I8867-2025)
  risks_and_guardrails:
  - 'The knowledge requirement is personal: Form 8867 instructions require the preparer to interview the taxpayer,
    ask adequate questions, document them contemporaneously and not ignore implications of information known to
    the preparer (IRS-I8867-2025, due diligence requirements, lines 3 and 4 text).'
  - The instructions do not mention AI; whether AI-generated questions or a chatbot interview satisfy the requirement
    is not addressed in any source read.
  human_checkpoints:
  - Preparer conducts the interview and signs Form 8867
  - Records retained for 3 years per the instructions
  role_evolution: Not described in any source.
  evidence_grade: D
  sources:
  - ref: IRS-I8867-2025
    title: 'Instructions for Form 8867: Paid Preparer''s Due Diligence Checklist (Rev. November 2025)'
    publisher: Internal Revenue Service
    type: regulator
    url: https://www.irs.gov/pub/irs-pdf/i8867.pdf
    date: 2025-11
    access: full
    locator: Due diligence requirements; Part VI Eligibility Certification
  - ref: COLUMBIA-TAXBENCH-2026
    title: TaxBench (benchmark in development)
    publisher: Columbia University DAP Lab
    type: academic
    url: https://daplab.cs.columbia.edu/benchmarks/taxbench/
    date: '2026'
    access: full
    locator: '''What it evaluates''; ''Dataset'''
  notes: Idea built from a benchmark design (researchers discuss agents that request missing information) and an
    existing legal requirement; no practitioner or firm describes doing this. Penalty amounts are inflation-adjusted
    yearly.
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-13
  archetype: tax
  module: compliance-individual-business
  title: Reprice compliance work from hours to value or bundled fees as AI shortens preparation
  function: service-delivery
  work_types:
  - client-interaction
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: If AI cuts hours per return, hourly billing loses revenue and may raise a fee question. OPR's alert says
    billing clients for manual time not actually spent, or double billing AI-assisted tasks, may violate the Circular
    230 bar on unconscionable fees depending on the facts, and says savings should be passed on openly.
  solution: 'Idea (under dispute): firms price on value delivered and bundle services. The AICPA says the OPR language
    does not appear to allow a value-pricing model and overlooks software, implementation, governance and training
    costs; its CEO said many CPAs have moved to value pricing, some bundle return preparation at no extra charge
    with advisory work, and the OPR language is not authoritative. The AICPA is working with the IRS on clarifying
    language and FAQs.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no figure published
    source_ref: AICPA-FEES-2026
  prerequisites:
  - A pricing policy documented before AI savings accrue
  - Engagement letters stating the fee basis
  risks_and_guardrails:
  - 'OPR''s wording: practitioners should disclose AI activities as needed and fairly credit the client''s account
    for cost reductions (IRS-OPR-2026, item 2).'
  - As of the AICPA's 2026-09-08 report no IRS clarification had been issued; none was found since.
  - Thomson Reuters Institute reports about a third of tax and audit professionals say their firms have not yet
    adapted commercial models, and nearly half feel pressure to generate financial gains from AI (TR-FOP-2026, introduction).
  human_checkpoints:
  - Partner approves fee basis; client agrees in engagement letter
  role_evolution: Fee conversations move from time spent to outcome. The AICPA encourages members toward advisory
    services (AICPA-FEES-2026).
  evidence_grade: D
  sources:
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework item 2 (section 10.27(a))
  - ref: AICPA-FEES-2026
    title: AICPA seeks IRS clarity on AI guidelines, CPA fees
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/news/2026/sep/aicpa-seeks-irs-clarity-on-ai-guidelines-cpa-fees/
    date: '2026-09-08'
    access: full
    locator: Paragraphs quoting Simpson, Lauridsen, Lewis and Koziel
  - ref: AICPA-CART-2026
    title: AICPA, former IRS commissioner to lead initiative on AI in tax
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/
    date: '2026-09-23'
    access: full
    locator: Final paragraphs on OPR cost-savings language
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026'
    access: full
    locator: Introduction
  - ref: JOFA-OPRNEWS-2026
    title: IRS outlines AI risks, Circular 230 duties for tax practitioners
    publisher: Journal of Accountancy (AICPA)
    type: press
    url: https://www.journalofaccountancy.com/news/2026/jun/irs-outlines-ai-risks-circular-230-duties-for-tax-practitioners/
    date: 2026-06
    access: full
    locator: '''Billing, written advice, and firm procedures'''
  notes: 'Idea: discussed by the IRS and AICPA but no firm''s repricing outcome was found. Bloomberg Tax''s March
    2026 pricing story (landscape) was not re-read.'
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-14
  archetype: tax
  module: compliance-individual-business
  title: Competence and training programme built on AI failure modes, with the junior pipeline protected
  function: people-hr
  work_types:
  - expert-judgment
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: 'Regulators make competence personal: OPR reads section 10.35 to require understanding how AI systems
    work, their limits and risks; the UK PCRT guidance asks that staff receive appropriate training for any AI tool;
    the TPB ties competence to supervision of entities providing services on the practitioner''s behalf. Meanwhile
    AI automates entry-level tasks.'
  solution: 'Idea (guidance and framework): training on the specific failure modes of each tool (confident, well-formatted
    wrong output; hallucinated authorities), tool-independent tax-law training, annual checks that staff can handle
    complex matters without the tool, and protected structured development for early-career staff. Thomson Reuters
    Institute''s paper tells firms to ensure junior staff still build professional judgment and to put supervision
    in place before automation erodes it.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: no figure published
    source_ref: AICPA-WERFELAPP-2026
  prerequisites:
  - A training owner
  - Defined escalation rules for novel positions regardless of AI confidence
  risks_and_guardrails:
  - Werfel's register describes skill erosion (juniors who cannot analyse a novel partnership allocation issue without
    the tool) and institutional knowledge loss when senior preparers leave earlier (AICPA-WERFELAPP-2026, Appendix
    C, risks 13 and 15); both are illustrative scenarios.
  - 'Training data: in the 2026 tax software survey only 41.2% of respondents received any training in how to use
    their tax software (AICPA-TAXSW-2026, ''Technical support and training''); that is software training, not AI
    training.'
  human_checkpoints:
  - Annual capability assessment independent of AI tools
  role_evolution: Thomson Reuters Institute's survey reports more than a quarter of professionals would not accept
    a job at a firm without professional-grade AI, and nearly one in three would consider leaving if AI expectations
    go unmet within two years (TR-FOP-2026, introduction). Black Ore frames AI as a response to a shortage of qualified
    accountants (BLACKORE-2026).
  evidence_grade: D
  sources:
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework item 3 (section 10.35)
  - ref: PCRT-AI-2026
    title: Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax
    publisher: ICAEW Insights (news item on the seven-body PCRT guidance)
    type: professional-body
    url: https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax
    date: '2026-01-19'
    access: full
    locator: 'Fundamental principles: professional competence and due care'
  - ref: TPB-GS55-2026
    title: TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct
    publisher: Tax Practitioners Board (Australia)
    type: regulator
    url: https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct
    date: '2026-07-22'
    access: full
    locator: Table 1 (Code items 7 and 8; Determination section 35)
  - ref: AICPA-WERFELAPP-2026
    title: Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register,
      preparer case study)
    publisher: The Tax Adviser (AICPA)
    type: professional-body
    url: https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf
    date: 2026-06
    access: full
    locator: Appendix C risks 13 and 15
  - ref: TR-FOP-2026
    title: What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026
    date: '2026'
    access: full
    locator: Universal priorities and introduction
  - ref: AICPA-TAXSW-2026
    title: 2026 tax software survey (1,808 AICPA members; AI adoption questions)
    publisher: The Tax Adviser and Journal of Accountancy (AICPA)
    type: survey
    url: https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/
    date: '2026-08-31'
    access: full
    locator: '''Technical support and training'''
  - ref: BLACKORE-2026
    title: AI Tax Startup Black Ore Opens Platform to CPA Firms
    publisher: Sovereign Magazine
    type: press
    url: https://www.sovereignmagazine.com/article/ai-tax-startup-black-ore-opens-platform-to-cpa-firms
    date: '2026-04-29'
    access: full
    locator: Paragraph on the accountant shortage
  notes: Idea. No firm training programmes with outcomes were found.
  last_reviewed: '2026-10-17'
- id: tax-compliance-individual-business-15
  archetype: tax
  module: compliance-individual-business
  title: AI-drafted client correspondence and plain-language explanations of the return, reviewed before sending
  function: customer-service
  work_types:
  - client-interaction
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Preparers write cover letters, query responses and explanations of positions to clients. The UK PCRT
    guidance warns that AI-prepared correspondence must be checked for tone and content.
  solution: Practitioners use AI to draft correspondence. In the 2026 AICPA tax software survey, 32% of respondents
    said they use AI for client communication. The PCRT guidance says members should review correspondence prepared
    by an AI tool to ensure tone and content are appropriate, and Australia's TPB lists chatbot functionality that
    can give tailored advice among the AI capabilities in tax agent services, and holds practitioners accountable
    for AI outputs they rely on.
  outcomes:
  - lever: capacity
    description: 'Adoption benchmark (not an outcome): about a third of surveyed CPA preparers use AI for client
      communication'
    figure: 32%
    measures: share of respondents (1,808 AICPA members who prepared 2025 returns for a fee) who said they use AI
      for client communication
    provenance: independent
    source_ref: AICPA-TAXSW-2026
  prerequisites:
  - Approved tool (see tax-compliance-individual-business-07)
  - Redaction or consent before client facts go into prompts
  risks_and_guardrails:
  - Written advice must rest on reasonable factual and legal assumptions and cannot rely on unverified AI output
    (IRS-OPR-2026, item 5, section 10.37).
  - A Taxpayer Advocate Service note cites a Washington Post informal test in which two tax software companies'
    chatbots gave inaccurate or irrelevant answers up to 50% of the time on first asking 16 complex tax questions;
    this concerns consumer chatbots, not preparer drafting tools (TAS-AIBLOG-2024).
  - In an experiment with a representative sample of US self-preparers, those shown aggressive AI advice reported
    more aggressively than those given none, although they relied less on AI than on CPA advice (SWIDER-2025, introduction);
    clients may arrive with AI-derived positions.
  human_checkpoints:
  - Preparer reads and edits every client communication before it is sent
  role_evolution: Not described in the sources beyond routine drafting moving to review.
  evidence_grade: C
  sources:
  - ref: AICPA-TAXSW-2026
    title: 2026 tax software survey (1,808 AICPA members; AI adoption questions)
    publisher: The Tax Adviser and Journal of Accountancy (AICPA)
    type: survey
    url: https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/
    date: '2026-08-31'
    access: full
    locator: '''Use of AI and other technical tools'''
  - ref: PCRT-AI-2026
    title: Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax
    publisher: ICAEW Insights (news item on the seven-body PCRT guidance)
    type: professional-body
    url: https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax
    date: '2026-01-19'
    access: full
    locator: 'Fundamental principles: professional behaviour'
  - ref: TPB-GS55-2026
    title: TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct
    publisher: Tax Practitioners Board (Australia)
    type: regulator
    url: https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct
    date: '2026-07-22'
    access: full
    locator: '''What is AI?'' capability list'
  - ref: IRS-OPR-2026
    title: Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)
    publisher: IRS Office of Professional Responsibility (GovDelivery bulletin)
    type: regulator
    url: https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70
    date: '2026-06-24'
    access: full
    locator: Regulatory Framework item 5
  - ref: TAS-AIBLOG-2024
    title: Is AI Generated Tax Advice Making the Grade?
    publisher: Taxpayer Advocate Service (IRS)
    type: regulator
    url: https://www.taxpayeradvocate.irs.gov/news/tax-tips/is-ai-generated-tax-advice-making-the-grade/2024/06/
    date: 2024-06
    access: full
    locator: Paragraph on the Washington Post review
  - ref: SWIDER-2025
    title: 'CPAs vs. AI Tax Advisors: Evaluating Reliance Across Advisory Contexts'
    publisher: Lucas A. Swider, University of Oklahoma; American Accounting Association Tax Section meeting paper
    type: academic
    url: https://aaahq.org/portals/0/documents/meetings/2025/ATA/Papers/3.02_Swider.pdf
    date: '2025'
    access: full
    locator: Abstract; introduction (findings summary)
  notes: 'Grade C: only a prevalence survey and guidance; no named firm or accuracy evidence for correspondence
    drafting. The TAS and Swider items concern the taxpayer-facing side and are context, not evidence for this use
    case.'
  last_reviewed: '2026-10-17'
```

## 3. Module notes

### Processes and key steps (with work types)

1. **Engagement, consent and client organizer** (client-interaction, document-production): engagement letter, section 7216 consents (Form 1040 series wording fixed by Rev. Proc. 2013-14), organizer and checklists.
2. **Document intake and classification** of W-2, 1099, K-1 and brokerage statements (transaction-processing).
3. **Data extraction or entry** into the tax software (transaction-processing, data-reporting).
4. **Due-diligence interview and credit eligibility**, with Form 8867 for the earned income, child, American opportunity and head-of-household claims (client-interaction, expert-judgment).
5. **Preparation and calculation** in the tax engine (transaction-processing).
6. **Technical research for positions** (Schedule C, partnership, S corporation items) (research-synthesis, expert-judgment).
7. **Preparer, senior and partner review** (review-assurance).
8. **Client review, signature authorisation (Form 8879) and e-file** through an Electronic Return Originator with a named Responsible Official (coordination-scheduling).
9. **Billing and pricing** (client-interaction).
10. Post-filing notices and examinations are covered by the controversy module.

### Common pain points

- Importing client data and integration with other software were the lowest-rated attributes in the 2026 AICPA tax software survey (importing data averaged 3.4 of 5 across the seven major products; AICPA-TAXSW-2026).
- Only 41.2% of survey respondents received any training in using their tax software (AICPA-TAXSW-2026), which is relevant to how AI features will be taught.
- Black Ore frames its product around a shortage of qualified accountants and cites Bureau of Labor Statistics and AICPA figures; the report notes the 125-million-hour shortfall figure was not attributed to an external source (BLACKORE-2026).
- Peak-season volume and the signing preparer's non-delegable responsibility (AICPA-WERFELAPP-2026, Appendix D, Step 1).
- Clients arrive with AI-derived positions: in a randomised experiment with a representative US sample of self-preparers, those shown aggressive AI advice reported more aggressively than a no-advice group (SWIDER-2025).

### Metrics and benchmarks (with sources and caveats)

| Metric | Value | Source and caveat |
|---|---|---|
| Use of AI in tax research | 65% of 1,808 AICPA members who prepared 2025 returns for a fee | AICPA-TAXSW-2026; survey 2026-06-01 to 06-19; the "Use of AI Tools" table is an image and was not read |
| Use of AI for client communication | 32% | same |
| No plans to use AI | 16% (24.3% in 2025) | same |
| Firms with AI policies | 25% of firms; 84% positive about AI among firms with policies vs 44% without | WK-FRA-2025, over 2,300 global participants, 2025-01-14, vendor survey; correlation only |
| Professionals using unauthorised AI tools | more than one-third | TR-FOP-2026, vendor-owned institute, sample not stated on page read |
| Unaided model accuracy on 1040 calculation (strict) | 32.35% best of four models; 51 simplified federal-only returns | COLUMN-TAXCALCBENCH-2025; mid-2025 models; authors' employer sells a deterministic engine; calculation only |
| Agentic preparer accuracy | "above 99%" across tens of thousands of pilot returns | BLACKORE-2026; company claim reported by press; no definition |
| Preparer time saving | about 1 hour per simple 1040 (one partner's estimate) | TR-COCOUNSEL-2025; vendor press release |
| Hallucination in retrieval-based legal research tools | 17% to 33% | MAGESH-HALLUC-2024; legal, not tax; adjacent, preregistered evaluation |
| Consumer tax-software chatbots | inaccurate or irrelevant answers up to 50% of the time on first asking 16 questions | TAS-AIBLOG-2024 citing an informal Washington Post test; consumer products |
| Human preparer errors (old baseline) | 2 of 19 undercover visits computed the correct refund; estimated errors in 60% of preparer-prepared vs 50% of self-prepared returns (TY2006-2009) | GAO-14467T-2014; sample not generalisable; over a decade old |
| Proposed control thresholds | hallucination rate at or below 2%; error rate at or below 1% over 90 days; override rate below 5% triggers review; suspend if error rate exceeds 1% in 30 days | AICPA-WERFELAPP-2026, Appendix D Step 7; illustrative figures in a hypothetical case study |
| Due-diligence penalty | $650 per credit, up to $2,600 for four credits, for a return filed in 2026 | IRS-I8867-2025, Part VI |

### Guardrails and regulatory points

- **Circular 230 (IRS-OPR-2026):** section 10.22 (due diligence), 10.27(a) (fees), 10.35 (competence), 10.36 (procedures to ensure compliance, with a pattern-or-practice and willfulness/recklessness/gross incompetence standard for principals' discipline), 10.37 (written advice) and 10.51(a)(15) (willful unauthorised disclosure). Section 10.34(a) (no signing a return containing an unreasonable or no-reasonable-basis position) is not cited in the alert but applies to the same work (TREAS-C230-2014).
- **Section 7216 and 6713, and the regulations (TREAS-7216-2008, IRS-RP201314-2013):** written, signed and dated consent identifying the purpose and recipient; no retroactive consent; special restrictions for disclosure abroad and for SSNs; software developers and e-file providers are "tax return preparers"; contractors for software work need written notice of 6713 and 7216. The sources read do not say how these apply to an LLM vendor.
- **Form 8867 and section 6695(g) (IRS-I8867-2025):** personal interview, contemporaneous documentation of questions and answers, retained 3 years.
- **E-file (IRS-PUB1345-2025):** taxpayers sign the authorisation after reviewing the return; a Responsible Official is accountable for the provider's compliance; an ERO that makes substantive changes to a collected return becomes a preparer and must sign.
- **Information security (IRS-PUB5708-2024, IRS-PUB4557-2024):** FTC Safeguards Rule treats tax preparers as financial institutions: qualified individual, risk assessment, service-provider contracts, multi-factor authentication, 30-day reporting of events affecting 500 or more people.
- **AICPA SSTS section 1.4, Reliance on Tools** (as summarised in TAXCT-CLINCO-2026): tools may be reasonably relied on but do not remove responsibility.
- **OPR organisation:** the IRS said in June 2026 it would merge OPR with the Return Preparer Office to form a Tax Professional Management Office (JOFA-OPRNEWS-2026).
- **UK (PCRT-AI-2026, PCRT-ATT-2026):** integrity, objectivity, competence and due care, confidentiality and professional behaviour applied to AI; risk-based due diligence on output; consult an AI specialist if unfamiliar; anonymise client data in public models.
- **Australia (TPB-GS55-2026):** Code items 6-10 and Determination sections 30, 35 and 40; client permission for entering client information into AI tools (engagement letter acceptable); due diligence on commercial and internally developed tools; Privacy Act and TFN rule.
- **State law:** OPR notes California, Colorado, Illinois and Utah have AI governance legislation (IRS-OPR-2026, State Law section); not examined here.
- **Courts:** *Clinco* shows the standard for filings; the Tax Court lacks a Rule 11 equivalent but its Rule 201(a) binds lawyers to the ABA Model Rules (TAXCT-CLINCO-2026).

### Frontier signals (dated and sourced)

- 2025-11-05: Thomson Reuters announces Ready to Review (agentic 1040 preparation) in an early-adopter program, general availability stated for December 2025 (TR-COCOUNSEL-2025).
- 2026-04-29: Black Ore opens Tax Autopilot to CPA firms after a two-year pilot with 75 firms (company figure) (BLACKORE-2026).
- 2025-04-15: H&R Block and OpenAI announce a preparer assistant targeted for the 2026 season and a joint study of return on investment (CNBC-HRB-2025). Outcome not found.
- 2026-01-19, 2026-06-24, 2026-07-22: PCRT, OPR and TPB guidance (see above).
- 2026-08-31 and 2026-09-23: Werfel framework published; AICPA launches CART to test and refine it (AICPA-WERFEL-2026, AICPA-CART-2026).
- 2026-09-08: AICPA asks IRS to clarify the OPR fee language and is working on clarifying text and FAQs (AICPA-FEES-2026).
- 2026: Columbia's TaxBench (500+ rules, 50+ scenarios, tax year 2025, field-level scoring, tests asking for missing information) is in development (COLUMBIA-TAXBENCH-2026).
- 2026: the share of surveyed CPA preparers with no plans to use AI fell from 24.3% to 16% (AICPA-TAXSW-2026).

### Workforce and role effects

- Reviewer and signer role strengthened on paper (BLACKORE-2026; IRS-OPR-2026), while Werfel warns of control dilution, skill erosion and early retirement of experienced preparers (AICPA-WERFELAPP-2026, Appendix C).
- Retention pressure: more than a quarter of surveyed tax and audit professionals would not accept a job at a firm lacking professional-grade AI, and nearly a third would consider leaving if AI expectations go unmet within two years (TR-FOP-2026).
- Early-career development is flagged as the thing to protect (TR-FOP-2026; AICPA-WERFELAPP-2026).
- Principals gain an explicit oversight duty under section 10.36 (IRS-OPR-2026).

### Objections and concerns practitioners raise

- **Fees:** the AICPA says passing all AI efficiency to clients ignores licence, implementation, governance and training costs and the liability the firm carries (AICPA-FEES-2026).
- **Liability stays with the signer** while vendors disclaim it (Werfel scenarios; illustrative) (AICPA-WERFELAPP-2026, Appendix C, risks 7-8).
- **Hallucinated authority** (*Clinco*) and **confidentiality leakage across clients** (IRS-OPR-2026).
- **Maturity of the guidance:** the OPR document calls itself introductory guidelines, and the AICPA's CEO described its fee language as not authoritative (AICPA-FEES-2026).
- **Vendor dependence** and **skill erosion** (AICPA-WERFELAPP-2026, Appendix C, risks 13-14).

### Interview probes for an advisor

1. Which of your AI features touch client return information, and where does that data go (vendor, region, retention, training)? What does your current engagement letter or consent say about it?
2. When an AI-assisted return is reviewed, what exactly does the reviewer see: the source document, the AI's suggestion, a log of accept/modify/reject? Do you track override rates or error rates, and what would make you suspend a tool?
3. Where is the line today between research and summarisation, deduction suggestion and position drafting, and who can move it?
4. How do you price returns now, and what happened to hours per return in the last busy season? Have you read the OPR fee language and the AICPA's response?
5. Which junior tasks has AI taken over, and how do staff learn to spot a wrong W-2 box 12 treatment or a fake citation without doing the work by hand?

## 4. Routed to other modules

- **controversy** (tax-authority AI and its oversight): the Taxpayer Advocate's 2026 objectives report discloses AI-assisted drafting and mentions an AI research tool for service representatives (its AI mentions were searched here; it is not used as a source). IRS audit and notice automation affecting individual and small-business clients; the Tax Court's *Clinco* procedural questions beyond preparer duties.
- **research-advisory:** the commercial tax research tools (Blue J, CoCounsel, Bloomberg, CCH) and their accuracy; the Stanford legal-research hallucination study is used here only as an adjacent measure.
- **compliance (corporate direct-tax compliance, in-house):** KPMG Germany's May 2026 tax-department survey, Thomson Reuters corporate tax department reports, and TEI material belong to the corporate-compliance lens.
- **cross-cutting professional responsibility:** the OPR, PCRT and TPB documents, the Werfel framework and CART apply to every module; this file cites them for the individual and small-business return workflow only.
- **consumer self-preparation agents (for example the general-purpose agent drafting federal returns reported in April 2026):** not read here; belongs with the practice angle or a consumer lens.
- **business-model / pricing (cross-cutting):** the fee dispute and AI-native roll-ups.

## 5. Sources

31 distinct sources, all opened and read (`access: full`). Types: academic 5, press 4, professional-body 6, regulator 12, survey 3, vendor 1.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | full |
| AICPA-FEES-2026 | AICPA seeks IRS clarity on AI guidelines, CPA fees | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-seeks-irs-clarity-on-ai-guidelines-cpa-fees/ | 2026-09-08 | full |
| AICPA-TAXSW-2026 | 2026 tax software survey (1,808 AICPA members; AI adoption questions) | The Tax Adviser and Journal of Accountancy (AICPA) | survey | https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/ | 2026-08-31 | full |
| AICPA-WERFEL-2026 | A risk framework for AI use in tax administration and preparation (Danny Werfel) | The Tax Adviser (AICPA), August 2026 issue | professional-body | https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/ | 2026-08-31 | full |
| AICPA-WERFELAPP-2026 | Appendices A to D to the AI risk framework (authorities register, authority case study, preparers register, preparer case study) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-06 | full |
| BLACKORE-2026 | AI Tax Startup Black Ore Opens Platform to CPA Firms | Sovereign Magazine | press | https://www.sovereignmagazine.com/article/ai-tax-startup-black-ore-opens-platform-to-cpa-firms | 2026-04-29 | full |
| CNBC-HRB-2025 | ChatGPT for taxes? OpenAI and H&R Block have a plan for tax pros | CNBC (via NBC 7 San Diego) | press | https://www.nbcsandiego.com/news/business/money-report/chatgpt-for-taxes-openai-and-hr-block-have-a-plan-for-tax-pros/3804532/?amp=1 | 2025-04-15 | full |
| COLUMBIA-TAXBENCH-2026 | TaxBench (benchmark in development) | Columbia University DAP Lab | academic | https://daplab.cs.columbia.edu/benchmarks/taxbench/ | 2026 | full |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126) | Column Tax authors (Bock, Molisee, Ozer, Shah), arXiv preprint | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full |
| GAO-14467T-2014 | Paid Tax Return Preparers: In a Limited Study, Preparers Made Significant Errors (GAO-14-467T) | U.S. Government Accountability Office | regulator | https://www.gao.gov/products/gao-14-467t | 2014-04 | full |
| IRS-I8867-2025 | Instructions for Form 8867: Paid Preparer's Due Diligence Checklist (Rev. November 2025) | Internal Revenue Service | regulator | https://www.irs.gov/pub/irs-pdf/i8867.pdf | 2025-11 | full |
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19) | IRS Office of Professional Responsibility (GovDelivery bulletin) | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| IRS-PUB1345-2025 | Publication 1345: Handbook for Authorized IRS e-file Providers of Individual Income Tax Returns (Rev. 12-2025) | Internal Revenue Service | regulator | https://www.irs.gov/pub/irs-pdf/p1345.pdf | 2025-12 | full |
| IRS-PUB4557-2024 | Publication 4557: Safeguarding Taxpayer Data (Rev. 5-2024; footer reads 6-2024) | Internal Revenue Service | regulator | https://www.irs.gov/pub/irs-pdf/p4557.pdf | 2024-06 | full |
| IRS-PUB5708-2024 | Publication 5708: Creating a Written Information Security Plan for your Tax and Accounting Practice (Rev. 8-2024) | Internal Revenue Service | regulator | https://www.irs.gov/pub/irs-pdf/p5708.pdf | 2024-08 | full |
| IRS-RP201314-2013 | Rev. Proc. 2013-14: format and content of taxpayer consents under section 301.7216-3 (Form 1040 series) | Internal Revenue Service | regulator | https://www.irs.gov/pub/irs-drop/rp-13-14.pdf | 2013-01 | full |
| JHU-TAXREASON-2025 | Language Models and Logic Programs for Trustworthy Tax Reasoning (arXiv 2508.21051; accepted to AAAI 2026) | Jurayj, Holzenberger and Van Durme, Johns Hopkins University | academic | https://arxiv.org/abs/2508.21051 | 2025-08-28 | full |
| JOFA-OPRNEWS-2026 | IRS outlines AI risks, Circular 230 duties for tax practitioners | Journal of Accountancy (AICPA) | press | https://www.journalofaccountancy.com/news/2026/jun/irs-outlines-ai-risks-circular-230-duties-for-tax-practitioners/ | 2026-06 | full |
| MAGESH-HALLUC-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362) | Magesh, Surani, Dahl, Suzgun, Manning and Ho (Stanford) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 | full |
| PCRT-AI-2026 | Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax | ICAEW Insights (news item on the seven-body PCRT guidance) | professional-body | https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax | 2026-01-19 | full |
| PCRT-ATT-2026 | Professional bodies issue AI advice to members | Association of Taxation Technicians (ATT) | professional-body | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 2026-01-19 | full |
| SWIDER-2025 | CPAs vs. AI Tax Advisors: Evaluating Reliance Across Advisory Contexts | Lucas A. Swider, University of Oklahoma; American Accounting Association Tax Section meeting paper | academic | https://aaahq.org/portals/0/documents/meetings/2025/ATA/Papers/3.02_Swider.pdf | 2025 | full |
| TAS-AIBLOG-2024 | Is AI Generated Tax Advice Making the Grade? | Taxpayer Advocate Service (IRS) | regulator | https://www.taxpayeradvocate.irs.gov/news/tax-tips/is-ai-generated-tax-advice-making-the-grade/2024/06/ | 2024-06 | full |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax (analysis of Clinco v. Commissioner, T.C. Memo. 2026-16) | Journal of Accountancy (AICPA) | press | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 | full |
| TPB-AI-2026 | TPB releases guidance on responsible AI use for tax practitioners (media release) | Tax Practitioners Board (Australia) | regulator | https://www.tpb.gov.au/tpb-releases-guidance-responsible-ai-use-tax-practitioners | 2026 | full |
| TPB-GS55-2026 | TPB(GS) 55/2026 The use of Artificial Intelligence and the Code of Professional Conduct | Tax Practitioners Board (Australia) | regulator | https://www.tpb.gov.au/tpbgs-552026-use-artificial-intelligence-and-code-professional-conduct | 2026-07-22 | full |
| TR-COCOUNSEL-2025 | Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows | 2025-11-05 | full |
| TR-FOP-2026 | What the 2026 Future of Professionals Report says tax and audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026 | full |
| TREAS-7216-2008 | 26 CFR 301.7216-1, 301.7216-2 and 301.7216-3: disclosure or use of tax return information by tax return preparers | U.S. Treasury (T.D. 9375, as amended 2008), text read from eCFR | regulator | https://www.ecfr.gov/current/title-26/section-301.7216-3 | 2008-01 | full |
| TREAS-C230-2014 | 31 CFR 10.34, Circular 230 standards with respect to tax returns and documents | U.S. Treasury (Circular 230, Rev. 6-2014), text read from eCFR | regulator | https://www.ecfr.gov/current/title-31/section-10.34 | 2014-06 | full |
| WK-FRA-2025 | Wolters Kluwer releases inaugural report, the Future Ready Accountant | Wolters Kluwer | survey | https://www.wolterskluwer.com/en/news/wolters-kluwer-releases-inaugural-report-the-future-ready-accountant | 2025-01-14 | full |

Date notes: TPB-AI-2026 and TR-FOP-2026 and COLUMBIA-TAXBENCH-2026 pages show no publication date, so only the year is given. AICPA-WERFELAPP-2026 is dated from the upload path (June 2026); the article that introduces it is dated 2026-08-31. JOFA-OPRNEWS-2026 is dated by month (the article says the bulletin was posted Wednesday, 2026-06-24). IRS-PUB4557-2024 shows Rev. 5-2024 in the file properties and 6-2024 in the footer. TREAS-7216-2008 and TREAS-C230-2014 were read from the eCFR (access by API) and are dated by the original rule and the Circular 230 revision date.

Reading depth: OPR Alert 2026-19, TPB(GS) 55/2026, the Werfel article and appendices, the *Clinco* article, the AICPA CART and fee articles, the tax software survey (text only; table images not read), Rev. Proc. 2013-14 (sections 1-5), Form 8867 instructions (due diligence sections), Publication 1345 (searched for AI and read for signature, ERO and Responsible Official passages) and Publication 5708 (requirements) were read in substantial part. The PCRT guidance itself was not opened; only the ICAEW and ATT news items about it. The arXiv items were read at abstract level, with the TaxCalcBench body read for method and results. Publication 4557 was read at the safeguards passage only.

## 6. Gaps

- **No independent quality evidence for AI-prepared returns:** no error rates, override rates, parallel-run results, notice rates, inspection findings or disciplinary actions were found for agentic or AI-assisted preparation of 1040, 1041, 1065 or 1120-S returns. All outcome figures are vendor-published, and the one third-party benchmark covers calculation only with mid-2025 models. A refresh of TaxCalcBench with newer models and the release of TaxBench were not found.
- **No evidence on trusts and estates (Form 1041), partnerships (1065) or S corporations (1120-S) specifically.** Black Ore, TR and Werfel's case study are individual-return centred; Basis's 1065 agent and PwC's K-1 agents are in the landscape file but were not read.
- **Wolters Kluwer CCH Axcess Expert AI (Scan, Advisor), Intuit, Drake and other major return-software vendors' AI features:** pages were bot-blocked or not reached; no governance statements from them were read. The AICPA survey's "Use of AI Tools" table is an image and was not read.
- **Not found:** HMRC guidance on agents' use of AI for Self Assessment (one search found only the transformation roadmap material); professional liability insurer AI exclusions or underwriting questions for tax preparers (one search found only design-sector material); state boards of accountancy or NASBA statements; NAEA and NATP statements; any IRS or OPR response to the AICPA's fee query; IRS statements on how Form 8867 or Circular 230 section 10.34 apply to AI-drafted positions.
- **Not opened:** the AICPA's own FAQs on AI in federal tax practice (member-gated); the PCRT guidance document itself; Thomson Reuters's *Future of Professionals* full report; the Blue J/CPA.com outlook report; the Basis and Perplexity items in the landscape file. Choi and Xie's field evidence on AI use by accountants (a search for it was blocked by the exhausted search budget) was not checked.
- **Search budget:** four web searches returned results; a fifth was refused because the shared budget was exhausted. Follow-up searches could target: HMRC and CIOT agent guidance; E&O insurer AI endorsements; state board statements; Tax Court AI certification rules; TaxBench release.
- **Practitioner discussion** (r/taxpros, TaxProTalk) was not reached.
- **Corrections to the landscape file:** (1) the Werfel "20 risks" are the authority register; the preparer register has 15 risks in five layers. (2) The framework appeared in the August 2026 issue (web date 2026-08-31); the CART article (2026-09-23) says "earlier this month". (3) The landscape's mention that the Tax Court judge floated an AI-use certification rule was not found in the Journal of Accountancy analysis; only the court's general caution and the observation that some courts require certifications were read. (4) OPR's alert also cites sections 10.27(a), 10.36, 10.37 and 10.51(a)(15), not only 10.22 and 10.35. (5) The TPB final statement is TPB(GS) 55/2026, issued 2026-07-22.
