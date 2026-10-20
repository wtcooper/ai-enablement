# Authoring report: ai-solution-delivery

Prepared 2026-10-20. Brief: `research/runs/suite/briefs/author-ai-solution-delivery.md`. All files are in
`plugins/ai-transformation/skills/ai-solution-delivery/`. No git commands were run.

## 1. Files written

| File | Lines | Fed by |
|---|---|---|
| `SKILL.md` | 231 | Spec addendum §2–§5; advisor `SKILL.md` (structure, voice, delegation wording); `core-rules.md` (block copied word for word); topic-delivery §4 (core questions), §8 (exit criteria); sibling `ai-portfolio` schema (stages, gates, `solution` back-link) and `ai-governance` schema (risk tiers) for the handoffs |
| `references/method/frame-problem.md` | 182 | topic-delivery §1, §3 moves 1–6, §4 Frame, §5 traps, §6 rows 5–6, 8, §8.1; shared pattern files (§2 "not when"); advisor `business-case.md` §7 and `prioritize.md` (running example `ct-07`) |
| `references/method/build-or-buy.md` | 213 | topic-delivery §2, §3 moves 7–11, §4 Build or buy, §5 traps, §6 rows 3, 9, 10, 12, 13, §8.2, §8.3 runtime mapping; shared `business-case.md` §3.4 (cost stack) |
| `references/method/design-brief.md` | 228 | topic-delivery §3 moves 12–16, §4 Solution design, §7A (GOV.UK Chat), §8.3; shared library §4, pattern files §3–§7, `plan-and-control.md` §3.4, `onboarding.md` §5 (delegation gates), `people-and-change.md` |
| `references/method/eval-plan.md` | 288 | topic-delivery §2, §3 moves 17–27, §4 Evaluation plan, §5 traps, §6 rows 15, 16, 18, 19, §7A, B, C, §8.4; archetype use cases `professional-services-quality-review-05` (B), `-07` (B), `assurance-quality-management-04` (C) |
| `references/method/readiness.md` | 235 | topic-delivery §3 moves 28–32, §4 Production readiness, §8.5; topic-partners §3 moves 10, 11, 14 and traps (CIPD-2026, BCG-ATWORK-2025, LAW360-2025); archetype use case `professional-services-firm-finance-11` (B) |
| `references/method/launch-review.md` | 185 | topic-delivery §3 moves 29, 33, §4 Launch and post-launch, §5 traps, §8.6; topic-partners §3 moves 6, 28 (PAPERJAM-2025); shared `plan-and-control.md` §3.3, §3.5; ai-portfolio `benefits.md` schema |
| `references/templates/brief.md` | 100 | topic-delivery §8.1–§8.3 template fields; advisor plan template |
| `references/templates/eval-plan.md` | 80 | topic-delivery §8.4 template sections |
| `references/templates/readiness.md` | 77 | topic-delivery §8.5 template fields |
| `references/templates/post-launch.md` | 42 | topic-delivery §8.6 template sections |
| `references/schemas/solution.md` | 150 | Advisor `plan.md` and `opportunities.md` schemas; shared `vocabulary.yaml`; governance tier ids |
| `references/briefs/review-solution.md` | 49 | Advisor `review-opportunities.md` brief format; topic-delivery §8.5 decision rules (NIST MS-4.2-005, independent review) |
| `references/library/index.md` | 22 | Shared library index (pointer and needs table) |
| `references/method/people-and-change.md` | 16 | Shared `people-and-change.md` (pointer) |

Validator: no errors in this skill's files except one that depends on a sibling (see §2, item 9). The core-rules
block matches. Every method file is under 300 lines with a contents list; `SKILL.md` is within the 150–250 target.
Schema examples parse with PyYAML (checked).

## 2. Conflicts resolved

1. **Calendar review points.** The research proposed 30/90/180-day post-launch reviews (topic-delivery §4, §8.6).
   That breaks rule 9. Review points are now events: the first full trace-review cycle on live work, the benefit
   horizon in the register, the portfolio rhythm, and triggers (incident, model change, metric out of range).
   Husain's two-to-four-week cycle is kept only as a trace-reading cadence.
2. **Core-rules paths.** Rules 6 and 8 point to `references/library/index.md` and
   `references/method/people-and-change.md`, which resolve from the advisor's folder only. Copying the block word
   for word into a sibling makes them unresolved. I added two short pointer files at those paths that lead to the
   shared files (ai-portfolio did the same for the library index). `SKILL.md` has one line explaining this.
