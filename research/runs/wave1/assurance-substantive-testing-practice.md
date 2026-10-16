# Module deep dive: assurance / substantive-testing / practice

- **Archetype:** assurance
- **Module:** substantive-testing. Substantive procedures on balances and transactions: journal-entry and fraud testing, substantive analytics, document matching and vouching, confirmations, revenue and inventory testing, support for testing accounting estimates, sampling versus full-population testing, contract review.
- **Angle:** practice. What firms actually do: named deployments, firm platforms and agents, vendor tools with named customers, measured outcomes, workflow and role changes.
- **Prepared:** 2026-10-16
- **Method note:** Pages were fetched and read with `curl` through the session proxy (`pdftotext` for PDFs). Where a host refused `curl` (MindBridge, Springer, pcaobus.org), the `r.jina.ai` text mirror was used and the source is marked `access: full` only where the relevant text was actually returned. The web-search quota ran out after the first round of searches, so later leads were followed by links only (see Gaps). **Almost every outcome figure below is self-reported by a firm or published by a vendor.** The only independent measures are regulator frequency counts (IFIAR), a regulator-independent benchmark survey (CPA.com, 54 firms), an academic drone-count study on livestock, and an academic study of AI investment and audit outcomes. No independent measure of the accuracy of any substantive-testing tool in live audits was found.

---

## 1. Summary

- **Journal-entry testing is the only substantive area where tool use is close to universal, and it is the best-evidenced.**
  - IFIAR members reported frequently seeing automated tools in journal-entry testing in 88% of 48 responding members in 2024, against 55% for substantive procedures such as revenue and inventory and 43% for internal-controls testing (IFIAR-TTF-2025).
  - Named deployments: Buzzacott started its MindBridge programme with journal entries (BUZZACOTT-PRIME-2025). BDO UK expanded MindBridge across its audit practice after a trial, announced 29 Jun 2026 (MINDBRIDGE-BDOUK-2026). EY says Canvas processes more than 1.4 trillion journal-entry lines a year (EY-CANVAS-2026).
  - No firm has published detection-quality figures such as false-positive rates or exceptions confirmed as misstatements.
- **Evidence-to-sample matching ("vouching") is where the new agent products are concentrated, and where the only per-task time figures are.**
  - Named firms and figures: FGMK reports testing per selection falling from 30–45 minutes to about five (DATASNIPPER-CONNECT-2026). The owner of a Kentucky firm (Oberlander Financial Services) reports 16 hours falling to five or six per engagement on Thomson Reuters Audit Intelligence Test (TR-AGENTIC-2025). Sanville & Co says sample selections of hundreds of transactions went from hours to minutes in many cases (FIELDGUIDE-SANVILLE-2026).
  - Big Four firms name the tools but publish no figures. PwC Evidence Match covers cash, receivables, payables and fixed assets (CFOBREW-PWC-2025). KPMG Clara agents cover expense vouching and unrecorded-liability search (KPMG-CLARA-2025).
- **The Big Four's own read on payoff is cautious.** A year into its programme, PwC's US assurance transformation leader says time savings are "not that drastic yet" and that busy-season effort has shifted only modestly (CFODIVE-PWC-2026). EY says its multi-agent framework is in all audit phases now and expects end-to-end support by 2028 (EY-CANVAS-2026).
- **Confirmations are the most automated step in small and mid-size practices, but mostly through workflow platforms rather than AI.** 39% of 54 US firms in the CPA.com benchmark have an automated confirmation solution, against 11% for substantive analytics (CPACOM-ATR-2025). Circit's named firm cases report time and response-rate gains (CIRCIT-MOORE-2026, CIRCIT-BEEVER-2026).
- **Full-population testing is a stated direction more than a measured practice.**
  - Stated direction: PwC Australia piloted an "AI-native" platform on five audit clients and plans all clients by 2028 (PWCAU-AT-2025). BDO NL states an ambition to replace sampling with 100% testing, enabled by direct bank data (CIRCIT-RABOBANK-BDONL-2026). A specialist 401(k) audit firm argues that testing every transaction raises exceptions and an expectation-gap risk (LEDGERLINE-CPAPA-2026).
  - Standard-setters have not required it. IAASB's exposure drafts say GenAI tools challenge the "input-output" model of audit evidence and choose guidance over a technology requirement (IAASB-ED500-2026, EM paras 65–71).
- **Regulators' observed problems are about use, not about the tools' existence.** 31% of IFIAR members reported findings that tools were not used as intended in 2024 (29% in 2023). The most common findings were misinterpreting tool results and the extent of testing of outliers (IFIAR-TTF-2025, p.5). The FRC warns that an auditor may read a contract-screening output as a complete review (FRC-GENAI-2026, p.18).
- **Roles are shifting at the edges.**
  - Staff and skills: PwC is hiring engineers into assurance and wants dual-track CPA and data-science recruits (PWC-AT-2025). A boutique firm says first-year staff now do complex revenue testing because reviewers have time to guide them (FIELDGUIDE-SANVILLE-2026). An FT analysis found AI-skilled roles were almost 7% of Big Four job postings in 2025 against just under 3% for audit roles (COMPUTERWORLD-FT-2026).
  - Evidence base: the only independent study of workforce effect is pre-GenAI. It links AI investment to fewer accounting employees after three to four years (FEDYK-2022).
- **Thin spots.** Inventory observation has only 2018–2021 evidence. Contract review has only a regulator's hypothetical example and one unnamed-customer vendor figure. Estimates testing is covered in the specialists module (see section 4).

---

## 2. Use cases

