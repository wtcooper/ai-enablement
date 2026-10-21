# Employee benefit plan audits (ERISA): AI in practice, discourse and governance

Researched 2026-10-21. Module `benefit-plans` (assurance, mid-market extension). Combined pass: practice, discourse, governance and evidence.

## 1. Summary

- **Where the evidence is.** Public AI evidence for plan audits comes almost entirely from software vendors and the firms that use them. One platform, Autire, carries most of it, with named firm accounts at Belfint, Lyons & Shuman (regional) and Rea & Associates (Top 100) [AUTIRE-BELFINT-2026; AUTIRE-REA-2026]. Other named uses: Kimberlin Company and Sensiba with Thomson Reuters CoCounsel Audit [TR-KIMBERLIN-2026; TR-SENSIBA-2026], Anders CPAs + Advisors with AuditMiner [AUDITMINER-ANDERS-2025], and Citrin Cooperman adopting the DAS suite including DAS EBP [CITRIN-DAS-2026].
- **No entry reaches grade A.** Every figure sits in a vendor-authored page or press release and none says how it was measured. No error rates, override rates, parallel-run results, inspection outcomes or independent measurements of AI in plan audits were found. No DOL EBSA, AICPA peer review or EBPAQC statement on AI in plan audits was found.
- **The "30 percent deficient" figure is the November 2023 DOL study, not a 2025 one.** About 30 percent of the audits reviewed (2020 filings) had major GAAS deficiencies, against 39 percent in the 2015 study of 2011 filings [BELFINT-DOLQ-2024; AICPA-EBPAQC-TOOLS-2024; AAFCPA-DOLQ-2024; EBSA-AUDITQ-2023, search-only]. The December 2025 Jones & Roth post repeats it [EBSA-AUDITQ-2025]. This resolves the landscape's open contradiction (30 versus 39 percent): they are two studies. The primary PDF could not be opened (dol.gov returned 403 to every route), so the figures come from secondary summaries.
- **Deficiencies cluster in the data steps vendors target.** Participant data (15.6 percent), contributions (15.3) and benefit payments (9.4) lead the deficient areas; firms with one or two plan audits had 70 percent deficient audits against 17 percent for firms with 100 or more [BELFINT-DOLQ-2024]. Vendors aim at full-population participant testing, data pulls from payroll and recordkeepers, plan-document reading and SOC 1 reading.
- **"AI" covers two things.** Autire says its full-population tests are hard-coded, standards-based logic, with AI used for exception grouping [AUTIRE-AI-2026; AUTIRE-ADVAI-2026]. Much else on sale (workpaper generation, request portals, methodology-led files) is automation the sources do not call AI [AUDITMINER-SITE-2026; SIKICH-BROCHURE-2026; CASEWARE-DASEBP-2026].
- **Discourse is thin.** CPE sessions on AI in plan audits exist (CalCPA, 4 June 2026; AICPA conference marketing, May 2026) but only abstracts are public [CALCPA-EBP-2026; AICPA-EBP-2026]. No podcast, community thread, job posting or academic study on AI in plan audits was found.
- **Counts.** 17 use cases: 0 grade A, 8 grade B, 6 grade C, 3 grade D (ideas). 45 sources (4 conference, 6 firm, 3 press, 7 professional-body, 1 regulator, 24 vendor).

## 2. Use cases

