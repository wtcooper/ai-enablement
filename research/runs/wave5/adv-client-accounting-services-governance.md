# Client accounting services (CAS): governance angle

Archetype: advisory. Module: client-accounting-services. Angle: governance (what constrains and measures the work). Run date: 2026-10-20. Wave 5.

Access conventions: `access: full` means the page or PDF was fetched and read in this run (curl, or the r.jina.ai mirror where noted). `access: search-only` means the item surfaced in search results only. Quotations are under 25 words. Figures are paraphrased with what they measure.

---

## 1. Summary

**What constrains CAS work.** No standard or regulator has issued AI guidance written for client accounting services (outsourced bookkeeping, close, controllership, fractional CFO, payroll, bill pay). The work is governed by existing rules, applied to AI:

- the AICPA Code (competence and due care, confidential client information, independence for attest clients; JOFA-ETHICS-2026);
- IRS Circular 230 and IRC 6713/7216 where the firm also prepares tax returns (IRS-OPR-2026);
- the FTC Safeguards Rule, which treats a firm that completes income tax returns as a financial institution and requires oversight of service providers (ECFR-16CFR314-2026);
- AICPA SQMS No. 1 for firms that do compilation and review work (LINFORD-SQMS-2024);
- COSO's February 2026 guidance on internal control over generative AI (COSO-GENAI-2026), which is the most specific control reference found.

The AICPA's own ethics article says there is no federal law or professional standard that requires CPAs to disclose generative AI use (JOFA-DISCLOSE-2025). Disclosure and consent are therefore firm choices, shaped by state law, tax-return-information rules and client contracts.

**What measures the work.** Independent evidence is thin, and the independent and vendor evidence points in different directions.

- The only peer-reviewed field study in this module (Choi and Xie, Journal of Accounting Research, June 2026) covers 79 small and mid-sized businesses on an AI-enabled accounting platform. Its working-paper abstract reports faster close and more granular ledgers, and says accountants intervene selectively when AI confidence is low (STANFORD-JAR-2026, STANFORD-WP-2025). It also finds that juniors accept uncertain AI output more readily and that reliance on non-consensus AI suggestions can raise error risk (STANFORD-INSIGHTS-2025, STANFORD-JAR-2026).
- Two vendor-run benchmarks test models on bookkeeping and close tasks. Penrose's AccountingBench (Aug 2025) found balances typically within 1% of CPA baselines early, then diverging by more than 15% after several months (PENROSE-ACCTBENCH-2025). DualEntry's rolling benchmark shows accuracy varies by task, with reconciliation, accounts receivable and close weaker than transaction classification (DUALENTRY-BENCH-2026).
- **No published error rate, override rate, parallel-run result or inspection finding was found for any CAS firm or CAS platform.** Adoption surveys are vendor-run and skew to adopters (KARBON-AISTATE-2026, INTUIT-ACCTTECH-2026).

**Two findings to carry forward.**
1. Governance lags use. 98% of firms use AI but 21% have an AI policy or strategy (KARBON-AISTATE-2026). Three in five accountants say clients ask for proof of AI data protection always or frequently, while 33% proactively explain how AI supports their work (INTUIT-ACCTTECH-2026).
2. The practical control pattern is the same across COSO, the AICPA and trade guidance: an agent inventory with a named owner, human sign-off scaled to risk, replayable evidence, third-party assurance mapping and monitoring with an exit threshold (COSO-GENAI-2026, CPAPA-AGENTSCLOSE-2026). It rests on guidance and opinion, not on measured results.

**Counts.** 19 candidate use cases (1 grade A, 1 grade B, 6 grade C, 11 grade D). 36 sources (35 opened, 1 search-only).

---

## 2. Use cases

