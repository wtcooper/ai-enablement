# Pattern files: report

Written 2026-10-20. Eleven pattern files written to
`plugins/transformation-advisor/skills/transformation-advisor/references/library/patterns/` (146–160 lines each,
each with a table of contents), and `library/index.md` §3 updated (each pattern id linked to its file; the
"working definitions" sentence replaced; table otherwise unchanged; nothing outside §3 touched).
`python3 scripts/validate.py`: 0 errors (23 pre-existing warnings, all on archetype use-case counts).

## 1. Inputs used per file

| File | Main input | Other inputs used | Archetype check |
|---|---|---|---|
| `intake-triage.md` | `b-patterns-front-door.md` §2.1, §3.1, §4.1 | `b-patterns-continuous.md` (WONG-ESM-2021); EC-2026 from `b-patterns-agents-scale.md` | grep of `pattern: intake-triage`, A/B listed |
| `service-agent-escalation.md` | `b-patterns-front-door.md` §2.2, §3.2, §4.2 | KLGATES-OMNIBUS-2026 from `b-patterns-knowledge.md` | 5 A/B entries exist; all listed |
| `document-to-decision.md` | `b-patterns-transactions.md` §2.1, §3.1, §4.1 | EC-2026 | A/B list re-checked |
| `reconcile-exceptions.md` | `b-patterns-transactions.md` §2.2, §3.2, §4.2 | EC-2026 | A/B list re-checked |
| `research-brief.md` | `b-patterns-knowledge.md` §2.1, §3.1, §4.1 | EC-2026 | A/B list re-checked |
| `grounded-knowledge-assistant.md` | `b-patterns-knowledge.md` §2.2, §3.2, §4.2 | EC-2026 | A/B list re-checked |
| `draft-review-loop.md` | `b-patterns-knowledge.md` §2.3, §3.3, §4.3 | EC-2026 | A/B list re-checked |
| `full-population-testing.md` | `b-patterns-continuous.md` §2.1, §3.1, §4.1 | EC-2026; BSI-ISO42001-2026 from front-door | A/B list re-checked |
| `monitor-diagnose-act.md` | `b-patterns-continuous.md` §2.2, §3.2, §4.2 | EC-2026; BSI-ISO42001-2026 | A/B list re-checked |
| `end-to-end-case-agent.md` | `b-patterns-agents-scale.md` §2.1, §3.1, §4.1, §5 | SIERRA/CRMArena/Klarna from front-door; NIST-SAMPLING from transactions | A/B list re-checked |
| `bulk-transformation.md` | `b-patterns-agents-scale.md` §2.2, §3.2, §4.2, §5 | EC-2026; BSI-ISO42001-2026 | A/B list re-checked |