```yaml
- id: assurance-benefit-plans-01
  title: Full-population testing of participant, payroll and contribution data in 401(k) plan audits (Autire at Belfint, Lyons & Shuman and Rea & Associates)
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [review-assurance, transaction-processing, data-reporting]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Participant data and contributions are the audit areas with the highest reported deficiency rates in the
    Department of Labor's 2023 audit quality study (BELFINT-DOLQ-2024). Firms have traditionally selected a
    sample and tested it, using audit software and checklists built for financial statement audits
    (AUTIRE-REA-2026; AUTIRE-BELFINT-2026).
  solution: >-
    Autire, a platform built for plan audits, applies testing rules to every available participant record (every
    contribution, distribution and eligible participant) at the start of the audit. Each flagged item is tied
    to source data with an occurrence count and dollar impact, so the firm goes to the client with focused
    questions (AUTIRE-TESTING-2026). Autire says the tests are hard-coded, standards-based logic that returns the
    same result on re-run, not model output (AUTIRE-AI-2026). Belfint, Lyons & Shuman (a Wilmington, Delaware
    regional firm that the vendor labels mid-market) moved eligible plans onto it from 2022. Rea & Associates (a
    Top 100 US firm in Ohio and Florida) has used it since 2022 (AUTIRE-BELFINT-2026; AUTIRE-REA-2026).
  outcomes:
    - lever: capacity
      description: "Belfint's average hours per audit fell from 80 to 54, and the practice grew from roughly 100 audits at adoption to 160-170, as reported in the vendor's case study"
      figure: "80 to 54 hours per audit; about 100 to 160-170 audits"
      measures: "average hours per audit for the preparer and both reviewers combined (source's words); audit count is the practice's plan audits at adoption versus 'today' (case study dated 2026-08-30). How the hours were tracked is not stated"
      provenance: vendor-published
      source_ref: AUTIRE-BELFINT-2026
    - lever: cost
      description: "Rea's managing director reports a 40 percent reduction in hours spent per audit since adopting, with improved profitability, and warns that going from 100 hours to 30 is not realistic overnight"
      figure: "40 percent fewer hours per audit"
      measures: "reduction in hours spent per audit since adopting Autire (source's words); baseline and period not given"
      provenance: vendor-published
      source_ref: AUTIRE-REA-2026
    - lever: quality
      description: "On first use at an existing client, Rea's file opened with about 8,000 flagged records; most traced to a single pay-code configuration issue, and the rest were items that warranted review"
      figure: "about 8,000 flags"
      measures: "flagged records in one existing engagement on first run, as quoted by the managing director; not a rate and not a count of true errors"
      provenance: vendor-published
      source_ref: AUTIRE-REA-2026
  prerequisites:
    - "Payroll, census, trust and recordkeeper data in a usable form, through integrations or direct upload (AUTIRE-HOME-2026)"
    - "A transition period: Belfint says benefits showed toward the end of the first year and into the second, with supervisors moving first (AUTIRE-BELFINT-2026)"
    - "Willingness to face more exceptions on existing clients; Rea worried that new findings would prompt questions about prior-year audits (AUTIRE-REA-2026)"
  risks_and_guardrails:
    - "Whole-population testing does not make the audit a guarantee; some risks sit outside transaction data, such as an incomplete population (LEDGERLINE-CPAPA-2026)"
    - "False failures are a real cost: Autire's June 2026 release removed what it called the two largest categories of false failures in the definition-of-compensation test (AUTIRE-ADVAI-2026)"
    - "The Department of Labor's study found more frequent deficiencies in areas unique to plan audits, including testing contributions and participant data (AICPA-EBPAQC-TOOLS-2024)"
  human_checkpoints:
    - "The auditor decides what each flagged item means; reviewers sign off in the workspace (AUTIRE-AI-2026; AUTIRE-HOME-2026)"
    - "Belfint added extra memos where its own quality control called for more documentation than the tool's defaults (AUTIRE-BELFINT-2026)"
  role_evolution: >-
    Belfint's audit manager says reviewers spend more time working out what is wrong and giving clients things they
    can fix, and that new staff ask to work on Autire files (AUTIRE-BELFINT-2026). Rea's managing director says the
    freed capacity can go to sit-down conversations with clients (AUTIRE-REA-2026).
  evidence_grade: B
  sources:
    - { ref: AUTIRE-BELFINT-2026, title: "How Belfint, Lyons & Shuman Grew From 100 to 170 EBP Audits (case study)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/case-studies/belfint-lyons-shuman/", date: "2026-08-30", access: full, locator: "\"The Numbers\"; \"What Changed\"" }
    - { ref: AUTIRE-REA-2026, title: "Rea Business Advisors Uses Full Population Testing to Gain the Upper Hand (case study)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/case-studies/rea-business-advisors/", date: "2026-08-30", access: full, locator: "\"Finding Every Flagged Record\"; \"Margins, Efficiency, and the Upper Hand\"" }
    - { ref: AUTIRE-TESTING-2026, title: "Automated EBP Audit Testing (platform testing page)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/platform/testing", date: "2026", access: full, locator: "\"Test Every Participant in Minutes\"" }
    - { ref: AUTIRE-AI-2026, title: "AI Built for EBP Audits (AI on Autire)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/platform/ai-on-autire", date: "2026", access: full, locator: "\"The Same Standard, Every Engagement\"" }
    - { ref: AUTIRE-ADVAI-2026, title: "Advanced AI Is Live Along With Other Product Upgrades", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/advanced-ai-live-product-upgrades-june-2026/", date: "2026-06-11", access: full, locator: "section \"DI-8: Improvements to Plan Definition of Compensation Testing\"" }
    - { ref: BELFINT-DOLQ-2024, title: "The 2023 DOL Audit Quality Study: Slight Improvements, but Audit Quality is Still Concerning", publisher: "Belfint, Lyons & Shuman (firm blog)", type: firm, url: "https://employeebenefitplanaudit.belfint.com/2023-dol-audit-quality-study/", date: "2024-03-07", access: full, locator: "\"EBP-specific Auditing Areas Still Have the Highest Deficiency Rates\"" }
    - { ref: AICPA-EBPAQC-TOOLS-2024, title: "EBPAQC tools that address 2023 DOL audit quality study deficiencies", publisher: "AICPA & CIMA", type: professional-body, url: "https://www.aicpa-cima.com/resources/download/ebpaqc-tools-that-address-2023-dol-audit-quality-study-deficiencies", date: "2024-08-20", access: full, locator: "paragraph 2" }
    - { ref: LEDGERLINE-CPAPA-2026, title: "Testing Every Transaction Changes the Audit - Here's What Firms Should Know Before They Sell It (Tunde Adewole, CEO of Ledgerline)", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/", date: "2026-10-15", access: full, locator: "section \"The trap\"" }
    - { ref: AUTIRE-CPAMERICA-2024, title: "Autire Partners with CPAmerica to Transform the EBP Auditing Process", publisher: "Autire Technologies (CPAmerica announcement)", type: vendor, url: "https://autire.com/autire-partners-with-cpamerica-to-transform-ebp-auditing-process/", date: "2024-10-14", access: full, locator: "announcement text" }
    - { ref: AUTIRE-BENCH-2024, title: "Autire Report Reveals CPA Firms Can Cut 401k Audit Hours in Half", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/autire-report-reveals-cpa-firms-can-cut-401k-audit-hours-in-half/", date: "2024-04-18", access: full, locator: "benchmarking paragraphs" }
    - { ref: AUTIRE-HOME-2026, title: "Autire: EBP Audit Software for CPA Firms (home page)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com", date: "2026", access: full, locator: "statistics row and Belfint case card" }
    - { ref: AUTIRE-ABOUT-2026, title: "Building the Future of EBP Audit (About)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/about", date: "2026", access: full, locator: "statistics row" }
  last_reviewed: "2026-10-21"
  notes: >-
    Graded B, not A: both hours figures sit in vendor-authored case studies and neither says how hours were tracked.
    The vendor's own headline claims (100+ down to 30 hours per plan; 7,000+ audits; 120+ firms; no peer review or
    DOL findings attributed to Autire) are on its home and about pages (AUTIRE-HOME-2026; AUTIRE-ABOUT-2026) and are
    not independently verified. Autire's April 2024 benchmarking release says first-time users reported a 40 percent
    cut in hours, over 50 hours per audit, and one firm saved 976 hours across 19 audits; that is vendor-collected data
    with unnamed firms (AUTIRE-BENCH-2024). CPAmerica, an association of independent CPA firms, added Autire as a
    preferred provider on 14 October 2024 (AUTIRE-CPAMERICA-2024). The full-population step is deterministic code; the AI sits in exception
    analysis (see 02). The same article describes the Ledgerline specialist-firm model already recorded in
    assurance-substantive-testing-25.

- id: assurance-benefit-plans-02
  title: AI exception analysis that groups flagged plan-audit exceptions by root cause (Autire Advanced AI)
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    After testing, auditors open source files in Excel, cross-reference payroll and recordkeeper reports and decide
    whether each flagged item matters; on complex plans with thousands of participants this can take several hours
    (AUTIRE-ADVAI-2026).
  solution: >-
    Autire released Advanced AI on 11 June 2026. An Analysis tab on two audit steps (initial reconciliation and
    data-intelligence tests, for 2025-version plans) reviews the full set of exceptions, categorises each by failure
    type, and shows whether an issue is isolated to one participant or systemic across a payroll run or deferral
    source. Auditors review by pattern and can share chosen findings with the client in the portal (AUTIRE-ADVAI-2026;
    AUTIRE-AI-2026). The vendor's security page says it uses Anthropic models on AWS Bedrock with guardrails that filter
    personal data, and that audit data is not used to train a model (AUTIRE-SECURITY-2026).
  outcomes:
    - lever: speed
      description: "An unnamed senior manager at an IPA Top 150 firm says compliance-testing flags take 30 minutes to resolve from start to finish; an unnamed senior auditor at an IPA Top 250 firm credits the platform with about 50 audit hours per audit, roughly half the earlier time"
      figure: "30 minutes; 50 hours per audit"
      measures: "30 minutes: time to resolve flagged compliance-testing results (testimonial, no sample size). 50 hours: audit hours per audit, 'about half the time before using Autire' (testimonial about the platform as a whole, not the AI tool). Both are unnamed-user quotes on the vendor's pages"
      provenance: vendor-published
      source_ref: AUTIRE-TESTING-2026
  prerequisites:
    - "Full-population test results to analyse; the feature works on the testing steps of the vendor's own methodology (AUTIRE-ADVAI-2026)"
    - "Plans on the vendor's 2025 version of the audit steps (AUTIRE-ADVAI-2026)"
  risks_and_guardrails:
    - "The vendor says the AI operates inside its methodology, does not make audit decisions, and handles research, cross-referencing and pattern recognition (AUTIRE-ADVAI-2026)"
    - "Grouping by pattern can hide an individual exception inside a cluster; no source reports a miss rate or override rate for the feature"
    - "AICPA's October 2026 practice aid says the auditor remains responsible for the audit and the opinion when AI is used (AICPA-AIPA-2026)"
  human_checkpoints:
    - "The auditor decides what to do with what the analysis surfaces and which findings go to the client (AUTIRE-ADVAI-2026)"
  role_evolution: >-
    The vendor says time shifts from finding exceptions to applying auditor judgment (AUTIRE-AI-2026). No firm account
    of changed roles for this feature was found.
  evidence_grade: C
  sources:
    - { ref: AUTIRE-ADVAI-2026, title: "Advanced AI Is Live Along With Other Product Upgrades", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/advanced-ai-live-product-upgrades-june-2026/", date: "2026-06-11", access: full, locator: "\"Advanced Audit Intelligence\"" }
    - { ref: AUTIRE-AI-2026, title: "AI Built for EBP Audits (AI on Autire)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/platform/ai-on-autire", date: "2026", access: full, locator: "\"Exceptions Grouped. Root Causes Surfaced.\"" }
    - { ref: AUTIRE-TESTING-2026, title: "Automated EBP Audit Testing (platform testing page)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/platform/testing", date: "2026", access: full, locator: "testimonial block \"30 Minutes\"" }
    - { ref: AUTIRE-SECURITY-2026, title: "Security and Compliance", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/security", date: "2026", access: full, locator: "\"AI Governance\"" }
    - { ref: AICPA-AIPA-2026, title: "Artificial Intelligence (AI) Considerations for Financial Statement Auditors: AICPA news release, read with the Journal of Accountancy report of 13 Oct 2026", publisher: "AICPA & CIMA", type: professional-body, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: "2026-10-13", access: full, locator: "quotation from the AICPA chief auditor" }
  last_reviewed: "2026-10-21"
  notes: >-
    Vendor-only. The feature had been live for about four months when reviewed; no named firm has published results
    for it. The two testimonials are unnamed users at firms the vendor describes by IPA ranking.

- id: assurance-benefit-plans-03
  title: Pulling payroll, census and recordkeeper data straight from source systems instead of requesting files
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [data-reporting, transaction-processing]
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Plan-audit testing starts from sponsors' payroll registers, census files and recordkeeper reports. Sikich names
    manual requests and follow-ups as something to reduce (SIKICH-BROCHURE-2026), and the AICPA's 2026 plan
    conference workshops cover testing procedures for payroll, definition of compensation, eligibility, participant
    data and contributions (AICPA-EBP-2026).
  solution: >-
    Sikich (a mid-market firm in an alternative practice structure; it says it audits over 800 plans) says it has
    relationships with payroll and recordkeeping platforms that enable audit-request automation, and uses standardised
    payroll data from selected systems to cut manual requests (SIKICH-BROCHURE-2026). Autire lists integrations to pull
    payroll and recordkeeper data automatically (AUTIRE-HOME-2026) and says it matches participants by unique
    identifier so Social Security numbers are not needed (AUTIRE-SECURITY-2026). AuditMiner says it standardises data
    across recordkeepers and payroll providers (AUDITMINER-SITE-2026). Trullion says its Data Match engine matches
    contribution amounts, hire dates and vesting information across payroll registers, plan documents and custodian
    statements (TRULLION-EBP-2025); no customer is named on that page. Ledgerline, a pre-launch specialist firm, plans
    to pull payroll data directly (see assurance-substantive-testing-25).
  outcomes:
    - lever: speed
      description: "none published for this step on its own"
      figure: "none published"
      measures: "Not applicable; Sikich's brochure states capabilities without figures"
      provenance: self-reported
      source_ref: SIKICH-BROCHURE-2026
  prerequisites:
    - "Connections to the sponsor's payroll provider and recordkeeper, which the sponsor sets up once (LEDGERLINE-SITE-2026)"
    - "Vendor or firm relationships with the payroll and recordkeeping platforms in use (SIKICH-BROCHURE-2026; AUTIRE-HOME-2026)"
  risks_and_guardrails:
    - "Participant data is personal data; Autire states it keeps data in US regions under SOC 2 Type 2 controls (vendor statement, AUTIRE-SECURITY-2026)"
    - "Overreliance on third-party service providers remained a deficiency theme in the DOL's November 2023 study (ICPAS-EBPQ-2024)"
  human_checkpoints:
    - "Audit programs include testing the completeness and accuracy of participant data (ICPAS-EBPQ-2024)"
  role_evolution: >-
    No source describes role change for this step alone. Sikich says all levels of its plan-audit team are dedicated,
    not only seniors (SIKICH-BROCHURE-2026).
  evidence_grade: B
  sources:
    - { ref: SIKICH-BROCHURE-2026, title: "Employee Benefit Plan Audits (brochure, file code SKCH_0726)", publisher: "Sikich", type: firm, url: "https://www.sikich.com/wp-content/uploads/2026/09/Employee-Benefit-Plan-Audit-Brochure_SKCH_0726.pdf", date: "2026", access: full, locator: "page 4 \"Engagement efficiencies\"" }
    - { ref: AUTIRE-HOME-2026, title: "Autire: EBP Audit Software for CPA Firms (home page)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com", date: "2026", access: full, locator: "\"Planning\" block (payroll / recordkeeper data)" }
    - { ref: AUTIRE-SECURITY-2026, title: "Security and Compliance", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/security", date: "2026", access: full, locator: "\"Less data. Less exposure.\"" }
    - { ref: AUDITMINER-SITE-2026, title: "Audit Software to Scale Your EBP Practice (home page)", publisher: "AuditMiner", type: vendor, url: "https://www.auditminer.com/", date: "2026", access: full, locator: "\"Grow Your EBP Practice\"" }
    - { ref: TRULLION-EBP-2025, title: "Employee Benefits Audit Software Powered by AI (blog)", publisher: "Trullion", type: vendor, url: "https://trullion.com/blog/ebp-audit-software-ai-automation/", date: "2025-04-27", access: full, locator: "section \"1. Automated data matching across source documents\"" }
    - { ref: AICPA-EBP-2026, title: "AICPA Employee Benefit Plans Conference 2026 (home page and pre-conference workshops page; agenda page did not load)", publisher: "AICPA & CIMA", type: conference, url: "https://events.aicpa-cima.com/EBP2026", date: "2026-05", access: full, locator: "pre-conference workshops page" }
    - { ref: LEDGERLINE-SITE-2026, title: "Ledgerline: Specialist 401(k) and 403(b) plan audits", publisher: "Ledgerline", type: firm, url: "https://ledgerlineaudit.com", date: "2026-10", access: full, locator: "\"We pull your payroll data, not request it\"" }
    - { ref: ICPAS-EBPQ-2024, title: "Enhancing Employee Benefit Plan Audit Quality (Andrea Wright, Johnson Lambert)", publisher: "Illinois CPA Society, Insight magazine (Spring 2024 issue)", type: professional-body, url: "https://www.icpas.org/resources/publications/insight-magazine/article-search/detail/spring-2024/enhancing-employee-benefit-plan-audit-quality", date: "2024", access: full, locator: "\"Challenges in ensuring audit quality\"; \"Best practices and strategies\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    Sikich's brochure (dated only by its file code SKCH_0726 and a September 2026 upload path) describes automation of
    requests and data, not AI. It is the only named-firm source on this step; no source gives hours saved.

- id: assurance-benefit-plans-04
  title: Extracting trust-statement PDFs into a trial balance and reconciling it to the Form 5500 and audited balances
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: document-to-decision
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    The trust report arrives as a PDF in each recordkeeper's own format; someone builds a trial balance from it, pulls
    the Form 5500, lines the two up in a workbook and chases differences (AUTIRE-TRUSTREC-2026).
  solution: >-
    Autire says an uploaded trust report is read to extract investment balances, contributions, distributions and plan
    activity, checked for completeness and accuracy, and turned into a trial balance shown beside the other balances,
    with a combined view across several service providers and mid-year recordkeeper changes (AUTIRE-TESTING-2026;
    AUTIRE-TRUSTREC-2026). Its team researches each provider's format and builds it in, so the auditor does not map
    fields on each engagement (AUTIRE-TRUSTREC-2026).
  outcomes:
    - lever: speed
      description: "The vendor says the step takes minutes instead of hours; no firm figure is published"
      figure: "none published"
      measures: "Not applicable; 'minutes instead of hours' is the vendor's general statement, with no sample or baseline"
      provenance: vendor-published
      source_ref: AUTIRE-TRUSTREC-2026
  prerequisites:
    - "Provider-specific format support kept current by the vendor; certified statements from different providers look nothing alike (AUTIRE-TRUSTREC-2026)"
  risks_and_guardrails:
    - "The vendor says final audit documentation stays in the auditor's control (AUTIRE-TRUSTREC-2026)"
    - "Extraction errors on unusual statements; no source reports an error rate"
  human_checkpoints:
    - "The auditor reviews the reconciled numbers before they flow to other audit steps (AUTIRE-TRUSTREC-2026)"
  role_evolution: >-
    The vendor says the time goes to judgment instead of the search for differences (AUTIRE-TRUSTREC-2026). No firm
    account found.
  evidence_grade: C
  sources:
    - { ref: AUTIRE-TRUSTREC-2026, title: "Built for EBP Audits: How Trust Reconciliation Works End to End on Autire", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/trust-reconciliation-on-autire/", date: "2026-07-31", access: full, locator: "opening section and \"Trust Reconciliation: Every Balance in One View\"" }
    - { ref: AUTIRE-TESTING-2026, title: "Automated EBP Audit Testing (platform testing page)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/platform/testing", date: "2026", access: full, locator: "\"Trial Balance in Minutes, Not Hours\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    Marked announced because no named firm ties its results to this feature, although the platform has named users
    (see 01). It is a Form 5500 tie-out as much as an AI step.

- id: assurance-benefit-plans-05
  title: Turning recordkeeper and payroll reports into standardised workpapers (AuditMiner at Anders CPAs + Advisors)
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [data-reporting, document-production]
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Setting up plan-audit workpapers meant hours of manual data entry, and audits could start with incomplete client
    data (AUDITMINER-ANDERS-2025).
  solution: >-
    AuditMiner says uploading plan reports generates up to ten automated workpapers, standardised across
    recordkeepers, and payroll reports for testing by pay period and annual census (AUDITMINER-SITE-2026). Anders CPAs
    + Advisors, a regional CPA firm (size not stated in the source), says it automated workpaper setup and SOC report
    analysis with it (AUDITMINER-ANDERS-2025). The sources do not describe machine learning or a language model in the
    product.
  outcomes:
    - lever: capacity
      description: "Anders says it saved hundreds of hours by automating repetitive tasks such as workpaper setup and SOC analysis"
      figure: "hundreds of hours"
      measures: "hours saved by the firm, unspecified period and engagements; a case-study statement, not a tracked metric"
      provenance: vendor-published
      source_ref: AUDITMINER-ANDERS-2025
  prerequisites:
    - "Recordkeeper and payroll reports in formats the vendor supports (AUDITMINER-SITE-2026)"
  risks_and_guardrails:
    - "The vendor describes per-audit pricing and workpapers that standardise how teams track, review and document testing (AUDITMINER-SITE-2026); no source reports workpaper error rates"
  human_checkpoints:
    - "Not described in the source beyond staff testing and analysing instead of keying data (AUDITMINER-ANDERS-2025)"
  role_evolution: >-
    The case study says removing monotonous tasks led to higher job satisfaction, better staff retention and a more
    manageable department; a partner says the tool helps keep focus on audit quality while reducing time on engagements
    (AUDITMINER-ANDERS-2025).
  evidence_grade: B
  sources:
    - { ref: AUDITMINER-ANDERS-2025, title: "Driving Efficiency and Enhancing Staff Morale at Anders CPAs + Advisors (case study PDF; date from PDF creation metadata, 20 Jan 2025; text layer absent, read as page images)", publisher: "AuditMiner", type: vendor, url: "https://6703923.fs1.hubspotusercontent-na1.net/hubfs/6703923/Anders%20Case%20Study%202025.pdf", date: "2025-01", access: full, locator: "pages 2-3 (\"The Challenges\"; \"The Results\")" }
    - { ref: AUDITMINER-SITE-2026, title: "Audit Software to Scale Your EBP Practice (home page)", publisher: "AuditMiner", type: vendor, url: "https://www.auditminer.com/", date: "2026", access: full, locator: "\"How It Works\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    Grade B because the figure is a rough estimate in a vendor case study. Included because it is the only named
    regional-firm case on workpaper generation; it is automation, and the sources do not call it AI.

- id: assurance-benefit-plans-06
  title: Reading plan documents and amendments with a citation-backed assistant (CoCounsel Audit at Kimberlin Company and Sensiba)
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Plan documents can run past 150 pages with several amendments, effective dates and detailed eligibility and
    compensation definitions; auditors scrolled for provisions, hand-keyed terms into workpapers and asked seniors to
    confirm readings (TR-KIMBERLIN-2026).
  solution: >-
    Kimberlin Company, PLLC (an Arizona specialist firm auditing medium-to-large 401(k) plans) uses Thomson Reuters
    CoCounsel Audit three to four days a week: auditors upload plan documents, ask which provisions and amendments
    apply, and follow source links to the page and section (TR-KIMBERLIN-2026). It also checks whether clients adopted
    required SECURE 2.0 amendments and the applicable effective dates (TR-KIMBERLIN-2026). Sensiba LLP (an independent
    Top 75 US firm) built CoCounsel workspace templates for employee benefit plan adoption agreements after first
    doing so for fund agreements; over 100 of its audit professionals use CoCounsel (TR-SENSIBA-2026). Ledgerline's CEO
    describes the same design: extract the provisions tested and cite page and section so a reviewer can verify
    (LEDGERLINE-CPAPA-2026).
  outcomes:
    - lever: speed
      description: "An auditor at Kimberlin estimates a plan-document error check that took 60 to 90 minutes now takes about 15 minutes; the vendor's headline tile says 80 percent time savings on routine checks"
      figure: "60-90 minutes down to about 15 minutes; 80 percent"
      measures: "time for one plan-document error-checking task, estimated by one auditor (source: 'Kern estimates'). The 80 percent tile is labelled time savings from faster responses and source-linked verification; its numerator and denominator are not stated"
      provenance: vendor-published
      source_ref: TR-KIMBERLIN-2026
  prerequisites:
    - "Plan documents and amendments uploaded to the tool; for Sensiba, workspace templates per document type (TR-SENSIBA-2026)"
    - "Staff who verify answers against the linked source; Sensiba says its goal is for staff not to rely blindly on AI (TR-SENSIBA-2026)"
  risks_and_guardrails:
    - "The vendor says professional judgment remains critical and the tool directs auditors to relevant sections faster (TR-KIMBERLIN-2026)"
    - "A wrong reading of a provision flows into eligibility and contribution tests; no source reports misreads"
  human_checkpoints:
    - "Auditors check the cited page and section before relying on an answer (TR-KIMBERLIN-2026)"
  role_evolution: >-
    Kimberlin says the tool reduces reliance on senior staff for routine checks and helps trainees answer routine
    questions on their own (TR-KIMBERLIN-2026).
  evidence_grade: B
  sources:
    - { ref: TR-KIMBERLIN-2026, title: "How Kimberlin Company accelerated 401(k) audits with CoCounsel Audit (case study)", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/how-kimberlin-company-accelerated-401-k-audits-with-cocounsel-audit", date: "2026-08-06", access: full, locator: "\"The solution\"; executive summary; closing section" }
    - { ref: TR-SENSIBA-2026, title: "How Sensiba boosts audit efficiency with CoCounsel Audit (case study)", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/accelerating-audit-efficiency-how-sensiba-llp-streamlined-technical-research-and-document-management-with-cocounsel-audit", date: "2026-01-06", access: full, locator: "\"Solution: CoCounsel saves time and increases efficiency\"" }
    - { ref: LEDGERLINE-CPAPA-2026, title: "Testing Every Transaction Changes the Audit - Here's What Firms Should Know Before They Sell It (Tunde Adewole, CEO of Ledgerline)", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/", date: "2026-10-15", access: full, locator: "section \"What full-population testing changes\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    Grade B: the figure is one auditor's estimate in a vendor-authored case study. Sensiba's case study is mostly
    about technical research and fund agreements; the plan-document part is one paragraph.

- id: assurance-benefit-plans-07
  title: AI-assisted reading of recordkeeper and TPA SOC 1 reports for plan-audit reliance (Kimberlin; AuditMiner toolkits)
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Plan audits lean on recordkeepers' and TPAs' SOC 1 reports, and overreliance on service providers was a deficiency
    theme in the Department of Labor's 2023 study (ICPAS-EBPQ-2024). The AICPA's plan audit quality center lists
    reliance on SOC 1 reports among tools aimed at that study's findings (AICPA-EBPAQC-TOOLS-2024). Reports run long;
    AuditMiner puts the average at over 20 pages (AUDITMINER-SOC-2026).
  solution: >-
    Kimberlin Company prompts CoCounsel Audit to map specific controls in a SOC 1 report to its testing focus areas as
    part of its CX 4.4 audit program and copies the structured result into workpapers (TR-KIMBERLIN-2026). AuditMiner
    sells over 1,000 reviewed SOC toolkits that turn reports into Excel workbooks and procedures, including toolkits
    for employee benefit plans among its industries; its pages describe workbooks and senior-CPA review, not AI
    (AUDITMINER-SOC-2026). Anders CPAs + Advisors lists SOC report analysis among the tasks it automated
    (AUDITMINER-ANDERS-2025).
  outcomes:
    - lever: speed
      description: "none published for SOC 1 review alone"
      figure: "none published"
      measures: "Not applicable; Kimberlin's time figure covers plan-document checks (see 06)"
      provenance: vendor-published
      source_ref: TR-KIMBERLIN-2026
  prerequisites:
    - "Current SOC 1 reports from each recordkeeper and TPA, with complementary user entity controls reviewed; Audenza says that section is frequently skipped (AUDENZA-EBP-2026, a vendor view)"
    - "A firm testing program that says what to extract (Kimberlin's CX 4.4 program) (TR-KIMBERLIN-2026)"
  risks_and_guardrails:
    - "A service organisation's own AI use now has AICPA technical Q&A for SOC 1 and SOC 2 engagements (AICPA-TQA9561-2026)"
    - "No source reports the accuracy of AI-mapped control summaries or any review rate for them"
  human_checkpoints:
    - "The auditor judges deviations and complementary user entity controls before relying (TR-KIMBERLIN-2026)"
  role_evolution: >-
    Kimberlin's auditors prompt the tool and paste structured results into workpapers (TR-KIMBERLIN-2026); no source
    describes a change in who concludes on reliance.
  evidence_grade: B
  sources:
    - { ref: TR-KIMBERLIN-2026, title: "How Kimberlin Company accelerated 401(k) audits with CoCounsel Audit (case study)", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/how-kimberlin-company-accelerated-401-k-audits-with-cocounsel-audit", date: "2026-08-06", access: full, locator: "paragraph on SOC 1 reports and the CX 4.4 audit program" }
    - { ref: AUDITMINER-SOC-2026, title: "SOC Report Toolkits for Auditors", publisher: "AuditMiner", type: vendor, url: "https://www.auditminer.com/soc-toolkits", date: "2026", access: full, locator: "\"OUR SOC LIBRary\"; \"Fun Fact\"" }
    - { ref: AUDITMINER-ANDERS-2025, title: "Driving Efficiency and Enhancing Staff Morale at Anders CPAs + Advisors (case study PDF; date from PDF creation metadata, 20 Jan 2025; text layer absent, read as page images)", publisher: "AuditMiner", type: vendor, url: "https://6703923.fs1.hubspotusercontent-na1.net/hubfs/6703923/Anders%20Case%20Study%202025.pdf", date: "2025-01", access: full, locator: "page 3 \"The Results\"" }
    - { ref: ICPAS-EBPQ-2024, title: "Enhancing Employee Benefit Plan Audit Quality (Andrea Wright, Johnson Lambert)", publisher: "Illinois CPA Society, Insight magazine (Spring 2024 issue)", type: professional-body, url: "https://www.icpas.org/resources/publications/insight-magazine/article-search/detail/spring-2024/enhancing-employee-benefit-plan-audit-quality", date: "2024", access: full, locator: "\"Challenges in ensuring audit quality\"" }
    - { ref: AICPA-EBPAQC-TOOLS-2024, title: "EBPAQC tools that address 2023 DOL audit quality study deficiencies", publisher: "AICPA & CIMA", type: professional-body, url: "https://www.aicpa-cima.com/resources/download/ebpaqc-tools-that-address-2023-dol-audit-quality-study-deficiencies", date: "2024-08-20", access: full, locator: "list of tools" }
    - { ref: AICPA-TQA9561-2026, title: "TQA Section 9561 SOC Examinations: Effect of the Service Organization's Use of AI on SOC 1 and SOC 2 Examinations (resource landing page; document body not opened)", publisher: "AICPA & CIMA", type: professional-body, url: "https://www.aicpa-cima.com/resources/download/tqa-section-9561-soc-examinations-effect-of-the-service-organizations-use-of-ai-on-soc1-and-soc2-examinations", date: "2026-09-11", access: full, locator: "landing-page description" }
    - { ref: AUDENZA-EBP-2026, title: "EBP Audit Guide 2026: Everything CPA Firms & Sponsors Need", publisher: "Audenza Advisory", type: vendor, url: "https://audenzaadvisory.com/employee-benefit-plan-audit-guide/", date: "2026-07-27", access: full, locator: "\"Section 8: Best Practices for Audit Readiness\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    Overlaps assurance-controls-testing-13 (AI review of third-party SOC reports); kept here because it is the plan
    audit's own reliance step with a named plan-audit firm.

- id: assurance-benefit-plans-08
  title: Risk assessment under SAS 145 generated from completed planning procedures
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Practitioners reported at the AICPA's plan conference that they were grappling with applying SAS 145 to plan
    audits, especially identifying controls, IT systems and related parties (JOFA-AAFOCUS-2024). The 2026 CalCPA
    conference ran a session on risk assessment from planning to workpapers for defined contribution and defined
    benefit plans (CALCPA-EBP-2026).
  solution: >-
    Autire announced in December 2024 an automated risk assessment. It says risk is calculated as a by-product of the
    standards-based procedures performed, with built-in management and governance questions, a process questionnaire
    for controls and walkthroughs, SOC assessments factored in, preliminary analytics, and responses documented by
    attribute and assertion and referenced to substantive procedures (AUTIRE-RISK-2024). Its home page says the risk
    assessment links to sample sizes and testing decisions (AUTIRE-HOME-2026).
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Not applicable; the release makes capability claims and gives no firm results"
      provenance: vendor-published
      source_ref: AUTIRE-RISK-2024
  prerequisites:
    - "Completed planning procedures and questionnaires in the vendor's workflow (AUTIRE-RISK-2024)"
  risks_and_guardrails:
    - "No source reports how inspectors or peer reviewers view tool-generated risk assessments"
    - "The vendor says deviation from the configured workflow requires a deliberate override (AUTIRE-COMPLIANCE-2026)"
  human_checkpoints:
    - "Stakeholders use it to support auditor judgments; the auditor still concludes (AUTIRE-RISK-2024)"
  role_evolution: >-
    The release says manual documentation is removed so firms can focus on higher-value tasks (AUTIRE-RISK-2024). No
    firm account found.
  evidence_grade: C
  sources:
    - { ref: AUTIRE-RISK-2024, title: "Autire Introduces First Audit Solution with Automated Risk Assessment, Transforming 401(k) Audit Compliance", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/autire-transforms-401k-audit-compliance-with-automated-risk-assessment/", date: "2024-12-02", access: full, locator: "opening paragraphs and capability list" }
    - { ref: AUTIRE-HOME-2026, title: "Autire: EBP Audit Software for CPA Firms (home page)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com", date: "2026", access: full, locator: "\"Testing\" block, Automated Risk Assessment" }
    - { ref: AUTIRE-COMPLIANCE-2026, title: "Consistent Audits. Defensible Files. (For Compliance Leaders)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/compliance-leaders", date: "2026", access: full, locator: "FAQ \"What happens if an auditor deviates\"" }
    - { ref: JOFA-AAFOCUS-2024, title: "A&A Focus recap: Top A&A and employee benefit plan issues", publisher: "Journal of Accountancy (AICPA)", type: press, url: "https://www.journalofaccountancy.com/newsletters/a-a-focus/a-a-focus-recap-top-a-a-and-employee-benefit-plan-issues.html", date: "2024-06-26", access: full, locator: "EBP conference recap, SAS 145 bullet" }
    - { ref: CALCPA-EBP-2026, title: "Employee Benefit Plans Audit Virtual Conference 2026 (session list)", publisher: "CalCPA", type: conference, url: "https://store.calcpa.org/catalog/activity/employee-benefit-plans-audit-virtual-conference-2026---1000004674", date: "2026-06-04", access: full, locator: "session \"Risk Assessment in Practice: From Planning to Workpapers\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    The vendor calls this fully automated and the first of its kind; both are unverified marketing claims. Whether any
    inspector or peer reviewer has commented on tool-generated risk assessments is not public.

- id: assurance-benefit-plans-09
  title: Methodology-embedded plan-audit file with plan profile and auto-drafted financial statements (DAS EBP at Citrin Cooperman)
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Caseware positions the product against outdated templates, with a standardised, methodology-led workflow
    (CASEWARE-DASEBP-2026). The DOL's 2023 study found deficiency rates falling as a firm's plan-audit volume rises
    (BELFINT-DOLQ-2024).
  solution: >-
    DAS EBP (originally OnPoint EBP, launched June 2020 by the AICPA and CPA.com on Caseware Cloud) tailors the file to
    plan type through a plan profile, scopes audit programs, links analytics and risks, and drafts financial
    statements and note disclosures from the profile and trial balance (CASEWARE-DASEBP-2026; AICPA-ONPOINT-2020).
    Citrin Cooperman, a firm serving private middle-market businesses and high-net-worth individuals, announced on 13
    July 2026 that it has implemented the full DAS suite including DAS EBP, with CPA.com as implementation partner
    (CITRIN-DAS-2026). The release also describes Caseware Verity agents in the audit file, including a disclosure
    checklist agent; it names no plan-audit agent (CITRIN-DAS-2026).
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Not applicable; Citrin's release is an adoption announcement with no results"
      provenance: vendor-published
      source_ref: CITRIN-DAS-2026
  prerequisites:
    - "Data migration, training and change management, which CPA.com provided for Citrin (CITRIN-DAS-2026)"
    - "Plan types inside scope: the 2020 FAQ limited the product to 401(k) audits under ERISA section 103(a)(3)(C) and excluded defined benefit, health and welfare, 403(b), ESOP and multiemployer plans; current coverage was not confirmed (AICPA-ONPOINT-2020)"
  risks_and_guardrails:
    - "Methodology embedded in software still needs firm quality-management oversight; the DOL study found 80 percent of deficient audits were done by plan audit quality center members, so membership and tools do not guarantee quality (BELFINT-DOLQ-2024)"
  human_checkpoints:
    - "Professionals complete the plan profile, run the programs and review the drafted financials (CASEWARE-DASEBP-2026)"
  role_evolution: >-
    Citrin's assurance innovation leader says the aim is to use AI and related tools to improve audit quality and
    accelerate learning while preserving critical thinking and professional judgment (CITRIN-DAS-2026).
  evidence_grade: B
  sources:
    - { ref: CITRIN-DAS-2026, title: "Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware to Advance Audit Quality, Professional Development, and Scalable Growth", publisher: "Caseware (press release)", type: vendor, url: "https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth", date: "2026-07-13", access: full, locator: "paragraphs 1-3 and 7" }
    - { ref: CASEWARE-DASEBP-2026, title: "DAS EBP (formerly OnPoint EBP) product page", publisher: "Caseware", type: vendor, url: "https://www.caseware.com/us/products/das-ebp", date: "2026", access: full, locator: "\"Features\"" }
    - { ref: AUTIRE-HOME-2026, title: "Autire: EBP Audit Software for CPA Firms (home page)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com", date: "2026", access: full, locator: "\"Audit Wrap Up\" navigation block (financial statement generation)" }
    - { ref: AICPA-ONPOINT-2020, title: "OnPoint EBP Frequently Asked Questions", publisher: "AICPA and CPA.com", type: professional-body, url: "https://www.cpa.com/sites/cpa/files/2020-08/OnPoint_EBP_FAQs.pdf", date: "2020-08", access: full, locator: "FAQ 1 and FAQ 3" }
    - { ref: BELFINT-DOLQ-2024, title: "The 2023 DOL Audit Quality Study: Slight Improvements, but Audit Quality is Still Concerning", publisher: "Belfint, Lyons & Shuman (firm blog)", type: firm, url: "https://employeebenefitplanaudit.belfint.com/2023-dol-audit-quality-study/", date: "2024-03-07", access: full, locator: "\"Some benefit to AICPA EBPAQC Membership\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    The DAS EBP product page does not mention AI features; the AI references in the Citrin release are about the wider
    DAS suite and Verity. Grade B rests on a vendor press release with a firm quote, not on a firm statement about
    plan-audit results. Autire's wrap-up phase also generates a financial statement package from audit data
    (AUTIRE-HOME-2026).

- id: assurance-benefit-plans-10
  title: Plan-specific request lists and client portals that cut what the plan sponsor has to send (Sikich on Suralink; Belfint on Autire)
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [coordination-scheduling, client-interaction]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Plan audits run on long request lists chased by email, landing in a seasonal scramble; Ledgerline describes the
    audit as roughly four months of requests, reviews and follow-ups (LEDGERLINE-SITE-2026).
  solution: >-
    Sikich uses the Suralink workflow platform to coordinate data gathering with custom requests, real-time progress
    views, per-person assignments and a chat feature in place of email (SIKICH-BROCHURE-2026). Autire sends
    plan-specific requests through a portal with reminders and status tracking (AUTIRE-HOME-2026). Belfint's audit
    manager says new engagements now start with a smaller request and that, if the sponsor supplies the initial
    documents, he can finish the audit in two weeks if required (AUTIRE-BELFINT-2026).
  outcomes:
    - lever: speed
      description: "Belfint's audit manager says an audit can be done in two weeks if the initial documents arrive; this is a stated capability, not a measured average"
      figure: "two weeks"
      measures: "calendar time to finish an audit once the sponsor supplies initial documents, 'if it had to be done' (audit manager's statement in a vendor case study)"
      provenance: vendor-published
      source_ref: AUTIRE-BELFINT-2026
  prerequisites:
    - "Sponsor willingness to use a portal and provide documents once; Sikich restricts sensitive items in the portal (SIKICH-BROCHURE-2026)"
  risks_and_guardrails:
    - "Sensitive and confidential items can be restricted inside the portal (SIKICH-BROCHURE-2026)"
  human_checkpoints:
    - "Requests are assigned to individual team members (SIKICH-BROCHURE-2026)"
  role_evolution: >-
    Belfint's audit manager says staff and sponsors both see speed as a selling point and that five to ten local TPAs
    send referrals (AUTIRE-BELFINT-2026).
  evidence_grade: B
  sources:
    - { ref: SIKICH-BROCHURE-2026, title: "Employee Benefit Plan Audits (brochure, file code SKCH_0726)", publisher: "Sikich", type: firm, url: "https://www.sikich.com/wp-content/uploads/2026/09/Employee-Benefit-Plan-Audit-Brochure_SKCH_0726.pdf", date: "2026", access: full, locator: "page 7 \"Suralink workflow platform\"" }
    - { ref: AUTIRE-BELFINT-2026, title: "How Belfint, Lyons & Shuman Grew From 100 to 170 EBP Audits (case study)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/case-studies/belfint-lyons-shuman/", date: "2026-08-30", access: full, locator: "\"What Changed\", \"The client ask\"" }
    - { ref: AUTIRE-HOME-2026, title: "Autire: EBP Audit Software for CPA Firms (home page)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com", date: "2026", access: full, locator: "\"Guided Document Requests\"" }
    - { ref: LEDGERLINE-SITE-2026, title: "Ledgerline: Specialist 401(k) and 403(b) plan audits", publisher: "Ledgerline", type: firm, url: "https://ledgerlineaudit.com", date: "2026-10", access: full, locator: "\"The problem today\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    Workflow automation, not AI. Included because it is how data reaches the tests in 01 and 03, and because it changes
    the client ask.

- id: assurance-benefit-plans-11
  title: Firm methodology configured once and enforced across plan audits, with vendor-supported DOL inspection and peer review
  archetype: assurance
  module: benefit-plans
  function: risk-compliance-legal
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    The Department of Labor's 2023 study found that peer review does not identify deficient plan audits and
    recommended an engagement review on top of the required system review (BELFINT-DOLQ-2024). In Tennessee's 2025
    peer review report, two of 21 ERISA engagements reviewed were nonconforming (TSCPA-PEERREVIEW-2025).
  solution: >-
    Autire says materiality, risk logic and testing conclusions are set once at firm level and cascade to every
    engagement, that its quality management materials are examined annually by an external reviewer, and that DOL
    inspection and peer review support from former plan auditors is in the per-audit fee (AUTIRE-COMPLIANCE-2026;
    AUTIRE-ABOUT-2026). Belfint says it added its own extra memos where its quality control needed more
    (AUTIRE-BELFINT-2026).
  outcomes:
    - lever: risk
      description: "The vendor claims zero peer review or DOL findings attributed to its platform across all firms; the claim is unverified"
      figure: "zero findings attributed to Autire"
      measures: "peer review or DOL findings 'attributed to Autire', per the vendor; no denominator, no definition of attribution, and not independently checked"
      provenance: vendor-published
      source_ref: AUTIRE-HOME-2026
  prerequisites:
    - "Firm-level configuration of methodology by someone who owns it (AUTIRE-COMPLIANCE-2026)"
  risks_and_guardrails:
    - "Consistency is not quality: the DOL found 80 percent of deficient audits were by plan audit quality center members (BELFINT-DOLQ-2024)"
    - "The vendor's examination covers its quality management materials as a practice aid, not any firm's engagement quality (AUTIRE-COMPLIANCE-2026)"
  human_checkpoints:
    - "Deviation from the configured workflow needs a deliberate override by a person (AUTIRE-COMPLIANCE-2026)"
  role_evolution: >-
    The vendor says its support team is entirely former plan auditors (AUTIRE-COMPLIANCE-2026), which moves some
    inspection preparation from the firm to the vendor.
  evidence_grade: C
  sources:
    - { ref: AUTIRE-COMPLIANCE-2026, title: "Consistent Audits. Defensible Files. (For Compliance Leaders)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/compliance-leaders", date: "2026", access: full, locator: "\"Your Standard, on Every File\"; \"DOL and Peer Review Support, Included\"; FAQ" }
    - { ref: AUTIRE-ABOUT-2026, title: "Building the Future of EBP Audit (About)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/about", date: "2026", access: full, locator: "\"A Team That's Done This Work Before\"" }
    - { ref: AUTIRE-HOME-2026, title: "Autire: EBP Audit Software for CPA Firms (home page)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com", date: "2026", access: full, locator: "statistics row" }
    - { ref: AUTIRE-BELFINT-2026, title: "How Belfint, Lyons & Shuman Grew From 100 to 170 EBP Audits (case study)", publisher: "Autire Technologies", type: vendor, url: "https://autire.com/case-studies/belfint-lyons-shuman/", date: "2026-08-30", access: full, locator: "\"What Changed\"" }
    - { ref: BELFINT-DOLQ-2024, title: "The 2023 DOL Audit Quality Study: Slight Improvements, but Audit Quality is Still Concerning", publisher: "Belfint, Lyons & Shuman (firm blog)", type: firm, url: "https://employeebenefitplanaudit.belfint.com/2023-dol-audit-quality-study/", date: "2024-03-07", access: full, locator: "\"Peer Review Not Meeting Objectives\"" }
    - { ref: TSCPA-PEERREVIEW-2025, title: "Annual Report on Peer Review Activities 2025", publisher: "Tennessee Society of CPAs", type: professional-body, url: "https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf", date: "2026-03-31", access: full, locator: "section II.2(c) nonconforming engagements table" }
  last_reviewed: "2026-10-21"
  notes: >-
    Vendor claims only; no inspector or peer reviewer has published a view of tool-generated files. The Tennessee figure
    is one state's small sample (21 engagements) and is context, not a benchmark.

- id: assurance-benefit-plans-12
  title: Specialist plan-audit firm building its own AI-assisted platform (Metz CPA, EBPAudit.ai)
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Plan audits are concentrated in specialist firms, and the DOL found the largest practices have far lower
    deficiency rates than firms with one or two plan audits (BELFINT-DOLQ-2024).
  solution: >-
    Metz CPA, PLLC, which calls itself a Top 100 plan-audit firm by volume with offices in Phoenix, Milwaukee and New
    York, markets fixed three-year pricing, a written service guarantee and a proprietary EBPAudit.ai platform that it
    says streamlines the audit and removes back-and-forth (METZ-EBPAUDITAI-2026).
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Not applicable; the page says the platform reduces turnaround time but gives no figure"
      provenance: self-reported
      source_ref: METZ-EBPAUDITAI-2026
  prerequisites:
    - "Specialist team with plan-specific experience; the firm says its auditors average over a decade of plan-audit experience (METZ-EBPAUDITAI-2026)"
  risks_and_guardrails:
    - "No source describes what the platform does or how its output is reviewed"
  human_checkpoints:
    - "Not described"
  role_evolution: >-
    The firm says clients work with an experienced plan auditor and not a junior rotation (METZ-EBPAUDITAI-2026).
  evidence_grade: C
  sources:
    - { ref: METZ-EBPAUDITAI-2026, title: "EBPAudit.ai: Employee Benefit Plan Audits by Metz CPA, PLLC", publisher: "Metz CPA, PLLC", type: firm, url: "https://ebpaudit.ai/", date: "2026", access: full, locator: "\"Why Metz CPA\" list item \"AI-assisted workflows\"" }
    - { ref: BELFINT-DOLQ-2024, title: "The 2023 DOL Audit Quality Study: Slight Improvements, but Audit Quality is Still Concerning", publisher: "Belfint, Lyons & Shuman (firm blog)", type: firm, url: "https://employeebenefitplanaudit.belfint.com/2023-dol-audit-quality-study/", date: "2024-03-07", access: full, locator: "strata table under \"Results\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    One marketing line on a firm site (page undated, copyright 2026). Kept at C because the page does not say what the
    AI does. The Ledgerline model (a pre-launch specialist firm) is already recorded in assurance-substantive-testing-25.

- id: assurance-benefit-plans-13
  title: Form 5500 search and analytics to size up plan engagements and find plan-audit prospects (AuditMiner Plan Research)
  archetype: assurance
  module: benefit-plans
  function: sales-marketing-bd
  work_types: [research-synthesis, data-reporting]
  pattern: research-brief
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: >-
    Firms need plan information to scope a complex engagement and to find retirement plans that fit their client
    profile (AUDITMINER-PLANRES-2026).
  solution: >-
    AuditMiner's Plan Research product combines Form 5500 search with plan analytics, historical filings and audit
    reports, for evaluating a current engagement and finding new business (AUDITMINER-PLANRES-2026).
  outcomes:
    - lever: growth
      description: "none published"
      figure: "none published"
      measures: "Not applicable; product page only"
      provenance: vendor-published
      source_ref: AUDITMINER-PLANRES-2026
  prerequisites:
    - "Public Form 5500 data and audit reports (AUDITMINER-PLANRES-2026)"
  risks_and_guardrails:
    - "Prospecting from public filings raises independence and acceptance questions handled elsewhere (see Routed to other modules)"
  human_checkpoints:
    - "Partner or manager decides whether to propose and accept"
  role_evolution: >-
    Not described.
  evidence_grade: C
  sources:
    - { ref: AUDITMINER-PLANRES-2026, title: "EBP Plan Research (product page)", publisher: "AuditMiner", type: vendor, url: "https://www.auditminer.com/ebp-plan-research", date: "2026", access: full, locator: "introduction and \"YOUR Audit ADVANTAGE\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    The page is undated and does not say it uses AI. It is the only Form 5500 data product aimed at plan auditors that
    was found.

- id: assurance-benefit-plans-14
  title: "Idea: firm-level governance and engagement documentation for AI used in plan audits"
  archetype: assurance
  module: benefit-plans
  function: risk-compliance-legal
  work_types: [review-assurance, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    AI tools are entering plan-audit workflows while the profession is still working out governance, limits and
    professional judgment; a CalCPA session in June 2026 was framed that way (CALCPA-EBP-2026).
  solution: >-
    Idea, discussed by practitioners: tighten controls around AI-assisted and outsourced work, document professional
    judgment against AI suggestions, set guardrails for automation used in testing (AUDITMINER-PREDICT-2026), and
    follow the AICPA's October 2026 practice aid on quality management, supervision and review when auditors use AI
    (AICPA-AIPA-2026). A Forvis Mazars quality leader told an AICPA webcast in 2024 that AI tool use should be
    documented at firm and engagement level, including data completeness and accuracy testing (JOFA-AAFOCUS-2024).
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Not applicable"
      provenance: self-reported
      source_ref: CALCPA-EBP-2026
  prerequisites:
    - "Firm AI policy and quality management system covering tools used on plan engagements (AICPA-AIPA-2026)"
  risks_and_guardrails:
    - "Plan data is participant personal data; sponsors and providers may already use AI that changes the data auditors receive (AUDITMINER-PREDICT-2026)"
  human_checkpoints:
    - "The auditor remains responsible for the audit and opinion (AICPA-AIPA-2026)"
  role_evolution: >-
    Not described for plan audits.
  evidence_grade: D
  sources:
    - { ref: CALCPA-EBP-2026, title: "Employee Benefit Plans Audit Virtual Conference 2026 (session list)", publisher: "CalCPA", type: conference, url: "https://store.calcpa.org/catalog/activity/employee-benefit-plans-audit-virtual-conference-2026---1000004674", date: "2026-06-04", access: full, locator: "final session \"Incorporating AI into EBP Audits: Balancing Risk and Reward\"" }
    - { ref: AUDITMINER-PREDICT-2026, title: "EBP Auditing Industry 2026: What Auditors Should Expect Next", publisher: "AuditMiner", type: vendor, url: "https://www.auditminer.com/post/ebp-audit-predictions-for-2026-what-2025-revealed-and-what-auditors-should-expect-next", date: "2026-01-23", access: full, locator: "prediction 2 and closing list" }
    - { ref: AICPA-AIPA-2026, title: "Artificial Intelligence (AI) Considerations for Financial Statement Auditors: AICPA news release, read with the Journal of Accountancy report of 13 Oct 2026", publisher: "AICPA & CIMA", type: professional-body, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: "2026-10-13", access: full, locator: "quotation from the AICPA chief auditor" }
    - { ref: JOFA-AAFOCUS-2024, title: "A&A Focus recap: Top A&A and employee benefit plan issues", publisher: "Journal of Accountancy (AICPA)", type: press, url: "https://www.journalofaccountancy.com/newsletters/a-a-focus/a-a-focus-recap-top-a-a-and-employee-benefit-plan-issues.html", date: "2024-06-26", access: full, locator: "Forvis Mazars segment" }
    - { ref: SIKICH-WEBINAR-2025, title: "Roses are Red, Audits are Due: Strategies for Employee Benefit Plan Audit Filing Success (webinar listing)", publisher: "Sikich", type: conference, url: "https://go.sikich.com/roses-are-red-audits-are-due-webinar-february2025.html", date: "2025-02-12", access: full, locator: "agenda bullet \"The role of AI in employee benefit plan audits\"" }
    - { ref: CALCPA-EBP-2025, title: "Employee Benefit Plans Audit Virtual Conference 2025 (session list)", publisher: "CalCPA", type: conference, url: "https://store.calcpa.org/catalog/activity/employee-benefit-plans-audit-virtual-conference-2025---1000003879", date: "2025-06-05", access: full, locator: "session \"Audit Efficiency\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    Idea. The CalCPA session was held on 4 June 2026; only its abstract was read, so nothing is known about its
    content. The AICPA practice aid is not specific to plan audits. A February 2025 Sikich webinar and a 2025 CalCPA
    session also named AI in plan audits (SIKICH-WEBINAR-2025; CALCPA-EBP-2025); neither published content.

- id: assurance-benefit-plans-15
  title: "Idea: assessing AI used by recordkeepers, TPAs, payroll providers and plan sponsors through SOC 1 reports and risk assessment"
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Plan data and controls sit with service providers whose AI use can change the data and controls the auditor relies
    on; AuditMiner expects auditors to evaluate how AI-generated data affects risk assessments (AUDITMINER-PREDICT-2026).
  solution: >-
    Idea: use the AICPA's September 2026 technical Q&A on a service organisation's use of AI in SOC 1 and SOC 2
    engagements (AICPA-TQA9561-2026) and the AICPA's October 2026 practice aid on a client's AI in reporting and
    controls (AICPA-AIPA-2026) as the basis for asking providers whether AI sits in the service and what the SOC report
    covers. No plan-audit-specific guidance was found.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Not applicable"
      provenance: self-reported
      source_ref: AUDITMINER-PREDICT-2026
  prerequisites:
    - "SOC 1 reports from every recordkeeper and TPA, including the system description and user entity controls (AUDENZA-EBP-2026)"
  risks_and_guardrails:
    - "AuditMiner names cybersecurity and fraud, such as account takeovers and fraudulent distributions, as frontline risks for 2026 (AUDITMINER-PREDICT-2026)"
  human_checkpoints:
    - "The auditor concludes on reliance and scope (AICPA-TQA9561-2026)"
  role_evolution: >-
    Not described.
  evidence_grade: D
  sources:
    - { ref: AUDITMINER-PREDICT-2026, title: "EBP Auditing Industry 2026: What Auditors Should Expect Next", publisher: "AuditMiner", type: vendor, url: "https://www.auditminer.com/post/ebp-audit-predictions-for-2026-what-2025-revealed-and-what-auditors-should-expect-next", date: "2026-01-23", access: full, locator: "prediction 2 (\"AI Will Influence EBP Audits\"); prediction 5" }
    - { ref: AICPA-TQA9561-2026, title: "TQA Section 9561 SOC Examinations: Effect of the Service Organization's Use of AI on SOC 1 and SOC 2 Examinations (resource landing page; document body not opened)", publisher: "AICPA & CIMA", type: professional-body, url: "https://www.aicpa-cima.com/resources/download/tqa-section-9561-soc-examinations-effect-of-the-service-organizations-use-of-ai-on-soc1-and-soc2-examinations", date: "2026-09-11", access: full, locator: "landing-page description" }
    - { ref: AICPA-AIPA-2026, title: "Artificial Intelligence (AI) Considerations for Financial Statement Auditors: AICPA news release, read with the Journal of Accountancy report of 13 Oct 2026", publisher: "AICPA & CIMA", type: professional-body, url: "https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing", date: "2026-10-13", access: full, locator: "description of the two parts" }
    - { ref: AUDENZA-EBP-2026, title: "EBP Audit Guide 2026: Everything CPA Firms & Sponsors Need", publisher: "Audenza Advisory", type: vendor, url: "https://audenzaadvisory.com/employee-benefit-plan-audit-guide/", date: "2026-07-27", access: full, locator: "\"Section 8\"" }
  last_reviewed: "2026-10-21"
  notes: >-
    Idea. The Q&A document body was not opened; the landing page gives its scope and date only. Related module:
    assurance-over-ai (see Routed to other modules).

- id: assurance-benefit-plans-16
  title: Citation-backed technical Q&A for plan auditors and trainees (SECURE 2.0, plan terms and standards)
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Plan audit teams field routine questions on plan provisions and rules, and juniors lean on seniors for
    confirmation (TR-KIMBERLIN-2026). Sensiba's staff spent 30 to 45 minutes digging through guidance and drafting
    memos from scratch (TR-SENSIBA-2026).
  solution: >-
    Kimberlin trainees use CoCounsel Audit to understand regulatory concepts and find answers to routine questions
    on their own (TR-KIMBERLIN-2026). Sensiba's senior audit manager says citation-backed answers let staff resolve an
    issue while learning the standard, and that the firm wants staff to apply judgment instead of relying blindly on
    AI (TR-SENSIBA-2026).
  outcomes:
    - lever: experience
      description: "Kimberlin and Sensiba report trainee confidence and learning benefits without figures"
      figure: "none published"
      measures: "Not applicable; testimonials"
      provenance: vendor-published
      source_ref: TR-KIMBERLIN-2026
  prerequisites:
    - "A tool with authoritative content and citations; Sensiba rolled it out in January so staff learned on live work (TR-SENSIBA-2026)"
  risks_and_guardrails:
    - "Sensiba says it wants staff not to rely blindly on AI, and says the citations shown beside each answer help reinforce that (TR-SENSIBA-2026)"
    - "The ICPAS article warns that time pressure can tempt auditors to rely too heavily on automated tools (ICPAS-EBPQ-2024)"
  human_checkpoints:
    - "Staff check the cited guidance; seniors review conclusions (TR-SENSIBA-2026)"
  role_evolution: >-
    Kimberlin says seniors spend less time answering routine questions (TR-KIMBERLIN-2026).
  evidence_grade: B
  sources:
    - { ref: TR-KIMBERLIN-2026, title: "How Kimberlin Company accelerated 401(k) audits with CoCounsel Audit (case study)", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/how-kimberlin-company-accelerated-401-k-audits-with-cocounsel-audit", date: "2026-08-06", access: full, locator: "paragraph on trainees" }
    - { ref: TR-SENSIBA-2026, title: "How Sensiba boosts audit efficiency with CoCounsel Audit (case study)", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/insights/case-studies/accelerating-audit-efficiency-how-sensiba-llp-streamlined-technical-research-and-document-management-with-cocounsel-audit", date: "2026-01-06", access: full, locator: "\"Challenge\" and \"An often-overlooked benefit\" paragraphs" }
    - { ref: ICPAS-EBPQ-2024, title: "Enhancing Employee Benefit Plan Audit Quality (Andrea Wright, Johnson Lambert)", publisher: "Illinois CPA Society, Insight magazine (Spring 2024 issue)", type: professional-body, url: "https://www.icpas.org/resources/publications/insight-magazine/article-search/detail/spring-2024/enhancing-employee-benefit-plan-audit-quality", date: "2024", access: full, locator: "\"Challenges in ensuring audit quality\", last paragraph" }
  last_reviewed: "2026-10-21"
  notes: >-
    Sensiba's case is about audit research generally; only the plan-document templates are plan-specific (see 06).

- id: assurance-benefit-plans-17
  title: "Idea: year-round plan-data monitoring shared between recordkeeper, TPA and auditor"
  archetype: assurance
  module: benefit-plans
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Remittance timing and eligibility errors are easiest to fix when found early, and plan audits cluster in one busy
    window (AUDENZA-EBP-2026).
  solution: >-
    Idea: reconcile contribution data and eligibility changes monthly (a readiness practice recommended by an
    outsourcing vendor, AUDENZA-EBP-2026). An August 2026 Plan Sponsor Council of America article, seen only in search
    results, reportedly discusses AI-enabled continuous monitoring of plan data and says it depends on integration
    between recordkeeper and TPA (PSCA-AIRK-2026; unverified). No auditor has described acting on such a feed.
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Not applicable"
      provenance: self-reported
      source_ref: AUDENZA-EBP-2026
  prerequisites:
    - "Recordkeeper and TPA data integration (PSCA-AIRK-2026, unverified)"
  risks_and_guardrails:
    - "A continuous feed from the plan's own providers raises independence and completeness questions the sources do not address"
  human_checkpoints:
    - "Not described"
  role_evolution: >-
    Not described.
  evidence_grade: D
  sources:
    - { ref: AUDENZA-EBP-2026, title: "EBP Audit Guide 2026: Everything CPA Firms & Sponsors Need", publisher: "Audenza Advisory", type: vendor, url: "https://audenzaadvisory.com/employee-benefit-plan-audit-guide/", date: "2026-07-27", access: full, locator: "\"Section 8: Best Practices for Audit Readiness\"" }
    - { ref: PSCA-AIRK-2026, title: "AI May Help Modernize Retirement Plan Recordkeeping (seen in search results only; page returned 403)", publisher: "Plan Sponsor Council of America", type: professional-body, url: "https://www.psca.org/news/psca-news/2026/8/ai-may-help-modernize-retirement-plan-recordkeeping/", date: "2026-08", access: search-only, locator: "search-result summary only" }
  last_reviewed: "2026-10-21"
  notes: >-
    Idea. The PSCA page returned 403 and was not read; the description comes from a search summary. Audenza's advice is
    about sponsors' own monthly reconciliation and does not mention AI.
```

