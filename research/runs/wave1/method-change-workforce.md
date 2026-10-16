# Method topic: change-workforce-fear

Stream M (method). Topic focus: the people side of AI transformation, covering fear of replacement, augmentation versus displacement evidence, role redesign, capacity redeployment versus cost reduction, reskilling, the junior-pipeline problem, change models (ADKAR, Kotter, Bridges) and how responsible leaders communicate workforce impact.
Phases fed: people-and-change, business-case, plan-and-control, onboarding.
Run date: 2026-10-16. Research was done through `curl`, `pdftotext` and a summarizing fetch tool. Each source in section 9 is marked `access: full` or `access: search-only`.

Conventions used in this file:

- Source refs follow `PUBLISHER-SHORT-YYYY`. A locator (page, section or figure) follows the ref wherever a claim is attributed.
- Provenance labels on figures: `independent` (academic, central bank, think tank, international body, measured by someone with no product to sell), `vendor-published` (published by a firm that sells AI, change-management or training products, or by an AI developer about its own usage data), `self-reported` (survey respondents or the publisher's own staff describing their own experience), `secondary` (press or other write-up of a primary source I could not open).
- Items tagged `(synthesis)` in the expert moves are my inference from the evidence cited, not a documented practitioner routine. The advisor should treat them as sensible practice, not as established method.
- Modal verbs from sources are kept ("expects", "plans", "predicts"). A prediction is not an observation.

---

## 1. Summary

- **Displacement evidence is thin in aggregate and concentrated at the entry level.** Several independent studies find no economy-wide job loss attributable to AI through 2026 (YALE-BUDGETLAB-2025; ANTHROPIC-LABOR-2026; STANFORD-CANARIES-2026 fact 1). The visible effect is on hiring of young workers into AI-exposed occupations. The updated Stanford/ADP paper reports employment of 22–25-year-olds in the most exposed occupations at 19% below where it would have been had it kept pace with less-exposed peers (descriptive, not causal). A Harvard résumé study finds junior employment at GenAI-adopting firms about 9% lower after six quarters relative to non-adopters, with senior employment on trend.
- **"Augmentation vs displacement" is decided at task level, and usage type matters.** In the Stanford/ADP data, declines sit where AI use substitutes for human tasks. Where use complements workers, employment is flat or rising. The advisor should therefore analyse tasks and the way they are delegated, not job titles.
- **Fear is widespread but mostly an information and trust problem that leaders can influence.** Surveys show a substantial minority of workers worried about their future (Anthropic Interviewer: 55% of the general-workforce sample expressed anxiety; WorkBank: 28% expressed concerns, of whom 23% named fear of replacement). Prosci reports leaders believe they communicate more than employees perceive. The same data show a larger problem in workplace norms: 69% of interviewed professionals mentioned social stigma around AI use.
- **Capacity release is a decision, not an outcome.** Measured time savings are often small (Danish study: 2.8% of work hours, self-reported, with no detectable effect on earnings or recorded hours). Where firms redeploy the time toward growth measures, reported ROI is higher in Wharton/GBK's 2026 survey (35% strongly positive vs 13% for efficiency-only measurement). Cutting on AI's potential rather than its performance is reported by HBR, Gartner and Oxford Economics as common and risky. Klarna's 2025 reversal is the best-known cautionary case.
- **The junior pipeline is the structural people problem for knowledge work.** Entry-level tasks are the training ground and the most exposed tasks at once. Evidence includes slowed hiring, GenAI-exposed tasks removed from junior job postings, mentorship loss reported inside Anthropic, and an RCT showing 17% lower mastery with AI assistance (with a usage-style effect). Redesigning apprenticeship deliberately is the response practitioners propose. Independent outcome evidence for any redesign is absent.
- **Change models are complementary, not competing.** ADKAR (Prosci) diagnoses where each individual or group is stuck. Kotter's eight steps address leadership direction and momentum. Bridges addresses the emotional transition (endings, neutral zone, new beginnings). Edmondson's psychological safety is the enabling condition for learning and reporting AI errors. Outcome evidence for these models applied to AI is vendor-published or absent.
- **Organizational conditions outweigh individual effort in what employees report.** Microsoft's 2026 survey associates 67% of reported AI impact with organizational factors (culture, manager support, talent practices) and 32% with individual factors. Prosci reports only 35% of organizations adequately prepare managers, and 38% of AI adoption challenges stem from insufficient training. Both are vendor-published.
- **Evidence that employees who lead AI change gain career value is correlational and weak.** The correlational sources are a self-reported survey, a wage-premium analysis of job ads, and a social-penalty study showing the penalty fades when managers use AI themselves. No study found tests champions or change leaders directly. The advisor can offer this as a reasonable bet, not a proven return.

---

## 2. Core concepts in plain language

**Task-level exposure is not job-level displacement.** Occupations are bundles of tasks. Exposure studies score tasks on whether AI could speed them up (Eloundou et al.: about 80% of US workers are in occupations with at least 10% of tasks exposed; about 19% have at least 50% exposed). Observed usage is far smaller than the theoretical ceiling: Anthropic's own measure puts coverage of Computer and Math tasks at 33% against a theoretical 94%. Exposure says where change is possible, not that a job disappears. Knowledge work has the highest exposure, so the advisor should expect questions about it, but should never present an exposure percentage as a headcount forecast.

**Automation vs augmentation is a property of how AI is used.** The same tool can be used to hand a task off (directive, automated end-to-end) or to work on it together (iterate, validate, learn). In the Stanford/ADP data, employment declines concentrate where usage is automation-type. In Anthropic's usage data the split moves around (automation briefly exceeded augmentation in Aug 2025; augmentation was back at 52% on Claude.ai in Nov 2025). Brynjolfsson's "Turing Trap" argument is that incentives lean toward automation rather than augmentation, although augmentation tends to create more value. For the advisor this is the link to the four reimagine lenses: "automate the flow" and "delegate the outcome" carry workforce consequences that "improve the step" usually does not. Say so explicitly when the user picks a lens.

**The entry-level asymmetry (codified vs tacit knowledge).** The Dallas Fed's reading of the evidence is that AI replicates codified, textbook knowledge, which is the expert part of an entry-level job and the routine part of an experienced worker's job. It complements tacit knowledge gained through experience. Whatever the final causal story, the observed pattern is that hiring into junior roles has slowed while experienced workers have not been hit. In knowledge work the junior tasks that AI absorbs (first drafts, research, data entry, first-pass review) are also how people learn. That is the apprenticeship problem.

**Capacity is released by AI, but it is spent by a decision.** Time saved only becomes value if someone decides where it goes: to a backlog, to new work, to quality, to slower hiring, or to headcount reduction. Evidence shows people spend part of it on new work (27% of Claude-assisted work at Anthropic would not have been done otherwise, self-reported by Anthropic staff). It also shows many firms measure only time saved. The advisor should make the decision explicit before the case is built, because it determines both the business case and how employees will read the project.

**Change is individual and organizational at once.** ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement) treats change as something each person goes through in sequence and lets you find the first element that is blocked. Kotter's eight steps cover the leadership side: urgency, coalition, vision, communication, removing barriers, short-term wins, consolidation, anchoring in culture. Bridges adds that every transition starts with an ending, so people need to name what they are losing before they can adopt something new. For AI in knowledge work this means respecting craft and professional identity, not only supplying training.

**Fear fills silence.** Prosci's evidence is that employees fill gaps in leadership communication with anxiety and that leaders overrate how much has landed. A second source of fear is social: using AI can carry a reputational cost (Duke experiments, search-only; Anthropic Interviewer: 69% mentioned stigma). So fear is partly about jobs and partly about being judged. Honest communication names what is known, what is not, and what leadership will commit to, and managers model use.

**AI attribution is a narrative as well as a fact.** Oxford Economics (via Fortune) suspects some firms dress up ordinary cuts as AI-driven. Gartner says most 2025 workforce reductions were driven by economic conditions, not automation alone, and predicts half of firms that attributed cuts to AI will rehire under different titles by 2027. For the advisor: check whether a proposed reduction is realized performance or expected potential, and check what the firm would say if AI were not the reason.

**Roles evolve through task mix, not announcements.** Role redesign means deciding which tasks leave, which stay, and which new ones appear (oversight, verification, data curation). Employees' stated preference is to keep tasks that define their professional identity and delegate routine work (Anthropic Interviewer). WorkBank finds workers want automation mainly to free time for high-value work, and that preferences for human involvement are high. Microsoft's 2026 survey lists quality control of AI output and critical thinking as the human skills AI users say grow in importance.

---

## 3. Expert moves

Format: **move**: when to use it; what it reveals; source ref (locator). `(synthesis)` marks an inference from the evidence.

1. **Break the role into a task bundle before anyone says "this job".** When: mapping, framing. Reveals: which tasks are exposed, which are not, and how much of the role the exposed tasks represent (time-weighted). Source: ANTHROPIC-LABOR-2026 (Measuring exposure); OPENAI-ELOUNDOU-2023 (Abstract).

2. **Rate each task on a human-involvement ladder, from "I do it" through "AI assists", "equal partnership" and "AI does, I verify", to "AI does end to end".** When: mapping, reimagining. Reveals: the real desired and feasible level of automation per task, and the red-light tasks where capability exceeds what people want. Source: STANFORD-WORKBANK-2026 (§1, contributions 2–3, Human Agency Scale).

3. **Ask people which tasks they would gladly hand off, and why, before showing them an automation list.** When: diagnosing, people-and-change. Reveals: that most workers want to automate low-value repetitive work to free time for high-value work (the top reason selected in 69.38% of responses), and where they do not (arts, design and media: only 17.1% of tasks received a positive automation-desire rating). Source: STANFORD-WORKBANK-2026 (Fig 4 text, §4 findings).

