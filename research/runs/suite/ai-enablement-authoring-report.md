# Authoring report: ai-enablement

Prepared 2026-10-20. Skill folder: `plugins/ai-transformation/skills/ai-enablement/`. Validator
(`python3 scripts/validate.py`): 0 errors; the 23 warnings are all pre-existing use-case target warnings in the core
skill's archetypes, none in this skill.

## 1. Files written

| File | Lines | Fed by |
|---|---|---|
| `SKILL.md` | 237 | Spec §2-5; core `SKILL.md` structure and voice; core-rules block (word for word, with markers); topic-enablement §1, §8; topic-partners §1 |
| `references/assess-and-segment.md` (step 1) | 202 | topic-enablement §2 (concepts 1, 4, 6), §3 moves 1-5, 17, §4, §5, §6 E7-E10, E12-E14, §8.1; core `library/journey-stages.md` (pointer) |
| `references/program-design.md` (step 2) | 201 | topic-enablement §2 (3, 10), §3 moves 6, 7, 20, 26, 28, §5, §6 E3-E6, E8, E11-E12, E21, E27, §8.2; topic-partners moves 4, 13, 15, 16; use cases `professional-services-talent-learning-01/-03/-15/-16`, `professional-services-knowledge-management-18`, `professional-services-work-production-22` |
| `references/curriculum.md` (step 3) | 184 | topic-enablement §3 moves 14-17, §5, §6 E2, E9, §8.3; topic-partners move 14; core `people-and-change.md` §6 (pointer); use cases `professional-services-talent-learning-01/-02/-06/-09`, `assurance-quality-management-10` |
| `references/champions-and-community.md` (step 4) | 177 | topic-enablement §2 (5, 7, 8), §3 moves 8-11, 27, §6 E17-E19, §7 examples 1-2, §8.4; topic-partners moves 2, 3, 12, 24; use cases `professional-services-talent-learning-02`, `professional-services-work-production-17`, `tax-research-advisory-07` |
| `references/workflow-library.md` (step 5) | 182 | topic-enablement §3 moves 13, 24, 25, 27, §6 E22-E23, §8.5, §10; topic-partners E14; use cases `professional-services-knowledge-management-18/-23`, `professional-services-work-production-23`, `assurance-quality-management-02` |
| `references/partners-and-skeptics.md` (step 6) | 223 | topic-partners §1-8 (most moves, the briefing structure, objection types, worked examples A-D); topic-enablement §3 moves 21-23, §8.7; archetype `objections.md` files (pointers) |
| `references/measure-adoption.md` (step 7) | 189 | topic-enablement §3 moves 2, 18, 19, 25, §5, §6 E12-E15, E26, E31, §7 example 3, §8.6, §10; topic-partners E2, move 28; use case `professional-services-talent-learning-16` |
| `references/templates/program.md` | 100 | Spec §4; topic-enablement §8 template fields; topic-partners stakeholder and objection fields |
| `references/templates/workflow.md` | 76 | topic-enablement §8.5 library entry fields |
| `references/templates/measures.yaml` | 42 | topic-enablement §8.6 metric template |
| `references/schemas/measures.md` (measures/v1) | 182 | topic-enablement §8.1, §8.6; shared `vocabulary.yaml` |
| `references/schemas/workflow.md` (workflow/v1) | 106 | topic-enablement §8.5; shared `vocabulary.yaml` |
| `references/briefs/draft-workflow-entry.md` | 47 | Core brief format (`analyze-document.md`) |
| `references/library/index.md` | 7 | Redirect stub (see §3) |
| `references/method/people-and-change.md` | 8 | Redirect stub (see §3) |

Worked examples use one invented 400-person accounting firm (audit, tax, advisory) across all seven steps,
labelled illustrative, with real practices cited separately.

## 2. Conflicts resolved

- **Stakeholder mapping versus core rule 1.** The research's stakeholder card has "person or group" and "name or role".
  Rule 1 bars actions about named individuals. Resolved: map roles and groups only; if the user names someone, keep
  the name out of the files and offer the group-level move. Champions are chosen by the user; files record them by group
  and role (a name only as an action owner, if offered, matching core `people-and-change.md` §2).
- **Fluency check and league tables versus rule 1.** The research recommends hands-on skill tests and reports Lewis
  Silkin's league tables. Resolved: fluency checks are anonymous or reported by group, with suppression below a minimum
  group size set by the firm's HR or privacy lead (no number invented); team-level recognition instead of individual
  rankings. Firm practices such as KPMG's reviews and Accenture's login tracking are reported as what firms do, and the
  skill states it helps design what a measure rewards but never rates anyone.
