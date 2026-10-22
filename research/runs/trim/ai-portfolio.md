# Trim report: ai-portfolio

Moderate trim of `plugins/ai-transformation/skills/ai-portfolio/`, following `brief.md`. The step structure and the
file set did not change, and no file was deleted or merged. The core-rules block is byte for byte the same.

Checks:
- `scripts/validate.py` reports no errors in ai-portfolio. Its one current error is in
  `ai-governance/references/professional-duties.md`, which another agent is trimming.
- `claude plugin validate --strict` passes.
- Both schema examples and both YAML templates parse with a loader that rejects duplicate keys. The
  `portfolio.md` format block uses type notation (`a | b`) and did not parse before the trim either.
- Every `[KEY]` citation resolves to a source entry in the same file, and no file lists a source it doesn't cite.

Other sessions' checkpoint commits (`09d2b45`, `4836edd` and earlier) swept these edits into git history while I
worked. I made no commits.

## Line counts

| File | Before | After |
|---|---|---|
| `SKILL.md` | 236 | 160 |
| `references/method/setup.md` | 198 | 110 |
| `references/method/intake.md` | 221 | 136 |
| `references/method/screen-and-score.md` | 210 | 130 |
| `references/method/stage-gates.md` | 272 | 193 |
| `references/method/acquired-firms.md` | 263 | 162 |
| `references/method/portfolio-review.md` | 184 | 112 |
| `references/method/value-tracking.md` | 176 | 100 |
| `references/method/people-and-change.md` | 77 | 34 |
| `references/method/index.md` | 15 | 15 |
| `references/schemas/portfolio.md` | 251 | 200 |
| `references/schemas/benefits.md` | 127 | 115 |
| `references/library/index.md` | 126 | 81 |
| `references/briefs/prepare-review-item.md` | 45 | 45 |
| `references/templates/intake.md` | 100 | 100 |
| `references/templates/review.md` | 100 | 100 |
| `references/templates/portfolio.yaml` | 46 | 42 |
| `references/templates/benefits.yaml` | 28 | 27 |
| **Total** | **2675** | **1862** |

How much shorter each group is:
- Method files (without the index): 1601 to 977 lines, 39% shorter.
- Method, schema, library and brief files: 2165 to 1433 lines, 34% shorter.
- All of `references/`: 2439 to 1702 lines, 30% shorter.

I left the templates almost as they were, because their lines are the contract with the files the skill writes.
No file is over 200 lines; `schemas/portfolio.md` is exactly 200. Files over 100 lines keep their contents list.

## What I cut or merged, and why

- **SKILL.md (236 to 160 lines).**
  - Each step's question list and paragraph are now one paragraph: the questions, exit and output. The full
    question sets live in the method files.
  - "How to talk" is now four sentences. "Start or resume" has two items instead of three.
  - The reference map is one paragraph.
  - The optional review-opportunities brief is gone from Delegation (see Deferred features).
  - Kept word for word or nearly so: the save rule (YAML check, duplicate-key check, search before adding a field,
    `step_completed` and `next_step` matching the files, stale header comments), the write-only-the-template rule,
    the Handoffs table, the rule for when `solution` is set, and the N2 pointer.
  - Step 1 now tells the skill to propose the default stages, light path and rhythm rather than ask the user to
    configure them.
- **"Name the step" items.** I removed the opening "Name the step" item from each method file's run list (setup,
  intake, screen, review, value tracking) and merged it into gate step 1. It repeated "How to talk".
- **Question banks, expert-move tables and trap tables.** Each method file now has a few lines of questions and
  traps. I dropped questions and moves that repeated a run step or the SKILL.md questions.
- **Worked examples.** One short example per step file. The duplicated examples are gone: the proposal-drafting
  recycle, the four-row scoring table (now two rows), and the review 3 narrative (now four lines).
- **Defaults are stated once.**
  - The 3.5 quadrant thresholds: `screen-and-score.md` §3.2.
  - The monthly review with a rebalance every third review: `setup.md` §3.1.
  - The light path: `stage-gates.md` §3.2. Setup no longer describes it again, and the library only points to it.
  - The two-reviews early-warning rule: `portfolio-review.md` §3.1.

  Each is labelled as a default the user or the forum can change. The portfolio template now fills in the rhythm
  and light path defaults instead of leaving them blank, so set-up confirms them rather than asking for them.
- **Duplicate content.**
  - `stage-gates.md` §9 is now a five-point summary that points to `acquired-firms.md`. It kept its section number
    because the advisor's `acquisitions.md` links to §9.
  - The acquired-firms layer table and readiness-check table are now one table.
  - The library's stage, outcome and item-class tables, which repeated stage-gates and intake, are now short lists
    with pointers.
  - The handoff rows for governance, enablement and the advisor in `stage-gates.md` §3.3 are one row that points to
    the SKILL.md Handoffs.
- **Payback hurdles** (`screen-and-score.md` §3.4) is now one line that points to `stage-gates.md` §4, which keeps
  the Deloitte claim. The Google Cloud 74% figure and the UK GBP 10 million business-case threshold are gone.