4. **Separate "AI could do this" from "AI is doing this here."** Ask for actual usage (logs, a short survey, shadow use) next to the capability claim. When: diagnosing, scoping the case. Reveals: the gap between theoretical and realized coverage, which is large in Anthropic's data (33% observed vs 94% theoretical for Computer and Math). Source: ANTHROPIC-LABOR-2026 (Measuring exposure, Fig 2).

5. **Ask for the measured time saved, not the felt time saved.** When: building the case, validating pilot claims. Reveals: self-report distortion. In the METR trial developers forecast a 24% reduction and afterwards still believed AI had cut time by 20%, while measured time rose 19%. In the Danish survey, reported savings averaged 2.8% of hours. Source: METR-2025 (Abstract); CHICAGO-HUMLUM-2025 (Intro p.2).

6. **Ask, for any proposed headcount number: "is this saving realized or expected?"** When: business case. Reveals: cuts based on AI's potential rather than demonstrated performance, which is the pattern HBR's 2026 piece reports. The Fortune/Oxford piece quotes Peter Cappelli saying many announcements say firms expect AI to cover the work and have not yet seen it. Source: HBR-DAVENPORT-2026 (summary); OXFORD-FORTUNE-2026 (Cappelli quote section).

7. **Make the capacity decision explicit before the pilot: where does saved time go?** Offer three pots (redeploy to backlog or growth, absorb through attrition and hiring pace, reduce) and set the rule in writing. When: framing, business case. Reveals: whether the case is growth or efficiency, which matters for ROI (Wharton 2026: 35% strongly positive ROI among leaders tracking at least one growth measure vs 13% among efficiency-only) and for how employees will read the project. Source: WHARTON-GBK-2026 (Key Takeaways, "Measure value beyond efficiency"). The framing as three pots is `(synthesis)`.

8. **Count new work, not just hours saved.** When: business case, benefits modelling. Reveals: expansion value. 27% of Claude-assisted work at Anthropic was work that would not otherwise have been done (self-reported, engineers). In Denmark, AI chatbots created new workloads for 17% of users, 10.9 percentage points through taking on new tasks. Source: ANTHROPIC-WORK-2025 (Key findings, survey data); CHICAGO-HUMLUM-2025 (Fig 5 text).

9. **Check whether the reduction is planned through attrition and hiring pace, and what that does to the pipeline.** When: plan, unit roll-up. Reveals: a hidden junior-pipeline cut. Klarna's headcount fell 22% in a year mostly through attrition under a hiring freeze, and the company later said the cost-cutting pursuit had gone too far in customer service. Source: KLARNA-ENTREPRENEUR-2025 (body); HARVARD-HOSSEINI-2026 (Abstract; hiring vs separations). The question itself is `(synthesis)`.

10. **Run a junior-task audit: for each task juniors do, label it production, training, or both.** When: role redesign, apprenticeship planning. Reveals: dual-purpose tasks where automation removes learning. Thomson Reuters Institute's author lists three purposes of junior lawyers: expand capacity, add review capacity, and build the talent pipeline. Hosseini and Lichtinger find GenAI-exposed tasks being removed from junior job postings within occupations. Source: TR-INSTITUTE-2026 (opening argument); HARVARD-HOSSEINI-2026 (Abstract). The labelling exercise is `(synthesis)`.

11. **Redesign junior work toward earlier judgment and verification, with supervision.** When: plan. Reveals: whether there is a path from the work AI absorbs to the work that builds expertise. The TR Institute column proposes juniors rotate through AI-enabled operational roles (AI compliance, legal data analysis, knowledge curation) as transitional steps. Treat it as a proposal, not an evaluated practice. Source: TR-INSTITUTE-2026 ("The AI-accelerated apprenticeship").

12. **Require juniors to explain AI output back before it is used.** When: onboarding AI into junior work, designing review. Reveals: whether people retain understanding. In Anthropic's RCT the AI-assisted group scored 17% lower on a mastery quiz, but participants who asked follow-up or conceptual questions kept more. Source: ANTHROPIC-SKILLS-2026 (Results). The explain-back routine is `(synthesis)`.

13. **Ask who is mentoring whom now.** When: diagnosing team health, people-and-change. Reveals: mentorship loss when AI becomes the first stop for questions. Anthropic's staff reported fewer junior questions to colleagues. Source: ANTHROPIC-WORK-2025 (Qualitative interviews: "workplace social dynamics").

14. **Ask people which tasks define how they see their professional identity, and which they would be glad to lose.** When: before reimagining, change planning. Reveals: tasks to protect or redesign gently. Bridges' point is that transition begins with naming endings. Anthropic Interviewer's general workforce wanted to keep identity-defining tasks and delegate routine ones. Source: ANTHROPIC-INTERVIEWER-2025 (Key findings); BRIDGES-TRANSITION-nd (Endings).

15. **Diagnose with ADKAR per role group: score Awareness, Desire, Knowledge, Ability, Reinforcement and find the first low element.** When: people-and-change, plan. Reveals: where adoption is stuck (for example, people know why but lack ability), so effort goes to the right lever. Source: PROSCI-ADKAR-2026 ("How it works", "Manage change intentionally"). Treat ADKAR scores as structured judgment, not a measured instrument.

16. **Map personas before the rollout and give each persona different support.** When: plan, onboarding. Reveals: that one training offer does not fit all groups. Prosci describes AT&T's Copilot rollout as built on persona mapping, over 200 live training sessions, embedded AI ambassadors and daily usage monitoring (vendor-published, self-reported). Source: PROSCI-ENTERPRISE-2026 (case summary).

17. **Test manager readiness with one question: "What will you say when a team member asks whether their job is safe?"** When: plan, onboarding. Reveals: the middle-layer gap. Prosci reports only 35% of organizations adequately prepare managers, and that manager behaviors track adoption outcomes (vendor-published). Source: PROSCI-ENTERPRISE-2026 (manager preparation). The question wording is `(synthesis)`.

18. **Check the send-receive gap: ask a sample of staff to restate what leadership said about AI and their roles.** When: after any announcement. Reveals: whether communication landed. Prosci says leaders report communicating more than employees observe. Wharton's 2026 survey finds a gap between managers and entry- and mid-level employees on organizational alignment (numbers not captured). Microsoft's 2026 survey: 26% of AI users say leadership is clearly and consistently aligned. Source: PROSCI-ENTERPRISE-2026 (Fear section); WHARTON-GBK-2026 (Organizational Alignment); MICROSOFT-WTI-2026 (leadership alignment).

19. **Draft the "what we know, what we don't, what we commit to" statement, and test it with a skeptic.** When: communication planning, before launch. Reveals: whether leaders are overpromising ("no one will lose a job") or leaving silence. Two public examples show different levels of candor: Amazon's CEO said in June 2025 the firm expects AI to reduce its total corporate workforce in the next few years while noting it is hard to know where it nets out. Anthropic's staff study states plainly that findings are uncertain and commits to follow-up. Source: AMAZON-JASSY-2025 (workforce paragraph); ANTHROPIC-WORK-2025 (Looking forward). The three-part template is `(synthesis)`.

20. **If reskilling has limits, say who gets a path and who does not, and on what criteria.** When: planning workforce impact. Reveals: honesty about the 11 of 100 problem. WEF employers expect 59 of 100 workers to need training by 2030: 29 upskilled in role, 19 upskilled and redeployed, 11 unlikely to receive it. Accenture's CEO said in Sept 2025 that upskilling is the first strategy and that people for whom reskilling is not viable are exited on a compressed timeline. Source: WEF-FOJ-2025 (Executive summary p.6); ACCENTURE-BI-2025 (call quotes). The advisor can use this to push users to define criteria and support up front. That step is `(synthesis)`.

21. **Look for stigma and hidden use.** Ask "Who uses AI and does not say so? Why?" When: diagnosing, onboarding. Reveals: stigma (69% of interviewed professionals mentioned it) and informal use that policy does not see. Duke experiments (search-only) found the penalty on AI-assisted workers shrinks when the evaluating manager uses AI. Source: ANTHROPIC-INTERVIEWER-2025 (general workforce findings); REIF-PNAS-2025 (search-only). The practical move, leaders using AI visibly, is `(synthesis)`.

22. **Add output quality to AI performance expectations, not only usage.** When: plan-and-control. Reveals: workslop risk. BetterUp/Stanford's survey found 40% of US desk workers had received workslop in the last month, taking about two hours each to resolve. Wharton's 2026 survey finds strongly-positive-ROI departments more often changed management structure and incorporated AI into performance reviews. Source: BETTERUP-WORKSLOP-2025 (stats panel); WHARTON-GBK-2026 (Key Takeaways, "Rebuild how work is managed").

23. **Name sponsors and ask what they do visibly, not what they approve.** When: onboarding, plan. Reveals: passive sponsorship. Prosci's 2026 research is reported to associate coalition-building and resourcing behaviours with better adoption outcomes. Source: PROSCI-ENTERPRISE-2026 (executive sponsorship paragraph).

24. **Ask how safe it is to say "the AI got this wrong" or "I don't know how to use this."** When: onboarding, team-level plan. Reveals: psychological safety, which Edmondson's field study of 51 manufacturing teams associates with team learning behavior. Source: EDMONDSON-1999 (Abstract). The AI-specific application is `(synthesis)`.

25. **Use short-term wins that people can see and tie to the change, and communicate them.** When: plan, first 6–18 months. Reveals: whether momentum is building. Kotter's step is described as needing wins that are visible, unambiguous and related to the change; the source for the 6–18 month window is secondary. Source: KOTTER-WIKI-2026 (Successful change); KOTTER-HBR-1995 (abstract only).

