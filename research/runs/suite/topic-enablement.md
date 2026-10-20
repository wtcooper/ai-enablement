# Topic research: AI enablement and adoption programs

Prepared 2026-10-20 for the `ai-enablement` skill (assess and segment, design the program, curriculum by role, champions and office hours, workflow library, measure adoption and impact, influence partners and skeptics).

Conventions used throughout:

- Source refs follow `PUBLISHER-SHORT-YYYY` (`ND` = no date on the page). Locators are sections, pages or exhibit names.
- "Provenance" is one of `self-reported` (the organization about itself), `vendor-published` (a tool or training vendor), `survey-self-report` (respondents describing themselves), `independent` (third-party measurement or peer-reviewed or working-paper design).
- Grade A rule (2026-10-17): a figure counts as **measured** only when the named organization reports it as measured. Tracked usage telemetry the organization reports counts; recollection, rough estimates and respondent self-estimates do not. Rows in section 6 carry a `Measured?` flag on this basis.
- Tools are described by runtime class (personal assistant, shared team skills, workflow automation, background agent, managed agent runtime). No vendor is recommended. Vendor names appear only where a source names them.
- Items marked **(synthesis)** are the analyst's reading across sources, not a single source's claim.

---

## 1. Summary

- **Access and licences are not adoption, and adoption is not skill.** Telemetry-style "active user" metrics set a low bar (one action in 28 days in one vendor dashboard, MSLEARN-VIVA-2026). A June 2026 survey of 5,026 US knowledge workers found 5.5% at the "proficient" bar, 73.5% "experimenters" using AI for one-off tasks and 20.9% novices (SECTION-2026; vendor-published, hands-on tested). Segment people by depth of use, not by login.
- **Leaders and frontline see different programs.** Frontline regular use stalled at 51% while more than three quarters of leaders and managers used generative AI several times a week (BCG-ATWORK-2025). Executives were far more likely than individual contributors to call AI widely integrated (57% vs 18%, SECTION-2026). Enablement designed from the leadership view overstates reach.
- **The manager is the weakest link and the cheapest lever.** Only 7% of managers require AI use and tie it to performance reviews, and only 21.3% had demonstrated their own use to the team in 30 days; employees whose managers expect and require use scored 1.5x higher on proficiency (SECTION-2026; correlational). Gallup found only 22% of employees said their organization had communicated a clear plan, and those who strongly agreed it had were 3x as likely to feel very prepared (GALLUP-2025).
- **What the expert-firm programs actually do** (law, accounting, consulting): protected and credited learning time (Ropes & Gray: 20% of billable hours, BLAW-ROPES-2026), embedded champion networks (Lewis Silkin, Womble Bond Dickinson, Ropes & Gray), peer "spotlight" sessions with mixed seniority, competitions that harvest real workflow ideas, and, at the Big Four, explicit expectations in performance reviews and promotion (KPMG, Accenture) and a stated "no free pass" line for partners (PwC US CEO). No source reports a controlled test of any of these against a comparison group.
- **Employer-led support measurably raises take-up, but time savings stay modest.** In Danish matched employer-employee data, employer encouragement and training nearly doubled take-up (47% to 83%), narrowed the gender gap (11.9 to 5 points) and raised benefits 10-40%, yet average time savings were about 3% and earnings and hours effects were precisely zero (HUMLUM-BFI-2025; independent working paper).
- **Self-reported time savings need discounting.** The UK cross-government Copilot trial reported 26 minutes per user per day from self-estimated ranges (UKGDS-2025); HMRC's randomized-licence evaluation reported 2-3% of the working week (about 60 minutes per week), after a deliberate roughly 20% downward adjustment (HMRC-2026). Both are self-reported; the gap is a method lesson.
- **Most value problems are workflow problems, not training problems.** BCG finds 5% of 1,250 firms get value at scale and 60% get little, and recommends 70% of effort on people and processes (BCG-VALUEGAP-2025). Mollick's practitioner view is that individual AI gains do not translate into organizational gains without organizational innovation (MOLLICK-LAB-2025). Pair enablement with workflow redesign.
- **Evidence gap:** there is no independent evidence on champion-network effect sizes, library curation practice, partner-specific adoption, or retention of use after the first year. The advisor should say so and help the user design their own measurement.

---

## 2. Core concepts in plain language

1. **Adoption depth ladder.** People move from not using, to one-off use ("looking things up"), to repeatable embedded workflows, to building workflows for others. Section's four levels (Novice, Experimenter, Practitioner, Expert; SECTION-2026) and Zapier's four (Unacceptable, Capable, Adoptive, Transformative; ZAPIER-2026) are the same idea. *Knowledge work:* most professionals sit in the middle rung and think they are further along. *AI:* the jump that matters is from occasional prompts to a workflow someone else could reuse.
2. **Individual gain vs organizational gain.** Individuals can feel faster without the firm changing how work is staffed, reviewed or priced (MOLLICK-LAB-2025; HUMLUM-BFI-2025). *Knowledge work:* hours-based or review-heavy models can absorb the saving without anyone noticing. *AI:* enablement ends in changed workflows, not in tool familiarity.
3. **Leadership, Lab, Crowd.** Mollick's practitioner frame: leaders set direction and incentives, a small central "lab" turns discoveries into shared products and measures them, and the crowd of employees finds use cases (MOLLICK-LAB-2025). Maps cleanly to executive sponsor, enablement team and champions.
4. **Hidden use.** Where official tools are weak or use is punished, people use personal tools quietly. One study of 52 organizations and a survey found staff at over 90% of surveyed companies using personal AI tools while about 40% of companies had bought an official subscription (MIT-NANDA-2025; preliminary, anonymized). Mollick describes the same pattern as "secret cyborgs" and traces it to unclear incentives (MOLLICK-LAB-2025). *Implication:* a baseline of "official tool logins" is wrong before you start.
5. **Discretionary technology.** Generative AI is optional in the moment: unlike a leave-booking system, you can keep working the old way (HARVEY-CHAMPIONS-2026, Lewis Silkin CTO). Adoption therefore depends on perceived value, expectations and social proof, not access.
6. **Jagged frontier and uneven benefit.** In a field experiment with 758 consultants, AI raised speed, quality and completion on tasks inside its capability and not uniformly outside it; users showed "centaur" (delegate by sub-task) and "cyborg" (integrate throughout) patterns (HBS-JAGGED-2023). In a call-centre study, gains were 34% for novices and minimal for experienced staff (NBER-BRYNJOLFSSON-2023). *Implication:* segment training by task fit and by experience; do not assume juniors and seniors benefit the same way.
7. **Psychological safety and learning.** Teams learn from new practice when people can try things and admit errors without penalty (EDMONDSON-1999). *Implication for experts:* partners and senior specialists have reputational downside from visible mistakes with AI; sessions that let them learn privately or from peers lower that cost **(synthesis)**.
8. **Community of practice.** People who share a concern and get better by interacting regularly (WENGER-ND). This is the mechanism behind clinics, spotlights and champion forums; it needs a shared domain, regular meeting and shared artifacts.
9. **Change-management structure.** ADKAR (awareness, desire, knowledge, ability, reinforcement) is a common checklist for diagnosing where individuals are stuck (PROSCI-ND). Use it to diagnose, not as a curriculum. For AI, "desire" and "reinforcement" (incentives and manager behaviour) are where the evidence above shows the gaps.
10. **Center of excellence that matures into advisory.** Microsoft's Cloud Adoption Framework suggests a central AI CoE early and a move toward advisory as capability embeds; its listed duties include skills assessment, learning pathways, intake and prioritization, reusable assets with compliance checklists, and adoption KPIs (MSLEARN-COE-ND).

---

## 3. Expert moves

Format: **move** — when to use it — what it reveals — source ref (locator).