- **Per-person telemetry versus rule 5.** The skill asks for aggregates by team and level, never per-person exports.
- **Prompt craft.** Mollick (prompts matter less) versus Section (21% write an effective prompt). Kept both, flagged
  the conflict, and taught framing, decomposition and checking, verified with a hands-on check.
- **Calendar language in the research** ("success obvious in 90 days", "visible win within one quarter", "12 months",
  "time-box pilots", "retire-by date"). Replaced with dependencies and conditions: targets carry `after` (a
  dependency), workflows carry `review_when` triggers, and the central team steps back on a stated condition.
- **The research's "(synthesis)" labels** became "advisor's working set", "advisor's judgment" or "working rule"
  (the word is barred in product files). The vocabulary id `research-synthesis` still appears where a work type is
  listed; it is a controlled value.
- **Thresholds.** The research's 25-point leader-frontline gap is kept, labelled a rule of thumb. The discount for
  self-reported time saved is a range agreed with the user and labelled judgment; HMRC's ~20% is cited as one reference
  point, not a standard. The example uses 20-50%, marked illustrative.
- **Provenance of a few items** was narrowed against the source wording: Section's 42 versus 33 is "Section's scoring",
  not a named index; the lunch-and-learn formats are attributed to "law firms in a Law360 report", not to Michael
  Best; Australia's 40% "reallocated time" carries no respondent base.

## 3. Gaps and notes for the owner

- **Core-rules paths.** Rules 6 and 8 point to `references/library/index.md` and
  `references/method/people-and-change.md`, which resolve from the core skill only. The sibling skills solved this with
  small redirect files; this skill does the same (two stubs pointing to the core files). A cleaner fix would be to make
  those two paths skill-neutral in `core-rules.md` (for example `../transformation-advisor/references/...`) and update
  every copy at once.
- **Leading-partners method file.** Another author is adding one to the core skill. Step 6 points to the archetype
  objections files and core `people-and-change.md`; once the new file lands, add a pointer in
  `references/partners-and-skeptics.md` §2 step 7 or §5 (not added now, since the file did not exist when this was
  validated).
- **Evidence gaps carried into the skill (rule 14):** no independent evidence on champion-network effect sizes, library
  curation or retirement practice, partner-specific adoption, retention beyond about a year, or training format
  effects. The skill says so and routes the user to their own measures.
- **Validator coverage.** It does not parse schema examples in skill-owned schema files; both examples were parsed by
  hand and checked against `vocabulary.yaml`.
- **Program frontmatter** (`program/v1`) is documented in the template rather than a separate schema file, because it
  is not a YAML file; say if you want a `schemas/program.md` like the core `plan.md`.

## 4. New vocabulary proposed

None added to the shared `vocabulary.yaml`. Controlled values defined and used only inside this skill's files
(listed in `references/schemas/measures.md` §3 and `references/schemas/workflow.md` §3):

| Field | Values | File |
|---|---|---|
| `layer` | reach, activity, depth, embedded, outcome, sentiment, side-effect | measures/v1 |
| `method` | telemetry, survey, sampled-work, records, comparison | measures/v1 |
| `depth` | not-using, one-off, repeatable, builder | measures/v1 |
| `main_barrier` | access, use-case, time, permission, security, belief, fear, none | measures/v1 |
| `manager_behaviour` | none, encourages, requires, unknown | measures/v1 |
| `kind` | prompt, skill, procedure | workflow/v1 |
| `status` | candidate, testing, approved, needs-retest, retired | workflow/v1 |
| `origin` | crowd, champion, central, solution | workflow/v1 |

Schema ids introduced: `measures/v1`, `workflow/v1`, `program/v1`. Shared ids reused: `value_levers`, `provenance`,
`work_types`, `patterns`, `ladder`, `runtime_classes`, `journey_stages`.

## 5. Open questions for the owner

1. Should the depth ladder ids (`not-using` … `builder`) move into the shared vocabulary, so the advisor's journey-stage
   markers and ai-portfolio's benefits can use them?
2. Should ai-solution-delivery write `enablement/workflows/<id>.md` directly (as the spec's handoff implies) using
   `workflow/v1`, or hand a draft to this skill to test and approve? The schema allows `origin: solution` either way.
3. Is a minimum reporting group size something the overlay (ai-governance) should set, so every skill uses the same
   number?
4. Do you want the two redirect stubs replaced by a change to the core-rules paths (§3)?
