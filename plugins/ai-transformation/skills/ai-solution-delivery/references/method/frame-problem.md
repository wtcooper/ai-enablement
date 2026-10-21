# Frame the problem (step 1)

Read this on entering step 1. It turns one opportunity into a problem frame: the real work, its users,
volumes and error costs, the metric the business owner will judge it by, and the simplest kind of solution that
could work. Most delivery failure starts here, not in the model. Keys in brackets are listed in §9. Lines marked
*(advisor default)* are working rules, not findings from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Checks and decision rules](#3-checks-and-decision-rules)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: evidence matching in an audit practice](#7-worked-example-evidence-matching-in-an-audit-practice)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** Agree what problem this solution solves, for whom, how success will be judged, and whether AI is the
right answer at all, before anyone compares tools.

**Exit when all of these are true:**

- **Starting point linked:** the portfolio item or advisor option it came from, or a note that it is new and
  should go through intake with the **ai-portfolio** skill.
- **Problem statement** in the business owner's words, and a **business owner** named by role who has confirmed
  the metric and can review outputs on a regular rhythm.
- **Success metric with a baseline** (or the record it will come from), each number labelled with where it
  came from: from a record, reported, or observed.
- **The work today** from a real recent instance: trigger, steps, handoffs, systems, last month's volume, time per
  item, and the share that needed rework or escalation.
- **Users, reviewers and the accountable professional** for the output.
- **Error costs:** which errors are costly or irreversible (client advice, a filing, a payment, a client send).
- **Fit checks done:** a rule or template version considered; agent-fit signals; the intern test.
- **Informal AI use** on this work noted, with any data risk.
- **Pattern and rung hypothesis** named, and the pattern file's "not when" list checked.
- **Decision:** proceed to step 2, solve without AI, or go back to the portfolio or the advisor.

## 2. How to run it

1. **Start from what exists.** Read the source item: the portfolio entry in `portfolio/portfolio.yaml` and its
   intake record, or the option in `opportunities.yaml` (pattern, ladder, runtime class, value range, human
   checkpoints, role evolution, evidence). In `transformation-plan.md`, read the item's Make the case page (cost
   lines and who carries them, the comparison and go/no-go, assumptions to test first) and its Plan steps, not
   only Map. Play back what you already know in three lines and ask only for what is missing. Before you raise a
   resource conflict or a missing estimate, check whether the plan already budgets or decides it.
2. **Ask for the last real instance**, start to finish, then for last month's actual count and the rework share
   from a record. Typical descriptions hide the exceptions that break solutions.
3. **Restate the goal as the owner's metric** and ask the owner to confirm it (§5, move 1). If the owner is not
   available to check outputs, say so now: leadership-driven causes, including leaders not available to check
   intent, were the most cited in RAND's interviews with 65 experienced data scientists and engineers
   [RAND-2024].
4. **Screen the stakes.** Ask which errors would be costly or irreversible and who would notice them.
5. **Run the fit checks** (§3): could a rule or checklist do it; do the agent-fit signals hold; would a competent
   graduate succeed with the same input and context.
6. **Ask what people already do** with personal AI tools on this work. It shows demand and data risk.
7. **Name the pattern and rung.** Open the pattern file
   (`../../../transformation-advisor/references/library/patterns/<pattern>.md`): read §2 "Where it fits",
   including its "not when" lines, and §10 Probes. If nothing fits, use `other` and describe the shape.
8. **Play back the frame**, record the decision, write the section and name step 2 as next.

If the user provides process documents or checklists, use the shared `analyze-document` brief (see SKILL.md,
Delegation). If there is no opportunity at all and the user is still asking where AI could help, hand off to
**transformation-advisor**.

## 3. Checks and decision rules

| Check | Ask | What decides it | Source |
|---|---|---|---|
| Rules first | "What would a rule-based or checklist version look like, and why is it not enough?" | If a rule, template or existing tool meets the quality bar on a sample, recommend that instead of a model-based solution | [GOOGLE-RULES, Rule 1; OPENAI-2025] |
| Agent fit | "Does the work need judgment on exceptions, rules nobody can maintain, or heavy unstructured documents?" | None of the three: a workflow or a single model call is likely enough | [OPENAI-2025] |
| Intern test | "Given exactly this input and context, would a competent graduate in the field succeed?" | No: missing context to add, a task to split, or a task too hard for current models | [APPLIEDLLMS-2024, 1.4.3] |
| Task type | "Which tasks in this role are inside what the tools do well, and which are not?" | Test by task, not by role; on one task outside the frontier, consultants using AI were 19% less likely to reach a correct solution (preregistered experiment with 758 BCG consultants, GPT-4, 2023) | [HBS-2023] |
| Stakes | "Where is an error costly or irreversible?" | Be cautious about fully automating significant decisions; high-impact or high-risk outputs need a person validating them | [UKGDS-2025] |
| Owner | "Who will check outputs against intent, every week if needed?" | Nobody: fix ownership before design *(advisor default)* | [RAND-2024] |

