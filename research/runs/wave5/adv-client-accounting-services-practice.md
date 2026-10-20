# Client accounting services: practice angle (advisory archetype)

Run date: 2026-10-20. Wave 5. Archetype `advisory`, module `client-accounting-services`, angle `practice`.

## 1. Summary

**Evidence base.** I opened 62 distinct sources across eight source types (press, vendor, job-posting, academic, professional-body, survey, firm, regulator) and saw 2 more only in search results. Most named deployments are vendor-published case studies from small and solo firms, vendor product launches, and trade-press interviews with Top 100 firm leaders. No source gave production override rates, error rates found in review, or parallel-run results from a CAS firm.

**Use cases by evidence grade (17).** A: 1. B: 10. C: 5. D: 1.

**What the evidence says.**

1. **Categorization and close timing have the only independent measurement.** A peer-reviewed study (Journal of Accounting Research, June 2026) of an unnamed AI-enabled accounting platform used by 79 small and midsize enterprises found genAI use associated with earlier monthly close and more granular ledgers, and found that senior accountants step in when AI confidence is low while junior staff tend to accept uncertain suggestions (STANFORD-JAR-2026; STANFORD-GSBINSIGHT-2025; MITSLOAN-CHOIXIE-2025). The study is an association and the platform is not named.
2. **Quality depends on context, and the best numbers are vendor-run.** In a Digits benchmark of 2,000 transactions, outsourced accountants seeing the books for the first time scored 79.1%, the best general model alone 79.5%, the best agent with ledger look-up 88.9%, and Digits' own ledger-native model 97.8% (DIGITS-BENCH-2026). DualEntry's separate test put the best of 19 general models at 77.3% across 101 accounting workflows (ACCTODAY-DUALENTRY-2026). Both are vendor tests.
3. **The delivery model is moving from software that helps staff to agents that prepare the close.** Pilot launched an autonomous AI Accountant on 4 Feb 2026 and Meridian for firms on 16 Jun 2026; Accrual bought Puzzle's firm technology on 2 Sep 2026; CLA announced a firm-trained model with Digits on 21 Jul 2026 (CPAPA-PILOT-2026; ACCTODAY-MERIDIAN-2026; ACCTODAY-ACCRUAL-2026; ACCTODAY-CLA-2026). Named customer firms and outcome data for these platforms were not found.
4. **Vendor fragility is a documented risk.** Botkeeper announced closure on 9 Feb 2026 and its Infinite platform was bought by Xendoo (CPAPA-XENDOO-2026; UKU-BOTKEEPER-2026).
5. **Controls are lagging the tools.** Practitioners recommend an agent inventory, replayable evidence, risk-scaled sign-off, SOC mapping and exit thresholds before agents touch a production close (CPAPA-AGENTSCLOSE-2026); Digits shipped locked-period review queues for agent writes on 13 Oct 2026 (DIGITS-WRITEMCP-2026).

**Independence.** Bookkeeping and preparing accounting records are barred for SEC-registrant audit clients under 17 CFR 210.2-01(c)(4)(i) (SEC-REG210-2026). The CAS clients described in the sources are mostly small and midsize private businesses; the AICPA and IESBA treatment for private audit clients was not checked in this run.

## 2. Use cases

