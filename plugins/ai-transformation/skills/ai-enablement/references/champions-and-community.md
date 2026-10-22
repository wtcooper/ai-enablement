# Champions, office hours and communities (step 4)

Read this on entering step 4. It designs the people who carry the program into each group (champions), the places
where people get help and show their work (clinics, office hours, spotlights), and the community that keeps it going.
Source keys in brackets are listed in §6.

## 1. Goal and exit criteria

**Goal.** Social proof and help close to the work. Generative AI is discretionary: people can keep working the old
way [HARVEY-CHAMPIONS-2026], so use has to be earned through value people can see, clear expectations and respected
peers using it.

**Exit when all of these are true:** selection criteria for champions and how they are invited (the user chooses the
people); a champion role card (§3); numbers per group, recorded as a hypothesis to test; forums with rhythm, owner and
audience (§4); a plan to reach segments that do not come on their own; routes out of forums (good workflows to the
library in step 5; blocked uses to governance).

## 2. How to run it

1. **Criteria first, before names:** "What should a champion here be known for, apart from technology?" Choose for
   workflow credibility and standing in the group, not AI expertise [HARVEY-CHAMPIONS-2026; LAW360-2025].
2. **Find candidates with data:** "Who do people in each group already go to with questions about how work is done?"
   Staff surveys, help-desk patterns and practice personas help [LAW360-2025]; step 1's builders are a starting list.
3. **Role card:** "How much of a champion's time will you protect, and what will each deliver?" Agree the time with
   the champions' managers. No protected time, no champion: if the hours are not released, record the risk.
4. **Forums:** "Who comes to clinics today, and how will you reach the groups that never come? Are juniors presenting
   to partners, or only enthusiasts to each other?" Link reach to step 6.
5. **Write it** into `program.md`; add forum measures to `measures.yaml` if wanted (attendance is reach, not depth).