1. **Ask for the 28-day active count by team and seniority, plus the weekly-versus-monthly split, not the licence count** — when assessing baseline — reveals concentration and whether "adopted" means a handful of heavy users. Lewis Silkin reports two-thirds of users monthly and about half of those weekly (HARVEY-CHAMPIONS-2026, adoption Q&A); Gallup shows leaders at 33% frequent use vs 16% for individual contributors (GALLUP-2025, section on frequent use); the dashboard definition of "active" is one action in 28 days (MSLEARN-VIVA-2026, readiness metrics).
2. **Re-label the metric before reporting it: "licensed", "activated", "weekly", "embedded in a named workflow"** — when a sponsor quotes a headline usage figure — reveals which rung of the ladder the number measures. Basis: depth ladders in SECTION-2026 (levels) and ZAPIER-2026 (rubric); Gowling tracks "adoption depth", how often and how naturally the tool appears in regular workflows (HARVEY-GOWLING-2025, success metrics answer).
3. **Test skill with a hands-on task, not a self-rating** — when segmenting — reveals the gap between confidence and capability. Section scored prompt-writing and assistant-instruction writing by hands-on tests: 21% wrote an effective prompt, 3.8% workable assistant instructions (SECTION-2026, Key Finding 2). Wharton's respondents self-identifying as "Expert" rose to 32% (WHARTON-GBK-2025, usage section), a self-label.
4. **Ask "who is using AI that we cannot see, and why would they hide it?"** — at kickoff — reveals shadow use and the incentive problem (fear of cost cuts, no reward for disclosure, expectation creep). MIT-NANDA-2025 section 3.3; MOLLICK-LAB-2025 (Crowd and Leadership sections).
5. **Interview managers before designing training: when did you last use AI in front of your team, and what do you expect of them?** — assess and segment, any scope — reveals whether expectations and modelling exist. Only 21.3% of managers had demonstrated use in the past month; 65% set no expectations or did not hold people accountable (SECTION-2026, Key Finding 4).
6. **Write down, in advance, what happens to time saved** (capacity, growth, no layoffs, or not yet decided), and share it — before launching incentives or a mandate — reveals whether the stated vision is credible. Mollick: workers want a vivid picture of the future and clear answers on layoffs vs growth and how use will be rewarded or punished (MOLLICK-LAB-2025, Leadership section). Gallup: 15% of employees expected AI to eliminate their job within five years (GALLUP-2025).
7. **Credit learning time as billable or chargeable and say how much** — when the constraint is time — reveals whether "no time" is real. Ropes & Gray lets first-years use 20% of billable hours to learn generative AI and gives full billable credit for a firm competition (BLAW-ROPES-2026). UK trial users cited limited capacity to take part in upskilling (UKGDS-2025, challenges, "User capacity").
8. **Pick champions for workflow knowledge and standing in the group, not AI expertise** — champion design — reveals who can translate use cases into the group's actual matters. Lewis Silkin: champions need not be the most advanced users, they need to know where the tool fits existing workflows; many are knowledge lawyers (HARVEY-CHAMPIONS-2026, advice answer).
9. **Make champion duty explicit: hours, a deliverable, a forum** — champion design — reveals whether the role is real. Womble Bond Dickinson champions commit roughly 2-3 hours a week and each completes a capstone (a custom agent or workflow for their practice group); more than 150 joined since early 2026 (WBD-CHAMPIONS-ND, AI Champions section; firm-reported, page undated).
10. **Run short peer "spotlights" with speakers from every level** — community design — reveals social proof is stronger than central instruction. Lewis Silkin spotlights feature three or four speakers from junior marketing managers to IP disputes partners; "a trainee and a partner" saying what they did carries more weight (HARVEY-CHAMPIONS-2026). Ropes & Gray registered-funds practice has two first-years present AI uses to partners monthly (BLAW-ROPES-2026).
11. **Use a competition to harvest real workflow problems, with judging criteria** — when use cases are thin — reveals candidate workflows and enthusiasm. Ropes & Gray's 25 teams were judged on problem-solving, feasibility, appropriate AI use and presentation; the firm's knowledge director said teams focused on processes they are involved in rather than a giant bot (BLAW-ROPES-2026). Lewis Silkin used league tables and use-case-of-the-month prizes early on (HARVEY-LEWISSILKIN-2025).
12. **Pilot with the measures you will later report** — tool and approach selection — reveals fit before scale. Gowling's pilots measured client responsiveness, quality and risk reduction and collected practitioner feedback on workflow fit (HARVEY-GOWLING-2025, platform-selection and success-metrics answers; vendor-published interview).
13. **Build an expert-graded evaluation before rolling out to skeptical experts** — regulated or high-judgment work — reveals whether the output meets the experts' bar and gives skeptics a say. Morgan Stanley describes advisors and prompt engineers grading summarization, plus comparison with expert advisor answers (OPENAI-MSTANLEY-ND; OPENAI-ENTGUIDE-ND, "Start with evals"; vendor-published).
14. **Teach task decomposition explicitly** — curriculum design — reveals why one-shot overloaded prompts disappoint. Gowling: break complex work into steps with explicit decision criteria (HARVEY-GOWLING-2025, lessons answer).
15. **Give a safe, low-stakes first phase** — early stage — reveals comfort as the bottleneck before skill. Gowling: space for "silly poems and cats" precedes professional use (HARVEY-GOWLING-2025); KPMG's survey reports sandbox environments and "AI agent shadowing" in organizations' training (KPMG-PULSE-2025, workforce section). Mollick suggests treating training as hands-on practice more than prompt tricks (MOLLICK-LAB-2025, Crowd section).
16. **Ask which role-specific use cases the training uses; reject generic-only content** — curriculum audit — reveals compliance-only or tool-tour training. Australian trial evaluation recommends agency-specific use-case training and prompt training (DTA-2024, recommendation 1.3); HMRC non-users and users asked for practical, tailored training and time to learn (HMRC-2026); only 17% of trained workers had been trained on agents or automations and 15% only on safety and compliance (SECTION-2026, Key Finding 5).
17. **Ask for confidence and familiarity ratings by group, then target the low-confidence groups** — targeting — reveals where coaching pays. The UK trial found a correlation between users' confidence and familiarity with AI and time savings and concluded change management with communications, engagement and training was needed (UKGDS-2025, section 6).
18. **Discount self-reported savings and ask what the time was spent on** — measuring impact — reveals overclaim and whether time became capacity. HMRC cut self-reported estimates by about 20% for non-users and respondent bias and called the figure a baseline (HMRC-2026); the UK trial could not identify how saved time was spent (UKGDS-2025, section 6).
19. **Sample downstream work for "workslop"** — after a mandate or target — reveals AI output that shifts rework to colleagues. BetterUp/Stanford survey: 40% of 1,150 US desk workers received it last month, about 2 hours to resolve each incident (BETTERUP-2025); HBR frames it as mandate-following without value (HBR-WORKSLOP-2025, introduction).
20. **Ask what behaviour the metric rewards before wiring it to reviews** — leader expectations — reveals gameable targets. KPMG tracks use through tool data and will assess 2026 AI objectives in reviews while saying monitoring is not for policing (BLAW-KPMG-2025); Accenture reportedly collects weekly logins of senior staff and links leadership promotion to "regular adoption" (DECRYPT-ACCENTURE-2026, citing the FT); Shopify's CEO memo says AI use will factor into performance reviews (CNBC-SHOPIFY-2025). Logins alone can be gamed **(synthesis)**.
21. **Ask senior experts to name the tasks they would hand off, not whether they like AI** — influencing skeptics — reveals willingness without ideology. In a study of 1,500 workers across 104 occupations, workers were positive about automation for 46.1% of tasks, mainly to free time for higher-value work (STANFORD-WORKBANK-2025, findings 1).
22. **Show senior experts that their judgment is the scarce input** — partners and skeptics — reveals the framing that fits experts. Mollick: people with deep job knowledge can judge usefulness by trial and error better than outsiders (MOLLICK-LAB-2025, Crowd section); Lewis Silkin: senior lawyers tend to be confident and evaluate outputs quickly, yet many high-volume use cases sit with associates (HARVEY-CHAMPIONS-2026).
23. **State the partner expectation plainly and have the most senior person model it** — partner engagement — reveals whether expectations are real. PwC's US CEO told the FT that partners who resist AI will not be at the firm for long (CPAPA-PWC-2026); Lewis Silkin's Joint Managing Partners lead the spotlight events and rollout (HARVEY-LEWISSILKIN-2025, lessons answer). Whether the PwC approach raised partner use is not published.
24. **Collect workflows from the crowd, then centralize the best into shared assets** — library design — reveals reuse potential. Mollick's lab takes crowd prompts and solutions and distributes them quickly, building simple prompts and agents, testing and measuring (MOLLICK-LAB-2025, Lab section); Microsoft's CoE guidance lists reusable assets with compliance checklists on an internal platform and templates for common use cases (MSLEARN-COE-ND, responsibilities table); Gowling aims to build playbooks, prompt patterns and repeatable workflows (HARVEY-GOWLING-2025).
25. **Build organization-specific benchmarks** — measuring quality — reveals fitness for your own work. Mollick: official AI benchmarks rarely test writing or financial-model analysis for your context (MOLLICK-LAB-2025, Lab section).
26. **Check who owns enablement** — design — reveals missing accountability. Section found 53.2% of workers said their organization has no Head of AI or they were unsure; workers with a full-time Head of AI averaged 42 vs 33 (SECTION-2026, Key Finding 5; correlational).
27. **Define the "default way" for a named task** — scaling — reveals whether adoption is converting to standard practice. Lewis Silkin's target: for work such as an employment-tribunal chronology, using the tool is "the standard way the work gets done" (HARVEY-CHAMPIONS-2026).
28. **Plan the CoE hand-off from central to advisory** — program design at organization scale — reveals when the central team should step back. MSLEARN-COE-ND (operating model and "Evolve AI CoE operations").

