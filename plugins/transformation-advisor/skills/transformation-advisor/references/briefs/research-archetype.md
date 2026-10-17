# Brief: research an archetype on the spot (Onboard fallback)

**Used by:** the advisor during Onboard, **only** when no archetype matches, the user agrees, and you have web
search and page-fetch tools. It is a lighter version of the research that built the plugin's archetypes. The
result is a **provisional** archetype in the user's workspace at `overlay/archetypes/<id>/`. It never changes the
plugin.

## Contents

1. [For the advisor: how to run it](#1-for-the-advisor-how-to-run-it)
2. [Subagent brief A: landscape](#2-subagent-brief-a-landscape)
3. [Subagent brief B: focus area](#3-subagent-brief-b-focus-area)
4. [Subagent brief C: check](#4-subagent-brief-c-check)
5. [Writing the provisional archetype](#5-writing-the-provisional-archetype)

## 1. For the advisor: how to run it

1. **Agree the scope with the user.** Name the field in one line (what is delivered, to whom, who regulates it)
   and propose three to six focus areas from what they told you. Say plainly that this takes a while, uses many
   web searches, and produces a provisional draft that has not been checked to the plugin's standard. Continue
   only if they agree. Carry on with Frame while it runs if your tool allows background work.
2. **Landscape first, alone.** Use one subagent with brief A. Wait for it: later steps depend on its source keys
   and leads, and the search allowance is shared.
3. **Focus areas in parallel.** Use subagents for this step: delegate one subagent per focus area with brief B, in
   parallel. If you cannot start subagents, do each focus area yourself, one at a time.
4. **Check in parallel.** Delegate one subagent per focus area with brief C, on the output of step 3. If you
   cannot start subagents, check each yourself. Do not skip this step: in the plugin's own research, fact-checking
   corrected most draft entries.
5. **Write the archetype** (section 5) and tell the user what it holds, its evidence mix, and that it is
   provisional. Then continue Onboard with it as the matched archetype.

For each subagent, pass the brief section's full text plus: the field description, the focus areas, today's
date, the paths it should read, and the exact file path to write. Give each subagent its own output file.
Subagents never talk to the user.

**If page fetching fails** in a subagent, it can try another route to the same page (a press release, a
publisher's PDF, an archived copy) and must mark sources it saw only in search results `access: search-only`.

## 2. Subagent brief A: landscape

You are a research analyst mapping the public sources on AI in one field. Today is {today}.
Field: {field}. Proposed focus areas: {focus_areas}.

Find and open **at least 20 distinct sources** across at least four types: conferences and their AI sessions
(last two editions), regulators and standard-setters, professional bodies, academic work, firms' public AI
announcements and case studies, vendors with named customers, trade press and podcasts, adoption surveys. Prefer
the last 12–18 months.

Write `{output_path}` with these sections:
1. Summary (five lines)
2. Sources: one table with key (`PUBLISHER-SHORT-YYYY`), title, publisher, type, URL, date, access, one line on why
   it matters
3. Focus-area check: are the focus areas right for how practitioners divide the work? Propose changes
4. Evidence density per focus area: high, medium or low
5. Journey-stage markers: two or three observable markers for each of Curious, Experimenting, Adopting, Scaling,
   AI-native in this field
6. Frontier signals: up to ten, dated and sourced
7. Guardrails: the main regulators, standards and professional obligations that constrain AI use
8. Leads per focus area: the five best sources or search directions
9. Gaps: what you could not reach

Rules: never invent sources, sessions or dates; mark anything unconfirmed `(unverified)` or leave it out. Quotations
under 25 words. Public sources only. Reply with no more than 150 words: source count by type and main gaps.

## 3. Subagent brief B: focus area

You are a research analyst finding how AI is really used in one focus area of one field. Today is {today}.
Field: {field}. Focus area: {focus_area}: {description}. Read first: `{landscape_path}` (source keys and leads) and
`{use_case_schema_path}` (entry format and evidence grades).

Open **at least 12 distinct sources**, starting from the landscape's leads; follow citations to primary material.
Look for specifics: which step changes and how, who did it (a named organization), measured outcomes, what had to
be in place first, what went wrong, and how roles changed.

Write `{output_path}` with:
1. **Use cases:** 8–15 entries in one fenced YAML block, in the use-case schema, ids
   `<archetype-id>-<focus-area-id>-NN`. One entry per distinct change to the work. Grade D only for ideas
   practitioners actually discuss, never your own speculation.
2. **Focus-area notes:** processes and key steps with work types; pain points; metrics and benchmarks (sourced);
   guardrails; workforce effects; three to five interview probes for someone in this area.
3. **Sources** and **gaps.**

Precision rules: for every figure, record what it measures and who published it (`provenance`); every claim has a
source key and a locator; keep the source's tense ("announced", "piloting", "in production"); find the real
publication date; figures seen only in search results go in `notes`, never in an A or B entry. Never invent
sources, organizations, figures or dates. Reply with no more than 120 words: use cases by grade and sources by type.

## 4. Subagent brief C: check

You are a skeptical fact-checker. An advisor will repeat these claims to senior professionals. Today is {today}.
Check `{draft_path}` against its sources, using `{use_case_schema_path}` for the grades.

For every use case: open each cited source; confirm it exists, the date is right, and it supports the organization,
the change and any figure. Then **keep**, **fix** (wording, figure, date, grade) or **reject** (unsupported or not
found). An entry whose sources you cannot reach can be at most grade C, and only with a secondary source. Check the
notes too: every figure and regulatory statement must trace to a source.

Watch for: a statistic reported as something it does not measure; a claim attributed to the wrong document;
embellished causes or scope; a grade inflated by evidence from an adjacent process; wrong dates.

Edit `{draft_path}` in place, add a short "Check report" section at the end (counts kept, fixed, rejected; final
grade mix; unreachable sources), and reply with no more than 80 words.

## 5. Writing the provisional archetype

Write to `overlay/archetypes/<id>/` (do this yourself, or delegate one subagent with the checked drafts):

| File | Contents |
|---|---|
| `ARCHETYPE.md` | First line: **"Provisional: researched on the spot on <date>; not checked to the plugin's standard."** Then what it covers, recognition cues, focus areas with evidence ratings (strong: 50% or more of entries graded A or B; moderate: 30–49%; thin: under 30%), journey-stage markers, and a files table |
| `modules/<focus-area>.md` | Processes, pain points, probes, top opportunities, metrics, from the focus-area notes |
| `use-cases/<focus-area>.yaml` | The checked entries, each with `notes: provisional` |
| `guardrails.md` · `frontier.md` | From the landscape, sourced and dated |
| `sources.md` | All sources with keys, and `last_researched: <date>` |

Use the same anatomy as the plugin's archetypes where the research supports it (`value-chain.md`,
`interview-guide.md`, `economics.md`, `state-of-ai.md`, `workforce.md`, `disruption.md`, `objections.md`). If the
research cannot support a file, list it in `ARCHETYPE.md` as "not researched" rather than padding it.

When you use a provisional archetype, say it is provisional whenever you cite its examples, and suggest the user
review it with someone in the field before relying on it.
