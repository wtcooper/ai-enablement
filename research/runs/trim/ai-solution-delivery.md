# Trim report: ai-solution-delivery

Moderate trim, 2026-10-22, following `brief.md` in this folder. Only files in
`plugins/ai-transformation/skills/ai-solution-delivery/` were edited. Nothing was committed.

## Checks

- `python3 scripts/validate.py`: 0 errors, the same 31 archetype warnings. The core-rules block is byte for byte.
- `claude plugin validate --strict plugins/ai-transformation`: passed.
- All four template frontmatters, the three frontmatter formats in schema §2 and the schema §5 example parse with
  a loader that rejects duplicate keys.
- Every bracketed source key in each method file has a Sources entry, and every Sources entry is cited (checked
  by script).

## Line counts (characters in brackets)

| File | Before | After |
|---|---|---|
| `SKILL.md` | 238 (15,762) | 159 (12,149) |
| `method/frame-problem.md` | 194 (15,695) | 113 (9,618) |
| `method/build-or-buy.md` | 221 (17,053) | 137 (11,996) |
| `method/design-brief.md` | 235 (16,418) | 135 (9,277) |
| `method/eval-plan.md` | 294 (21,492) | 169 (12,698) |
| `method/readiness.md` | 239 (17,044) | 131 (10,837) |
| `method/launch-review.md` | 187 (12,580) | 117 (7,674) |
| `schemas/solution.md` | 173 (9,221) | 159 (8,431) |
| `templates/readiness.md` | 77 (2,967) | 47 (2,588) |
| `templates/brief.md`, `eval-plan.md`, `post-launch.md` | 100, 80, 42 | unchanged |
| `briefs/review-solution.md` | 49 | unchanged |
| **Method files** | **1,370 (100,282)** | **802 (62,100): −41% lines, −38% chars** |
| **All reference files** | **1,891 (125,266)** | **1,279 (85,915): −32% lines, −31% chars** |

No file is over 200 lines. Every file over 100 lines has a contents list. No files were deleted or merged.

## What was cut or merged, and why

**SKILL.md**
- Each step now has one paragraph: what to read, the goal, three or four core questions, and its exit and
  output. Before, each step had a goal line, five questions and a separate exit block. The full exit criteria
  live in the method files.
- Rules 13 (no go-live without …) and 14 (the professional stays accountable) overlapped, so they are now one
  rule, 13. The old rule 15 is now rule 14. Only `design-brief.md` cited a rule by number (rule 12), and that
  number did not change.
- "How to talk" is one paragraph. Start or resume is shorter, but keeps every handoff condition. The Delegation
  wording is shorter. The reference map lists folders instead of every file.
- The save rule is kept in full: tick a step only when its exit criteria are met, the YAML check, the
  duplicate-key check, and the rule for files written by sibling skills. Brief-open and `solution` handback,
  Handoffs and "where the steps meet the gates" are also kept unchanged.

**Method files (the same cuts in all six)**
- Removed the **Question bank** sections. The core questions are in SKILL.md, and each check table has an "Ask"
  column.
- **Expert moves** and **Common traps** repeated the checks and decision rules, usually citing the same source a
  second or third time. Each claim is now stated once, in the checks, criteria or decision rules. A few traps
  survive as one line each.
- Each worked example is cut to one short paragraph or list. The facts that later steps rely on are kept: the
  owner's metric, the `configure` decision, the zero-tolerance checks, the go-with-conditions decision and the
  Review 1 decision. So is the D3 handback line in step 1.
- Intros are cut to two or three lines. Each source entry now takes one line.
- Citations that only decorated a rule (the rule cited a source but made no claim from it) were removed. Sources
  that nothing else cited were dropped:
  - build-or-buy: OPENAI-2025.
  - design-brief: ANTHROPIC-2024, UKGDS-2024, YAN-2023.
  - eval-plan: APPLIEDLLMS-2024, BOE-2023, FRC-2025, MSFT-REDTEAM, OWASP-2025, THOUGHTWORKS-2025, VALS-2025.
  - readiness: ANTHROPIC-2026, BCG-2024, GOOGLE-2021, OWASP-2025, UKGDS-2024.
  - launch-review: ANTHROPIC-2024, ANTHROPIC-2026, APPLIEDLLMS-2024, GOOGLE-RULES.

