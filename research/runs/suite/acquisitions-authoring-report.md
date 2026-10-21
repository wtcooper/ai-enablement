# Authoring report: acquisition path and acquired-firm rollout playbook

Date: 2026-10-20. Brief: `research/runs/suite/briefs/author-acquisitions.md`. Research input:
`research/runs/suite/topic-acquisitions.md`. No sources were downloaded, so no private working folder was needed.

## Files written or changed

| File | Change | Lines |
|---|---|---|
| `plugins/ai-transformation/skills/transformation-advisor/references/method/acquisitions.md` | New. Contents list; when to use it; intake; ten dimensions to ask about and count, placed on the journey stages; red flags; value-creation questions; recording the assessment as a unit (`units/<target-id>/`); traps; illustrative accounting-firm worked example; output; sources | 262 |
| `plugins/ai-transformation/skills/transformation-advisor/references/briefs/assess-target-firm.md` | New subagent brief, modelled on `desk-review-unit.md`; output labelled "draft to validate" | 63 |
| `plugins/ai-transformation/skills/transformation-advisor/references/method/index.md` | One row added (acquisitions.md) | 20 |
| `plugins/ai-transformation/skills/transformation-advisor/SKILL.md` | One delegation-table row (assess-target-firm); one sentence in Onboard, "Adapt the path" | 234 (was 232) |
| `plugins/ai-transformation/skills/ai-portfolio/references/method/stage-gates.md` | §9 placeholder replaced by the rollout playbook summary (eight rules and a layer table); contents entry renamed; three source keys added to §11 | 252 (was 227) |
| `plugins/ai-transformation/skills/ai-portfolio/references/method/acquired-firms.md` | New detail file: dependency layers, readiness checks per layer, client-data separation and consent, independence checks, change management for incoming partners and staff, tracking in `benefits.yaml`, how to describe the platform's AI without overstating it, questions and traps, worked example, sources | 250 |
| `plugins/ai-transformation/skills/ai-portfolio/SKILL.md` | Description now says "or roll proven capabilities into an acquired firm" (1,012 characters); reference map points to stage-gates §9 and acquired-firms.md | 221 |

## How the rules were applied

- **Facts.** Figures and factual claims come from research points that cite a source and carry no [synthesis] or
  [proposed] tag. The research file tags only synthesis and proposed points, so untagged points with a source key
  counted as sourced. Facts from existing files are cited by path (onboarding §5, journey-stages §2,
  ai-governance professional-duties §4).
- **Excluded.** The Thomson Reuters figure that 35% of professionals use unapproved AI, which the research marks
  unconfirmed. Synthesis or proposed points are used only as method and are labelled "advisor rule", "advisor
  heuristic", "advisor synthesis", "advisor move" or "proposed default": AI upside kept out of the base case, the
  independence assessment for shared AI services across the attest line, the dependency layers, rollout and pause
  gates, entry at `pilot`, and the staggered-start counterfactual.
- **Provenance.** Survey figures give their sample size and say they are vendor-published. Company claims (Current's
  31%, 98% and 7,000 returns) are marked self-reported, with no baseline published. Health-care roll-up evidence is
  marked as an adjacent industry with no AI element.
- **Sequencing.** No calendar plans. Sources that use a "first 100 days" frame are mentioned only to say this skill
  sequences by dependency instead (rule 9). Deal phases (diligence, sign to close, after close) are situations, not
  deadlines.
- **People.** No named individuals; roles only (for example "Baker Tilly's CEO"). Quotations are two to three words
  each ("table stakes", "red herring").
- **Worked examples** are labelled illustrative. Both use the same invented target, `units/target-cedar/`. The
  portfolio example continues the K-1 item from stage-gates §8.

## Validation

`python3 scripts/validate.py`: 0 errors. The 27 warnings all concern archetype use-case grade targets, which are not
in these files. Every new file is within 300 lines and has a contents list. All backtick paths resolve.

## Follow-ups outside this brief's file list

- `plugins/ai-transformation/skills/ai-portfolio/references/method/index.md` still describes stage-gates.md as
  having a "placeholder for acquired firms", and it does not list `acquired-firms.md`. That file was not in the list
  of files I could edit, so I left it unchanged. Suggested row: `| [acquired-firms.md](acquired-firms.md) | 4 Stage
  gates (acquired firms) | Rolling proven capabilities into an acquired firm | Dependency layers, readiness checks,
  consent and independence, incoming partners, benefits rows, describing the platform's AI |`, and change
  "placeholder for acquired firms" to "rollout playbook for acquired firms".
- Gaps carried over from the research: there is no authoritative reading of AI tools under Sec. 7216, no guidance
  on shared AI services across the attest line, and no outcome data on partner or client retention. The final status
  of the AICPA independence rules also needs checking. The files tell the user to take counsel's view or to confirm
  the current status.