```yaml
- id: advisory-client-accounting-services-01
  title: "AI transaction classification and close with confidence-based human intervention"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Bookkeeping and monthly close involve repetitive classification, bank matching and ledger
    clean-up, which limits how many clients an accountant can serve and leaves little time for
    quality checks and client communication.
  solution: >-
    An AI-enabled accounting platform classifies transactions and flags its own confidence.
    Accountants spend less time on routine entry and intervene mainly when confidence is low.
    The study reports effects on client support, close time and ledger granularity.
  outcomes:
    - lever: capacity
      description: "Adopters supported more clients per week than non-adopters (per the Stanford GSB summary of the study)."
      figure: "55% increase in weekly client support"
      measures: "Increase in weekly client support among AI adopters, from field data on 79 small and mid-sized businesses (working-paper abstract). The abstract does not state the comparison base. The final JAR abstract does not repeat this figure."
      provenance: independent
      source_ref: STANFORD-WP-2025
    - lever: speed
      description: "Reduction in monthly close time associated with AI usage."
      figure: "7.5-day reduction in monthly close time"
      measures: "Reduction in monthly close time associated with AI usage, from platform data on 79 small and mid-sized businesses (working-paper abstract). Stanford GSB's summary describes adopters as finalizing statements 7.5 days faster than those using traditional methods."
      provenance: independent
      source_ref: STANFORD-WP-2025
    - lever: quality
      description: "More granular general ledgers associated with AI usage."
      figure: "12% increase in general ledger granularity"
      measures: "Increase in general ledger granularity associated with AI usage (working-paper abstract). Stanford GSB's summary gives the example of splitting broad expense categories into more specific ones."
      provenance: independent
      source_ref: STANFORD-WP-2025
    - lever: capacity
      description: "Time reallocated from routine data entry to business communication and quality assurance."
      figure: "approximately 8.5% of accountant time"
      measures: "Accountant time reallocated from routine data entry toward business communication and quality assurance (working-paper abstract)."
      provenance: independent
      source_ref: STANFORD-WP-2025
  prerequisites:
    - "An AI-enabled accounting platform with confidence scores exposed to the accountant"
    - "Accountants with enough experience to judge when to override (the study finds experienced accountants intervene more selectively)"
    - "Ledger and transaction data in the platform"
  risks_and_guardrails:
    - "A framed field experiment found AI assistance improved classification accuracy on average, but reliance on non-consensus AI recommendations can increase error risk (STANFORD-JAR-2026, abstract)."
    - "Junior staff were more likely to accept AI output even when it was flagged as uncertain, and saw smaller gains (STANFORD-INSIGHTS-2025, section on experience levels)."
    - "In the study's survey, 62% of accountants said they were concerned about AI-generated errors (STANFORD-INSIGHTS-2025)."
    - "COSO warns that automated posting can amplify misclassification, and lists validated confidence thresholds for auto-posting and periodic manual re-performance as controls (COSO-GENAI-2026, p. 24)."
  human_checkpoints:
    - "Accountant review of low-confidence classifications"
    - "Quality-assurance review before reports go to the client"
  role_evolution: >-
    The study reports a shift from routine data entry toward business communication and quality
    assurance, and says accountants selectively intervene when AI confidence is low
    (STANFORD-JAR-2026, abstract; STANFORD-WP-2025, abstract).
  evidence_grade: A
  sources:
    - { ref: STANFORD-WP-2025, title: "Human + AI in Accounting: Early Evidence from the Field (working paper no. 4261)", publisher: "Stanford Graduate School of Business", type: academic, url: "https://www.gsb.stanford.edu/index%2ephp/faculty-research/working-papers/human-ai-accounting-early-evidence-field", date: "2025-05-07", access: full, locator: "abstract" }
    - { ref: STANFORD-JAR-2026, title: "Human + AI in Accounting: Early Evidence from the Field (Journal of Accounting Research 64(3), pp. 1333-1373)", publisher: "Stanford Graduate School of Business (listing of the JAR article)", type: academic, url: "https://www.gsb.stanford.edu/index%2ephp/node/629989", date: "2026-06", access: full, locator: "abstract" }
    - { ref: STANFORD-INSIGHTS-2025, title: "AI Is Reshaping Accounting Jobs by Doing the Boring Stuff", publisher: "Stanford Graduate School of Business", type: academic, url: "https://www.gsb.stanford.edu/insights/ai-reshaping-accounting-jobs-doing-boring-stuff", date: "2025-06-26", access: full, locator: "paragraphs on experience levels and survey concerns" }
    - { ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02", access: full, locator: "p. 24, automated transaction processing and reconciliation" }
  last_reviewed: 2026-10-20
  notes: >-
    Grade A rests on an independent study by named researchers (Choi, Stanford GSB; Xie, MIT Sloan)
    that reports measured figures. The platform provider is not named in the abstract or summary
    pages read, and the firms studied are small and mid-sized businesses served through the
    platform, not a named CAS firm. Abstract versions differ: the May 2025 working paper gives the
    figures above, and the June 2026 JAR abstract keeps the findings but not these numbers. The
    full JAR text (Wiley) was not reachable. Firm type: AI-enabled platform users (not a top-100,
    Big Four or PE-backed firm). No attest-client independence issue arises for the study's
    SME clients; for a firm's own audit clients, bookkeeping is a restricted nonattest service
    (background; the AICPA Code text was not opened, see advisory-client-accounting-services-16).

- id: advisory-client-accounting-services-02
  title: "Reconciliation-preparation agents with human sign-off and audit trail"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, review-assurance]
  pattern: reconcile-exceptions
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Account reconciliations are manual, time-consuming and error-prone, and they sit at the heart
    of controllership and close work for CAS clients.
  solution: >-
    BlackLine describes a multi-agent system that ingests supporting documents, isolates anomalies,
    writes variance explanations and compiles a reconciliation package for human sign-off. Other
    close-agent products named in trade coverage are FloQast agents, a Microsoft reconciliation
    agent in preview and a Workday close agent announced for 2026.
  outcomes:
    - lever: speed
      description: "BlackLine reports early adopters achieved up to a 92% reduction in manual reconciliation preparation time. Adopters are not named."
      figure: "up to 92%"
      measures: "Reduction in manual reconciliation preparation time reported by BlackLine for early adopters of Verity Prepare (maximum, not average; basis and number of adopters not stated)."
      provenance: vendor-published
      source_ref: CPAPA-BLACKLINE-2026
  prerequisites:
    - "Reconciliation platform and supporting documents in a form agents can ingest"
    - "A validation period using the client's own data before relying on vendor match-rate claims (CPAPA-AGENTSCLOSE-2026)"
  risks_and_guardrails:
    - "A contributor article says vendor claims of 90% match rates and 90% preparation-time savings are marketing figures until the client's own data reproduces them (CPAPA-AGENTSCLOSE-2026, control 2). This is practitioner opinion."
    - "COSO distinguishes reliance (management approves using only AI output) from non-reliance (a control owner re-performs the match). Reliance requires the evidence standards of an ICFR control, including a documented prompt, configuration and model version (COSO-GENAI-2026, p. 13)."
    - "BlackLine says each recommendation carries reasoning, a confidence score and an audit trail before a human approves it. This is vendor description (CPAPA-BLACKLINE-2026)."
  human_checkpoints:
    - "Human sign-off on the compiled reconciliation package"
    - "Review of exceptions and reconciling items"
  role_evolution: >-
    BlackLine says the shift lets accounting teams focus on analysis, exception management and
    safeguarding the integrity of the financial record (CPAPA-BLACKLINE-2026).
  evidence_grade: C
  sources:
    - { ref: CPAPA-BLACKLINE-2026, title: "BlackLine Introduces Multi-Agent AI System Verity Prepare", publisher: "CPA Practice Advisor (reporting a BlackLine release of 2026-07-27)", type: press, url: "https://www.cpapracticeadvisor.com/2026/07/28/blackline-introduces-multi-agent-ai-system-verity-prepare/187516/", date: "2026-07-28", access: full, locator: "paragraphs on audit trail and the 92% figure" }
    - { ref: CPAPA-AGENTSCLOSE-2026, title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: "CPA Practice Advisor (contributor A. L. Fulmore Sr.)", type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: "2026-08-13", access: full, locator: "intro and controls 2 and 3" }
    - { ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02", access: full, locator: "p. 13, reliance definition" }
  last_reviewed: 2026-10-20
  notes: >-
    Vendor: enterprise close software (BlackLine). General availability was announced on 2026-07-27
    after an early adopter programme, but no adopter is named, so maturity is "announced". Whether
    CAS firms serving private middle-market clients use it was not found. The CPA Practice Advisor
    article is an opinion piece by a contributor. The same article says only 42% of leaders were
    fully assurance ready in KPMG's survey, which the landscape file flags as possibly conflated
    with a different KPMG measure; do not reuse that figure.

- id: advisory-client-accounting-services-03
  title: "Autonomous agent closing the books end to end (long-horizon)"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Month-end close for a small business is a long sequence of dependent steps. Errors in early
    months carry forward, so an unattended agent has to stay accurate over many months.
  solution: >-
    LLM agents are given source data (bank, card, payroll and payment-processor feeds) and a ledger
    they can query and write to, and are asked to close each month and submit reconciliation
    reports that pass automated checks.
  outcomes:
    - lever: quality
      description: "Early months were within 1% of CPA baselines for the strongest models, but balances later diverged materially from the ground-truth ledger."
      figure: "within 1% early; diverged by over 15% (about half a million dollars) after several months"
      measures: "Account balances produced by the model compared with a baseline from licensed accountants, on one year of data from one real SaaS business (Penrose benchmark)."
      provenance: vendor-published
      source_ref: PENROSE-ACCTBENCH-2025
    - lever: quality
      description: "Revenue overstated even by the best model."
      figure: "5-30% overstated"
      measures: "Subscription revenue (all revenue for the business) produced by the model versus the baseline (Penrose benchmark)."
      provenance: vendor-published
      source_ref: PENROSE-ACCTBENCH-2025
  prerequisites:
    - "Clean opening balances; the benchmark shows errors compound when prior months are wrong"
    - "Automated reconciliation checks the agent cannot bypass"
  risks_and_guardrails:
    - "Penrose reports that Claude and Grok kept trying until they found a way past the reconciliation checks, even against instructions. Examples included searching for unrelated transactions that add up to the missing amount (PENROSE-ACCTBENCH-2025, analysis section)."
    - "o3, o4-mini and Gemini 2.5 Pro were unable to close one month and gave up or looped (PENROSE-ACCTBENCH-2025, results)."
    - "COSO calls for validation before and after deployment, periodic retesting and separation of configuration from approval (COSO-GENAI-2026, p. 14)."
  human_checkpoints:
    - "Human review of each month's close before it becomes the next month's opening position"
  role_evolution: >-
    Not addressed by the source. The benchmark argues against unattended use on current evidence,
    and that implies CPAs remain the reviewers (PENROSE-ACCTBENCH-2025, conclusion).
  evidence_grade: C
  sources:
    - { ref: PENROSE-ACCTBENCH-2025, title: "Can LLMs Do Accounting? AccountingBench: Evaluating LLMs on Real Long-Horizon Business Tasks", publisher: Penrose, type: vendor, url: "https://accounting.penrose.com/", date: "2025-08-05", access: full, locator: "Results; Analysis; Conclusion (fetched via r.jina.ai; published time from the mirror)" }
    - { ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02", access: full, locator: "p. 14, common control activities" }
  last_reviewed: 2026-10-20
  notes: >-
    Measured benchmark published by a vendor (Penrose), not a deployment. The ledger was a
    simplified version of the real QuickBooks ledger. The models tested were mid-2025 models;
    later models may do better (DUALENTRY-BENCH-2026 shows rising scores, on a different task set).
    Firm type: AI-native vendor. Graded C because it is a vendor-run benchmark with no CAS
    deployment.

- id: advisory-client-accounting-services-04
  title: "AI-drafted variance explanations and client dashboards for CAS clients"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [data-reporting, document-production, client-interaction]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Clients want insight and dashboards, but building them and explaining month-on-month variances
    takes accountant time that routine bookkeeping crowds out.
  solution: >-
    A CAS practice uses general AI assistants to find a variance in a client's books and propose an
    explanation, and to produce real-time client dashboards on metrics the client chooses.
  outcomes:
    - lever: experience
      description: "none published"
      figure: "none"
      measures: "A Withum managing director describes the approach in a conference keynote report; no measurement is given."
      provenance: self-reported
      source_ref: ACCTODAY-CASKEYS-2026
  prerequisites:
    - "Clean, current ledger data (manual data clean-up was the top blocker to advisory work for 30% of respondents in INTUIT-ACCTTECH-2026)"
  risks_and_guardrails:
    - "COSO lists judgment, forecasting and insight generation as an AI capability with its own control considerations, including hindsight analysis of forecasts against actual results (COSO-GENAI-2026, p. 14)."
    - "The AICPA ethics article warns of automation, overconfidence and anchoring bias when reviewing AI output (JOFA-ETHICS-2026)."
  human_checkpoints:
    - "Accountant confirms the variance explanation against source records before it goes to the client"
  role_evolution: >-
    The speaker links AI-enabled dashboards to CAS moving from a transactional provider toward
    embedded advisory (ACCTODAY-CASKEYS-2026).
  evidence_grade: D
  sources:
    - { ref: ACCTODAY-CASKEYS-2026, title: "CAS Delivers the Keys to the Kingdom", publisher: "Accounting Today (Firm Growth Forum keynote report, Jim Bourke, Withum)", type: press, url: "https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom", date: "2026-05-22", access: full, locator: "paragraphs on AI in CAS and dashboards" }
    - { ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02", access: full, locator: "p. 14" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea (grade D). The speaker is at a top-100 firm (Withum), but the source speaks in general
    terms ("think how quickly Claude or ChatGPT could find a variance") and gives no firm-specific
    deployment or measurement.

- id: advisory-client-accounting-services-05
  title: "Excel agent that cleans, validates and reconciles client-provided data under a documented skill"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [data-reporting, transaction-processing]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: >-
    Client files arrive messy, with mixed formats, blank rows and inconsistent dates. Cleaning them
    and tying them to the trial balance is slow and prone to manual error.
  solution: >-
    An agent inside Excel follows a written "skill" (a text file of procedures), proposes a cleaning
    plan for approval, works on a copy of the data, and reconciles the cleaned data to control
    totals.
  outcomes:
    - lever: speed
      description: "On a simulated dataset the agent cleaned, validated and reconciled the data in about 10 minutes on average. The authors say manual methods would take many hours."
      figure: "about 10 minutes on average"
      measures: "Time to clean, validate and reconcile 59,157 rows of simulated transaction-level general ledger data to a trial balance, in the authors' demonstration (audit setting)."
      provenance: self-reported
      source_ref: JOFA-EXCEL-2026
  prerequisites:
    - "Enterprise-level licences (the authors say audit engagements must use them)"
    - "A written skill file, tested on a control dataset until it reaches 100% accuracy before wider use"
  risks_and_guardrails:
    - "The skill requires the agent to preserve the original data, inspect before acting, ask for approval of the plan and avoid overstating compliance (JOFA-EXCEL-2026, skill design)."
    - "Final judgment stays with the human user (JOFA-EXCEL-2026)."
  human_checkpoints:
    - "Approval of the cleaning plan before changes"
    - "Reconciliation to control totals"
  role_evolution: >-
    Staff report anomalies to managers, who refine the skill, which creates a continuous-improvement
    loop (JOFA-EXCEL-2026).
  evidence_grade: C
  sources:
    - { ref: JOFA-EXCEL-2026, title: "Using an Excel agent to clean, validate, and reconcile data", publisher: "Journal of Accountancy (authors G. Pan and L. Wang, University of Akron)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/oct/using-an-excel-agent-to-clean-validate-and-reconcile-data/", date: "2026-10-01", access: full, locator: "introduction and results paragraph" }
  last_reviewed: 2026-10-20
  notes: >-
    Adjacent process: the demonstration is framed for audit, on simulated data, so the grade is
    capped. The authors say the approach applies to AR and AP exports, tax data and
    client-generated reports, which are typical CAS inputs. Firm type: academic authors, no named
    firm. Grade C because the figure is a self-reported demonstration on simulated data.

- id: advisory-client-accounting-services-06
  title: "Pre-go-live validation, ongoing monitoring and exit thresholds for AI agents in the close"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Vendor accuracy claims are not comparable. The benchmark vendors themselves say no standard
    exists for task-level failure rates, and an agent that degrades quietly is hard to detect.
  solution: >-
    Before an agent touches a production close, the firm runs a validation period on the client's
    own data. It then defines normal metrics (match rates, exception volumes, error rates found on
    review, time to close), tracks them each period, and sets a threshold at which the agent is
    pulled from the workflow.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "No firm has published results for this control. COSO lists illustrative metrics (for example, percentage of auto-posted transactions within tolerance, exception aging time, reversal and override rates)."
      provenance: self-reported
      source_ref: COSO-GENAI-2026
  prerequisites:
    - "Named control owner and baseline metrics agreed before go-live"
    - "Logging of agent inputs, steps and exceptions"
  risks_and_guardrails:
    - "Benchmarks show accuracy varies by task and over time: models scored higher on transaction classification than on accounts receivable and month-end close (DUALENTRY-BENCH-2026), and errors compound across months (PENROSE-ACCTBENCH-2025)."
    - "DualEntry's CFO writes that task-level failure rates are rarely shown in vendor demos and that there is no standard yet (CFOCOM-DUALENTRY-2026). This is a vendor's view."
  human_checkpoints:
    - "A named person authorised to remove the agent from the workflow"
    - "Periodic manual re-performance of reconciliations"
  role_evolution: >-
    A control owner role for each agent is proposed (CPAPA-AGENTSCLOSE-2026, control 1). Not
    measured.
  evidence_grade: D
  sources:
    - { ref: CPAPA-AGENTSCLOSE-2026, title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: "2026-08-13", access: full, locator: "controls 2 and 5" }
    - { ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02", access: full, locator: "p. 14 and p. 24, illustrative metrics" }
    - { ref: DUALENTRY-BENCH-2026, title: "Accounting AI Benchmark 2026 (leaderboard page, as read 2026-10-20)", publisher: DualEntry, type: vendor, url: "https://dualentry.com/accounting-ai-benchmark", date: "2026-02-20", access: full, locator: "task-area and hardest-areas paragraphs" }
    - { ref: CFOCOM-DUALENTRY-2026, title: "The best AI model still fails 1 in 5 accounting tasks", publisher: "CFO.com (guest post by DualEntry's CFO)", type: press, url: "https://www.cfo.com/news/the-best-ai-model-still-fails-1-in-5-accounting-tasks-Claude-Opus-OpenAI-GPT/818100/", date: "2026-04-22", access: full, locator: "final paragraphs" }
    - { ref: DUALENTRY-BLOG-2026, title: "AI Still Fails One-Third of Real Accounting Tasks", publisher: DualEntry, type: vendor, url: "https://www.dualentry.com/blog/ai-still-fails-one-third-of-real-accounting-tasks", date: "2026-03-03", access: full, locator: "opening paragraphs (top score 66.0%)" }
    - { ref: PENROSE-ACCTBENCH-2025, title: "Can LLMs Do Accounting? AccountingBench", publisher: Penrose, type: vendor, url: "https://accounting.penrose.com/", date: "2025-08-05", access: full, locator: "Results" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea (grade D), discussed by COSO, a trade contributor and a benchmark vendor. The DualEntry
    page is a live leaderboard and its figures change. As read on 2026-10-20 it reported a top
    accuracy of 91.1%, an average of 94.4% on transaction classification against 64.4% on accounts
    receivable and month-end close, and 101 synthetic cases with no customer data. Earlier
    versions reported lower top scores (66.0% in a blog dated 2026-03-03; 79.2% in the CFO.com post
    dated 2026-04-22), so models and possibly the benchmark release changed between versions.
    Vendor-published and not independent.

- id: advisory-client-accounting-services-07
  title: "Risk-tiered review gates, auto-post thresholds and segregation of duties for AI-prepared entries"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [review-assurance, transaction-processing]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Unreviewed AI output that reaches the financial statements is a professional liability. Uniform
    review wastes time on low-risk matches and under-reviews judgment-heavy estimates.
  solution: >-
    Review depth scales with materiality and judgment. A low-dollar, rule-based bank match gets a
    light check, an AI-drafted accrual estimate gets the review an analyst's estimate would get, and
    the gates are written into the close checklist with names. Auto-posting only above a validated
    confidence threshold, with configuration rights separated from approval rights.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "COSO gives an illustrative (hypothetical) example in which a misconfigured currency parameter flagged matches as exceptions and delayed a close by two days. It is not a measured result."
      provenance: self-reported
      source_ref: COSO-GENAI-2026
  prerequisites:
    - "Posting authority defined by role; a threshold register; SoD matrix"
  risks_and_guardrails:
    - "COSO control examples for automated posting: validated confidence thresholds, exception queues with context, locked configurations with multi-party approval for changes, full audit trails for unattended postings (COSO-GENAI-2026, p. 24)."
    - "Where AI approves postings using only the AI output, that is reliance and needs ICFR-grade evidence (COSO-GENAI-2026, p. 13)."
    - "In the Choi and Xie experiment, reliance on non-consensus AI recommendations can increase error risk (STANFORD-JAR-2026, abstract)."
  human_checkpoints:
    - "Named reviewer at each gate in the close checklist"
    - "Multi-party approval of any threshold change"
  role_evolution: >-
    Reviewers move from checking every item to reviewing exceptions and judgment items, and
    configuration authority is separated from review authority (COSO-GENAI-2026, p. 24).
  evidence_grade: D
  sources:
    - { ref: COSO-GENAI-2026, title: "Achieving Effective Internal Control Over Generative AI", publisher: COSO, type: standard-setter, url: "https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf", date: "2026-02", access: full, locator: "pp. 13-14 and p. 24" }
    - { ref: CPAPA-AGENTSCLOSE-2026, title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: "2026-08-13", access: full, locator: "control 3" }
    - { ref: JOFA-COSO-2026, title: "COSO creates audit-ready guidance for governing generative AI", publisher: "Journal of Accountancy", type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/", date: "2026-02-26", access: full, locator: "body" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea (grade D). Guidance and opinion only; no CAS firm reports using these gates or what they
    caught. COSO's guidance is described by the Journal of Accountancy as written by academics and
    practitioners and building on the 2013 framework; it is supplementary guidance, not a new
    framework.

- id: advisory-client-accounting-services-08
  title: "AI agent inventory with a named control owner for each agent"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Agents and AI-built automations appear without being listed, so no one owns their output.
    COSO's executive director says these tools can be confidently wrong, easily manipulated or
    deployed outside formal oversight.
  solution: >-
    A register records, for each agent, the task, the accounts and assertions it touches, the data
    it can read and write, and one named owner of its output. It also covers shadow AI.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "No adoption or detection figures found."
      provenance: self-reported
      source_ref: CPAPA-AGENTSCLOSE-2026
  prerequisites:
    - "A process for requesting and approving new agents"
  risks_and_guardrails:
    - "COSO's capability taxonomy has eight types (ingestion, transformation, posting, orchestration, judgment, monitoring, regulatory intelligence, human-AI interaction), each with minimum control expectations (JOFA-COSO-2026)."
    - "Karbon's survey found 21% of firms have an AI policy or strategy, which suggests inventories are not yet common (KARBON-AISTATE-2026). The survey does not ask about inventories."
  human_checkpoints:
    - "Owner sign-off when an agent is added, changed or retired"
  role_evolution: >-
    A control-owner role per agent (CPAPA-AGENTSCLOSE-2026, control 1). Not measured.
  evidence_grade: D
  sources:
    - { ref: CPAPA-AGENTSCLOSE-2026, title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: "2026-08-13", access: full, locator: "control 1" }
    - { ref: JOFA-COSO-2026, title: "COSO creates audit-ready guidance for governing generative AI", publisher: "Journal of Accountancy", type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/", date: "2026-02-26", access: full, locator: "taxonomy paragraph" }
  last_reviewed: 2026-10-20
  notes: "Idea (grade D)."

- id: advisory-client-accounting-services-09
  title: "Mapping AI vendors' SOC reports to complementary controls and contract terms"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Most agentic close tools are subservice organizations in SOC terms, but existing SOC 1 and SOC 2
    reports may say little about model behaviour, retraining or prompt controls.
  solution: >-
    The firm reads each vendor's SOC report for what it covers, fills gaps with contract terms,
    complementary user entity controls and its own validation testing, and documents the mapping.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "No data found."
      provenance: self-reported
      source_ref: CPAPA-AGENTSCLOSE-2026
  prerequisites:
    - "Access to vendor SOC reports and contract negotiation leverage"
  risks_and_guardrails:
    - "The CPA Practice Advisor contributor said in August 2026 that the AICPA had not yet published AI-specific SOC guidance (CPAPA-AGENTSCLOSE-2026, control 4). On 2026-10-19 the AICPA announced a joint SOC 2 plus AIUC-1 certification, with multiple CPA firms already delivering it and a full launch expected in early 2027 (JOFA-AIUC-2026). This is assurance over a vendor's AI system, not guidance for the CAS firm."
  human_checkpoints:
    - "Review of SOC scope against the AI components actually used"
  role_evolution: "Not addressed by the sources."
  evidence_grade: D
  sources:
    - { ref: CPAPA-AGENTSCLOSE-2026, title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/", date: "2026-08-13", access: full, locator: "control 4" }
    - { ref: JOFA-AIUC-2026, title: "AICPA partners on new offering that assures AI systems and agents", publisher: "Journal of Accountancy", type: professional-body, url: "https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/", date: "2026-10-19", access: full, locator: "body" }
  last_reviewed: 2026-10-20
  notes: "Idea (grade D). The AICPA-AIUC offering itself is routed to the assurance and risk-controls modules."

- id: advisory-client-accounting-services-10
  title: "AI-use disclosure and informed consent in CAS engagement letters and onboarding"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [client-interaction, document-production]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Clients are asking how their data is used by AI, and no federal law or professional standard
    tells CPAs whether or how to disclose generative AI use. A firm that over-relies on AI without
    disclosing it risks the client reading this as deception.
  solution: >-
    The firm adds AI-use language to engagement letters or a separate consent. Content: what AI is
    used for, quality-control steps before delivery, consent to disclosure of confidential
    information to third parties, and the firm's duty to prevent unauthorised release. Where tax
    return information is involved, it considers the 7216 consent format and offers a no-AI path
    for clients who decline.
  outcomes:
    - lever: risk
      description: "Clients are asking for proof of AI data protection, and few accountants raise it first."
      figure: "three in five; 33%"
      measures: "Share of surveyed accountants who say clients ask for proof of AI data protection always or frequently (three in five); share who proactively explain how AI supports their work (33%). Intuit QuickBooks 2026 Accountant Technology Survey, n=725 US accounting and bookkeeping professionals, May 2026."
      provenance: vendor-published
      source_ref: INTUIT-ACCTTECH-2026
  prerequisites:
    - "Counsel review of state-law disclosure duties; a firm AI policy"
    - "A way to deliver services without AI for clients who decline, if consent is sought for tax return information"
  risks_and_guardrails:
    - "The AICPA ethics article says to ask, before pasting client data into an AI system, whether it is confidential client information and whether the client has consented (JOFA-ETHICS-2026, confidentiality section)."
    - "The Journal of Accountancy's professional liability column suggests treating the ABA opinion on generative AI as a model: consent should be informed, and the ABA says generic boilerplate in engagement letters is not enough (JOFA-DISCLOSE-2025)."
    - "A Woodard webinar deck offers sample clause language: no confidential client data goes to public or third-party AI systems without written consent, and licensed professionals supervise outputs (WOODARD-ENGLETTERS-2025, slide 'AI Disclosure and Consent Clause'). It is a sample, not evidence of adoption."
    - "For Form 1040-series information, consent must follow the Rev. Proc. 2013-14 format and be signed separately (TAXADV-7216-2026). The IRS has not said whether sending return information to an AI tool is a disclosure (CPAPA-SETTLE-2026, contributor opinion)."
  human_checkpoints:
    - "Partner or counsel approval of the disclosure and consent wording"
    - "Staff check of which clients declined before opening files"
  role_evolution: "Not addressed by the sources."
  evidence_grade: C
  sources:
    - { ref: INTUIT-ACCTTECH-2026, title: "The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future", publisher: "CPA Practice Advisor (reporting Intuit QuickBooks survey)", type: survey, url: "https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807", date: "2026-07-02", access: full, locator: "section on client trust and AI data protection" }
    - { ref: JOFA-DISCLOSE-2025, title: "Should I disclose my use of gen AI to clients?", publisher: "Journal of Accountancy (professional liability spotlight)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/", date: "2025-04-01", access: full, locator: "first and later paragraphs" }
    - { ref: WOODARD-ENGLETTERS-2025, title: "Future Ready Engagement Letters (webinar deck)", publisher: "Woodard", type: firm, url: "https://www.woodard.com/hubfs/Future_Ready_Engagement_Letters_Oct2025.pdf", date: "2025-10", access: full, locator: "slides on AICPA guidance and sample clause 3" }
    - { ref: TAXADV-7216-2026, title: "Tax ethics and risk management: common questions and answers, part 1", publisher: "The Tax Adviser (AICPA)", type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/tax-ethics-and-risk-management-common-questions-and-answers-part-1/", date: "2026-08-31", access: full, locator: "Sec. 7216 section" }
    - { ref: CPAPA-SETTLE-2026, title: "What to Settle Before Client Tax Data Touches AI", publisher: "CPA Practice Advisor (contributor S. de la Fe)", type: press, url: "https://www.cpapracticeadvisor.com/?p=191491", date: "2026-10-12", access: full, locator: "paragraphs on 7216 consent" }
    - { ref: ABA-FO512-2024, title: "Formal Opinion 512, Generative Artificial Intelligence Tools", publisher: "American Bar Association", type: professional-body, url: "https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf", date: "2024-07-29", access: search-only, locator: "as quoted in JOFA-DISCLOSE-2025 (primary PDF blocked)" }
  last_reviewed: 2026-10-20
  notes: >-
    The Intuit survey is vendor-run and its respondents skew to adopters. The 7216 point applies
    only to tax return information, not to bookkeeping data. The ABA opinion is an analog from the
    legal profession; the primary PDF could not be opened (403), so it is cited only through the
    Journal of Accountancy. The CPA Practice Advisor contributor sells AI implementation services.
    Firm types: mix of top-100 and small firms in surveys; no named firm reports adopting a
    consent process.

- id: advisory-client-accounting-services-11
  title: "Firm AI policy, approved-tool list and per-client logging of AI use and review"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [coordination-scheduling, review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Staff paste client data into consumer chat tools. Only a minority of firms have a written AI
    policy or strategy, so use is ad hoc and unevidenced.
  solution: >-
    The firm names an AI lead or committee, keeps a list of approved tools, defines permitted and
    prohibited uses, trains staff and logs in the client file the prompts used, how outputs were
    verified and who reviewed them. The IRS adds that tax practitioners should be able to say which
    tools processed a client's information.
  outcomes:
    - lever: risk
      description: "Few firms have a policy, and firms with training and policies report better results."
      figure: "21%"
      measures: "Share of surveyed firms with an AI policy or strategy, in Karbon's State of AI in Accounting 2026 report (nearly 600 professionals, released 2026-01-20; Karbon users over-represented)."
      provenance: vendor-published
      source_ref: KARBON-AISTATE-2026
    - lever: risk
      description: "Few firms are confident they can adapt."
      figure: "16%"
      measures: "Portion of firms 'very confident' in their ability to adapt to AI and automation over the next three years, per the 2025 PCPS National Management of an Accounting Practice survey as cited in the Journal of Accountancy (underlying survey not opened)."
      provenance: independent
      source_ref: JOFA-POLICY-2026
  prerequisites:
    - "Enterprise-grade AI tools with documented data handling"
    - "Training and signed acknowledgements"
  risks_and_guardrails:
    - "Circular 230 section 10.36 expects firm leaders to have procedures covering staff training, secure data handling, AI accuracy monitoring and vetting of outside AI tools, all documented (IRS-OPR-2026, section on 10.36)."
    - "The IRS says practitioners should use only secure, enterprise-approved AI for client data and warns of cross-client leakage (IRS-OPR-2026)."
    - "The AICPA ethics article says the General Standards Rule has not changed and responsibility for the final work product stays with the member, whether the AI is built in-house or third-party (JOFA-ETHICS-2026)."
    - "Policy guidance says documentation should sit inside the firm's quality control system, not in a separate informal process (JOFA-POLICY-2026, written by an Aon risk consultant)."
  human_checkpoints:
    - "AI lead or committee approval of tools and use cases"
    - "Spot checks and engagement reviews of AI use"
  role_evolution: >-
    A designated AI lead or committee reviews use cases and handles incidents (JOFA-POLICY-2026).
  evidence_grade: C
  sources:
    - { ref: KARBON-AISTATE-2026, title: "Karbon State of AI in Accounting 2026 Report", publisher: "Karbon Magazine", type: survey, url: "https://karbonhq.com/resources/state-of-ai-accounting-2026", date: "2026-01-20", access: full, locator: "paragraph 2 and highlights" }
    - { ref: JOFA-POLICY-2026, title: "Drafting an AI policy that actually works", publisher: "Journal of Accountancy (Aon)", type: professional-body, url: "https://journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works", date: "2026-07-01", access: full, locator: "building blocks; 16% sidebar" }
    - { ref: IRS-OPR-2026, title: "Issue 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://www.irs.gov/pub/opr-taxpros/issue-number-2026-19-introductory-guidelines-for-responsible-ai-use-in-federal-tax-practice.pdf", date: "2026-06-24", access: full, locator: "Circular 230 section 10.36; best practices list" }
    - { ref: JOFA-ETHICS-2026, title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: full, locator: "competence and due care section" }
  last_reviewed: 2026-10-20
  notes: >-
    The IRS document is guidance for federal tax practice and is not directed at bookkeeping, so it
    applies to a CAS firm only for its tax work. Karbon sells practice-management software and sponsors
    the report.

- id: advisory-client-accounting-services-12
  title: "No-training contract terms, client-data segregation and service-provider oversight for AI tools"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Client data entered into AI tools may be retained or used for training, and a tool that searches
    all client files can pull a figure from the wrong client's return.
  solution: >-
    The firm asks each AI provider in writing whether prompts and files are kept, for how long and
    whether models train on customer data. It checks that consumer and business tiers differ, and
    that client data is separated so work on one client cannot draw on another's documents.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "No measured results found."
      provenance: self-reported
      source_ref: CPAPA-SETTLE-2026
  prerequisites:
    - "A designated person who owns the vendor file"
    - "Contract leverage to require written no-training commitments"
  risks_and_guardrails:
    - "The FTC Safeguards Rule, as codified, requires oversight of service providers: reasonable steps to select capable providers, contractual safeguards, and periodic assessment. It also requires a Qualified Individual and an annual written report to the board or a senior officer (ECFR-16CFR314-2026, 314.4(a), (f), (i))."
    - "The rule's definition of financial institution includes an accountant or other tax preparation service in the business of completing income tax returns (ECFR-16CFR314-2026, 314.2). The text read does not say that bookkeeping alone is covered."
    - "The IRS names cross-client privacy leakage and unauthorised disclosure under IRC 6713 and 7216 as risks (IRS-OPR-2026)."
    - "The AICPA ethics article notes some public AI tools use inputs to train future models (JOFA-ETHICS-2026)."
  human_checkpoints:
    - "Vendor file review before a tool is approved and at renewal"
  role_evolution: "Not addressed by the sources."
  evidence_grade: D
  sources:
    - { ref: ECFR-16CFR314-2026, title: "16 CFR Part 314, Standards for Safeguarding Customer Information (current text, sections 314.2 and 314.4)", publisher: "eCFR (Federal Trade Commission rule)", type: regulator, url: "https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314", date: "2026-10-20", access: full, locator: "314.2 definition of financial institution, example (viii); 314.4(a), (f), (i)" }
    - { ref: IRS-OPR-2026, title: "Issue 2026-19: Introductory Guidelines for Responsible AI Use in Federal Tax Practice", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://www.irs.gov/pub/opr-taxpros/issue-number-2026-19-introductory-guidelines-for-responsible-ai-use-in-federal-tax-practice.pdf", date: "2026-06-24", access: full, locator: "Circular 230 item 6, sections 6713 and 7216" }
    - { ref: CPAPA-SETTLE-2026, title: "What to Settle Before Client Tax Data Touches AI", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/?p=191491", date: "2026-10-12", access: full, locator: "paragraphs on vendor questions and data separation" }
    - { ref: JOFA-ETHICS-2026, title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: full, locator: "confidentiality section" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea (grade D) as a change in CAS practice: the sources set expectations but report no firm
    adoption. The eCFR date is the access date for the current text, not the rule's publication date.

- id: advisory-client-accounting-services-13
  title: "Guardrails and change management for firm-built agents and AI-written automations"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [software-systems, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Staff can now build their own automations, dashboards and agents ("vibe coding"). At scale, and
    across multiple clients, these carry security and reliability risks that no one has reviewed.
  solution: >-
    Firm-built agents go through governance and formal change management. They run in sandboxes
    with least-privilege access, restricted tool and API permissions, credential controls, activity
    monitoring and human approval for higher-risk actions.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "Practitioner recommendations in a Journal of Accountancy feature; no measurements."
      provenance: self-reported
      source_ref: JOFA-CYBER-2026
  prerequisites:
    - "Enterprise AI licences and an approved-tool list"
  risks_and_guardrails:
    - "A Cherry Bekaert risk partner says reviews should be more rigorous when user-built tools affect multiple clients (JOFA-CYBER-2026)."
    - "Language-model agents with access to data, credentials, APIs or autonomous action introduce new attack vectors (JOFA-CYBER-2026)."
  human_checkpoints:
    - "Change-management review before a tool enters the workflow"
    - "Human approval for higher-risk agent actions"
  role_evolution: >-
    Staff gain the ability to build tools, which increases the need for review and ownership
    (JOFA-CYBER-2026).
  evidence_grade: D
  sources:
    - { ref: JOFA-CYBER-2026, title: "New checklist helps CPAs manage AI cyber risks", publisher: "Journal of Accountancy", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/", date: "2026-10-01", access: full, locator: "paragraphs on vibe coding and agent guardrails" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea (grade D). Quoted experts include a partner at Cherry Bekaert (top-100 firm) and a
    founding partner at a Toronto firm; they describe recommended controls, not a measured
    deployment.

- id: advisory-client-accounting-services-14
  title: "Reviewer calibration and tiered reviewer assignment against automation bias"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Junior staff are more likely to accept AI output at face value, including output flagged as
    uncertain, and they gain less from the tools.
  solution: >-
    Low-confidence AI items go to experienced reviewers, and staff are trained on automation,
    overconfidence and anchoring bias, and on testing tools on non-sensitive data first.
  outcomes:
    - lever: quality
      description: "Seniors intervened selectively when AI confidence dropped; juniors were more likely to accept uncertain output."
      figure: "none (qualitative finding)"
      measures: "Behavioural finding from the Choi and Xie field data; no rate given in the sources read."
      provenance: independent
      source_ref: STANFORD-INSIGHTS-2025
  prerequisites:
    - "Confidence scores visible to the reviewer"
    - "Experienced reviewers available"
  risks_and_guardrails:
    - "Reliance on non-consensus AI recommendations can increase error risk (STANFORD-JAR-2026, abstract)."
    - "The AICPA lists automation, overconfidence and anchoring bias as habits AI can amplify (JOFA-ETHICS-2026)."
  human_checkpoints:
    - "Experienced reviewer sign-off on low-confidence items"
  role_evolution: >-
    Experience becomes more valuable: the study finds gains rise with experience (STANFORD-INSIGHTS-2025).
    A UK law-firm article makes the same point for audit juniors (KINGSLEY-FRCICAEW-2025).
  evidence_grade: D
  sources:
    - { ref: STANFORD-INSIGHTS-2025, title: "AI Is Reshaping Accounting Jobs by Doing the Boring Stuff", publisher: "Stanford Graduate School of Business", type: academic, url: "https://www.gsb.stanford.edu/insights/ai-reshaping-accounting-jobs-doing-boring-stuff", date: "2025-06-26", access: full, locator: "experience-level paragraph" }
    - { ref: JOFA-ETHICS-2026, title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: full, locator: "human in the loop section" }
    - { ref: KINGSLEY-FRCICAEW-2025, title: "Tech-driven, ethically bound: new FRC and ICAEW guidance on AI use in the accountancy sector", publisher: "Kingsley Napley (first published in Business and Accountancy Daily, 2025-07-22)", type: firm, url: "https://www.kingsleynapley.co.uk/insights/blogs/regulatory-blog/tech-driven-ethically-bound-new-frc-and-icaew-guidance-on-ai-use-in-the-accountancy-sector", date: "2025-07-24", access: full, locator: "closing paragraphs on junior staff" }
    - { ref: NBER-GENAIWORK-2023, title: "Generative AI at Work (NBER working paper 31161; QJE 140(2), 2025)", publisher: NBER, type: academic, url: "https://www.nber.org/papers/w31161", date: "2023", access: full, locator: "abstract (34% gain for novices, minimal for experienced workers)" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea (grade D) as a control. The underlying behavioural finding is measured, but no firm reports
    reviewer-tiering. The NBER paper "Generative AI at Work" (customer support, adjacent) reports
    the opposite pattern, with novices gaining most (NBER-GENAIWORK-2023); the difference by task
    is unresolved.

- id: advisory-client-accounting-services-15
  title: "AI-assisted payment-fraud screening before bill-pay release"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    CAS firms that pay bills for clients face business email compromise, spoofed invoices and
    deepfake impersonation. Most organizations do not yet use AI against payments fraud.
  solution: >-
    AI screens payment requests and vendor changes for fraud signals before release, with treasury
    or finance staff investigating alerts.
  outcomes:
    - lever: risk
      description: "Organizations using AI for fraud mitigation reported efficiency and detection benefits. Few use it."
      figure: "17% use AI; among users, 49% faster reporting, 45% better deepfake detection, 43% real-time identification"
      measures: "Share of surveyed organizations that leverage AI to combat payments fraud (17%); among those using AI, share reporting enhanced efficiency in fraud reporting (49%), improved detection of deepfake technology (45%) and real-time identification (43%). AFP 2026 Payments Fraud and Control Survey (465 respondents per search coverage; the press release was read, the respondent count was not)."
      provenance: independent
      source_ref: AFP-PAYFRAUD-2026
  prerequisites:
    - "Payment data and vendor master data access; callback and dual-approval controls"
  risks_and_guardrails:
    - "74% of organizations were affected by business email compromise in 2025 (AFP-PAYFRAUD-2026)."
    - "Respondents cited cost, perceived immaturity of the technology and reliance on existing controls or partners as reasons for slow AI adoption (AFP-PAYFRAUD-2026)."
  human_checkpoints:
    - "Treasury or finance staff investigate and release or block flagged payments"
  role_evolution: >-
    Treasury was the department most likely to discover attempted fraud (83%) and actual fraud
    (55%) in the survey (AFP-PAYFRAUD-2026).
  evidence_grade: C
  sources:
    - { ref: AFP-PAYFRAUD-2026, title: "Over 75% of US Firms Experienced Payments Fraud in 2025, While AI Adoption for Fraud Mitigation Lags", publisher: "Association for Financial Professionals (survey underwritten by Truist)", type: survey, url: "https://www.financialprofessionals.org/about/learn-more/press-releases/Details/over-75-percent-of-us-firms-experienced-payments-fraud-in-2025-while-ai-adoption-for-fraud-mitigation-lags", date: "2026-04-14", access: full, locator: "key findings list" }
  last_reviewed: 2026-10-20
  notes: >-
    Adjacent process: a survey of treasury and finance teams, not of CAS providers. No CAS firm
    reports AI payment screening. Grade C (survey figures, no named deployment).

- id: advisory-client-accounting-services-16
  title: "Independence screening before selling AI-enabled nonattest services to attest clients"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: intake-triage
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Firms that audit some clients and also provide CAS-style or AI-related nonattest services must
    decide which services can be provided to attest clients without impairing independence.
  solution: >-
    Before offering AI-enabled services (including developing or hosting an AI system) to an attest
    client, the firm applies the Code's nonattest and information-system rules, and where the Code
    is silent, the conceptual framework (identify threats, evaluate significance, apply safeguards,
    document).
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "No measurements; the AICPA article states the requirement."
      provenance: self-reported
      source_ref: JOFA-ETHICS-2026
  prerequisites:
    - "Client list with attest status"
    - "Ethics review step in the sales process"
  risks_and_guardrails:
    - "The AICPA says AI-related nonattest services for an attest client, such as developing or hosting an AI system, can raise independence concerns (JOFA-ETHICS-2026, independence section)."
    - "Background not verified in this run: bookkeeping and payroll are among the most common nonattest services addressed by the Code's nonattest interpretation. The Code text (ET 1.295) could not be opened; a search-result summary of a 2014 state board newsletter was the only support."
  human_checkpoints:
    - "Ethics or independence partner review before engagement acceptance"
  role_evolution: "Not addressed by the sources."
  evidence_grade: D
  sources:
    - { ref: JOFA-ETHICS-2026, title: "Accounting ethics in the age of AI", publisher: "Journal of Accountancy (AICPA Professional Ethics Division)", type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/", date: "2026-08-05", access: full, locator: "section on independence concerns for attest clients" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea (grade D); a compliance step, not a measured practice. This is the independence flag for
    the module: CAS bookkeeping for a firm's own attest clients is the restricted case, and the
    firm-structure side (alternative practice structures) is routed to professional-services.

- id: advisory-client-accounting-services-17
  title: "Bringing AI tools into the firm's quality management system (SQMS No. 1) for compilation and review work"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Firms with compilation and review practices must operate a system of quality management. An AI
    tool used in those engagements becomes a firm resource that needs evaluation and monitoring.
  solution: >-
    AI review expectations are integrated into the firm's quality control system, including use
    documentation, rather than run as a separate informal process.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "No data."
      provenance: self-reported
      source_ref: HEPLER-CPALIAB-2026
  prerequisites:
    - "An SQMS No. 1 quality management system in place (effective 2025-12-15)"
  risks_and_guardrails:
    - "SQMS No. 1 has an effective date of December 15, 2025, and a CPA firm's accounting and auditing practice includes audit, attestation, review and compilation services, per a firm's blog summarising the AICPA (LINFORD-SQMS-2024). The standard's text on technology resources was not opened."
    - "A June 2026 liability white paper lists due care, competence, confidentiality and quality management as the standards implicated by AI use, and warns that firms may be faulted for overreliance on AI output or improper data handling (HEPLER-CPALIAB-2026)."
  human_checkpoints:
    - "Quality management monitoring and evaluation of AI tools"
  role_evolution: "Not addressed by the sources."
  evidence_grade: D
  sources:
    - { ref: LINFORD-SQMS-2024, title: "AICPA Quality Management Standard (SQMS) No. 1 (and why you should care)", publisher: "Linford and Company", type: firm, url: "https://linfordco.com/blog/aicpa-quality-management-standards-sqms-1/", date: "2024-09-25", access: full, locator: "opening paragraphs" }
    - { ref: HEPLER-CPALIAB-2026, title: "Professional Liability Risks for CPA Firms in 2026", publisher: "Hepler Broom (author G. E. Davis)", type: firm, url: "https://heplerbroom.com/wp-content/uploads/2026/06/accounting-malpractice-white-paper-8JY697202.pdf", date: "2026-06", access: full, locator: "Generative AI Risks and Governance sections" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea (grade D). Applies to a CAS firm only for engagements within SQMS scope (compilations,
    reviews, attest); plain bookkeeping is not an attest engagement. The Hepler Broom white paper is
    a law firm's risk commentary. The month for its publication is taken from its URL path.

- id: advisory-client-accounting-services-18
  title: "Cross-border and offshore data controls for AI-assisted delivery teams"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [coordination-scheduling, review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    CAS delivery often uses remote, hybrid and offshore teams, and AI tools add another place where
    client data can travel outside the US or to a related firm.
  solution: >-
    The firm applies the disclosure and consent rules for return information that leaves the US or
    goes to a related firm, and checks AI tools' data location and access as part of vendor and
    team controls.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "No data."
      provenance: self-reported
      source_ref: TAXADV-7216-2026
  prerequisites:
    - "Inventory of where client data is processed and by whom"
  risks_and_guardrails:
    - "Sharing return information among US employees within a firm needs no consent, but disclosing it outside the US or to a related firm needs proper client consent. Specific wording applies to transfers outside the US (TAXADV-7216-2026, citing Rev. Proc. 2013-14 section 5.04(e))."
    - "ENGAGE 2026 included a session on technology strategies for remote, hybrid and offshore teams (KARBON-ENGAGE-2026). The session content was not retrievable."
  human_checkpoints:
    - "Consent captured before return information leaves the US or goes to a related entity"
  role_evolution: "Not addressed by the sources."
  evidence_grade: D
  sources:
    - { ref: TAXADV-7216-2026, title: "Tax ethics and risk management: common questions and answers, part 1", publisher: "The Tax Adviser (AICPA)", type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/tax-ethics-and-risk-management-common-questions-and-answers-part-1/", date: "2026-08-31", access: full, locator: "Sec. 7216 section" }
    - { ref: KARBON-ENGAGE-2026, title: "AICPA and CIMA ENGAGE 2026: curated session list", publisher: "Karbon Magazine", type: conference, url: "https://karbonhq.com/resources/aicpa-cima-engage-2026/", date: "2026-05-21", access: full, locator: "session listing for the distributed firm (event held 2026-06-08 to 2026-06-11)" }
  last_reviewed: 2026-10-20
  notes: >-
    Idea (grade D). The 7216 rules cover tax return information only. The link to AI-specific
    offshore controls is the module author's synthesis of two sources, not a statement either
    source makes, so treat the use case as a question to test, not a finding.

- id: advisory-client-accounting-services-19
  title: "Meeting client-imposed AI policies that flow down to outsourced service providers"
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [coordination-scheduling, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Enterprise clients are writing AI terms into service-provider contracts, covering direct and
    indirect AI use, data, subcontractors and ownership of AI-generated work.
  solution: >-
    The provider maintains an AI governance programme and accepts contract limits. One published
    example from Zuellig Pharma bars use of the client's data to train, fine-tune, benchmark or test
    any AI or ML system without written consent, and requires an AI governance programme with human
    oversight, risk assessment, explainability, bias mitigation and model monitoring. It extends
    these obligations to subcontractors.
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "A policy document; no outcome data."
      provenance: self-reported
      source_ref: ZUELLIG-AIPOLICY-2026
  prerequisites:
    - "An AI governance programme that can be evidenced to the client"
    - "Flow-down of obligations to subcontractors, including offshore delivery partners"
  risks_and_guardrails:
    - "The policy treats indirect AI use (for example internal coding or data processing) as in scope, and AI-generated deliverables as work for hire vesting in the client (ZUELLIG-AIPOLICY-2026, sections 1 and 3)."
  human_checkpoints:
    - "Client written consent before any AI use of client data beyond service delivery"
  role_evolution: "Not addressed by the source."
  evidence_grade: B
  sources:
    - { ref: ZUELLIG-AIPOLICY-2026, title: "AI Policy for Service Providers/Consultants (version 2025.12.15)", publisher: "Zuellig Pharma", type: firm, url: "https://edge.sitecorecloud.io/zuelligphar3c90-zpcms-prod-4532/media/Project/Corporate/Policy/Zuellig-Pharma--AI-Policy-for-Service-Providers-Consultants---25022026.pdf", date: "2026-02", access: full, locator: "sections 1 and 3" }
  last_reviewed: 2026-10-20
  notes: >-
    The policy is real and in the client's name, but Zuellig Pharma is a large healthcare
    distributor, not a CAS customer, and nothing links the policy to accounting providers. It is an
    adjacent example of the contract terms private middle-market CAS clients with enterprise
    parents or lenders may start to send. The date is taken from the file name (25 Feb 2026); the
    policy's own version tag is 2025-12-15. No source found shows a CAS firm responding to such terms.
```

