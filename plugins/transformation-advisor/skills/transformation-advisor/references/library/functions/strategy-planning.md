# Strategy and planning

Function id `strategy-planning`. Last reviewed 2026-10-20. Source keys in brackets are listed in §8. **Read this first:** this
function has the thinnest deployment evidence of any card. No named corporate strategy team with a measured outcome was found. The
measured items are public-sector consultation analysis and academic experiments; treat experiment results as ideas (grade D) until
a deployment shows them.

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

The in-house strategy, corporate planning and performance-management function of any organization: strategy development, market
and competitive intelligence, annual planning and target setting, scenarios and capital allocation, transformation tracking, and
board reporting. Firm-level strategy of professional-services firms (fee mix, AI investment envelope, ownership) is in the
professional-services `firm-finance` module. Consulting firms that sell strategy work are the professional-services archetype.

## 2. Processes and key steps

The process list is a working grouping; no process framework for strategy was used.

| Process | Key steps | Work types | Typical pain |
|---|---|---|---|
| Strategy development | Environment scanning; option generation; evaluation and choice; articulation | research-synthesis, expert-judgment, document-production | Option evaluation is slow and subjective: investor evaluators disagreed enough that an LLM's scores explained about 29% of variation in theirs (experiment) [CSASZAR-2024] |
| Market and competitive intelligence | Monitor sources; synthesize; draw implications | research-synthesis | No measured case found |
| Annual planning, budgeting, targets | Assumptions; targets; resource allocation; reconcile bottom-up and top-down | data-reporting, coordination-scheduling, expert-judgment | Forecasts built from many manual submissions (see the finance card) [NEUGROUP-2025] |
| Scenario and capital-allocation analysis | Scenario design; modelling; investment cases | data-reporting, expert-judgment | Strategic and executional decisions made in separate tools; Walmart built a simulation platform to connect them [INFORMS-2024] |
| Portfolio and transformation tracking | Initiative status; benefits tracking; course corrections | coordination-scheduling, data-reporting | No measured case found |
| Board and executive reporting | Pack assembly; commentary; Q&A preparation | document-production, data-reporting | No measured case found |
| Stakeholder and public input analysis | Collect responses; theme; summarize for decision | research-synthesis, transaction-processing | The UK government projects about 75,000 days of manual consultation analysis a year, costing £20 million (a projection) [DSIT-2025] |

## 3. Where AI is changing the work

**Improve the step** (assist or augment)

- **Theme large volumes of qualitative input** ([document-to-decision](../patterns/document-to-decision.md); augment; step).
  Scottish Government with the UK government's Incubator for AI (public sector): on a consultation of over 2,000 responses, themes
  scored F1 0.76 against a single human reviewer; reviewers made no changes for 60% of responses; median 23 seconds to review a
  response; negligible effect on theme ranking; the tool "struggled to identify missing themes". Self-reported by the builders; policy
  consultation, not corporate strategy. Grade B [IAI-CONSULT-SCOT-2025; DSIT-2025]. A larger evaluation of the same tool is in the
  service-delivery card.
- **Draft and critique strategic options; a second opinion** ([research-brief](../patterns/research-brief.md); assist; step). LLM
  versions of ten business plans were rated 0.14 standard deviations higher by 250 evaluators with investing experience
  (pre-registered experiment). Idea (experiment only), grade D [CSASZAR-2024].
- **Screen plans at scale** ([intake-triage](../patterns/intake-triage.md); augment; step). LLM scores on 138 competition plans
  explained about 29% of the variation in judges' scores. Idea (experiment only), grade D [CSASZAR-2024].
- **Link network or portfolio design to daily execution** ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); augment;
  process). Walmart (retail): optimization models produce long-term network designs, and plans were "approved" for investments
  involving billions of dollars; no measured outcome of the design itself; optimization, not generative AI. Grade B [INFORMS-2024].
- **Board and executive pack assembly** ([draft-review-loop](../patterns/draft-review-loop.md); augment; step). Idea; no measured
  named case found. Grade D.

**Automate the flow**

