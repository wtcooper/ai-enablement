# Security value chain

Last researched 2026-10-17. Use this in Map to lay out functions, processes and key steps before asking for real
volumes and times, and to pick focus modules. The stages are the six NIST CSF 2.0 functions [NIST-CSF-2024]. Each step
carries work types from the controlled vocabulary. Step detail, pain points and AI use cases are in the module files'
§2 and §3; this file does not repeat them. Source keys in brackets resolve in §8 or in [sources.md](sources.md).

## Contents

1. [How to use it](#1-how-to-use-it)
2. [Functions at a glance](#2-functions-at-a-glance)
3. [Modules mapped onto NIST CSF 2.0](#3-modules-mapped-onto-nist-csf-20)
4. [Function by function](#4-function-by-function)
5. [The telemetry and data layer](#5-the-telemetry-and-data-layer)
6. [Where the work types cluster](#6-where-the-work-types-cluster)
7. [Variants: providers, small teams, OT](#7-variants-providers-small-teams-ot)
8. [Sources](#8-sources)

## 1. How to use it

- Security leaders often already speak NIST CSF, ISO 27001 or CISSP domains. Show the function table in §2, ask which
  functions their team owns, buys as a service or leaves to IT, then open the linked modules.
- CSF is a map of outcomes, not an org chart. One team (often the SOC) spans Detect and Respond; GRC spans Govern and
  part of Identify. Use §3 to translate the leader's team names into modules.
- For each process the leader cares about, open the module's §2 step table, then ask for their own numbers: alerts a
  day, share investigated, hours per case, findings open, questionnaires a month, access reviews a quarter.
- Two things cut across every function: the telemetry and data layer (§5), and securing the AI the team itself uses
  (ai-security). A third applies to providers: the service wrapper of scoping, pricing and client reporting (§7).

## 2. Functions at a glance

| CSF function | What it is for | Main processes | Modules | Public AI evidence |
|---|---|---|---|---|
| Govern | Strategy, risk appetite, roles, policy, oversight, supply-chain risk | Risk register and quantification, policy, control frameworks, customer and vendor reviews, board and regulator reporting, AI governance, workforce | [governance-risk](modules/governance-risk.md); [ai-security](modules/ai-security.md) (AI governance) | Vendor customer stories for questionnaires and evidence; no auditor-side evidence |
| Identify | Know assets, data, exposures and risks | Asset and attack-surface inventory, data discovery, vulnerability discovery and prioritisation, threat intelligence requirements, AI inventory | [vulnerability-exposure](modules/vulnerability-exposure.md), [data-privacy](modules/data-privacy.md), [cloud-infrastructure](modules/cloud-infrastructure.md), [threat-intelligence](modules/threat-intelligence.md) | Strongest for vulnerability discovery (named open-source programmes); disclosure volume doubled in 2026 [GTIG-VULNTRENDS-2026] |
| Protect | Safeguards: identity, data, platforms, software, people | IAM and privileged access, DLP and encryption, posture and IaC, secure development, awareness, agent identity and containment | [identity-access](modules/identity-access.md), [data-privacy](modules/data-privacy.md), [cloud-infrastructure](modules/cloud-infrastructure.md), [application-security](modules/application-security.md), [human-risk](modules/human-risk.md), [ai-security](modules/ai-security.md) | AI code review and pre-merge scanning at very large firms; IAM and DLP evidence thin |
| Detect | Find attacks and anomalies | Detection engineering, alert triage, investigation, hunting, monitoring agents | [operations](modules/operations.md), [threat-intelligence](modules/threat-intelligence.md) | Most measured area; 79% of SOCs use AI, 36% in a defined workflow [SANS-SOC-2026] |
| Respond | Act on a detected incident | Declare, investigate and scope, contain, notify, communicate | [incident-response](modules/incident-response.md), [operations](modules/operations.md) (response actions) | Forensic summaries and timelines; Mandiant (a vendor) advises keeping containment deterministic [MANDIANT-AVM-2026] |
| Recover | Restore and learn | Recovery planning, restore and validation, post-incident review | [incident-response](modules/incident-response.md) | Thin: vendor scenarios, one job posting and one product release; no AI in a real recovery test or exercise found |

## 3. Modules mapped onto NIST CSF 2.0

P = primary home, S = secondary. A module may sit in several functions; the value chain is the leader's view, not ours.

| Module | Govern | Identify | Protect | Detect | Respond | Recover |
|---|---|---|---|---|---|---|
| governance-risk | P | S | | | S (notification decisions) | |
| threat-intelligence | | P | | S (hunting) | S | |
| vulnerability-exposure | | P | S (remediation) | | | |
| cloud-infrastructure | | S | P | S (runtime) | S | |
| identity-access | | | P | S (ITDR) | S (revocation) | |
| data-privacy | S (privacy) | P (discovery) | P | | | |
| application-security | | | P | | | |
| human-risk | | | P | S (reported email, insider risk) | | |
| operations | | | | P | P (response actions) | |
| incident-response | S (plans) | | | | P | P |
| ai-security | P (AI governance) | P (AI inventory) | P (agent controls) | S (agent monitoring) | S (agent incidents) | |

## 4. Function by function

Key steps are summaries; the module's §2 has the full step table with pains and sources.

**Govern**

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Risk management | Intake, assess, quantify in money, treat, report | expert-judgment, data-reporting | [governance-risk](modules/governance-risk.md) |
| Policy and control frameworks | Draft policy, map controls across frameworks, collect and check evidence, support audits | document-production, review-assurance | [governance-risk](modules/governance-risk.md) |
| Customer and supplier assurance | Answer questionnaires, run the trust centre, assess and monitor vendors | client-interaction, review-assurance | [governance-risk](modules/governance-risk.md) |
| Oversight and reporting | Board packs, regulator reporting, materiality support | document-production, expert-judgment | [governance-risk](modules/governance-risk.md); [guardrails.md](guardrails.md) |
| AI governance | Inventory AI, tier by autonomy, approve, assure third-party AI | review-assurance, expert-judgment | [ai-security](modules/ai-security.md), [governance-risk](modules/governance-risk.md) |
| Workforce and operating model | Roles, hiring, training, career paths, sourcing | coordination-scheduling | [governance-risk](modules/governance-risk.md); [workforce.md](workforce.md) |

**Identify**

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Asset and exposure inventory | Discover assets, accounts and internet-facing apps; assign owners | data-reporting | [vulnerability-exposure](modules/vulnerability-exposure.md), [cloud-infrastructure](modules/cloud-infrastructure.md) |
| Vulnerability discovery and triage | Scan, audit, fuzz, test; reproduce, deduplicate, rate | review-assurance, software-systems, expert-judgment | [vulnerability-exposure](modules/vulnerability-exposure.md) |
| Prioritisation | Rank by exploitation, exposure, asset value | data-reporting, expert-judgment | [vulnerability-exposure](modules/vulnerability-exposure.md) |
| Data discovery and classification | Scan stores, label, settle edge cases | data-reporting, transaction-processing | [data-privacy](modules/data-privacy.md) |
| Threat intelligence | Requirements, collection, enrichment, analysis, reporting, sharing | research-synthesis, expert-judgment, document-production | [threat-intelligence](modules/threat-intelligence.md) |

**Protect**

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Identity lifecycle and access | Joiner-mover-leaver, requests, approvals, reviews, privileged access, authentication | transaction-processing, review-assurance | [identity-access](modules/identity-access.md) |
| Data protection | DLP policy and alert triage, access governance, keys and certificates, privacy reviews | software-systems, review-assurance | [data-privacy](modules/data-privacy.md) |
| Platform and cloud hardening | Posture fixes, IaC guardrails, network and endpoint policy | software-systems | [cloud-infrastructure](modules/cloud-infrastructure.md) |
| Secure development | Threat model, code review, pipeline scanning, fixing, supply-chain intake | review-assurance, software-systems | [application-security](modules/application-security.md) |
| Remediation | Write, test and deploy fixes; verify | software-systems, coordination-scheduling | [vulnerability-exposure](modules/vulnerability-exposure.md), [application-security](modules/application-security.md) |
| People | Awareness content, simulation, training follow-up, hiring verification | document-production, review-assurance | [human-risk](modules/human-risk.md) |
| Securing AI | Threat-model, red-team, issue agent identities, contain, vet AI supply chain | expert-judgment, software-systems, review-assurance | [ai-security](modules/ai-security.md) |

**Detect**

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Detection engineering | Write, test, tune and retire rules | software-systems, expert-judgment | [operations](modules/operations.md), [cloud-infrastructure](modules/cloud-infrastructure.md) |
| Triage and investigation | Enrich, close or escalate; pivot across logs; verdict | transaction-processing, research-synthesis, expert-judgment | [operations](modules/operations.md) |
| Hunting | Hypothesis, query, analysis, convert to a detection | research-synthesis, expert-judgment | [threat-intelligence](modules/threat-intelligence.md) |
| Specialist signals | Reported phishing, insider risk, identity threats, DLP alerts | transaction-processing, review-assurance | [human-risk](modules/human-risk.md), [identity-access](modules/identity-access.md), [data-privacy](modules/data-privacy.md) |
| Monitoring agents | Log agent actions, attribute them, alert on out-of-scope behaviour | review-assurance, data-reporting | [ai-security](modules/ai-security.md) |

**Respond and Recover**

| Process | Key steps | Work types | Module |
|---|---|---|---|
| Preparation | Plans, playbooks, exercises, retainers | document-production, coordination-scheduling | [incident-response](modules/incident-response.md) |
| Investigation and scoping | Collect evidence, build timelines, find root cause | research-synthesis, data-reporting | [incident-response](modules/incident-response.md) |
| Containment | Isolate, revoke, block; approve each action | transaction-processing, expert-judgment | [incident-response](modules/incident-response.md), [operations](modules/operations.md) |
| Notification | Decide reportability, draft notices to regulators and customers | expert-judgment, document-production | [incident-response](modules/incident-response.md); [guardrails.md](guardrails.md) §2 |
| Recovery and learning | Restore in order, validate, post-incident review | coordination-scheduling, review-assurance | [incident-response](modules/incident-response.md) |
| AI-agent incidents | Detect, halt, investigate and report incidents where an agent acted | expert-judgment, coordination-scheduling | [incident-response](modules/incident-response.md), [ai-security](modules/ai-security.md) |

## 5. The telemetry and data layer

Detection, triage, hunting and response AI all run on logs, asset data and case history. The sources agree that data,
not model choice, limits results, so discuss this layer before any agent is planned.

- SANS 2026: SOCs that plan their data strategy before buying tools report the highest satisfaction [SANS-SOC-2026].
- CrowdStrike names fragmented data first among three reasons agentic SOC efforts fail (vendor view) [CROWDSTRIKE-AGSOC-2026];
  Latio, as summarised by a vendor, warns against buying an AI SOC to fix underlying data problems [EXAFORCE-LATIO-2026].
- Closed cases need a reason and notes before AI can learn from precedent (operations `#01`, `#02`).
- Pricing follows data: Microsoft's SIEM licence benefit includes Defender data, with other data at USD 2.40 per GB from
  2026-10-01, per a competitor's reading [PROPHET-ISOC-2026].
- Ask: which log sources have no detections; how long logs are kept; whether asset and identity data name an owner;
  whether the data the AI reads may leave the tenant.

## 6. Where the work types cluster

Use this in Diagnose to judge AI fit by step type. It summarises the module tables; the modules give the evidence.

| Work type | Typical security steps | Usual AI pattern | Evidence strength |
|---|---|---|---|
| transaction-processing | Tier-1 triage, reported email, access requests, DLP alerts, phishing takedowns | intake-triage, monitor-diagnose-act | Many vendor figures; one replay benchmark found standard designs missed 40.4% or more of attack alerts [ARXIV-2610.10608] |
| research-synthesis | Investigation, hunting, intelligence analysis, forensics | end-to-end-case-agent, research-brief | Self-reported in-house results (operations `#09`); lab benchmarks |
| review-assurance | Code review, vulnerability validation, evidence checks, access reviews, closure sampling | full-population-testing, reconcile-exceptions | Strong for code at very large firms; thin for access reviews |
| software-systems | Detection rules, fixes, IaC, agent identity and containment | draft-review-loop, bulk-transformation | Rule and fix drafting measured by deployers; patch benchmarks disputed [TOB-1PASSWORD-2026] |
| document-production | Policy, questionnaires, incident reports, board packs, awareness content | draft-review-loop, grounded-knowledge-assistant | Vendor customer stories |
| data-reporting | Inventories, prioritisation, metrics, risk quantification | monitor-diagnose-act | Thin; few measured AI results |
| expert-judgment | Materiality, containment approvals, risk acceptance, attribution | assist only; AI as input | Legal clocks start from human determinations ([guardrails.md](guardrails.md) §6) |
| client-interaction | Customer reviews, MDR client updates, help-desk verification | service-agent-escalation | Vendor-described |
| coordination-scheduling | Routing findings to owners, exercises, recovery order | monitor-diagnose-act | Thin |

## 7. Variants: providers, small teams, OT

- **Providers (MDR, MSSP, testing and IR firms).** The same chain sits inside a service wrapper: scoping, per-unit
  pricing, onboarding a client's telemetry, client reporting and renewal ([economics.md](economics.md) §4). Gartner (as
  quoted) tells buyers to demand clarity on which parts are AI-augmented and which analyst-delivered [EXPEL-GARTNERMDR-2026].
  Professional-services, not yet written, would cover the generic wrapper.
- **Small teams.** SOC coverage can be bought per unit: managed EDR with a 24/7 SOC lists at USD 8.99 per endpoint a
  month (MSRP at 100 units) [HUNTRESS-PRICING-2026].
  Public case evidence comes almost entirely from large enterprises and large providers, so check fit.
- **OT and critical infrastructure.** No module. Evidence is mostly vendor programmes and regulator warnings; Accenture
  agreed on 2026-06-18 to take a majority stake in Dragos, closed 2026-09-16 [ACCENTURE-DRAGOS-2026]. Use the method and the closest modules (vulnerability-exposure, incident-response).
- **In-house versus outsourced split.** ISC2 respondents offset skills shortages by outsourcing (20%), third-party
  providers (19%) and AI and automation (25%) [ISC2-WORKFORCE-2025]. Map who does each step before planning.

## 8. Sources

Keys not listed here are in [sources.md](sources.md).

- **MANDIANT-AVM-2026**: Mandiant (Google Cloud), *A Blueprint for AI-Assisted Vulnerability Management* (vendor, 2026-07-16). https://cloud.google.com/blog/topics/threat-intelligence/ai-assisted-vulnerability-management