## 3. Module notes

### Processes and key steps (with work types)

| Step | What happens | Work type | AI evidence |
|---|---|---|---|
| Acceptance and setup | Confirm the plan needs an audit (100 or more eligible participants at the start of the plan year, with an 80-120 election rule), plan type (401(k), 403(b), ESOP, defined benefit, health and welfare, multiple-employer and pooled plans), predecessor auditor contact [METZ-EBPAUDITAI-2026] | expert-judgment, coordination-scheduling | Plan Research data tool (13) |
| Planning and risk assessment | SAS 145 risk assessment, plan profile, understanding service providers and IT [JOFA-AAFOCUS-2024; CALCPA-EBP-2026] | expert-judgment, document-production | Generated risk assessment (08); plan-profile file (09) |
| Document and data gathering | Plan document, amendments, adoption agreement, trust statements, payroll registers, census, recordkeeper files [AUTIRE-TRUSTREC-2026; LEDGERLINE-SITE-2026] | coordination-scheduling, data-reporting | Portals (10); data pulls (03); workpaper generation (05) |
| Service-provider reliance | Read recordkeeper, TPA and payroll SOC 1 reports; user entity controls; the EBPAQC has a tool for reliance on SOC 1 reports [AICPA-EBPAQC-TOOLS-2024] | review-assurance | SOC 1 reading (07) |
| Investments and trust reconciliation | Trust report to trial balance to Form 5500; limited-scope (ERISA 103(a)(3)(C)) versus full-scope [AICPA-ONPOINT-2020] | data-reporting, review-assurance | Trust-report extraction (04) |
| Participant-data testing | Eligibility, deferrals and definition of compensation, match, vesting and forfeitures, loans, hardships, distributions, timely remittance [AICPA-EBP-2026, pre-conference workshops] | transaction-processing, review-assurance | Full-population tests (01); exception analysis (02) |
| Plan-document and compliance review | Operation against plan terms, SECURE 2.0 amendments, prohibited transactions [TR-KIMBERLIN-2026; AICPA-EBPAQC-TOOLS-2024] | expert-judgment, research-synthesis | Plan-document reading (06); Q&A (16) |
| Financial statements, disclosures, Form 5500 | Draft statements and notes; tie Form 5500 to audited balances; file the report with the 5500 [CASEWARE-DASEBP-2026; JOFA-AAFOCUS-2024] | document-production | Auto-drafted statements (09) |
| Review, inspection and peer review readiness | Reviewer sign-off; DOL inspection; AICPA peer review with must-select EBP engagements [TSCPA-PEERREVIEW-2025] | review-assurance | Methodology enforcement (11) |

