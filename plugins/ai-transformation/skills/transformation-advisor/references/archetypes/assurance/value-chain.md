# Assurance value chain

Last researched 2026-10-17. Use this in Map to lay out stages, processes and key steps before asking for real
volumes and times, and to pick focus modules. Each step carries work types from the controlled vocabulary. Step detail,
pain points and AI use cases are in the module files; this file does not repeat them. Source keys in brackets resolve in
§8 or in [sources.md](sources.md).

## Contents

1. [How to use it](#1-how-to-use-it)
2. [Stages at a glance](#2-stages-at-a-glance)
3. [Financial-statement and ICFR audit, stage by stage](#3-financial-statement-and-icfr-audit-stage-by-stage)
4. [The data and evidence acquisition layer](#4-the-data-and-evidence-acquisition-layer)
5. [Other assurance service lines](#5-other-assurance-service-lines)
6. [In-house internal audit](#6-in-house-internal-audit)
7. [Where the work types cluster](#7-where-the-work-types-cluster)
8. [Sources](#8-sources)

## 1. How to use it

- Show the leader the stage table in §2 and ask them to confirm, merge or split stages for their practice. A SOC
  practice, a sustainability team and an internal audit function each use their own section (§5, §6).
- For each process the leader cares about, open the linked module's §2 for the step table and typical pains, then ask
  for their own numbers: engagements a year, hours per step, review notes, rework, findings.
- Stages 0 and 7 come from professional-services and work the same way here, with the assurance differences noted.
- Inspection findings show where the work is hardest. In IFIAR's 2025 survey of the six largest networks, 35% of inspected
  listed public-interest audits had at least one finding. Internal control testing produced the most findings by count;
  accounting estimates had the highest share of inspected audits with a finding [IFIAR-SURVEY-2026].

## 2. Stages at a glance

| # | Stage | Main processes | Module | Public AI evidence |
|---|---|---|---|---|
| 0 | Win and price the work | Tenders, proposals, fee setting | professional-services | Buyers cite AI in fee talks; no tool evidence |
| 1 | Accept and continue | Client risk, KYC, independence, engagement letter | [acceptance-independence](modules/acceptance-independence.md) | Thin |
| 2 | Plan | Understand the entity and its AI, risk assessment, materiality, scoping, budget | [planning-risk-assessment](modules/planning-risk-assessment.md) | Moderate |
| 3 | Acquire data and evidence | Requests, ledger extraction, confirmations, authenticity | §4 below | Moderate, vendor-heavy |
| 4a | Test controls | Walkthroughs, ITGCs, operating effectiveness, deficiencies | [controls-testing](modules/controls-testing.md) | Strong |
| 4b | Test substantively | Journal entries, vouching, analytics, contracts, estimates | [substantive-testing](modules/substantive-testing.md) | Strong |
| 4c | Use experts | Valuation, actuarial, tax, forensic; client AI as an input | [specialists](modules/specialists.md) | Thin |
| 5 | Complete and report | Disclosures, tie-out, going concern, EQR, KAMs, opinion | [completion-reporting](modules/completion-reporting.md) | Thin |
| 6 | Manage quality | Tool governance, supervision and review, monitoring, inspections | [quality-management](modules/quality-management.md) | Moderate |
| 7 | Bill, collect and learn | Invoicing, realization, knowledge capture | professional-services | None audit-specific |

## 3. Financial-statement and ICFR audit, stage by stage

### Stage 0. Win and price the work (inherited)

| Process | Key steps | Work types |
|---|---|---|
| Tender and proposal | Respond to request for proposal; meet the audit committee; describe team, approach and technology | client-interaction, document-production |
| Fee and scope | Budget hours by grade; set the fee; agree scope changes | expert-judgment, data-reporting |

Assurance differences: for listed clients the audit committee oversees the tender, and buyers who ran a competitive
review reported fee cuts of 25-30% in one 95-respondent survey [FERF-2026]. Two-thirds of 54 US firms surveyed present
their technology to clients as a value differentiator [CPACOM-ATR-2025]. See [economics.md](economics.md).

### Stage 1. Accept and continue

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Client risk and due diligence | Intake questionnaire; risk score; KYC and AML screening | client-interaction, research-synthesis, transaction-processing | [acceptance-independence](modules/acceptance-independence.md) |
| Independence clearance | Map affiliates; check services, relationships, holdings; rotation | review-assurance, data-reporting, coordination-scheduling | same |
| Decide and contract | Partner and risk approval; engagement letter, covering AI use and data consent where law, contract or firm policy requires it | expert-judgment, document-production | same |

### Stage 2. Plan

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Understand the entity | Read minutes and filings; walk through processes; find where the client uses AI | research-synthesis, review-assurance | [planning-risk-assessment](modules/planning-risk-assessment.md) |
| Assess risk | Analytics; risks of material misstatement by assertion; fraud discussion | data-reporting, expert-judgment | same |
| Set materiality and scope | Benchmarks; components and locations in scope | expert-judgment | same |
| Plan and resource | Planning memo, planned tool use, budget, staffing | document-production, coordination-scheduling | same, and [quality-management](modules/quality-management.md) |

### Stage 4. Execute

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Controls testing | Walkthrough; test of design; information produced by the entity; sample; test; ITGCs; deficiency evaluation | research-synthesis, review-assurance, data-reporting, expert-judgment | [controls-testing](modules/controls-testing.md) |
| Journal-entry and fraud testing | Validate population; score or filter; investigate selections | data-reporting, review-assurance | [substantive-testing](modules/substantive-testing.md) |
| Tests of details | Select items; vouch and tie out; confirm; inspect contracts | review-assurance, transaction-processing, research-synthesis | same |
| Analytics and estimates | Build expectations; challenge management's methods and assumptions | data-reporting, expert-judgment | same, and [specialists](modules/specialists.md) |
| Inventory | Attend counts; test counts | physical-field | [substantive-testing](modules/substantive-testing.md) |
| Experts | Decide an expert is needed; evaluate competence and objectivity; evaluate their work | expert-judgment, review-assurance | [specialists](modules/specialists.md) |
| Document and review | Workpapers, review notes, sign-off, record of tool use | document-production, review-assurance | [quality-management](modules/quality-management.md) |

### Stage 5. Complete and report

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Financial statement review | Disclosure checklist; casting and tie-out; other information | review-assurance, data-reporting | [completion-reporting](modules/completion-reporting.md) |
| Completion judgments | Subsequent events; going concern; representations; uncorrected misstatements | expert-judgment, research-synthesis | same |
| Review and release | Partner review; engagement quality review | review-assurance | same |
| Report and communicate | KAMs or CAMs; audit committee communications; opinion | document-production, client-interaction | same |

### Stage 6. Manage quality (runs across all stages)

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Firm-level tool governance | Business case; select or build; certify per use case; control access; monitor; recertify | software-systems, review-assurance, data-reporting | [quality-management](modules/quality-management.md) |
| Engagement supervision | Plan AI use; direct; review output; document; stand back | coordination-scheduling, review-assurance, document-production | same |
| Monitoring and inspection | Internal inspections; root-cause analysis; regulator dialogue | expert-judgment, client-interaction | same |

### Stage 7. Bill, collect and learn (inherited)

Billing, realization and knowledge management work as in professional-services. The assurance difference is that 87% of
54 surveyed US firms track realization and only 13% track value-billed engagements [CPACOM-ATR-2025], so hours saved are
likely to show up first as realization or idle capacity (inference). See [economics.md](economics.md).

## 4. The data and evidence acquisition layer

No module owns this layer, but it decides whether AI tools in stages 2-5 work at all.

**Why it matters.** Among 54 US firms surveyed, the top-ranked blockers were untrained staff (66%), poor client data (60%)
and no access to client information and systems (53%), and firms further along named client-data access as their
biggest obstacle more often. The most common automated solutions were workflow management, foot-and-proof and
confirmations (39% each) and trial-balance import (35%); data ingestion was 19% and substantive analytics 11%
[CPACOM-ATR-2025]. KPMG argues continuous testing "cannot be achieved
without continuous evidence collection" (a forecast) [KPMG-SOX-2026].

| Process | Key steps | Work types | Notes |
|---|---|---|---|
| Request and collect | Request list (PBC); client uploads; match each upload to the request; chase gaps | coordination-scheduling, client-interaction | Agents that pre-screen client uploads are vendor-described [SURALINK-CTEST-2026]; Optro lists automated evidence collection as upcoming [OPTRO-CRX-2026] |
| Extract and import | Pull ledger and trial balance from the client's system; map fields; reconcile to the trial balance | data-reporting, software-systems | Extraction layers claim any-system coverage (vendor) [VALIDIS-2026; INFLO-ADA-2026] |
| Validate reliability | Completeness and accuracy of the population; reliability of electronic information from the client | review-assurance | AS 1105.10A (fiscal years beginning on or after 15 Dec 2025) requires evaluating external information the company supplies electronically; a PCAOB policy statement (18 Sep 2025) says separate testing may be unnecessary where the risk of modification is remote [PCAOB-TAA-2024] |
| Confirm with third parties | Bank, receivables, payables and legal confirmations; direct access to source data | transaction-processing, review-assurance | AS 2310 allows direct access to a knowledgeable external source, with intermediary due diligence [PCAOB-AS2310-2023]; SAS 150 applies to periods ending on or after 15 Dec 2028 [JOFA-SAS150-2026] |
| Check authenticity | Spot altered or generated documents; verify out of band | review-assurance, expert-judgment | 75% of 713 anti-fraud professionals saw GenAI document fraud rise over two years; audit-specific incidence is unmeasured [ACFE-SAS-2026] |

**Three channels, three reliability levels.** (a) Client-supplied files and screenshots are weakest on authenticity;
(b) extracts from client systems depend on completeness, field mapping and IT general controls; (c) data held at the
source (banks, counterparties) is strongest, provided the intermediary's controls and independence from the client are
assessed [IAASB-ED500-2026; PCAOB-AS2310-2023]. The IAASB notes that the ability to extract information in usable form
may affect whether a procedure can be performed with technological tools, and that privacy law may bar some client data
from some tools without consent or safeguards [IAASB-ED500-2026]. BDO Netherlands moved bank data from client downloads to a bank consent flow,
aiming to test whole populations (self-reported, no outcome figures) [CIRCIT-CS-BDONL-2026].

Every time-saving figure found for this layer is vendor-published or a customer quote, for example a sole practitioner
going from about 16 hours to five or six per engagement on sample-to-evidence matching [TR-AGENTIC-2025]. Ask for a
parallel run on one engagement before using any of them in a business case.

## 5. Other assurance service lines

**SOC and attestation** ([soc-attestation](modules/soc-attestation.md); test detail in
[controls-testing](modules/controls-testing.md)).

| Process | Key steps | Work types |
|---|---|---|
| Scope and accept | Report type, criteria, system boundary, subservice organisations, independence | expert-judgment, coordination-scheduling |
| Readiness and system description | Gap assessment; management drafts Section 3 | review-assurance, document-production |
| Test and evaluate | Walkthroughs; evidence collection; operating-effectiveness tests; deviations | review-assurance, data-reporting, expert-judgment |
| Report and after | Opinion and report; bridge letters; customer use of the report | document-production, client-interaction |

**Sustainability assurance** ([sustainability-assurance](modules/sustainability-assurance.md)).

| Process | Key steps | Work types |
|---|---|---|
| Accept and scope | Criteria, preconditions, independence (including reporting software); value-chain components | expert-judgment, review-assurance |
| Understand the reporting process | Materiality or double-materiality process; information system and controls | review-assurance, research-synthesis |
| Gather evidence | Analytics, inspection, recalculation; estimates and value-chain data | review-assurance, data-reporting |
| Conclude and report | Misstatements; representations; limited or reasonable assurance conclusion | expert-judgment, document-production |

**Assurance over AI** ([assurance-over-ai](modules/assurance-over-ai.md)).

| Process | Key steps | Work types |
|---|---|---|
| Entity AI inside an audit | Inventory AI use; classify AI-enabled controls; scope ITGCs to models and agents; choose evidence | research-synthesis, review-assurance, software-systems |
| Standalone assurance | Pick assessment type and criteria; readiness; certification audit or attestation; technical testing; report | expert-judgment, review-assurance, document-production |

## 6. In-house internal audit

Internal audit uses the same modules with a different chain. Map it as follows.

| Stage | Key steps | Work types | Modules |
|---|---|---|---|
| Audit universe and risk assessment | Maintain the universe; assess risk; refresh in year | research-synthesis, expert-judgment | [planning-risk-assessment](modules/planning-risk-assessment.md) |
| Annual or rolling plan | Prioritise; resource; agree with the audit committee | coordination-scheduling, client-interaction | same |
| SOX programme | Scope key controls; test; evaluate deficiencies; support the external auditor | review-assurance, data-reporting | [controls-testing](modules/controls-testing.md) |
| Engagements | Planning memo; fieldwork; analytics; findings | review-assurance, data-reporting, expert-judgment | [controls-testing](modules/controls-testing.md), [substantive-testing](modules/substantive-testing.md) |
| Report and follow up | Draft report; agree actions; track remediation | document-production, client-interaction | [completion-reporting](modules/completion-reporting.md) |
| Assure the business's AI | Inventory; governance review; AI risks in the plan | review-assurance, expert-judgment | [assurance-over-ai](modules/assurance-over-ai.md) |
| Run the function | Budget, staffing, co-source, methodology, tool governance | coordination-scheduling | [quality-management](modules/quality-management.md) |

Context: SOX testing hours per control rose from 12 (FY2022) to 16 (FY2024) in KPMG's company survey [KPMG-SOX-2026], and
only 28% of 213 internal audit leaders were confident their teams could audit AI risks (vendor survey) [OPTRO-FOF-2026].

## 7. Where the work types cluster

Use this in Diagnose to judge AI fit by step type. It summarises the module tables; the modules give the evidence.

| Work type | Typical assurance steps | Usual AI pattern | Evidence strength |
|---|---|---|---|
| review-assurance | Tests of controls, vouching, disclosure checklists, review of workpapers | full-population-testing, reconcile-exceptions, draft-review-loop | Strong in controls and substantive testing; thin at completion |
| data-reporting | Ledger analytics, journal entries, population validation | full-population-testing, monitor-diagnose-act | Strong for journal entries (88% of IFIAR members answering frequently saw tools there, 2024 data) [IFIAR-TTF-2025] |
| research-synthesis | Reading minutes, contracts, prior files, SOC reports | document-to-decision, research-brief | Moderate; regulator worked examples exist [FRC-GENAI-2026] |
| document-production | Planning memos, walkthrough write-ups, Section 3 text, reports | draft-review-loop | Moderate; widely used, rarely measured |
| expert-judgment | Risk assessment, materiality, deficiency severity, going concern, opinion | assist only; AI as input | Regulators keep these with the auditor [FRC-GENAI-2026; NFRA-CAALLEY-2026] |
| coordination-scheduling, client-interaction | Requests, chasing, staffing, audit committee | intake-triage, service-agent-escalation | Vendor-described |
| transaction-processing | Confirmations, KYC screening | reconcile-exceptions | Vendor-published platform figures |
| physical-field | Inventory counts | other | Older, pre-GenAI evidence only |

## 8. Sources

Keys not listed here are in [sources.md](sources.md).

- **INFLO-ADA-2026**: Inflo, *Audit Data Analytics* (vendor, undated page, accessed 17 Oct 2026). https://inflo.com/audit-data-analytics/
- **SURALINK-CTEST-2026**: Suralink, *Cloud Testing Suite* (vendor, undated page, accessed 17 Oct 2026). https://www.suralink.com/technology/cloud-testing-suite-suralink
- **VALIDIS-2026**: Validis, *Validis home page* (vendor, undated page, accessed 17 Oct 2026). https://validis.com/