---

## 4. Question bank

Tags: scope `[T]` team, `[U]` unit (practice, department), `[O]` organization; stage `explore` (access and first use), `scale` (broad rollout), `embed` (workflow change, sustained use).

### Onboard and frame

- Who sponsors this and what do they expect to be different in 12 months? Do they use it in front of others? `[U][O] explore`
- What is the outcome: faster work, better quality, new services, lower cost, or fewer people? Has anyone said that to staff? `[T][U][O] explore`
- Which tools can people use today, officially and in practice? What do people use on personal accounts? `[T][U][O] explore`
- What has been tried already (training, pilots, mandates) and what happened? `[U][O] explore`
- Who in the unit has the authority to change how a workflow runs? `[T][U] embed`

### Assess and segment

- Give me last month's active users by team and grade: how many used it weekly, monthly, once? `[T][U][O] scale`
- Among regular users, who has a repeatable workflow someone else could reuse? Who has built something for others? `[T][U] embed`
- Which groups are not using it: no access, no use case, no time, no permission, security worry, or no belief? `[T][U][O] explore`
- Do managers set expectations, model use, and hold people accountable? Ask for the last time each did. `[T][U] scale`
- How do leaders' and frontline staff's experience differ (access, training, tool fit)? `[U][O] scale`
- Who are the quiet power users and why are they quiet? `[T][U] explore`
- Where do senior experts (partners, principals, specialists) sit: use, skepticism, or avoidance, and for what reason? `[U] scale`
- How confident are people, by group? Which groups have been trained only on policy? `[U][O] scale`
- What do you believe about job security, and what has leadership said? `[T][U] explore`

### Design the program

- What is the one workflow per role where success would be obvious in 90 days? `[T][U] explore`
- How much working time can people spend learning, and does it count toward targets (billable, utilization)? `[T][U][O] explore`
- Who are the 5-10 respected people per practice group who would act as champions, and what share of their time will you protect? `[U] scale`
- What is the forum (clinic, spotlight, community) and how often? Who leads it? `[U][O] scale`
- Is there a CoE or enablement team, who leads it, and how will it hand over to the units? `[O] scale`
- What is the gate for new use cases: intake, review, risk sign-off? `[U][O] scale`

### Curriculum by role

- For each role, what are the three tasks where AI is most useful and the three where it is not? Can you show examples from your own matters or files? `[T][U] explore`
- What does a first-year or junior person need to learn now that AI changes how they learn the craft (e.g., supervised practice, simulated drafting)? `[U][O] scale`
- Who needs to learn to build and maintain shared workflows, not only use them? `[U] embed`
- What does a reviewer or approver need to check, and have they been taught? `[T][U] scale`
- What is the minimum training before access, if any, and does it differ by risk? `[O] explore`

### Champions, office hours, communities

- How will champions be chosen, recognized and relieved of other work? `[U] scale`
- What do champions deliver (a workflow, a talk, a library entry)? `[U] scale`
- Who attends clinics: users with a problem or the already keen? How do you reach the rest? `[U] scale`
- Are juniors presenting to partners, or do only enthusiasts present? `[U] scale`

### Workflow library

- Who can add a workflow, who reviews it, how is it tested and when is it retired? `[U][O] scale`
- How do people find a workflow? How do you know anyone reused it? `[U][O] embed`
- Which entries carry client, privacy or confidentiality rules and where are the checklists? `[U][O] scale`
- Which entries were created by users vs the central team? `[U][O] scale`

### Measure adoption and impact

- What does "active" mean in your numbers, and what window? `[T][U][O] scale`
- How many users have an embedded workflow vs occasional prompts? `[T][U][O] embed`
- Which time-saving figures are measured and which are estimated, and by whom? `[U][O] embed`
- What outcome (quality, turnaround, client responsiveness, risk, revenue) will tell you the program worked? `[U][O] embed`
- What downstream rework or review burden has appeared? `[T][U] embed`
- What happens to freed capacity? `[U][O] embed`

### Influence partners and skeptics

- What exactly does the skeptic worry about: accuracy, confidentiality, client reaction, craft, status, job security? `[T][U] explore`
- Which tasks would they gladly hand off? `[T][U] explore`
- Who do they respect who already uses it, and will that person show a real example? `[U] scale`
- What expectation will the most senior leaders state publicly, and will they demonstrate it? `[U][O] scale`
- What incentive or review criterion changes, if any? Could it be gamed? `[U][O] scale`

---

## 5. Common traps