Defined benefit plans (actuarial work) and health and welfare plans are separate audit types. No AI evidence for either was found; the 2020 OnPoint FAQ excluded both from that product [AICPA-ONPOINT-2020].

### Common pain points

- Staffing and concentration: the number of firms doing plan audits fell from 7,330 (2011 filings) to 4,300 (2020 filings) while audits rose from 81,162 to 86,863 [BELFINT-DOLQ-2024]. Firms with 100 or more audits did 47,982 of the 86,863 (about 55 percent, my arithmetic) [BELFINT-DOLQ-2024].
- Small-practice quality: 70.0 percent of audits by firms with one or two plan audits had major deficiencies [BELFINT-DOLQ-2024].
- Data in many formats and repeated requests, and a busy season that overlaps extension deadlines [SIKICH-BROCHURE-2026; AUDENZA-EBP-2026 (vendor view)].
- Applying SAS 145 to plans: controls, IT systems, related parties [JOFA-AAFOCUS-2024].
- Form 5500 errors "remain a frequent issue", and recurring peer review deficiencies include missed actuarial considerations (session abstracts, not data) [CALCPA-EBP-2026].
- Initial audits (new auditor or newly audit-required plans) present quality challenges [JOFA-AAFOCUS-2024].
- Supervision and documentation of outsourced and offshore support (vendor commentary) [AUDITMINER-PREDICT-2026].

