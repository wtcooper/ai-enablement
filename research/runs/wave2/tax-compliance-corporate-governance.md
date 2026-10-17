# Module deep dive: tax / compliance-corporate: angle: governance

- **Archetype:** tax
- **Module:** compliance-corporate. Corporate direct-tax compliance in house and at large firms: federal, state and international income tax returns (1120, 5471/8858, state apportionment and SALT income tax), return workpapers and review, tax credits and incentives (R&D credit, Form 6765 Section G), estimated payments and the tax calendar.
- **Angle:** governance. What constrains and measures the work: regulator and tax-authority statements, professional-body guidance, standards, academic studies and working papers, surveys and benchmarks.
- **Prepared:** 2026-10-17 (wave 2)
- **Method note:** Primary documents were fetched with `curl` (text extraction, `pdftotext` for PDFs, the arXiv listing and abstract pages, eCFR point-in-time XML). A private working folder was used. About 40 distinct sources were opened; seven web searches were spent on new directions. Paywalled pages are marked in the Sources table (only the open lead was read). Figures from surveys are given with what they count; vendor-owned surveys are labelled `vendor-published`.

---

## 1. Summary

**What the rules say (October 2026).** No source read here prohibits AI in corporate income tax compliance, and none sets AI-specific requirements for corporate returns. The governing texts are existing duties applied to AI. They were written for practitioners and firms, not for in-house corporate tax departments, and none of the governance documents read addresses in-house teams directly.

- **IRS Office of Professional Responsibility, Alert 2026-19 (24 Jun 2026).** Maps Circular 230 sections 10.22 (due diligence), 10.27 (fees), 10.35 (competence), 10.36 (firm procedures) and 10.37 (written advice), plus IRC 6713 and 7216 (disclosure of return information), onto generative AI. It says practitioners must review AI output carefully and document AI use and verification.
- **UK.** The PCRT bodies (19 Jan 2026) and HMRC's guidance for tax-software developers (28 Jan 2026) take the same line: AI supports, not replaces, human judgment.
- **AICPA and CIMA.** A risk framework by Danny Werfel, former IRS Commissioner, was published in The Tax Adviser (31 Aug 2026), and the AICPA launched a Council on AI Risk in Tax (CART) on 23 Sep 2026 to test and refine it. The framework is notional and states that it is the author's view, not AICPA policy.

**What is specific to corporate compliance.**

- **Form 6765 Section G.** The IRS instructions (revised 12/2025) make Section G (business-component reporting for the research credit) optional for tax years beginning before 2026 and required for tax years beginning after 2025. Filers report by business component at least 80% of total qualified research expenses (QREs) or up to 50 components. Treasury Reg. 1.41-4(d) already requires records "in sufficiently usable form and detail". This is the clearest dated, corporate-specific documentation requirement that AI tooling is aimed at, but the only source describing the AI tooling is a vendor blog.
- **The IRS can already score corporate returns.** TIGTA (19 May 2025) reports that LB&I deployed a Line Anomaly Recommender in March 2021 that analyses Forms 1120 with total assets of $10M to $250M, with human classifiers reviewing the output. TIGTA says LB&I has no specific data on its examination results. GAO (24 Mar 2026) counts 126 active IRS AI use cases. The IRS CEO told staff on 30 Sep 2026 that the agency will be "AI-first".

**What is measured.**

- **Independent accuracy evidence is research-grade and covers individual returns, not corporate ones.**
  - TaxCalcBench (Column Tax, Jul 2025): the best of four 2025 models computed 32.35% of 51 simplified federal Form 1040 test returns correctly under a strict line-by-line match.
  - DeonticBench (Apr 2026): best hard-subset score of 44.4% on SARA Numeric.
  - A Sep 2026 paper found strong models computed straight through injected contradictions and returned the clean-input answer 63% to 76% of the time with no warning.
  - An Oct 2026 paper reports a neuro-symbolic system matching 51 held-out TaxCalcBench returns at 100% cell-level and form-level accuracy, against a best LLM alone at 66%.
- **No error rate, override rate, parallel-run result or inspection finding for AI-prepared corporate returns was found.** The only quantified review controls are illustrative thresholds in a worked case study in the Werfel appendices.
- **Governance is lagging adoption.**
  - Thomson Reuters (2025): 17% of corporate tax departments had specific AI and data policies and 45% had no relevant policy.
  - RSM (21 Jul 2026): 48% apply governance controls before production, 16% only after issues arise, and 36% track model documentation and lineage.
  - Fonoa (indirect-tax leaders, Jun 2026): 57.4% would not be confident defending AI-assisted decisions to a tax authority, and only 12.5% have specific AI targets or KPIs.

**Two most important insights.**
1. **The binding constraint on corporate compliance AI is defensibility, not capability.** Every governing text puts accountability on the human signer and asks for documented verification. The surveys show that most teams have not built the documentation, logging or metrics to show it, and the one measured failure mode (computing through defective inputs) is the kind a deterministic engine or a verification gate catches.
2. **Corporate-specific governance evidence is thin.** The texts and benchmarks are written for practitioners and individual returns. Nothing was found on Forms 5471/8858, state apportionment or the estimated-payment calendar, and nothing measures AI quality on corporate returns.

**Grades.** 0 A, 0 B, 6 C, 10 D (16 candidate use cases). The governance angle rarely surfaces named deployments; the practice angle should carry B and A evidence.

---

## 2. Use cases