```yaml
- id: assurance-substantive-testing-01
  title: Full-population journal-entry analytics and anomaly scoring (fraud and management-override testing)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Journal-entry testing responds to the risk of management override. Selecting entries from ledgers with very
    large line counts relies on filters and auditor judgment, and rule-based tests produce many false positives
    (ARXIV-AUDITCOPILOT-2025, abstract). Large general ledgers held across many Excel files make sampling,
    searching and navigating slow (BUZZACOTT-PRIME-2025).
  solution: >-
    Machine-learning and statistical scoring of every ledger entry, with drill-down by account, period and risk
    attribute, so that auditors select entries for testing from scored populations. Named users: Buzzacott (started
    its MindBridge programme with journal entries), BDO UK (expanded across its audit practice after a trial, June
    2026), KPMG (MindBridge alliance feeding Clara, 2024) and EY (a general-ledger analyzer used in most audits per
    its assurance digital leader in 2024, with anomaly detection being embedded).
  outcomes:
    - lever: quality
      description: Regulator-observed adoption. This is a prevalence measure, not an outcome measure.
      figure: "88% of responding members in 2024 (86% in 2023)"
      measures: >-
        Share of the 48 IFIAR members answering the 2024 survey that "frequently observed" automated tools and
        techniques in journal entry testing in audit files (2023 column: 49 members answered)
      provenance: independent
      source_ref: IFIAR-TTF-2025
    - lever: capacity
      description: Scale of journal-entry data processed on the firm platform. Volume only; no time or quality result is given.
      figure: "more than 1.4 trillion lines a year"
      measures: >-
        Lines of journal-entry data processed per year on EY Canvas, per the press report of EY's 7 Apr 2026 release
        (the 2024 interview gave "more than 800 billion line items of general ledger data" a year for the GL analyzer)
      provenance: self-reported
      source_ref: EY-CANVAS-2026
  prerequisites:
    - A complete general-ledger extract reconciled to the trial balance, loaded in one place (BUZZACOTT-PRIME-2025).
    - A technical committee or equivalent that owns standards mapping, methodology and policy (BUZZACOTT-PRIME-2025).
    - Access to client systems and clean client data, which 60% and 53% of US firms rank as blockers (CPACOM-ATR-2025, Theme 1 chart).
  risks_and_guardrails:
    - 31% of IFIAR members reported findings that tools were not used as intended in 2024; the common findings were misreading results and thin testing of outliers (IFIAR-TTF-2025, p.5).
    - Buzzacott teams routinely run datasets with and without the tool to check findings against professional expectations (BUZZACOTT-PRIME-2025).
    - Under the IAASB exposure draft, items that look unusual for the population need further investigation, with the extent depending on the purpose of the procedure (IAASB-ED500-2026, EM paras 63–64).
  human_checkpoints:
    - Auditor sets control-point weightings and decides how scored results are applied (BUZZACOTT-PRIME-2025).
    - Auditor investigates flagged entries and decides what is a misstatement (IAASB-ED500-2026, EM para 64).
  role_evolution: >-
    Buzzacott reports buy-in from new joiners to partners (BUZZACOTT-PRIME-2025). RSM Australia describes the role
    moving from selecting samples to investigating and understanding exceptions, so that quality depends on how
    exceptions are triaged (RSM-AUS-2026).
  evidence_grade: B
  sources:
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: "2025-03-27", access: full, locator: "Insights from IFIAR Members, p.5 (table, 2024 and 2023)" }
    - { ref: EY-CANVAS-2026, title: "EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/", date: "2026-04-07", access: full, locator: "para 2" }
    - { ref: ACCTODAY-EY-2024, title: "EY beefs up use of AI amid $1B investment", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/ey-beefs-up-use-of-ai-amid-1b-investment", date: "2024-10-16", access: full, locator: "paras 3–4 (Jeschonneck on the GL analyzer)" }
    - { ref: BUZZACOTT-PRIME-2025, title: "How Buzzacott's AI partnership is elevating audit quality", publisher: PrimeGlobal (Buzzacott), type: firm, url: "https://www.primeglobal.net/news/how-buzzacotts-ai-partnership-is-elevating-audit-quality", date: "2025-12-18", access: full, locator: "sections 'Implementation' and 'Building trust'" }
    - { ref: MINDBRIDGE-BDOUK-2026, title: "BDO UK and MindBridge Partner to Accelerate Data-Driven Audit", publisher: MindBridge, type: vendor, url: "https://www.mindbridge.ai/news/bdo-uk-and-mindbridge-partner-to-accelerate-data-driven-audit", date: "2026-06-29", access: full, locator: "paras 2–3" }
    - { ref: MINDBRIDGE-KPMG-2024, title: "Innovating Audits: KPMG's AI-Driven Audit Approach Leveraging MindBridge AI", publisher: MindBridge, type: vendor, url: "https://www.mindbridge.ai/docs/resources/customer-stories/KPMG/KPMG-AI-Driven-Audit-with-MindBridge_02262024.pdf", date: "2024-02", access: full, locator: "pp.4–5 (date taken from the file name)" }
    - { ref: RSM-AUS-2026, title: "AI in Audit and Accounting Firms: Use Cases and Risks", publisher: RSM Australia, type: firm, url: "https://www.rsm.global/australia/insights/what-role-ai-audit-and-accounting-firms", date: "2026-08", access: full, locator: "section 'Fieldwork', first paragraph" }
    - { ref: IAASB-ED500-2026, title: "Explanatory Memorandum to the ED for Proposed ISA 500 (Revised), Audit Evidence", publisher: IAASB, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf", date: "2026-08-05", access: full, locator: "Section 1-E, paras 63–64" }
  last_reviewed: "2026-10-16"
  notes: >-
    No detection-quality, false-positive or override-rate figure was found for any named firm. The MindBridge page
    for KPMG describes the alliance, not results. An undated EY page on its Helix GL Anomaly Detector (a pilot on
    about 20 engagements in FY18, tested against planted fraudulent entries) was read but not cited because its
    date could not be established.

- id: assurance-substantive-testing-02
  title: "Idea: LLM-based anomaly detection with written explanations for journal-entry tests"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance]
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Rule-based journal-entry tests generate overwhelming false positives and miss subtle irregularities, and
    machine-learning scores do not explain themselves (ARXIV-AUDITCOPILOT-2025, abstract).
  solution: >-
    A language model scores ledger records as anomalous and writes a natural-language explanation for each, so an
    auditor can review the reasoning. Researchers benchmarked open models (named in the abstract as LLaMA and Gemma)
    against rule-based journal-entry tests and classical machine-learning baselines.
  outcomes:
    - lever: quality
      description: >-
        Authors report that the models consistently outperformed rule-based tests and classical baselines on
        synthetic and anonymised real ledgers. Metrics are not in the abstract. No firm deployment found.
      figure: "none published in the abstract"
      measures: "Benchmark comparison on synthetic and anonymised real-world ledgers, per the abstract; not a live audit"
      provenance: independent
      source_ref: ARXIV-AUDITCOPILOT-2025
  prerequisites:
    - Ledger data that can be shared with a model under client-confidentiality terms.
    - A firm-side test set to measure precision on its own ledgers before relying on it.
  risks_and_guardrails:
    - Evidence is a benchmark on synthetic and anonymised ledgers, not live audit results (ARXIV-AUDITCOPILOT-2025).
    - Agent benchmarks on whole engagements find models sometimes perform inappropriate procedures or write incorrect documentation (ARXIV-FAB-2026, abstract).
  human_checkpoints:
    - Auditor reviews the explanation and the entry before treating an entry as an exception.
  role_evolution: >-
    None published. The abstract pictures auditors collaborating with models rather than being replaced
    (ARXIV-AUDITCOPILOT-2025).
  evidence_grade: D
  sources:
    - { ref: ARXIV-AUDITCOPILOT-2025, title: "AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping", publisher: arXiv (Kadir et al.), type: academic, url: "https://arxiv.org/abs/2512.02726", date: "2025-12-02", access: full, locator: "abstract" }
    - { ref: ARXIV-FAB-2026, title: "FinancialAuditBench: Benchmark Construction under Differential Privacy Using Real-World Priors", publisher: arXiv, type: academic, url: "https://arxiv.org/abs/2609.32835", date: "2026-09-26", access: full, locator: "abstract" }
  last_reviewed: "2026-10-16"
  notes: >-
    Idea: discussed by researchers only. No public deployment found. The landscape's extract about a sharp fall in
    real-data precision without a statistical hint was not in the abstract and is not used.

- id: assurance-substantive-testing-03
  title: KPMG Clara agents for expense vouching and unrecorded-liability search
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Vouching expenses and searching for unrecorded liabilities are repetitive, document-heavy substantive
    procedures that use large amounts of staff time (KPMG-CLARA-2025).
  solution: >-
    KPMG announced AI agents in its Clara platform that support and automate parts of substantive procedures,
    including expense vouching and the search for unrecorded liabilities and accrued expenses. It said more agents
    would follow within 12 months, integrated into controls testing and financial statement analysis.
  outcomes:
    - lever: capacity
      description: >-
        None published. The release states an aim to empower more than 95,000 auditors; it gives no usage, time or
        quality figure.
      figure: "none published"
      measures: "Not applicable; the 95,000 is the auditor population the deployment is aimed at, not users or an effect"
      provenance: self-reported
      source_ref: KPMG-CLARA-2025
  prerequisites:
    - Engagement documentation and methodology inside the Clara platform (KPMG-CLARA-2025).
    - Upskilling of professionals to keep professional skepticism (KPMG-CLARA-2025).
  risks_and_guardrails:
    - KPMG says auditors stay in control of decision-making, with a human in the loop (KPMG-CLARA-2025).
    - The promised follow-on agents for controls testing were not confirmed as released in any source read.
  human_checkpoints:
    - Auditor decides and keeps professional skepticism; agents give recommendations from data analysis (KPMG-CLARA-2025).
  role_evolution: >-
    KPMG says agents free auditors for high-risk areas and sector-specific challenges and that it is upskilling
    staff (KPMG-CLARA-2025).
  evidence_grade: C
  sources:
    - { ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html", date: "2025-04-22", access: full, locator: "Highlights; paras 4–6" }
    - { ref: ACCTODAY-KPMG-2025, title: "KPMG builds AI agents into audit platform", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/kpmg-builds-ai-agents-into-audit-platform", date: "2025-04-24", access: full, locator: "para 2" }
  last_reviewed: "2026-10-16"
  notes: >-
    The release describes agents as deployed, but no usage figure, customer, inspection comment or outcome was
    found 18 months later, so the use is graded as announced. A Bloomberg Tax headline of 1 Apr 2026 ("KPMG to
    Test Advanced AI Agents in Next Phase") appears in the landscape; its text was not opened.

- id: assurance-substantive-testing-04
  title: PwC Evidence Match for matching and validating evidence in cash, receivables, payables and fixed assets
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Auditors spend much of substantive testing gathering information from the client, matching it to systems,
    and tracing and tying it, before they reach the differences where judgment adds value (CFOBREW-PWC-2025).
  solution: >-
    An agent-led module extracts and matches evidence against documents. PwC says it ingests about 20 kinds of
    document, connects to PwC's assurance skills library, and leaves a clear evidence trail for each match. Its
    partner expects to use something like it in all areas of substantive testing.
  outcomes:
    - lever: quality
      description: >-
        PwC's US assurance AI leader says accuracy is the success measure for Evidence Match, because a match is a
        yes-or-no result. No accuracy figure is published.
      figure: "none published"
      measures: "Not applicable; PwC names the measure (accuracy of match decisions) but publishes no value"
      provenance: self-reported
      source_ref: CFOBREW-PWC-2025
  prerequisites:
    - Ability to ingest the full variety of client documents, "20 different kinds" per PwC (PWC-AT-2025).
    - Integration with PwC's assurance skills library (PWC-AT-2025).
  risks_and_guardrails:
    - PwC says it measures usefulness and performance over time and will move off a tool if it stops helping (CFOBREW-PWC-2025).
    - Matching outputs on external information the client supplies electronically fall under the PCAOB requirement to evaluate source and handling of that information (PCAOB-PS2025-004, para .10A).
  human_checkpoints:
    - Auditors analyse the anomalies and differences that matching surfaces (CFOBREW-PWC-2025).
  role_evolution: >-
    PwC says AI systems need significant expertise to build, test and monitor, so some people move into those
    roles. It is hiring engineers it would not previously have hired into assurance (CFOBREW-PWC-2025, PWC-AT-2025).
  evidence_grade: B
  sources:
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: "2025-10-28", access: full, locator: "paras on Evidence Match (Maryanski) and on hiring (Panson)" }
    - { ref: CFOBREW-PWC-2025, title: "A look at PwC's 'next generation' audit", publisher: CFO Brew, type: press, url: "https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit", date: "2025-11-05", access: full, locator: "paras 5–7 and 'ROI' paragraphs (Kosar)" }
    - { ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: "2026-10-07", access: full, locator: "paras 3–9" }
    - { ref: PCAOB-PS2025-004, title: "Policy Statement Regarding Implementation of Paragraph .10A of AS 1105, Audit Evidence (Release 2025-004)", publisher: PCAOB, type: regulator, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/rulemaking/docket-052/pcaob-release-no-2025-004.pdf", date: "2025-09-18", access: full, locator: "p.1 and footnote 2 (text of paragraph .10A)" }
  last_reviewed: "2026-10-16"
  notes: >-
    The CFO Brew article describes eight tools "either currently in use or in the pilot phase" without saying which;
    Accounting Today says PwC "already has" Evidence Match, so in-production is PwC's own claim. In Oct 2026 PwC
    said its Simplified Audit - Execute tool reads supporting documents and flags missing information, and that for
    2026 year-end audits it would use it; this may overlap with this use case but the source does not say
    (CFODIVE-PWC-2026). The firm-wide statement that savings are "not that drastic yet" is not specific to Evidence Match.

- id: assurance-substantive-testing-05
  title: Thomson Reuters Audit Intelligence Test for matching samples to evidence and bank activity
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Matching each selected sample to its supporting evidence, and tracing recorded transactions to bank activity,
    is manual and time-consuming. A single customer payment can cover several invoices (TR-AGENTIC-2025).
  solution: >-
    AI automates the matching and documenting of samples to evidence and checks whether amounts were collected, by
    tracing accounting transactions to banking activity, including one payment matched to several invoices. It was
    built with Valid8 Financial, whose technology came from transaction advisory, forensic and financial-crime work.
  outcomes:
    - lever: speed
      description: "A named sole practitioner reports engagement time for organising client material and running tests falling from about two days to five or six hours"
      figure: "about 16 hours down to 5–6 hours per engagement"
      measures: >-
        Oberlander Financial Services PLLC's own estimate, quoted in the vendor's press release, of the time per
        engagement for organising client materials and running tests before and after; no sample, method or
        number of engagements stated
      provenance: vendor-published
      source_ref: TR-AGENTIC-2025
  prerequisites:
    - Client accounting data and bank-activity data to trace against (TR-AGENTIC-2025).
    - Use alongside Audit Intelligence Analyze for sample selection, per the same customer (TR-AGENTIC-2025).
  risks_and_guardrails:
    - Release gives no accuracy, false-match or override rate (TR-AGENTIC-2025).
    - Outputs on company-supplied external information need source and process understanding under PCAOB paragraph .10A (PCAOB-PS2025-004).
  human_checkpoints:
    - Auditors review the matches and documented results; the product is described as supporting standardised procedures and documentation (TR-AGENTIC-2025).
  role_evolution: >-
    The customer frames the gain as time freed per engagement. No role change is described
    (TR-AGENTIC-2025).
  evidence_grade: A
  sources:
    - { ref: TR-AGENTIC-2025, title: "Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html", date: "2025-11-05", access: full, locator: "section 'Introducing New AI-powered Audit Solutions'; Notes to Editors (availability)" }
  last_reviewed: "2026-10-16"
  notes: >-
    Graded A because a named organisation gives a before-and-after figure, but the figure is one sole
    practitioner's estimate published by the vendor (n = 1, no method). The release says the product was in an early
    adopter programme in the US with general availability planned for November 2025, hence piloting. The
    engagement is not described as controls or substantive, but the product traces samples to evidence and bank activity.

- id: assurance-substantive-testing-06
  title: Firm-built Excel agents for cash, journal-entry and financial-statement testing (FGMK on DataSnipper)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Testing each selection means locating the right evidence, extracting values and comparing them with what was
    recorded. Preparers build workpapers by hand and reviewers re-check them (DATASNIPPER-CONNECT-2026).
  solution: >-
    FGMK built agents in DataSnipper Excel Agents for cash testing, journal entry testing and financial statement
    testing, and used them on busy-season work. Preparer-side agents build workpapers and snip source evidence.
    Reviewer-side agents check consistency across a workbook and check that financial statements roll up.
    FGMK's QC department also runs financial statements through an agent alongside its own review. In 2026 FGMK
    joined the design-partner programme for Alwin, a cloud agent platform launched 22 Sep 2026 that runs whole
    procedures across hundreds of documents with every step logged.
  outcomes:
    - lever: speed
      description: "DataSnipper reports that Excel Agents cut FGMK's testing time per selection from 30–45 minutes to about five"
      figure: "30–45 minutes down to about 5 minutes per selection (roughly 85%)"
      measures: >-
        Testing time per selection at FGMK, before and after Excel Agents, as reported in DataSnipper's recap of its
        2026 New York event; the test type, sample and measurement method are not stated
      provenance: vendor-published
      source_ref: DATASNIPPER-CONNECT-2026
  prerequisites:
    - Agents built and approved by the firm, with control over who can create and who can use them (DATASNIPPER-FGMK-2026).
    - A contract term that client information does not train the models (DATASNIPPER-FGMK-2026).
    - Source documents the agent can snip, so every number traces to its source (DATASNIPPER-ALWIN-2026).
  risks_and_guardrails:
    - Every agent is versioned and approved before it runs; every result traces to its source document and the auditor signs off (DATASNIPPER-CONNECT-2026).
    - FGMK still reviews everything itself; the review agents are a second pass (DATASNIPPER-FGMK-2026).
  human_checkpoints:
    - Auditor signs off at the end; review notes are left on cells and sent in batches (DATASNIPPER-FGMK-2026).
  role_evolution: >-
    FGMK splits agents by role (preparer, reviewer, QC) and manages who builds them (DATASNIPPER-FGMK-2026).
    Preparers become builders of reusable agents ("Chat into Agent" turns a working conversation into a reusable
    agent).
  evidence_grade: A
  sources:
    - { ref: DATASNIPPER-CONNECT-2026, title: "DataSnipper Connect New York 2026: 6 Takeaways on AI and Auditing", publisher: DataSnipper, type: conference, url: "https://www.datasnipper.com/resources/the-6-biggest-takeaways-from-datasnipper-connect-new-york-2026", date: "2026", access: full, locator: "Takeaway 1 (page undated; refers to a September 2026 release, so published after Aug 2026)" }
    - { ref: DATASNIPPER-FGMK-2026, title: "FGMK Uses Alwin to Automate Larger, More Complex Audit Work Securely", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/fgmk-alwin-success-story", date: "2026", access: full, locator: "'Taking audit automation further' and Q&A (page undated; after Alwin's 22 Sep 2026 launch)" }
    - { ref: DATASNIPPER-ALWIN-2026, title: "DataSnipper Launches Alwin: End-to-End Agentic Automation for Audit & Finance", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/datasnipper-launches-alwin-end-to-end-agentic-automation-for-audit-finance", date: "2026-09-22", access: full, locator: "paras 1–3 (Robbins, FGMK)" }
  last_reviewed: "2026-10-16"
  notes: >-
    Graded A on one named firm's before-and-after figure, vendor-published, with no method. Alwin itself is an
    announced product (22 Sep 2026); FGMK is a design partner. DataSnipper's vendor claims (more than 600,000
    users in 175 countries, all Big Four as customers, $1.4B of productivity savings in 2025) are in
    DATASNIPPER-CHILE-2026 and DATASNIPPER-PRODUCTIVITY-2026 and are not independently measured.

- id: assurance-substantive-testing-07
  title: Excel-embedded evidence snipping and AI extraction for tie-out and vouching (DataSnipper)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Auditors reconcile numbers from invoices, bank statements and inventory documents to transactions by hand,
    and reviewers must re-find the evidence; DataSnipper's customer story describes reviewers instead clicking
    through to the source (DATASNIPPER-ODP).
  solution: >-
    The auditor "snips" values from source documents into Excel, where they reconcile to the transaction and keep
    a link to the source. AI Extractions and DocuMine add extraction from unstructured documents across languages
    and a document question-and-answer tool. DataSnipper says AI pre-validated more than two million data points
    from client-provided documents in 2025 through its PBC product.
  outcomes:
    - lever: cost
      description: >-
        DataSnipper cites a UK Parliament Public Accounts Committee hearing as referencing the National Audit Office
        as reporting efficiency savings and routine audit work completed up to three times faster.
      figure: "£400,000 of efficiency savings; routine audit work up to three times faster"
      measures: >-
        Figures that DataSnipper attributes to the NAO via a PAC hearing on the NAO Annual Report; the work covered,
        the baseline and the period are not stated, and the hearing record was not opened
      provenance: vendor-published
      source_ref: DATASNIPPER-PRODUCTIVITY-2026
    - lever: capacity
      description: "Volume of client-document data points pre-validated by AI in the vendor's PBC product in 2025"
      figure: "more than 2 million data points"
      measures: "Data points from client-provided documents that DataSnipper says its AI pre-validated across customers in 2025; not audit-quality or accuracy"
      provenance: vendor-published
      source_ref: DATASNIPPER-PRODUCTIVITY-2026
  prerequisites:
    - Working papers in Excel and source documents that can be loaded to the tool.
    - Regional data residency for enterprise customers (DataSnipper says it added U.S., EU and Australian data centres, DATASNIPPER-PRODUCTIVITY-2026).
  risks_and_guardrails:
    - Every number traces to its snip, giving reviewers a visible trail (DATASNIPPER-ALWIN-2026).
    - A firm's own written position on evidence of this kind still needs the source-reliability analysis of PCAOB paragraph .10A for company-provided external information (PCAOB-PS2025-004).
  human_checkpoints:
    - Auditor selects and snips the evidence; reviewer clicks through to the source (DATASNIPPER-ODP).
  role_evolution: >-
    Vendor says the audience widened in 2025 from external audit to internal audit and corporate finance, with new
    corporate customers up nearly 100% year over year (DATASNIPPER-PRODUCTIVITY-2026).
  evidence_grade: B
  sources:
    - { ref: DATASNIPPER-PRODUCTIVITY-2026, title: "DataSnipper Delivers $1.4B in Productivity Savings in 2025 as Audit and Finance Enter the AI Era", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/datasnipper-delivers-1-4b-in-productivity-savings-in-2025-as-audit-and-finance-enter-the-ai-era", date: "2026-01-14", access: full, locator: "sections 'Scaling AI-Powered Workflows Globally' and 'Measurable Productivity Savings'" }
    - { ref: DATASNIPPER-CHILE-2026, title: "DataSnipper Brings AI-Powered Audit Technology to Chile", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/datasnipper-brings-ai-powered-audit-technology-to-chile", date: "2026-03-25", access: full, locator: "para 2" }
    - { ref: DATASNIPPER-ODP, title: "DataSnipper Success Stories - The ODP Corporation", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/the-odp-corporation", date: "2026", access: full, locator: "'Using DataSnipper as an Internal Audit Reviewer' (undated internal-audit story, controls and operational audits)" }
  last_reviewed: "2026-10-16"
  notes: >-
    Capped at B: the only named-organisation figure (NAO) is second-hand and the type of work is not stated. The
    ODP Corporation story concerns internal audit (SOX and operational audits) and is cited only for the reviewer
    workflow; it also says preparers expect testing times could be halved in some cases. An older Baker Tilly
    Germany story on the vendor site (40–50% time saved on repetitive tasks) is undated and is not relied on.

- id: assurance-substantive-testing-08
  title: Agentic sample testing that traces incoming client documents to selections (Sanville & Co on Fieldguide)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >-
    A small broker-dealer and fund auditor faced sample selections running into the hundreds of transactions, each
    traced and vouched by hand, with reviewers and the engagement quality reviewer absorbing the backlog
    (FIELDGUIDE-SANVILLE-2026).
  solution: >-
    Fieldguide's Field Auditor agents inside the testing sheets trace incoming client documents to the selections
    requested, which removed the time to validate and screen support for revenue and related-party testing. The
    firm rebuilt its audit programmes as firm-wide templates in the same project.
  outcomes:
    - lever: speed
      description: "Partner says sample selections of hundreds of transactions that took hours often took minutes"
      figure: "hours to minutes, 'in many cases'"
      measures: >-
        Partner's description of time to test sample selections of hundreds of transactions at Sanville & Co, before
        and after; no timings or sample counts given
      provenance: vendor-published
      source_ref: FIELDGUIDE-SANVILLE-2026
    - lever: quality
      description: "First PCAOB inspection conducted entirely on the platform ended with no comment forms"
      figure: "zero comment forms"
      measures: >-
        PCAOB comment forms on one broker-dealer engagement inspected, the firm's first fully clean broker-dealer
        inspection (one engagement; the platform and methodology were overhauled together)
      provenance: vendor-published
      source_ref: FIELDGUIDE-SANVILLE-2026
    - lever: growth
      description: "Blended realization on the firm's lowest-margin engagements rose"
      figure: "$150–$200 an hour to $250 or more (up to $300–$350 in some cases)"
      measures: "Blended realization per hour on the firm's lowest-priced, lowest-margin engagements, as reported by the firm via the vendor"
      provenance: vendor-published
      source_ref: FIELDGUIDE-SANVILLE-2026
  prerequisites:
    - Audit programmes built as templates on the platform, referencing PCAOB standards step by step (FIELDGUIDE-SANVILLE-2026).
    - A partner champion; the overhaul took under a year against an expected 18–24 months (FIELDGUIDE-SANVILLE-2026).
  risks_and_guardrails:
    - Fieldguide's product material says agents stop at major steps for review and give citations for each result (FIELDGUIDE-ORCH-2026; FIELDGUIDE-FIELDAGENTS-2025).
    - A single clean inspection on one engagement is not evidence of tool accuracy.
  human_checkpoints:
    - Reviewers apply judgment to exceptions; the firm updated a programme the morning after a PCAOB exam point and pushed it to every open engagement (FIELDGUIDE-SANVILLE-2026).
  role_evolution: >-
    The partner says first-year staff who previously had no chance at complex revenue testing now do it because
    reviewers have bandwidth to guide them (FIELDGUIDE-SANVILLE-2026).
  evidence_grade: A
  sources:
    - { ref: FIELDGUIDE-SANVILLE-2026, title: "How Sanville & Co passed a PCAOB inspection with zero comment forms in under a year with Fieldguide", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/case-studies/how-sanville-co-passed-a-pcaob-inspection-with-zero-comment-forms-in-under-a-year-with-fieldguide", date: "2026", access: full, locator: "Key Results; sections 'Building a Methodology' and 'A Clean Inspection'" }
    - { ref: FIELDGUIDE-FIELDAGENTS-2025, title: "Increase Capacity and Audit Quality with Field Agents for Financial Audit", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/blog/increase-capacity-and-audit-quality-with-field-agents-for-financial-audit", date: "2025-06-04", access: full, locator: "section 'Fully Automate Audit Testing'" }
    - { ref: FIELDGUIDE-ORCH-2026, title: "Introducing Field Orchestrator: The Intelligence Layer for Financial Audit", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/blog/field-orchestrator", date: "2026-06-08", access: full, locator: "section 'Human-in-the-loop by design'" }
  last_reviewed: "2026-10-16"
  notes: >-
    Case study page is undated; the year 2026 is inferred (it calls QC 1000 forthcoming and describes the 2025 Field
    Agents product). Firm size is about 20 people. Fieldguide also claims its Audit Testing Agent automates "up to
    70%" of testing (vendor claim, no sample; FIELDGUIDE-FIELDAGENTS-2025) and names Cherry Bekaert, LSL CPAs and
    Baker Tilly as customers (see use case 09 and section 4). No customer-level outcome other than Sanville's was found.

- id: assurance-substantive-testing-09
  title: Field Orchestrator coordinates testing agents to run a substantive test end to end (search for unrecorded liabilities)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    In most teams the auditor is both the orchestrator and the executor of substantive testing, driving each step
    by hand, which keeps the time between evidence collection and a finished workpaper long (FIELDGUIDE-ORCH-2026).
  solution: >-
    The auditor directs a conversational agent that plans the test, analyses the population, calculates the sample,
    prompts for evidence, then coordinates specialised testing agents that extract, link documents and evaluate.
    The first test it runs end to end is the search for unrecorded liabilities (completeness): post-cutoff payments
    traced to bank statements, vendor invoices and payment records, with exceptions flagged with context.
  outcomes:
    - lever: capacity
      description: "None published. The vendor says firms using it this year will enter 2027 with a materially different picture of capacity."
      figure: "none published"
      measures: "Not applicable; product announcement without customer data"
      provenance: vendor-published
      source_ref: FIELDGUIDE-ORCH-2026
  prerequisites:
    - A population file and engagement context loaded in the testing workspace (FIELDGUIDE-ORCH-2026).
    - Evidence collected and linked as the agent prompts (FIELDGUIDE-ORCH-2026).
  risks_and_guardrails:
    - The agent stops at each major step for human review by design (FIELDGUIDE-ORCH-2026).
    - FRC guidance notes that outputs on whole populations may be less conclusive for each item than traditional substantive work (FRC-GENAI-2026, p.19).
  human_checkpoints:
    - Auditor confirms the plan, reviews outputs after each phase, reviews exceptions and signs off the conclusion (FIELDGUIDE-ORCH-2026).
  role_evolution: >-
    Vendor describes senior staff moving from running the procedure to reviewing results, evaluating exceptions and
    advising on conclusions (FIELDGUIDE-ORCH-2026).
  evidence_grade: C
  sources:
    - { ref: FIELDGUIDE-ORCH-2026, title: "Introducing Field Orchestrator: The Intelligence Layer for Financial Audit", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/blog/field-orchestrator", date: "2026-06-08", access: full, locator: "sections 'What Field Orchestrator actually does' and 'The first test case'" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03", access: full, locator: "p.19 (methodology risk: whole-population outputs)" }
  last_reviewed: "2026-10-16"
  notes: >-
    Product post only; no named customer for Field Orchestrator was found. The same procedure (search for
    unrecorded liabilities) is also in KPMG's April 2025 agent list (use case 03) and DataSnipper describes
    prebuilt payables agents that check post-period payments for unrecorded liabilities (DATASNIPPER-PAYABLES-2026).

- id: assurance-substantive-testing-10
  title: Digital confirmation and evidence-request platforms for bank and third-party confirmations (Circit)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [transaction-processing, coordination-scheduling]
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Firms prepared and sent bank, lawyer, customer and supplier requests by hand, stored responses manually, and
    chased late replies. One firm's earlier circularisation platform allowed only two mailings per third party and
    was distrusted by recipients (CIRCIT-MOORE-2026, CIRCIT-CROWE-2026).
  solution: >-
    A platform creates, sends and tracks confirmation requests, with standard templates, reminders, roll-forward of
    prior-year requests without fresh client authority, a request status dashboard and an audit trail. Moore Polska
    uses it for confirmations, client document (PBC) requests and AR/AP confirmations; Crowe Spain uses it for the
    same three; Beever & Struthers (now Menzies) runs 80–90% of its confirmations through it; Kreston Iberaudit
    adopted it in January 2023.
  outcomes:
    - lever: capacity
      description: "A named audit department director reports hours saved per audit across all three modules"
      figure: "up to 20 hours per audit; document PDF preparation from about 3 minutes to 3 seconds"
      measures: >-
        Moore Polska's audit-team hours saved per audit across Circit's confirmation, PBC and AR/AP products, as
        stated by its Director of the Audit Department; the 98% is the vendor's calculation from 3 minutes to 3
        seconds; method not stated
      provenance: vendor-published
      source_ref: CIRCIT-MOORE-2026
    - lever: speed
      description: "Firm says the share of bank confirmations returned within three months of year-end rose against its internal benchmark"
      figure: "improved; no figure published"
      measures: "Beever & Struthers' internal benchmark: confirmation responses received within three months of year-end; the rate before and after is not stated"
      provenance: vendor-published
      source_ref: CIRCIT-BEEVER-2026
    - lever: capacity
      description: "Adoption of an automated confirmation solution across US firms in the benchmark survey"
      figure: "39% of firms"
      measures: "Share of the 54 firms with complete data in the 2025 CPA.com and AICPA benchmark that answered 'confirmations' to the question on which functions have an automated solution"
      provenance: independent
      source_ref: CPACOM-ATR-2025
  prerequisites:
    - Adoption work beyond licensing: training of key users, internal communications, consistent workflow (CIRCIT-BEEVER-2026).
    - Clients and banks willing to use the channel; Circit says its U.S. network gained direct bank connections (banner on CIRCIT-MOORE-2026; vendor claim).
  risks_and_guardrails:
    - Circit's own case studies are vendor-authored; no figure states how savings were measured.
    - The tool is workflow automation, not an AI model; AI and APIs are described as a next step by Beever & Struthers (CIRCIT-BEEVER-2026).
  human_checkpoints:
    - Auditor decides what to confirm and evaluates replies and exceptions; the platform tracks status and follow-up.
  role_evolution: >-
    Beever & Struthers staffed the work with a digital transformation lead on a university knowledge-transfer
    project (CIRCIT-BEEVER-2026). Kreston Iberaudit plans to extend use across its whole audit team
    (CIRCIT-KRESTON-2026).
  evidence_grade: A
  sources:
    - { ref: CIRCIT-MOORE-2026, title: "Moore Polska saves 20 hours per Audit with Circit's PBC and Confirmation requests", publisher: Circit, type: vendor, url: "https://circit.io/case-study/moore-polska-case-study", date: "2026-05-13", access: full, locator: "sections 'The solution with Circit' and 'Implementing Circit'" }
    - { ref: CIRCIT-BEEVER-2026, title: "Why Beever & Struthers (now Menzies) Made Circit Central to Audit Delivery", publisher: Circit, type: vendor, url: "https://circit.io/case-study/beever-struthers-case-study", date: "2026-06-26", access: full, locator: "sections 'Measurable ROI' and 'A critical platform for audit delivery'" }
    - { ref: CIRCIT-CROWE-2026, title: "How Crowe Spain boosted accuracy and improved response rates with Circit", publisher: Circit, type: vendor, url: "https://circit.io/case-study/crowe-case-study", date: "2026-05-19", access: full, locator: "sections 'Before Circit' and 'Implementing Circit'" }
    - { ref: CIRCIT-KRESTON-2026, title: "How Kreston Iberaudit improved efficiency and control with Circit", publisher: Circit, type: vendor, url: "https://circit.io/case-study/kreston-iberaudit", date: "2026-07-13", access: full, locator: "sections 'Before Circit' and 'Using Circit'" }
    - { ref: CPACOM-ATR-2025, title: "Audit Transformation Report: 2025 CPA.com and AICPA Audit Benchmark Survey", publisher: CPA.com and AICPA, type: professional-body, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: "2025-12", access: full, locator: "Theme 1, chart 'For which of the following does the firm have an automated solution?'; Appendix I (54 of 74 firms)" }
  last_reviewed: "2026-10-16"
  notes: >-
    Case-study dates are the vendor pages' own datePublished values and probably reflect site republication: the
    text refers to 2023–2025 events. Graded A on Moore Polska's figure. This is workflow automation, not AI; it is
    kept because the module brief lists confirmation platforms. Circit claims 400+ audit firms and trust in over
    150,000 audits (vendor claims; the landscape records the 10 Feb 2026 funding).

- id: assurance-substantive-testing-11
  title: Direct, consent-based bank data connection for auditors, as a base for cash testing and 100% testing (Rabobank, BDO NL and Circit)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Bank transaction data reached the auditor as files that customers downloaded and emailed or uploaded, and BDO
    NL says there were sometimes more than 156 files per engagement across several accounts, with risk of omission
    or manipulation (CIRCIT-RABOBANK-BDONL-2026).
  solution: >-
    Rabobank customers consent, through Circit, to share transaction data directly with their auditor. BDO NL
    was one of the first Dutch firms to define requirements and test it in practice. BDO NL says it could then
    track payments to the correct supplier and bank account and aims to reduce reliance on sampling in favour of
    100% testing and, later, continuous auditing.
  outcomes:
    - lever: risk
      description: "Auditor receives data straight from the bank, so it cannot be altered by the client; replaces manual downloads"
      figure: "previous process: sometimes more than 156 files per engagement"
      measures: >-
        Number of separate batch-detail files a Rabobank customer might have to download per engagement when it had
        several accounts, as described by BDO NL's audit innovation manager for the earlier process; not a measured
        result of the new process
      provenance: vendor-published
      source_ref: CIRCIT-RABOBANK-BDONL-2026
  prerequisites:
    - A bank that offers the consent-based feed (Rabobank here) and customers who grant consent.
    - Existing automated tests for debtors, creditors and purchase invoices at BDO NL (CIRCIT-RABOBANK-BDONL-2026).
  risks_and_guardrails:
    - Customers can grant and revoke consent at any time (CIRCIT-RABOBANK-BDONL-2026).
    - Inference, not stated in the source: where a US audit relies on company-provided external information, PCAOB paragraph .10A asks the auditor to understand the source and the handling of the information; a direct-from-bank feed changes that analysis (PCAOB-PS2025-004).
  human_checkpoints:
    - Auditor investigates the outliers, anomalies and risks that analytics flag (CIRCIT-RABOBANK-BDONL-2026).
  role_evolution: >-
    BDO NL describes a shift from visiting the client twice a year to more continuous work with earlier alerts to
    clients (CIRCIT-RABOBANK-BDONL-2026). This is a stated ambition, not an observed change.
  evidence_grade: B
  sources:
    - { ref: CIRCIT-RABOBANK-BDONL-2026, title: "Rabobank & BDO NL: Building the Foundation for Continuous, Trusted Audit Data", publisher: Circit, type: vendor, url: "https://circit.io/case-study/rabobank-bdo-nl", date: "2026-05-21", access: full, locator: "sections 'Direct-from-Bank Reliability', 'Automation and Audit Quality at Scale' and 'A Foundation for Continuous Audit'" }
    - { ref: PCAOB-PS2025-004, title: "Policy Statement Regarding Implementation of Paragraph .10A of AS 1105, Audit Evidence (Release 2025-004)", publisher: PCAOB, type: regulator, url: "https://assets.pcaobus.org/pcaob-dev/docs/default-source/rulemaking/docket-052/pcaob-release-no-2025-004.pdf", date: "2025-09-18", access: full, locator: "p.1 and footnote 2" }
  last_reviewed: "2026-10-16"
  notes: >-
    The piece says BDO NL tested the connection; it does not report a go-live or use on an issued audit, so
    piloting. Rabobank's product is described as arriving ahead of upcoming regulation (vendor and bank quote).

- id: assurance-substantive-testing-12
  title: AI document analysis grid for client contracts and supporting documents (CoCounsel Document Analysis)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: >-
    Reviewing client documents, such as contracts and leases, for audit evidence is slow, and a tool that only
    screens for a term can be mistaken for a complete read (FRC-GENAI-2026, p.18).
  solution: >-
    A spreadsheet-style AI grid, integrated with the vendor's audit product, applies agentic AI to extract and
    review client documents at scale. Auditors can delegate client-document review to it and iterate and
    collaborate in the grid. RSM Australia notes that extraction of key terms from leases and contracts has become
    available to mid-tier firms through vendors rather than proprietary platforms.
  outcomes:
    - lever: speed
      description: "Early adopters saw faster preparation and workpaper review; customers are not named"
      figure: "up to 70% faster"
      measures: >-
        Vendor's description of preparation and workpaper review time for unnamed early-adopter customers; the
        baseline, sample and what 'up to' covers are not stated
      provenance: vendor-published
      source_ref: TR-AGENTIC-2025
  prerequisites:
    - Client documents in a form the tool can read, in a platform already used for the audit (TR-AGENTIC-2025).
  risks_and_guardrails:
    - An AI tool that checks whether contracts contain leases and summarises those sections can be misread as a complete summary, so no other procedures are performed (FRC-GENAI-2026, p.18).
    - RSM Australia advises being wary of tools marketed as auditing a balance or concluding (RSM-AUS-2026).
  human_checkpoints:
    - Auditor reviews the extraction in the grid and decides what it supports (TR-AGENTIC-2025).
  role_evolution: >-
    A named senior audit manager at Sensiba says the tool helps teams shift mindset to adopting AI responsibly
    (TR-AGENTIC-2025); no change in tasks is described.
  evidence_grade: C
  sources:
    - { ref: TR-AGENTIC-2025, title: "Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html", date: "2025-11-05", access: full, locator: "section 'Introducing New AI-powered Audit Solutions'; Notes to Editors" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03", access: full, locator: "p.18 (misinterpretation of output risk)" }
    - { ref: RSM-AUS-2026, title: "AI in Audit and Accounting Firms: Use Cases and Risks", publisher: RSM Australia, type: firm, url: "https://www.rsm.global/australia/insights/what-role-ai-audit-and-accounting-firms", date: "2026-08", access: full, locator: "section 'Fieldwork', paras 2–3" }
  last_reviewed: "2026-10-16"
  notes: >-
    The release says the tool was in an early adopter programme in the US, with general availability planned for
    January 2026. No named customer with a measured result was found.

- id: assurance-substantive-testing-13
  title: "Idea: risk-scored contract selection for revenue testing (FRC illustrative example)"
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Auditors testing revenue often sample contracts on a risk basis, and a firm may use AI to target the sample on
    higher-risk contracts (FRC-GENAI-2026, p.49).
  solution: >-
    In the FRC's illustration, uploaded contracts are chunked and indexed with stable identifiers. A model extracts
    risk indicators under prewritten prompts: unambiguous ones (bonus, contingent payment, refund, long term) and
    ones needing evaluation (distinct performance obligations, control transferring over time, constrained variable
    consideration), each evaluated by its own prompt. A computation step scores each contract, and those above a
    threshold form the sample the auditor tests.
  outcomes:
    - lever: quality
      description: none published
      figure: "none published"
      measures: "Not applicable; the FRC describes a hypothetical firm's tool design, not a deployment"
      provenance: independent
      source_ref: FRC-GENAI-2026
  prerequisites:
    - Contracts digitised and indexed with stable identifiers so output can cite its source (FRC-GENAI-2026, p.51).
    - Prompt design with specialist technical audit and accounting teams (FRC-GENAI-2026, p.52).
    - Retrieval of curated firm technical resources for the evaluation step (FRC-GENAI-2026, p.52).
  risks_and_guardrails:
    - FRC lists four deficiency risks: extraction prompt not fit for purpose, LLM misses or adds content, LLM misevaluates, and weighting or threshold inappropriate (FRC-GENAI-2026, p.51).
    - The auditor documents use of the tool, why its use was appropriate, the contracts selected, the risk indicators they showed and the substantive testing done (FRC-GENAI-2026, p.50).
  human_checkpoints:
    - The tool can escalate to human review at the extraction and evaluation steps; auditor sees which indicators were present for each contract (FRC-GENAI-2026, pp.49–51).
  role_evolution: >-
    Not stated; the example concerns targeting of the sample, with the auditor still performing the substantive
    testing (FRC-GENAI-2026, p.50).
  evidence_grade: D
  sources:
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03", access: full, locator: "Illustrative example 2, Contract review, pp.49–53" }
  last_reviewed: "2026-10-16"
  notes: >-
    Idea: a regulator's illustrative design; the FRC states the examples are one way tools may be designed and do
    not describe approved practice. No firm has announced this specific use. Related practice: RSM Australia says
    contract-term extraction is within reach of mid-tier firms (RSM-AUS-2026).

- id: assurance-substantive-testing-14
  title: AI risk scoring to cut substantive sample sizes under a firm-approved methodology (Cherry Bekaert on MindBridge)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Firms that rely only on a third-party audit methodology may have to obtain a large share of assurance from
    sampling, which in busy season means a senior spending hours on journal-entry selection or testing 200 revenue
    items (MINDBRIDGE-CHERRY-2022).
  solution: >-
    Cherry Bekaert adopted MindBridge in 2020 and built the deployment deliberately: research, standards mapping,
    methodology and sampling-form development, QC validation and policy drafting, with a firm-wide policy for each
    use. The aim is to obtain more assurance from risk scoring of full populations and therefore need smaller
    samples.
  outcomes:
    - lever: cost
      description: "Firm demonstrated a sample size reduction on an illustrative client at moderate risk of material misstatement"
      figure: "66% reduction in sample size"
      measures: >-
        Reduction in sample size demonstrated by Cherry Bekaert for a moderate risk of material misstatement in an
        illustrative client (a worked demonstration, not measured across live engagements), per the vendor's case study
      provenance: vendor-published
      source_ref: MINDBRIDGE-CHERRY-2022
  prerequisites:
    - Standards mapping, sampling-form development and QC validation before roll-out (MINDBRIDGE-CHERRY-2022).
    - Firm-wide policy covering each use of the tool (MINDBRIDGE-CHERRY-2022).
  risks_and_guardrails:
    - The vendor says an independent algorithm audit by University College London Consulting found MindBridge's algorithms operate as expected (MINDBRIDGE-CHERRY-2022; vendor-described, report not opened).
    - IFIAR reports findings on thin testing of outliers and misreading of tool results (IFIAR-TTF-2025, p.5).
  human_checkpoints:
    - Associates keep autonomy to make decisions and exercise professional judgment (MINDBRIDGE-CHERRY-2022).
  role_evolution: >-
    Cherry Bekaert partners describe differentiating value for clients and freeing senior time in busy season
    (MINDBRIDGE-CHERRY-2022). In June 2026 Cherry Bekaert chose Fieldguide as its strategic AI partner for
    financial audit, internal audit and SOC on one platform (FIELDGUIDE-CHERRY-2026).
  evidence_grade: B
  sources:
    - { ref: MINDBRIDGE-CHERRY-2022, title: "How Cherry Bekaert drove ROI for their audit engagements", publisher: MindBridge, type: vendor, url: "https://www.mindbridge.ai/resources/case-studies/cherry-bekaert-llp-case-study", date: "2022", access: full, locator: "sections 'Redefining risk to save time' and 'The value of implementing a vision' (year inferred from image upload paths; page header shows a crawl date)" }
    - { ref: FIELDGUIDE-CHERRY-2026, title: "Cherry Bekaert Selects Fieldguide as Strategic AI Partner to Modernize Audit and Advisory Delivery", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/blog/cherry-bekaert-fieldguide-financial-audit", date: "2026-06-03", access: full, locator: "paras 1–3" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: "2025-03-27", access: full, locator: "p.5-6 (inspection findings)" }
  last_reviewed: "2026-10-16"
  notes: >-
    The 66% is an illustration, so this stays at B even though a figure is named. The year of the case study is
    uncertain (see locator). The statement that a firm needs 60% of its assurance from sampling under a third-party
    methodology is a quotation of a Cherry Bekaert director in the vendor's page and is not independently checked.

- id: assurance-substantive-testing-15
  title: AI-native specialist firm testing every transaction in employee-benefit-plan audits (Ledgerline)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: full-population-testing
  ladder: automate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >-
    The annual 401(k) audit is described as a four-month chore of requests, reviews and follow-ups, and testing is
    a sample of contributions extrapolated to the plan (LEDGERLINE-CPAPA-2026; firm website).
  solution: >-
    The firm pulls payroll and recordkeeper data directly from systems instead of requesting it, reconciles
    contributions across payroll, trust and recordkeeper, and uses AI agents with deterministic code to check every
    deposit against payroll, every match against the plan formula and every distribution against its record. Agents
    read plan documents and cite the page and section for each provision tested.
  outcomes:
    - lever: speed
      description: >-
        None published for the firm's engagements. The CEO's article asserts, in general terms, that work taking a
        junior associate 20 hours can run in minutes.
      figure: "none published"
      measures: "Not applicable; the 20-hours statement is generic and no study or engagement data is given"
      provenance: self-reported
      source_ref: LEDGERLINE-CPAPA-2026
  prerequisites:
    - Connections to payroll providers (the site names Rippling, Gusto, ADP and Paychex) and recordkeepers (Fidelity, Empower, Vanguard).
    - Shadow mode on completed engagements, then gradual cutover, per the CEO's advice (LEDGERLINE-CPAPA-2026).
  risks_and_guardrails:
    - Testing 100% surfaces more exceptions, so more follow-up and judgment about materiality (LEDGERLINE-CPAPA-2026).
    - Reasonable assurance is not absolute; some risks sit outside the transaction data, such as an incomplete population, so "we test everything" can widen the expectation gap (LEDGERLINE-CPAPA-2026).
  human_checkpoints:
    - A person stays accountable for every conclusion; agents produce work a reviewer can check with sources cited (LEDGERLINE-CPAPA-2026).
  role_evolution: >-
    The article says the hours saved move to investigating exceptions, assessing controls and deciding what a
    finding means (LEDGERLINE-CPAPA-2026). The firm's site says it was built by operators with experience at named companies.
  evidence_grade: B
  sources:
    - { ref: LEDGERLINE-CPAPA-2026, title: "Testing Every Transaction Changes the Audit - Here's What Firms Should Know Before They Sell It", publisher: CPA Practice Advisor (contributed by Ledgerline's CEO), type: press, url: "https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/", date: "2026-10-15", access: full, locator: "sections 'What full-population testing changes', 'The trap', 'How to roll it out safely'" }
    - { ref: LEDGERLINE-SITE-2026, title: "Ledgerline: Specialist 401(k) and 403(b) plan audits", publisher: Ledgerline, type: firm, url: "https://ledgerlineaudit.com", date: "2026-10", access: full, locator: "'Our approach' section (undated site, read 2026-10-16)" }
  last_reviewed: "2026-10-16"
  notes: >-
    Graded B on the firm's description of its operating model; there is no independent evidence of its audit
    quality, client count or inspection history. It is included because it is a live example of a different service
    model (an audit firm built on data pulls and agents), not because outcomes are shown.

- id: assurance-substantive-testing-16
  title: PwC Australia AI-native audit platform pilot with full-population analysis
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: >-
    Auditors spend time on data gathering and documentation rather than analysis, and sampling limits the
    scrutiny applied to balances (PWCAU-AT-2025).
  solution: >-
    PwC Australia is rolling out an AI-native platform, as part of a global pilot, in which AI agents assess risk,
    design audit plans and workflows and test balances and controls, with auditors in the loop. PwC says analysis
    would run in real time on full population sets and against trusted third-party data. The programme starts with
    five audit clients, with a plan to reach all audit clients by 2028, for 1,600 auditors.
  outcomes:
    - lever: quality
      description: "None published. PwC says full-population analysis gives unprecedented scrutiny of judgments; no result is given."
      figure: "none published"
      measures: "Not applicable; announcement of a pilot of five audit clients"
      provenance: self-reported
      source_ref: PWCAU-AT-2025
  prerequisites:
    - Real-time access to client data and to third-party data (PWCAU-AT-2025).
  risks_and_guardrails:
    - An RSM Australia partner, quoted in the same article, cautions that over-reliance on AI over professional judgment could introduce errors and poorer audit quality (PWCAU-AT-2025).
    - IFIAR members report minimal GenAI in most inspected public-company audits to date (IFIAR-TTF-2025, section 3).
  human_checkpoints:
    - Auditors provide context, analysis and decisions; PwC says humans keep final judgments (PWCAU-AT-2025).
  role_evolution: >-
    PwC says auditors spend less time on routine tasks and workflow management and more on analysis and
    judgment (PWCAU-AT-2025).
  evidence_grade: B
  sources:
    - { ref: PWCAU-AT-2025, title: "PwC Australia rolls out pilot program for AI-assisted full audits", publisher: Accounting Times, type: press, url: "https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits", date: "2025-10-28", access: full, locator: "paras 1–6 and the RSM partner's comments" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: "2025-03-27", access: full, locator: "section 3 (governance considerations, GenAI)" }
  last_reviewed: "2026-10-16"
  notes: >-
    A named pilot with a client count but no published measure. No follow-up reporting on the pilot was found.
    The landscape's PwC "global agentic platform about 18 months after 2026" is in PWC-AT-2025.

- id: assurance-substantive-testing-17
  title: Network-scale multi-agent platforms that run preliminary procedures for review (EY Canvas, Deloitte Omnia, Grant Thornton Gtap)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    Global firms need consistent execution of methodology across thousands of engagements and limited senior staff
    time for judgment-heavy work (DELOITTE-OMNIA-2026, EY-CANVAS-2026).
  solution: >-
    Firms put agent networks inside their audit platforms. Deloitte says its agents execute preliminary procedures,
    including data extraction, evidence analysis, drafting documentation and preliminary conclusions for
    professionals to review. EY says its multi-agent framework is embedded in all phases across 130,000 assurance
    professionals and 160,000 engagements. Grant Thornton US says its platform has AI-driven workflows and agents
    that identify risks and anomalies, with private-company audits first and public companies the following year.
  outcomes:
    - lever: speed
      description: >-
        PwC's US assurance transformation leader says time savings a year in are not dramatic yet and that
        busy-season time shifted only modestly. (PwC is a related firm programme, not one of the three platforms above.)
      figure: "none published"
      measures: "Not applicable; qualitative statement by PwC US's assurance transformation leader, answering whether three months of work became one"
      provenance: self-reported
      source_ref: CFODIVE-PWC-2026
  prerequisites:
    - A single global platform and methodology so agents apply consistently (DELOITTE-OMNIA-2026).
    - Training: EY has a global programme for all audit and technology-risk professionals; Deloitte has a "tutor mode" in Omnia (EY-CANVAS-2026, DELOITTE-OMNIA-2026).
  risks_and_guardrails:
    - Deloitte says capabilities are developed under its Trustworthy AI framework (DELOITTE-OMNIA-2026).
    - Grant Thornton US attest services sit in a separate licensed firm under an alternative practice structure, which raises independence questions treated in the acceptance-independence module (GT-GTAP-2026).
  human_checkpoints:
    - Professionals review preliminary conclusions; Grant Thornton says professionals supervise every step (DELOITTE-OMNIA-2026, GT-GTAP-2026).
  role_evolution: >-
    Deloitte says professionals will "supervise, validate, and work alongside AI" (DELOITTE-OMNIA-2026). EY
    expects the platform to support all end-to-end audit activities by 2028 (EY-CANVAS-2026).
  evidence_grade: C
  sources:
    - { ref: DELOITTE-OMNIA-2026, title: "Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia to Advance Audit & Assurance", publisher: Deloitte, type: firm, url: "https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html", date: "2026-06-24", access: full, locator: "paras 1–4; 'Investing in upskilling' section" }
    - { ref: EY-CANVAS-2026, title: "EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/", date: "2026-04-07", access: full, locator: "paras 2–3, 7" }
    - { ref: GT-GTAP-2026, title: "Grant Thornton launches AI platform for audit business", publisher: Consultancy.org (Consulting.us), type: press, url: "https://www.consulting.us/news/13378/grant-thornton-launches-ai-platform-for-audit-business", date: "2026-05-11", access: full, locator: "paras 1–3, 7–8" }
    - { ref: CFODIVE-PWC-2026, title: "PwC exec ushers in AI-assisted audits, awaits bigger time savings", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/", date: "2026-10-07", access: full, locator: "paras 8–9" }
    - { ref: BLOOMBERGTAX-RSM-2025, title: "Auditor RSM Commits $1 Billion to AI Growth Across US Firm", publisher: Bloomberg Tax, type: press, url: "https://news.bloombergtax.com/financial-accounting/auditor-rsm-commits-1-billion-to-deploy-ai-tools-across-us-firm", date: "2025-06-09", access: search-only, locator: "paywalled teaser, first three paragraphs only" }
  last_reviewed: "2026-10-16"
  notes: >-
    These are cross-module announcements; only the substantive-relevant parts are used here. Deloitte's release
    says "launch" and "capabilities expected to build on this foundation", with no usage figure. The Bloomberg Tax
    teaser says RSM US plans to invest $1 billion over three years to weave agents into assurance, tax and
    consulting; it is search-only and supports nothing above. Grant Thornton's launch date in the landscape is 7 May;
    the opened article is dated 11 May 2026.

- id: assurance-substantive-testing-18
  title: PwC Audit Innovation Hub for financial-statement tie-out and testing in fund audits
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: document-to-decision
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Fund audits require financial-statement tie-outs and testing of extracted data and documents, a large volume of
    repeat work per engagement (PWC-AT-2025).
  solution: >-
    The tool extracts, organises and tests financial data and documents for non-registered fund-to-fund audits
    under AICPA standards, automating parts of tie-out and testing. It was being tested with certain asset and
    wealth management engagement teams, with a plan to expand the pilot.
  outcomes:
    - lever: capacity
      description: none published
      figure: "none published"
      measures: "Not applicable; PwC describes a pilot with no figures"
      provenance: self-reported
      source_ref: PWC-AT-2025
  prerequisites:
    - Engagement teams in the fund sector willing to pilot (PWC-AT-2025).
  risks_and_guardrails:
    - PwC says it measures usefulness and performance per tool and will retire tools that stop adding value (CFOBREW-PWC-2025).
  human_checkpoints:
    - Not described in the source.
  role_evolution: >-
    None described for this tool; PwC's broader comments on hiring engineers and dual-track recruits are in
    PWC-AT-2025.
  evidence_grade: B
  sources:
    - { ref: PWC-AT-2025, title: "PwC expects end-to-end AI audit automation within 2026", publisher: Accounting Today, type: press, url: "https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026", date: "2025-10-28", access: full, locator: "paragraph on Audit Innovation Hub" }
    - { ref: CFOBREW-PWC-2025, title: "A look at PwC's 'next generation' audit", publisher: CFO Brew, type: press, url: "https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit", date: "2025-11-05", access: full, locator: "'ROI' paragraphs (Kosar)" }
  last_reviewed: "2026-10-16"
  notes: >-
    Pilot status per Oct 2025; no later report was found. Graded B only because PwC names the engagement area
    in which it is being tested.

- id: assurance-substantive-testing-19
  title: Technology-assisted substantive analytical procedures with sharper expectations
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Year-over-year comparisons dominate substantive analytics in many firms. Only 11% of 54 US firms have an
    automated solution for substantive analytics and 89% say they are not using technology to enable it
    (CPACOM-ATR-2025).
  solution: >-
    Technology builds a more precise expectation (for example, modelling cost of sales on revenue with seasonal
    and pricing variables, or structuring unstructured industry data) and compares it with recorded amounts. Firms
    that report using it mention visualisations, full-population testing, AI anomaly detection, continuous testing,
    and expense and revenue testing. The IAASB proposes application material that gives these as examples.
  outcomes:
    - lever: capacity
      description: "Adoption of automated solutions for substantive analytics among surveyed US firms"
      figure: "11% of firms (89% do not use technology to enable substantive analytics)"
      measures: >-
        Share of the 54 firms with complete data in the 2025 CPA.com and AICPA benchmark that have an automated
        solution for substantive analytics; the 89% is the report's statement of firms not currently leveraging
        technology to enable substantive analytics
      provenance: independent
      source_ref: CPACOM-ATR-2025
  prerequisites:
    - Access to client data, which even the firms using analytics cite as a difficulty (CPACOM-ATR-2025, 'Risk-driven approach and technology').
  risks_and_guardrails:
    - FRC notes outputs on whole populations may be less conclusive for each item, and professional judgment decides what conclusions follow (FRC-GENAI-2026, p.19).
    - IAASB's draft ISA 520 says technology-enabled analysis may leave the residual risk of material misstatement in the rest of the population acceptably low (IAASB-ED520-2026, EM para 23).
  human_checkpoints:
    - Auditor investigates fluctuations, unusual items and outliers, including by inquiry of management (IAASB-ED520-2026, EM para 23).
  role_evolution: >-
    About a third of surveyed firms said they need at least one non-traditional skill and about 20% had hired staff
    with non-traditional backgrounds, such as data analysts and IT specialists (CPACOM-ATR-2025, Theme 3).
  evidence_grade: C
  sources:
    - { ref: CPACOM-ATR-2025, title: "Audit Transformation Report: 2025 CPA.com and AICPA Audit Benchmark Survey", publisher: CPA.com and AICPA, type: professional-body, url: "https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf", date: "2025-12", access: full, locator: "Theme 1 chart; 'Risk-driven approach and technology'; Theme 3 'New approaches require new skills'" }
    - { ref: IAASB-ED520-2026, title: "Explanatory Memorandum to the ED for Proposed ISA 520 (Revised), Analytical Procedures", publisher: IAASB, type: standard-setter, url: "https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-520-Exposure-Draft.pdf", date: "2026-08-05", access: full, locator: "EM para 5 (p.6), para 23 (pp.10–11); proposed standard application material A20" }
    - { ref: IFIAR-TTF-2025, title: "Use of technology in audits: observations, risks and further evolution", publisher: IFIAR, type: regulator, url: "https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf", date: "2025-03-27", access: full, locator: "p.5 (substantive audit procedures 55% in 2024, 51% in 2023)" }
    - { ref: FRC-GENAI-2026, title: "Generative and Agentic AI Guidance", publisher: Financial Reporting Council, type: regulator, url: "https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf", date: "2026-03", access: full, locator: "p.19" }
  last_reviewed: "2026-10-16"
  notes: >-
    No named firm deployment of AI-built expectations was found. The IFIAR "substantive audit procedures" row (55%
    frequently observed in 2024) covers tool use across revenues and inventory testing, not analytics alone. The CPA.com
    report's text says "about one in four" and "about one-third" use no AI in different places (landscape data conflict).

- id: assurance-substantive-testing-20
  title: Drone and computer-vision inventory counts with reconciliation to perpetual records
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [physical-field, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: >-
    Inventory observation needs auditors present at counts of large warehouses and outdoor stock, which is slow
    and disruptive to clients (EY-DRONE-JOFA-2018).
  solution: >-
    EY ran a proof of concept in which drones fly mapped routes autonomously, scan barcodes, QR codes, RFID and
    labels, and send the data to the audit platform to reconcile to the client's perpetual records. An academic
    design-science study tested drones with automated counting software on cattle and sheep.
  outcomes:
    - lever: speed
      description: "Study found drone counts were much faster than manual counts"
      figure: "681 hours down to 19 hours"
      measures: "Count time in a design-science study of drones with automated counting software on cattle and sheep (homogeneous items), manual versus drone"
      provenance: independent
      source_ref: CHRIST-DRONE-2021
    - lever: quality
      description: "Study found error rates fell while documentation quality rose"
      figure: "0.15% down to 0.03%"
      measures: "Error rates in the same cattle-and-sheep study, manual versus drone count"
      provenance: independent
      source_ref: CHRIST-DRONE-2021
  prerequisites:
    - Per-client set-up that teaches the drone what to scan; EY said this limits use to large clients (EY-DRONE-JOFA-2018).
    - Perpetual inventory records to reconcile to (EY-DRONE-JOFA-2018).
  risks_and_guardrails:
    - A missed label shows as a difference to the perpetual records; blocked RFID reads are a practical limit (EY-DRONE-JOFA-2018).
    - Interviews in the study found firms reluctant to be first movers and standard setters slow to give guidance (CHRIST-DRONE-2021, abstract).
  human_checkpoints:
    - Auditor sets scan parameters and sampling technique (100% scan or every fifth box) and reconciles results (EY-DRONE-JOFA-2018).
  role_evolution: >-
    EY described a drone flying autonomously so that no auditor has to fly it inside a client's warehouse, with
    less disruption to the client (EY-DRONE-JOFA-2018). No staffing change is reported.
  evidence_grade: B
  sources:
    - { ref: CHRIST-DRONE-2021, title: "Prepare for takeoff: improving asset measurement and audit quality with drone-enabled inventory audit procedures", publisher: Review of Accounting Studies (Christ, Emett, Summers and Wood), type: academic, url: "https://link.springer.com/article/10.1007/s11142-020-09574-5", date: "2021", access: full, locator: "abstract and note 1 (full text paywalled; abstract read via text mirror)" }
    - { ref: EY-DRONE-JOFA-2018, title: "Using drones to enhance audits", publisher: Journal of Accountancy podcast (EY global assurance digital leader), type: podcast, url: "https://www.journalofaccountancy.com/podcast/using-drones-to-enhance-audits/", date: "2018-07-30", access: full, locator: "transcript, answers on the proof of concept and on mistakes" }
  last_reviewed: "2026-10-16"
  notes: >-
    Grade capped at B: the independent measure is for livestock, which the study chose because current technology
    suits homogeneous items, not warehouse stock, and EY's work was a 2018 proof of concept. Evidence is older than
    the 12–18 month window and no 2025–26 firm deployment of AI-based counting was found; an unopened July 2026
    preprint on drone imagery and inventory verification (search snippet only) is not used.

- id: assurance-substantive-testing-21
  title: GenAI assistant that helps teams design substantive procedures from engagement documentation (KPMG Clara)
  archetype: assurance
  module: substantive-testing
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Designing substantive procedures requires reading engagement documents and methodology; in PCAOB's 2024
    outreach, firms listed scoping, risk assessment and disclosure completeness as potential GenAI areas, while
    current use was mainly administrative and research (PCAOB-GENAI-2024).
  solution: >-
    KPMG said in July 2024 it integrated GenAI directly into Clara for 90,000 auditors, interacting with
    engagement documentation and methodology to help teams refine risk assessments, develop substantive testing
    procedures and enhance documentation.
  outcomes:
    - lever: speed
      description: none published
      figure: "none published"
      measures: "Not applicable; announcement; the 90,000 is the number of auditors the integration was announced for"
      provenance: self-reported
      source_ref: KPMG-CLARA-2025
  prerequisites:
    - Engagement documentation and methodology held in the platform (KPMG-CLARA-2025).
  risks_and_guardrails:
    - PCAOB staff recorded that some firms barred GenAI for audit procedures over privacy and reliability concerns (PCAOB-GENAI-2024; staff view, not Board policy).
  human_checkpoints:
    - Auditors remain in control of decision-making (KPMG-CLARA-2025).
  role_evolution: >-
    PCAOB staff recorded that firms investing in GenAI expected it to augment, not replace, auditors, and that
    some firms said their supervision and review policies had not changed (PCAOB-GENAI-2024).
  evidence_grade: C
  sources:
    - { ref: KPMG-CLARA-2025, title: "KPMG advances AI integration in KPMG Clara smart audit platform", publisher: KPMG International, type: firm, url: "https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html", date: "2025-04-22", access: full, locator: "'Today's announcement builds on' (July 2024 bullet)" }
    - { ref: PCAOB-GENAI-2024, title: "Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting", publisher: PCAOB staff, type: regulator, url: "https://pcaobus.org/documents/generative-ai-spotlight.pdf", date: "2024-07", access: full, locator: "key observations: current use, investment, limitations, supervision" }
  last_reviewed: "2026-10-16"
  notes: >-
    The July 2024 integration is reported in KPMG's April 2025 release; the original July 2024 release was not opened.
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Define and validate the population** (`data-reporting`): extract the ledger or sub-ledger, reconcile it to the trial balance, confirm completeness. Firms cite poor client data (60%) and lack of system access (53%) as top blockers (CPACOM-ATR-2025, Theme 1).
- **Journal-entry and fraud testing** (`review-assurance`, `data-reporting`): score entries, select, test, investigate. The most tool-supported step (IFIAR-TTF-2025).
- **Sample selection and sizing** (`review-assurance`): risk-based selection, sample-size determination, and (where methodology allows) reduced samples after analytics (use case 14).
- **Evidence request and collection (PBC)** (`coordination-scheduling`): request lists, client uploads, status tracking. Platforms are used for this and for confirmations (use case 10).
- **Confirmations** (`transaction-processing`): bank, AR/AP, legal and other third-party requests.
- **Vouching, tracing and matching** (`review-assurance`, `transaction-processing`): trace each sample to documents and bank activity, recompute, foot, tie out. This is where agents are most active (use cases 03, 04, 05, 06, 08, 09).
- **Contract and lease review** (`research-synthesis`, `review-assurance`): extract terms, identify risk indicators (use cases 12, 13).
- **Substantive analytics** (`data-reporting`): build expectations, compare, investigate fluctuations (use case 19).
- **Inventory observation** (`physical-field`): attend counts, test counts, reconcile to perpetual records (use case 20).
- **Exception investigation and conclusion** (`expert-judgment`): decide whether a difference is a misstatement, extend testing, conclude.
- **Workpaper documentation and review** (`document-production`): agents increasingly produce source-linked documentation for review (use cases 06, 08).

### Common pain points

- Manual tick-and-tie matching of samples to documents, with fatigue on large selections (TR-AGENTIC-2025, FIELDGUIDE-SANVILLE-2026, DATASNIPPER-PAYABLES-2026).
- Chasing clients and third parties for documents and confirmations (CIRCIT-MOORE-2026, CIRCIT-CROWE-2026).
- Receiving bank and ledger data as many manually downloaded files (CIRCIT-RABOBANK-BDONL-2026).
- Reviewer and engagement-quality-review bottlenecks in busy season (FIELDGUIDE-SANVILLE-2026).
- Staff not trained in new approaches (66% of firms) and no documented transformation plan (75%) (CPACOM-ATR-2025).
- Tool and methodology fit: many firms rely on a third-party methodology that limits what the tool can change (CPACOM-ATR-2025; MINDBRIDGE-CHERRY-2022).

### Metrics and benchmarks (with sources and provenance)

| Metric | Value | What it measures | Provenance | Source |
|---|---|---|---|---|
| Tool use in journal-entry testing | 88% (2024), 86% (2023) | Share of responding IFIAR members that "frequently observed" automated tools in journal-entry testing | independent | IFIAR-TTF-2025, p.5 |
| Tool use in substantive procedures | 55% (2024), 51% (2023) | Same measure, substantive procedures on accounts such as revenue and inventory | independent | IFIAR-TTF-2025, p.5 |
| Findings that tools were not used as intended | 31% (2024), 29% (2023) | Share of IFIAR members reporting such findings | independent | IFIAR-TTF-2025, p.5 |
| Firms with automated confirmations | 39% | Of 54 US firms with complete data | independent | CPACOM-ATR-2025 |
| Firms with automated substantive analytics | 11% | Of 54 US firms with complete data | independent | CPACOM-ATR-2025 |
| Firms with no automated solution of any kind in the list | 22% | Of 54 US firms | independent | CPACOM-ATR-2025 |
| Testing time per selection, FGMK | 30–45 min to about 5 min | FGMK's reported before and after, method not stated | vendor-published | DATASNIPPER-CONNECT-2026 |
| Engagement time, Oberlander | about 16 h to 5–6 h | One sole practitioner's estimate | vendor-published | TR-AGENTIC-2025 |
| Hours saved per audit, Moore Polska | up to 20 h | Across confirmations, PBC and AR/AP | vendor-published | CIRCIT-MOORE-2026 |
| Sample size reduction, Cherry Bekaert | 66% | Illustrative client at moderate RMM | vendor-published | MINDBRIDGE-CHERRY-2022 |
| Drone count time and error | 681 h to 19 h; 0.15% to 0.03% | Cattle and sheep, design-science study | independent | CHRIST-DRONE-2021 |
| AI investment and audit outcomes | one-standard-deviation change in AI investment: 5.0% lower restatement likelihood, 0.9% lower audit fees, accounting employees down 3.6% after 3 years and 7.1% after 4 | Resume-based AI-hiring measure for the 36 largest audit firms; pre-GenAI; adjacent (firm-level, not this module) | independent | FEDYK-2022 |

### Guardrails and regulatory points

- **PCAOB AS 1105 amendments** on technology-assisted analysis apply to audits of fiscal years beginning on or after 15 Dec 2025 (PCAOB-TAA-2024). New paragraph .10A requires auditors to understand the source of external electronic information provided by the company and its handling, and to test the information or the controls (PCAOB-PS2025-004; staff examples issued Oct 2025, PCAOB-STAFF-1105-2025). This bears directly on matching, vouching and bank-data feeds.
- **IAASB exposure drafts** for ISA 330, 500 and 520 (published 5 Aug 2026; comments due 15 Dec 2026 per the landscape): ED-500 gives guidance, not a requirement, on technological tools, because it is premature to settle one workable model and GenAI tools may make it impossible to fully evaluate inputs or operation (IAASB-ED500-2026, EM paras 67–70). ED-500 also clarifies the investigation of outliers and exceptions (EM paras 63–64). ED-520 gives examples of technology-built expectations (IAASB-ED520-2026, A20).
- **FRC guidance (March 2026):** risk categories (deficient output, misuse of output, non-compliant methodology), documentation of tool use on the audit file, and a warning that the persuasiveness of whole-population output may be hard to compare with traditional procedures (FRC-GENAI-2026, pp.18–19, 49–53). The FRC's June 2025 guidance said AI tools were moving beyond experimentation in certain audit scenarios (FRC-AIAUDIT-2025).
- **IFIAR:** monitoring of tool impact is sometimes unclear between network and member firm (IFIAR-TTF-2025, section 1). Most inspections had seen minimal AI or GenAI in public-company audits to that date (section 3).
- **PCAOB staff (July 2024):** firms viewed standards as no impediment; some firms barred GenAI on audit procedures; global networks were further along than non-affiliated firms (PCAOB-GENAI-2024; staff view).

### Frontier signals (dated, sourced)

- **2026-10-15:** Contributed article warns firms not to sell "we test everything" as certainty, and recommends shadow-mode runs on completed engagements before cutover (LEDGERLINE-CPAPA-2026).
- **2026-09-22:** DataSnipper launches Alwin, agents running multi-step procedures end to end with logged steps; MindBridge announces Agentic Risk Assessment and an agent that designs analyses (DATASNIPPER-ALWIN-2026, MINDBRIDGE-ARA-2026).
- **2026-08-05:** IAASB exposure drafts on audit evidence, risk response and analytical procedures (IAASB-ED500-2026, IAASB-ED520-2026).
- **2026-06-29:** BDO UK expands MindBridge across audit after a trial (MINDBRIDGE-BDOUK-2026).
- **2026-06-08:** Fieldguide Field Orchestrator coordinates testing agents for an end-to-end substantive test (FIELDGUIDE-ORCH-2026).
- **2026-05-21:** BDO NL and Rabobank test direct consent-based bank data, aimed at 100% testing and continuous audit (CIRCIT-RABOBANK-BDONL-2026).
- **2026-04-07:** EY says agents are in all audit phases and expects end-to-end support by 2028 (EY-CANVAS-2026).
- **2025-10-28:** PwC Australia pilots an AI-native platform on five audit clients, targeting all clients by 2028 (PWCAU-AT-2025).
- **2025-09-18 and 2025-10-01:** PCAOB policy statement and staff examples on AS 1105 paragraph .10A, ahead of the amendments taking effect for fiscal years beginning on or after 15 Dec 2025 (PCAOB-PS2025-004, PCAOB-STAFF-1105-2025, PCAOB-TAA-2024).

### Workforce and role effects

- Platforms put preparers into agent-building and reviewers into agent-review roles; FGMK splits agents by preparer, reviewer and QC (DATASNIPPER-FGMK-2026).
- First-year staff doing complex revenue testing once reviewers have time (FIELDGUIDE-SANVILLE-2026).
- PwC hires engineers and prefers dual-track CPA and data-science recruits (PWC-AT-2025); some people move into roles building, testing and monitoring AI (CFOBREW-PWC-2025).
- AI-skilled roles were almost 7% of Big Four postings in 2025 against under 2% in 2022; audit roles were just under 3% (COMPUTERWORLD-FT-2026, a report of an FT analysis of more than 50,000 postings; see also RESULTSENSE-2026). Computerworld notes the industry is adapting to AI undercutting some junior roles.
- 81% of tax and audit professionals say they use AI regularly (TRI-FOP-2026); the same paper stresses that junior staff still need structured development to build judgment when work is automated.
- Pre-GenAI evidence: AI investment links to fewer accounting employees after three to four years (FEDYK-2022).
- Deloitte's Omnia has a "tutor mode" for on-demand micro-training in the flow of work (DELOITTE-OMNIA-2026).

### Objections and concerns practitioners raise

- **Expectation gap:** testing every transaction is not a guarantee of no error; marketing it that way widens the gap (LEDGERLINE-CPAPA-2026).
- **Misreading screening output as completeness**, for example treating a lease-screening summary as a full contract review (FRC-GENAI-2026, p.18).
- **Auditors may discount AI-sourced contradictory evidence** relative to a human specialist when judging complex estimates (COMMERFORD-2022).
- **Tools not used as intended** and thin follow-up of outliers (IFIAR-TTF-2025, p.5).
- **Over-reliance risk:** an RSM Australia partner warns over-reliance on AI over judgment could introduce errors (PWCAU-AT-2025). RSM Australia advises scepticism toward tools marketed as auditing a balance (RSM-AUS-2026).
- **Evidence the input-output model cannot be fully tested** for GenAI tools (IAASB-ED500-2026, EM para 68).
- **Privacy:** some firms bar GenAI on audit procedures because of client-data concerns (PCAOB-GENAI-2024). FGMK requires that client data not train models (DATASNIPPER-FGMK-2026).
- **Speed of change and unrealised savings:** PwC reports the pace of change as the biggest surprise and savings "not that drastic yet" (CFODIVE-PWC-2026).
- **Fee tension:** earlier interview evidence cited in the drone study reports clients expect efficiency to lower fees while auditors say they must recoup technology investment (CHRIST-DRONE-2021, note 2).

### Interview probes for an advisor

1. For each substantive step where you use an AI tool (journal entries, vouching, confirmations, contracts), how did you calibrate it before using it: a parallel run against past engagements, what was the miss rate, and who signed off?
2. When you test 100% of a population, how many more exceptions do you now get, who triages them, and how do you decide what extends testing?
3. Where does the time saved go (reviewer queue, EQR, more testing, fewer hours billed), and has it changed your fee or realization?
4. What is the binding constraint: client data access and population completeness, tool accuracy, methodology permission, or staff capability?
5. How do you describe the procedure to the audit committee, the client and the inspector (sample versus full population), and what do you document on the file?

---

## 4. Routed to other modules

| Item | Target module | Why |
|---|---|---|
| Disclosure-checklist agents: Thomson Reuters Disclosure Review (about 30% of eligible Disclosure-module customers using it, close to 300 analyses a month; 23 Sep 2026), Caseware Verity Disclosure Checklist Agent (beta firms saved 2.7 hours per run, vendor figure), KPMG Financial Report Analyzer, DataSnipper Disclosure Agents (TR-DISCLOSURE-2026, CASEWARE-VERITY-2026, KPMG-CLARA-2025, DATASNIPPER-AGENTS-2025) | completion-reporting | Disclosure review is a completion step |
| MindBridge Agentic Risk Assessment and Analysis Designer Agent (MINDBRIDGE-ARA-2026); PwC Simplified Audit planning tool and Advanced Walkthrough Assistant (PWC-AT-2025); Caseware Verity planning-review scenario (CASEWARE-VERITY-2026) | planning-risk-assessment | Risk assessment and planning |
| Fieldguide Field Agents for Testing (control testing workflow, help-centre article of 24 Jun 2026), Baker Tilly's expansion of Fieldguide across SOC, PCI, HITRUST, ISO, FedRAMP, SOX and internal audit (27 May 2026), the ODP Corporation internal-audit story, KPMG Clara controls agents promised (FIELDGUIDE-HELP-2026, FIELDGUIDE-BAKERTILLY-2026, DATASNIPPER-ODP) | controls-testing / other-assurance | Controls and SOC testing |
| BVR "How Big Four Firms Are Using—and Limiting—AI in Their Valuation Practices" (March 2026, paywalled teaser only; BVR-BIGFOUR-2026); Commerford et al. on auditor reliance on AI for complex estimates (COMMERFORD-2022) | specialists | Estimates and valuation support; this angle found no firm deployment evidence for estimates testing |
| FGMK QC agent run over financial statements alongside independent review; reviewer-side agents (DATASNIPPER-FGMK-2026) | quality-management | Review and QC |
| Grant Thornton Gtap under an alternative practice structure; PwC and RSM investment commitments; Fieldguide customer announcements as platform-wide moves (GT-GTAP-2026, BLOOMBERGTAX-RSM-2025) | acceptance-independence, quality-management | Ownership and independence; firm-level governance |
| FT-based finding on Big Four hiring; TR Institute 81% regular AI use (COMPUTERWORLD-FT-2026, TRI-FOP-2026) | quality-management (workforce lens) | Cross-cutting workforce evidence |
| PwC tool that analyses audit-committee communications (CFODIVE-PWC-2026) | completion-reporting | Audit-committee communications |
| IFIAR's findings on tool certification and network-versus-member monitoring (IFIAR-TTF-2025) | quality-management | Firm-level tool governance |

---

## 5. Sources

Access: `full` means the relevant text was opened and read. Dates are publication dates unless the Notes column says otherwise.

| Ref | Title | Publisher | Type | URL | Date | Access | Notes |
|---|---|---|---|---|---|---|---|
| IFIAR-TTF-2025 | Use of technology in audits: observations, risks and further evolution | IFIAR | regulator | https://www.fsa.go.jp/cpaaob/sonota/kokusai/2025TTFReport.pdf | 2025-03-27 | full | Mirror on the Japan FSA site |
| FRC-GENAI-2026 | Generative and Agentic AI Guidance | FRC | regulator | https://media.frc.org.uk/documents/Generative_and_Agentic_AI_Guidance_crosPeBU.pdf | 2026-03 | full | PDF dated "March 2026"; landscape records 30 Mar |
| FRC-AIAUDIT-2025 | FRC publishes landmark guidance on the uses of AI | FRC | regulator | https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/ | 2025-06-26 | full | |
| PCAOB-TAA-2024 | Amendments Related to Aspects of Designing and Performing Audit Procedures that Involve Technology-Assisted Analysis (Release 2024-007) | PCAOB | regulator | https://pcaobus.org/oversight/standards/implementation-resources-PCAOB-standards-rules/amendments-related-to-aspects-of-designing-and-performing-audit-procedures-that-involve-technology-assisted-analysis-of-information-in-electronic-form | 2024-06-12 | full | Read via text mirror; adoption date as stated on the page |
| PCAOB-PS2025-004 | Policy Statement Regarding Implementation of Paragraph .10A of AS 1105 | PCAOB | regulator | https://assets.pcaobus.org/pcaob-dev/docs/default-source/rulemaking/docket-052/pcaob-release-no-2025-004.pdf | 2025-09-18 | full | |
| PCAOB-STAFF-1105-2025 | Staff Guidance: Examples of Evaluating the Reliability of External Information Provided by the Company in Electronic Form | PCAOB staff | regulator | https://pcaobus.org/standards/documents/staff-guidance-examples-of-evaluating-the-reliability-of-external-information-provided-by-the-company-in-electronic-form.pdf | 2025-10 | full | Staff view, not Board rules |
| PCAOB-GENAI-2024 | Spotlight: Staff Update on Outreach Activities Related to the Integration of Generative AI in Audits and Financial Reporting | PCAOB staff | regulator | https://pcaobus.org/documents/generative-ai-spotlight.pdf | 2024-07 | full | Staff view, not Board policy |
| IAASB-ED500-2026 | Explanatory Memorandum to the ED for Proposed ISA 500 (Revised) | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-500-Exposure-Draft.pdf | 2026-08-05 | full | Release date per landscape; file is in the 2026-08 folder |
| IAASB-ED520-2026 | Explanatory Memorandum to the ED for Proposed ISA 520 (Revised) | IAASB | standard-setter | https://ifacweb.blob.core.windows.net/publicfiles/2026-08/IAASB-Audit-Evidence-Risk-Response-ISA-520-Exposure-Draft.pdf | 2026-08-05 | full | |
| CPACOM-ATR-2025 | Audit Transformation Report: 2025 CPA.com and AICPA Audit Benchmark Survey | CPA.com and AICPA | professional-body | https://www.cpa.com/sites/cpa/files/2025-12/2025_Audit_Transformation_Report.pdf | 2025-12 | full | Survey June–Aug 2025; 54 firms |
| TRI-FOP-2026 | What the "2026 Future of Professionals Report" says tax and audit firm leaders should prioritize | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07 | full | Month from landscape; page shows "July 21" |
| KPMG-CLARA-2025 | KPMG advances AI integration in KPMG Clara smart audit platform | KPMG International | firm | https://kpmg.com/xx/en/media/press-releases/2025/04/kpmg-advances-ai-integration-in-kpmg-clara-smart-audit-platform.html | 2025-04-22 | full | |
| ACCTODAY-KPMG-2025 | KPMG builds AI agents into audit platform | Accounting Today | press | https://www.accountingtoday.com/news/kpmg-builds-ai-agents-into-audit-platform | 2025-04-24 | full | |
| EY-CANVAS-2026 | EY Rolls Out Agentic AI in Assurance Across Its Global Network of Accounting Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/07/ey-rolls-out-agentic-ai-in-assurance-across-its-global-network-of-accounting-firms/181097/ | 2026-04-07 | full | EY's own release not opened |
| ACCTODAY-EY-2024 | EY beefs up use of AI amid $1B investment | Accounting Today | press | https://accountingtoday.com/news/ey-beefs-up-use-of-ai-amid-1b-investment | 2024-10-16 | full | Older than 18 months; foundation |
| DELOITTE-OMNIA-2026 | Deloitte Unveils Connected Agentic Intelligence in Deloitte Omnia | Deloitte | firm | https://www.deloitte.com/global/en/about/press-room/unveils-connected-agentic-intelligence-omnia-advance-audit-assurance.html | 2026-06-24 | full | |
| PWC-AT-2025 | PwC expects end-to-end AI audit automation within 2026 | Accounting Today | press | https://accountingtoday.com/news/pwc-expects-end-to-end-ai-audit-automation-within-2026 | 2025-10-28 | full | |
| CFOBREW-PWC-2025 | A look at PwC's "next generation" audit | CFO Brew | press | https://www.cfobrew.com/stories/2025/11/05/a-look-at-pwc-s-next-generation-audit | 2025-11-05 | full | |
| CFODIVE-PWC-2026 | PwC exec ushers in AI-assisted audits, awaits bigger time savings | CFO Dive | press | https://www.cfodive.com/news/pwc-exec-ushers-ai-assisted-audits-awaits-bigger-time-savings/832412/ | 2026-10-07 | full | |
| PWCAU-AT-2025 | PwC Australia rolls out pilot program for AI-assisted full audits | Accounting Times | press | https://www.accountingtimes.com.au/profession/pwc-australia-rolls-out-pilot-program-for-ai-assisted-full-audits | 2025-10-28 | full | |
| GT-GTAP-2026 | Grant Thornton launches AI platform for audit business | Consultancy.org (Consulting.us) | press | https://www.consulting.us/news/13378/grant-thornton-launches-ai-platform-for-audit-business | 2026-05-11 | full | |
| BLOOMBERGTAX-RSM-2025 | Auditor RSM Commits $1 Billion to AI Growth Across US Firm | Bloomberg Tax | press | https://news.bloombergtax.com/financial-accounting/auditor-rsm-commits-1-billion-to-deploy-ai-tools-across-us-firm | 2025-06-09 | search-only | Paywalled teaser only |
| RSM-AUS-2026 | AI in Audit and Accounting Firms: Use Cases and Risks | RSM Australia | firm | https://www.rsm.global/australia/insights/what-role-ai-audit-and-accounting-firms | 2026-08 | full | Page metadata shows 11 and 17 Aug 2026 |
| BUZZACOTT-PRIME-2025 | How Buzzacott's AI partnership is elevating audit quality | PrimeGlobal | firm | https://www.primeglobal.net/news/how-buzzacotts-ai-partnership-is-elevating-audit-quality | 2025-12-18 | full | |
| MINDBRIDGE-BDOUK-2026 | BDO UK and MindBridge Partner to Accelerate Data-Driven Audit | MindBridge | vendor | https://www.mindbridge.ai/news/bdo-uk-and-mindbridge-partner-to-accelerate-data-driven-audit | 2026-06-29 | full | Read via text mirror |
| MINDBRIDGE-KPMG-2024 | Innovating Audits: KPMG's AI-Driven Audit Approach Leveraging MindBridge AI | MindBridge | vendor | https://www.mindbridge.ai/docs/resources/customer-stories/KPMG/KPMG-AI-Driven-Audit-with-MindBridge_02262024.pdf | 2024-02 | full | Date from file name |
| MINDBRIDGE-CHERRY-2022 | How Cherry Bekaert drove ROI for their audit engagements | MindBridge | vendor | https://www.mindbridge.ai/resources/case-studies/cherry-bekaert-llp-case-study | 2022 | full | Year inferred; read via text mirror |
| MINDBRIDGE-ARA-2026 | MindBridge Advances Financial Oversight for the Agentic Era | MindBridge (Business Wire) | vendor | https://www.bnnbloomberg.ca/press-releases/2026/09/22/mindbridge-advances-financial-oversight-for-the-agentic-era-with-new-platform-capabilities/ | 2026-09-22 | full | |
| TR-AGENTIC-2025 | Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows.html | 2025-11-05 | full | |
| TR-DISCLOSURE-2026 | Turning Disclosure Review From Manual Matching Into AI-Assisted Confidence | Thomson Reuters | vendor | https://www.thomsonreuters.com/en-us/posts/innovation/turning-disclosure-review-from-manual-matching-into-ai-assisted-confidence/ | 2026-09-23 | full | Routed |
| DATASNIPPER-PRODUCTIVITY-2026 | DataSnipper Delivers $1.4B in Productivity Savings in 2025 | DataSnipper | vendor | https://www.datasnipper.com/resources/datasnipper-delivers-1-4b-in-productivity-savings-in-2025-as-audit-and-finance-enter-the-ai-era | 2026-01-14 | full | |
| DATASNIPPER-CHILE-2026 | DataSnipper Brings AI-Powered Audit Technology to Chile | DataSnipper | vendor | https://www.datasnipper.com/resources/datasnipper-brings-ai-powered-audit-technology-to-chile | 2026-03-25 | full | |
| DATASNIPPER-AGENTS-2025 | DataSnipper and Microsoft Launch AI Agents for Audit and Finance | DataSnipper | vendor | https://www.datasnipper.com/resources/datasnipper-and-microsoft-launch-ai-agents-for-audit-and-finance | 2025-10-01 | full | Routed (disclosure agents) |
| DATASNIPPER-ALWIN-2026 | DataSnipper Launches Alwin | DataSnipper | vendor | https://www.datasnipper.com/resources/datasnipper-launches-alwin-end-to-end-agentic-automation-for-audit-finance | 2026-09-22 | full | |
| DATASNIPPER-CONNECT-2026 | DataSnipper Connect New York 2026: 6 Takeaways on AI and Auditing | DataSnipper | conference | https://www.datasnipper.com/resources/the-6-biggest-takeaways-from-datasnipper-connect-new-york-2026 | 2026 | full | Vendor recap of a customer conference; page undated |
| DATASNIPPER-FGMK-2026 | FGMK Uses Alwin to Automate Larger, More Complex Audit Work Securely | DataSnipper | vendor | https://www.datasnipper.com/resources/fgmk-alwin-success-story | 2026 | full | Page undated |
| DATASNIPPER-PAYABLES-2026 | 5 AP Audit Procedures External Auditors Run With a Prebuilt Agent | DataSnipper | vendor | https://www.datasnipper.com/resources/5-payables-and-expenses-procedures-external-auditors-can-run-with-a-prebuilt-agent | 2026 | full | Page undated; names three-way match and duplicate payment agents |
| DATASNIPPER-ODP | DataSnipper Success Stories - The ODP Corporation | DataSnipper | vendor | https://www.datasnipper.com/resources/the-odp-corporation | 2026 | full | Page undated; internal audit |
| FIELDGUIDE-SANVILLE-2026 | How Sanville & Co passed a PCAOB inspection with zero comment forms in under a year with Fieldguide | Fieldguide | vendor | https://www.fieldguide.io/case-studies/how-sanville-co-passed-a-pcaob-inspection-with-zero-comment-forms-in-under-a-year-with-fieldguide | 2026 | full | Page undated; year inferred |
| FIELDGUIDE-FIELDAGENTS-2025 | Increase Capacity and Audit Quality with Field Agents for Financial Audit | Fieldguide | vendor | https://www.fieldguide.io/blog/increase-capacity-and-audit-quality-with-field-agents-for-financial-audit | 2025-06-04 | full | |
| FIELDGUIDE-ORCH-2026 | Introducing Field Orchestrator | Fieldguide | vendor | https://www.fieldguide.io/blog/field-orchestrator | 2026-06-08 | full | |
| FIELDGUIDE-CHERRY-2026 | Cherry Bekaert Selects Fieldguide as Strategic AI Partner | Fieldguide | vendor | https://www.fieldguide.io/blog/cherry-bekaert-fieldguide-financial-audit | 2026-06-03 | full | |
| FIELDGUIDE-BAKERTILLY-2026 | Baker Tilly advances AI-enabled assurance and advisory delivery with Fieldguide | Fieldguide | vendor | https://www.fieldguide.io/blog/baker-tilly-advances-ai-enabled-assurance-and-advisory-delivery-with-fieldguide | 2026-05-27 | full | Routed |
| FIELDGUIDE-HELP-2026 | Field Agents for Testing | Fieldguide Help Center | vendor | https://help.fieldguide.io/en/articles/12292640-field-agents-for-testing | 2026-06-24 | full | Routed (control testing) |
| FIELDGUIDE-LSL-2026 | LSL CPAs Selects Fieldguide to Transform Financial Audit Delivery | Fieldguide | vendor | https://www.fieldguide.io/blog/lsl-cpas-financial-audit | 2026-04-28 | full | Selection announcement; no outcomes |
| CIRCIT-MOORE-2026 | Moore Polska saves 20 hours per Audit with Circit | Circit | vendor | https://circit.io/case-study/moore-polska-case-study | 2026-05-13 | full | Likely a republication date |
| CIRCIT-BEEVER-2026 | Why Beever & Struthers (now Menzies) Made Circit Central to Audit Delivery | Circit | vendor | https://circit.io/case-study/beever-struthers-case-study | 2026-06-26 | full | |
| CIRCIT-CROWE-2026 | How Crowe Spain boosted accuracy and improved response rates with Circit | Circit | vendor | https://circit.io/case-study/crowe-case-study | 2026-05-19 | full | |
| CIRCIT-KRESTON-2026 | How Kreston Iberaudit improved efficiency and control with Circit | Circit | vendor | https://circit.io/case-study/kreston-iberaudit | 2026-07-13 | full | |
| CIRCIT-RABOBANK-BDONL-2026 | Rabobank & BDO NL: Building the Foundation for Continuous, Trusted Audit Data | Circit | vendor | https://circit.io/case-study/rabobank-bdo-nl | 2026-05-21 | full | |
| LEDGERLINE-CPAPA-2026 | Testing Every Transaction Changes the Audit - Here's What Firms Should Know Before They Sell It | CPA Practice Advisor (Ledgerline CEO) | press | https://www.cpapracticeadvisor.com/2026/10/15/testing-every-transaction-changes-the-audit-heres-what-firms-should-know-before-they-sell-it/191713/ | 2026-10-15 | full | Contributed article |
| LEDGERLINE-SITE-2026 | Ledgerline: Specialist 401(k) and 403(b) plan audits | Ledgerline | firm | https://ledgerlineaudit.com | 2026-10 | full | Undated; read 2026-10-16 |
| COMPUTERWORLD-FT-2026 | The Big Four accounting firms are now hiring more AI specialists than accountants | Computerworld | press | https://www.computerworld.com/article/4173296/the-big-four-accounting-firms-are-now-hiring-more-ai-specialists-than-accountants.html | 2026-05-19 | full | Reports an FT analysis of job postings; FT original not opened |
| RESULTSENSE-2026 | Big Four AI hiring overtakes auditor recruitment | Resultsense | press | https://www.resultsense.com/insights/2026-05-20-big-four-ai-hiring-eclipses-audit-frc-implications/ | 2026-05-20 | full | Secondary commentary on the FT analysis; date from URL |
| FEDYK-2022 | Is artificial intelligence improving the audit process? | Review of Accounting Studies (Fedyk, Hodson, Khimich, Fedyk) | academic | https://ideas.repec.org/a/spr/reaccs/v27y2022i3d10.1007_s11142-022-09697-x.html | 2022 | full | Abstract page |
| COMMERFORD-2022 | Man Versus Machine: Complex Estimates and Auditor Reliance on Artificial Intelligence | Journal of Accounting Research | academic | https://ideas.repec.org/a/bla/joares/v60y2022i1p171-201.html | 2022 | full | Abstract page |
| CHRIST-DRONE-2021 | Prepare for takeoff: drone-enabled inventory audit procedures | Review of Accounting Studies | academic | https://link.springer.com/article/10.1007/s11142-020-09574-5 | 2021 | full | Abstract and notes via text mirror |
| EY-DRONE-JOFA-2018 | Using drones to enhance audits | Journal of Accountancy podcast | podcast | https://www.journalofaccountancy.com/podcast/using-drones-to-enhance-audits/ | 2018-07-30 | full | Foundation; older than 18 months |
| ARXIV-AUDITCOPILOT-2025 | AuditCopilot: Leveraging LLMs for Fraud Detection in Double-Entry Bookkeeping | arXiv | academic | https://arxiv.org/abs/2512.02726 | 2025-12-02 | full | Abstract |
| ARXIV-FAB-2026 | FinancialAuditBench | arXiv | academic | https://arxiv.org/abs/2609.32835 | 2026-09-26 | full | Abstract |
| ARXIV-LLMAUDIT-2025 | Automating Financial Statement Audits with LLMs | arXiv | academic | https://arxiv.org/abs/2506.17282 | 2025-06 | full | Abstract; used in Gaps only |
| BVR-BIGFOUR-2026 | How Big Four Firms Are Using—and Limiting—AI in Their Valuation Practices | Business Valuation Resources | press | https://www.bvresources.com/articles/business-valuation-update/how-big-four-firms-are-using-and-limiting-ai-in-their-valuation-practices | 2026-03 | search-only | Paywalled teaser; routed |
| CASEWARE-VERITY-2026 | From AiDA to agentic: How Caseware's AI has evolved | Caseware | vendor | https://www.caseware.com/resources/blog/from-aida-to-agentic-how-casewares-ai-has-evolved | 2026-07-28 | full | Routed |

---

## 6. Gaps

- **Search quota.** The web-search quota ran out mid-task, so these leads were not followed by search: customers of Fieldguide Field Orchestrator; the text of Bloomberg Tax's 1 Apr 2026 "KPMG to Test Advanced AI Agents in Next Phase"; Aprio's and LSL's Fieldguide outcomes; Clark's "Material Intelligence" launch (seen only as an Accounting Today headline, 16 Oct 2026, text unopened); Wolters Kluwer, Validis and Trullion audit tools; the FRC 2026 audit-quality inspection report; direct job postings. Only link-following with `curl` was used afterwards.
- **No independent quality evidence for any named tool in a live audit.** No false-positive, false-negative or override rate, no parallel-run result and no inspection finding specific to AI in substantive procedures was found for 2025–2026. IFIAR gives only frequency and generic finding types; the FinancialAuditBench and AuditCopilot results are benchmarks on synthetic data (ARXIV-FAB-2026, ARXIV-AUDITCOPILOT-2025). A one-line benchmark result: five-stage LLM audit tests find that models identify errors with transaction history but struggle to explain them, cite standards and execute complete audits (ARXIV-LLMAUDIT-2025).
- **Blocked or unreachable.** SSRN randomized field experiment on LLMs and audit quality in inventory valuation (Cloudflare challenge on SSRN and on the mirror); Gartner Aug 2026 release (403); `pwc.co.uk` transparency report and `pwc.ch` paper (403); `accountancyage.com` (Cloudflare block); `controllerscouncil.org` and `preprints.org` (blocked; the July 2026 drone-imagery preprint was not read); Springer full text (paywall, abstract read only); BVR articles (teaser only); Bloomberg Tax (teaser only); a `datasnipper.com` resource with spaces in the URL (failed); EY's own 7 Apr 2026 press release (a guessed URL returned 404); Deloitte press-room index (stub page).
- **Undated or doubtfully dated pages.** DataSnipper success stories and recap pages, the Sanville & Co case study, and the Cherry Bekaert case study carry no publication date; years given are inferences stated in the Notes. Circit's case-study dates look like site republication dates. The MindBridge KPMG date is taken from a file name.
- **Primary of the NAO claim.** The UK Parliament PAC hearing record behind DataSnipper's NAO figures (£400,000; up to three times faster) was not found (the NAO annual-report URL tried returned 404).
- **Thin areas.**
  - Estimates testing: nothing on firm deployments (routed to specialists).
  - Revenue contract review: no named audit deployment with measures beyond a regulator's hypothetical example and one unnamed-customer vendor figure.
  - Inventory observation: no 2025–2026 firm deployment evidence; only 2018 and 2021 sources.
  - Non-Big-Four firms outside the US and UK: only named users of vendor tools (BDO UK, BDO NL, Moore Polska, Crowe Spain, Kreston Iberaudit, Beever & Struthers).
  - Job postings: only a secondary report of an FT analysis, not postings that show substantive-testing use.
  - Conference and podcast depth: one vendor customer-conference recap and a 2018 podcast.
- **Open data conflicts.** CPA.com's report says both "about one in four" and "about one-third" of firms use no AI (landscape conflict, not resolved); EY "all phases now" versus "end-to-end by 2028"; PwC "end-to-end in 2026" versus "not that drastic yet" in Oct 2026.
- **Landscape check.** The landscape's DataSnipper "600,000+ users in 175 countries" is confirmed on the 25 Mar 2026 page as a vendor claim. The landscape's Grant Thornton date (7 May) differs from the opened article (11 May 2026). The landscape's PwC Evidence Match list (cash, receivables, payables) is extended to fixed assets by the CFO Brew report.