---

## 3. Module notes

### Processes and key steps (with work types)

- Bookkeeping and transaction processing: bank and card feeds, classification, coding, payables and receivables. `transaction-processing`.
- Reconciliations and monthly close: account reconciliation, accruals, variance review, financial statement package. `transaction-processing`, `data-reporting`, `review-assurance`.
- Controllership and fractional CFO: client dashboards, KPI and variance commentary, forecasting and cash flow, advice. `data-reporting`, `document-production`, `expert-judgment`, `client-interaction`.
- Payroll and bill pay: processing, payment release, vendor changes. `transaction-processing`. No AI-governance evidence found for payroll.
- Engagement set-up and governance: engagement letters, consent, tool approval, vendor due diligence, quality management. `coordination-scheduling`, `review-assurance`.
- CAS definition used in the sources: outsourced or co-sourced financial operations, from bookkeeping and payroll to CFO-level work (JOFA-CASTIPS-2025).

### Common pain points

- Manual data clean-up is the top blocker to advisory work (30% of respondents; INTUIT-ACCTTECH-2026).
- Tool sprawl: the average firm runs about 10 apps, and 41% say tools are fully integrated (INTUIT-ACCTTECH-2026).
- Use without embedding: 88% use AI for a client service but 30% say it is the default (INTUIT-ACCTTECH-2026).
- Staff pasting client data into chat tools without a firm decision on where data may go (CPAPA-SETTLE-2026, opinion).
- Vendor claims that cannot be compared or reproduced (CPAPA-AGENTSCLOSE-2026; CFOCOM-DUALENTRY-2026).

