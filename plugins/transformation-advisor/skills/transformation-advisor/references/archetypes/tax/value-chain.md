# Tax value chain

Last researched 2026-10-17. Use this in Map to lay out stages, processes and key steps before asking for real volumes
and times, and to pick focus modules. Each step carries work types from the controlled vocabulary. Step detail, pain
points and AI use cases are in the module files' §2 and §3; this file does not repeat them. Source keys in brackets
resolve in §7 or in [sources.md](sources.md).

## Contents

1. [How to use it](#1-how-to-use-it)
2. [Stages at a glance](#2-stages-at-a-glance)
3. [The tax data layer](#3-the-tax-data-layer)
4. [Where the work types cluster](#4-where-the-work-types-cluster)
5. [Stage by stage](#5-stage-by-stage)
6. [Firm and in-house variants](#6-firm-and-in-house-variants)
7. [Sources](#7-sources)

## 1. How to use it

- Tax is not one chain but several service lines that share the same spine: get the data, determine the tax, take
  and support positions, file or report, sign, and defend later. Show the leader the stage table in §2 and ask which
  service lines (modules) they run, then confirm, merge or split stages for each.
- For each process the leader cares about, open the linked module's §2 for the step table and typical pains, then ask
  for their own numbers: returns, entities, jurisdictions or notices a year, hours per step, review notes, rework,
  amended returns, penalties.
- Stages 0 and 9 come from professional-services and work the same way, with the tax differences noted.
- Three things cut across every line: the data layer (§3), the filing calendar (work bunches at deadlines, so any
  change has to land outside the peak), and professional duties ([guardrails.md](guardrails.md)), which attach at
  consent, research, signature and billing.

## 2. Stages at a glance

| # | Stage | Main processes | Modules | Public AI evidence |
|---|---|---|---|---|
| 0 | Win and price the work (firms) / budget the department (in house) | Proposals, fee basis, adviser spend | professional-services; [economics.md](economics.md) | Leaders' statements on pricing; no tool evidence |
| 1 | Engage and accept | Engagement letter, section 7216 consent, AI disclosure, scope | [compliance-individual-business](modules/compliance-individual-business.md); [guardrails.md](guardrails.md) | No AI-specific consent practice published |
| 2 | Collect data and documents | Organizers and requests, source documents, ERP and ledger extracts, TP and Pillar Two data | §3; [data-technology](modules/data-technology.md) | Vendor-heavy; extraction is the busiest product area |
| 3 | Determine and calculate | Return preparation, book-to-tax, provision, GloBE, indirect determination, TP calculations | compliance modules, [provision-pillar-two](modules/provision-pillar-two.md), [indirect-tax](modules/indirect-tax.md), [transfer-pricing](modules/transfer-pricing.md) | Agentic preparation shipped; rules engines still calculate |
| 4 | Research and take positions | Research, memos, written advice, planning, diligence | [research-advisory](modules/research-advisory.md) | Broad use; speed figures are practitioner estimates |
| 5 | Document and report | Workpapers, footnotes, local and master files, GIR XML, e-invoices, returns | all service-line modules | Drafting tools widely used, rarely measured |
| 6 | Review, sign and file | Preparer, manager and partner review; signature; e-file and submission | compliance modules; [guardrails.md](guardrails.md) | Review is the new bottleneck; no error rates published |
| 7 | Respond and defend | Notices, exams, IDRs, Appeals, litigation, audit defence, APAs | [controversy](modules/controversy.md), [transfer-pricing](modules/transfer-pricing.md) | Practitioner side thin; authority side measured |
| 8 | Monitor and govern | Rule changes, calendar, automation sustainment, AI policy and vendor review | [data-technology](modules/data-technology.md), [compliance-corporate](modules/compliance-corporate.md) | Vendor monitoring tools; governance mostly policy |
| 9 | Bill, collect and learn | Invoicing, realization, knowledge capture | professional-services | Fee rule now ties AI to billing [IRS-OPR-2026] |

## 3. The tax data layer

Every service line starts by getting data into a tax engine or workpaper, and most tax AI evidence is about this
layer. It deserves its own discussion before any agent is planned.

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Source documents (individuals and pass-throughs) | Classify W-2s, 1099s, K-1s and brokerage statements; extract; map K-1 footnotes | transaction-processing, review-assurance | [compliance-individual-business](modules/compliance-individual-business.md) |
| Ledger to tax (corporate and provision) | Extract trial balances from many entities; map to the tax chart of accounts; load engines | data-reporting, transaction-processing | [compliance-corporate](modules/compliance-corporate.md), [data-technology](modules/data-technology.md) |
| Transaction data (indirect tax) | Feed ERP, billing and checkout data to the engine; maintain product and customer master data | data-reporting, software-systems | [indirect-tax](modules/indirect-tax.md) |
| Group data (TP and Pillar Two) | Collect entity financials and jurisdictional data from several ERPs | data-reporting | [transfer-pricing](modules/transfer-pricing.md), [provision-pillar-two](modules/provision-pillar-two.md) |
| Real-time reporting interfaces | Validate and submit e-invoices; handle rejections | transaction-processing, software-systems | [data-technology](modules/data-technology.md), [indirect-tax](modules/indirect-tax.md) |
| Agent access | Let assistants and agents call tax platforms through MCP | software-systems | [data-technology](modules/data-technology.md) |

How hard it is, from the sources: 51% of tax and finance functions say they are early in data-management maturity
[EY-TFO-2025]; in KPMG's indirect tax benchmark, data quality is the top concern for 58%, 61% fix it by hand and 23%
say their ERP is fit for purpose [KPMG-INDIRECT-2026]; 79% of TP leaders in a vendor survey spend more than a tenth of
TP time on data [AIBIDIA-LEADERS-2026]; the first GloBE return asks for more than 100 data points [TR-CORPAI-2026]. For
many groups the hard part of the first GIR season was the XML, not the tax law [FGS-GIR-2026].

## 4. Where the work types cluster

Use this in Diagnose to judge AI fit by step type. It summarises the module tables; the modules give the evidence.

| Work type | Typical tax steps | Usual AI pattern | Evidence strength |
|---|---|---|---|
| transaction-processing | Document extraction, data entry, product mapping, return preparation, e-invoice handling | bulk-transformation, end-to-end-case-agent, document-to-decision | Many launches; figures vendor-published (one co-developer's pilot with an accuracy definition: compliance-individual-business `#05`) |
| data-reporting | Ledger mapping, provision inputs, rate reconciliation, GIR data, TP data | bulk-transformation, reconcile-exceptions | Mostly rules-based software; AI claims thin |
| research-synthesis | Research, regulatory monitoring, functional analysis, notice reading | grounded-knowledge-assistant, research-brief, monitor-diagnose-act | Broad use [AICPA-TAXSW-2026]; independent tests of models are unflattering [VALS-TAXAGENT-2026; COLUMN-TAXCALCBENCH-2025] |
| document-production | Memos, client letters, local files, intercompany agreements, footnotes, notice responses | draft-review-loop | Widely used, rarely measured |
| review-assurance | Return review, citation checks, certificate validation, reconciliations | full-population-testing, reconcile-exceptions | Ideas and vendor products; no published override or error rates |
| expert-judgment | Positions, valuation allowances, uncertain positions, TP policy, signing | assist only; AI as input | Regulators keep these with the practitioner [IRS-OPR-2026; IRS-LBI-TP-2026] |
| client-interaction | Organizers, due-diligence interviews, client questions, advice calls | intake-triage, service-agent-escalation | Vendor-described; Form 8867 interview stays personal |
| coordination-scheduling | Calendar, extensions, information requests, review queues | monitor-diagnose-act | Thin |
| software-systems | Engines, pipelines, automations, MCP access | other | Job postings and vendor documentation; no customer outcome |

## 5. Stage by stage

### Stage 0. Win and price the work (inherited)

| Process | Key steps | Work types |
|---|---|---|
| Proposal and fee basis | Scope; choose per-return, fixed, hourly or value fee | client-interaction, expert-judgment |
| In-house budget | Technology and adviser spend; make, buy or co-source | expert-judgment, data-reporting |

Tax differences: tax-return preparation is the most profitable service for 75% of 639 firm respondents in one vendor
survey [TR-SOTP-2025]; Circular 230 bars contingent fees for most IRS matters [ECFR-10.27]. See [economics.md](economics.md).

### Stage 1. Engage and accept

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Engagement and consent | Engagement letter; section 7216 consent for use or disclosure of return data; disclosure abroad | document-production, client-interaction | [compliance-individual-business](modules/compliance-individual-business.md) |
| AI disclosure and opt-out | Decide what to tell clients about AI use and how to credit savings | expert-judgment, document-production | [guardrails.md](guardrails.md) |

### Stage 2. Collect data and documents

See §3. Add the client-facing steps: send organizers, chase missing items, check what arrived (client-interaction,
coordination-scheduling) in [compliance-individual-business](modules/compliance-individual-business.md); and TP
functional interviews (research-synthesis) in [transfer-pricing](modules/transfer-pricing.md).

### Stage 3. Determine and calculate

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Individual and pass-through returns | Federal and state logic, basis, depreciation, allocations, trial balance to 1065 or 1120-S | transaction-processing, expert-judgment | [compliance-individual-business](modules/compliance-individual-business.md) |
| Corporate returns and credits | Book-to-tax, 1120, 5471 and 8858, apportionment, R&D credit and Section G | transaction-processing, data-reporting, expert-judgment | [compliance-corporate](modules/compliance-corporate.md) |
| Provision | Current and deferred tax, valuation allowance, uncertain positions, rate reconciliation | transaction-processing, expert-judgment | [provision-pillar-two](modules/provision-pillar-two.md) |
| Pillar Two | Jurisdictional ETRs, safe harbours, top-up tax, QDMTT | transaction-processing | same |
| Indirect determination | Taxability, rate and place of supply per transaction; product codes; certificates; nexus | transaction-processing, review-assurance | [indirect-tax](modules/indirect-tax.md) |
| TP calculations | Benchmarking, operational TP monitoring and true-ups | research-synthesis, data-reporting | [transfer-pricing](modules/transfer-pricing.md) |

### Stage 4. Research and take positions

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Research | Frame the question; locate and read authority; conclude | research-synthesis, expert-judgment | [research-advisory](modules/research-advisory.md) |
| Advice and planning | Memos, written advice, opinions, planning alternatives, M&A diligence | document-production, expert-judgment | same |
| In-house questions | Answer finance, legal and auditors' questions | research-synthesis, client-interaction | same |

### Stage 5. Document and report

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Workpapers and footnotes | Roll forward; draft; ASU 2023-09 disclosures | document-production, data-reporting | compliance modules, [provision-pillar-two](modules/provision-pillar-two.md) |
| TP documentation | Local file, master file, CbCR; intercompany agreements | document-production | [transfer-pricing](modules/transfer-pricing.md) |
| Filings | Returns, GIR XML, VAT and sales tax returns, e-invoices | data-reporting, software-systems | all service-line modules |

### Stage 6. Review, sign and file

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Review | Preparer, manager, partner or national-office review; citation checks | review-assurance | all service-line modules |
| Sign and authorise | Signing preparer; Form 8879; Form 8867 due diligence | expert-judgment, client-interaction | [compliance-individual-business](modules/compliance-individual-business.md) |
| File and correct | E-file, portals, corrections and amendments | coordination-scheduling, data-reporting | compliance modules, [provision-pillar-two](modules/provision-pillar-two.md) |

### Stage 7. Respond and defend

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Notices | Intake, triage, response drafting, deadlines | transaction-processing, document-production | [controversy](modules/controversy.md) |
| Exams and IDRs | Information requests, interviews, proposed adjustments | coordination-scheduling, document-production | same |
| Appeals and litigation | Protests, settlement, briefs, expert reports | expert-judgment, research-synthesis | same; [transfer-pricing](modules/transfer-pricing.md) for TP audits, APAs and MAPs |

### Stage 8. Monitor and govern (runs across all stages)

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Rule and calendar monitoring | Track law, rate and mandate changes; due dates across entities | research-synthesis, coordination-scheduling | [compliance-corporate](modules/compliance-corporate.md), [indirect-tax](modules/indirect-tax.md) |
| Automation sustainment | Inventory, document, version, approve and hand over automations | software-systems, review-assurance | [data-technology](modules/data-technology.md) |
| AI governance | Policy, approved tools, vendor review, training, record of use | review-assurance, coordination-scheduling | [guardrails.md](guardrails.md); [data-technology](modules/data-technology.md) |

### Stage 9. Bill, collect and learn (inherited)

Tax difference: OPR says billing manual time not actually spent may breach the Circular 230 fee rule, and the AICPA
disputes this reading [IRS-OPR-2026; JOFA-FEES-2026]. Pricing policy for AI-assisted work is therefore a governance
document as well as a commercial one ([economics.md](economics.md) §7).

## 6. Firm and in-house variants

- **Small and mid-size firms** run mostly stages 1-3 and 6 for individuals and pass-throughs, with a deadline peak and
  often offshore preparation (68% of IPA 100 firms offshore tax returns) [IPA-OFFSHORE-2026]. Start Map at stage 2.
- **Large firms** run every line for corporate clients and add managed services; their platforms span stages 2-8.
- **In-house departments** run stages 2-8 for one group with an average home-country team of 9 tax professionals
  (36 at companies above US$6bn revenue) in one vendor survey [TR-SOTCD-2024], buy outside help for peaks and
  specialisms, and depend on finance and IT for stage 2. Over half of their time is reactive [TR-CORPTAX-2025]. Start
  Map at §3 and stage 8.
- **Tax authorities** sit opposite stages 6-7 and increasingly see data before the taxpayer files (see
  [controversy](modules/controversy.md)).

## 7. Sources

Keys not listed here are in [sources.md](sources.md).

(All keys cited here are in sources.md.)
