# Pattern: research-brief

Gathers sources, compares them and writes a cited brief; the expert reads the sources behind the key claims. Read
this when an option produces background packs, scans or research memos. Keys in brackets are listed in §11. Lines
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

The AI plans the research, searches wide then narrows, compares sources and drafts a brief in which each claim
points to its source; an expert checks the sources behind the claims that matter. "Cited" does not mean "correct":
in one test only 51.5% of generated sentences were fully supported by their citations [STANFORD-LIU-2023], and
retrieval-grounded legal tools hallucinated on 17% to 33% of 202 queries [STANFORD-LEGAL-2024]. Citation checking
has to be a built step.

**How to recognize it** *(guidance)*: "I spend two days reading before a client call or decision"; "we need a
landscape, competitor or regulatory scan"; "the question needs forty documents read"; "juniors build the background
pack"; "we redo the same scan every quarter".

## 2. Where it fits

- **Work types:** `research-synthesis`, `expert-judgment` (the AI prepares; a person decides).
- **Best fit:** open-ended, breadth-first questions worth the cost. A multi-agent research run uses about 15 times the tokens of a chat [ANTHROPIC-MULTIAGENT-2025].
- **Not when nobody will open the sources**, or the brief goes out unreviewed (Deloitte Australia) [GUARDIAN-DELOITTE-2025].
- **Not for weighing nuanced mixed evidence outside the tool's reliable range.** On such a task, consultants using GPT-4 performed 23% worse than controls [BCG-2023].
- **Not when the brief replaces judgment in a high-risk decision** (EU AI Act Annex III 8(a), Art. 14) [EU-AIACT-2024].
- **Not for a single known fact**, where a search is cheaper [ANTHROPIC-MULTIAGENT-2025].
- **Not where doing the work is how juniors build expertise** (`professional-services-talent-learning-11` measures this for AI drafting).

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Runs research in a chat session | Owns every check | `personal-assistant` | A gold set of past questions with expert-checked answers |
| `augment` | Produces a standard brief from an approved source set, with an enforced citation pass | Opens sources for load-bearing claims; edits | `shared-team-skills`, `workflow-automation` | Unsupported-claim rate measured and within target; logs of sources and plan kept |
| `delegate` | Works a question end to end, or on a schedule, and submits a cited memo | Reviews the memo; samples sources | `background-agent`, `managed-agent-runtime` | Automated citation check plus expert sampling; one archetype entry only, grade C (`tax-research-advisory-03`) |

The usual range is assist to augment. Choose the rung by how cheaply claims can be verified *(guidance)*. Scheduled
briefs on a feed shade into `monitor-diagnose-act`.

## 4. How it is built

- **Inputs.** The question, the allowed source set, the output format and the criteria. Each sub-task needs "an objective, an output format, guidance on the tools and sources to use, and clear task boundaries" [ANTHROPIC-MULTIAGENT-2025].
- **The AI's role.** Plan, search, run parallel sub-tasks, combine the findings, then pass the draft to a separate citation step that finds the location for each claim [ANTHROPIC-MULTIAGENT-2025]. Scale effort by rule: simple fact-finding one agent with 3 to 10 tool calls; comparisons 2 to 4 sub-agents [ANTHROPIC-MULTIAGENT-2025].
- **Human checkpoint.** The expert opens the sources behind key claims. NIST asks organizations to "review and verify sources and citations" before deployment and in monitoring [NIST-AI600-2024].
- **Sampling** *(guidance)*: verify 100% of claims that drive a decision or leave the team; sample the rest, as in acceptance sampling [NIST-SAMPLING-2026]; raise the sample while the unsupported-claim rate is above target.
- **Evaluation.** Start with about 20 real queries, then score factual accuracy, citation accuracy, completeness and source quality; human testers found early agents preferred SEO content farms [ANTHROPIC-MULTIAGENT-2025]. Check that model-based scoring agrees with human scoring before relying on it [HUSAIN-2024].
- **Logging.** Full tracing helped diagnose why agents missed obvious information [ANTHROPIC-MULTIAGENT-2025]; FINRA lists stored prompts, outputs and model versions [FINRA-OVERSIGHT-2026]. Save the sources and plan with each brief, since runs are "non-deterministic between runs" [ANTHROPIC-MULTIAGENT-2025].

## 5. Prerequisites

