# Pattern: grounded-knowledge-assistant

Answers questions from an approved body of knowledge, with citations; content owners keep the knowledge current.
Read this when an option helps people find answers that already exist in documents. Keys in brackets are listed in
§11. Lines marked *(guidance)* are design advice, not findings from a source.

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

The assistant retrieves passages from a curated, permissioned corpus, answers, cites the passage, and declines
when the question is outside scope. Retrieval carries the load: seven failure points were reported across three
case studies, from missing content to incomplete answers [DEAKIN-BARNETT-2024]. Where it works, owners measure
accuracy against expert-scored samples and keep measuring: GOV.UK Chat reports accuracy rising from 76% to 90% over
18 months [GDS-GOVUKCHAT-2026A]. When the audience is the public or clients and the assistant hands off to people,
the work becomes `service-agent-escalation` *(guidance)*.

**How to recognize it** *(guidance)*: "people keep asking the same questions and the answers are in documents
nobody can find"; "new joiners ask seniors"; "the policy manual is 400 pages"; "we answer security questionnaires
from last year's answers"; "technicians search manuals on the shop floor".

## 2. Where it fits

- **Work types:** `client-interaction`, `research-synthesis`, `expert-judgment`, `physical-field`.
- **Seen with:** advisers querying the firm's research [OPENAI-MORGANSTANLEY-2026]; citizens querying government guidance [GDS-GOVUKCHAT-2026A]; support agents served documentation links [NBER-BRYNJOLFSSON-2023].
- **Not public-facing on rules without measured accuracy** (MyCity, Air Canada) [MARKUP-MYCITY-2024; GUARDIAN-AIRCANADA-2024].
- **Not over a corpus nobody owns, or with permissions nobody cleaned** [GDS-COPILOT-2025].
- **Not for questions needing personal case data the assistant cannot see**; GOV.UK pilot users wanted an adviser with their information [GDS-GOVUKCHAT-2026A].
- **Not when the answer is a legal or clinical decision nobody will verify** [STANFORD-LEGAL-2024; NIST-AI600-2024].
- **Not in place of the learning path of juniors** who need their own judgment (`professional-services-knowledge-management-19`) [MSR-LEE-2025].

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Answers staff questions from an approved corpus with cited passages | Checks the passage; decides | `personal-assistant`, `shared-team-skills` | Corpus owner and review dates; gold set of questions with expert answers |
| `augment` | Places answers inside the work step (suggested replies, precedent retrieval) | Uses, edits or declines each answer | `shared-team-skills`, `workflow-automation` | Expert-scored accuracy on a held-out set; adherence or override rate tracked |
| `automate` | Releases answers without a person when confident; routes uncertain ones to an analyst (`security-governance-risk-01`) | Answers routed questions; samples released ones | `workflow-automation`, `managed-agent-runtime` | Refusal rule, live monitoring and an owner for every corpus; measured accuracy before wider release |

The usual rung is assist. GOV.UK Chat moved from a 2023 prototype to public pilots, and in March 2026 GDS said it
would open access more widely, starting with all users of the GOV.UK app [GDS-GOVUKCHAT-2026A].

## 4. How it is built

- **Inputs.** A curated corpus with owners, dates and permissions. GOV.UK Chat draws "exclusively" on published guidance and counts an answer accurate only if it meets all the standards of that content [GDS-GOVUKCHAT-2026A]. Retrieval that follows the user's permissions can expose over-shared files [GDS-COPILOT-2025].
- **The AI's role.** Retrieve, answer, cite, and decline outside scope [GDS-GOVUKCHAT-2026A]. Errors in legal tools traced to naive retrieval, inapplicable authority, sycophancy and reasoning errors [STANFORD-LEGAL-2024].
- **Human checkpoints.** Content owners approve what enters the corpus and retire what is stale; users check the cited source; an analyst takes uncertain answers when automated.
- **Thresholds and sampling.** GOV.UK manually reviewed 419 conversations and 1,084 question-answer pairs in one pilot, with automated scoring [GDS-GOVUKCHAT-2026A]; Morgan Stanley runs a daily regression suite [OPENAI-MORGANSTANLEY-2026]; a support tool gave no suggestion when it lacked training data, an abstain threshold [NBER-BRYNJOLFSSON-2023].
- **Logging.** Automated live monitoring flags issues for human review [GDS-GOVUKCHAT-2026B]; FINRA lists stored prompts and outputs, model-version tracking and regular error checks [FINRA-OVERSIGHT-2026].

## 5. Prerequisites