```yaml
- id: tax-compliance-corporate-01
  title: AI-assisted import, validation and mapping of source data into the corporate return, with tie-out sampling against source documents
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types: [ data-reporting, transaction-processing ]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Corporate return workpapers start from trial balances, partnership K-1s and other source documents. A misread or misclassified figure can flow into the return without any alert, and the signer is accountable for it."
  solution: "Thomson Reuters describes its goal for ONESOURCE direct tax as agentic AI that does data import, validation and mapping while direct tax professionals keep oversight and focus on judgment-intensive work. The AICPA-published preparer risk register treats incorrect document extraction (W-2, 1099, K-1) as a technical-layer risk and lists independent verification of AI-extracted figures against source documents and spot-check audits of extraction accuracy as controls."
  outcomes:
    - { lever: quality, description: "No extraction accuracy rate, error rate or time saving for corporate return data import was published in the sources read", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: TR-CORPAI-2026 }
  prerequisites:
    - "Source documents in a form the extraction tool can read, and a defined set of source-to-return mappings"
    - "A tie-out sampling plan and an escalation rule for complex or ambiguous documents (Werfel Appendix C risk 3)"
  risks_and_guardrails:
    - "Errors enter the return silently if extraction is not independently verified (Werfel Appendix C risk 3, controls column)"
    - "Circular 230 section 10.22 requires due diligence and verification of the accuracy of facts, citations and calculations produced by AI (OPR Alert 2026-19, Regulatory Framework item 1)"
    - "Treas. Reg. 1.6694-1(e)(1) lets a preparer rely in good faith without verification on information furnished by the taxpayer or another adviser, but not ignore apparent errors or gaps. The sources read do not say how this applies to AI-extracted data."
  human_checkpoints:
    - "Preparer ties out a sample of extracted figures to source documents"
    - "Complex or ambiguous source documents escalate to a person"
  role_evolution: "Preparers move from keying and mapping to verifying extraction and resolving exceptions; the AICPA-published register warns that staff may build skill in operating the tool rather than in the underlying tax law (Werfel risk 'skill erosion')."
  evidence_grade: C
  sources:
    - { ref: TR-CORPAI-2026, title: "AI in corporate tax: 2026 key trends and use cases", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/", date: 2026-07-01, access: full, locator: "section 'Thomson Reuters: From compliance to intelligent compliance', paragraph 1" }
    - { ref: AICPA-WERFEL-2026, title: "AI Risk Register for Tax Preparers (Appendix C)", publisher: AICPA (Danny Werfel), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Appendix C, risk 3 'Incorrect Document Extraction' (PDF p. 27)" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework, item 1 (section 10.22)" }
    - { ref: ECFR-1694-1, title: "26 CFR 1.6694-1, Section 6694 penalties applicable to tax return preparers", publisher: eCFR (Treasury), type: regulator, url: "https://www.ecfr.gov/current/title-26/section-1.6694-1", date: 2026-10-01, access: full, locator: "paragraph (e)(1)" }
  last_reviewed: 2026-10-17
  notes: "The TR blog is vendor content and names no customer or result. Landscape item PWC-MEGNA-2025 (PwC K-1 mapping agents in production, 2025) is the practice-angle evidence for this step; it was not re-read for this file. The Werfel appendices date is from the upload path (2026/06); the PDF metadata shows creation on 2026-05-14 and the main article is dated 2026-08-31."

- id: tax-compliance-corporate-02
  title: Contemporaneous R&D credit evidence capture and Form 6765 Section G business-component reporting
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types: [ document-production, data-reporting ]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "From tax years beginning after 2025, Form 6765 Section G requires qualified research expenses by business component. Credit studies built from engineer interviews and retrospective surveys are slow to produce at that level of detail."
  solution: "Thomson Reuters describes Neo.Tax as connecting to project-management and engineering tools, clustering the data into business components, applying the four-part test, reconciling payroll and general-ledger data to allocate costs, and populating Form 6765 including Section G through its ONESOURCE integration. The IRS instructions set the reporting rule that any such tool must meet."
  outcomes:
    - { lever: speed, description: "Vendor says the tool can speed up recreating prior-year studies; no time or credit figure is published", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: TR-CORPAI-2026 }
  prerequisites:
    - "Project, time and payroll data captured at business-component level as the work happens"
    - "Business-component names or identifiers consistent with the books and records that substantiate the research (Instructions, column 49(c))"
    - "Reconciliation of Section G totals to Section F lines and to payroll and general ledger"
  risks_and_guardrails:
    - "Section G is required for tax years beginning after 2025 unless the filer is a qualified small business claiming the reduced payroll credit, or has controlled-group QREs of $1.5 million or less, average annual gross receipts of $50 million or less for the prior three years, and files an original return (Instructions for Form 6765 (12/2025), Requirements To Complete Section G)"
    - "Filers report by business component a minimum of 80% of total QREs or a maximum of 50 components, in descending QRE order, with the remainder in aggregate (Instructions, How To Complete Section G)"
    - "Treas. Reg. 1.41-4(d) requires records in sufficiently usable form and detail to substantiate the credit"
    - "IRS acceptance of a filed Form 6765 is not acceptance of a statistical sample as adequate substantiation; a sampling plan must be attached (Instructions, Statistical Sampling)"
    - "The 'audit-ready' and 'contemporaneous standard' statements are the vendor's, and they cite the Kyocera case without detail; they were not independently checked"
  human_checkpoints:
    - "R&D tax lead reviews whether each AI-clustered business component qualifies"
    - "Engineers or project owners confirm the project and time data"
    - "Preparer reviews the 80%/Top 50 selection and the aggregate line"
  role_evolution: "The vendor says tax teams get more analytical capacity; the sources read give no staffing figure. The credit study shifts from a periodic interview exercise to ongoing data governance with engineering and finance."
  evidence_grade: C
  sources:
    - { ref: IRS-F6765-INSTR-2025, title: "Instructions for Form 6765 (12/2025)", publisher: Internal Revenue Service, type: regulator, url: "https://www.irs.gov/instructions/i6765", date: 2025-12, access: full, locator: "What's New; Section G sections: Requirements To Complete Section G, How To Complete Section G, Statistical Sampling, Columns 49(a)-(f) and 50-56" }
    - { ref: ECFR-141-4, title: "26 CFR 1.41-4, Qualified research for expenditures paid or incurred in taxable years ending on or after December 31, 2003", publisher: eCFR (Treasury), type: regulator, url: "https://www.ecfr.gov/current/title-26/section-1.41-4", date: 2026-10-01, access: full, locator: "paragraph (d) Recordkeeping for the research credit" }
    - { ref: TR-CORPAI-2026, title: "AI in corporate tax: 2026 key trends and use cases", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/", date: 2026-07-01, access: full, locator: "section 'Neo.Tax: Automating R&D credits under the new IRS rules'" }
  last_reviewed: 2026-10-17
  notes: "The TR blog says Section G was 'optional for tax year 2025' and mandatory 'starting with tax year 2026 returns'; the IRS wording is tax years beginning before or after 2026 and is the one used above. The regulation dates are eCFR point-in-time versions. No named customer or measured result was found; TEI Midyear 2026 had a Tax Lab titled 'Research Credit Automation' (landscape TEI-MIDYEAR-2026, not re-read)."

- id: tax-compliance-corporate-03
  title: Gated rollout and reviewer metrics for AI-drafted return sections
  archetype: tax
  module: compliance-corporate
  function: risk-compliance-legal
  work_types: [ review-assurance ]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Faster AI-enabled preparation can make existing review and sign-off less rigorous in practice while staying unchanged on paper. A reviewer who accepts nearly every AI suggestion adds no independent check."
  solution: "The AICPA-published framework sets out a phased adoption design: research and summarisation only, then AI-suggested deductions and credits, then AI-drafted positions. Each phase has gate conditions and required controls: 100% logging of AI suggestions and preparer decisions (accept, modify, reject), review of override rates by preparer, and tool suspension or scope restriction when error rates cross thresholds. The thresholds are illustrative values in a worked case study for a firm preparing client returns, not a standard."
  outcomes:
    - { lever: quality, description: "No firm applied the thresholds in a published result; the case study sets illustrative gate and suspension values", figure: "none published", measures: "n/a", provenance: independent, source_ref: AICPA-WERFEL-2026 }
  prerequisites:
    - "100% logging of AI suggestions and the preparer's decision on each"
    - "A named AI governance owner with authority to restrict or suspend the tool"
    - "Engagement terms and vendor contract terms in place before Phase 2 (Werfel Appendix D, Steps 6 and 7)"
  risks_and_guardrails:
    - "Control dilution: review processes that do not adapt to volume (Appendix C risk 6)"
    - "Case-study thresholds: expansion from Phase 1 to Phase 2 requires a hallucination rate of 2% or less for 60 consecutive days; Phase 3 requires a Phase 2 error rate of 1% or less for 90 consecutive days; an override rate below 5% for any preparer triggers mandatory review because it signals rubber-stamping (Appendix D, Steps 7 and 8, PDF pp. 45-46)"
    - "Automatic suspension when the error rate exceeds 1% in any 30-day window in Phase 3, and immediate suspension above 2% in any 30-day window (Appendix D, Steps 7 and 8). These are the author's worked-example values."
    - "The signing preparer bears full responsibility; the contract cannot transfer it (Appendix D, Step 6 note)"
  human_checkpoints:
    - "Signing preparer verifies every AI-drafted position before filing"
    - "Novel or uncertain positions escalate to senior review regardless of AI confidence"
    - "Managing partner and general counsel sign off before phase expansion"
  role_evolution: "Reviewers move from approving to genuine independent analysis, and a firm-level governance owner is named. The framework also requires an annual check that staff can still do AI-assisted tasks without the tool."
  evidence_grade: D
  sources:
    - { ref: AICPA-WERFEL-2026, title: "AI Risk Register for Tax Preparers (Appendix C) and Applying the Register, Case Study 2 (Appendix D)", publisher: AICPA (Danny Werfel), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Appendix C risk 6 (PDF p. 28); Appendix D Steps 5, 7, 8 (PDF pp. 41, 45, 46)" }
    - { ref: TAXADVISER-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08-31, access: full, locator: "sections 'AI risk register for tax preparers' and 'Innovate, but responsibly'; author disclaimer" }
    - { ref: AICPA-CART-2026, title: "AICPA, former IRS commissioner to lead initiative on AI in tax", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/", date: 2026-09-23, access: full, locator: "paragraphs 2-4 (CART purpose)" }
  last_reviewed: 2026-10-17
  notes: "Idea. The worked case is a preparer firm using the tool on client returns (examples are individual: W-2, 1099, Schedule C) and is not a corporate-return case. The article states the views are the author's and not AICPA policy. The framework date conflict: the article page is dated 2026-08-31 while the CART release (2026-09-23) says the framework was published 'earlier this month'."

- id: tax-compliance-corporate-04
  title: AI-use log and verification record kept in the return workpapers
  archetype: tax
  module: compliance-corporate
  function: risk-compliance-legal
  work_types: [ review-assurance, document-production ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Tax teams are asked to defend positions and calculations to authorities and auditors. When AI helped produce a figure or a memo, a record of what the tool did and what the person checked may not exist, and then the team cannot show the process behind the output."
  solution: "The IRS Office of Professional Responsibility lists documenting AI usage and verification processes as a best practice and ties section 10.36 compliance to documented procedures. The AICPA Journal of Accountancy firm-policy checklist adds documentation of AI use, review and citation verification. The AICPA-published framework asks for 100% logging of AI suggestions and preparer decisions."
  outcomes:
    - { lever: risk, description: "No published result. Baseline: in a vendor-run survey of indirect-tax leaders, more than half said they would not be confident defending AI-assisted decisions to an authority", figure: "57.4%", measures: "share of 176 surveyed indirect tax leaders who said they would not be confident that AI-assisted decisions would hold up if challenged by a tax authority (indirect tax, adjacent to income tax)", provenance: vendor-published, source_ref: FONOA-2026 }
  prerequisites:
    - "An approved-tool list and a standard log format (tool, version, prompt or task, output used, verifier, date)"
    - "Retention aligned with workpaper retention and with section 7216 confidentiality rules"
  risks_and_guardrails:
    - "Section 10.36 requires firm procedures and documentation to show adherence; failure through willfulness, recklessness or gross incompetence can lead to discipline (OPR Alert 2026-19, item 4)"
    - "Logs of prompts and client data are themselves return information; IRC 6713 and 7216 apply (OPR Alert 2026-19, item 6)"
    - "Only about a third of surveyed indirect-tax organizations run formal human-in-the-loop review of AI outputs (Fonoa 2026)"
  human_checkpoints:
    - "Preparer records what was verified and against which source"
    - "Reviewer confirms the log entry exists for AI-assisted items before sign-off"
  role_evolution: "Preparers and reviewers take on a documentation duty for AI-assisted work; a tax-technology or governance owner maintains the log standard."
  evidence_grade: D
  sources:
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework item 4 (section 10.36); Best Practices for Responsible AI Use" }
    - { ref: TAXCT-CLINCO-2026, title: "A recipe for sanctions: AI-hallucinated citations in tax", publisher: Journal of Accountancy (AICPA), type: press, url: "https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/", date: 2026-09-01, access: full, locator: "sidebar 'Firm policies for responsible AI use in tax practice'" }
    - { ref: AICPA-WERFEL-2026, title: "AI Risk Register for Tax Preparers (Appendix C) and Case Study 2 (Appendix D)", publisher: AICPA (Danny Werfel), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Appendix D Step 5 intensity table, 'Coverage & Sampling' (PDF p. 41)" }
    - { ref: FONOA-2026, title: "State of Indirect Tax in the AI Era 2026", publisher: Fonoa, type: survey, url: "https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026", date: 2026-06-17, access: full, locator: "sections 'Most tax teams can't defend their AI decisions to an authority' and 'Why AI governance matters more than the AI model you choose'" }
    - { ref: DELOITTE-TTT-2026, title: "Riding the wave: A framework to plan for AI (Tax Transformation Trends, AI-enabled Tax Transformation)", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: 2026-07, access: full, locator: "page 8 'A combination of scenarios' (decisions that apply across all four: clear ownership, explainability and audit trails)" }
  last_reviewed: 2026-10-17
  notes: "Idea: no named corporate deployment of AI-use logging was found. The Fonoa figures are indirect-tax and vendor-sponsored. The Deloitte date is the PDF creation date (2026-07-02); the document shows only '2026'."

- id: tax-compliance-corporate-05
  title: Grounded tax-technical research for return positions, with citation verification before reliance
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types: [ research-synthesis, document-production ]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Corporate return teams research technical questions behind positions on the return. General chatbots can invent authorities, and a hallucinated citation in a memo or a filing is a professional-conduct and credibility risk."
  solution: "Thomson Reuters says CoCounsel Tax was embedded in ONESOURCE direct tax solutions in late 2024, grounded in Checkpoint content and returning structured, cited output; the vendor says junior staff can work through more complex questions with cited sources and teams may need outside advisers less often for some of them. Governance sources require the user to verify every cited authority."
  outcomes:
    - { lever: capacity, description: "Vendor says teams may need outside advisers less often for some questions; no figure published", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: TR-CORPAI-2026 }
  prerequisites:
    - "A tool grounded in an authoritative tax library, with source links on every answer"
    - "A written policy on permitted uses and verification of authorities (JofA firm-policy checklist)"
  risks_and_guardrails:
    - "In Clinco v. Commissioner, T.C. Memo. 2026-16, the Tax Court found three of four cited cases likely fabricated by a language model, and the judge said submitting fictitious case law is a recipe for sanctions; the court stopped short of formal sanctions (JofA, Sep 2026)"
    - "Circular 230 section 10.37: cannot rely on AI projections or authorities without independent verification; if the system's logic is opaque, reliance may be unreasonable (OPR Alert 2026-19, item 5)"
    - "AICPA SSTS Section 1.4 (Reliance on Tools): members may use AI but not to supplant professional judgment, and remain responsible for the work product (as summarised in JofA, Sep 2026)"
  human_checkpoints:
    - "Preparer reads each cited authority before relying on it"
    - "Reviewer cross-checks authorities in memos that support return positions"
  role_evolution: "The vendor says junior staff can handle more complex questions; the AICPA-published framework warns that staff may lose the ability to catch AI errors if they learn the tool but not the law."
  evidence_grade: C
  sources:
    - { ref: TR-CORPAI-2026, title: "AI in corporate tax: 2026 key trends and use cases", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/", date: 2026-07-01, access: full, locator: "section 'Thomson Reuters: From compliance to intelligent compliance', paragraph 2" }
    - { ref: TAXCT-CLINCO-2026, title: "A recipe for sanctions: AI-hallucinated citations in tax", publisher: Journal of Accountancy (AICPA), type: press, url: "https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/", date: 2026-09-01, access: full, locator: "sections 'The apparitions in the briefing', 'A recipe for sanctions', 'Circular 230, SSTSs, and professional responsibility'" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework items 1, 3 and 5" }
  last_reviewed: 2026-10-17
  notes: "Clinco involved an individual's Schedule C and a restaurant owner, not a corporate return; it is cited for the verification duty. Research-advisory is the main home for this use case; it is kept here because return positions depend on it. No independent head-to-head benchmark of commercial tax research tools was found (landscape ACC-BENCH)."

- id: tax-compliance-corporate-06
  title: Passing AI efficiency to the client or business unit, and moving corporate compliance fees from hours to outcomes
  archetype: tax
  module: compliance-corporate
  function: service-delivery
  work_types: [ client-interaction, document-production ]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "AI can cut the time needed for return preparation. The OPR alert says billing for manual time not spent may breach the unconscionable-fee rule; the AICPA says the language does not appear to allow value-based pricing."
  solution: "OPR says cost savings should be passed on openly and AI activities disclosed, with reduced costs credited to the client's account. The AICPA has asked the IRS for clarification, saying the language overlooks implementation costs and risks and does not appear to allow value pricing. A Thomson Reuters Institute survey says about a third of tax and audit professionals report that their firms have not yet adapted commercial models."
  outcomes:
    - { lever: cost, description: "No fee or margin outcome published", figure: "none published", measures: "n/a", provenance: independent, source_ref: IRS-OPR-2026 }
  prerequisites:
    - "Engagement terms that describe AI use, the fee basis and how efficiencies are shared"
    - "Time and activity records that show what was done by the tool and by people"
  risks_and_guardrails:
    - "Section 10.27(a): billing for manual labor or time not actually spent, or double billing for AI-assisted tasks, may violate the rule depending on the facts such as a pattern across clients or the size of the differentials (OPR Alert 2026-19, item 2)"
    - "Open question: whether value-based pricing is compatible with the OPR language; the AICPA has sought clarification (The Tax Adviser, 23 Sep 2026)"
  human_checkpoints:
    - "Engagement partner or tax director sets the fee basis and approves disclosure language"
  role_evolution: "Pricing and engagement-letter drafting becomes a partner and general-counsel task; billing hours stop being a proxy for effort."
  evidence_grade: D
  sources:
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework item 2 (section 10.27(a))" }
    - { ref: AICPA-CART-2026, title: "AICPA, former IRS commissioner to lead initiative on AI in tax", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/", date: 2026-09-23, access: full, locator: "penultimate paragraph (OPR guidelines and the AICPA request for clarification)" }
    - { ref: TR-FOP-2026, title: "What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: 2026-07-21, access: full, locator: "paragraph 'Many tax & audit professionals surveyed say client expectations are rising'" }
  last_reviewed: 2026-10-17
  notes: "Idea. The OPR text covers practitioners practising before the IRS; it does not address in-house teams. Landscape BTAX-PRICING-2026 (Bloomberg Tax, Mar 2026, firms exploring value-based fees) was not re-read here."

- id: tax-compliance-corporate-07
  title: Governed enterprise AI environment for return data in place of unapproved public tools
  archetype: tax
  module: compliance-corporate
  function: technology-it
  work_types: [ software-systems, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Preparers use public AI tools with return data. Client or company data can be exposed or retained by the vendor, and under IRC 7216 and 6713 unauthorized disclosure or use of return information carries civil and criminal exposure."
  solution: "Move tax staff to enterprise-approved AI under access controls with vendor terms that bar training on client data. OPR says practitioners must use only secure, enterprise-approved AI for client data. In a KPMG Germany survey of tax departments, company-wide standard tools were reported far more often than tax-specific applications."
  outcomes:
    - { lever: risk, description: "KPMG Germany: company-wide standard AI tools are the most common type in tax departments, ahead of tax-specific applications", figure: "89%", measures: "share reported using company-wide standard AI solutions in tax departments (29% reported specialized tax applications; the release does not state the base or the sample size)", provenance: vendor-published, source_ref: KPMG-DE-2026 }
  prerequisites:
    - "IT approval and data-protection review of the tool (the leading hurdles in the KPMG Germany survey)"
    - "Vendor terms prohibiting use of company data for model training (Werfel Appendix C risk 2)"
    - "An acceptable-use policy and training"
  risks_and_guardrails:
    - "Hurdles named by KPMG Germany respondents: IT approvals 47%, data protection requirements 41%, lack of knowledge about AI applications 41% (percent of respondents; base and sample size not stated)"
    - "Thomson Reuters Institute: more than one-third of surveyed tax and audit professionals admit using unauthorized AI tools"
    - "UK PCRT guidance: entering client data into a publicly available AI model without consent is likely to breach confidentiality"
  human_checkpoints:
    - "Tax director approves the tool list; IT and legal approve data terms"
  role_evolution: "Tax technology staff own the approved-tool list and training; preparers work inside the governed tool."
  evidence_grade: C
  sources:
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework item 6 (IRC 6713 and 7216(a))" }
    - { ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: 2026-05-07, access: full, locator: "paragraphs 'Tax departments are already making extensive use of AI' and 'AI boosts efficiency but requires clear organizational prerequisites'" }
    - { ref: TR-FOP-2026, title: "What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: 2026-07-21, access: full, locator: "'Universal priorities for firm leaders', first bullet" }
    - { ref: PCRT-AI-2026, title: "Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax", publisher: ICAEW (for the seven PCRT bodies), type: professional-body, url: "https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax", date: 2026-01-19, access: full, locator: "'Fundamental principles', Confidentiality" }
    - { ref: AICPA-WERFEL-2026, title: "AI Risk Register for Tax Preparers (Appendix C)", publisher: AICPA (Danny Werfel), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Appendix C, risk 2 'Client Data Leakage'" }
  last_reviewed: 2026-10-17
  notes: "Maturity is set to emerging because the evidence is survey-level only and no named organization is described. The KPMG Germany sample covers German companies and the release does not give a sample size. The TR-FOP figure covers tax and audit professionals, not only corporate tax departments."

- id: tax-compliance-corporate-08
  title: Deterministic tax engine plus language-model layer, with rule-to-logic translation verified by tests
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types: [ software-systems, data-reporting ]
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Language models asked to compute a return directly do not do it reliably, and the IRS expects returns computed exactly. Rule updates (new forms, instructions, new provisions) must still reach the calculation engine."
  solution: "Researchers propose using the model to translate statutes, forms and instructions into executable logic that is checked against test returns, then letting a symbolic solver or the existing deterministic engine compute. The IRS publishes Modernized e-File schemas and business rules (reject criteria) for Forms 1120 and others, which give a deterministic check on what is submitted."
  outcomes:
    - { lever: quality, description: "Best of four 2025 models, calculating a simplified federal Form 1040 directly, got the return fully right in about a third of outputs", figure: "32.35%", measures: "strict 'correct returns' rate on 51 TY2024 federal Form 1040 test cases: the share of model outputs in which every evaluated line matched the expected amount exactly (Gemini 2.5 Pro, best of four models; 4 runs per model per thinking level)", provenance: vendor-published, source_ref: COLUMN-TAXCALCBENCH-2025 }
    - { lever: quality, description: "A neuro-symbolic form-formalization system matched all 51 held-out TaxCalcBench returns, while the strongest language model alone reached 66%", figure: "100% vs 66%", measures: "cell-level and form-level accuracy of the system on 51 held-out TaxCalcBench returns, versus the 'accuracy' of the most advanced LLM alone as the abstract states it (the abstract does not say which unit)", provenance: independent, source_ref: HAN-LAWORDER-2026 }
    - { lever: quality, description: "On a statutory-reasoning benchmark, best frontier models still fail many hard tasks", figure: "44.4%", measures: "best hard-subset score on the SARA Numeric tasks across frontier LLMs and coding models in DeonticBench (6,232 tasks across four domains)", provenance: independent, source_ref: DEONTICBENCH-2026 }
  prerequisites:
    - "Reference returns or test cases per form and rule set, and a maintained rule library"
    - "A route into the IRS MeF XML schemas and business rules, which models could not produce natively in the TaxCalcBench setup"
  risks_and_guardrails:
    - "TaxCalcBench authors sell a deterministic tax engine, and the study is of personal income tax, so its results are adjacent to corporate returns"
    - "TaxCalcBench: models misuse tax tables, make calculation errors and misjudge eligibility; scores fall as the number of runs required to agree rises"
    - "Auditability, not raw accuracy, is argued to be the bottleneck for automated tax calculation (Jurayj, Holzenberger, Van Durme, AAAI 2026 paper)"
  human_checkpoints:
    - "Tax technology staff review generated logic and test coverage"
    - "Preparer reviews the computed return and flagged exceptions"
  role_evolution: "Tax technologists maintain rule libraries and tests; preparers review outputs of an engine they can audit."
  evidence_grade: D
  sources:
    - { ref: COLUMN-TAXCALCBENCH-2025, title: "TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task", publisher: Column Tax (arXiv 2507.16126), type: academic, url: "https://arxiv.org/abs/2507.16126", date: 2025-07-22, access: full, locator: "abstract; full-text section 4.2 'Takeaways' (results table)" }
    - { ref: JHU-TAXREASON-2025, title: "Language Models and Logic Programs for Trustworthy Tax Reasoning", publisher: arXiv preprint (Jurayj, Holzenberger, Van Durme), accepted to AAAI 2026, type: academic, url: "https://arxiv.org/abs/2508.21051", date: 2025-08-28, access: full, locator: "abstract" }
    - { ref: HAN-LAWORDER-2026, title: "Law And Order: Tax Law Autoformalization", publisher: arXiv preprint (Han, Takashima, Wei, Li, Genesereth; 2610.02792), type: academic, url: "https://arxiv.org/abs/2610.02792", date: 2026-10-02, access: full, locator: "abstract" }
    - { ref: DEONTICBENCH-2026, title: "DeonticBench: A Benchmark for Reasoning over Rules", publisher: arXiv preprint (Dou et al.; 2604.04443), type: academic, url: "https://arxiv.org/abs/2604.04443", date: 2026-04-06, access: full, locator: "abstract" }
    - { ref: IRS-MEF-2026, title: "Modernized e-File (MeF) schemas and business rules", publisher: Internal Revenue Service, type: regulator, url: "https://www.irs.gov/e-file-providers/modernized-e-file-mef-schemas-and-business-rules", date: 2026-05-29, access: full, locator: "introductory paragraph and form list (Forms 1120/1120-F/1120-H/1120-L/1120-PC/1120-REIT/1120-RIC/1120-S)" }
  last_reviewed: 2026-10-17
  notes: "Idea with measured research results, all on individual or statutory-reasoning data. Provenance: the TaxCalcBench figure is vendor-published (its authors work at a vendor of a deterministic engine). The Han et al. authors built the system they measured; 'independent' here means a third-party academic source, not a replication. Author affiliations were not shown on the abstract pages and are not asserted. The TaxCalcBench publication date is the arXiv submission date. TaxBench (Columbia DAP Lab, in development, 500+ rules and 50+ scenarios for tax year 2025, field-by-field comparison with a reviewed reference return) may later give a second benchmark; the page is undated."

- id: tax-compliance-corporate-09
  title: Input-verification gate that flags missing or contradictory facts before a model computes a tax result
  archetype: tax
  module: compliance-corporate
  function: risk-compliance-legal
  work_types: [ review-assurance, data-reporting ]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Real inputs are often incomplete or internally inconsistent. A model that computes straight through a contradiction returns a confident number with no sign that anything is wrong."
  solution: "Researchers add one extra model call that verifies the input for conflicts before the solve, and abstain when it reports one. The same model flagged most contradictions when asked to verify rather than to solve."
  outcomes:
    - { lever: quality, description: "Strong models computed through injected contradictions and returned the clean-input answer without any signal of the conflict", figure: "63% to 76%", measures: "share of injected-contradiction cases in which the strongest models (of six studied) returned the clean-input answer, on SARA-derived tax cases", provenance: independent, source_ref: SADOWSKI-VERIFY-2026 }
    - { lever: quality, description: "The gate recovered most of the missed abstentions at a limited cost to clean-case accuracy", figure: "at most about 5 percentage points", measures: "loss in clean-input accuracy across all six models from adding the verification call, as the abstract reports", provenance: independent, source_ref: SADOWSKI-VERIFY-2026 }
  prerequisites:
    - "Structured case facts and a place in the workflow to hold the case for a person when a conflict is flagged"
  risks_and_guardrails:
    - "Evidence is from statutory benchmark cases (SARA, individual tax), not corporate returns"
    - "The abstract says high accuracy on well-formed inputs is an incomplete measure of reliability"
  human_checkpoints:
    - "A person resolves every case where the gate abstains"
  role_evolution: "Preparers handle flagged input defects instead of finding them late in review."
  evidence_grade: D
  sources:
    - { ref: SADOWSKI-VERIFY-2026, title: "Solving versus Verifying: Catching Contradictions in Tax Reasoning Systems", publisher: arXiv preprint (Sadowski, Chudziak; 2609.05928), type: academic, url: "https://arxiv.org/abs/2609.05928", date: 2026-09-05, access: full, locator: "abstract" }
  last_reviewed: 2026-10-17
  notes: "Idea. Preprint, not peer reviewed as far as the page shows. Author affiliations were not shown on the abstract page and are not asserted. Only the abstract was read."

- id: tax-compliance-corporate-10
  title: Pre-filing anomaly screening of the return, informed by how authorities score returns
  archetype: tax
  module: compliance-corporate
  function: risk-compliance-legal
  work_types: [ review-assurance, data-reporting ]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: "The IRS already uses machine-learning models to score returns for examination. TIGTA describes one that produces risk scores for each line item of Forms 1120 within a defined asset band. Preparers get no equivalent signal before filing."
  solution: "Deloitte describes AI agents flagging common anomalies in source data and account reconciliations for human review as a detective control, and describes a scenario in which tax authorities' AI progress outpaces the company's, with heightened audit and dispute exposure. Taxpayer-side line-level screening modelled on authority scoring is not documented in the sources read."
  outcomes:
    - { lever: risk, description: "No published taxpayer-side result", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: DELOITTE-TTT-2026 }
  prerequisites:
    - "Return data at line level and a history of notices and exam adjustments to calibrate against"
  risks_and_guardrails:
    - "TIGTA: LB&I deployed the Line Anomaly Recommender in March 2021 to analyse Forms 1120 with total assets between $10 million and up to $250 million; it is unsupervised, outputs are reviewed by human classifiers, and LB&I has no specific data on its examination results (TIGTA 2025-308-022, p. 7)"
    - "A prior TIGTA audit found nearly 50% of Form 1120 returns closed in the older discriminant-analysis workstream (FY2015 to FY2018) were closed with no change (TIGTA 2025-308-022, Appendix IV, p. 20)"
    - "GAO: IRS inventory showed 126 active AI use cases as of June 2025, 65 of them withheld as sensitive or exempt research (GAO-26-107522, Highlights)"
    - "Authority model details are largely redacted; a taxpayer-side screen cannot replicate them"
  human_checkpoints:
    - "Reviewer decides whether a flagged item is an error, a reportable position or a documentation gap"
  role_evolution: "Reviewers get an additional machine-generated review list; the Deloitte scenario view says human roles shift toward judgment and dispute resolution."
  evidence_grade: D
  sources:
    - { ref: TIGTA-2025, title: "The IRS Could Leverage Examination Results in Artificial Intelligence Examination Case Selection Models and Improve Processes to Evaluate Performance (2025-308-022)", publisher: Treasury Inspector General for Tax Administration, type: regulator, url: "https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf", date: 2025-05-19, access: full, locator: "Results of Review, LAR discussion (p. 7); Appendix IV (p. 20)" }
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: U.S. Government Accountability Office, type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: 2026-03-24, access: full, locator: "What GAO Found; Recommendations" }
    - { ref: DELOITTE-TTT-2026, title: "Riding the wave: A framework to plan for AI", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: 2026-07, access: full, locator: "framework diagram (p. 3) and Scenario 1 text (p. 4)" }
    - { ref: IRS-AIFIRST-2026, title: "Tax chief pushes 'AI-first IRS' to get more out of agency's workforce", publisher: Nextgov/FCW, type: press, url: "https://www.nextgov.com/artificial-intelligence/2026/10/tax-chief-pushes-ai-first-irs-get-more-out-agencys-workforce/416389/", date: 2026-10-02, access: full, locator: "paragraphs 1-6" }
  last_reviewed: 2026-10-17
  notes: "Idea. The GAO publication date (2026-03-24) is taken from the landscape file; the GAO page text read via the text mirror did not show a publication date. The Line Anomaly Recommender was one of three IRS projects in the Treasury's August 2022 AI inventory per TIGTA. The IRS CEO said on 30 Sep 2026 that the agency aims for a mid-90s compliance rate in five years versus about 85% now (Nextgov). Not an evidenced taxpayer-side practice."

- id: tax-compliance-corporate-11
  title: Writing AI-made data corrections back to the source system of record to keep an audit-ready trail
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types: [ data-reporting, review-assurance ]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "When an AI agent corrects or reclassifies data on its way into the tax return, the correction can exist only in the tax tool. The source system then disagrees with the filed return and the audit trail breaks."
  solution: "Deloitte's scenario framework says agentic corrections to source data will need to be stored back to the relevant system of record to maintain an audit-ready tax posture, and recommends investment in flexible integrations and an audit trail that supports results from automated processes in the formats less advanced authorities require."
  outcomes:
    - { lever: risk, description: "none published", figure: "none published", measures: "n/a", provenance: self-reported, source_ref: DELOITTE-TTT-2026 }
  prerequisites:
    - "Integration between the tax platform and ERP or the general ledger, and a data owner for each source"
  risks_and_guardrails:
    - "Deloitte: accountability becomes harder to trace in AI-driven processes (Scenario 2 text)"
    - "The Werfel register lists lack of auditability and agentic AI risk (irreversible actions before a human can intervene) for authorities; the preparer register lists control dilution"
  human_checkpoints:
    - "Data owner approves each write-back or reviews a log of them"
  role_evolution: "Tax functions take part earlier in enterprise governance of AI-driven finance processes (Deloitte Scenario 2)."
  evidence_grade: D
  sources:
    - { ref: DELOITTE-TTT-2026, title: "Riding the wave: A framework to plan for AI", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: 2026-07, access: full, locator: "Scenario 2, p. 5" }
    - { ref: TAXADVISER-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08-31, access: full, locator: "Figure 1 risks 14 and 18" }
  last_reviewed: 2026-10-17
  notes: "Idea from a consultancy scenario paper; no deployment found."

- id: tax-compliance-corporate-12
  title: Monitoring of form, instruction and rule changes with change reports mapped to the compliance calendar
  archetype: tax
  module: compliance-corporate
  function: risk-compliance-legal
  work_types: [ coordination-scheduling, research-synthesis ]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: "Forms and instructions change frequently. The Form 6765 instructions were revised in 12/2025 and reference new section 174A treatment from Public Law 119-21. Missed changes become return errors."
  solution: "Thomson Reuters describes Orbitax's Tax Flows as tracking regulatory changes across jurisdictions and proactively distributing comparison reports to stakeholders. HMRC expects tax software that uses generative AI to apply continuous monitoring, version control and timely updating of code and data sources as law, case law and guidance change."
  outcomes:
    - { lever: risk, description: "No published detection or error figure", figure: "none published", measures: "n/a", provenance: vendor-published, source_ref: TR-CORPAI-2026 }
  prerequisites:
    - "A defined list of forms, jurisdictions and rules in scope, and an owner for each alert"
  risks_and_guardrails:
    - "HMRC expectation applies to software developers serving UK customers, not to corporate tax departments"
    - "OPR lists staying updated on relevant federal and state laws and guidance as a best practice"
  human_checkpoints:
    - "Tax technical lead confirms which changes affect the return process before updating templates"
  role_evolution: "Technical staff review change reports instead of searching sources by hand."
  evidence_grade: C
  sources:
    - { ref: TR-CORPAI-2026, title: "AI in corporate tax: 2026 key trends and use cases", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/", date: 2026-07-01, access: full, locator: "section 'Orbitax: International tax intelligence and the Pillar Two deadline', 'Tax Flows'" }
    - { ref: HMRC-GENAI-SW-2026, title: "Guidelines for using generative artificial intelligence if you're a software developer", publisher: HM Revenue & Customs (GOV.UK), type: regulator, url: "https://www.gov.uk/guidance/guidelines-for-using-generative-artificial-intelligence-if-youre-a-software-developer", date: 2026-01-28, access: full, locator: "section 'Using reliable source data'" }
    - { ref: IRS-F6765-INSTR-2025, title: "Instructions for Form 6765 (12/2025)", publisher: Internal Revenue Service, type: regulator, url: "https://www.irs.gov/instructions/i6765", date: 2025-12, access: full, locator: "What's New (Revised 12/2025; section 174A paragraph)" }
  last_reviewed: 2026-10-17
  notes: "Tax Flows is part of Orbitax's international tax product; it is cited here as a pattern, not as a corporate-return deployment. No named customer."

- id: tax-compliance-corporate-13
  title: Quality and ROI instrumentation for AI-assisted compliance workflows
  archetype: tax
  module: compliance-corporate
  function: finance-accounting
  work_types: [ data-reporting ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Leadership asks tax functions to adopt AI but few measure what it does. Without baselines for cycle time, review rework, errors found, notices and penalties, the team cannot show value or catch quality decline."
  solution: "Thomson Reuters suggests tracking baselines for cycle time, documentation hours and audit exposure. The AICPA-published framework adds hallucination rate, override rate by preparer, audit disallowances on AI-assisted returns and client disputes citing AI as monitored indicators. Fonoa's survey links accountability structures with faster workload reduction."
  outcomes:
    - { lever: quality, description: "Small share of surveyed indirect-tax functions have AI targets or KPIs", figure: "12.5%", measures: "share of 176 surveyed indirect tax leaders whose functions have specific targets or KPIs for AI (indirect tax, adjacent)", provenance: vendor-published, source_ref: FONOA-2026 }
    - { lever: cost, description: "Few organizations measure return on GenAI investment", figure: "20%", measures: "share of organizations measuring return on investment, in a Thomson Reuters Institute 2025 professional-services report as quoted by TR (covers professional services broadly, not only tax)", provenance: vendor-published, source_ref: TR-GENAI-2025 }
    - { lever: risk, description: "Controls are applied before production by under half of respondents", figure: "48%", measures: "share of RSM Middle Market AI Survey 2026 respondents who said governance controls are applied before production (16% only after issues arise, 7% inconsistently; sample size not stated on the page)", provenance: vendor-published, source_ref: RSM-AISURVEY-2026 }
  prerequisites:
    - "Baselines before rollout; agreed definitions of an error, an override and a rework cycle"
  risks_and_guardrails:
    - "Metrics can be gamed: an override rate below 5% per preparer is treated as a sign of rubber-stamping in the case study (Werfel Appendix D, Step 8)"
    - "Only 36% of RSM respondents cite model documentation and lineage tracking as a current practice"
  human_checkpoints:
    - "Tax director reviews indicators on a set cadence and decides on scope restriction"
  role_evolution: "A tax operations or tax technology role owns measurement and reporting."
  evidence_grade: C
  sources:
    - { ref: FONOA-2026, title: "State of Indirect Tax in the AI Era 2026", publisher: Fonoa, type: survey, url: "https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026", date: 2026-06-17, access: full, locator: "section 'The AI mandate is real, but what leaders want is unclear'" }
    - { ref: TR-GENAI-2025, title: "5 GenAI tensions corporate tax departments should address", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address-tri/", date: 2025-06-24, access: full, locator: "Tension point 3: the ROI measurement gap" }
    - { ref: RSM-AISURVEY-2026, title: "AI is working in tax. Scaling it is the hard part (RSM Middle Market AI Survey 2026)", publisher: RSM US, type: survey, url: "https://rsmus.com/insights/services/business-tax/ai-is-working-in-tax-scaling-it-is-the-hard-part.html", date: 2026-07-21, access: full, locator: "section 'AI governance in tax: From policy to practice'" }
    - { ref: TR-CORPAI-2026, title: "AI in corporate tax: 2026 key trends and use cases", publisher: Thomson Reuters Tax & Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/", date: 2026-07-01, access: full, locator: "'Four steps to build AI momentum in corporate tax', step 3" }
    - { ref: AICPA-WERFEL-2026, title: "Applying the AI Risk Register for Tax Preparers, Case Study 2 (Appendix D)", publisher: AICPA (Danny Werfel), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Step 8 'Indicators and Thresholds' (PDF p. 46)" }
  last_reviewed: 2026-10-17
  notes: "All three survey figures come from vendor or firm sponsors with undisclosed or partial samples. The TR 20% figure is quoted from TR's own summary of a broader report; the corporate tax subset was not shown for that metric."

- id: tax-compliance-corporate-14
  title: Vendor accuracy terms and model-change revalidation before each filing season
  archetype: tax
  module: compliance-corporate
  function: procurement-supply-chain
  work_types: [ review-assurance, software-systems ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Tax software vendors update models and content during the year. A silent change in behaviour (drift) can alter outputs without any single failure that triggers review."
  solution: "The AICPA-published framework lists illustrative contract terms for AI tax tools: an accuracy SLA with a financial remedy, explicit liability allocation for positions disallowed on audit, 60 days' notice before material model, training-data or citation-method changes with a revalidation window, independent audit rights on 30 days' notice, and 24-hour notice of systematic output errors. HMRC expects developers to apply continuous monitoring and version control."
  outcomes:
    - { lever: risk, description: "none published; no vendor contract adopting these terms was found", figure: "none published", measures: "n/a", provenance: independent, source_ref: AICPA-WERFEL-2026 }
  prerequisites:
    - "Procurement and legal involvement in tax-technology contracts; a regression test set per form"
  risks_and_guardrails:
    - "A vendor contract cannot transfer the signing preparer's professional responsibility (Werfel Appendix D, Step 6 note)"
    - "Authority register risk 2 (drift) and risk 5 (policy drift) describe the same failure for authority tools"
    - "The terms are illustrative from a worked example, not a market norm"
  human_checkpoints:
    - "Tax director and procurement approve contracts; tax technology staff revalidate after each notified change"
  role_evolution: "Tax technology staff run acceptance tests on vendor releases before the filing season."
  evidence_grade: D
  sources:
    - { ref: AICPA-WERFEL-2026, title: "Applying the AI Risk Register for Tax Preparers, Case Study 2 (Appendix D)", publisher: AICPA (Danny Werfel), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Step 6 'Contractual Requirements' (PDF p. 44); Appendix A risk 2 (PDF p. 2)" }
    - { ref: HMRC-GENAI-SW-2026, title: "Guidelines for using generative artificial intelligence if you're a software developer", publisher: HM Revenue & Customs (GOV.UK), type: regulator, url: "https://www.gov.uk/guidance/guidelines-for-using-generative-artificial-intelligence-if-youre-a-software-developer", date: 2026-01-28, access: full, locator: "'Using reliable source data', last paragraph" }
    - { ref: NIST-AI600-2024, title: "Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1)", publisher: NIST, type: standard-setter, url: "https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence", date: 2024-07-26, access: full, locator: "abstract (voluntary cross-sectoral profile of AI RMF 1.0; landing page only)" }
  last_reviewed: 2026-10-17
  notes: "Idea. NIST AI 600-1 is a voluntary, cross-sector profile; only its landing page was read."

- id: tax-compliance-corporate-15
  title: Keeping unaided competence and early-career development while AI prepares first drafts
  archetype: tax
  module: compliance-corporate
  function: people-hr
  work_types: [ expert-judgment, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "If AI does the first draft of routine compliance work, juniors may not build the judgment needed to review it, and the team may lose the ability to work without the tool or catch its errors."
  solution: "The AICPA-published framework gates expansion on an annual capability assessment showing that staff can still do AI-assisted tasks without the tool. Thomson Reuters Institute's paper says firms should ensure supervision before automation erodes junior development. RSM respondents expect hybrid and AI-orchestration roles."
  outcomes:
    - { lever: capacity, description: "Survey expectations about role change, not outcomes", figure: "48%", measures: "share of RSM respondents qualified to answer tax-specific questions who expect the focus of work to shift from compliance execution to strategic planning and business partnership (44% expect AI orchestration roles, 43% hybrid roles); sample size not stated", provenance: vendor-published, source_ref: RSM-AISURVEY-2026 }
  prerequisites:
    - "Structured rotation of juniors through review and exception handling; unaided exercises"
  risks_and_guardrails:
    - "Skill erosion and institutional knowledge loss are listed as workforce risks 13 to 15 in the preparer register (Figure 3)"
    - "Sala argues AI cannot bear regulatory, ethical or financial culpability and so will not shrink corporate tax teams much; KPMG Germany respondents mostly expect stable headcount (58% domestic, 72% abroad)"
  human_checkpoints:
    - "Managers run the annual unaided capability check and sign off"
  role_evolution: "Preparers shift toward oversight, interpretation and exception handling (Deloitte Scenario 4 'preparation to oversight, interpretation, policy interaction, and dispute resolution'). RSM respondents expect hybrid roles."
  evidence_grade: D
  sources:
    - { ref: TAXADVISER-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08-31, access: full, locator: "Figure 3, 'Workforce and strategic' risks" }
    - { ref: AICPA-WERFEL-2026, title: "Applying the AI Risk Register for Tax Preparers, Case Study 2 (Appendix D)", publisher: AICPA (Danny Werfel), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Step 7 Phase 3 gate conditions (PDF p. 45)" }
    - { ref: TR-FOP-2026, title: "What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: 2026-07-21, access: full, locator: "'Universal priorities', fourth bullet" }
    - { ref: RSM-AISURVEY-2026, title: "AI is working in tax. Scaling it is the hard part (RSM Middle Market AI Survey 2026)", publisher: RSM US, type: survey, url: "https://rsmus.com/insights/services/business-tax/ai-is-working-in-tax-scaling-it-is-the-hard-part.html", date: 2026-07-21, access: full, locator: "section 'Tax AI and the workforce: Defining where judgment matters'" }
    - { ref: SALA-TAXNOTES-2026, title: "AI Won't Shrink Corporate Tax Teams Much. Here's Why.", publisher: Tax Notes State (via TaxProf Blog), type: academic, url: "https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/", date: 2026-07-20, access: full, locator: "abstract as posted on TaxProf Blog (article text not read)" }
    - { ref: KPMG-DE-2026, title: "Tax departments are increasingly turning to artificial intelligence", publisher: KPMG Germany, type: survey, url: "https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html", date: 2026-05-07, access: full, locator: "first paragraph (headcount expectations)" }
    - { ref: DELOITTE-TTT-2026, title: "Riding the wave: A framework to plan for AI", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: 2026-07, access: full, locator: "Scenario 4, p. 7" }
  last_reviewed: 2026-10-17
  notes: "Idea. The percentages in the outcomes entry are expectations from a survey of mid-market organisations, not measured workforce changes."

- id: tax-compliance-corporate-16
  title: In-house requirement that outside tax providers disclose AI use and pass on efficiency
  archetype: tax
  module: compliance-corporate
  function: procurement-supply-chain
  work_types: [ client-interaction, review-assurance ]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: "Corporate tax departments outsource return preparation and review to firms. They want providers to use generative AI, but many do not know whether their providers do, so they cannot assess quality, risk or fees."
  solution: "In-house teams ask outside providers to state what AI is used, how output is verified and how fees reflect it. OPR says practitioners should disclose AI activities and credit cost reductions. The AICPA-published register lists lack of transparency and client-trust risks and recommends engagement-letter language on AI use and responsibility."
  outcomes:
    - { lever: risk, description: "Baseline of the transparency gap", figure: "59%", measures: "share of surveyed business tax departments that are not sure whether their tax service providers use GenAI (77% want their providers to use it); survey is the Thomson Reuters 2025 Generative AI in Professional Services Report as summarised by TR, sample not stated in the summary", provenance: vendor-published, source_ref: TR-GENAI-2025 }
  prerequisites:
    - "Procurement language and a periodic provider assessment"
  risks_and_guardrails:
    - "Disclosure may reveal provider methods or conflict with provider confidentiality"
    - "Fee guidance under section 10.27 is contested between OPR and the AICPA (see tax-compliance-corporate-06)"
  human_checkpoints:
    - "Tax director reviews provider disclosures at engagement renewal"
  role_evolution: "Tax directors act as informed buyers of AI-enabled services."
  evidence_grade: D
  sources:
    - { ref: TR-GENAI-2025, title: "5 GenAI tensions corporate tax departments should address", publisher: Thomson Reuters Tax & Accounting, type: survey, url: "https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address-tri/", date: 2025-06-24, access: full, locator: "Tension point 1: the vendor transparency gap" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework item 2" }
    - { ref: PCRT-AI-2026, title: "Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax", publisher: ICAEW (for the seven PCRT bodies), type: professional-body, url: "https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax", date: 2026-01-19, access: full, locator: "'Fundamental principles', Integrity" }
    - { ref: AICPA-WERFEL-2026, title: "AI Risk Register for Tax Preparers (Appendix C)", publisher: AICPA (Danny Werfel), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-06, access: full, locator: "Appendix C, risks 8 to 12 (legal and business layers)" }
  last_reviewed: 2026-10-17
  notes: "Idea: no deployment of such a provider-disclosure requirement was found. The survey figure is a gap measure, not an outcome."
```