- **Forecast and plan on full data instead of manual submissions**
  ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); automate; process). The treasury forecasting cases in the finance card
  show the shape. For earnings, a working paper reports an LLM outperforming the median analyst at predicting annual earnings
  ("preliminary"). Idea (experiment only), grade D [CHICAGOBOOTH-2024].
- **Continuous competitive-intelligence monitoring** ([monitor-diagnose-act](../patterns/monitor-diagnose-act.md); automate;
  process). Described as an illustrative use in a corporate blog; no deployment or result. Idea, grade D [INDIAMART-2025, search-only].

**Delegate the outcome**

- No evidence of an agent owning a planning outcome was found. Plan nothing here before the stage gates in
  `../../method/onboarding.md` §5 hold.

**Reinvent the work**

- Operating-model and investment decisions about AI itself are the strategy function's model-level work. The evidence sits in the
  professional-services archetype: an AI investment envelope reviewed against existing finance measures
  (`professional-services-firm-finance-07`, B) and entry-level intake reshaped as AI absorbs junior work
  (`professional-services-talent-learning-19`, B).

**In the archetypes**: `professional-services-firm-finance-01` (B), `professional-services-firm-finance-07` (B),
`professional-services-firm-finance-10` (B), `professional-services-firm-finance-15` (B), `professional-services-firm-finance-17` (B),
`professional-services-talent-learning-19` (B), `professional-services-scoping-pricing-17` (C), `tax-transfer-pricing-19` (C).

## 4. Metrics and benchmarks

- **Agreement with a human reviewer:** F1 0.76 (95% CI 0.75-0.77) per response; in an earlier evaluation two reviewers scored F1 0.81
  against each other and mapped exactly the same themes 62% of the time. Self-reported by the tool's builder
  [IAI-CONSULT-SCOT-2025].
- **Review time:** median 23 seconds per response; 77% of responses reviewed in under a minute [IAI-CONSULT-SCOT-2025].
- **Inside and outside the AI frontier:** 758 BCG consultants on 18 tasks completed 12.2% more tasks, 25.1% faster, at higher quality;
  on one task chosen to be outside the frontier they were 19% less likely to be correct. Independent academic study
  [HBS-DELLACQUA-2023].
- **Not found:** any benchmark for plan-to-actual variance, strategy cycle time or planning cost.

## 5. Interview probes

1. "Which decisions did the last planning cycle change, and what input did each rely on?" Reveals where synthesis actually bears on
   decisions; the consultation report treats theme ranking as the key driver of recommendations [IAI-CONSULT-SCOT-2025].
2. "How many documents, comments or responses do you read, and how many do you sample?" Reveals candidates for full-population
   synthesis [IAI-CONSULT-SCOT-2025].
3. "Who would check the themes, and what would they do about a missing theme?" Reveals the review design; missing themes were the
   tool's weak point [IAI-CONSULT-SCOT-2025].
4. "Where do your strategy and execution tools disconnect?" Reveals a process opportunity of the Walmart kind [INFORMS-2024].
5. "Would you use AI to generate options, or only to critique them?" Reveals homogenization exposure: AI-inspired stories were more
   similar to each other (creative-writing experiment, adjacent) [EXETER-2024].
6. "Which of your tasks is outside what current AI does reliably?" Reveals jagged-frontier awareness [HBS-DELLACQUA-2023].
7. "How do you evaluate a plan today, and how much do your evaluators agree with each other?" Reveals whether there is a stable
   standard to test an AI screen against [CSASZAR-2024].
8. "Which forecasts are built from manual submissions?" Reveals forecasting candidates [NEUGROUP-2025].
9. "What will the freed analysis time buy?" Reveals whether speed is treated as the outcome; the consultation report says faster
   analysis "freed up time" for implications [IAI-CONSULT-SCOT-2025].

## 6. Guardrails

- **The choice stays human:** strategy, capital allocation and which options to pursue. In the consultation trial reviewers wanted to
  influence the themes and needed more confidence before reviewing only a share of responses [IAI-CONSULT-SCOT-2025].
- **Tasks outside the frontier:** 19% lower odds of a correct answer when AI was used on a task outside its competence
  [HBS-DELLACQUA-2023].
