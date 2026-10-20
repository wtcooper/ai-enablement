# Authoring report: ai-portfolio

Date 2026-10-20. Skill folder: `plugins/ai-transformation/skills/ai-portfolio/`. No git run.

## Files written

| File | Lines | Inputs that fed it |
|---|---|---|
| `SKILL.md` | 208 | Suite spec §2-5; advisor `SKILL.md` (structure, voice); core-rules block copied verbatim; all method files below |
| `references/method/index.md` | 14 | Own method files |
| `references/method/setup.md` | 191 | topic-portfolio §2, §3 moves 10, 21-23, §4 intake and review questions, §5 traps, §8 portfolio review (cadence, forum); topic-partners §1, §3 moves 1 and 4 (constellation, business-minded partners); shared `frame.md` §4, `prioritize.md` §3.5 |
| `references/method/intake.md` | 168 | topic-portfolio §2 (intake as register), §3 moves 1-4, 26-27, §4 intake, §8 intake (checklist, decision rule); topic-partners move 20 (shadow use); shared `opportunities.md` schema for the import mapping |
| `references/method/screen-and-score.md` | 199 | topic-portfolio §2 (screening), §3 moves 4-8, 15, 23, 25, §5 traps, §6 E14-E15, §8 screen (thresholds, payback, spend); shared library §6 and `prioritize.md` §3 |
| `references/method/stage-gates.md` | 226 | topic-portfolio §2 (gates, outcomes), §3 moves 9-14, 20, 24-25, §4 gates and stop questions, §5 traps, §7.1-7.2 (utility, Lloyds), §8 stage gates and stop or redirect; brief (placeholder) |
| `references/method/portfolio-review.md` | 180 | topic-portfolio §3 moves 8, 16, 19-21, 26, §4 review questions, §5 traps, §8 review pack and cadence; topic-partners moves 5, 6, 25, 28, evidence rows 2, 20 |
| `references/method/value-tracking.md` | 174 | topic-portfolio §2 (benefits, attribution, J-curve), §3 moves 16-18, 27-29, §4 value questions, §6 E1, E15, E16, E19-E21, §7.3-7.4, §8 value tracking, §10 redeploy gap; topic-partners evidence row 2; shared `business-case.md` §3.2 and `people-and-change.md` §5 |
| `references/method/people-and-change.md` | 77 | topic-partners §1-3 (Empson, Polsinelli, Magesh, Perlin, KPMG, Accountancy Age); shared `people-and-change.md` |
| `references/library/index.md` | 117 | Shared library index; topic-portfolio (Cooper outcomes, MSFT classes, HBR horizon and warnings, AUSGOV benefit types); ai-governance's tier ids |
| `references/schemas/portfolio.md` | 216 | Shared `opportunities.md` and `plan.md` (format, rules); topic-portfolio §8 template fields |
| `references/schemas/benefits.md` | 127 | topic-portfolio §8 value tracking (AUSGOV-2013, IVI fields), DBS counterfactual; shared `business-case.md` §3.2 |
| `references/templates/portfolio.yaml` | 44 | portfolio/v1 |
| `references/templates/intake.md` | 55 | topic-portfolio §8 intake card fields |
| `references/templates/review.md` | 99 | topic-portfolio §8 review pack fields |
| `references/templates/benefits.yaml` | 28 | benefits/v1 |
| `references/briefs/prepare-review-item.md` | 45 | Advisor brief format (`review-opportunities.md`) |

Validator: 0 errors across the plugin after all sibling skills landed (the `../ai-enablement/SKILL.md` handoff path
now resolves). Both schema examples parse (checked with
`yaml.safe_load`). Description is 960 characters.

## Conflicts resolved

- **Core-rules paths.** The verbatim core rules point to `references/library/index.md` and
  `references/method/people-and-change.md`, which resolve against each skill's own folder. I mirrored the advisor's
  layout (`references/method/`, `references/library/`) and made both files useful in their own right: a portfolio
  library (portfolio-only values plus pointers to the shared library) and a portfolio-specific people file that
  points to the shared one. The other siblings did the same.
- **Stage names.** The brief's six stages are used; the stage-gates file maps them to Cooper's six and HBR's four.
  An `intake` value was added for unscreened items, so the six gated stages stay as the brief names them.
