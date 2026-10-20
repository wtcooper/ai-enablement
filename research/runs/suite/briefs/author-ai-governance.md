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

**ai-governance**: Set practical AI governance for a firm, especially one handling confidential client data and professional obligations. Steps: (1) baseline: current tools in use (sanctioned and not), data handled, existing policies, who owns what (IT, security, risk, practice leaders); (2) acceptable-use policy and data rules (data classes, which data may go to which tool tier and contract); (3) risk tiers and the human review each tier needs, mapped to the shared patterns and ladder; (4) records of AI use and auditability, proportionate to the work; (5) profession-specific duties (confidentiality, independence when buying or using AI tools, consent for tax-return information, documentation expectations in audit, bar guidance), pointing to the archetypes' `guardrails.md`; (6) vendor and tool evaluation with a repeatable scorecard (security and privacy, data retention and training, certifications, contract terms, sub-processor and model changes, exit) and the approved-tool catalog; (7) moving IT and security from risk identification to secure enablement (fast request path, review cadence). Workspace files: `overlay/policy.md`, `overlay/guardrails.md` and `overlay/tool-catalog.yaml` (the advisor already reads these two; check `../transformation-advisor/SKILL.md` and the workspace template under `/home/user/ai-enablement/templates/workspace/` for their current shape and keep compatible), `overlay/vendors/<vendor>.md`. Include a subagent brief `references/briefs/evaluate-tool.md` that fills the scorecard for one tool from public documentation. Hands off to ai-solution-delivery and ai-portfolio, and back to transformation-advisor.

**Research inputs:** `/home/user/ai-enablement/research/runs/suite/topic-governance.md`. Also useful: `/home/user/ai-enablement/research/runs/suite/topic-partners.md` for leadership and stakeholder points.

## Files to write, in `/home/user/ai-enablement/plugins/ai-transformation/skills/ai-governance/`

- `SKILL.md`: frontmatter `name: ai-governance` and a `description` (at most 1,024 characters) that names the moment
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

Write the files, then `/home/user/ai-enablement/research/runs/suite/ai-governance-authoring-report.md`: files written with line counts, which inputs fed each,
conflicts resolved, gaps, any new vocabulary proposed, and open questions for the owner. Do not run git. Reply with a
summary of no more than 150 words.
