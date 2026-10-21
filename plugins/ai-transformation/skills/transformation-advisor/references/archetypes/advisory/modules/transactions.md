# Transactions (advisory)

Sources checked 2026-10-20 and re-verified 2026-10-21. Use cases live in `../use-cases/transactions.yaml` (16 entries). Ids are shortened
here: `#04` means `advisory-transactions-04`; other modules' ids are in full. Source keys in brackets, such as
[FORVIS-QOE-2026], are in the YAML or in §10. **Evidence is thin.** No entry is graded A; 5 of 16 are graded B, and
those rest on named deployments with usage counts, not measured results. Every speed figure is vendor-published or
self-reported, with no method. No error rate, override rate, parallel run or independent accuracy test of AI-assisted
quality of earnings exists. Say so when you quote a figure.

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

Transaction advisory services (TAS): quality of earnings (QoE, the analysis of how much of a target's reported
earnings are recurring and supportable), financial due diligence (FDD) for buyers, lenders and sellers, data-room
review, deal support, and post-deal integration. Practitioners sit in Big Four deal groups, top-100 and mid-market
accounting firms, and a new set of AI-native QoE providers; their clients are PE sponsors, corporate acquirers,
searchers (individuals buying one small company) and lenders. Valuation, purchase price allocation and fairness
opinions are in the valuation module; transaction tax is in the tax archetype; how the firm prices and staffs its
own deal work is in professional-services.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Scoping, data request, data-room set-up | Agree scope, send request list, get access | coordination-scheduling, transaction-processing | Targets with little deal experience struggle to pull data, even when the adviser's tools are fast [FORVIS-QOE-2026] |
| Data ingestion and trial balance mapping | Load ledgers and statements, map accounts to a standard format | transaction-processing, data-reporting | A large share of junior time goes to collecting and checking data before interpretation [TECHEU-OPIO-2026] |
| Proof of cash | Tie revenue and expenses to bank statements | transaction-processing, review-assurance | Scanned statements, several accounts, system migrations, year-end-only accruals in small targets; weeks by hand [QOEAGENT-CASE-2026] |
| Trend, flux and anomaly analysis; management meetings | Find unusual movements, prepare questions | data-reporting, client-interaction | Teams eyeball trial balances and comb thousands of rows before the first meeting [CPAPA-AUDITSIGHT-2025] |
| Adjusted EBITDA, add-backs, net working capital, debt-like items | Normalize earnings; decide what changes the price | expert-judgment | Slow to support and trace in spreadsheets [SHEPI-HOME-2026]; where practitioners say AI is least reliable [WORKWISE-QOE-2026] |
| Customer, vendor, SKU and workforce analysis | Deeper cuts of the business | data-reporting | Gets more time only when routine work is automated [FORVIS-QOE-2026] |
| Contract and data-room review | Read agreements and documents for issues | research-synthesis, review-assurance | Data rooms grow, timelines compress [PWC-TOLTIQ-2026]; contract review was often descoped before AI [ICAEW-BIGSIX-2024] |
| Databook, red-flag report, summaries | Produce the deliverable | document-production | Specialist page production; an AI lab seeks managers with 4+ years to train models on it [GC-ETHOS-JOB-2026]; no source measures the time |
| SPA support and completion accounts | Support the sale and purchase agreement and closing accounts | expert-judgment, document-production | KPMG's TAS AI lead names carve-out planning and large data sets for completion accounts as AI roles; spoken view, no deployment detail [ICAEW-BIGSIX-2024] |
| Post-deal: Day 1, integration planning, TSAs, synergies | Plan and run integration | coordination-scheduling | Less structured and harder to scale than pre-deal work [CFODIVE-ACCENTURE-2026] |
| Sell-side readiness | Seller-commissioned QoE before marketing | document-production, review-assurance | Findings arrive late in a buyer's process and move price [PEASEBELL-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step; "(process)" marks augment entries that also redesign the flow), automate
(no person on the normal path), delegate (an agent owns a multi-step outcome), reinvent (the service or operating
model changes). Improve is crowded. Automate has one entry; delegate has only an idea (D); no named delegate
deployment exists. Firm types are given because the evidence differs sharply by type.