---

## 3. Module notes

### Processes and key steps (with work types)

| Step | Work types | Governance sources found |
|---|---|---|
| Data collection and mapping: trial balance, K-1s, foreign financials into the return system | `data-reporting`, `transaction-processing` | Werfel Appendix C risk 3; OPR section 10.22 |
| Federal return (1120) workpapers and computation | `document-production`, `data-reporting` | TaxCalcBench and related benchmarks (individual returns); IRS MeF schemas and business rules for 1120 |
| Tax-technical research behind positions | `research-synthesis`, `expert-judgment` | Clinco; OPR sections 10.35 and 10.37; AICPA SSTS 1.4 (via JofA) |
| Credits and incentives: R&D credit, Form 6765 Section G | `document-production`, `data-reporting` | IRS Form 6765 instructions (12/2025); Treas. Reg. 1.41-4(d) |
| Review and sign-off | `review-assurance` | Werfel Appendix C risk 6 and Appendix D; OPR section 10.36 |
| International forms (5471/8858), state apportionment and SALT income tax, estimated payments and the tax calendar | `data-reporting`, `coordination-scheduling` | None found for AI governance in these steps (see Gaps) |
| E-filing and post-filing | `transaction-processing` | IRS MeF page; notices and exams are routed to controversy |

### Common pain points (governance angle)