Every archetype id cited in the files was checked against the use-case YAML (exists; grade as recorded; the
"In the archetypes" ids carry the file's pattern). Every inline key resolves to a §11 source entry and every entry
is cited.

## 2. Conflicts resolved

**Grades re-applied under the 2026-10-17 rule** (a tool test or benchmark is not A for a work outcome; recollections,
user estimates and unnamed organizations are not A):

| Example | Input grade | Grade used | Reason |
|---|---|---|---|
| FCDO correspondence triage (accuracy 0.7333) | A | B | Classifier accuracy on a test, not a work outcome |
| FCDO consular triage (76–81% vs staff) | A | B | Tool test on historic enquiries |
| HMRC digital assistant (83.03% intent accuracy) | A | B | Test-set intent accuracy, not resolution |
| STORM (Stanford) | A | B | Authors evaluating their own prototype |
| ASIC proof of concept | A | B | Tool output scored on a test; not used in work |
| Stanford/Yale legal tools | A | B | Independent tool benchmark |
| NBER customer-support study | A | B | Measured, but the firm is not named |
| UK cross-government Copilot (26 min/day) | A | B | Time figure is a user estimate |
| MGB/Dana-Farber drafts (Lancet) | A | B | Simulation; drafts judged, not a work outcome |
| Meta root-cause ranking (42%) | A | B | Backtest, not production |
| Microsoft RCACopilot (micro-F1 0.766) | A | B | Test-set score |
| Epic Sepsis Model validation | A | B | Validation of a model, not a work outcome |
| University of Kentucky extraction | A | B | Research benchmark on 100 patients |

Kept A where an organization reports a measured work outcome: Taobao field experiment, Copenhagen RCT, DWP
telephony, Klarna month-one figures (estimates flagged), NS&I, Bank of America, BCG experiment, METR RCT, MSR-PENG,
MIT-NOY, Stanford Health Care, UCLA scribes RCT, Google code review, GOV.UK Chat (live pilot scoring), Australian
Treasury evaluation, TREWS, BCOOLER live tests, Knight (failure, regulator), HSBC, DWP advances model, US Treasury,
CMS FPS, Tricorder, Google migrations, Airbnb, Amazon (79% shipped unchanged), Consult DWP evaluation.

**Other conflicts.**
- Klarna 2024 is A in the front-door input and B (adjacent) in the agents-scale input. Used A in `service-agent-escalation.md` and B as an adjacent example in `end-to-end-case-agent.md`.
- Consult appears as B (adjacent, theme coding) in `research-brief.md` and A in `bulk-transformation.md`, where the DWP evaluation is the pattern itself.
- One document, one key across files: EU AI Act (EUAIA-2024, EU-AIACT-ANNEX3/ART12/ART14/ART26, EUR-2024) → `EU-AIACT-2024` (EUR-Lex URL); GDPR → `EU-GDPR-2016`; NIST AI 100-1 → `NIST-AIRMF-2023`; NIST AI 600-1 → `NIST-AI600-2024`; NIST handbook §6.2.1 and §6.2.2 → `NIST-SAMPLING-2026`; τ-bench → `SIERRA-TAUBENCH-2024`; CRMArena-Pro → `SALESFORCE-CRMARENA-2025`; Generative AI at Work → `NBER-BRYNJOLFSSON-2023`; Klarna → `KLARNA-AIASSISTANT-2024` and `ENTREPRENEUR-KLARNA-2025`; Anthropic → `ANTHROPIC-AGENTS-2024`, `ANTHROPIC-MULTIAGENT-2025`; SR 11-7 → `FRB-SR117-2011`; automation-bias review → `GODDARD-AB-2012`; FINRA 2026 report → `FINRA-OVERSIGHT-2026` (dated 2025-12, per the agents-scale input); METR RCT kept as `METR-2025` (same as `method/prioritize.md`), METR time-horizon paper → `METR-HORIZON-2025`; Robodebt → `ROBODEBT-RC-2023`.
- Undated keys: `-n/d` and suffix-less keys given the retrieval year (`OPENAI-MORGANSTANLEY-2026`, `ANTHROPIC-NOVO-2026`, `BLACKLINE-BEAUTYPIE-2026`, `CASESTUDIES-GLOBE-2026`, `ZENML-VENDR-2026`), with "retrieved" noted where the page is undated.
- EU timing: inputs cite mirror pages, a think-tank timeline and law-firm summaries. Files cite the Commission's news item (`EC-2026`: Annex III from 2 December 2027) and, for Art. 50, the K&L Gates summary (2 August 2026).
- Gartner agentic forecast: one input read it only as search-only press coverage; files cite the version read in full (`GARTNER-AGENTIC-2025`).
- Unlabelled design advice in the inputs ("advisor judgment", "advisor inference", "(S)") is marked *(guidance)* in the files.

## 3. Gaps

- No cross-industry grade A example for `document-to-decision`, `reconcile-exceptions` or `end-to-end-case-agent`; the files say so. The best measured reconciliation case is rule-based; end-to-end case agents publish speed figures or none.
- No source publishes, for any of the eleven patterns in production, override rate, escalation rate and error rate together; no silent-error rate after a bulk cutover; no false-match rate for AI reconciliation; no published review sampling plan.
- `service-agent-escalation` has only five A/B archetype entries; the file lists all five.
- ISO/IEC 42001 was not read in any input (paywalled); files cite only the BSI description or secondary Annex A summaries.
- Retail and manufacturing are thin across all patterns (Danfoss, Siemens, BMW, Walmart, Beauty Pie, Konica Minolta: mostly vendor or press figures).
- Several clinical sources are abstract-only (TREWS, Epic Sepsis Model, NEJM AI scribes).
- Delegate-rung evidence outside the archetypes (security, assurance, tax) is announcement-level or anecdote.
- Index §3 "Usual ladder" left unchanged as instructed. The evidence suggests `monitor-diagnose-act` runs at assist/augment in practice (Meta, Microsoft) rather than automate → delegate; worth a later review.

## 4. Archetype use cases tagged `pattern: other` that the inputs suggest should carry a pattern id

All ids checked: they exist and are `pattern: other`. Archetype files were not edited.

| Id (grade) | Suggested pattern | Reason |
|---|---|---|
| `security-human-risk-12` (B) | `document-to-decision` | Identity-document and liveness checks on remote hires; same mechanism as `security-identity-access-19`, already tagged |
| `tax-indirect-tax-22` (D) | `document-to-decision` | Deterministic engine checks each step of an agent's VAT determination: the decision stage as a control. The continuous input suggested `full-population-testing`; `document-to-decision` fits the item better |
| `tax-research-advisory-12` (C) | `document-to-decision` | Model translates rules and facts; deterministic engine computes. Low confidence |
| `tax-compliance-individual-business-10` (D) | `document-to-decision` | Same model-intake, deterministic-calculation split. Low confidence; the front-door input would keep `other` |
| `assurance-soc-attestation-04` (C) | `bulk-transformation` | Mapping controls, commitments and evidence across frameworks; same shape as `security-governance-risk-05` (A, `bulk-transformation`). The transactions input offered `document-to-decision` at low confidence |
| `professional-services-billing-collections-01` (B) | `draft-review-loop` | AI-drafted time entries reviewed and released by the professional |
| `professional-services-knowledge-management-21` (D) | `draft-review-loop` | Idea: AI-drafted stories reviewed by the expert who holds the knowledge |
| `tax-compliance-corporate-21` (C) | `draft-review-loop` | Gated rollout of AI-drafted return work with logging and override and error thresholds. The continuous input suggested `monitor-diagnose-act`; the work itself is drafting, the monitoring is its control |
| `professional-services-knowledge-management-20` (C) | `grounded-knowledge-assistant` | Personas answer colleagues from one person's work product; the corpus owner is an individual |
| `professional-services-staffing-resourcing-21` (D) | `monitor-diagnose-act` | Logs AI staffing recommendations and decisions, tracks overrides, tests disparate impact; same shape as `professional-services-quality-review-11` |
| `security-ai-security-12` (B) | `monitor-diagnose-act` | Agent-action logging tied to a human sponsor; the monitoring layer for agent runs. Weak fit (infrastructure) |
| `professional-services-quality-review-14` (B) | `full-population-testing` | After an AI error, the whole matter or filing set is re-reviewed. Weak fit (a response step, not a standing control) |
| `professional-services-delivery-management-11` (C) | `end-to-end-case-agent` | Matter run from a template with tasks routed to agents and people and named review gates (three inputs agree) |
| `professional-services-delivery-management-14` (B) | `end-to-end-case-agent` | Engagement leads run teams of people and agents; delegate |
| `assurance-controls-testing-18` (B) | `end-to-end-case-agent` | Orchestrated agent swarms alongside internal auditors; multi-step |
| `security-application-security-10` (A) | `end-to-end-case-agent` | Validator-gated agentic testing of running applications; alternatively `monitor-diagnose-act` |
| `tax-compliance-individual-business-09` (C) | `end-to-end-case-agent` | General-purpose agents run taught routines and build return workpapers; delegate |
| `security-ai-security-08` (A) | `intake-triage` (secondary) or keep `other` | Classifier gates agent actions between auto-approve and human approval; triage shape applied to agent actions, not inbound requests |

Considered and left as `other` by the inputs: `tax-data-technology-19`, `tax-indirect-tax-15`,
`assurance-assurance-over-ai-04` (decision logs and audit trails); `security-governance-risk-16`,
`security-application-security-16`; `assurance-quality-management-01`, `-02`, `-11`,
`assurance-planning-risk-assessment-22`, `professional-services-quality-review-01` (governance or resourcing, AI
role unspecified).
