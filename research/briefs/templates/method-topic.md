# Brief template: method topic (stream M)

Placeholders: `{topic}`, `{topic_focus}`, `{phases}`, `{output_path}`, `{today}`.

---


**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are researching **how expert transformation practitioners actually work**, so an AI advisor can
guide a business leader through transforming their part of the business with AI, the way a
seasoned transformation lead would. Today is {today}.

- **Topic:** {topic}: {topic_focus}
- **The advisor's phases this topic feeds:** {phases}

The advisor's loop: Onboard → Frame → Map → Diagnose → Reimagine (four lenses: improve the step,
automate the flow, delegate the outcome, reinvent the work) → Prioritize → Make the case → Plan. At
higher levels it also breaks the scope into units and rolls their plans back up. It works with users
from individual team leads to practice leaders and heads of AI, often in knowledge-work and
professional-services settings.

## Access and precision

Follow the **Access** and **Precision rules** sections of
`/home/user/ai-enablement/research/briefs/templates/module-angle.md`. In short:

- use `curl` and `pdftotext`
- give every claim a source ref and a locator
- don't embellish
- record what each statistic measures and who measured it

## What to find

Read **at least 25 distinct sources** across practitioner and academic material:

- books and practitioner guides (summarized from public material: publisher pages, author articles,
  reputable summaries)
- consultancy and research-firm publications from 2024–2026
- academic and working papers
- professional-body guidance
- practitioner case write-ups and talks

Prefer recent material for anything AI-specific. Classic method sources are fine for foundations.

## Output

Write a markdown file to `{output_path}` with these sections:

1. **Summary.** Five to eight bullets.
2. **Core concepts in plain language.** The handful of ideas the advisor must understand, each in two
   or three sentences, with what they mean for knowledge work and for AI.
3. **Expert moves.** 15–30 concrete things an experienced practitioner does: probing questions,
   heuristics, quick analyses, facilitation tactics. Format each as:
   - **move** — when to use it — what it reveals — source ref
   - Example: "Ask for last month's actual volume, not a typical week — when mapping — reveals
     variation and hidden rework."
4. **Question bank.** Questions the advisor can ask, grouped by phase and tagged with scope level
   (team / unit / organization) and journey stage where relevant.
5. **Common traps.** What goes wrong, why, and how to avoid it, with evidence where available.
   Example: automating waste.
6. **Evidence.** Data points: failure rates, value capture, adoption, outcomes. Each one with what it
   measures, its provenance and its source.
7. **Worked examples.** Two to four short examples, preferably from knowledge work or professional
   services.
8. **Mapping to phases.** For each phase in {phases}, what this topic contributes.
9. **Sources.** ref, title, publisher or author, type, URL, date, access.
10. **Gaps.**

Then reply with a summary of **no more than 150 words**.