```yaml
- id: advisory-client-accounting-services-01
  title: AI transaction categorization with confidence-based accountant review (outsourced bookkeeping)
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Coding bank and card transactions is the largest manual step in CAS bookkeeping, it is repeated every month for every client, and it sets the quality of every later report.
  solution: A model proposes the account for each transaction and attaches a confidence score. Accountants review low-confidence items and edit in bulk. Ledger-native models learn each client's own booking conventions instead of relying on a general model's accounting knowledge.
  outcomes:
  - lever: capacity
    description: Share of accountant time moved away from routine data entry (independent academic study of an AI-enabled accounting platform used by 79 small and midsize enterprises; platform not named)
    figure: approximately 8.5%
    measures: reallocation of approximately 8.5% of accountant time from routine data entry toward high-value tasks such as business communication and quality assurance (MIT Sloan's wording of the study)
    provenance: independent
    source_ref: MITSLOAN-CHOIXIE-2025
  - lever: speed
    description: Monthly statements finalized earlier by accountants using AI (reported as an association in the paper's abstract, not a proven cause)
    figure: 7.5 days
    measures: days faster to finalize monthly statements for accountants using AI than for those using traditional methods (Stanford GSB summary of the study)
    provenance: independent
    source_ref: STANFORD-GSBINSIGHT-2025
  - lever: quality
    description: More granular reporting among firms using generative AI
    figure: 12%
    measures: 'rise in reporting granularity: finer expense categories, for example bonuses, benefits or meals instead of a broad payroll line (Stanford GSB summary of the study)'
    provenance: independent
    source_ref: STANFORD-GSBINSIGHT-2025
  - lever: quality
    description: 'Vendor-run categorization benchmark: ledger-native model against outsourced accountants and general models'
    figure: 97.8% vs 79.1%
    measures: share of 2,000 transactions from four small businesses that use Digits classified correctly against categories reviewed by US accountants applying GAAP. Digits' own ledger-native model 97.8%; 12 outsourced accountants seeing the books for the first time 79.1%; best general-purpose model working alone 79.5%; best agent with ledger look-up 88.9%
    provenance: vendor-published
    source_ref: DIGITS-BENCH-2026
  - lever: quality
    description: Vendor-run test of 19 general-purpose models on 101 accounting workflows (accuracy ceiling for general models)
    figure: 77.3% best
    measures: highest accuracy of 19 general models on 101 workflow questions graded deterministically (DualEntry); one engineer reports a model can reach 92% on classification yet 30-40% on journal entry creation
    provenance: vendor-published
    source_ref: ACCTODAY-DUALENTRY-2026
  - lever: capacity
    description: Small CAS firm's own estimate of auto-categorized share after about nine months on an AI-native ledger
    figure: about 90%
    measures: share of transactions auto-categorized across migrated clients, as estimated by the firm's co-owner; no tracked metric shown
    provenance: vendor-published
    source_ref: DIGITS-LINCOLN-2026
  prerequisites:
  - Bank and card feeds connected to the ledger, and a chart of accounts that reflects the client's own conventions
  - 'Access to the client''s booking history: the best agent in the Digits benchmark gained about 10 points over its one-shot score by looking up past bookings (DIGITS-BENCH-2026)'
  - Reviewer time reserved for low-confidence and recurring-merchant exceptions
  risks_and_guardrails:
  - Junior accountants tended to accept AI suggestions even when the system flagged them as uncertain, while senior accountants intervened (STANFORD-GSBINSIGHT-2025)
  - A framed experiment in the study found AI assistance improved classification accuracy on average, but reliance on non-consensus AI recommendations can increase the risk of error (STANFORD-JAR-2026)
  - 'General-purpose models plateaued: the seven best one-shot configurations were within 0.4 points of each other and the best was 1.2 points below the earlier revision (DIGITS-BENCH-2026)'
  - A small firm reported that a built-in categorization feature began mis-suggesting transactions it had previously coded correctly, creating rework (DIGITS-LINCOLN-2026)
  - In the survey behind the study, 62% of accountants worried about errors in AI-generated reporting (MITSLOAN-CHOIXIE-2025)
  human_checkpoints:
  - Accountant reviews low-confidence transactions
  - Month-end review and sign-off before reports go to the client
  role_evolution: Accountants spend less time on line-by-line coding and more on quality assurance and client communication, and more experienced accountants gain more from the tool (MITSLOAN-CHOIXIE-2025; STANFORD-GSBINSIGHT-2025).
  evidence_grade: A
  sources:
  - ref: STANFORD-JAR-2026
    title: 'Human + AI in Accounting: Early Evidence from the Field (Choi, Xie), Journal of Accounting Research 64(3), pp 1333-1373'
    publisher: Stanford Graduate School of Business (publication listing with abstract)
    type: academic
    url: https://www.gsb.stanford.edu/index.php/node/629989
    date: 2026-06
    access: full
    locator: abstract (survey of 277 accountants; field data on 79 SMEs, 200,000+ transaction records; confidence-score and framed-experiment findings)
  - ref: MITSLOAN-CHOIXIE-2025
    title: How generative AI can make accountants more productive
    publisher: MIT Sloan Ideas Made to Matter
    type: academic
    url: https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-can-make-accountants-more-productive
    date: '2025-08-05'
    access: full
    locator: paragraphs on 8.5% time reallocation, confidence scores and the 62% concern figure
  - ref: STANFORD-GSBINSIGHT-2025
    title: AI Is Reshaping Accounting Jobs by Doing the 'Boring' Stuff
    publisher: Stanford Graduate School of Business Insights
    type: academic
    url: https://gsb.stanford.edu/insights/ai-reshaping-accounting-jobs-doing-boring-stuff
    date: '2025-06-09'
    access: full
    locator: paragraphs on 7.5 days faster, 12% granularity, senior versus junior behaviour
  - ref: DIGITS-BENCH-2026
    title: 'Breaking: AI Can''t Close Your Books From the Outside (Yes, Including Jev)'
    publisher: Digits
    type: vendor
    url: https://digits.com/blog/ai-cant-close-books-from-outside/
    date: '2026-10-07'
    access: full
    locator: sections 'Digits AGL classified 97.8%', 'best model working alone', 'It misses house rules'
  - ref: ACCTODAY-AIBEATS-2026
    title: AI beats human accountants at monthly close, transaction categorization
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization
    date: '2026-10-16'
    access: full
    locator: 'Digits experiment paragraphs: 12 outsourced accountants in three-person teams, majority vote, 4 hours 43 minutes per 500 transactions'
  - ref: ACCTODAY-DUALENTRY-2026
    title: Generalist AI model accuracy tops out at 77% for accounting
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/generalist-ai-model-accuracy-tops-out-at-77-for-accounting
    date: '2026-03-17'
    access: full
    locator: paragraphs on 19 models, 101 workflows, 77.3%, and the classification versus journal-entry split
  - ref: DIGITS-LINCOLN-2026
    title: How Lincoln Accounting Reclaimed 30+ Hours a Month by Switching to Digits
    publisher: Digits (case study)
    type: vendor
    url: https://digits.com/case-studies/lincoln-accounting/
    date: '2026-09-02'
    access: full
    locator: paragraphs on QuickBooks AI categorization rework and the roughly 90% auto-categorized estimate
  last_reviewed: '2026-10-20'
  notes: 'Firm type: the independent study covers an unnamed AI-enabled platform and unnamed small and midsize enterprises; the Digits benchmark is a vendor (AI-native ledger) test; Lincoln Accounting is a small two-partner firm. Grade A rests on the independent study plus the vendor benchmark; the platform in the study is not named and the study is an association, so treat A as the strongest evidence in this module, not as proof of cause. Digits'' human baseline had no client history or ability to ask questions, which its own report flags. Botkeeper''s chief executive wrote that its platform coded 80%+ of transactions at 98% accuracy (CPAPA-XENDOO-2026), but the company announced its closure on 9 Feb 2026 and its Infinite platform was bought by Xendoo (announced 3 Mar 2026 per UKU-BOTKEEPER-2026); the accuracy figure is a company claim. Independence: bookkeeping and preparing accounting records for an audit client is barred under SEC Rule 2-01(c)(4)(i) when the audit client is an SEC registrant (confirmed in eCFR, SEC-REG210-2026). Treatment for private audit clients under the AICPA and IESBA codes was not checked in this run, so confirm before a firm offers this service to its own attest clients.'
- id: advisory-client-accounting-services-02
  title: AI bank and cash reconciliation with an exceptions queue and natural-language matching rules
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - review-assurance
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Reconciling bank, card and clearing accounts means exporting statements, maintaining fragile matching rules and hunting mismatches, and unreconciled legacy balances make cleanups unprofitable to offer.
  solution: Matching software ingests statements or feeds, matches transactions without hand-built rules, finalizes clean reconciliations and presents a short prioritized exceptions list. Staff describe matching logic in natural language for high-volume clearing accounts.
  outcomes:
  - lever: speed
    description: Cash match rate at an in-house finance team that piloted a cash-matching product (enterprise, not a CAS firm)
    figure: 30% to more than 90%
    measures: match rate of bank transactions against ledger entries at Brex before and after the pilot, as stated in Numeric's funding announcement
    provenance: vendor-published
    source_ref: CPAPA-NUMERIC-2025
  - lever: speed
    description: Time on specific project bank reconciliations at an anonymised Top 100 firm's CAS practice
    figure: 37.5% (8 hours to 5 hours)
    measures: reduction in monthly labor on specific bank reconciliations; the case study says saving up to three hours every month
    provenance: vendor-published
    source_ref: FLOQAST-CASCASE-2026
  - lever: capacity
    description: One clearing-account cleanup
    figure: 10,000+ rows in minutes
    measures: rows pulled from a clearing account and matched by AI Transaction Matching in one project, per the CAS manager quoted; a client with seven years of unreconciled data asked for a recurring quarterly engagement
    provenance: vendor-published
    source_ref: FLOQAST-CASCASE-2026
  - lever: capacity
    description: 'Foundation (May 2024, robotic process automation, not generative AI): a Top 25 firm''s digital worker replaced a client''s reconciliation work'
    figure: 15 hours a week; 500 hours a year
    measures: client spent 15 hours a week reconciling funds across 70 entities before the digital worker; a second worker covering 100+ investment statements (50 hours a month) saves about 500 hours a year, as stated by the firm's AI partner
    provenance: self-reported
    source_ref: ACCTODAY-USECASE-2024
  prerequisites:
  - ERP connectors that work across the client mix (the FloQast case firm abandoned an earlier tool after connectors failed, and its clients use QuickBooks Online, Sage Intacct and Xero)
  - Standard work papers and one reconciliation procedure per balance-sheet account (FLOQAST-CASCASE-2026)
  risks_and_guardrails:
  - Vendor match rates are marketing figures until the client's own data reproduces them; build a validation period into the rollout and keep the results (CPAPA-AGENTSCLOSE-2026)
  - 'Statements are messy: duplicates, fees hidden in summaries and sync delays make true mismatches hard to separate from timing (DIGITS-BANKREC-2025)'
  human_checkpoints:
  - Accountant clears the exceptions list
  - Job manager reviews and signs off the reconciliation checklist
  role_evolution: Staff move from ticking and tying to reviewing exceptions and consulting; one Digits customer says the role is 'flipped' to reviewing a clean set of exceptions (DIGITS-BANKREC-2025; FLOQAST-CASCASE-2026).
  evidence_grade: B
  sources:
  - ref: FLOQAST-CASCASE-2026
    title: How One CAS Practice Uses FloQast AI Transaction Matching to Scale Client Support (case study PDF; file name FloQast_MillerCooper_CAS_Case_Study_August_2026)
    publisher: FloQast
    type: vendor
    url: https://get.floqast.com/hubfs/Assets/Case%20Studies/FloQast_MillerCooper_CAS_Case_Study_August_2026.pdf
    date: 2026-08
    access: full
    locator: Results panel; sections 'The Challenge', 'How FloQast Helps', 'The FloQast Difference'
  - ref: CPAPA-NUMERIC-2025
    title: AI Accounting Platform Numeric Raises $51M Series B
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2025/11/20/ai-accounting-platform-numeric-raises-51m-series-b/173638/
    date: '2025-11-20'
    access: full
    locator: paragraphs on cash matching and the Brex controller quote
  - ref: DIGITS-BANKREC-2025
    title: 'Always Be Closing: Introducing AI Bank Reconciliations'
    publisher: Digits
    type: vendor
    url: https://digits.com/blog/ai-bank-reconciliations/
    date: '2025-11-10'
    access: full
    locator: sections on drag-and-drop bank statement reconciliation, exception list and customer quote
  - ref: ACCTODAY-USECASE-2024
    title: Making the use case for AI in accounting
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/making-the-use-case-for-ai-in-accounting
    date: '2024-05-06'
    access: full
    locator: Armanino digital-worker paragraphs (Carmel Wynkoop, OJ Laos)
  - ref: IAB-BLACKLINE-2026
    title: BlackLine rolls out Verity Prepare AI for finance teams
    publisher: International Accounting Bulletin
    type: press
    url: https://www.internationalaccountingbulletin.com/news/blackline-rolls-out-verity-prepare-ai-for-finance-teams/
    date: '2026-07-28'
    access: full
    locator: paragraphs on Verity Prepare agents compiling a reconciliation package for human approval
  - ref: CPAPA-AGENTSCLOSE-2026
    title: 'Before You Let the Agents Run the Close: Five Controls to Put in Writing First'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/
    date: '2026-08-13'
    access: full
    locator: controls 2 and 3
  last_reviewed: '2026-10-20'
  notes: 'Firm types: FloQast case is a Top 100 firm that the text does not name (the file name indicates Miller Cooper, which the text does not confirm); Armanino is a Top 25 firm; Brex is an in-house team and an enterprise, so the Numeric figure is adjacent to CAS delivery and caps the grade at B. BlackLine says Verity Prepare reached general availability in July 2026 and early adopters saw reductions of up to 92% in manual reconciliation preparation time (BLACKLINE-Q2-2026, search-only, adopters unnamed; not used as an outcome). Independence: bookkeeping and preparing accounting records for an audit client is barred under SEC Rule 2-01(c)(4)(i) when the audit client is an SEC registrant (confirmed in eCFR, SEC-REG210-2026). Treatment for private audit clients under the AICPA and IESBA codes was not checked in this run, so confirm before a firm offers this service to its own attest clients.'
- id: advisory-client-accounting-services-03
  title: Agent-run month-end close preparation across a firm's client portfolio, with accountants reviewing finished books
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  - review-assurance
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: 'CAS capacity is capped by headcount: each close needs categorization, reconciliation, exception handling and statement preparation per client, so firms turn away or under-serve clients.'
  solution: 'An agent platform sits on the firm''s existing ledgers and prepares the close for every client: categorization, reconciliation, exception handling and statements. Accountants open finished books, review the reasoning behind each judgment call and sign off before anything reaches the client.'
  outcomes:
  - lever: capacity
    description: Months of books closed on the platform that underlies Pilot's Meridian (company statement in a job posting)
    figure: 199,000 months across more than 8,000 businesses
    measures: months of books closed on the platform Pilot has run in production since 2017; the posting does not separate AI-prepared from human-prepared months
    provenance: vendor-published
    source_ref: PILOT-JOBS-2026
  - lever: capacity
    description: Average time savings reported by firms using Basis agents (company statement; undated page)
    figure: 30%
    measures: time savings on average, as stated by Basis and OpenAI; no baseline, sample or measurement method given
    provenance: vendor-published
    source_ref: OPENAI-BASIS-2026
  - lever: speed
    description: Staff accountant at an AI-native practice running two clients' quarterly closes through an assistant on a ledger connector
    figure: about 7 hours by hand vs 1 hour 40 minutes
    measures: one accountant's account of two Q3 closes for two clients (one SaaS, one e-commerce); recollection, not a tracked metric
    provenance: vendor-published
    source_ref: DIGITS-WRITEMCP-2026
  - lever: quality
    description: 'Lab test: AI against 12 junior CPAs on four simulated month-end close scenarios'
    figure: AI 100% on each of 20 attempts; humans generally below 50%
    measures: share of 13 to 22 accountant-written rubric criteria met per task; LLM grader agreed 98% with hand grading on 8 submissions; tasks stripped client context and the ability to ask questions
    provenance: independent
    source_ref: ACCTODAY-AIBEATS-2026
  prerequisites:
  - Clean ledger access and permissions per client; Meridian is described as sitting on top of a firm's existing ledger with no migration (PILOT-JOBS-2026)
  - Firm-level preferences and client-level overrides configured before the first close (PILOT-JOBS-2026)
  - A review layer that shows what the AI did, why, and the few exceptions that need a human (PILOT-JOBS-2026)
  risks_and_guardrails:
  - No independent measurement of production close quality was found; the lab test used simulated tasks and the vendors' own figures are not independently verified (ACCTODAY-AIBEATS-2026)
  - 'Evidence that the agent can drop a correct answer: in three of four non-perfect AI-assisted sessions the AI had the correct figure at some point and it did not reach the final submission (ACCTODAY-AIBEATS-2026)'
  - Agent-written entries in a closed period need a proposal and review queue rather than a password or warning (DIGITS-WRITEMCP-2026)
  - 'Vendor viability: Botkeeper announced closure in Feb 2026 and its platform was acquired weeks later (CPAPA-XENDOO-2026; UKU-BOTKEEPER-2026)'
  human_checkpoints:
  - Accountant reviews finished books and signs off before client delivery
  - Locked-period changes go through a review queue
  role_evolution: Each accountant is expected to oversee a larger book and spend more time on advisory and client relationships; Pilot's own product posting sets success as more clients per accountant and less review time per close (PILOT-JOBS-2026). Basis hires accountants to write the procedures and skills its agents use (BASIS-JOBS-2026).
  evidence_grade: B
  sources:
  - ref: ACCTODAY-MERIDIAN-2026
    title: Pilot touts Meridian, says AI comparable to seasoned accountant
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/pilot-touts-meridian-says-ai-comparable-to-seasoned-accountant
    date: '2026-06-16'
    access: full
    locator: paragraphs on Meridian launch at Scaling New Heights, controls and validation gates, McKellar quote
  - ref: PILOT-JOBS-2026
    title: 'Pilot job postings: Solutions Engineer (Meridian); Senior Product Manager, Meridian; Sr. Software Engineer, Bookkeeping Automation'
    publisher: Pilot (Greenhouse job board)
    type: job-posting
    url: https://job-boards.greenhouse.io/pilothq/jobs/8880563002
    date: '2026-10-09'
    access: full
    locator: Solutions Engineer posting 'About Meridian' (199,000 months; 8,000 businesses); Senior Product Manager, Meridian posting 'The Role' and 'What Success Looks Like'
  - ref: OPENAI-BASIS-2026
    title: Basis scales accounting by turning OpenAI model progress into trusted agents
    publisher: OpenAI (customer story)
    type: vendor
    url: https://openai.com/index/basis
    date: '2026-10-20'
    access: full
    locator: final section 'Scaling trust, not just tasks' (30% time savings)
  - ref: BASIS-SERIESB-2026
    title: Basis Raises $100 Million to Deploy AI Agents for Accounting Firms
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/02/24/basis-raises-100-million-to-deploy-ai-agents-for-accounting-firms/178759/
    date: '2026-02-24'
    access: full
    locator: paragraphs on long-horizon agents, ~30% of top 25 firms (company claim), review of completed deliverables
  - ref: BASIS-JOBS-2026
    title: 'Basis job postings: Accounting Solutions Consultant; Member of Accounting Staff; Intelligence Architect'
    publisher: Basis (Ashby job board)
    type: job-posting
    url: https://jobs.ashbyhq.com/basis-ai/bf7e34d6-e678-491b-87ee-e7c1f3e0384f
    date: '2026-05-20'
    access: full
    locator: Member of Accounting Staff and Intelligence Architect postings
  - ref: ARCLOW-SITE-2026
    title: Arclow home page (AI-native accounting practice; page undated, date is access date)
    publisher: Arclow
    type: firm
    url: https://arclow.com
    date: '2026-10-20'
    access: full
    locator: 'hero text: AI categorises and reconciles as transactions land; a licensed CPA works the close and confirms it'
  - ref: DIGITS-WRITEMCP-2026
    title: 'Agentic Accounting With Confidence: Introducing Write MCP and Locked Period Controls'
    publisher: Digits
    type: vendor
    url: https://digits.com/blog/write-mcp/
    date: '2026-10-13'
    access: full
    locator: Arclow paragraph (about seven hours versus 1 hour 40 minutes) and Locked Periods section
  - ref: ACCTODAY-ACCRUAL-2026
    title: Accrual acquires Puzzle's tech to add to their CAS offering
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/accrual-acquires-puzzles-tech-to-add-to-their-cas-offering
    date: '2026-09-02'
    access: full
    locator: paragraphs on Puzzle's Close AI and Accrual's CAS offering in early access
  - ref: ACCTODAY-AIBEATS-2026
    title: AI beats human accountants at monthly close, transaction categorization
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization
    date: '2026-10-16'
    access: full
    locator: Mercor experiment paragraphs
  - ref: MERCOR-APEX-2026
    title: 'AI vs. Accountants: Frontier Models Outscore CPAs'
    publisher: Mercor
    type: vendor
    url: https://www.mercor.com/blog/human-baselines-for-benchmarks-ai-now-outperforms-junior-accountants/
    date: '2026-10-01'
    access: full
    locator: 'caveats: tasks tested what AI is best at; no coworkers or accumulated context'
  - ref: CPAPA-XENDOO-2026
    title: Xendoo Buys Botkeeper Infinite; AI Platform Will Remain 'Active and Supported'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/02/28/xendoo-buys-botkeeper-infinite-ai-platform-will-remain-active-and-supported/179027/
    date: '2026-02-28'
    access: full
    locator: paragraphs on Botkeeper closure and Xendoo purchase
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Pilot is an AI-native provider that also sells Meridian to firms; Arclow is an AI-native practice (a licensed CPA reviews every close per its site); Basis, Accrual and Puzzle are vendors. Named customer firms for Meridian and Basis were not found, so the grade rests on the vendors'' and Arclow''s own use. Accrual says its CAS offering built on Puzzle''s Close AI is in early access with broader availability planned by the end of 2026 (announced, not general availability). Pilot''s launch of Meridian was announced 16 Jun 2026; its blog gives ''7,000+'' businesses served while the Oct 2026 posting gives 8,000+, so the two counts differ in scope or date. Independence: bookkeeping and preparing accounting records for an audit client is barred under SEC Rule 2-01(c)(4)(i) when the audit client is an SEC registrant (confirmed in eCFR, SEC-REG210-2026). Treatment for private audit clients under the AICPA and IESBA codes was not checked in this run, so confirm before a firm offers this service to its own attest clients.'
- id: advisory-client-accounting-services-04
  title: Fully autonomous AI bookkeeping delivered direct to small businesses by an AI-native provider
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  - client-interaction
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: Small businesses and startups pay for bookkeeping that is slow, inconsistent and hard to scale with human staff, and book catch-up takes weeks.
  solution: The provider's agent onboards a business, configures the ledger, closes historical books, handles edge cases and produces statements, with a chat advisor for owner questions and a logged audit trail for every transaction and decision.
  outcomes:
  - lever: speed
    description: Provider's claim for onboarding and closing books
    figure: hours, not weeks
    measures: time for a business to be fully onboarded with books closed, as stated by Pilot's chief executive; no sample, baseline or independent test published
    provenance: vendor-published
    source_ref: CPAPA-PILOT-2026
  - lever: quality
    description: Provider's claim of operation without a person on the normal path
    figure: zero human intervention
    measures: Pilot's description of the AI Accountant running onboarding to monthly close; not independently tested in anything found
    provenance: vendor-published
    source_ref: PILOT-AIACCOUNTANT-2026
  prerequisites:
  - Operating data and process knowledge from years of human-delivered bookkeeping (Pilot says it draws on its work for over 7,000 startups and small businesses)
  - Bank, payroll and billing integrations (ACCTODAY-MERIDIAN-2026)
  risks_and_guardrails:
  - Zero-human-intervention is a company claim; general-purpose models alone reached about 79.5% on categorization and ledger-aware agents 88.9% in a vendor test, so end-to-end autonomy depends on the provider's own specialized system (DIGITS-BENCH-2026)
  - Practitioners say autonomous bookkeeping 'only works for very constrained, simpler cases' such as single-entity bookkeeping (ACCTODAY-BIGYEAR-2026)
  human_checkpoints:
  - Business owner reviews flagged items and the audit history
  - Pilot says clients can review or adjust transaction-level decisions
  role_evolution: Pilot's chief executive says that by automating repetitive work the product gives accountants more time for higher-value advisory work (CPAPA-PILOT-2026).
  evidence_grade: C
  sources:
  - ref: CPAPA-PILOT-2026
    title: Pilot Rolls Out Fully Autonomous AI Accountant
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/02/04/pilot-rolls-out-fully-autonomous-ai-accountant/177453/
    date: '2026-02-04'
    access: full
    locator: paragraphs on the AI Accountant launch of 4 Feb 2026 and McKellar quote
  - ref: PILOT-AIACCOUNTANT-2026
    title: Pilot Unveils AI Accountant
    publisher: Pilot (company blog)
    type: vendor
    url: https://pilot.com/blog/pilot-unveils-ai-accountant-a-major-leap-toward-artificial-general-intelligence-in-accounting
    date: '2026-02-04'
    access: full
    locator: 'announcement text: ''Pilot''s AI Accountant autonomously performs the full scope...''; ''Auditable and transparent'''
  - ref: PILOT-PARTNERHUB-2026
    title: What's New at Pilot - Partner Resource Hub
    publisher: Pilot
    type: vendor
    url: https://partners.pilot.com/Partner%20Hub/pages/whats-new.html
    date: 2026-04
    access: full
    locator: entries dated Feb 4, 2026 and Dec 9, 2025 (Local Partner Program)
  - ref: ACCTODAY-BIGYEAR-2026
    title: A big year for AI in accounting
    publisher: Accounting Today
    type: press
    url: https://accountingtoday.com/news/a-big-year-for-ai-in-accounting
    date: '2026-02-04'
    access: full
    locator: Ellen Choi (Edgefield Group) paragraph on constrained cases
  - ref: DIGITS-BENCH-2026
    title: 'Breaking: AI Can''t Close Your Books From the Outside (Yes, Including Jev)'
    publisher: Digits
    type: vendor
    url: https://digits.com/blog/ai-cant-close-books-from-outside/
    date: '2026-10-07'
    access: full
    locator: summary section
  last_reviewed: '2026-10-20'
  notes: 'Firm type: AI-native provider (Pilot). The announcement date is 4 Feb 2026 (CPAPA-PILOT-2026); the blog page''s metadata shows a later date that appears to be a modification. Pilot launched a Local Partner Program for independent bookkeepers and accounting firms on 9 Dec 2025 (PILOT-PARTNERHUB-2026). Graded C because the only measurements are the vendor''s own claims. Independence: bookkeeping and preparing accounting records for an audit client is barred under SEC Rule 2-01(c)(4)(i) when the audit client is an SEC registrant (confirmed in eCFR, SEC-REG210-2026). Treatment for private audit clients under the AICPA and IESBA codes was not checked in this run, so confirm before a firm offers this service to its own attest clients.'
- id: advisory-client-accounting-services-05
  title: Firm-trained proprietary AI model embedded in a Top 20 firm's client accounting and advisory service levels
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  - expert-judgment
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Most small and midsize clients cannot afford enterprise AI, and generic software with AI bolted on gives a firm no way to encode its own judgment and industry specialization.
  solution: CLA says it will use Digits' platform and model-training infrastructure and supply data from decades of its own work to shape a CLA-trained model, offered as an option within its client accounting and advisory service levels.
  outcomes:
  - lever: experience
    description: none published
    figure: none
    measures: no outcome figure published; the plan is to deploy to thousands of current and future clients over the next three years
    provenance: vendor-published
    source_ref: ACCTODAY-CLA-2026
  prerequisites:
  - An AI-native ledger platform (CLA says it chose Digits because it was built around AI from the start)
  - Firm data and professional judgment to train the model (ACCTODAY-CLA-2026)
  risks_and_guardrails:
  - Announced on 21 Jul 2026 with no deployment results; the model's quality and review model were not described in the source
  human_checkpoints:
  - Not described in the source
  role_evolution: CLA's chief outsourcing officer says the firm's value is in training the model with professional judgment, industry specialization and client experience rather than rebuilding platform technology (ACCTODAY-CLA-2026).
  evidence_grade: C
  sources:
  - ref: ACCTODAY-CLA-2026
    title: CLA working with Digits to develop proprietary AI model
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/cla-working-with-digits-to-develop-proprietary-ai-model
    date: '2026-07-21'
    access: full
    locator: paragraphs 1-4 (announcement, CAAS rollout, three-year plan, Engler quotes)
  last_reviewed: '2026-10-20'
  notes: 'Firm type: CLA is a Top 20 firm; Digits is the vendor. The article says the foundation is Digits'' Firm Model offering rolled out last year. Whether CLA also audits CAAS clients and how independence is handled was not stated. Independence: bookkeeping and preparing accounting records for an audit client is barred under SEC Rule 2-01(c)(4)(i) when the audit client is an SEC registrant (confirmed in eCFR, SEC-REG210-2026). Treatment for private audit clients under the AICPA and IESBA codes was not checked in this run, so confirm before a firm offers this service to its own attest clients.'
- id: advisory-client-accounting-services-06
  title: 'Outcome-based pricing of an AI ledger: firm pays only for clients automated at 95% or more with zero human touch'
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - coordination-scheduling
  pattern: other
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: announced
  problem: Per-seat or per-client software pricing makes firms pay for potential automation rather than hours actually removed from the CAS workflow.
  solution: Digits charges firms only for clients where the platform automated 95% or more of transactions with no human creating or editing them before close; if staff touch more than 5%, the platform is free for that client. Pricing is binary, not graduated.
  outcomes:
  - lever: cost
    description: Vendor-stated threshold for charging
    figure: 95% of transactions with zero human touch
    measures: share of a client's transactions neither created nor edited by a human accountant before the books are closed; Digits says it reached 95% accuracy across a range of businesses (no data shown)
    provenance: vendor-published
    source_ref: ACCTODAY-DIGITSPRICING-2026
  prerequisites:
  - Platform built to automate categorization and close for each client; firm must run clients through the platform
  risks_and_guardrails:
  - No named firm adopting the pricing was found; whether the 95% threshold holds across complex clients is not independently shown (the article says price varies by firm size and client complexity)
  human_checkpoints:
  - 'Not applicable: a commercial term rather than a workflow'
  role_evolution: Not described in the source.
  evidence_grade: C
  sources:
  - ref: ACCTODAY-DIGITSPRICING-2026
    title: Digits announces outcome-based pricing
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/digits-announces-outcome-based-pricing
    date: '2026-04-08'
    access: full
    locator: paragraphs 1-4
  last_reviewed: '2026-10-20'
  notes: 'Firm type: vendor (Digits) pricing to firms. This is a vendor-to-firm tool price, so it belongs to this module''s delivery stack; how firms price their own CAS to clients is routed to professional-services. A Digits blog says one firm used Claude to build close flowcharts for clients to help justify outcome-based pricing (DIGITS-WRITEMCP-2026, unnamed firm).'
- id: advisory-client-accounting-services-07
  title: AI-assisted variance explanation, live dashboards and client Q&A as the CAS advisory layer
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - data-reporting
  - client-interaction
  - document-production
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Static month-end PDFs arrive late, and building dashboards and explaining movements takes time away from advice.
  solution: Accountants use ledger-connected dashboards and an assistant to spot unusual spikes, drill into drivers, draft explanations and walk clients through live financials in meetings.
  outcomes:
  - lever: experience
    description: none measured
    figure: none
    measures: no tracked figure; the Withum leader describes real-time dashboards as differentiating and says a model could find a variance and probably explain it (statement, not a measurement)
    provenance: self-reported
    source_ref: ACCTODAY-CASKEYS-2026
  prerequisites:
  - Clean, current categorized data in the ledger
  - Dashboard and assistant connected to the ledger (for example Ask Digits)
  risks_and_guardrails:
  - An accountant must verify AI explanations in context; a Xero adviser says small business owners cannot easily verify what AI tells them (CFODIVE-XERO-2026)
  - The Withum quote on variance explanation is a prediction, not a deployed result (ACCTODAY-CASKEYS-2026)
  human_checkpoints:
  - Accountant reviews unusual items before they are shown to the client
  role_evolution: Firms describe moving from producing reports to interpreting them; a Top 50 firm leader describes CAS as the quarterback between advisory and compliance (ACCTODAY-BONADIO-2026).
  evidence_grade: B
  sources:
  - ref: ACCTODAY-CASKEYS-2026
    title: CAS delivers 'the keys to the kingdom'
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom
    date: '2026-05-22'
    access: full
    locator: section 'AI in CAS' (Bourke at Firm Growth Forum, May 2026)
  - ref: DIGITS-LINCOLN-2026
    title: How Lincoln Accounting Reclaimed 30+ Hours a Month by Switching to Digits
    publisher: Digits (case study)
    type: vendor
    url: https://digits.com/case-studies/lincoln-accounting/
    date: '2026-09-02'
    access: full
    locator: paragraphs on live reporting, drill-down and Ask Digits
  - ref: DIGITS-TFMA-2026
    title: How TFMA LLC Improved Workflow Efficiency by 70% with Digits
    publisher: Digits (case study)
    type: vendor
    url: https://digits.com/case-studies/how-tfma-llc-improved-workflow-efficiency-by-70-with-digits/
    date: '2026-04-20'
    access: full
    locator: paragraphs on screen-sharing live financials in client meetings
  - ref: ACCTODAY-BONADIO-2026
    title: CAS and outsourced accounting fuel Bonadio Group
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/cas-and-outsourced-accounting-fuel-bonadio-group
    date: '2026-07-30'
    access: full
    locator: Genovese quotes on AI in CAS (Top 50 firm)
  - ref: CFODIVE-XERO-2026
    title: 'Xero: Leaning on fractional CFOs for strategic finance'
    publisher: CFO Dive
    type: press
    url: https://www.cfodive.com/news/xero-leaning-fractional-cfos-strategic-finance/809896/
    date: '2026-01-16'
    access: full
    locator: paragraph on verifying AI output
  - ref: APRIO-JOB-2026
    title: Accounting Manager, Client Accounting & Advisory Services (Aprio, listed on Built In NYC)
    publisher: Aprio via Built In NYC
    type: job-posting
    url: https://www.builtinnyc.com/job/accounting-manager-client-accounting-advisory-services/11189037
    date: '2026-09-15'
    access: full
    locator: 'responsibilities: KPI dashboards, board-ready reporting narratives'
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Withum is a Top 100 firm; Bonadio is a Top 50 firm; Lincoln Accounting and TFMA are small firms; Aprio is a Top 20 firm (job posting dated 2026-09-15 shows dashboards and board narratives as manager duties and asks for AI-enabled workflows, but does not say AI produces them). Xero says its JAX assistant use rose 61% in three months (ACCTODAY-XEROAI-2026, vendor-published, measures not defined). Grade B because named firms describe use but publish no measurement.'
- id: advisory-client-accounting-services-08
  title: Automated monthly client financial package built from ledger API data
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - document-production
  - data-reporting
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: Producing monthly packages meant exporting trial balances, cleaning data, formatting statements and PDFs, and delivering them client by client, which consumed most of the month.
  solution: A solo fractional-CFO practice pulls P&L and balance sheet programmatically from an AI-native ledger and generates and delivers branded statements to each client every month through its own pipeline.
  outcomes:
  - lever: capacity
    description: Monthly reporting hours for the practice, before and after (self-reported in a vendor case study)
    figure: approximately 108 hours to about 20
    measures: hours spent each reporting cycle by the solo owner across 37 client engagements; the case study uses 'approximately' and does not show a time log
    provenance: vendor-published
    source_ref: DIGITS-ELEV8-2026
  prerequisites:
  - Programmatic access to ledger statements
  - Time to migrate clients (27 clients in about 40 hours per the case study)
  risks_and_guardrails:
  - Single-source vendor case study with approximate figures
  - 'Solo practice: findings may not transfer to a mid-market team'
  human_checkpoints:
  - Owner reviews statements before delivery (the case study does not describe a formal review step)
  role_evolution: Owner says the practice moved from a 'bookkeeping factory' to advisory and fractional CFO work without hiring staff accountants (DIGITS-ELEV8-2026).
  evidence_grade: B
  sources:
  - ref: DIGITS-ELEV8-2026
    title: 'From Bookkeeping Factory to Fractional CFO Firm: How Elev8 Built Big-Firm Output Without Adding Staff'
    publisher: Digits (case study)
    type: vendor
    url: https://digits.com/case-studies/elev8-cfo/
    date: '2026-07-08'
    access: full
    locator: paragraphs on 108 hours across 18 days, migration of 27 clients in about 40 hours, Digits Connect API reporting pipeline
  last_reviewed: '2026-10-20'
  notes: 'Firm type: small or solo firm (Elev8 CFO, El Paso, Texas), not mid-market. Date of the case study is 2026-07-08 per its metadata. Independence: bookkeeping and preparing accounting records for an audit client is barred under SEC Rule 2-01(c)(4)(i) when the audit client is an SEC registrant (confirmed in eCFR, SEC-REG210-2026). Treatment for private audit clients under the AICPA and IESBA codes was not checked in this run, so confirm before a firm offers this service to its own attest clients.'
- id: advisory-client-accounting-services-09
  title: Drafting technical accounting memos and client analyses with retrieval over a firm's own memo library
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - document-production
  - expert-judgment
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Fractional CFO and controllership clients ask for technical accounting memos (for example goodwill impairment after an acquisition) that take hours to write clearly.
  solution: The advisory group turned its library of past memos into a retrieval index behind a memo-generator bot; staff get a first draft and a person reviews and corrects it.
  outcomes:
  - lever: speed
    description: Time per accounting memo, as estimated by the firm's head of AI research (June 2025)
    figure: 4 hours to 30 minutes
    measures: estimated time for an accounting memo including careful human review; an estimate by the builder, not a tracked metric; build took about 60 hours of the builder's time
    provenance: self-reported
    source_ref: JOFA-REALLIFE-2025
  prerequisites:
  - Library of prior memos prepared for retrieval
  - In-house technical skill (about 60 hours to build); the builder says many organizations may do better to wait for a vendor product
  risks_and_guardrails:
  - 'Hallucination: the builder says he tried to remove it with specific instructions and examples; a human stays in the loop (JOFA-REALLIFE-2025)'
  - Per-run cost of several dollars for advanced bots (JOFA-REALLIFE-2025)
  human_checkpoints:
  - Human reviews and corrects every memo draft
  role_evolution: A fractional CFO says AI helps draft technical memos and oversee routine AP and AR, and that helping the company adopt AI is a new CFO responsibility (CFODIVE-FRACTIONAL-2026).
  evidence_grade: B
  sources:
  - ref: JOFA-REALLIFE-2025
    title: Real-life ways accountants are using AI
    publisher: Journal of Accountancy (AICPA & CIMA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2025/jun/real-life-ways-accountants-are-using-ai/
    date: '2025-06-01'
    access: full
    locator: section on Glenn Hopper, Eventus Advisory Group (payoff, degree of difficulty, cost)
  - ref: CFODIVE-FRACTIONAL-2026
    title: Fractional CFOs see demand surge in AI age
    publisher: CFO Dive
    type: press
    url: https://www.cfodive.com/news/fractional-cfos-see-demand-surge-ai-age/827264/
    date: '2026-08-06'
    access: full
    locator: paragraphs quoting Jason Hope, Hope Financial Consulting
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Eventus Advisory Group is a mid-market advisory firm serving private and small-to-midsize public companies with fractional CFO and controllership; Hope Financial Consulting is a small San Diego fractional CFO firm that charges hourly. Date 2025-06 is about 16 months old, inside the window but near its edge. Technical accounting memos for an audit client raise independence questions that were not checked.'
- id: advisory-client-accounting-services-10
  title: AI-accelerated books cleanup, catch-up and platform migration sold as a project
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - client-interaction
  pattern: bulk-transformation
  ladder: automate
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: Annual cleanups and catch-up work took weeks of data entry and reconciliation, were unprofitable for budget-conscious clients, and delayed any advisory work.
  solution: Firms use AI categorization and matching to bring books current in days, price cleanups as discrete projects or recurring quarterly engagements, and migrate clients between ledgers with AI-assisted conversion.
  outcomes:
  - lever: speed
    description: Small firm's positioning of cleanup turnaround after adopting an AI ledger
    figure: 2 to 4 days
    measures: the firm now markets bringing books up to date in two to four days; previous cleanups took weeks (self-reported, vendor case study)
    provenance: vendor-published
    source_ref: DIGITS-TFMA-2026
  - lever: capacity
    description: Time per bookkeeping engagement per client per month at the same firm
    figure: 1-3 hours
    measures: hours per bookkeeping client per month reported by the owner; priced at $200-$400 a month against $500-$1,000 for advisory
    provenance: vendor-published
    source_ref: DIGITS-TFMA-2026
  - lever: capacity
    description: Solo advisory firm's own estimate of bookkeeping workload reduction after adopting an AI ledger
    figure: approximately 75%
    measures: reduction in bookkeeping workload, stated as approximate by the vendor case study; bookkeeping was roughly 70% of the owner's workload before; the owner had earlier tried building custom AI agents but found them costly to keep reliable
    provenance: vendor-published
    source_ref: DIGITS-ADEPT-2026
  - lever: growth
    description: Cleanup turned into a recurring service at a Top 100 CAS practice
    figure: one client
    measures: a client with seven years of unreconciled clearing-account data asked the firm to make the cleanup a recurring quarterly engagement
    provenance: vendor-published
    source_ref: FLOQAST-CASCASE-2026
  prerequisites:
  - Client books accessible on an AI-enabled platform or matching tool
  - A defined, priced project offer
  risks_and_guardrails:
  - Cleanup output still needs review for write-offs and judgment calls (FLOQAST-CASCASE-2026)
  - Platform migration depends on a single vendor; Botkeeper's Feb 2026 closure left firms to migrate in a three-week gap (UKU-BOTKEEPER-2026)
  human_checkpoints:
  - Accountant reviews write-offs and opening balances
  role_evolution: Firms reposition from hourly bookkeeping toward advisory pricing; one owner says AI lets him run with one strong bookkeeper instead of several layers of support (DIGITS-TFMA-2026).
  evidence_grade: B
  sources:
  - ref: DIGITS-TFMA-2026
    title: How TFMA LLC Improved Workflow Efficiency by 70% with Digits
    publisher: Digits (case study)
    type: vendor
    url: https://digits.com/case-studies/how-tfma-llc-improved-workflow-efficiency-by-70-with-digits/
    date: '2026-04-20'
    access: full
    locator: paragraphs on annual cleanups, two to four days, 1-3 hours per client, $500-$1,000 advisory
  - ref: FLOQAST-CASCASE-2026
    title: How One CAS Practice Uses FloQast AI Transaction Matching to Scale Client Support (case study PDF; file name FloQast_MillerCooper_CAS_Case_Study_August_2026)
    publisher: FloQast
    type: vendor
    url: https://get.floqast.com/hubfs/Assets/Case%20Studies/FloQast_MillerCooper_CAS_Case_Study_August_2026.pdf
    date: 2026-08
    access: full
    locator: paragraph on the seven-year clearing-account cleanup and quarterly engagement
  - ref: DIGITS-ELEV8-2026
    title: 'From Bookkeeping Factory to Fractional CFO Firm: How Elev8 Built Big-Firm Output Without Adding Staff'
    publisher: Digits (case study)
    type: vendor
    url: https://digits.com/case-studies/elev8-cfo/
    date: '2026-07-08'
    access: full
    locator: migration of 27 clients in about 40 hours
  - ref: DIGITS-ADEPT-2026
    title: 'How Adept: Accounting Principles & Solutions Reduced Bookkeeping by 75% with Digits'
    publisher: Digits (case study)
    type: vendor
    url: https://digits.com/case-studies/adept-accounting/
    date: '2026-03-23'
    access: full
    locator: section 'A 75% Reduction in Bookkeeping Time' and the paragraph on bookkeeping as 70% of workload and earlier custom agents
  - ref: DIGITS-MANA-2025
    title: 'Mana Accounting & Advisory: Saving Hours with AI-Powered Accounting'
    publisher: Digits (case study)
    type: vendor
    url: https://digits.com/case-studies/mana-accounting-advisory-saving-hours-with-ai-powered-accounting/
    date: '2025-10-10'
    access: full
    locator: paragraphs on cleanups that took hours now taking minutes and frictionless client onboarding (qualitative; no figures)
  - ref: UKU-BOTKEEPER-2026
    title: 'Botkeeper Alternatives: 7 Best Options for Accounting Firms'
    publisher: Uku
    type: vendor
    url: https://getuku.com/articles/botkeeper-alternatives/
    date: '2026-02-13'
    access: full
    locator: section 'What Happened to Botkeeper?' (shutdown 9 Feb 2026; Xendoo announcement 3 Mar 2026)
  last_reviewed: '2026-10-20'
  notes: 'Firm types: TFMA LLC, Elev8, Adept (solo) and Mana Accounting & Advisory (startup and law-firm clients) are small firms; the FloQast firm is an unnamed Top 100 firm. The pricing figures describe a small firm''s own prices; firm pricing in general is routed to professional-services. Independence: bookkeeping and preparing accounting records for an audit client is barred under SEC Rule 2-01(c)(4)(i) when the audit client is an SEC registrant (confirmed in eCFR, SEC-REG210-2026). Treatment for private audit clients under the AICPA and IESBA codes was not checked in this run, so confirm before a firm offers this service to its own attest clients.'
- id: advisory-client-accounting-services-11
  title: Payroll preparation with AI-guided workflows, anomaly flagging and multi-client oversight
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - review-assurance
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Payroll prep means re-entering hours, reimbursements and deductions that clients send by email, then pulling the same reports after every run, client by client.
  solution: Accountants run payroll from one firm dashboard; connected email drafts hours, reimbursements and deductions; the tool shows what changed since the last run, flags anomalies for review and learns which reports the firm pulls. Intuit's payroll agent collects and validates data, flags inconsistencies and can run payroll for the business owner.
  outcomes:
  - lever: capacity
    description: none published
    figure: none
    measures: no outcome figure in either announcement
    provenance: vendor-published
    source_ref: ACCTODAY-GUSTO-2026
  prerequisites:
  - Clients on the vendor's payroll platform
  - Mail or document connectors (Outlook, Google Drive and OneDrive connectors were described as coming soon)
  risks_and_guardrails:
  - Gusto says accountants want AI assistance but not full automation of payroll; the tool flags anomalies instead of pushing them through (ACCTODAY-GUSTO-2026)
  - QuickBooks Workforce was to be generally available 'in the coming weeks' from 8 May 2026; no named customer outcomes (ACCTODAY-QBWORKFORCE-2026)
  human_checkpoints:
  - Accountant reviews flagged anomalies and approves payroll changes
  role_evolution: Gusto says the goal is to put the accountant back in the advising seat and out of report hunting (ACCTODAY-GUSTO-2026).
  evidence_grade: C
  sources:
  - ref: ACCTODAY-GUSTO-2026
    title: Gusto adds accounting firm-centered enhancements to platform, partner program
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/gusto-adds-accounting-firm-centered-enhancements-to-platform-partner-program
    date: '2026-10-09'
    access: full
    locator: paragraphs on built-in AI-guided workflows, Gmail connector, anomaly flagging, multiclient MCP
  - ref: ACCTODAY-QBWORKFORCE-2026
    title: Intuit launches QuickBooks Workforce for HCM, payroll
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/intuit-launches-quickbooks-workforce-for-hcm-payroll
    date: '2026-05-08'
    access: full
    locator: paragraphs on the Payroll Agent and availability
  - ref: PILOT-AIACCOUNTANT-2026
    title: Pilot Unveils AI Accountant
    publisher: Pilot (company blog)
    type: vendor
    url: https://pilot.com/blog/pilot-unveils-ai-accountant-a-major-leap-toward-artificial-general-intelligence-in-accounting
    date: '2026-02-04'
    access: full
    locator: sentence on ticking and tying payroll liabilities
  last_reviewed: '2026-10-20'
  notes: 'Firm type: vendors (Gusto, Intuit, Pilot); no firm deployment named. Payroll is part of the CAS service set per JOFA-CASTIPS-2025.'
- id: advisory-client-accounting-services-12
  title: 'Accounts payable and vendor-admin agents: invoice coding, vendor Q&A drafts and W-9 collection'
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - client-interaction
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: AP and bill pay for CAS clients involve invoice coding, vendor emails and collecting vendor tax documents, which are repetitive and slow cash and compliance.
  solution: Agents code invoices, draft answers to routine vendor and payment questions, capture receipts and collect vendor tax documents. Xero's assistant is described as handling a bill from capture to payment and automatic reconciliation.
  outcomes:
  - lever: capacity
    description: Vendor-stated aggregate for a receipt and expense agent
    figure: 1,100-plus hours
    measures: hours of manual work saved across customers since the agent's October 2025 launch, as stated by BILL; no per-customer data
    provenance: vendor-published
    source_ref: CPAPA-BILLAGENTS-2026
  - lever: capacity
    description: Vendor-stated aggregate for a tax-document collection agent
    figure: approximately 1,000 days
    measures: days of manual work saved across customers since its October 2025 launch, as stated by BILL
    provenance: vendor-published
    source_ref: CPAPA-BILLAGENTS-2026
  prerequisites:
  - Clients on the vendor's AP platform (BILL or Xero online bill pay)
  risks_and_guardrails:
  - Moving money raises the stakes; Xero says it designs for 'accountable intelligence' with audit trails and the owner or adviser in the driver's seat (ACCTODAY-XEROAI-2026)
  - Aggregate vendor hours cannot be tied to any named firm or baseline
  human_checkpoints:
  - Owner or adviser approves payments
  role_evolution: A BILL executive predicts pre-processing of bills (sourcing documents, extracting data, categorizing) will see the largest reduction in human involvement (ACCTODAY-AITHOUGHT-2026).
  evidence_grade: C
  sources:
  - ref: CPAPA-BILLAGENTS-2026
    title: BILL Releases New and Enhanced AI Agents
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/02/10/bill-releases-new-and-enhanced-ai-agents/177829/
    date: '2026-02-10'
    access: full
    locator: paragraphs on the agents and the hours-saved figures
  - ref: ACCTODAY-XEROAI-2026
    title: Xero aims to make AI core to platform functionality
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/xero-aims-to-make-ai-core-to-platform-functionality
    date: '2026-03-16'
    access: full
    locator: paragraphs on JAX, online bill pay and Melio
  - ref: ACCTODAY-AITHOUGHT-2026
    title: 'AI Thought Leaders Survey 2026: Process Predictions'
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/list/ai-thought-leaders-survey-2026-process-predictions
    date: '2025-12-30'
    access: full
    locator: Misherghi (Bill) quote on pre-processing
  last_reviewed: '2026-10-20'
  notes: 'Firm type: vendors (BILL, Xero). BILL also says nearly 90 of the top 100 firms use its platform (seen in a search summary only; not used here). No named firm outcome was found for AP agents in CAS.'
- id: advisory-client-accounting-services-13
  title: Agent that chases missing client documents and requests during close (idea)
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - client-interaction
  - coordination-scheduling
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Teams spend large amounts of time chasing documents, organizing files and preparing work before the real work can start; clients take 10 to 12 days to answer email follow-ups in one firm's account.
  solution: 'Idea discussed by vendor and practice-management leaders: AI takes the first pass organizing client information, flagging what is missing, requesting documents and setting up meetings.'
  outcomes:
  - lever: capacity
    description: none published
    figure: none
    measures: no figure; a prediction by Karbon's chief executive and others for 2026
    provenance: vendor-published
    source_ref: ACCTODAY-AITHOUGHT-2026
  prerequisites:
  - Client portal or email integration inside the practice-management system
  risks_and_guardrails:
  - Idea only; no named deployment found for CAS close
  human_checkpoints:
  - Not described
  role_evolution: Karbon's chief executive says far fewer people will spend days pulling information together before work can start (ACCTODAY-AITHOUGHT-2026).
  evidence_grade: D
  sources:
  - ref: ACCTODAY-AITHOUGHT-2026
    title: 'AI Thought Leaders Survey 2026: Process Predictions'
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/list/ai-thought-leaders-survey-2026-process-predictions
    date: '2025-12-30'
    access: full
    locator: paragraphs on preparatory work and the Karbon CEO quote
  - ref: DIGITS-ELEV8-2026
    title: 'From Bookkeeping Factory to Fractional CFO Firm: How Elev8 Built Big-Firm Output Without Adding Staff'
    publisher: Digits (case study)
    type: vendor
    url: https://digits.com/case-studies/elev8-cfo/
    date: '2026-07-08'
    access: full
    locator: paragraph on follow-up emails taking 10 to 12 days before and a few business days now
  last_reviewed: '2026-10-20'
  notes: 'Label: idea. Practitioners and vendors discuss it; a Digits case study reports faster client responses when requests go through the ledger, which is a related but different mechanism.'
- id: advisory-client-accounting-services-14
  title: Redesigning offshore and outsourced CAS delivery around documented processes, AI and review
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Early offshoring was a lift-and-shift of the same process to cheaper labor, and firms that outsourced undocumented work struggled.
  solution: Firms map the as-is process, improve it with automation and AI, and make the offshore team's output a review of work, with pods mixing US leads, offshore teams and AI-enabled workflows.
  outcomes:
  - lever: capacity
    description: Share of responding firms that offshore (2025 AICPA PCPS and CPA.com management survey, as reported)
    figure: 29%
    measures: share of responding firms that leverage offshoring; nearly three-quarters of firms with net client fees of $10 million or more offshore some work
    provenance: independent
    source_ref: ACCTODAY-OUTSOURCING-2026
  - lever: capacity
    description: Share of surveyed accounting and bookkeeping professionals who outsourced at least one service (Intuit survey, n=725)
    figure: 80%
    measures: respondents who outsourced at least one service for the second year in a row; 65% plan to increase outsourcing
    provenance: vendor-published
    source_ref: INTUIT-ACCTTECH-2026
  prerequisites:
  - Standardized procedures, defined scope and tracked performance metrics (ACCTODAY-OUTSOURCING-2026)
  - 'Documented processes before automation: outsourcing forces documentation that AI needs (a commenter on INTUIT-ACCTTECH-2026)'
  risks_and_guardrails:
  - 'Outsourcing ''chaos'' fails: workflows that live in people''s heads do not transfer (ACCTODAY-OUTSOURCING-2026)'
  - Mid-level roles may become harder to fill if entry-level roles are automated (ACCTODAY-MAVI-2026)
  human_checkpoints:
  - US lead reviews offshore output
  - Job manager sign-off
  role_evolution: CohnReznick's CAS leader says offshore work is moving toward review of work and upskilling will speed up with AI (ACCTODAY-OUTSOURCING-2026). Aprio's CAAS manager posting expects coordination of US leads, offshore teams and AI-enabled workflows (APRIO-JOB-2026).
  evidence_grade: B
  sources:
  - ref: ACCTODAY-OUTSOURCING-2026
    title: Making outsourcing work for your accounting firm
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/making-outsourcing-work-for-your-accounting-firm
    date: '2026-02-05'
    access: full
    locator: paragraphs quoting Kane Polakoff (CohnReznick) and the 29% survey figure
  - ref: INTUIT-ACCTTECH-2026
    title: 'The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future'
    publisher: CPA Practice Advisor (reporting the Intuit QuickBooks Accountant Technology Survey)
    type: survey
    url: https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807
    date: '2026-07-02'
    access: full
    locator: paragraph on outsourcing as a second engine (80%, 65%)
  - ref: APRIO-JOB-2026
    title: Accounting Manager, Client Accounting & Advisory Services (Aprio, listed on Built In NYC)
    publisher: Aprio via Built In NYC
    type: job-posting
    url: https://www.builtinnyc.com/job/accounting-manager-client-accounting-advisory-services/11189037
    date: '2026-09-15'
    access: full
    locator: responsibilities 'Quarterbacking' and 'Process & Delivery Innovation'
  - ref: ACCTODAY-MAVI-2026
    title: MAVI offers AI-aided international financial talent service
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/mavi-offers-ai-aided-offshore-financial-talent-service
    date: '2026-09-30'
    access: full
    locator: paragraphs on mid-level talent shortage and AI screening of candidates
  - ref: JOFA-CASTIPS-2025
    title: Tips for providing the CAS services clients want
    publisher: Journal of Accountancy (AICPA & CIMA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2025/jul/tips-for-providing-the-cas-services-clients-want/
    date: '2025-07-01'
    access: full
    locator: paragraph on CohnReznick hiring industry experts including staff in Chennai
  last_reviewed: '2026-10-20'
  notes: 'Firm types: CohnReznick is a Top 100 firm; Aprio is a Top 20 firm; MAVI is a talent vendor (its 50% cost saving is its own comparison). No measured effect of AI on offshore throughput or quality was found. The AICPA PCPS survey result is reported secondhand in Accounting Today.'
- id: advisory-client-accounting-services-15
  title: Staff accountants drive close entries and reconciliations through a general AI assistant connected to the ledger
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: Booking entries and reconciling closes by hand is slow, and read-only AI cannot change the books.
  solution: Accountants use a general assistant connected to the ledger through an agent connector. Writes apply automatically in open periods and are queued for manager approval in locked periods.
  outcomes:
  - lever: speed
    description: One AI-native practice's account of two client quarterly closes
    figure: about 7 hours vs 1 hour 40 minutes (roughly four times faster)
    measures: time for one staff accountant to book entries and reconcile the Q3 closes for two clients (one SaaS, one e-commerce), by hand versus through the assistant; recollection quoted by the vendor, not a tracked metric
    provenance: vendor-published
    source_ref: DIGITS-WRITEMCP-2026
  prerequisites:
  - Ledger with write access for agents and period-lock controls
  - 'Role-based permissions: agents work within the user''s permissions'
  risks_and_guardrails:
  - An agent that writes to the ledger touches the system of record; conventional closed-period passwords and pop-ups do not stop an agent (DIGITS-WRITEMCP-2026)
  - Humans using an assistant in the Mercor study took about 15 times longer than the model alone and sometimes overrode a correct AI answer (ACCTODAY-AIBEATS-2026, lab setting)
  human_checkpoints:
  - Manager approves queued changes to locked periods
  - A licensed CPA reviews every close at Arclow (ARCLOW-SITE-2026)
  role_evolution: Staff accountants become operators and reviewers of assistant-produced entries; managers and admins approve changes to locked periods (DIGITS-WRITEMCP-2026).
  evidence_grade: B
  sources:
  - ref: DIGITS-WRITEMCP-2026
    title: 'Agentic Accounting With Confidence: Introducing Write MCP and Locked Period Controls'
    publisher: Digits
    type: vendor
    url: https://digits.com/blog/write-mcp/
    date: '2026-10-13'
    access: full
    locator: paragraphs on Write MCP, Locked Periods, and the Arclow staff accountant
  - ref: ARCLOW-SITE-2026
    title: Arclow home page (AI-native accounting practice; page undated, date is access date)
    publisher: Arclow
    type: firm
    url: https://arclow.com
    date: '2026-10-20'
    access: full
    locator: hero text on CPA review
  - ref: ACCTODAY-AIBEATS-2026
    title: AI beats human accountants at monthly close, transaction categorization
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization
    date: '2026-10-16'
    access: full
    locator: paragraphs on human-with-AI sessions
  last_reviewed: '2026-10-20'
  notes: 'Firm type: AI-native practice (Arclow) and vendor (Digits). Digits says its connector launched in April 2026 and firms used a general assistant for a 13-week cash flow forecast, a 2026 budget from ledger data and budget-versus-actual reports (unnamed firms; vendor-published). Independence: bookkeeping and preparing accounting records for an audit client is barred under SEC Rule 2-01(c)(4)(i) when the audit client is an SEC registrant (confirmed in eCFR, SEC-REG210-2026). Treatment for private audit clients under the AICPA and IESBA codes was not checked in this run, so confirm before a firm offers this service to its own attest clients.'
- id: advisory-client-accounting-services-16
  title: In-house controller automation to scan, summarize and ticket incoming vendor mail and invoices
  archetype: advisory
  module: client-accounting-services
  function: finance-accounting
  work_types:
  - transaction-processing
  - coordination-scheduling
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: 'A small accounting team was inundated with physical mail: vendor invoices, tax notices and statements.'
  solution: The controller built an automation that scans each item, summarizes it with AI, opens a ticket in the team's workflow system with the summary and original mail, and supports status look-ups and follow-up actions.
  outcomes:
  - lever: capacity
    description: Staff time saved per week (controller's estimate, June 2025)
    figure: about four hours a week
    measures: total staff time saved per week; the team handles mail in 20-minute sprints on 'Mail Mondays'; estimate by the controller
    provenance: self-reported
    source_ref: JOFA-REALLIFE-2025
  prerequisites:
  - An existing digital environment and workflow system to receive the output
  - Months of earlier work connecting systems and data, plus automation skill
  risks_and_guardrails:
  - Depends on one builder's skill; no extra licenses were needed
  human_checkpoints:
  - Staff review tickets and act on them
  role_evolution: The controller built the automation himself, which shows the in-house controllership role absorbing workflow-builder tasks (JOFA-REALLIFE-2025).
  evidence_grade: B
  sources:
  - ref: JOFA-REALLIFE-2025
    title: Real-life ways accountants are using AI
    publisher: Journal of Accountancy (AICPA & CIMA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2025/jun/real-life-ways-accountants-are-using-ai/
    date: '2025-06-01'
    access: full
    locator: section on Karl Spanbauer, controller of the Capital Area Food Bank
  last_reviewed: '2026-10-20'
  notes: 'Firm type: in-house finance team at a not-for-profit (Capital Area Food Bank), not a CAS provider. Included because the brief covers in-house teams. Date 2025-06 is about 16 months old.'
- id: advisory-client-accounting-services-17
  title: Client 13-week cash flow forecasts and budgets built from ledger data with automation and AI
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Fractional CFO clients need forward-looking cash flow and budget views, which take time to assemble from spend and cash data.
  solution: A firm tool gathers spend and cash data with robotic process automation, analyses it with machine learning and projects cash over 13 weeks (Armanino, 2024). Firms now also use a general assistant on ledger data to build 13-week forecasts, budgets and budget-versus-actual reports.
  outcomes:
  - lever: experience
    description: none measured
    figure: none
    measures: Armanino reports 'a lot of traction' on a client basis for its 13-week cash flow tool; no figure given
    provenance: self-reported
    source_ref: ACCTODAY-USECASE-2024
  prerequisites:
  - Clean spend and cash data feeding the tool or assistant
  risks_and_guardrails:
  - The 2024 Armanino tool uses RPA and machine learning, not generative AI; its source is older than the 12-18 month window and is used as a foundation only
  - The newer forecasting examples come from an unnamed set of firms in a vendor blog (DIGITS-WRITEMCP-2026)
  human_checkpoints:
  - Adviser reviews forecast assumptions before client delivery (implied; not described)
  role_evolution: Aprio's CAAS manager is expected to build budgets, 13-week cash flow models and scenario analyses, with AI-enabled templates and workflows (APRIO-JOB-2026).
  evidence_grade: B
  sources:
  - ref: ACCTODAY-USECASE-2024
    title: Making the use case for AI in accounting
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/making-the-use-case-for-ai-in-accounting
    date: '2024-05-06'
    access: full
    locator: Armanino 13 Week Cashflow paragraph (OJ Laos)
  - ref: DIGITS-WRITEMCP-2026
    title: 'Agentic Accounting With Confidence: Introducing Write MCP and Locked Period Controls'
    publisher: Digits
    type: vendor
    url: https://digits.com/blog/write-mcp/
    date: '2026-10-13'
    access: full
    locator: paragraph on 13-week cash flow forecast, 2026 budget and budget-versus-actual built with Claude
  - ref: APRIO-JOB-2026
    title: Accounting Manager, Client Accounting & Advisory Services (Aprio, listed on Built In NYC)
    publisher: Aprio via Built In NYC
    type: job-posting
    url: https://www.builtinnyc.com/job/accounting-manager-client-accounting-advisory-services/11189037
    date: '2026-09-15'
    access: full
    locator: responsibilities 'Financial Modeling & FP&A'
  last_reviewed: '2026-10-20'
  notes: 'Firm types: Armanino is a Top 25 firm; the newer examples are unnamed. Date of the named deployment is 2024-05-06, so grade B reflects a named but dated, non-generative deployment. FP&A and performance-improvement work belongs in the fpa-performance module; this entry keeps only the CFO-services forecast step that CAS teams deliver.'
```

