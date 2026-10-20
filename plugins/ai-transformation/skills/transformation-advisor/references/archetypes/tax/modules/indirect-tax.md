# Indirect tax (tax)

Sources checked 2026-10-17. Use cases live in `../use-cases/indirect-tax.yaml` (22 entries). Ids are shortened
here: `#05` means `tax-indirect-tax-05`; other modules' ids are in full. Source keys in brackets are in the YAML or in
§10. Read this first: almost every figure in this module is **vendor-published** (Thomson Reuters, Avalara, Sovos,
Vertex, Numeral, Fonoa). No error rate, override rate or parallel-run result exists for any commercial indirect-tax AI
tool. The only measured AI results are a VAT place-of-supply study (independent, `#06`) and Dell's tax-code test
(self-reported, `#01`); a synthetic agent pilot behind an idea (`#22`) also reports scores. The module is honestly
thin: 4 of 22 entries are graded A or B. Say "vendor claim" whenever you quote a vendor figure.

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

Taxes on transactions rather than income: VAT and GST (value added and goods and services taxes) and US sales and use
tax. The work runs from tax determination at each sale through product mapping, exemption certificates, registration
and nexus (the sales level that creates a duty to collect in a US state), returns, e-invoicing and continuous
transaction controls (CTC: the authority sees or clears each invoice in real time), to audits and notices. It covers
in-house tax departments, advisers and managed-service providers. Tax-authority AI is in the controversy module.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Determination | Engine sets taxability, rate and place of supply for each transaction from ERP, billing or checkout | transaction-processing | Vendors keep it rule-based [FONOA-STACK-2025, TR-AGENTICIT-2026]; stale rules multiply errors [STI-AGENTIC-2026] |
| Product mapping | Map each product (SKU) to a tax code or category | transaction-processing, data-reporting | Thousands of SKUs, manual, inconsistent; wrong code means wrong tax [TR-CLASSIFICATION-2026] |
| Exemption certificates | Collect, validate, store and link customer certificates | review-assurance | Manual; invalid certificates found only at audit (`#03`, `#04`) |
| Registration and nexus | Track thresholds, register in new states or countries | transaction-processing, expert-judgment | A few stray orders from a new channel can cross a threshold [TAXCLOUD-2025] |
| Returns and filing | Import, validate, map to forms, reconcile, file and pay | data-reporting, transaction-processing | 19,000+ US jurisdictions [TR-SUTAI-2026]; 71% have not fully automated one workflow end to end [FONOA-176-2026] |
| E-invoicing and CTC | Issue structured invoices, clear them with the authority, fix rejections | software-systems, transaction-processing | Risk moves from filing time to the invoice [INNOVATETAX-VXE-2026]; ownership split Finance 38%, Tax 30%, IT 11% [KPMG-INDIRECT-2026] |
| Input VAT recovery | Validate supplier invoices, receipts and expenses; reclaim VAT | transaction-processing | Fragmented receipts; VAT lost [SOVOS-BLUEDOT-2026] |
| Data quality | Fix master and transaction data feeding the engine | data-reporting | Top concern for 58%; 61% fix it by hand; 23% say their ERP is fit for purpose [KPMG-INDIRECT-2026] |
| Regulatory change | Watch rule, rate and mandate changes across countries | research-synthesis | 70+ countries changed e-invoicing rules since 2020 (vendor statement) [FONOA-MONITORING-2026] |
| Audits and notices | Answer authorities, produce records of decisions | review-assurance, document-production | 57.4% not confident defending AI-assisted decisions [FONOA-2026]; authorities arrive with data already analysed [TRINST-TEIAUDITOR-2026] |
| Advice and new models | Marketplace and agentic-commerce status, scenarios, accruals | expert-judgment | Who collects when an AI agent buys is unsettled [BTAX-AGENTICCOMMERCE-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (the service or operating model changes). Every vendor filing, rule-activation and correction design
reviewed puts a person's approval first.

**Determination and product mapping**
- Improve: `#01` AI proposes product tax codes with confidence scores; a person confirms. The only measured result is
  Dell's own HSN/SAC code model: precision 70%, recall 61% against experts (grade A). Vertex, Thomson Reuters, Sovos
  and Avalara offer or announce versions; their speed claims are vendor figures.
- Improve: `#07` plain-language rule drafting, simulated on past transactions and approved before activation (Avalara,
  Vertex; announced).
- Idea: `#22` a deterministic rule engine checks each step of an AI agent's VAT determination.

**Exemption certificates**
- Improve: `#03` AI validates and routes certificates as they arrive (Avalara; announced).
- Automate: `#04` re-validating the whole certificate store; Numeral says 30-40% of migrated certificates fail (vendor).

**Returns and filing**
- Delegate: `#02` agents import, validate, map and prepare sales and use tax and VAT returns; filing waits for
  approval (Thomson Reuters ONESOURCE Sales and Use Tax AI, Avalara Returns AI, Deloitte proofs of concept). Vendor
  claims: up to 65% less routine reporting time, 30 to 11 days, up to 75% lower audit exposure. Customers unnamed.
- Improve (process): `#11` anomaly detection and exception triage across all invoices before filing.

**E-invoicing and continuous transaction controls**
- Improve: `#08` diagnosis of rejected e-invoices, with corrections run after a user approves (Sovos). Sovos's 1.6%
  French rejection rate is a platform figure it does not attribute to AI (data side: `tax-data-technology-14`).
- Automate: `#10` extraction and enrichment of invoices, receipts and expenses for VAT recovery and e-invoicing
  onboarding (Blue dot, now Sovos; Brinta, now Vertex).
- Reinvent: `#18` finance agents for AP, procure-to-pay and invoicing with VAT rules built in (Sovos-Flowie, announced 1 Oct 2026).

**Registration and nexus**
- Delegate: `#13` agents monitor nexus, answer nexus questions and prepare and file registrations (Avalara early
  access, Numeral, Deloitte illustration). Numeral claims up to 80% less time on filings and registrations.

**Research and regulatory change**
- Improve: `#05` grounded taxability Q&A inside the tax platform; Singer Equipment's tax accountant used Avalara
  Aviator in beta (grade B, no measurement). `#06` VAT place-of-supply assistant checked by an adviser: 16 of 20 real
  client cases correct (grade A, research prototype). `#09` (process) regulatory-change monitoring with alerts tied to
  primary sources (Fonoa, Sovos; announced).

**Audits, notices and defensibility**
- Automate: `#14` intake, extraction and routing of authority notices. Reading and reply drafting are
  `tax-controversy-01` and `tax-controversy-02`.
- Improve (process): `#15` audit-ready records of every AI-assisted determination, override and approval. The
  strongest survey link to confidence: respondents with formal human review were more than twice as likely as those
  with no defined process to feel able to defend AI decisions (Fonoa, vendor survey; see also `tax-data-technology-19`).

**Data foundation and everyday use**
- Idea (process): `#12` validation and repair of master and transaction data at entry (Deloitte describes it as a
  potential use; 49% of KPMG respondents say data quality will be their main AI use). The fuller entry on validation
  before submission is `tax-data-technology-13`.
- Improve: `#20` general AI for first-pass analysis and month-end summaries in a sanctioned workspace (Plusgrade job
  posting, grade B). Analyst-built pipelines are `tax-compliance-corporate-17`; Oxford Industries' governed
  automation, whose vendor demos also covered sales and use tax and VAT, is `tax-compliance-corporate-10`.

**Commerce, delivery model and advice**
- Automate: `#17` tax determination at checkouts that AI shopping agents complete; keep tax in the merchant's engine
  and make holiday rules machine-readable (Sales Tax Institute; emerging).
- Reinvent: `#16` tax engines callable by customers' own agents through MCP (Model Context Protocol) and A2A
  (agent-to-agent) protocols (Avalara, Sovos; announced; the company side is `tax-data-technology-18`). `#19`
  AI-enabled managed sales tax and VAT compliance (Numeral, Taxually). The VAT and customs part of cross-tax
  intercompany review is `tax-transfer-pricing-11`.
- Idea: `#21` ongoing exposure, accrual and scenario analysis by agents (Deloitte).

**Tax-authority side (context, held elsewhere)**: California CDTFA's agent-assist tool for sales and use tax enquiries
is `tax-controversy-20`; authority chatbots including Singapore's IRAS are `tax-controversy-18`; risk targeting in
Austria, Hungary (including at invoice issuance) and South Carolina sales and use tax is `tax-controversy-15`.

**Coverage.** Ladder: assist 1, augment 12, automate 5, delegate 4. Scope: step 9, process 10, model 3. Assist-level
evidence is described inside augment entries. Delegate rests on vendor launches with unnamed customers; no measured
delegate deployment exists. Model-scope entries are announcements plus one provider's own funding release (`#19`).
No AI evidence was found for VAT on imports, Peppol networks, SAF-T reporting or India, Brazil and Gulf markets
beyond headlines.

## 4. Interview probes

1. **"Which indirect-tax decisions are made by a deterministic engine and which by a model or agent today? Who drew
   that line?"** Reveals whether AI touches the calculation itself, which vendors and researchers advise against
   (`#22`), or stays in mapping, research and exceptions.
2. **"Pick your last AI-assisted determination or filing. What record shows the rule version, inputs, reviewer and
   approver, and could you give it to an auditor within a day?"** Reveals audit defensibility (`#15`); 57.4% would
   not be confident defending an AI-assisted decision.
3. **"What are your human error and override rates for product mapping, certificate checks and return lines? Have
   you measured an AI tool against them?"** Reveals whether any baseline exists; without one, vendor claims cannot be tested.
4. **"Which of these does a vendor agent do without a person today: validate certificates, prepare a return, file,
   register, correct an e-invoice?"** Reveals the real ladder position (`#02`, `#04`, `#08`, `#13`).
5. **"Who owns e-invoicing and its master data: Tax, Finance or IT? What share of rejections trace to master data,
   and what happens when one lands on a filing day?"** Reveals readiness for `#08` and `#12`.
6. **"What share of data fixes are manual? Is your ERP fit for tax? Do you have technology specialists in the team?"**
   Reveals the data constraint (KPMG: 61% manual, 23% ERP fit, a third with no specialists).
7. **"Who owns AI in the tax function? Which tools do people use that the function has not approved?"** Reveals shadow
   AI and confidentiality exposure (`#20`); at TEI two hands of 50+ said tax owns AI implementation.
8. **"When did you last validate the whole certificate store? What share failed?"** Reveals hidden exposure (`#04`).
9. **"If an AI agent bought from your site or marketplace tomorrow, which engine rules (holidays, exemptions, mappings)
   would apply, and who confirms they are current and machine-readable?"** Reveals agentic-commerce readiness (`#17`).
10. **"What would an authority holding your transaction-level invoice data see that your returns do not, and how do
    you reconcile to it?"** Reveals exposure under CTC and ViDA reporting.
11. **"For any vendor AI figure you rely on, what customers, baseline and sample stood behind it? Did you run it in
    parallel?"** Reveals how much of the business case rests on unverified claims.
12. **"Has AI reduced your workload yet, or added a review step?"** Reveals the common pattern Fonoa reports: only
    6.8% saw workload fall in the past year.

## 5. Metrics and benchmarks

**Research results (academic papers and one company test; dated by model generation)**
- VAT place of supply (Austrian and EU law): 93.24% on 74 textbook cases with RAG (retrieval-augmented generation),
  68.92% plain GPT-4o; 16 of 20 real client inquiries correct with RAG, 55-70% for other set-ups [LUKETINA-VAT-2026].
- Synthetic cross-border VAT agents: 0.755 single agent, 0.830 best orchestrated; one hallucinated record degraded
  every set-up [SANTOS-VAT-2026]. Adjacent: frontier models compute under a third of simplified US income tax
  returns correctly [COLUMN-TAXCALCBENCH-2025].
- Dell HSN/SAC code prediction (self-reported test set of 16,000 records): precision 70%, recall 61%, F1 65% [NATH-DELL-2025].

**Surveys (none is a probability sample)**
- Fonoa, 176 indirect tax leaders, Jun 2026, vendor-sponsored: 92% use AI in some form; 12.5% have specific AI
  targets; 57.4% not confident defending AI decisions; about a third run formal documented sign-off; 60.8% rely mainly
  on individuals using public tools; 71% have not fully automated one workflow; 6.8% saw workload fall in the past
  year, 85.8% saw it grow over two years, 31.2% grew headcount; 2.8% fully formalised, reporting workload falling at
  8x the rate of others [FONOA-2026, FONOA-176-2026].
- KPMG, 53 large multinationals, May 2026: data quality top concern 58% (44% in 2021); 61% fix data manually; 23% ERP
  fit for purpose; 58% have a VAT/GST control framework, 28% call their controls ineffective; local in-house return
  preparation 23% (44% in 2021) against 26% co-sourced and 19% outsourced [KPMG-INDIRECT-2026].
- Thomson Reuters, Aug 2026: 65% use GenAI tools, 26% measure ROI, 36% of corporate professionals use unsanctioned
  tools; denominators undefined [TR-INDIRECT-2026]. Deloitte relays that 77% of surveyed tax leaders require 90%+
  accuracy before trusting AI [DELOITTE-AGENTIC-2026].
- Avalara/Censuswide, 1,500+ finance leaders (finance-wide, not indirect-tax): 76% lack in-house expertise to
  understand how their agents work; 30% have not updated their control framework for AI-driven actions in the past year [AVALARA-GOVERNANCE-2026].

**Vendor claims (grade C; ask for named, measured cases)**
- Thomson Reuters: up to 65% less routine reporting time (40-60% in an earlier release); 30 to 11 days; up to 75% lower
  audit exposure; about $25,000 and $60,000+ a year saved (`#02`). 100 SKUs mapped in 5 minutes (`#01`).
- Vertex: categorization from more than 1.5 minutes to seconds per product (`#01`). Numeral: 30-40% of migrated
  certificates fail; up to 400 hours a year; up to 80% less time on filings and registrations (`#04`, `#13`).
- Sovos: 1.6% French rejection rate against an estimated 20% market-wide, not attributed to AI (`#08`); Blue dot
  accuracy above 98%, undefined (`#10`). Avalara: connectors in days, not months (`#16`).
- Pre-GenAI, commissioned, composite: Forrester study of ONESOURCE Indirect Tax, invoice error rate from 3% to well
  below 1% and 120% ROI over three years [TR-FORRESTER-2024].

**What to measure**: override rate on AI-proposed codes, certificate decisions and return lines; error rate against a
human baseline; e-invoice rejection rate and share caused by master data; time from rejection to fix; certificate
failure rate; notices and assessments per period; share of AI-assisted decisions with a complete record; review hours
per return, not preparation hours alone.

## 6. Guardrails

**No regulator has written rules specifically for AI in indirect tax.** The binding constraints are general:
- **EU ViDA (VAT in the Digital Age), Directive (EU) 2025/516**, adopted 11 Mar 2025, in force 14 Apr 2025: e-invoices
  should in principle follow the European standard EN 16931; 1 Jan 2027 OSS and IOSS clarifications; 1 Jul 2028
  single VAT registration and platform deemed-supplier rules (short-term accommodation, passenger transport; the
  directive lets Member States apply the platform rule as late as 1 Jan 2030); 1 Jul
  2030 digital reporting for cross-border B2B; 1 Jan 2035 alignment of domestic real-time systems. The Commission
  estimates up to EUR 11 billion a year less VAT fraud [EU-DIRECTIVE-2025-516, EC-VIDA-2026].
- **France**: from 1 Sep 2026 every established company must be able to receive e-invoices and large and medium
  companies must issue and report; smaller ones follow in Sep 2027 (vendor summary) [SOVOS-FRANCE-GOLIVE-2026].
- **Marketplace and deemed-supplier rules** apply by function (payment control, transmitting orders), not label; AI
  has no legal personality, so an agent's operator may have to collect [BTAX-AGENTICCOMMERCE-2026].
- **Shared conduct rules** (IRS Office of Professional Responsibility (OPR) Alert 2026-19, section 7216 consent, the UK PCRT
  (Professional Conduct in Relation to Taxation) and Australian Tax Practitioners Board guidance) are in
  [the archetype guardrails](../guardrails.md). The OPR alert covers federal practice and does not address state
  sales tax or VAT [IRS-OPR-2026]; the PCRT guidance applies to UK VAT work [ATT-PCRTAI-2026, ICAEW-PCRT-2026].
- **UK tribunal**: in *Rafique v HMRC* [2026] TC09874 a VAT-penalty appeal struck out for breaching unless orders was not
  reinstated; the tribunal found repeated AI-generated submissions with fabricated citations and said every party must verify what it submits [ROSSMARTIN-RAFIQUE-2026].
- **EU AI Act**: Article 4 requires AI literacy measures for staff [EU-AIACT-2024]. Recital 59 keeps tax-administration
  systems out of the law-enforcement high-risk class; Hadwick counts at least 85 such systems in 26 Member States [HADWICK-EUAIACT].
- **Authority advice**: California's Publication 70 excuses liabilities only for written advice, while AI-assisted
  answers from agency staff are verbal [CDTFA-2025].
- **Frameworks**: Werfel's 20-risk register and vendor-diligence questions (tamper-proof output log; scope limits
  enforced in the model) [AICPA-WERFEL-2026]; the AICPA Council on AI Risk in Tax launched 23 Sep 2026
  [AICPA-CART-2026]; NIST AI RMF, voluntary [NIST-AIRMF-2023].