- **Missed themes:** check for what the synthesis left out, not only for what it got wrong [IAI-CONSULT-SCOT-2025].
- **Homogenization:** with one AI idea, stories were 10.7% more similar to each other than with none (adjacent experiment)
  [EXETER-2024]. Keep human-generated options in the set.
- **Risk frameworks:** NIST AI RMF 1.0 and its Generative AI Profile [NIST-AIRMF-2023; NIST-AI600-1-2024].
- **Decisions that need human judgment:** which strategy and options to pursue; capital allocation; targets; what a missing theme
  means; anything presented to the board as the organization's view.

## 7. Roles and how they evolve

- **Analysts move from coding responses to checking and interpreting them:** faster analysis "freed up time" to focus on
  implications, and reviewers felt the tool helped reduce reviewer bias [IAI-CONSULT-SCOT-2025].
- **Strategists' search and aggregation may change:** Csaszar and co-authors argue AI may change search, representation and
  aggregation in strategic decisions and enable "virtual strategy simulations"; a framework, not a measurement [CSASZAR-2024].
- **Planners connect strategy and execution models** where optimization links them (Walmart) [INFORMS-2024].

## 8. Sources

- **CHICAGOBOOTH-2024**: Kim, Muhn, Nikolaev, Chicago Booth, *Financial Statement Analysis with Large Language Models* (academic, 2024-05). https://www.chicagobooth.edu/research/fama-miller/finance-research/funding/a-demand-system-approach-for-fixed-income/financial-statement-analysis-with-large-language-models
- **CSASZAR-2024**: Csaszar, Ketkar, Kim, *Artificial Intelligence and Strategic Decision-Making: Evidence from Entrepreneurs and Investors* (academic, arXiv 2408.08811, 2024-08-16). https://arxiv.org/abs/2408.08811
- **DSIT-2025**: UK Department for Science, Innovation and Technology, *Government-built "Humphrey" AI tool reviews responses to consultation for first time* (government release, 2025-05-14). https://www.gov.uk/government/news/government-built-humphrey-ai-tool-reviews-responses-to-consultation-for-first-time-in-bid-to-save-millions
- **EXETER-2024**: University of Exeter on Doshi and Hauser, *AI found to boost individual creativity but results in less varied content* (academic, 2024-07-15). https://news.exeter.ac.uk/?p=13749
- **HBS-DELLACQUA-2023**: Dell'Acqua et al., *Navigating the Jagged Technological Frontier*, HBS Working Paper 24-013 (academic, 2023-09). https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
- **IAI-CONSULT-SCOT-2025**: Incubator for AI (UK government), *Consult Evaluation: Scottish Government's Non-surgical cosmetic procedures consultation* (government evaluation, 2025-03-20). https://digitalgovernmenthub.org/wp-content/uploads/2026/02/Scot_Gov_NSCP_Evaluation_Report.pdf
- **INDIAMART-2025**: IndiaMART corporate blog, *The new C-suite ally: generative AI* (press, 2025-07-29; search-only). https://corporate.indiamart.com/2025/07/29/the-new-c-suite-ally-generative-ai
- **INFORMS-2024**: Mehrotra et al., *Optimizing Walmart's Supply Chain from Strategy to Execution*, INFORMS Journal on Applied Analytics 54(1) (academic, 2024-01). https://courses.ie.bilkent.edu.tr/ie479/wp-content/uploads/sites/16/2024/11/Optimizing-Walmarts-Supply-Chain-from-Strategy-to-Execution.pdf
- **NEUGROUP-2025**: NeuGroup, *Working Cash Flow Forecast Magic With Data Wizards and ML Models* (peer-group community, 2025-09-24). https://connect.neugroup.com/public/blogs/working-cash-flow-forecast-magic-with-data-wizards-and-ml-models
- **NIST-AIRMF-2023**: NIST, *AI Risk Management Framework 1.0* (standard-setter, 2023-01). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- **NIST-AI600-1-2024**: NIST, *AI RMF: Generative AI Profile* (standard-setter, 2024-07). https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