## 3. Module notes

### 3.1 Processes and key steps (with work types)

- **Client onboarding, ledger set-up and cleanup** (transaction-processing; software-systems). Migrating clients to a new ledger and catching up books; AI-assisted migration of 27 clients in about 40 hours is reported by one solo firm (DIGITS-ELEV8-2026).
- **Transaction capture and categorization** (transaction-processing). Bank feeds, receipts, coding. Use case 01.
- **Reconciliations** (transaction-processing; review-assurance). Bank, card, clearing accounts, payroll liabilities. Use cases 02, 03.
- **Month-end close and statements** (data-reporting; document-production). Checklist routing to job managers, review, sign-off. Use cases 03, 04, 08, 15.
- **Management reporting, dashboards, variance explanations** (data-reporting; client-interaction). Use case 07.
- **AP, bill pay, AR** (transaction-processing). Use case 12.
- **Payroll preparation and runs** (transaction-processing). Use case 11.
- **Controllership and technical accounting** (expert-judgment; document-production). Memos, accruals, cleanups. Use cases 09, 10.
- **Fractional CFO services** (expert-judgment; data-reporting). Budgets, 13-week cash flow, scenarios, board reporting. Use case 17.
- **Client requests and communication** (client-interaction; coordination-scheduling). Use case 13.
- **Practice workflow and review layer** (coordination-scheduling). Checklists, job manager dashboards (FLOQAST-CASCASE-2026).

