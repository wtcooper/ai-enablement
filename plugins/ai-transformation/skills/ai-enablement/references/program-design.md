# Design the program (step 2)

Read this on entering step 2. It turns the baseline into a program charter: goals tied to business outcomes, an owner,
leader expectations, protected learning time, links to governance, and a measurement plan. Source keys in brackets
are listed in §8.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [The operating model](#4-the-operating-model)
5. [Leader expectations, learning time and incentives](#5-leader-expectations-learning-time-and-incentives)
6. [Worked example](#6-worked-example)
7. [Output](#7-output)
8. [Sources](#8-sources)

## 1. Goal and exit criteria

**Goal.** A program people can see is about their work and the firm's results, with someone accountable for it, and
the conditions that make sustained use likely: time, expectations, safe tools and a reason to share.

**Exit when all of these are true:**
- **Goal tied to business outcomes** (quality, turnaround, client responsiveness, capacity, growth, risk), with one to
  three **target workflows per role** where success would be obvious.
- **Owner** named by role, with budget and authority; a **sponsor** who uses AI where others can see it.
- **Operating model:** who leads, who builds shared assets, how the crowd contributes, and when the central team
  moves to an advisory role (§4).
- **Learning time:** how much, for whom, and whether it counts toward billable or utilisation targets.
- **Leader and manager expectations** in writing, with whether usage tracking is for measurement or for policing (§5).
- **What happens to time saved**, stated honestly: redeploy, reduce, or not yet decided (core rule 2).
- **Governance links:** approved tools, data rules, training before access, and the intake gate for new use cases.
- **Measurement plan:** every measure the charter names is defined in `enablement/measures.yaml`.
- **Steps** sequenced as Now, Next and Later by dependency, each with an owner by role (core rule 9).

## 2. How to run it

1. **Start from the business problem** (P1). Training alone rarely moves value: BCG finds 5% of 1,250 firms get
   value at scale and 60% little, and recommends putting 70% of effort into people and processes (BCG's recommended
   split, not an observed fact; vendor-published) [BCG-VALUEGAP-2025]. Individual gains do not become organizational
   gains without changes to how work is organized [MOLLICK-LAB-2025]; route such workflows to transformation-advisor.
2. **Name target workflows per role** (P2). "AI literacy" is not a goal.
3. **Find the owner** (P3). In Section's survey, 53.2% said their organization had no Head of AI or were unsure;
   workers with a full-time Head of AI averaged 42 against 33 on Section's scoring (correlational, vendor-published)
   [SECTION-2026].
4. **Decide learning time and credit** (P4), and **write expectations** for leaders and managers (§5).
5. **Say what happens to time saved** (P5). Workers want clear answers on layoffs versus growth and on how use will be
   rewarded or punished [MOLLICK-LAB-2025]; 15% of US employees said AI or automation would likely eliminate their job
   within five years [GALLUP-2025]. If it is undecided, say so, and what the decision depends on.
6. **Link governance** (P6). If `overlay/policy.md` and `overlay/tool-catalog.yaml` exist, cite them. If not, hand off
   to ai-governance before any curriculum covers client data.
7. **Define measures** in `measures.yaml` using the layers in `measure-adoption.md` §4, including at least one
   `embedded` and one `outcome` measure.
8. **Sequence** Now, Next, Later by dependency. Play back the charter and write it.

## 3. Question bank

| # | Question | Notes |
|---|---|---|
| P1 | If this works, what will be different for clients and for the firm's results, not only for tool use? | Ties the program to outcomes |
| P2 | For each role, which one workflow would make success obvious if people did it the new way? | Target workflows |
| P3 | Who owns this, with what budget, and what can they decide? | No owner, no program |
| P4 | How much working time can people spend learning, and does it count toward their targets? | The credit rule |
| P5 | If people save time, what happens to it? Has anyone told staff? | The credibility test |
| P6 | Which tools may people use, with which data, and who decides new uses? | Governance links |
| P7 | What has been tried already (training, pilots, mandates), and what happened? | Avoid repeating failures |
| P8 | What would the sponsor accept as proof the program worked? | The measurement plan |

## 4. The operating model

**Leadership, Lab, Crowd.** Leaders set direction and incentives, a small central "lab" turns discoveries into shared
assets and measures them, and the crowd of employees finds the use cases [MOLLICK-LAB-2025]. In a firm: the sponsor and
practice leaders, an enablement or knowledge team, and the champion network (step 4). In law firms the knowledge team
often runs it (`professional-services-knowledge-management-18`, grade B).

**Central first, then advisory.** Microsoft's Cloud Adoption Framework suggests a central AI centre of excellence early
and a move to an advisory role as capability embeds (vendor guidance) [MSLEARN-COE-ND]. Write the condition for
stepping back ("each practice has an active champion group and its own library reviewer"), not a date.

**Governance gate.** ILTA's 2026 survey of 508 law firms found 11% of firms under 50 lawyers and 72% of those over 700
require training before use (trade association survey) [ILTA-2026] (`professional-services-talent-learning-01`, grade
B; `professional-services-work-production-22`, grade B). ai-governance owns the policy; this program links to it.

## 5. Leader expectations, learning time and incentives

**Expectations.** In Section's survey, only 7% of managers required AI use and tied it to performance reviews;
employees whose managers expect and require use scored 1.5 times higher on proficiency (correlational,
vendor-published) [SECTION-2026]. In Gallup's panel, 22% said their organization had communicated a clear plan; those
who strongly agreed were three times as likely to feel very prepared [GALLUP-2025].

**What firms report doing** (announcements; no outcome data): KPMG tracks use through tool data and will assess staff
on AI objectives in 2026 reviews, saying monitoring is not for policing [BLAW-KPMG-2025]
(`professional-services-talent-learning-15`, grade B). Shoosmiths tied an extra GBP 1 million in its bonus pool to one
million prompts and reported reaching it early (`professional-services-talent-learning-16`, grade A); the metric is
activity, not skill or quality.

**How this skill writes expectations:** by role, as behaviours and outputs ("each manager demonstrates one real use
to the team each month and names one target workflow"), never as ratings of people. If the firm puts AI objectives
into performance reviews, that runs through its own HR process.

**Learning time.** Ropes & Gray lets first-years put 20% of billable hours toward learning AI [BLAW-ROPES-2026]
(`professional-services-talent-learning-03`, grade B). Decide the credit rule even if the answer is no: Polsinelli's
chair gives no billing credit for AI training [POLSINELLI-2026], and under ABA Formal Opinion 512 a lawyer may not bill
a client for gaining AI competence unless the client asks (secondary summary) [LAWNEXT-2024]. If no time can be
protected, expect weaker take-up and say so: UK trial users said work capacity limited their participation
[UKGDS-2025].

**Rules of thumb** (tell the user they are working rules):
- Pair training with a named workflow and a manager expectation: regular use was sharply higher among employees with
  at least five hours of training and in-person coaching (correlational) [BCG-ATWORK-2025].
- Never tie a login or prompt-count target to reward without a quality check; mandates without value produce
  "workslop" that shifts rework to colleagues [BETTERUP-2025]. Say whether tracking is measurement or policing.
- Set only consequences the firm will actually apply.
- Plan for adoption gains first and outcome gains only where workflows change: in Danish data, employer encouragement
  nearly doubled take-up (47% to 83%), yet users saved about 3% of hours on average, with no measurable effect on
  earnings or recorded hours (independent working paper) [HUMLUM-BFI-2025].

## 6. Worked example

*Illustrative; the firm and figures are invented.* The accounting firm from step 1. Goal: faster, better first drafts
of engagement memos and tax research summaries, and audit review notes cleared with less rework. Owner: the director of
knowledge, with a budget line. A three-person central team builds shared assets and moves to advice once each practice
has an active champion group and a library reviewer. Learning time: two hours a week on a non-chargeable code that
counts toward targets. Expectations: each manager shows one real use a month; usage is reported by group for
measurement. Time saved: redeploy to the advisory backlog; no role reductions planned now, revisited once outcome
measures exist. Now: owner, charter, data rule. Next: curriculum and champions. Later: library at scale.

## 7. Output

- **`enablement/program.md`**, section 2: the charter (fields in §1).
- **`enablement/measures.yaml`**: every charter measure defined, including at least one `embedded` and one `outcome`.
- Frontmatter: `step_completed: 2`, `next_step: 3`, `links` updated, `updated`.

## 8. Sources

- `BCG-ATWORK-2025`: *AI at Work: Momentum Builds, but Gaps Remain*, BCG, June 2025. https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain
- `BCG-VALUEGAP-2025`: *The Widening AI Value Gap*, BCG, October 2025. https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf
- `BETTERUP-2025`: *Workslop: The Hidden Cost of AI-Generated Busywork*, BetterUp Labs with Stanford Social Media Lab, September 2025. https://www.betterup.com/workslop
- `BLAW-KPMG-2025`: *KPMG Staff to Be Rated on AI Usage in Yearly Performance Reviews*, Bloomberg Law, 2025-10-31. https://news.bgov.com/health-law-and-business/kpmg-staff-to-be-rated-on-ai-usage-in-yearly-performance-reviews
- `BLAW-ROPES-2026`: *What Does It Take to Get Big Law Associates Excited About AI?*, Bloomberg Law, 2026-07-30. https://news.bgov.com/business-and-practice/what-does-it-take-to-get-big-law-associates-excited-about-ai
- `GALLUP-2025`: *AI Use at Work Has Nearly Doubled in Two Years*, Gallup, June 2025. https://www.gallup.com/workplace/691643/work-nearly-doubled-two-years.aspx
- `HUMLUM-BFI-2025`: *Large Language Models, Small Labor Market Effects* (WP 2025-56), Becker Friedman Institute, 2025-05-09. https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf
- `ILTA-2026`: *The ILTA Technology Survey 2026 Executive Summary*, ILTA, June 2026. https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
- `LAWNEXT-2024`: *In First Ethics Ruling on Gen AI, ABA Says Lawyers Must Have Reasonable Understanding of the Technology*, LawSites, 2024-07-30. https://lawnext.com/2024/07/in-first-ethics-ruling-on-gen-ai-aba-says-lawyers-must-have-reasonable-understanding-of-the-technology-but-need-not-become-experts.html
- `MOLLICK-LAB-2025`: *Making AI Work: Leadership, Lab, and Crowd*, One Useful Thing, 2025-05-22. https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- `MSLEARN-COE-ND`: *Establish an AI Center of Excellence* (Cloud Adoption Framework), Microsoft Learn, undated. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence
- `POLSINELLI-2026`: *Why Polsinelli Lawyers Won't Get Billing Credit for AI Training* (podcast transcript), Bloomberg Law, 2026-03-24. https://news.bgov.com/business-and-practice/why-polsinelli-lawyers-wont-get-billing-credit-for-ai-training
- `SECTION-2026`: *The AI Proficiency Report*, Section, June 2026. https://www.sectionai.com/ai/the-ai-proficiency-report
- `UKGDS-2025`: *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, UK Government Digital Service, June 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf

Archetype use cases cited (grades as recorded): `professional-services-talent-learning-01`, `-03`, `-15`, `-16`;
`professional-services-knowledge-management-18`; `professional-services-work-production-22`, in
`../../transformation-advisor/references/archetypes/professional-services/use-cases/`.