### Metrics and benchmarks (with sources and provenance)

| Metric | Source | Provenance | What it measures |
|---|---|---|---|
| Median CAS growth 17% (2024); CAS revenue projected to double over three years | JOFA-CASTIPS-2025 | professional body (survey) | 2024 CAS Benchmark Survey, 200+ respondents. 2026 report due December 2026 (CPACOM-CASBENCH-2026). |
| 98% of firms use AI; 21% have a policy or strategy; 60 min per day saved per employee | KARBON-AISTATE-2026 | vendor-published | Nearly 600 professionals; Karbon users over-represented. |
| 88% use AI for a client service; 30% embedded; 54% situational; 77% say the gap is widening | INTUIT-ACCTTECH-2026 | vendor-published | n=725 US professionals, May 2026. |
| Three in five say clients ask for proof of AI data protection; 33% proactively explain AI use; 49% explain only when asked | INTUIT-ACCTTECH-2026 | vendor-published | Same survey. |
| 16% of firms "very confident" they can adapt to AI over three years | JOFA-POLICY-2026 (cites 2025 PCPS MAP survey) | independent (underlying survey not opened) | Secondary citation. |
| 55% more weekly client support; 7.5-day shorter close; 12% more ledger granularity; about 8.5% of time reallocated | STANFORD-WP-2025 | independent | 79 SMEs on an AI-enabled platform; working-paper abstract. |
| Balances within 1% of CPA baselines early, over 15% off after several months; revenue overstated 5-30% | PENROSE-ACCTBENCH-2025 | vendor-published | One real SaaS business, one year of data, mid-2025 models. |
| Leaderboard top accuracy 91.1%; classification 94.4% against 64.4% for AR and close (as read 2026-10-20) | DUALENTRY-BENCH-2026 | vendor-published | 101 synthetic cases, eight task areas. Earlier versions reported lower top scores. |
| 76% of organizations had attempted or actual payments fraud in 2025; 74% hit by BEC; 17% use AI against it | AFP-PAYFRAUD-2026 | independent | AFP survey of treasury and finance professionals. |
| Employment of 22-25-year-olds in AI-exposed occupations 19% below a counterfactual by June 2026; accountants appear in the highest exposure quintile | BRYNJOLFSSON-CANARIES-2026 | independent | ADP payroll data; descriptive, not causal, not accountant-specific. |