**Rule 11 in practice.** The user picks the people. Record champions by group and role ("two senior managers, audit
Leeds"). Never rank champions or users; recognise teams and workflows.

## 3. The champion role

**Role card:** group; role level; time per week; deliverable; forum duties; reporting line; recognition; term; the
route for what they learn (library, central team, governance).

**What firms report** (firm-reported; no comparison groups): Womble Bond Dickinson champions commit roughly 2-3 hours a
week and each completes a capstone workflow or agent for their practice group [WBD-CHAMPIONS-ND]. Lewis Silkin's
champions need not be the most advanced users; they know where the tool fits existing workflows
[HARVEY-CHAMPIONS-2026]. Ropes & Gray reports over 60 champions and growth from 32 users to about 2,200 (firm page
citing the Wall Street Journal) [ROPES-WSJ-2026]. Duane Morris names practice-group champions who test tools against
real work (`professional-services-talent-learning-02`, grade B); PwC reports over 3,200 AI champions
(`tax-research-advisory-07`, grade B).

**Numbers.** No source gives a champion-to-user ratio with outcomes. Treat any ratio as a hypothesis (Ropes & Gray's
outcome is not isolated) and review it in step 7. Say plainly that no published study measures what champion networks
add to sustained use; the firm's own measures are the test.

## 4. Forums

| Forum | Purpose | Design points |
|---|---|---|
| **Spotlight** | Social proof: people show real uses | Speakers from every level, because "a trainee and a partner" saying what they did carries weight [HARVEY-CHAMPIONS-2026]; in one Ropes & Gray practice two first-years present to partners each month [BLAW-ROPES-2026] |
| **Clinic** | Fix a specific problem on real work | Bring a task; leave with a working approach or a library candidate |
| **Office hours** | A safe place for basic questions | Specialists available [LEXIS-CONSULT-2025]; private for senior people who do not want to look unskilled |
| **Community of practice** | Learning between events | A shared domain, regular interaction and a shared practice [WENGER-ND] |

A competition that harvests real workflow problems is one alternative format [BLAW-ROPES-2026]. Keep a fixed rhythm
(for example, monthly spotlight, weekly clinic) as a habit, not a deadline; Lewis Silkin calls its cadence a
"drumbeat" [HARVEY-CHAMPIONS-2026]. Teams learn when people can admit errors without penalty (pre-AI field study)
[EDMONDSON-1999], so give senior people private and peer settings.

## 5. Rules of thumb, example and output

- **Pair a respected peer with a group of skeptics** for repeated hands-on sessions when broadcast training stalls:
  diffusion is "essentially a social process" (Gawande, citing Rogers) [GAWANDE-2013]. Early adopters are scarce in a
  low-risk-tolerance profession, so lean on trusted staff, not only volunteers [LAW360-2025].
- **After early wins, ask which tasks will be declared the default way and who signs that off;** Lewis Silkin aims for
  the tool to be "the standard way the work gets done" for tasks such as tribunal chronologies [HARVEY-CHAMPIONS-2026].
- **Traps:** champions chosen for enthusiasm alone or with no time; forums that reach only the keen; league tables.

*Illustrative (invented).* The file records "audit: two senior managers and one senior, Leeds". Role card: two hours a
week, counted toward targets; one capstone workflow each, tested in step 5; one clinic a month; a one-cycle term. A
monthly spotlight led by the managing partner puts a junior and a partner on stage.

**Output:** `program.md` section 4 (criteria, role card, numbers per group as a hypothesis, forums with rhythm and
owner, reach plan, routes); optional measures in `measures.yaml`; frontmatter `step_completed: 4`, `next_step: 5`,
`updated`.

## 6. Sources

- `BLAW-ROPES-2026`: *What Does It Take to Get Big Law Associates Excited About AI?*, Bloomberg Law, 2026-07-30. https://news.bgov.com/business-and-practice/what-does-it-take-to-get-big-law-associates-excited-about-ai
- `EDMONDSON-1999`: *Psychological Safety and Learning Behavior in Work Teams*, Amy Edmondson, Administrative Science Quarterly 44(2), June 1999. https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Group_Performance/Edmondson%20Psychological%20safety.pdf
- `GAWANDE-2013`: *Slow Ideas*, Atul Gawande, The New Yorker, 2013-07-29. https://www.newyorker.com/magazine/2013/07/29/slow-ideas
- `HARVEY-CHAMPIONS-2026`: *Harvey Power Users: The Champions Network* (Lewis Silkin interview), Harvey blog, vendor-published, 2026-06-02. https://www.harvey.ai/blog/harvey-power-users-the-champions-network
- `LAW360-2025`: *How Law Firms Turn AI Skeptics Into 'Champions'*, Law360 Pulse, 2025-09-26. https://www.law360.com/pulse/articles/2392818
- `LEXIS-CONSULT-2025`: *Driving Adoption: How Consulting Firms Can Manage Change and Overcome GenAI Resistance*, LexisNexis, vendor article, 2025-05-19. https://www.lexisnexis.com/community/insights/professional/b/industry-insights/posts/manage-change-ai-resistance
- `ROPES-WSJ-2026`: *In the WSJ, Howard Glazer Discusses Ropes & Gray's AI Champions Program*, Ropes & Gray, 2026-07-08. https://www.ropesgray.com/en/news-and-events/news/2026/07/in-the-wall-street-journal-howard-glazer-discusses-ropes-grays-ai-champions-program
- `WBD-CHAMPIONS-ND`: *Our technology solutions* (AI Champions section), Womble Bond Dickinson, undated. https://www.womblebonddickinson.com/us/about/our-technology-solutions
- `WENGER-ND`: *Introduction to communities of practice*, Wenger-Trayner, undated. https://www.wenger-trayner.com/introduction-to-communities-of-practice/
- Archetype use cases (grades as recorded): `../../transformation-advisor/references/archetypes/index.md`.