**Data, proof of cash and analysis**
- Improve: `#01` FDD workbench for ingestion, trial balance mapping and first-draft databook (Forvis Mazars Group
  rollout of Opio after a nine-month pilot; vendor claims 27% time saved per FDD; grade B). `#02` anomaly scoring
  of every transaction and flux analysis to prepare management meetings (Audit Sight; named customer Miller Cooper;
  vendor claims 80% less prep; grade B). `#10` (process) time freed from routine work goes to SKU, customer, vendor
  and working-capital analysis (Forvis Mazars US view; no tool named).
- Automate: `#03` AI agents run proof of cash and bank-to-ledger matching, CPAs review flagged items (QoEAgent,
  AI-native; "within 1% in 24 hours" vendor claim; one case where the buyer walked away; grade B).

**Adjustments and judgment**
- Improve: `#04` AI suggests EBITDA adjustment candidates, each linked to source evidence, and a person approves or
  rejects each (Shepi; demo figures only; grade C).
- Delegate (idea): `#16` an agent owns the whole QoE. Dealmakers rank it among disruptions expected by 2030
  [INTRALINKS-AIDEAL-2026]; a buyer's guide says no tool runs a full QoE [WORKWISE-QOE-2026].

**Data-room and document review**
- Improve: `#09` grounded data-room review with citations (PwC Deals with ToltIQ: 4,000+ practitioners, 5,000+
  deals; PwC UK with Harvey; grade B). Only adjacent accuracy data exists: a law firm's contract-review test,
  74% to 95% [ARTLAW-AG-2024].

**Deliverables**
- Improve: `#12` AI drafts QoE exhibits, summary slides and red-flag reports from workpapers (PwC UK, secondary
  report; an AI lab hiring TAS managers to train models on these pages; grade C).

**Lifecycle and integration**
- Improve: `#11` (process) Deloitte's M&A Platform with an agent harness, in more than 1,000 client engagements;
  EY-Parthenon's Diligence Edge (grade B on Deloitte's usage count). `#14` integration workplans, TSA drafts and
  synergy sizing (Bain forecast, survey data; grade C). `#15` (assist) chat over the target's system knowledge to keep
  rather than replace its ERP (academic case, unnamed firms).

**Sell-side and lender work**
- Improve: `#08` AI-assisted sell-side QoE and pre-sale readiness (Pease Bell, mid-market firm; no data). `#07`
  (process) lender QoE for SBA 7(a) acquisition loans under the SOP effective 2026-10-01 (QoEAgent offer; announced).

**Service and operating model**
- Reinvent: `#05` AI-native QoE tiers at fixed list prices (Shepi $1,000 self-service [SHEPI-PRICING-2026]; QoEAgent staged products;
  grade C). `#06` white-labelled AI QoE capacity sold to TAS and CPA firms (announced, no named firm). `#13` buyers and
  sponsors run first-pass diligence in-house (31% of PE, VC and LP respondents report AI somewhat or fully integrated
  in diligence [SPGLOBAL-PE-2026]; grade C).

## 4. Interview probes

Ask in the person's setting (Big Four deal group, mid-market TAS team, AI-native provider or in-house deal team).

1. **"In your last three QoEs, which steps did a tool touch (mapping, proof of cash, flux, add-back candidates,
   databook), and what did the reviewer change?"** Reveals where the work sits on the ladder (`#01` to `#04`) and
   whether anyone tracks override or exception rates. No public source reports them.
2. **"How long from data received to first management meeting, and where does the time go?"** Reveals the baseline
   for `#02` and whether the bottleneck is the target's data, which tools do not fix [FORVIS-QOE-2026].
