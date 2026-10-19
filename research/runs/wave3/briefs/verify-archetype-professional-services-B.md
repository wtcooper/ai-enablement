**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are a skeptical fact-checker for markdown knowledge files that an AI advisor will quote to senior
professionals. Today is 2026-10-19.

**Files to check:** `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/ARCHETYPE.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/interview-guide.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/value-chain.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/guardrails.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/objections.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/professional-services/sources.md`

## Tasks

1. **Check every factual claim.** That means every figure, date, attributed statement, regulatory
   point and forecast.
   - Open the cited source with `curl` (and `pdftotext` for PDFs) and confirm the claim.
   - Then **keep**, **fix** (wording, figure, date, attribution, or a better source), or **remove**
     it.
   - If a source is blocked, try other routes before removing the claim.
2. **Check the known error patterns** from `/home/user/ai-enablement/research/briefs/templates/verifier.md`:
   - misread statistics
   - attribution drift
   - embellished qualifiers
   - unsourced connective claims
   - wrong dates
   - forecasts presented as facts
3. **Check structure.**
   - Every source key used resolves to a listed source with a URL and a date.
   - Files over 100 lines start with a table of contents.
   - Size limits are respected.
   - Run `python3 /home/user/ai-enablement/scripts/validate.py` and fix every ERROR in these files.

## Output

Edit the files in place, then write `/home/user/ai-enablement/research/runs/wave3/professional-services-archetype-verification-B-report.md`. The report covers:

- counts of claims checked, kept, fixed and removed
- a table of every fix and removal, with the reason
- sources that couldn't be reached
- error patterns seen

Then reply with a summary of **no more than 150 words**.


## Notes for this wave

- Access: use `curl -sSL --max-time 30 -A "Mozilla/5.0" <url>`, `pdftotext` for PDFs, and `curl -sSL "https://r.jina.ai/<url>"` for blocked sites. Web search is rationed; open cited URLs directly. Source keys resolve in each file's Sources list or in `sources.md`.
- Edit only the files listed above. Another agent may be checking the other archetype-level files.
- Known traps in this field: bar and regulator guidance read through secondary summaries (ABA Formal Opinion 512, SRA pages were often blocked: say "as quoted by" when only a summary was read); survey populations applied to the wrong group (law firms vs corporate legal vs all industries; stand-out lawyers vs all lawyers); vendor-commissioned surveys presented as independent; McKinsey's outcome-based fee share (secondary sources differ); the NBER patent-lawyer trial (Google ran and funded it; say so); conference talks not yet held reported as held; examples without their firm type.
- Grade A rule (2026-10-17): A needs a figure the named organization reports as measured. Check that ARCHETYPE.md's Evidence column matches the validator's A/B counts (run `python3 /home/user/ai-enablement/scripts/validate.py`). Also check that `archetypes/index.md` lists professional-services as available with correct module ids, and that the links added to the assurance, tax and security ARCHETYPE.md files resolve.
- Public sources only; no client-confidential information.
