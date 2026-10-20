# Pattern: monitor-diagnose-act

Watches signals continuously, explains anomalies and proposes or takes actions. Read this when an option replaces
someone watching a dashboard, an inbox of alerts or a periodic check. Keys in brackets are listed in §11. Lines
marked *(guidance)* are design advice, not findings from a source.

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

Three separable verbs, often delivered at different rungs: **detect** (rules or a model watch telemetry, records or
events), **diagnose** (rank likely causes and assemble context), **act** (recommend, or execute from a closed set).
Meta's system diagnoses only, ranking candidate code changes to a top five [META-RCA-2024]. Autonomy is earned by
bounding the action, not by trusting the model: the one documented production control design starts in
recommendation mode, goes live only when an operator flips a switch, and falls back automatically on a constraint
breach [DEEPMIND-BCOOLER-2022]. Alert acceptance is the metric that links the pattern to outcomes [HENRY-TREWS-2022].

**How to recognize it** *(guidance)*: "someone watches a dashboard"; "we find out from the customer"; "alerts go to
a shared inbox nobody reads"; "on-call spends the first hour gathering context"; "the same triage steps every time".

## 2. Where it fits

- **Work types:** `coordination-scheduling`, `data-reporting`, `physical-field`.
- **Seen with:** incident root-cause analysis in cloud operations [MSFT-RCACOPILOT-2024; META-RCA-2024]; clinical early warning [HENRY-TREWS-2022]; building cooling control [DEEPMIND-BCOOLER-2022]; real-time fraud monitoring [FINTECHFUTURES-DANSKE-2017]; security operations (§9).
- **Not for automatic actions that are hard to reverse** without a closed action set, a halt control and a tested incident procedure (Knight Capital) [SEC-KNIGHT-2013].
- **Not to page people on every anomaly**; page only on urgent, actionable conditions [GOOGLE-SREBOOK-2017].
- **Not for time-critical clinical alerts without local validation and a response design** [WONG-ESM-2021; FDA-CDS-2026].
- **Not when a high headline accuracy is taken as proof of diagnosis** [CLOUDOPSBENCH-2026].
- **Not for work that needs only a rule or a report**; Gartner says many use cases "positioned as agentic today don't require agentic implementations" [GARTNER-AGENTIC-2025].

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Explains an alert or summarizes context on request | Diagnoses and acts | `personal-assistant` | Historical incidents with known causes for backtesting |
| `augment` | Detects and diagnoses; ranks causes with evidence | Verifies and acts (Meta, Microsoft) | `workflow-automation`, `shared-team-skills` | Accuracy measured on the evidence, not only the answer; alert-to-action and override rates tracked |
| `automate` | Acts from a closed, pre-authorized set; falls back automatically | Enables via a switch; can disable; reviews actions | `background-agent` | Tested stop control; constraint checks; count of unattended actions reversed |
| `delegate` | Owns detect, diagnose and fix across systems | Approves irreversible actions; audits | `managed-agent-runtime` | Sources describe plans, not results, at this rung [META-RCA-2024]; keep `delegate` out of Adopting teams (`../index.md` §1) |

## 4. How it is built

- **Inputs.** Telemetry, asset and ownership data, change history, runbooks. Meta's retrieval uses code ownership and the runtime code graph to cut thousands of changes to a few hundred before a model ranks them [META-RCA-2024]; Microsoft matches incidents to team-built handlers that collect diagnostics [MSFT-RCACOPILOT-2024].
- **Alert design is the first control.** Page a human only for urgent, actionable, user-affecting conditions; ask "Could the action be safely automated?" [GOOGLE-SREBOOK-2017].
- **The AI's role.** Summarize and rank, not decide. Meta avoids recommending low-confidence answers, "sacrificing reach in favor of precision" [META-RCA-2024].
- **Bounding the action.** BCOOLER enforces action constraints, the building system applies its own safety checks, control reverts to the existing controller on a constraint breach, and operators can disable it [DEEPMIND-BCOOLER-2022].
- **Human checkpoints.** Responders must be able to "independently reproduce" results [META-RCA-2024]; clinicians confirm or dismiss each alert on an evaluation page [HENRY-TREWS-2022].
- **Logging.** Capture responder feedback [MSFT-RCACOPILOT-2024]; EU deployers keep logs at least six months [EU-AIACT-2024]; NIST MANAGE 4.1 monitoring with override [NIST-AIRMF-2023].

## 5. Prerequisites

