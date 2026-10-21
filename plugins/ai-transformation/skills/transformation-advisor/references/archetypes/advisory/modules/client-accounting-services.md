# Client accounting services (advisory)

Sources checked 2026-10-20 and re-verified 2026-10-21. Use cases live in `../use-cases/client-accounting-services.yaml` (24 entries). Ids are
shortened here: `#05` means `advisory-client-accounting-services-05`; other modules' ids are in full. Source keys in
brackets, such as [CPAPA-AGENTSCLOSE-2026], are in the YAML or in §10. **The best evidence is an association study
and vendor benchmarks.** One entry is grade A (`#01`), resting on an independent field study (Choi and Xie) of one
unnamed platform's small-business customers; 11 are grade B (a named deployment without published measurement), and
many rest on small firms or AI-native practices in vendor case studies. No CAS firm or platform has published an error rate, override
rate, parallel-run result or inspection finding. Say so when you quote a figure.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Client accounting services (CAS): outsourced or co-sourced financial operations, from bookkeeping and payroll to
CFO-level work [JOFA-CASTIPS-2025]. That means transaction coding, reconciliation and month-end close, management
reporting, controllership and fractional CFO work (a part-time finance lead), payroll and bill pay, delivered on
subscription by top-100 and mid-market accounting firms, small firms and solo practitioners, AI-native providers, and
in-house finance teams. The firm's own pricing, staffing and private-equity (PE) ownership are in
professional-services; control and AI-governance services sold to clients are in advisory risk-controls; FP&A and
ERP advisory beyond the CFO-services forecast are in advisory fpa-performance; tax work is in tax.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Onboarding, migration, cleanup | Chart of accounts, opening balances, bank and payroll feeds; catch-up of messy books | transaction-processing, coordination-scheduling | Weeks of catch-up; cleanups unprofitable; migration often called the biggest obstacle [DIGITS-TFMA-2026, FLOQAST-CASCASE-2026, CPAPA-ELEV8-2026] |
| Transaction coding | Bank, card and receipt categorization against each client's house rules | transaction-processing | Manual data cleanup is the top advisory blocker (30%) [INTUIT-ACCTTECH-2026] |
| Reconciliation | Bank, card, clearing accounts, payroll liabilities | transaction-processing, review-assurance | Fragile rules; duplicates, hidden fees and sync timing [DIGITS-BANKREC-2025] |
| Month-end close | Entries, accruals, review, sign-off, lock the period | data-reporting, review-assurance | Clients expect about 10-12 days; headcount caps capacity [ACCTODAY-COHNPOD-2026] |
| Reporting | Package, variance commentary, KPI dashboards | document-production, data-reporting | Commentary added late; static PDFs; dashboards slow to build [JOFA-CASAI-2026, DIGITS-TFMA-2026, ACCTODAY-CASKEYS-2026] |
| AP, bill pay, payroll | Invoice capture and coding, approvals, payments; payroll prep and entries | transaction-processing | Re-keying from email; payment fraud; client-by-client reports [ACCTODAY-GUSTO-2026, AFP-PAYFRAUD-2026] |
| Controllership, fractional CFO | Memos, budgets, 13-week cash flow, board packs, advice | expert-judgment | Scarce senior time; hours-based fees [CFODIVE-FRACTIONAL-2026] |
| Client collaboration | Questions, document chasing, status | client-interaction, coordination-scheduling | Email replies took 10-12 days at one firm [DIGITS-ELEV8-2026] |
| Practice layer | Checklists, portfolio status, offshore pods, tool approval | coordination-scheduling | About 10 apps per firm, 41% fully integrated, about 5 hours a week re-keying [INTUIT-ACCTTECH-2026] |

**Context.** In a recent Accounting Today survey, 85% of 88 responding Top 100 Firms reported a boost in CAS
[ACCTODAY-BONADIO-2026]; the 2024 CAS Benchmark Survey (CPA.com and AICPA PCPS, 200+ respondents) found median growth
of 17% [JOFA-CASTIPS-2025]. Withum's advisory leader says an advisory practice built on a small CAS team reached "$70
million in revenue in the space" in seven years and that advisory "sells best next to CAS" [ACCTODAY-CASKEYS-2026].
Bonadio's outsourced accounting leader describes an "evaporation of traditional bookkeepers" [ACCTODAY-BONADIO-2026].