### Metrics and benchmarks (with sources)

| Metric | Figure | What it measures | Provenance |
|---|---|---|---|
| Major GAAS deficiencies, 2020 filings (Nov 2023 study) | about 30% | audits reviewed with one or more major GAAS deficiencies; Belfint's text says 307 plans reviewed, its table totals 308 | secondary summary of a regulator study [BELFINT-DOLQ-2024; AICPA-EBPAQC-TOOLS-2024] |
| Same, 2015 study (2011 filings) | 39% | same measure, 400 audits | [BELFINT-DOLQ-2024] |
| History | 23% (1989), 19% (1997), 33% (2004), 39% (2015), 30% (2023) | same measure across five studies | [BELFINT-DOLQ-2024] |
| By firm plan-audit volume, 2020 filings | 70.0% (1-2 plans, 20 audits reviewed), 51.2% (3-5, 23), 50.1% (6-24, 54), 38.0% (25-99, 74), 17.0% (100+, 137) | share of audits reviewed in each stratum with deficiencies; the 100+ stratum was 12.0% in the 2015 study | [BELFINT-DOLQ-2024] |
| Deficiency areas | participant data 15.6%, contributions 15.3%, benefit payments 9.4%, internal controls 5.90%, planning and supervision 3.30% | rate per audit area as reported by Belfint; denominator not stated in the secondary source | [BELFINT-DOLQ-2024] |
| EBPAQC membership | members had a significantly lower deficiency rate, yet 80% of deficient audits were by members | share of deficient audits performed by quality-center members | [BELFINT-DOLQ-2024; AAFCPA-DOLQ-2024] |
| Peer review, Tennessee 2025 | ERISA: 2 of 21 engagements nonconforming (10%) | engagements reviewed that were not performed in conformity with standards in all material respects; one state, small sample | [TSCPA-PEERREVIEW-2025] |
| Hours per audit, Belfint on Autire | 80 to 54 | preparer plus two reviewers, average | vendor-published [AUTIRE-BELFINT-2026] |
| Hours per audit, Rea on Autire | 40% fewer | hours per audit since adoption | vendor-published [AUTIRE-REA-2026] |
| Plan-document error check, Kimberlin | 60-90 minutes to about 15 | one auditor's estimate | vendor-published [TR-KIMBERLIN-2026] |
| Vendor-wide claims, Autire | 100+ to 30 hours per plan; 7,000+ audits; 120+ firms | not defined | vendor-published, unverified [AUTIRE-HOME-2026] |

