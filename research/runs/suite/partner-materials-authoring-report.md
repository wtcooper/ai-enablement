# Partner materials authoring report

Date: 2026-10-20. Brief: `briefs/author-partner-materials.md`. Input: `topic-partners.md`.

## Files changed

- **New:** `plugins/ai-transformation/skills/transformation-advisor/references/method/leading-partners.md`
  (299 lines, contents list). Sections: why influence beats authority; partner economics as barrier and lever
  (table); stakeholder map by role (columns, decision rules); one-page partner briefing (seven steps, including
  graded evidence, the honest role picture and the ask); objection handling for skeptical seniors (concede /
  control table, pointers to all four archetypes' `objections.md`); leader expectations and accountability;
  visible wins and champions; question bank ([T] / [U/O] tags); traps; worked example (an accounting firm's
  partner meeting, continuing the audit practice's `ct-07`, labelled illustrative); output; 33 sources.
- **`method/index.md`:** one row for `leading-partners.md`.
- **`method/people-and-change.md`:** one bullet in §7 Communicating change pointing to the new file.
- **`SKILL.md`:** phase 6 Read now line extended to name `leading-partners.md` when partners or senior experts
  must back the case (229 to 230 lines).

## Provenance choices

- Every figure carries a source key and provenance from the research file (self-reported, vendor, secondary,
  opinion, abstract only). Analyst-proposed structures (briefing order, three pricing scenarios, sponsor-standing
  rule) and inferences are labelled as such.
- Rule 1: the stakeholder map records roles, segments and stance basis, never names; research questions that
  pointed at specific partners were reworded to roles, practices or forums. The worked example shows the advisor
  declining to rank partners.
- Rule 9: the research's "visible win within one quarter" and "decision date" were dropped in favour of early
  wins and a deciding forum.
- People are referred to by role (for example "one firm's chair", "PwC's US CEO"); all quotations are under
  25 words. The worked example's numbers reuse the illustrative `ct-07` case in `business-case.md` §7.

## Validation

`python3 scripts/validate.py`: no ERROR lines; existing use-case coverage warnings are unrelated to these files.