## 3. Where AI is changing the work

Grouped by the four Reimagine lenses: improve (assist or augment a step), automate (no person on the normal path),
delegate (an agent owns a multi-step outcome), reinvent (the service or operating model changes). Every ladder level
and change scope has entries. Delegation rests on vendor and AI-native practice evidence (`#03` B; `#16`, `#17` C);
the only grade A is at automate-step (`#01`). Four entries are controls or ideas (`#21`-`#24`).

**Transaction coding and reconciliation**
- Automate: `#01` confidence-gated categorization; uncertain items go to an accountant (Choi and Xie: 7.5-day shorter
  close, 12% more granular ledgers, associations). `#02` AI matching with a short exceptions list (unnamed Top 100
  firm: 8 to 5 hours on specific reconciliations, vendor case study; Hiline named by Digits, no figure).
- Improve: `#04` staff post entries via a general assistant with ledger write access and locked periods (Arclow).

**Close and reporting**
- Delegate: `#03` agents prepare the close across a portfolio and accountants approve entries and review finished
  books (Pilot Meridian, Ramp Stack, BlackLine Verity Prepare, Basis, Arclow; CohnReznick pilot being set up).
- Automate: `#05` continuous close and automated packages on an AI-native ledger (solo firm: close 18 to 5 days).
- Improve: `#06` AI-assisted live dashboards and variance explanations (Bonadio, small firms; Withum's view; no named
  firm reports AI-drafted commentary). `#07`
  forecasts, budgets and on-demand finance answers from ledger data (Armanino 13-week cash flow, 2024).

**Controllership and fractional CFO**
- Improve: `#08` technical memos from a retrieval index of past memos (Eventus: 4 hours to 30 minutes, an estimate).
- Reinvent: `#20` advising clients on their own AI adoption as a new service on the CAS relationship.

**Onboarding, cleanup and client requests**
- Automate and reinvent: `#09` cleanup, catch-up and migration in days, sold as projects or recurring engagements
  (TFMA 2-4 days; Elev8 27 clients in about 40 hours; Excel agent under a written skill).
- Improve: `#12` AI chasing of documents and questions in the ledger (announced); `#13` cross-client close view (beta).

**AP, bill pay and payroll**
- Automate: `#10` invoice capture, coding and approval routing, with fraud screening before release (BILL, Xero;
  vendor aggregates only). `#14` in-house controller tickets scanned mail and invoices (Capital Area Food Bank).
- Improve: `#11` payroll prep with anomaly flags, payroll entries and liability tie-out (Gusto, Intuit, Ramp; announced).

**Delivery and business model**
- Improve the process: `#15` offshore pods rebuilt around documented processes, AI and onshore review (CohnReznick).
- Reinvent: `#16` AI-native provider sells autonomous bookkeeping direct to small businesses (Pilot AI Accountant).
  `#17` provider supplies platform and leads while a local firm delivers. `#18` a Top 20 firm co-builds a
  firm-trained model (CLA with Digits, announced). `#19` vendor outcome pricing: the firm pays only for clients at 95%
  zero-touch (Digits).

**Controls that make the rest safe**
- `#21` idea: five written controls before agents touch a production close, with risk-tiered review and reviewer
  calibration. `#22` firm AI policy, approved tools, vendor data terms, change control for firm-built automations.
  `#23` AI disclosure, consent and client AI terms. `#24` idea: independence and data-custody screening.

## 4. Interview probes

Ask in the person's setting (top-100 CAS practice, small firm, fractional CFO, AI-native provider, in-house team).

1. **"Walk me through one client's month: coding, reconciliations, close, package. Where do the hours go, and how many
   clients per accountant?"** Reveals the baseline and whether the pain is coding (`#01`), reconciliation (`#02`),
   close (`#03`) or reporting (`#05`, `#06`).
2. **"Which step runs with no person on the normal path today? What share of transactions, what threshold, who set
   it?"** Separates the 30% embedded from the 54% situational [INTUIT-ACCTTECH-2026]; shows whether `#01` is live.