- **Claims and sources removed** (each source entry went with its last citation):
  - BCG in setup (kept in screen).
  - Gartner 2024 and CIO Dive in setup (Gartner 2024 kept in stage-gates).
  - NAO, both times.
  - JOTWELL in setup (kept in people-and-change).
  - The MIT NANDA figures: the pilot-to-production contrast, the budget skew and the partnership deployment rate.
  - Google 2025, UK GBP 10m, HBR-2018 (moonshot), Umbrex.
  - McKinsey's 14% versus 32% workforce figure and its 1-in-5 run-cost figure.
  - DBS SGD 1bn, Bain PE growth, Partners Group, Wharton.
  - The NAO named-owner figure, and TRI in value tracking (TRI kept in review and people-and-change).
  - LexisNexis, Polsinelli.
  - Magesh (hallucination rates), Perlin (billable hour), Accountancy Age, KPMG.
  - In acquired firms: Aprio, NYSSCPA, Accountancy Europe, ICAEW, Bloomberg Tax, CFO Brew, TR Future of
    Professionals, Bain Capability, JofA culture, TechCrunch, FTI, UVA, Wolters Kluwer, Reuters, Newcomer.
- **Schema fields.**
  - `portfolio/v1`: dropped `settings.axes`, a fixed heuristic that was presented as a setting. The axes are now
    defined once, in `screen-and-score.md` §3.2, and the score rule points there.
  - `portfolio/v1`: dropped `rhythm.benefits_review`. Value tracking already reviews benefits at every review.
  - `benefits/v1`: dropped `depends_on`; dependencies between benefits were never used.
  - Fewer lines without dropping fields: `roles`, `rhythm`, `state` and `gate_paths` use flow style, and the field
    rules are shorter. Cross-skill fields (`solution`, `risk_tier`, `ai_use`, `source`, `rolled_up_from`, `label`)
    are unchanged.
- **Source lists.** Wrapped source entries are now one line each, matching the style the skill's other files
  already used.

## Deferred features

- **Tailoring by journey stage** (light path for most items when experimenting, full gates when adopting, a unit
  intake feeding one portfolio when scaling). Worth adding back once firms at different stages use the skill and
  the defaults visibly misfit.
- **Payback hurdles per item class**, plus spend thresholds that trigger heavier governance. Worth it once a
  finance lead asks for hurdle rates, or the portfolio holds large-spend items.
- **Benefit dependencies** (`benefits[].depends_on`). Worth it once one benefit regularly waits on another, for
  example platform benefits feeding use-case benefits, which is likely past about 20 live items.
- **Configurable screening axes** (`settings.axes`). Worth it only if a firm wants a dimension moved between value
  and readiness.
- **A separate benefits-review rhythm** (`rhythm.benefits_review`). Worth it if benefits need reviewing more or
  less often than the portfolio review.
- **An optional independent challenge before `g1` or `g2` on a big bet** (the advisor's `review-opportunities`
  brief, run as a subagent). Worth it once big bets reach `g2` and the forum wants a second opinion.
- **Budget split by function and spend benchmarks at rebalance** (the MIT NANDA skew; the McKinsey and Deloitte
  shares of ICT budget). Worth it once the forum asks how its AI spend compares, or a budget split is contested.
- **Partner economics at the case gates** (hours, rate, write-offs and expenses for hourly-billed work). Worth it
  for law and consulting firms whose items change billable work.
- **Wider acquired-firm guidance**: the talent argument, culture data, the platform's sample wording, the trap
  table, the scrutiny expected from UK regulators, and the cost of a platform migration per FTE. Worth it after the
  first real roll-up rollout, or for a PE-backed platform client.
- **Private-equity benchmarks in value tracking** (Bain's EBITDA growth bar, Partners Group's example). Worth it
  for a PE-owned firm that tracks an EBITDA bridge.
- **The central team moving from gatekeeper to advisor as a rebalance item, with its trap and expert move.** Only
  a short note remains, in `setup.md` §3.2. Worth expanding when a firm has a centre of excellence that has become
  a queue.

## Kept, though a reader might expect it cut

- **All of the intake import procedure** (10 steps) and **the tool-already-in-use block.** Each step came from an
  e2e fix: parsing, copying values verbatim, the capacity choice, "From the plan", grades, role labels,
  draft-to-validate, `rolled_up_from` (rounds 1 to 3, D9).
- **Field rules in `schemas/portfolio.md` that repeat the method files** (back-links, duplicates and drafts,
  capacity choice, no AI needed, solution link, provisional tier, tools in use). FIXES lists the schema as a home
  for each, so the rule lives in both places but is shorter.
- **The `risk_tier` paragraph in `library/index.md` §2, in full.** ai-solution-delivery's `solution.md` §4 links to
  it, and it carries the D4 rule for a provisional tier.
- **The `stage-gates.md` §9 section number**, so the link from the advisor's `acquisitions.md` still works.
- **The `acquired-firms.md` consent and independence detail** (AICPA file transfer, Sec. 7216, the proposed AICPA
  rules and their status, PCAOB scrutiny). These are legal claims. Shortening them further would risk misstating
  them.
- **The intake and review templates**, unchanged, because they define what the skill writes. The intake template
  holds several fixed lines (Next gate evidence, In use today, From the plan, Risk tier, AI use).
- **A new surfacing rule**: an item pending `g0` with the forum goes into the review. This is not a new feature.
  `screen-and-score.md` step 11 already said such an item "goes into the next review pack"; the rule now sits
  where the review looks.

## Shared files that need a change

None. The two inbound links still resolve:
- `transformation-advisor/references/method/acquisitions.md` links to `stage-gates.md` §9 and to
  `acquired-firms.md`.
- `ai-solution-delivery/references/schemas/solution.md` links to `library/index.md` §2.

The dropped fields `settings.axes` and `rhythm.benefits_review` appear only in old e2e run workspaces
(`evals/e2e/2026-10-21-*/workspace/portfolio/portfolio.yaml`). The skill now ignores them, so nothing breaks.
