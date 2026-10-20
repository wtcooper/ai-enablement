# The workflow library (step 5)

Read this on entering step 5. It sets up how reusable workflows (prompts, skills and procedures) are captured, tested,
curated and retired, per role, each with its human checkpoint. The library is how one person's gain becomes the
group's default way of working. Source keys in brackets are listed in §11. Tags: **[T]** team, **[U]** unit,
**[O]** organization.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [The lifecycle](#4-the-lifecycle)
5. [Testing an entry](#5-testing-an-entry)
6. [Expert moves](#6-expert-moves)
7. [Checklist and decision rules](#7-checklist-and-decision-rules)
8. [Common traps](#8-common-traps)
9. [Worked example](#9-worked-example)
10. [Output](#10-output)
11. [Sources](#11-sources)

## 1. Goal and exit criteria

**Goal.** A small, trusted set of workflows per role that people can find, that have been tested on real cases, that
name who checks the output, and that are retired when they stop being right.

**Exit when all of these are true:**
- **Library rules** written: who can add, who reviews, the test standard, what approval means, the data rules, the
  review triggers and how entries are retired.
- **Intake routes:** from any user, from champions (capstones), from the central team, and from launched solutions.
- **First entries** written as `enablement/workflows/<id>.md`, at least one per target workflow from step 2, each with
  a human checkpoint and a data rule (or `data_rules: "unknown"` and status `candidate`).
- **Index** of entries in `program.md` section 5.
- **Reuse tracking** method chosen (how you will know a workflow is used beyond its author).
- **Routes out:** workflows worth redesigning go to the transformation-advisor skill; workflows that should run without
  a person on the normal path go to the ai-solution-delivery skill.

## 2. How to run it

1. **Collect what the crowd already uses** (L1). Start from what people have built, then centralize the best:
   Mollick's "lab" takes crowd prompts and solutions, distributes them quickly, and tests and measures them
   [MOLLICK-LAB-2025].
2. **Triage** each candidate: is it reusable, is the task common, is the data rule known, is it `assist` or
   `augment`? Anything that would run unattended is a solution, not a library entry.
3. **Write the entry** with `references/templates/workflow.md`. Fill `human_checkpoint` and `data_rules` first.
4. **Test it** (§5) on real, sanitized cases, run by someone other than the author.
5. **Approve or send back.** Approval needs a reviewer, a passed test and a known data rule.
6. **List it** in the index and tell the groups it serves (clinic, spotlight).
7. **Set review triggers** and the reuse signal; retire entries that fail them.
8. If you have several candidate documents or prompt collections, use the `draft-workflow-entry` brief (SKILL.md,
   Delegation) and confirm each draft with the user.

## 3. Question bank

| # | Question | Scope | Notes |
|---|---|---|---|
| L1 | Which prompts, skills or procedures do people already pass around? Where do they live? | [T][U] | Crowd supply |
| L2 | Who can add a workflow, who reviews it, and how is it tested before others rely on it? | [U][O] | Library rules |
| L3 | For this workflow, who checks the output, against what, before it is used or leaves the team? | [T][U] | The human checkpoint |
| L4 | Which data may go in, under which rule, and which client terms apply? | [U][O] | Data rule, from governance |
| L5 | How do people find a workflow today? How would you know anyone else used it? | [U][O] | Discoverability and reuse |
| L6 | What would make this workflow wrong: a tool change, a rule change, a new form or template? | [T][U] | Review triggers |
| L7 | Which entries came from users and which from the central team? | [U][O] | Balance of supply |
| L8 | Which workflow would you declare the default way for that task, and who signs that off? | [U] | Embedded use |

## 4. The lifecycle

`candidate` → `testing` → `approved` → (`needs-retest` → `testing`) → `retired`. Field rules are in
`schemas/workflow.md`.

| Stage | Who | What happens | Leaves the stage when |
|---|---|---|---|
| Candidate | Anyone | Submitted with task, role, steps and a proposed checkpoint | Triage accepts it |
| Testing | A tester who is not the author | Run on real, sanitized cases (§5) | Passed, or sent back |
| Approved | Reviewer (role) | Listed, announced, tracked for reuse | A review trigger fires |
| Needs retest | Owner | Re-run the test after a change | Passed again, or retired |
| Retired | Owner | Withdrawn with a reason; file kept | Never deleted |

**Kinds.** `prompt` (a pattern a person adapts), `skill` (packaged and used the same way across a team; the
`shared-team-skills` runtime class), `procedure` (written steps mixing AI and manual work and checks).

**Where entries come from.** Microsoft's guidance for an AI centre of excellence lists reusable assets with compliance
checklists on an internal platform and templates for common use cases (vendor guidance) [MSLEARN-COE-ND]. Law firms
report knowledge teams curating approved tools, use cases and playbooks in one place
(`professional-services-knowledge-management-18`, grade B); Gowling WLG aims for durable playbooks, prompt patterns and
repeatable workflows [HARVEY-GOWLING-2025]. Audit firms and regulators describe risk-tiered permitted-use policies, including the option of a curated prompt
library (`assurance-quality-management-02`, grade B). BBVA reports over 2,900 custom assistants built by staff in five months
(vendor-published, not verified) [OPENAI-ENTGUIDE-ND].

## 5. Testing an entry

- **Real cases, sanitized.** Use past work with client and personal details removed, unless the tool is approved for
  that data. Never paste client-confidential data into the workflow file itself.
- **A reference answer.** Compare output with what an expert produced or would accept. Firms test tools on their own
  work against an expert baseline and re-test when tools change (`professional-services-work-production-23`, grade
  B). Morgan Stanley describes advisors grading summaries against expert answers (vendor-published)
  [OPENAI-MSTANLEY-ND]. Official AI benchmarks rarely test your own kind of work; build your own small set
  [MOLLICK-LAB-2025].
- **Someone other than the author** runs the test and records cases, passes and what failed.
- **Test the checkpoint too.** Plant a known error and confirm the checkpoint as written would catch it. Legal research
  tools hallucinated 17% to 33% of the time in one preregistered study (independent) [ARXIV-MAGESH-2024]; a checkpoint
  that does not open the sources would miss that.
- **Record where it fails.** AI helps inside its capability and not uniformly outside it [HBS-JAGGED-2023]; the entry's
  "Do not use it for" section comes from the failures.

How many cases are enough is a judgment for the reviewer; write the number and the reason in `tested.notes`. No
published standard was found.

## 6. Expert moves

| Move | When | What it reveals |
|---|---|---|
| Collect workflows from the crowd, then centralize the best | Starting the library | Reuse potential [MOLLICK-LAB-2025] |
| Ask for the human checkpoint before the prompt | Writing any entry | Whether the workflow is safe to reuse at all |
| Make champion capstones library candidates | Linking step 4 | A steady supply with an owner [WBD-CHAMPIONS-ND] |
| Ask "which task is this now the default way for?" | After approval | Whether use is embedded; Lewis Silkin aims for the tool to be "the standard way the work gets done" [HARVEY-CHAMPIONS-2026] |
| Track reuse and last-tested dates as the guard | Curation | Stale entries. Evidence on curation, retirement and reuse rates is thin; these two signals are the practical guard |
| Measure the knowledge layer with search and reuse data, and re-test when tools change | Scaling the library | Whether the library is used and still right (`professional-services-knowledge-management-23`, grade C) |
| Send high-volume, painful workflows to redesign rather than polishing the prompt | A popular entry hits limits | Where the process, not the prompt, is the constraint (transformation-advisor skill) |

## 7. Checklist and decision rules

**Checklist:** intake route; triage; test on real cases; owner; reviewer; data rule and risk tier; versioning
(change log); discoverability (index, announcements); reuse signal; review triggers; retirement.

**Decision rules**
- No approval without a named human checkpoint, a passed test by someone other than the author, and a known data
  rule.
- `data_rules: "unknown"` keeps the entry at `candidate` and goes to the ai-governance skill.
- Library entries are `assist` or `augment`. If no person would be on the normal path, route it to the
  ai-solution-delivery skill.
- Name a tool only if `overlay/tool-catalog.yaml` lists it; otherwise describe the runtime class (core rule 6).
- When a review trigger fires, set `needs-retest`; do not leave a known-stale entry `approved`.
- Retire rather than delete, so links from measures and solutions still resolve.

## 8. Common traps

| Trap | How to avoid it |
|---|---|
| A dumping ground of untested prompts | Lifecycle and test standard (§4, §5) |
| Entries with no checkpoint, so review becomes a rubber stamp | `human_checkpoint` required and tested |
| Stale entries after a model or policy change | `review_when` triggers; `needs-retest` |
| Only the central team contributes | Crowd and champion intake; credit contributors' teams |
| Client data in examples | Sanitize; examples labelled illustrative |
| Polishing prompts for a broken process | Route to the transformation-advisor skill |

## 9. Worked example

*Illustrative; the firm and figures are invented.* In the accounting firm's tax practice a senior's prompt for drafting
replies to routine notices circulates by email. A champion turns it into a procedure: AI drafts from the notice, the
return and a sanitized summary of the file; the senior checks figures; the manager checks every cited rule against
the source before signing. Data rule from governance: client identifiers stay out unless the tool is approved for
client data. A manager who did not write it tests twelve past notices; ten drafts are usable after the checkpoint, and
two cited the wrong period, both caught. The reviewer approves it as `notice-response-draft`, origin `champion`,
review triggers "tool or model changes", "notice format changes" and "data rule changes". When the practice later
moves to a new assistant, the entry goes to `needs-retest`. Separately, the volume of notices and the hand
re-keying around them suggest a process problem; the user takes that workflow to the transformation-advisor skill.

## 10. Output

- **`enablement/workflows/<id>.md`** for each entry, from `references/templates/workflow.md` (schema
  `schemas/workflow.md`).
- **`enablement/program.md`**, section 5: library rules and the index table (id, title, roles, kind, status, owner,
  checkpoint).
- **`enablement/measures.yaml`**: `links.workflows` on the `embedded` measures.
- Frontmatter: `step_completed: 5`, `next_step: 6`, `updated`.

## 11. Sources

- `ARXIV-MAGESH-2024`: *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, Magesh et al., arXiv 2405.20362, 2024-05-30. https://arxiv.org/abs/2405.20362
- `HARVEY-CHAMPIONS-2026`: *Harvey Power Users: The Champions Network*, Harvey blog, vendor-published, 2026-06-02. https://www.harvey.ai/blog/harvey-power-users-the-champions-network
- `HARVEY-GOWLING-2025`: *Al Hounsell on Driving Legal Transformation That Lasts*, Harvey blog, vendor-published, 2025-10-30. https://www.harvey.ai/blog/al-hounsell-on-driving-legal-transformation-that-lasts
- `HBS-JAGGED-2023`: *Navigating the Jagged Technological Frontier* (summary), Harvard D^3 Institute with BCG, 2023-09-21. https://d3.harvard.edu/navigating-the-jagged-technological-frontier/
- `MOLLICK-LAB-2025`: *Making AI Work: Leadership, Lab, and Crowd*, One Useful Thing, 2025-05-22. https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- `MSLEARN-COE-ND`: *Establish an AI Center of Excellence*, Microsoft Learn, undated. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence
- `OPENAI-ENTGUIDE-ND`: *AI in the Enterprise*, OpenAI, vendor guide, undated. https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf
- `OPENAI-MSTANLEY-ND`: *Morgan Stanley uses AI evals to shape the future of financial services*, OpenAI, vendor case study, undated. https://openai.com/index/morgan-stanley/
- `WBD-CHAMPIONS-ND`: *Our technology solutions* (AI Champions section), Womble Bond Dickinson, undated. https://www.womblebonddickinson.com/us/about/our-technology-solutions

Archetype use cases cited (grades as recorded): `professional-services-knowledge-management-18`, `-23`;
`professional-services-work-production-23`; `assurance-quality-management-02`
(`../../transformation-advisor/references/archetypes/index.md`).
