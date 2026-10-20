**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are a skeptical reviewer of one skill in the `ai-transformation` plugin, which an AI assistant will use with
senior leaders. Today is 2026-10-20. Check both **facts** and **fitness for use**.

**Files to check:** `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/method/leading-partners.md` and the pointers to it in `method/index.md`, `method/people-and-change.md` and `SKILL.md` (do not review the rest of the skill). Design:
`/home/user/ai-enablement/spec/2026-10-20-skill-suite.md`. Research inputs: `/home/user/ai-enablement/research/runs/suite/topic-partners.md`. Authoring report:
`/home/user/ai-enablement/research/runs/suite/partner-materials-authoring-report.md`.

## Tasks

1. **Facts.** Check every figure, date, attributed statement, named example, standard or regulatory point and
   forecast against its cited source (`curl -sSL --max-time 30 -A "Mozilla/5.0" <url>`, `pdftotext`, the mirror
   `curl -sSL "https://r.jina.ai/<url>"`; web search is rationed). Keep, fix or remove. Check the known error
   patterns in `/home/user/ai-enablement/research/briefs/templates/verifier.md` (misread statistics, attribution
   drift, embellished qualifiers, unsourced connective claims, wrong dates, forecasts as facts, vendor claims as
   independent). Survey figures must name their population and who ran the survey.
2. **Fitness for use.** Read `SKILL.md` as the assistant would: is the description specific about the moment and
   the sibling skills; does each step have a goal, core questions, exit criteria, an output file and one "Read now"
   pointer; does it save state after each step and resume from the workspace; are handoffs named with the file-read
   fallback; does it stay within the core rules (no named individuals, ranges not point values, grades as recorded,
   no calendar deadlines, designs and plans but never claims to build or run)? Fix gaps directly.
3. **Formats.** Every schema example parses (`python3 -c "import yaml,sys;yaml.safe_load(open(sys.argv[1]))"` on an
   extracted example); templates match their schemas; ids used are in the shared `vocabulary.yaml` or listed as new
   in the authoring report.
4. **Structure.** `python3 /home/user/ai-enablement/scripts/validate.py` reports no ERROR for these files (the core
   rules block matches; every backtick path resolves; sizes and contents lists hold).

## Output

Edit the files in place, then write `/home/user/ai-enablement/research/runs/suite/partner-materials-verification-report.md`: claims checked, kept, fixed and removed;
a table of every fix and removal with the reason; usability fixes; sources not reached; open questions for the
owner. Do not run git. Reply with a summary of no more than 150 words.