### 3.2 Common pain points

- Manual data cleanup is the top blocker to more advisory work, named by 30% of respondents, ahead of staffing shortages (24%) and app overload (16%) (INTUIT-ACCTTECH-2026).
- Tool sprawl: the average firm runs about 10 apps, only 41% say tools are fully integrated, and accountants report losing about five hours a week moving or re-entering data (INTUIT-ACCTTECH-2026).
- Lack of standardization as CAS teams grow: one CAS team that grew from 25 to 65 professionals had every manager tracking to-dos differently (FLOQAST-CASCASE-2026).
- Broken bank connections that need the client to log in again, and slow client replies (10 to 12 days of email follow-ups at one solo firm before it used ledger-based requests) (DIGITS-LINCOLN-2026; DIGITS-ELEV8-2026).
- Talent supply: practitioners describe a shortage of traditional bookkeepers; 61% of finance leaders in a Controllers Council survey (quoted by MAVI) reported a talent shortage in 2026 (ACCTODAY-BONADIO-2026; ACCTODAY-MAVI-2026).
- Noisy built-in AI: one small firm saw a platform's new AI categorization mis-suggest transactions it had coded correctly before (DIGITS-LINCOLN-2026).

### 3.3 Metrics and benchmarks (with sources and provenance)

| Metric | Figure | What it measures | Source | Provenance |
|---|---|---|---|---|
| CAS growth | 17% median in 2024; CAS revenue projected to double over three years | Median growth rate among 200+ respondents to the biennial CAS Benchmark Survey (CPA.com and AICPA PCPS), as reported by JofA | JOFA-CASTIPS-2025 | independent |
| CAS growth among large firms | 85% | Share of the 88 responding Top 100 firms reporting a boost in the CAS line, up five points from the prior year | ACCTODAY-BONADIO-2026 | independent |
| Fixed-fee recurring model | 90% | Share of CAS practices that sell fixed-fee recurring services, per the JofA article | JOFA-CASTIPS-2025 | independent |
| Withum CAS revenue | $70 million | Withum's CAS revenue seven years after launch, stated by its advisory leader | ACCTODAY-CASKEYS-2026 | self-reported |
| AI use for client services | 88% (client service); 86% (firm operations) | Respondents (n=725) using AI for at least one client service or one firm operation | INTUIT-ACCTTECH-2026 | vendor-published |
| Embedded AI | 30% embedded as default; 54% situational | Share of respondents describing their AI use that way | INTUIT-ACCTTECH-2026 | vendor-published |
| AI policy | 21% | Share of firms with an AI policy or strategy (nearly 600 respondents) | KARBON-AISTATE-2026 | vendor-published |
| Offshoring | 29% | Share of responding firms that offshore (2025 AICPA PCPS and CPA.com management survey, as reported) | ACCTODAY-OUTSOURCING-2026 | independent |
| Time to close | 7.5 days faster | AI users versus non-users in the field data (association) | STANFORD-GSBINSIGHT-2025 | independent |
| Time reallocated | about 8.5% | Accountant time shifted from routine data entry to communication and QA | MITSLOAN-CHOIXIE-2025 | independent |
| Categorization accuracy | 97.8% vs 79.1% | Ledger-native model versus outsourced accountants on 2,000 transactions | DIGITS-BENCH-2026 | vendor-published |
| General-model accuracy | 77.3% best | Best of 19 general models on 101 accounting workflows | ACCTODAY-DUALENTRY-2026 | vendor-published |
| Lab close test | AI 100% on 20 attempts; juniors generally below 50% | Rubric criteria met on four simulated close tasks, 12 junior CPAs | ACCTODAY-AIBEATS-2026; MERCOR-APEX-2026 | independent (third-party lab study) |
| Interim CFO demand | +14% year on year; interim C-suite requests +151% since 2021 | Business Talent Group figures quoted by CFO Dive | CFODIVE-FRACTIONAL-2026 | independent |
| Billable hours per CAS lead | about 1,700 to 500-600 a year; 47% revenue growth | One BST & Co leader's own account after moving to leveraging technology; not attributed to AI | JOFA-CASTIPS-2025 | self-reported |
| Clients per CAS team member | more than 15 to about 6 | One Sweeney Conrad leader's account | JOFA-CASTIPS-2025 | self-reported |
| Assistant use at Xero | +61% in three months | Growth in use of JAX AI in the last three months (measure not defined) | ACCTODAY-XEROAI-2026 | vendor-published |
| Search-only: Intuit accounting agent | 237 million transactions categorized in January (search summary of Q2 FY26 call) | Intuit's statement on agent volume; not read in full | INTUIT-FY26Q2-2026 | vendor-published, search-only |

