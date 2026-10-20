# Pattern: draft-review-loop

Drafts a deliverable from inputs and templates; a reviewer edits and approves before anything leaves the team.
Read this when an option produces reports, notes, letters, replies or code changes for someone to sign off. Keys in
brackets are listed in §11. Lines marked *(guidance)* are design advice, not findings from a source.

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

The AI produces a first draft from a template, approved text and case facts; sometimes a second pass checks the
first. A named reviewer edits and decides before release. The review is where value is won or lost and it is the
least measured part: reviewers anchor on drafts [LANCET-CHEN-2024], the time saved can fail to appear
[JAMA-GARCIA-2024], and people misjudge their own gains (developers forecast 24% faster and were 19% slower)
[METR-2025]. Design the review and measure it before scaling the draft.

**How to recognize it** *(guidance)*: "first drafts take days and reviewers fix the same things"; "we write the
same report for every client or period"; "the note is written after the meeting from memory"; "the partner
rewrites what the associate drafted".

## 2. Where it fits

- **Work types:** `document-production`, `review-assurance`, `software-systems`.
- **Seen with:** clinical study reports [ANTHROPIC-NOVO-2026]; patient-message replies and visit notes [JAMA-GARCIA-2024; NEJMAI-LUKAC-2025]; client meeting notes and follow-ups [OPENAI-MORGANSTANLEY-2026]; code changes [GOOGLE-CODEREVIEW-2023].
- **Value depends on task fit.** On a task inside the tool's range, consultants did 40% better; outside it, 23% worse [BCG-2023].
- **Not when review volume exceeds reviewer capacity or skill**, so sign-off becomes a stamp *(guidance)*.
- **Not for high-severity content where a reviewer cannot spot the failure** (wrong acuity in drafted patient replies) [LANCET-CHEN-2024].
- **Not where drafting is the learning** for juniors (`professional-services-talent-learning-11`).
- **Not where original or varied thinking is the point**: ideas were 41% less diverse with the tool [BCG-2023].
- **Not without a baseline of time and errors before launch** [METR-2025].

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Drafts in a chat tool on request | Owns the text | `personal-assistant` | Templates and approved text exist; baseline time and error rate measured |
| `augment` | Drafts inside the workflow; draft, edits and final stored together | Reviews every item; mandatory, logged sign-off | `shared-team-skills`, `workflow-automation` | Override rate, edit size and defects found later meet written thresholds per category |
| `automate` | Drafts release for narrow, proven categories | Samples by risk tier | `workflow-automation`, `background-agent` | Tracked error and override rates under threshold for that category (a gated example: `tax-compliance-corporate-21`, C) |
| `delegate` | Agents draft and cross-check each other | Approves at named gates | `managed-agent-runtime` | Evidence that checker models are reliable is thin *(guidance)*; see `assurance-quality-management-18` |

The usual range is assist to augment.

## 4. How it is built

- **Inputs.** A template, approved source text and case facts; Novo Nordisk combines retrieval with "domain expert-approved text and case-specific variables" [ANTHROPIC-NOVO-2026].
- **The AI's role.** A first pass; an evaluator-optimizer loop (one model drafts, another critiques) suits work with clear criteria [ANTHROPIC-AGENTS-2024].
- **Human checkpoint.** A named reviewer decides before release. Morgan Stanley advisers "review and adjust" notes before finalising [OPENAI-MORGANSTANLEY-2026]; in the Stanford pilot clinicians chose to start from the draft or from a blank reply [JAMA-GARCIA-2024].
- **Thresholds.** Google calibrated suggested code edits to 50% target precision and filtered low-confidence ones [GOOGLE-CODEREVIEW-2023]. Officials reviewing AI themes made no change for 60% of responses at a median 23 seconds each [IAI-SCOT-2025].
- **Sampling** *(guidance)*: when moving to sampled review, set sample size and accept or reject limits from an acceptable defect level [NIST-SAMPLING-2026]; tighten when defects appear and relax when they stay low.
- **Logging.** Draft utilization per clinician was the primary outcome in Stanford's pilot [JAMA-GARCIA-2024]; FINRA lists prompt and output logs, model version and human review [FINRA-OVERSIGHT-2026]. Keep draft, edits and final together so override rate and edit size can be computed *(guidance)*.

## 5. Prerequisites