- **Data.** An owned, current, permissioned corpus. Morgan Stanley moved from 7,000 answerable questions to a 100,000-document corpus through retrieval tuning [OPENAI-MORGANSTANLEY-2026].
- **Access.** Identity-aware retrieval; permissions fixed before indexing.
- **Policy.** The kinds of queries the assistant should refuse [NIST-AI600-2024]; disclosure and a route to a person.
- **Skills.** Content curation, evaluation design and a channel for user feedback.

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Wrong or invented answers despite retrieval | 17% to 33% hallucination across legal research tools [STANFORD-LEGAL-2024] | Gold-set testing before launch; scope limits; abstain rule |
| Illegal or harmful advice from a public bot | MyCity said employers could take workers' tips [MARKUP-MYCITY-2024]; it was later slated for removal [MARKUP-MYCITY-2026] | Narrow scope; live monitoring; named owner; disclaimers are not a control *(guidance)* |
| Inconsistent answers | The same housing question got "yes" once and "no" ten times [MARKUP-MYCITY-2024] | Test repeats; log and compare answers |
| Organization held to what the bot said | Tribunal ordered Air Canada to pay after a wrong fare answer [GUARDIAN-AIRCANADA-2024] | Treat bot output as published policy; one source of truth |
| Stale or unapproved content | Users over-trust a trusted brand [GDS-GOVUKCHAT-2024] | Content owner and review date per document |
| Over-exposure of files | Retrieval surfaces files users should not have had [GDS-COPILOT-2025] | Fix permissions before indexing |
| Cannot show which document was used | Agents "struggled to identify the exact documents" [GDS-COPILOT-2025] | Require source passages in every answer |
| Low take-up | Agents followed suggestions 38% of the time [NBER-BRYNJOLFSSON-2023] | Treat adherence as a quality signal; study declined answers |

## 7. Value and metrics

- **Levers:** `capacity`, `speed`, `quality`, `experience`, `risk`.
- **Typical figures:** support agents resolved 14% more issues an hour, 34% for novice and low-skilled agents (5,179 agents; independent academic study of an unnamed firm) [NBER-BRYNJOLFSSON-2023]; GOV.UK Chat 90% accuracy, 88% in-scope answer rate, 73% of app survey respondents found it useful (self-reported) [GDS-GOVUKCHAT-2026A]; Australian Treasury found lower-than-expected use and no clear evidence of improved work outcomes in a 14-week trial [ACE-TREASURY-2025].
- **Quality metrics** *(guidance)*: expert-scored accuracy on a held-out set; in-scope answer rate; share of answers with a valid citation; escalation rate; stale-document share; adherence or override rate; repeat-question consistency.

## 8. Governance

- **NIST.** Confabulation and automation bias are named generative AI risks; verify that retrieval data are grounded (MS-2.5-005) [NIST-AI600-2024].
- **EU AI Act.** Tell users they are interacting with AI unless obvious (Art. 50(1)); AI literacy (Art. 4) [EU-AIACT-2024]. An answer assistant is not in Annex III by itself; use in essential services, employment or justice may be *(guidance)*. Annex III duties apply from 2 December 2027 [EC-2026].
- **ISO/IEC 42001.** Impact assessment, operational monitoring and use-of-AI controls, via a secondary guide [AIGL-ISO42001-2026].
- **Sector.** FINRA's communications, supervision and recordkeeping rules apply [FINRA-RN2409-2024]; California requires a disclaimer and a route to a human on AI-generated patient clinical communications unless a licensed provider has read and reviewed them [CALEG-AB3030-2024]; tribunal liability [GUARDIAN-AIRCANADA-2024].

## 9. Evidence

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| UK Government Digital Service | Public sector | GOV.UK Chat answers citizens only from published guidance | Accuracy 76% to 90% by expert plus automated scoring; 508 jailbreak attempts blocked; over 10,000 users (self-reported) | A | GDS-GOVUKCHAT-2026A |
| Australian Treasury | Public sector | 218 staff used a retrieval-grounded assistant for 14 weeks | Use lower than expected; clearest benefit in admin tasks; no clear outcome gain (internal evaluation) | A | ACE-TREASURY-2025 |
| Unnamed Fortune 500 software firm | Technology | Suggested replies and documentation links shown to support agents | Issues resolved per hour +14%, +34% for novices; 38% adherence (independent academics; firm not named) | B | NBER-BRYNJOLFSSON-2023 |
| Twelve UK government organizations | Public sector | 20,000 staff used an assistant that retrieves with their permissions | 26 minutes a day saved by user estimate; 17% saw no clear saving (self-reported survey) | B | GDS-COPILOT-2025 |
| Morgan Stanley | Financial services | Advisers query the firm's knowledge base; daily regression suite | "Over 98% of advisor teams" use it; document access measure undefined (vendor-published) | B | OPENAI-MORGANSTANLEY-2026 |
| Stanford and Yale researchers | Legal | Test of three retrieval-based legal research tools | Accurate on 65%, 42% and 20% of queries (independent; tool test) | B | STANFORD-LEGAL-2024 |
| City of New York | Public sector | MyCity chatbot for business rules | Wrong answers in press testing; later narrowed, then slated for removal (independent) | B | MARKUP-MYCITY-2026 |
| Air Canada | Aviation | Website chatbot misstated bereavement-fare rules | Tribunal ordered the airline to pay (independent) | B | GUARDIAN-AIRCANADA-2024 |
| Siemens | Manufacturing | Assistant for maintenance staff | 25% reactive maintenance time saved in "first pilot use cases"; method not given (vendor-published) | C | SIEMENS-COPILOT-2025 |

