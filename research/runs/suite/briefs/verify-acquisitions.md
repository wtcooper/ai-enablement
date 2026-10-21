**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad.

You are a skeptical reviewer of new acquisition material in the `ai-transformation` plugin. Today is 2026-10-21.

**Files to check:** `/home/user/ai-enablement/plugins/ai-transformation/skills/transformation-advisor/references/method/acquisitions.md`,
`.../transformation-advisor/references/briefs/assess-target-firm.md`, `/home/user/ai-enablement/plugins/ai-transformation/skills/ai-portfolio/references/method/acquired-firms.md`
and §9 of `.../ai-portfolio/references/method/stage-gates.md`, plus the one-line pointers to them in both skills' `SKILL.md`
and index files. Research input: `/home/user/ai-enablement/research/runs/suite/topic-acquisitions.md`. Authoring report:
`/home/user/ai-enablement/research/runs/suite/acquisitions-authoring-report.md`.

Check every figure, date, attributed statement, named example and regulatory point against its source (`curl -sSL
--max-time 30 -A "Mozilla/5.0" <url>`, `pdftotext`, the mirror `curl -sSL "https://r.jina.ai/<url>"`); keep, fix or
remove. Check the error patterns in `/home/user/ai-enablement/research/briefs/templates/verifier.md`; self-reported
platform claims must be labelled as such. Check fitness for use: the advisor knows when to take the path, records the
assessment as a unit, keeps desk drafts labelled; the playbook sequences by dependency (no calendar deadlines), covers
consent and independence, and never targets named individuals. Run `python3 /home/user/ai-enablement/scripts/validate.py`
and fix every ERROR in these files. Edit in place; write `/home/user/ai-enablement/research/runs/suite/acquisitions-verification-report.md`
(counts, a table of fixes with reasons, sources not reached, open questions). Do not run git. Reply in no more than
150 words.