3. **"When the AI is uncertain or wrong, who sees it first? Do you track override and error-found-in-review rates,
   by reviewer seniority?"** Reveals review design and the junior-acceptance risk (`#01`, `#21`). Usually untracked.
4. **"What can an agent write to the ledger, and what stops it editing a closed period?"** Reveals whether locked
   periods, plan approval and audit trails exist (`#03`, `#04`).
5. **"Before go-live, did you run a parallel close or validate vendor match rates on your own data?"** Reveals
   whether any quality evidence exists; Elev8's owner advises one parallel close on five clients (`#05`, `#21`).
6. **"Did you build, buy from your ledger vendor, or adopt an AI-native platform? What is your exit plan if the
   vendor fails?"** Reveals platform strategy (`#18`) and Botkeeper-type exposure (`#03`, `#17`).
7. **"Which CAS services do you provide to clients you also audit, and under which rules?"** Reveals independence
   exposure: bookkeeping is restricted for SEC audit clients and limited under the AICPA and IESBA codes (`#24`).
8. **"Which AI tools touch client data, what do contracts say about retention and training, and what do engagement
   letters say about AI?"** Reveals data and consent gaps (`#22`, `#23`); three in five say clients ask for proof.
9. **"When a client's books are clean and current, what advisory have you sold them in the last year, at what fee
   basis?"** Tests the CAS-to-advisory claim (`#06`, `#07`, `#20`) and routes fee design to professional-services.
10. **"Since adopting the tools, what changed in clients per accountant, review time and the clients you accept or
    refuse? Where did saved hours go?"** Reveals whether capacity was redeployed (professional-services-firm-finance-09).
11. **"How do juniors learn to judge a coding or accrual if AI does the first pass?"** Reveals pipeline risk (`#01`,
    professional-services-talent-learning-07).
12. **"Are AI-native providers or clients doing it themselves taking simple bookkeeping work from you?"** Reveals
    competitive pressure (`#16`, `#19`) and the case for moving up to review and advice.

## 5. Metrics and benchmarks

**Baselines to ask for first**: hours per client per month by complexity; days to close; clients per accountant;
review time per close; share of transactions auto-posted; exceptions per close; reviewer changes to AI output; cost
per client including software. COSO's illustrative metrics are a starting list: auto-posted transactions within
tolerance, exception aging, reversal and override rates [COSO-GENAI-2026]. A JofA guide suggests a 30-60 day pilot on
one workflow measuring time saved, added review time, error reduction and client feedback [JOFA-CASAI-2026].

**Independent measurement (associations, abstract-level)**: Choi and Xie, 79 SMEs on one unnamed platform: 7.5-day
shorter monthly close, 12% more ledger granularity, about 8.5% of accountant time moved from data entry to
communication and quality assurance, 55% more weekly client support (working paper; not in the journal abstract)
`#01`. Junior staff accepted uncertain AI output more; reliance on non-consensus AI suggestions can raise error risk.

**Benchmarks (vendor-run unless stated; none is a production metric)**
- Digits, 2,000 transactions from four businesses: ledger-native model 97.8%, best one-shot general model 79.5%, best
  look-up agent 88.9%, 12 outsourced accountants seeing the books cold 79.1% `#01`.
- DualEntry: best of 19 general models 77.3% on 101 workflows (March 2026); leaderboard top 91.1% when read in October,
  with classification well above AR and month-end close `#01`, `#21`. Intuit bank-feed accuracy about 78% to nearly 88%.
- Mercor lab study (third party, simulated close tasks): AI 100% on 20 of 20 attempts; 12 licensed CPAs averaging
  about five and a half years' experience (Mercor calls them junior) generally below 50%; people with an assistant took
  about 15 times longer than the model alone `#03`, `#04`.
- Penrose (one SaaS business, mid-2025 models): balances within 1% early, more than 15% off after several months;
  revenue overstated 5-30% `#03`.