Quality evidence for AI itself: none independent. The closest items are (a) Rea's first-run file with about 8,000 flags, mostly one pay-code configuration issue [AUTIRE-REA-2026]; (b) Autire's June 2026 removal of the two largest categories of false failures in one test [AUTIRE-ADVAI-2026]; (c) the vendor's "zero peer review or DOL findings attributed to Autire", which is undefined and unchecked [AUTIRE-HOME-2026]. These show that whole-population tests throw false positives and need triage; they do not measure miss rates. No override rates or parallel-run results exist in public sources. The vendor-collected benchmark (40 percent fewer hours; 976 hours saved across 19 audits at one first-year firm) has unnamed firms [AUTIRE-BENCH-2024].

### Guardrails and regulatory points

- Standards: SAS 136 (plan financial statements, effective for periods ending on or after 15 Dec 2021) and SAS 145 (risk assessment) [AICPA-ONPOINT-2020; JOFA-AAFOCUS-2024]. AICPA quality management standards took effect 15 Dec 2025 [JOFA-AAFOCUS-2024].
- Regulator: DOL EBSA's Office of the Chief Accountant studies plan audit quality. Its 2023 study asked for authority over registration, suspension and debarment of plan auditors, civil penalties for substandard audits, and repeal of the limited-scope audit provision; for peer review it asked for disclosure of deficiencies and an added engagement review for firms doing plan audits (as summarised by Belfint, who disagrees on limited scope) [BELFINT-DOLQ-2024]. The study said peer review was not identifying deficient plan audits [BELFINT-DOLQ-2024].
- AICPA: Peer review treats ERISA as a must-select engagement type [TSCPA-PEERREVIEW-2025]. The EBPAQC published a tool list answering the 2023 study (planning, timely remittance, plan document compliance, parties in interest, fraud, SOC 1 reliance, section 103(a)(3)(C) audits, specialists) [AICPA-EBPAQC-TOOLS-2024].
- AI guidance: AICPA's October 2026 practice aid covers a client's AI in reporting and an audit firm's own AI use (quality management, supervision, review, judgment, skepticism); it is for financial statement audits generally, not plan-specific [AICPA-AIPA-2026]. TQA 9561 (11 Sep 2026) covers a service organisation's AI in SOC 1 and SOC 2 engagements, which bears on recordkeeper and TPA reliance [AICPA-TQA9561-2026]. No plan-audit-specific AI guidance was found.
- Data: plan audits hold participant personal data. Autire states US-only hosting, SOC 2 Type 2 controls and matching without Social Security numbers (vendor statements) [AUTIRE-SECURITY-2026].
- The ICPAS article cautions that time pressure can tempt auditors to rely too heavily on automated tools and that overreliance on service providers remained a deficiency theme [ICPAS-EBPQ-2024].

