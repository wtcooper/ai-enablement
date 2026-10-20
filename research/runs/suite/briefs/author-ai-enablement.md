**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are the author of one skill in an Agent Skills plugin, `ai-transformation`. Today is 2026-10-20. Read first:

1. `/home/user/ai-enablement/spec/2026-10-20-skill-suite.md`: the suite design (skills, shared knowledge, workspace
   layout, handoffs, quality gates). Follow it.
2. `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/SKILL.md`: the core skill. Match its voice, structure and discipline (rules first,
   one question at a time, read-now pointers per step, save after every step, delegation table, reference map).
3. `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/schemas/core-rules.md`: the core rules block. Copy the text between the
   markers into your `SKILL.md` **word for word** (the validator checks it).
4. The shared knowledge you will point to (read the indexes, open files as needed):
   `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/method/index.md`, `.../library/index.md` (patterns, functions, journey
   stages), `.../archetypes/index.md`, `.../schemas/opportunities.md`, `.../schemas/vocabulary.yaml`.
5. Your research inputs (below). They are fact-checked research notes with source keys.

## Skill to write

**ai-enablement**: Raise AI fluency and sustained use across a firm. Steps: (1) assess and segment: who uses what, how deeply (not logins), power users, mainstream, skeptics, by practice and level, with a short fluency check; (2) design the program: goals tied to business outcomes, leader expectations, protected learning time, governance links; (3) curriculum by role and level, built around real workflows; (4) champions, office hours, clinics and communities of practice; (5) the workflow library: capture, test, curate and retire reusable workflows (prompts, skills, procedures) per role, each with its human checkpoint; (6) bring partners and skeptics along: stakeholder map, partner briefings, objection handling with the archetypes' objections files and graded evidence; (7) measure sustained adoption and impact (depth of use, embedded workflows, outcomes versus self-reported time saved, with honest discounting). Workspace files: `enablement/program.md`, `enablement/workflows/<id>.md`, `enablement/measures.yaml` (schema measures/v1). Hands off to transformation-advisor (find the workflows worth redesigning), ai-portfolio, ai-governance (approved tools and data rules).

**Research inputs:** `/home/user/ai-enablement/research/runs/suite/topic-enablement.md`, `/home/user/ai-enablement/research/runs/suite/topic-partners.md`. Also useful: `/home/user/ai-enablement/research/runs/suite/topic-partners.md` for leadership and stakeholder points.

## Files to write, in `/home/user/ai-enablement/plugins/ai-transformation/skills/ai-enablement/`

- `SKILL.md`: frontmatter `name: ai-enablement` and a `description` (at most 1,024 characters) that names the moment
  the skill is for and points to sibling skills for neighbouring moments. Body: purpose (two or three sentences);
  the core rules block; any extra rules for this skill; how to talk; start or resume (which workspace files to
  look for, and the overlay); the steps, each with goal, three to five core questions, exit criteria, output file,
  and **one "Read now" pointer**; handoffs to sibling skills by name, with the fallback "If you can't invoke a
  skill by name, read `../<skill>/SKILL.md` and follow it"; a delegation table if subagent briefs help; a
  reference map. Target 150-250 lines; never over 400.
- `references/`: one method file per step (each at most 300 lines, with a contents list if over 100 lines),
  written for an assistant to read on entering the step: goal and exit criteria, how to run it, question bank,
  expert moves (when to use, what it reveals), checklists and decision rules, common traps, a short worked
  example from a professional-services firm (accounting, tax, audit, advisory, legal or consulting), output, and
  a short Sources list (key, title, publisher, date, URL) for every research-backed claim.
- `references/templates/`: one template per workspace file the skill writes.
- `references/schemas/`: one schema file per YAML file the skill writes (format, field rules, a short example
  that parses), versioned like `opportunities/v1`. Reuse ids from the shared `vocabulary.yaml`; do not invent new
  controlled values without listing them in your report.
- Point to shared files with backtick paths like `../transformation-advisor/references/library/index.md` (from
  `SKILL.md`) or `../../transformation-advisor/references/...` (from a file in your `references/`). Every path must
  resolve.

## Rules

- Facts, figures and named examples only from the research inputs or the shared knowledge, with their source
  keys; keep provenance and modal verbs; no unsourced connective claims; quotations under 25 words.
- Evidence grades exactly as recorded where you cite archetype use cases. Describe tools by runtime class; never
  recommend a vendor. Sequence by dependencies and stages, never calendar deadlines (no 30/60/90-day plans).
- No build-process words in the product files (wave, deep dive, synthesis, verifier, research/runs paths).
- The skill designs, plans, assesses and records. It never claims to build, deploy or run anything.
- Run `python3 /home/user/ai-enablement/scripts/validate.py` and fix every ERROR in your files.

## Output

Write the files, then `/home/user/ai-enablement/research/runs/suite/ai-enablement-authoring-report.md`: files written with line counts, which inputs fed each,
conflicts resolved, gaps, any new vocabulary proposed, and open questions for the owner. Do not run git. Reply with a
summary of no more than 150 words.