3. **Source keys.** The research keys differ from keys already used in the shared files for the same sources
   (for example `ANTHROPIC-2026` and `ANTHROPIC-EVALS-2026`, `OPENAI-2025` and `OPENAI-GUIDE-2025`,
   `STANFORD-2024` and `STANFORD-MAGESH-2024`, `HBS-2023` and `HBS-DELLACQUA-2023`). I kept the research keys;
   each method file lists its own sources, so nothing is ambiguous inside a file.
4. **Rung for the running example.** The advisor's business case labels `ct-07` as `automate`; the shared
   opportunities example uses `augment`. The worked example launches at `augment` with `ladder_target: automate`
   and a written promotion rule, which follows the research's "climb one rung at a time".
5. **Runtime-class mapping.** The research's mapping of the autonomy ladder to runtime classes is the analyst's
   own (topic-delivery §10). It is labelled "advisor mapping, not from a source".
6. **Journey-stage labels.** The research used its own Explore, Pilot, Scale and Embed labels. I did not use them;
   the skill uses the shared journey stages and the ai-portfolio stages and gates.
7. **One readiness step, two gates.** The research has one readiness review; ai-portfolio has gates into pilot
   and into production. The readiness file says to run the same review at a lighter depth before a live pilot and
   in full before production (marked advisor default).
8. **Risk tiers and status values.** Risk tiers are copied from ai-governance (`tier-1` to `tier-4`), never
   defined here. Solution `status` is kept separate from the portfolio's `stage` and `status`.
9. **Pending sibling.** `SKILL.md` and the people-and-change pointer reference `ai-enablement/SKILL.md`, which did
   not exist when I last ran the validator (2 errors in my files, 1 in ai-portfolio's, all the same missing
   path). They clear once the ai-enablement skill is written.
10. **Partner-firm example.** The research's Deloitte Australia case is described without naming the firm in the
    eval-plan traps (the Guardian source names it); the shared pattern files already name it.

## 3. Gaps

- No public, independently measured override, escalation or error rates for live knowledge-work systems, and no
  parallel-run results. The files say to set normal ranges from the team's own pilot.
- No measured total-cost-of-ownership comparison for build versus buy; the only deployment-rate comparison
  (MITNANDA-2025) is self-reported and confounded, and is presented as a caution, not a rule.
- No published firm-level acceptance thresholds, sampling plans or documentation templates from a named
  professional-services firm. Regulator and professional-body points (FRC-2025, ABA-2024) are principle level;
  the FRC guidance PDF itself was not read (release only), and BOE-2023 was read only in part.
- Several empirical results use 2023–2024 models (STANFORD-2024, SIERRA-2024, HBS-2023); they show method and
  order of magnitude, not current performance.
- The worked examples are illustrative throughout (labelled), continuing the advisor's audit practice; no real
  professional-services delivery case with measured outcomes was available.

## 4. New controlled values (local to `solution/v1`, not in the shared vocabulary)

| Field | Values |
|---|---|
| `doc` | `brief`, `eval-plan`, `readiness`, `post-launch` |
| `sourcing` | `buy`, `configure`, `build-on-model`, `build-custom`, `undecided` |
| `status` (solution) | `in-progress`, `live`, `paused`, `stopped`, `retired` |
| `status` (eval plan) | `draft`, `agreed` |
| `decision` (readiness) | `pending`, `go`, `go-with-conditions`, `no-go` |
| `last_decision` (post-launch) | `continue`, `tighten`, `loosen`, `redesign`, `retire` |

Schema id: `solution/v1` (one schema covering the frontmatter of the four markdown files). The skill writes no
standalone YAML file.

## 5. Open questions for the owner

1. Should the `sourcing` ids and the readiness and post-launch decision ids move into the shared
   `vocabulary.yaml`?
2. Should the validator resolve core-rules paths against the advisor's folder for every skill, so the pointer
   files are not needed? If so, the two pointer files can be removed.
3. Is running the readiness review twice (before a live pilot, and before production) the intended fit with the
   portfolio's gates, or should delivery own only the production gate?
4. Confirm the split for benefits: delivery prepares the metric, baseline, range and counterfactual; ai-portfolio
   writes `benefits.yaml`. Same for workflows: delivery hands off; ai-enablement writes `enablement/workflows/`.
5. The extra brief `review-solution.md` (independent challenge before go/no-go) is not in the spec's list of
   files. Keep it?
6. Should one set of source keys be adopted across the suite (shared keys versus research keys)?