**Quality evidence.** Independent: the JAR study's framed experiment (AI helps on average, but following non-consensus AI answers can add errors) and the Mercor lab test (AI scored perfectly, humans paired with an assistant took about 15 times longer than the model alone and sometimes overrode correct answers, on tasks without client context). Vendor-run: Digits and DualEntry accuracy figures. Not found: override rates, parallel-run results, review-found error rates or inspection outcomes for any CAS firm in production.

### 3.4 Guardrails and regulatory points

- **Independence.** Bookkeeping or preparing accounting records for an SEC-registrant audit client is barred (SEC-REG210-2026). Financial information system design and implementation is a separate barred category in the same paragraph. Private-company audit clients: not checked in this run.
- **Five written controls before an agent touches a production close** (agent inventory with a named owner; replayable evidence; human sign-off gates scaled to risk; reading third-party assurance reports for what they cover; monitoring with exit thresholds). The author also cites COSO's February 2026 guidance on internal control over generative AI (not fetched) and says no AICPA SOC guidance specific to AI had been published, a practitioner claim not checked here (CPAPA-AGENTSCLOSE-2026).
- **Ledger-level controls for agents.** Locked periods with a proposal-and-review queue for agent and user edits (DIGITS-WRITEMCP-2026); Pilot says every transaction and decision is logged (PILOT-AIACCOUNTANT-2026); Basis says its agents expose assumptions, data sources and logic behind each decision (OPENAI-BASIS-2026).
- **Client data and trust.** Three in five respondents say clients ask for proof of AI data protection always or frequently; only 33% explain their AI use proactively (INTUIT-ACCTTECH-2026).
- **Vendor-claim discipline.** Treat 90% match rates and 90% preparation-time savings as marketing until reproduced on the client's data and keep a validation period (CPAPA-AGENTSCLOSE-2026).
- **Technology selection.** CPA.com advises a vendor scorecard (quality, delivery time, cost, compliance, stakeholder feedback) rather than the newest tool (JOFA-CASTIPS-2025).