- **Contemporaneous documentation.** Section G (tax years beginning after 2025) needs business-component detail that interview-based studies struggle to supply (IRS-F6765-INSTR-2025; the TR-CORPAI-2026 blog is the vendor's reading).
- **Under-resourcing and reactive work.** 58% of surveyed corporate tax departments say they are under-resourced, up from 51% a year earlier; the base is 288 tax departments worldwide (TR-CORPTAX-2025).
- **Unclear ownership and unmeasured value.** Fonoa (indirect tax): 12.5% have AI targets or KPIs. RSM: 48% apply governance controls before production. TR: 45% of corporate tax departments had no relevant AI policy (2025).
- **Data quality.** RSM: data quality, availability and lineage issues rank as the single greatest inhibitor to AI deployment (34% of respondents) and the most cited cause of stalled pilots (53% of respondents who ran pilots).

### Metrics and benchmarks (what each measures)

| Metric | Source | What it counts | Provenance |
|---|---|---|---|
| 32.35% strict-correct (best of four models) | COLUMN-TAXCALCBENCH-2025 | Model outputs on 51 TY2024 federal Form 1040 test cases where every evaluated line matched exactly; lenient (within $5) 51.96%; line-level 81.22% | vendor-published (Column Tax) |
| 44.4% hard-subset | DEONTICBENCH-2026 | Best frontier-model score on SARA Numeric tasks | independent |
| 63% to 76% | SADOWSKI-VERIFY-2026 | Share of injected-contradiction cases where the strongest models returned the clean-input answer | independent |
| 100% vs 66% | HAN-LAWORDER-2026 | Neuro-symbolic system vs strongest LLM alone on 51 held-out TaxCalcBench returns (unit of the 66% not stated in the abstract) | independent (own system) |
| 71% use AI tools; 66% of users see noticeable time savings | KPMG-DE-2026 | Surveyed German companies' tax departments (sample size not stated) | vendor-published |
| 67% not using GenAI; 58% under-resourced; 31% vs 56% penalised | TR-CORPTAX-2025 | 288 corporate tax departments. 31% of those spending over half their time on proactive work incurred penalties against 56% of those spending over half reactive | vendor-published |
| 17% specific AI policy; 21% covered by general technology policy; 45% none | TR-GENAI-2025 | Corporate tax departments, 2025 report (sample not stated in summary) | vendor-published |
| 51% moderate or limited pilot success; 98% have risk controls; 36% track model documentation and lineage | RSM-AISURVEY-2026 | RSM Middle Market AI Survey 2026 respondents (sample not stated) | vendor-published |
| 65% of AICPA preparers use AI in tax research; 16% have no plans (24.3% a year earlier) | AICPA-TAXSW-2026 | 1,808 AICPA members who prepared 2025 returns for a fee (individual-heavy sample) | independent (professional body) |
| 126 active IRS AI use cases; 25%+ of inventory entries lacked benefit information | GAO-2026 | IRS inventory June 2025 | independent |
| About 50% of Form 1120 returns closed no-change in the earlier DAS workstream, FY2015 to FY2018 | TIGTA-2025 (Appendix IV, citing a prior TIGTA report) | Returns closed in that workstream | independent |

No parallel-run result, override rate, review-rework rate or inspection finding for AI-prepared corporate returns was found. Werfel's thresholds (hallucination rate 2% or less for 60 days; Phase 2 error rate 1% or less for 90 days; override rate below 5% triggers review) are illustrative values in a worked example.

### Guardrails and regulatory points

- **Circular 230 (OPR Alert 2026-19, 24 Jun 2026):** sections 10.22, 10.27(a), 10.35, 10.36, 10.37, with IRC 6713 and 7216 and Circular 230 section 10.51(a)(15) on unauthorized use or disclosure. The alert covers practitioners; the texts read do not address in-house corporate tax departments directly.
- **Return preparer penalty regulation:** Treas. Reg. 1.6694-1(e) allows good-faith reliance on information from the taxpayer or another adviser without independent verification, but not ignoring apparent errors or omissions, and requires appropriate inquiries into facts a Code section makes a condition of a credit. How it applies to AI output is not addressed in the sources read.
- **Research credit:** Form 6765 Section G required for tax years beginning after 2025 (exceptions listed in use case 02); records under Treas. Reg. 1.41-4(d); a statistical sampling plan under Rev. Proc. 2011-42 must be attached if sampling is used.
- **Professional standards:** AICPA SSTS Section 1.4, Reliance on Tools (summarised by JofA); UK PCRT AI guidance (19 Jan 2026); HMRC guidelines for developers of AI-enabled tax software (28 Jan 2026); NIST AI 600-1 (voluntary generative-AI profile, 26 Jul 2024).
- **Courts:** Clinco v. Commissioner, T.C. Memo. 2026-16: three of four cited cases appeared fabricated by an AI model; no formal sanction; the judge said the court "wants to proceed gingerly" on guardrails. IRC 6673 is the provision the judge named as the main available penalty (Bloomberg Tax, 20 Mar 2026, lead only).
- **What the authority sees:** the IRS IRM 10.24.1 update (10 Feb 2026) bars IRS staff from entering sensitive taxpayer data into generative tools or using them for binding determinations (Tax Notes via TaxProf Blog). TIGTA records that LB&I scores Forms 1120 in a defined asset band with an unsupervised model plus human classifiers.

### Frontier signals (dated and sourced)

| Date | Signal | Source |
|---|---|---|
| 2026-01-28 | HMRC publishes expectations for generative-AI tax software: transparency, reliable source data, human oversight, security, ethics | HMRC-GENAI-SW-2026 |
| 2026-06-24 | IRS OPR issues first AI alert for Circular 230 practice | IRS-OPR-2026 |
| 2026-08-31 | Werfel risk framework published in The Tax Adviser | TAXADVISER-WERFEL-2026 |
| 2026-09-23 | AICPA launches the Council on AI Risk in Tax; AICPA asks IRS to clarify OPR fee language | AICPA-CART-2026 |
| 2026-09-05 and 2026-10-02 | Research on input-defect gates and verified formalization of tax forms | SADOWSKI-VERIFY-2026; HAN-LAWORDER-2026 |
| 2026-10-02 (reported) | IRS CEO describes an "AI-first IRS"; headcount flat at about 74,000; aim of a mid-90s compliance rate in five years | IRS-AIFIRST-2026 |
| Tax years beginning after 2025 | Form 6765 Section G becomes required | IRS-F6765-INSTR-2025 |

### Workforce and role effects

- RSM respondents who answered tax-specific questions: 98% expect AI to change the nature of work in two to three years; 48% expect a shift from compliance execution to strategic planning, 44% AI orchestration roles, 43% hybrid roles (RSM-AISURVEY-2026).
- KPMG Germany: 58% expect stable domestic headcount and 72% stable foreign headcount (KPMG-DE-2026).
- TR Institute: more than one quarter would not accept a job at a firm without professional-grade AI; almost one in three would consider leaving if AI expectations are unmet in two years (TR-FOP-2026).
- Sala: tax preparation (moving data into forms) is already automated; tax practice involves engagement with authorities, auditors and executives, and AI cannot carry culpability, so teams will not shrink much (SALA-TAXNOTES-2026, abstract only).
- Werfel: skill erosion, vendor dependence and institutional knowledge loss are workforce risks of the preparer register (TAXADVISER-WERFEL-2026, Figure 3).

### Objections and concerns practitioners raise

- Fee rules may not allow value pricing and overlook implementation cost and risk (AICPA on OPR guidance, AICPA-CART-2026).
- Hallucinated authorities and confidential-data leakage (OPR, Clinco, PCRT).
- Rubber-stamping: reviewers who accept almost every AI suggestion (Werfel Appendix D, Step 8).
- Unclear owner and unmeasured value (Fonoa, TR-GENAI-2025, RSM).
- Models compute through contradictory inputs without warning (SADOWSKI-VERIFY-2026).
- Researchers on tax calculation argue auditability matters more than raw accuracy (JHU-TAXREASON-2025).

### Interview probes for an advisor

1. Who signs the corporate return and the Form 6765, and what do they need to see (logs, tie-outs, source links) to be willing to rely on an AI-prepared section?
2. Do you capture R&D project, time and payroll data at business-component level today, and who reconciles it to the general ledger for Section G?
3. Where is AI use recorded in your workpapers, and could you show an examiner or auditor what the tool did and what a person checked on a given line?
4. What does your outside return provider tell you about its AI use, and has that changed fees or review?
5. Which AI tools may staff use with return data, and how do you find out about use outside that list?

---

## 4. Routed to other modules

| Item | Target module |
|---|---|
| GloBE Information Return XML, first filing 30 Jun 2026, Orbitax XatBot modes (from TR-CORPAI-2026) | international-pillar-two |
| FASB ASU 2023-09 disclosure workload; Bloomberg Tax Provision AI features | provision |
| Fonoa indirect-tax survey (92% use AI; 57.4% not confident; 12.5% KPIs) beyond the cross-cutting lessons used above | indirect-tax |
| Clinco, Tax Court guardrails, Khoja v. Commissioner (IRS motion citing a non-existent case), IRC 6673 | controversy |
| TIGTA and GAO findings on IRS AI, IRS amended-return AI (12 to 16 weeks down to under three days per IRS CIO, Nextgov), IRM 10.24.1, CDTFA generative AI tool (Aug 2025), EY 2025 Tax Risk and Controversy Survey (70% implemented or integrating a GenAI tool for controversy; 46% of AI users very satisfied vs 31% of non-users) | controversy (tax-authority AI) |
| Hallucination rate and benchmark results for research tools; NormBench, TaxPraBen | research-advisory |
| KPMG Global Tax Readiness Dividend (2,084 leaders; top quartile 4 to 6 times more likely to outperform) | tax-data-technology |
| Individual and small-business return preparation (TaxCalcBench, AICPA tax software survey, Werfel case study) | compliance (individual and small-business lens) |

---

## 5. Sources

Dates are ISO. Access is `full` unless noted. "Lead only" means the open portion of a paywalled page.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| GAO-2026 | Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522) | GAO | regulator | https://www.gao.gov/products/gao-26-107522 | 2026-03-24 (from landscape; not shown on page read) | full (Highlights page via text mirror) |
| TIGTA-2025 | The IRS Could Leverage Examination Results in AI Examination Case Selection Models ... (2025-308-022) | TIGTA | regulator | https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf | 2025-05-19 | full |
| IRS-F6765-INSTR-2025 | Instructions for Form 6765 (12/2025), with About Form 6765 page (reviewed 2026-06-20) | IRS | regulator | https://www.irs.gov/instructions/i6765 | 2025-12 | full |
| ECFR-1694-1 | 26 CFR 1.6694-1 | eCFR | regulator | https://www.ecfr.gov/current/title-26/section-1.6694-1 | 2026-10-01 (point-in-time version) | full |
| ECFR-141-4 | 26 CFR 1.41-4 | eCFR | regulator | https://www.ecfr.gov/current/title-26/section-1.41-4 | 2026-10-01 (point-in-time version) | full |
| IRS-MEF-2026 | Modernized e-File (MeF) schemas and business rules | IRS | regulator | https://www.irs.gov/e-file-providers/modernized-e-file-mef-schemas-and-business-rules | 2026-05-29 | full |
| HMRC-GENAI-SW-2026 | Guidelines for using generative AI if you're a software developer | HMRC (GOV.UK) | regulator | https://www.gov.uk/guidance/guidelines-for-using-generative-artificial-intelligence-if-youre-a-software-developer | 2026-01-28 | full |
| NIST-AI600-2024 | AI RMF: Generative AI Profile (NIST AI 600-1) | NIST | standard-setter | https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence | 2024-07-26 | full (landing page only) |
| TAXADVISER-WERFEL-2026 | A risk framework for AI use in tax administration and preparation | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/ | 2026-08-31 | full |
| AICPA-WERFEL-2026 | Werfel framework appendices A to D (risk registers, methodology, case studies) | AICPA (Danny Werfel) | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-06 (upload path; PDF created 2026-05-14) | full |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | full |
| PCRT-AI-2026 | PCRT bodies publish guidance on using AI in tax (ICAEW) | ICAEW for seven PCRT bodies | professional-body | https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax | 2026-01-19 | full |
| PCRT-ATT-2026 | Professional bodies issue AI advice to members | ATT | professional-body | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 2026-01-19 | full |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 | full |
| BLOOMBERG-TAXCT-2026 | Tax Court Navigates AI Misuse Rules for Self-Represented Filers | Bloomberg Tax | press | https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers | 2026-03-20 | full (lead only; paywalled) |
| IRS-AIFIRST-2026 | Tax chief pushes 'AI-first IRS' ... | Nextgov/FCW | press | https://www.nextgov.com/artificial-intelligence/2026/10/tax-chief-pushes-ai-first-irs-get-more-out-agencys-workforce/416389/ | 2026-10-02 | full |
| TAXPROF-IRSGENAI-2026 | IRS Adopts Generative Artificial Intelligence Policy (Tax Notes abstract) | TaxProf Blog | press | https://taxprofblog.aals.org/2026/02/17/irs-adopts-generative-artificial-intelligence-policy/ | 2026-02-17 | full (abstract only) |
| CDTFA-2025 | Experts Urge Caution as State Tax Agencies Deploy Generative AI | Tax Notes (via Kogod) | press | https://kogod.american.edu/hubfs/experts_urge_caution_as_state_tax_agencies_deploy_generative_ai_20250826-161144.pdf | 2025-08-26 | full |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task | Column Tax (arXiv 2507.16126) | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full (HTML version) |
| COLUMBIA-TAXBENCH-2026 | TaxBench (in development) | Columbia DAP Lab | academic | https://daplab.cs.columbia.edu/benchmarks/taxbench/ | 2026 (page undated) | full |
| JHU-TAXREASON-2025 | Language Models and Logic Programs for Trustworthy Tax Reasoning | arXiv 2508.21051 (AAAI 2026) | academic | https://arxiv.org/abs/2508.21051 | 2025-08-28 | full (abstract) |
| DEONTICBENCH-2026 | DeonticBench: A Benchmark for Reasoning over Rules | arXiv 2604.04443 | academic | https://arxiv.org/abs/2604.04443 | 2026-04-06 | full (abstract) |
| NORMBENCH-2026 | From Statute to Control Flow: Span-Grounded Deontic Trees ... (NormBench) | arXiv 2606.08932 | academic | https://arxiv.org/abs/2606.08932 | 2026-06-08 | full (abstract) |
| SADOWSKI-VERIFY-2026 | Solving versus Verifying: Catching Contradictions in Tax Reasoning Systems | arXiv 2609.05928 | academic | https://arxiv.org/abs/2609.05928 | 2026-09-05 | full (abstract) |
| HAN-LAWORDER-2026 | Law And Order: Tax Law Autoformalization | arXiv 2610.02792 | academic | https://arxiv.org/abs/2610.02792 | 2026-10-02 | full (abstract) |
| TAXPRABEN-2026 | TaxPraBen: Benchmark for LLMs in Chinese Real-World Tax Practice | arXiv 2604.08948 | academic | https://arxiv.org/abs/2604.08948 | 2026-04-10 | full (abstract) |
| SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. | Tax Notes State (via TaxProf Blog) | academic | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 | full (abstract only) |
| KPMG-DE-2026 | Tax departments are increasingly turning to artificial intelligence | KPMG Germany | survey | https://kpmg.com/de/en/media/press-releases/2026/05/tax-departments-are-increasingly-turning-to-artificial-intelligence.html | 2026-05-07 | full |
| TR-CORPTAX-2025 | The GenAI paradox (2025 State of the Corporate Tax Department) | Thomson Reuters | survey | https://tax.thomsonreuters.com/blog/the-genai-paradox-why-most-tax-departments-arent-using-ai-yet-and-what-early-adopters-are-gaining-tri/ | 2025-10-22 | full |
| TR-GENAI-2025 | 5 GenAI tensions corporate tax departments should address | Thomson Reuters | survey | https://tax.thomsonreuters.com/blog/the-corporate-tax-genai-evolution-five-key-tensions-your-department-should-address-tri/ | 2025-06-24 | full |
| TR-CORPTECH-2026 | Corporate tax teams eager for AI, but frustrated by pace of change (2026 Corporate Tax Department Technology Report, 170 tax leaders) | Thomson Reuters Institute with TEI | survey | https://www.thomsonreuters.com/en-us/posts/corporates/corporate-tax-department-technology-report-2026 | 2026-03-16 | full (summary page) |
| TR-FOP-2026 | What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 | full |
| RSM-AISURVEY-2026 | AI is working in tax. Scaling it is the hard part (RSM Middle Market AI Survey 2026) | RSM US | survey | https://rsmus.com/insights/services/business-tax/ai-is-working-in-tax-scaling-it-is-the-hard-part.html | 2026-07-21 | full |
| EY-TAXRISK-2025 | EY 2025 Tax Risk and Controversy Survey | EY | survey | https://www.ey.com/en_gl/newsroom/2025/12/ey-2025-tax-risk-and-controversy-survey-tax-leaders-turn-to-ai-to-strengthen-tax-management-as-new-risks-loom | 2025-12-11 | full |
| FONOA-2026 | State of Indirect Tax in the AI Era 2026 | Fonoa | survey | https://www.fonoa.com/resources/guides/state-of-indirect-tax-in-the-ai-era-2026 | 2026-06-17 | full (landing page; report gated) |
| KPMG-READINESS-2026 | 2026 KPMG Global Tax Readiness Dividend | KPMG | survey | https://kpmg.com/xx/en/our-insights/transformation/global-tax-readiness-dividend.html | 2026 (page undated) | full (landing page) |
| AICPA-TAXSW-2026 | 2026 tax software survey | The Tax Adviser (AICPA) | survey | https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/ | 2026-08-31 | full |
| DELOITTE-TTT-2026 | Riding the wave: A framework to plan for AI | Deloitte Global | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf | 2026-07 (PDF creation date 2026-07-02) | full |
| TR-CORPAI-2026 | AI in corporate tax: 2026 key trends and use cases | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/blog/ai-in-corporate-tax-key-trends-use-cases-and-whats-next/ | 2026-07-01 | full |

