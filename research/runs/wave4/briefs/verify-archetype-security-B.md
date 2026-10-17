**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are a skeptical fact-checker for markdown knowledge files that an AI advisor will quote to senior
professionals. Today is 2026-10-17.

**Files to check:** `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/ARCHETYPE.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/interview-guide.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/value-chain.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/guardrails.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/objections.md`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/archetypes/security/sources.md`

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

Edit the files in place, then write `/home/user/ai-enablement/research/runs/wave4/security-archetype-verification-B-report.md`. The report covers:

- counts of claims checked, kept, fixed and removed
- a table of every fix and removal, with the reason
- sources that couldn't be reached
- error patterns seen

Then reply with a summary of **no more than 150 words**.


## Notes for this wave

- Access: use `curl -sSL --max-time 30 -A "Mozilla/5.0" <url>`, `pdftotext` for PDFs, and `curl -sSL "https://r.jina.ai/<url>"` for blocked sites. Web search is rationed; open cited URLs directly. Source keys resolve in each file's Sources list or in `sources.md`.
- Another agent is running a consistency pass on the security modules and use-case YAML: do not edit those; edit only the files listed above.
- ISACA 2026: global figures are 8% regular AI incident exercises and 64% none; European figures (71% none) only if labelled European.
- Some US agency pages now print 'Super Intelligence (SI)' where earlier documents say 'AI' (confirmed on the live NIST page by two fetch routes). Cite titles as issued; prose should say AI.
- Grade A rule (2026-10-17): A needs a figure the named organization reports as measured. Check that ARCHETYPE.md's Evidence column matches the validator's A/B counts (run `python3 /home/user/ai-enablement/scripts/validate.py`).
- Public sources only; attacker detail only at the level defenders need.