**Named outcomes (self-reported or vendor-published; time, not quality)**: Elev8 close 18 to 5 days and about 108 to 20
hours a month `#05`; Arclow two quarterly closes about 7 hours to 1 hour 40 minutes `#04`; unnamed Top 100 firm 8 to 5
hours on specific reconciliations `#02`; TFMA cleanups in 2-4 days, Adept about 75% less bookkeeping `#09`; Eventus
memos 4 hours to 30 minutes `#08`; Capital Area Food Bank about 4 hours a week `#14`; Basis 30% average time savings
and BlackLine early adopters up to 92% less reconciliation prep (unnamed) `#03`; one top-400 firm's automation about 75%
to 98% (Digits) `#19`. BST & Co.'s CAS leader went from about 1,700 to 500-600 billable hours a year while CAS revenue
grew 47%, not attributed to AI [JOFA-CASTIPS-2025].

**Adoption and market** (vendor surveys skew to adopters)
- 88% use AI for at least one client service, 30% embedded as default, 54% situational (Intuit, n=725)
  [INTUIT-ACCTTECH-2026]. 98% use AI, 21% have an AI policy or strategy, 60 minutes a day saved per employee
  (self-reported) [KARBON-SOAI-2026].
- 67% of 200+ firm leaders agree AI is pushing them toward CAS; 9% report substantial results on scaling capacity
  without headcount; fixed fee 66%, hourly 60% [BILL-AIAMBITION-2026].
- 29% of firms offshore (AICPA PCPS and CPA.com) `#15`. The JofA says 90% of CAS practices sell fixed-fee recurring
  services, citing no source [JOFA-CASTIPS-2025]. CAS margins "over 40%" at some firms and 60-70% gross margin
  in Woodard's consulting data, unaudited [WOODARD-TWR-2025]. Interim CFO demand up 14% year on year (Business Talent
  Group, cited by CFO Dive) [CFODIVE-FRACTIONAL-2026].

## 6. Guardrails

**No standard or regulator has issued AI guidance written for CAS.** Existing duties apply:
- **AICPA Code.** Competence and due care are unchanged and the member owns the final work product; ask whether data is
  confidential client information and whether the client consented before it goes into AI [JOFA-ETHAI-2026].
- **Independence** (the firm's own audit clients only). SEC Rule 2-01(c)(4) bars bookkeeping and financial-system
  design for issuer audit clients, and (c)(5) bars contingent fees [SEC-RULE2-01-2026]. The AICPA permits nonattest
  services when the client takes management responsibility (2016 description) [JOFA-NONATTEST-2016]; IESBA allows
  routine or mechanical bookkeeping for non-public-interest audit clients and treats hosting client data as a
  management responsibility [IESBA-TECHREV-2023]. Developing or hosting AI for an attest client can raise concerns
  [JOFA-ETHAI-2026]. PE-backed structures split attest and advisory arms (Crowe) and the AICPA rule is still
  moving `#24`.
- **Data.** The FTC Safeguards Rule covers firms that complete income tax returns (service-provider oversight, a
  Qualified Individual); section 7216 consent and Circular 230 section 10.36 apply to tax work [FTC-SAFEGUARDS-2026,
  IRS-OPR-2026]. No federal law or professional standard requires CPAs to disclose AI use [JOFA-DISCLOSE-2025].
- **Control frameworks.** COSO's February 2026 guidance on generative AI (eight capability types; reliance on AI
  output needs ICFR-grade evidence) [COSO-GENAI-2026]; SQMS No. 1 for compilation and review work from 15 Dec 2025
  [LINFORD-SQMS-2024]. Sources conflict on AICPA SOC guidance for AI (`#21`).

**Design guardrails seen in products and guidance**: confidence thresholds with exception queues (`#01`); nothing posts
without approval (Ramp) and locked-period review queues (Digits) (`#03`, `#04`); agent actions logged (Intuit skill runs, Pilot decisions);
validation on the client's own data before relying on vendor match rates (`#02`); a parallel close on a starter cohort
(`#05`); an agent inventory with a named owner and an exit threshold (`#21`); keep your own data exports (`#16`).

**Steps that stay with a person**: low-confidence coding and recurring-merchant exceptions; write-offs and opening
balances; accruals, estimates and technical memos; approval of agent plans, entries and locked-period changes;
month-end sign-off; payment approval and release; variance explanations before they reach the client; independence and
consent decisions.

## 7. Roles and how they evolve