26. **Check the track record behind any exposure forecast you quote.** When: framing, answering "will my job go?" Reveals: forecast fragility. Anthropic's labor-market paper warns that a prominent offshorability forecast flagged about a quarter of US jobs as vulnerable, and most kept healthy growth a decade on. Source: ANTHROPIC-LABOR-2026 (Introduction).

27. **Before attributing a change to AI externally, ask what would be said if AI were not available as an explanation.** When: communication, business case. Reveals: AI-washing risk. Source: OXFORD-FORTUNE-2026 (investor-message section); GARTNER-ITNEWS-2026 (body). The question wording is `(synthesis)`.

28. **Ask what share of staff is trained, how many hours, and what kind of training (tool tour vs working on own tasks).** When: plan-and-control, onboarding. Reveals: the training gap. Prosci reports insufficient training is 38% of adoption challenges, the single largest reported barrier. BCG's 2025 survey (search-only) reports 36% of employees feel adequately trained, and more regular use among those with five or more hours. Source: PROSCI-ENTERPRISE-2026 (training paragraph); BCG-ATWORK-2025 (search-only).

---

## 4. Question bank

Scope tags: `[team]`, `[unit]`, `[org]`. Stage tags use the advisor's loop (Onboard, Frame, Map, Diagnose, Reimagine, Prioritize, Make the case, Plan) and, at higher levels, the roll-up.

### Onboarding

- What is the worst thing people on your team think this project will mean for them, and how do you know? `[team]` Onboard
- Has leadership said anything about jobs and AI so far? What did people hear? `[team][unit]` Onboard
- Who already uses AI at work, openly or quietly? `[team][unit]` Onboard
- What are you allowed and not allowed to do with AI today? Does the team know? `[team][unit][org]` Onboard
- Which of your own tasks would you be glad to give up, and which define how you see your professional role? `[team]` Onboard, Map
- How comfortable is it on your team to say "the AI got this wrong" or "I have no idea how to use this"? `[team]` Onboard, Diagnose
- Who is the change owner and who is the visible sponsor? What does the sponsor do that others can see? `[unit][org]` Onboard, Plan
- What has this team been through in change recently? Is there fatigue? `[team][unit]` Onboard, Diagnose

### People-and-change

- For each role group, which ADKAR element is weakest: why change, wanting it, knowing how, being able to, or sticking with it? `[team][unit]` Diagnose, Plan
- What does each role group stand to lose (tasks, status, learning, income, control)? What do they stand to gain? `[team][unit]` Diagnose, Reimagine
- Which tasks would people automate first if it were up to them? Which would they refuse to automate, and why? `[team]` Map, Reimagine
- Are managers equipped to answer "is my job safe?" honestly? What have they been told? `[unit][org]` Diagnose, Plan
- Do people fear being judged for using AI, or for not using it? Who sets the norm? `[team][unit]` Diagnose
- Where does AI-generated work reach colleagues unreviewed? What does it cost them? `[team][unit]` Diagnose, Plan
- Who mentors juniors today, and how often do juniors still ask people rather than the tool? `[team][unit]` Diagnose
- Which roles will change shape (task mix) and which could shrink? Who has a credible path elsewhere in the firm and who does not? `[unit][org]` Reimagine, Plan
- What do you want people to be able to do in 12 months that they cannot do now? How will they get there (hours, support, protected time)? `[team][unit]` Plan

### Business-case

- If the project saves time, where does the saved time go? Backlog, new work, quality, slower hiring, or fewer people? Who decides? `[team][unit][org]` Frame, Make the case
- Is any headcount saving in the case already realized, or is it expected? What evidence would show it? `[unit][org]` Make the case
- What did you measure before the pilot, and is time saved the only metric? Which growth or quality metrics could you add? `[team][unit]` Prioritize, Make the case
- What work is not done today that would be done with the freed capacity? Is there demand for it? `[team][unit]` Reimagine, Make the case
- If the case includes reduced hiring, what is the effect on your junior pipeline in three to five years? `[unit][org]` Make the case, Plan
- What are the people costs in the case (training hours, manager time, change support, parallel running, rework)? `[team][unit]` Make the case
- What would you say publicly or internally about the reason for this change if AI were not part of the explanation? `[unit][org]` Make the case
- What happens to the case if quality or customer experience drops and you need to bring people back? `[unit][org]` Make the case, Plan

### Plan-and-control

- Which tasks require a human to verify AI output, and who is trained to do it? `[team][unit]` Plan
- How will juniors learn the judgment that the absorbed tasks used to teach? What replaces the apprenticeship work? `[team][unit][org]` Plan
- What leading indicators will tell you the people side is working (use quality not just volume, adoption by group, stigma, manager confidence, attrition of top performers)? `[team][unit]` Plan
- When will you review the workforce assumptions in the plan, and what findings would change them? `[unit][org]` Plan
- What are the commitments to staff (training, redeployment support, notice) and who owns them? `[unit][org]` Plan
- How will performance reviews treat AI-assisted work (credit, expectations, review burden)? `[team][unit]` Plan
- Where do the units' plans collide on shared people resources (training capacity, change support, the same managers)? `[org]` Plan, roll-up
- Which units are creating the hiring slowdowns that, added together, hollow out the pipeline? `[org]` roll-up
- What is the consistent workforce message across units, and where would a unit's plan contradict it? `[org]` roll-up

---

## 5. Common traps

1. **Quoting exposure as a forecast.** Why it happens: exposure percentages are headline-friendly. Evidence: exposure measures say what AI could speed up, not what will be adopted. Observed coverage is a fraction of theoretical, Yale finds no relation between exposure measures and employment or unemployment changes, and Eloundou et al. state they make no predictions about adoption timelines. Avoid by pairing exposure with observed usage and local evidence. Source: ANTHROPIC-LABOR-2026; YALE-BUDGETLAB-2025 (Key Takeaways); OPENAI-ELOUNDOU-2023 (Abstract).

2. **Cutting on potential rather than performance.** Why: investor and board pressure, plus AI as a convenient narrative. Evidence: HBR's January 2026 article, based on a December 2025 survey of 1,006 executives, reports cuts made in anticipation of what AI might do. Gartner says only about a fifth of customer service leaders had reduced agent staffing due to AI, and predicts half of firms that attributed reductions to AI will rehire for similar functions under different titles by 2027 (a prediction). Klarna's CEO said in May 2025 that cost-driven AI service was lower quality. Avoid by tying reductions to measured results and phasing them. Source: HBR-DAVENPORT-2026; GARTNER-ITNEWS-2026; KLARNA-ENTREPRENEUR-2025.

3. **AI-washing the story.** Why: AI attribution reads better than over-hiring or weak demand. Evidence: Oxford Economics (via Fortune) says it suspects some firms dress up layoffs as good news. Challenger data cited there show AI named in about 55,000 US job cuts in the first 11 months of 2025, 4.5% of total reported job losses. Avoid by checking real drivers before external messaging. Employees notice, and credibility on workforce statements is hard to recover (synthesis). Source: OXFORD-FORTUNE-2026.

4. **Leaving silence.** Why: leaders do not know the answer, so say nothing. Evidence: Prosci says employees fill silence with anxiety and that leaders report communicating more than staff observe. Avoid by saying what is known, unknown and committed, and repeating it through managers. Source: PROSCI-ENTERPRISE-2026 (Fear section).

5. **Promising more than can be kept.** Why: reassurance seems kind. Evidence: none directly; Amazon's memo is an example of the opposite choice, stating the direction (a smaller corporate workforce) while admitting uncertainty about the net. Avoid by not promising "no job losses" unless a commitment is real and funded (synthesis). Source: AMAZON-JASSY-2025.

6. **Hollowing the junior pipeline by accident.** Why: each unit trims entry-level hiring because the exposed tasks are cheap to automate. Evidence: reduced hiring (not separations) drives the junior employment gap in both Stanford/ADP and Harvard/résumé studies; Dallas Fed attributes under-25 declines to weak hiring; CIPD's autumn 2025 survey of 2,000+ UK employers finds 62% of those expecting AI to shrink headcount name clerical, junior managerial, professional or administrative roles as most at risk. Avoid with a roll-up check of pipeline effects and a deliberate apprenticeship plan. Source: STANFORD-CANARIES-2026; HARVARD-HOSSEINI-2026; DALLASFED-2026; CIPD-WI-2025.

7. **Automating the learning.** Why: cognitive offloading is attractive. Evidence: Anthropic's RCT (52 mostly junior engineers) found 17% lower quiz scores with AI assistance, though use style mattered. Anthropic staff worry about skills atrophy. Wharton's 2025 survey: 43% of leaders see risk of declining skill proficiency. Avoid with explain-back routines and structured stretch work. Source: ANTHROPIC-SKILLS-2026; ANTHROPIC-WORK-2025; WHARTON-GBK-2025.

8. **Measuring only time saved.** Why: easy to measure. Evidence: Wharton 2026 notes the most common investment metric is time saved, yet growth-metric departments report much higher strong ROI. Humlum finds minimal earnings or hours effects despite employer investment, with 2.8% reported time savings. Avoid by pre-committing where time goes and measuring outcomes. Source: WHARTON-GBK-2026; CHICAGO-HUMLUM-2025.

9. **Passive sponsorship and unready managers.** Why: AI is treated as an IT rollout. Evidence: Prosci (vendor-published) reports 35% of organizations adequately prepare managers and that passive sponsorship is a common failure mode. Microsoft 2026: only 26% of AI users say leadership is clearly aligned. Avoid by naming visible sponsor actions and preparing managers first. Source: PROSCI-ENTERPRISE-2026; MICROSOFT-WTI-2026.

10. **Training as a tool tour.** Why: easy to scale. Evidence: Prosci reports insufficient training as the single largest reported barrier (38% of adoption challenges), and that in 2026 the challenge shifted toward verification, governance and team coordination. Avoid with task-specific, practice-based training. Source: PROSCI-ENTERPRISE-2026.

