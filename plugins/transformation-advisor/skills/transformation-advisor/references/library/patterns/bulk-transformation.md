# Pattern: bulk-transformation

Converts, migrates or rewrites large volumes of content, data or code, with sampled quality checks and sign-off
before cutover. Read this when an option clears a backlog of many similar conversions. Keys in brackets are listed
in §11. Lines marked *(guidance)* are design advice, not findings from a source.

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

A pipeline finds the items to change, has a model generate each conversion, checks every output with a deterministic
validator (tests, type checks, schema checks or a gold set), retries or repairs failures, and sends the rest and a
sample to people before cutover. Public results are good only where such a validator sits next to the model: Google
states the model's role "is focused on the edit generation", with locating and validating changes done mostly by
deterministic techniques [GOOGLE-2025]. Without validators, correct code translations ranged from 2.1% to 47.3%
across models in one study [IBM-2024]. Public evidence for it is stronger than for `end-to-end-case-agent`, but no
source reports a rate of silent errors found after cutover.

**How to recognize it** *(guidance)*: "we have thousands of files, records or documents to move, reformat, reclassify or
upgrade"; "this has sat on the backlog for years"; "every team has to make the same change". Google completed
migrations that had stalled for several years [GOOGLE-2025].

## 2. Where it fits

- **Work types:** `software-systems`, `document-production`, `data-reporting`.
- **Seen with:** code migrations [GOOGLE-2025; AIRBNB-2025; AMAZON-2024]; product catalogue data [RETAILDIVE-2024; AMAZON-2025]; free text into structured data [IAI-DWP-2025; UKY-2025].
- **Best fit:** a repeated, well-defined transformation with many instances, a checkable result and a large baseline cost [GOOGLE-2025; AIRBNB-2025].
- **Not with a general chat model and no validators on a many-file migration** [IBM-2024; GOOGLE-2025].
- **Not where equivalence is a judgment, not a test, without domain review** [GOOGLE-2025].
- **Not with savings claimed against an inflated manual baseline** [PRAGMATIC-2026].
- **Not with a cutover sample too small to find rare errors, or more output than reviewers can absorb** [GOOGLE-2025].
- **Not when the "data cleaning" actually changes decisions about people**, such as bulk re-scoring of individuals *(guidance)*; profiling is always high-risk under the EU AI Act [EU-AIACT-2024].

## 3. Up the ladder

| Rung | What the AI does | What the person does | Runtime class | Checkpoint before moving up |
|---|---|---|---|---|
| `assist` | Converts one item on request | Checks and applies it | `personal-assistant` | A target specification and worked examples |
| `augment` | Drafts each conversion | Reviews every output (Consult reviewers took a median 23 seconds a response [IAI-SCOT-2025]) | `shared-team-skills`, `workflow-automation` | A validator the team trusts; model-vs-reviewer agreement compared with reviewer-vs-reviewer |
| `automate` | Per-item pipeline with validators, retries and a capped number of attempts | Handles failures; samples results; signs off cutover | `workflow-automation`, `background-agent` | Acceptance sample with a stop rule [NIST-SAMPLING-2026] *(guidance)*; rollback path |
| `delegate` | Owns the campaign: finds locations, edits, repairs, shards changes to owners | Expert checks before sharding; owners review; a person lands and rolls out | `managed-agent-runtime` | Review capacity matched to output; gradual rollout [GOOGLE-2025] |

## 4. How it is built

- **Inputs.** The source population, the target specification, worked examples and validation tooling. Airbnb's prompts grew to 40,000-100,000 tokens with up to 50 related files; choosing the right related files mattered more than prompt wording [AIRBNB-2025].
- **The AI's role.** Generate edits; deterministic analysis finds change sites and validates results; failed validations can trigger a repair step [GOOGLE-2025].
- **Human checkpoints.** Google reviews generated code like any other change, and landing and rollout "still require a human operator" [GOOGLE-2025]; Airbnb finished the last ~3% of files by hand [AIRBNB-2025].
- **Thresholds.** Airbnb capped retries per step, tuned on 5-10 failing files at a time ("sample, tune, sweep"), and stopped automating files retried 50-100 times [AIRBNB-2025]. Google limited weekly output so reviewers were not overwhelmed [GOOGLE-2025].
- **Sampling.** For data, Kentucky benchmarked against 100 expert-annotated patients; its manual baseline used a 10% independent quality check [UKY-2025]. Tuning samples are not acceptance samples *(guidance)*.
- **Logging.** Airbnb stamped each file with the status of each step and allowed re-runs by stuck step [AIRBNB-2025]; Google measured AI-authored share by comparing the first generated version with the committed one [GOOGLE-2025].

## 5. Prerequisites

- **Data.** An expert-annotated gold set and an agreed definition; Kentucky found billing codes selected patients of whom only 51% truly had the condition [UKY-2025].
- **Access.** A campaign tool that can re-run subsets; a gradual rollout and rollback path [GOOGLE-2025].
- **Policy.** An honestly stated baseline: Asana's $6 million manual estimate was a back-of-envelope figure (time per file times file count), as its developer-productivity lead described it to the newsletter [PRAGMATIC-2026].
- **Skills.** Reviewers with capacity and ownership; people who define rules and build validators. One engineer could generate all the changes in Google's ID migration, cutting coordination overhead [GOOGLE-2025].

