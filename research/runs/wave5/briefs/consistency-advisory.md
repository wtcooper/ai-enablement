**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are the editor who makes the advisory module files consistent with each other before the
archetype-level files are written. Seven modules were written and verified in parallel by different agents. Today is
2026-10-21.

**Scope:** the 7 module files (`modules/*.md`) and 7 use-case files (`use-cases/*.yaml`) under
`/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/archetypes/advisory/`.
Do not touch the archetype-level files, the archetypes index or other archetypes.

**Inputs:** the 7 synthesis and 7 verification reports in `/home/user/ai-enablement/research/runs/wave5/`
(`<module>-synthesis-report.md`, `<module>-verification-report.md`), and the coordinator's notes below.

## Tasks

1. **Source keys.** The same document often carries different keys across files (the synthesis reports list several, e.g. IESBA-TECH-2023 vs IESBA-TECHREV-2023, and one IVSC paper under two keys), and one key sometimes names different documents. Give each document one key across
   all 7 YAML files and module files, with the same title, date, type and URL. Where two similar keys name different
   documents (a press release versus the report), keep both and say so in the YAML file header. Also check keys
   shared with the tax, assurance and security archetypes: a key must not name a different document there
   (also check the professional-services archetype).
2. **Duplicates across modules.** Find entries in different modules that describe the same change to the same work.
   Keep the entry in the module whose work it changes most, and replace the other with a cross-reference by full id
   in the module file (do not delete an entry if each module adds something distinct; then cross-reference both
   ways). Report every pair you looked at.
3. **Cross-references.** Every id mentioned (`advisory-…`, `assurance-…`, `tax-…`, `security-…`) must
   exist. Fix off-by-one and renumbered references.
4. **Provenance consistency.** Where the same figure is labelled with different provenance across files, decide from the source and apply one label everywhere. Change no evidence grade unless the provenance fix requires it under the grade rules, and list every grade change.
5. **Build-process words.** Remove references to the build from product files: "wave", "deep dive", "angle",
   "landscape scan", "synthesis", "verifier", "merged from P10/D08", `research/runs/` paths, candidate counts, grade
   history. Keep any fact such a sentence held, in plain words.
6. **Firm type.** Each example should say what kind of organization it is (top-100 or mid-market accounting firm, Big Four, PE-backed platform, AI-native provider, vendor, client in-house team). Add the type where missing, only if the entry's source makes it
   clear.
7. **Run** `python3 /home/user/ai-enablement/scripts/validate.py` and fix every ERROR in these files. Modules stay at
   or under 300 lines with a table of contents.

## Rules

- Do not change what any source says. Do not delete entries except as in task 2. Keep every id stable.
- Before you start, record each entry's id, grade, ladder and maturity; at the end, confirm by script that every
  entry is still present with the same values (except listed grade changes).

## Output

Edit the files in place, then write `/home/user/ai-enablement/research/runs/wave5/advisory-consistency-report.md`:
keys unified, duplicates handled, cross-references fixed, provenance and grade changes, build words removed, and
the validator result. Do not run git. Reply with a summary of **no more than 150 words**.
- GT-AIIMPACT-2026 names a different Grant Thornton report in three other files (risk-controls verifier).
