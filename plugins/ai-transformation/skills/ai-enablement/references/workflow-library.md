# The workflow library (step 5)

Read this on entering step 5. It sets up how reusable workflows (prompts, skills and procedures) are captured, tested,
curated and retired, per role, each with its human checkpoint. The library is how one person's gain becomes the
group's default way of working. Source keys in brackets are listed in §8.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [The lifecycle](#4-the-lifecycle)
5. [Testing an entry](#5-testing-an-entry)
6. [Rules and traps](#6-rules-and-traps)
7. [Worked example and output](#7-worked-example-and-output)
8. [Sources](#8-sources)

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
- **Routes out:** workflows worth redesigning go to transformation-advisor; workflows that should run without a person
  on the normal path go to ai-solution-delivery.

## 2. How to run it

1. **Collect what the crowd already uses** (L1), then centralize the best: Mollick's "lab" takes crowd prompts and
   solutions, distributes them quickly, and tests and measures them [MOLLICK-LAB-2025]. Champion capstones are a
   steady supply with an owner [WBD-CHAMPIONS-ND].
2. **Triage** each candidate: reusable, a common task, a known data rule, `assist` or `augment`? Anything that would
   run unattended is a solution, not a library entry.
3. **Write the entry** from `references/templates/workflow.md`. Fill `human_checkpoint` and `data_rules` first.
4. **Test it** (§5) on real, sanitized cases, run by someone other than the author.
5. **Approve or send back.** Approval needs a reviewer, a passed test and a known data rule.
6. **List it** in the index and tell the groups it serves (clinic, spotlight).
7. **Set review triggers** and the reuse signal; retire entries that fail them.
8. With several source documents or prompt collections, use the `draft-workflow-entry` brief (SKILL.md, Delegation)
   and confirm each draft with the user.

## 3. Question bank

| # | Question | Notes |
|---|---|---|
| L1 | Which prompts, skills or procedures do people already pass around? Where do they live? | Crowd supply |
| L2 | Who can add a workflow, who reviews it, and how is it tested before others rely on it? | Library rules |
| L3 | For this workflow, who checks the output, against what, before it is used or leaves the team? | The human checkpoint |
| L4 | Which data may go in, under which rule, and which client terms apply? | Data rule, from governance |
| L5 | How do people find a workflow today? How would you know anyone else used it? | Discoverability and reuse |
| L6 | What would make this workflow wrong: a tool change, a rule change, a new form or template? | Review triggers |
| L7 | Which workflow would you declare the default way for that task, and who signs that off? | Embedded use |

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

**Precedents.** Law firms report knowledge teams curating approved tools, use cases and playbooks in one place
(`professional-services-knowledge-management-18`, grade B). Audit firms and regulators describe risk-tiered
permitted-use policies, including a curated prompt library (`assurance-quality-management-02`, grade B).

## 5. Testing an entry

- **Real cases, sanitized.** Use past work with client and personal details removed, unless the tool is approved for
  that data. Never paste client-confidential data into the workflow file itself.
- **A reference answer.** Compare output with what an expert produced or would accept. Firms test tools on their own
  work against an expert baseline and re-test when tools change (`professional-services-work-production-23`, grade
  B). Official benchmarks rarely test your own kind of work; build your own small set [MOLLICK-LAB-2025].
- **Someone other than the author** runs the test and records cases, passes and what failed.
- **Test the checkpoint too.** Plant a known error and confirm the checkpoint as written would catch it. Leading legal
  research tools hallucinated 17% to 33% of the time in a preregistered 2024 study (independent) [ARXIV-MAGESH-2024];
  a checkpoint that does not open the sources would miss that.
- **Record where it fails.** AI helps inside its capability and not uniformly outside it [HBS-JAGGED-2023]; the entry's
  "Do not use it for" section comes from the failures.

How many cases are enough is the reviewer's judgment; write the number and the reason in `tested.notes`. No published
standard was found.

## 6. Rules and traps

- No approval without a named human checkpoint, a passed test by someone other than the author, and a known data rule.
  Ask for the checkpoint before the prompt.
- `data_rules: "unknown"` keeps the entry at `candidate` and goes to ai-governance.
- Library entries are `assist` or `augment`. If no person would be on the normal path, route it to
  ai-solution-delivery.
- When a review trigger fires, set `needs-retest`; do not leave a known-stale entry `approved`. Retire rather than
  delete, so links from measures and solutions still resolve.
- Track reuse and last-tested dates as the guard against stale entries; evidence on curation, retirement and reuse
  rates is thin.
- Send high-volume, painful workflows to transformation-advisor rather than polishing the prompt.
- **Traps:** a dumping ground of untested prompts; entries with no checkpoint, so review becomes a rubber stamp; only
  the central team contributes; client data in examples.

## 7. Worked example and output

*Illustrative; the firm and figures are invented.* A senior's prompt for replies to routine tax notices circulates by
email. A champion turns it into a procedure: AI drafts from the notice, the return and a sanitized file summary; the
manager checks every figure and cited rule against the source before signing. A manager who did not write it tests
twelve past notices; ten drafts are usable, and two cited the wrong period, both caught. It is approved as
`notice-response-draft` (origin `champion`); a later tool change sends it to `needs-retest`. The volume of notices and
the hand re-keying around them go to transformation-advisor.

**Output:** `enablement/workflows/<id>.md` for each entry (schema `schemas/workflow.md`); `program.md` section 5
(library rules and the index: id, title, roles, kind, status, owner, checkpoint); `links.workflows` on the `embedded`
measures in `measures.yaml`; frontmatter `step_completed: 5`, `next_step: 6`, `updated`.

## 8. Sources

- `ARXIV-MAGESH-2024`: *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, Magesh et al., arXiv 2405.20362, 2024-05-30. https://arxiv.org/abs/2405.20362
- `HBS-JAGGED-2023`: *Navigating the Jagged Technological Frontier* (summary), Harvard D^3 Institute with BCG, 2023-09-21. https://d3.harvard.edu/navigating-the-jagged-technological-frontier/
- `MOLLICK-LAB-2025`: *Making AI Work: Leadership, Lab, and Crowd*, One Useful Thing, 2025-05-22. https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- `WBD-CHAMPIONS-ND`: *Our technology solutions* (AI Champions section), Womble Bond Dickinson, undated. https://www.womblebonddickinson.com/us/about/our-technology-solutions

Archetype use cases cited (grades as recorded): `professional-services-knowledge-management-18`;
`professional-services-work-production-23`; `assurance-quality-management-02`
(`../../transformation-advisor/references/archetypes/index.md`).