- **From keying to reviewing.** Choi and Xie find time moving from data entry to communication and quality assurance,
  with experienced accountants gaining more (`#01`). Hiline's accounting services manager says AI bank reconciliations
  "flipped" her role to reviewing exceptions, and FloQast's case firm describes moving from ticking and tying to
  client consulting (`#02`).
- **Seniors move up a layer.** CohnReznick expects senior accountants to do more review and client time; a Deloitte
  contributor expects staff to orchestrate AI-prepared work (`#03`). Pilot sets success as more clients per
  accountant and less review time per close.
- **Reporting to interpreting.** Bonadio's outsourced accounting leader calls the practice "the quarterback between
  advisory and compliance"; Aprio's CAAS manager posting lists dashboards, board narratives, 13-week cash flow and
  AI-enabled delivery methodologies (`#06`, `#07`).
- **The CFO as AI guide.** A fractional CFO calls helping clients adopt AI "a new responsibility for the CFO" (`#08`,
  `#20`). **Offshore work becomes review work** (CohnReznick), with mid-level roles harder to fill (`#15`).
- **New roles**: agent owners and AI leads (`#21`, `#22`); controllers who build automations (`#14`); vendors hiring
  accountants to write agent procedures and skills (Basis) and solutions engineers with three to five years of public
  accounting experience in audit, tax or CAS (Pilot) [BASIS-JOBS-2026, PILOT-JOBS-2026] (`#03`).
- **Juniors and the pipeline.** Juniors accept uncertain AI output more readily (`#01`). Hiring signals: strategic
  judgment (38%) and AI fluency (22%) lead; 56% say an entry-level hire needs six months or more to reach full
  billable capacity [INTUIT-ACCTTECH-2026]. Stanford/ADP data show employment of 22-25-year-olds in AI-exposed
  occupations 19% below trend, not accounting-specific and descriptive [STANFORD-CANARIES-2026]; ICAEW reports the
  Big Four still plan to hire at least 1,000 juniors each [ICAEW-HOWTO-2026]. Staffing design is in professional-services.

## 8. Frontier

- **2025-08-05** Penrose's long-horizon benchmark shows compounding errors and agents bypassing checks [PENROSE-ACCTBENCH-2025].
- **2025-12-09 / 2026-02-04** Pilot launches a Local Partner Program, then an AI Accountant it calls fully autonomous
  [CPAPA-PILOTPARTNER-2025, CPAPA-PILOTAI-2026].
- **2026-02-09 / 02-24 / 02-28** Botkeeper announces closure; Basis raises $100M (claims use by about 30% of the top 25
  firms); Xendoo buys Botkeeper's platform [UKU-BOTKEEPER-2026, BASIS-SERIESB-2026, CPAPA-XENDOO-2026].
- **2026-02** COSO guidance on internal control over generative AI (reported 2026-02-26) [COSO-GENAI-2026, JOFA-COSO-2026].
- **2026-04-07** Digits announces pay-only-at-95%-zero-touch pricing for firms [DIGITS-OUTCOME-2026].
- **2026-05-08** Intuit launches QuickBooks Workforce with a Payroll Agent [ACCTODAY-QBWORKFORCE-2026].
- **2026-06** Ramp announces Stack (06-03); Pilot releases Meridian for firms (06-16); Intuit describes expert-verified
  auto-categorization and cross-client insights (06-26); the Choi and Xie paper appears in the Journal of Accounting
  Research [ACCTODAY-RAMPSTACK-2026, ACCTODAY-MERIDIAN-2026, CPAPA-INTUITCONNECT-2026, STANFORD-JAR-2026].
- **2026-06-24** IRS OPR guidance on AI in tax practice, including fees for time not spent [IRS-OPR-2026].
- **2026-07-21 / 07-27** CLA announces a firm-trained model with Digits for its CAAS practice; BlackLine makes
  Verity Prepare generally available [ACCTODAY-CLA-2026, CPAPA-BLACKLINE-2026].
- **2026-08-07** Crowe closes KKR's strategic investment; Crowe LLP keeps attest work and Crowe Advisory LLC provides
  non-attest services [CROWE-KKR-2026].
