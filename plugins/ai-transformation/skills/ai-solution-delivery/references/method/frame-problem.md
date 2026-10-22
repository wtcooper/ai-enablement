# Frame the problem (step 1)

Read this on entering step 1. It turns one opportunity into a problem frame: the real work, volumes and error
costs, the business owner's metric, and the simplest kind of solution that could work. Most delivery failure
starts here, not in the model. Keys in brackets are listed in §6. *(advisor default)* marks a working rule, not a
finding from a source.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Checks, decision rules and traps](#3-checks-decision-rules-and-traps)
4. [Worked example: evidence matching in an audit practice](#4-worked-example-evidence-matching-in-an-audit-practice)
5. [Output](#5-output)
6. [Sources](#6-sources)

## 1. Goal and exit criteria

**Goal.** Agree what problem this solves, for whom, how success will be judged, and whether AI is the right
answer at all, before anyone compares tools.

**Exit when all of these are true:**

- **Starting point linked:** the portfolio item or advisor option, or a note that it is new and should go
  through intake with **ai-portfolio**.
- **Problem statement** in the business owner's words; the **business owner**, by role, has confirmed the
  metric and can review outputs on a regular rhythm.
- **Success metric with a baseline** (or the record it will come from), labelled from a record, reported or
  observed.
- **The work today** from a real recent instance: trigger, steps, handoffs, systems, last month's volume, time
  per item, rework share; **users, reviewers and the accountable professional**; **error costs** (which errors
  are costly or irreversible).
- **Fit checks done** (§3); **informal AI use** noted, with any data risk; **pattern and rung hypothesis** named
  and the pattern file's "not when" list checked.
- **Decision:** proceed to step 2, solve without AI, or go back to the portfolio or the advisor.

## 2. How to run it

1. **Start from what exists.** Read the source item: the portfolio entry in `portfolio/portfolio.yaml` and its
   intake record, or the option in `opportunities.yaml` (pattern, ladder, runtime class, value range, human
   checkpoints, role evolution, evidence). In `transformation-plan.md`, read the item's Make the case page (cost
   lines and who carries them, the comparison and go/no-go, assumptions to test first) and its Plan steps, not
   only Map. Play back what you already know in three lines and ask only for what is missing. Before you raise a
   resource conflict or a missing estimate, check whether the plan already budgets or decides it.
2. **Ask for the last real instance**, then last month's actual count and rework share from a record. Typical
   descriptions hide the exceptions that break solutions.
3. **Restate the goal as the owner's metric and get it confirmed.** RAND's example is the price that gives the
   greatest profit margin, not the price that sells the most items [RAND-2024].
4. **Screen the stakes:** which errors would be costly or irreversible, and who would notice.
5. **Run the fit checks** (§3).
6. **Ask what people already do** with personal AI tools on this work; it shows demand and data risk. MIT Project
   NANDA reports workers at over 90% of surveyed companies using personal AI tools while 40% of companies had
   bought an LLM subscription (52 interviews and 153 leaders surveyed; self-reported; directional) [MITNANDA-2025].
7. **Name the pattern and rung.** In `../../../transformation-advisor/references/library/patterns/<pattern>.md`,
   read §2 "Where it fits", including its "not when" lines, and §10 Probes. If nothing fits, use `other`.
8. **Play back the frame**, record the decision, write the section and name step 2.

For process documents, use the shared `analyze-document` brief (SKILL.md, Delegation). If the user is still
asking where AI could help, hand off to **transformation-advisor**.

## 3. Checks, decision rules and traps

| Check | Ask | What decides it | Source |
|---|---|---|---|
| Rules first | "What would a rule or checklist version look like, and why is it not enough?" | If a rule, template or existing tool meets the bar on a sample, recommend it; it is also the baseline to beat | [GOOGLE-RULES, Rule 1] |
| Agent fit | "Does the work need judgment on exceptions, rules nobody can maintain, or heavy unstructured documents?" | None of the three: a workflow or a single model call is likely enough | [OPENAI-2025] |
| Intern test | "Given exactly this input and context, would a competent graduate succeed?" | No: context to add, a task to split, or a task too hard for current models | [APPLIEDLLMS-2024, 1.4.3] |
| Task type | "Which tasks are inside what the tools do well?" | Test by task, not by role; on one task outside the frontier, consultants using AI were 19% less likely to reach a correct solution (preregistered experiment, 758 BCG consultants, GPT-4, 2023) | [HBS-2023] |
| Stakes | "Where is an error costly or irreversible?" | Be cautious about fully automating significant decisions; high-impact outputs need a person validating them | [UKGDS-2025] |
| Owner | "Who will check outputs against intent, every week if needed?" | Nobody: fix ownership before design *(advisor default)*. In RAND's interviews (65 data scientists and engineers, 50 from industry), 84% cited one or more leadership-driven causes, such as leaders not available to check intent, as the primary reason projects fail (the mostly non-managerial sample may skew this) | [RAND-2024] |

**Decision rules.** If the pattern's "not when" list matches, say which line and reconsider the pattern or rung.
If the metric is "AI usage" or "people like it", ask again; usage is not value. If the baseline is not in a
record, name who will collect it; never design on an invented baseline (rule 4).

**Traps.** Data trouble found late: 30 of 50 RAND industry interviewees discussed persistent data-quality
problems, so look at a real input sample now [RAND-2024]. Technology over the user problem: 16 of 50 described
technology-driven failures [RAND-2024]. People and process ignored: BCG's survey of 1,000 CxOs attributes about
70% of implementation challenges to people and process, 20% to technology and 10% to algorithms (self-reported)
[BCG-2024], so frame workflow change as part of the problem.

## 4. Worked example: evidence matching in an audit practice

Illustrative. Portfolio item `ct-evidence-matching` (`document-to-decision`, `augment`, `workflow-automation`) is
in discover. Time records show 50–80 hours of matching per engagement last season (from record). The audit
partner rejects "hours saved" alone and confirms "net staff hours per engagement with review notes on evidence no
higher than last season". Bank confirmations already match by rule, so they are excluded; the intern test shows
the attribute checklist must be an input, so it becomes a dependency. **Decision:** proceed to step 2. Once
`brief.md` was written, the delivery lead handed back to **ai-portfolio**, which then set the item's `solution`
(the `g0` Go had not set it); the brief's Handoffs table records it.

## 5. Output

In `brief.md`, write §1 Problem frame from `../templates/brief.md`. In the frontmatter set `id`, `title`,
`source`, `scope`, `owners.business`, `owners.delivery`, a provisional `classification`, `step_completed: 1`,
`next_step: 2` and `updated`. Record the decision in the decisions log. Advance `step_completed` only when every
exit criterion in §1 is met; otherwise list the open ones beside the unticked step. If the decision is "back to
the portfolio", set `status: stopped` and say which skill takes it from here.

**Solve without AI.** Set `ai_use: none` and the AI fields to null (`../schemas/solution.md` §4). For a portfolio
item, hand the finding and the sourcing leaning back to **ai-portfolio** to record on the item, then close the
brief with `status: stopped`. If the user wants to keep it open as design evidence for the gate, keep
`status: in-progress` and record that choice and its reason in the decisions log.

## 6. Sources

- `APPLIEDLLMS-2024` — Yan, Bischof, Frye, Husain, Liu, Shankar, *What We've Learned From A Year of Building with LLMs*, practitioner guide, 2024-06-08. https://applied-llms.org/
- `BCG-2024` — Boston Consulting Group, *AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value*, press release, 2024-10-24. https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value
- `GOOGLE-RULES` — Google for Developers (M. Zinkevich), *Rules of Machine Learning*, practitioner guide, page last updated 2025-08-25. https://developers.google.com/machine-learning/guides/rules-of-ml
- `HBS-2023` — Dell'Acqua et al., *Navigating the Jagged Technological Frontier*, HBS working paper 24-013, 2023-09. https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
- `MITNANDA-2025` — MIT Project NANDA, *The GenAI Divide: State of AI in Business 2025*, preliminary research report, 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `OPENAI-2025` — OpenAI, *A practical guide to building agents*, vendor guide, 2025-04. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `RAND-2024` — RAND Corporation, *The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed*, research report, 2024-08-13. https://www.rand.org/pubs/research_reports/RRA2680-1.html
- `UKGDS-2025` — UK Government, *Artificial Intelligence Playbook for the UK Government*, government guidance, 2025-02-10. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
