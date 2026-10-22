# Curriculum by role and level (step 3)

Read this on entering step 3. It builds learning around the real work of each role and level: hands-on practice,
task framing, decomposition and checking, with separate tracks for reviewers, builders, leaders and juniors. Source
keys in brackets are listed in §8.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [Tiers and module design](#4-tiers-and-module-design)
5. [Juniors and the apprenticeship](#5-juniors-and-the-apprenticeship)
6. [Rules of thumb and traps](#6-rules-of-thumb-and-traps)
7. [Worked example and output](#7-worked-example-and-output)
8. [Sources](#8-sources)

## 1. Goal and exit criteria

**Goal.** Each role learns to do its own target workflows with AI, to check the output, and to know where AI is weak,
with practice on real (sanitized) work rather than a tool tour.

**Exit when all of these are true:**
- **Role map:** the roles and levels in scope, grouped where the work is alike.
- **Per role:** three tasks where AI helps and three where it does not, with examples from the user's own work.
- **Tiers** chosen (§4) and **modules** written on the module card.
- **Reviewer content:** what approvers must check in AI-assisted work.
- **Junior route:** how juniors still learn judgment (§5).
- **Access rule:** whether training is required before tool access, agreed with governance.
- **Refresh triggers:** what sends a module back for update (tool, model or policy change).
- **Order of delivery** by segment and dependency: low-confidence and blocked groups first where data rules allow.

## 2. How to run it

1. **Start from the segments and target workflows** of steps 1 and 2.
2. **Map roles** (C1) and ask for the helps / does-not-help lists (C2). AI helps inside its capability and not
   uniformly outside it, even within one workflow [HBS-JAGGED-2023]; teach both sides.
3. **Pick tiers** (§4) and draft one module per target workflow.
4. **Add the reviewer track** (C3), using the archetype's guardrails and any overlay policy.
5. **Design the junior route** (§5) with the user's talent lead.
6. **Agree the access rule** (C4). If no policy exists, hand off to ai-governance. No module about client data until
   the data rule exists.
7. **Order delivery** by segment and dependency, and write the curriculum.

## 3. Question bank

| # | Question | Notes |
|---|---|---|
| C1 | Which roles and levels are in scope, and where is the work alike enough to share a module? | Role map |
| C2 | For each role, what are three tasks where AI is most useful and three where it is not? Can you show one from your own files? | The jagged frontier, made local |
| C3 | What does a reviewer need to check in AI-assisted work, and have they been taught? | Reviewer track |
| C4 | Is training required before access, and does that differ by risk? | With governance |
| C5 | What does a first-year need to learn now that AI does tasks that used to teach the craft? | Junior route |
| C6 | Who needs to learn to build and maintain shared workflows, not only use them? | Builder track; links to step 4 |
| C7 | How much time per person, and in what format? Which groups have been trained only on policy? | Fits the credit rule from step 2 |

## 4. Tiers and module design

| Tier | Who | Content |
|---|---|---|
| Foundations | Everyone | Safe use and data rules from the overlay; a low-stakes first exercise; framing a task; checking output; where AI is weak |
| Role workflows | By role and level | The target workflows, practised on sanitized real work, with the role's checks |
| Builder | Champions, power users | Packaging a workflow for others, testing it on cases, writing the library entry (step 5) |
| Leader and manager | Partners, managers | Modelling use, setting expectations, reviewing AI-assisted work, talking about roles honestly |

**Module card** (one per module, in `program.md`): role; tier; tasks in scope; an example from the user's own work
(sanitized); practice exercise; verification step; risk rule; time required; hands-on check; follow-up (clinic or
champion).

**What to teach.** Task framing, decomposition and checking, not prompt tricks. Mollick argues prompt techniques
matter less as models infer intent better [MOLLICK-LAB-2025], while Section's hands-on tests found only 21% of US
knowledge workers wrote an effective prompt [SECTION-2026]. The evidence conflicts on prompt craft; framing and
checking are useful either way, and the hands-on check shows whether they were learned.

**Role-differentiated content.** An audit regulator's staff paper separates what preparers, reviewers and engagement
partners need: safe use; critical evaluation and bias awareness; governance and disclosure judgment. The UK audit
regulator says training should cover how to review and oversee a tool, automation bias (over-trusting machine output)
and the tool's known weaknesses (both in `assurance-quality-management-10`, grade B).

## 5. Juniors and the apprenticeship

Junior tasks often serve production and training at once. When AI takes them, design a replacement learning route
before the tasks go. Use the junior-task audit and explain-back technique in
`../../transformation-advisor/references/method/people-and-change.md` §6.

- **Supervised practice and verification:** reviewers question juniors on the reasoning behind AI-assisted results
  (`professional-services-talent-learning-09`, grade C).
- **A fixed rule on drafts:** Duane Morris holds that a first draft is never an appropriate final submission
  (`professional-services-talent-learning-02`, grade B).
- **Skill atrophy is a stated worry:** 43% of leaders in Wharton and GBK's survey warn of it without role design,
  coaching and practice time [WHARTON-GBK-2025].
- **Juniors may gain more:** in a call-centre study, gains were 34% for novices and minimal for experienced staff
  (adjacent process) [NBER-BRYNJOLFSSON-2023]. Do not assume juniors and seniors need the same module.

## 6. Rules of thumb and traps

- **Use role-specific cases, not generic or compliance-only content.** In Section's survey, 15% of those trained got
  only safety and compliance training (vendor-published) [SECTION-2026]; HMRC's evaluation lists the need for more
  practical, tailored training and time to learn [HMRC-2026].
- **Give a safe, low-stakes first phase.** Gowling WLG describes space for "silly poems and cats" before professional
  use [HARVEY-GOWLING-2025].
- **Target low-confidence groups early** (working rule: the UK trial found confidence correlated with time saved, which
  does not show coaching causes savings) [UKGDS-2025].
- **Keep formats short and varied:** one law firm named lunch-and-learns, short videos and one-page handouts among its
  most successful formats [LAW360-2025].
- **Gate access by training where risk warrants:** a CIPD case firm required training before use [CIPD-2026].
- **Assess with a hands-on task**, reported by group (step 1 §5), never as a personal score. Completion is reach, not
  skill.
- **Traps:** a tool tour; overweighting prompt tricks; one course for every level; training with no protected time;
  letting the junior pipeline erode.

## 7. Worked example and output

*Illustrative; the firm and figures are invented.* The accounting firm's tax practice. Helps: summarising a prior-year
file, first-draft research memos with cited sources, routine notice replies. Does not help (as tested): final
technical conclusions, calculations without a separate check. Modules: *Foundations* (90 minutes, all staff);
*Seniors: research summary* (verification step: open every cited source; hands-on check: find the planted wrong
citation); *Managers: reviewing AI-assisted work*; *Builder* (champions package the notice-reply procedure for step 5);
*Partners* (a private session on their own matters). Juniors explain a sample of AI-assisted answers back each month.

**Output:** `enablement/program.md` section 3 (role map, helps / does-not-help lists, tiers, module table, reviewer
track, junior route, access rule, refresh triggers, delivery order); module measures, if any, in `measures.yaml` as
`reach` or `depth`; frontmatter `step_completed: 3`, `next_step: 4`, `updated`.

## 8. Sources

- `CIPD-2026`: *How a law firm introduced an AI legal assistant*, CIPD with Institute for the Future of Work, 2026-03-25. https://www.cipd.org/ae/knowledge/case-studies/ai-legal-assistant/
- `HARVEY-GOWLING-2025`: *Al Hounsell on Driving Legal Transformation That Lasts*, Harvey blog, vendor-published, 2025-10-30. https://www.harvey.ai/blog/al-hounsell-on-driving-legal-transformation-that-lasts
- `HBS-JAGGED-2023`: *Navigating the Jagged Technological Frontier* (summary), Harvard D^3 Institute with BCG, 2023-09-21. https://d3.harvard.edu/navigating-the-jagged-technological-frontier/
- `HMRC-2026`: *Evaluating the impact of Microsoft Copilot in HMRC*, HM Revenue and Customs, 2026-07-09. https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot/evaluating-the-impact-of-microsoft-copilot-in-hmrc
- `LAW360-2025`: *How Law Firms Turn AI Skeptics Into 'Champions'*, Law360 Pulse, 2025-09-26. https://www.law360.com/pulse/articles/2392818
- `MOLLICK-LAB-2025`: *Making AI Work: Leadership, Lab, and Crowd*, One Useful Thing, 2025-05-22. https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- `NBER-BRYNJOLFSSON-2023`: *Generative AI at Work* (NBER WP 31161), Brynjolfsson, Li, Raymond, 2023. https://www.nber.org/system/files/working_papers/w31161/w31161.pdf
- `SECTION-2026`: *The AI Proficiency Report*, Section, June 2026. https://www.sectionai.com/ai/the-ai-proficiency-report
- `UKGDS-2025`: *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, UK Government Digital Service, June 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf
- `WHARTON-GBK-2025`: *Accountable Acceleration: Gen AI Fast-Tracks into the Enterprise*, Wharton Human-AI Research and GBK Collective, October 2025. https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf

Archetype use cases cited (grades as recorded): `professional-services-talent-learning-02`, `-09` in the
professional-services archetype; `assurance-quality-management-10` in the assurance archetype
(`../../transformation-advisor/references/archetypes/index.md`).
