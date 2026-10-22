# The workflow library (step 5)

Read this on entering step 5. It sets up how reusable workflows (prompts, skills and procedures) are captured, tested,
curated and retired, per role, each with its human checkpoint. The library is how one person's gain becomes the
group's default way of working. Source keys in brackets are listed in §6.

## 1. Goal and exit criteria

**Goal.** A small, trusted set of workflows per role that people can find, that have been tested on real cases, that
name who checks the output, and that are retired when they stop being right.

**Exit when all of these are true:** library rules written (who can add, who reviews, the test standard, what approval
means, data rules, review triggers, retirement); intake routes (any user, champions' capstones, the central team,
launched solutions); first entries as `enablement/workflows/<id>.md`, at least one per target workflow from step 2,
each with a human checkpoint and a data rule (or `data_rules: "unknown"` and status `candidate`); an index in
`program.md` section 5; a reuse signal (how you will know a workflow is used beyond its author); routes out
(redesign to transformation-advisor; no person on the normal path to ai-solution-delivery).

## 2. How to run it

1. **Collect what the crowd already uses:** "Which prompts, skills or procedures do people already pass around, and
   where do they live?" Mollick's "lab" takes crowd solutions, distributes them quickly, and tests and measures them
   [MOLLICK-LAB-2025]. Champion capstones are a steady supply with an owner [WBD-CHAMPIONS-ND].
2. **Triage** each candidate: reusable, a common task, a known data rule, `assist` or `augment`? Anything that would
   run unattended is a solution, not a library entry.
3. **Write the entry** from `references/templates/workflow.md`, checkpoint first: "For this workflow, who checks the
   output, against what, before it is used or leaves the team?" Then the data rule: "Which data may go in, under
   which rule, and which client terms apply?" Unknown keeps it at `candidate` and goes to ai-governance.
4. **Test it** (§4), run by someone other than the author. **Approve** only with a reviewer, a passed test and a known
   data rule; otherwise send it back.
5. **List it** in the index and tell the groups it serves (clinic, spotlight). Ask how people find workflows today and
   how you would know anyone else used one.
6. **Set review triggers:** "What would make this workflow wrong: a tool change, a rule change, a new template?"
7. With several source documents or prompt collections, use the `draft-workflow-entry` brief (SKILL.md, Delegation)
   and confirm each draft with the user.

## 3. The lifecycle

`candidate` (anyone submits task, role, steps and a proposed checkpoint) → `testing` (a tester who is not the author
runs real, sanitized cases) → `approved` (a reviewer role lists it; reuse is tracked) → `needs-retest` (a review
trigger fired; the owner re-runs the test) → `retired` (withdrawn with a reason; the file is kept so links from
measures and solutions resolve). Never leave a known-stale entry `approved`. Field rules: `schemas/workflow.md`.

**Kinds:** `prompt` (a pattern a person adapts), `skill` (packaged and used the same way across a team; the
`shared-team-skills` runtime class), `procedure` (written steps mixing AI and manual work and checks).

**Precedents.** Law firms report knowledge teams curating approved tools, use cases and playbooks in one place
(`professional-services-knowledge-management-18`, grade B). Audit firms and regulators describe risk-tiered
permitted-use policies, including a curated prompt library (`assurance-quality-management-02`, grade B).

## 4. Testing an entry

- **Real cases, sanitized,** unless the tool is approved for that data. Never paste client-confidential data into the
  workflow file itself.
- **A reference answer.** Compare output with what an expert produced or would accept; firms test tools on their own
  work against an expert baseline and re-test when tools change (`professional-services-work-production-23`, grade
  B). Official benchmarks rarely test your own kind of work [MOLLICK-LAB-2025].
- **Test the checkpoint too.** Plant a known error and confirm the checkpoint as written would catch it. Leading legal
  research tools hallucinated 17% to 33% of the time in a preregistered 2024 study (independent) [ARXIV-MAGESH-2024];
  a checkpoint that does not open the sources would miss that.
- **Record where it fails.** AI helps inside its capability and not uniformly outside it [HBS-JAGGED-2023]; the
  entry's "Do not use it for" section comes from the failures.
- How many cases are enough is the reviewer's judgment; write the number and reason in `tested.notes`. No published
  standard was found.

## 5. Rules of thumb, example and output

- Track reuse and last-tested dates as the guard against stale entries; evidence on curation and reuse rates is thin.
- Send high-volume, painful workflows to transformation-advisor rather than polishing the prompt.
- **Traps:** a dumping ground of untested prompts; entries with no checkpoint, so review becomes a rubber stamp; only
  the central team contributes; client data in examples.

*Illustrative (invented).* A champion turns a circulating prompt for routine tax notice replies into a procedure: AI
drafts from the notice, the return and a sanitized file summary; the manager checks every figure and cited rule
against the source before signing. A manager who did not write it tests twelve past notices: ten usable, two cited
the wrong period, both caught. It is approved as `notice-response-draft`; a later tool change sends it to
`needs-retest`.

**Output:** `enablement/workflows/<id>.md` per entry; `program.md` section 5 (library rules and the index: id, title,
roles, kind, status, owner, checkpoint); `links.workflows` on the `embedded` measures; frontmatter
`step_completed: 5`, `next_step: 6`, `updated`.

## 6. Sources

- `ARXIV-MAGESH-2024`: *Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools*, Magesh et al., arXiv 2405.20362, 2024-05-30. https://arxiv.org/abs/2405.20362
- `HBS-JAGGED-2023`: *Navigating the Jagged Technological Frontier* (summary), Harvard D^3 Institute with BCG, 2023-09-21. https://d3.harvard.edu/navigating-the-jagged-technological-frontier/
- `MOLLICK-LAB-2025`: *Making AI Work: Leadership, Lab, and Crowd*, One Useful Thing, 2025-05-22. https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- `WBD-CHAMPIONS-ND`: *Our technology solutions* (AI Champions section), Womble Bond Dickinson, undated. https://www.womblebonddickinson.com/us/about/our-technology-solutions
- Archetype use cases (grades as recorded): `../../transformation-advisor/references/archetypes/index.md`.