## 6. Failure modes and controls

| Failure | How it shows up | Control that catches it |
|---|---|---|
| Silent semantic errors | Changes compile and pass weak tests; 15 categories of translation bug [IBM-2024] | Stronger tests; expert review for semantically risky classes; staged rollout |
| Plain prompting fails | "Not sufficient for anything but the simplest of migrations" [GOOGLE-2025] | Combine deterministic analysis, model edits and validation |
| Review becomes the throttle | Output piles up awaiting review [GOOGLE-2025] | Shard to code owners; cap weekly output |
| Reviewers revert parts of changes | "In most cases, the human needed to revert at least some changes" [GOOGLE-2025] | Expert pre-check before sharding |
| Long tail | ~3% left after 50-100 retries [AIRBNB-2025] | Tune breadth-first, then finish by hand |
| Gold standard itself wrong | Some model "errors" were gold-set errors [UKY-2025]; reviewers disagreed on 40% of exact mappings in an earlier test [IAI-SCOT-2025] | Compare model-vs-reviewer with reviewer-vs-reviewer agreement (0.816 vs 0.710 F1 [IAI-DWP-2025]) |
| Hidden bias by group | Performance differs across groups | Test subgroups first (no difference by disability status in [IAI-DWP-2025]) |

## 7. Value and metrics

- **Levers:** `capacity`, `cost`, `speed`, `quality`, `risk`.
- **Typical figures:** Airbnb automated 97% of ~3,500 test files (75% in 4 hours, the rest after four more days of tuning) and finished in 6 weeks against a 1.5-year manual estimate [AIRBNB-2025]; Google ~87% of generated code committed unchanged in one migration and 80% of landed changes fully AI-authored in another; time savings of ~50% are engineer estimates [GOOGLE-2025]; Amazon 79% of generated code reviews shipped without changes; developer-years and dollar savings are estimates [AMAZON-2024]; Consult reviewers changed nothing for 73% of 87,738 responses [IAI-DWP-2025].
- **Measure end to end.** Count time to find locations, review and roll out, not code-generation speed alone [GOOGLE-2025].
- **Quality metrics:** share accepted unchanged; validator pass rate; model-vs-reviewer agreement; errors found in the cutover sample; *(guidance)* errors found after cutover, which no source yet publishes.

## 8. Governance

- **NIST AI RMF.** MANAGE 2.4 (disengage on inconsistent performance) [NIST-AIRMF-2023]; confabulation and information integrity for generated records and code [NIST-AI600-2024].
- **EU AI Act.** Many internal conversions will not be high-risk; Art. 6(3) lets a provider document that a narrow procedural or preparatory task is not high-risk, but profiling of natural persons always is [EU-AIACT-2024]. Whether a given job is in scope is a legal question to check. Annex III duties apply from 2 December 2027 [EC-2026].
- **ISO/IEC 42001.** An organization-level, certifiable management system [BSI-ISO42001-2026].
- **Software supply chain.** Quality stays assured by the normal review process; Google says the long-term effect on quality "remains to be seen" [GOOGLE-2025].
- **Personal data.** Data-protection duties apply when converting personal records such as patient notes; sector texts were not reviewed here.

## 9. Evidence

| Organization | Industry | What changed | Outcome (provenance) | Grade | Source |
|---|---|---|---|---|---|
| Google | Technology | Toolkit for repo-wide migrations: deterministic location finding, model edits, tests, human review | ~87% of code committed unchanged (JUnit, 5,359 files in 3 months); 80% of ID-migration changes fully AI-authored (self-reported) | A | GOOGLE-2025 |
| Airbnb | Travel marketplace | ~3,500 test files migrated by a per-file pipeline with retries | 75% in 4 hours; 97% after 4 more days; rest by hand in a week (self-reported, tracked) | A | AIRBNB-2025 |
| Amazon | Technology, retail | Automated Java upgrades across internal systems | 79% of generated reviews shipped unchanged; over half of production Java systems upgraded in under six months (self-reported; Amazon also sells the tool) | A | AMAZON-2024 |
| UK Incubator for AI (Consult) | Public sector | Themes generated for 87,738 consultation responses; 125 reviewers checked | No change for 73%; F1 0.816 model vs reviewer, 0.710 reviewer vs reviewer (self-reported by the builders) | A | IAI-DWP-2025 |
| University of Kentucky | Healthcare research | Local model extracts structured fields from clinical notes | Over 82% agreement on all but one field, 100-patient benchmark (research study; tool test) | B | UKY-2025 |
| UK Incubator for AI (Extract) | Public sector | Old planning documents converted into usable data for councils | 2 minutes per document in "early testing" (self-reported) | B | IAI-PLANNING-2026 |
| Walmart | Retail | Models create or improve product-catalogue data | Over 850 million data points; no quality metric (executives via press) | B | RETAILDIVE-2024 |
| Amazon Stores | Retail | Models check and correct catalogue attributes | "Thousands of hours" of review saved; no error rates (self-reported) | B | AMAZON-2025 |
| Nubank | Banking | Coding agent splits an 8-year-old ETL monolith; humans approve | 8-12x engineering efficiency, figures inconsistent on the page (vendor-published) | C | COGNITION-2024 |
| Asana | Software | Test framework replaced with a coding agent | ~$12K cost vs a ~$6M plan; the plan was a back-of-envelope estimate (vendor account; baseline contested) | C | PRAGMATIC-2026 |

