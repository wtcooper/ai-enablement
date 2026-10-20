# Build, buy or configure (step 2)

Read this on entering step 2. It helps the user choose how the solution will be sourced (buy a tool as it is,
configure a bought tool, build around a bought model, or build most of it) and the simplest runtime class that
could meet the quality bar. It is mostly a question of differentiation and maintenance, not capability. Keys in
brackets are listed in §9. Lines marked *(advisor default)* are working rules, not findings from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Options, criteria and decision rules](#3-options-criteria-and-decision-rules)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: evidence matching in an audit practice](#7-worked-example-evidence-matching-in-an-audit-practice)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** A sourcing decision the firm can defend later: the option, the runtime class and starting rung, the
reasons, who maintains it, and what would make the firm revisit it.

**Exit when all of these are true:**

- At least two options compared, one of them a non-build option, plus the rule or existing-tool baseline from
  step 1 where it was plausible.
- Each option assessed on the criteria in §3.2: differentiation, evidence on the firm's own sample, total cost,
  data boundaries, switching cost and exit, maintenance, and fit to the systems professionals already use.
- The overlay's tool catalog checked; anything outside it flagged, with a vendor evaluation requested through the
  **ai-governance** skill.
- The **simplest runtime class and rung** that could meet the quality bar chosen, with the reason.
- A **post-launch owner** named by role for prompts, retrieval, integrations, evaluations and the vendor
  relationship.
- The decision recorded with an event that would trigger a revisit (never a date).

## 2. How to run it

1. **Name the step.** "Now we decide whether to buy, configure or build, and on what kind of runtime."
2. **Check the overlay.** Read `overlay/tool-catalog.yaml` if it exists: which approved tools could do this,
   under what conditions and for which data classes. Read any `overlay/vendors/<vendor>.md` already written.
   Without a catalog, describe options by runtime class only (rule 6).
3. **List the options** (§3.1). Always include the simplest: the rule or existing-tool version from step 1, and a
   bought or configured tool.
4. **Ask the differentiation question** (§5, move 1). It settles most cases.
5. **Design the sample test.** The decision should rest on the firm's own cases, not vendor benchmarks. Help the
   user pick 20–50 real cases with known answers and a simple pass/fail sheet; the user runs it in an approved
   environment and brings back results by task type (step 4 builds the full plan from this) [ANTHROPIC-2026].
   Never ask for the case content itself (rule 5).
6. **Price it in full.** Licences or consumption, integration, review time, evaluation, support and re-testing
   when models change. Use the cost stack in
   `../../../transformation-advisor/references/method/business-case.md` §3.4. Give ranges.
7. **Price the exit.** Ask what it would cost to switch models or vendors and what would have to be retested.
8. **Pick the runtime class and rung** (§3.3): the simplest that could meet the bar.
9. **Name the owner after launch.** If nobody can be named, do not start a build *(advisor default)*.
10. **Play back** the options table and the decision; write the section; hand vendor questions to
    **ai-governance**; name step 3 as next.

## 3. Options, criteria and decision rules

### 3.1 Options

| Option (`sourcing` id) | What it means | Usually fits |
|---|---|---|
| `buy` | Use a bought tool as it is | General capabilities many firms need |
| `configure` | Configure a bought tool: settings, templates, approved content, connectors | General capability plus the firm's own method or content |
| `build-on-model` | Build the workflow, retrieval, checks and evaluations around a bought model or platform | A proprietary workflow, data or method on general model capability |
| `build-custom` | Build most components in-house | Rare; a differentiating capability nothing on the market covers |

### 3.2 Criteria

| Criterion | Ask | Source |
|---|---|---|
| Differentiation | "Is this where we win, or a general problem many firms have?" Practitioners list text-to-SQL, documentation chatbots and knowledge-base support bots as not worth building in a product company | [APPLIEDLLMS-2024, 3.2.4] |
| Evidence on our tasks | "What did a sanctioned tool get wrong on a sample of our real tasks?" | [STANFORD-2024; A16Z-2025, item 11] |
| Total cost | "What is the run cost at expected volume, including review time, support and re-evaluation?" | [UKGDS-2024; GOOGLE-2015] |
| Data boundaries | "What data leaves our boundary, under which terms, and can the vendor use it for other purposes?" | [NIST-2024, GV-6.2-007; UKGDS-2025] |
| Lock-in and exit | "What does switching cost, and what would we retest?" CIOs told a16z that agent workflows tuned for one model are hard to move | [A16Z-2025, item 10; UKGDS-2025] |
| Maintenance | "Who re-evaluates models, and retunes prompts and guardrails when the model changes?" Models are the least durable component | [APPLIEDLLMS-2024, 2.2.2, 3.2.1; GOOGLE-2015] |
| Incidents and change | "How does the vendor notify incidents and model changes, and is it in the contract?" | [NIST-2024, GV-6.2-007] |
| Fit to existing systems | "Does it work inside the systems professionals already use, or ask them to move?" | *(advisor default)* |

### 3.3 Runtime class and rung

Start with the simplest that could work: rules or existing software, a single model call with retrieval and
examples, a fixed multi-step workflow, an agent that picks its own steps, then several agents. Higher rungs cost
more latency, money and testing effort [ANTHROPIC-2024; OPENAI-2025]. Runtime classes are defined in the shared
library §4 (`../../../transformation-advisor/references/library/index.md`). Typical fit *(advisor mapping, not
from a source)*:

| Runtime class | Typical fit | Main risk to design for |
|---|---|---|
| `personal-assistant` | Individual drafting, summarizing, analysis, with a person reviewing every output | Unmanaged data handling; inconsistent practice |
| `shared-team-skills` | Repeatable team tasks with agreed prompts, templates and reference material | Version drift; no shared evaluations |
| `workflow-automation` | Fixed multi-step flows through existing systems | Silent failure; brittle integrations |
| `background-agent` | Tasks that can wait, reviewed at the end; 66% of surveyed deployed agents tolerate minutes or longer [BERKELEY-2026] | Compounding errors; permissions |
| `managed-agent-runtime` | Tool-using agents that need logging, permissions, isolation and rollback | Cost; lock-in; complexity |

### 3.4 Decision rules

- **General capability: buy or configure.** Build only around a proprietary workflow, data or method, and put
  the firm's effort into evaluations, guardrails and data loops around whatever model is used
  [APPLIEDLLMS-2024, 3.2.1 and 3.2.4].
- **Regulated or high-risk work:** a16z reports the shift to buying has not played out there; assume more
  in-house control and ask for stronger evidence [A16Z-2025, item 12].
- **Do not fine-tune first.** Prompt, retrieve and evaluate first; fine-tune only with proof. Practitioners
  report fine-tuning driven more by fear of missing out than strategy [APPLIEDLLMS-2024, 3.1.2]. In a Berkeley
  study, 70% of 20 interviewed deployed-agent cases used off-the-shelf models without weight tuning
  [BERKELEY-2026].
- **Treat build-versus-partner success rates as a caution, not a rule.** MIT NANDA reports external partnerships
  reaching deployment about 67% of the time against about 33% for internal builds; the figures are
  self-reported, and the authors say they may reflect organizational capability rather than approach
  [MITNANDA-2025].
- **No named owner after launch, no build** *(advisor default)*.
- **Outside the catalog:** flag it and hand the vendor evaluation to **ai-governance**; do not treat the option
  as available until it is approved.

## 4. Question bank

Tags: **[T]** team, **[U/O]** unit or organization.

- Is this a place we differentiate, or a general capability? [U/O]
- Have we tried a sanctioned off-the-shelf tool on a sample of real tasks, and what did it get wrong? [T][U/O]
- Who will own the system after the builder moves on: prompts, retrieval, integrations, evaluations, vendor? [U/O]
- What does it cost to switch models or vendors, and what would we have to retest? [U/O]
- What data leaves our boundary, under which contract terms, and can the vendor use it for secondary purposes? [U/O]
- What is the total run cost at expected volume, including review time, support and re-evaluation? [U/O]
- How does the vendor handle incidents, model changes and notification, and is it in the agreement? [U/O]
- Would the vendor run our evaluation cases and show results by task type? [U/O]
- Which approved tools in our catalog could do this already? [T][U/O]

## 5. Expert moves

1. **"Is this where we differentiate?"** at the build-or-buy gate. Reveals internal effort going into commodity
   capability [APPLIEDLLMS-2024].
2. **Price maintenance, not just build:** ask who re-evaluates models and retunes prompts and guardrails when the
   model changes. Reveals the hidden recurring cost and the switching cost [A16Z-2025; APPLIEDLLMS-2024;
   GOOGLE-2015].
3. **Put lock-in and exit in the requirements; give suppliers dummy data and a problem statement, not a solution
   spec.** UK guidance says to consider strategies to avoid vendor lock-in, start with the problem statement and
   budget for hidden costs [UKGDS-2025].
4. **Treat vendor accuracy claims as hypotheses; run your own cases on the vendor tool.** In a preregistered
   study, legal research tools marketed with "hallucination-free" or similar language hallucinated 17% to 33%
   of the time on the study's queries (independent; 2024 product versions) [STANFORD-2024].
5. **Baseline against the current process on the same tasks.** Vals' legal study used a lawyer control group:
   AI tools beat it on four of seven tasks and none beat it on one research task (third-party benchmark;
   vendors chose which tasks to enter). In the Berkeley survey only 39% compared their agent to a non-agentic
   baseline [VALS-2025; BERKELEY-2026].

## 6. Common traps

| Trap | Evidence | How to avoid |
|---|---|---|
| Believing vendor accuracy claims | 17% to 33% hallucination in tested legal research tools [STANFORD-2024] | Run the firm's own sample; require results by task type |
| Building everything; fine-tuning too early | [APPLIEDLLMS-2024, 3.1.2, 3.2.1]; a16z's investor view that fine-tuning looks less necessary as models improve [A16Z-2025, item 6] | Prompt, retrieve and evaluate first |
| Model and prompt lock-in | "Migrating prompts across models is a pain" [APPLIEDLLMS-2024, 2.2.2]; newer models can break agent workflows [BERKELEY-2026] | Keep the evaluation set as the portable asset; pin and version models |
| Pricing the licence, not the run | No source gives measured total-cost comparisons (gap) | Full cost stack with ranges, including review time and re-testing |
| An agent where a workflow would do | Errors compound across steps [ANTHROPIC-2024] | Start at the lowest rung that meets the bar |

## 7. Worked example: evidence matching in an audit practice

Illustrative, continuing step 1.

| Option | Sample result | Cost (range, season) | Exit | Differentiation | Owner after launch |
|---|---|---|---|---|---|
| Rules only (amount and date match) | Works on structured items only; already in use | Nil | — | None | Methodology team |
| `configure`: matching feature of the firm's approved audit platform, with the practice's attribute checklist | Pilot lead runs 30 closed-engagement samples in the platform; errors cluster on approval evidence in emails | Licence already held; configuration and checklist 60–100 hours | Low: checklist and cases are reusable | The checklist and review procedure are the firm's own | Methodology team |
| `build-on-model` with firm IT | Not tested | Build plus maintenance, wide range | Medium | Low: matching is not where the firm wins | Not named |
| Specialist point tool | Not in the catalog | Unknown | Unknown | Low | Not named |

- **Decision:** `configure` on `workflow-automation`, starting at `augment` (every match reviewed). Matching is a
  general capability; the firm's edge is its attribute checklist and review procedure, so effort goes there. No
  post-launch owner exists for a build.
- **Handoffs:** the point tool goes to **ai-governance** as a possible later evaluation, not a current option.
- **Revisit when:** the platform feature fails the step 4 thresholds, the vendor changes the model or terms, or
  volume rises enough to change the cost picture.

## 8. Output

In `brief.md`, write §2 Build, buy or configure from `../templates/brief.md`: the options table, catalog check,
decision, maintenance owner and revisit trigger. In the frontmatter set `sourcing`, `tools`,
`classification.runtime_class`, `classification.ladder`, `vendor_evaluations` (if any),
`step_completed: 2`, `next_step: 3` and `updated`. Add the decision to the decisions log.

## 9. Sources

- `A16Z-2025` — Andreessen Horowitz, *How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025*, investor
  survey, 2025-06-10. https://a16z.com/ai-enterprise-2025/
- `ANTHROPIC-2024` — Anthropic, *Building effective agents*, vendor engineering guide, 2024-12-19.
  https://www.anthropic.com/engineering/building-effective-agents
- `ANTHROPIC-2026` — Anthropic, *Demystifying evals for AI agents*, vendor engineering guide, 2026-01-09.
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `APPLIEDLLMS-2024` — Yan, Bischof, Frye, Husain, Liu, Shankar, *What We've Learned From A Year of Building with
  LLMs*, practitioner guide, 2024-06-08. https://applied-llms.org/
- `BERKELEY-2026` — Pan, Arabzadeh et al., *Measuring Agents in Production*, academic paper (arXiv 2512.04123 v4),
  2026-06-04. https://arxiv.org/pdf/2512.04123
- `GOOGLE-2015` — Sculley et al., *Hidden Technical Debt in Machine Learning Systems*, NeurIPS paper, 2015.
  https://papers.nips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf
- `MITNANDA-2025` — MIT Project NANDA, *The GenAI Divide: State of AI in Business 2025*, preliminary research
  report, 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, standards-body profile, 2024-07.
  https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, vendor guide, 2025-04.
  https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `STANFORD-2024` — Magesh et al. (Stanford, Yale), *Hallucination-Free? Assessing the Reliability of Leading AI
  Legal Research Tools*, preprint, 2024-05-30. https://arxiv.org/pdf/2405.20362
- `UKGDS-2024` — UK Government Digital Service, *Generative AI Framework for HMG*, government guidance (withdrawn
  2025-02-10), 2024-01-18. https://www.gov.uk/government/publications/generative-ai-framework-for-hmg/generative-ai-framework-for-hmg-html
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, government guidance,
  2025-02-10. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
- `VALS-2025` — Vals AI with Legaltech Hub, *Vals Legal AI Report*, third-party benchmark, updated 2025-02-27.
  https://www.vals.ai/vlair
