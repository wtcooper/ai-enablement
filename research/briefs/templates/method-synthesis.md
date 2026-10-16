# Brief template: method synthesis (stream M)

Placeholders: `{input_paths}`, `{files_to_write}`, `{method_dir}`, `{report_out}`, `{today}`.

---

You are the editor who writes the **method reference files**, pillar 1 of the product. These files
guide an AI advisor, phase by phase, as it takes a business leader through transforming their part of
the business with AI. The advisor has to act like an expert transformation lead, using plain language.
Today is {today}.

**Inputs:** {input_paths} (the stream-M topic research files)
**Product design:** `/home/user/ai-enablement/spec/2026-10-16-ai-transformation-advisor.md`. Read
§3 (onboarding and adaptation), §4 (the loop, the four lenses, Break down and Roll-up, conversation
rules), §6.1–6.7 (method, ladder and change scope, value tree, journey stages) and §9 (rules).
**Files to write in `{method_dir}/`:** {files_to_write}

## What each phase file contains

Each file is ≤ 300 lines, with a table of contents if over 100 lines. It is written so the advisor can
read it on entering the phase and act on it straight away.

1. **Goal and exit criteria.** What must be true before moving on.
2. **How to run it.** A short sequence of steps. One question at a time. Play back what you heard.
3. **Question bank.** Core questions first, then follow-ups. Mark which are for **team** scope and
   which for **unit or organization** scope, and adapt by **journey stage** where it matters.
4. **Expert moves.** The probes, heuristics and quick analyses an experienced lead uses, each with
   when to use it and what it reveals.
5. **Common traps**, and how the advisor avoids them.
6. **Worked example.** A short example from knowledge work or professional services, ideally
   assurance or tax.
7. **Output.** Exactly what to write into the plan file at the end of the phase. Field names follow
   spec §5.3.
8. **Sources.** A short key list. Every research-backed claim, figure or framework attribution in the
   file has a key.

Cross-cutting files follow the same spirit, organized for their purpose:

- `onboarding.md`: profile questions, archetype detection, journey-stage markers and diagnostic
  questions, and how to adapt the path
- `people-and-change.md`: honest framing of job impact, role evolution, redeploy versus reduce,
  communication, responding to fear
- `interviewing.md`: question craft, sequencing and playback for an AI interviewer
- `breakdown-and-rollup.md`: how to split a scope into units, write unit briefs, run desk reviews,
  and roll up

`index.md` is one table: file, phase, when to read it, one-line summary.

## Rules

- Synthesize across the inputs. Merge overlapping advice and resolve conflicts (note them in the
  report).
- Prefer moves backed by evidence or by well-established practice. Don't invent statistics. Keep
  provenance on any figure.
- Use plain language. Method terms (DMAIC, value stream and so on) are fine **for the advisor**, but
  every question it asks the user must be in plain language.
- Respect spec §9. In particular, `people-and-change.md` must make the redeploy-versus-reduce choice
  and role evolution concrete, and must never target individuals.
- Run `python3 /home/user/ai-enablement/scripts/validate.py` and fix every ERROR in your files.

## Output

Write the files, then write `{report_out}`. The report covers:

- which inputs fed each file
- conflicts you resolved
- gaps
- suggestions for the skill's `SKILL.md` loop checklist (the three to five core questions per phase)

Then reply with a summary of **no more than 150 words**.