- **2026-09-02** Accrual buys Puzzle's firm technology; CAS offering in early access, wider by end of 2026 [ACCTODAY-ACCRUAL-2026].
- **2026-10-01 to 10-16** Mercor and Digits benchmarks published [MERCOR-APEX-2026, DIGITS-BENCH-2026, ACCTODAY-AIBENCH-2026].
- **2026-10-09 / 10-13** Gusto adds AI-guided payroll prep; Digits ships agent write access with locked periods
  [ACCTODAY-GUSTO-2026, DIGITS-WRITEMCP-2026].
- **2026-10-19** AICPA and AIUC announce a joint SOC 2 plus AIUC-1 engagement; full launch expected early 2027 [JOFA-AIUC-2026].
- **Watch:** the 2026 CAS Benchmark Survey report, due December 2026 [CPACOM-CASBENCH-2026]; named customer results
  for Meridian, Stack and Basis; a second AICPA exposure draft on alternative practice structures [JOFA-PEEC-2026].

## 9. Common objections

- **"Reviewing AI takes as long as doing it."** Sometimes true: a forum thread says so, and 97% accuracy still means
  many errors at volume. Route by confidence, review exceptions, sample auto-posted items, and measure added review
  time in the pilot (`#01`, `#21`).
- **"The accuracy numbers are vendor marketing."** Mostly correct. The independent study reports associations, Digits
  and DualEntry run their own tests, and Mercor's tasks favoured models. Validate on your own clients' data and run a
  parallel close (`#02`, `#05`).
- **"General AI can't do bookkeeping."** Alone, general models plateaued near 79% on categorization in Digits' test;
  the gain came from each client's booking history (ledger-native or look-up). Pick tools that use client context (`#01`).
- **"Agents will post errors to the books."** Design for it: plan approval, nothing posts without authorization,
  locked-period queues, monthly review before the next opening balance. Penrose saw errors compound when unattended (`#03`, `#04`).
- **"Our vendor could disappear."** It happened: Botkeeper announced its closure in February 2026, and firms migrated
  during the weeks before Xendoo revived the platform. Keep exports and an exit plan (`#03`, `#17`).
- **"AI-native providers and clients will take the work."** Pilot sells autonomous bookkeeping direct, and consultants
  report clients arriving with AI-prepared work. An AI consultant (Edgefield Group) says autonomy only works for
  constrained, simple cases today; move toward review, interpretation and AI advisory (`#16`, `#20`).
- **"We can't put client data into AI."** Not into consumer tools. Use enterprise tools with written no-training
  terms, an approved-tool list and client consent where needed (`#22`, `#23`).
- **"We can't offer this to audit clients."** Correct for bookkeeping to SEC audit clients and limited elsewhere; the
  restrictions apply only to clients the firm also audits or reviews. Screen by client, not service line (`#24`).
- **"Savings will just be given away."** That is a pricing choice: under fixed fees the firm keeps the gain until
  renegotiation, and the IRS says billing hours not spent may breach Circular 230 in tax matters. See
  professional-services-scoping-pricing-17 [IRS-OPR-2026].

## 10. Sources

Full details (title, publisher, type, URL, date, access) are in the YAML.
- **Academic:** STANFORD-JAR-2026; STANFORD-WP-2025; STANFORD-INSIGHTS-2025; MITSLOAN-CHOIXIE-2025; NBER-GENAIWORK-2023.
- **Regulators and standard-setters:** SEC-RULE2-01-2026; PWC-SECFAQ-2019; IESBA-TECHREV-2023; FTC-SAFEGUARDS-2026;
  IRS-OPR-2026; COSO-GENAI-2026.
- **Professional bodies:** JOFA-CASTIPS-2025; JOFA-CASAI-2026; JOFA-REALLIFE-2025; JOFA-EXCELAGENT-2026; JOFA-ETHAI-2026;
  JOFA-AIPOLICY-2026; JOFA-DISCLOSE-2025; JOFA-CHECKLIST-2026; JOFA-COSO-2026; JOFA-AIPA-2026; JOFA-AIUC-2026;
  JOFA-NONATTEST-2016; JOFA-PEEC-2026; TAXADV-7216-2026; NYSSCPA-CONTFEE-2015; ABA-FO512-2024 (search-only).