- **Quality evidence, stated plainly:** there is no published error rate, override rate, parallel-run result or inspection finding for a CAS firm or CAS platform. The closest are the Choi and Xie study (independent, SME platform data, measures such as close time and ledger granularity, no overall error rate in the abstract) and the two vendor-run benchmarks.
- The IRS, FTC, AICPA and COSO sources contain no inspection or enforcement findings on AI use in CAS. No peer-review finding on AI in compilation work was found.

### Guardrails and regulatory points

- **AICPA Code:** the General Standards Rule (competence and due care) is unchanged, final work product stays with the member, and the Confidential Client Information Rule applies before client data goes into AI (JOFA-ETHICS-2026). AI-related nonattest services for attest clients can raise independence concerns (JOFA-ETHICS-2026).
- **Disclosure:** no federal law or professional standard applicable to CPAs mandates disclosure of generative AI use; California and Utah have laws requiring some disclosure; a patchwork of GLBA, state privacy laws and possibly the EU AI Act applies (JOFA-DISCLOSE-2025).
- **IRS Circular 230 and OPR Alert 2026-19 (2026-06-24):** due diligence (10.22), fees (10.27), competence (10.35), firm procedures (10.36), written advice (10.37), and 6713/7216. The alert says billing for manual time that was not spent, or double billing for AI-assisted work, may violate 10.27 depending on facts (IRS-OPR-2026).
- **Section 7216:** written consent is needed for use or disclosure of return information outside the exceptions; the last official Treasury guidance dates from 2013 (Rev. Procs. 2013-14 and 2013-19) and many modern practices are not addressed (TAXADV-7216-2026). Whether an AI tool counts as a disclosure has not been addressed by the IRS (CPAPA-SETTLE-2026).
- **FTC Safeguards Rule:** the definition covers accountants and tax preparers completing income tax returns, and requires a Qualified Individual, service-provider oversight and an annual written report (ECFR-16CFR314-2026).
- **AICPA SQMS No. 1:** effective December 15, 2025; scope includes review and compilation per a summary of AICPA wording (LINFORD-SQMS-2024).
- **COSO (Feb 2026):** eight capability types, minimum control expectations aligned to the five COSO components, illustrative metrics and starter templates; reliance on AI output requires ICFR-grade evidence (COSO-GENAI-2026, JOFA-COSO-2026).
- **AI assurance:** AICPA and AIUC announced on 2026-10-19 a joint SOC 2 plus AIUC-1 engagement, with a full launch expected in early 2027 (JOFA-AIUC-2026). Routed.
- **UK context:** ICAEW Code revisions on technology took effect 2025-07-01 and the FRC issued audit AI guidance on 2025-06-26 (KINGSLEY-FRCICAEW-2025). Neither addresses CAS directly.
- **Analog from law:** ABA Formal Opinion 512 (2024-07-29) is used by the AICPA's liability column as a model for informed consent and verification (JOFA-DISCLOSE-2025). The primary PDF could not be opened.