11. **Workslop.** Why: AI makes polished output cheap, and pressure to show usage rewards volume. Evidence: BetterUp/Stanford survey of 1,150 US desk workers (Sept 2025): 40% had received workslop in the prior month. Avoid by setting quality expectations and review ownership. Source: BETTERUP-WORKSLOP-2025.

12. **Mistaking usage for value.** Why: usage is visible. Evidence: Wharton 2026: 80% report positive return but only 28% strongly positive; the NY Fed 2026 notes usage within adopting firms is concentrated in a small share of workers (median 17% of workers in service firms). Avoid by asking about depth of workflow change. Source: WHARTON-GBK-2026; NYFED-2026.

13. **Overclaiming that change leaders gain.** Why: attractive message for engagement. Evidence: sources are correlational (self-reported promotion rates after training, wage-premium comparisons of job ads), so causality is untested. Avoid by presenting it as plausible, not proven, and by not making it a promise to staff. Source: CLUTCH-BW-2025 (search-only); PWC-BAROMETER-2025 (search-only).

14. **Treating ADKAR or Kotter as the evidence.** Why: tidy frameworks. Evidence: outcome claims for these methods come mainly from the vendors that sell them (for example Prosci's long-running claim that excellent change management makes meeting objectives seven times more likely). Search results flagged that the widely repeated "70% of change programs fail" statistic could not be traced to a single origin. Do not cite it. Use the models as diagnostic structure. Source: PROSCI-ENTERPRISE-2026; PROSCI-WP-nd.

15. **Trusting self-assessed productivity.** Why: people believe they are faster. Evidence: METR RCT, 16 experienced developers on 246 tasks: measured time rose 19% while developers believed it fell. Limit: small, specific setting, early-2025 tools. Avoid by measuring a baseline and sampling outputs. Source: METR-2025.

---

## 6. Evidence

Every row gives the figure, what it measures (numerator and denominator in the source's terms where available), provenance, and source with locator.

### 6a. Labor-market and task-exposure evidence

| # | Data point | What it measures | Provenance | Source (locator) |
|---|---|---|---|---|
| E1 | 19% | Employment of workers aged 22–25 in AI-exposed occupations versus where it would be had it kept pace with less-exposed peers, ADP payroll data through June 2026. Authors call it descriptive, not causal. | independent (academic; uses ADP data) | STANFORD-CANARIES-2026 (Abstract, Introduction) |
| E2 | About 11% fall vs about 10% rise | Employment of 22–25-year-olds from Nov 2022 to Jun 2026: two most exposed quintiles fell about 11%; three least-exposed quintiles grew about 10%. | independent | STANFORD-CANARIES-2026 (Introduction p.3) |
| E3 | 13% (Jul 2025 data), 16% (Sep 2025 data), 15% to 19% | Earlier versions' regression-adjusted relative decline, and the "kept-pace shortfall" as of the Jul 2025 vintage versus Jun 2026. Shows the estimate moves with vintage and method. | independent | STANFORD-CANARIES-2026 (Introduction p.3) |
| E4 | Facts 1 and 5 | No evidence of widespread economy-wide displacement; declines concentrate where AI use substitutes, while complementary use is flat or rising, especially for experienced workers. | independent | STANFORD-CANARIES-2026 (Abstract) |
| E5 | About 9% after six quarters | Junior employment at GenAI-adopting firms relative to non-adopters; senior employment trend largely unchanged. Based on 65M workers at 280,000+ firms; adoption inferred from "GenAI integrator" job postings; adopters are 3.7% of 281,000 firms and about 16% of employment. | independent (academic working paper) | HARVARD-HOSSEINI-2026 (Abstract; Introduction) |
| E6 | No systematic unemployment increase; about 14% drop in job-finding rate for ages 22–25 | Anthropic's study of CPS unemployment in exposed vs unexposed occupations since late 2022 found no systematic rise. The job-finding rate for young workers entering exposed occupations was about 14% lower than in 2022, but the paper calls this barely statistically significant and lists alternative explanations. | vendor-published (AI developer's analysis, uses public CPS and its own usage data) | ANTHROPIC-LABOR-2026 (Initial results) |
| E7 | 0.6 percentage points per 10 | Decrease in BLS 2024–34 projected employment growth for every 10 percentage point increase in observed coverage (a weak relationship, per the authors). | vendor-published | ANTHROPIC-LABOR-2026 (How exposure tracks with projected job growth) |
| E8 | 33% vs 94% | Claude's observed coverage of Computer and Math tasks vs the theoretical LLM feasibility (β) in that category. | vendor-published | ANTHROPIC-LABOR-2026 (Measuring exposure, Fig 2 text) |
| E9 | About 80% and about 19% | Share of US workers in occupations where at least 10% (and at least 50%) of tasks could be affected by LLMs, by the authors' rubric; no adoption timeline asserted. | independent/vendor mixed (OpenAI and university authors) | OPENAI-ELOUNDOU-2023 (Abstract) |
| E10 | 1 in 4; 3.3% | Workers in an occupation with some GenAI exposure; employment in the highest exposure category (4.7% of female vs 2.4% of male employment). ILO concludes transformation of jobs is the most likely impact. | independent (international body) | ILO-2025 (abstract page) |
| E11 | 2.2% vs 11.7% | Wage value of current visible AI adoption in tech (Surface Index) vs wage value of skills AI systems could technically perform across administrative, financial and professional services (Iceberg Index, about $1.2 trillion). A simulation-based exposure measure, not an employment forecast. | independent (MIT/ORNL authors) | MIT-ICEBERG-2025 (Abstract) |
| E12 | About 1 percentage point; no discernible disruption | Occupational mix change since ChatGPT (33 months) was about 1 percentage point above the Internet-era path, and began before generative AI. Exposure, automation and augmentation measures showed no relation to changes in employment or unemployment. | independent (think tank) | YALE-BUDGETLAB-2025 (Key Takeaways; Figures 1–2 text) |
| E13 | +2.5%; −1%; −5% | US total employment since fall 2022; most AI-exposed 10% of sectors; computer systems design. | independent (central bank research note) | DALLASFED-2026 (Employment section) |
| E14 | 7.5%; 8.5%; 16.7% | Nominal weekly wage growth since fall 2022: nationwide, top 10% AI-exposed industries, computer systems design. Occupation-level exposure shows no relationship with wage growth (trend nearly flat), per the note. | independent | DALLASFED-2026 (Wages section) |
| E15 | Median 40% | Median experience premium (experienced vs entry wages) across 205 occupations in BLS modelled wage data; premium correlates positively with exposure. Used to support a codified-vs-tacit reading. | independent (single-author note) | DALLASFED-2026 (Deriving the returns) |
| E16 | Within 1%; 2.8%; 17% | Danish study, 11 exposed occupations, about 25,000 workers, 7,000 workplaces: confidence intervals rule out earnings and recorded-hours effects larger than 1%; average reported time savings 2.8% of work hours; new workloads created for 17% of users. | independent (surveys 2023–24 linked to administrative data) | CHICAGO-HUMLUM-2025 (Abstract; Intro p.2; Fig 5 text) |
| E17 | 10%–40% | Benefits (time savings, quality, creativity, task expansion, job satisfaction) are 10%–40% greater when employers encourage use. | independent | CHICAGO-HUMLUM-2025 (Intro p.2) |
| E18 | 14% and 34% | Issues resolved per hour with an AI assistant among 5,179 customer-support agents at one firm: 14% average, 34% for novice and low-skilled workers, minimal for experienced workers. | independent (academic; company data) | NBER-BRYNJOLFSSON-2023 (Abstract) |

### 6b. Organization-level and workforce-decision evidence

| # | Data point | What it measures | Provenance | Source (locator) |
|---|---|---|---|---|
| E20 | 61% (2026), 40% (2025), 25% (2024) | Share of NY–Northern NJ service firms reporting they used AI in business processes in the prior six months. Manufacturers 51%, 26%, 16%. Regional survey only. | independent (central bank survey) | NYFED-2026 (AI adoption section) |
| E21 | 4%; about 15%; about 13% | Service firms reporting, over six months: layoffs due to AI (4%, up from 1%); hiring fewer workers than otherwise (about 15%); hiring more due to AI (about 13%). The post's chart axes read "share of AI users"; the text states shares of "service firms". | independent | NYFED-2026 (Retraining Remains Common, Layoffs Limited) |
| E22 | Just over a third; median 17% | Service-firm AI users retraining workers in response to AI; median share of workers using AI at service-firm adopters. | independent | NYFED-2026 |
| E23 | 17%; 62%; 26% | CIPD autumn 2025 Labour Market Outlook (2,000+ UK employers): expect AI to shrink workforce in next year; of those, share naming clerical, junior managerial, professional or administrative roles as most at risk; share of those expecting to lose more than 10% of workforce. | independent (professional body survey), secondary report | CIPD-WI-2025 (opening paragraphs) |
| E24 | About 55,000; 4.5%; 245,000 | Challenger, Gray & Christmas, as cited by Oxford Economics: US job cuts citing AI in first 11 months of 2025; their share of total reported job losses; cuts citing market and economic conditions. | independent (outplacement firm data; analyst briefing), secondary | OXFORD-FORTUNE-2026 ("Data behind the hype") |
| E25 | A fifth; prediction of 50% by 2027 | Share of customer service leaders who actually reduced agent staffing due to AI (Gartner survey, details as reported by iTnews). Separately, Gartner predicts half of companies that attributed headcount reduction to AI will rehire for similar work under different titles by 2027. The second is a forecast. | vendor-published (analyst firm), secondary | GARTNER-ITNEWS-2026 (body) |
| E26 | 1,006 executives | HBR/Return on AI Institute survey of global executives, December 2025, on AI-linked headcount decisions. Only the summary and framing were accessible. | vendor-published (author's institute), search-only for findings | HBR-DAVENPORT-2026 (summary) |
| E27 | 170M, 92M, net 78M; 39%; 85%; 40%; 50% | WEF Future of Jobs 2025 (employer survey): jobs created and displaced by 2030 as a share of 1.2bn formal jobs in the dataset (22% churn, net +7%); share of workers' skills transformed or outdated by 2030; employers prioritizing upskilling; planning to reduce staff as skills become less relevant; planning to transition staff to growing roles. | independent (survey of employers' expectations) | WEF-FOJ-2025 (Executive summary p.5–6) |
| E28 | 59 / 29 / 19 / 11 per 100 | Of 100 workers, employers foresee 59 needing training by 2030: 29 upskilled in role, 19 upskilled and redeployed, 11 unlikely to receive it. | independent | WEF-FOJ-2025 (p.6) |
| E29 | 47% / 22% / 30%, then near-even | Employer-estimated share of work tasks done mainly by humans alone, mainly by technology, and by both today, and the employers' expectation of a near-even three-way split by 2030. | independent | WEF-FOJ-2025 (Fig 2.7 and text) |
| E30 | 80%; 28%; 35% vs 13%; 67% vs 19% | Wharton/GBK 2026 (enterprise leaders; departments): positive ROI; strongly positive ROI; strongly positive ROI among departments tracking growth outcomes vs efficiency only; strongly positive ROI among departments meeting all three "transformational success" components vs not. Sample size not captured. | independent academic partner with commercial research firm (GBK) | WHARTON-GBK-2026 (Wave 4; Key Takeaways) |
| E31 | 64% vs 47% | Share of departments with strongly positive ROI that changed management structure because of AI, vs those without strong ROI, "while reporting no more staff reductions or hiring freezes than anyone else". | same | WHARTON-GBK-2026 (Key Takeaways) |
| E32 | 62% daily; excited −8pp; skeptical +9pp; cautious +7pp | Daily use and shift in sentiment from the prior year. | same | WHARTON-GBK-2026 (Wave 4) |
| E33 | 89%; 43% | Wharton/GBK 2025: agree AI enhances employees' skills; see risk of declines in skill proficiency. | same | WHARTON-GBK-2025 (Wave 3) |
| E34 | 67% vs 32%; 19%; 26%; 65% | Microsoft 2026 (20,000 AI-using knowledge workers, 10 markets): share of reported AI impact associated with organizational vs individual factors (statistical association, not causal); share of AI users in the "Frontier" zone; share saying leadership is clearly and consistently aligned; share fearing falling behind if they do not adapt. | vendor-published (Microsoft, via Edelman survey), summarizing fetch | MICROSOFT-WTI-2026 (key stats) |
| E35 | 31,000 workers; 53% / 80%; 33% / 32% | Microsoft 2025: knowledge workers surveyed in 31 markets; leaders saying productivity must increase vs workers saying they lack time or energy; leaders considering headcount reductions vs considering increases. Also reports 43% of workers globally fear AI will take their jobs. | vendor-published, summarizing fetch (figures not re-checked against the report) | MICROSOFT-WTI-2025 (summary) |
| E36 | $615M; about $865M; 779,000 vs 791,000 | Accenture: Q4 FY25 severance-type charge; expected total with the next quarter's charge; headcount at end of August 2025 vs about three months earlier. Also over 550,000 trained in GenAI fundamentals. | company statements on an earnings call, secondary report | ACCENTURE-BI-2025 (body) |
| E37 | 22% to 3,500 | Klarna headcount change over a hiring freeze that the article says lasted over 12 months, mostly through attrition; the company later said AI customer service was lower quality and began recruiting human agents again. | company statements, secondary | KLARNA-ENTREPRENEUR-2025 (body) |

### 6c. Change-management and adoption evidence

| # | Data point | What it measures | Provenance | Source (locator) |
|---|---|---|---|---|
| E38 | 29% | Prosci pages state both "29% of participants say fear and lack of understanding of AI are a top concern" (white paper page) and "29% of employees worry about job displacement or role ambiguity" (blog). The wording differs; treat as one figure with ambiguous definition. | vendor-published, self-selected samples | PROSCI-WP-nd; PROSCI-ENTERPRISE-2026 (Fear section) |
| E39 | 56%–64% | Prosci: share of reported AI implementation challenges that were human factors rather than technical. | vendor-published | PROSCI-ENTERPRISE-2026 (challenges section) |
| E40 | 37%; 35%; 38% | Prosci: organizations investing significantly in change management during AI implementation; organizations adequately preparing managers; share of adoption challenges stemming from insufficient training. | vendor-published | PROSCI-ENTERPRISE-2026 |
| E41 | 43% | Prosci white paper page: respondents indicating more than half of the resistance they experienced from managers could have been avoided. A search-result summary of the same white paper quoted 47% for employee resistance and 51% for manager resistance; I could not reconcile them. | vendor-published | PROSCI-WP-nd |
| E42 | 18,000+ users in six weeks; 96.4% | AT&T Microsoft 365 Copilot rollout built on ADKAR: active users reached in six weeks; sustained adoption rate among assigned users; licenses expanded from 20,000 to 60,000. | vendor-published (Prosci), self-reported | PROSCI-ENTERPRISE-2026 (case summary) |
| E44 | 40%; 2 hours; $186 | BetterUp Labs/Stanford Social Media Lab, online survey of 1,150 full-time US desk workers, Sept 2025: share who received workslop in the last month; average time to resolve each incident; monthly cost per employee. The firm-level $9M annual figure is the publisher's extrapolation for 10,000 people. | vendor-published (with academic partner) | BETTERUP-WORKSLOP-2025 (stats panel) |
| E45 | 55%; 41%; 69%; 86%; 65% | Anthropic Interviewer, general workforce sample (N=1,000): anxious about AI's impact on their future; felt secure and believe human skills irreplaceable; mentioned social stigma of using AI at work; said AI saves them time; satisfied with AI's role. AI-conducted interviews; self-selected sample. | vendor-published, self-reported | ANTHROPIC-INTERVIEWER-2025 (general workforce) |
| E46 | 65% vs 35% against 47% vs 49% | Professionals' self-description of AI use (augmentative vs automative) vs Anthropic's observed Claude conversations. The authors list possible reasons for the difference. | vendor-published | ANTHROPIC-INTERVIEWER-2025 (Augmentation vs automation) |
| E47 | 46.1%; 69.38%; 28.0%; 45.0% / 23.0% / 16.3% | WorkBank (1,500 workers, 844 tasks, 104 occupations): tasks where workers have positive automation attitudes; share of responses citing "free up time for high-value work"; workers who voiced fears or negative sentiment; among them lack of trust in accuracy, fear of replacement, and missing human qualities. | independent (Stanford) | STANFORD-WORKBANK-2026 (§1; Appendix F.1 text) |
| E48 | 45.2% | Occupations whose dominant worker-desired level is H3 (equal partnership) on the Human Agency Scale; workers generally prefer higher human agency than experts see as needed. | independent | STANFORD-WORKBANK-2026 (§1) |
| E49 | 132 surveyed, 53 interviewed; 60% / 50% / 27% / 0–20% | Anthropic internal study (Aug 2025): self-reported share of work using Claude, productivity boost, share of Claude-assisted work that would not otherwise have been done, and the range of work staff say they can fully delegate. Engineers and researchers at an AI developer: not generalizable, as the authors say. | vendor-published, self-reported | ANTHROPIC-WORK-2025 (Key findings) |
| E50 | 17% lower | Quiz score of AI-assisted group vs hand-coding group, RCT with 52 mostly junior software engineers learning a new Python library; speed difference not statistically significant. | vendor-published (AI developer's RCT) | ANTHROPIC-SKILLS-2026 (Results) |
| E51 | +19% time; forecast 24%; belief 20% | METR RCT, 16 experienced open-source developers, 246 tasks, early-2025 tools: completion time when AI was allowed vs disallowed; their forecast of reduction; their post-hoc estimate of reduction. | independent (non-profit evaluator) | METR-2025 (Abstract) |
| E52 | Teams without AI +0.24 SD over individuals; teams with AI +0.39 SD; individuals with AI matched teams without AI | P&G field experiment, 776 professionals on real product-development tasks. Sample size was 791 in the later journal version. | independent (academic; P&G funded part of the institute's work, disclosed) | NBER-DELLACQUA-2025 (Abstract); MOLLICK-2025 (results paragraphs) |
| E53 | 27% to 39%; 77% vs about 50%; 52% | Anthropic Economic Index: directive (fully delegated) share of Claude.ai conversations from late 2024 to Aug 2025; automation share in first-party API traffic vs Claude.ai; augmented share of Claude.ai conversations in Nov 2025 (up 5pp). | vendor-published usage data | ANTHROPIC-EI-2025 (Key findings); ANTHROPIC-EI-2026 (Augmentation is again dominant) |
| E54 | 51 teams | Edmondson 1999: field study in a manufacturing company; team psychological safety associated with learning behavior, and learning behavior mediates between safety and team performance. | independent (peer-reviewed, pre-AI) | EDMONDSON-1999 (Abstract) |

### 6d. Search-only figures (not to be used in A or B entries without verification)

- McKinsey, *Superagency in the workplace* (Jan 2025): survey of 3,613 employees and 238 C-level executives in six countries. C-suite leaders estimated that 4% of employees use gen AI for at least 30% of daily work, while 13% report doing so. 92% of companies plan to increase AI investment over three years. Source: MCKINSEY-SUPERAGENCY-2025 (search-only, via search result summary).
- McKinsey State of AI (2025 and 2026 editions): a 2026 chart is described as reporting that 32% of 2025 respondents expected AI-driven headcount reductions while 14% reported reductions a year later. Source: MCKINSEY-SOTA-2026 (search-only).
- BCG, *AI at Work 2025* (26 Jun 2025): about 10,600 workers in 11 countries; frontline regular use about 51%; about 41% of respondents worry their roles could disappear within a decade; 36% feel adequately trained; more regular use among those with five or more hours of training. Source: BCG-ATWORK-2025 (search-only).
- PwC, *2025 Global AI Jobs Barometer* (Jun 2025): average 56% wage premium for jobs requiring AI skills versus similar roles that do not (up from 25%); productivity growth of 27% (2018–2024) in the most AI-exposed industries vs 9% in the least exposed. The headline "fourfold" compares different windows. Source: PWC-BAROMETER-2025 (search-only).
- Duke (Reif, Larrick, Soll), PNAS 2025: four preregistered experiments with 4,439 participants; AI-assisted workers were rated lazier and less competent; the penalty shrank when managers used AI themselves. Source: REIF-PNAS-2025 (search-only; the PMC page fetch failed).
- Clutch (Oct 2025, 428 US employees): 89% of those who completed AI training reported a raise or promotion in the past year vs 53% of those who did not. Self-reported correlation. Source: CLUTCH-BW-2025 (search-only).
- UK Big Four graduate intake: KPMG 1,399 (2023) to 942, Deloitte 1,700 to 1,400, EY 1,800 to 1,600, PwC 1,600 to 1,500, as reported by the press. Source: BIGFOUR-PRESS-2025 (search-only, secondary).
- General Assembly survey (Mar 2026, 258 leaders): 71% of law-firm leaders expect junior roles to evolve. Publisher sells AI training. Source: GA-LAW-2026 (search-only).
- Challenger, Gray & Christmas: a secondary report puts AI-cited US job cuts at 101,743, or 23% of layoffs, through 1 Jul 2026. Source: CHALLENGER-YAHOO-2026 (search-only, secondary).

---

## 7. Worked examples

### Example 1: Two public workforce statements, two levels of candor (large employers)

- **Amazon, 17 June 2025.** The CEO's message to employees said that as generative AI and agents roll out, the company will need fewer people in some jobs and more in others, that it is hard to know where this nets out, and that in the next few years it expects AI to reduce its total corporate workforce. It asked employees to be curious, take training and experiment. What the message did: named the direction, admitted uncertainty on the net effect, gave an action for employees. What it did not do: give numbers, timing or any redeployment commitments (AMAZON-JASSY-2025, workforce paragraphs).
- **Accenture, 25 Sep 2025 earnings call.** The CEO said upskilling is the first strategy, and that the firm is exiting, on a compressed timeline, people for whom reskilling is not a viable path for the skills it needs. Alongside, it reported about $615M of severance-related charges in the quarter (about $865M expected in total) and said headcount is expected to rise across markets in the next fiscal year (ACCENTURE-BI-2025).
- **Lesson for the advisor.** Both statements put the trade-off in the open. Whether employees saw them as honest is not measured in any source I found. The reusable pattern is the one in move 19 and move 20: state the direction, say what is unknown, state the criteria and the commitments, and make sure managers can answer follow-ups. The pattern of publicly signalling cuts is not endorsed here. These are examples of explicitness, not best practice.

### Example 2: Cost-first customer service, then a reversal (Klarna) and the analyst warning

- **What happened.** Klarna paused hiring for over a year (per the article), saw headcount fall 22% to 3,500 largely through attrition, and in February 2024 said AI was doing the work of 700 customer service agents and had taken 75% of chats. In May 2025 its CEO told Bloomberg the cost-cutting had gone too far, that chatbots were cheaper but lower quality, and that Klarna was recruiting human agents so customers could always reach a person (KLARNA-ENTREPRENEUR-2025).
- **Context.** Gartner's 2026 customer service guidance advises resisting headline pressure and making strategic reductions over time, guided by data. It predicts half of companies that attributed cuts to AI will rehire for similar work under different titles by 2027 (a forecast, GARTNER-ITNEWS-2026).
- **What the advisor takes from it.** In service functions, test quality and customer effect before banking headcount savings. Make the capacity decision (move 7) explicit. Include a rollback assumption in the plan. The case does not show that AI cannot reduce service costs, only that one firm judged its first attempt had cost quality.

### Example 3: Redesigning the junior apprenticeship in a law firm (proposal plus reported practice)

- **Problem.** Junior lawyers' work served capacity, review, and pipeline-building purposes. If drafting and research become cheap, juniors lose the tasks that taught judgment (TR-INSTITUTE-2026).
- **Proposed redesign (a proposal, not an evaluated program).** Rotate first- and second-year lawyers through AI-enabled operational roles such as AI compliance (policy, audit trail, vendor claims), legal data analysis (turning matter history into usable structure), and knowledge curation, with the aim of giving them judgment calls earlier. The author also says firms must redesign training programs, adjust compensation structures and develop new metrics for junior performance, and warns of a messy transition in which juniors double-check outputs without being taught how (TR-INSTITUTE-2026).
- **Reported practice (search-only).** One legal-careers summary says that at one large firm juniors previously doing first-level review now QA and contextualize AI-produced results. I could not verify it against a firm source (VAULT-LAW-2026, search-only).
- **Advisor use.** Apply the junior-task audit (move 10) to any professional-services unit. Pair it with the explain-back routine (move 12) and a roll-up check that the unit's hiring pace does not hollow the pyramid (question bank, roll-up).

### Example 4: ADKAR-based Copilot rollout at AT&T (vendor case)

- **What is reported.** Prosci describes AT&T scaling Microsoft 365 Copilot to more than 18,000 active users in six weeks, with a 96.4% sustained adoption rate among assigned users, using persona mapping, more than 200 live training sessions, AI ambassadors in each business unit and daily usage monitoring. Leadership then expanded from 20,000 to 60,000 licenses (PROSCI-ENTERPRISE-2026).
- **How to read it.** This is vendor-published and self-reported. "Sustained adoption among assigned users" is a usage metric with a selected denominator. It tells nothing about value, quality or job effects. It is useful as a description of the change mechanics (personas, training, ambassadors, monitoring). It is not independent evidence that ADKAR causes adoption.
- **Advisor use.** Borrow the mechanics for onboarding and plan-and-control. Ask the user to add a value or quality measure and a people-side measure (confidence, stigma) so adoption does not stand in for outcome.

---

## 8. Mapping to phases

**people-and-change**
- Reframe "will AI take my job?" as a task-level question, using the exposure caveats in sections 2 and 5 so the advisor neither dismisses nor inflates fear.
- Diagnose with ADKAR per role group, Bridges for endings and neutral zone, Kotter for leadership direction and visible wins, Edmondson for safety. Use as structure, not proof.
- Surface stigma, hidden use and identity-defining tasks (moves 14 and 21).
- Role evolution: task mix shifts toward verification, oversight and interpersonal skills (WORKBANK; WTI 2026), and employees prefer high human agency.
- Junior and apprenticeship design: junior-task audit, explain-back, earlier supervised judgment (moves 10–13).
- Responsible communication: known, unknown, committed; managers prepared; check send-receive gap (moves 17–20).
- Employee-led change: offer champions and ambassadors as a reasonable mechanism (AT&T, vendor-published) and be honest that evidence of career gain is correlational.

**business-case**
- Make the capacity decision explicit (move 7) and include new-work value, not just hours (move 8).
- Treat headcount in the case as realized or expected, and apply the AI-washing check (moves 6 and 27).
- Include people costs: training, manager time, change support, rework from poor output.
- Use ranges and measured baselines, not perceived time savings (move 5). Cite cautionary cases (Klarna, Gartner) as risk assumptions, not as proof against automation.
- Pipeline cost: a hiring slowdown has a deferred cost that the case should name.

**plan-and-control**
- Plan manager readiness, sponsor behaviours, persona-based training, and verification roles.
- Control through leading indicators on both sides: quality of AI-assisted output, adoption depth by group, stigma, manager confidence, junior learning (mastery, mentoring), plus the workforce assumptions in the case.
- Schedule reviews of workforce assumptions and communication commitments.
- At unit and organization level: roll up pipeline effects, shared training and change capacity, and consistency of workforce messaging across units.

**onboarding**
- Ask early about fears, past change fatigue, current AI use (open and hidden), policy clarity, and who is sponsor.
- Establish a safe-to-say-what-went-wrong norm and set honest expectations about what the advisor process will and will not decide about jobs.
- Capture what leaders have already said about AI and jobs, as that context shapes everything the user plans.
- Use light-touch ADKAR questions per audience to pick where to start.

---

## 9. Sources

Access key: `full` = the document or page text was read in this run. `full (summarizing fetch)` = read through a summarizing fetch tool, not raw text; figures should be checked before reuse. `search-only` = only search results or snippets were seen; the primary was blocked or unreachable.

| Ref | Title | Publisher / author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ANTHROPIC-LABOR-2026 | Labor market impacts of AI: A new measure and early evidence | Anthropic (Massenkoff, McCrory) | vendor research | https://www.anthropic.com/research/labor-market-impacts | 5 Mar 2026 | full |
| STANFORD-CANARIES-2026 | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence (updated version) | Brynjolfsson, Chandar, Chen, Stanford Digital Economy Lab | academic working paper | https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf | Aug 2026 (updates Aug 2025 paper) | full |
| OPENAI-ELOUNDOU-2023 | GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models | Eloundou, Manning, Mishkin, Rock | working paper | https://arxiv.org/pdf/2303.10130 | v5 21 Aug 2023 | full |
| CHICAGO-HUMLUM-2025 | Large Language Models, Small Labor Market Effects (BFI WP 2025-56) | Humlum, Vestergaard, Univ. of Chicago BFI | academic working paper | https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf | 9 May 2025 | full |
| YALE-BUDGETLAB-2025 | Evaluating the Impact of AI on the Labor Market: Current State of Affairs | Gimbel, Kinder, Kendall, Lee, Yale Budget Lab | think-tank analysis | https://budgetlab.yale.edu/research/evaluating-impact-ai-labor-market-current-state-affairs | 2025 (33 months after ChatGPT; day not captured) | full |
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work (NBER WP 31161) | Brynjolfsson, Li, Raymond | academic working paper | https://www.nber.org/system/files/working_papers/w31161/w31161.pdf | Apr 2023, rev. Nov 2023 | full |
| HARVARD-HOSSEINI-2026 | Generative AI as Seniority-Biased Technological Change: Evidence from U.S. Résumé and Job Posting Data | Hosseini, Lichtinger, Harvard | academic working paper | https://raw.githack.com/s-mahdihosseini/Website/b99fa2962dcc4c165bbc3c41dd283afa99c5ccfb/GenAI_SenBTC_May_2026.pdf | 6 May 2026 (first version 31 Aug 2025) | full |
| DALLASFED-2026 | AI is simultaneously aiding and replacing workers, wage data suggest | Scott Davis, Federal Reserve Bank of Dallas | central bank research note | https://www.dallasfed.org/research/economics/2026/0224 | 24 Feb 2026 | full |
| NYFED-2025 | Are Businesses Scaling Back Hiring Due to AI? | Abel, Deitz, Emanuel, Hyman, Montalbano, NY Fed Liberty Street Economics | central bank survey analysis | https://libertystreeteconomics.newyorkfed.org/2025/09/are-businesses-scaling-back-hiring-due-to-ai/ | 4 Sep 2025 | full |
| NYFED-2026 | Businesses Are Using AI to Transform Work, Not Cut Jobs | Abel, Deitz, Emanuel, Montalbano, NY Fed | central bank survey analysis | https://libertystreeteconomics.newyorkfed.org/2026/09/businesses-are-using-ai-to-transform-work-not-cut-jobs/ | 1 Sep 2026 | full |
| NYFED-ATHREYA-2026 | AI's Impact on Labor and Hiring (Street Level) | Kartik Athreya, NY Fed | central bank commentary | https://libertystreeteconomics.newyorkfed.org/2026/08/ais-impact-on-labor-and-hiring/ | 5 Aug 2026 | full |
| ILO-2025 | Generative AI and Jobs: A Refined Global Index of Occupational Exposure (WP 140) | International Labour Organization | international body working paper | https://www.ilo.org/publications/generative-ai-and-jobs-refined-global-index-occupational-exposure | 20 May 2025 | full (abstract page) |
| MIT-ICEBERG-2025 | The Iceberg Index: Measuring Skills-centered Exposure in the AI Economy | Chopra et al., MIT / Oak Ridge National Lab | academic preprint | https://arxiv.org/pdf/2510.25137 | v2 26 Nov 2025 | full |
| ANTHROPIC-EI-2025 | Anthropic Economic Index report: Uneven geographic and enterprise AI adoption | Anthropic | vendor usage data report | https://www.anthropic.com/research/anthropic-economic-index-september-2025-report | 15 Sep 2025 | full |
| ANTHROPIC-EI-2026 | Anthropic Economic Index report: Economic primitives | Anthropic | vendor usage data report | https://www.anthropic.com/research/anthropic-economic-index-january-2026-report | 15 Jan 2026 | full |
| STANFORD-WORKBANK-2026 | Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce | Shao, Zope et al., Stanford | academic preprint | https://arxiv.org/pdf/2506.06576 | v3 1 Feb 2026 | full |
| NBER-DELLACQUA-2025 | The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise (NBER WP 33641) | Dell'Acqua et al. | academic working paper | https://www.nber.org/system/files/working_papers/w33641/w33641.pdf | Apr 2025 | full |
| MOLLICK-2025 | The Cybernetic Teammate | Ethan Mollick, One Useful Thing | practitioner article | https://www.oneusefulthing.org/p/the-cybernetic-teammate | 2025 (day not captured) | full |
| METR-2025 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | Becker, Rush, Barnes, Rein, METR | independent RCT preprint | https://arxiv.org/pdf/2507.09089 | v2 25 Jul 2025 | full |
| ANTHROPIC-SKILLS-2026 | How AI assistance impacts the formation of coding skills | Anthropic | vendor RCT write-up | https://www.anthropic.com/research/AI-assistance-coding-skills | 29 Jan 2026 | full |
| ANTHROPIC-WORK-2025 | How AI is transforming work at Anthropic | Anthropic | company self-study (survey, interviews, usage data) | https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic | 2 Dec 2025 | full |
| ANTHROPIC-INTERVIEWER-2025 | Introducing Anthropic Interviewer: What 1,250 professionals told us about working with AI | Anthropic | vendor research | https://www.anthropic.com/research/anthropic-interviewer | 4 Dec 2025 | full |
| ANTHROPIC-POLICY-2025 | Preparing for AI's economic impact: exploring policy responses | Anthropic | policy discussion | https://www.anthropic.com/research/economic-policy-responses | 14 Oct 2025 | full (read for context; not cited for figures) |
| BRYNJOLFSSON-TURING-2022 | The Turing Trap: The Promise and Peril of Human-Like Artificial Intelligence | Erik Brynjolfsson, Daedalus | academic essay | https://arxiv.org/pdf/2201.04200 | Jan 2022 (arXiv) | full (abstract and introduction) |
| WEF-FOJ-2025 | The Future of Jobs Report 2025 | World Economic Forum | international survey report | https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf | Jan 2025 | full |
| WHARTON-GBK-2025 | 2025 AI Adoption Report: Accountable Acceleration | Wharton Human-AI Research and GBK Collective | academic/commercial survey (landing page) | https://knowledge.wharton.upenn.edu/special-report/2025-ai-adoption-report/ | 28 Oct 2025 | full (landing page; full report not read) |
| WHARTON-GBK-2026 | 2026 AI Adoption Report: The Adaptive Advantage | Wharton Human-AI Research and GBK Collective | academic/commercial survey (landing page) | https://knowledge.wharton.upenn.edu/special-report/2026-ai-adoption-report/ | 13 Oct 2026 | full (landing page; full report not read; alignment percentages did not render) |
| MICROSOFT-WTI-2025 | 2025: The year the Frontier Firm is born | Microsoft WorkLab (Edelman Data x Intelligence survey) | vendor survey report | https://www.microsoft.com/en-us/worklab/work-trend-index/2025-the-year-the-frontier-firm-is-born | 23 Apr 2025 | full (summarizing fetch) |
| MICROSOFT-WTI-2026 | 2026 Work Trend Index Annual Report: Agents, human agency, and the opportunity for every organization | Microsoft WorkLab | vendor survey report | https://microsoft.com/en-us/worklab/work-trend-index/agents-human-agency-and-the-opportunity-for-every-organization | 5 May 2026 | full (summarizing fetch) |
| PROSCI-ADKAR-2026 | The Prosci ADKAR Model | Prosci | vendor framework page | https://www.prosci.com/methodology/adkar | undated; accessed Oct 2026 | full |
| PROSCI-ENTERPRISE-2026 | Enterprise AI adoption best practices | Prosci | vendor blog with research claims | https://www.prosci.com/blog/enterprise-ai-adoption-best-practices | updated 6 Oct 2026 | full |
| PROSCI-WP-nd | Win With AI by Leading the Human Side (white paper landing page) | Prosci | vendor white paper page | https://empower.prosci.com/ai-adoption-white-paper | undated | full (landing page only) |
| PROSCI-EARLY-nd | AI in Change Management: Early Findings | Prosci | vendor blog | https://www.prosci.com/blog/ai-in-change-management-early-findings | updated 5 Oct 2026 (study date not captured) | full (read for context; about change practitioners' own AI use) |
| KOTTER-HBR-1995 | Leading Change: Why Transformation Efforts Fail | John P. Kotter, Harvard Business Review | practitioner article | https://hbr.org/1995/05/leading-change-why-transformation-efforts-fail-2 | Mar–Apr 1995 | search-only (abstract page; paywalled body) |
| KOTTER-WIKI-2026 | John Kotter (change model summary) | Wikipedia, citing Kotter's *Leading Change* (1996) | secondary reference | https://en.wikipedia.org/wiki/John_Kotter | accessed Oct 2026 | full (secondary) |
| BRIDGES-TRANSITION-nd | What is the Bridges Transition Model? | William Bridges Associates | framework page | https://wmbridges.com/about/what-is-transition/ | undated | full |
| EDMONDSON-1999 | Psychological Safety and Learning Behavior in Work Teams | Amy Edmondson, Administrative Science Quarterly | peer-reviewed paper | https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Group_Performance/Edmondson%20Psychological%20safety.pdf | 1999 | full |
| HBR-DAVENPORT-2026 | Companies Are Laying Off Workers Because of AI's Potential, Not Its Performance | Davenport, Srinivasan, Harvard Business Review | practitioner article | https://hbr.org/2026/01/companies-are-laying-off-workers-because-of-ais-potential-not-its-performance | 29 Jan 2026 (updated 3 Feb 2026) | search-only (summary and intro only; findings paywalled) |
| OXFORD-FORTUNE-2026 | AI layoffs are looking more and more like corporate fiction (reporting on an Oxford Economics briefing of 7 Jan 2026) | Fortune (Nick Lichtenberg) | press coverage | https://fortune.com/2026/01/07/ai-layoffs-convenient-corporate-fiction-true-false-oxford-economics-productivity/ | 7 Jan 2026 | full (secondary; Oxford Economics original not read) |
| GARTNER-ITNEWS-2026 | Half of firms that cut customer service staff due to AI will rehire by 2027 | iTnews Asia reporting on Gartner | press coverage of analyst research | https://www.itnews.asia/news/half-of-firms-that-cut-customer-service-staff-due-to-ai-will-rehire-by-2027-623867 | 25 Feb 2026 (Gartner release 3 Feb 2026) | full (secondary; Gartner primary blocked) |
| CIPD-WI-2025 | Employers increasingly see AI as a way of reducing headcount (on CIPD Labour Market Outlook) | Workplace Insight reporting on CIPD | press coverage of professional-body survey | https://workplaceinsight.net/employers-increasingly-see-ai-as-a-way-of-reducing-headcount/ | 10 Nov 2025 | full (secondary) |
| AMAZON-JASSY-2025 | Message from CEO Andy Jassy: Some thoughts on Generative AI | Amazon | company statement | https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-on-generative-ai | 17 Jun 2025 | full |
| ACCENTURE-BI-2025 | Accenture is cutting staff it can't retrain in the age of AI, but it still plans to hire more people | Business Insider via Yahoo Finance, reporting on Accenture's earnings call | press coverage | https://finance.yahoo.com/news/accenture-cutting-staff-cant-retrain-063900475.html | 25 Sep 2025 | full (secondary) |
| KLARNA-ENTREPRENEUR-2025 | Klarna CEO Reverses Course By Hiring More Humans, Not AI | Entrepreneur, reporting on a Bloomberg interview | press coverage | https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 | May 2025 | full (secondary) |
| TR-INSTITUTE-2026 | The AI Law Professor: When AI forces us to rethink how we train junior lawyers | Tom Martin, Thomson Reuters Institute | practitioner column | https://thomsonreuters.com/en-us/posts/legal/ai-law-professor-train-junior-lawyers | 2 Feb 2026 (date from the page's article card) | full |
| BETTERUP-WORKSLOP-2025 | Workslop: The Hidden Cost of AI-Generated Busywork | BetterUp Labs and Stanford Social Media Lab | vendor research page | https://www.betterup.com/workslop | survey Sept 2025 | full (landing page) |
| OCM-TRENDS-2025 | 2025-2026 Organizational Change Management Trends Report | OCM Solution | vendor trend report | https://www.ocmsolution.com/wp-content/uploads/2025/08/2025-2026-Organizational-Change-Management-OCM-Trends-Report.pdf | Aug 2025 | full (read; low-provenance aggregation, not cited for figures) |
| MCKINSEY-SUPERAGENCY-2025 | Superagency in the workplace: Empowering people to unlock AI's full potential at work | McKinsey & Company | consultancy report | https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work | Jan 2025 | search-only |
| MCKINSEY-SOTA-2026 | The state of AI (2025 edition; 2026 chart "AI job losses fall short of forecasts") | McKinsey & Company | consultancy survey | https://www.mckinsey.com/featured-insights/charts/ai-job-losses-fall-short-of-forecasts | 2025 and Aug 2026 | search-only |
| BCG-ATWORK-2025 | AI at Work 2025: Momentum Builds, but Gaps Remain | Boston Consulting Group | consultancy survey | https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain | 26 Jun 2025 | search-only |
| PWC-BAROMETER-2025 | 2025 Global AI Jobs Barometer | PwC | consultancy analysis | https://pwc.com/gx/en/news-room/press-releases/2025/ai-linked-to-a-fourfold-increase-in-productivity-growth.html | Jun 2025 | search-only |
| REIF-PNAS-2025 | Evidence of a social evaluation penalty for using AI | Reif, Larrick, Soll, PNAS (DOI 10.1073/pnas.2426766122) | academic | https://pmc.ncbi.nlm.nih.gov/articles/PMC12088386/ | 2025 | search-only (fetch failed) |
| CLUTCH-BW-2025 | Clutch report: workers who embrace AI more likely to get promoted | Clutch via Business Wire | vendor survey press release | https://www.businesswire.com/news/home/20251028781175/en/Clutch-Report-Workers-Who-Embrace-AI-Are-More-Likely-to-Get-Promoted-and-Find-Better-Work-Life-Balance | 28 Oct 2025 | search-only |
| DELLACQUA-JAGGED-2023 | Navigating the Jagged Technological Frontier (HBS Working Paper 24-013) | Dell'Acqua et al. | academic working paper | https://papers.ssrn.com/abstract=4573321 | 2023 | search-only (blocked; no figures used) |
| AUTOR-THOMPSON-2025 | Expertise (Journal of the European Economic Association 23(4)) | Autor, Thompson | academic | https://econpapers.repec.org/RePEc:oup:jeurec:v:23:y:2025:i:4:p:1203-1271. | 2025 | search-only (described through Dallas Fed note and search summaries) |
| BURNINGGLASS-2025 | No Country for Young Grads | Burning Glass Institute | research report | not retrieved (reported by eWeek and others) | 2025 | search-only |
| BIGFOUR-PRESS-2025 | Big Four cut graduate hiring (UK) | Accountancy Today, Telegraph, Guardian and others | press coverage | https://www.accountancytoday.co.uk/2025/06/24/big-four-firms-cut-grad-jobs-in-favour-of-ai/ | Jun 2025 | search-only |
| GA-LAW-2026 | General Assembly survey of leaders on junior roles (reported by Law360 and others) | General Assembly | vendor survey, press | https://www.law360.com/articles/2456965/ai-set-to-transform-junior-lawyer-roles-survey-finds | Mar 2026 | search-only |
| VAULT-LAW-2026 | How AI-Powered Legal Assistants are Transforming Entry-Level Legal Work | Vault | careers publication | https://legacy.vault.com/blogs/vaults-law-blog-legal-careers-and-industry-news/how-ai-powered-legal-assistants-are-transforming-entry-level-legal-work | undated | search-only |
| CHALLENGER-YAHOO-2026 | Layoffs accelerate in May 2026 as firms restructure around AI (and related Challenger coverage) | Yahoo Finance | press | https://finance.yahoo.com/sectors/technology/articles/layoffs-accelerate-may-2026-firms-040430218.html | 2026 | search-only |
| ABA-512-2024 | ABA Formal Opinion 512 on generative AI | American Bar Association | professional-body guidance | https://www.americanbar.org/content/dam/aba/administrative/professional_responsibility/ethics-opinions/aba-formal-opinion-512.pdf | 29 Jul 2024 | search-only (blocked; supervisory-duty summary only, no figures) |

Distinct sources read in full or full-via-summary: 45. Search-only: 16. Total listed: 61.

---

## 10. Gaps

- **Blocked primaries.** McKinsey (Superagency, State of AI), BCG, PwC, Gartner's own release, the HBR article body, Kotter's own site, the Dell'Acqua et al. jagged-frontier paper (SSRN and HBS both refused), the ABA opinion and the Duke PNAS paper (fetch failed) could not be read. Figures from them appear only in section 6d and should be verified before use.
- **Microsoft figures** came through a summarizing fetch tool. The 2025 report's "43% of workers fear AI will take their jobs" and the 2026 percentages should be checked against the reports.
- **Wharton/GBK 2026** was read at landing-page level. The sample size, the leader vs employee alignment percentages (rendered as placeholders) and the full "human capital" findings were not read.
- **Prosci's 2026 State of AI Adoption** is behind a membership wall. Prosci pages gave different values for related figures (29% described two ways; 43% on the page vs 47%/51% in a search summary of the same white paper). The widely repeated "70% of change programs fail" statistic could not be traced to a primary source, and I did not use it.
- **No independent outcome evidence** for ADKAR, Kotter or Bridges applied to AI adoption. Outcome claims come from the vendors that sell them. The Kotter step list was not read in full in this run; the Wikipedia secondary source and the HBR abstract were all that were accessible, so the eight step names are not directly sourced here.
- **Employee-led change and career gain.** No rigorous study found on employees who lead AI adoption. Available evidence is a self-reported survey (Clutch), wage premia from job ads (PwC, search-only) and a social-penalty study (Duke, search-only). A reputable HBR piece on this was not located.
- **Responsible communication.** Evidence on which messages reduce fear or improve adoption is thin. The sources show examples (Amazon, Accenture, Anthropic) and consultancy/vendor assertions, but no trial of messaging approaches and no measure of how employees received those statements. Union and works-council consultation practice (for example the Partnership on AI shared-prosperity guidelines, whose PDF link failed) is not covered.
- **Professional-body guidance** is thin. CIPD appears only through press coverage of its survey. ABA 512 is search-only. No ICAEW, ACCA or AICPA guidance on AI and trainee pipelines was found.
- **Junior pipeline.** The strongest evidence is US-centered descriptive labor data. No outcome evaluation of an apprenticeship redesign exists in the sources. Burning Glass and Big Four graduate-cut data are search-only and press-derived. The Canaries and Hosseini studies caution against reading their patterns as causal.
- **Seniority and leadership roles.** Almost no evidence on how AI changes the roles of partners, directors and middle managers beyond manager-readiness survey data from vendors.
- **Scope of data.** Many figures are US or Denmark-specific, or from one firm (customer support agents, P&G, Anthropic employees). The NY Fed data cover one region. Surveys of practitioners and employees are self-selected and often sponsored by firms selling AI, training or change services.
- **Practitioner talks, podcasts and books.** Not covered beyond one practitioner article (Mollick). Books (Kotter, Hiatt, Bridges, Mollick's *Co-Intelligence*) were summarized only from framework pages and secondary references, not from the books.
- **Version drift.** The Stanford/ADP paper's headline figure has changed across versions (13%, 16%, 19%) and the Harvard study has multiple versions. The advisor should cite the vintage and treat them as descriptive.