**Design guardrails in vendor designs**: approval before filing, rule activation or correction (`#02`, `#07`, `#08`);
confidence thresholds that route uncertain items to people (`#01`, `#11`); primary source attached to every research
answer and alert (`#05`, `#09`); a decision log with rule version and approver (`#15`); calculation kept in the
deterministic engine (`#22`); customer data kept out of external model training (Sovos) [SOVOS-SOVI-2026].

**Steps that stay with a person**: taxability and place-of-supply judgments on new products or chain transactions;
approval of rule and mapping changes; sign-off of returns; registration decisions; certificate acceptance where
good-faith rules apply (those rules were not reviewed for this module); marketplace or deemed-supplier status; answers to authorities.

## 7. Roles and how they evolve

- **Data managers and ERP gatekeepers**: KPMG's survey foreword says indirect-tax professionals are likely to take these
  roles and to lead on AI in tax; 58% expect AI to leave headcount largely unchanged, 21% expect a rise, 21% a fall [KPMG-INDIRECT-2026].
- **Reviewers of AI output**: classifiers become reviewers of low-confidence cases (Thomson Reuters view)
  [TR-CLASSIFICATION-2026]; preparers move to review and sign-off (vendor projection) [TR-AGENTICIT-2026].
- **Tax technology roles appear in job postings**: OpenAI hires an Indirect Tax Technology Manager to run Vertex, product mappings,
  exemption configuration and testing [OPENAI-JOB-2026]; EY advertises an indirect-tax engine implementation manager
  [EY-JOB-2026]; Plusgrade's tax manager posting expects a CPA who builds AI workflows [PLUSGRADE-JOB-2026].