| Trap | Why it happens | Evidence | How to avoid |
|---|---|---|---|
| **Counting logins or licences as adoption** | Easy to collect; looks like progress | Dashboard "active" means one action in 28 days (MSLEARN-VIVA-2026). 69% of workers said their organization had acted on agents but 16% used an agentic tool (SECTION-2026). | Report a depth ladder; add workflow-level and outcome measures. |
| **Designing from the leaders' view** | Sponsors are the heaviest users and the most enthusiastic | BCG-ATWORK-2025: frontline regular use 51% vs leaders/managers over three quarters; SECTION-2026: 82% of C-suite excited vs 30% of ICs. | Survey and interview frontline and mid-level separately. |
| **Silent or weak managers** | No expectations, no modelling | SECTION-2026: 65% of managers set no expectations or no accountability; 7% tie to reviews. | Brief and equip managers first; give them a script and a ritual (demonstrate one use per month). |
| **Compliance-only or generic training** | Safe to deliver, easy to scale | 15% of trained workers received only safety/compliance training; 17% trained on agents or automations (SECTION-2026). Wharton: training investment -8pp and confidence in training as the path to fluency -14pp (WHARTON-GBK-2025). | Role-specific, workflow-based training with hands-on practice. |
| **No plan or use case communicated** | Rollout treated as a tool deployment | 44% of employees said their organization was integrating AI; 22% a clear plan; top adoption challenge "unclear use case or value proposition" (GALLUP-2025). | Name use cases per role and say what success means. |
| **Hidden use and fear** | Unclear incentives, fear of cuts or of being devalued | MIT-NANDA-2025 s3.3 (personal tools at over 90% of companies surveyed); MOLLICK-LAB-2025. Accenture reportedly says it will exit staff for whom reskilling is not viable (BLAW-KPMG-2025 notes this; DECRYPT-ACCENTURE-2026). | Publish permitted zones, reward disclosure, say what happens to time saved. |
| **Mandate without value ("workslop")** | Pressure to show use | 40% received workslop last month, about 2 hours each (BETTERUP-2025; survey, vendor-published); HBR-WORKSLOP-2025. | Pair expectations with quality review; measure rework. |
| **Pilot-to-production chasm** | Tools run as experiments with no workflow owner | MIT-NANDA-2025: reported 5% of integrated pilots reach production value (preliminary, anonymized); BCG-VALUEGAP-2025: 60% of firms minimal value. RAND cites "more than 80%" AI project failure as an estimate by others (RAND-2024; adjacent: AI projects broadly). | Assign a workflow owner; time-box pilots with exit criteria. |
| **Individual gains, no organizational change** | No redesign of staffing, review, pricing | HUMLUM-BFI-2025: about 3% average time savings, no significant earnings or hours effects; MOLLICK-LAB-2025. | Link enablement to workflow redesign (route to portfolio and delivery skills). |
| **Overclaimed time savings** | Self-estimates; selection of active users | HMRC-2026 vs UKGDS-2025 method difference; Anthropic's internal study is self-reported (ANTHROPIC-INTERNAL-2025). | Label measured vs estimated; discount; sample actual work. |
| **Junior skill pipeline erodes** | Tasks that taught craft go away | Wharton: 43% of leaders warn of skill atrophy without role design, coaching and practice time (WHARTON-GBK-2025). Kennedys is building simulated drafting and review training (KENNEDYS-SPELLBOOK-ND; not yet reported as run). | Design supervised practice and review as part of the curriculum. |
| **Uneven take-up by group** | Differences in encouragement and training | Gender gap in chatbot adoption 11.9 points, 5 when employers encouraged use (HUMLUM-BFI-2025). | Check usage by gender, grade and location; target. |
| **No owner for enablement** | Priority without accountability | 53.2% say no Head of AI or unsure (SECTION-2026). | Name an owner with budget. |
| **Overweighting prompt tricks** | Easy to teach | Mollick: prompt techniques matter less as models improve at inferring intent (MOLLICK-LAB-2025); Section: only 21% write an effective prompt (SECTION-2026). Evidence conflicts. | Teach task framing, decomposition and checking; verify with hands-on tasks. |
| **Mandatory metrics become the goal** | Logins tied to promotion | Accenture reportedly tracks weekly logins of senior staff (DECRYPT-ACCENTURE-2026, via FT); KPMG says monitoring is not for policing (BLAW-KPMG-2025). No published evidence either way on gaming. | Track depth and outcome alongside; sample for quality. |

---

## 6. Evidence

`Measured?` applies the Grade A rule: yes only if the named organization reports a tracked metric or study of its own.

