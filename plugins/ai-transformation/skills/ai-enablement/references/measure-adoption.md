# Measure sustained adoption and impact (step 7)

Read this on entering step 7, and whenever someone quotes an adoption or time-saved figure. It measures depth of use,
embedded workflows and outcomes, labels what is measured and what is estimated, and discounts self-reports honestly.
Source keys in brackets are listed in §11. Tags: **[T]** team, **[U]** unit, **[O]** organization.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [The measurement layers](#4-the-measurement-layers)
5. [Time saved: measured, estimated and discounted](#5-time-saved-measured-estimated-and-discounted)
6. [Expert moves](#6-expert-moves)
7. [Checklist and decision rules](#7-checklist-and-decision-rules)
8. [Common traps](#8-common-traps)
9. [Worked example](#9-worked-example)
10. [Output](#10-output)
11. [Sources](#11-sources)

## 1. Goal and exit criteria

**Goal.** An honest picture of whether use is sustained and deepening, which workflows have become the default way of
working, and what that has done to outcomes the firm cares about.

**Exit when all of these are true:**
- **Readings** for each measure in `measures.yaml`, by segment, with the window and the denominator (non-users
  included).
- **Depth and embedded counts:** how many people have a repeatable workflow, how many build for others, and which named
  workflows are now the default way.
- **Outcomes** against the charter, kept separate from self-reported time saved.
- **Every time-saved figure labelled** measured or estimated, with the discount range and its basis for estimates.
- **Side effects** checked: downstream rework, review burden, policy breaches.
- **An honest read:** what we know, what we do not, and what the evidence cannot show.
- **Decisions:** what changes in the program next, and what goes to sibling skills (benefits to ai-portfolio;
  workflows worth redesigning to transformation-advisor).

## 2. How to run it

1. **Re-read the definitions** in `measures.yaml` before looking at any number (M1).
2. **Collect readings** by group from the agreed sources; never per person.
3. **Report by layer** (§4), from reach up to outcome, so nobody mistakes activity for value.
4. **Treat time saved separately** (§5): raw, discounted, and what the time went to.
5. **Check side effects** (M6).
6. **Compare** with a control group where one exists (random allocation, staggered rollout, or groups not yet
   reached).
7. **Write the honest read** and the decisions; play them back to the user.
8. **Hand off** outcome figures that the portfolio tracks to the ai-portfolio skill (`portfolio/benefits.yaml`).

## 3. Question bank

| # | Question | Scope | Notes |
|---|---|---|---|
| M1 | What does "active" mean in your numbers, and over what window? | [T][U][O] | Definitions first |
| M2 | How many people have an embedded workflow, compared with occasional prompts? | [T][U][O] | Depth, not activity |
| M3 | Which tasks are now done the AI way by default, and who signed that off? | [U] | Embedded |
| M4 | Which time-saving figures were measured, which were estimated, and by whom? | [U][O] | Label before use |
| M5 | What outcome (quality, turnaround, client responsiveness, risk, revenue) tells you the program worked? | [U][O] | Outcomes |
| M6 | What downstream rework or extra review has appeared? | [T][U] | Side effects |
| M7 | What happened to the time freed: which work did it go to? | [U][O] | Capacity needs a destination |
| M8 | Who stopped using it, and why? | [T][U] | Lapsed users; keep them in the denominator |
| M9 | Is there a group not yet reached that could serve as a comparison? | [U][O] | Comparison design |

## 4. The measurement layers

| Layer | What it shows | Example measure | Watch out for |
|---|---|---|---|
| `reach` | Access | Licensed share | Says nothing about use |
| `activity` | Use in a window | Weekly active share | One vendor dashboard counts one action in 28 days as active [MSLEARN-VIVA-2026] |
| `depth` | How deeply | Share with a repeatable workflow; share building for others; a shift from back-and-forth chat to handing over whole tasks | Needs sampled work or examples, not self-rating |
| `embedded` | The default way | Named workflows where the AI way is standard (library entries linked) | Declared defaults that nobody follows |
| `outcome` | Business effect | Cycle time, review findings, rework, client responsiveness, capacity redeployed | Attribution; capacity without a destination |
| `sentiment` | Confidence and usefulness | Confidence by segment | Leaders and frontline differ |
| `side-effect` | Costs pushed elsewhere | Rework received from colleagues | Hidden from the user's own view |

Notes on the layers:
- **Depth signals.** Anthropic's platform data show the share of conversations in which users delegate whole tasks
  rising from 27% to 39% (Claude.ai conversation samples, late 2024 to 2025; not enterprise-specific)
  [ANTHROPIC-ECONIDX-2025]; a similar shift inside a firm is one depth signal.
- **Outcome measures from pilots.** Gowling WLG's pilots measured client responsiveness, quality and risk reduction and
  collected practitioner feedback on workflow fit (vendor-published interview) [HARVEY-GOWLING-2025].
- **Activity is not value.** Shoosmiths' bonus target counted prompts (`professional-services-talent-learning-16`,
  grade A); the measure is activity, not skill or quality. Usage rose while few organizations track ROI: 18% of
  respondents to a Thomson Reuters Institute survey of more than 1,500 professionals knew theirs did [TRI-AIPS-2026].
- **Hours released are not value** until the capacity has a destination
  (`../../transformation-advisor/references/library/index.md` §5).

## 5. Time saved: measured, estimated and discounted

**Two evaluations of the same tool show why method matters.**
- The UK cross-government experiment (20,000 staff, October to December 2024) asked users to pick a time-saving range
  and used the midpoint: 26 minutes per user per day. 17% saw no clear savings, and the evaluation could not identify
  how saved time was spent (self-reported) [UKGDS-2025].
- HMRC randomly allocated 3,000 licences, drew on a survey answered by 1,364 of them (45%) and on dashboard usage data.
  Participants self-reported saving 2-3% of the working week, about 60 minutes, and HMRC reduced self-reported estimates
  by about 20% because not every licence holder used the tool and active users were likelier to answer (savings
  self-reported) [HMRC-2026].
- Large-scale data point the same way: in Danish survey data linked to registry records, users' average time savings
  were about 3% of work hours, and the study estimates no measurable effect on earnings or recorded hours (independent
  working paper) [HUMLUM-BFI-2025].

**How to report time saved**
1. Keep **measured** (tracked records, sampled work, a comparison) and **estimated** (surveys, recollection) apart. Never
   add them together.
2. For every estimate, agree a **discount range** with the user and write its basis in `discount`. HMRC's roughly 20%
   is one published reference point; a larger discount is a reasonable judgment where only keen users answered. Say it
   is judgment.
3. Show **raw and discounted** side by side, as ranges.
4. **Keep non-users in the denominator**, and record their reasons (HMRC: 46% of non-users named security and data
   privacy concerns as the main reason) [HMRC-2026].
5. Ask **what the time was used for** (M7). In Australia's government trial, 40% of participants reported being able to
   reallocate time to higher-value work (self-reported) [DTA-2024].
6. Prefer **outcome measures** from existing records (turnaround, review findings, rework) over time estimates.

## 6. Expert moves

| Move | When | What it reveals |
|---|---|---|
| Re-label the metric before reporting it: licensed, activated, weekly, embedded | A sponsor quotes a headline figure | Which rung the number measures [SECTION-2026; HARVEY-GOWLING-2025] |
| Discount self-reported savings and ask what the time was spent on | Measuring impact | Overclaim, and whether time became capacity [HMRC-2026; UKGDS-2025] |
| Use random allocation or a not-yet-reached group as a comparison | Rolling out in stages | Effect versus enthusiasm [HMRC-2026] |
| Sample downstream work for "workslop" | After a mandate or target | Output that shifts rework to colleagues: 40% of 1,150 US desk workers received it in the past month, about two hours to resolve each (BetterUp and Stanford survey) [BETTERUP-2025] |
| Build a small test set of your own work | Measuring quality | Fitness for your work; official benchmarks rarely test it [MOLLICK-LAB-2025] |
| Ask how a champion's cited saving was measured before repeating it | Reporting wins | Recollection versus tracking [PAPERJAM-2025] |
| Look at lapsed users, not only growth | Sustained use | Whether use persists; no published retention curves go beyond about a year |
| Report outcomes in the measures partners already watch | Partner reporting | Credibility with the partner group (step 6) |

## 7. Checklist and decision rules

**Checklist:** each metric defined; window stated; licensed, activated, active, repeated and embedded separated;
outcome measures added; baseline in place; quality sampled; comparison where possible; measured versus estimated
labelled; discounts written; side effects checked; readings by group only.

**Decision rules**
- Report measured or controlled results separately from survey estimates; discount estimates as a stated range.
- Always include non-users in denominators and capture reasons.
- Never link a login or prompt target to reward without a quality check (advisor's judgment).
- If activity rises but depth and embedded stay flat, the problem is use cases or workflow, not awareness: go back to
  steps 3 and 5, and consider the transformation-advisor skill.
- If outcomes do not move where use is embedded, the workflow itself may need redesign: hand off to the
  transformation-advisor skill.
- Say plainly where the evidence is thin: there is no independent evidence on champion-network effect sizes, library
  curation, partner-specific adoption, or use retained beyond the first year. The firm's own measures are the test.

## 8. Common traps

| Trap | How to avoid it |
|---|---|
| Counting logins or licences as adoption [MSLEARN-VIVA-2026] | Report by layer |
| Overclaimed time savings [UKGDS-2025; HMRC-2026] | Label, discount, sample real work |
| Non-users dropped from the denominator | Population as denominator |
| Metrics become the goal | Track depth and outcome alongside; sample for quality |
| Per-person dashboards | Groups only (core rule 1) |
| Single-number ROI | Ranges with assumptions (core rule 3) |

## 9. Worked example

*Illustrative; the firm and figures are invented.* The accounting firm after its champions and library are running.
Weekly active share has risen from about a third to about a half of the population; depth (a repeatable workflow, from
sampled work) from roughly one in ten to one in five; three workflows are declared the default way, each linked to a
library entry. Tax staff report saving one to two hours a week; with a discount of 20-50% agreed with the sponsor and
labelled as judgment, the report shows 0.5 to 1.6 hours per person per week, estimated. Measured outcomes: the share of
audit planning memos returned by reviewers fell in the groups using the planning workflow, compared with an office not
yet reached; the effect size is reported as a range, and the comparison is not random. A sample of review notes shows
no rise in rework. Unknown: whether use persists after the champions rotate. Decisions: the notice-reply workflow goes
to the transformation-advisor skill for redesign; the planning-memo outcome goes to ai-portfolio as a tracked benefit.

## 10. Output

- **`enablement/measures.yaml`**: `readings` for each measure; `discount` on every self-reported time-saved measure.
- **`enablement/program.md`**, section 7: readings by layer and segment, measured versus estimated, embedded
  workflows, outcomes, side effects, the honest read, decisions and handoffs; update the Summary.
- Frontmatter: `step_completed: 7`, `next_step: null` (or the step to revisit), `updated`.

## 11. Sources

- `ANTHROPIC-ECONIDX-2025`: *Anthropic Economic Index report (September 2025)*, Anthropic, platform usage research, 2025-09-15. https://www.anthropic.com/research/anthropic-economic-index-september-2025-report
- `BETTERUP-2025`: *Workslop: The Hidden Cost of AI-Generated Busywork*, BetterUp Labs with Stanford Social Media Lab, September 2025. https://www.betterup.com/workslop
- `DTA-2024`: *Copilot trial summary report: executive summary*, Digital Transformation Agency (Australia), 2024. https://www.digital.gov.au/initiatives/copilot-trial/summary-evaluation-findings/cts-executive-summary
- `HARVEY-GOWLING-2025`: *Al Hounsell on Driving Legal Transformation That Lasts*, Harvey blog, vendor-published, 2025-10-30. https://www.harvey.ai/blog/al-hounsell-on-driving-legal-transformation-that-lasts
- `HMRC-2026`: *Evaluating the impact of Microsoft Copilot in HMRC*, HM Revenue and Customs, 2026-07-09. https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot/evaluating-the-impact-of-microsoft-copilot-in-hmrc
- `HUMLUM-BFI-2025`: *Large Language Models, Small Labor Market Effects* (WP 2025-56), Becker Friedman Institute, 2025-05-09. https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf
- `MOLLICK-LAB-2025`: *Making AI Work: Leadership, Lab, and Crowd*, One Useful Thing, 2025-05-22. https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- `MSLEARN-VIVA-2026`: *Microsoft Copilot Dashboard in Viva Insights*, Microsoft Learn, undated. https://learn.microsoft.com/en-us/viva/insights/org-team-insights/copilot-dashboard
- `PAPERJAM-2025`: *Why AI is a strategic priority for modern law firms: Francesca Bennetts*, Paperjam, 2025-06-19. https://en.paperjam.lu/article/why-ai-is-a-strategic-priority-for-modern-law-firms-francesca-bennetts
- `SECTION-2026`: *The AI Proficiency Report*, Section, June 2026. https://www.sectionai.com/ai/the-ai-proficiency-report
- `TRI-AIPS-2026`: *2026 AI in Professional Services Report*, Thomson Reuters Institute, 2026-02-09. https://www.thomsonreuters.com/en-us/posts/technology/ai-in-professional-services-report-2026/
- `UKGDS-2025`: *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, UK Government Digital Service, June 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf

Archetype use case cited (grade as recorded): `professional-services-talent-learning-16`
(`../../transformation-advisor/references/archetypes/index.md`).
