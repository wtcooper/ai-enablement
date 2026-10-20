# Intake (step 2)

Read this on entering step 2: when someone brings a new AI idea from any practice or function, or when the user
wants to import items from an advisor `opportunities.yaml`. It tells you how to log an idea so it can be screened,
and how to import with a back-link. Keys in brackets are listed in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Checklists and decision rules](#3-checklists-and-decision-rules)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: three ideas and an import](#7-worked-example-three-ideas-and-an-import)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** Every idea is in one register, described as a business problem, classed, owned and ready to screen.
Intake is a register, not an inbox: the UK AI Playbook suggests a use cases register for capturing ideas and
deciding which to explore first [UKGOV-2025], and Microsoft's guidance keeps a prioritized backlog with consistent
criteria [MSFT-PLAN-2026].

**Exit criteria** for each item:

- An intake record and a `portfolio.yaml` entry with the same id, `stage: intake`.
- One sentence naming the activity and the expected result.
- Last month's actual volume of the activity, labelled with where the number came from.
- A class: individual-productivity, business-automation or new-value.
- An owner (a role), and the data it needs with the data owner.
- The rules-or-AI check done, and a duplicate check against the register.
- `status: outline` if the problem, owner or data source is missing; otherwise ready to screen.
- For imports: `source` pointing to the advisor file and item.

## 2. How to run it

**A new idea**

1. **Name the step.** "Let's log this idea so it can be screened. Next we score it."
2. **Get the sentence.** Ask for the activity and the result in one sentence, then for how often the activity
   happened last month [MSFT-PLAN-2026]. Ask one question at a time.
3. **Start from the problem.** If the idea starts from a tool ("we should use agents for…"), ask where results
   miss expectations or people repeat manual work [MSFT-PLAN-2026; UKGOV-2025].
4. **Class it** (§3.2). Route seat and licence roll-outs to the enablement line.
5. **Rules or AI.** Ask whether a few if-then rules, a template or an existing feature would do [RAND-2024].
6. **Data and owner.** Ask what data it needs, who owns it, and whether anyone has looked at it in its real state.
7. **Duplicates.** Search `portfolio.yaml` for the same process, pattern or unit. Link near-duplicates.
8. **Early read.** Note risk exposure, a build, buy or partner leaning, and any archetype use cases that show
   the idea working elsewhere, with grades exactly as recorded.
9. **Write** the intake record from `../templates/intake.md` and the `portfolio.yaml` entry. Play it back.

**An import from the advisor**

1. Read `opportunities.yaml` (schema `../../../transformation-advisor/references/schemas/opportunities.md`).
   Ask which items to bring in: usually the chosen top options and foundations, not parked items.
2. For each item: copy `id` (prefix the unit if ids could clash), `title`, `process`, `pattern`, `ladder`,
   `change_scope`, `runtime_class`, `value`, `scores`, `category`, `depends_on`, `role_evolution` and `evidence`.
   Set `source: { file, item }`, `stage: intake`, and fill the intake record from the item's `description`.
3. An item with `label: draft-to-validate` stays `status: outline`, marked "Draft to validate", until people who
   do the work confirm it.
4. Never edit the advisor's file. The back-link lives in `portfolio.yaml`.

## 3. Checklists and decision rules

### 3.1 Intake checklist

- One sentence: activity plus expected result [MSFT-PLAN-2026].
- Volume from a record, not a typical week (proposed default for the volume prompt).
- Class set [MSFT-PLAN-2026].
- Owner named as a role; benefit owner asked for, even if not yet known [IVI-ITCMF-n.d.].
- Rules-or-AI check done [RAND-2024; UKGOV-2025].
- Data sources and owners listed.
- Duplicate check done.

**Decision rule.** Items without an owner, a problem statement and a data source stay `outline` and are not
scored.

### 3.2 Classes and routes

| Class | Test | Route |
|---|---|---|
| `individual-productivity` | People do the same work in existing tools, faster or better | A seat or licence roll-out goes on the enablement line and to ai-enablement; a packaged team workflow can be a portfolio item |
| `business-automation` | The flow of work changes: steps removed, merged or run without a person on the normal path | Portfolio item; full or light path by risk tier |
| `new-value` | A new service, product or price | Portfolio item; judged on revenue mechanics |

Why separate them: MIT NANDA reports widely adopted chat tools mainly "enhance individual productivity, not P&L
performance", and an apparent pilot-to-implementation rate of about 83% for generic chat tools against 5% for
task-specific tools (interview-based; its authors call the figures directional) [MITNANDA-2025]. Counting seat
roll-outs as portfolio wins inflates the pipeline (derived from that contrast).

## 4. Question bank

Tags: **[T]** team, **[U]** unit or practice, **[O]** organization.

**Core**
- Describe the activity and the result you expect in one sentence. How often did it happen last month? [T]
- Is this a change to how people work in existing tools, or a change to how the work flows? [T]
- Could simpler rules, a template or existing software handle this? [T] [RAND-2024; UKGOV-2025]
- What data does it need, who owns it, and has anyone looked at it in its real state? [T]
- Who in the business would own the benefit? [U] [IVI-ITCMF-n.d.]

**Follow-ups**
- Where do ideas come from today: strategy, practice leaders, staff, vendors? [U] [UKGOV-2025; MSFT-PLAN-2026]
- Where are people already using personal AI tools for this work? [T][U]
- Is any other practice working on the same problem? [U]
- What would make the people doing this work reject it? [T]
- What client data or professional duties does it touch? [T][U]

## 5. Expert moves

| Move | When | What it reveals |
|---|---|---|
| **Make every entry a one-sentence activity-plus-result statement before scoring** | Every intake | Vague ideas, and whether the activity happens often enough to justify the work [MSFT-PLAN-2026] |
| **Start from business problems, not technology** | Ideas that arrive as a tool | Novelty-driven requests; UK guidance says use cases should be led by business and user needs [UKGOV-2025] |
| **Ask "could a few if-then rules do this?"** | Every intake | AI applied where it is not needed; RAND's interviewees described datasets with a handful of dominant patterns [RAND-2024] |
| **Class the item and route seat roll-outs to the enablement line** | Every intake | Inflated pipeline counts [MITNANDA-2025] (derived) |
| **Ask for the benefit owner by role at intake** | Every intake | Orphan benefits; the share of projects with a benefits owner is a maturity measure [IVI-ITCMF-n.d.] |
| **Ask where people already use personal AI tools** | Intake drives across a practice | Real demand and unsanctioned risk; MIT NANDA reports workers at over 90% of surveyed companies used personal AI tools regularly (small, non-random sample; directional) [MITNANDA-2025] |

## 6. Common traps

| Trap | How to avoid it |
|---|---|
| **An inbox, not a register:** ideas in email threads and meeting notes | One record per idea, one id across files |
| **Technology-first ideas** | Ask for the problem and the metric before the tool |
| **Seat roll-outs counted as wins** | Enablement line, reported apart |
| **Typical-week volumes** | Ask for last month's count from a record; label the number |
| **Re-scoring an imported item from scratch without its history** | Keep the advisor's ranges and scores and the back-link; re-score only against the portfolio's weights |
| **Duplicates across practices** | Search the register at every intake; HBR's whole-portfolio view exists to see them [HBR-2026] |

## 7. Worked example: three ideas and an import

*Illustrative*, continuing the firm from `setup.md`.

- A tax operations manager proposes: "Extract K-1 and source-document data with confidence flags so preparer hours
  per return fall." Last season's time records show about 3,000 K-1-heavy returns. Class: business-automation.
  Data: client documents in the document system, owned by the tax practice. Archetype evidence:
  `tax-compliance-individual-business-02` (grade B). Ready to screen.
- The business development team asks for first drafts of proposal answers from approved content. Class:
  business-automation. A near-duplicate exists: the advisory practice logged the same idea. They are linked and
  screened together. Evidence: `professional-services-pursuit-proposals-01` (grade B).
- Several partners ask for licences for a general chat assistant. Class: individual-productivity, a seat
  roll-out. It goes on the enablement line and to ai-enablement; it is not scored as a portfolio item.
- The tax unit's advisor file holds four chosen options. They are imported with `source` set; one carries
  `label: draft-to-validate` from a desk review and stays `outline` until the preparers confirm it.

## 8. Output

- `portfolio/intake/<id>.md` from `../templates/intake.md`, one per item.
- A `portfolio.yaml` entry per item with the step 2 fields in `../schemas/portfolio.md` §2.
- Update `state.step_completed: 2` (first time through), `next_step: 3`, `updated`.

## 9. Sources

- `HBR-2026` — Nelson, Davenport, Scade, *Manage your AI investments like a portfolio*, Harvard Business
  Review, 2026-01 (read via reprint). https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio
- `IVI-ITCMF-n.d.` — Innovation Value Institute, *Benefits Harvesting (IT-CMF 18.07)*, maturity-model
  guidance, undated. https://portal.ivi.ie/+itcmf/18.07/value/BAR/C/C3
- `MITNANDA-2025` — Challapally, Pease, Raskar, Chari, MIT Project NANDA, *The GenAI divide: state of AI in
  business 2025*, research report (preliminary), 2025-07. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `MSFT-PLAN-2026` — Microsoft Learn, *Plan for AI adoption*, vendor guidance, updated 2026-10-15.
  https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/plan
- `RAND-2024` — RAND Corporation, *The root causes of failure for artificial intelligence projects and how they
  can succeed*, research report, 2024-08-13. https://www.rand.org/pubs/research_reports/RRA2680-1.html
- `UKGOV-2025` — UK Government Digital Service, *Artificial Intelligence Playbook for the UK Government*,
  government guidance, 2025. https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html