- **Hybrid skills**: the Vertex Exchange Europe recap describes teams combining tax with ERP, data, automation and AI
  [INNOVATETAX-VXE-2026]; a TEI recap calls the job as much data science as accounting [TRINST-TEIAUDITOR-2026].
- **Ownership gap**: tax rarely owns AI implementation [TEI-TAXTECH-2026]; Fonoa frames the leader's job as setting KPIs
  and accountability [FONOA-2026].
- **Workload outgrows teams**: 85.8% saw workload grow and 31.2% grew headcount [FONOA-176-2026].
- **Vendors' own staff**: Vertex announced a reduction in force (its CEO would not call it AI-related) while saying
  support analysts handle more cases with AI [VERTEX-Q1CALL-2026].

## 8. Frontier

- **2025-09-30** Avalara launches agents with "have your agent call our agent" and MCP servers [ACCTODAY-AVALARA-2025].
- **2026-01-15** Thomson Reuters launches ONESOURCE Sales and Use Tax AI, "touchless by default, manual by exception" [TR-SUTAI-2026].
- **2026-01-26 to 29** OECD VAT forum names AI and crypto emerging challenges for VAT administration [BTAX-OECDVAT-2026].
- **2026-02-24 / 07-29** Who collects tax when an AI agent buys; sales tax holidays at agent checkout [BTAX-AGENTICCOMMERCE-2026, STI-AGENTIC-2026].
- **2026-02-26** Hungary's audit plan says its authority uses AI models, including at invoice issuance [KPMG-HU-2026].
- **2026-03-24** Sovos: error remediation, Ask Sovi, MCP Gateway in development, A2A expected [SOVOS-SOVI-2026].
- **2026-05-07** Vertex: Smart Categorization in production use; Brinta acquired in Q1; ERP agents [VERTEX-Q1CALL-2026].
- **2026-09-01** France's e-invoicing mandate goes live [SOVOS-FRANCE-GOLIVE-2026].
- **2026-09 to 10** Fonoa reports headlines on Spanish B2B e-invoicing dates, Dutch plans and a Bulgarian proposal for 2028 [FONOA-BLOGINDEX-2026].
- **2026-08-24 / 09-02** A pilot on splitting VAT determination across agents and a peer-reviewed VAT RAG study [SANTOS-VAT-2026, LUKETINA-VAT-2026].
- **2026-09-15 / 10-01** Sovos buys Blue dot (VAT recovery AI) and Flowie (finance agents) [SOVOS-BLUEDOT-2026, SOVOS-FLOWIE-2026].
- **2026-09-23** Numeral raises $100M [NUMERAL-2026]; Avalara unveils Aviator, generally available 8 Oct per Avalara,
  which plans "self-healing" agents [AVALARA-AVIATOR-2026, AVALARA-CRUSHEU-2026]; AICPA launches CART [AICPA-CART-2026].