- **Firms and job postings:** ACCTODAY-CASKEYS-2026; ACCTODAY-BONADIO-2026; ACCTODAY-COHNPOD-2026; ACCTODAY-OUTSOURCING-2026;
  ARCLOW-SITE-2026; CROWE-KKR-2026; APRIO-JOB-2026; PILOT-JOBS-2026; BASIS-JOBS-2026; WOODARD-ENGLETTERS-2025;
  ZUELLIG-AIPOLICY-2026; LINFORD-SQMS-2024; HEPLER-CPALIAB-2026.
- **Vendors and benchmarks:** DIGITS-BENCH-2026; DIGITS-WRITEMCP-2026; DIGITS-BANKREC-2025; DIGITS-ELEV8-2026;
  DIGITS-LINCOLN-2026; DIGITS-TFMA-2026; DIGITS-ADEPT-2026; DIGITS-MANA-2025; FLOQAST-CASCASE-2026; MERCOR-APEX-2026;
  PENROSE-ACCTBENCH-2025; DUALENTRY-BENCH-2026; OPENAI-BASIS-2026; PILOT-AIACCOUNTANT-2026; PILOT-PARTNERHUB-2026;
  UKU-BOTKEEPER-2026; ANTHROPIC-PRIVACY-2026; MS-COPILOTPRIV-2026.
- **Press, podcasts, community:** ACCTODAY-AIBENCH-2026; ACCTODAY-DUALENTRY-2026; ACCTODAY-RAMPSTACK-2026;
  ACCTODAY-MERIDIAN-2026; ACCTODAY-ACCRUAL-2026; ACCTODAY-CLA-2026; ACCTODAY-DIGITSPRICING-2026; DIGITS-OUTCOME-2026;
  CPAPA-PILOTAI-2026; CPAPA-PILOTMERIDIAN-2026; CPAPA-PILOTPARTNER-2025; CPAPA-XENDOO-2026; CPAPA-ELEV8-2026;
  CPAPA-INTUITCONNECT-2026; CPAPA-AGENTSCLOSE-2026; CPAPA-BLACKLINE-2026; CPAPA-NUMERIC-2025; CPAPA-BILLAGENTS-2026;
  CPAPA-SETTLE-2026; BASIS-SERIESB-2026; ACCTODAY-GUSTO-2026; ACCTODAY-QBWORKFORCE-2026; ACCTODAY-XEROAI-2026;
  ACCTODAY-AITHOUGHT-2026; ACCTODAY-BIGYEAR-2026; ACCTODAY-TRENDS-2026; ACCTODAY-CATALYST-2026; ACCTODAY-MAVI-2026;
  ACCTODAY-USECASE-2024; CFODIVE-FRACTIONAL-2026; CFODIVE-XERO-2026; CFOCOM-DUALENTRY-2026; ACCOUNTEX-2026;
  WOODARD-TWR-2025; WOODARD-EP163-2026; BEANCOUNT-REVIEWBURDEN-2026; KARBON-ENGAGE-2026 (scheduled-session listing).
  Surveys: INTUIT-ACCTTECH-2026; KARBON-SOAI-2026; AFP-PAYFRAUD-2026; TR-FOP-2026.
- **Not in the YAML:**
  - BILL-AIAMBITION-2026: BILL with NewtonX, *Accounting Firm AI Ambition Survey, vol 4* (200+ firm leaders, fieldwork late 2025), 2026 (page undated), https://www.bill.com/blog/ai-ambition-survey-vol-4-findings
  - CPACOM-CASBENCH-2026: CPA.com and AICPA PCPS, *CAS Benchmark Survey* page (2026 report due December 2026), 2026, https://cpa.com/cas-benchmark-survey
  - STANFORD-CANARIES-2026: Brynjolfsson, Chandar, Chen, *Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI* (August 2026 version), Stanford Digital Economy Lab, 2026-08, https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf
  - ICAEW-HOWTO-2026: ICAEW, *Why we still need junior accountants and how their role might change*, 2026-04-02, https://www.icaew.com/insights/viewpoints-on-the-news/2026/apr-2026/why-we-still-need-junior-accountants-and-how-their-role-might-change
