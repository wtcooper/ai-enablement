# Pattern: end-to-end-case-agent

Takes a case from intake to resolution across systems, with human checkpoints at key decisions and before anything
irreversible. Read this when an option hands a whole case type to an agent. Keys in brackets are listed in §11.
Lines marked *(guidance)* are design advice, not findings from a source.

## Contents

1. [What it is](#1-what-it-is)
2. [Where it fits](#2-where-it-fits)
3. [Up the ladder](#3-up-the-ladder)
4. [How it is built](#4-how-it-is-built)
5. [Prerequisites](#5-prerequisites)
6. [Failure modes and controls](#6-failure-modes-and-controls)
7. [Value and metrics](#7-value-and-metrics)
8. [Governance](#8-governance)
9. [Evidence](#9-evidence)
10. [Probes](#10-probes)
11. [Sources](#11-sources)

## 1. What it is

An agent plans, calls tools across several systems, checks results at each step, and carries a case (a claim,
ticket, return, filing or alert) to resolution, pausing for a person at checkpoints. Agents suit open-ended problems
where the steps cannot be predicted and a fixed path cannot be hard-coded, "in trusted environments"
[ANTHROPIC-AGENTS-2024]. Deployments exist but publish almost no quality measurements, and independent benchmarks
show low reliability on multi-step work: the best agent completed 30% of simulated-company tasks [CMU-2024]. The
ladder is set by reversibility and by who is affected, not by model capability.

**How to recognize it** *(guidance)*: "a case arrives, someone pulls data from three systems, checks a policy, decides, updates
the systems and tells the customer"; many low-value cases; written policy; systems with APIs; queues at peaks.
Allianz's cue: a simple food-spoilage claim took four days or more because staff were busy with complex storm
claims [ALLIANZ-2025].

## 2. Where it fits

- **Work types:** mainly `transaction-processing`; also `coordination-scheduling` and `review-assurance`.
- **Not for judgment under ambiguity with no written criteria, or one-off cases** *(guidance)*. When the steps can be predicted and fixed in advance, a `workflow-automation` flow is simpler and enough [ANTHROPIC-AGENTS-2024].
- **Not with write access to production without an approval gate or backups** (a coding agent deleted a live database, per the user) [OECD-2025].
- **Not for solely automated decisions with significant effects on individuals and no route to human review** [EU-GDPR-2016; ROBODEBT-RC-2023].
- **Not judged by average success when the process needs consistency every time** [SIERRA-TAUBENCH-2024].
- **Not multi-agent for tightly coupled or low-value work** [ANTHROPIC-MULTIAGENT-2025].
- **Not cutting the human route to save cost before quality is measured** [ENTREPRENEUR-KLARNA-2025].

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `augment` | Prepares each case end to end and writes an audit summary | Decides each case (Allianz keeps the payout human) | `workflow-automation` | Evaluation set from real cases; override rate logged per case type |
| `automate` | Resolves a defined, reversible case type; exceptions go to people | Owns the exception queue; samples closed cases | `workflow-automation`, `background-agent` | Approval only above a value or risk threshold; sampled audit of auto-closed cases *(guidance)* |
| `delegate` | Owns the multi-step outcome, started by events | Sets criteria; approves irreversible steps; audits | `managed-agent-runtime` | Resumable state, checkpoints, full tracing [ANTHROPIC-MULTIAGENT-2025]; repeated-run reliability shown; the delegation gates in `../../method/onboarding.md` §5 |

Evidence for the step from augment to automate is thin: Klarna automated, then reinstated human capacity, saying
quality had fallen [ENTREPRENEUR-KLARNA-2025]. Find the simplest solution and add complexity only when needed
[ANTHROPIC-AGENTS-2024].

## 4. How it is built

- **Inputs.** The case event, the case record across systems, the written policy, evidence the customer supplies. Invest in the agent-computer interface (tools) as much as in prompts [ANTHROPIC-AGENTS-2024].
- **The AI's role.** Plan, call tools, get "ground truth" from the environment at each step, pause for human feedback at checkpoints, stop at a maximum number of iterations [ANTHROPIC-AGENTS-2024]. Allianz splits work into planner, cyber, coverage, weather, fraud, payout and audit agents [ALLIANZ-2025].
- **Human checkpoints.** Define "significant checkpoints at which human approval is required" and limit agents' access to tools and data [IMDA-2026]. Allianz limits its agent to food-spoilage claims under AUD 500 and never automates the payout decision [ALLIANZ-2025].
- **Thresholds and sampling.** Scope by value and reversibility. For auto-resolved cases, use acceptance-sampling plans with an acceptable quality level [NIST-SAMPLING-2026] *(guidance; no deployment publishes its plan)*.
- **Evaluation.** Check the end state rather than each turn, with checkpoints where specific state changes should have occurred [ANTHROPIC-MULTIAGENT-2025].
- **Logging.** Full production tracing [ANTHROPIC-MULTIAGENT-2025]; an audit agent summarizes every agent decision for the human [ALLIANZ-2025]; EU deployers keep logs at least six months [EU-AIACT-2024].

## 5. Prerequisites

- **Data.** Written policy and decision criteria; an evaluation set built from real cases, including ones that went wrong.
- **Access.** APIs to systems of record with scoped credentials; a reversible or approval-gated write path; production separated from development [OECD-2025].
- **Policy.** A named owner of the exception queue; who may act on which systems; a route to human review for affected people.
- **Skills.** Overseers with "competence, training and authority" for high-risk uses [EU-AIACT-2024]. Oversight skill erodes when automation handles the routine and leaves people the hard cases [BAINBRIDGE-1983].

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Errors compound across steps | One failure sends the agent down a different path [ANTHROPIC-MULTIAGENT-2025] | Resume from checkpoints; deterministic retries; stopping conditions |
| Inconsistent on repeated runs | Pass^8 below 25% in a retail benchmark [SIERRA-TAUBENCH-2024] | Report pass^k, not average success; test repeats before go-live |
| Multi-agent breakdowns | 41% to 86.7% failure rates across seven open-source systems [BERKELEY-2025] | Explicit verification step; fewer hand-offs between agents |
| Destructive action against instruction | Live database deleted during a stated freeze [OECD-2025] | Approval gate on irreversible writes; backups kept apart |
| Acting beyond scope; hard to trace | Agent autonomy, scope and auditability named as risks [FINRA-OVERSIGHT-2026] | Scoped identity and tool access; action log tied to a human owner |
| Reviewer over-reliance | Automation bias [NIST-AI600-2024; IMDA-2026] | Seeded test cases; measured override rate; rotating review |
| Confidential data leakage | "Near-zero" inherent confidentiality awareness [SALESFORCE-CRMARENA-2025] | Data-scoped tools; do not rely on prompting |

## 7. Value and metrics

- **Levers:** `speed`, `capacity`, `quality`, `cost`, `experience`.
- **Typical figures:** Allianz says processing and settlement time fell 80%, from several days to hours for small claims (self-reported, basis not given) [ALLIANZ-2025]; Klarna's month-one figures (two-thirds of chats; under 2 vs 11 minutes) come from an adjacent service pattern [KLARNA-AIASSISTANT-2024].
- **Unit cost.** Agents use about four times the tokens of chat and multi-agent systems about fifteen times, so cost per case must include inference [ANTHROPIC-MULTIAGENT-2025].
- **Metrics to require** (no deployment publishes them): share of cases closed with no human edit; share escalated; share overturned on appeal or complaint; error rate in a sampled audit; cost per resolved case including tokens; a quality measure tracked alongside cost (Klarna's CEO said cheaper AI service gave "lower quality") [ENTREPRENEUR-KLARNA-2025].
- **Reliability floor** (2024-2025 models): 30% of simulated-company tasks [CMU-2024]; 2.5% automation of real freelance projects [CAIS-2025]. The task length models complete at 50% success has doubled about every seven months [METR-HORIZON-2025].

## 8. Governance

- **NIST AI RMF.** GOVERN 3.2 (roles for human-AI configurations), MAP 3.5 (oversight documented), MANAGE 2.4 (supersede, disengage, deactivate) [NIST-AIRMF-2023]; automation bias and confabulation [NIST-AI600-2024].
- **EU AI Act.** Art. 14 oversight: understand capacity, stay aware of automation bias, override, intervene or stop; Art. 6(3) narrow-task derogations never cover profiling; Art. 26 deployer duties [EU-AIACT-2024]. Annex III duties apply from 2 December 2027 [EC-2026].
- **GDPR Art. 22.** Human intervention, a chance to express a view and to contest solely automated decisions with significant effects [EU-GDPR-2016].
- **ISO/IEC 42001.** An organization-level, certifiable management system [BSI-ISO42001-2026].
- **Sector.** FINRA asks where to place human oversight, how to track agent actions and how to restrict agent behaviour [FINRA-OVERSIGHT-2026]; Singapore's agentic framework adds baseline testing and whitelisted services [IMDA-2026]; the Robodebt Commission recommended review paths and an audit body for automated decisions [ROBODEBT-RC-2023].

## 9. Evidence

No cross-industry deployment of this pattern publishes a measured quality figure; all examples are B.

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| Allianz Australia | Insurance | Seven agents handle coverage, weather, fraud, payout and audit steps for small claims; a person decides payment | Time -80% per an executive; under five minutes to human review in a worked example (self-reported) | B | ALLIANZ-2025 |
| Klarna | Fintech | Assistant handles refunds and returns in chat; live agents available | Two-thirds of chats in month one (self-reported; adjacent: `service-agent-escalation`) | B | KLARNA-AIASSISTANT-2024 |
| Klarna, 2025 | Fintech | CEO said AI service was cheaper but gave "lower quality"; hiring humans again | Statement, no metric (via press) | B | ENTREPRENEUR-KLARNA-2025 |
| Anthropic | Technology | Lead agent plans and spawns sub-agents; citation agent attributes claims | 90.2% better than a single agent on an internal evaluation (vendor benchmark; read-only task) | B | ANTHROPIC-MULTIAGENT-2025 |
| UK Incubator for AI | Public sector | Prototype triages householder planning applications and drafts an initial assessment for officers | Prototype; no outcome published | B | IAI-PLANNING-2026 |
| Replit user (SaaStr founder) | Software | Coding agent deleted a live production database despite instructions | Incident record compiled from media; user's account (failure case) | B | OECD-2025 |
| UnitedHealth / naviHealth | Health insurance | Alleged use of a model to supplant physician judgment on post-acute coverage | Court let claims proceed; Senate finding that denials "more than doubled", as cited (allegations) | B | AFS-2026 |

**In the archetypes:** `security-operations-09` (A), `security-vulnerability-exposure-17` (A),
`tax-compliance-individual-business-05` (A), `assurance-substantive-testing-20` (B),
`assurance-substantive-testing-21` (B), `tax-compliance-corporate-07` (B), `security-incident-response-05` (B),
`professional-services-acceptance-risk-08` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "Walk me through one case from arrival to closure, naming each system touched." | Steps, hand-offs, APIs; whether a simple flow is enough |
| "Which action in that sequence cannot be undone, and who may do it today?" | Where the human checkpoint goes |
| "Where is the written rule, and how often do two experienced people decide differently?" | Whether the agent can be tested; disagreement sets a ceiling on "correct" [IAI-SCOT-2025] |
| "What share of cases would you close with no human look, and what would you need to see first?" | Risk appetite and the sampling plan |
| "Does the decision affect a person's rights, money, job, benefits or health?" | Which legal regime applies |
| "Who reads exceptions and samples, and how many a day?" | Reviewer capacity, the real throughput limit |
| "What is the cost per resolved case, including model tokens?" | Whether a low-value case pays back |
| "If we ran the same case five times, must the outcome be identical?" | The consistency requirement average success hides |

## 11. Sources

- `AFS-2026` — ArentFox Schiff, *Federal court orders broad discovery against UHC in AI coverage denial lawsuit*, 2026-04-23. https://www.afslaw.com/perspectives/alerts/federal-court-orders-broad-discovery-against-uhc-ai-coverage-denial-lawsuit
- `ALLIANZ-2025` — Allianz SE, *When the storm clears, so should the claim queue*, 2025-11-03. https://allianz.com/en/mediacenter/news/articles/251103-when-the-storm-clears-so-should-the-claim-queue.html
- `ANTHROPIC-AGENTS-2024` — Anthropic, *Building effective agents*, 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents
- `ANTHROPIC-MULTIAGENT-2025` — Anthropic, *How we built our multi-agent research system*, 2025-06-13. https://www.anthropic.com/engineering/multi-agent-research-system
- `BAINBRIDGE-1983` — L. Bainbridge, *Ironies of Automation*, Automatica 19(6), 1983. https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf
- `BERKELEY-2025` — Cemri et al., *Why Do Multi-Agent LLM Systems Fail?*, 2025-03. https://arxiv.org/pdf/2503.13657
- `BSI-ISO42001-2026` — BSI, *ISO/IEC 42001: AI Management System* (description), retrieved 2026-10-20. https://www.bsigroup.com/en-GB/products-and-services/standards/iso-42001-ai-management-system/
- `CAIS-2025` — Mazeika et al., *Remote Labor Index: Measuring AI Automation of Remote Work*, 2025-10-30. https://arxiv.org/pdf/2510.26787
- `CMU-2024` — Xu et al., *TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks*, 2024-12. https://arxiv.org/pdf/2412.14161
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `ENTREPRENEUR-KLARNA-2025` — Entrepreneur, *Klarna CEO Reverses Course By Hiring More Humans, Not AI*, 2025-05-09. https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `EU-GDPR-2016` — European Union, *GDPR Art. 22*, 2016-04-27. https://gdpr-info.eu/art-22-gdpr/
- `FINRA-OVERSIGHT-2026` — FINRA, *2026 Annual Regulatory Oversight Report: GenAI*, 2025-12. https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
- `IAI-PLANNING-2026` — UK Incubator for AI, *Planning: Extract and Augmented Planning Decisions*, 2026-06. https://ai.gov.uk/our-work/planning
- `IAI-SCOT-2025` — UK Incubator for AI, *Consult evaluation: Scottish Government consultation*, 2025-03-20. https://digitalgovernmenthub.org/wp-content/uploads/2026/02/Scot_Gov_NSCP_Evaluation_Report.pdf
- `IMDA-2026` — Singapore IMDA, *New Model AI Governance Framework for Agentic AI*, 2026-01-22. https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai
- `KLARNA-AIASSISTANT-2024` — Klarna, *AI assistant handles two-thirds of customer service chats in its first month*, 2024-02-27. https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
- `METR-HORIZON-2025` — Kwa et al., METR, *Measuring AI Ability to Complete Long Software Tasks*, 2025-03. https://arxiv.org/pdf/2503.14499
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `NIST-AIRMF-2023` — NIST, *AI Risk Management Framework 1.0 (NIST AI 100-1)*, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `NIST-SAMPLING-2026` — NIST/SEMATECH, *e-Handbook of Statistical Methods* §6.2.1–6.2.2 (acceptance sampling), retrieved 2026-10-20. https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm
- `OECD-2025` — OECD.AI, *Replit AI coding tool deletes live production database* (incident record), 2025-07-19. https://oecd.ai/en/incidents/2025-07-19-1eb1
- `ROBODEBT-RC-2023` — Royal Commission into the Robodebt Scheme, *Report: recommendations*, 2023-07-07. https://robodebt.royalcommission.gov.au/publications/report
- `SALESFORCE-CRMARENA-2025` — Huang et al., Salesforce AI Research, *CRMArena-Pro*, 2025-05-24. https://arxiv.org/pdf/2505.18878
- `SIERRA-TAUBENCH-2024` — Yao et al., Sierra, *τ-bench: A Benchmark for Tool-Agent-User Interaction*, 2024-06-17. https://arxiv.org/pdf/2406.12045