### Frontier signals (dated)

- 2026-01-23: AuditMiner predicts AI will touch plan audits even where firms do not adopt it, because sponsors and providers already use it; expects tighter accountability for outsourced work [AUDITMINER-PREDICT-2026] (vendor view).
- 2026-03-03: private-equity investor Serent Capital announces an investment in Autire, describing plan audits as historically manual and calling Autire an innovator; terms not disclosed [SERENT-AUTIRE-2026].
- 2026-05-04 to 06: AICPA Employee Benefit Plans Conference markets "AI integration"; agenda did not load [AICPA-EBP-2026].
- 2026-06-04: CalCPA conference ends with a session on incorporating AI into plan audits, framed as risk and reward [CALCPA-EBP-2026].
- 2026-06-11: Autire ships AI exception analysis [AUTIRE-ADVAI-2026].
- 2026-07-13: Citrin Cooperman announces adoption of the DAS suite including DAS EBP [CITRIN-DAS-2026].
- 2026-08-06: Thomson Reuters publishes the Kimberlin plan-document case [TR-KIMBERLIN-2026].
- 2026-09-11 and 2026-10-13: AICPA issues TQA 9561 and the AI practice aid [AICPA-TQA9561-2026; AICPA-AIPA-2026].
- 2026-10-15: Ledgerline's CEO writes about whole-population plan testing; the firm's site lists availability from 1 Dec 2026 [LEDGERLINE-CPAPA-2026; LEDGERLINE-SITE-2026].
- Direction: from sampling to whole-population testing, from request lists to data pulls, and from document reading to exception analysis. No regulator has endorsed or restricted any of it.

### Workforce and role effects

