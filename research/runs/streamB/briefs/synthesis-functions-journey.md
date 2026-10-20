**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are the editor who writes the **function cards** and the **journey-stage file** of an AI transformation
advisor's shared library. The advisor reads a function card when the user's work sits in a business function
(finance, HR, IT, procurement and so on) rather than an archetype's core value chain, and the journey-stage file
when it places a scope on its AI journey and plans the next stage. Today is 2026-10-20.

**Inputs:** `/home/user/ai-enablement/research/runs/streamB/b-functions-finance-strategy-procurement.md`, `/home/user/ai-enablement/research/runs/streamB/b-functions-commercial.md`,
`/home/user/ai-enablement/research/runs/streamB/b-functions-people-technology.md`, `/home/user/ai-enablement/research/runs/streamB/b-functions-delivery-risk.md`, `/home/user/ai-enablement/research/runs/streamB/b-journey-stages.md`, the current
`/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/index.md`, `.../references/method/onboarding.md` §5, and the archetype use cases (searched by `function:`).
**Vocabulary:** `/home/user/ai-enablement/research/briefs/templates/vocabulary.md`

## Files to write

**Function cards** in `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/functions/`, one per function id: `strategy-planning.md`, `sales-marketing-bd.md`,
`product-service-development.md`, `service-delivery.md`, `customer-service.md`, `people-hr.md`,
`technology-it.md`, `finance-accounting.md`, `procurement-supply-chain.md`, `risk-compliance-legal.md`. Each is at
most 250 lines, with a table of contents if over 100 lines. Sections:

1. **What this function covers.** Two or three sentences; which archetype covers firms that sell this work (for
   example, legal and audit firms are professional services and assurance; security operations is security).
2. **Processes and key steps**, as a table: process, key steps, work types, typical pain.
3. **Where AI is changing the work**, grouped by the four Reimagine lenses (improve the step, automate the flow,
   delegate the outcome, reinvent the work): each opportunity with its pattern id (linked to
   `../patterns/<id>.md`), ladder, change scope, and one or two graded examples (organization, industry, outcome
   with provenance, grade, source key). Then "In the archetypes": relevant archetype use-case ids (full id and
   grade; at most eight).
4. **Metrics and benchmarks**, with provenance.
5. **Interview probes.** Eight to twelve questions for a function leader, with what each reveals.
6. **Guardrails.** Rules and the decisions that need human judgment.
7. **Roles and how they evolve.**
8. **Sources.** Short key list.

**Journey stages:** `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/journey-stages.md` (at most 250 lines, table of contents). For each stage (curious,
experimenting, adopting, scaling, ai-native): what a leader can show or count, typical blockers, what to emphasize,
the investments and capabilities that move a scope to the next stage, exit criteria, and the failure points between
stages. Then how organizations are spread across stages (dated surveys, population, provenance) and how published
maturity models compare. **Don't repeat** `method/onboarding.md` §5 (diagnosis, stage cards, delegation gates):
link to it, and say this file is for planning the move to the next stage.

Then update `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/index.md`: in §7 add a link to `journey-stages.md` (one sentence); in §8 link each function id to its
card and replace the paragraph saying detailed cards are not yet in this version with one saying each function has
a card. Change nothing else in the index. Add one pointer line to `../library/journey-stages.md` at the end of
`method/onboarding.md` §5 only if the file stays at or under 300 lines.

## Rules

- Facts only from the inputs or the archetype YAML. Do not change what a source says. Keep modal verbs and
  provenance. No unsourced connective claims. Quotations under 25 words.
- Grade A rule (2026-10-17): A needs a figure the named organization reports as measured; recollections and rough
  estimates are B.
- Describe tools by runtime class, never recommend a vendor. No framework ids. Public sources only. No headcount
  targets for people; talk about roles and capacity.
- No build-process words in the product files. Every archetype id you cite must exist (check with grep).
- Run `python3 /home/user/ai-enablement/scripts/validate.py` and fix every ERROR in your files.

## Output

Write the files, then `/home/user/ai-enablement/research/runs/streamB/functions-journey-synthesis-report.md`: inputs used per file, conflicts resolved, gaps.
Do not run git. Reply with a summary of no more than 150 words.