### 3.5 Frontier signals (dated and sourced)

- 2025-11-19: Numeric raised $51M for AI cash matching; Brex reported a match-rate rise from 30% to more than 90% (CPAPA-NUMERIC-2025).
- 2026-02-04: Pilot announced an AI Accountant it describes as fully autonomous from onboarding to close (CPAPA-PILOT-2026).
- 2026-02-09: Botkeeper announced closure; Xendoo's purchase of the Infinite platform was reported on 2026-02-28, with a formal announcement dated 3 Mar 2026 per Uku (UKU-BOTKEEPER-2026; CPAPA-XENDOO-2026).
- 2026-02-24: Basis raised $100M at a reported $1.15B valuation and describes long-horizon agents completing accounting workflows for review (BASIS-SERIESB-2026).
- 2026-03-16: Xero said 2026 is about AI as the core engine and described bill pay assisted end to end by its assistant (ACCTODAY-XEROAI-2026).
- 2026-04-08: Digits introduced pay-only-if-95%-zero-touch pricing (ACCTODAY-DIGITSPRICING-2026).
- 2026-05-08: Intuit launched QuickBooks Workforce with a Payroll Agent (ACCTODAY-QBWORKFORCE-2026).
- 2026-05-12: Xero's Claude integration launched, per Accountex coverage (ACCOUNTEX-2026).
- 2026-06-16: Pilot announced Meridian for accounting firms (ACCTODAY-MERIDIAN-2026).
- 2026-07-21: CLA announced a firm-trained model with Digits, starting in its CAAS practice (ACCTODAY-CLA-2026).
- 2026-07-28: BlackLine announced Verity Prepare, a multi-agent reconciliation preparation system (IAB-BLACKLINE-2026).
- 2026-09-02: Accrual acquired Puzzle's firm technology; CAS offering in early access, wider availability planned by end of 2026 (ACCTODAY-ACCRUAL-2026).
- 2026-10-01 and 2026-10-07: Mercor's lab study and Digits' benchmark were published (MERCOR-APEX-2026; DIGITS-BENCH-2026).
- 2026-10-09: Gusto released AI-guided payroll prep and a multi-client MCP (ACCTODAY-GUSTO-2026).
- 2026-10-13: Digits shipped write access for agents with locked periods (DIGITS-WRITEMCP-2026).
- Scheduled: the 2026 CAS Benchmark Survey report is due in December 2026 (CPACOM-CASBENCH-2026).