- Reviewers move from checklists and hunting for exceptions to judging exception patterns and giving clients fixes (Belfint) [AUTIRE-BELFINT-2026]; trainees ask tools routine questions, which reduces reliance on seniors (Kimberlin) [TR-KIMBERLIN-2026].
- Anders reports better job satisfaction and retention after automating repetitive setup [AUDITMINER-ANDERS-2025]. Belfint says new staff prefer the platform [AUTIRE-BELFINT-2026].
- Capacity: Belfint grew from about 100 to 160-170 plan audits (the vendor's case-study card says without adding headcount) [AUTIRE-BELFINT-2026; AUTIRE-HOME-2026]. Plan audits have concentrated into fewer, larger practices [BELFINT-DOLQ-2024].
- Vendors put former plan auditors in support roles, including inspection and peer review support [AUTIRE-ABOUT-2026; AUTIRE-COMPLIANCE-2026].
- Outsourced and offshore plan-audit support is growing, with supervision a concern [AUDITMINER-PREDICT-2026; AUDENZA-EBP-2026] (both vendors).

### Objections and concerns practitioners raise

- Whole-population testing is not a guarantee, and "we test everything" can widen the expectation gap [LEDGERLINE-CPAPA-2026].
- New findings on existing clients prompt "why was this missed before" questions [AUTIRE-REA-2026].
- Savings take time: Rea says 100 hours to 30 is not realistic overnight and that there is a learning curve [AUTIRE-REA-2026].
- Time pressure and overreliance on automated tools or service providers [ICPAS-EBPQ-2024].
- Documentation: AI tool use should be documented at firm and engagement level (Forvis Mazars, 2024) [JOFA-AAFOCUS-2024]; auditors need to document judgment against AI suggestions [AUDITMINER-PREDICT-2026].
- Participant personal data in third-party tools [AUTIRE-SECURITY-2026].
- Probabilistic AI in a setting where accuracy is non-negotiable (a vendor's argument for deterministic tests) [AUTIRE-AI-2026].

### Interview probes for an advisor

1. Which plan-audit steps still run on samples, and for what share of plans can you test the whole participant population? What exception and false-positive rates do you see, and who triages them?
2. How does participant, payroll and recordkeeper data reach you today (portal, email, direct connection)? Who checks completeness and accuracy of data a tool pulls?
3. How do you document the use of AI or automation on a plan file for peer review and DOL inspection? Has a reviewer or inspector ever asked?
4. How do you rely on recordkeeper and TPA SOC 1 reports, and do any of those providers disclose AI use in the services?
5. If hours per audit fall by a third, what happens to fees, staffing and referrals from TPAs and plan sponsors, and are you a specialist practice or a generalist one given the DOL volume pattern?

## 4. Routed to other modules

- Ledgerline's whole-population specialist-firm model: already recorded as `assurance-substantive-testing-25`; not duplicated here (sources LEDGERLINE-CPAPA-2026, LEDGERLINE-SITE-2026 are cited in 03, 06 and 10 only for the supporting detail).
- Reading third-party SOC 1 reports: overlaps `assurance-controls-testing-13`; an EBP-specific entry is kept here (07).
- SOC toolkits and the AICPA's September 2026 SOC AI Q&A: also belong to `soc-attestation` [AICPA-TQA9561-2026; AUDITMINER-SOC-2026].
- Firm-level AI tool governance, supervision and documentation (14): also belongs to `quality-management` [AICPA-AIPA-2026].
- Assessing recordkeepers' and TPAs' own AI (15) and any audit of AI used by plans for claims or benefit decisions: belongs to `assurance-over-ai`. A search summary mentioned a 2024 ERISA Advisory Council recommendation that plans disclose whether AI was used in a benefit determination; the report was not opened, so it is not cited.
- Prospecting and acceptance from Form 5500 data (13): also touches `acceptance-independence`.
- Evidence snipping in Excel for eligible-compensation validation (a DataSnipper case page names plan audits but is undated): belongs to `assurance-substantive-testing-14`.
- Form 5500 preparation, compliance testing and census scrubbing by TPAs and plan administrators (a Stax.ai page, undated, not cited): no module in this archetype; closest is a future plan-administration or tax compliance module.
- Outsourced and offshore plan-audit capacity: belongs to the archetype-level workforce and economics files.

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| AAFCPA-DOLQ-2024 | DOL Audit Quality Study Underscores the Need for Specialized EBP CPA | AAFCPAs | firm | https://www.aafcpa.com/?p=24524 | 2024-01-25 | full |
| AICPA-AIPA-2026 | Artificial Intelligence (AI) Considerations for Financial Statement Auditors: AICPA news release, read with the Journal of Accountancy report of 13 Oct 2026 | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/news/article/aicpa-releases-guidance-to-help-auditors-address-the-use-of-ai-in-financial-reporting-and-auditing | 2026-10-13 | full |
| AICPA-EBP-2026 | AICPA Employee Benefit Plans Conference 2026 (home page and pre-conference workshops page; agenda page did not load) | AICPA & CIMA | conference | https://events.aicpa-cima.com/EBP2026 | 2026-05 | full |
| AICPA-EBPAQC-TOOLS-2024 | EBPAQC tools that address 2023 DOL audit quality study deficiencies | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/resources/download/ebpaqc-tools-that-address-2023-dol-audit-quality-study-deficiencies | 2024-08-20 | full |
| AICPA-ONPOINT-2020 | OnPoint EBP Frequently Asked Questions | AICPA and CPA.com | professional-body | https://www.cpa.com/sites/cpa/files/2020-08/OnPoint_EBP_FAQs.pdf | 2020-08 | full |
| AICPA-TQA9561-2026 | TQA Section 9561 SOC Examinations: Effect of the Service Organization's Use of AI on SOC 1 and SOC 2 Examinations (resource landing page; document body not opened) | AICPA & CIMA | professional-body | https://www.aicpa-cima.com/resources/download/tqa-section-9561-soc-examinations-effect-of-the-service-organizations-use-of-ai-on-soc1-and-soc2-examinations | 2026-09-11 | full |
| AUDENZA-EBP-2026 | EBP Audit Guide 2026: Everything CPA Firms & Sponsors Need | Audenza Advisory | vendor | https://audenzaadvisory.com/employee-benefit-plan-audit-guide/ | 2026-07-27 | full |
| AUDITMINER-ANDERS-2025 | Driving Efficiency and Enhancing Staff Morale at Anders CPAs + Advisors (case study PDF; date from PDF creation metadata, 20 Jan 2025; text layer absent, read as page images) | AuditMiner | vendor | https://6703923.fs1.hubspotusercontent-na1.net/hubfs/6703923/Anders%20Case%20Study%202025.pdf | 2025-01 | full |
| AUDITMINER-PLANRES-2026 | EBP Plan Research (product page) | AuditMiner | vendor | https://www.auditminer.com/ebp-plan-research | 2026 | full |
| AUDITMINER-PREDICT-2026 | EBP Auditing Industry 2026: What Auditors Should Expect Next | AuditMiner | vendor | https://www.auditminer.com/post/ebp-audit-predictions-for-2026-what-2025-revealed-and-what-auditors-should-expect-next | 2026-01-23 | full |
| AUDITMINER-SITE-2026 | Audit Software to Scale Your EBP Practice (home page) | AuditMiner | vendor | https://www.auditminer.com/ | 2026 | full |
| AUDITMINER-SOC-2026 | SOC Report Toolkits for Auditors | AuditMiner | vendor | https://www.auditminer.com/soc-toolkits | 2026 | full |
| AUTIRE-ABOUT-2026 | Building the Future of EBP Audit (About) | Autire Technologies | vendor | https://autire.com/about | 2026 | full |
| AUTIRE-ADVAI-2026 | Advanced AI Is Live Along With Other Product Upgrades | Autire Technologies | vendor | https://autire.com/advanced-ai-live-product-upgrades-june-2026/ | 2026-06-11 | full |
| AUTIRE-AI-2026 | AI Built for EBP Audits (AI on Autire) | Autire Technologies | vendor | https://autire.com/platform/ai-on-autire | 2026 | full |
| AUTIRE-BELFINT-2026 | How Belfint, Lyons & Shuman Grew From 100 to 170 EBP Audits (case study) | Autire Technologies | vendor | https://autire.com/case-studies/belfint-lyons-shuman/ | 2026-08-30 | full |
| AUTIRE-BENCH-2024 | Autire Report Reveals CPA Firms Can Cut 401k Audit Hours in Half | Autire Technologies | vendor | https://autire.com/autire-report-reveals-cpa-firms-can-cut-401k-audit-hours-in-half/ | 2024-04-18 | full |
| AUTIRE-COMPLIANCE-2026 | Consistent Audits. Defensible Files. (For Compliance Leaders) | Autire Technologies | vendor | https://autire.com/compliance-leaders | 2026 | full |
| AUTIRE-CPAMERICA-2024 | Autire Partners with CPAmerica to Transform the EBP Auditing Process | Autire Technologies (CPAmerica announcement) | vendor | https://autire.com/autire-partners-with-cpamerica-to-transform-ebp-auditing-process/ | 2024-10-14 | full |
| AUTIRE-HOME-2026 | Autire: EBP Audit Software for CPA Firms (home page) | Autire Technologies | vendor | https://autire.com | 2026 | full |
| AUTIRE-REA-2026 | Rea Business Advisors Uses Full Population Testing to Gain the Upper Hand (case study) | Autire Technologies | vendor | https://autire.com/case-studies/rea-business-advisors/ | 2026-08-30 | full |
| AUTIRE-RISK-2024 | Autire Introduces First Audit Solution with Automated Risk Assessment, Transforming 401(k) Audit Compliance | Autire Technologies | vendor | https://autire.com/autire-transforms-401k-audit-compliance-with-automated-risk-assessment/ | 2024-12-02 | full |
| AUTIRE-SECURITY-2026 | Security and Compliance | Autire Technologies | vendor | https://autire.com/security | 2026 | full |
| AUTIRE-TESTING-2026 | Automated EBP Audit Testing (platform testing page) | Autire Technologies | vendor | https://autire.com/platform/testing | 2026 | full |
| AUTIRE-TRUSTREC-2026 | Built for EBP Audits: How Trust Reconciliation Works End to End on Autire | Autire Technologies | vendor | https://autire.com/trust-reconciliation-on-autire/ | 2026-07-31 | full |
| BELFINT-DOLQ-2024 | The 2023 DOL Audit Quality Study: Slight Improvements, but Audit Quality is Still Concerning | Belfint, Lyons & Shuman (firm blog) | firm | https://employeebenefitplanaudit.belfint.com/2023-dol-audit-quality-study/ | 2024-03-07 | full |
| CALCPA-EBP-2025 | Employee Benefit Plans Audit Virtual Conference 2025 (session list) | CalCPA | conference | https://store.calcpa.org/catalog/activity/employee-benefit-plans-audit-virtual-conference-2025---1000003879 | 2025-06-05 | full |
| CALCPA-EBP-2026 | Employee Benefit Plans Audit Virtual Conference 2026 (session list) | CalCPA | conference | https://store.calcpa.org/catalog/activity/employee-benefit-plans-audit-virtual-conference-2026---1000004674 | 2026-06-04 | full |
| CASEWARE-DASEBP-2026 | DAS EBP (formerly OnPoint EBP) product page | Caseware | vendor | https://www.caseware.com/us/products/das-ebp | 2026 | full |
| CITRIN-DAS-2026 | Citrin Cooperman & Company, LLP Adopts AI-Enabled DAS Suite Powered by Caseware to Advance Audit Quality, Professional Development, and Scalable Growth | Caseware (press release) | vendor | https://www.caseware.com/news/citrin-cooperman-company-llp-adopts-ai-enabled-das-suite-powered-by-caseware-to-advance-audit-quality-professional-development-and-scalable-growth | 2026-07-13 | full |
| EBSA-AUDITQ-2023 | Audit Quality Study (EBSA Office of the Chief Accountant), November 2023 | US Department of Labor, EBSA | regulator | https://www.dol.gov/sites/dolgov/files/ebsa/about-ebsa/our-activities/resource-center/publications/november-2023-audit-quality-study.pdf | 2023-11 | search-only |
| EBSA-AUDITQ-2025 | ERISA Covered Employee Benefit Plans Audit Quality (secondary summary of the 2023 EBSA study) | Jones & Roth CPAs & Business Advisors | firm | https://www.jrcpa.com/?p=24899 | 2025-12-03 | full |
| ICPAS-EBPQ-2024 | Enhancing Employee Benefit Plan Audit Quality (Andrea Wright, Johnson Lambert) | Illinois CPA Society, Insight magazine (Spring 2024 issue) | professional-body | https://www.icpas.org/resources/publications/insight-magazine/article-search/detail/spring-2024/enhancing-employee-benefit-plan-audit-quality | 2024 | full |
| JOFA-AAFOCUS-2024 | A&A Focus recap: Top A&A and employee benefit plan issues | Journal of Accountancy (AICPA) | press | https://www.journalofaccountancy.com/newsletters/a-a-focus/a-a-focus-recap-top-a-a-and-employee-benefit-plan-issues.html | 2024-06-26 | full |
| LEDGERLINE-CPAPA-2026 | Testing Every Transaction Changes the Audit - Here's What Firms Should Know Before They Sell It (Tunde Adewole, CEO of Ledgerline) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/ | 2026-10-15 | full |
| LEDGERLINE-SITE-2026 | Ledgerline: Specialist 401(k) and 403(b) plan audits | Ledgerline | firm | https://ledgerlineaudit.com | 2026-10 | full |
| METZ-EBPAUDITAI-2026 | EBPAudit.ai: Employee Benefit Plan Audits by Metz CPA, PLLC | Metz CPA, PLLC | firm | https://ebpaudit.ai/ | 2026 | full |
| PSCA-AIRK-2026 | AI May Help Modernize Retirement Plan Recordkeeping (seen in search results only; page returned 403) | Plan Sponsor Council of America | professional-body | https://www.psca.org/news/psca-news/2026/8/ai-may-help-modernize-retirement-plan-recordkeeping/ | 2026-08 | search-only |
| SERENT-AUTIRE-2026 | Serent Capital Invests in Autire, a Cloud-Based and AI-Powered Platform Supporting CPA Firms in Employee Benefit Plan Audits | Serent Capital (Business Wire release, 3 Mar 2026) | press | https://serentcapital.com/insights/serent-capital-announces-investment-in-autire-a-cloud-based-and-ai-powered-platform-supporting-cpa-firms-in-employee-benefit-plan-audits-2/ | 2026-03-03 | full |
| SIKICH-BROCHURE-2026 | Employee Benefit Plan Audits (brochure, file code SKCH_0726) | Sikich | firm | https://www.sikich.com/wp-content/uploads/2026/09/Employee-Benefit-Plan-Audit-Brochure_SKCH_0726.pdf | 2026 | full |
| SIKICH-WEBINAR-2025 | Roses are Red, Audits are Due: Strategies for Employee Benefit Plan Audit Filing Success (webinar listing) | Sikich | conference | https://go.sikich.com/roses-are-red-audits-are-due-webinar-february2025.html | 2025-02-12 | full |
| TR-KIMBERLIN-2026 | How Kimberlin Company accelerated 401(k) audits with CoCounsel Audit (case study) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/insights/case-studies/how-kimberlin-company-accelerated-401-k-audits-with-cocounsel-audit | 2026-08-06 | full |
| TR-SENSIBA-2026 | How Sensiba boosts audit efficiency with CoCounsel Audit (case study) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/insights/case-studies/accelerating-audit-efficiency-how-sensiba-llp-streamlined-technical-research-and-document-management-with-cocounsel-audit | 2026-01-06 | full |
| TRULLION-EBP-2025 | Employee Benefits Audit Software Powered by AI (blog) | Trullion | vendor | https://trullion.com/blog/ebp-audit-software-ai-automation/ | 2025-04-27 | full |
| TSCPA-PEERREVIEW-2025 | Annual Report on Peer Review Activities 2025 | Tennessee Society of CPAs | professional-body | https://tscpa.com/wp-content/uploads/2026/03/Annual-Report-on-Peer-Review-Activities-2025-final.pdf | 2026-03-31 | full |

## 6. Gaps

**Blocked, unread or unverified**
- DOL EBSA November 2023 audit quality study: dol.gov returned 403 for the PDF and every related page, and the r.jina.ai mirror was blocked. All study figures come from Belfint, AAFCPAs, ICPAS and the AICPA's EBPAQC page. Belfint's text says 307 plans, its table totals 308; the by-area rates have no stated denominator. Check the primary PDF before quoting any figure to a client.
- No 2025 or 2026 EBSA follow-up study, no EBSA Office of the Chief Accountant speech and no EBSA statement on AI in plan audits were found.
- AICPA Employee Benefit Plans Conference 2026 agenda and speaker pages load by JavaScript; no session list was read. CalCPA's session on AI was read as an abstract only; no slides or content. A Virginia society listing of a session called "From Excel to AI" (search result only) returned 404 and is not cited.
- AICPA TQA 9561 and the practice aid: the landing page and news release were read, not the documents themselves.
- PSCA article on AI and recordkeeping (search summary only; 403). A Moss Adams (now Baker Tilly) December 2025 plan-audit panel was named in a search summary; its page returned 404.
- Undated pages not used as sources: the Whitley Penn DataSnipper case (names plan audits, no date), a Stax.ai article on AI for TPAs, and AuditMiner and Autire product pages whose dates are the copyright year only.
- Peer review: no confirmation that the AICPA Peer Review Board changed its plan-audit requirements after the 2023 study; the Tennessee report is one state's small sample.

**Absent, as far as public sources show**
- Any independent measure of AI quality in plan audits: error rates, override rates, parallel-run or shadow-mode results, miss rates after whole-population testing, or inspection findings that mention AI. Every figure is self-reported or vendor-published.
- Any account from a regional or local firm that is not authored or hosted by a vendor.
- Any AI evidence for defined benefit plan audits (actuarial data), health and welfare plan audits, multiemployer plans or full-scope investment testing.
- Academic studies: a search for peer-reviewed work on plan audit quality and technology returned only agency, trade and news items.
- Podcasts, community threads and job postings about AI in plan audits: not found (the landscape found Reddit-type communities return 403 and they were not retried; one job-posting search returned vendor and firm pages instead).
- Pricing and fee effects of faster plan audits beyond the vendor claim that tool-supported audits are more profitable [AUTIRE-BELFINT-2026].
- Whether the "zero peer review or DOL findings attributed to Autire" claim can be checked: no public source says whether findings record the tool used.
