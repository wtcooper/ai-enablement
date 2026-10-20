

**Working folder:** download sources into a private folder (`mktemp -d`), never the shared scratchpad. Other agents run in parallel and can overwrite shared files.

You are researching **how expert practitioners actually do one part of running an AI program**, so an AI
assistant can guide a head of AI, practice leader or program lead through it the way a seasoned
practitioner would. The assistant is one skill in a suite: an advisor finds and plans AI opportunities;
other skills run the portfolio, deliver solutions, run enablement and set governance. Today is 2026-10-20.

- **Topic:** AI in acquisitions and integration: how acquirers, especially private-equity-backed platforms consolidating accounting, advisory and other professional-services firms, use AI in the acquisition thesis and integration: assessing a target firm's AI and data maturity in diligence (what to ask, what to count, red flags); the repeatable capabilities (tools, workflows, training, data platforms) deployed across acquired firms and how fast; integration playbooks (sequencing, change management for incoming partners and staff, client-data separation and consent, independence checks); measuring synergy and value creation from AI after acquisition; how platforms describe AI to attract target firms and incoming partners; failures and limits. Include named platforms and firms, PE value-creation teams and operating partners, and evidence from other roll-up industries where professional-services evidence is thin
- **The skill and the steps this topic feeds:** transformation-advisor (an acquisition path: assess a target or newly acquired firm's AI maturity, with a subagent brief) and ai-portfolio (a playbook for rolling repeatable capabilities into acquired firms)

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

Write a markdown file to `/home/user/ai-enablement/research/runs/suite/topic-acquisitions.md` with these sections:

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
8. **Mapping to steps.** For each step listed above, what this topic contributes: checklists, templates
   (fields and sections), decision rules and thresholds.
9. **Sources.** ref, title, publisher or author, type, URL, date, access.
10. **Gaps.**

Then reply with a summary of **no more than 150 words**.

## Notes

- Grade A rule (2026-10-17): a figure counts as measured only when the named organization reports it as measured; recollections and rough estimates are not.
- Describe tools by runtime class (personal assistant, shared team skills, workflow automation, background agent, managed agent runtime), never recommend a vendor.
- Public sources only; no client-confidential information. Web search is rationed and shared; follow links with curl.