**Decision rules**

- If the pattern file's "not when" list matches the situation, say which line and reconsider the pattern or the
  rung before moving on.
- If the success metric is "AI usage" or "people like it", ask again for the owner's metric; usage is activity,
  not value.
- If the baseline cannot be found in a record, name who will collect it and how; never start design on an
  invented baseline (rule 4).

## 4. Question bank

Tags: **[T]** team, **[U/O]** unit or organization. Core questions are in SKILL.md; use these to follow up.

- Describe the last real instance of this work, start to finish. What came in, who touched it, what went out,
  how long did it take? [T]
- Give me last month's actual volume, not a typical week, and the share that needed rework or escalation. [T]
- Which step do people dislike or get wrong most often, and how do you know? [T]
- What metric would the owner of this process use to say it improved? Is that the metric the pilot will
  track? [T][U/O]
- What would a rule-based or checklist version of this step look like, and why is it not enough? [T]
- Does the work need judgment on exceptions, unstructured documents, or a rule set nobody can maintain? [T]
- What do people already do with personal AI tools on this task? [T][U/O]
- Who is the single accountable owner, and are they available weekly to review outputs? [T][U/O]
- What are the cases where an error is costly or irreversible (client advice, filing, payment)? [T][U/O]
- Across the units in scope, which share the same workflow and which need separate solutions? [U/O]
- Which parts rely on our own data or method, and which are problems many firms have? [U/O]

## 5. Expert moves

1. **Restate the goal as the business metric the owner needs, and get it confirmed in writing.** RAND's
   example is the price that gives the greatest profit margin, not the price that sells the most items. Reveals
   proxy-metric errors
   and an owner who is not available to the team [RAND-2024].
2. **Ask "would a few if-then rules do this?" and try the rule version first.** Reveals AI applied to a simple
   problem, and gives a baseline to beat [RAND-2024; GOOGLE-RULES, Rules 1 and 3; OPENAI-2025].
3. **Check the three agent-fit signals** when someone proposes an agent: nuanced judgment or exceptions, rules
   too tangled to maintain, heavy unstructured data. Reveals whether a workflow or single call is enough
   [OPENAI-2025].
4. **Run the intern test.** Reveals missing context, tasks too hard for current models, or tasks to decompose
   [APPLIEDLLMS-2024].
5. **Test by task type, not by role**, before a role-wide rollout. Reveals tasks inside and outside the jagged
   capability frontier [HBS-2023].
6. **Ask what people already do with personal AI tools.** Reveals demand, the flexibility users expect and what
   a sanctioned solution must match. MIT Project NANDA reports workers at over 90% of surveyed companies using
   personal AI tools while 40% of companies had bought an LLM subscription (interviews with 52 organizations and
   a survey of 153 senior leaders; self-reported; the report calls its figures directional) [MITNANDA-2025].

## 6. Common traps

| Trap | Why it happens | Evidence | How to avoid |
|---|---|---|---|
| Optimizing the wrong problem or metric | Technical staff translate a vague goal; owners are not there to check intent | In RAND's interviews with experienced data scientists and engineers (65 in all, 50 from industry), 84% of interviewees cited one or more leadership-driven causes as the primary reason projects fail (interview tally; RAND notes its mostly non-managerial sample may skew toward leadership causes) [RAND-2024] | Move 1; a named owner reviewing outputs |
| Using AI where rules would do | AI treated as a buzzword | [RAND-2024; GOOGLE-RULES, Rule 1] | Build and measure the rule or single-call baseline first |
| Automating waste | The workflow was not mapped or diagnosed first | No source measured this directly; NANDA reports interview accounts of brittle workflows and misalignment with daily operations [MITNANDA-2025] | Ask for the last real instance and last month's rework; baseline the current process |
| Chasing technology over the user problem | Builders want the newest tools | 16 of 50 RAND industry interviewees described bottom-up, technology-driven failures [RAND-2024] | Tie each design choice to the problem statement |
| Ignoring people and process | Algorithms get the attention | BCG's survey of 1,000 CxOs and senior executives in 59 countries attributes about 70% of implementation challenges to people and process, 20% to technology, 10% to algorithms (self-reported) [BCG-2024] | Frame adoption and workflow change as part of the problem |
| Data trouble found late | Nobody looked at the real data | 30 of 50 RAND industry interviewees discussed persistent data-quality problems [RAND-2024] | Ask where the inputs live and look at a real sample in step 1 |