- **Watch**: Vertex Exchange, 25-28 Oct 2026 [VERTEX-EXCHANGE-2026]; German e-invoicing in 2027 (Vertex expects revenue
  to ramp then) [VERTEX-Q1CALL-2026]; HMRC plans real-time risking on VAT returns and guidance usable by AI products
  [HMRC-ROADMAP-2025]; ViDA 1 Jul 2028, 1 Jul 2030 and 1 Jan 2035 [EC-VIDA-2026].

## 9. Common objections

- **"AI can't be trusted to calculate tax."** Agreed, and the vendors and researchers reviewed don't ask it to: they keep
  the math in a deterministic engine [FONOA-STACK-2025, TR-AGENTICIT-2026]. The one real-case VAT study got 20-30% of
  analyses wrong and its authors call that unacceptable (`#06`). Use AI for mapping, research, exceptions and records.
- **"We could never defend an AI decision to an authority."** 57.4% feel that way. Fonoa's data say the predictor is a
  defined process, not the tool; a BDO partner: you are "demonstrating a process" [FONOA-2026]. Build the record (`#15`).
- **"The vendor says 65% time saved."** No baseline, sample or named customer is published, and two releases differ
  (`#02`). Ask for a named reference and run a parallel period.
- **"Our data isn't ready."** True for most: 58% name data quality their top concern [KPMG-INDIRECT-2026]. That is the
  case for starting with data validation and rejection diagnosis (`#12`, `#08`), not for waiting.
