# Build, buy or configure (step 2)

Read this on entering step 2. Sourcing is mostly a question of differentiation and maintenance, not capability.
Keys in brackets are listed in §6; *(advisor default)* marks a working rule, not a finding from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Options, criteria and decision rules](#3-options-criteria-and-decision-rules)
4. [Worked example: evidence matching in an audit practice](#4-worked-example-evidence-matching-in-an-audit-practice)
5. [Output](#5-output)
6. [Sources](#6-sources)

## 1. Goal and exit criteria

**Goal.** A sourcing decision the firm can defend later: the option, runtime class and starting rung, the
reasons, who maintains it, and what would make the firm revisit it.

**Exit when all of these are true:**

- At least two options compared, one of them a non-build option, plus the step 1 rule or existing-tool baseline
  where plausible; each assessed on the §3.2 criteria.
- The overlay's tool catalog checked; anything outside it flagged, with a vendor evaluation requested through
  **ai-governance**.
- The **simplest runtime class and rung** that could meet the bar chosen, with the reason.
- A **post-launch owner** named by role for prompts, retrieval, integrations, evaluations and the vendor.
- The decision recorded with an event that would trigger a revisit (never a date).

## 2. How to run it

1. **Check the overlay:** `overlay/tool-catalog.yaml` (which approved tools could do this, under what conditions,
   for which data classes) and any `overlay/vendors/<vendor>.md`. Without a catalog, use runtime classes (rule 6).
2. **List the options** (§3.1), always including the step 1 rule or existing tool and a bought or configured tool.
3. **Ask the differentiation question:** "Is this where we win, or a problem many firms have?" It settles most
   cases.
4. **Design the sample test:** 20–50 real cases with known answers and a pass/fail sheet, run by the user in an
   approved environment, results by task type (step 4 builds the full plan from this) [ANTHROPIC-2026]. Never
   ask for case content (rule 5).
5. **Price it in full and price the exit:** licences or consumption, integration, review time, evaluation,
   support and re-testing when models change, as ranges, using the cost stack in
   `../../../transformation-advisor/references/method/business-case.md` §3.4; then the cost of switching.
6. **Pick the runtime class and rung** (§3.3) and **name the owner after launch**.
7. **Play back** the options and the decision; write the section; hand vendor questions to **ai-governance**;
   name step 3. A decision with open exit criteria is a leaning, and `sourcing` stays `undecided` (§5).

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
| Differentiation | "Is this where we win?" Practitioners list text-to-SQL, documentation chatbots and knowledge-base support bots as not worth building in a product company | [APPLIEDLLMS-2024, 3.2.4] |
| Evidence on our tasks | "What did a sanctioned tool get wrong on our real tasks?" Legal research tools marketed as "hallucination-free" or similar hallucinated 17% to 33% of the time in a preregistered study (independent; 2024 versions) | [STANFORD-2024] |
| Total cost | "What is the run cost at expected volume, including review, support and re-evaluation?" | [UKGDS-2024] |
| Data boundaries | "What data leaves our boundary, under which terms, and can the vendor use it for other purposes?" | [NIST-2024, GV-6.2-007] |
| Lock-in and exit | "What does switching cost, and what would we retest?" a16z reports, from its survey of 100 CIOs, that guardrails and prompts built for agentic workflows make switching models harder. UK guidance: give suppliers a problem statement and dummy data, not a solution spec | [A16Z-2025, item 10; UKGDS-2025] |
| Maintenance | "Who re-evaluates and retunes prompts and guardrails when the model changes?" Models are the least durable component; keep the evaluation set as the portable asset | [APPLIEDLLMS-2024, 3.2.1; GOOGLE-2015] |
| Incidents and change | "How does the vendor notify incidents and model changes, and is it in the contract?" | [NIST-2024, GV-6.2-007] |
| Fit to existing systems | "Does it work inside the systems professionals already use?" | *(advisor default)* |

### 3.3 Runtime class and rung

Start with the simplest that could work: rules or existing software, a single model call with retrieval, a fixed
workflow, an agent that picks its own steps, then several agents. Higher rungs cost more latency, money and
testing effort, and errors compound across steps [ANTHROPIC-2024]. Classes are defined in the shared library §4
(`../../../transformation-advisor/references/library/index.md`). Typical fit *(advisor mapping)*:

| Runtime class | Typical fit | Flow, and where the checkpoint usually sits | Main risk to design for |
|---|---|---|---|
| `personal-assistant` | Individual drafting and analysis | Person → model → person uses or edits; every output reviewed | Unmanaged data handling; inconsistent practice |
| `shared-team-skills` | Repeatable team tasks with agreed prompts and reference material | Shared skill + approved material → model → team's tool; sign-off before anything leaves the team | Version drift; no shared evaluations |
| `workflow-automation` | Fixed multi-step flows through existing systems | Trigger → fixed steps, a model at some → system of record; review queue for low-confidence or high-risk items, sampled checks | Silent failure; brittle integrations |
| `background-agent` | Tasks that can wait; 66% of surveyed deployed agent systems allow response times of minutes or longer (UC Berkeley-led academic survey, N=53) [BERKELEY-2026] | Event → agent works through steps → result held; review at the end and before anything irreversible | Compounding errors; permissions |
| `managed-agent-runtime` | Tool-using agents that need logging, permissions, isolation and rollback | Hosted agent inside business systems; named checkpoints, approval for irreversible actions | Cost; lock-in; complexity |

### 3.4 Decision rules

- **General capability: buy or configure.** Build only around a proprietary workflow, data or method, and put
  the firm's effort into evaluations, guardrails and data loops [APPLIEDLLMS-2024, 3.2.4].
- **Regulated or high-risk work:** a16z reports the shift from building to buying has not played out in
  regulated or high-risk industries such as healthcare [A16Z-2025, item 12]; ask for stronger evidence.
- **Do not fine-tune first.** Prompt, retrieve and evaluate first. Practitioners report fine-tuning driven more by
  fear of missing out than strategy [APPLIEDLLMS-2024, 3.1.2]; 14 of 20 interviewed deployed-agent teams used
  off-the-shelf models without weight tuning (UC Berkeley-led study) [BERKELEY-2026].
- **Build-versus-partner rates are a caution, not a rule.** MIT Project NANDA reports external partnerships
  reaching deployment about 67% of the time against about 33% for internal builds (52 organizations;
  self-reported; may reflect capability rather than approach) [MITNANDA-2025].
- **Baseline on the same tasks.** In Vals' legal study at least one AI tool beat a lawyer control group on four of
  seven tasks, and lawyers did better on two (third-party benchmark; vendors chose their tasks) [VALS-2025].
- **No named owner after launch, no build** *(advisor default)*. **Outside the catalog:** not an option until
  **ai-governance** approves it.

## 4. Worked example: evidence matching in an audit practice

Illustrative, continuing step 1. Rules already match structured items. The approved audit platform's matching
feature, configured with the attribute checklist, is run by the pilot lead on 30 closed-engagement samples:
errors cluster on approval evidence in emails; setup is 60–100 hours on a licence already held. A build with firm
IT is untested and has no owner. **Decision:** `configure` on `workflow-automation` at `augment`; matching is
general, and the firm's edge is its checklist and review procedure. **Revisit when:** the feature fails step 4
thresholds or the vendor changes the model or terms.

## 5. Output

In `brief.md`, write §2 Build, buy or configure from `../templates/brief.md`: the options table, catalog check,
decision, maintenance owner and revisit trigger. In the frontmatter set `sourcing`, `tools`,
`classification.runtime_class`, `classification.ladder`, `vendor_evaluations` (if any),
`step_completed: 2`, `next_step: 3` and `updated`. Add the decision to the decisions log.

Keep `sourcing: undecided` until every exit criterion in §1 is met (for example, the own-sample test not yet run,
or the business owner not yet confirmed). Until then, write the leaning in §2 as "proposed" and in the decisions
log as a draft, and list the open criteria beside the unticked step. When ai-governance writes a vendor file for
this solution, add its path to `vendor_evaluations` at once, whatever its decision.

## 6. Sources

- `A16Z-2025` — Andreessen Horowitz, *How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025*, investor survey, 2025-06-10. https://a16z.com/ai-enterprise-2025/
- `ANTHROPIC-2024` — Anthropic, *Building effective agents*, vendor engineering guide, 2024-12-19. https://www.anthropic.com/engineering/building-effective-agents
- `ANTHROPIC-2026` — Anthropic, *Demystifying evals for AI agents*, vendor engineering guide, 2026-01-09. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `APPLIEDLLMS-2024` — Yan, Bischof, Frye, Husain, Liu, Shankar, *What We've Learned From A Year of Building with LLMs*, practitioner guide, 2024-06-08. https://applied-llms.org/
- `BERKELEY-2026` — Pan, Arabzadeh et al., *Measuring Agents in Production*, academic paper (arXiv 2512.04123 v4), 2026-06-04. https://arxiv.org/pdf/2512.04123
- `GOOGLE-2015` — Sculley et al., *Hidden Technical Debt in Machine Learning Systems*, NeurIPS paper, 2015. https://papers.nips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf
- `MITNANDA-2025` — MIT Project NANDA, *The GenAI Divide: State of AI in Business 2025*, preliminary research report, 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `NIST-2024` — NIST, *AI 600-1: Generative AI Profile*, standards-body profile, 2024-07. https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- `STANFORD-2024` — Magesh et al. (Stanford, Yale), *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, preprint, 2024-05-30. https://arxiv.org/pdf/2405.20362
- `UKGDS-2024` — UK Government Digital Service, *Generative AI Framework for HMG*, government guidance (withdrawn 2025-02-10), 2024-01-18. https://www.gov.uk/government/publications/generative-ai-framework-for-hmg/generative-ai-framework-for-hmg-html
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, government guidance, 2025-02-10. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
- `VALS-2025` — Vals AI with Legaltech Hub, *Vals Legal AI Report*, third-party benchmark, updated 2025-02-27. https://www.vals.ai/vlair