- **Data.** Telemetry with consistent labels; historical incidents with known root causes (Meta backtested against past investigations; Microsoft used a year of incidents labelled by experienced engineers) [META-RCA-2024; MSFT-RCACOPILOT-2024].
- **Policy.** Written rules for which actions may run unattended, who can switch the system off, and what triggers fallback. Knight lacked written incident and deployment procedures [SEC-KNIGHT-2013].
- **Skills.** An owner of detection quality: Google SRE teams typically have "one or sometimes two" members on monitoring [GOOGLE-SREBOOK-2017].
- **Safety engineering** where physical or clinical consequences exist; setting BCOOLER's constraints took "significant time" with the systems provider [DEEPMIND-BCOOLER-2022].

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Alert fatigue | People "second-guess, skim, or even ignore" alerts [GOOGLE-SREBOOK-2017]; clinical alert override rates of 46.2% to 96.2% [POLY-OVERRIDE-2020] | Page only on actionable conditions; track alert-to-action rate and override reasons; analyze overrides as a performance signal [FRB-SR117-2011] |
| Automation bias under time pressure | Over-reliance grows with workload and urgency [GODDARD-AB-2012; FDA-CDS-2026] | Training, accountability, confidence display, reproducible evidence |
| Wrong diagnosis presented confidently | Top-five backtest accuracy 42% [META-RCA-2024]; evidence closure as low as 0.15 in a benchmark [CLOUDOPSBENCH-2026] | Require cited evidence; measure the evidence process, not just the answer |
| Unsafe automatic action | Knight's router ran 45 minutes with no halt: $460 million loss [SEC-KNIGHT-2013] | Closed action set, scoped credentials, automatic fallback, a tested stop [EU-AIACT-2024 Art. 14(4)(e); NIST-AIRMF-2023 MANAGE 2.4] |
| Poor external validity | A widely used vendor sepsis model missed 67% of cases locally [WONG-ESM-2021] | Validate on your data before reliance; re-validate periodically |
| Association mistaken for effect | Outcome gains tied to fast confirmation, in an observational study [ADAMS-TREWS-2022] | Say "associated with"; prefer a stepped rollout or control group *(guidance)* |

## 7. Value and metrics

- **Levers:** `speed`, `risk`, `quality`, `cost`, `capacity`, `experience`.
- **Typical figures:** TREWS: 89% of alerts evaluated, 38% confirmed; confirmation within 3 hours associated with a 3.3% adjusted absolute mortality reduction and 1.85 hours faster antibiotics (observational) [ADAMS-TREWS-2022; HENRY-TREWS-2022]; BCOOLER about 9% and 13% energy savings in alternating-day live tests (vendor-published) [DEEPMIND-BCOOLER-2022]; Danske 50% fewer false positives (executive statement) [FINTECHFUTURES-DANSKE-2017].
- **Quality metrics to require:** alert-to-action rate; override rate with reasons; share of alerts that were true; evidence-closure rate for diagnoses; automatic fallback or manual disable rate; unattended actions reversed.
- No source reports a parallel run against a human-only process for this pattern.

## 8. Governance

- **NIST AI RMF.** MEASURE 2.4 (monitored in production), MANAGE 2.4 (supersede, disengage, deactivate), MANAGE 4.1, GOVERN 1.5 [NIST-AIRMF-2023]; confabulation and automation bias where models explain alerts [NIST-AI600-2024].
- **EU AI Act.** Annex III 2 covers safety components in critical digital infrastructure, road traffic and utilities; Art. 14(4)(e) requires a "stop" button or similar; Art. 26 assigns competent overseers, monitoring and log keeping [EU-AIACT-2024]. Annex III duties apply from 2 December 2027 [EC-2026].
- **ISO/IEC 42001.** An organization-level, certifiable management system [BSI-ISO42001-2026].
- **US federal.** OMB requires monitoring for post-deployment change, operator training, human oversight and, "when practicable", a fail-safe [OMB-M2521-2025].
- **Health.** FDA treats software that detects a condition such as sepsis and alerts a clinician as "a device function" [FDA-CDS-2026].
- **Finance.** Model risk guidance expects override analysis; a high override rate often signals a model needs revision [FRB-SR117-2011].

## 9. Evidence

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| TREWS, five hospitals | Healthcare | ML sepsis alert; clinicians confirm or dismiss each alert | 590,736 patients monitored; 38% of evaluated alerts confirmed; mortality association with fast confirmation (self-reported, peer-reviewed; developer licence disclosed) | A | ADAMS-TREWS-2022 |
| Trane with DeepMind/Google | Commercial facilities | Agent sends cooling setpoints; operator switch; automatic fallback | About 9% and 13% energy savings in live alternating-day tests (vendor-published) | A | DEEPMIND-BCOOLER-2022 |
| Knight Capital | Financial services | Automated order router acted on defective code with no halt | 45 minutes, $460 million loss, $12 million penalty (independent regulator; not AI) | A | SEC-KNIGHT-2013 |
| Michigan Medicine | Healthcare | External validation of a widely deployed vendor sepsis model | AUC 0.63; 67% of sepsis cases missed; alerts on 18% of patients (independent; validation of the model, not a work outcome) | B | WONG-ESM-2021 |
| Microsoft (RCACopilot) | Technology | Handlers collect diagnostics; a model predicts the root-cause category | Micro-F1 0.766 on a test set; collection module used by over 30 teams (self-reported; tool test) | B | MSFT-RCACOPILOT-2024 |
| Meta | Technology | Retrieval plus a fine-tuned ranker suggests a top five root causes | 42% of investigations had the cause in the top five in backtesting (self-reported; not a production result) | B | META-RCA-2024 |
| Danske Bank | Financial services | AI fraud engine replaced handcrafted rules | 50% fewer false positives (executive statement, no definition) | B | FINTECHFUTURES-DANSKE-2017 |