3. **"Show me how a reviewer gets from an adjustment in the bridge back to the source document."** Reveals
   traceability, the control every vendor claims (`#01`, `#04`) and the one thin reports lack.
4. **"How do your engagement letters, seller NDAs and data-room terms treat AI tools? Has a seller, lender or
   insurer asked how AI was used?"** Reveals confidentiality exposure [KJK-NDA-2026] and the consent question
   [JOFA-ETHAI-2026].
5. **"Which of your diligence clients are also audit clients of your firm or an affiliate, and who checks before a
   new AI-enabled service is offered?"** Reveals whether independence is checked in a system or by memory
   (assurance-acceptance-independence-15).
6. **"When a sponsor arrives with its own first-pass analysis, or a cheaper AI-native QoE is on the table, what
   changes in scope and price? What do you do when their numbers conflict with yours?"** Reveals pressure from `#13`
   and `#05`; route the firm's own pricing to professional-services-scoping-pricing-17.
7. **"Build, buy or partner: which platform, how long was the pilot, and what would make you stop?"** Reveals
   maturity. Forvis Mazars Group piloted nine months before rollout [FORVISGROUP-OPIO-2026].
8. **"Do you do lender QoE for SBA loans? How has the October 2026 SOP changed volume and who commissions the
   report?"** Reveals exposure to `#07`; the clause was read only through vendor pages.
9. **"Who does spreading and reconciliation now, and how do juniors learn what a sound adjustment looks like?"**
   Reveals the pipeline risk Forvis Mazars US flags [FORVIS-QOE-2026] (professional-services-talent-learning-07).
10. **"After signing, does the same team or tool carry the data into integration planning and TSAs?"** Reveals
    whether a lifecycle platform (`#11`) or integration drafting (`#14`) is relevant; post-deal evidence is weakest.

## 5. Metrics and benchmarks

| Measure | Figure | Source and provenance |
|---|---|---|
| Time saved per FDD | 27%; no method | [OPIO-SITE-2026] vendor-published |
| Management-meeting prep eliminated | 80%; basis not published | [CPAPA-AUDITSIGHT-2025] vendor-published |
| Proof of cash tie-out | within 1% in 24 hours; one engagement at a 99.4% average match rate | [QOEAGENT-HOME-2026] [QOEAGENT-WHO-2026] vendor-published |
| Platform use | 4,000+ PwC Deals practitioners, 5,000+ deals; Deloitte platform in 1,000+ engagements | [PWC-TOLTIQ-2026] [DELOITTE-MAPLATFORM-2026] self-reported adoption counts |
| Diligence time saving | 21-30%, dealmakers' own estimate (400 respondents) | [INTRALINKS-AIDEAL-2026] vendor survey |
| AI incidents or near-misses, past 12 months | 80% of dealmakers; clusters: access-control lapses 48%, hallucinated outputs 40% (base not stated) | [INTRALINKS-AIDEAL-2026] vendor survey |
| AI regularly embedded in diligence | 50% (1,000 dealmakers, March 2026); 62% say human-only decisions are no longer defensible in complex deals | [DATASITE-NEWDEALTEAM-2026] vendor survey |
| Respondents with AI somewhat or fully integrated in diligence | 31% of PE, VC and LP respondents, highest of the areas listed; the report itself is quoted as "just shy of one in four GPs" [POSTTRADE-SPGLOBAL-2026] | [SPGLOBAL-PE-2026] independent |
| Pre-deal and post-deal GenAI investment | 46% and 27% of organizations (2026) | [CFODIVE-ACCENTURE-2026] vendor survey |
| M&A timeline and cost effect | 10-30% shorter; about 20% lower cost; M&A generally, not TAS-specific (McKinsey survey, February 2025) | [CFODIVE-MCKINSEY-2026] vendor survey |
| Contract-review accuracy (adjacent, legal DD) | 74% to 95% | [ARTLAW-AG-2024] self-reported |
| QoE price points | Shepi $1,000 per project self-service and $5,000 Done-For-You (list); a searcher quotes $500 to $25,000+; a broker page estimates $25,000-$200,000 (an estimate) | [SHEPI-PRICING-2026] [SEARCHFUNDER-COLUMBIA-2026] [CTACQ-QOE-2026] |