| # | Data point | What it measures | Provenance | Measured? | Source (locator) |
|---|---|---|---|---|---|
| E1 | 46% of business leaders use generative AI daily (+17pp year on year), 82% at least weekly; 72% formally track business-linked ROI | Share of about 800 US enterprise decision-makers (1,000+ employees) surveyed 26 Jun-11 Jul 2025 | Wharton Human-AI Research with GBK Collective; survey-self-report | Survey result; not telemetry | WHARTON-GBK-2025, executive summary, sections 1-2 |
| E2 | Training investment down 8pp; confidence in training as primary path to fluency down 14pp; 61% implementing employee training and awareness programs; 43% warn of skill atrophy | Same survey | survey-self-report | No | WHARTON-GBK-2025, section 3 |
| E3 | 5% of 1,250 firms achieve AI value at scale; 60% report minimal value; 35% scaling | Self-reported value outcomes in BCG study of 1,250 firms | BCG; vendor-published survey | No | BCG-VALUEGAP-2025, p.1 and Exhibit 1 |
| E4 | Future-built firms upskill more than 50% of internal workforce; BCG exhibit says they are 4x as likely to dedicate time and structure programs for AI learning and 2x as likely to involve employees (comparison group per BCG's exhibit) | Survey comparison between top 5% and others | BCG; vendor-published | No | BCG-VALUEGAP-2025, "Secure and enable necessary talent" exhibit |
| E5 | 10-20-70 rule: 70% of strategic focus on people and processes, 20% technology, 10% algorithms | BCG's recommended allocation, not an observed fact | BCG; vendor-published | No | BCG-VALUEGAP-2025, conclusions |
| E6 | Frontline regular use 51%; over three quarters of leaders and managers use several times a week; sentiment positive rises 15% to 55% with strong leadership support | BCG AI at Work survey of 10,600+ leaders, managers, frontline staff in 11 countries and regions | BCG; survey-self-report | No | BCG-ATWORK-2025, Key Takeaways and opening |
| E7 | 5.5% proficient; 73.5% experimenters; 20.9% novices; 21% write an effective prompt; 3.8% workable assistant instructions | 5,026 US knowledge workers, proficiency from usage, knowledge and hands-on skill tests | Section; vendor-published (AI training company) | Hands-on tested by Section; the vendor reports it | SECTION-2026, Key Finding 2 |
| E8 | 7% of managers require AI use and tie it to performance reviews; 21.3% demonstrated AI use to their team in 30 days; employees whose managers expect and require use score 1.5x higher and are 2.7x more likely to be excited | Same survey; association, not causal | vendor-published | No | SECTION-2026, Key Finding 4 |
| E9 | 62% of workers received AI training; 37.8% none; 15% of trained had only safety and compliance; 17% trained on agents or automations | Same survey | vendor-published | No | SECTION-2026, Key Finding 5 |
| E10 | Employees: 40% used AI at work a few times a year or more (21% in 2023); 19% frequent; 8% daily; professional services 34% frequent; leaders 33% vs ICs 16% | Gallup Panel of US employees, self-administered web surveys | Gallup; independent survey | Survey; not telemetry | GALLUP-2025, opening sections (page dated June 2025) |
| E11 | 44% say organization integrating AI; 22% say clear plan communicated; clear plan associated with 3x "very prepared" and 2.6x comfortable; 16% of users strongly agree provided tools are useful | Same panel | independent survey | No | GALLUP-2025, "Leadership Guidance on AI Lags Integration" |
| E12 | Take-up 47% to 83% with employer encouragement and initiatives; gender gap 11.9 to 5 points; benefits 10-40% greater with encouragement; 30% of employees trained; average time savings 3%; zero effect on earnings and hours (CI excludes over 1%) | Surveys of 25,000 workers, 7,000 workplaces, 11 occupations (late 2023 and 2024) linked to Danish administrative data | Chicago Booth BFI working paper (not peer reviewed at publication); independent | Time savings self-reported; earnings and hours are administrative records | HUMLUM-BFI-2025, abstract and introduction |
| E13 | 26 minutes saved per user per day on average; about 80% adoption; 39% used multiple times a day and 43% multiple times a week; 17% saw no clear savings; correlation between confidence/familiarity and time saved | 20,000 government employees, 30 Sep-31 Dec 2024; savings from self-selected time ranges (midpoint method) | UK Government Digital Service; self-reported (published June 2025) | Usage engagement as surveyed; savings self-estimated | UKGDS-2025, sections 3-6 |
| E14 | 83% of randomly licensed staff used it; satisfaction 7.1 out of 10; 61% would be disappointed to lose it; self-reported time saving 2-3% of the working week (about 60 minutes), estimates reduced about 20% | 3,000 randomly allocated licences plus 500 volunteers; survey of 1,364 (45% of random group), usage statistics, focus groups | HMRC; self-reported survey with telemetry | Usage from dashboard; savings self-reported | HMRC-2026, methodology and results (published 9 July 2026) |
| E15 | Only a third used Copilot daily; 64% of managers perceived efficiency and quality uplift; 40% reallocated time | Australian Public Service whole-of-government trial evaluation | DTA; self-reported evaluation | Partly | DTA-2024, overarching findings |
| E16 | Resistance to AI agents fell from 47% to 21% in a quarter; 55% accepting or embracing | KPMG Q3 2025 AI Quarterly Pulse of organizational leaders (sample size not read) | KPMG; vendor-published survey | No | KPMG-PULSE-2025, workforce transformation |
| E17 | Ropes & Gray: 32 Harvey users two years ago to about 2,200 employees sending over 282,000 prompts a month; each user three times as active as a year ago; over 60 champions | Platform usage reported by the firm via a law-firm news page citing the WSJ (WSJ article not read) | self-reported | Yes (firm-reported usage figures; second-hand) | ROPES-WSJ-2026 |
| E18 | Lewis Silkin: two-thirds of users engage monthly, about half of those weekly | Firm-reported usage distribution | self-reported via vendor blog | Yes (firm-reported); definitions not given | HARVEY-CHAMPIONS-2026 |
| E19 | Womble Bond Dickinson: 150+ champions, 2-3 hours per week, capstone workflow per champion | Program description | self-reported; undated page | Yes (program fact) | WBD-CHAMPIONS-ND |
| E20 | Accenture: 550,000 of 780,000 employees trained in generative AI (30 in 2022); $1 billion a year on learning | Reported by Decrypt from Accenture-attributed figures; second-hand | self-reported via press | Not verified at source | DECRYPT-ACCENTURE-2026 |
| E21 | KPMG tracks AI use via Copilot data and will assess 2026 AI objectives in reviews | Program description by KPMG's global AI workforce lead | self-reported via Bloomberg | Program fact | BLAW-KPMG-2025 |
| E22 | Morgan Stanley: case page says over 98% of advisor teams actively use the assistant; the guide says 98% of advisors use OpenAI daily; document access from 20% to 80% | Firm and vendor statements; wording differs between the two pages | vendor-published | Not verified; definition unclear | OPENAI-MSTANLEY-ND; OPENAI-ENTGUIDE-ND, "Start with evals" |
| E23 | BBVA: over 2,900 custom GPTs in five months; 125,000 employees; Legal team uses ChatGPT for 40,000 questions a year | Vendor-reported usage | vendor-published | Not verified | OPENAI-ENTGUIDE-ND, "Get AI in the hands of experts" |
| E24 | Anthropic internal survey: employees report using Claude in 59-60% of work and +50% productivity (from 28% and +20% a year earlier); 27% of assisted work would not otherwise have been done | 132 engineers and researchers surveyed Aug 2025, 53 interviews, plus usage data | Anthropic; self-reported | Survey self-report | ANTHROPIC-INTERNAL-2025, key findings |
| E25 | 95% of organizations getting zero return; 5% of integrated pilots extract value; external partnerships twice the success of internal builds; shadow use at over 90% of companies vs 40% official subscriptions | 52 organization interviews, 153 leaders surveyed, 300 public initiatives; authors say findings are preliminary and company data anonymized | MIT NANDA project; independent but unverified | No | MIT-NANDA-2025, executive summary and 3.3 |
| E26 | Downstream "workslop": 40% received last month; 2 hours per incident; $186 per employee per month | 1,150 US full-time desk workers surveyed Sep 2025; cost is a vendor model | BetterUp Labs with Stanford Social Media Lab | No | BETTERUP-2025 |
| E27 | Training required before access: 11% of firms under 50 lawyers, 30% (50-149), 47% (150-349), 63% (350-699), 72% (700+); encourage experimentation within policy 24% to 57% | ILTA 2026 survey of law-firm technology leaders (respondent count not read) | ILTA; survey-self-report | No | ILTA-2026, Q3.18 |
| E28 | Insufficient worker skills the biggest barrier to integrating AI into workflows; 53% educating broader workforce to raise fluency; 48% upskilling and reskilling | 3,235 senior leaders in 24 countries, Aug-Sep 2025 | Deloitte; survey-self-report | No | DELOITTE-2026 |
| E29 | 14% productivity gain on average, 34% for novice and low-skilled; minimal for experienced | 5,179 customer support agents, staggered rollout, issues resolved per hour (administrative data) | NBER working paper; independent | Yes (study measured) | NBER-BRYNJOLFSSON-2023, abstract (adjacent: customer support) |
| E30 | Inside the capability frontier: speed over 25%, human-rated quality over 40%, completion over 12% | Field experiment, 758 BCG consultants | HBS/BCG-Harvard collaboration; independent design | Yes (study measured) | HBS-JAGGED-2023, key findings (adjacent: consulting tasks, not enablement) |
| E31 | Directive (delegating whole tasks) share of Claude.ai conversations rose from 27% to 39% | Sample of conversations; not enterprise-specific | Anthropic; self-reported | Yes (platform data) | ANTHROPIC-ECONIDX-2025, key findings |
| E32 | Workers positive about automation for 46.1% of 844 tasks | 1,500 workers, 104 occupations | Stanford-led working paper; independent | Survey | STANFORD-WORKBANK-2025, intro finding 1 |
| E33 | Prosci reports 60% of leaders have no clear path to AI implementation; 29% of participants cite fear and lack of understanding; 43% say more than half of manager resistance was avoidable | Prosci research; sample not on page | vendor-published | No | PROSCI-ND, landing page |
| E34 | JPMorgan: all new hires to get prompt engineering training (stated 2024) | Executive statement at investor day | self-reported | No (statement, not completion data) | QUARTZ-JPM-2024 |
| E35 | A&O: about 3,500 lawyers sent about 40,000 queries during trial (from Nov 2022) | Firm press release | self-reported | Yes (firm-reported); dated 2023 | AO-HARVEY-2023 |

---

## 7. Worked examples

### Example 1: Credited time plus peer showcase in a large law firm (Ropes & Gray)

- **Situation:** a large firm wanted associates, not only enthusiasts, to use AI in their daily work despite career anxiety (BLAW-ROPES-2026).
- **What was done (as reported):** a firmwide program lets first-years devote 20% of billable hours to learning generative AI; in one practice two first-years each month present uses to partners; a firm-and-summer-associate "World Cup" of 25 teams, full billable credit, judged on problem-solving, feasibility, appropriate AI use and presentation; a winning team built an extraction workflow for closing documents. The firm separately reports a champions network of over 60 and growth from 32 to about 2,200 users (ROPES-WSJ-2026).
- **What is not published:** whether usage persisted, quality effects, partner usage, or the cost of the credited hours.
- **Lessons for the advisor:** credit the time, make juniors visible to partners, and harvest process-level ideas rather than "a bot that solves everything". Ask the user for their equivalent of the 20% allowance and the equivalent audience.

### Example 2: Embedded leads and spotlights (Lewis Silkin)

- **Situation:** the CTO describes AI as "highly discretionary" and wants the tool to be the default for tasks like tribunal chronologies (HARVEY-CHAMPIONS-2026).
- **What was done (as reported):** Knowledge Lawyers front the program; each team has a lead who works with champions to find use cases; firmwide spotlights led by the Joint Managing Partners; league tables and use-case-of-the-month prizes early on; communications cadence. Top users span apprentices to senior partners (HARVEY-LEWISSILKIN-2025).
- **Result reported:** two-thirds of users monthly, half of those weekly; consistent growth since launch; success defined at that time as "a culture of experimentation and some good use cases", with usage tracked and feedback collected. No outcome metrics.
- **Lessons:** the firm itself identifies the next step as moving from individual experimentation to group-level adoption. Advisor prompt: "Which tasks will you declare the default way, and who signs that off?"

### Example 3: Measuring savings honestly (UK government trials)

- **Situation:** two UK public-sector evaluations of the same assistant tool gave very different headline savings (UKGDS-2025; HMRC-2026).
- **What was done:** the cross-government experiment (20,000 staff, Oct-Dec 2024) asked users to pick a time-saving range and used the midpoint, giving 26 minutes per day; HMRC randomly allocated 3,000 licences, surveyed 1,364, used usage dashboards, and discounted estimates by about 20%, giving 2-3% of the week (about 60 minutes).
- **Lessons:** use random allocation when you can; compare licensed users with a control; discount self-reports; ask what the time was used for; keep non-users in the denominator; capture reasons for non-use (HMRC: 46% of non-users cited security and data privacy concerns).

### Example 4: Big Four expectations and partner messaging (KPMG, Accenture, PwC)

- **Situation:** firms moving from access to expectation (BLAW-KPMG-2025; DECRYPT-ACCENTURE-2026; CPAPA-PWC-2026).
- **What was done (as reported):** KPMG tracks tool use from Copilot data and will assess each person's 2026 AI objectives in reviews; Accenture reportedly collects weekly logins of senior staff and requires "regular adoption" for leadership promotion; PwC's US CEO told the FT partners who resist AI will not stay.
- **What is not published:** use after the policies, quality effects, attrition, or whether partners complied. KPMG says its monitoring is to measure the value of its investment and not for policing.
- **Lessons:** expectation setting is common at the top of the market, but the evidence is announcements. Advisor prompt: "What would the metric reward, and how would you check the quality of what it produces?"

---

## 8. Mapping to steps

Thresholds below are **proposed defaults** drawn from the sources, not validated cut-offs. Tell the user which are rules of thumb.

### 8.1 Assess and segment

- **Checklist**
  - Pull 28-day active counts by team, grade, location, gender; split weekly, monthly, once.
  - Ask for personal-tool and unofficial use (survey with safe disclosure).
  - Interview managers on expectations and modelling.
  - Sample actual work for depth: repeatable workflow, shared workflow, built something.
  - Find senior experts' position and reasons.
- **Segment template (fields):** segment name; size; depth rung (not using / one-off / repeatable / builder); access (yes/no, which class of tool); main barrier (access, use case, time, permission, security, belief, fear); manager behaviour (none / encourages / requires); confidence rating; role task examples; proposed first move.
- **Default segments (synthesis):** power users and builders; regular but one-off users; occasional or lapsed; non-users blocked by access or permission; non-users by belief or fear (skeptics); senior experts (use and lead status vary independently).
- **Decision rules**
  - If "official tool" use is under 50% but surveyed personal use is higher, treat as an access and trust problem first, not a skills problem (MIT-NANDA-2025; MOLLICK-LAB-2025).
  - If the sponsor's view and frontline view differ by more than 25 points on "AI widely integrated" or use, treat leadership view as unreliable and re-baseline (SECTION-2026 gap 57% vs 18%; BCG-ATWORK-2025).
  - Do not use a login metric alone; require one depth indicator.
- **Skill test:** use a short hands-on task per role rather than self-rating (SECTION-2026).

### 8.2 Design the program

- **Checklist:** sponsor and message; owner (named); time allowance and credit rule; curriculum by role; champion network; forums; library and gate; measurement plan; manager enablement; expectation and incentive design; CoE-to-advisory transition plan.
- **Program charter template (fields):** goal and time horizon; the workflow(s) targeted; segments and targets; learning time per person and how credited; champion count, hours, deliverable; forums and cadence; library governance (owner, reviewer, retire); metrics (activity, depth, outcome) with definitions and data source; leader and manager expectations; what happens to saved time; risk and policy links (route to governance skill).
- **Decision rules**
  - Centralize first when capability is low; move to advisory as units embed (MSLEARN-COE-ND).
  - Pair training with a named workflow and manager expectation; training alone has weak backing (BCG-ATWORK-2025 says five or more hours of training plus in-person coaching associated with higher regular use; qualitative statement).
  - Reserve learning time; if none can be protected, expect low take-up (UKGDS-2025 capacity).

### 8.3 Curriculum by role

- **Checklist:** role map; top three tasks where AI helps and three where it does not (jagged frontier); safe sandbox; hands-on practice on real work; decomposition and verification; reviewer checks; build track for champions; junior supervised practice; refreshers as tools change.
- **Curriculum template (fields):** role; tasks in scope; example from own work; practice exercise; verification step; risk rule; time required; assessment (hands-on); follow-up (clinic or champion).
- **Tiers (synthesis built on the depth ladders):** Foundations (all), Role workflows (by role), Builder (champions and power users), Leader and manager (expectations, modelling, review of AI-assisted work).
- **Decision rules**
  - Content must include building and reuse, not only safety and compliance (SECTION-2026: 15% compliance-only; 17% trained on agents).
  - Target low-confidence groups first (UKGDS-2025 correlation).
  - Treat prompt techniques as perishable; teach task framing, decomposition and checking (MOLLICK-LAB-2025; HARVEY-GOWLING-2025).

### 8.4 Champions and office hours

- **Checklist:** selection criteria; time and recognition; kick-off and community charter; spotlight cadence with mixed seniority; clinics for specific problems; escalation path to the library; communications drumbeat.
- **Champion role card (fields):** group; name; time per week (reference 2-3 hours, WBD-CHAMPIONS-ND); deliverable (capstone workflow or use-case write-up); forum duties; reporting line; recognition; term.
- **Decision rules**
  - Choose by workflow credibility and influence, not by being the most advanced user (HARVEY-CHAMPIONS-2026).
  - Include juniors in showcases to partners (BLAW-ROPES-2026).
  - Cadence: pick a fixed rhythm (monthly spotlights, regular clinics) and keep it; Lewis Silkin calls the cadence "drumbeat".
  - No source gives a champion-to-user ratio with outcomes; the advisor should treat ratio as a hypothesis to test (e.g., Ropes & Gray: over 60 champions for about 2,200 users, outcome not isolated).

### 8.5 Workflow library

- **Checklist:** intake from crowd; triage; test on real examples; owner; review and risk tags; versioning; discoverability; reuse tracking; retirement.
- **Library entry template (fields):** name; task and role; inputs and outputs; instructions or prompt pattern; example input and output; known failure modes; verification step; risk and confidentiality tag; owner; reviewer; last tested; reuse count; retire-by date.
- **Decision rules**
  - Start from what the crowd has built (MOLLICK-LAB-2025; BBVA's bottom-up custom assistants, OPENAI-ENTGUIDE-ND, vendor-published).
  - Publish reusable assets with compliance checklists on an internal platform (MSLEARN-COE-ND).
  - Evidence on curation practice and retirement is thin (see Gaps); use reuse counts and last-tested dates as the guard.

### 8.6 Measure adoption and impact

- **Checklist:** define each metric; pick window; separate licensed, activated, active, repeated, embedded; add outcome measures; run a baseline; sample quality; compare to control where possible; report measured vs estimated.
- **Metric template (fields):** name; definition; numerator and denominator; window; data source; who measures; provenance (telemetry / survey / observed); known bias; target; owner.
- **Suggested layers (synthesis):**
  1. Reach: licensed, activated.
  2. Activity: weekly active (not 28-day one action), by segment.
  3. Depth: share with a repeatable workflow; share building for others; collaboration mode shift (cf. ANTHROPIC-ECONIDX-2025 directive vs iterative).
  4. Embedded: named workflows where the tool is the default.
  5. Outcome: cycle time, quality (review findings, rework), client responsiveness and risk (HARVEY-GOWLING-2025), capacity redeployed.
  6. Sentiment and confidence by segment.
- **Decision rules**
  - Time-saving claims: report measured or controlled results separately from survey estimates; discount estimates (HMRC-2026 used about 20%).
  - Always include non-users in denominators and capture reasons.
  - Watch for downstream rework (BETTERUP-2025).
  - Do not link a login target to rewards without a quality check **(synthesis)**.

### 8.7 Influence partners and skeptics

- **Checklist:** map concerns; find respected users; peer demonstrations on their own matters; state expectations; model by most senior leaders; provide private practice; reward disclosure; handle accuracy and client questions with an evaluation or review standard.
- **Stakeholder card (fields):** person or group; role and influence; stated concern; underlying driver (accuracy, status, craft, client, job); trusted peer; first low-risk task; evidence they would accept; expectation and by when.
- **Decision rules**
  - Use peer demonstration plus a stated expectation; neither alone is backed (HARVEY-CHAMPIONS-2026; CPAPA-PWC-2026).
  - For high-judgment work offer an expert-graded evaluation before asking for use (OPENAI-MSTANLEY-ND).
  - Frame experts' judgment as the scarce input (MOLLICK-LAB-2025).
  - Check that incentives do not reward visible use over quality (BETTERUP-2025; HBR-WORKSLOP-2025).

---

## 9. Sources

Access: `full` = read in full or the relevant sections; `partial` = read part (paywall, truncated, gated or only a landing page). All retrieved 2026-10-20 by curl, pdftotext or the r.jina.ai text mirror unless noted. Provenance of each source is in section 6 or the claim.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| WHARTON-GBK-2025 | Accountable Acceleration: Gen AI Fast-Tracks into the Enterprise | Wharton Human-AI Research and GBK Collective | survey report (PDF) | https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf | Oct 2025 | full |
| BCG-VALUEGAP-2025 | The Widening AI Value Gap | BCG | consultancy report (PDF) | https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf | Oct 2025 | full |
| BCG-ATWORK-2025 | AI at Work: Momentum Builds, but Gaps Remain | BCG | consultancy article | https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain | Jun 2025 (slideshow file names) | partial (article via text mirror; slideshow not read) |
| MOLLICK-LAB-2025 | Making AI Work: Leadership, Lab, and Crowd | Ethan Mollick, One Useful Thing | practitioner article | https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and | 22 May 2025 | full |
| PRH-COINTEL-ND | Co-Intelligence (book page) | Ethan Mollick, Penguin Random House | book, publisher page | https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/ | 2024 book; page undated | partial (blurb only) |
| MIT-NANDA-2025 | The GenAI Divide: State of AI in Business 2025 | MIT NANDA (Challapally et al.) | research report (PDF, preliminary) | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf | Jul 2025 | full |
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work (NBER WP 31161) | Brynjolfsson, Li, Raymond | academic working paper | https://www.nber.org/system/files/working_papers/w31161/w31161.pdf | Apr 2023, rev. Nov 2023 | partial (abstract and introduction) |
| HBS-JAGGED-2023 | Navigating the Jagged Technological Frontier (summary page) | Harvard D^3 Institute with BCG | academic study summary | https://d3.harvard.edu/navigating-the-jagged-technological-frontier/ | 21 Sep 2023 | partial (summary, not the full paper) |
| HUMLUM-BFI-2025 | Large Language Models, Small Labor Market Effects (WP 2025-56) | Humlum and Vestergaard, Becker Friedman Institute | academic working paper | https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf | 9 May 2025 | partial (abstract, introduction) |
| STANFORD-WORKBANK-2025 | Future of Work with AI Agents (WORKBank, Human Agency Scale) | Shao et al., arXiv 2506.06576 | academic paper | https://arxiv.org/pdf/2506.06576 | Jun 2025 | partial (abstract, introduction) |
| EDMONDSON-1999 | Psychological Safety and Learning Behavior in Work Teams | Amy Edmondson, Administrative Science Quarterly 44(2) | academic paper (classic) | https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Group_Performance/Edmondson%20Psychological%20safety.pdf | Jun 1999 | partial (abstract) |
| WENGER-ND | Introduction to communities of practice | Wenger-Trayner | practitioner guide | https://www.wenger-trayner.com/introduction-to-communities-of-practice/ | undated | partial (definition) |
| PROSCI-ND | Win With AI by Leading the Human Side; ADKAR Model | Prosci | method vendor pages | https://empower.prosci.com/ai-adoption-white-paper ; https://www.prosci.com/methodology/adkar | undated | partial (landing pages; white paper not downloaded) |
| RAND-2024 | The Root Causes of Failure for AI Projects and How They Can Succeed | RAND | research report | https://www.rand.org/pubs/research_reports/RRA2680-1.html | 13 Aug 2024 | partial (summary) |
| GALLUP-2025 | AI Use at Work Has Nearly Doubled in Two Years | Gallup (Ryan Pendell) | independent survey article | https://www.gallup.com/workplace/691643/work-nearly-doubled-two-years.aspx | Jun 2025 (page metadata 15 Jun 2025) | full |
| SECTION-2026 | The AI Proficiency Report | Section | training-vendor survey report | https://www.sectionai.com/ai/the-ai-proficiency-report | Jun 2026 | partial (public summary; full report gated) |
| ZAPIER-2026 | How to measure your AI fluency, and move to the next level | Zapier (Jessica Lau) | practitioner article | https://zapier.com/blog/ai-fluency/ | 2 Feb 2026 | full |
| MSFT-WTI-2025 | 2025: The year the Frontier Firm is born (Work Trend Index) | Microsoft | vendor research report | https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born | 2025 | partial (used only for context) |
| MSLEARN-COE-ND | Establish an AI Center of Excellence (Cloud Adoption Framework) | Microsoft Learn | vendor practitioner guide | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence | undated | full |
| MSLEARN-VIVA-2026 | Microsoft Copilot Dashboard in Viva Insights | Microsoft Learn | product documentation | https://learn.microsoft.com/en-us/viva/insights/org-team-insights/copilot-dashboard | undated (mentions Feb 2026 fix) | partial |
| KPMG-PULSE-2025 | KPMG Q3 2025 AI Quarterly Pulse Survey | KPMG US | firm survey press release | https://kpmg.com/us/en/media/news/q3-ai-pulse.html | 18 Sep 2025 | full |
| BLAW-KPMG-2025 | KPMG Staff to Be Rated on AI Usage in Yearly Performance Reviews | Bloomberg Law (James Booth) | news | https://news.bgov.com/health-law-and-business/kpmg-staff-to-be-rated-on-ai-usage-in-yearly-performance-reviews | 31 Oct 2025 | full |
| DECRYPT-ACCENTURE-2026 | Accenture Is Tracking Whether Employees Use AI, and Promotions Are on the Line | Decrypt, citing the Financial Times | news (second-hand) | https://decrypt.co/358616/accenture-tracking-employees-use-ai-promotions | 19 Feb 2026 | partial (FT original not read) |
| CPAPA-PWC-2026 | PwC CEO Says Partners Who Resist AI "Have No Place at the Firm" | CPA Practice Advisor, citing the Financial Times | news (second-hand) | https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/ | 25 Mar 2026 | full (FT original not read) |
| QUARTZ-JPM-2024 | JPMorgan Chase is training every new hire on AI | Quartz | news | https://qz.com/jpmorgan-chase-ai-banking-training-mary-erdoes-1851488056 | 20 May 2024 | full |
| BLAW-ROPES-2026 | What Does It Take to Get Big Law Associates Excited About AI? | Bloomberg Law (Roy Strom) | news column | https://news.bgov.com/business-and-practice/what-does-it-take-to-get-big-law-associates-excited-about-ai | 30 Jul 2026 | full |
| ROPES-WSJ-2026 | In the WSJ, Howard Glazer Discusses Ropes & Gray's AI Champions Program | Ropes & Gray | firm news page | https://www.ropesgray.com/en/news-and-events/news/2026/07/in-the-wall-street-journal-howard-glazer-discusses-ropes-grays-ai-champions-program | 8 Jul 2026 | full (WSJ original not read) |
| HARVEY-GOWLING-2025 | Al Hounsell on Driving Legal Transformation That Lasts | Harvey blog (interview, Gowling WLG) | vendor-published interview | https://www.harvey.ai/blog/al-hounsell-on-driving-legal-transformation-that-lasts | 30 Oct 2025 | full |
| HARVEY-LEWISSILKIN-2025 | Alex Bazin on Empowering Teams With Legal AI | Harvey blog (interview, Lewis Silkin) | vendor-published interview | https://www.harvey.ai/blog/alex-bazin-on-empowering-teams-with-legal-ai | 27 Nov 2025 | full |
| HARVEY-CHAMPIONS-2026 | Harvey Power Users: The Champions Network | Harvey blog (interview, Lewis Silkin) | vendor-published interview | https://www.harvey.ai/blog/harvey-power-users-the-champions-network | 2 Jun 2026 (page metadata) | full |
| WBD-CHAMPIONS-ND | Our technology solutions | Womble Bond Dickinson | firm web page | https://www.womblebonddickinson.com/us/about/our-technology-solutions | undated | full (champions section) |
| AO-HARVEY-2023 | A&O announces exclusive launch partnership with Harvey | Allen & Overy | firm press release | https://www.aoshearman.com/en/news/ao-announces-exclusive-launch-partnership-with-harvey | 15 Feb 2023 | partial |
| KENNEDYS-SPELLBOOK-ND | Kennedys customer story | Spellbook | vendor case page | https://spellbook.com/stories/kennedys | undated (programme "set to debut later this year") | full |
| OPENAI-ENTGUIDE-ND | AI in the Enterprise | OpenAI | vendor guide (PDF) | https://cdn.openai.com/business-guides-and-resources/ai-in-the-enterprise.pdf | undated | full |
| OPENAI-MSTANLEY-ND | Morgan Stanley uses AI evals to shape the future of financial services | OpenAI | vendor case study | https://openai.com/index/morgan-stanley/ | undated | full |
| ANTHROPIC-INTERNAL-2025 | How AI is transforming work at Anthropic | Anthropic | organization self-study | https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic | 2 Dec 2025 | partial |
| ANTHROPIC-ECONIDX-2025 | Anthropic Economic Index report (September 2025) | Anthropic | platform usage research | https://www.anthropic.com/research/anthropic-economic-index-september-2025-report | 15 Sep 2025 | partial |
| UKGDS-2025 | Microsoft 365 Copilot Experiment: Cross-Government Findings Report | UK Government Digital Service | government evaluation (PDF) | https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf | Jun 2025 (publication 2 Jun 2025 per GOV.UK listing) | full |
| HMRC-2026 | Evaluating the impact of Microsoft Copilot in HMRC | HM Revenue and Customs | government evaluation | https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot/evaluating-the-impact-of-microsoft-copilot-in-hmrc | 9 Jul 2026 | full |
| DTA-2024 | Copilot trial summary report: executive summary | Digital Transformation Agency (Australia) | government evaluation | https://www.digital.gov.au/initiatives/copilot-trial/summary-evaluation-findings/cts-executive-summary | 2024 (Oct 2024 per file path) | full |
| BETTERUP-2025 | Workslop: The Hidden Cost of AI-Generated Busywork | BetterUp Labs with Stanford Social Media Lab | vendor research page | https://www.betterup.com/workslop | Sep 2025 survey | full |
| HBR-WORKSLOP-2025 | AI-Generated "Workslop" Is Destroying Productivity | Harvard Business Review | practitioner article | https://hbr.org/2025/09/ai-generated-workslop-is-destroying-productivity | 22 Sep 2025 | partial (opening only) |
| ILTA-2026 | The ILTA Technology Survey 2026 Executive Summary | ILTA | professional-body survey (PDF) | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | Jun 2026 (file name) | partial |
| DELOITTE-2026 | The State of AI in the Enterprise, 2026 AI report | Deloitte | consultancy survey report | https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html | 2026 (survey Aug-Sep 2025) | partial |
| CNBC-SHOPIFY-2025 | Shopify CEO says staffers need to prove jobs can't be done by AI | CNBC | news | https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html | 7 Apr 2025 | full |
| HARVEY-PU-ND | Perspectives on Legal AI's Power Users (RSGI) | Harvey / RSGI | vendor-sponsored feature | https://www.harvey.ai/resources/reports/perspectives-on-legal-ais-power-users | 2026 (undated) | search-only (landing page read; report gated; no figures used) |

Search results used only to locate sources (not as evidence): JPMorgan LLM Suite reach and KPMG/Deloitte academy offerings (`search-only`, no figures used).

---

## 10. Gaps

- **Champion and office-hours effectiveness:** no published controlled or even before-and-after measurement tying champion networks, clinics or communities to sustained use. Available figures are firm-reported counts (Ropes & Gray, Womble Bond Dickinson, Lewis Silkin) without comparison groups. The Australian trial recommends champions but its basis was not read in detail.
- **Partner and senior-expert adoption:** announcements (PwC, KPMG, Accenture) and interview statements only. No published usage or quality data for partners after expectations were set; no data on attrition or compliance.
- **Retention and sustained use:** no cohort retention curves beyond about a year. Ropes & Gray's "three times as active" is one firm's per-user activity figure over one year.
- **Library curation:** only the Microsoft CoE guidance and practitioner statements; no evidence on review cadence, retirement, reuse rates or quality effects.
- **Training effectiveness by role:** BCG's "five hours of training plus in-person coaching" is a qualitative statement in the article; the slideshow with the numbers was not read. No randomized or matched evaluation of training formats was found.
- **Certification:** no completion or pass-rate data for Big Four AI academies or badges found (a search snippet claimed a KPMG assessment-cheating case via a secondary blog; not verified, not used).
- **Not accessible or not read:** McKinsey State of AI (mirror returned nothing), the full Section report (gated), Harvey/RSGI power-user report (gated), the Australian Treasury evaluation (unreadable document), Kotter's *Leading Change* (paywalled, not used), ABA Formal Opinion 512 on competence and supervision (fetch failed), Microsoft champions guidance pages (not found), the full Dell'Acqua paper (summary only), the original FT and WSJ articles behind the PwC, Accenture and Ropes & Gray items.
- **Second-hand figures:** Accenture's 550,000 trained and promotion link come via Decrypt citing the FT; PwC's remarks via CPA Practice Advisor citing the FT. Treat as reported, not verified.
- **Adjacent evidence:** the call-centre (NBER), consulting experiment (HBS) and RAND results are adjacent processes; they cap any grade for enablement at B.
- **MIT NANDA 95%:** preliminary, anonymized, small sample; the report itself says barrier scores reflect reported frequency, not measurement. Do not present as a measured failure rate.
- **Measured vs reported:** few organizations publish tracked enablement metrics. The best-measured items are HMRC's randomized allocation with telemetry, Gallup's panel and the Danish administrative-data study; most firm figures are self-reported.
