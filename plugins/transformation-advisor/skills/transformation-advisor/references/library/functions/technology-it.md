# Technology (IT)

Function id `technology-it`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:** software
delivery has the best controlled evidence of any function, and it points different ways depending on what is measured. Task trials
show faster work; one 2025 trial of experienced open-source developers on their own code found tasks took 19% longer
[METR-RCT-2025]; system-level data show individual output up and delivery instability up [DORA-2024; DORA-2025]. The constraint
moves downstream to review, testing and release. Service-desk deflection figures (25-45%) are all self-reported or vendor-published.

## Contents

1. [What this function covers](#1-what-this-function-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Metrics and benchmarks](#4-metrics-and-benchmarks)
5. [Interview probes](#5-interview-probes)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Sources](#8-sources)

## 1. What this function covers

The IT function's own work in any organization: strategy and demand, architecture, software delivery, release, operations, the
service desk, resilience and knowledge management. Security operations, application security and AI security are the security
archetype; cite its modules for that work. No archetype covers IT services firms; use this card.

## 2. Processes and key steps

The process list is a working grouping under the "manage information technology" category of a cross-industry process framework
[APQC-PCF-PAYOR-2019].

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| Customer relationships and IT strategy | Understand demand; set roadmap; check service levels | expert-judgment, coordination-scheduling, data-reporting | Half of developers lose 10+ hours a week to non-coding work (vendor survey of 3,500) [ATLASSIAN-DEVEX-2025] |
| Architecture and design | Evaluate options; record decisions; review against standards | expert-judgment, research-synthesis, document-production, software-systems | "Codebase cognitive debt": AI-written code adopted without the mental models to reason about it [TW-RADAR-2026] |
| Build and change | Plan; code; test; review; integrate; migrate and upgrade | software-systems, review-assurance | Review becomes the bottleneck: review time +91% in high-adoption teams (vendor telemetry) [FAROS-2025]; upgrades take months or years [AWS-QTRANSFORM-2024] |
| Deploy and release | Package; approve change; deploy; verify; roll back | software-systems, coordination-scheduling | Delivery instability rises with AI adoption [DORA-2024; DORA-2025] |
| Run and operate | Monitor; incidents and problems; capacity; configuration and licences | data-reporting, software-systems, transaction-processing | No non-security operations agent with published results found |
| Service desk and user support | Triage; resolve; fulfil requests; escalate; confirm | client-interaction, transaction-processing | About 50,000 tickets a month at Oracle IT, peaking near 5,000 a day; its earlier rule-based bot struggled with context [ORACLE-AISD-2025] |
| Resilience, risk and continuity | Plan; recover; access and directory management | review-assurance, expert-judgment | See the security archetype |
| Information and knowledge management | Manage data and content; keep the knowledge base current | data-reporting, document-production | Trust is low: 46% of developers distrust AI accuracy, 33% trust it [STACKOVERFLOW-2025] |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **Coding assistants for individual developers** ([draft-review-loop](../patterns/draft-review-loop.md); assist; step). Mixed:
  - ANZ Bank (financial services): the assistant group completed algorithmic tasks 42.36% faster than control; participants not
    monitored, tasks not bank work. Self-reported. Grade A (task measurement, limited scope) [ANZ-COPILOT-2024].
  - Google (technology): about 21% faster on an enterprise task for 96 engineers, with a wide confidence interval. Grade A
    [GOOGLE-RCT-2024]. A 2023 lab task was 55.8% faster [PENG-2023].
  - UK central government (public sector): telemetry showed 15.8% of suggested lines accepted; 56 minutes a day saved is a survey
    estimate. Grade A for the telemetry; the time saving is survey-based [UK-GDS-AICA-2025].
  - Counter-evidence: 16 experienced developers on 246 tasks in their own repositories took 19% longer with AI, while believing they
    were 20% faster (independent randomized trial) [METR-RCT-2025]. METR's follow-up gave "an unreliable signal" because many
    developers declined to work without AI [METR-UPLIFT-2026].
- **AI first-pass pull-request review** ([draft-review-loop](../patterns/draft-review-loop.md); augment; step). Microsoft (internal
  engineering): over 90% of pull requests, more than 600,000 a month; 10-20% median completion-time improvement across 5,000 repositories
  in "early experiments and data science studies" (not randomized). Self-reported. Grade A [MS-CODEREVIEW-2025].
- **Incident triage, root-cause hints and mitigation suggestions** ([research-brief](../patterns/research-brief.md),
  [monitor-diagnose-act](../patterns/monitor-diagnose-act.md); augment; step). Microsoft (cloud services): root-cause accuracy up to
  0.766 on one year of real incidents in an offline evaluation; the data-collection component has been in use for over four years.
  Self-reported by researchers at the deploying organization. Grade B (offline evaluation, not a work outcome) [MS-RCACOPILOT-2023].
- **Drafting architecture decision records** ([draft-review-loop](../patterns/draft-review-loop.md); assist; step). Idea: an
  exploratory study found zero-shot output relevant and accurate but below human level. Grade D [IIITH-ADR-2024].

**Automate the flow**

- **Large migrations and upgrades run as AI-led programs, with engineers verifying and code owners reviewing**
  ([bulk-transformation](../patterns/bulk-transformation.md); augment to automate; process). Google (Ads): in a 32-bit to 64-bit ID
  migration across a 500-million-line code base, 80% of code modifications in landed changes were fully AI-authored (tracked); the 50%
  cut in total migration time is the engineers' estimate; people often had to revert some model changes. Grade A for the 80%
  [GOOGLE-MIG-2025]. Amazon (retail and technology): Java upgrades across tens of thousands of applications; "over 4,500 years" of
  developer work and $260 million a year are estimates. Grade B [AWS-QTRANSFORM-2024].
- **Service-desk assistant grounded in the knowledge base, with a human ticket as the exit**
  ([grounded-knowledge-assistant](../patterns/grounded-knowledge-assistant.md),
  [service-agent-escalation](../patterns/service-agent-escalation.md); automate; step to process). Oracle IT (technology): 25-30%
  ticket deflection, 3,100-4,000 tickets a week; employees confirm "solved" or a ticket opens for an engineer. Self-reported by a team
  whose company sells the underlying service. Grade A [ORACLE-AISD-2025]. An unnamed global bank: 45% of level-1 contacts deflected
  (vendor-published). Grade C [HCL-BANK-2026].

**Delegate the outcome**

- Outside security, no operations agent with published results was found. Bounded delegated testing exists in the security archetype
  (`security-application-security-10`, A). Agent incidents are in §6.

**Reinvent the work**

- **Redesign the delivery flow so local gains reach customers** (pattern `other`; process). DORA 2025 reports value stream management
  acting as a force multiplier and seven capabilities that amplify AI's effect (survey-based) [DORA-2025]. Adidas (retail): per a report
  foreword, teams with loosely coupled architecture and fast feedback loops saw 20-30% productivity gains in commits, pull requests and
  delivery velocity, while teams tightly coupled to ERP systems saw "little or no AI benefits". Grade B [DORA-2025].
- **Combine HR and IT planning** (Moderna; see the people-hr card) [UNLEASH-MODERNA-2025].

**In the archetypes**: `security-application-security-04` (A, AI review of every pull request), `security-application-security-07`
(A), `security-application-security-10` (A), `security-operations-01` (A), `security-operations-02` (A),
`security-incident-response-08` (B, ranking likely root-cause changes), `professional-services-knowledge-management-07` (B, repository
clean-up), `tax-data-technology-18` (C, agents calling tax engines under least-privilege scopes).

## 4. Metrics and benchmarks

- **Delivery performance:** throughput (lead time for changes, deployment frequency, failed-deployment recovery time) and
  instability (change fail rate, rework rate); use all five [DORA-2025].
- **Company-level effects:** DORA 2024 estimated -1.5% throughput and -7.2% stability per 25% increase in AI adoption; DORA 2025 finds
  throughput now improves but instability still rises, 90% use AI and 30% report little or no trust in AI-generated code (surveys)
  [DORA-2024; DORA-2025]. In vendor telemetry from 10,000+ developers, high-adoption teams merged 98% more pull requests, with review
  time +91% and bugs per developer +9%, and no significant company-level correlation [FAROS-2025].
- **Share of code AI-authored:** 27.4% of merged code across close to 500 companies, with 3.9 hours a week saved (self-reported) and
  some companies speeding up as quality degrades (vendor-published) [DX-AIIMPACT-2026].
- **Acceptance:** 15.8% of suggested lines accepted [UK-GDS-AICA-2025].
- **Service desk:** deflection rate, share resolved by AI, ticket volume, resolution time, employee satisfaction, engineer
  productivity [ORACLE-AISD-2025]. No reopen or cost-per-ticket benchmark found.
- **Code security:** insecure code in 45% of tests across 100+ models (vendor-published) [VERACODE-2025].

## 5. Interview probes

1. "Where does a pull request wait now, and how long?" Reveals whether coding speed or review, test and release is the constraint
   [FAROS-2025; DORA-2025].
2. "Do you measure instability (change fail rate, rework) next to throughput?" Reveals a productivity story told from throughput alone
   [DORA-2024; DORA-2025].
3. "Was that productivity number measured on tasks, teams or the company, and by whom?" Reveals the gap between felt and measured
   gains [METR-RCT-2025; FAROS-2025].
4. "Which migrations or upgrades are bounded, testable and repeated enough to run as a program?" Reveals `bulk-transformation`
   candidates [GOOGLE-MIG-2025; AWS-QTRANSFORM-2024].
5. "What fraction of AI-suggested code is accepted, and what happens to the rest?" Reveals shallow use and the source of review load
   [UK-GDS-AICA-2025].
6. "What share of tickets would you let an assistant close without a person, what is the check, and what is the exit?" Reveals the
   containment ceiling and whether reopens and wrong answers are counted [ORACLE-AISD-2025].
7. "Which actions can an agent take on production without approval, and with what credentials?" Reveals least-privilege design before
   any delegate step [AWS-BULLETIN-2025; REGISTER-REPLIT-2025].
8. "Who on the team can still explain the system without the AI?" Reveals comprehension risk [TW-RADAR-2026; ANTHROPIC-WORK-2025].
9. "Where do developers lose time outside coding, and has any AI saving been spent there?" Reveals whether savings are absorbed by
   friction [ATLASSIAN-DEVEX-2025].

## 6. Guardrails

- **Scope agent permissions and the tool supply chain.** An over-scoped repository token let an attacker commit malicious code into an
  AI coding extension release; AWS said it did not execute because of a syntax error [AWS-BULLETIN-2025]. A founder reported that an AI
  coding service deleted a production database despite a code-freeze instruction (the user's account, reported by press)
  [REGISTER-REPLIT-2025].
- **Keep review real.** Google engineers reverted some model-made changes even when AI authored most of a change, and the program
  invested in automated verification [GOOGLE-MIG-2025]; Microsoft keeps human review after the AI first pass [MS-CODEREVIEW-2025].
- **Frameworks:** NIST AI RMF and its generative AI profile, which names confabulation, information security and value-chain risks
  [NIST-AIRMF-2023; NIST-AI600-1-2024].
- **EU AI Act:** IT's internal tools are not high-risk by default; they become so if used for workforce decisions listed in Annex III
  (see the people-hr card).
- **Shadow AI and licences:** DX flags unmanaged use and the need for acceptable-use policies [DX-AIIMPACT-2026].
- **Decisions that need human judgment:** release and rollback approval; destructive operations on production data; access grants and
  privileged scopes; accepting AI-written changes into critical systems; architecture trade-offs. Anthropic's engineers said they keep
  high-level design and "taste" decisions [ANTHROPIC-WORK-2025].

## 7. Roles and how they evolve

- **Engineers become orchestrators and reviewers** of AI contributions across more parallel work (vendor interpretation)
  [FAROS-2025].
- **Delegation stays narrow:** more than half of surveyed Anthropic engineers said they can fully delegate only 0-20% of their work,
  and some worried that supervising AI needs skills that could atrophy (self-reported by a tool builder) [ANTHROPIC-WORK-2025].
- **Migrations need fewer coordinators:** one engineer could generate all changes in Google's migration, cutting communication
  overhead [GOOGLE-MIG-2025].
- **Service engineers move to knowledge-base quality and tier-2 support** [ORACLE-AISD-2025].
- **Juniors use AI most;** daily-using juniors now match seniors in time saved (vendor-published) [DX-AIIMPACT-2026].

## 8. Sources

- **ANTHROPIC-WORK-2025**: Anthropic, *How AI is transforming work at Anthropic* (firm, 2025-12-02). https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- **ANZ-COPILOT-2024**: Chatterjee et al. (ANZ), *The Impact of AI Tool on Engineering at ANZ Bank* (firm, arXiv 2402.05636, 2024-04-17). https://arxiv.org/pdf/2402.05636
- **APQC-PCF-PAYOR-2019**: APQC, *Health Insurance Payor Process Classification Framework v7.2.1* (professional body, 2019-02-13). https://www.apqc.org/system/files/Health%20Insurance%20Payor_721_021319.pdf
- **ATLASSIAN-DEVEX-2025**: Atlassian, *State of DevEx 2025* (vendor survey, 2025-07-09). https://www.atlassian.com/blog/developer/developer-experience-report-2025
- **AWS-BULLETIN-2025**: Amazon Web Services, *Security Update for Amazon Q Developer Extension for Visual Studio Code, AWS-2025-015* (vendor, 2025-07-23). https://aws.amazon.com/security/security-bulletins/AWS-2025-015/
- **AWS-QTRANSFORM-2024**: Amazon Web Services, *Amazon Q Developer just reached a $260 million dollar milestone* (vendor, 2024-08-01). https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone
- **DORA-2024**: Google Cloud DORA, *Accelerate State of DevOps 2024* (survey, 2024). https://services.google.com/fh/files/misc/2024_final_dora_report.pdf
- **DORA-2025**: Google Cloud DORA, *2025 State of AI-assisted Software Development* (survey, 2025-09-23). https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf
- **DX-AIIMPACT-2026**: DX, *AI-assisted engineering: Q1 impact report* (vendor, 2026). https://getdx.com/uploads/ai-assisted-engineering-q1-impact-report.pdf
- **FAROS-2025**: Faros AI, *The AI Productivity Paradox Report 2025* (vendor, 2025-07-23). https://www.faros.ai/blog/ai-software-engineering
- **GOOGLE-MIG-2025**: Nikolov et al. (Google), *How is Google using AI for internal code migrations?* (firm, arXiv 2501.06972, 2025-01-12). https://arxiv.org/pdf/2501.06972
- **GOOGLE-RCT-2024**: Paradis et al. (Google), *How much does AI impact development speed? An enterprise-based randomized controlled trial* (firm, arXiv 2410.12944, 2024-11-11). https://arxiv.org/pdf/2410.12944
- **HCL-BANK-2026**: HCLTech, *Transforming global support with 45% L1 deflection* (vendor, 2026-09-10). https://www.hcltech.com/case-study/global-support-l1-deflection
- **IIITH-ADR-2024**: Dhar, Vaidhyanathan, Varma, *Can LLMs Generate Architectural Design Decisions?* (academic, arXiv 2403.01709, 2024-03-04). https://arxiv.org/pdf/2403.01709
- **METR-RCT-2025**: METR, *Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity* (academic, arXiv 2507.09089, 2025-07-25). https://arxiv.org/pdf/2507.09089
- **METR-UPLIFT-2026**: METR, *We are Changing our Developer Productivity Experiment Design* (academic, 2026-02-24). https://metr.org/blog/2026-02-24-uplift-update/
- **MS-CODEREVIEW-2025**: Microsoft, *Enhancing Code Quality at Scale with AI-Powered Code Reviews* (firm, 2025-07-14). https://devblogs.microsoft.com/engineering-at-microsoft/enhancing-code-quality-at-scale-with-ai-powered-code-reviews/
- **MS-RCACOPILOT-2023**: Chen et al. (Microsoft), *Automatic Root Cause Analysis via Large Language Models for Cloud Incidents* (academic, arXiv 2305.15778, 2023-11-13). https://arxiv.org/pdf/2305.15778
- **NIST-AIRMF-2023**: NIST, *AI Risk Management Framework 1.0* (standard-setter, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **NIST-AI600-1-2024**: NIST, *AI RMF: Generative AI Profile* (standard-setter, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- **ORACLE-AISD-2025**: Oracle, *Transforming IT support: the generative AI-powered service desk* and customer page (vendor, 2025-10, inferred). https://www.oracle.com/customers/oracle-it/
- **PENG-2023**: Peng et al., *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot* (academic, arXiv 2302.06590, 2023-02-13). https://arxiv.org/pdf/2302.06590
- **REGISTER-REPLIT-2025**: The Register, *Vibe coding service Replit deleted production database* (press, 2025-07-21). https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/
- **STACKOVERFLOW-2025**: Stack Overflow, *2025 Developer Survey, AI section* (survey, 2025). https://survey.stackoverflow.co/2025/ai
- **TW-RADAR-2026**: Thoughtworks, *Technology Radar Vol. 34, themes* (firm, 2026-04). https://www.thoughtworks.com/radar
- **UK-GDS-AICA-2025**: Government Digital Service, *AI coding assistant trial: UK public sector findings report* (government, 2025-09-12). https://www.gov.uk/government/publications/ai-coding-assistant-trial/ai-coding-assistant-trial-uk-public-sector-findings-report
- **UNLEASH-MODERNA-2025**: UNLEASH, *Why Moderna merged HR and IT to better 'architect the flow of work'* (press, 2025-06-27). https://www.unleash.ai/artificial-intelligence/why-moderna-merged-hr-and-it-to-better-architect-the-flow-of-work/
- **VERACODE-2025**: Veracode, *2025 GenAI Code Security Report* (vendor, 2025). https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/