### 3.6 Workforce and role effects

- Time shifts from data entry to communication and quality assurance; experienced accountants gain more; juniors defer to uncertain AI output (MITSLOAN-CHOIXIE-2025; STANFORD-GSBINSIGHT-2025).
- Entry-level hiring signals: 53% of respondents say technology certifications and 53% say AI, automation and data skills improve an entry-level candidate's chances, against 50% for CPA status; 38% prioritize strategic judgment and 22% AI fluency in hires (INTUIT-ACCTTECH-2026).
- Pipeline worry: if entry-level tasks are automated, juniors may not build the skills to judge AI output; one adviser says senior people with AI tools could manage agents doing the work of entry-level teams, and that the pipeline must be rebuilt (ACCTODAY-BIGYEAR-2026).
- New roles at vendors that sell to CAS firms need accountants: Basis hires accountants to write agent procedures and skills and says it wants a CPA or accounting master's holder (BASIS-JOBS-2026); Pilot's Solutions Engineer role requires 3 to 5 years of public accounting experience in audit, assurance, tax or CAS (PILOT-JOBS-2026); Rillet hires deployment leads for accounting solutions and a partnerships lead aimed at Big 4, top firms, boutiques and fractional CFOs (RILLET-JOBS-2026).
- Firm-side posting: Aprio's CAAS manager is expected to review board-ready financials, build reusable templates and AI-enabled workflows and coordinate offshore teams, with success measured partly by how little client-lead review time pod financials need (APRIO-JOB-2026).
- Control-minded posting (negative evidence): Kruze Consulting's Controller posting, dated 2026-09-10, describes a 15 to 20 client load and full-cycle close work and does not mention AI (KRUZE-JOB-2026).
- Fractional CFOs describe AI adoption as a new CFO responsibility and say AI has made clients more comfortable with outsourced finance leadership (CFODIVE-FRACTIONAL-2026).
- A Thomson Reuters executive predicted firms will have about one virtual agent per CPA within five years; this is a prediction, not a measurement (ACCTODAY-BIGYEAR-2026).

### 3.7 Objections and concerns practitioners raise

- Accuracy and trust: 62% of surveyed accountants worried about errors in AI-generated reporting, 43% about data security and 37% about job stability (STANFORD-GSBINSIGHT-2025).
- General AI is not good enough alone: vendors say general models plateau around 79% on categorization and 77% on accounting workflows (DIGITS-BENCH-2026; ACCTODAY-DUALENTRY-2026).
- Unreviewed output is a liability; the CPA Practice Advisor article cites a 2025 fee refund by Deloitte Australia after fabricated citations (CPAPA-AGENTSCLOSE-2026).
- Complexity limits: practitioners say autonomous bookkeeping only works for constrained cases (single entities) today (ACCTODAY-BIGYEAR-2026).
- Competition and automation risk: Withum's leader warns of complete automation of tax and of bigger firms coming down market with AI (ACCTODAY-CASKEYS-2026); consultants say clients are self-preparing work with AI tools (ACCTODAY-CATALYST-2026).
- AI-for-in-house substitution: one consultant estimates AI could cut external accounting costs 20 to 50% for routine outsourced work at $10M to $70M revenue companies, an estimate that is not measured data (ACCTODAY-WILLAI-2026).
- Vendor and platform risk: Botkeeper's closure; Puzzle's firm product folded into Accrual (CPAPA-XENDOO-2026; ACCTODAY-ACCRUAL-2026).
- Marketing content quality: one firm stopped using AI for marketing copy because editing erased the time savings (ACCTODAY-USECASE-2024, older).

### 3.8 Interview probes for an advisor

1. Show me one step where AI output reaches the client with no person touching it. What share of transactions and of closes is that, how is it tracked, and who set the threshold?
2. When the AI is uncertain or wrong, who sees it first? Do you track override rates by reviewer seniority, and what do you do about junior staff who accept low-confidence suggestions?
3. What can an agent write to the ledger, and what stops it editing a closed period? Have your SOC or audit reviewers asked about the AI components, and for clients you also audit, how do you handle independence?
4. Since adopting the tools, what changed in clients per accountant, fixed-fee versus hourly mix, and the clients you now accept or refuse? Where did the saved hours go?
5. Which vendor on your stack could disappear or be bought next year, and what is your exit plan and data-export test?

## 4. Routed to other modules

- **professional-services (firm operations, pricing, PE).** Withum's account of CAS as the engine for cross-selling advisory and its $70M revenue figure (ACCTODAY-CASKEYS-2026); how firms price their own CAS, including the 90% fixed-fee statistic and the move away from hourly billing (JOFA-CASTIPS-2025; INTUIT-ACCTTECH-2026); Current's rebrand and AI roll-up thesis, and Larson Gross joining Current and adding a fractional CFO firm (ACCTODAY-CURRENT-2026; CPAPA-LARSON-2026; note the two sources name the investor differently: Thrive Holdings versus Thrive Capital); CBIZ's enterprise agent platform with Microsoft (CBIZ-MICROSOFT-2026); a fractional CFO firm's minority investment with no AI detail (ACCTODAY-CFOSEL-2026); MAVI's AI-vetted offshore talent marketplace as a staffing model (ACCTODAY-MAVI-2026); a firm using AI-generated marketing pages and a custom GPT for lead generation (JOFA-REALLIFE-2025, ACCTODAY-USECASE-2024).
- **fpa-performance.** Citrin Cooperman's acquisition of Rosetree Solutions to sell AI implementation to middle-market clients (ACCTODAY-ROSETREE-2026); AI-native ERP vendors partnering with firms and fractional CFOs (RILLET-JOBS-2026); firm FP&A, scenario and board-reporting work (APRIO-JOB-2026); the consulting view that clients are self-preparing work with AI (ACCTODAY-CATALYST-2026).
- **risk-controls.** The five controls for client-side close agents, COSO's February 2026 guidance on generative AI controls, and the SOC-reporting gap for agent vendors (CPAPA-AGENTSCLOSE-2026).
- **tax.** Withum's prediction of complete automation of the tax process and the Instagram-ads observation on basic individual returns (ACCTODAY-CASKEYS-2026; ACCTODAY-AITHOUGHT-2026).
- **private-client.** GWCPA's custom GPT on ownership transitions for family-held businesses (JOFA-REALLIFE-2025).
- **assurance.** Close and reconciliation evidence that auditors will ask for (replayable evidence, SOC mapping) is relevant to attest work (CPAPA-AGENTSCLOSE-2026); not researched here.

## 5. Sources