- **Data.** Templates and approved text to draft from; coverage matters, since 25% of messages had no draft in the Stanford pilot [JAMA-GARCIA-2024].
- **Access.** The system where the draft lands (record system, CRM, repository).
- **Policy.** Disclosure and review rules; California's exemption turns on a licensed provider having "read and reviewed" the draft [CALEG-AB3030-2024].
- **Skills.** Reviewers with domain competence and a time budget per item.

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Reviewer anchors on the draft | Physicians judged the draft a risk of severe harm in 7.1% of assessments; assisted replies resembled drafts [LANCET-CHEN-2024] | Severity checklist; reviewer forms a view first *(guidance)* |
| No time saved end to end | No significant change in reply time [JAMA-GARCIA-2024]; summaries could create more work [ASIC-AWS-2024] | Measure time end to end; stop if no gain |
| Perceived gain differs from real gain | Developers believed they were faster and were slower [METR-2025] | Measure; do not rely on self-estimates |
| Over-trust of persuasive output | Warned consultants still accepted wrong output [BCG-2023]; automation bias is "a fairly robust and generic effect" [GODDARD-AB-2012] | Task-fit map; accountability; show confidence [GODDARD-AB-2012] |
| Uniform drafts | 41% less diversity of ideas [BCG-2023] | Keep independent first drafts for judgment-heavy work *(guidance)* |
| Unreviewed drafts shipped | Report with fabricated references delivered to a client [GUARDIAN-DELOITTE-2025] | Named reviewer; pre-issue reference check |
| Low use of drafts | 20% draft utilization [JAMA-GARCIA-2024] | Treat low use as a diagnostic, not a target to force up |
| Skills erosion | Less critical thinking reported with higher confidence in the tool [MSR-LEE-2025] | Unaided skill checks |

## 7. Value and metrics

- **Levers:** `capacity`, `speed`, `quality` (consistency), `experience` (burnout).
- **Typical figures:** one ambient scribe cut time-in-note 9.5% against controls, the other not significantly, in a 238-physician randomized trial [NEJMAI-LUKAC-2025]; developers were 55.8% faster on one controlled task (vendor-affiliated authors) [MSR-PENG-2023]; writing time down 0.8 standard deviations and quality up 0.4 in a writing experiment [MIT-NOY-2023]; 40% to 50% of previewed code-edit suggestions applied [GOOGLE-CODEREVIEW-2023]; Novo Nordisk's director says writing time on study reports fell 90% (a quoted estimate) [ANTHROPIC-NOVO-2026].
- **Quality metrics** *(guidance)*: first-pass acceptance (utilization); edit size; returns from the next reviewer; defects found after release; severe-error catch rate on seeded or sampled drafts; reviewer time per item; zero-edit rate as a rubber-stamp warning.

## 8. Governance

- **NIST.** Automation bias "can exacerbate" confabulation and bias risks [NIST-AI600-2024]; oversight processes defined (MAP 3.5) [NIST-AIRMF-2023].
- **EU AI Act.** Art. 14(4)(b) automation-bias awareness; Art. 6(3) describes cases that may not be high-risk even in Annex III areas, such as improving the language of a drafted document or preparatory tasks; Art. 50(4) editorial-control exemption [EU-AIACT-2024]. Annex III duties apply from 2 December 2027 [EC-2026].
- **ISO/IEC 42001.** Lifecycle monitoring and human oversight controls, via a secondary guide [AIGL-ISO42001-2026].
- **Sector.** California AB 3030 for health communications [CALEG-AB3030-2024]; FINRA supervision, communications and recordkeeping, with summarization and extraction the top generative AI use among member firms [FINRA-RN2409-2024; FINRA-OVERSIGHT-2026].

