# Measure sustained adoption and impact (step 7)

Read this on entering step 7, and whenever someone quotes an adoption or time-saved figure. It measures depth of use,
embedded workflows and outcomes, labels what is measured and what is estimated, and discounts self-reports honestly.
Source keys in brackets are listed in §6.

## 1. Goal and exit criteria

**Goal.** An honest picture of whether use is sustained and deepening, which workflows have become the default way of
working, and what that has done to outcomes the firm cares about.

**Exit when all of these are true:** readings for each measure in `measures.yaml`, by segment, with the window and the
denominator (non-users included); depth and embedded counts (how many have a repeatable workflow, how many build for
others, which named workflows are the default way); outcomes against the charter, kept apart from self-reported time
saved; every time-saved figure labelled measured or estimated, with a discount range and its basis for estimates; side
effects checked (downstream rework, review burden, policy breaches); an honest read (what we know, what we do not,
what the evidence cannot show); decisions, and handoffs (benefits to ai-portfolio; redesign to
transformation-advisor).

## 2. How to run it

1. **Definitions first:** "What does 'active' mean in your numbers, and over what window?" Re-read `measures.yaml`.
2. **Collect readings** by group from the agreed sources; never per person. Ask who stopped using it, and why.
3. **Report by layer** (§3), from reach up to outcome: "How many people have an embedded workflow, compared with
   occasional prompts? Which tasks are now done the AI way by default, and who signed that off?"
4. **Time saved** (§4): "Which time-saving figures were measured, which estimated, and by whom? What happened to the
   time freed?"
5. **Side effects:** "What downstream rework or extra review has appeared?"
6. **Compare** with a control group where one exists (random allocation, staggered rollout, or groups not yet reached)
   [HMRC-2026].
7. **Write the honest read** and the decisions; play them back. Hand outcome figures the portfolio tracks to
   ai-portfolio (`portfolio/benefits.yaml`).

## 3. The measurement layers

| Layer | What it shows | Example measure | Watch out for |
|---|---|---|---|
| `reach` | Access | Licensed share | Says nothing about use |
| `activity` | Use in a window | Weekly active share | One dashboard counts one action in 28 days as active [MSLEARN-VIVA-2026] |
| `depth` | How deeply | Share with a repeatable workflow, or building for others | Needs sampled work, not self-rating |
| `embedded` | The default way | Named workflows where the AI way is standard (library entries linked) | Declared defaults nobody follows |
| `outcome` | Business effect | Cycle time, review findings, rework, client responsiveness, capacity redeployed | Attribution; capacity without a destination |
| `sentiment` | Confidence, usefulness | Confidence by segment | Leaders and frontline differ |
| `side-effect` | Costs pushed elsewhere | Rework received from colleagues | Hidden from the user's own view |

Activity is not value: Shoosmiths' bonus target counted prompts (`professional-services-talent-learning-16`, grade
A), and only 18% of respondents to a Thomson Reuters Institute survey of more than 1,500 professionals knew their
organization tracked AI ROI [TRI-AIPS-2026]. Hours released are not value until the capacity has a destination
(`../../transformation-advisor/references/library/index.md` §5).

## 4. Time saved: measured, estimated and discounted

Two evaluations of the same tool show why method matters. The UK cross-government experiment (20,000 staff) asked
users to pick a range and used the midpoint, 26 minutes per user per day; 17% saw no clear savings, and it could not
identify how saved time was spent (self-reported) [UKGDS-2025]. HMRC randomly allocated 3,000 licences; participants
self-reported saving 2-3% of the working week, and HMRC cut those estimates by about 20% because not every licence
holder used the tool and active users were likelier to answer [HMRC-2026].

1. Keep **measured** (tracked records, sampled work, a comparison) and **estimated** (surveys, recollection) apart.
   Never add them together.
2. For every estimate, agree a **discount range** with the user and write its basis in `discount`. HMRC's roughly 20%
   is one published reference point; a larger discount is reasonable where only keen users answered. Say it is
   judgment. Show **raw and discounted** side by side, as ranges.
3. **Keep non-users in the denominator**, and record their reasons.
4. Ask **what the time was used for:** in Australia's government trial, 40% of participants reported being able to
   reallocate time to higher-value work (self-reported) [DTA-2024]. Prefer outcome measures from existing records.

## 5. Rules of thumb, example and output

- **Sample downstream work for "workslop"** after a mandate or target: 40% of 1,150 US desk workers had received it in
  the past month, about two hours to resolve each [BETTERUP-2025].
- **Ask how a cited saving was measured** before repeating it: A&O Shearman lawyers "report saving two to three hours a
  week" (self-reported) [PAPERJAM-2025]. Look at lapsed users, not only growth; no published retention curves go
  beyond about a year. Report outcomes in the measures partners already watch.
- If activity rises but depth and embedded stay flat, go back to steps 3 and 5. If outcomes do not move where use is
  embedded, the workflow may need redesign: hand off to transformation-advisor. Say where evidence is thin (rule 14).
- **Traps:** logins as adoption; non-users dropped; metrics that become the goal; per-person dashboards; one-number ROI.

*Illustrative (invented).* Tax staff report saving one to two hours a week; with a 20-50% discount agreed with the
sponsor and labelled as judgment, the report shows 0.5 to 1.6 hours per person per week, estimated. Measured apart:
fewer planning memos returned by reviewers than in an office not yet reached (not random; a range). The planning-memo
outcome goes to ai-portfolio as a tracked benefit.

**Output:** `measures.yaml` readings, with `discount` on every self-reported time-saved measure; `program.md` section 7
(readings by layer and segment, measured versus estimated, embedded workflows, outcomes, side effects, the honest read,
decisions and handoffs) and the Summary; frontmatter `step_completed: 7`, `next_step: null` (or the step to revisit),
`updated`.

## 6. Sources

- `BETTERUP-2025`: *Workslop: The Hidden Cost of AI-Generated Busywork*, BetterUp Labs with Stanford Social Media Lab, September 2025. https://www.betterup.com/workslop
- `DTA-2024`: *Copilot trial summary report: executive summary*, Digital Transformation Agency (Australia), 2024. https://www.digital.gov.au/initiatives/copilot-trial/summary-evaluation-findings/cts-executive-summary
- `HMRC-2026`: *Evaluating the impact of Microsoft Copilot in HMRC*, HM Revenue and Customs, 2026-07-09. https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot/evaluating-the-impact-of-microsoft-copilot-in-hmrc
- `MSLEARN-VIVA-2026`: *Microsoft Copilot Dashboard in Viva Insights*, Microsoft Learn, undated. https://learn.microsoft.com/en-us/viva/insights/org-team-insights/copilot-dashboard
- `PAPERJAM-2025`: *Why AI is a strategic priority for modern law firms: Francesca Bennetts*, Paperjam, 2025-06-19. https://en.paperjam.lu/article/why-ai-is-a-strategic-priority-for-modern-law-firms-francesca-bennetts
- `TRI-AIPS-2026`: *2026 AI in Professional Services Report*, Thomson Reuters Institute, 2026-02-09. https://www.thomsonreuters.com/en-us/posts/technology/ai-in-professional-services-report-2026/
- `UKGDS-2025`: *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, UK Government Digital Service, June 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf
- Archetype use case (grade as recorded): `../../transformation-advisor/references/archetypes/index.md`.
