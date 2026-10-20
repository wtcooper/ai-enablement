# Client accounting services (CAS): practitioner discourse on AI

Run date: 2026-10-20. Wave 5. Archetype: `advisory`. Module: `client-accounting-services`. Angle: `discourse`.

Scope: outsourced bookkeeping and close, controllership, fractional CFO, payroll and bill pay delivered to clients on subscription, and the CAS delivery stack. Material is from roughly Apr 2025 to Oct 2026. Quotations are under 25 words. Everything else is paraphrased. Vendor, firm and survey figures are self-reported or vendor-published unless marked `independent`.

---

## 1. Summary

I read 43 distinct sources in full (no source here is search-only). They span press (22), podcasts (7), professional-body articles (3), surveys (4), vendors (3), conferences (2), one academic paper and one community thread. There were no regulator, standard-setter or job-posting sources, because this angle is about what practitioners say.

**What practitioners are saying**

1. **CAS is the place firms say AI pays off first, and the main route into advisory.** Withum's Jim Bourke said "AI in CAS" is where firms get "the most bang for your buck" (ACCTODAY-CASKEYS-2026). Bonadio's CAS lead describes CAS as "the quarterback between advisory and compliance" (ACCTODAY-BONADIO-2026). BILL's survey of 200+ firm leaders (late 2025) found 67% agree AI is pushing them toward CAS (BILL-AIAMBITION-2026).
2. **The discussion has moved from "assist" to "agents that do the close".** Between February and September 2026 there were launches from Pilot (autonomous AI Accountant; Meridian), Ramp (Stack), Intuit (expert-verified auto-categorization; cross-client insights) and Accrual (buying Puzzle's Close AI). CLA announced a firm-trained model with Digits. Most of this is announced or in beta. The named firm deployments are thin: CohnReznick describes a pilot phase being set up, and Elev8 CFO (a small firm) reports measured-looking but self-estimated results.
3. **The best quality evidence is a vendor benchmark, and it supports a narrow claim.** Digits reports 97.8% category accuracy for its ledger-native model on 2,000 transactions from four businesses, against 79.5% for the best one-shot general model and 79.1% for human outsourced accountants seeing the books cold (DIGITS-BENCH-2026). The gain came from knowing each business's own booking history, not from a better general model. Mercor's separate month-end close study found frontier AI far ahead of 12 junior CPAs, but the authors say the tasks favored what models do best (MERCOR-APEX-2026).
4. **Independent measurement is almost absent.** The one peer-reviewed source (STANFORD-JAR-2026) finds productivity gains and faster month-end closing, accountants stepping in when AI confidence is low, and a risk of error when people lean on non-consensus AI recommendations. I found no published firm-side error, override or parallel-run rates for CAS deliverables, apart from Elev8's own advice to run one parallel close.
5. **Adoption is wide and shallow.** 88% of surveyed professionals use AI for a client service but 30% say it is embedded as the default (INTUIT-ACCTTECH-2026, vendor-published). Only 9% of BILL's leaders report substantial results on scaling capacity without headcount (BILL-AIAMBITION-2026).
6. **The worries are review burden, liability, vendor failure and client self-service.** One community thread says reviewing AI suggestions takes almost as long as doing them. Botkeeper closed in Feb 2026 and its platform was bought three weeks later. Consultants report clients arriving having already used AI tools themselves (ACCTODAY-CATALYST-2026).

**Two insights that matter most for an advisor:** (a) the unit of change is shifting from "faster categorization" to "who owns the ledger context", meaning ledger-native or firm-trained models versus general models bolted on; (b) the review gate, not the model, is the constraint, and nobody publishes review-gate performance.

---

## 2. Use cases

Notes on the fields. `function` is `service-delivery` for every entry. Firm type is stated in `notes`. Independence: bookkeeping, payroll, bill pay and similar management-type services are commonly restricted for a firm's own audit clients. That is general background carried over from the landscape and was not verified in this run, so confirm against AICPA, SEC, PCAOB and IESBA rules before use.

```yaml
- id: advisory-client-accounting-services-01
  title: Confidence-gated transaction categorization with exception review
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: reconcile-exceptions
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Staff spend hours coding bank and card transactions across clients with different charts of accounts and house rules. Manual data cleanup is the top-cited blocker to advisory work."
  solution: "AI takes the first pass at coding each bank-feed transaction. High-confidence items post automatically and uncertain ones go to a person. The strongest reported results come from models that learn each business's own ledger history. General-purpose models without that context plateaued in the vendor's benchmark."
  outcomes:
    - lever: quality
      description: "On a 2,000-transaction benchmark, Digits' ledger-native model scored 97.8% against 79.5% for the best one-shot general model, 88.9% for the best agent with ledger look-up, and 79.1% for 12 outsourced human accountants working from the same context-free information."
      figure: "97.8% vs 79.5% vs 88.9% vs 79.1%"
      measures: "Share of 2,000 transactions from four small businesses whose assigned category matched categories reviewed by US accountants applying GAAP (source's words: graded against accountant-reviewed categories). Human baseline is a majority vote of three accountants per team, four teams."
      provenance: vendor-published
      source_ref: DIGITS-BENCH-2026
    - lever: speed
      description: "Digits reports 40 milliseconds per transaction for its model against 74 seconds for the best look-up agent. The human team averaged about 4 hours 43 minutes per 500 transactions."
      figure: "40 ms vs 74 s per transaction; 4 h 43 min per 500 (about 34 s each)"
      measures: "Processing time per transaction in the same vendor benchmark; the human figure is average time to categorize each team's 500-transaction allocation."
      provenance: vendor-published
      source_ref: ACCTODAY-AIBENCH-2026
    - lever: quality
      description: "Intuit says bank-feed categorization accuracy rose from about 78% on the old feed to nearly 88% on the new one. It is also launching expert-verified auto-categorization, where only high-confidence items post automatically."
      figure: "about 78% to nearly 88%"
      measures: "Bank-feed transaction categorization accuracy, old versus new feed. The article does not state how accuracy is measured or the denominator."
      provenance: vendor-published
      source_ref: CPAPA-INTUITCONNECT-2026
    - lever: quality
      description: "Peer-reviewed field data on an AI-enabled accounting platform: accountants selectively intervene when AI confidence scores are low. In a framed experiment AI help raised classification accuracy on average, but reliance on non-consensus AI recommendations can increase error risk. No numeric effect sizes in the abstract."
      figure: none published in the abstract
      measures: "Survey of 277 accountants, platform data on 79 SMEs (200,000+ transaction records), and a framed field experiment, per the abstract."
      provenance: independent
      source_ref: STANFORD-JAR-2026
  prerequisites:
    - "Clean history in the client's general ledger so the model can learn house rules"
    - "Confidence scores exposed to reviewers"
    - "A defined threshold for auto-posting versus review"
  risks_and_guardrails:
    - "Failures cluster on recurring merchants and on categories defined by the business, such as near-duplicate categories and payment-processor clearing accounts (DIGITS-BENCH-2026, ACCTODAY-AIBENCH-2026)."
    - "Reliance on non-consensus AI recommendations can increase error risk (STANFORD-JAR-2026)."
    - "A practitioner thread argues that even 97% accuracy leaves hundreds of errors a year per client and that professional responsibility forces full review (BEANCOUNT-REVIEWBURDEN-2026, anecdotal)."
    - "Intuit's expert-verified categorization is off by default for firm-billed clients; the accountant decides when to switch it on (CPAPA-INTUITCONNECT-2026)."
  human_checkpoints:
    - "Review of low-confidence and flagged items"
    - "Periodic sampling of auto-posted items"
    - "Accountant approval before the vendor service is enabled for a client"
  role_evolution: "Staff move from keying categories to reviewing exceptions and maintaining the client's categorization conventions (STANFORD-JAR-2026 describes a shift from routine data entry toward communication and quality-assurance tasks)."
  evidence_grade: A
  sources:
    - { ref: DIGITS-BENCH-2026, title: "Breaking: AI Can't Close Your Books From the Outside", publisher: Digits, type: vendor, url: "https://digits.com/blog/ai-cant-close-books-from-outside/", date: "2026-10-07", access: full, locator: "Sections 'No context', 'With access to the ledger', 'Native to the ledger'" }
    - { ref: ACCTODAY-AIBENCH-2026, title: "AI beats human accountants at monthly close, transaction categorization", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization", date: "2026-10-16", access: full, locator: "Section 'The Digits benchmark' and 'Don't count humans out just yet'" }
    - { ref: CPAPA-INTUITCONNECT-2026, title: "Intuit Connect ON: What You Need to Know About the Latest Platform Innovations", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/06/26/intuit-connect-on-what-you-need-to-know-about-the-latest-platform-innovations/185810/", date: "2026-06-26", access: full, locator: "Sections 'QuickBooks: Foundational Fixes' and 'Continuously Clean Books'" }
    - { ref: STANFORD-JAR-2026, title: "Human + AI in Accounting: Early Evidence from the Field", publisher: Journal of Accounting Research (via Stanford GSB), type: academic, url: "https://www.gsb.stanford.edu/index.php/node/629989", date: "2026-06", access: full, locator: "Abstract; JAR vol 64(3), pp 1333-1373" }
    - { ref: BEANCOUNT-REVIEWBURDEN-2026, title: "I Adopted AI Bookkeeping for Time Savings, But Reviewing Every Transaction Takes Just as Long", publisher: Beancount and Plain-Text Accounting Forum, type: community, url: "https://beancount.io/forum/t/i-adopted-ai-bookkeeping-for-time-savings-but-reviewing-every-transaction-takes-just-as-long/1823", date: "2026-03-22", access: full, locator: "Original post and replies 1-3" }
  last_reviewed: "2026-10-20"
  notes: "Digits and Intuit are vendors. The Digits benchmark is vendor-run on four small businesses and is not a firm production metric; no independent replication found. Graded A because the named vendor reports measured figures for the core CAS step (not an adjacent process). The AT article says the one-shot spread among top models is within sampling error of the human baseline (0.4 points) and that the look-up agents had access to booking history the humans lacked. Botkeeper's CEO said its platform was capable of coding 80%+ of transactions at 98% accuracy (quoted in CPAPA-XENDOO-2026 and UKU-BOTKEEPER-2026); that is a vendor claim with no stated denominator, from a company that then closed. The community thread is pseudonymous and anecdotal and is used only for the objection. Independence: restricted-service background applies when the firm audits the client (unverified)."

- id: advisory-client-accounting-services-02
  title: Ledger-native AI platform replaces month-end report production with a continuous close
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: other
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "A small firm spent about two-thirds of each month producing financials (exporting trial balances, cleaning data, formatting and emailing PDFs), and every new bookkeeping client added production work."
  solution: "The firm moved its clients to an AI-native ledger with real-time transaction visibility and client collaboration inside the platform. Close work shrank, year-to-date numbers became available mid-month, and freed time went to advisory and marketing."
  outcomes:
    - lever: speed
      description: "Monthly close time fell from 18 days to five for the firm's clients. The owner also says he could close all 27 migrated clients within two days if needed."
      figure: "18 days to 5 days"
      measures: "Owner's reported close cycle length across the 27 migrated clients (source's words: monthly close time fell from 18 days to five)."
      provenance: self-reported
      source_ref: CPAPA-ELEV8-2026
    - lever: capacity
      description: "Monthly bookkeeping work fell from roughly 108 hours to about 20, returning nearly 90 hours a month. The firm supports 37 client engagements with no staff accountant."
      figure: "about 108 h to about 20 h per month"
      measures: "Owner's estimate of total monthly hours on bookkeeping and financial-statement production (source says 'approximately' and 'roughly')."
      provenance: self-reported
      source_ref: CPAPA-ELEV8-2026
  prerequisites:
    - "Migration of historical balances, charts of accounts, payroll connections and bank feeds (27 clients in about 40 hours, per the owner)"
    - "An API or platform capable of automated statement generation"
    - "A small starting cohort"
  risks_and_guardrails:
    - "Owner's advice: start with five clients, run one parallel close, confirm the numbers reconcile (CPAPA-ELEV8-2026)."
    - "The page reads as a vendor case study and sponsorship is not stated, so independence of the account is unclear."
  human_checkpoints:
    - "Parallel close on a starter cohort before cut-over"
    - "Owner review of closed books"
  role_evolution: "The owner says he no longer does bookkeeping and now focuses on interpreting data for clients and advisory work (CPAPA-ELEV8-2026)."
  evidence_grade: B
  sources:
    - { ref: CPAPA-ELEV8-2026, title: "How an AI-Native Accounting Platform Helped One Solo Firm Reclaim 90 Hours a Month and Scale Advisory Without Hiring", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/07/21/how-an-ai-native-accounting-platform-helped-one-solo-firm-reclaim-90-hours-a-month-and-scale-advisory-without-hiring/187093/", date: "2026-07-21", access: full, locator: "Sections 'Reinventing the Month-End Close' and 'What Saving 90 Hours Made Possible'" }
  last_reviewed: "2026-10-20"
  notes: "Small solo firm (Elev8 CFO and Elevate Tax & Accounting, El Paso), not a top-100 or mid-market firm. The platform is Digits (a vendor). Single case; figures are the owner's estimates, so B not A under the 2026-10-17 rule. Pattern is `other`: continuous close on an AI-native ledger with automated reporting, no agent. Independence is not an issue for this firm as described."

- id: advisory-client-accounting-services-03
  title: Agent-prepared reconciliations, journal entries and close workpapers with human approval gates
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, review-assurance, data-reporting]
  pattern: draft-review-loop
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "Most CAS staff time goes to AP, reconciliations and financial statements. Clients expect a close in about 10 to 12 days, and staff are scarce."
  solution: "An agent loads client memory and the firm's standard procedure (a 'skill'), pulls ledger and file data, proposes a plan, drafts the workpaper and the journal entry, and posts only after a person approves. CohnReznick describes a pilot with a handful of clients aimed at categorization and classification, recommended or drafted journal entries, and a dynamic close checklist, focused on senior accountants."
  outcomes:
    - lever: capacity
      description: "CohnReznick's CAS leader says he is looking at improving capacity 'by 50% or even more' once reconciliation and transactional steps are assisted. This is an expectation, not a result."
      figure: "50% or more (expectation)"
      measures: "Leader's expectation of CAS team capacity improvement; no denominator given."
      provenance: self-reported
      source_ref: ACCTODAY-COHNPOD-2026
    - lever: quality
      description: "In Mercor's simulated month-end close tasks, a frontier model scored 100% on all 20 attempts and humans mostly scored below 50%. Mercor says the tasks tested what models do best and removed client context and colleagues."
      figure: "20 of 20 attempts scored 100% (AI) vs generally below 50% (12 junior CPAs)"
      measures: "Rubric-item scores on four simulated close scenarios (13 to 22 rubric items per task); AI attempts per the AT article, humans' scores per the same article."
      provenance: independent
      source_ref: ACCTODAY-AIBENCH-2026
  prerequisites:
    - "A stable tech stack and core client base (CohnReznick says it waited three years for this)"
    - "Firm procedures written down as editable skills or checklists"
    - "Connectors to the client's ledger"
    - "Staff certification and training"
  risks_and_guardrails:
    - "Nothing posts to a client's general ledger without explicit human authorization (Ramp's stated design, ACCTODAY-RAMPSTACK-2026)."
    - "Write five controls down before any agent touches a production close: agent inventory with a named owner, replayable evidence, sign-off gates scaled to risk, read SOC reports for AI coverage, and exception metrics with a kill threshold (CPAPA-AGENTSCLOSE-2026)."
    - "In Mercor's study, in three of four imperfect AI-assisted sessions the model had the right figure at some point but it did not reach the final answer (ACCTODAY-AIBENCH-2026)."
  human_checkpoints:
    - "Approval of the agent's plan before execution"
    - "Review and approval of the drafted entry and workpaper"
    - "Ongoing QC"
  role_evolution: "Senior accountants are expected to move up a layer to more review and more client time (ACCTODAY-COHNPOD-2026). Staff become orchestrators of AI-prepared work (ACCTODAY-TRENDS-2026, Deloitte contributor)."
  evidence_grade: B
  sources:
    - { ref: ACCTODAY-COHNPOD-2026, title: "The meeting of CAS and AI (On the Air podcast with Kane Polakoff, Intuit-sponsored)", publisher: Accounting Today, type: podcast, url: "https://www.accountingtoday.com/podcast/at-intuit-sponsored-podcast-03-16", date: "2026-03-16", access: full, locator: "Transcript 00:32 to 02:56 (pilot), 07:10 to 08:56 (capacity and close)" }
    - { ref: ACCTODAY-RAMPSTACK-2026, title: "Ramp launches Stack, made specifically for accounting firms", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/ramp-launches-stack-made-specifically-for-accounting-firms", date: "2026-06-03", access: full, locator: "Paragraphs 3-10 (skills, plan approval, posting)" }
    - { ref: ACCTODAY-ACCRUAL-2026, title: "Accrual acquires Puzzle's tech to add to their CAS offering", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/accrual-acquires-puzzles-tech-to-add-to-their-cas-offering", date: "2026-09-02", access: full, locator: "Paragraphs 1-4" }
    - { ref: ACCTODAY-AIBENCH-2026, title: "AI beats human accountants at monthly close, transaction categorization", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization", date: "2026-10-16", access: full, locator: "Section 'The Mercor benchmark'" }
    - { ref: MERCOR-APEX-2026, title: "Human Baselines for Benchmarks: AI Now Outperforms Junior Accountants", publisher: Mercor, type: vendor, url: "https://www.mercor.com/blog/human-baselines-for-benchmarks-ai-now-outperforms-junior-accountants/", date: "2026-10-01", access: full, locator: "Sections 'What we did' and 'What do these results mean'" }
    - { ref: CPAPA-AGENTSCLOSE-2026, title: "Before You Let the Agents Run the Close: Five Controls to Put in Writing First", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/188496/", date: "2026-08-13", access: full, locator: "Controls 1 to 5" }
    - { ref: ACCTODAY-TRENDS-2026, title: "How will technology shape accounting trends in 2026?", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/how-will-technology-shape-accounting-trends-in-2026", date: "2026-01-09", access: full, locator: "Contributor quote from Will Bible, Deloitte" }
  last_reviewed: "2026-10-20"
  notes: "Firm: CohnReznick is a top-100 firm; the podcast is Intuit-sponsored. The pilot is described in the present and future tense as being set up ('going through a pilot phase first, identifying five to seven clients'), so maturity is `piloting` at most and the grade rests on one practitioner interview. Ramp Stack (vendor) and Accrual/Puzzle (vendor) are announced products; Stack's first ledger is QuickBooks Online with NetSuite and Sage Intacct slated. Accrual's CAS offering is in early access with broader availability planned by end of 2026, and the Puzzle deal was expected to close in the coming weeks. The Mercor measurement is a simulated-task study (an adjacent measure) and caps this entry at B. Mercor is a commercial AI-data company and its judge model was the same model family as the tested one (98% agreement on eight hand-graded submissions); the provenance label `independent` means third party to the vendors and firms, not peer-reviewed. The KPMG-derived 42% readiness figure quoted in CPAPA-AGENTSCLOSE-2026 may be conflated, per the landscape; not used. Independence: management-type services restricted for the firm's attest clients (unverified)."

- id: advisory-client-accounting-services-04
  title: Firm-trained proprietary model deployed across a CAS client base
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, expert-judgment]
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Generic AI features bolted onto old accounting software do not reflect a firm's specialization and judgment, and most mid-market firms cannot fund their own platform."
  solution: "CLA announced it will work with Digits to train its own model on the firm's accumulated data and experience, deploy it starting with its client accounting and advisory practice, and offer it as an option within service levels. CLA plans to deploy it to thousands of current and future clients over three years."
  outcomes:
    - lever: growth
      description: "none published"
      figure: none
      measures: "No results reported; announcement only."
      provenance: self-reported
      source_ref: ACCTODAY-CLADIGITS-2026
  prerequisites:
    - "Decades of firm data and industry specialization to train on"
    - "A platform partner supplying model-training infrastructure"
    - "Client data rights"
  risks_and_guardrails:
    - "CLA declined to discuss financial terms, platform architecture or infrastructure (ACCTODAY-CLADIGITS-2026), so data handling and model governance are not public."
  human_checkpoints:
    - "Not described in the source"
  role_evolution: "Not described in the source."
  evidence_grade: C
  sources:
    - { ref: ACCTODAY-CLADIGITS-2026, title: "CLA working with Digits to develop proprietary AI model", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/cla-working-with-digits-to-develop-proprietary-ai-model", date: "2026-07-21", access: full, locator: "Paragraphs 1-4" }
  last_reviewed: "2026-10-20"
  notes: "CLA is described by the source as a Top 20 firm (mid-market and national). Digits is a vendor. Announcement only, with no evidence of use. The decision between build, GL-native and integrated provider is a live question among CAS leaders (ACCTODAY-COHNPOD-2026, 03:58 to 04:36)."

- id: advisory-client-accounting-services-05
  title: AI-assisted management reporting with variance commentary and KPI dashboards
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [document-production, data-reporting]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "CAS teams compile monthly statements by hand and add client commentary late in the cycle. Clients like dashboards but they used to take a lot of time to build."
  solution: "AI finds variances in a client's books and drafts an explanation. Reporting tools generate the package and draft commentary from variances, trends and KPIs, and real-time dashboards show the metrics the client wants. Staff review and edit."
  outcomes:
    - lever: speed
      description: "none published. Withum's Bourke says dashboards 'took a lot of time' at first and that using AI to deliver real-time dashboards is how a CAS practice differentiates; Bonadio says AI helps it deliver services faster and build key metrics for owners."
      figure: none
      measures: "No measured outcome in either source."
      provenance: self-reported
      source_ref: ACCTODAY-CASKEYS-2026
  prerequisites:
    - "Current ledger data"
    - "Agreed client KPIs"
    - "Review step before client delivery"
  risks_and_guardrails:
    - "Over-automating without oversight can miss categorization errors or misread context, especially in client-facing content (JOFA-CASAI-2026)."
    - "Explanations an AI proposes for a variance are hypotheses for a reviewer, not findings (ACCTODAY-CASKEYS-2026 says AI would 'probably' come up with one)."
  human_checkpoints:
    - "Preparer or manager review of commentary before delivery"
  role_evolution: "Time shifts from assembling the package to interpreting it with the client (ACCTODAY-BONADIO-2026; JOFA-CASAI-2026)."
  evidence_grade: B
  sources:
    - { ref: ACCTODAY-CASKEYS-2026, title: "CAS delivers 'the keys to the kingdom'", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom", date: "2026-05-22", access: full, locator: "Section 'AI in CAS'" }
    - { ref: ACCTODAY-BONADIO-2026, title: "CAS and outsourced accounting fuel Bonadio Group", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/cas-and-outsourced-accounting-fuel-bonadio-group", date: "2026-07-30", access: full, locator: "Paragraphs 5-7" }
    - { ref: JOFA-CASAI-2026, title: "Simple but effective AI use cases for CAS", publisher: Journal of Accountancy (AICPA and CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/", date: "2026-01-01", access: full, locator: "Use-case category 'Reporting' and 'Common pitfalls'" }
  last_reviewed: "2026-10-20"
  notes: "Firms: Withum (top-100) and Bonadio (Top 50 per the source). JOFA-CASAI-2026 is by two CohnReznick CAS leaders (top-100) and names reporting tools such as Reach Reporting, Qvinci and Spotlight Reporting; that is tool guidance, not a measured deployment. Neither named firm states a deployed workflow or measurement, so B is generous; a stricter reading is C. Independence background applies if the firm audits the client (unverified)."

- id: advisory-client-accounting-services-06
  title: Client-facing AI finance Q and A, forecasts and benchmarked scenario planning on live ledger data
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [client-interaction, expert-judgment, data-reporting]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Clients want forward-looking insight, not a historical package thrown over the fence, and advisory capacity is limited by data cleanup and staffing."
  solution: "Platform vendors are adding conversational answers grounded in the client's own ledger, AI cash-flow forecasts benchmarked against similar businesses, and scenario modeling. CohnReznick's CAS leader describes AI producing a 'script' of insights and benchmark data for advisory conversations, but expects that later."
  outcomes:
    - lever: experience
      description: "Intuit reports conversational business intelligence arriving in late July 2026, with forecasts and scenario planning. Separately, 51% of surveyed professionals name financial forecasting as a top AI client-service use."
      figure: "51%"
      measures: "Percentage listing financial forecasting among top client-service uses of AI in Intuit's survey of 725 US accounting and bookkeeping professionals (May 2026). The article does not say whether the base is all 725 or the 88% who use AI for a client service."
      provenance: vendor-published
      source_ref: INTUIT-ACCTTECH-2026
  prerequisites:
    - "Reliable, categorized ledger data"
    - "Client permission for AI use on their data"
    - "A defined advisory deliverable"
  risks_and_guardrails:
    - "Three in five respondents say clients ask for proof of AI data protection always or frequently, yet only one in three proactively explain how AI supports their work (INTUIT-ACCTTECH-2026)."
    - "A CohnReznick CAS leader expects the advisory script capability to take longer than the transactional steps (ACCTODAY-COHNPOD-2026, 09:50 to 10:46)."
  human_checkpoints:
    - "Accountant interprets and presents insights"
    - "Accountant sets assumptions in scenarios"
  role_evolution: "Staff are expected to hold more analytical and client-conversation roles as compliance work automates (ACCTODAY-COHNPOD-2026, 11:52 to 12:41)."
  evidence_grade: C
  sources:
    - { ref: CPAPA-INTUITCONNECT-2026, title: "Intuit Connect ON: What You Need to Know About the Latest Platform Innovations", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/06/26/intuit-connect-on-what-you-need-to-know-about-the-latest-platform-innovations/185810/", date: "2026-06-26", access: full, locator: "Section 'AI that Actually Knows Your Client's Books'" }
    - { ref: INTUIT-ACCTTECH-2026, title: "The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future", publisher: CPA Practice Advisor (Intuit QuickBooks survey), type: survey, url: "https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807", date: "2026-07-02", access: full, locator: "Sections 'Are You a Firm of the Future' and 'Trust and Transparency'" }
    - { ref: ACCTODAY-COHNPOD-2026, title: "The meeting of CAS and AI", publisher: Accounting Today, type: podcast, url: "https://www.accountingtoday.com/podcast/at-intuit-sponsored-podcast-03-16", date: "2026-03-16", access: full, locator: "Transcript 09:50 to 10:46" }
    - { ref: ACCTODAY-CASSUMMIT-2026, title: "CAS Summit Virtual 2026: Session abstracts (CAS 3.0; Deepening Adoption of AI and Automation)", publisher: Accounting Today, type: conference, url: "https://www.accountingtoday.com/cas-summit-virtual-2026-session", date: "2026-08-13", access: full, locator: "Session abstracts only; no talk content" }
    - { ref: CPAPA-PILOTAI-2026, title: "Pilot Rolls Out Fully Autonomous AI Accountant", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/02/04/pilot-rolls-out-fully-autonomous-ai-accountant/177453/", date: "2026-02-04", access: full, locator: "Feature list, 'Financial insights on demand'" }
  last_reviewed: "2026-10-20"
  notes: "Vendors: Intuit, Pilot. The conference source is an abstract of a session already held, so it is a signal only and does not support the grade. Intuit's conversational and cash-flow features were announced for late July 2026 (beta or release status not confirmed afterward). Firm: CohnReznick (top-100), future tense."

- id: advisory-client-accounting-services-07
  title: Fractional CFO drafting, oversight and dashboards with AI
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [expert-judgment, document-production, client-interaction]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Fractional CFOs spend scarce senior time on recurring process, technical memos and oversight of AP and AR, and mid-market clients need part-time finance leadership."
  solution: "A San Diego fractional CFO uses AI to draft technical memos, to speed AP and AR invoicing work he oversees, and to show clients how to build dashboards and drill into data with tools such as Claude. He says his methods changed 'dramatically' in about three months."
  outcomes:
    - lever: capacity
      description: "none published for the firm. Context: interim C-suite requests are up 151% since 2021 and interim CFO demand is up 14% year on year, per a Business Talent Group report cited by CFO Dive."
      figure: "151% since 2021; 14% year on year (market context)"
      measures: "BTG's 2026 High-End Independent Talent Report: growth in requests for interim C-suite leaders since 2021; growth in interim CFO demand year on year. The BTG report was not opened; cited via CFO Dive."
      provenance: independent
      source_ref: CFODIVE-FRACTIONAL-2026
  prerequisites:
    - "Systems and processes already set up for the client so ongoing work is recurring"
    - "Client comfort with AI"
  risks_and_guardrails:
    - "He says some clients could use AI for the accounting work and some probably will, though he has been surprised by the lack of desire so far (CFODIVE-FRACTIONAL-2026)."
    - "He charges hourly, so AI-driven time savings are a pricing question for him (CFODIVE-FRACTIONAL-2026)."
  human_checkpoints:
    - "CFO owns the memos and outputs"
  role_evolution: "He sees helping the company adopt and learn AI as 'a new responsibility for the CFO' (CFODIVE-FRACTIONAL-2026)."
  evidence_grade: B
  sources:
    - { ref: CFODIVE-FRACTIONAL-2026, title: "Fractional CFOs see demand surge in AI age", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/fractional-cfos-see-demand-surge-ai-age/827264/", date: "2026-08-06", access: full, locator: "Sections 'AI opens gates to on-demand talent' and 'An AI-enabled finance future'" }
  last_reviewed: "2026-10-20"
  notes: "Hope Financial Consulting is a small boutique, not a top-100 or mid-market accounting firm. Single practitioner interview with no figures for the firm. Independence is not discussed."

- id: advisory-client-accounting-services-08
  title: Client onboarding and migration automation
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, coordination-scheduling]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Onboarding suffers from inconsistent data collection and slow back-and-forth, and migration is often the biggest obstacle to modernizing."
  solution: "Intelligent forms and automated document requests track onboarding tasks and flag missing information. Platform automation and AI-assisted workflows move balances, charts of accounts, payroll connections and bank feeds. Vendors also pitch AI that onboards a client and closes historical books."
  outcomes:
    - lever: speed
      description: "One firm migrated 27 clients in about 40 hours. The owner estimates the same migration would have taken roughly twice the effort using traditional methods."
      figure: "27 clients in about 40 hours"
      measures: "Owner's estimate of hours to migrate 27 clients (balances, charts of accounts, payroll connections, bank feeds); the 'twice the effort' comparison is the owner's estimate."
      provenance: self-reported
      source_ref: CPAPA-ELEV8-2026
  prerequisites:
    - "Source-system access"
    - "Standard onboarding checklist"
    - "A small pilot cohort"
  risks_and_guardrails:
    - "Pilot's claim that it 'closes historical books' and onboards clients is a vendor claim (CPAPA-PILOTMERIDIAN-2026)."
    - "A guide advises a 30 to 60 day pilot on one workflow, measuring time saved, added review time, error reduction and client feedback (JOFA-CASAI-2026)."
  human_checkpoints:
    - "Reconciliation check against source before go-live (parallel close)"
  role_evolution: "Implementation specialists per accounting package are worth investing in (JOFA-CASTIPS-2025, BST and Co.)."
  evidence_grade: B
  sources:
    - { ref: CPAPA-ELEV8-2026, title: "How an AI-Native Accounting Platform Helped One Solo Firm Reclaim 90 Hours a Month and Scale Advisory Without Hiring", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/07/21/how-an-ai-native-accounting-platform-helped-one-solo-firm-reclaim-90-hours-a-month-and-scale-advisory-without-hiring/187093/", date: "2026-07-21", access: full, locator: "Section 'Making Migration Manageable'" }
    - { ref: JOFA-CASAI-2026, title: "Simple but effective AI use cases for CAS", publisher: Journal of Accountancy (AICPA and CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/", date: "2026-01-01", access: full, locator: "Use-case category 'Client onboarding' and Step 3" }
    - { ref: CPAPA-PILOTMERIDIAN-2026, title: "Pilot Says New AI Accounting Platform Meridian Runs Monthly Close From Start to Finish", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/06/23/pilot-says-new-ai-accounting-platform-meridian-runs-monthly-close-from-start-to-finish/185541/", date: "2026-06-23", access: full, locator: "Paragraphs 2-4" }
    - { ref: JOFA-CASTIPS-2025, title: "Tips for providing the CAS services clients want", publisher: Journal of Accountancy (AICPA and CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2025/jul/tips-for-providing-the-cas-services-clients-want/", date: "2025-07-01", access: full, locator: "Section 'Build your technology stack wisely'" }
  last_reviewed: "2026-10-20"
  notes: "Small firm (Elev8) for the migration figure; Pilot and Intuit are vendors (Intuit's Intelligent Onboarding was announced as beta from late July 2026, per CPAPA-INTUITCONNECT-2026). The AI share of the migration time saving is not separated from platform automation in the source. Independence background applies for attest clients (unverified)."

- id: advisory-client-accounting-services-09
  title: AI-chased client questions and missing documents inside the ledger or portal
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [client-interaction, coordination-scheduling]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Close cycles stretch when clients take days to answer transaction questions or provide documents, and email chains pile up."
  solution: "Transaction questions and answers happen in the transaction feed or a collaboration inbox, and AI handles follow-up chasing for missing documents and open questions."
  outcomes:
    - lever: speed
      description: "The Elev8 owner says moving bookkeeping questions into the platform let clients respond faster and cut delays that used to extend the close by more than a week. The article attributes this to platform collaboration, not specifically to AI."
      figure: "delays of more than a week reduced (no figure)"
      measures: "Owner's description of close-cycle delay from slow client replies; not quantified."
      provenance: self-reported
      source_ref: CPAPA-ELEV8-2026
  prerequisites:
    - "Client collaboration inside the platform"
    - "Defined escalation rules"
  risks_and_guardrails:
    - "Intuit says the collaboration inbox lets Intuit Intelligence handle follow-up chasing automatically; its availability status was not stated (CPAPA-INTUITCONNECT-2026)."
  human_checkpoints:
    - "Accountant handles escalations and judgment calls"
  role_evolution: "Staff stop writing repeat follow-ups (CPAPA-ELEV8-2026)."
  evidence_grade: C
  sources:
    - { ref: CPAPA-INTUITCONNECT-2026, title: "Intuit Connect ON: What You Need to Know About the Latest Platform Innovations", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/06/26/intuit-connect-on-what-you-need-to-know-about-the-latest-platform-innovations/185810/", date: "2026-06-26", access: full, locator: "Section 'Intuit Accountant Suite: The Firm's Control Tower'" }
    - { ref: CPAPA-ELEV8-2026, title: "How an AI-Native Accounting Platform Helped One Solo Firm Reclaim 90 Hours a Month and Scale Advisory Without Hiring", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/07/21/how-an-ai-native-accounting-platform-helped-one-solo-firm-reclaim-90-hours-a-month-and-scale-advisory-without-hiring/187093/", date: "2026-07-21", access: full, locator: "Section 'Reinventing the Month-End Close', paragraph on client communication" }
    - { ref: ACCOUNTEX-2026, title: "Accountex London 2026: product roundup", publisher: Financial Accountant (IFA), type: press, url: "https://financialaccountant.co.uk/blog/accountex-london-2026-product-roundup/", date: "2026-05-19", access: full, locator: "Section 'Intuit QuickBooks'" }
  last_reviewed: "2026-10-20"
  notes: "Vendors (Intuit) and a small firm (Elev8). Graded C because the AI-specific contribution is not isolated. The Accountex roundup describes Intuit Accountant Suite questions and answers in the transaction feed (UK launch context)."

- id: advisory-client-accounting-services-10
  title: AI invoice capture, coding, approval routing and payment scheduling (bill pay)
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Manual entry of vendor invoices and payment coordination create bottlenecks, with workflows that differ by client, industry and system."
  solution: "AI-enabled AP tools extract invoice details from PDFs and email, categorize expenses, match to purchase orders, route multi-level approvals and schedule payments based on cash-flow predictions."
  outcomes:
    - lever: capacity
      description: "none published. In Intuit's survey, invoicing and payments is the top firm-operations use of AI."
      figure: "53%"
      measures: "Percentage of surveyed professionals listing invoicing and payments among top firm-operations uses of AI (Intuit survey, n=725, May 2026); base not specified in the article. This is a firm-operations use, not CAS delivery to clients."
      provenance: vendor-published
      source_ref: INTUIT-ACCTTECH-2026
  prerequisites:
    - "AP platform integrated to the client's ledger and bank"
    - "Approval matrix"
  risks_and_guardrails:
    - "Bill's executive predicts pre-processing (sourcing documents, extraction, categorization) will see the largest drop in human involvement (ACCTODAY-BIGYEAR-2026); this is a vendor forecast."
  human_checkpoints:
    - "Approval of payments"
    - "Review of exceptions"
  role_evolution: "Not described beyond general capacity-release claims."
  evidence_grade: C
  sources:
    - { ref: JOFA-CASAI-2026, title: "Simple but effective AI use cases for CAS", publisher: Journal of Accountancy (AICPA and CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/", date: "2026-01-01", access: full, locator: "Use-case category 'Spend and expense management'" }
    - { ref: INTUIT-ACCTTECH-2026, title: "The 2026 Accountant Technology Survey", publisher: CPA Practice Advisor (Intuit survey), type: survey, url: "https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807", date: "2026-07-02", access: full, locator: "Section 'Are You a Firm of the Future'" }
    - { ref: ACCTODAY-BIGYEAR-2026, title: "A big year for AI in accounting", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/a-big-year-for-ai-in-accounting", date: "2026-02-04", access: full, locator: "Section 'Agents, integrations and data flows'" }
  last_reviewed: "2026-10-20"
  notes: "Vendors named as examples by JofA (written by CohnReznick CAS leaders): BILL, Tipalti, Ramp. No named-firm deployment or measurement found. A CPA.com webinar abstract lists vendor onboarding, bill pay, reconciliation and exception management as agentic AI starting points with Aprio and BILL speakers, but the page is undated and is used only as a lead (see Gaps). Independence: AP and payment processing are commonly restricted for attest clients (unverified)."

- id: advisory-client-accounting-services-11
  title: Payroll entry preparation and liability tie-out by agent
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Payroll journal entries need employer and employee cost splits and department allocations, and payroll liabilities have to be tied out each period."
  solution: "An agent pulls payroll reports, computes splits and allocations, and drafts the entry for approval and posting. Another vendor says its AI ticks and ties payroll liabilities."
  outcomes:
    - lever: speed
      description: "none published"
      figure: none
      measures: "Product announcements only."
      provenance: vendor-published
      source_ref: ACCTODAY-RAMPSTACK-2026
  prerequisites:
    - "Connected payroll data"
    - "Documented account mappings"
  risks_and_guardrails:
    - "Nothing posts without human authorization in Ramp's stated design (ACCTODAY-RAMPSTACK-2026)."
  human_checkpoints:
    - "Approval of workpaper and entry"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: ACCTODAY-RAMPSTACK-2026, title: "Ramp launches Stack, made specifically for accounting firms", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/ramp-launches-stack-made-specifically-for-accounting-firms", date: "2026-06-03", access: full, locator: "Paragraph 3 and the payroll example in paragraph 9" }
    - { ref: CPAPA-PILOTAI-2026, title: "Pilot Rolls Out Fully Autonomous AI Accountant", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/02/04/pilot-rolls-out-fully-autonomous-ai-accountant/177453/", date: "2026-02-04", access: full, locator: "Paragraph on local bookkeepers and accountants" }
  last_reviewed: "2026-10-20"
  notes: "Vendors only. This entry covers payroll accounting, not running payroll or filing payroll taxes; I found no AI-specific discourse on running payroll itself (see Gaps). Independence: payroll services are commonly restricted for attest clients (unverified)."

- id: advisory-client-accounting-services-12
  title: AI cleanup and audit of historical or messy books (catch-up work)
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, review-assurance]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "New clients arrive with years of messy data, duplicates, mispostings and unreconciled periods that must be fixed before a clean close is possible."
  solution: "Agents audit an existing ledger for duplicates, mispostings and unreconciled periods and draft correcting entries. Excel-integrated agents clean and standardize raw exports and reconcile them to control totals, logging each change."
  outcomes:
    - lever: speed
      description: "In a JofA walkthrough, an Excel agent cleaned, validated and reconciled a simulated 59,157-row general ledger to the trial balance in about 10 minutes on average. This is a simulated audit-setting demonstration, not a CAS deployment."
      figure: "about 10 minutes for 59,157 rows"
      measures: "Average time for the full clean, validate and reconcile process on the authors' simulated dataset."
      provenance: self-reported
      source_ref: JOFA-EXCEL-2026
  prerequisites:
    - "A skill or procedure that preserves the source file, plans before acting and logs every change"
    - "Control totals to reconcile to"
  risks_and_guardrails:
    - "The authors say the human approval step reduces but does not eliminate the risk of inappropriate data changes (JOFA-EXCEL-2026)."
    - "Botkeeper's CEO claimed its platform could clean years of messy data in minutes; the company then shut down (CPAPA-XENDOO-2026)."
  human_checkpoints:
    - "Approval of the cleaning plan before execution"
    - "Review of the modifications log"
  role_evolution: "Not described for CAS."
  evidence_grade: C
  sources:
    - { ref: ACCTODAY-RAMPSTACK-2026, title: "Ramp launches Stack, made specifically for accounting firms", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/ramp-launches-stack-made-specifically-for-accounting-firms", date: "2026-06-03", access: full, locator: "Paragraph 3 (audit a client's existing books)" }
    - { ref: JOFA-EXCEL-2026, title: "Using an Excel agent to clean, validate, and reconcile data", publisher: Journal of Accountancy (AICPA and CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/oct/using-an-excel-agent-to-clean-validate-and-reconcile-data/", date: "2026-10-01", access: full, locator: "Introduction and Steps 1-3" }
    - { ref: CPAPA-XENDOO-2026, title: "Xendoo Buys Botkeeper Infinite; AI Platform Will Remain Active and Supported", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/02/28/xendoo-buys-botkeeper-infinite-ai-platform-will-remain-active-and-supported/179027/", date: "2026-02-28", access: full, locator: "Quoted CEO note in the related-article block" }
  last_reviewed: "2026-10-20"
  notes: "The JofA figure comes from an audit-focused simulation, so it is an adjacent measure; the grade is capped below B. The Excel-agent topic is routed to assurance for the audit use. Vendors: Ramp, Botkeeper (closed, then platform bought by Xendoo). Independence: bookkeeping cleanup and system work are commonly restricted for attest clients (unverified)."

- id: advisory-client-accounting-services-13
  title: AI-native provider delivers autonomous end-to-end bookkeeping and close
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, data-reporting, client-interaction]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Traditional firms rely on laborious manual processes, so speed, consistency and scale suffer; three in four firms are said to turn away clients they lack capacity to serve (a vendor statement)."
  solution: "Pilot says its AI Accountant onboards a business, configures systems, closes historical books, handles edge cases and produces full financial statements with an audit trail. In June 2026 it released Meridian for accounting firms, which closes books end to end in the firm's own ledger and returns review-ready financials."
  outcomes:
    - lever: capacity
      description: "Pilot says Meridian was built inside Pilot and has closed more than 187,000 months of books for over 8,000 businesses, and claims it changes the unit economics of the work."
      figure: "187,000+ months of books; 8,000+ businesses"
      measures: "Count of client-months closed and number of businesses, as stated by the vendor. No accuracy or override rate published."
      provenance: vendor-published
      source_ref: CPAPA-PILOTMERIDIAN-2026
  prerequisites:
    - "Ledger-native deployment (QuickBooks Online first, Xero and NetSuite supported per Pilot)"
    - "Firm accounting policies configured"
  risks_and_guardrails:
    - "The Feb 2026 release claims 'zero human intervention'. A Dec 2025 Pilot release says its dataset is verified by US-based accounting experts, and the Meridian release returns work to the firm for review. The scope of human review is unclear (CPAPA-PILOTAI-2026, CPAPA-PILOTPARTNER-2025, CPAPA-PILOTMERIDIAN-2026)."
    - "First-generation AI bookkeeping vendor Botkeeper announced closure on 9 Feb 2026 and its Infinite platform was bought by Xendoo (CPAPA-XENDOO-2026, UKU-BOTKEEPER-2026); firms are urged to keep their own data exports."
  human_checkpoints:
    - "Firm reviews completed books (Meridian)"
  role_evolution: "Accountants review completed work instead of supervising task-by-task agent work, per Pilot (CPAPA-PILOTMERIDIAN-2026)."
  evidence_grade: C
  sources:
    - { ref: CPAPA-PILOTAI-2026, title: "Pilot Rolls Out Fully Autonomous AI Accountant", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/02/04/pilot-rolls-out-fully-autonomous-ai-accountant/177453/", date: "2026-02-04", access: full, locator: "Paragraphs 1-3 and feature list" }
    - { ref: CPAPA-PILOTMERIDIAN-2026, title: "Pilot Says New AI Accounting Platform Meridian Runs Monthly Close From Start to Finish", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/06/23/pilot-says-new-ai-accounting-platform-meridian-runs-monthly-close-from-start-to-finish/185541/", date: "2026-06-23", access: full, locator: "Paragraphs 1-6 and key features" }
    - { ref: CPAPA-PILOTPARTNER-2025, title: "Pilot Unveils Local Partner Program", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2025/12/09/pilot-unveils-local-partner-program/174577/", date: "2025-12-09", access: full, locator: "Paragraph on dataset verification" }
    - { ref: CPAPA-XENDOO-2026, title: "Xendoo Buys Botkeeper Infinite; AI Platform Will Remain Active and Supported", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/02/28/xendoo-buys-botkeeper-infinite-ai-platform-will-remain-active-and-supported/179027/", date: "2026-02-28", access: full, locator: "Opening paragraphs and related-article block" }
    - { ref: UKU-BOTKEEPER-2026, title: "Botkeeper Alternatives: 7 Best Options for Accounting Firms", publisher: Uku (practice-management vendor blog), type: vendor, url: "https://getuku.com/articles/botkeeper-alternatives/", date: "2026-02-13", access: full, locator: "Section 'What Happened to Botkeeper?'" }
  last_reviewed: "2026-10-20"
  notes: "AI-native provider (Pilot) and vendors. Pilot serves small businesses and startups directly and now sells a firm-facing product. The Botkeeper closure date (9 Feb 2026), Xendoo acquisition (announced on Xendoo's site, reported 2026-02-28; Uku gives 3 Mar 2026) and 'three weeks' gap come from a vendor blog plus the trade-press piece; the dates differ by source. A Digits outcome-based pricing claim (95% zero-touch) appeared only in a search snippet and is not used. Independence background applies when a firm sells this to its own attest clients (unverified)."

- id: advisory-client-accounting-services-14
  title: Cross-client portfolio monitoring for close status and anomalies
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [data-reporting, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: "A CAS manager running dozens of clients cannot see which close is late or which client's expenses have spiked until the client calls."
  solution: "A portfolio view shows close status for every client, open tasks and who is working on them, and AI summarizes issues across the client base and alerts on anomalies. Cross-client queries compare margins between entities."
  outcomes:
    - lever: risk
      description: "none published"
      figure: none
      measures: "Feature descriptions only; beta and announced products."
      provenance: vendor-published
      source_ref: CPAPA-INTUITCONNECT-2026
  prerequisites:
    - "Clients on a single platform or consistent data feeds"
  risks_and_guardrails:
    - "Every skill run is logged in an audit trail showing when it ran, who triggered it and what changed (CPAPA-INTUITCONNECT-2026, vendor description)."
  human_checkpoints:
    - "Manager decides what to act on"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: CPAPA-INTUITCONNECT-2026, title: "Intuit Connect ON: What You Need to Know About the Latest Platform Innovations", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/06/26/intuit-connect-on-what-you-need-to-know-about-the-latest-platform-innovations/185810/", date: "2026-06-26", access: full, locator: "Section 'Intuit Accountant Suite: The Firm's Control Tower'" }
    - { ref: ACCTODAY-RAMPSTACK-2026, title: "Ramp launches Stack, made specifically for accounting firms", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/ramp-launches-stack-made-specifically-for-accounting-firms", date: "2026-06-03", access: full, locator: "Paragraph 5 (Advisor Console)" }
    - { ref: ACCOUNTEX-2026, title: "Accountex London 2026: product roundup", publisher: Financial Accountant (IFA), type: press, url: "https://financialaccountant.co.uk/blog/accountex-london-2026-product-roundup/", date: "2026-05-19", access: full, locator: "Section 'Intuit QuickBooks'" }
  last_reviewed: "2026-10-20"
  notes: "Vendor sources only (Intuit, Ramp). Intuit's cross-client insights were described as open beta in June 2026."

- id: advisory-client-accounting-services-15
  title: Automated generation and distribution of branded monthly financial packages
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [document-production, data-reporting]
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Preparing PDFs and emailing them to each client by hand consumes time every month."
  solution: "A firm owner used the platform's API to build a workflow that generates and sends branded monthly statements. All 27 migrated clients now get automated reporting and 10 have moved to self-service dashboards."
  outcomes:
    - lever: speed
      description: "Statements arrive faster and more consistently, per the owner. Counts of clients on automated reporting and self-service are reported."
      figure: "27 clients on automated monthly reporting; 10 on self-service dashboards"
      measures: "Counts of the firm's migrated clients receiving automated reports, and of those on self-service dashboard access, per the owner."
      provenance: self-reported
      source_ref: CPAPA-ELEV8-2026
  prerequisites:
    - "An API or reporting tool with templates"
    - "Close that finishes before distribution"
  risks_and_guardrails:
    - "Automated delivery assumes the numbers were reviewed; the owner advises a parallel close to prove the numbers tie (CPAPA-ELEV8-2026)."
  human_checkpoints:
    - "Owner review of closed books before release"
  role_evolution: "Owner moves from producing reports to explaining them (CPAPA-ELEV8-2026)."
  evidence_grade: B
  sources:
    - { ref: CPAPA-ELEV8-2026, title: "How an AI-Native Accounting Platform Helped One Solo Firm Reclaim 90 Hours a Month and Scale Advisory Without Hiring", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/07/21/how-an-ai-native-accounting-platform-helped-one-solo-firm-reclaim-90-hours-a-month-and-scale-advisory-without-hiring/187093/", date: "2026-07-21", access: full, locator: "Section 'Building a Scalable Reporting Process'" }
    - { ref: JOFA-CASAI-2026, title: "Simple but effective AI use cases for CAS", publisher: Journal of Accountancy (AICPA and CIMA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/", date: "2026-01-01", access: full, locator: "Use-case category 'Reporting'" }
  last_reviewed: "2026-10-20"
  notes: "Small firm (Elev8), single case. This is mostly API-based automation rather than generative AI; included because the case is framed by the vendor as part of the AI-native platform. Same source as entries 02 and 08, so it is not independent corroboration."

- id: advisory-client-accounting-services-16
  title: Advising clients on their own AI adoption (selection, data security, workflows)
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [expert-judgment, client-interaction]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Clients ask their accountant which AI tools to use, what the risks are, and how to build dashboards. Some arrive having already used AI to self-prepare work."
  solution: "CAS and fractional CFO teams add AI advisory: tool selection, data-protection answers, and hands-on demonstrations of dashboards and analysis. Firms treat it as a new advisory service layered on the CAS relationship."
  outcomes:
    - lever: growth
      description: "none published. Bonadio's CAS lead says more client projects involving AI are kicking off. A survey reports that 62% say clients need more guidance on technology management."
      figure: "62%"
      measures: "Percentage of Intuit survey respondents (n=725) saying clients need more guidance on technology management; the article words it 'say clients need more guidance'."
      provenance: vendor-published
      source_ref: INTUIT-ACCTTECH-2026
  prerequisites:
    - "Firm AI policy and data-security story it can explain to clients (only 21% of firms have an AI policy or strategy per KARBON-AISTATE-2026)"
  risks_and_guardrails:
    - "Only 33% of respondents proactively explain how AI supports their work; 49% address it only when a client brings it up (INTUIT-ACCTTECH-2026)."
    - "Firms that do not enter the advisory conversation risk clients self-preparing with AI and asking why the firm did not (ACCTODAY-CATALYST-2026)."
  human_checkpoints:
    - "Accountant owns advice and risk framing"
  role_evolution: "Advisers become guides to client AI adoption. One fractional CFO calls it 'a new responsibility for the CFO' (CFODIVE-FRACTIONAL-2026)."
  evidence_grade: B
  sources:
    - { ref: ACCTODAY-BONADIO-2026, title: "CAS and outsourced accounting fuel Bonadio Group", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/cas-and-outsourced-accounting-fuel-bonadio-group", date: "2026-07-30", access: full, locator: "Final quoted paragraphs on AI projects" }
    - { ref: CFODIVE-FRACTIONAL-2026, title: "Fractional CFOs see demand surge in AI age", publisher: CFO Dive, type: press, url: "https://www.cfodive.com/news/fractional-cfos-see-demand-surge-ai-age/827264/", date: "2026-08-06", access: full, locator: "Section 'An AI-enabled finance future'" }
    - { ref: ACCTODAY-CATALYST-2026, title: "AI - the catalyst and solution to advisory", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/ai-the-catalyst-and-solution-to-advisory", date: "2026-07-13", access: full, locator: "Quoted paragraphs from Madeline Reeves" }
    - { ref: INTUIT-ACCTTECH-2026, title: "The 2026 Accountant Technology Survey", publisher: CPA Practice Advisor (Intuit survey), type: survey, url: "https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807", date: "2026-07-02", access: full, locator: "Sections 'Trust and Transparency' and 'Your Role is Expanding'" }
    - { ref: KARBON-ENGAGE-2026, title: "23 must-see sessions at AICPA and CIMA ENGAGE 2026", publisher: Karbon Magazine, type: conference, url: "https://karbonhq.com/resources/aicpa-cima-engage-2026/", date: "2026-05-21", access: full, locator: "Session 'AI conversations and integration' (scheduled abstract)" }
  last_reviewed: "2026-10-20"
  notes: "Firms: Bonadio (Top 50 per source) and a boutique fractional CFO. The ENGAGE listing is a pre-event abstract of a session scheduled for 9 June 2026 (Weaver and Tidwell, GW CPA and Karbon speakers) and does not support the grade. B reflects named practitioners describing live client conversations without outcomes. Most client AI advisory evidence is anecdotal."

- id: advisory-client-accounting-services-17
  title: AI-assisted vendor spend assessment as a quick advisory deliverable (idea)
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [research-synthesis, expert-judgment]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "A spend assessment that would normally take hours is hard to offer as a low-cost entry advisory product."
  solution: "AI produces a first-pass spend assessment in minutes that staff supervise like a new intern."
  outcomes:
    - lever: speed
      description: "none published. A podcast summary says Joe Woodard shared an AI-powered spend assessment that takes five minutes against hours; the firm that did it is not named."
      figure: "five minutes vs hours (anecdote)"
      measures: "Unmeasured anecdote reported in a podcast write-up; no sample or denominator."
      provenance: self-reported
      source_ref: WOODARD-TWR-2025
  prerequisites:
    - "Access to the client's spend data"
  risks_and_guardrails:
    - "Both speakers say to treat AI like a new intern needing supervision (WOODARD-TWR-2025)."
  human_checkpoints:
    - "Review of AI output before it goes to the client"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: WOODARD-TWR-2025, title: "TWR Podcast Episode 120: How CAS and AI Are Reshaping the Top 100 Firms", publisher: The Woodard Report, type: podcast, url: "https://report.woodard.com/articles/twr-podcast-episode-120-how-cas-and-ai-are-reshaping-the-top-100-firms-oaiwr-twrpod-bllwr", date: "2025-04-30", access: full, locator: "Section 'AI is coming fast, but it's not quite here yet'" }
  last_reviewed: "2026-10-20"
  notes: "Idea: discussed by a consultant and a trade editor; no firm deployment found. The source is a written summary of the episode, not a transcript. Podcast is 17 months old, at the edge of the window. CPA.com lists a '5 Steps to Spend Management Advisory' whitepaper in a related-resources panel (title only, undated, not read)."

- id: advisory-client-accounting-services-18
  title: AI-native provider supplies platform and leads while a local firm delivers the client service
  archetype: advisory
  module: client-accounting-services
  function: service-delivery
  work_types: [transaction-processing, client-interaction]
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Independent bookkeepers and small firms lack capacity and technology to scale, and AI-native platforms need distribution and local relationships."
  solution: "Pilot launched a local partner program giving independent bookkeepers and firms its platform and automation, advisory services and matched leads, in select cities with nationwide expansion planned. Puzzle will work with accounting partners who deliver the service. Xendoo, Pilot and Decimal are cited by Woodard as examples of providers now moving to support accountants and bookkeepers."
  outcomes:
    - lever: growth
      description: "none published"
      figure: none
      measures: "No partner results reported; program announcements only."
      provenance: vendor-published
      source_ref: CPAPA-PILOTPARTNER-2025
  prerequisites:
    - "Provider platform and lead engine"
    - "Partner firm with local presence"
  risks_and_guardrails:
    - "Vendor dependence: the Botkeeper episode shows a platform can vanish for weeks (CPAPA-XENDOO-2026, UKU-BOTKEEPER-2026)."
    - "Puzzle will no longer market a standalone firm-facing product after the Accrual deal, so partner firms depend on the provider's strategy (ACCTODAY-ACCRUAL-2026)."
  human_checkpoints:
    - "Not described"
  role_evolution: "Firms become delivery partners rather than platform customers, per the Puzzle plan (ACCTODAY-ACCRUAL-2026)."
  evidence_grade: C
  sources:
    - { ref: CPAPA-PILOTPARTNER-2025, title: "Pilot Unveils Local Partner Program", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2025/12/09/pilot-unveils-local-partner-program/174577/", date: "2025-12-09", access: full, locator: "Paragraphs 2-6" }
    - { ref: ACCTODAY-ACCRUAL-2026, title: "Accrual acquires Puzzle's tech to add to their CAS offering", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/accrual-acquires-puzzles-tech-to-add-to-their-cas-offering", date: "2026-09-02", access: full, locator: "Paragraph 4 (Orloff on partner model)" }
    - { ref: WOODARD-EP163-2026, title: "AI, Scams, and the Future of CAS in a Changing Profession (Episode 163)", publisher: The Woodard Report, type: podcast, url: "https://report.woodard.com/articles/ai-scams-future-of-cas-ombwr-twrpod", date: "2026-03-18", access: full, locator: "Section 'A new chapter for Botkeeper and a bigger shift in CAS'" }
  last_reviewed: "2026-10-20"
  notes: "AI-native providers and vendors. The Woodard source is a written summary of the episode. The Pilot program was available in select cities as of Dec 2025, with nationwide plans 'in the coming year'. No partner count or results found."
```

---

## 3. Module notes

### Processes and key steps (with work types)

- **Client onboarding and migration**: intake, chart of accounts, historical balances, bank and payroll connections, catch-up cleanup. `transaction-processing`, `coordination-scheduling`.
- **Transaction processing**: bank and card feed coding, AP invoice capture and approvals, AR, payroll entries. `transaction-processing`.
- **Reconciliation and month-end close**: account reconciliations, accruals and recurring schedules, journal entries, review, lock periods. `review-assurance`, `data-reporting`. Clients are said to expect 10 to 12 days (ACCTODAY-COHNPOD-2026).
- **Reporting**: financial package, commentary, KPI dashboards. `document-production`, `data-reporting`.
- **Controllership and fractional CFO**: review, policies, budgets, forecasts, cash-flow models, board packages. `expert-judgment`.
- **Client collaboration**: questions, document chasing, status. `client-interaction`.
- **Payment and payroll execution**: bill pay and running payroll; no AI-specific discourse found for the execution step itself.

### Common pain points

- **Staffing**: accounting professionals leaving, long ramp times (56% say an entry-level hire needs six months or more to reach full billable capacity) and hard-to-fill mid-level roles (INTUIT-ACCTTECH-2026, ACCTODAY-BIGYEAR-2026).
- **Fragmented tools**: firms average about 10 apps and only 41% say tools are fully integrated. Respondents report losing about five hours a week moving or re-entering data (INTUIT-ACCTTECH-2026).
- **Manual data cleanup** is the top advisory blocker (30%), ahead of staffing (24%) and app overload (16%) (INTUIT-ACCTTECH-2026).
- **Client-specific house rules** that general models miss (DIGITS-BENCH-2026).
- **Vendor fragility** (Botkeeper) and platform lock-in (UKU-BOTKEEPER-2026, WOODARD-EP163-2026).
- **Billable-hour mindset versus fixed-fee recurring work**: one JofA source says 90% of CAS practices sell fixed-fee recurring services. A BST and Co. leader's billable hours fell from about 1,700 to 500 or 600 a year while CAS revenue grew 47% (JOFA-CASTIPS-2025).

### Metrics and benchmarks (with provenance)

| Metric | Figure | Source | Provenance |
|---|---|---|---|
| Ledger-native categorization accuracy | 97.8% vs 79.5% best one-shot, 79.1% human | DIGITS-BENCH-2026 | vendor-published |
| Best look-up agent accuracy | 88.9%; 74 s and 16,295 tokens per transaction | DIGITS-BENCH-2026 | vendor-published |
| QuickBooks bank-feed categorization accuracy | about 78% to nearly 88% | CPAPA-INTUITCONNECT-2026 | vendor-published |
| Month-end close tasks, AI vs junior CPAs | AI 100% on 20 of 20 attempts; humans mostly below 50% | ACCTODAY-AIBENCH-2026, MERCOR-APEX-2026 | independent (third party; simulated tasks) |
| Close cycle, one small firm | 18 days to 5 | CPAPA-ELEV8-2026 | self-reported |
| Top 100 firms reporting CAS growth | 85% of 88 responding firms (up five points) | ACCTODAY-BONADIO-2026 | press report of an Accounting Today survey |
| AI use for at least one client service | 88%; 30% embedded as default; 54% situational | INTUIT-ACCTTECH-2026 | vendor-published |
| Firms with AI policy or strategy | 21% | KARBON-AISTATE-2026 | vendor-published |
| Time saved | average 60 minutes per day per employee | KARBON-AISTATE-2026 | vendor-published (self-reported by respondents) |
| Leaders reporting substantial results on scaling capacity without headcount | 9% | BILL-AIAMBITION-2026 | vendor-published |
| Leaders agreeing AI pushes them toward CAS | 67% | BILL-AIAMBITION-2026 | vendor-published |
| Pricing in use | fixed fee 66%, hourly 60% (multiple answers) | BILL-AIAMBITION-2026 | vendor-published |
| Interim CFO demand | up 14% year on year | CFODIVE-FRACTIONAL-2026 | independent (via secondary) |
| Respondents ranking AI as top ethical challenge | 61% (32% in 2024) | ACCTODAY-ACCAETHICS-2026 | independent (professional body) |

**Missing**: any published firm-side error rate, override rate, rework rate or parallel-run result for CAS deliverables, and any independent replication of vendor accuracy claims. The 2026 CAS Benchmark Survey report is due in December 2026 and the 2024 data set is for participants only.

### Guardrails and regulatory points

- **Five written controls before agents run a client close**: agent inventory with a named owner, replayable evidence, risk-scaled sign-off gates, a read of third-party assurance reports, and monitoring with an exit threshold. The article notes that the AICPA has not yet published guidance on AI in SOC reporting and that COSO issued guidance on internal control over generative AI in Feb 2026 (CPAPA-AGENTSCLOSE-2026).
- **Client data protection**: three in five respondents say clients ask for proof of AI data protection always or frequently (INTUIT-ACCTTECH-2026).
- **Human sign-off by design**: Ramp (nothing posts without authorization), Intuit (expert-verified categorization off by default for firm-billed clients, accountant in control), Pilot (firm reviews completed books).
- **Independence**: bookkeeping, payroll, bill pay and similar services for the firm's own audit clients are commonly restricted. Not verified in this run.
- **Liability**: Deloitte Australia's October 2025 refund of part of a fee over fabricated citations is cited as a lesson that unreviewed output is a professional liability (CPAPA-AGENTSCLOSE-2026, as cited; not independently checked).
- **Ethics**: 61% of ACCA's 1,178 respondents rank AI use as the leading ethical challenge, with concerns centred on accountability, transparency, explainability, confidentiality and judgment (ACCTODAY-ACCAETHICS-2026).

### Frontier signals (dated and sourced)

- **2026-02-04**: Pilot announces an AI Accountant described as fully autonomous from onboarding to monthly close (CPAPA-PILOTAI-2026). Vendor claim.
- **2026-02-09 to 2026-02-28**: Botkeeper announces closure, then Xendoo acquires the Infinite platform (CPAPA-XENDOO-2026, UKU-BOTKEEPER-2026).
- **2026-03-04**: Woodard hosts note practice-management and close-automation products converging, with Canopy announcing a bookkeeping module (WOODARD-EP161-2026).
- **2026-06-03**: Ramp announces Stack, with agents driven by editable skills (ACCTODAY-RAMPSTACK-2026).
- **2026-06-16 (release), reported 2026-06-23**: Pilot launches Meridian for firms (CPAPA-PILOTMERIDIAN-2026).
- **2026-06-26**: Intuit describes expert-verified auto-categorization, conversational BI and cross-client insights (CPAPA-INTUITCONNECT-2026).
- **2026-07-21**: CLA announces a firm-trained model with Digits, starting in its CAS practice (ACCTODAY-CLADIGITS-2026).
- **2026-09-02**: Accrual agrees to buy Puzzle's firm-facing technology and plans a CAS offering with broader availability by end of 2026 (ACCTODAY-ACCRUAL-2026).
- **2026-10-01 to 2026-10-16**: Mercor and Digits publish benchmarks; Digits argues one-shot LLM classification has plateaued and ledger-native models win (MERCOR-APEX-2026, DIGITS-BENCH-2026, ACCTODAY-AIBENCH-2026).
- **2026-01-15**: Tom Hood says the next phase is managing AI agents in finance and accounting (JOFA-HOOD-2026).
- **2026-07-01**: Technology Lab hosts describe a frenzy of AI-and-private-equity talk, with PE driving forced modernization in firms (CPAPA-TECHLAB-2026).

### Workforce and role effects

- Senior accountants are expected to move up to review and client conversation (ACCTODAY-COHNPOD-2026). A Deloitte contributor expects staff accountants to shift from executing processes to orchestrating technology (ACCTODAY-TRENDS-2026).
- 52% of BILL's leaders expect AI to reduce headcount (68% at firms of 201+). 47% expect more need for IT and technical roles (BILL-AIAMBITION-2026).
- Hiring criteria are shifting: strategic judgment (38%) and AI fluency (22%) lead; AI, automation and data skills tie with software certifications (53%) as entry-level signals, slightly ahead of CPA status (50%) (INTUIT-ACCTTECH-2026).
- A Bonadio CAS lead describes an 'evaporation of traditional bookkeepers' (ACCTODAY-BONADIO-2026). A Surgent executive predicts firms will cut hiring and not raise wages, which is an opinion (ACCTODAY-BIGYEAR-2026).
- 91% say graduates are more likely to join firms using AI (KARBON-AISTATE-2026).
- Mercor notes its junior-CPA study did not measure client communication, asking the right questions or tacit context, which it expects to matter more (MERCOR-APEX-2026).

### Objections and concerns

- **Review burden**: reviewing AI suggestions can take nearly as long as doing the work, and 97% accuracy still means many errors at volume (BEANCOUNT-REVIEWBURDEN-2026, anecdotal and pseudonymous).
- **Reliance risk**: following non-consensus AI recommendations can increase error (STANFORD-JAR-2026). In Mercor's study, people deferred to wrong revisions in some sessions (ACCTODAY-AIBENCH-2026).
- **General models plateau without client context**; agents are costly and sometimes do not finish (DIGITS-BENCH-2026, vendor).
- **Vendor failure and lock-in** (Botkeeper).
- **Clients self-serving with AI**: consultants hear of clients arriving with AI-prepared work (ACCTODAY-CATALYST-2026), and a columnist suggests AI could lower outsourced accounting costs by 20 to 50% (ACCTODAY-REPLACE-2026, opinion; the article says it was developed using ChatGPT).
- **Hype fatigue**: hosts call much of the AI talk 'gratuitous' (CPAPA-TECHLAB-2026).
- **Tax revenue exposure**: Withum's Bourke expects complete automation of the tax process and sees CAS as the hedge (ACCTODAY-CASKEYS-2026).
- **Pricing**: hourly billing is called unsustainable once AI cuts hours (ACCTODAY-DECISIONS-2026, written by Digits' founder and so vendor-voiced). Only a minority has changed pricing (routed below).

### Interview probes

1. Which steps of your close and transaction processing run with no person on the normal path today? What share of transactions or accounts is that, and what is your exception, override or error-found-on-review rate?
2. Before an agent or auto-posting touches a client ledger, who is the named approver and what evidence is retained? Did you run a parallel close, as Elev8 advises?
3. Did you build, buy from your ledger vendor, or adopt an AI-native platform? What is your exit plan if the vendor fails (Botkeeper)?
4. What happened to hours per client, clients per staff member, net revenue per FTE and review time? Which of those do you measure?
5. Which CAS services do you sell to your own audit clients, and how do you handle independence and client-data confidentiality questions about AI?

---

## 4. Routed to other modules

| Item | Why it belongs elsewhere | Target |
|---|---|---|
| Pricing the firm's own CAS (fixed fee vs hourly, outcome pricing, skim pricing): BILL-AIAMBITION-2026 (66% fixed fee, 60% hourly, 68% ruling out or undecided on new pricing), ACCTODAY-FEES-2025 (Ignition survey, 219 firms), WOODARD-EP161-2026 (skim pricing), WOODARD-EP163-2026, ACCTODAY-DECISIONS-2026. A Digits outcome-pricing claim (95% zero-touch) was a search snippet only | Firm operations | professional-services |
| Staffing, junior pipeline, hiring criteria, headcount expectations: INTUIT-ACCTTECH-2026, BILL-AIAMBITION-2026, KARBON-AISTATE-2026, ACCTODAY-BIGYEAR-2026 | Firm operations | professional-services |
| PE ownership, alternative practice structures, consolidation: CPAPA-TECHLAB-2026, ACCTODAY-CURRENT-2026, WOODARD-EP185-2026 (Grant Thornton Advisors and CBIZ), BILL-AIAMBITION-2026 (half considering outside investment) | Firm operations | professional-services |
| Practice-management platforms adding bookkeeping and close modules (Canopy, Karbon): WOODARD-EP161-2026, ACCOUNTEX-2026 | Firm tooling | professional-services |
| Controls and assurance over clients' agentic close tools: CPAPA-AGENTSCLOSE-2026 (five controls, COSO Feb 2026, SOC gaps). A headline on AICPA and AIUC jointly assured AI certification was seen only in page sidebars, unopened | Sold as an advisory service | risk-controls (boundary with assurance) |
| Excel-agent data cleaning for audit populations: JOFA-EXCEL-2026 | Audit procedure | assurance |
| Automation of tax preparation (Bourke prediction) and tax-season exposure: ACCTODAY-CASKEYS-2026 | Tax technical work | tax |
| FP&A and forecasting platforms that sit beside fractional CFO work | Narrowed FP&A scope | fpa-performance |
| Family-office clients as a CAS niche (Sweeney Conrad focus, JOFA-CASTIPS-2025) | Private-client | private-client |
| ACCA ethics survey and the Deloitte Australia refund as governance evidence | Governance and evidence angle | governance-and-evidence (other angle) |

---

## 5. Sources

All sources were opened and read (`access: full`). Types: press 22, podcast 7, professional-body 3, survey 4, vendor 3, conference 2, academic 1, community 1 (43 in total).

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| ACCTODAY-CASKEYS-2026 | CAS delivers 'the keys to the kingdom' | Accounting Today | press | https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom | 2026-05-22 |
| ACCTODAY-BONADIO-2026 | CAS and outsourced accounting fuel Bonadio Group | Accounting Today | press | https://www.accountingtoday.com/news/cas-and-outsourced-accounting-fuel-bonadio-group | 2026-07-30 |
| ACCTODAY-CLADIGITS-2026 | CLA working with Digits to develop proprietary AI model | Accounting Today | press | https://www.accountingtoday.com/news/cla-working-with-digits-to-develop-proprietary-ai-model | 2026-07-21 |
| ACCTODAY-AIBENCH-2026 | AI beats human accountants at monthly close, transaction categorization | Accounting Today | press | https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization | 2026-10-16 |
| ACCTODAY-ACCRUAL-2026 | Accrual acquires Puzzle's tech to add to their CAS offering | Accounting Today | press | https://www.accountingtoday.com/news/accrual-acquires-puzzles-tech-to-add-to-their-cas-offering | 2026-09-02 |
| ACCTODAY-CATALYST-2026 | AI - the catalyst and solution to advisory | Accounting Today | press | https://www.accountingtoday.com/news/ai-the-catalyst-and-solution-to-advisory | 2026-07-13 |
| ACCTODAY-RAMPSTACK-2026 | Ramp launches Stack, made specifically for accounting firms | Accounting Today | press | https://www.accountingtoday.com/news/ramp-launches-stack-made-specifically-for-accounting-firms | 2026-06-03 |
| ACCTODAY-DECISIONS-2026 | AI and accounting firms: the decisions that actually matter (op-ed by Digits' founder) | Accounting Today | press | https://www.accountingtoday.com/opinion/ai-and-accounting-firms-the-decisions-that-actually-matter | 2026-06-01 |
| ACCTODAY-REPLACE-2026 | Will AI replace accounting firms in the small biz market? (opinion, August Aquila) | Accounting Today | press | https://www.accountingtoday.com/opinion/will-ai-replace-accounting-firms-in-the-small-biz-market | 2026-08-24 |
| ACCTODAY-TRENDS-2026 | How will technology shape accounting trends in 2026? | Accounting Today | press | https://www.accountingtoday.com/news/how-will-technology-shape-accounting-trends-in-2026 | 2026-01-09 |
| ACCTODAY-BIGYEAR-2026 | A big year for AI in accounting | Accounting Today | press | https://www.accountingtoday.com/news/a-big-year-for-ai-in-accounting | 2026-02-04 |
| ACCTODAY-ACCAETHICS-2026 | Majority of accountants agree AI is profession's top ethical challenge (ACCA Navigating Ethics for Trust) | Accounting Today | press | https://www.accountingtoday.com/news/majority-of-accountants-agree-ai-is-professions-top-ethical-challenge | 2026-10-15 |
| ACCTODAY-CURRENT-2026 | Crete Professionals Alliance rebrands as Current | Accounting Today | press | https://www.accountingtoday.com/news/crete-professionalls-alliance-rebrands-as-current | 2026-06-02 |
| ACCTODAY-FEES-2025 | Accounting and tax firms plan to raise fees in 2026 (Ignition survey) | Accounting Today | survey | https://www.accountingtoday.com/news/accounting-and-tax-firms-plan-to-raise-fees-in-2026 | 2025-08-21 |
| CPAPA-AGENTSCLOSE-2026 | Before You Let the Agents Run the Close: Five Controls to Put in Writing First | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/08/13/before-you-let-the-agents-run-the-close-five-controls-to-put-in-writing-first/188496/ | 2026-08-13 |
| CPAPA-ELEV8-2026 | How an AI-Native Accounting Platform Helped One Solo Firm Reclaim 90 Hours a Month and Scale Advisory Without Hiring | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/07/21/how-an-ai-native-accounting-platform-helped-one-solo-firm-reclaim-90-hours-a-month-and-scale-advisory-without-hiring/187093/ | 2026-07-21 |
| CPAPA-PILOTAI-2026 | Pilot Rolls Out Fully Autonomous AI Accountant | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/04/pilot-rolls-out-fully-autonomous-ai-accountant/177453/ | 2026-02-04 |
| CPAPA-PILOTMERIDIAN-2026 | Pilot Says New AI Accounting Platform Meridian Runs Monthly Close From Start to Finish | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/06/23/pilot-says-new-ai-accounting-platform-meridian-runs-monthly-close-from-start-to-finish/185541/ | 2026-06-23 |
| CPAPA-PILOTPARTNER-2025 | Pilot Unveils Local Partner Program | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/12/09/pilot-unveils-local-partner-program/174577/ | 2025-12-09 |
| CPAPA-XENDOO-2026 | Xendoo Buys Botkeeper Infinite; AI Platform Will Remain 'Active and Supported' | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/28/xendoo-buys-botkeeper-infinite-ai-platform-will-remain-active-and-supported/179027/ | 2026-02-28 |
| CPAPA-INTUITCONNECT-2026 | Intuit Connect ON: What You Need to Know About the Latest Platform Innovations | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/06/26/intuit-connect-on-what-you-need-to-know-about-the-latest-platform-innovations/185810/ | 2026-06-26 |
| CFODIVE-FRACTIONAL-2026 | Fractional CFOs see demand surge in AI age | CFO Dive | press | https://www.cfodive.com/news/fractional-cfos-see-demand-surge-ai-age/827264/ | 2026-08-06 |
| ACCOUNTEX-2026 | Accountex London 2026: product roundup | Financial Accountant (IFA) | press | https://financialaccountant.co.uk/blog/accountex-london-2026-product-roundup/ | 2026-05-19 |
| ACCTODAY-COHNPOD-2026 | The meeting of CAS and AI (On the Air with Accounting Today, Intuit-sponsored) | Accounting Today | podcast | https://www.accountingtoday.com/podcast/at-intuit-sponsored-podcast-03-16 | 2026-03-16 |
| CPAPA-TECHLAB-2026 | Thought Leader and 40 Under 40 AICPA Think Tank, Accounting Technology Lab Podcast, July 2026 | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/thought-leader-40-under-40-aicpa-think-tank-accounting-technology-lab-podcast-july-2026/ | 2026-07-01 |
| JOFA-HOOD-2026 | Tom Hood on AI, hybrid work, and other 2026 themes shaping accounting | Journal of Accountancy podcast | podcast | https://www.journalofaccountancy.com/podcast/2026/jan/tom-hood-on-ai-hybrid-work-and-other-2026-themes-shaping-accounting/ | 2026-01-15 |
| WOODARD-TWR-2025 | TWR Podcast Episode 120: How CAS and AI Are Reshaping the Top 100 Firms | The Woodard Report | podcast | https://report.woodard.com/articles/twr-podcast-episode-120-how-cas-and-ai-are-reshaping-the-top-100-firms-oaiwr-twrpod-bllwr | 2025-04-30 |
| WOODARD-EP161-2026 | AI Fluency, Pricing Strategy, and Accounting's Future (Episode 161) | The Woodard Report | podcast | https://report.woodard.com/articles/ai-fluency-pricing-strategy-and-accountings-future-twrpod-ombwr | 2026-03-04 |
| WOODARD-EP163-2026 | AI, Scams, and the Future of CAS in a Changing Profession (Episode 163) | The Woodard Report | podcast | https://report.woodard.com/articles/ai-scams-future-of-cas-ombwr-twrpod | 2026-03-18 |
| WOODARD-EP185-2026 | Surviving or Thriving? The Future of Accounting in an AI-Driven Profession (Episode 185) | The Woodard Report | podcast | https://report.woodard.com/articles/surviving-or-thriving-the-future-of-accounting-in-an-ai-driven-profession-twrpod | 2026-08-19 |
| JOFA-CASAI-2026 | Simple but effective AI use cases for CAS (Polakoff and Voyer, CohnReznick) | Journal of Accountancy (AICPA and CIMA) | professional-body | https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/ | 2026-01-01 |
| JOFA-CASTIPS-2025 | Tips for providing the CAS services clients want | Journal of Accountancy (AICPA and CIMA) | professional-body | https://www.journalofaccountancy.com/issues/2025/jul/tips-for-providing-the-cas-services-clients-want/ | 2025-07-01 |
| JOFA-EXCEL-2026 | Using an Excel agent to clean, validate, and reconcile data | Journal of Accountancy (AICPA and CIMA) | professional-body | https://www.journalofaccountancy.com/issues/2026/oct/using-an-excel-agent-to-clean-validate-and-reconcile-data/ | 2026-10-01 |
| STANFORD-JAR-2026 | Human + AI in Accounting: Early Evidence from the Field (Choi, Xie) | Journal of Accounting Research via Stanford GSB | academic | https://www.gsb.stanford.edu/index.php/node/629989 | 2026-06 |
| KARBON-AISTATE-2026 | Karbon State of AI in Accounting 2026 Report | Karbon Magazine | survey | https://karbonhq.com/resources/state-of-ai-accounting-2026 | 2026-01-20 |
| INTUIT-ACCTTECH-2026 | The 2026 Accountant Technology Survey: Turning Data Revelations into a Firm of the Future | CPA Practice Advisor (Intuit QuickBooks survey) | survey | https://cpapracticeadvisor.com/2026/07/02/the-2026-accountant-technology-survey-turning-data-revelations-into-a-firm-of-the-future/185807 | 2026-07-02 |
| BILL-AIAMBITION-2026 | BILL Accounting Firm AI Ambition Survey, vol 4 (with vol 3 reference) | BILL | survey | https://www.bill.com/blog/ai-ambition-survey-vol-4-findings | 2026 (page undated; fieldwork late 2025) |
| DIGITS-BENCH-2026 | Breaking: AI Can't Close Your Books From the Outside | Digits | vendor | https://digits.com/blog/ai-cant-close-books-from-outside/ | 2026-10-07 |
| MERCOR-APEX-2026 | Human Baselines for Benchmarks: AI Now Outperforms Junior Accountants | Mercor | vendor | https://www.mercor.com/blog/human-baselines-for-benchmarks-ai-now-outperforms-junior-accountants/ | 2026-10-01 |
| UKU-BOTKEEPER-2026 | Botkeeper Alternatives: 7 Best Options for Accounting Firms | Uku | vendor | https://getuku.com/articles/botkeeper-alternatives/ | 2026-02-13 |
| KARBON-ENGAGE-2026 | 23 must-see sessions at AICPA and CIMA ENGAGE 2026 | Karbon Magazine | conference | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | 2026-05-21 |
| ACCTODAY-CASSUMMIT-2026 | CAS Summit Virtual 2026: Session abstracts | Accounting Today | conference | https://www.accountingtoday.com/cas-summit-virtual-2026-session | 2026-08-13 |
| BEANCOUNT-REVIEWBURDEN-2026 | I Adopted AI Bookkeeping for Time Savings, But Reviewing Every Transaction Takes Just as Long | Beancount and Plain-Text Accounting Forum | community | https://beancount.io/forum/t/i-adopted-ai-bookkeeping-for-time-savings-but-reviewing-every-transaction-takes-just-as-long/1823 | 2026-03-22 |

Notes on source handling: ACCTODAY-DECISIONS-2026 is authored by Digits' founder, so its claims are vendor-voiced. ACCTODAY-REPLACE-2026 says it was developed using ChatGPT. The KARBON-AISTATE-2026 date is the release dateline (the page was posted 2026-01-23). For BILL-AIAMBITION-2026 I found no publication date on the page. BILL says the survey was run with NewtonX in late 2025, so the date is left at the year.

---

## 6. Gaps

- **Quality evidence is thin.** I found no firm-side published error, override, rework or parallel-run rates for CAS. The only measured figures are vendor benchmarks (Digits, Intuit) and a simulated-task study (Mercor). The peer-reviewed paper (STANFORD-JAR-2026) was read as an abstract, so effect sizes (including a 55% rise in weekly client support mentioned in the landscape) are not confirmed here.
- **No independent replication** of the Digits or Pilot claims. Pilot's own releases are inconsistent about human involvement.
- **Full CAS Benchmark Survey data** (2024 participants-only data set; 2026 report due December 2026) was not reachable. The CPA.com page is undated and was not used as a source.
- **Conference sessions**: ENGAGE, Digital CPA and CAS Summit content is behind registration or shown only as abstracts. I could not obtain the Firm Growth Forum keynote page (403) and relied on the Accounting Today write-up (ACCTODAY-CASKEYS-2026). No recordings or decks were found. ILTACON, Legalweek, CLOC and Legal Geek are not relevant to CAS.
- **Undated pages not used for claims**: a CPA.com webinar page ("How CAS Firms Are Unlocking New Potential with Agentic AI", with Aprio and BILL speakers), a CPA.com agentic CAS whitepaper, and a BILL "AI and the future of CAS" guide.
- **Woodard podcast episodes 167, 169 (Decimal), 170** surfaced only as titles in search results and were not read. Episode pages fetched were written summaries, not transcripts.
- **Payroll and bill pay execution**: little AI-specific practitioner discussion beyond vendor tools. No named-firm deployment for payroll.
- **Named-firm detail missing** for Baker Tilly, Armanino, Aprio, Cherry Bekaert and Wipfli CAS AI work (only ENGAGE session titles and the Aprio webinar listing).
- **Community voice is weak.** Reddit blocked automated access (403). The only community source is a pseudonymous plain-text-accounting forum thread whose posts read as templated, so treat it as anecdotal. Going Concern, CPA Trendlines and the CAS Minute podcast were not read.
- **Items seen only in snippets or sidebars** and not used: Accountancy Age coverage of the BILL survey (blocked), a Digits outcome-based pricing claim, an AICPA and AIUC joint certification headline, Fractionus and Rework tool listings.
- **Date conflicts**: Botkeeper closure and acquisition dates differ slightly across sources (9 Feb closure; Xendoo reported 2026-02-28 vs 3 Mar in a vendor blog). The CAS Summit page shows sessions on 13 Aug 2026; the landscape listed 29 Jul as a conflicting date.
- **KPMG 42% readiness figure** quoted in CPAPA-AGENTSCLOSE-2026 may be conflated, per the landscape. It was not used.