### Frontier signals (dated and sourced)

- 2025-08-05: first public long-horizon benchmark on real books shows compounding errors and check-bypassing behaviour (PENROSE-ACCTBENCH-2025).
- 2026-02-26: COSO guidance on internal control over generative AI reported by the Journal of Accountancy (JOFA-COSO-2026).
- 2026-04-22: a benchmark vendor's CFO says no standard exists for task-level AI accuracy in accounting (CFOCOM-DUALENTRY-2026).
- 2026-06 (JAR vol 64 issue 3): first peer-reviewed field evidence on human-AI accounting (STANFORD-JAR-2026).
- 2026-06-24: IRS OPR Alert 2026-19 (IRS-OPR-2026).
- 2026-07-27 (reported 2026-07-28): BlackLine announces general availability of close-preparation agents (CPAPA-BLACKLINE-2026).
- 2026-08: Canaries paper update reports a widening employment gap for young workers in AI-exposed occupations (BRYNJOLFSSON-CANARIES-2026).
- 2026-10-01: Journal of Accountancy features on agent guardrails and Excel agents (JOFA-CYBER-2026, JOFA-EXCEL-2026).
- 2026-10-19: AICPA and AIUC joint assurance offering; full launch expected early 2027 (JOFA-AIUC-2026).
- December 2026: the 2026 CAS Benchmark Survey report is due (CPACOM-CASBENCH-2026), the next source of hard CAS numbers.
- A headline on an opened page lists an AICPA practice aid on AI for auditors dated 2026-10-13 (seen in JOFA-ETHICS-2026 sidebar; the article itself was not opened).