- **Data and access.** Sources the tool may lawfully read and the user may see; tools that reach where the context lives [ANTHROPIC-MULTIAGENT-2025].
- **Policy.** What may be sent to an external tool; personal-data safeguards and an impact assessment, as GOV.UK did [GDS-GOVUKCHAT-2024].
- **Skills.** Experts who can judge sources; an evaluation set; training. In the UK government trial, users with lower familiarity and confidence reported lower savings [GDS-COPILOT-2025].

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Fabricated or misattributed citations | Nonexistent references in a delivered report [GUARDIAN-DELOITTE-2025]; 31% of 2,709 assistant news answers had a significant sourcing issue [BBC-EBU-2025] | Separate citation step; open every cited source for load-bearing claims; spot-check the rest |
| Confident wrong answers instead of "not found" | Eight search tools together answered over 60% of citation queries incorrectly, rarely signalling doubt [CJR-TOW-2025] | Make "could not find" an allowed output and reward it in evaluation *(guidance)* |
| Weak source selection | SEO farms preferred [ANTHROPIC-MULTIAGENT-2025]; "source bias transfer" [STANFORD-STORM-2024] | Source-quality rules; allow-lists for regulated work |
| Lost nuance | Summaries missed nuance or context [ASIC-AWS-2024] | Expert reads the primary text on contested points |
| Over-trust | Warned consultants still did not challenge wrong output [BCG-2023] | Task-fit map; reviewer forms a view first *(guidance)* |
| Runaway effort and cost | 50 sub-agents spawned for simple queries [ANTHROPIC-MULTIAGENT-2025] | Effort-scaling rules; token budget per brief |

## 7. Value and metrics

- **Levers:** `capacity`, `speed` (hours to a first brief), `quality` (coverage, accuracy), `risk` (missed sources).
- **Published figures:** more than 70% of 7,115 UK civil servants surveyed agreed an assistant reduced time spent searching for information (self-reported) [GDS-COPILOT-2025]; multi-agent research beat a single agent by 90.2% on a vendor's internal evaluation (a benchmark, not a work outcome) [ANTHROPIC-MULTIAGENT-2025].
- **Quality metrics** *(guidance)*: share of claims supported by the cited source (citation precision and recall, as in [STANFORD-LIU-2023]); expert edit or override rate; share of briefs sent back; material errors found after release; time to first usable brief; token cost per brief.
- No source publishes override or escalation rates for a research-brief deployment.

## 8. Governance

- **NIST AI RMF.** Oversight processes "defined, assessed, and documented" (MAP 3.5) [NIST-AIRMF-2023]; confabulated citations "may further mislead humans" [NIST-AI600-2024].
- **EU AI Act.** Annex III 8(a) makes AI that assists a judicial authority in researching and interpreting facts and law high-risk; AI literacy (Art. 4); automation-bias awareness (Art. 14(4)(b)); Art. 50(4) disclosure for AI text published on matters of public interest unless a person holds editorial responsibility [EU-AIACT-2024]. Annex III duties apply from 2 December 2027 [EC-2026].
- **ISO/IEC 42001.** Controls on impact assessment, lifecycle monitoring and use of AI, read through a secondary guide [AIGL-ISO42001-2026].
- **Sector.** FINRA says its supervision, communications and recordkeeping rules apply to generative AI [FINRA-RN2409-2024]. Professional duty: Deloitte Australia repaid the final instalment of a contract [GUARDIAN-DELOITTE-2025].