**In the archetypes:** `security-data-privacy-02` (A), `security-governance-risk-05` (A),
`security-vulnerability-exposure-13` (A), `tax-indirect-tax-01` (A), `security-data-privacy-01` (B),
`security-threat-intelligence-05` (B), `professional-services-knowledge-management-05` (B),
`assurance-planning-risk-assessment-07` (B).

## 10. Probes

| Ask | What the answer reveals |
|---|---|
| "How many items, how many kinds, and how long would the manual route take, by whose estimate?" | Scale and an honest baseline |
| "How would you know a converted item is right without a person reading it?" | Whether a validator exists; without one, augment at best |
| "Which items look right after conversion but could behave differently?" | Semantically risky classes for expert review |
| "Who reviews, who owns each part, and how many changes can they absorb a week?" | Review capacity |
| "What happens to the last 3% to 25%?" | The long-tail plan |
| "What sample will you check before cutover, and what error rate stops it?" | Turns "sampled checks" into numbers |
| "Is your gold standard itself reliable?" | Whether reviewer-vs-reviewer agreement must be measured |
| "Can it be rolled out gradually and rolled back?" | Cutover risk |

## 11. Sources

- `AIRBNB-2025` — Airbnb Engineering, *Accelerating large-scale test migration with LLMs*, 2025-03. https://airbnb.tech/uncategorized/accelerating-large-scale-test-migration-with-llms/
- `AMAZON-2024` — Amazon (A. Jassy, post on Amazon Q code transformation), 2024-08-22. https://x.com/ajassy/status/1826608791741493281
- `AMAZON-2025` — Amazon Science, *Using LLMs to improve Amazon product listings*, 2025-11-28. https://www.amazon.science/blog/using-llms-to-improve-amazon-product-listings
- `BSI-ISO42001-2026` — BSI, *ISO/IEC 42001: AI Management System* (description), retrieved 2026-10-20. https://www.bsigroup.com/en-GB/products-and-services/standards/iso-42001-ai-management-system/
- `COGNITION-2024` — Cognition, *How Nubank refactors millions of lines of code with Devin*, 2024-11-14. https://devin.ai/customers/nubank
- `EC-2026` — European Commission, *AI Omnibus enters into force*, 2026-07-27. https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force
- `EU-AIACT-2024` — European Union, *Regulation (EU) 2024/1689 (AI Act)*, 2024-06-13. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
- `GOOGLE-2025` — Nikolov et al., Google, *How is Google using AI for internal code migrations?*, 2025-01-12. https://arxiv.org/pdf/2501.06972
- `IAI-DWP-2025` — UK Incubator for AI, *Consult evaluation: DWP Pathways to Work consultation*, 2025-08-27. https://assets.publishing.service.gov.uk/media/68f63fe01c9076042263f0bd/evaluation-report.pdf
- `IAI-PLANNING-2026` — UK Incubator for AI, *Planning: Extract and Augmented Planning Decisions*, 2026-06. https://ai.gov.uk/our-work/planning
- `IAI-SCOT-2025` — UK Incubator for AI, *Consult evaluation: Scottish Government consultation*, 2025-03-20. https://digitalgovernmenthub.org/wp-content/uploads/2026/02/Scot_Gov_NSCP_Evaluation_Report.pdf
- `IBM-2024` — Pan et al., IBM Research and UIUC, *Lost in Translation: bugs introduced by LLMs while translating code* (ICSE '24), 2024-04. https://arxiv.org/pdf/2308.03109
- `NIST-AI600-2024` — NIST, *AI RMF Generative AI Profile (NIST AI 600-1)*, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `NIST-AIRMF-2023` — NIST, *AI Risk Management Framework 1.0 (NIST AI 100-1)*, 2023-01. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- `NIST-SAMPLING-2026` — NIST/SEMATECH, *e-Handbook of Statistical Methods* §6.2.1–6.2.2 (acceptance sampling), retrieved 2026-10-20. https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc21.htm
- `PRAGMATIC-2026` — The Pragmatic Engineer (G. Orosz), *The Pulse: we need to talk about migrations with AI*, 2026-08-27. https://blog.pragmaticengineer.com/the-pulse-we-need-to-talk-about-migrations-with-ai/
- `RETAILDIVE-2024` — Retail Dive, *Walmart used AI to crunch 850M product data points*, 2024-08-20. https://www.retaildive.com/news/walmart-generative-ai-product-data-points/724782/
- `UKY-2025` — Klusty et al., University of Kentucky, *Leveraging LLMs for structured data extraction from unstructured patient records*, 2025-12. https://arxiv.org/pdf/2512.13700
