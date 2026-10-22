# Measure sustained adoption and impact (step 7)

Read this on entering step 7, and whenever someone quotes an adoption or time-saved figure. It measures depth of use,
embedded workflows and outcomes, labels what is measured and what is estimated, and discounts self-reports honestly.
Source keys in brackets are listed in §8.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [The measurement layers](#4-the-measurement-layers)
5. [Time saved: measured, estimated and discounted](#5-time-saved-measured-estimated-and-discounted)
6. [Rules of thumb and traps](#6-rules-of-thumb-and-traps)
7. [Worked example and output](#7-worked-example-and-output)
8. [Sources](#8-sources)

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
5. **Check side effects** (M5).
6. **Compare** with a control group where one exists (random allocation, staggered rollout, or groups not yet
   reached) [HMRC-2026].
7. **Write the honest read** and the decisions; play them back to the user.
8. **Hand off** outcome figures that the portfolio tracks to ai-portfolio (`portfolio/benefits.yaml`).

## 3. Question bank

| # | Question | Notes |
|---|---|---|
| M1 | What does "active" mean in your numbers, and over what window? | Definitions first |
| M2 | How many people have an embedded workflow, compared with occasional prompts? Which tasks are now done the AI way by default, and who signed that off? | Depth and embedded |
| M3 | Which time-saving figures were measured, which were estimated, and by whom? | Label before use |
| M4 | What outcome (quality, turnaround, client responsiveness, risk, revenue) tells you the program worked, and what happened to the time freed? | Outcomes; capacity needs a destination |
| M5 | What downstream rework or extra review has appeared? | Side effects |
| M6 | Who stopped using it, and why? | Lapsed users stay in the denominator |

## 4. The measurement layers

| Layer | What it shows | Example measure | Watch out for |
|---|---|---|---|
| `reach` | Access | Licensed share | Says nothing about use |
| `activity` | Use in a window | Weekly active share | One vendor dashboard counts one action in 28 days as active [MSLEARN-VIVA-2026] |
| `depth` | How deeply | Share with a repeatable workflow; share building for others; handing over whole tasks rather than chatting | Needs sampled work or examples, not self-rating |
| `embedded` | The default way | Named workflows where the AI way is standard (library entries linked) | Declared defaults that nobody follows |
| `outcome` | Business effect | Cycle time, review findings, rework, client responsiveness, capacity redeployed | Attribution; capacity without a destination |
| `sentiment` | Confidence and usefulness | Confidence by segment | Leaders and frontline differ |
| `side-effect` | Costs pushed elsewhere | Rework received from colleagues | Hidden from the user's own view |

- **Activity is not value.** Shoosmiths' bonus target counted prompts (`professional-services-talent-learning-16`,
  grade A). Usage rose while few track ROI: 18% of respondents to a Thomson Reuters Institute survey of more than 1,500
  professionals knew their organization did [TRI-AIPS-2026].
- **Hours released are not value** until the capacity has a destination
  (`../../transformation-advisor/references/library/index.md` §5).

## 5. Time saved: measured, estimated and discounted

**Two evaluations of the same tool show why method matters.**
- The UK cross-government experiment (20,000 staff, late 2024) asked users to pick a time-saving range and used the
  midpoint: 26 minutes per user per day. 17% saw no clear savings, and the evaluation could not identify how saved time
  was spent (self-reported) [UKGDS-2025].
- HMRC randomly allocated 3,000 licences; participants self-reported saving 2-3% of the working week, and HMRC reduced
  self-reported estimates by about 20% because not every licence holder used the tool and active users were likelier
  to answer [HMRC-2026].

**How to report time saved**
1. Keep **measured** (tracked records, sampled work, a comparison) and **estimated** (surveys, recollection) apart.
   Never add them together.
2. For every estimate, agree a **discount range** with the user and write its basis in `discount`. HMRC's roughly 20%
   is one published reference point; a larger discount is a reasonable judgment where only keen users answered. Say
   it is judgment.
3. Show **raw and discounted** side by side, as ranges.
4. **Keep non-users in the denominator**, and record their reasons.
5. Ask **what the time was used for** (M4). In Australia's government trial, 40% of participants reported being able
   to reallocate time to higher-value work (self-reported) [DTA-2024].
6. Prefer **outcome measures** from existing records (turnaround, review findings, rework) over time estimates.

## 6. Rules of thumb and traps

- **Sample downstream work for "workslop"** after a mandate or target: 40% of 1,150 US desk workers had received it in
  the past month, about two hours to resolve each [BETTERUP-2025].
- **Ask how a cited saving was measured** before repeating it: A&O Shearman lawyers "report saving two to three hours a
  week" (self-reported) [PAPERJAM-2025].
- **Look at lapsed users, not only growth.** No published retention curves go beyond about a year.
- **Report outcomes in the measures partners already watch** (step 6).
- If activity rises but depth and embedded stay flat, the problem is use cases or workflow, not awareness: go back to
  steps 3 and 5. If outcomes do not move where use is embedded, the workflow may need redesign: hand off to
  transformation-advisor.
- Never link a login or prompt target to reward without a quality check.
- Say plainly where the evidence is thin (rule 14). The firm's own measures are the test.
- **Traps:** counting logins as adoption; overclaimed time savings; non-users dropped from the denominator; metrics
  that become the goal; per-person dashboards; a single-number ROI.

## 7. Worked example and output

*Illustrative; the firm and figures are invented.* Weekly active share has risen from about a third to about a half;
depth (from sampled work) from roughly one in ten to one in five; three workflows are declared the default way. Tax
staff report saving one to two hours a week; with a 20-50% discount agreed with the sponsor and labelled as judgment,
the report shows 0.5 to 1.6 hours per person per week, estimated. Measured: fewer audit planning memos returned by
reviewers in groups using the workflow, against an office not yet reached (not random; reported as a range). Unknown:
whether use persists after champions rotate. Decisions: the notice-reply workflow goes to transformation-advisor; the
planning-memo outcome goes to ai-portfolio as a tracked benefit.

**Output:**
- **`enablement/measures.yaml`**: `readings` for each measure; `discount` on every self-reported time-saved measure.
- **`enablement/program.md`**, section 7: readings by layer and segment, measured versus estimated, embedded
  workflows, outcomes, side effects, the honest read, decisions and handoffs; update the Summary.
- Frontmatter: `step_completed: 7`, `next_step: null` (or the step to revisit), `updated`.

## 8. Sources

- `BETTERUP-2025`: *Workslop: The Hidden Cost of AI-Generated Busywork*, BetterUp Labs with Stanford Social Media Lab, September 2025. https://www.betterup.com/workslop
- `DTA-2024`: *Copilot trial summary report: executive summary*, Digital Transformation Agency (Australia), 2024. https://www.digital.gov.au/initiatives/copilot-trial/summary-evaluation-findings/cts-executive-summary
- `HMRC-2026`: *Evaluating the impact of Microsoft Copilot in HMRC*, HM Revenue and Customs, 2026-07-09. https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot/evaluating-the-impact-of-microsoft-copilot-in-hmrc
- `MSLEARN-VIVA-2026`: *Microsoft Copilot Dashboard in Viva Insights*, Microsoft Learn, undated. https://learn.microsoft.com/en-us/viva/insights/org-team-insights/copilot-dashboard
- `PAPERJAM-2025`: *Why AI is a strategic priority for modern law firms: Francesca Bennetts*, Paperjam, 2025-06-19. https://en.paperjam.lu/article/why-ai-is-a-strategic-priority-for-modern-law-firms-francesca-bennetts
- `TRI-AIPS-2026`: *2026 AI in Professional Services Report*, Thomson Reuters Institute, 2026-02-09. https://www.thomsonreuters.com/en-us/posts/technology/ai-in-professional-services-report-2026/
- `UKGDS-2025`: *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, UK Government Digital Service, June 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf

Archetype use case cited (grade as recorded): `professional-services-talent-learning-16`
(`../../transformation-advisor/references/archetypes/index.md`).