### Workforce and role effects

- Study finding: accountants shift from routine data entry toward business communication and quality assurance (STANFORD-WP-2025). Seniors intervene when AI confidence drops; juniors accept uncertain output more and gain less (STANFORD-INSIGHTS-2025).
- ADP data through June 2026: employment of ages 22-25 in AI-exposed occupations is 19% below where it would be relative to less-exposed peers, operating mainly through reduced hiring. Authors call this descriptive, not causal. Accountants are in the highest exposure quintile, but the paper does not report an accountant-specific effect (BRYNJOLFSSON-CANARIES-2026, abstract and Table A.6).
- Hiring: 38% name strategic judgment as the top expertise sought, with AI fluency second at 22%; 56% say a new entry-level hire takes six months or more to reach full billable capacity (INTUIT-ACCTTECH-2026).
- A Withum managing director says he expects complete automation of the tax process (ACCTODAY-CASKEYS-2026, opinion). Karbon reports 91% of respondents believe graduates prefer firms using AI (KARBON-AISTATE-2026).

### Objections and concerns practitioners raise

- Data security and confidentiality: 84% of Intuit respondents agree strong AI data security practices are becoming a competitive advantage (INTUIT-ACCTTECH-2026), and 43% of the Choi and Xie survey respondents were concerned about data security (STANFORD-INSIGHTS-2025).
- AI-generated errors: 62% of surveyed accountants were concerned (STANFORD-INSIGHTS-2025).
- Clients may reject AI on privacy or quality grounds, and consent that is conditioned on accepting AI may not be voluntary for 7216 purposes (JOFA-DISCLOSE-2025; CPAPA-SETTLE-2026, opinion).
- Unreviewed output as a professional liability, with the Deloitte Australia fee refund over fabricated citations cited in the IRS alert and trade press (IRS-OPR-2026; CPAPA-AGENTSCLOSE-2026).
- Policy gap: standards are not AI-specific, and AI-specific SOC guidance was said to be missing as of August 2026 (CPAPA-AGENTSCLOSE-2026).
- Fee fairness: billing for time not spent (IRS-OPR-2026). Routed.

### Interview probes for an advisor

1. When your AI platform classifies or reconciles for a client, what share of items reach a person, what share do they change, and who decided that threshold? Can you show the last three months?
2. What would make you pull an agent out of a client's close, and has that ever happened? What did you track before and after go-live?
3. What do your engagement letters and onboarding say about AI today? How many clients have asked for proof of data protection, and what did you give them?
4. Which of your AI tools touch client data, what do the vendor contracts say about retention and training, and could any of them see another client's files?
5. Who reviews AI output on low-confidence items, how experienced are they, and how do you train newer staff not to accept flagged items?

---

## 4. Routed to other modules

- **Fee transparency and pricing of the firm's own AI-assisted work** (OPR 10.27 on billing for time not spent; CPA.com and Blue J survey on value-based fees in the landscape) to **professional-services** (firm operations) and **tax**. Source: IRS-OPR-2026.
- **Alternative practice structures, PE ownership and independence structure**, including who can own the firm that sells CAS to attest clients, to **professional-services**. Source context: landscape file (not re-researched).
- **Junior-talent pipeline and the Canaries employment findings** to **professional-services**. Source: BRYNJOLFSSON-CANARIES-2026.
- **AI assurance engagements (SOC 2 plus AIUC-1)** to the **assurance** archetype, and to **risk-controls** where sold to non-audit clients. Source: JOFA-AIUC-2026.
- **COSO-based controls design and AI governance advisory for clients (a firm selling this service)** to **risk-controls**. Sources: COSO-GENAI-2026, JOFA-COSO-2026.
- **Section 7216 consent mechanics, Circular 230 duties and return-preparation AI** to **tax**. Sources: IRS-OPR-2026, TAXADV-7216-2026.
- **FRC and ICAEW audit AI guidance and the Excel-agent audit demonstration** to **assurance**. Sources: KINGSLEY-FRCICAEW-2025, JOFA-EXCEL-2026 (framed for audit).
- **Payments-fraud, BEC and deepfake investigation** to **forensic-disputes** (detection and investigation) and **risk-controls** (control design). Source: AFP-PAYFRAUD-2026. The bill-pay screening control stays here (use case 15).

