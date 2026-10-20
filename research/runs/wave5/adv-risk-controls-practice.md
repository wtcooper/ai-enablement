# Advisory / risk-controls / practice: what firms and in-house teams actually do

Run date: 2026-10-20. Wave 5. Archetype: `advisory`. Module: `risk-controls`. Angle: `practice`.
Refs follow `PUBLISHER-SHORT-YYYY`. Refs shared with `landscape-advisory.md` reuse its spelling. "access: full" means the page or PDF was opened and read in this run (directly, or via the r.jina.ai mirror where noted). "access: search-only" means it surfaced only in a search result.

---

## 1. Summary

**Where the practice actually is.** In this module the work that has visibly changed is **control testing and the paperwork around it** (SOX and internal-audit test execution, evidence handling, workpaper drafting). The change shows up in three places:

1. **In-house internal-audit teams** at named companies (Reddit, Klaviyo, FJ Management, Havertys, Microsoft's own finance team). These are vendor-published or self-reported, and none comes with an independent measurement.
2. **Advisory and outsourcing firms** building or buying agentic testing for co-sourced and outsourced internal audit. Examples: Riveron (co-sourced and outsourced IA), RSM (Beacon, with Andera, announced 2026-08-28), Protiviti (Fieldguide alliance, 2026-03-03), Cherry Bekaert and Aprio (Fieldguide), and PwC (Dynamic Testing).
3. **AI-native vendors** selling the same testing straight to enterprise audit teams (Petual, Midship, Andera, Optro's Autonomous Testing). This is the main commercial threat to co-sourcing.

**Seven points the evidence supports:**

1. **Every deployment keeps a human reviewer.** Riveron says every test result is reviewed by its professionals before it enters the workpaper (RIVERON-MONDAQ-2026). RSM says the AI "does not make judgment calls" and flags ambiguity as an open item (RSM-BEACON-2026). Havertys says managers keep approving the work (OPTRO-HAVERTYS-2026). Nobody publishes an automate-with-exceptions-only design for control testing.
2. **Named in-house cases are the best practice evidence, but no figure is independently measured.** Reddit's reported 60% average cut in testing time per control comes from the vendor's press release (OPTRO-AGENTS-2026). Microsoft's 850 hours and $185K are self-reported and do not say how they were measured (MSFT-SOXAGENT-2026). The grade ceiling for the whole module is therefore **B**. No A-grade entry exists under the 2026-10-17 rule.
3. **There is no published override rate, error rate or parallel-run result for AI control testing.** The only practitioner method for one is a recommendation to run old and new side by side on 5-10 controls (CPAPA-5Q-2026, by a vendor CEO). Grant Thornton warns that AI can flag false exceptions where the business relies on undocumented practice (GT-INFERENCEGAP-2026).
4. **Sourcing is the model-level change.** Havertys started with the IT controls it already paid outsiders to test (OPTRO-HAVERTYS-2026). Midship's seed announcement says its agents run SOX testing lifecycles (MIDSHIP-SEED-2026). Co-sourcing providers are responding by embedding agents in their own delivery (Riveron, RSM, Protiviti).
5. **Client AI governance is a real advisory line, but public evidence is mostly positioning.** The one named-practice case is Grant Thornton's anonymised AI-governance lifecycle audit for a large global bank (GT-BANK-2026). RSM is hiring AI-risk consultants (RSM-JOB-AIRISK-2026). COSO's February 2026 GenAI guidance gives the reference roadmap (COSO-GENAI-2026). Mid-market client deployments are not documented.
6. **Surveys point to a governance gap on the client side.** 63% of surveyed organisations have no formal AI risk appetite or governance framework (AUDITBOARD-FOCUS-2025). 78% lack strong confidence they could pass an independent AI governance audit within 90 days (GT-AIIMPACT-2026). 34% of 417 GRC and audit leaders report acting on an inaccurate agent output (OPTRO-AGENTICREPORT-2026, vendor survey).
7. **Landscape correction.** The landscape file doubted whether "42% fully assurance ready" was a conflation. The KPMG release itself says fewer than half of organisations (42%) are fully assurance-ready, and separately that 42% of assurance-ready organisations are confident about scaling (KPMG-AIFINANCE-2026). Both statements are in the source.

**Counts.** 19 use cases: A = 0, B = 11, C = 6, D = 2. 46 sources listed: 44 opened (two of them, ANDERA-HOME-2026 and IIA-GAM-2026, used only as context) and 2 search-only job-posting leads (CITI-JOB-2026, AMEX-JOB-2026). Types: firm 15, press 11, vendor 7, survey 6, job-posting 3, conference 2, standard-setter 1, professional-body 1. See section 5.

---

## 2. Use cases

```yaml
- id: advisory-risk-controls-01
  title: "In-house internal-audit teams use an agent to run the first pass of SOX control tests"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "SOX testing is repetitive: match evidence to samples, check attributes, document the result. Teams spend most of their hours here and little on judgment-heavy work."
  solution: "The audit team's GRC platform runs agentic testing on defined controls. The agent reads the evidence, tests each attribute and writes up the result with a citation trail. The auditor reviews and signs off. Named users are Reddit, Klaviyo and FJ Management (in-house teams, not advisory firms). The firm-side equivalent is use case 03."
  outcomes:
    - lever: speed
      description: "Reddit's internal audit team reports automating 175 controls in the first three months and cutting testing time per control by about 60% on average. It has since expanded agentic testing to over 75% of its SOX controls and to other recurring testing programs."
      figure: "175 controls (more than 40% of SOX scope) in 3 months; 60% average reduction in testing time per control; over 75% of SOX controls now on agentic testing"
      measures: "Per the vendor release: 175 controls automated divided by SOX scope (more than 40%); reduction in testing time per control, averaged. Baseline and measurement method are not stated."
      provenance: vendor-published
      source_ref: OPTRO-AGENTS-2026
    - lever: quality
      description: "Klaviyo's VP of Internal Audit and Compliance says accuracy is non-negotiable and the audit trail shows how each conclusion was reached. No metric given."
      figure: "none published"
      measures: "Quote only; no count or rate"
      provenance: vendor-published
      source_ref: OPTRO-AGENTS-2026
  prerequisites:
    - "SOX tests, results and documentation already held in one platform (Havertys says clean, consistent data gave it confidence to move to autonomous testing)"
    - "Controls described with attributes and evidence rules precise enough for an agent to apply"
  risks_and_guardrails:
    - "Every figure comes from the vendor's own press release; the customers' internal measurements are not published"
    - "Optro's own survey reports 34% of organisations have acted on an inaccurate agent decision or output (OPTRO-AGENTICREPORT-2026), so first-pass test output needs review"
  human_checkpoints:
    - "Auditor review and approval of each test conclusion (Havertys: 'same review processes in place as before')"
  role_evolution: "Klaviyo says the team spends less time on manual work and more on judgment and foresight (OPTRO-AGENTS-2026). Havertys describes auditors moving toward process design, business risk and root-cause analysis (OPTRO-HAVERTYS-2026)."
  evidence_grade: B
  sources:
    - {ref: OPTRO-AGENTS-2026, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: "2026-10-14", access: full, locator: "Autonomous Testing paragraph (Reddit); customer quotes (Klaviyo, FJ Management)"}
    - {ref: OPTRO-HAVERTYS-2026, title: "Havertys Brings Agentic AI Into Internal Audit", publisher: Optro, type: vendor, url: "https://optro.ai/blog/havertys-furniture-success-story", date: "2026-09-04", access: full, locator: "paragraphs on review and 'humans in the loop'"}
  last_reviewed: "2026-10-20"
  notes: "Vendor: Optro (appears to be AuditBoard's current brand: the AuditBoard-hosted 2025 blog refers to Optro; no rebrand announcement was opened). Grade is B, not A, because the figures are the vendor's report, not a customer-reported tracked metric. These are companies, not advisory firms; the entry tells an advisor what their clients' in-house teams are doing."

- id: advisory-risk-controls-02
  title: "ITGC change-management testing agents extract ticket attributes and mark up evidence (Microsoft Frontier Finance)"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Auditors open tickets in several systems to check testing, approvals and timing against deployment, then copy attributes into spreadsheets. Ticket formats vary and the work crowds out exception analysis."
  solution: "Two agents built with Copilot Studio. An attribute-extraction agent reads tickets, pulls tester, approver and dates into a standard table and pre-fills pass/fail logic. An evidence-annotation agent marks where each attribute was found in the source evidence."
  outcomes:
    - lever: capacity
      description: "Microsoft's innovation story lists 850 hours of annual time savings and $185K of annual cost savings, launched in 1 to 3 months."
      figure: "850 hours per year; $185K per year; launched in 1-3 months"
      measures: "Annual time savings and annual cost savings as labelled in the story; it does not say whether they are measured or estimated, or against what baseline"
      provenance: self-reported
      source_ref: MSFT-SOXAGENT-2026
  prerequisites:
    - "Ticket data accessible to the agents"
    - "Rules-based pass/fail logic for change-management attributes"
  risks_and_guardrails:
    - "Single self-published one-page story; no error rate or reviewer-override data"
  human_checkpoints:
    - "The story says the output is audit-ready and traceable to source evidence; the auditor still validates (the page describes auditors as required to validate evidence; the review step after the agents is not described in detail)"
  role_evolution: "The story says auditors shift from administrative evidence handling to higher-risk exceptions and professional judgment, without adding headcount."
  evidence_grade: B
  sources:
    - {ref: MSFT-SOXAGENT-2026, title: "Microsoft Frontier Finance Innovation Story: SOX Change Management Testing Agent", publisher: Microsoft, type: vendor, url: "https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/SOX-Change-Management-Testing-Agent.pdf", date: "2026", access: full, locator: "Solution Overview; Key Results panel"}
  last_reviewed: "2026-10-20"
  notes: "Page carries no day; the URL path is 'fy26' (Microsoft's fiscal year 2026 runs July 2025 to June 2026), so '2026' is a bound, not a publication date. The customer is Microsoft's own finance function, a vendor of the tools. Grade B and not A because the story gives no measurement method."

- id: advisory-risk-controls-03
  title: "Advisory firms embed agentic control testing into co-sourced and outsourced internal-audit and SOX delivery"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Co-sourced and outsourced SOX testing is billed on testing hours. Evidence arrives in mixed formats, workpapers must stand up to external-auditor reliance, and clients want shorter cycles."
  solution: "Firms run different AI agents at specific steps of the engagement workflow (evidence handling, attribute testing, annotated workpaper) on their own methodology, with professional review before anything enters the file. Examples are Riveron (co-sourced and outsourced IA, per its own article), RSM Beacon with Andera (control test workpapers; announced 2026-08-28), Protiviti on Fieldguide (evidence request/review, sample selection, control evaluation, standard workpapers; alliance announced 2026-03-03) and PwC Dynamic Testing (agentic workflow with review checkpoints)."
  outcomes:
    - lever: speed
      description: "PwC says automated test-procedure generation, evidence parsing and annotation can reduce effort by 30-40% and shrink turnarounds from weeks to days. The page gives no sample, client or date."
      figure: "30-40% effort reduction"
      measures: "Effort reduction on controls testing, as stated by PwC; denominator and baseline not stated"
      provenance: vendor-published
      source_ref: PWC-DYNTEST-2026
    - lever: quality
      description: "Riveron says it measures AI-enabled programs by shorter testing cycles, faster escalation to management, easier-to-review workpapers and more capacity for remediation follow-through, not by hours saved. It publishes no figures."
      figure: "none published"
      measures: "Indicators listed, not measured results"
      provenance: self-reported
      source_ref: RIVERON-MONDAQ-2026
  prerequisites:
    - "Firm testing methodology codified well enough to configure agents (RSM: uses its own proprietary testing methodology; Aprio: its professionals configure the vendor platform to the firm's engagement methodology)"
    - "Control metadata, test attributes, evidence requirements, sampling logic and exception rules defined more precisely than many programs have historically (RIVERON-MONDAQ-2026)"
    - "Agreement from clients on handling of their data (RSM says Beacon client data is kept in a segregated environment and is not used to train Andera's commercial product)"
  risks_and_guardrails:
    - "Missing documentation may mean a control was performed informally, not that it failed (Riveron). Treat 'missing support' and 'true exception' as separate outcomes."
    - "No published parallel-run, override or error figures for any of these firms"
    - "Independence: internal-audit outsourcing is generally restricted for a firm's own audit clients. This is background from the landscape and was not confirmed from an independence rule in this run; check AICPA, SEC and PCAOB rules before relying on it."
  human_checkpoints:
    - "Riveron: every test result reviewed by experienced professionals before it becomes part of the workpaper"
    - "RSM Beacon: ambiguous items flagged as open items for a human auditor; reviewers see the reasoning log beside the evidence"
    - "PwC: users review and edit AI-generated test instructions before execution"
  role_evolution: "Riveron says teams focus more on review, challenge, exception analysis and stakeholder dialogue. Protiviti says the aim is to enhance, not replace, human judgment. Neither gives staffing numbers."
  evidence_grade: B
  sources:
    - {ref: RIVERON-MONDAQ-2026, title: "AI In Internal Audit And SOX: Applying Methods That Work", publisher: Riveron (via Mondaq), type: firm, url: "https://www.mondaq.com/unitedstates/audit/1805956/ai-in-internal-audit-and-sox-applying-methods-that-work", date: "2026-06-24", access: full, locator: "paragraphs 'Riveron is applying this approach in co-sourced and outsource internal audit engagements' and 'Every test result is reviewed'"}
    - {ref: RSM-BEACON-2026, title: "RSM launches AI-guided internal audit platform 'Beacon' with Andera", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/rsm-launches-ai-guided-internal-audit-platform-beacon-with-andera", date: "2026-08-28", access: full, locator: "paragraphs 2-5 (agent-based workflow; 'the AI does not make judgment calls'; segregated environments)"}
    - {ref: PROTIVITI-FIELDGUIDE-2026, title: "Protiviti Announces Strategic Alliance with Fieldguide to Accelerate AI-Enabled Internal Audit, SOX, and Controls Transformation", publisher: Protiviti / PR Newswire (via finviz), type: firm, url: "https://finviz.com/news/328216/protiviti-announces-strategic-alliance-with-fieldguide-to-accelerate-ai-enabled-internal-audit-sox-and-controls-transformation", date: "2026-03-03", access: full, locator: "paragraphs 2-4"}
    - {ref: PWC-DYNTEST-2026, title: "What if controls testing could be done in a fraction of the time, without compromising audit rigor? (Dynamic Testing)", publisher: PwC US, type: firm, url: "https://www.pwc.com/us/en/tech-effect/ai-analytics/dynamic-controls-testing.html", date: "2026", access: full, locator: "benefits list ('reducing effort by 30-40%')"}
  last_reviewed: "2026-10-20"
  notes: "Firm types: Riveron is a consulting firm owned by affiliates of Kohlberg & Company per the article's own boilerplate (PE-backed platform); RSM is a top-10 US firm serving the middle market; Protiviti is a global consulting firm (Robert Half subsidiary); PwC is Big Four. PwC page is undated (read via r.jina.ai mirror; direct curl returned 403); '2026' comes from the page's 2017-2026 footer, so treat it as a bound. RSM Beacon is announced, with no stated client count. Riveron is 'applying' the approach in client engagements per its own article, which is the basis for in-production. Grade B because no outcome figure is a measured result from a named organization."

- id: advisory-risk-controls-04
  title: "Risk-advisory teams test 100% of a control population with document extraction and Excel agents instead of a sample"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Procedures such as vendor bank-detail changes, invoice-to-contract tie-outs and deposit reconciliations are tested on a 1-of-25 sample. Manual review misses a digit and tying hundreds of documents eats hours."
  solution: "Armanino's risk-advisory team (Data Automation and Transformation staff) used DataSnipper's DocuMine, Document Matching and Excel Agents on live client engagements. The tool extracts names, account numbers and contract terms, matches them to supporting documents and reconciles deposits; the auditor reviews each suggested match."
  outcomes:
    - lever: quality
      description: "A manager said manual review would miss a digit across dozens of account numbers and the tool let the team test 100% of the changes."
      figure: "100% of vendor bank/payment-detail changes tested (vs a 1-of-25 sample)"
      measures: "Share of the population of vendor bank and payment-method changes tested, per the Armanino manager quoted; the engagement and period are not identified"
      provenance: vendor-published
      source_ref: DATASNIPPER-ARMANINO-2026
    - lever: capacity
      description: "A manager estimated about 25-plus hours saved on one deposit reconciliation."
      figure: "about 25+ hours (one reconciliation; estimate)"
      measures: "Hours saved on bank-deposit-to-report reconciliation, an estimate by the manager quoted ('I estimate')"
      provenance: vendor-published
      source_ref: DATASNIPPER-ARMANINO-2026
  prerequisites:
    - "Source documents available in files the tool can read"
    - "A procedure with clear match rules"
  risks_and_guardrails:
    - "The article is on the vendor's site, with Armanino quoted by the vendor; the 25-hour figure is an estimate, so this is grade B and not A under the 2026-10-17 rule"
    - "Full-population coverage does not remove the need for the reviewer to check each flagged mismatch"
  human_checkpoints:
    - "Auditor reviews each suggested deposit combination before it stands; the agent shows source for every answer and the auditor keeps judgment and sign-off"
  role_evolution: "The article says staff move from flipping through PDFs to the items that do not match. Armanino's quoted staff hold titles in a Data Automation and Transformation group inside risk advisory."
  evidence_grade: B
  sources:
    - {ref: DATASNIPPER-ARMANINO-2026, title: "AI and Auditing: 3 SOX Tests", publisher: DataSnipper, type: vendor, url: "https://www.datasnipper.com/resources/three-use-cases-for-ai-in-internal-audit", date: "2026-08-12", access: full, locator: "three use-case sections; quotes from Claire Koch and Amanda Finley"}
  last_reviewed: "2026-10-20"
  notes: "Firm type: Armanino is a mid-market accounting and advisory firm (top-25 per its published rankings; not confirmed in this run). Independence: not stated in the article; internal-audit-style work for attest clients would be subject to the firm's independence rules."

- id: advisory-risk-controls-05
  title: "Year-round control testing replaces a single point-in-time test (in-house SOX teams)"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Testing is bundled into one point in time, so issues surface late and fixes are rushed near year end."
  solution: "With agent-run tests, the team schedules testing throughout the year. Klaviyo's head of internal audit and compliance says this lets the team catch issues earlier and work with control owners to fix them sooner. Reddit's team extended agentic testing to other recurring testing programs."
  outcomes:
    - lever: speed
      description: "Klaviyo describes testing throughout the year instead of at a single point in time. It gives no metric."
      figure: "none published"
      measures: "Quote about testing cadence only"
      provenance: vendor-published
      source_ref: OPTRO-AGENTS-2026
  prerequisites:
    - "Control evidence available through the year, not only at period end (KPMG: continuous testing needs continuous evidence collection)"
    - "Control owners willing to respond to issues sooner"
  risks_and_guardrails:
    - "KPMG notes the line between first-line monitoring and third-line testing must stay clear so internal audit independence is preserved (KPMG-SOX2030-2026)"
  human_checkpoints:
    - "Control-owner follow-up and auditor review of exceptions"
  role_evolution: "KPMG says SOX practitioners will increasingly advise on control redesign and AI governance, not only report whether a control worked."
  evidence_grade: B
  sources:
    - {ref: OPTRO-AGENTS-2026, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: "2026-10-14", access: full, locator: "Klaviyo quote (Carmen Lam)"}
    - {ref: KPMG-SOX2030-2026, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: "2026-09-24", access: full, locator: "POV 3, sections 'Continuous, real-time assurance' and 'Automating evidence collection'"}
  last_reviewed: "2026-10-20"
  notes: "The named deployment is a single quote in a vendor press release. Kept separate from entry 01 because the change is to the cadence of the whole testing process, not to the first pass of one test."

- id: advisory-risk-controls-06
  title: "A company replaces outsourced third-party testers with agents, starting with IT SOX controls (Havertys)"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: model
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Havertys paid outside testers to run IT SOX tests. Tester turnover (internal or at the third party) is a risk, and the spend buys testing hours rather than advisory work."
  solution: "Havertys is adding Optro Autonomous Testing on top of its four-year-old Optro SOX system of record. It starts with the IT controls it already outsources, and plans to move to business-process controls and operational audits once IT controls are tested autonomously."
  outcomes:
    - lever: cost
      description: "Havertys will measure success partly by how its controls spend shifts, with more of the external support it buys expected to go to higher-value advisory work. No result is reported yet."
      figure: "none published"
      measures: "Plan only; no figure given"
      provenance: vendor-published
      source_ref: OPTRO-HAVERTYS-2026
  prerequisites:
    - "Several years of structured test results and documentation already in the platform"
    - "Evidence that a third-party tester could be taught the work, and so could an agent (Havertys' reasoning)"
  risks_and_guardrails:
    - "Case study is published by the vendor; no outcome yet"
  human_checkpoints:
    - "Managers continue to review and approve the work; IT Audit Manager says the team is still responsible for reviewing"
  role_evolution: "The VP of Internal Audit expects auditors to spend less time on controls expected to pass and more on process design and root cause. The company expects its spend on external support to move toward advisory work."
  evidence_grade: B
  sources:
    - {ref: OPTRO-HAVERTYS-2026, title: "Havertys Brings Agentic AI Into Internal Audit", publisher: Optro, type: vendor, url: "https://optro.ai/blog/havertys-furniture-success-story", date: "2026-09-04", access: full, locator: "paragraphs on third-party testers, 'We started with IT because we were already outsourcing those tests', and success measures"}
  last_reviewed: "2026-10-20"
  notes: "Direct signal for co-sourcing providers: the displaced work is the outsourced testing hours. Maturity is piloting because the page describes the IT-first rollout as the 'first goal', with no result."

- id: advisory-risk-controls-07
  title: "AI pre-review of workpapers before manager review (calibrated reviews)"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Manager review of audit workpapers is slow and inconsistent."
  solution: "FJ Management's head of internal audit says Optro lets the team analyse workpapers automatically, run calibrated reviews and log evidence inside live audit workflows, with an auditable human-in-the-loop standard."
  outcomes:
    - lever: capacity
      description: "The quote says it has changed what the team can get through. No figure given."
      figure: "none published"
      measures: "Quote only"
      provenance: vendor-published
      source_ref: OPTRO-AGENTS-2026
  prerequisites:
    - "Structured audit platform with workpapers held as data"
  risks_and_guardrails:
    - "One quote in a vendor release; the 'calibrated' method is not described"
  human_checkpoints:
    - "Human-in-the-loop standard retained, per the quote"
  role_evolution: "Not described beyond the quote."
  evidence_grade: B
  sources:
    - {ref: OPTRO-AGENTS-2026, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: "2026-10-14", access: full, locator: "Matt Sewell (FJ Management) quote"}
  last_reviewed: "2026-10-20"
  notes: "Thin: one named customer, one quote. It is kept because workpaper pre-review is a distinct change and no firm-side equivalent was found. Treat it as a lead."

- id: advisory-risk-controls-08
  title: "Evidence-request (PBC) generation, intake validation and follow-up handled by AI"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [coordination-scheduling, review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Auditors chase control owners by email and spreadsheet. Wrong or incomplete evidence is found weeks later, and the follow-up trail goes cold."
  solution: "Platform agents generate and route evidence requests, read each submission as it arrives, flag wrong-period or incomplete files, and track follow-ups. Diligent AuditAI (launched March 2026) and Optro Agentic Stakeholder Management (announced 2026-10-14) do this; Fieldguide describes the same pattern."
  outcomes:
    - lever: speed
      description: "Diligent says early adopters reduced time on audit administration by about 70%, from roughly 120 hours of manual coordination to 35. Customers are not named."
      figure: "about 70% less audit administration time; roughly 120 hours to 35"
      measures: "Time spent on audit administration / manual coordination per audit cycle among unnamed 'early adopters', per Diligent"
      provenance: vendor-published
      source_ref: DILIGENT-AUDITAI-2026
  prerequisites:
    - "Requests mapped to controls on one platform"
  risks_and_guardrails:
    - "No named customer and no method for the 70% figure"
    - "A vendor-CEO article reports about one in five PBC requests coming back wrong the first time; it does not cite a source for the figure (CPAPA-5Q-2026)"
  human_checkpoints:
    - "Diligent says auditors stay in control of key decisions through structured workflows and approvals"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - {ref: DILIGENT-AUDITAI-2026, title: "Diligent launches AuditAI to streamline internal audits", publisher: CFOtech, type: press, url: "https://cfotech.news/story/diligent-launches-auditai-to-streamline-internal-audits", date: "2026-03-13", access: full, locator: "paragraphs 3-5"}
    - {ref: OPTRO-AGENTS-2026, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: "2026-10-14", access: full, locator: "Agentic Stakeholder Management paragraph"}
    - {ref: FIELDGUIDE-SIXWAYS-2026, title: "Six Ways Internal Audit Teams Are Putting AI to Work", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/six-ways-internal-audit-teams-are-putting-ai-to-work", date: "2026", access: full, locator: "section on real-time evidence review"}
  last_reviewed: "2026-10-20"
  notes: "Firm type: vendors (Diligent, Optro, Fieldguide). Diligent date is the CFOtech article date; the vendor said the launch coincided with the IIA GAM conference (March 9-11). The CFOtech URL used here is the cfotech.news copy of the article."

- id: advisory-risk-controls-09
  title: "Agents draft internal-audit planning, risk assessment agendas and risk scores"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Annual risk assessment and engagement planning start from a blank page and a mass of external and internal information."
  solution: "Grant Thornton published 16 sample agent instructions for internal audit, including a risk-assessment agenda agent that pulls external information and builds a role-tailored agenda and a planning-memo agent, with missing inputs listed as open items. Optro announced agentic risk-assessment scoring that recommends starting scores with supporting evidence."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Not applicable; no result reported by either source"
      provenance: vendor-published
      source_ref: GT-16AGENTS-2026
  prerequisites:
    - "Prior-year files, scope and methodology as agent inputs; governance for agent development, testing and data access"
  risks_and_guardrails:
    - "Fieldguide notes a drafted risk assessment is a starting point and needs a person who knows the entity's real risks"
    - "GT says the agents need appropriate governance for development, testing, training, security and data access"
  human_checkpoints:
    - "Auditor refines and finalises the audit-ready first draft with professional judgment"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - {ref: GT-16AGENTS-2026, title: "16 sample AI agents for Internal Audit", publisher: Grant Thornton Advisors, type: firm, url: "https://www.grantthornton.com/insights/articles/advisory/2026/16-sample-ai-agents-for-internal-audit", date: "2026-08-06", access: full, locator: "intro; first two agent tables (risk assessment agenda; planning memorandum)"}
    - {ref: OPTRO-AGENTS-2026, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: "2026-10-14", access: full, locator: "Agentic Risk Assessment Scoring paragraph"}
    - {ref: FIELDGUIDE-SIXWAYS-2026, title: "Six Ways Internal Audit Teams Are Putting AI to Work", publisher: Fieldguide, type: vendor, url: "https://www.fieldguide.io/resource-articles/six-ways-internal-audit-teams-are-putting-ai-to-work", date: "2026", access: full, locator: "section on planning and drafting"}
  last_reviewed: "2026-10-20"
  notes: "Firm type: Grant Thornton (large US firm; see entry 10) and vendors Optro and Fieldguide. GT's piece is guidance with sample prompts, not a report of a deployment; no client or result is named. Fieldguide's article describes drafting as the most mature, lowest-risk use. It quotes the IIA's 2025 Pulse of Internal Audit (41% of CAEs use generative AI for internal audit activities; 25% for advisory; 15% for assurance); that figure is second-hand and the IIA source was not opened, so it sits here in notes only. BDO's Risk Assessment Coach is an audit-side (assurance) tool and is routed."

- id: advisory-risk-controls-10
  title: "Generative AI drafts risk and control matrices, control definitions, narratives and test steps (Grant Thornton CompliAI)"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Designing controls, rationalising them, writing narratives and preparing test steps for a client takes days or weeks of drafting."
  solution: "Grant Thornton's CompliAI combines its controls library with generative AI to do control gap assessment, rationalisation, narrative preparation, control definition and enhancement, test-step preparation and identification of required evidence. The firm announced in February 2024 that it had deployed it for its internal audit, compliance and risk professionals."
  outcomes:
    - lever: speed
      description: "The firm says control design and assessment tasks run in minutes where they would traditionally take days or weeks."
      figure: "minutes versus days or weeks (qualitative)"
      measures: "Elapsed time for control design and assessment tasks, as described qualitatively by the firm; no count"
      provenance: self-reported
      source_ref: GT-COMPLIAI-2024
  prerequisites:
    - "A curated controls library to ground the model (the firm's global controls library)"
  risks_and_guardrails:
    - "Press release; no quality measure"
  human_checkpoints:
    - "Firm professionals use the tool; review steps are not described in the release"
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - {ref: GT-COMPLIAI-2024, title: "Grant Thornton taps Microsoft technology to help clients manage compliance and risk using generative AI", publisher: Grant Thornton LLP, type: firm, url: "https://www.grantthornton.com/insights/press-releases/2024/february/grant-thornton-taps-microsoft-technology-to-help-clients-manage-compliance-and-risk-using-generative-ai", date: "2024-02-06", access: full, locator: "paragraphs 1-4; capabilities list"}
  last_reviewed: "2026-10-20"
  notes: "Older than the 12-18 month window; kept as the foundation for control-design drafting. Firm type: Grant Thornton is a large US firm; Grant Thornton Advisors (non-attest) sits in an alternative practice structure with New Mountain Capital as owner per the landscape (GT-GTAP-2026, not re-read here); the APS statement is in the GT-EAS-2026 boilerplate. Current use of CompliAI was not confirmed in 2026 sources."

- id: advisory-risk-controls-11
  title: "Agents review third-party SOC reports and vendor due diligence"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Teams read vendors' SOC reports and run onboarding due diligence by hand: extracting control descriptions, testing results and exceptions."
  solution: "KPMG lists integrated third-party risk and SOC report review as an agent type in its SOX framework, with agents extracting control descriptions and testing results. Optro announced an Agentic TPRM workflow in which agents perform onboarding and due diligence tasks while teams set policy and judge outcomes."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "Not applicable"
      provenance: vendor-published
      source_ref: OPTRO-AGENTS-2026
  prerequisites:
    - "Vendor documents in readable formats"
  risks_and_guardrails:
    - "CPAPA op-ed says SOC reports may say little about AI components, so user entities need contract terms and complementary controls (CPAPA-AGENTSCLOSE-2026). It also says the AICPA has not published AI-specific SOC guidance; the Journal of Accountancy later lists AICPA guidance on service organisations' AI use in SOC 1 and SOC 2 as issued earlier in 2026 (AICPA-AUDITAID-2026). The two sources disagree."
  human_checkpoints:
    - "Teams configure policy and evaluate outcomes (Optro); human review not detailed by KPMG"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - {ref: KPMG-AGENTICSOX-2025, title: "Seize the future: The agentic shift in SOX compliance", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/articles/2025/seize-the-future-the-agentic-shift-in-sox-compliance.html", date: "2025-07", access: full, locator: "list of agent use cases ('Integrated third-party risk and SOC report review')"}
    - {ref: OPTRO-AGENTS-2026, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: "2026-10-14", access: full, locator: "Agentic TPRM paragraph"}
  last_reviewed: "2026-10-20"
  notes: "KPMG page date: page metadata shows 2025-07-31 and a May 2026 value; '2025-07' is used with that uncertainty. Firm type: KPMG (Big Four) and vendor Optro. Reading others' SOC reports is user-entity work and stays here; issuing SOC reports is assurance."

- id: advisory-risk-controls-12
  title: "Audit of a client's agentic AI systems: AI governance lifecycle audit and extension of the SOX perimeter to AI"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Traditional AI governance assumes risk is handled before deployment through policies and approvals. Agents make decisions at run time, so an internal-audit team needs a repeatable way to test them without duplicating model-risk and compliance work."
  solution: "Grant Thornton, as AI governance lifecycle audit advisor, helped a large global financial-services client's internal audit team build a repeatable approach to evaluating AI systems: developing questions and validating controls for net-new risks, aligned to the NIST AI Risk Management Framework. The client completed its first AI lifecycle audit. KPMG's point of view says ICFR programs will need to extend to AI systems that generate or validate financial data."
  outcomes:
    - lever: risk
      description: "Grant Thornton reports seven AI governance domains under active audit coverage and over 100 production AI use cases with governance oversight validated, within a framework covering over 1,000 AI initiatives."
      figure: "7 domains; 100+ production use cases validated; 1,000+ AI initiatives governed"
      measures: "Counts of governance domains, production use cases validated and AI initiatives within the client's framework, as listed in the firm's case-study panel; whether they came from this engagement alone is not stated"
      provenance: self-reported
      source_ref: GT-BANK-2026
  prerequisites:
    - "An AI inventory and an existing model-risk or governance function to audit against (the client had both)"
    - "A reference framework (NIST AI RMF here; COSO's GenAI guidance extends the 2013 internal control framework)"
  risks_and_guardrails:
    - "Client is anonymous and very large; it is not a mid-market engagement"
    - "KPMG expects the first wave of AI-related material weaknesses in 2027 and notes SOX programs mostly still test around AI controls today (KPMG-SOX2030-2026)"
  human_checkpoints:
    - "The work is human audit design; AI is the subject of the audit, not the auditor"
  role_evolution: "KPMG says SOX and ICFR professionals will need to be fluent in accounting and AI systems, and that skills to audit a language model are not core to the CPA curriculum."
  evidence_grade: B
  sources:
    - {ref: GT-BANK-2026, title: "Bank strengthens oversight of 1,000+ AI initiatives without slowing innovation", publisher: Grant Thornton, type: firm, url: "https://www.grantthornton.com/insights/case-studies/banking/2026/global-bank-strengthens-oversight-of-ai-initiatives", date: "2026", access: full, locator: "headline panel; 'Our role' and 'Our solution'; challenge and result paragraphs"}
    - {ref: KPMG-SOX2030-2026, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: "2026-09-24", access: full, locator: "POV 1: The governance of AI, subsection 'The first AI-related material weaknesses'"}
    - {ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02-23", access: full, locator: "Implementation roadmap section (six steps); eight capability types"}
  last_reviewed: "2026-10-20"
  notes: "GT case study has no date on the page; '2026' comes from the URL path. The COSO publication is the PDF copy hosted by a Spanish internal-auditors site; the release date of 2026-02-23 is from Deloitte's DART summary (DART-COSO-2026). COSO authors per the PDF: Emett, Pikoos, Eulerich, Wood and Guthrie (EY). Firm type: Grant Thornton (large US firm, PE-owned advisory arm per the landscape) for the client case; KPMG (Big Four) for the SOX point of view. The client is a large bank, not mid-market. This is risk-advisory work on the client's AI; certification against AIUC-1 or ISO 42001 is assurance and is routed."

- id: advisory-risk-controls-13
  title: "AI governance framework and readiness advisory for clients (inventory, risk tiering, control mapping, monitoring)"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [expert-judgment, document-production]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Clients deploy AI faster than they document ownership, controls and evidence. Policies and review committees exist but do not show how a specific system was tested or how it behaves in use."
  solution: "Firms sell design of governance operating models: accountability across business, risk and internal audit; risk-based review before go-live; monitoring and decision logging after. COSO's GenAI guidance gives a six-step cycle (govern, inventory, assess, design, implement, monitor). RSM is hiring for AI/ML risk assessments and model governance documentation. Grant Thornton markets an AI governance model built on clear accountability and evidence."
  outcomes:
    - lever: risk
      description: "none published. Demand signals only: 78% of 950 surveyed leaders lack strong confidence they could pass an independent AI governance audit in 90 days."
      figure: "none published (demand figure: 78%)"
      measures: "78% = survey respondents lacking strong confidence they could pass an independent AI governance audit in 90 days, of 950 C-suite and senior business leaders (Grant Thornton's own survey); not an outcome of any engagement"
      provenance: self-reported
      source_ref: GT-AIIMPACT-2026
  prerequisites:
    - "A client AI inventory (COSO step 2) and named owners"
    - "Delivery staff with AI/ML and cloud-control skills (RSM posting asks for Python, GenAI stack and risk-framework experience)"
  risks_and_guardrails:
    - "Evidence is firm positioning and a job posting; no named client engagement or result was found for mid-market clients"
    - "Independence: AI governance advisory sold to a firm's audit client raises the same independence questions as other management-support services; the rules were not checked in this run"
  human_checkpoints:
    - "All work is human-led advisory"
  role_evolution: "RSM's posting lists work with engineering, data science, cybersecurity, model risk and audit teams across the first and second lines, and prefers certifications such as AAIA, AAISM and AIGP."
  evidence_grade: C
  sources:
    - {ref: RSM-JOB-AIRISK-2026, title: "Senior Associate, Technology Risk Advisory - AI Risk", publisher: RSM US, type: job-posting, url: "https://jobs.rsmus.com/posting/senior-associate-technology-risk-advisory---ai-risk/JR119804/", date: "2026-10-01", access: full, locator: "responsibilities list; qualifications"}
    - {ref: GT-AIGOV-2026, title: "AI governance that holds up under scrutiny", publisher: Grant Thornton, type: firm, url: "https://www.grantthornton.com/insights/articles/advisory/2026/ai-governance-that-holds-up-under-scrutiny", date: "2026-04-20", access: full, locator: "sections on traditional governance and accountability model"}
    - {ref: GT-AIIMPACT-2026, title: "2026 AI Impact Survey Report", publisher: Grant Thornton, type: survey, url: "https://www.grantthornton.com/services/advisory-services/artificial-intelligence/2026-ai-impact-survey", date: "2026-03-18", access: full, locator: "statistics panel; source note 'n = 950'"}
    - {ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02-23", access: full, locator: "Implementation roadmap section"}
    - {ref: DART-COSO-2026, title: "Heads Up: COSO Releases Publication on Internal Controls Related to Generative AI", publisher: Deloitte (DART), type: firm, url: "https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai", date: "2026-04-03", access: full, locator: "opening paragraph (release date February 23, 2026); roadmap"}
  last_reviewed: "2026-10-20"
  notes: "Firm types: RSM (top-10 US firm serving the middle market) and Grant Thornton. Grade C because the evidence is firm marketing, a standard and one job posting; a posting shows hiring, not delivered engagements. Bloomberg Law reports (2026-09-30) that the Big Four are pitching governance services to clients (BLOOMBERG-BIGFOUR-2026, opened via mirror). EY's survey about materially negative AI incidents is cited there second-hand. The landscape's note that GT's CEO expects AI governance demand (GT-CBIZ-2026) was not re-read in this run. Boundary: certification or attestation over AI systems (AIUC-1, ISO 42001, SOC) is assurance, see section 4."

- id: advisory-risk-controls-14
  title: "AI inventory and shadow-AI discovery to feed a client's AI risk register"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Shadow AI starts outside formal IT oversight, and teams cannot govern what they have not listed. COSO's guidance makes inventory the first step of its roadmap."
  solution: "Optro announced Agentic AI Governance: intake that pre-populates AI system records from existing documentation and an evidence evaluator that flags which controls are already satisfied. A separate AI Discovery capability to surface shadow AI is described as previewing ahead of 2027 availability."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Not applicable"
      provenance: vendor-published
      source_ref: OPTRO-AGENTS-2026
  prerequisites:
    - "Existing documentation of AI systems; a governance platform"
  risks_and_guardrails:
    - "Announced product only; no named customer"
  human_checkpoints:
    - "Teams own the attestations and judgments (Optro)"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - {ref: OPTRO-AGENTS-2026, title: "Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance", publisher: Optro, type: vendor, url: "https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance", date: "2026-10-14", access: full, locator: "Agentic AI Governance paragraph"}
    - {ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02-23", access: full, locator: "Implementation roadmap, Step 1 (inventory) and shadow-AI discussion"}
  last_reviewed: "2026-10-20"
  notes: "Firm type: vendor (Optro). The tool is announced; AI Discovery is only a preview."

- id: advisory-risk-controls-15
  title: "Board and audit-committee materials analysed for anomalies and turned into audit actions"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Board packs, audit actions and remediation tracking live in separate places, so signals in governance materials do not become audit follow-up."
  solution: "Diligent links AuditAI to Smart Prep 360, which reviews board and committee materials for accounting anomalies, control gaps, repeat findings and potential fraud indicators and produces questions for directors. AuditAI turns those signals into risk-aware evidence requests and tracks remediation to closure."
  outcomes:
    - lever: quality
      description: "none published"
      figure: "none published"
      measures: "Not applicable"
      provenance: vendor-published
      source_ref: DILIGENT-AUDITAI-2026
  prerequisites:
    - "Diligent Boards and the Diligent One platform in use"
  risks_and_guardrails:
    - "Announced; no named customer; the 70% figure for admin time is in entry 08"
  human_checkpoints:
    - "Auditors keep key decisions through structured workflows and approvals (vendor claim)"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - {ref: DILIGENT-AUDITAI-2026, title: "Diligent launches AuditAI to streamline internal audits", publisher: CFOtech, type: press, url: "https://cfotech.news/story/diligent-launches-auditai-to-streamline-internal-audits", date: "2026-03-13", access: full, locator: "paragraphs on Smart Prep 360"}
  last_reviewed: "2026-10-20"
  notes: "Single vendor source. Firm type: vendor (Diligent)."

- id: advisory-risk-controls-16
  title: "Risk-advisory practices move IA, ISO, HITRUST and PCI engagements onto one AI-native platform with firm-built agents"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Risk-advisory engagements run on email, spreadsheets and bespoke tools, with client requests chased by hand and methodology applied inconsistently."
  solution: "Aprio standardised SOC, ISO, HITRUST and PCI work on Fieldguide in its Risk Advisory Services practice from December 2025, then extended into financial audit in May 2026 and announced agent co-development on 2026-08-05. Cherry Bekaert announced on 2026-06-03 that it would consolidate planning, testing, review and reporting for Financial Audit, Internal Audit and SOC onto the same vendor's platform, after an existing deployment in its Risk and Cybersecurity practice. Only the internal-audit, ISO, HITRUST and PCI advisory portion belongs here."
  outcomes:
    - lever: capacity
      description: "none published for the advisory work. Fieldguide's Series C release says its platform is used by half of the top 100 US accounting firms (a company claim)."
      figure: "none published"
      measures: "Not applicable. The 'half of the top 100' figure is the vendor's claim and was not checked."
      provenance: vendor-published
      source_ref: FIELDGUIDE-SERIESC-2026
  prerequisites:
    - "Firm methodology configured into the platform (Aprio: Aprio's own methodology shapes how each agent is designed)"
    - "Open APIs to connect the platform to the firm's wider infrastructure (Cherry Bekaert release)"
  risks_and_guardrails:
    - "Vendor concentration: all named firms use one vendor; the vendor's own CEO quotes drive the announcements"
    - "Aprio says workflows are built to comply with AICPA, PCAOB and GAAS; human oversight at every stage (firm statement, not tested)"
  human_checkpoints:
    - "Cherry Bekaert: Field Agents with full human oversight; Aprio: human oversight at every stage"
  role_evolution: "Aprio says professionals spend more time interpreting results and advising. Cherry Bekaert's release describes more collaboration across audit and advisory teams. Fieldguide's CEO links the shift to a shrinking CPA pipeline (vendor statement)."
  evidence_grade: B
  sources:
    - {ref: APRIO-FIELDGUIDE-2026, title: "Aprio and Fieldguide Co-Build the Future of Audit with Agentic AI", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/?p=188025", date: "2026-08-05", access: full, locator: "final paragraph (timeline: March 2023 PCI pilot; December 2025 Risk Advisory expansion; May 2026 financial audit)"}
    - {ref: CB-FIELDGUIDE-2026, title: "Cherry Bekaert Selects Fieldguide as Strategic AI Partner to Modernize Audit and Advisory Delivery", publisher: Cherry Bekaert, type: firm, url: "https://www.cbh.com/newsroom/cherry-bekaert-expands-ai-audit-with-fieldguide/", date: "2026-06-03", access: full, locator: "paragraphs 1-2"}
    - {ref: FIELDGUIDE-SERIESC-2026, title: "Fieldguide Raises $75M Series C Round to Boost Audit and Advisory Firms' Agentic AI Capabilities", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/02/02/fieldguide-raises-75m-series-c-round-to-boost-audit-and-advisory-firms-agentic-ai-capabilities/177323", date: "2026-02-03", access: full, locator: "paragraph on 'half of the top 100 accounting firms'"}
  last_reviewed: "2026-10-20"
  notes: "Firm types: Cherry Bekaert (top-20 firm per its release) and Aprio (20th-largest US advisory and accounting firm per its release) are mid-market firms. Fieldguide's Series C item is dated by the CPA Practice Advisor byline (2026-02-03); the vendor announced on Feb 2. SOC and financial-audit parts are assurance and are routed. Fieldguide's customer case-study pages (Weaver, Warren Averett, BerryDunn, Forvis Mazars, Aprio PCI) were opened but carry no publication date and mostly describe pre-agent workflow platforms; they are not used as evidence here."

- id: advisory-risk-controls-17
  title: "AI-native providers sell SOX and internal-audit testing straight to enterprise audit teams"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Public companies spend heavily on SOX testing (Midship cites roughly $2.3 million a year on SOX audit services for the average US public company, a vendor figure) and testing stays manual."
  solution: "Vendors sell agents that follow an audit plan, gather evidence, test controls and produce review-ready workpapers with an approval workflow. Petual (a16z-backed, $20M raise reported 2026-04-24) names Navan as a customer. Midship raised a $4.15M seed (2026-01-27). Andera (whose technology RSM Beacon uses) markets a 70% time saving."
  outcomes:
    - lever: capacity
      description: "Petual reports customers achieve efficiency gains of between 68% and 80% on existing SOX workflows, and that work papers take minutes rather than double or triple-digit hours. Navan's head of audit, risk and compliance says it lets the company keep quality while scaling."
      figure: "68%-80% efficiency gain on SOX workflows (vendor claim)"
      measures: "Efficiency gain on existing SOX workflows across Petual customers, as reported by Petual; the metric, sample and period are not given"
      provenance: vendor-published
      source_ref: FINTECHGLOBAL-PETUAL-2026
  prerequisites:
    - "Enterprise-scale evidence in readable formats; external-auditor acceptance of the workpaper format"
  risks_and_guardrails:
    - "All figures are vendor claims at funding announcements"
    - "CPAPA-5Q-2026 warns that every major firm is building its own AI testing tools and external auditors will scrutinise how a client applies them"
  human_checkpoints:
    - "Built-in approval workflow keeps human oversight central (Petual); agents keep humans in the loop (Midship)"
  role_evolution: "Midship's release frames the shift as moving audit teams from evidence collection and documentation toward advisory work."
  evidence_grade: B
  sources:
    - {ref: FINTECHGLOBAL-PETUAL-2026, title: "Petual raises $20m for AI-powered SOX compliance", publisher: Fintech Global, type: press, url: "https://fintech.global/2026/04/24/petual-raises-20m-for-ai-powered-sox-compliance/", date: "2026-04-24", access: full, locator: "paragraphs 3-6 (efficiency figure; Navan quote)"}
    - {ref: MIDSHIP-SEED-2026, title: "Midship Raises $4.15M to Automate SOX Testing with Agentic AI", publisher: Venture Capital Access Online, type: press, url: "https://www.vcaonline.com/news/2026012714/midship-raises-4-15m-to-automate-sox-testing-with-agentic-ai/", date: "2026-01-27", access: full, locator: "paragraphs 1-4"}
  last_reviewed: "2026-10-20"
  notes: "Firm type: AI-native vendors, not accounting firms; they are the competitive context for co-sourcing. Grade B rests on a named production customer (Navan) with a quote; the figure is vendor-published. Andera's homepage (opened) carries the 70% claim and a $37M raise banner; the raise date came only from a search result (June 2026) so it is not used as evidence."

- id: advisory-risk-controls-18
  title: "Embedded, self-healing controls and first-line continuous monitoring (idea)"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [review-assurance, software-systems]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "Detective controls such as reconciliations and exception reports find issues after the fact. Control health is assessed once a year."
  solution: "IDEA (discussed by practitioners). KPMG's 2030 point of view describes preventive, embedded and increasingly self-healing controls that identify and sometimes correct configuration problems, with first-line owners using continuous monitoring and internal audit testing the monitoring. Havertys' VP of Internal Audit expects controls could one day be tested at each occurrence as documentation is approved (OPTRO-HAVERTYS-2026)."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Not applicable; forward-looking statements only"
      provenance: self-reported
      source_ref: KPMG-SOX2030-2026
  prerequisites:
    - "Automated evidence collection and standard repositories"
    - "Clear split between first-line monitoring and third-line testing"
  risks_and_guardrails:
    - "KPMG lists black-box audit difficulty, rubber-stamp human review, model drift, bias and prompt injection (including hidden instructions in evidence aimed at testing agents) as open challenges"
  human_checkpoints:
    - "Not specified"
  role_evolution: "KPMG: the SOX practitioner moves from reporting whether a control worked to advising on how to redesign it."
  evidence_grade: D
  sources:
    - {ref: KPMG-SOX2030-2026, title: "The Future of SOX: A point of view for 2030 and beyond", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html", date: "2026-09-24", access: full, locator: "POV 2: Embedded and autonomous controls; 'Challenges on the horizon'"}
    - {ref: OPTRO-HAVERTYS-2026, title: "Havertys Brings Agentic AI Into Internal Audit", publisher: Optro, type: vendor, url: "https://optro.ai/blog/havertys-furniture-success-story", date: "2026-09-04", access: full, locator: "paragraph beginning 'Beyond that plan, Stephanouk sees a bigger future'"}
  last_reviewed: "2026-10-20"
  notes: "Idea. No deployment found. Firm type: KPMG (Big Four). KPMG also says external auditors and practitioners already test 100% of certain transaction types; see entry 04."

- id: advisory-risk-controls-19
  title: "Pre-go-live control package for client finance agents: inventory and owner, evidence standard, sign-off gate, assurance mapping, exit threshold (idea)"
  archetype: advisory
  module: risk-controls
  function: service-delivery
  work_types: [expert-judgment, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Close agents (BlackLine, FloQast, Microsoft, Workday per the source) are reaching production while only some finance teams can show assurance readiness. Vendor match-rate claims are not reproduced on the client's data."
  solution: "IDEA (practitioner proposal). A one-page signed memo: agent inventory with a named human owner; an evidence standard (inputs, steps, exceptions, basis for each match); human approval gates scaled to materiality; mapping of subservice-organisation assurance (SOC) to complementary controls and contract terms; and monitoring with a threshold at which the agent is pulled."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "Not applicable; an article proposal"
      provenance: self-reported
      source_ref: CPAPA-AGENTSCLOSE-2026
  prerequisites:
    - "An approved list of agents; a close checklist where gates can be written"
  risks_and_guardrails:
    - "Author is a university professor, not a firm; no deployment cited"
    - "Cites vendor claims of 90% match rates and 90% preparation time savings as marketing figures until reproduced on client data"
  human_checkpoints:
    - "Controller signs the memo; approval gates in the close checklist"
  role_evolution: "CAS and controllership advisors hand clients the checklist; auditors will ask the same questions."
  evidence_grade: D
  sources:
    - {ref: CPAPA-AGENTSCLOSE-2026, title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: "2026-08-13", access: full, locator: "five numbered controls and closing paragraph"}
    - {ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02-23", access: full, locator: "Implementation roadmap"}
  last_reviewed: "2026-10-20"
  notes: "Idea. Source is a university professor's article in a trade outlet. The client-accounting side of agentic close belongs to client-accounting-services; the control design belongs here. The article's own '42 percent assurance ready' paraphrase matches the KPMG release (see Summary point 7)."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Annual risk assessment and audit planning** (research-synthesis, document-production): interviews, external risk scanning, planning memo, work program. AI is drafting here (entries 09, 15).
- **SOX scoping, RCM and control design** (document-production, expert-judgment): control rationalisation, narratives, control attributes (entry 10).
- **Walkthroughs** (review-assurance): scheduling, transcription, documentation. KPMG lists agent support for these, with no deployment found (entry 11 note; KPMG-AGENTICSOX-2025).
- **Evidence requests / PBC** (coordination-scheduling): request generation, intake checks, follow-up (entry 08).
- **Control testing** (review-assurance): evidence-to-sample matching, attribute tests, annotated workpapers, ITGC tests (entries 01-07, 17).
- **Workpaper review and issue evaluation** (review-assurance, expert-judgment): pre-review (entry 07); deficiency evaluation remains human.
- **Reporting to management and audit committee** (document-production): entry 15.
- **Third-party and SOC report review** (review-assurance): entry 11.
- **AI governance advisory and audit of client AI** (expert-judgment, review-assurance): entries 12-14, 19.

### Common pain points

- Evidence in mixed formats (spreadsheets, PDFs, logs, emails) with no standard naming (RIVERON-MONDAQ-2026; CPAPA-5Q-2026).
- Cost and hours rising. KPMG's 2025 SOX survey excerpts: cost of maintaining SOX controls up 45% between its 2023 and 2025 surveys; average testing hours per control up from 12 (FY2022) to 16 (FY2024) (KPMG-SOX2030-2026, 'Introduction' insert).
- Capacity: 52% of internal-audit departments in that survey spent more than 40% of total hours on SOX in FY2024 (same insert; KPMG's own survey).
- Distinguishing "missing support" from "true exception" (RIVERON-MONDAQ-2026; GT-INFERENCEGAP-2026).
- Spreadsheets and email for request tracking (DILIGENT-AUDITAI-2026; vendor language).

### Metrics and benchmarks (with sources)

| Metric | Value as reported | What it counts | Source | Provenance |
|---|---|---|---|---|
| Reddit SOX automation | 175 controls (more than 40% of SOX scope) in the first three months; 60% average cut in testing time per control; later over 75% of SOX controls | Controls automated; testing time per control | OPTRO-AGENTS-2026 | vendor-published |
| Microsoft change-management testing | 850 hours and $185K a year | Annual time and cost savings, method not stated | MSFT-SOXAGENT-2026 | self-reported |
| PwC Dynamic Testing | 30-40% effort reduction | Controls-testing effort, baseline not stated | PWC-DYNTEST-2026 | vendor-published |
| Diligent AuditAI early adopters | about 70% less audit admin time; about 120 hours to 35 | Audit administration time, unnamed adopters | DILIGENT-AUDITAI-2026 | vendor-published |
| Petual customers | 68%-80% efficiency gain on SOX workflows | Not defined | FINTECHGLOBAL-PETUAL-2026 | vendor-published |
| AI maturity of finance (first line) | 5% high progress; 26% moderate; 55% some pilots; 15% not started | Self-assessed maturity of respondents' finance and accounting function, from about 3,900 leaders on an April 2026 KPMG webcast | KPMG-ICFR-WEBCAST-2026 | firm poll (self-selected audience) |
| Obstacle to AI enablement | about 26% say lack of time and resources is the primary obstacle | Same poll | KPMG-ICFR-WEBCAST-2026 | firm poll |
| Use of outsourced SOX testers | 28% of companies polled used outsourced providers for SOX testing; 58% (denominator as stated in source: unclear, likely users of outsourced providers) said outsourced providers were more than 20% of SOX budget | KPMG 2025 SOX survey excerpt | KPMG-SOX2030-2026 | firm survey |
| Finance AI use and assurance readiness | Active AI use 30% (2024) to 75% (2026); 42% of organisations fully assurance-ready; 29% track where AI adoption fails | Survey of 1,013 senior finance leaders at organisations with revenue of at least $250M ($500M in US), March 2026 | KPMG-AIFINANCE-2026 | firm survey |
| Governance gap | 63% have no formal AI risk appetite or governance framework; 28% of IA respondents confident in their team's ability to audit AI risks | 2026 Focus on the Future survey of internal-audit leaders (sample size not captured in the opened blog post) | AUDITBOARD-FOCUS-2025 | vendor-sponsored survey |
| Agent failures | 34% experienced an inaccurate agent decision or output that was acted upon; 38% authorise agents to approve or reject transactions; 9% have redesigned workflows for agents; 46% say employees spend more time reviewing or correcting AI output | 417 GRC, audit, risk and security leaders, organisations of 250+ employees | OPTRO-AGENTICREPORT-2026 | vendor survey |
| AI governance confidence | 78% lack strong confidence they could pass an independent AI governance audit in 90 days | 950 C-suite and senior business leaders | GT-AIIMPACT-2026 | firm survey |
| IT-related material weaknesses | rose from 31% (2021) to 58% (2025) | KPMG 2025 Trends in Material Weaknesses study, as cited | KPMG-IPO-2026 | firm study |
| Agent integration plans | more than 68% expect to have integrated autonomous or semi-autonomous agents by 2026 | About 900 respondents; study dated 2025-09-30 | PROTIVITI-AIPULSE-2025 | firm survey |

**Quality evidence: absent.** No source gives an error rate, override rate, false-exception rate, parallel-run result, inspection finding or independent measurement for AI control testing. What exists: a recommendation to run a parallel pilot on 5-10 controls and compare exceptions (CPAPA-5Q-2026); a warning that vendor match-rate claims are unproven until reproduced on client data (CPAPA-AGENTSCLOSE-2026); and the "inference gap" description of false flags (GT-INFERENCEGAP-2026). Vendor-sponsored surveys (Optro, AuditBoard, Diligent) and KPMG's webcast poll draw self-selected audiences.

### Guardrails and regulatory points

- **COSO, February 2026:** extends the 2013 Internal Control framework to generative AI, with eight capability types, mapping to five components and 17 principles, and a six-step roadmap (govern, inventory, assess, design, implement, monitor) (COSO-GENAI-2026; DART-COSO-2026).
- **AICPA practice aid, 2026-10-13:** covers organisations' AI in financial reporting and firms' AI use in audits; non-authoritative; more guidance (risk of material misstatement, audit evidence) is planned. JofA also lists earlier-2026 AICPA guidance on service organisations' AI and SOC 1/SOC 2 (AICPA-AUDITAID-2026).
- **No PCAOB standard for AI in audits.** Zanin says staff observations of July 2024 never became guidance and that AS 1215 is the working bar (CPAPA-5Q-2026; opinion of a vendor CEO). The landscape lists the PCAOB spotlight (PCAOB-GENAI-2024).
- **KPMG expects PCAOB and SEC to develop disclosure thinking on AI in financial systems and controls** (KPMG-SOX2030-2026, 'Challenges on the horizon').
- **Independence.** Internal-audit outsourcing and other management-support services for audit clients are generally restricted; this note comes from the landscape, was not confirmed against rules in this run, and applies to entries 03, 04 and 13.
- **Data handling:** RSM states client data processed through Beacon stays in a segregated environment and is not used to train Andera's commercial product (RSM-BEACON-2026).
- **External-auditor reliance:** KPMG expects management testing to matter less where external auditors test 100% of populations with their own AI (KPMG-SOX2030-2026, POV 5).

### Frontier signals (dated, sourced)

- 2026-01-27: Midship raises $4.15M seed for agentic SOX testing (MIDSHIP-SEED-2026).
- 2026-02-23: COSO publishes GenAI internal-control guidance (COSO-GENAI-2026; date per DART-COSO-2026).
- 2026-03-03: Protiviti announces its Fieldguide alliance for IA and SOX (PROTIVITI-FIELDGUIDE-2026).
- 2026-03-13: Diligent launches AuditAI (DILIGENT-AUDITAI-2026).
- 2026-04-24: Petual raises $20M; names Navan (FINTECHGLOBAL-PETUAL-2026).
- 2026-06-03: Cherry Bekaert consolidates audit, IA and SOC on one agentic platform (CB-FIELDGUIDE-2026).
- 2026-08-05: Aprio announces co-development of audit agents (APRIO-FIELDGUIDE-2026).
- 2026-08-28: RSM announces Beacon with Andera and says it is evaluating SOC, NIST, PCI and operational audits (RSM-BEACON-2026).
- 2026-09-24: KPMG says it expects the first wave of AI-related material weaknesses in 2027 (KPMG-SOX2030-2026).
- 2026-10-14: Optro extends autonomous testing beyond SOX to operational audit testing; AI Discovery for shadow AI previewing ahead of 2027 availability (OPTRO-AGENTS-2026).
- Deloitte names agentic AI the "Mega Hot Topic" for 2026 internal audit, per a secondary summary; the summary's date is unclear (GRCREPORT-DELOITTE-2026).

### Workforce and role effects

- **Review stays human; execution moves.** Riveron and RSM keep reviewers on every conclusion; roles shift toward review, challenge and exception analysis (RIVERON-MONDAQ-2026; RSM-BEACON-2026).
- **Spend moves from testing hours to advisory.** Havertys expects its external support to shift toward higher-value advisory (OPTRO-HAVERTYS-2026).
- **New skills.** KPMG says auditing AI requires skills not core to the CPA curriculum and mentions data scientists specialising in audit and dual-credentialed staff (KPMG-SOX2030-2026, POV 5). RSM's AI-risk posting asks for a Python and GenAI stack background, plus AAIA, AAISM or AIGP-type certifications (RSM-JOB-AIRISK-2026).
- **Capability gap inside internal audit.** Only 28% of surveyed IA respondents are confident in their team's ability to audit AI risks (AUDITBOARD-FOCUS-2025).
- **Pipeline.** Fieldguide and Cherry Bekaert's release cite a CPA pipeline at a 17-year low (CB-FIELDGUIDE-2026; vendor statement).
- **Headcount.** The CPA Practice Advisor article cites the Internal Audit Foundation as finding 57% of IA functions hold headcount flat (CPAPA-5Q-2026; second-hand).

### Objections and concerns practitioners raise

- **Inference gap and false exceptions:** AI can flag what humans intuitively accept, exposing undocumented practice (GT-INFERENCEGAP-2026).
- **Single tools do not meet audit grade:** general LLMs in isolation do not (RIVERON-MONDAQ-2026).
- **Black box and rubber stamping:** a human approval that rubber-stamps every recommendation provides no control value (KPMG-SOX2030-2026).
- **Evidence tampering:** control owners may hide instructions in evidence to steer testing agents (KPMG-SOX2030-2026, 'Challenges on the horizon').
- **Silent degradation:** an agent that degrades quietly is more dangerous than one that fails loudly (CPAPA-AGENTSCLOSE-2026).
- **Time spent reviewing:** 46% report employees spending more time reviewing or correcting AI outputs (OPTRO-AGENTICREPORT-2026, vendor survey).

### Interview probes for an advisor

1. "Which control tests does your team run first-pass with an agent today, and what did you compare it against before trusting it? Show me a reviewer override or rework count if you track one."
2. "How do you tell a missing document from a failed control when an agent reports an exception, and who decides?"
3. "If a co-source provider is testing for you, what is their plan for agents, and do you expect your testing spend to fall, stay flat or move to advisory?"
4. "Which AI systems and agents in your finance and audit processes are on an inventory with a named owner, and has your external auditor asked about them?"
5. "How have you tested that your own AI testing tools hold up when the external auditor reviews the file?"

---

## 4. Routed to other modules

- **To assurance (archetype):**
  - Grant Thornton Enterprise Assurance Services, with AIUC-1 provisional accreditation and ISO certification (GT-EAS-2026, opened).
  - Aprio's ANAB accreditation to certify against ISO/IEC 42001, effective 2026-04-24, announced 2026-07-30 (APRIO-ISO42001-2026, opened).
  - The SOC and financial-audit portions of Cherry Bekaert's and Aprio's Fieldguide deployments.
  - BDO's AI Risk Assessment Coach for audit risk assessment, described as being evaluated, and Chat BDO (BDO-AI-2025, opened).
  - AICPA practice aid on AI for financial-statement auditors (AICPA-AUDITAID-2026).
  - KPMG's 'AI as the subject of the audit' framing where the work is an attest opinion.
- **To professional-services (firm operations):**
  - Aprio's $300M five-year AI and automation investment (APRIO-FIELDGUIDE-2026).
  - Realization and capacity effects at firms using engagement platforms; for example Fieldguide's Series C release claims, and case-study pages report, increases in realization, with no dates (not used here).
  - PE ownership context for Riveron (Kohlberg) and the APS split (GT-EAS-2026 boilerplate).
  - Pricing: the shift of outsourced testing spend (Havertys) to advisory, as a billing-model question.
- **To client-accounting-services:** how agentic close tools (BlackLine, FloQast, Microsoft, Workday) are governed for CAS clients (CPAPA-AGENTSCLOSE-2026); entry 19 is kept here only for the control design.
- **To forensic-disputes:** Diligent Smart Prep 360's flagging of fraud indicators in board materials (DILIGENT-AUDITAI-2026); no firm deployment was found.

---

## 5. Sources

Access is `full` unless stated. Type counts are at the end of the table.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| OPTRO-AGENTS-2026 | Optro Launches Domain-Trained Agents for Audit, Compliance, Third-Party Risk, and AI Governance | Optro | vendor | https://optro.ai/blog/optro-launches-domain-trained-agents-for-audit-compliance-third-party-risk-and-ai-governance | 2026-10-14 |
| OPTRO-HAVERTYS-2026 | Havertys Brings Agentic AI Into Internal Audit | Optro | vendor | https://optro.ai/blog/havertys-furniture-success-story | 2026-09-04 |
| OPTRO-AGENTICREPORT-2026 | One in Three Organizations Say They Have Acted on Wrong Decisions Made by AI Agents (Authority without oversight report) | Optro | survey | https://optro.ai/blog/one-in-three-organizations-say-they-have-acted-on-wrong-decisions-made-by-ai-agents-optro-research-finds | 2026-10-08 |
| AUDITBOARD-FOCUS-2025 | Top takeaways from 2026 Focus on the Future | AuditBoard (Optro) | survey | https://auditboard.com/blog/top-takeaways-from-2026-focus-on-the-future | 2025-11-12 |
| MSFT-SOXAGENT-2026 | Microsoft Frontier Finance Innovation Story: SOX Change Management Testing Agent | Microsoft | vendor | https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/mcaps/documents/fy26/SOX-Change-Management-Testing-Agent.pdf | 2026 (FY26 URL path; no day) |
| DILIGENT-AUDITAI-2026 | Diligent launches AuditAI to streamline internal audits | CFOtech | press | https://cfotech.news/story/diligent-launches-auditai-to-streamline-internal-audits | 2026-03-13 |
| DATASNIPPER-ARMANINO-2026 | AI and Auditing: 3 SOX Tests | DataSnipper | vendor | https://www.datasnipper.com/resources/three-use-cases-for-ai-in-internal-audit | 2026-08-12 |
| FINTECHGLOBAL-PETUAL-2026 | Petual raises $20m for AI-powered SOX compliance | Fintech Global | press | https://fintech.global/2026/04/24/petual-raises-20m-for-ai-powered-sox-compliance/ | 2026-04-24 |
| MIDSHIP-SEED-2026 | Midship Raises $4.15M to Automate SOX Testing with Agentic AI | Venture Capital Access Online | press | https://www.vcaonline.com/news/2026012714/midship-raises-4-15m-to-automate-sox-testing-with-agentic-ai/ | 2026-01-27 |
| FIELDGUIDE-SIXWAYS-2026 | Six Ways Internal Audit Teams Are Putting AI to Work | Fieldguide | vendor | https://www.fieldguide.io/resource-articles/six-ways-internal-audit-teams-are-putting-ai-to-work | 2026 (no day on page; listing title says 2026) |
| FIELDGUIDE-AIGOV-2026 | What AI governance means for audit and assurance firms | Fieldguide | vendor | https://www.fieldguide.io/resource-articles/ai-governance-audit-assurance-firms | 2026 (no day; refers to Dec 2025 SEC item) |
| FIELDGUIDE-SERIESC-2026 | Fieldguide Raises $75M Series C Round... | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/02/fieldguide-raises-75m-series-c-round-to-boost-audit-and-advisory-firms-agentic-ai-capabilities/177323 | 2026-02-03 |
| RIVERON-MONDAQ-2026 | AI In Internal Audit And SOX: Applying Methods That Work | Riveron (via Mondaq) | firm | https://www.mondaq.com/unitedstates/audit/1805956/ai-in-internal-audit-and-sox-applying-methods-that-work | 2026-06-24 |
| RSM-BEACON-2026 | RSM launches AI-guided internal audit platform "Beacon" with Andera | Accounting Today | press | https://www.accountingtoday.com/news/rsm-launches-ai-guided-internal-audit-platform-beacon-with-andera | 2026-08-28 |
| RSM-JOB-AIRISK-2026 | Senior Associate, Technology Risk Advisory - AI Risk | RSM US | job-posting | https://jobs.rsmus.com/posting/senior-associate-technology-risk-advisory---ai-risk/JR119804/ | 2026-10-01 |
| PROTIVITI-FIELDGUIDE-2026 | Protiviti Announces Strategic Alliance with Fieldguide... | Protiviti (PR Newswire via finviz) | firm | https://finviz.com/news/328216/protiviti-announces-strategic-alliance-with-fieldguide-to-accelerate-ai-enabled-internal-audit-sox-and-controls-transformation | 2026-03-03 |
| PROTIVITI-AIPULSE-2025 | More Than 68% of Organizations Expect to Have Integrated AI Agents By 2026 | Protiviti | survey | https://www.protiviti.com/us-en/press-release/ai-agents-adoption-by-2026-protiviti-study | 2025-09-30 |
| PWC-DYNTEST-2026 | Dynamic controls testing with AI (Dynamic Testing) | PwC US | firm | https://www.pwc.com/us/en/tech-effect/ai-analytics/dynamic-controls-testing.html (read via r.jina.ai mirror) | 2026 (undated page) |
| CB-FIELDGUIDE-2026 | Cherry Bekaert Selects Fieldguide as Strategic AI Partner | Cherry Bekaert | firm | https://www.cbh.com/newsroom/cherry-bekaert-expands-ai-audit-with-fieldguide/ | 2026-06-03 |
| APRIO-FIELDGUIDE-2026 | Aprio and Fieldguide Co-Build the Future of Audit with Agentic AI | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=188025 | 2026-08-05 |
| APRIO-ISO42001-2026 | Aprio Accredited to Certify Organizations On International AI Governance Standard | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/07/30/aprio-accredited-to-certify-organizations-on-international-ai-governance-standard/187654/ | 2026-07-30 |
| BDO-AI-2025 | BDO USA Unveils Comprehensive Artificial Intelligence Strategy | BDO USA | firm | https://www.bdo.com/insights/press-releases/bdo-usa-unveils-comprehensive-artificial-intelligence-strategy-fusing-practical-innovation | 2025-05-27 (per landscape; page date not re-extracted) |
| GT-EAS-2026 | Grant Thornton launches first-of-its-kind Enterprise Assurance Services practice | Grant Thornton LLP | firm | https://www.grantthornton.com/insights/press-releases/2026/september/gt-launches-first-of-its-kind-enterprise-assurance-services | 2026-09-23 (per landscape; URL path September 2026) |
| GT-BANK-2026 | Bank strengthens oversight of 1,000+ AI initiatives without slowing innovation | Grant Thornton | firm | https://www.grantthornton.com/insights/case-studies/banking/2026/global-bank-strengthens-oversight-of-ai-initiatives | 2026 (URL path; no day) |
| GT-INFERENCEGAP-2026 | The unexpected obstacle to AI-enabled SOX | Grant Thornton | firm | https://www.grantthornton.com/insights/articles/advisory/2026/the-unexpected-obstacle-to-ai-enabled-sox-and-internal-audit | 2026-08-12 |
| GT-16AGENTS-2026 | 16 sample AI agents for Internal Audit | Grant Thornton | firm | https://www.grantthornton.com/insights/articles/advisory/2026/16-sample-ai-agents-for-internal-audit | 2026-08-06 |
| GT-AIGOV-2026 | AI governance that holds up under scrutiny | Grant Thornton | firm | https://www.grantthornton.com/insights/articles/advisory/2026/ai-governance-that-holds-up-under-scrutiny | 2026-04-20 |
| GT-AIIMPACT-2026 | 2026 AI Impact Survey Report | Grant Thornton | survey | https://www.grantthornton.com/services/advisory-services/artificial-intelligence/2026-ai-impact-survey | 2026-03-18 |
| GT-COMPLIAI-2024 | Grant Thornton taps Microsoft technology... (CompliAI) | Grant Thornton LLP | firm | https://www.grantthornton.com/insights/press-releases/2024/february/grant-thornton-taps-microsoft-technology-to-help-clients-manage-compliance-and-risk-using-generative-ai | 2024-02-06 |
| KPMG-SOX2030-2026 | The Future of SOX: A point of view for 2030 and beyond (web page and PDF) | KPMG US | firm | https://kpmg.com/us/en/articles/2026/future-sox-point-view-2030-beyond.html | 2026-09-24 |
| KPMG-ICFR-WEBCAST-2026 | Revolutionizing internal controls (insights from an April 2026 Future of SOX webcast) | KPMG US | survey | https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2026/revolutionizing-internal-controls.pdf | 2026-04 (webcast month; PDF undated) |
| KPMG-AGENTICSOX-2025 | Seize the future: The agentic shift in SOX compliance | KPMG US | firm | https://kpmg.com/us/en/articles/2025/seize-the-future-the-agentic-shift-in-sox-compliance.html | 2025-07 |
| KPMG-IPO-2026 | The IT leader's guide to IPO preparedness | KPMG US | firm | https://kpmg.com/us/en/articles/2026/it-leaders-guide-ipo-preparedness.html | 2026-06-10 |
| KPMG-AIFINANCE-2026 | AI adoption in finance doubles, but assurance readiness determines who wins | KPMG International | survey | https://kpmg.com/xx/en/media/press-releases/2026/05/ai-adoption-in-finance-doubles-but-assurance-readiness-determines-who-wins.html | 2026-05-11 |
| KPMG-GAM-2026 | KPMG at the IIA's 2026 GAM conference | KPMG US | conference | https://kpmg.com/us/en/events/2026/kpmg-iias-2026-gam-conference.html | 2026-02-24 |
| COSO-GENAI-2026 | Achieving Effective Internal Control Over Generative AI | COSO | standard-setter | https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf | 2026-02-23 (release date per DART-COSO-2026) |
| DART-COSO-2026 | Heads Up: COSO Releases Publication on Internal Controls Related to Generative AI | Deloitte DART | firm | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai | 2026-04-03 |
| AICPA-AUDITAID-2026 | AI and the audit: AICPA publishes practice aid | Journal of Accountancy (AICPA & CIMA) | professional-body | https://www.journalofaccountancy.com/news/2026/oct/ai-and-the-audit-aicpa-publishes-practice-aid-to-assist-auditors/ | 2026-10-13 |
| CPAPA-AGENTSCLOSE-2026 | Before You Let the Agents Run the Close: Five Controls to Put in Writing First | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/ | 2026-08-13 |
| CPAPA-5Q-2026 | 5 Questions to Ask Before Your SOX Team Adopts AI Agents (author: CEO of Bead AI, a vendor) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/18/5-questions-to-ask-before-your-sox-team-adopts-ai-agents/188703/ | 2026-08-18 |
| BLOOMBERG-BIGFOUR-2026 | Big Four Firms Bet on AI's Promise as Technology Threats Escalate (read via r.jina.ai mirror) | Bloomberg Law | press | https://news.bloomberglaw.com/financial-accounting/big-four-firms-bet-on-ais-promise-as-technology-threats-escalate | 2026-09-30 |
| GRCREPORT-DELOITTE-2026 | Deloitte Sees Internal Audit Moving Closer to the Center of Enterprise Risk in 2026 | GRC Report | press | https://www.grcreport.com/post/deloitte-sees-internal-audit-moving-closer-to-the-center-of-enterprise-risk-in-2026 | 2026 (summary date unclear) |
| CITI-JOB-2026 | Senior Audit Manager, AI Governance and Risks (page now closed; search-only) | Citi | job-posting | https://jobs.citi.com/job/new-york/senior-audit-manager-ai-governance-and-risks/287/88394329696 | 2026-07 (per search result; access: search-only) |
| AMEX-JOB-2026 | Director, Internal Audit AI/GenAI assurance strategy (search-only; page not opened) | American Express | job-posting | not captured (search result only) | 2026-08 (per search result; access: search-only) |
| ANDERA-HOME-2026 | Andera: Automate your controls testing with AI (home page; opened, used only for context) | Andera | vendor | https://www.andera.ai/ | 2026 (undated page) |
| IIA-GAM-2026 | The IIA's Great Audit Minds Conference to be Held March 9-11 (opened; not used as evidence) | The IIA | conference | https://www.theiia.org/en/content/communications/press-releases/2026/the-institute-of-internal-auditors-great-audit-minds-conference-to-be-held-march-9-11-in-las-vegas/ | 2026-02 (page text says February 3, 2025; likely typo) |

**Source count by type (46 listed; 44 opened; 2 search-only).**

| Type | Count |
|---|---|
| firm | 15 |
| press | 11 |
| vendor | 7 |
| survey | 6 |
| job-posting | 3 (1 opened; 2 search-only) |
| conference | 2 |
| standard-setter | 1 |
| professional-body | 1 |
| **Total** | **46** |

Two opened items (ANDERA-HOME-2026, IIA-GAM-2026) are context only and support no entry; BDO-AI-2025 and GT-EAS-2026 are used only for routing. Dates marked "per landscape" were taken from `landscape-advisory.md`.

---

## 6. Gaps

- **No quality evidence of any kind.** No error, override, false-exception, parallel-run, rework or inspection data for AI control testing. No independent (academic, regulator or third-party) measurement found. Searches for parallel-run results returned only guidance and vendor claims.
- **Mid-market advisory firms.** Beyond RSM, Cherry Bekaert, Aprio, Armanino, Riveron and Grant Thornton, no named Baker Tilly, Crowe, Forvis Mazars, CohnReznick, Moss Adams, CBIZ or Weaver internal-audit or SOX AI deployment was found in 2026 sources. One search for these firms returned only KPMG material and staff pages.
- **Fieldguide customer case studies.** Weaver (GRC), Warren Averett, BerryDunn, Forvis Mazars and Aprio PCI pages were opened but carry no publication date, and most describe workflow platforms from the 2020-2023 period; Weaver's 10-12% year-one realization increase and Warren Averett's 15-25% were not used because dates and AI scope could not be confirmed. They also belong to firm operations.
- **Job postings.** Only one open posting was read (RSM, 2026-10-01). Citi's and American Express's AI-governance audit roles surfaced only in search results; Citi's page now returns "Job Not Found". Crowe and Protiviti postings seen in search were not AI-specific and were not read. No posting from a Big Four internal-audit or SOX practice was found.
- **SOX readiness for private and pre-IPO companies.** One KPMG article (2026-06-10) says AI's impact on SOX is "still in its infancy". No firm offering AI-enabled SOX readiness was found.
- **Enterprise risk management.** No ERM-specific AI deployment (risk registers, horizon scanning, quantification) with a named user was found; coverage is limited to IA risk assessment (entry 09) and AI inventory (entry 14).
- **Cyber and IT risk advisory.** Not covered beyond ITGC testing; the landscape also found little.
- **Unverified or conflicting items.**
  - The CPA Practice Advisor article says the AICPA has not published AI-specific SOC guidance; the Journal of Accountancy says it issued such guidance earlier in 2026. Not resolved.
  - The IIA 2025 Pulse figures (41% / 25% / 15%) are second-hand via Fieldguide; the IIA source was not opened.
  - The Internal Audit Foundation's 57%-flat-headcount finding is second-hand.
  - The Bloomberg Law reference to an EY survey (a third of AI leaders reporting a materially negative AI incident) is second-hand.
  - The IIA GAM press release text says "February 3, 2025" for a 2026 event; likely a typo, not resolved.
  - The Deloitte "Mega Hot Topic" item is a secondary summary with an unclear date.
  - A podcast blurb seen in search said Optro acquired Midship; not confirmed from a primary source, not used.
- **Independence rules** for internal-audit outsourcing and AI-governance advisory to audit clients were not checked against AICPA, SEC, PCAOB or IESBA text in this run.
- **Blocked or unavailable:** PwC page via direct curl (403; read via mirror); COSO website had no GenAI page on the home page, so the PDF copy hosted by a Spanish internal-auditors site was used; GT-EAS-2026, BDO-AI-2025 and KPMG-GAM-2026 dates are partly from the landscape or page metadata and were not re-verified in full.
- **Searches used:** 17 web searches across the run. Several search summaries contained claims that are not repeated here (for example, third-party listicle figures and AI-generated roundup pages).
