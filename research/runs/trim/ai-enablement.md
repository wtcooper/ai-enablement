# Trim report: ai-enablement

Moderate trim per `brief.md`. The step structure (profile plus steps 1-7) and the file set are unchanged; no file
was deleted or merged. Base for "before": commit `2e82c6d`. A later checkpoint commit by another session
(`474c957`) swept part-way edits into history; I made no commits.

Checks: `python3 scripts/validate.py` reports 0 errors (the 31 warnings are archetype content targets, as before).
`claude plugin validate --strict plugins/ai-transformation` passes. Both schema examples, `templates/measures.yaml`
and the frontmatter of both templates and of `SKILL.md` parse with a loader that rejects duplicate keys. Every
source key cited in a step file is listed in that file's Sources, and every listed key is cited. All 12 archetype
use-case grades cited match `evidence_grade` as recorded.

## Line counts

| File | Before | After | Words before → after |
|---|---|---|---|
| `SKILL.md` | 246 | 158 | 2,533 → 1,686 |
| `references/assess-and-segment.md` | 202 | 98 | 2,566 → 1,199 |
| `references/program-design.md` | 204 | 100 | 2,492 → 1,258 |
| `references/curriculum.md` | 185 | 97 | 2,063 → 1,098 |
| `references/champions-and-community.md` | 177 | 92 | 2,036 → 1,061 |
| `references/workflow-library.md` | 183 | 89 | 1,916 → 968 |
| `references/partners-and-skeptics.md` | 228 | 90 | 2,713 → about 1,040 |
| `references/measure-adoption.md` | 191 | 98 | 2,092 → 1,123 |
| `references/schemas/measures.md` | 203 | 149 | 1,521 → 1,076 |
| `references/schemas/workflow.md` | 106 | 85 | 824 → 689 |
| `references/templates/program.md` | 100 | 93 | 673 → 567 |
| `references/templates/workflow.md` | 76 | 76 | unchanged |
| `references/templates/measures.yaml` | 42 | 42 | unchanged |
| `references/briefs/draft-workflow-entry.md` | 47 | 47 | unchanged |
| **References total** | **1,944** | **1,156 (−41%)** | **19,922 → about 11,100 (−44%)** |

Only `schemas/measures.md` is still over 100 lines, and it keeps its contents list. The other files are at or under
100 lines, so they no longer need one.

## What I cut or merged, and why

**SKILL.md (246 → 158).** The core-rules block is byte for byte the same. Rules 10-14 are kept and reworded more
briefly. "How to talk" now holds only what is specific to the skill: records rather than self-ratings, one early
example with its provenance, and partner vocabulary. One question at a time, play-back and naming the step are
already in `interviewing.md`, which the section tells the reader to read first. Start or resume is compressed. Each
step is one paragraph (Read now, goal, exit, output). Steps 1 and 2 keep their core questions; for steps 3-7 the
questions now live only in the step files, which the skill reads on entry. Handoffs use one fallback sentence
(`../<skill>/SKILL.md`) in place of four. Delegation is prose rather than a table. The Reference map is removed,
because every path it held is already named where it is used; its "read each index first" line moved to the steps
intro. Kept unchanged in meaning: the save rule, the YAML quote-and-parse check, the duplicate-key sentence (FIXES N6),
`origin: solution` for workflows from launched solutions, and the rule that the user may jump to any step.

**Step files (all seven).** These were cut in the same way in each file:
- The separate question-bank table is merged into "How to run it", with each question quoted at its step.
- "Expert moves", "Checklist and decision rules" and "Common traps" are merged into one "Rules of thumb" list. Moves
  that repeated the run steps are dropped, and the traps are one line.
- The worked examples are cut to three to five lines each.
- The scope tags (`[T]`, `[U]`, `[O]`) and the contents lists are removed. The tags drove nothing in the skill, and
  the files are now 100 lines or fewer.
- The per-file lists of cited archetype use cases are replaced by a pointer to the archetype index. The ids and
  grades stay inline where they are cited.

**partners-and-skeptics.md (228 → 90).** This file now points to
`../../transformation-advisor/references/method/leading-partners.md` for partner economics, the stakeholder-map
columns, the briefing structure, the graded objection answers, leader expectations, extra questions and traps. That
material and its sources were duplicated there. The file keeps what is specific to enablement:
- the exit criteria and the program section it writes;
- how rule 11 applies when a partner is named;
- the objection-log columns and the five objection types;
- "which tasks would you hand off";
- the expert-graded evaluation;
- peer demonstration combined with an expectation;
- the rule to resolve an objection once when three or more groups raise it;
- the workslop check;
- routing senior people to step 4's forums.

**Schemas.** `measures.md`: the "Controlled values used only here" table is folded into comments on the format, with
pointers to the ladder (step 1 §3) and the layers (step 7 §3). The field rules are merged; for example, the discount
rule and the measured-versus-estimated rule became one bullet. The example now has one segment and two measures,
`embedded-workflows` and `time-saved-self`, which show `links.workflows` and `discount`. Before, it had two segments
and three measures. `workflow.md`: the controlled-values table is folded into comments and a pointer to the lifecycle
(library §3). No fields were removed from either schema. The cross-skill fields (`risk_tier`, `links.solution`,
`links.benefit`, `links.opportunity`, `lever`, `origin: solution`) and the tool field are unchanged.