**Merges that remove repetition**
- The runtime-class tables in build-or-buy §3.3 and design-brief §3.1 are now one table in build-or-buy §3.3,
  with columns for fit, flow and checkpoint, and main risk. Design-brief §3.1 points to it.
- The regulator documentation claims (FRC, SR 11-7, PRA SS1/23) were in both eval-plan §3.9 and readiness §3.4.
  They now appear once, in readiness §3, and eval-plan points there.
- The checklist in readiness §3 repeated the template line by line. It is now one table of what to look for,
  with sources, and the template holds the lines.
- The readiness template's five block tables are now one table with a Block column. Every line is still there.
- Schema: the `sourcing` meanings point to build-or-buy §3.1. Four one-line field rules are merged into
  "Plain rules". The State rule is shorter. The example uses a flow mapping for `owners`.

**Sourced claims cut (each sounds like a fact told to the user, but none changes what the skill does)**
- Thoughtworks moving LLM-as-a-judge to "Assess".
- Rechat's plateau before evals.
- GOV.UK Chat red-teaming with cyber experts.
- NANDA's "brittle workflows" interview accounts.
- a16z: fine-tuning looks less necessary.
- The quote "migrating prompts across models is a pain".
- Huyen: data-changing queries need approval. Read-only first is kept, with LangChain.
- BCG 70/20/10, repeated in readiness. It stays in frame-problem.
- The strongest-model cost baseline.

## Deferred features

- **Question banks per step** (team and unit/organization follow-ups): add back when user tests show the
  interview stalling after the core questions, or when the skill is used at unit or firm level more than at team
  level.
- **Expert-moves sections:** add back as coaching notes if users ask "how would an expert approach this?", or if
  reviewers find the skill missing moves the checks don't cover.
- **Full common-traps tables** (licences without use as a separate trap, autonomy creep, stale gold set,
  pricing the licence rather than the run): add back after real launches show which traps users actually hit.
- **Long worked examples** (step 2's full options table, step 5's block-by-block table, Review 1's users and
  handoffs): add back as a separate example file once a second archetype needs its own example, so step files
  stay short.
- **Five core questions per step in SKILL.md** (now three or four): add back if tests show steps 1, 3 or 6
  missing information that the dropped question used to gather. The dropped questions were "Where would an error
  be costly?", "What should it do when it doesn't know?", "What changed in the inputs?" and "What would people do
  if we took it away?". All four still appear in the method files.
- **Readiness template with a table per block:** go back to it if readiness files grow long enough that one
  table is hard to read (for example, managed-agent solutions with many systems).
- **Decorative research citations and the cut claims listed above:** add back only if a user or reviewer asks
  for evidence on that point, after checking the source again.

## Kept that a reader might expect to be cut

- **The three unchanged templates (brief, eval plan, post-launch) and the review-solution brief.** They define
  the workspace files. The brief template's header comment holds fixes 6, D5 and D7. Their section numbers are
  cited from SKILL.md and the method files: brief §1–§3, eval-plan §8 and §10.
- **Schema §4 field rules, which are long.** ai-portfolio cites §4 (`ai-portfolio/references/library/index.md`),
  and it holds the load-bearing handoff rules: the provisional tier, `ai_use: none`, the Portfolio link (D3),
  Who decides (D7), Sibling files (D5) and State (fix 6).
- **The provisional `risk_tier` rule in three places** (schema §4, design-brief §3.4 and §5). D4 named both
  files, and the design step is where it is applied. The design-brief copies point to schema §4.
- **The Make-the-case and Plan-steps paragraph in frame-problem step 1 (fix 1), and the D3 handback sentence in
  its worked example.** Both are nearly verbatim.
- **"Seen in the field"** in eval-plan, with evidence ids and grades as recorded, and
  `professional-services-firm-finance-11` in readiness. These are graded evidence the skill shows to users.
- **The pilot-first lighter readiness review** in readiness §2. This is delivery's own light path.

## Shared files that need a change

None are required. All cross-skill pointers still resolve. ai-portfolio's pointer to `solution.md` §4 is
unchanged.

One historical record now has stale section numbers. `evals/e2e/2026-10-21-suite-handoff/FIXES.md` cites
sections that have been renumbered:

| FIXES.md cites | Now |
|---|---|
| `frame-problem.md` §7 and §8 | §4 and §5 |
| `design-brief.md` §8 | §5 (§3.4 is unchanged) |
| `build-or-buy.md` §2 step 10 and §8 | §2 step 7 and §5 |

Update it only if that file is meant to stay current.
