**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are a skeptical fact-checker for knowledge files that an AI advisor will quote to senior leaders. Today is
2026-10-20.

**Files to check:** the 10 function cards in `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/functions/`, `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/journey-stages.md`, and §7-§8 of `/home/user/ai-enablement/plugins/transformation-advisor/skills/transformation-advisor/references/library/index.md`.

## Tasks

1. **Check every factual claim**: every figure, date, attributed statement, graded example, regulatory point and
   forecast. Open the cited source (`curl -sSL --max-time 30 -A "Mozilla/5.0" <url>`, `pdftotext` for PDFs, the
   text mirror `curl -sSL "https://r.jina.ai/<url>"` for blocked sites; web search is rationed). Then keep, fix
   (wording, figure, date, attribution, grade, or a better source) or remove it. Try other routes before removing.
2. **Check grades** against the vocabulary (`/home/user/ai-enablement/research/briefs/templates/vocabulary.md`).
   Grade A rule (2026-10-17): A needs a figure the named organization reports as measured; recollections and rough
   estimates are B; a tool benchmark alone is not A for a work outcome.
3. **Check the known error patterns** in `/home/user/ai-enablement/research/briefs/templates/verifier.md`: misread
   statistics, attribution drift, embellished qualifiers, unsourced connective claims, wrong dates, forecasts
   presented as facts, vendor claims presented as independent.
4. **Check structure.** Every source key resolves to a listed source with URL and date; every archetype use-case id
   cited exists (grep the YAML) and its grade matches; links resolve; size limits and tables of contents hold; no
   vendor recommendations. Run `python3 /home/user/ai-enablement/scripts/validate.py` and fix every ERROR in these
   files.

## Output

Edit the files in place, then write `/home/user/ai-enablement/research/runs/streamB/functions-journey-verification-report.md`: claims checked, kept, fixed and removed; a
table of every fix and removal with the reason; sources that couldn't be reached; error patterns seen. Do not run
git. Reply with a summary of no more than 150 words.