## 9. Evidence

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| Boston Consulting Group | Professional services | Over 750 consultants did tasks with or without GPT-4 | Outside the tool's range: 23% worse than controls; inside: 40% better; warned users did not challenge wrong output (self-reported, with academics) | A | BCG-2023 |
| ASIC with AWS | Financial regulator | Proof of concept: model summarized public submissions; assessors scored against staff summaries | AI 35 of 75 (47%) vs human 61 (81%); assessors said AI could create more work (self-reported; a test of the tool, not used in work) | B | ASIC-AWS-2024 |
| UK Incubator for AI (Consult) | Public sector | Tool proposes themes for every consultation response; officials review | F1 0.76 vs reviewers; no change for 60% of responses; median 23 seconds a review (self-reported; theme coding is adjacent) | B | IAI-SCOT-2025 |
| Anthropic | Technology | Lead agent plans, sub-agents search in parallel, citation step attributes claims | 90.2% better than single agent on an internal evaluation (vendor-published benchmark) | B | ANTHROPIC-MULTIAGENT-2025 |
| Stanford and Yale researchers | Legal | Preregistered test of three retrieval-based legal research tools on 202 queries | Hallucination 17% to 33%; accurate 65%, 42%, 20% (independent; tool test) | B | STANFORD-LEGAL-2024 |
| Stanford (STORM) | Academia | Prototype asks perspective-guided questions, builds an outline, then writes | Editors rated more articles organized (+25%) and broad (+10%); flagged source bias (authors' own evaluation) | B | STANFORD-STORM-2024 |
| Deloitte Australia | Professional services | Government report produced with generative AI help contained nonexistent references | Final instalment of an A$440,000 contract repaid (independent press; failure case) | B | GUARDIAN-DELOITTE-2025 |

**In the archetypes:** `security-ai-security-18` (A), `tax-research-advisory-02` (B),
`professional-services-pursuit-proposals-08` (B), `professional-services-client-development-06` (B),
`professional-services-acceptance-risk-06` (B), `professional-services-work-production-01` (B),
`security-threat-intelligence-10` (B), `security-incident-response-08` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "Walk me through the last brief. Who reads the sources behind the key claims, and how long does it take?" | Whether review exists and its true cost |
| "Which claims would hurt you if wrong, and which are background?" | The split between full verification and sampling |
| "What may the tool read, and who owns it?" | Access, licensing, confidentiality, and whether an approved source list is possible |
| "Give me ten past briefs whose right answer you now know." | Whether a gold set exists for evaluation |
| "Is the question breadth-first, or one deep judgment?" | Fit; nuanced weighing sits outside the reliable range [BCG-2023] |
| "What does the brief feed: a meeting, a client deliverable, a public document, a regulated decision?" | Risk tier and disclosure duties |
| "What happens today when you cannot find an answer?" | Whether "not found" is acceptable output |
| "How often is the same scan repeated?" | Whether a scheduled brief at a higher rung is justified |

## 11. Sources

- `AIGL-ISO42001-2026` — AI Governance Library, *AIMS Simplified: What ISO 42001 Actually Requires*, 2026-08-31. https://www.aigl.blog/aims-simplified-iso-42001-annex-a-controls-guide/
- `ANTHROPIC-MULTIAGENT-2025` — Anthropic, *How we built our multi-agent research system*, 2025-06-13. https://www.anthropic.com/engineering/multi-agent-research-system
- `ASIC-AWS-2024` — ASIC and AWS, *Gen AI document summarisation proof of concept* (answer to Senate question), 2024-07. https://www.aph.gov.au/DocumentStore.ashx?id=b4fd6043-6626-4cbe-b8ee-a5c7319e94a0&subId=766627
- `BBC-EBU-2025` — BBC and EBU, *News Integrity in AI Assistants*, 2025-10. https://www.bbc.co.uk/aboutthebbc/documents/news-integrity-in-ai-assistants-report.pdf
- `BCG-2023` — Boston Consulting Group, *How people can create, and destroy, value with generative AI*, 2023-09-21. https://www.bcg.com/publications/2023/how-people-create-and-destroy-value-with-gen-ai
- `CJR-TOW-2025` — Tow Center, Columbia Journalism Review, *AI search has a citation problem*, 2025-03. https://www.cjr.org/tow_center/we-compared-eight-ai-search-engines-theyre-all-bad-at-citing-news.php
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `FINRA-OVERSIGHT-2026` — FINRA, *2026 Annual Regulatory Oversight Report: GenAI*, 2025-12. https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai
- `FINRA-RN2409-2024` — FINRA, *Regulatory Notice 24-09: obligations when using generative AI*, 2024-06-27. https://www.finra.org/rules-guidance/notices/24-09
- `GDS-COPILOT-2025` — UK Government Digital Service, *Microsoft 365 Copilot experiment: cross-government findings*, 2025-06-02. https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report/microsoft-365-copilot-experiment-cross-government-findings-report-html
- `GDS-GOVUKCHAT-2024` — UK Government Digital Service, *The findings of our first generative AI experiment: GOV.UK Chat*, 2024-01-18. https://insidegovuk.blog.gov.uk/2024/01/18/the-findings-of-our-first-generative-ai-experiment-gov-uk-chat/
- `GUARDIAN-DELOITTE-2025` — The Guardian, *Deloitte to pay money back after using AI in $440,000 report*, 2025-10-06. https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report
- `HUSAIN-2024` — Hamel Husain, *Your AI product needs evals*, 2024-03-29. https://hamel.dev/blog/posts/evals/
- `IAI-SCOT-2025` — UK Incubator for AI, *Consult evaluation: Scottish Government consultation*, 2025-03-20. https://digitalgovernmenthub.org/wp-content/uploads/2026/02/Scot_Gov_NSCP_Evaluation_Report.pdf
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `NIST-AIRMF-2023` — NIST, *AI Risk Management Framework 1.0 (NIST AI 100-1)*, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `NIST-SAMPLING-2026` — NIST/SEMATECH, *e-Handbook of Statistical Methods* §6.2.1–6.2.2 (acceptance sampling), retrieved 2026-10-20. https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm
- `STANFORD-LEGAL-2024` — Magesh et al., *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, 2024-05-30. https://arxiv.org/abs/2405.20362
- `STANFORD-LIU-2023` — Liu, Zhang, Liang, *Evaluating Verifiability in Generative Search Engines*, 2023-04. https://arxiv.org/abs/2304.09848
- `STANFORD-STORM-2024` — Shao et al., *Assisting in Writing Wikipedia-like Articles From Scratch with LLMs*, 2024-02. https://arxiv.org/abs/2402.14207