## 7. Worked example: evidence matching in an audit practice

Illustrative, continuing the advisor's audit practice. The portfolio item `ct-evidence-matching` is in the
discover stage, and its owner opens `solutions/ct-evidence-matching/`.

- **Started from:** portfolio item `ct-evidence-matching` (from the advisor option of the same id:
  `document-to-decision`, `augment`, `workflow-automation`, grade-B evidence `assurance-controls-testing-07`).
- **Last real instance:** the pilot lead walks through a closed engagement: samples selected, client evidence
  received as PDFs and email exports, staff open each file and tick test attributes, the senior reviews. Time
  records show 50–80 hours of matching per engagement last season (from record).
- **Owner's metric:** the audit partner rejects "hours saved" alone and confirms "net staff hours per
  engagement with review notes on evidence no higher than last season".
- **Stakes:** a wrong match accepted into the file means an unsupported test conclusion that an inspection
  could find. It is caught before sign-off if review is real, so it is costly rather than irreversible.
- **Fit checks:** structured bank confirmations already match by rule, so they are excluded. Invoices and
  approvals in mixed formats are unstructured: a model-based extraction fits. Intern test: a graduate with the
  attribute checklist would succeed, so the checklist must be part of the input.
- **Informal use:** some staff paste evidence into personal chat tools. The delivery lead flags it as a data
  risk for **ai-governance** and as demand the solution must meet.
- **Pattern and rung:** `document-to-decision` at `augment`; the pattern file's "not when" line about criteria
  that are unwritten applies until the attribute checklist (the advisor's foundation item F1) exists, so F1
  becomes a dependency.
- **Decision:** proceed to step 2, with the checklist as a dependency.
- **Handoff:** when the brief opened, the delivery lead handed back to **ai-portfolio**, which set the item's
  `solution`; the brief's Handoffs table records it.

## 8. Output

In `brief.md`, write §1 Problem frame from `../templates/brief.md`. In the frontmatter set `id`, `title`,
`source`, `scope`, `owners.business`, `owners.delivery`, a provisional `classification`, `step_completed: 1`,
`next_step: 2` and `updated`. Record the decision in the decisions log. Advance `step_completed` only when every
exit criterion in §1 is met; otherwise list the open ones beside the unticked step. If the decision is "back to
the portfolio", set `status: stopped` and tell the user which skill takes it from here.

**Solve without AI.** Set `ai_use: none` and the AI fields to null (`../schemas/solution.md` §4). For a portfolio
item, hand the finding and the sourcing leaning back to **ai-portfolio** to record on the item, then close the
brief with `status: stopped`. If the user wants to keep it open as design evidence for the gate, keep
`status: in-progress` and record that choice and its reason in the decisions log.

## 9. Sources

- `APPLIEDLLMS-2024` — Yan, Bischof, Frye, Husain, Liu, Shankar, *What We've Learned From A Year of Building with
  LLMs*, practitioner guide, 2024-06-08. https://applied-llms.org/
- `BCG-2024` — Boston Consulting Group, *AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale
  Value*, press release, 2024-10-24. https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- `GOOGLE-RULES` — Google for Developers (M. Zinkevich), *Rules of Machine Learning*, practitioner guide,
  page last updated 2025-08-25. https://developers.google.com/machine-learning/guides/rules-of-ml
- `HBS-2023` — Dell'Acqua et al., *Navigating the Jagged Technological Frontier*, HBS working paper 24-013,
  2023-09. https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
- `MITNANDA-2025` — MIT Project NANDA, *The GenAI Divide: State of AI in Business 2025*, preliminary research
  report, 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, vendor guide, 2025-04.
  https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `RAND-2024` — RAND Corporation, *The Root Causes of Failure for Artificial Intelligence Projects and How They
  Can Succeed*, research report, 2024-08-13. https://www.rand.org/pubs/research_reports/RRA2680-1.html
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, government guidance,
  2025-02-10. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