**Templates.** Only the section comments in `program.md` are shorter. The workflow template, the measures template
and the brief are unchanged.

**Claims and sources removed with the claims they backed:**
- `ZAPIER-2026` (fluency model), `HARVEY-GOWLING-2025` in step 1 ("adoption depth"), the Lewis Silkin monthly and
  weekly split, the gender-gap equity check (`HUMLUM-BFI-2025` in step 1 only), and the task-fit segmentation note
  (`NBER`/`HBS` in step 1 only).
- `DECRYPT-ACCENTURE-2026`, plus `CPAPA-PWC-2026` and `CIPD-2026` in step 2 (both are kept in the advisor's
  leading-partners method).
- `DTA-2024` and `KPMG-PULSE-2025` in step 3, `KENNEDYS-SPELLBOOK-ND`, and Wharton's fall in training investment.
- `HARVEY-LEWISSILKIN-2025`, the competition judging criteria, and `professional-services-work-production-17` in step 4.
- `MSLEARN-COE-ND`, `OPENAI-ENTGUIDE-ND` (BBVA), `OPENAI-MSTANLEY-ND` and `HARVEY-*` in step 5, and
  `professional-services-knowledge-management-23`.
- `ANTHROPIC-ECONIDX-2025`, `HUMLUM-BFI-2025`, `SECTION-2026` and `MOLLICK-LAB-2025` in step 7.
- In step 6, every partner-method source now covered by leading-partners §12: `JOTWELL-EMPSON`, `LF-PERLIN`,
  `ACCTAGE`, `ICAEW-CAW`, `BLOOMBERG-ACC`, `TRI-AIPS`, `LAWNEXT`, `LEGALCHEEK-BAKER`, `NONBILLABLE-AO`, `PAPERJAM`,
  `AO-AGENT`, `IAB-KPMG`, `VINCI`, `PROSCI-ADKAR`, `GAWANDE`, `ARXIV-MAGESH`, `HBS-DELLACQUA`, `PEOPLEMATTERS`,
  `POLSINELLI`, `LEXIS-CONSULT`, `MOLLICK-LAB` and `CIPD`.

A source is removed from a file only when nothing left in that file cites it.

## Deferred features

Each line says what the feature would add back and when it would be worth it.

- **Scope tags on questions (`[T]`/`[U]`/`[O]`):** filtering the questions by scope. Worth it once the skill runs at
  team level often enough that firm-level questions get in the way.
- **Full question banks per step (about 8-12 questions each):** more follow-ups. Worth it if test runs show the skill
  running out of questions or asking generic ones.
- **Equity check by grade, location and gender (Humlum gender gap):** an uneven-take-up lens in step 1. Worth it when a
  firm already reports these splits in aggregate and asks about inclusion.
- **Competition and junior-to-partner showcase as separate forums:** a richer forum catalogue in step 4. Worth it when
  a firm has run spotlights and clinics and wants new formats.
- **Simulated practice environments (Kennedys) and training-spend trend (Wharton):** more junior-route and funding
  material in step 3. Worth it for firms designing a graduate programme around AI.
- **Depth signal from task delegation (Anthropic Economic Index):** a further depth indicator in step 7. Worth it when
  a firm has conversation-level telemetry it can sample.
- **Per-step checklists:** a quick audit list beside the exit criteria. Worth it if reviewers find exits missed in runs.
- **A third measure and second segment in the measures example:** a fuller worked example. Worth it if runs write
  malformed `activity` measures.
- **Partner-specific evidence duplicated locally (economics, briefing, graded objections):** step 6 working without
  reading the advisor file. Worth it only if a test run shows the skill skipping the pointer.

## Kept, though a reader might expect it cut

- **Rule 14 (no independent evidence on champions, curation, partner adoption, retention):** shown to users, and step 4
  and step 7 rely on it.
- **The `sentiment` and `side-effect` layers:** step 7's exit requires a side-effect check (rework), and the
  layer ids are in the schema enum.
- **Both HMRC and UK GDS figures in step 7:** together they are the evidence for the discount rule, which is what the
  skill does.
- **The objection-type table in step 6:** the objection log's `type` column needs it, and it is shorter than
  sending the reader to leading-partners §5 for every type.
- **`scope.parent` in the program template:** it matches the advisor's scope shape, and it is one inline field.
- **The `draft-workflow-entry` brief, unchanged:** a subagent gets only the brief, so it needs the vocabulary ids
  written out.
- **The SOP-analysis delegation for steps 3 and 5:** it is in use in the suite and costs two lines.

## Shared files that need a change

None are required. One note: the advisor's `leading-partners.md` now carries the partner method for both skills, so a
future change to its section numbers (§2, §3, §4, §5, §6, §8, §9, §12) should also update
`ai-enablement/references/partners-and-skeptics.md`.