Not found: error rates, override rates, parallel-run results, inspection outcomes or any independent measure of
AI-assisted QoE accuracy or timeline. What to measure in a pilot: days from data receipt to first draft databook;
proof-of-cash variance; share of AI-proposed adjustments the reviewer changes or rejects; findings missed and later
found; senior review hours per deal; client and lender queries per report.

## 6. Guardrails

- **Confidentiality and NDAs.** Public AI tools may retain inputs, and an AI provider may not count as a permitted
  representative under an NDA. Some sellers now bar uploads to public AI or require prior written consent; parties
  are agreeing secure enterprise or closed-environment tools [KJK-NDA-2026]. The AICPA Code means asking whether
  client consent is needed before client data goes into an AI tool [JOFA-ETHAI-2026].
- **Independence (the firm's own audit clients).** For SEC issuer audit clients, investment-banking-type services
  and any contingent fee impair independence [SEC-RULE2-01-2026]. Deloitte notes that certain services may not be
  available to attest clients [DELOITTE-GENAIMA-2025]. Which diligence services are restricted was not verified;
  confirm with the assurance team (assurance-acceptance-independence-15). A firm CEO forecasts outcome-linked advisory
  fees, and notes that audit firms cannot accept contingent fees tied to financial results [BBTAX-SH-2026]
  (professional-services-scoping-pricing-19).
- **Lender rules.** SBA SOP 50 10 8.1 took effect 2026-10-01 [SBA-SOP5010-2026]. Per vendor summaries it requires an
  independent QoE with a cash proof on 7(a) acquisitions of $3 million or more, bars the seller-prepared report, and
  needs a lender-vendor review of a buyer-commissioned one [QOEAGENT-SBAUPDATE-2026]. The clause text is unverified.
- **R&W insurance.** Fasken expects insurers to scrutinise target-AI risk, with possible exclusions [FASKEN-RWI-2026].
  No source covers how underwriters treat QoE reports prepared with AI.
- **Professional standards.** The AICPA consulting standard (CS 100) applies competence, due care, planning and
  supervision, and sufficient relevant data to consulting work [JOFA-CS100-2024]. No AICPA, IESBA or PCAOB statement
  on AI in transaction advisory was found.
- **Vendor controls are self-descriptions.** Opio says on premise, no training on client data, every figure
  traceable [FORVISGROUP-OPIO-2026]; Deloitte says ring-fenced data [DELOITTE-MAPLATFORM-2026].
- **Deliverable quality.** Thin reports can look professional [FORVIS-QOE-2026]; Deloitte Australia agreed to repay the
  final instalment of a government review's fee after AI-generated errors, including nonexistent references [CITYAM-DELOITTE-2025]. Check every reference and figure
  before issue (professional-services-quality-review-04). Do not cite the withdrawn 2024 arXiv paper on GPT-4 earnings
  prediction as evidence of LLM skill with financial statements [ARXIV-KIM-2024].
- **Steps that need human judgment:** which flagged movements become adjustments; add-backs, normalization, net
  working capital and debt-like items; what matters to the deal and when to stop; management interviews; the
  conclusions a lender relies on (QoEAgent: software cannot be the provider [QOEAGENT-WHO-2026]); sign-off.

## 7. Roles and how they evolve

- **Juniors move from spreading to analysis, if firms keep them.** Opio's CEO says automation moves junior time to
  analysis, judgement and client relationships [TECHEU-OPIO-2026]. Pease Bell says many entry-level tasks can be
  handled by AI with minimal oversight and staff must challenge outputs [PEASEBELL-2026]. No source gives staffing data.
- **The pipeline warning.** Forvis Mazars US: depleting junior ranks will create future holes in executive-level
  insight, and over-reliance yields people who cannot tell thin from sound work [FORVIS-QOE-2026]. See
  professional-services-talent-learning-07 and -19.
- **AI can create work.** PwC's deals GenAI leader (Toby Popplewell): newly reviewable contracts produce anomalies that
  need about 20 hours of follow-up in his example. BDO's transaction services partner expects roles in AI oversight, data interpretation
  and client engagement [ICAEW-BIGSIX-2024].
- **Expertise is being sold to model builders.** An AI lab pays experienced TAS managers $100 an hour to evaluate
  AI-generated QoE pages [GC-ETHOS-JOB-2026].
- **Hiring signals are weak.** An EY-Parthenon diligence posting (2026-10-09) mentions AI only in the firm
  description [EY-JOB-2026].
- **Integration teams.** Bain says GenAI will pick up project management tasks and M&A teams should rethink skills
  toward value creation [BAIN-GENAIMA-2025].
- **Feeder model.** Withum's managing director of advisory services says much of its advisory work comes out of its CAS
  practice, and transaction advisory is among the services added since [ACCTODAY-CASKEYS-2026].

## 8. Frontier

- 2026-04-08: Intralinks survey ranks autonomous QoE analysis among disruptions most anticipated by 2030
  [INTRALINKS-AIDEAL-2026].
- 2026-04-27 to 29: ACG DealMAX 2026 (3,500+ attendees) included AI-and-deals content; the recap names no session
  [ACG-DEALMAX-2026].
- 2026-06-15: PwC and ToltIQ enter a strategic relationship, with PwC as ToltIQ's exclusive professional services advisor
  [PWC-TOLTIQ-2026].
- 2026-07-08: Datasite survey: 62% say human-only decision-making is no longer defensible in complex deals
  [DATASITE-NEWDEALTEAM-2026].
- 2026-07-18: An AI lab recruits TAS managers to train models on QoE exhibits and databook slides [GC-ETHOS-JOB-2026].
- 2026-08-13: Fasken says insurer scrutiny of AI in R&W is underway and that some insurers may move to standardized AI
  exclusions [FASKEN-RWI-2026].
- 2026-09-08: Forvis Mazars US says AI is also increasing lower-quality, cost-cut QoE products [FORVIS-QOE-2026].
- 2026-09-16: Opio raises EUR 4M and names Forvis Mazars Group and BDO as customers [TECHEU-OPIO-2026].
- 2026-09-22: Deloitte unveils its M&A Platform with an agentic harness [DELOITTE-MAPLATFORM-2026].
- 2026-09-25: Forvis Mazars Group rolls out Opio across multiple countries after a nine-month pilot
  [FORVISGROUP-OPIO-2026].
- 2026-10-01: SBA SOP 50 10 8.1 takes effect, creating QoE demand for larger SBA acquisitions [SBA-SOP5010-2026].
- Forecast in a 2025 report: Bain expects early adopters to draft integration workplans and TSAs in under 20% of the
  prior time [BAIN-GENAIMA-2025].

## 9. Common objections

- **"AI gets add-backs wrong."** Practitioners agree: extraction degrades on add-backs, adjustments and footnotes
  [WORKWISE-QOE-2026], and fully automated tools fall short once normalization matters
  [SEARCHFUNDER-SOURCETABLE-2025]. Response: use AI for mapping, proof of cash and candidates (`#01` to `#04`); keep
  each adjustment a human decision with a source link.
- **"It will make our reports thin."** Forvis Mazars US says exactly this [FORVIS-QOE-2026]. Response: spend the freed
  time on deeper cuts (`#10`) and keep senior review; Forvis Mazars Group pairs its rollout with mandatory human review
  [FORVISGROUP-OPIO-2026].
- **"The speed numbers are vendor hype."** Correct: 27%, 80% and 24 hours have no published method. Response: run your
  own parallel test on a closed deal and track reviewer changes before scaling.
- **"Sellers won't let us put data room files into AI."** Some won't [KJK-NDA-2026]. Response: closed or enterprise
  tools, written consent where needed, and citations back to source (`#09`).
- **"Clients will do it themselves."** Some first-pass work is moving in-house (`#13`), and among AI-using mid-market
  organizations that raise AI spend, 40% reallocate budget from external consulting services [CPAPA-RSMMM-2026]; the
  survey does not say who replaces the consulting. Response: dealmakers still say signing and judgment stay human (45%
  say the decision to sign should always remain human [DATASITE-NEWDEALTEAM-2026]); a lender-side reply says banks favour
  providers who help them get comfortable with a reconciliation [SEARCHFUNDER-COLUMBIA-2026].
- **"Cheap AI-native QoE will undercut us."** It exists (`#05`), but lenders may require independent CPA involvement
  [SHEPI-HOME-2026] and, per QoEAgent's reading of the SBA rule, software cannot be the provider [QOEAGENT-WHO-2026].
- **"Our seniors don't trust it."** Over 57% of dealmakers report rising senior resistance on accuracy and fiduciary
  grounds [INTRALINKS-AIDEAL-2026]. Response: start with steps a reviewer can check line by line (`#03`, `#09`).

## 10. Sources

Full details for keys used in the use cases are in the YAML. Keys cited above that are not in the YAML:

- ACCTODAY-CASKEYS-2026: "CAS delivers 'the keys to the kingdom'", Accounting Today, 2026-05-22, https://www.accountingtoday.com/news/cas-delivers-the-keys-to-the-kingdom
- ACG-DEALMAX-2026: "ACG Sets New Benchmark with Largest, Most Efficient DealMAX to Date", Association for Corporate Growth, 2026-04-29, https://www.acg.org/news-trends/news/acg-sets-new-benchmark-largest-most-efficient-dealmax-date
- ARXIV-KIM-2024: "Financial Statement Analysis with Large Language Models" (Kim, Muhn, Nikolaev; temporarily withdrawn 2025-02-20 after a co-author found data inconsistencies), arXiv, 2024-07-25, https://arxiv.org/abs/2407.17866
- BBTAX-SH-2026: "Traditional Accounting Firm Model May Shift to Special Offerings" (Smith + Howard CEO; forecast), Bloomberg Tax, 2026-01-08, https://news.bloombergtax.com/tax-insights-and-commentary/traditional-accounting-firm-model-may-shift-to-special-offerings
- CFODIVE-MCKINSEY-2026: "Generative AI reduces M&A costs by 20%, McKinsey says", CFO Dive, 2026-02-18, https://www.cfodive.com/news/generative-ai-reduces-merger-acquisition-costs-20percent-mckinsey/812514/
- CPAPA-RSMMM-2026: "The Middle Market Has Embraced AI. Now Comes the Hard Part" (RSM Middle Market AI Survey 2026: 1,030 AI-using leaders, fieldwork March 5-16, 2026; RSM sells consulting), CPA Practice Advisor, 2026-07-22, https://www.cpapracticeadvisor.com/2026/07/22/the-middle-market-has-embraced-ai-now-comes-the-hard-part/187171/
- EY-JOB-2026: "EYP Associate/Senior Associate - Financial Diligence (Kuala Lumpur)", EY, 2026-10-09, https://careers.ey.com/ey/job/Kuala-Lumpur-EYP-Associate-Senior-Associate-Financial-Diligence-Fede-50490/1214314201/
- FASKEN-RWI-2026: "When AI meets RWI in M&A", Fasken, 2026-08-13, https://www.fasken.com/en/knowledge/2026/08/when-ai-meets-rwi-in-ma-what-impact-will-ai-have-on-representation-and-warranty-insurance
- JOFA-CS100-2024: "Clarification proposed for CPAs' financial statement preparation engagements" (CS 100 general standards), Journal of Accountancy, 2024-09-20, https://www.journalofaccountancy.com/news/2024/sep/updates-cpa-consulting-services/