Refs follow PUBLISHER-SHORT-YYYY and reuse the landscape file's refs where the document is the same. Access is `full` unless marked. Dates are publication dates except where noted in the title.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ACCTODAY-CASKEYS-2026 | CAS delivers 'the keys to the kingdom' | Accounting Today | press | https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom | 2026-05-22 | full |
| JOFA-CASTIPS-2025 | Tips for providing the CAS services clients want | Journal of Accountancy (AICPA & CIMA) | professional-body | https://www.journalofaccountancy.com/issues/2025/jul/tips-for-providing-the-cas-services-clients-want/ | 2025-07-01 | full |
| CPAPA-AGENTSCLOSE-2026 | Before You Let the Agents Run the Close: Five Controls to Put in Writing First | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/ | 2026-08-13 | full |
| CFODIVE-FRACTIONAL-2026 | Fractional CFOs see demand surge in AI age | CFO Dive | press | https://www.cfodive.com/news/fractional-cfos-see-demand-surge-ai-age/827264/ | 2026-08-06 | full |
| INTUIT-ACCTTECH-2026 | The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future | CPA Practice Advisor (reporting the Intuit QuickBooks Accountant Technology Survey) | survey | https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807 | 2026-07-02 | full |
| ACCTODAY-CURRENT-2026 | Crete Professionals Alliance rebrands as Current | Accounting Today | press | https://www.accountingtoday.com/news/crete-professionalls-alliance-rebrands-as-current | 2026-06-02 | full |
| CBIZ-MICROSOFT-2026 | CBIZ Expands AI Partnership with Microsoft | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/21/cbiz-expands-ai-partnership-with-microsoft/181999/ | 2026-04-21 | full |
| ACCOUNTEX-2026 | Accountex London 2026: product roundup | Financial Accountant (IFA) | press | https://financialaccountant.co.uk/blog/accountex-london-2026-product-roundup/ | 2026-05-19 | full |
| UKU-BOTKEEPER-2026 | Botkeeper Alternatives: 7 Best Options for Accounting Firms | Uku | vendor | https://getuku.com/articles/botkeeper-alternatives/ | 2026-02-13 | full |
| CPAPA-XENDOO-2026 | Xendoo Buys Botkeeper Infinite; AI Platform Will Remain 'Active and Supported' | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/28/xendoo-buys-botkeeper-infinite-ai-platform-will-remain-active-and-supported/179027/ | 2026-02-28 | full |
| KARBON-AISTATE-2026 | Karbon State of AI in Accounting 2026 Report shows strategy, training, and governance unlock AI's full potential | Karbon Magazine | survey | https://karbonhq.com/resources/state-of-ai-accounting-2026 | 2026-01-20 | full |
| STANFORD-JAR-2026 | Human + AI in Accounting: Early Evidence from the Field (Choi, Xie), Journal of Accounting Research 64(3), pp 1333-1373 | Stanford Graduate School of Business (publication listing with abstract) | academic | https://www.gsb.stanford.edu/index.php/node/629989 | 2026-06 | full |
| MITSLOAN-CHOIXIE-2025 | How generative AI can make accountants more productive | MIT Sloan Ideas Made to Matter | academic | https://mitsloan.mit.edu/ideas-made-to-matter/how-generative-ai-can-make-accountants-more-productive | 2025-08-05 | full |
| STANFORD-GSBINSIGHT-2025 | AI Is Reshaping Accounting Jobs by Doing the 'Boring' Stuff | Stanford Graduate School of Business Insights | academic | https://gsb.stanford.edu/insights/ai-reshaping-accounting-jobs-doing-boring-stuff | 2025-06-09 | full |
| BASIS-SERIESB-2026 | Basis Raises $100 Million to Deploy AI Agents for Accounting Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/24/basis-raises-100-million-to-deploy-ai-agents-for-accounting-firms/178759/ | 2026-02-24 | full |
| OPENAI-BASIS-2026 | Basis scales accounting by turning OpenAI model progress into trusted agents | OpenAI (customer story) | vendor | https://openai.com/index/basis | 2026-10-20 | full |
| CPAPA-PILOT-2026 | Pilot Rolls Out Fully Autonomous AI Accountant | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/04/pilot-rolls-out-fully-autonomous-ai-accountant/177453/ | 2026-02-04 | full |
| PILOT-AIACCOUNTANT-2026 | Pilot Unveils AI Accountant | Pilot (company blog) | vendor | https://pilot.com/blog/pilot-unveils-ai-accountant-a-major-leap-toward-artificial-general-intelligence-in-accounting | 2026-02-04 | full |
| PILOT-PARTNERHUB-2026 | What's New at Pilot - Partner Resource Hub | Pilot | vendor | https://partners.pilot.com/Partner%20Hub/pages/whats-new.html | 2026-04 | full |
| ACCTODAY-MERIDIAN-2026 | Pilot touts Meridian, says AI comparable to seasoned accountant | Accounting Today | press | https://www.accountingtoday.com/news/pilot-touts-meridian-says-ai-comparable-to-seasoned-accountant | 2026-06-16 | full |
| PILOT-JOBS-2026 | Pilot job postings: Solutions Engineer (Meridian); Senior Product Manager, Meridian; Sr. Software Engineer, Bookkeeping Automation | Pilot (Greenhouse job board) | job-posting | https://job-boards.greenhouse.io/pilothq/jobs/8880563002 | 2026-10-09 | full |
| ACCTODAY-BIGYEAR-2026 | A big year for AI in accounting | Accounting Today | press | https://accountingtoday.com/news/a-big-year-for-ai-in-accounting | 2026-02-04 | full |
| FLOQAST-CASCASE-2026 | How One CAS Practice Uses FloQast AI Transaction Matching to Scale Client Support (case study PDF; file name FloQast_MillerCooper_CAS_Case_Study_August_2026) | FloQast | vendor | https://get.floqast.com/hubfs/Assets/Case%20Studies/FloQast_MillerCooper_CAS_Case_Study_August_2026.pdf | 2026-08 | full |
| BASIS-JOBS-2026 | Basis job postings: Accounting Solutions Consultant; Member of Accounting Staff; Intelligence Architect | Basis (Ashby job board) | job-posting | https://jobs.ashbyhq.com/basis-ai/bf7e34d6-e678-491b-87ee-e7c1f3e0384f | 2026-05-20 | full |
| RILLET-JOBS-2026 | Rillet job postings: Head of Accounting & Advisory Partnerships; Deployment Lead - Accounting Solutions | Rillet (Ashby job board) | job-posting | https://jobs.ashbyhq.com/rillet/edbff973-0404-45ef-a435-164ef7955abd | 2026-09-15 | full |
| KRUZE-JOB-2026 | Controller (Kruze Consulting) | Kruze Consulting (Lever job board) | job-posting | https://jobs.lever.co/kruzeconsulting/f24249f5-b646-4565-a3d4-ff84e285d447 | 2026-09-10 | full |
| APRIO-JOB-2026 | Accounting Manager, Client Accounting & Advisory Services (Aprio, listed on Built In NYC) | Aprio via Built In NYC | job-posting | https://www.builtinnyc.com/job/accounting-manager-client-accounting-advisory-services/11189037 | 2026-09-15 | full |
| ACCTODAY-AIBEATS-2026 | AI beats human accountants at monthly close, transaction categorization | Accounting Today | press | https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization | 2026-10-16 | full |
| MERCOR-APEX-2026 | AI vs. Accountants: Frontier Models Outscore CPAs | Mercor | vendor | https://www.mercor.com/blog/human-baselines-for-benchmarks-ai-now-outperforms-junior-accountants/ | 2026-10-01 | full |
| DIGITS-BENCH-2026 | Breaking: AI Can't Close Your Books From the Outside (Yes, Including Jev) | Digits | vendor | https://digits.com/blog/ai-cant-close-books-from-outside/ | 2026-10-07 | full |
| ACCTODAY-CLA-2026 | CLA working with Digits to develop proprietary AI model | Accounting Today | press | https://www.accountingtoday.com/news/cla-working-with-digits-to-develop-proprietary-ai-model | 2026-07-21 | full |
| ACCTODAY-ACCRUAL-2026 | Accrual acquires Puzzle's tech to add to their CAS offering | Accounting Today | press | https://www.accountingtoday.com/news/accrual-acquires-puzzles-tech-to-add-to-their-cas-offering | 2026-09-02 | full |
| ACCTODAY-BONADIO-2026 | CAS and outsourced accounting fuel Bonadio Group | Accounting Today | press | https://www.accountingtoday.com/news/cas-and-outsourced-accounting-fuel-bonadio-group | 2026-07-30 | full |
| ACCTODAY-CATALYST-2026 | AI - the catalyst and solution to advisory | Accounting Today | press | https://www.accountingtoday.com/news/ai-the-catalyst-and-solution-to-advisory | 2026-07-13 | full |
| ACCTODAY-GUSTO-2026 | Gusto adds accounting firm-centered enhancements to platform, partner program | Accounting Today | press | https://www.accountingtoday.com/news/gusto-adds-accounting-firm-centered-enhancements-to-platform-partner-program | 2026-10-09 | full |
| ACCTODAY-ROSETREE-2026 | Citrin Cooperman acquires Rosetree Solutions | Accounting Today | press | https://www.accountingtoday.com/news/citrin-cooperman-acquires-rosetree-solutions | 2026-10-06 | full |
| ACCTODAY-DIGITSPRICING-2026 | Digits announces outcome-based pricing | Accounting Today | press | https://www.accountingtoday.com/news/digits-announces-outcome-based-pricing | 2026-04-08 | full |
| ACCTODAY-DUALENTRY-2026 | Generalist AI model accuracy tops out at 77% for accounting | Accounting Today | press | https://www.accountingtoday.com/news/generalist-ai-model-accuracy-tops-out-at-77-for-accounting | 2026-03-17 | full |
| ACCTODAY-XEROAI-2026 | Xero aims to make AI core to platform functionality | Accounting Today | press | https://www.accountingtoday.com/news/xero-aims-to-make-ai-core-to-platform-functionality | 2026-03-16 | full |
| ACCTODAY-OUTSOURCING-2026 | Making outsourcing work for your accounting firm | Accounting Today | press | https://www.accountingtoday.com/news/making-outsourcing-work-for-your-accounting-firm | 2026-02-05 | full |
| ACCTODAY-MAVI-2026 | MAVI offers AI-aided international financial talent service | Accounting Today | press | https://www.accountingtoday.com/news/mavi-offers-ai-aided-offshore-financial-talent-service | 2026-09-30 | full |
| ACCTODAY-QBWORKFORCE-2026 | Intuit launches QuickBooks Workforce for HCM, payroll | Accounting Today | press | https://www.accountingtoday.com/news/intuit-launches-quickbooks-workforce-for-hcm-payroll | 2026-05-08 | full |
| ACCTODAY-CFOSEL-2026 | CFO Selections gets investment from Laird Norton | Accounting Today | press | https://www.accountingtoday.com/news/cfo-selections-gets-investment-from-laird-norton | 2026-04-27 | full |
| CPAPA-BILLAGENTS-2026 | BILL Releases New and Enhanced AI Agents | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/10/bill-releases-new-and-enhanced-ai-agents/177829/ | 2026-02-10 | full |
| ACCTODAY-AITHOUGHT-2026 | AI Thought Leaders Survey 2026: Process Predictions | Accounting Today | press | https://www.accountingtoday.com/list/ai-thought-leaders-survey-2026-process-predictions | 2025-12-30 | full |
| DIGITS-ELEV8-2026 | From Bookkeeping Factory to Fractional CFO Firm: How Elev8 Built Big-Firm Output Without Adding Staff | Digits (case study) | vendor | https://digits.com/case-studies/elev8-cfo/ | 2026-07-08 | full |
| DIGITS-LINCOLN-2026 | How Lincoln Accounting Reclaimed 30+ Hours a Month by Switching to Digits | Digits (case study) | vendor | https://digits.com/case-studies/lincoln-accounting/ | 2026-09-02 | full |
| DIGITS-TFMA-2026 | How TFMA LLC Improved Workflow Efficiency by 70% with Digits | Digits (case study) | vendor | https://digits.com/case-studies/how-tfma-llc-improved-workflow-efficiency-by-70-with-digits/ | 2026-04-20 | full |
| DIGITS-ADEPT-2026 | How Adept: Accounting Principles & Solutions Reduced Bookkeeping by 75% with Digits | Digits (case study) | vendor | https://digits.com/case-studies/adept-accounting/ | 2026-03-23 | full |
| DIGITS-MANA-2025 | Mana Accounting & Advisory: Saving Hours with AI-Powered Accounting | Digits (case study) | vendor | https://digits.com/case-studies/mana-accounting-advisory-saving-hours-with-ai-powered-accounting/ | 2025-10-10 | full |
| DIGITS-WRITEMCP-2026 | Agentic Accounting With Confidence: Introducing Write MCP and Locked Period Controls | Digits | vendor | https://digits.com/blog/write-mcp/ | 2026-10-13 | full |
| DIGITS-BANKREC-2025 | Always Be Closing: Introducing AI Bank Reconciliations | Digits | vendor | https://digits.com/blog/ai-bank-reconciliations/ | 2025-11-10 | full |
| IAB-BLACKLINE-2026 | BlackLine rolls out Verity Prepare AI for finance teams | International Accounting Bulletin | press | https://www.internationalaccountingbulletin.com/news/blackline-rolls-out-verity-prepare-ai-for-finance-teams/ | 2026-07-28 | full |
| JOFA-REALLIFE-2025 | Real-life ways accountants are using AI | Journal of Accountancy (AICPA & CIMA) | professional-body | https://www.journalofaccountancy.com/issues/2025/jun/real-life-ways-accountants-are-using-ai/ | 2025-06-01 | full |
| ACCTODAY-USECASE-2024 | Making the use case for AI in accounting | Accounting Today | press | https://www.accountingtoday.com/news/making-the-use-case-for-ai-in-accounting | 2024-05-06 | full |
| ACCTODAY-WILLAI-2026 | Will AI replace accounting firms in the small biz market? | Accounting Today (opinion) | press | https://www.accountingtoday.com/opinion/will-ai-replace-accounting-firms-in-the-small-biz-market | 2026-08-24 | full |
| CFODIVE-XERO-2026 | Xero: Leaning on fractional CFOs for strategic finance | CFO Dive | press | https://www.cfodive.com/news/xero-leaning-fractional-cfos-strategic-finance/809896/ | 2026-01-16 | full |
| CPAPA-NUMERIC-2025 | AI Accounting Platform Numeric Raises $51M Series B | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/11/20/ai-accounting-platform-numeric-raises-51m-series-b/173638/ | 2025-11-20 | full |
| CPAPA-LARSON-2026 | Larson Gross Adds ScaleUp Financial Solutions in Denver | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/10/15/larson-gross-adds-scaleup-financial-solutions-in-denver/191797/ | 2026-10-15 | full |
| ARCLOW-SITE-2026 | Arclow home page (AI-native accounting practice; page undated, date is access date) | Arclow | firm | https://arclow.com | 2026-10-20 | full |
| CPACOM-CASBENCH-2026 | CAS Benchmark Survey | CPA.com | professional-body | https://cpa.com/cas-benchmark-survey | 2026-10-20 | full |
| SEC-REG210-2026 | 17 CFR 210.2-01 Qualifications of accountants, paragraph (c)(4) non-audit services (eCFR, version dated 2026-10-01) | U.S. Securities and Exchange Commission via eCFR | regulator | https://www.ecfr.gov/current/title-17/chapter-II/part-210/section-210.2-01 | 2026-10-01 | full |
| BLACKLINE-Q2-2026 | BlackLine Announces Second Quarter Financial Results (Verity Prepare general availability; early-adopter figure seen in search result only) | BlackLine investor relations | vendor | https://investors.blackline.com/news-releases/news-release-details/blackline-announces-second-quarter-financial-results-8 | 2026-08 | search-only |
| INTUIT-FY26Q2-2026 | Intuit Q2 fiscal 2026 earnings call (accounting agent usage figures seen in search result only) | MarketBeat transcript | vendor | https://www.marketbeat.com/earnings/reports/2026-2-26-intuit-inc-stock/ | 2026-02-26 | search-only |

**Counts by type:** press 33, vendor 16, job-posting 5, professional-body 3, academic 3, survey 2, firm 1, regulator 1. Total 64 (62 opened, 2 search-only).

## 6. Gaps

- **No production quality data from a CAS firm.** No override rates, error rates found in review, parallel-run results or inspection outcomes. The only independent measurement is the academic study (association, platform unnamed) and a lab study with simulated tasks. The JAR full text was not read; the abstract and two university summaries were.
- **Named customer firms for the main agent platforms.** Meridian (Pilot), Basis and Accrual/Puzzle name no customer firms in what I could open. Basis' 'about 30% of the top 25 firms' and Pilot's customer counts are company claims. The OpenAI customer page on Basis carries no publication date.
- **Firm newsrooms.** Armanino and Aprio newsrooms returned 403, Wipfli returned 429, the Baker Tilly and CohnReznick pages gave no CAS AI items, and the Cherry Bekaert page showed only the Fieldguide audit item. No CAS-specific AI announcement from Armanino, Baker Tilly, Cherry Bekaert, Wipfli or CohnReznick was found beyond the sources above.
- **Job postings.** Only one firm-side CAS posting with AI language (Aprio) was found; Kruze's has none. The other postings are from vendors. Large-firm applicant-tracking systems were not searchable through public APIs.
- **Conferences, podcasts and communities.** None opened in this run (the CAS Summit, Digital CPA and ENGAGE agendas were not retrievable per the landscape). The 2026 CAS Benchmark Survey is not yet published (due December 2026).
- **Payroll, bill pay and fractional CFO.** Evidence is vendor launches and one interview; no named firm outcome for payroll or AP agents. Fractional CFO evidence is a handful of interviews and one RAG memo bot.
- **Search-only figures.** BlackLine's early-adopter figure (up to 92% reduction in reconciliation preparation time) and Intuit's agent volume (237 million transactions in January) were seen only in search summaries.
- **Conflicts and approximations.** Pilot gives 7,000+ businesses (Feb 2026 blog) and 8,000+ (Oct 2026 posting). Botkeeper's funding appears as nearly $90 million (CPA Practice Advisor) and over $100 million (Uku); I used the former. The Stanford GSB insight page date (2025-06-09) is inferred from a page time element. The FloQast case study text does not name the firm; its file name says Miller Cooper, which I did not treat as confirmed. BlackLine's Q2 release date is approximate.
- **AICPA and IESBA independence treatment for private audit clients** was not checked; only the SEC rule text was opened.
