# Champions, office hours and communities (step 4)

Read this on entering step 4. It designs the people who carry the program into each group (champions), the places
where people get help and show their work (clinics, office hours, spotlights), and the community that keeps it going.
Source keys in brackets are listed in §8.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [The champion role](#4-the-champion-role)
5. [Forums](#5-forums)
6. [Rules of thumb and traps](#6-rules-of-thumb-and-traps)
7. [Worked example and output](#7-worked-example-and-output)
8. [Sources](#8-sources)

## 1. Goal and exit criteria

**Goal.** Social proof and help close to the work. Generative AI is discretionary: people can keep working the old
way [HARVEY-CHAMPIONS-2026], so use has to be earned through value people can see, clear expectations and respected
peers using it.

**Exit when all of these are true:**
- **Selection criteria** for champions, and how they are invited (the user chooses the people).
- **A champion role card:** time per week, deliverable, forum duties, recognition, reporting line, term.
- **Numbers per group**, recorded as a hypothesis to test, not a ratio known to work.
- **Forums** with their rhythm, owner and audience: spotlights, clinics, office hours, a community of practice.
- **Reach to the not-keen:** how forums reach segments that do not come on their own.
- **Routes out of forums:** good workflows go to the library (step 5); blocked uses go to governance.

## 2. How to run it

1. **Agree the criteria first** (H1), before anyone suggests names. Choose for workflow credibility and standing in
   the group, not AI expertise [HARVEY-CHAMPIONS-2026; LAW360-2025].
2. **Find candidates with data** (H2): staff surveys, help-desk patterns and practice personas, as one firm did
   [LAW360-2025]. The step 1 builders segment is a starting list.
3. **Write the role card** (§4) and agree the time with the champions' managers.
4. **Design the forums** (§5): a fixed rhythm, mixed seniority on stage, clinics for real problems.
5. **Plan reach** to skeptics and blocked groups (H5), and link to step 6.
6. **Write it** into `program.md`; add forum measures to `measures.yaml` if wanted (attendance is reach, not depth).

**Rule 11 in practice.** The user picks the people. Record champions by group and role ("two senior managers, audit
Leeds"). Never rank champions or users; recognise teams and workflows, not individuals by usage.

## 3. Question bank

| # | Question | Notes |
|---|---|---|
| H1 | What should a champion here be known for, apart from technology? | Criteria before names |
| H2 | Who do people in each group already go to with questions about how work is done? | Informal influence |
| H3 | How much of a champion's time will you protect, and what will each deliver? | The role is real only with time |
| H4 | Who comes to clinics today: people with a problem, or the already keen? | Reach |
| H5 | How will you reach the groups that never come? | Skeptics and blocked segments |
| H6 | Are juniors presenting to partners, or only enthusiasts presenting to each other? | Mixed seniority |
| H7 | Who leads the forum, and what rhythm will you keep even when people are busy? | Cadence |

## 4. The champion role

**Role card fields:** group; role level; time per week; deliverable; forum duties; reporting line; recognition; term;
the route for what they learn (library, central team, governance).

**What firms report** (firm-reported; no comparison groups):
- Womble Bond Dickinson champions commit roughly 2-3 hours a week and each completes a capstone, a custom agent or
  workflow for their practice group (undated firm page) [WBD-CHAMPIONS-ND].
- Lewis Silkin's champions need not be the most advanced users; they need to know where the tool fits existing
  workflows, and many are knowledge lawyers [HARVEY-CHAMPIONS-2026].
- Ropes & Gray reports over 60 champions and growth from 32 users to about 2,200 (firm news page citing the Wall
  Street Journal) [ROPES-WSJ-2026].
- Duane Morris names practice-group champions who test tools against real work
  (`professional-services-talent-learning-02`, grade B); PwC reports over 3,200 AI champions firm-wide
  (`tax-research-advisory-07`, grade B).

**Numbers.** No source gives a champion-to-user ratio with outcomes. Treat any ratio as a hypothesis (for example,
Ropes & Gray's, outcome not isolated) and review it in step 7. No protected time, no champion: if managers will not
release the hours, record the risk.

## 5. Forums

| Forum | Purpose | Design points |
|---|---|---|
| **Spotlight** | Social proof: people show real uses | Speakers from every level; Lewis Silkin's ran from junior marketing managers to partners, because "a trainee and a partner" saying what they did carries weight [HARVEY-CHAMPIONS-2026]. In one Ropes & Gray practice two first-years present AI uses to partners each month [BLAW-ROPES-2026] |
| **Clinic** | Fix a specific problem on real work | Bring a task; leave with a working approach or a library candidate |
| **Office hours** | A safe place for basic questions | Specialists available [LEXIS-CONSULT-2025]; useful for senior people who do not want to look unskilled |
| **Community of practice** | Keep learning between events | A shared domain, a community that interacts regularly, and a shared practice [WENGER-ND] |

A competition that harvests real workflow problems is one alternative format [BLAW-ROPES-2026].

**Cadence.** Pick a fixed rhythm (for example, monthly spotlight, weekly clinic) as a habit, not a deadline; Lewis
Silkin calls its cadence a "drumbeat" [HARVEY-CHAMPIONS-2026]. A rhythm the senior sponsor attends survives busy
periods.

**Psychological safety.** Teams learn from new practice when people can try things and admit errors without penalty
(pre-AI field study) [EDMONDSON-1999]. Private sessions and peer settings lower the cost for senior people.

## 6. Rules of thumb and traps

- **Pair a respected peer with a group of skeptics** for repeated hands-on sessions when broadcast training stalls:
  diffusion is "essentially a social process" (Gawande, citing Rogers) [GAWANDE-2013].
- **Early adopters are scarce in a low-risk-tolerance profession:** lean on trusted staff, not only volunteers
  [LAW360-2025].
- **After early wins, ask which tasks will be declared the default way and who signs that off.** Lewis Silkin aims for
  the tool to be "the standard way the work gets done" for tasks such as tribunal chronologies [HARVEY-CHAMPIONS-2026].
- **Say plainly** that no published study measures what champion networks add to sustained use; the firm's step 7
  measures are the test.
- **Traps:** champions chosen for enthusiasm alone; champions with no time or deliverable; forums that only reach the
  keen; only enthusiasts on stage; league tables of named people; a cadence that lapses.

## 7. Worked example and output

*Illustrative; the firm and figures are invented.* Criteria: respected in their group for how work is done, willing to
show unfinished work, able to explain to partners. The file records "audit: two senior managers and one senior, Leeds;
tax: one manager and one senior, York". Role card: two hours a week, counted toward targets; one capstone workflow each
(tested in step 5); one clinic a month; a one-cycle term. Forums: a monthly spotlight led by the managing partner with a
junior and a partner on stage; weekly clinics per practice; private office hours for partners.

**Output:** `enablement/program.md` section 4 (criteria, role card, numbers per group as a hypothesis, forums with
rhythm and owner, reach plan, routes to library and governance); optional measures in `measures.yaml`; frontmatter
`step_completed: 4`, `next_step: 5`, `updated`.

## 8. Sources

- `BLAW-ROPES-2026`: *What Does It Take to Get Big Law Associates Excited About AI?*, Bloomberg Law, 2026-07-30. https://news.bgov.com/business-and-practice/what-does-it-take-to-get-big-law-associates-excited-about-ai
- `EDMONDSON-1999`: *Psychological Safety and Learning Behavior in Work Teams*, Amy Edmondson, Administrative Science Quarterly 44(2), June 1999. https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Group_Performance/Edmondson%20Psychological%20safety.pdf
- `GAWANDE-2013`: *Slow Ideas*, Atul Gawande, The New Yorker, 2013-07-29. https://www.newyorker.com/magazine/2013/07/29/slow-ideas
- `HARVEY-CHAMPIONS-2026`: *Harvey Power Users: The Champions Network* (Lewis Silkin interview), Harvey blog, vendor-published, 2026-06-02. https://www.harvey.ai/blog/harvey-power-users-the-champions-network
- `LAW360-2025`: *How Law Firms Turn AI Skeptics Into 'Champions'*, Law360 Pulse, 2025-09-26. https://www.law360.com/pulse/articles/2392818
- `LEXIS-CONSULT-2025`: *Driving Adoption: How Consulting Firms Can Manage Change and Overcome GenAI Resistance*, LexisNexis, vendor article, 2025-05-19. https://www.lexisnexis.com/community/insights/professional/b/industry-insights/posts/manage-change-ai-resistance
- `ROPES-WSJ-2026`: *In the WSJ, Howard Glazer Discusses Ropes & Gray's AI Champions Program*, Ropes & Gray, 2026-07-08. https://www.ropesgray.com/en/news-and-events/news/2026/07/in-the-wall-street-journal-howard-glazer-discusses-ropes-grays-ai-champions-program
- `WBD-CHAMPIONS-ND`: *Our technology solutions* (AI Champions section), Womble Bond Dickinson, undated. https://www.womblebonddickinson.com/us/about/our-technology-solutions
- `WENGER-ND`: *Introduction to communities of practice*, Wenger-Trayner, undated. https://www.wenger-trayner.com/introduction-to-communities-of-practice/

Archetype use cases cited (grades as recorded): `professional-services-talent-learning-02`, `tax-research-advisory-07`
(`../../transformation-advisor/references/archetypes/index.md`).