## 9. Evidence

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| Stanford Health Care | Healthcare | Model drafts replies to patient messages; 162 clinicians, 5 weeks | 20% draft utilization; no significant time change; burden and burnout measures improved (academic, health system) | A | JAMA-GARCIA-2024 |
| UCLA Health | Healthcare | Two ambient scribes draft visit notes; randomized, 238 physicians | Time-in-note -9.5% for one, -1.7% (not significant) for the other; occasional significant inaccuracies (academic; the health system's own researchers) | A | NEJMAI-LUKAC-2025 |
| Google | Technology | Model proposes the edit for each code-review comment | 40% to 50% of previewed suggestions applied (self-reported) | A | GOOGLE-CODEREVIEW-2023 |
| METR | Software (research) | Randomized trial: 16 developers, 246 tasks, AI allowed or not | 19% slower with AI; forecast 24% faster (independent) | A | METR-2025 |
| Microsoft Research, GitHub, MIT | Technology | 95 developers built a server with or without an AI pair programmer | 55.8% faster (vendor-affiliated) | A | MSR-PENG-2023 |
| MIT researchers | Professional writing | 444 professionals did writing tasks, half with the tool | Time -0.8 SD; quality +0.4 SD (independent) | A | MIT-NOY-2023 |
| Mass General Brigham, Dana-Farber | Healthcare | Six oncologists edited model drafts for 100 simulated patient messages | Drafts judged a severe-harm risk in 7.1% of assessments (11 of 156); replies converged on drafts (independent; simulation) | B | LANCET-CHEN-2024 |
| Novo Nordisk | Pharmaceuticals | Platform drafts clinical study reports from approved text; people review | Director says writing time cut 90%; no error rates (vendor-published quotation) | B | ANTHROPIC-NOVO-2026 |
| Morgan Stanley | Financial services | Meeting recordings become CRM notes and draft follow-ups advisers refine | Follow-ups "days" to "hours", per an executive; no figures (vendor-published) | B | OPENAI-MORGANSTANLEY-2026 |

**In the archetypes:** `professional-services-work-production-06` (A), `professional-services-work-production-07` (A),
`professional-services-talent-learning-11` (A), `security-application-security-04` (A),
`security-incident-response-14` (A), `security-operations-15` (A), `assurance-quality-management-18` (B),
`assurance-controls-testing-01` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "Who signs off, what do they check, and how much time do they have per item?" | Whether review is real or a stamp |
| "What is the worst error that could pass review, and would the reviewer see it?" | Severity and anchoring risk |
| "How long does the whole task take now, including checking?" | A baseline; perceived and measured effects can disagree |
| "What share of drafts are used as is, edited or discarded?" | Utilization or override rate as the main quality metric |
| "Does the reviewer form a view before seeing the draft?" | Anchoring and automation-bias exposure |
| "Which category could move to sampled review, and what error rate would you accept?" | Whether thresholds can be written down for `automate` |
| "Who learns from drafting today, and what replaces that?" | Skills erosion and junior-role effects |
| "Where are the draft, the edits and the final stored?" | Whether override and edit metrics and an audit trail are possible |

## 11. Sources

- `AIGL-ISO42001-2026` — AI Governance Library, *AIMS Simplified: What ISO 42001 Actually Requires*, 2026-08-31. https://www.aigl.blog/aims-simplified-iso-42001-annex-a-controls-guide/
- `ANTHROPIC-AGENTS-2024` — Anthropic, *Building effective agents*, 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents
- `ANTHROPIC-NOVO-2026` — Anthropic, *Novo Nordisk accelerates clinical documentation with Claude* (customer story, undated), retrieved 2026-10-20. https://claude.com/customers/novo-nordisk
- `ASIC-AWS-2024` — ASIC and AWS, *Gen AI document summarisation proof of concept* (answer to Senate question), 2024-07. https://www.aph.gov.au/DocumentStore.ashx?id=b4fd6043-6626-4cbe-b8ee-a5c7319e94a0&subId=766627
- `BCG-2023` — Boston Consulting Group, *How people can create, and destroy, value with generative AI*, 2023-09-21. https://www.bcg.com/publications/2023/how-people-create-and-destroy-value-with-gen-ai
- `CALEG-AB3030-2024` — California Legislature, *AB 3030, Health and Safety Code s.1339.75*, 2024. https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202320240AB3030
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `FINRA-OVERSIGHT-2026` — FINRA, *2026 Annual Regulatory Oversight Report: GenAI*, 2025-12. https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
- `FINRA-RN2409-2024` — FINRA, *Regulatory Notice 24-09: obligations when using generative AI*, 2024-06-27. https://www.finra.org/rules-guidance/notices/24-09
- `GODDARD-AB-2012` — Goddard, Roudsari, Wyatt, *Automation bias: a systematic review*, JAMIA, 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3240751/
- `GOOGLE-CODEREVIEW-2023` — Google Research, *Resolving code review comments with ML*, 2023-05-23. https://research.google/blog/resolving-code-review-comments-with-ml/
- `GUARDIAN-DELOITTE-2025` — The Guardian, *Deloitte to pay money back after using AI in $440,000 report*, 2025-10-06. https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report
- `IAI-SCOT-2025` — UK Incubator for AI, *Consult evaluation: Scottish Government consultation*, 2025-03-20. https://digitalgovernmenthub.org/wp-content/uploads/2026/02/Scot_Gov_NSCP_Evaluation_Report.pdf
- `JAMA-GARCIA-2024` — Garcia et al., *AI-Generated Draft Replies to Patient Inbox Messages*, JAMA Network Open, 2024-03-04. https://pmc.ncbi.nlm.nih.gov/articles/PMC10955355/
- `LANCET-CHEN-2024` — Chen et al., *The effect of using a large language model to respond to patient messages*, Lancet Digital Health, 2024-04-24. https://pmc.ncbi.nlm.nih.gov/articles/PMC11829255/
- `METR-2025` — METR, *Impact of early-2025 AI on experienced open-source developer productivity*, 2025-07. https://arxiv.org/abs/2507.09089
- `MIT-NOY-2023` — Noy and Zhang, *Experimental evidence on the productivity effects of generative AI*, 2023-03-02. https://economics.mit.edu/sites/default/files/inline-files/Noy_Zhang_1.pdf
- `MSR-LEE-2025` — Lee et al., *The Impact of Generative AI on Critical Thinking* (CHI '25), 2025-04. https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf
- `MSR-PENG-2023` — Peng et al., *The Impact of AI on Developer Productivity: Evidence from GitHub Copilot*, 2023-02-13. https://arxiv.org/abs/2302.06590
- `NEJMAI-LUKAC-2025` — Lukac et al., *Ambient AI Scribes in Clinical Practice: A Randomized Trial*, NEJM AI, 2025-11-26. https://europepmc.org/article/MED/41497288
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `NIST-AIRMF-2023` — NIST, *AI Risk Management Framework 1.0 (NIST AI 100-1)*, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `NIST-SAMPLING-2026` — NIST/SEMATECH, *e-Handbook of Statistical Methods* §6.2.1–6.2.2 (acceptance sampling), retrieved 2026-10-20. https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm
- `OPENAI-MORGANSTANLEY-2026` — OpenAI, *Morgan Stanley uses AI evals to shape the future of financial services* (customer story, undated), retrieved 2026-10-20. https://openai.com/index/morgan-stanley/
