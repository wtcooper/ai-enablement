**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are the editor who **widens existing tax modules** (compliance-individual-business and research-advisory) for mid-market firms. Today is 2026-10-21.

**Inputs:** `/home/user/ai-enablement/research/runs/wave6/mm-widen-tax.md`, `/home/user/ai-enablement/research/runs/wave6/landscape-mid-market.md`, and the "Routed to other modules" sections of every `mm-*.md` file in `/home/user/ai-enablement/research/runs/wave6/` naming these modules. **Vocabulary:** `/home/user/ai-enablement/research/briefs/templates/vocabulary.md`.
**Files to edit:** for each target module, `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/tax/modules/<module>.md` and `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/tax/use-cases/<module>.yaml`.

## Tasks

1. Read each target module and its YAML first. Add new use cases only where they change the work in a way the existing entries don't cover; merge into an existing entry (keeping all its sources) when it is the same change. Number new entries after the last existing id. Never renumber or delete existing entries; never change an existing entry's grade unless the new evidence is about that same entry, and then list it.
2. In each module file, add a short section (or extend the relevant sections) on what is different for mid-market firms, keeping the file at or under 300 lines with its contents list; trim wording elsewhere if needed, not facts.
3. Keep the module's Sources section and the YAML consistent: every cited key resolves.

## Rules

Facts only from the inputs; keep provenance and modal verbs; no unsourced connective claims; quotations under 25 words; grade A rule (2026-10-17): A needs a figure the named organization reports as measured. Say what kind of firm each example comes from. Run `python3 /home/user/ai-enablement/scripts/validate.py` and fix every ERROR in your files.

## Output

Edit the files, then write `/home/user/ai-enablement/research/runs/wave6/widen-tax-synthesis-report.md`: entries added and merged per module, sections added, grade changes, gaps. Do not run git. Reply with a summary of no more than 150 words.