**In the archetypes:** `security-threat-intelligence-21` (A), `security-threat-intelligence-22` (A),
`security-ai-security-15` (A), `security-human-risk-01` (A), `tax-controversy-19` (A),
`assurance-controls-testing-09` (B), `professional-services-quality-review-11` (B), `security-ai-security-11` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "When a signal fires today, what is the first thing a person does?" | Repetitive diagnostic steps worth automating |
| "What share of your alerts lead to action, and what happens to the rest?" | Alert-to-action and override rates; fatigue |
| "Which actions could the system take on its own, and which could not be undone?" | The closed action set; irreversible actions stay human-approved |
| "Who can switch it off, how fast, and when did you last test that?" | The stop control regulators expect |
| "When a suggestion is wrong, how would you know?" | Whether evidence is reproducible and measured |
| "Do you have past incidents with known causes?" | Whether backtesting is possible |
| "Has this been validated on your own data, not the supplier's?" | External-validity risk |
| "What is the cheapest version: detect only, diagnose, or also act?" | The right first rung |

## 11. Sources

- `ADAMS-TREWS-2022` — Adams et al., *Prospective, multi-site study of patient outcomes after implementation of TREWS*, Nature Medicine, 2022-07-21. https://www.nature.com/articles/s41591-022-01894-0
- `BSI-ISO42001-2026` — BSI, *ISO/IEC 42001: AI Management System* (description), retrieved 2026-10-20. https://www.bsigroup.com/en-GB/products-and-services/standards/iso-42001-ai-management-system/
- `CLOUDOPSBENCH-2026` — *Cloud-OpsBench: a reproducible benchmark for agentic root cause analysis* (preprint), 2026-03. https://arxiv.org/abs/2603.00468
- `DEEPMIND-BCOOLER-2022` — Luo et al., *Controlling Commercial Cooling Systems Using Reinforcement Learning*, 2022-12-15. https://arxiv.org/abs/2211.07357
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `FDA-CDS-2026` — US FDA, *Clinical Decision Support Software: guidance*, 2026-01. https://www.fda.gov/media/109618/download
- `FINTECHFUTURES-DANSKE-2017` — FinTech Futures, *Danske Bank turns to Teradata for AI-powered fraud detection*, 2017-10-23. https://www.fintechfutures.com/ai-in-fintech/danske-bank-turns-to-teradata-for-ai-powered-fraud-detection
- `FRB-SR117-2011` — Federal Reserve and OCC, *SR 11-7: Model Risk Management*, 2011-04-04. https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf
- `GARTNER-AGENTIC-2025` — Gartner, *Over 40% of agentic AI projects will be canceled by end of 2027* (forecast), 2025-06-25. https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- `GODDARD-AB-2012` — Goddard, Roudsari, Wyatt, *Automation bias: a systematic review*, JAMIA, 2012. https://doi.org/10.1136/amiajnl-2011-000089
- `GOOGLE-SREBOOK-2017` — Google, *Site Reliability Engineering*, ch. 6 "Monitoring Distributed Systems", 2017. https://sre.google/sre-book/monitoring-distributed-systems/
- `HENRY-TREWS-2022` — Henry et al., *Factors driving provider adoption of TREWS*, Nature Medicine, 2022-07-21. https://www.nature.com/articles/s41591-022-01895-z
- `META-RCA-2024` — Engineering at Meta, *Leveraging AI for efficient incident response*, 2024-06-24. https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/
- `MSFT-RCACOPILOT-2024` — Chen et al., *Automatic Root Cause Analysis via LLMs for Cloud Incidents* (EuroSys '24), 2024-04. https://arxiv.org/abs/2305.15778
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `NIST-AIRMF-2023` — NIST, *AI Risk Management Framework 1.0 (NIST AI 100-1)*, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `OMB-M2521-2025` — US OMB, *M-25-21: Accelerating federal use of AI*, 2025-04-03. https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf
- `POLY-OVERRIDE-2020` — Poly et al., *Appropriateness of overridden alerts in computerized physician order entry: systematic review*, 2020-07-20. https://doi.org/10.2196/15653
- `SEC-KNIGHT-2013` — US SEC, *In the Matter of Knight Capital Americas LLC* (Release 70694), 2013-10-16. https://www.sec.gov/files/litigation/admin/2013/34-70694.pdf
- `WONG-ESM-2021` — Wong et al., *External Validation of a Widely Implemented Proprietary Sepsis Prediction Model*, JAMA Internal Medicine, 2021-08. https://doi.org/10.1001/jamainternmed.2021.2626