- **"AI will shrink the team."** Most respondents expect headcount unchanged, and workload grew for 85.8%; Fonoa says AI
  often adds a review step before it removes one [KPMG-INDIRECT-2026, FONOA-176-2026].
- **"People already use ChatGPT; that's fine."** 60.8% rely mainly on ungoverned public tools; client data in a public
  model is likely a confidentiality breach in the UK [FONOA-176-2026, ICAEW-PCRT-2026]. Move the work to approved tools (`#20`).
- **"A chatbot can look up rates."** Avalara's own one-off test caught a wrong effective date; a Florida attorney found
  about five serious errors in an AI draft (`#05`). Both sell sales tax services; still, demand primary sources.
- **"Agentic commerce is years away."** The checks are configuration work now: current, machine-readable holiday and
  exemption rules and catalogue data (`#17`). No regulator guidance exists yet.

## 10. Sources

- **In the YAML, research and standards:** LUKETINA-VAT-2026, SANTOS-VAT-2026, NATH-DELL-2025, COLUMN-TAXCALCBENCH-2025, IRS-OPR-2026, ICAEW-PCRT-2026, AICPA-WERFEL-2026, NIST-AIRMF-2023, EU-AIACT-2024, EU-DIRECTIVE-2025-516, HMRC-ROADMAP-2025, OECD-GOVAI-2025.
- **In the YAML, surveys, firms and conferences:** FONOA-2026, FONOA-176-2026, KPMG-INDIRECT-2026, TR-INDIRECT-2026, DELOITTE-AGENTIC-2026, INNOVATETAX-VXE-2026, TEI-TAXTECH-2026, TRINST-TEIAUDITOR-2026, SAFFERY-VAT-2026, FLSALESTAX-AI-2026, STI-AGENTIC-2026, BTAX-AGENTICCOMMERCE-2026, BTAX-VAT2026, BTAX-OECDVAT-2026, OPENAI-JOB-2026, PLUSGRADE-JOB-2026.
- **In the YAML, vendors:** TR-SUTAI-2026, TR-ONESOURCEPLUS-2025, TR-CLASSIFICATION-2026, TR-HELP-PRODCLASS, TR-AGENTICIT-2026, TR-INSTITUTE-2025, TR-BUSINESSCASE-2026, TR-WEBINAR-JLL, ACCTODAY-AVALARA-2025, AVALARA-AGENTIC-2025b, AVALARA-AVI-2025, AVALARA-AVIATOR-2026, AVALARA-CRUSHEU-2026, AVALARA-NEXT-2026, AVALARA-ECM-2026, AVALARA-LLMTEST-2025, SOVOS-SOVI-2026, SOVOS-FRANCE-GOLIVE-2026, SOVOS-FRANCE-2026b, SOVOS-BLUEDOT-2026, SOVOS-FLOWIE-2026, SOVOS-DOCS-AICLASS, VERTEX-Q1CALL-2026, VERTEX-SMARTCAT-2026, VERTEX-COPILOT-2025, FONOA-CITATION-2026, FONOA-MONITORING-2026, FONOA-STACK-2025, FONOA-ACCURACY-2025, FONOA-ERRORRATE-2025, NUMERAL-2026, TAXUALLY-2026, TAXCLOUD-2025, TRUSS-KINTSUGI-2026.
- **Not in the YAML:**
  - EC-VIDA-2026 (European Commission, *VAT in the Digital Age (ViDA)*, 2026-07-29, https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en).
  - CDTFA-2025 (Tax Notes, *Experts Urge Caution as State Tax Agencies Deploy Generative AI*, 2025-08-26, https://kogod.american.edu/hubfs/experts_urge_caution_as_state_tax_agencies_deploy_generative_ai_20250826-161144.pdf); in controversy YAML.
  - KPMG-HU-2026 (KPMG Hungary, tax alert, 2026-02-26, https://kpmg.com/hu/en/insights/2026/02/taxalert-2026-02-26.html); in controversy YAML.
  - HADWICK-EUAIACT (D. Hadwick, *Slipping Through the Cracks*, European Papers 9(3), 2024-12-30, https://www.europeanpapers.eu/e-journal/slipping-through-cracks-carve-outs-ai-tax-enforcement-systems-eu-ai-act).
  - ROSSMARTIN-RAFIQUE-2026 (Ross Martin Tax, summary of *Rafique v HMRC* [2026] TC09874, 2026-05-13, https://rossmartin.co.uk/sme-tax-news/8927-ai-hallucinates-at-the-ftt-again).
  - ATT-PCRTAI-2026 (ATT for the PCRT bodies, *Professional bodies issue AI advice to members*, 2026-01-19, https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members).
  - AICPA-CART-2026 (The Tax Adviser, Council on AI Risk in Tax, 2026-09-23, https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/).
  - AVALARA-GOVERNANCE-2026 (Avalara, *Agentic AI in finance: Speed is outrunning governance*, 2026-08-11, https://www.avalara.com/us/en/blog/agentic-ai-finance-governance-survey.html).
  - TR-FORRESTER-2024 (Thomson Reuters, Forrester TEI summary, 2024-03-25, https://tax.thomsonreuters.com/blog/the-corporate-tax-department-business-case-making-the-final-tax-technology-pitch/).
  - EY-JOB-2026 (EY Careers, Tax Technology and Transformation - Indirect Tax - Manager, 2026-10-15, https://careers.ey.com/ey/job/new-york-tax-technology-and-transformation-indirect-tax-manager-ny-10001-8604/1437580833/).
  - VERTEX-EXCHANGE-2026 (Vertex, Vertex Exchange 2026, 2026-06-24, https://www.vertexinc.com/node/8263).
  - FONOA-BLOGINDEX-2026 (Fonoa blog index, headlines only, latest item 2026-10-09, https://www.fonoa.com/resources/blog).
