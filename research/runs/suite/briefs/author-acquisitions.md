**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are adding an **acquisition path** to the core skill of the `ai-transformation` plugin and an
**acquired-firm rollout playbook** to its ai-portfolio skill. Today is 2026-10-20. Read
`/home/user/ai-enablement/spec/2026-10-20-skill-suite.md` §6, `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/SKILL.md`,
`/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/method/index.md`, `.../method/breakdown-and-rollup.md`,
`.../method/onboarding.md` §5, `.../library/journey-stages.md`, `.../briefs/desk-review-unit.md` (as a model for a
brief), and `/home/user/ai-enablement/plugins/ai-transformation/skills/ai-portfolio/SKILL.md` with its stage-gates method file (§9 is a placeholder for the playbook).
Research input: `/home/user/ai-enablement/research/runs/suite/topic-acquisitions.md` (points are tagged
[sourced], [synthesis] or [proposed]; only [sourced] points may carry facts or figures).

## Write

1. `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/method/acquisitions.md` (at most 300 lines, contents list): assessing a
   target or newly acquired firm's AI and data maturity. When to use it (diligence, or the first period after
   close); what to ask and what to count, placed on the journey stages; red flags (unsanctioned tools, client-data
   handling, consent for tax-return information, independence with the acquirer's audit clients, vendor contracts
   that do not transfer); the value-creation questions for the acquisition thesis; how to record the assessment as a
   unit in the plan (reuse Break down: `units/<target-id>/`); traps; a worked example of an accounting-firm
   acquisition, labelled illustrative; Sources.
2. `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/briefs/assess-target-firm.md`: a subagent brief that turns public
   information and documents the user provides about one firm into a draft maturity assessment labelled
   "draft to validate", modelled on `desk-review-unit.md`.
3. Add: one row to `method/index.md`; one row to the delegation table in `SKILL.md`; one sentence in the Onboard or
   Map section of `SKILL.md` saying when to take the acquisition path (keep `SKILL.md` within its budget). Change
   nothing else in the core skill.
4. Replace the placeholder §9 in the ai-portfolio stage-gates method file with the **rollout playbook for acquired
   firms**: which repeatable capabilities (approved tools, workflows from the enablement library, governance
   overlay, data foundations) move first and in what order by dependency, the readiness checks before each, change
   management for incoming partners and staff, client-data separation and consent, independence checks, how
   capability adoption and value are tracked in `benefits.yaml`, and how to describe the platform's AI to incoming
   partners without overstating it. Keep the file within 300 lines (move detail to a new file
   `references/method/acquired-firms.md` in ai-portfolio if needed, and point to it). Update the ai-portfolio
   `SKILL.md` description and reference map to mention it, keeping the description under 1,024 characters.

## Rules

Facts only from [sourced] research points or existing files, with source keys; keep provenance and modal verbs; no
unsourced connective claims; quotations under 25 words; no named individuals; sequence by dependencies, never
calendar deadlines (no 100-day plans). Run `python3 /home/user/ai-enablement/scripts/validate.py` and fix every
ERROR in your files. Write a report to `/home/user/ai-enablement/research/runs/suite/acquisitions-authoring-report.md`.
Do not run git. Reply with a summary of no more than 150 words.
