# Intake (step 2)

Read this on entering step 2: a new AI idea from any practice or function, an import from an advisor
`opportunities.yaml`, or a tool already in use. Keys in brackets are listed in §7.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Decision rules](#3-decision-rules)
4. [Questions and traps](#4-questions-and-traps)
5. [Worked example](#5-worked-example)
6. [Output](#6-output)
7. [Sources](#7-sources)

## 1. Goal and exit criteria

**Goal.** Every idea is in one register, described as a business problem, classed, owned and ready to screen.
Intake is a register, not an inbox: the UK AI Playbook suggests a use cases register for capturing ideas and
deciding which to explore first [UKGOV-2025].

**Exit criteria** for each item:

- An intake record and a `portfolio.yaml` entry with the same id, `stage: intake` (a tool already in use: the
  stage its use supports).
- One sentence naming the activity and the expected result, and last month's actual volume with its basis.
- A class (§3.2), an owner (a role), and the data it needs with the data owner.
- The rules-or-AI check and a duplicate check against the register done.
- `status: outline` if the problem, owner or data source is missing; otherwise ready to screen.
- For imports: `source` set; the parse check reported; the plan's case in "From the plan"; grades as recorded.

## 2. How to run it

**A new idea**

1. **Name the step.** "Let's log this idea so it can be screened. Next we score it."
2. **Get the sentence.** Ask for the activity and the result in one sentence, then for how often the activity
   happened last month, from a record, not a typical week [MSFT-PLAN-2026]. If the idea starts from a tool ("we
   should use agents for…"), ask where results miss expectations or people repeat manual work [UKGOV-2025].
3. **Class it** (§3.2). Route seat and licence roll-outs to the enablement line.
4. **Rules or AI.** Ask whether a few if-then rules, a template or an existing feature would do [RAND-2024] (§3.1).
5. **Data and owners.** Ask what data it needs, who owns it, whether anyone has looked at it in its real state, and
   who in the business would own the benefit.
6. **Duplicates.** Search `portfolio.yaml` for the same process, pattern or unit. Link near-duplicates.
7. **Early read.** Note risk exposure and tier (`../library/index.md` §2), a build, buy or partner leaning, and
   archetype use cases that show the idea working elsewhere, with grades exactly as recorded.
8. **Write** the record from `../templates/intake.md` and the `portfolio.yaml` entry. Fill every template line,
   including "AI use"; write "none recorded" where there is nothing yet. Add no other sections. Play it back.

**An import from the advisor**

1. **Check the file parses** (schema `../../../transformation-advisor/references/schemas/opportunities.md`).
   Parse it if a parser is available. If it fails, or you cannot run a parser, say so and give the line (re-read
   near it for unquoted colons). Import only after the user agrees; never import it unmentioned. Offer
   **transformation-advisor** to fix the file; do not fix it yourself.
2. Ask which items to bring in: usually the chosen top options and foundations, not parked items.
3. For each item, copy `id` (prefix the unit if ids could clash), `title`, `pattern`, `ladder`, `change_scope`,
   `runtime_class`, `value`, `scores`, `category`, `depends_on`, `human_checkpoints`, `role_evolution`, `evidence`
   and `label` as they stand. Set `source: { file, item }` and `stage: intake`. Fill the record from the item's
   `description`, `process`, `prerequisites` and `next_step`. Copy each `value` line verbatim (same lever, numbers
   and assumptions); put any rewrite (option numbers turned into ids, a lever you would map differently) in the
   intake record. A lever not in `settings.value_levers` is kept as it stands and flagged.
4. **Keep the advisor's capacity choice.** Copy `role_evolution.capacity_use` as it stands, even when
   `settings.capacity_stance` is `undecided`; never write `undecided` on an item. Note in the record that the
   firm's stance is still open; the choice is confirmed at `g3`.
5. **Read the plan's case, not only the item.** In `transformation-plan.md`, read the item's Make the case page
   (cost lines and who carries them, the comparison and go/no-go under "How we will know", assumptions to test
   first), its Now, Next and Later steps, its control-plan row and the people steps. Copy them into "From the plan",
   naming the section each line came from, and each figure with what it covers (a total, or the part of a total one
   task takes). Before you raise a conflict or a gap later, check this section and the plan section it names.
6. **Look up grades.** For each evidence id, open the use case in the archetype files
   (`../../../transformation-advisor/references/archetypes/index.md`) and write its `evidence_grade` exactly as
   recorded into Early read. If an id is not found, say so; never guess a grade.
7. **One label per role.** Map the plan's roles to one label each and record them in `roles.other`. If the plan
   names one role two ways, or the owner and sponsor are the same role, say so and use one label.
8. An item with `label: draft-to-validate` stays `status: outline`, with "Draft to validate" in the record's
   Status, until people who do the work confirm it. Then set `label: null`.
9. **Duplicates across units.** If two advisor items are the same idea, import one and list the other in its
   `rolled_up_from` (the advisor's Roll-up field); its value is counted once. Note in the record what the merged
   item adds. Near-duplicates that keep their own entries are linked in each record's duplicates line.
10. Never edit the advisor's file. The back-link lives in `portfolio.yaml`.

**A tool already in use** (from the step 1 inventory, or named later)

1. Log it like an idea, with `source: null` and Source "In use today". Set `stage` to what its current use
   supports, not `intake`: usually `production` for a supported tool in general use, `pilot` for a trial group.
   Record no decisions for gates it never passed.
2. `owner` is the business owner who decides how it is used; the technical owner (licences, admin settings) goes in
   `roles.other` and on the record's Technical owner line. `status: active` once the business owner is named.
3. Fill the record's "In use today" section. Items that depend on the tool go on the duplicates line. Do not score
   it; a seat roll-out is not a portfolio win, and training and adoption go to ai-enablement.

## 3. Decision rules

### 3.1 Outline and no-AI items

Items without an owner, a problem statement and a data source stay `outline` and are not scored.

**No AI needed.** If the rules-or-AI check finds that rules, a template or an existing tool is enough (or the
advisor's case says no AI is required), set `ai_use: none` and leave `ladder`, `runtime_class` and `risk_tier`
null; note the advisor's values in the record. Keep the item only if it earns a place, for example as a
`foundation` other items depend on; the review counts it apart from AI items. Otherwise record the finding and
hand the idea back to its owner.

### 3.2 Classes and routes

| Class | Test | Route |
|---|---|---|
| `individual-productivity` | People do the same work in existing tools, faster or better | A seat or licence roll-out goes on the enablement line and to ai-enablement; a packaged team workflow can be an item |
| `business-automation` | The flow of work changes: steps removed, merged or run without a person on the normal path | Portfolio item; full or light path by risk tier |
| `new-value` | A new service, product or price | Portfolio item; judged on revenue mechanics |

Why separate them: MIT NANDA reports widely adopted chat tools "primarily enhance individual productivity, not P&L
performance", and only 5% of organizations got task-specific tools into production (52 interviews and a survey of
153 senior leaders; its authors call the figures directional) [MITNANDA-2025]. Counting seat roll-outs as wins
inflates the pipeline.

## 4. Questions and traps

- Is this a change to how people work in existing tools, or to how the work flows?
- Where are people already using personal AI tools for this work? Is another practice working on the same problem?
- What client data or professional duties does it touch? What would make the people doing the work reject it?

| Trap | How to avoid it |
|---|---|
| **Technology-first ideas** | Ask for the problem and the metric before the tool [UKGOV-2025] |
| **Re-scoring an import from scratch** | Keep the advisor's ranges, scores and back-link; re-score only against the portfolio's weights |
| **Importing the item without the plan's case** | Copy its cost lines, go/no-go and steps into "From the plan"; check there before raising a conflict |
| **Duplicates across practices** | Search the register at every intake |

## 5. Worked example

*Illustrative.* A tax operations manager proposes: "Extract K-1 and source-document data with confidence flags so
preparer hours per return fall." Time records show about 3,000 K-1-heavy returns last season. Class:
business-automation; data in the document system, owned by the tax practice; evidence
`tax-compliance-individual-business-02` (grade B). Ready to screen. Partners asking for chat licences go on the
enablement line. The tax unit's advisor file holds four chosen options; they are imported with `source` set, and
one with `label: draft-to-validate` stays `outline` until the preparers confirm it.

## 6. Output

- `portfolio/intake/<id>.md` from `../templates/intake.md`, every template line filled ("none recorded" if empty)
  and no other sections.
- A `portfolio.yaml` entry per item with the step 2 fields in `../schemas/portfolio.md` §2.
- `state.step_completed: 2` (first time through), `next_step: 3`, `updated`.

## 7. Sources

- `MITNANDA-2025` — Challapally, Pease, Raskar, Chari, MIT Project NANDA, *The GenAI divide: state of AI in
  business 2025*, research report (preliminary), 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `MSFT-PLAN-2026` — Microsoft Learn, *Plan for AI adoption*, vendor guidance, updated 2026-10-15.
  https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/plan
- `RAND-2024` — RAND Corporation, *The root causes of failure for artificial intelligence projects and how they
  can succeed*, research report, 2024-08-13. https://www.rand.org/pubs/research_reports/RRA2680-1.html
- `UKGOV-2025` — UK Government Digital Service, *Artificial Intelligence Playbook for the UK Government*,
  government guidance, 2025. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
