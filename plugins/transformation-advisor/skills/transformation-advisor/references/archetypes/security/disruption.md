# Security disruption scenarios

Last researched 2026-10-17. Use this at provider or function scope, in Frame (exposure) and in Reimagine lens 4
(reinvent the work). The scenarios are assembled from cited signals; no source forecasts them in this form. Each says
what would change, the evidence for and against, and what to watch. Source keys in brackets resolve in §10 or in
[sources.md](sources.md).

## Contents

1. [How to use the scenarios](#1-how-to-use-the-scenarios)
2. [A. MDR becomes AI-run and human-accountable](#2-a-mdr-becomes-ai-run-and-human-accountable)
3. [B. Work moves in-house to AI SOC software](#3-b-work-moves-in-house-to-ai-soc-software)
4. [C. Testing shifts from finding to fixing and assuring](#4-c-testing-shifts-from-finding-to-fixing-and-assuring)
5. [D. Securing AI becomes a line of business](#5-d-securing-ai-becomes-a-line-of-business)
6. [E. Platform bundling compresses point products](#6-e-platform-bundling-compresses-point-products)
7. [F. The in-house function becomes the AI risk owner](#7-f-the-in-house-function-becomes-the-ai-risk-owner)
8. [Pricing shifts and exposure by service](#8-pricing-shifts-and-exposure-by-service)
9. [Using this in a conversation](#9-using-this-in-a-conversation)
10. [Sources](#10-sources)

## 1. How to use the scenarios

- The scenarios are not exclusive; most providers face A, B and E at once.
- **Evidence status** uses three labels: *visible* (named organizations doing it, vendor-reported), *early* (launches,
  funding, announcements), *speculative* (forecasts or one author's framework).
- Ask the leader which scenario would hurt most, which they could lead, and what signal would tell them it is arriving.
- AI-native competitors here are mostly AI SOC startups and AI-first MDR; no source shows an AI-native security
  provider with a published cost or quality advantage measured by a third party.

## 2. A. MDR becomes AI-run and human-accountable

**What changes:** agents handle most first-pass investigation; the provider sells context, accountability and validated
outcomes, with humans on escalation and consequential actions.
- **For:** Arctic Wolf says agents close "more than 60%" of case volume and humans verify about one-third of complex
  cases [ARCTICWOLF-AURORA-2026]; eSentire pitches human accountability for "boards, regulators, and cyber insurers"
  [ESENTIRE-2026]; Gartner's MDR guide (as quoted) adds "AI-augmented, human-led" and forecasts 90% of initial findings
  AI-processed with no human action by 2029, from 30% [EXPEL-GARTNERMDR-2026].
- **Against:** a competitor lists buyer complaints about MDR (limited custom detections, lack of context, cost
  trajectory) and pushes software instead [PROPHET-MDR-2026].
- **Status:** visible (vendor-reported). **Watch:** whether providers publish closure accuracy and human-validation
  rates; renewal prices; warranties.

## 3. B. Work moves in-house to AI SOC software

**What changes:** buyers replace part of a managed contract with AI SOC software run by a few in-house engineers; the
managed layer thins to after-hours or specialist response.
- **For:** Gartner (via a vendor) expects more organizations to consider insourcing MDR and says AI SOC agents increase
  "internal competition for traditional MDR services" [INTEZER-GARTNERMDR-2026]; Exaforce cites customer teams
  "replacing legacy MDRs" [EXAFORCE-SERIESB-2026].
- **Against:** AI SOC tools cannot fix incomplete data (Latio, via a vendor) [EXAFORCE-LATIO-2026]; a replay benchmark
  shows high miss rates for standard designs [ARXIV-2610.10608]; 46% of home-built AI SOC tools were abandoned or replaced, per a vendor's survey (operations §9).
- **Status:** early. **Watch:** insourcing at renewals; AI SOC pricing per investigation [DROPZONE-PRICING-2026]; who
  in the buyer's team would own the agents.

## 4. C. Testing shifts from finding to fixing and assuring

**What changes:** bug-finding becomes cheap and automated; testing and consultancy firms move to validating
exploitability, writing and verifying fixes, and assuring AI-found results.
- **For:** Patch the Planet sends patches rather than bug reports because maintainers face a flood of findings
  [TOB-PTP-2026]; AWS ships autonomous exploit testing as a product feature [AWS-SECAGENT-2026]; Trail of Bits says
  agents made exploratory audit tooling cheap ("a failed side project only costs tokens") [TOB-AUDIT-2026]; GTIG says
  likely AI-found flaws skew to remote code execution (an early indicator) [GTIG-VULNTRENDS-2026].
- **Against:** 32.3% of Trail of Bits' agent-assisted pull requests were closed unmerged, and 12.5% of human first
  fixes fail review [TOB-1PASSWORD-2026].
- **Status:** visible at a few firms. **Watch:** pentest buyers asking how AI is used; accreditation of AI-enabled
  pentests; whether quarterly testing gives way to continuous validation (vulnerability-exposure §2, §8).

## 5. D. Securing AI becomes a line of business

**What changes:** providers sell AI-agent discovery, red teaming, monitoring and AI incident response.
- **For:** eSentire bought an AI security startup for AI observability and control (2026-09-15) [ESENTIRE-2026]; GTIG
  counts 2,076 cumulative AI-stack CVEs [GTIG-VULNTRENDS-2026]; the EU plans a secure testing platform for critical
  sectors [EC-ACTIONPLAN-2026]; only 8% of organizations run AI incident exercises regularly [ISACA-SOC-2026].
- **Against:** buyers lack mature requirements: 48% of ISACA respondents either lack AI incident playbooks or do not
  know whether they have them [ISACA-SOC-2026].
- **Status:** early. **Watch:** agent-identity and AI gateway products arriving from platform vendors (ai-security §8).

## 6. E. Platform bundling compresses point products

**What changes:** AI triage, SIEM and agent security arrive inside licences buyers already own, squeezing standalone
tools and the providers that resell them.
- **For:** Microsoft includes Security Copilot capacity in E5 and E7 [MSLEARN-SCU-2026] and added SIEM tooling in
  preview, per a competitor [PROPHET-ISOC-2026]; CrowdStrike says the agentic SOC is "only possible on a unified
  platform" [CROWDSTRIKE-AGSOC-2026]; 51% of CrowdStrike subscription customers use six or more modules [CRWD-FY27Q2-2026].
- **Against:** Forrester: consolidation "doesn't eliminate tools, skills, or complexity" [FORRESTER-RSAC-2026]; one
  newsletter author argues in-line enforcement and runtime-data products are more defensible than analysis-only ones
  (opinion) [VENTUREINSEC-FOURQ-2026].
- **Status:** visible. **Watch:** data-ingestion prices; contract terms after acquisitions [FORRESTER-PV-2026].

## 7. F. The in-house function becomes the AI risk owner

**What changes:** the CISO organization governs AI for the whole business (policy, vendor review, agent identity,
incidents) while competing for money that often sits elsewhere.
- **For:** 56% of ISACA respondents helped write an AI-use policy [ISACA-SOC-2026]; 38% of organizations fund AI
  security outside the security budget [IANS-BUDGET-2026]; Gartner tells leaders to identify sanctioned and
  unsanctioned agents and write playbooks for them [GARTNER-TRENDS-2026].
- **Against:** ownership is split: in ISACA's poll only 13% named the CISO as responsible if AI causes harm
  [ISACA-AIPULSE-2026].
- **Status:** visible. **Watch:** a distinct AI security budget line (associated with more funding growth)
  [IANS-BUDGET-2026]; board reporting on AI risk.

## 8. Pricing shifts and exposure by service

| Shift | Evidence | Status |
|---|---|---|
| Per endpoint or identity to per investigation | Dropzone prices by investigation capacity [DROPZONE-PRICING-2026] | Early |
| Per seat to compute units | Microsoft Security Copilot units [MSLEARN-SCU-2026] | Visible |
| Metered to flat or unlimited | Arctic Wolf "unlimited investigations" [ARCTICWOLF-AURORA-2026] | Visible |
| Activity metrics to outcome metrics | Gartner advice via a vendor; Arctic Wolf's "Mean Time to Trusted Action" [INTEZER-GARTNERMDR-2026; MSSPALERT-AW-2026] | Early |
| Fees that vary with outcomes | Only warranties found [MSSPALERT-AW-2026] | Not found |
| Insurance bundled with services | Coalition's "Active Insurance" combines insurance coverage with security tools [COALITION-CLAIMS-2026] | Visible |

Exposure by service, an inference from the scenarios above (not a finding of any source):

| Service | Most exposed part | Most defended part |
|---|---|---|
| MDR and MSSP | Tier-1 triage priced per endpoint | Context, response authority, accountability to boards and insurers |
| Pentest and red team | Scanner-like finding work | Exploit validation, fixes, threat-led testing for regulators |
| IR retainer | Log review and timeline building | Crisis leadership, legal and regulator interface, recovery |
| GRC consulting | Questionnaire and evidence drafting | Judgment on risk, regulator dialogue |
| AI security services | Commodity scanning of prompts and skills | Agent containment design, incident response for agents |

## 9. Using this in a conversation

- For a provider: "Which of your services would AI threaten, change a lot, or mainly help? What do clients pay you for
  that an AI SOC product plus one engineer cannot supply?"
- For an in-house leader: "Which managed contracts renew in the next 24 months, and what would you insource if agents
  took tier 1?"
- For both: "Which signal in this file would tell you a scenario is arriving, and who would notice it first?"

## 10. Sources

Keys not listed here are in [sources.md](sources.md).

- **PROPHET-MDR-2026**: Prophet Security, *MDR vs. Agentic AI SOC Analyst: Complementary or Replacement?* (vendor blog, 2026-06-17). https://www.prophetsecurity.ai/blog/mdr-vs-agentic-ai-soc-analyst-complementary-or-replacement
- **TOB-AUDIT-2026**: Trail of Bits, *Auditing in the age of (good enough) AI* (consultancy blog, 2026-09-18). https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/
- **VENTUREINSEC-FOURQ-2026**: Venture in Security (Ross Haleliuk), *Four questions that answer if a security product will survive in the AI-first world* (newsletter, opinion, 2026-06-02). https://ventureinsecurity.net/p/four-questions-to-answer-if-a-security
