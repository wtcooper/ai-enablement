**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are a skeptical fact-checker. An AI advisor will repeat these claims to senior professionals, so
any error damages credibility. Check the synthesized content against its sources. Today is 2026-10-21.

**Files to check:** `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/use-cases/private-company.yaml` (use cases) and `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/private-company.md` (the module file)
**Vocabulary:** `/home/user/ai-enablement/research/briefs/templates/vocabulary.md`

## Tasks

1. **Check every use case.**
   - Open each cited source (web fetch). Confirm that the source exists, that its date is correct,
     and that it supports the claim about the organization, the change to the work, and any figure.
   - Assign the evidence grade from the vocabulary based on what the source actually shows. Downgrade
     anything overstated.
   - Then take one action:
     - **Keep:** the entry is supported.
     - **Fix:** correct the wording, figure, date or grade, or add a better source you found.
     - **Reject:** the claim is unsupported, or the source can't be found.
   - If a source is blocked, try another route (a publisher mirror, a press release, an archived
     copy). If you still can't confirm it, the most an entry can be is grade C, and only if a
     secondary source supports it. Otherwise reject it.
2. **Check the module file.** Every figure, benchmark, regulatory statement and frontier signal must
   trace back to a source. Fix or remove anything that doesn't.
3. **Known error patterns** from the pilot. Check each one explicitly:
   - a statistic reported as something it doesn't measure
   - a claim attributed to the wrong document or speaker
   - embellished qualifiers or causes
   - unsourced connective claims in `role_evolution` and `risks_and_guardrails`
   - wrong or missing dates
   - a grade inflated by evidence from an adjacent process
   - a search-only figure used inside an A or B entry
4. **Check the format.** Values come from the vocabulary. Ids are unique. Every source has a URL and
   a date. Quotations are under 25 words.

## Output

- Edit `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/use-cases/private-company.yaml` and `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/assurance/modules/private-company.md` in place with your fixes and removals.
- Write `/home/user/ai-enablement/research/runs/wave6/private-company-verification-report.md`, a verification report:
  - counts: kept, fixed, rejected
  - the final grade mix
  - a table of every fix and rejection, with the reason
  - sources that couldn't be reached
  - whether the module meets its targets: 15–25 use cases, at least 50% graded A or B, every source
    dated
  - patterns of error to fix in the briefs

Then reply with a summary of **no more than 150 words**.

- **Grade A rule (2026-10-17):** A needs a figure the named organization reports as measured (a tracked metric, a study or data). A practitioner's recollection or rough estimate quoted in a vendor case study, even with numbers, is grade B; keep the figure, labelled with its provenance.
- Cross-references to other modules and archetypes (`assurance-…`, `tax-…`, `security-…`, `professional-services-…` ids) must name entries that exist; fix any that don't.
