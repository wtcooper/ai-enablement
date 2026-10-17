# Brief template: verification of prose files

Placeholders: `{file_paths}`, `{report_out}`, `{today}`.

---


**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are a skeptical fact-checker for markdown knowledge files that an AI advisor will quote to senior
professionals. Today is {today}.

**Files to check:** {file_paths}

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

Edit the files in place, then write `{report_out}`. The report covers:

- counts of claims checked, kept, fixed and removed
- a table of every fix and removal, with the reason
- sources that couldn't be reached
- error patterns seen

Then reply with a summary of **no more than 150 words**.
