**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are the editor who integrates new mid-market modules into the **assurance** and **tax** archetypes of the
`ai-transformation` plugin. Today is 2026-10-21. The modules are already written and verified; your job is the
archetype-level files, a consistency check across the new and widened modules, and the index.

**New modules:** assurance `private-company`, `benefit-plans`, `nonprofit-government`; tax `multistate-private`.
**Widened modules:** tax `compliance-individual-business`, `research-advisory`; assurance `quality-management`,
`soc-attestation`, `assurance-over-ai`. Reports: every `*-synthesis-report.md` and `*-verification-report.md` in
`/home/user/ai-enablement/research/runs/wave6/`, and `/home/user/ai-enablement/research/runs/wave6/landscape-mid-market.md`.

## Tasks

1. **Consistency across the new and widened files** (in `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/` and `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/tax/` modules and use-case YAML only):
   one key per document with the same title, date, type and URL across the archetype (the reports list conflicts,
   e.g. TR-SCALING-2026 vs TR-CASESTUDIES-2026; the Vals P-004 page is dated 2026-10-20 on the live page, so use that
   date in `tax-research-advisory-04` and `tax-multistate-private`); every cross-referenced id exists; no
   build-process words. Do not change grades.
2. **`ARCHETYPE.md`** for assurance and tax: add the new modules to the module table with a one-line summary and
   the **Evidence** column ("strong (N of M A/B)", 50% or more; moderate 30-49%; thin under 30%), and update the
   Evidence column for the widened modules, computing every count from the current YAML (`python3
   /home/user/ai-enablement/scripts/validate.py` prints them). Add mid-market recognition cues (private-company
   audits, reviews and compilations, benefit plan audits, nonprofit and single audits, owner-managed and multistate
   tax). Each `ARCHETYPE.md` must stay at or under 100 lines: tighten wording, don't drop facts.
3. **`value-chain.md`** and **`interview-guide.md`** for both: add the new modules where they sit in the value chain,
   and a few mid-market questions, each at or under 300 lines.
4. **`/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/index.md`**: add the new module ids to the assurance and tax rows and a mid-market cue.

## Rules

Facts only from the existing files and reports, with their source keys; keep provenance; no unsourced connective
claims. Run the validator and fix every ERROR. Write `/home/user/ai-enablement/research/runs/wave6/mid-market-integration-report.md`
(keys unified, ids fixed, files changed, final counts). Do not run git. Reply in no more than 150 words.