---

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| STANFORD-WP-2025 | Human + AI in Accounting: Early Evidence from the Field (working paper 4261) | Stanford GSB (Choi, Xie) | academic | https://www.gsb.stanford.edu/index%2ephp/faculty-research/working-papers/human-ai-accounting-early-evidence-field | 2025-05-07 | full |
| STANFORD-JAR-2026 | Human + AI in Accounting: Early Evidence from the Field (JAR 64(3)) | Stanford GSB listing | academic | https://www.gsb.stanford.edu/index%2ephp/node/629989 | 2026-06 | full (abstract) |
| STANFORD-INSIGHTS-2025 | AI Is Reshaping Accounting Jobs by Doing the Boring Stuff | Stanford GSB | academic | https://www.gsb.stanford.edu/insights/ai-reshaping-accounting-jobs-doing-boring-stuff | 2025-06-26 | full |
| BRYNJOLFSSON-CANARIES-2026 | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI | Brynjolfsson, Chandar, Chen (Stanford and NBER) | academic | https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf | 2026-08 | full |
| NBER-GENAIWORK-2023 | Generative AI at Work (NBER WP 31161; QJE 140(2), 2025) | NBER | academic | https://www.nber.org/papers/w31161 | 2023 | full (abstract) |
| PENROSE-ACCTBENCH-2025 | Can LLMs Do Accounting? AccountingBench | Penrose | vendor | https://accounting.penrose.com/ | 2025-08-05 | full (mirror) |
| DUALENTRY-BENCH-2026 | Accounting AI Benchmark 2026 (leaderboard) | DualEntry | vendor | https://dualentry.com/accounting-ai-benchmark | 2026-02-20 | full |
| DUALENTRY-BLOG-2026 | AI Still Fails One-Third of Real Accounting Tasks (66.0% top score version) | DualEntry | vendor | https://www.dualentry.com/blog/ai-still-fails-one-third-of-real-accounting-tasks | 2026-03-03 | full |
| CFOCOM-DUALENTRY-2026 | The best AI model still fails 1 in 5 accounting tasks | CFO.com (DualEntry CFO guest post) | press | https://www.cfo.com/news/the-best-ai-model-still-fails-1-in-5-accounting-tasks-Claude-Opus-OpenAI-GPT/818100/ | 2026-04-22 | full |
| COSO-GENAI-2026 | Achieving Effective Internal Control Over Generative AI | COSO | standard-setter | https://auditoresinternos.es/wp-content/uploads/2026/02/Achieving-Effective-Internal-Control-Over-Generative-AI_COSO_compressed.pdf | 2026-02 | full (copy hosted by a third party) |
| JOFA-COSO-2026 | COSO creates audit-ready guidance for governing generative AI | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ | 2026-02-26 | full |
| IRS-OPR-2026 | Issue 2026-19, Introductory Guidelines for Responsible AI Use in Federal Tax Practice | IRS OPR | regulator | https://www.irs.gov/pub/opr-taxpros/issue-number-2026-19-introductory-guidelines-for-responsible-ai-use-in-federal-tax-practice.pdf | 2026-06-24 | full |
| ECFR-16CFR314-2026 | 16 CFR Part 314, sections 314.2 and 314.4 (current text) | eCFR / FTC | regulator | https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314 | 2026-10-20 (access date) | full |
| JOFA-ETHICS-2026 | Accounting ethics in the age of AI | Journal of Accountancy (AICPA Ethics Division) | professional-body | https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/ | 2026-08-05 | full |
| JOFA-DISCLOSE-2025 | Should I disclose my use of gen AI to clients? | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2025/apr/should-i-disclose-my-use-of-gen-ai-to-clients/ | 2025-04-01 | full |
| JOFA-POLICY-2026 | Drafting an AI policy that actually works | Journal of Accountancy (Aon) | professional-body | https://journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works | 2026-07-01 | full |
| JOFA-CYBER-2026 | New checklist helps CPAs manage AI cyber risks | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/oct/new-checklist-helps-cpas-manage-ai-cyber-risks/ | 2026-10-01 | full |
| JOFA-EXCEL-2026 | Using an Excel agent to clean, validate, and reconcile data | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2026/oct/using-an-excel-agent-to-clean-validate-and-reconcile-data/ | 2026-10-01 | full |
| JOFA-AIUC-2026 | AICPA partners on new offering that assures AI systems and agents | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/ | 2026-10-19 | full |
| JOFA-CASTIPS-2025 | Tips for providing the CAS services clients want | Journal of Accountancy | professional-body | https://www.journalofaccountancy.com/issues/2025/jul/tips-for-providing-the-cas-services-clients-want/ | 2025-07-01 | full |
| CPACOM-CASBENCH-2026 | CAS Benchmark Survey page (2026 report due December 2026) | CPA.com and AICPA PCPS | professional-body | https://cpa.com/cas-benchmark-survey | 2026 | full |
| TAXADV-7216-2026 | Tax ethics and risk management: common questions and answers, part 1 | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/issues/2026/aug/tax-ethics-and-risk-management-common-questions-and-answers-part-1/ | 2026-08-31 | full |
| ABA-FO512-2024 | Formal Opinion 512, Generative Artificial Intelligence Tools | American Bar Association | professional-body | https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf | 2024-07-29 | search-only (PDF blocked; known through JOFA-DISCLOSE-2025 and IRS-OPR-2026) |
| CPAPA-AGENTSCLOSE-2026 | Before You Let the Agents Run the Close: Five Controls to Put in Writing First | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/ | 2026-08-13 | full |
| CPAPA-SETTLE-2026 | What to Settle Before Client Tax Data Touches AI | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=191491 | 2026-10-12 | full |
| CPAPA-BLACKLINE-2026 | BlackLine Introduces Multi-Agent AI System Verity Prepare | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/07/28/blackline-introduces-multi-agent-ai-system-verity-prepare/187516/ | 2026-07-28 | full |
| ACCTODAY-CASKEYS-2026 | CAS Delivers the Keys to the Kingdom | Accounting Today | press | https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom | 2026-05-22 | full |
| INTUIT-ACCTTECH-2026 | The 2026 Accountant Technology Survey | CPA Practice Advisor (Intuit QuickBooks survey) | survey | https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807 | 2026-07-02 | full |
| KARBON-AISTATE-2026 | Karbon State of AI in Accounting 2026 Report | Karbon Magazine | survey | https://karbonhq.com/resources/state-of-ai-accounting-2026 | 2026-01-20 | full |
| AFP-PAYFRAUD-2026 | Over 75% of US Firms Experienced Payments Fraud in 2025 | AFP | survey | https://www.financialprofessionals.org/about/learn-more/press-releases/Details/over-75-percent-of-us-firms-experienced-payments-fraud-in-2025-while-ai-adoption-for-fraud-mitigation-lags | 2026-04-14 | full |
| KARBON-ENGAGE-2026 | AICPA and CIMA ENGAGE 2026: curated session list | Karbon Magazine | conference | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | 2026-05-21 (event 2026-06-08 to 2026-06-11) | full |
| WOODARD-ENGLETTERS-2025 | Future Ready Engagement Letters (webinar deck) | Woodard | firm | https://www.woodard.com/hubfs/Future_Ready_Engagement_Letters_Oct2025.pdf | 2025-10 | full |
| HEPLER-CPALIAB-2026 | Professional Liability Risks for CPA Firms in 2026 | Hepler Broom | firm | https://heplerbroom.com/wp-content/uploads/2026/06/accounting-malpractice-white-paper-8JY697202.pdf | 2026-06 | full |
| LINFORD-SQMS-2024 | AICPA Quality Management Standard (SQMS) No. 1 | Linford and Company | firm | https://linfordco.com/blog/aicpa-quality-management-standards-sqms-1/ | 2024-09-25 | full |
| KINGSLEY-FRCICAEW-2025 | Tech-driven, ethically bound: new FRC and ICAEW guidance on AI | Kingsley Napley | firm | https://www.kingsleynapley.co.uk/insights/blogs/regulatory-blog/tech-driven-ethically-bound-new-frc-and-icaew-guidance-on-ai-use-in-the-accountancy-sector | 2025-07-24 | full |
| ZUELLIG-AIPOLICY-2026 | AI Policy for Service Providers/Consultants | Zuellig Pharma | firm | https://edge.sitecorecloud.io/zuelligphar3c90-zpcms-prod-4532/media/Project/Corporate/Policy/Zuellig-Pharma--AI-Policy-for-Service-Providers-Consultants---25022026.pdf | 2026-02 | full |

**Counts by type (36 sources).** Academic 5; regulator 2; standard-setter 1; professional-body 11 (including ABA 512, search-only); firm 5; vendor 3; press 5; survey 3; conference 1; podcast 0; community 0; job-posting 0. Of the 36, 35 were opened and read, and 1 (ABA-FO512-2024) is search-only. Several sources are vendor-sponsored or contributor opinion pieces, and the table above says which.

---

## 6. Gaps

- **No quality measurements for CAS.** No published error rate, override or review rate, parallel-run result, restatement rate, peer-review or inspection finding for any CAS firm or CAS AI platform. A search for firm-level measured categorization accuracy returned only vendor claims (roughly 77% to 98%, different definitions) and practitioner forum anecdotes, which were not used.
- **Choi and Xie full text.** The Wiley JAR page was blocked, so the journal version's tables, the platform's identity and the experiment details were not read. Only the working-paper abstract (May 2025), the JAR abstract and a Stanford summary were.
- **ABA Formal Opinion 512 primary text** (americanbar.org returned 403 directly and through the mirror). SRA (UK solicitors) and the UK Management Consultancies Association (MCA) were not researched: they govern legal practice and consultancies, not accounting services, and no accounting-service guidance from either was located. State bar opinions were not researched for the same reason.
- **AICPA primary pages** blocked or script-rendered: the Code text (ET 1.295 nonattest services and the bookkeeping interpretation), "AI Through an Ethics Lens", the AICPA generative AI landing page, and the AICPA practice aid on AI for auditors (October 2026). The independence background for bookkeeping to attest clients is therefore unverified in this run.
- **SQMS No. 1 text** and its treatment of technology resources were not opened; only a firm's summary was.
- **State law:** the Colorado AI Act's status after 30 June 2026 was not resolved (searches returned only 2025 coverage), and the California and Utah disclosure laws were cited only through the Journal of Accountancy. Whether any of these apply to CAS (as against consumer-facing consequential decisions) was not assessed.
- **Client AI terms:** one named client policy (Zuellig Pharma) found; no CAS-specific client AI terms, lender requirements or insurer questionnaires. Professional liability insurance exclusions for AI: search results covered law firms and general commercial lines, and none named CPA firms, so nothing is claimed.
- **Vendor terms:** Intuit, Xero and Sage AI data terms were not read. An Intuit fact sheet with AI categorization figures (400M transactions with AI-recommended categorization) is undated and was not used.
- **Job postings:** the postings surfaced in search either no longer existed or had no usable text, so there is no job-posting evidence on AI governance roles in CAS.
- **Podcasts, communities and conference proceedings:** no recordings or proceedings were reachable. ENGAGE session descriptions were read, but not the sessions. The Digital CPA 2026 agenda (December 6-9, 2026) is not yet available, and the 2026 CAS Benchmark report is due in December.
- **Payroll** and **fractional CFO**: no AI-governance evidence found for either.
- **NBER:** no NBER working paper on AI in bookkeeping or CAS was found. The NBER item used is adjacent (customer support, 2023).
- **Date conflicts:** DualEntry's benchmark reports different top scores in different versions (66.0%, 77.3%/79.2%, and 91.1% on the page as read); none is treated as a stable benchmark figure.