- **Redirect.** The research lists Redirect beside Cooper's four outcomes; it is modelled as `recycle` with a
  `recycle_to` field, keeping the brief's four outcomes.
- **Value and readiness split of the six shared scores** is a skill heuristic: value axis = value, strategic fit,
  time to value; readiness axis = feasibility, data readiness, risk. Quadrant thresholds (3.5) are labelled
  proposed defaults.
- **Payback.** Deloitte (two to four years) against Google Cloud (74% ROI within a year): both shown, with the
  reason they differ; Google's figure is not used for hurdles, as the research advises.
- **ROI tracking.** TRI-AIPS-2026 (18% know it is tracked, professional services) against WHARTON-2025 (72%, US
  enterprises): flagged as different samples, context only.
- **MIT NANDA budget skew** is internally inconsistent (50% vs about 70%); stated as such.
- **Review cadence and the PIR timing.** No source sets a cadence; monthly review with a rebalance every third
  review is a proposed default (a rhythm, not a deadline). IVI's "within six months" is reported only as what IVI
  measures; review points are set by trigger at `g3` to respect rule 9.
- **Risk tiers.** Aligned `risk_tier` with ai-governance's `risk_tiers` ids (`tier-1` to `tier-4`) instead of
  inventing a scale.
- **Spec trigger for acquired firms.** The description does not claim the acquired-firm rollout, since the playbook
  is a placeholder (stage-gates §9, clearly marked, with interim instructions).

## Gaps

- No source gives stage-gate pass rates, kill rates, time in stage or realised-versus-forecast rates for an AI
  portfolio; no independent audit of AI benefits.
- No professional-services portfolio evidence; all worked examples are illustrative (a mid-sized accounting, tax
  and advisory firm) and labelled so. Archetype use cases cited with grades as recorded:
  `tax-compliance-individual-business-02` (B), `professional-services-pursuit-proposals-01` (B),
  `professional-services-knowledge-management-01` (B).
- No source on how firms decide redeploy versus reduce after launch; the skill relies on the shared
  people-and-change method.
- Forum composition, pack contents and cadence rest on HBR-2026 and Microsoft guidance only.
- The acquired-firm rollout playbook is not written (placeholder).

## New vocabulary proposed (defined in `references/library/index.md`, not yet in `vocabulary.yaml`)

- `stage`: intake, discover, prototype, pilot, production, scale, retire
- `status`: outline, active, hold, killed, retired
- gate ids: g0, g1, g2, g3, g4, retire
- `outcome`: go, kill, hold, recycle
- `item_class`: individual-productivity, business-automation, new-value
- `horizon`: near, medium, long
- `gate_path`: light, full
- early-warning `type`: slippage, cost-overrun, performance-shortfall
- benefit `type`: direct, indirect, interim, disbenefit; `level`: use-case, enterprise
- `counterfactual`: control-group, staggered-start, parallel-run, baseline-comparison, assumption
- `basis`: from-record, reported, observed, outside-in (the advisor's Map labels, made ids)
- benefit `status`: forecast, tracking, realised, partly-realised, not-realised, withdrawn; `confidence`: low,
  medium, high
- Reused without change: `category` (quick-win, foundation, big-bet, park, from opportunities/v1) and
  `capacity_use`/`capacity_stance` values (redeploy, reduce, mixed, undecided, from plan/v1); `risk_tier` uses
  ai-governance's `tier-1` to `tier-4`.

## Open questions for the owner

1. Add the portfolio values above to `vocabulary.yaml`, and extend the validator to check `portfolio/v1` and
   `benefits/v1` examples and enums?
2. Are the proposed defaults acceptable: quadrant thresholds of 3.5, monthly review with rebalance every third,
   the light path (g1 and g2 combined), "two reviews running" for an early-warning surfacing rule?
3. Should the core-rules block use shared paths (`../transformation-advisor/references/...`) instead, so siblings do
   not need mirrored `library/index.md` and `method/people-and-change.md` files?
4. The stage-gates placeholder and the handoff refer to the advisor's acquisition path (spec §6), which is not yet in
   the advisor's `SKILL.md`. Who writes the acquired-firm playbook, and from which research?
5. Should the advisor's `opportunities.yaml` carry a forward link to the portfolio id? The skill currently never
   edits the advisor's file and keeps the back-link only in `portfolio.yaml`.
