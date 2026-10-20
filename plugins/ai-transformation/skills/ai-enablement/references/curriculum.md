# Curriculum by role and level (step 3)

Read this on entering step 3. It builds learning around the real work of each role and level: hands-on practice,
task framing, decomposition and checking, with separate tracks for reviewers, builders, leaders and juniors. Source
keys in brackets are listed in §11. Tags: **[T]** team, **[U]** unit, **[O]** organization.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [Tiers and module design](#4-tiers-and-module-design)
5. [Juniors and the apprenticeship](#5-juniors-and-the-apprenticeship)
6. [Expert moves](#6-expert-moves)
7. [Checklist and decision rules](#7-checklist-and-decision-rules)
8. [Common traps](#8-common-traps)
9. [Worked example](#9-worked-example)
10. [Output](#10-output)
11. [Sources](#11-sources)

## 1. Goal and exit criteria

**Goal.** Each role learns to do its own target workflows with AI, to check the output, and to know where AI is weak,
with practice on real (sanitized) work rather than a tool tour.

**Exit when all of these are true:**
- **Role map:** the roles and levels in scope, grouped where the work is alike.
- **Per role:** three tasks where AI helps and three where it does not, with examples from the user's own work.
- **Tiers** chosen (§4) and **modules** written, each with a real task, a practice exercise, a verification step, a
  risk rule, the time needed, a hands-on check and a follow-up.
- **Reviewer content:** what approvers must check in AI-assisted work.
- **Junior route:** how juniors still learn judgment (§5).
- **Access rule:** whether training is required before tool access, agreed with governance.
- **Refresh triggers:** what sends a module back for update (tool, model or policy change).
- **Order of delivery** by segment and dependency: low-confidence and blocked groups first where data rules allow.

## 2. How to run it

1. **Start from the segments and target workflows** of steps 1 and 2. The curriculum serves them.
2. **Map roles** (C1) and ask for the helps / does-not-help lists (C2). AI helps inside its capability and not
   uniformly outside it, even within one workflow [HBS-JAGGED-2023]; teach both sides.
3. **Pick tiers** (§4) and draft one module per target workflow, using the module card.
4. **Add the reviewer track** (C4). Check the archetype's guardrails and any overlay policy for what reviewers must do.
5. **Design the junior route** (§5) with the user's talent lead.
6. **Agree the access rule** with governance (C5). If no policy exists, hand off to the ai-governance skill.
7. **Order delivery** by segment and dependency, and write the curriculum.

## 3. Question bank

| # | Question | Scope | Notes |
|---|---|---|---|
| C1 | Which roles and levels are in scope, and where is the work alike enough to share a module? | [T][U] | Role map |
| C2 | For each role, what are three tasks where AI is most useful and three where it is not? Can you show an example from your own files? | [T][U] | The jagged frontier, made local |
| C3 | Who needs to learn to build and maintain shared workflows, not only use them? | [U] | Builder track; links to step 4 |
| C4 | What does a reviewer or approver need to check in AI-assisted work, and have they been taught? | [T][U] | Reviewer track |
| C5 | What is the minimum training before access, if any, and does it differ by risk? | [O] | With governance |
| C6 | What does a first-year need to learn now that AI does some of the tasks that used to teach the craft? | [U][O] | Junior route |
| C7 | How much time per person, and in what format: workshop, clinic, short video, practice on live work? | [T][U] | Fits the credit rule from step 2 |
| C8 | Which groups have been trained only on policy so far? | [U][O] | Fill the gap with practice |

## 4. Tiers and module design

**Tiers** (the advisor's working structure, built on the depth ladder):

| Tier | Who | Content |
|---|---|---|
| Foundations | Everyone | Safe use and data rules from the overlay; a low-stakes first phase; framing a task; checking output; where AI is weak |
| Role workflows | By role and level | The target workflows, practised on sanitized real work, with the role's checks |
| Builder | Champions, power users | Packaging a workflow for others, testing it on cases, writing the library entry (step 5) |
| Leader and manager | Partners, managers | Modelling use, setting expectations, reviewing AI-assisted work, talking about roles honestly |

**Module card** (one per module, written into `program.md`): role; tier; tasks in scope; an example from the user's own
work (sanitized); practice exercise; verification step; risk rule; time required; hands-on check; follow-up (clinic or
champion).

**What to teach.** Teach task framing, decomposition and checking, not prompt tricks. Gowling WLG teaches breaking
complex work into steps with explicit decision criteria [HARVEY-GOWLING-2025]. Mollick argues prompt techniques
matter less as models get better at inferring intent [MOLLICK-LAB-2025], while Section's hands-on tests found only 21%
wrote an effective prompt [SECTION-2026]. The evidence conflicts on prompt craft; framing and checking are useful
either way, and the hands-on check shows whether they were learned.

**Role-differentiated content.** An audit regulator's staff paper separates what preparers, reviewers and engagement
partners need: safe use; critical evaluation and bias awareness; governance and disclosure judgment. The UK audit
regulator says training should cover how to review and oversee a tool, automation bias (over-trusting machine output)
and the tool's known weaknesses (both in `assurance-quality-management-10`, grade B).

## 5. Juniors and the apprenticeship

Junior tasks often serve production and training at once. When AI takes them, design a replacement learning route
before the tasks go. The core skill's `../../transformation-advisor/references/method/people-and-change.md` §6 has the
junior-task audit and the explain-back technique; use it here.

- **Supervised practice and verification.** Teach and check verification and independent reasoning explicitly:
  reviewers question juniors on the reasoning behind AI-assisted results (`professional-services-talent-learning-09`,
  grade C).
- **A fixed rule on drafts.** Duane Morris holds one principle for new lawyers: a first draft is never an appropriate
  final submission, with practice-group champions showing the tools (`professional-services-talent-learning-02`,
  grade B).
- **Simulated practice.** Kennedys is building simulated drafting and review training (not yet reported as run)
  [KENNEDYS-SPELLBOOK-ND]; related practice environments are `professional-services-talent-learning-06` (grade C).
- **Skill atrophy is a stated worry.** 43% of leaders in Wharton's survey warn of skill atrophy without role design,
  coaching and practice time [WHARTON-GBK-2025].
- **Juniors may gain more.** In a call-centre study, gains were 34% for novices and minimal for experienced staff
  (adjacent process) [NBER-BRYNJOLFSSON-2023]. Do not assume juniors and seniors need the same module.

## 6. Expert moves

| Move | When | What it reveals |
|---|---|---|
| Ask which role-specific use cases the training uses; reject generic-only content | Curriculum audit | Compliance-only or tool-tour training. 15% of trained workers received only safety and compliance training and 17% were trained on agents or automations (vendor-published) [SECTION-2026]. Australia's trial evaluation recommends agency-specific use-case training [DTA-2024]; HMRC users and non-users asked for practical, tailored training and time to learn [HMRC-2026] |
| Give a safe, low-stakes first phase | Early stage | Comfort as the bottleneck before skill. Gowling describes space for "silly poems and cats" before professional use [HARVEY-GOWLING-2025]; KPMG's survey reports sandbox environments and "AI agent shadowing" in organizations' training (vendor-published) [KPMG-PULSE-2025] |
| Target low-confidence groups first | Ordering delivery | Where coaching pays [UKGDS-2025] |
| Teach decomposition explicitly | Module design | Why one-shot, overloaded prompts disappoint [HARVEY-GOWLING-2025] |
| Keep formats short and varied | Busy professionals | Law firms in a Law360 report used lunch-and-learns, short videos and one-page handouts [LAW360-2025] |
| Make training a condition of access where risk warrants | Rollout | Whether access is gated by capability. A CIPD case firm required training before use [CIPD-2026] (`professional-services-talent-learning-01`, grade B) |
| Check whether training spend is falling while expectations rise | Funding | Wharton reports training investment down 8 points and confidence in training as the main path to fluency down 14 points [WHARTON-GBK-2025] |

## 7. Checklist and decision rules

**Checklist:** role map; helps / does-not-help lists; safe sandbox; practice on real work; decomposition and
verification; reviewer checks; builder track; junior supervised practice; leader and manager track; access rule;
refresh triggers.

**Decision rules**
- Content must include practice on real workflows and building for reuse, not only safety and compliance
  [SECTION-2026].
- Target low-confidence groups first [UKGDS-2025].
- Treat prompt techniques as perishable; teach framing, decomposition and checking [MOLLICK-LAB-2025;
  HARVEY-GOWLING-2025].
- Assess with a hands-on task, reported by group (step 1 §5), never as a personal score.
- No module about client data until the data rule exists.

## 8. Common traps

| Trap | How to avoid it |
|---|---|
| Compliance-only or generic training [SECTION-2026] | One module per target workflow, on real work |
| Overweighting prompt tricks [MOLLICK-LAB-2025] | Framing, decomposition, checking |
| Training as a tool tour | Practice on people's own tasks, with protected time |
| The junior pipeline erodes [WHARTON-GBK-2025] | Supervised practice and explain-back (§5) |
| Training without time [UKGDS-2025] | Use the credit rule from step 2 |
| One course for every level [NBER-BRYNJOLFSSON-2023] | Tiers and role modules |

## 9. Worked example

*Illustrative; the firm and figures are invented.* The accounting firm's tax practice. Roles: preparers and seniors;
managers (reviewers); partners. Helps: summarising a client's prior-year file, first-draft research memos with cited
sources, drafting routine notice replies. Does not help (as tested): final technical conclusions, anything needing
the client's unreleased data in an unapproved tool, calculations without a separate check.

Modules: *Foundations* (90 minutes, all staff: data rule, a low-stakes first exercise, framing and checking).
*Seniors: research summary* (practice on three sanitized past questions; verification step: open every cited source;
hands-on check: find the planted wrong citation). *Managers: reviewing AI-assisted work* (what to sample, how to spot
confident errors, the "first draft is never final" rule). *Builder* (champions package the notice-reply procedure and
test it on cases, feeding step 5). *Partners* (a private session on their own matters, plus how to state
expectations). Juniors explain a sample of AI-assisted answers back to a manager each month. Training before access:
foundations only, agreed with governance.

## 10. Output

- **`enablement/program.md`**, section 3: role map, helps / does-not-help lists, tiers, module table, reviewer
  track, junior route, access rule, refresh triggers and delivery order.
- If modules need measures (completion is reach, not skill), add them to `measures.yaml` as `reach` or `depth`.
- Frontmatter: `step_completed: 3`, `next_step: 4`, `updated`.

## 11. Sources

- `CIPD-2026`: *How a law firm introduced an AI legal assistant*, CIPD with Institute for the Future of Work, 2026-03-25. https://www.cipd.org/ae/knowledge/case-studies/ai-legal-assistant/
- `DTA-2024`: *Copilot trial summary report: executive summary*, Digital Transformation Agency (Australia), 2024. https://www.digital.gov.au/initiatives/copilot-trial/summary-evaluation-findings/cts-executive-summary
- `HARVEY-GOWLING-2025`: *Al Hounsell on Driving Legal Transformation That Lasts*, Harvey blog, vendor-published, 2025-10-30. https://www.harvey.ai/blog/al-hounsell-on-driving-legal-transformation-that-lasts
- `HBS-JAGGED-2023`: *Navigating the Jagged Technological Frontier* (summary), Harvard D^3 Institute with BCG, 2023-09-21. https://d3.harvard.edu/navigating-the-jagged-technological-frontier/
- `HMRC-2026`: *Evaluating the impact of Microsoft Copilot in HMRC*, HM Revenue and Customs, 2026-07-09. https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot/evaluating-the-impact-of-microsoft-copilot-in-hmrc
- `KENNEDYS-SPELLBOOK-ND`: *Kennedys customer story*, Spellbook, vendor case page, undated. https://spellbook.com/stories/kennedys
- `KPMG-PULSE-2025`: *KPMG Q3 2025 AI Quarterly Pulse Survey*, KPMG US, 2025-09-18. https://kpmg.com/us/en/media/news/q3-ai-pulse.html
- `LAW360-2025`: *How Law Firms Turn AI Skeptics Into 'Champions'*, Law360 Pulse, 2025-09-26. https://www.law360.com/pulse/articles/2392818
- `MOLLICK-LAB-2025`: *Making AI Work: Leadership, Lab, and Crowd*, One Useful Thing, 2025-05-22. https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- `NBER-BRYNJOLFSSON-2023`: *Generative AI at Work* (NBER WP 31161), Brynjolfsson, Li, Raymond, 2023. https://www.nber.org/system/files/working_papers/w31161/w31161.pdf
- `SECTION-2026`: *The AI Proficiency Report*, Section, June 2026. https://www.sectionai.com/ai/the-ai-proficiency-report
- `UKGDS-2025`: *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, UK Government Digital Service, June 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf
- `WHARTON-GBK-2025`: *Accountable Acceleration: Gen AI Fast-Tracks into the Enterprise*, Wharton Human-AI Research and GBK Collective, October 2025. https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf

Archetype use cases cited (grades as recorded): `professional-services-talent-learning-01`, `-02`, `-06`, `-09` in
the professional-services archetype; `assurance-quality-management-10` in the assurance archetype
(`../../transformation-advisor/references/archetypes/index.md`).
