# Advisory value chain

Last researched 2026-10-21. Use this in Map to lay out stages, processes and key steps before asking for real volumes
and times, and to pick focus modules. Each step carries work types from the controlled vocabulary. Step detail, pains
and AI use cases are in the module files' §2 and §3; this file does not repeat them. Source keys in brackets resolve in
[sources.md](sources.md).

## Contents

1. [How to use it](#1-how-to-use-it)
2. [Stages at a glance](#2-stages-at-a-glance)
3. [The client data layer](#3-the-client-data-layer)
4. [Where the work types cluster](#4-where-the-work-types-cluster)
5. [Stage by stage](#5-stage-by-stage)
6. [Firm and in-house variants](#6-firm-and-in-house-variants)

## 1. How to use it

- Advisory is a family of service lines, not one chain. They share a spine: screen the client, get the client's data,
  do the analysis, form a judgment, deliver something a client, lender, court or board relies on, and keep it current.
  Show the leader the stage table in §2, ask which service lines (modules) they run, then confirm, merge or split.
- The four stages run from the most recurring work to the most event-driven: recurring outsourced services (CAS,
  FP&A), then risk and controls, then deal and event work (transactions, valuation, forensic), then owner and family
  services (private client). Firms often grow along this order: Withum's advisory leader says much of its advisory
  comes out of CAS [ACCTODAY-CASKEYS-2026].
- Stages 0, 1 and 6 come from professional-services and work the same way, with the advisory differences noted.
- Three things cut across every line: who the client is (independence, stage 1), the client data layer (§3), and
  review, because almost every AI use case in this archetype keeps a person on the conclusion.
- For each process the leader cares about, open the module's §2 and ask for their own numbers: clients, controls,
  deals, reports or entities a year; hours per step; review notes; rework; days to deliver.

## 2. Stages at a glance

| # | Stage | Main processes | Modules | Public AI evidence |
|---|---|---|---|---|
| 0 | Win and price the work | Proposals, fee basis, packaging | professional-services; [economics.md](economics.md) | Pricing intent surveyed; no fee data |
| 1 | Accept and screen | Attest-client check, scope, engagement letter, AI terms and consent | [guardrails.md](guardrails.md) §3-4; professional-services acceptance-risk | Rules clear for SEC audit clients; no AI-specific ruling |
| A | Recurring outsourced services | Bookkeeping and close, reporting, AP and payroll, fractional CFO; budgets, forecasts, planning platforms | [client-accounting-services](modules/client-accounting-services.md), [fpa-performance](modules/fpa-performance.md) | Densest: one independent field study, many vendor benchmarks; FP&A thin |
| B | Risk and controls | Planning, RCM and test design, evidence, testing, review, reporting, client AI governance | [risk-controls](modules/risk-controls.md) | Named in-house agent deployments; outsourced-provider outcomes unpublished |
| C | Deal and event work | QoE and FDD, valuation and fair value, investigations, damages and testimony | [transactions](modules/transactions.md), [valuation](modules/valuation.md), [forensic-disputes](modules/forensic-disputes.md) | Usage counts and vendor speed claims; standards and evidence law moving |
| D | Owner and family services | Family-office accounting, alternatives, consolidated reporting, payment controls, succession and exit | [private-client](modules/private-client.md) | Thin and mostly from sellers to family offices |
| 6 | Bill, keep and learn | Invoicing, renewal, cross-sell, knowledge capture | professional-services | The OPR fee reading applies to tax matters [IRS-OPR-2026] |

## 3. The client data layer

Every advisory line starts by getting the client's data into a ledger, workpaper, data room or model, and much of the
AI evidence is about this layer. Discuss it before any agent is planned.

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Ledger and bank access | Connect the client's ledger, bank and card feeds; set write permissions and locked periods | software-systems, transaction-processing | [client-accounting-services](modules/client-accounting-services.md) §2 |
| Catch-up and cleanup | Opening balances, chart of accounts, migration between ledgers | transaction-processing | [client-accounting-services](modules/client-accounting-services.md) `#09` |
| Control evidence | Requests to control owners, evidence matching to samples | coordination-scheduling, review-assurance | [risk-controls](modules/risk-controls.md) `#04` |
| Deal data | Request list, data room, trial balance mapping, scanned bank statements | transaction-processing, data-reporting | [transactions](modules/transactions.md) §2 |
| Matter data | Legal hold, collection (now including enterprise AI chats), structured extraction from statements and checks | data-reporting | [forensic-disputes](modules/forensic-disputes.md) §2 |
| Planning data | Actuals and drivers into a planning model; governed data to assistants through MCP | data-reporting, software-systems | [fpa-performance](modules/fpa-performance.md) `#06` |
| Family data | Manager portals, capital calls, K-1s, multi-entity feeds, an entity map | transaction-processing, data-reporting | [private-client](modules/private-client.md) `#02` |

How hard it is, from the sources: manual data cleanup is the top advisory blocker (30%), firms run about 10 apps and 41%
say they are fully integrated [INTUIT-ACCTTECH-2026]; data quality is the top barrier for large finance functions
(36%) [KPMG-AIFINANCE-2026] and for middle-market companies (34%) [RSM-MMAI-2026]. Targets with little deal
experience struggle to pull data however fast the adviser's tools are [FORVIS-QOE-2026]. Firm-hosted data for an audit
client raises an independence question too ([guardrails.md](guardrails.md) §3).

## 4. Where the work types cluster

| Work type | Where it dominates | What AI does there today (from the modules) |
|---|---|---|
| transaction-processing | Coding, reconciliation, AP, payroll, proof of cash, alternatives intake | Confidence-gated automation with exception queues; the only grade A evidence |
| data-reporting | Packages, dashboards, flux, forecasts, consolidated family views | AI-assisted dashboards and commentary for review; forecasting rated weakly |
| review-assurance | Control testing, workpaper review, document review, report QC | Agents test defined attributes; reviewers sign off; no override rates published |
| document-production | RCMs, observations, databooks, valuation and expert reports | First drafts for review; fabricated citations are the known failure |
| research-synthesis | Risk scans, comparables, data-room review, case law | Grounded tools with citations; selection stays human |
| expert-judgment | Add-backs, deficiency severity, conclusions of value, damages, opinions | Stays with a named professional in every source |
| coordination-scheduling | Evidence requests, document chasing, close calendars, integration plans | Request agents and chasers, mostly announced |
| client-interaction | Management meetings, principals, counsel, audit committees | Preparation support; relationships stay human |
| software-systems | Planning and ERP implementation, ledger and agent set-up | Partner alliances with AI-native platforms, announced |

## 5. Stage by stage

**Stage 1. Accept and screen.** Steps: identify whether the client (or an affiliate) is an attest client and under
which regime; check the service against restrictions; agree scope and AI terms; ask whether client consent is needed
before data goes into AI. Work types: review-assurance, document-production. Modules: CAS `#24` (screening idea),
[guardrails.md](guardrails.md). The SEC restricted-service list and contingent-fee bar apply to issuer audit clients
[SEC-RULE2-01-2026]; developing or hosting AI for an attest client can raise concerns [JOFA-ETHAI-2026].

**Stage A. Recurring outsourced services.**

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Bookkeeping and reconciliation | Code transactions against client rules; match bank and cards; work exceptions | transaction-processing, review-assurance | [CAS](modules/client-accounting-services.md) `#01`, `#02` |
| Month-end close | Entries and accruals, review, sign-off, lock the period | data-reporting, review-assurance | [CAS](modules/client-accounting-services.md) `#03`-`#05` |
| Reporting | Package, variance commentary, KPI dashboards | document-production, data-reporting | [CAS](modules/client-accounting-services.md) `#06`; [FP&A](modules/fpa-performance.md) `#01` |
| AP, bill pay, payroll | Capture and code invoices, approve and release payments, prepare payroll | transaction-processing | [CAS](modules/client-accounting-services.md) `#10`, `#11` |
| Controllership and fractional CFO | Memos, 13-week cash flow, board packs, advice | expert-judgment | [CAS](modules/client-accounting-services.md) `#07`, `#08` |
| Budget and forecast | Collect inputs, route approvals, baseline forecast, scenarios | coordination-scheduling, data-reporting, expert-judgment | [FP&A](modules/fpa-performance.md) `#02`-`#04` |
| Planning and ERP platforms | Readiness, selection, implementation, agent enablement | software-systems | [FP&A](modules/fpa-performance.md) `#09`-`#12` |
| Managed FP&A | An outside team runs forecasting and reporting on a recurring basis | data-reporting, expert-judgment | [FP&A](modules/fpa-performance.md) `#13` |

**Stage B. Risk and controls.**

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Plan and assess risk | External scan, interviews, planning memo, risk scores | research-synthesis, expert-judgment | [risk-controls](modules/risk-controls.md) `#01`, `#02` |
| Design and scope | RCM, narratives, attributes, scoping AI inside business controls | document-production, expert-judgment | `#03`, `#20` |
| Test | Evidence requests, sample or full-population tests, workpapers | review-assurance, coordination-scheduling | `#04`-`#09` |
| Review and report | Pre-review, missing support versus true exception, severity, observations | review-assurance, document-production | `#10`, `#11` |
| Third parties | Read vendors' SOC reports, map gaps, vendor AI risk | review-assurance, research-synthesis | `#12` |
| Client AI governance | Inventory, ownership, control design, readiness for certification | expert-judgment | `#17`-`#21` |

Issuing the SOC report or certifying the AI system is attest work in the assurance archetype.

**Stage C. Deal and event work.**

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Diligence data and analysis | Mapping, proof of cash, flux, management-meeting prep | transaction-processing, data-reporting | [transactions](modules/transactions.md) `#01`-`#03` |
| Adjustments and deliverables | Add-backs, working capital, databook, red-flag report | expert-judgment, document-production | `#04`, `#12` |
| Data-room review | Contracts and documents with citations | research-synthesis, review-assurance | `#09` |
| Valuation research and modelling | Comparables, discount rates, DCF, sensitivities | research-synthesis, expert-judgment | [valuation](modules/valuation.md) `#01`-`#07` |
| Valuation report and review | Drafting, standards and policy review, defence | document-production, review-assurance | `#08`-`#11` |
| Investigation | Preserve and collect, prepare data, trace funds, review documents | data-reporting, research-synthesis | [forensic-disputes](modules/forensic-disputes.md) `#01`-`#05` |
| Expert work | Damages, report, testimony, disclosure of AI use | expert-judgment, document-production | `#06`, `#07`, `#09` |

**Stage D. Owner and family services.**

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Family-office accounting | Multi-entity close, intercompany, bill pay | transaction-processing | [private-client](modules/private-client.md) `#01`, `#04` |
| Alternatives administration | Collect capital calls, distributions, valuations, K-1s; extract and review | transaction-processing, data-reporting | `#02` |
| Reporting to principals | Consolidated view, commentary, meeting material | data-reporting, client-interaction | `#03`, `#08`-`#10` |
| Controls and policy | Payment approvals and call-backs; the family's AI policy | review-assurance, expert-judgment | `#07`, `#14` |
| Succession and exit | Successor and exit-readiness conversations | expert-judgment, client-interaction | `#12`, `#13`, `#17` |

## 6. Firm and in-house variants

- **Firm versus in-house.** In-house teams run the same steps for one group: controllers run the close, CAEs the
  testing, corporate development the diligence, family-office staff the reporting. Their agent use sets what they buy
  from firms (risk-controls `#05`, `#14`; transactions `#13`).
- **Small firm versus platform.** Small and solo CAS firms show most of the named results in vendor case studies; larger
  firms show platform announcements and usage counts (CAS module §5; transactions module §5).
- **APS firms.** Where an advisory entity sits beside a separate licensed attest firm, stage 1 carries extra weight:
  Crowe notes some services may not be available to attest clients [CROWE-KKR-2026].
- **What is outside the chain.** Attest opinions (assurance), returns and tax advice (tax), and regulated investment
  advice. Pricing, staffing and ownership of the firm itself sit in professional-services.