**In the archetypes:** `security-governance-risk-01` (A), `security-operations-02` (A), `security-operations-12` (A),
`tax-indirect-tax-06` (A), `professional-services-knowledge-management-01` (B),
`professional-services-knowledge-management-03` (B), `assurance-quality-management-12` (B), `tax-controversy-20` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "Which document is the single source of truth for this answer, and who owns it?" | Content ownership and stale-content risk |
| "Show me five answers staff gave last month that were wrong or out of date." | Real error classes and a seed for the gold set |
| "Who asks, and who bears the cost of a wrong answer?" | Audience risk; public answers become published policy |
| "What should it refuse, and where does the person go instead?" | Scope and handoff design |
| "Are document permissions clean?" | Over-sharing risk when retrieval follows user access |
| "How will you score accuracy, how often, and with whom?" | Whether an evaluation plan exists |
| "What share of suggestions do people use, and why do they decline the rest?" | Adherence as a quality signal |
| "Is this really a client-facing agent?" | Whether the work belongs to `service-agent-escalation` |

## 11. Sources

- `ACE-TREASURY-2025` — Australian Centre for Evaluation, *Evaluation of a trial of generative AI in the Department of the Treasury*, 2025-02. https://evaluation.treasury.gov.au/sites/evaluation.treasury.gov.au/files/2025-02/evaluation-generative-artificial-intelligence-summary.pdf
- `AIGL-ISO42001-2026` — AI Governance Library, *AIMS Simplified: What ISO 42001 Actually Requires*, 2026-08-31. https://www.aigl.blog/aims-simplified-iso-42001-annex-a-controls-guide/
- `CALEG-AB3030-2024` — California Legislature, *AB 3030, Health and Safety Code s.1339.75*, 2024. https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB3030
- `DEAKIN-BARNETT-2024` — Barnett et al., *Seven Failure Points When Engineering a Retrieval Augmented Generation System*, 2024-01-11. https://arxiv.org/abs/2401.05856
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `FINRA-OVERSIGHT-2026` — FINRA, *2026 Annual Regulatory Oversight Report: GenAI*, 2025-12. https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
- `FINRA-RN2409-2024` — FINRA, *Regulatory Notice 24-09*, 2024-06-27. https://www.finra.org/rules-guidance/notices/24-09
- `GDS-COPILOT-2025` — UK Government Digital Service, *Microsoft 365 Copilot experiment: cross-government findings*, 2025-06-02. https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report/microsoft-365-copilot-experiment-cross-government-findings-report-html
- `GDS-GOVUKCHAT-2024` — UK Government Digital Service, *The findings of our first generative AI experiment: GOV.UK Chat*, 2024-01-18. https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/
- `GDS-GOVUKCHAT-2026A` — UK Government Digital Service, *5 things we learned testing GOV.UK Chat*, 2026-03-16. https://insidegovuk.blog.gov.uk/2026/03/16/5-things-we-learned-testing-gov-uk-chat-an-ai-assistant-for-government/
- `GDS-GOVUKCHAT-2026B` — UK Government Digital Service, *Developing GOV.UK Chat: our data science and AI engineering journey*, 2026-05-15. https://insidegovuk.blog.gov.uk/2026/05/15/developing-gov-uk-chat-our-data-science-and-ai-engineering-journey/
- `GUARDIAN-AIRCANADA-2024` — The Guardian, *Air Canada ordered to pay customer who was misled by airline's chatbot*, 2024-02-16. https://www.theguardian.com/world/2024/feb/16/air-canada-chatbot-lawsuit
- `MARKUP-MYCITY-2024` — The Markup, *NYC's AI Chatbot Tells Businesses to Break the Law*, 2024-03-29. https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law
- `MARKUP-MYCITY-2026` — The Markup, *Mamdani to kill the NYC AI chatbot*, 2026-01-30. https://themarkup.org/artificial-intelligence/2026/01/30/mamdani-to-kill-the-nyc-ai-chatbot-we-caught-telling-businesses-to-break-the-law
- `MSR-LEE-2025` — Lee et al., *The Impact of Generative AI on Critical Thinking* (CHI '25), 2025-04. https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf
- `NBER-BRYNJOLFSSON-2023` — Brynjolfsson, Li, Raymond, *Generative AI at Work* (NBER w31161), 2023-11. https://www.nber.org/papers/w31161
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-MORGANSTANLEY-2026` — OpenAI, *Morgan Stanley uses AI evals to shape the future of financial services* (customer story, undated), retrieved 2026-10-20. https://openai.com/index/morgan-stanley/
- `SIEMENS-COPILOT-2025` — Siemens, *Siemens expands Industrial Copilot with maintenance offering*, 2025-03-24. https://press.siemens.com/global/en/pressrelease/siemens-expands-industrial-copilot-new-generative-ai-powered-maintenance-offering
- `STANFORD-LEGAL-2024` — Magesh et al., *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, 2024-05-30. https://arxiv.org/abs/2405.20362