**Count by type (distinct sources read):** regulator 8, standard-setter 1, professional-body 5, press 5, academic 9, survey 10, firm 1, vendor 1. Total 40. Types with no sources: conference, podcast, community, job-posting (outside this angle's reach; see Gaps).

---

## 6. Gaps

- **Quality evidence for corporate returns.** No error rate, override rate, parallel-run result, review-time change or inspection finding was found for AI-prepared 1120s, Form 5471/8858 packages, state returns or R&D credit studies. The only measured accuracy work covers individual 1040 data or statutory benchmarks (SARA).
- **International and state steps.** No AI governance source was found for Forms 5471/8858, state apportionment or SALT income tax filings, or estimated payments and the tax calendar. The Federation of Tax Administrators generative-AI paper for state agencies was not located (publication unconfirmed); one search returned only a 2025 report that it was being prepared.
- **In-house applicability.** OPR, PCRT, SSTS and the Werfel preparer register are written for practitioners and firms. No source read says how they apply to employees who prepare their own employer's return, or how Treas. Reg. 1.6694-1(e) reliance applies to AI output.
- **Primary text not reached.** AICPA SSTS Section 1.4 (page showed a download shell; cited via the Journal of Accountancy summary), ISO/IEC 42001 (403), Tax Notes full articles (Sala, IRS IRM 10.24.1: abstract only), Bloomberg Tax articles (lead only), Fonoa, TR and KPMG full reports (gated; landing pages and press summaries read), the TEI Annual Conference 2026 agenda (no AI titles; starts 17 to 18 Oct 2026).
- **Date uncertainty.** The Werfel framework: article dated 2026-08-31 on its page while the CART release of 2026-09-23 says published "earlier this month"; appendices upload path is June 2026 and PDF metadata shows 2026-05-14. GAO publication date is from the landscape (24 Mar 2026); the page read did not show it. KPMG Readiness and TaxBench pages are undated.
- **Statistics with unstated bases.** KPMG Germany, RSM and the TR 2025 GenAI report do not state sample sizes in the pages read. The TaxCalcBench percentage is per output across repeated runs; its exact run count was not recorded beyond the "4 runs per model at each thinking level" statement.
- **Search and quota.** Seven web searches were used on new directions. Vendor claims for the Kyocera research-credit case, Neo.Tax and Orbitax were not checked against primary sources. Landscape items not re-read (PwC K-1 agents, EY agent factory, KPMG Digital Gateway, Black Ore, TEI sessions) are practice-angle evidence and are only referenced in notes.
- **Not found.** A Tax Court rule or standing order on AI (none confirmed: the Bloomberg Tax lead says the court is weighing guardrails). Malpractice insurer or engagement-letter market practice for AI in corporate compliance. Any IRS or state enforcement action involving AI-prepared corporate returns.
