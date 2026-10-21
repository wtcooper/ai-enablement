# Design the program (step 2)

Read this on entering step 2. It turns the baseline into a program charter: goals tied to business outcomes, an owner,
leader expectations, protected learning time, links to governance, and a measurement plan. Source keys in brackets
are listed in §11. Tags: **[T]** team, **[U]** unit, **[O]** organization.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [The operating model](#4-the-operating-model)
5. [Leader expectations and incentives](#5-leader-expectations-and-incentives)
6. [Expert moves](#6-expert-moves)
7. [Checklist and decision rules](#7-checklist-and-decision-rules)
8. [Common traps](#8-common-traps)
9. [Worked example](#9-worked-example)
10. [Output](#10-output)
11. [Sources](#11-sources)

## 1. Goal and exit criteria

**Goal.** A program people can see is about their work and the firm's results, with someone accountable for it, and
the conditions that make sustained use likely: time, expectations, safe tools and a reason to share.

**Exit when all of these are true:**
- **Goal tied to business outcomes** (quality, turnaround, client responsiveness, capacity, growth, risk), with one to
  three **target workflows per role** where success would be obvious.
- **Owner** named by role, with budget and authority; a **sponsor** who uses AI where others can see it.
- **Operating model:** who leads, who builds shared assets, how the crowd contributes, and when the central team
  moves to an advisory role (§4).
- **Learning time:** how much, for whom, and whether it counts toward billable or utilisation targets, decided and
  recorded.
- **Leader and manager expectations** in writing, with whether usage tracking is for measurement or for policing (§5).
- **What happens to time saved**, stated honestly: redeploy, reduce, or not yet decided (core rule 2).
- **Governance links:** approved tools, data rules, training before access, and the intake gate for new use cases.
- **Measurement plan:** every measure the charter names is defined in `enablement/measures.yaml`.
- **Steps** sequenced as Now, Next and Later by dependency, each with an owner by role (core rule 9).

## 2. How to run it

1. **Start from the business problem** (P1). Training alone rarely moves value: BCG finds 5% of 1,250 firms get
   value at scale and 60% little, and recommends putting 70% of effort into people and processes (BCG's recommended
   split, not an observed fact; vendor-published) [BCG-VALUEGAP-2025]. Individual gains do not become organizational
   gains without changes to how work is organized [MOLLICK-LAB-2025].
2. **Name target workflows per role** (P2). "AI literacy" is not a goal.
3. **Find the owner** (P3). Section's survey of 5,026 US knowledge workers found 53.2% said their organization had no
   Head of AI or they were unsure; workers with a full-time Head of AI averaged 42 against 33 on Section's scoring
   (correlational, vendor-published) [SECTION-2026].
4. **Decide learning time and credit** (P4). Say the rule out loud (§6).
5. **Write expectations** for leaders and managers (§5).
6. **Say what happens to time saved** (P6). Workers want clear answers on layoffs versus growth and on how use will be
   rewarded or punished [MOLLICK-LAB-2025]. If it is undecided, say that, and when it will be decided by dependency.
7. **Link governance** (P7). If `overlay/policy.md` and `overlay/tool-catalog.yaml` exist, cite them. If not, hand off
   to the ai-governance skill before any curriculum covers client data.
8. **Define measures** in `measures.yaml` using the layers in `measure-adoption.md` §4.
9. **Sequence** Now, Next, Later by dependency. Play back the charter and write it.

## 3. Question bank

| # | Question | Scope | Notes |
|---|---|---|---|
| P1 | If this works, what will be different for clients and for the firm's results, not only for tool use? | [T][U][O] | Ties the program to outcomes |
| P2 | For each role, which one workflow would make success obvious if people did it the new way? | [T][U] | Target workflows |
| P3 | Who owns this, with what budget, and what can they decide? | [U][O] | No owner, no program |
| P4 | How much working time can people spend learning, and does it count toward their targets? | [T][U][O] | The credit rule |
| P5 | What will leaders and managers be expected to do, and will the most senior people do it visibly? | [U][O] | Expectations and modelling |
| P6 | If people save time, what happens to it? Has anyone told staff? | [T][U][O] | The credibility test |
| P7 | Which tools may people use, with which data, and who decides new uses? | [U][O] | Governance links |
| P8 | What has been tried already (training, pilots, mandates), and what happened? | [U][O] | Avoid repeating failures |
| P9 | Is there a central team, and how will it hand over to the practices as they mature? | [O] | Operating model |
| P10 | What would the sponsor accept as proof the program worked? | [U][O] | The measurement plan |

## 4. The operating model

**Leadership, Lab, Crowd.** Mollick's practitioner frame: leaders set direction and incentives, a small central "lab"
turns discoveries into shared assets and measures them, and the crowd of employees finds the use cases
[MOLLICK-LAB-2025]. In a firm this maps to the sponsor and practice leaders, an enablement or knowledge team, and the
champion network (step 4).

**Central first, then advisory.** Microsoft's Cloud Adoption Framework suggests a central AI centre of excellence early
and a move toward an advisory role as capability embeds. Its listed duties include skills assessment, learning
pathways, intake and prioritization, reusable assets with compliance checklists, and adoption KPIs (vendor guidance)
[MSLEARN-COE-ND]. Write the condition for stepping back (for example, "each practice has an active champion group and
its own library reviewer"), not a date.

**Knowledge teams often run it in law firms.** Troutman Pepper Locke, Lewis Silkin, Ropes & Gray and Gowling WLG put
knowledge-management people at the centre of AI know-how (`professional-services-knowledge-management-18`, grade B).

**Governance gate.** Training and policy as a condition of tool access is common in large firms and rare in small ones:
ILTA's 2026 survey of 508 law firms found 11% of firms under 50 lawyers and 72% of those over 700 require training
before use (trade association survey) [ILTA-2026] (`professional-services-talent-learning-01`, grade B;
`professional-services-work-production-22`, grade B). The ai-governance skill owns the policy; this program links to it.

## 5. Leader expectations and incentives

Manager expectations are a recurring gap. In Section's survey, only 7% of managers required AI use and tied it to
performance reviews; employees whose managers expect and require use scored 1.5 times higher on proficiency
(correlational, vendor-published) [SECTION-2026]. Gallup's panel survey of US employees found 22% said their
organization had communicated a clear plan; those who strongly agreed were three times as likely to feel very prepared
(independent survey) [GALLUP-2025]. In BCG's survey, the share of employees positive about AI rose from 15% to 55% with
strong leadership support (correlational) [BCG-ATWORK-2025].

**What firms report doing** (announcements; no outcome data published):
- KPMG tracks use through tool data and will assess staff on AI objectives in 2026 reviews, saying monitoring is not
  for policing [BLAW-KPMG-2025] (`professional-services-talent-learning-15`, grade B).
- Accenture reportedly collects weekly logins of senior staff and links leadership promotion to "regular adoption"
  (via the Financial Times, second-hand) [DECRYPT-ACCENTURE-2026].
- PwC's US CEO told the Financial Times that partners who resist AI will not be at the firm for long (second-hand)
  [CPAPA-PWC-2026].
- Shoosmiths tied an extra GBP 1 million in its firmwide bonus pool to one million prompts; the firm reported reaching
  it early (`professional-services-talent-learning-16`, grade A). The metric is activity, not skill or quality.

**How this skill writes expectations** (core rule 1): by role, as behaviours and outputs ("each manager demonstrates one
real use to the team each month and names one target workflow"), never as ratings of people. If the firm puts AI
objectives into performance reviews, that runs through its own HR process; this skill helps design what the measure
rewards and how quality is checked, and does not rate anyone.

## 6. Expert moves

| Move | When | What it reveals |
|---|---|---|
| Credit learning time and say how much | The constraint is "no time" | Whether the priority is real. Ropes & Gray lets first-years put 20% of billable hours toward learning AI [BLAW-ROPES-2026] (`professional-services-talent-learning-03`, grade B). UK trial users cited limited capacity to take part in upskilling [UKGDS-2025] |
| Decide the credit rule even if the answer is no | Partners ask "what about my hours?" | Polsinelli's chair says there is no billing credit for AI training [POLSINELLI-2026]; under ABA Formal Opinion 512 a lawyer may not bill a client for time spent gaining AI competence unless the client asks (secondary summary) [LAWNEXT-2024] |
| Write down what happens to time saved, before incentives or mandates | Launch | Whether the vision is credible. Gallup: 15% of US employees said it was very or somewhat likely that AI or automation would eliminate their job within five years [GALLUP-2025] |
| Ask what behaviour a metric rewards before wiring it to reviews | Leader expectations | Gameable targets. Logins alone can be gamed (advisor's judgment; no published evidence either way) |
| Separate usage tracking from policing, and say which it is | Setting expectations | Fear of surveillance [BLAW-KPMG-2025] |
| Pair training with a named workflow and a manager expectation | Design | Training alone has weak backing. In BCG's survey, regular use was sharply higher among employees with at least five hours of training and access to in-person training and coaching (correlational) [BCG-ATWORK-2025] |
| Put a respected, business-minded senior person in charge and frame it as a business problem | Earlier efforts produced activity without progress | Legitimacy with partners [POLSINELLI-2026] |
| Pick the forum where the program is reviewed and keep its rhythm | Governance | A law firm in a CIPD case ran a fortnightly cross-functional steering group (anonymized case) [CIPD-2026] |

## 7. Checklist and decision rules

**Charter checklist:** goal and target workflows; segments and target ranges; owner and budget; operating model and
step-back condition; learning time and credit rule; champion network (step 4); forums; library rules (step 5);
measures (layers, definitions, data source); leader and manager expectations; what happens to saved time; governance
links; Now / Next / Later.

**Decision rules**
- Centralize first when capability is low; move to advisory as practices embed [MSLEARN-COE-ND].
- If no learning time can be protected, expect weaker take-up and say so (working rule; UK trial users said their work
  capacity limited their participation [UKGDS-2025]).
- Never tie a login or prompt-count target to reward without a quality check (advisor's judgment; Shoosmiths' metric
  measured activity only, `professional-services-talent-learning-16`).
- Set only consequences the firm will actually apply.
- Employer encouragement matters: in Danish survey and registry data, employer encouragement nearly doubled take-up for
  a typical worker (47% to 83%), yet users' average time saved was about 3% and the study estimates no measurable effect
  on earnings or recorded hours (independent working paper) [HUMLUM-BFI-2025]. Plan for adoption gains first and outcome
  gains only where workflows change (advisor's reading).

## 8. Common traps

| Trap | How to avoid it |
|---|---|
| No plan or use case communicated [GALLUP-2025] | Name target workflows per role and say what success means |
| No owner for enablement [SECTION-2026] | Name an owner with budget |
| Mandate without value, producing "workslop" that shifts rework to colleagues [BETTERUP-2025] | Pair expectations with quality review; measure rework (step 7) |
| Individual gains, no organizational change [HUMLUM-BFI-2025; MOLLICK-LAB-2025] | Route target workflows to the transformation-advisor skill for redesign |
| Calendar time boxes for adoption | Sequence by dependency (core rule 9) |

## 9. Worked example

*Illustrative; the firm and figures are invented.* The accounting firm from step 1. Goal: faster, better first drafts
of engagement memos and tax technical summaries, and audit review notes cleared with less rework. Target workflows:
audit seniors' planning memo first draft; tax managers' research summary; advisory analysts' interview summaries. Owner:
the director of knowledge, with a budget line and a seat at the operations committee. Operating model: a three-person
central team builds shared assets and measures; champions in each practice; the central team moves to advice once each
practice has an active champion group and a library reviewer. Learning time: two hours a week for the first
foundations and role modules, recorded on a non-chargeable code that counts toward targets (a firm decision; one law
firm credits far more). Expectations: each manager shows one real use a month and names one target workflow per team;
usage data is reported by group for measurement, not discipline. Time saved: the managing partner commits to redeploy
capacity to the advisory backlog and earlier audit planning; no role reductions are planned now, and this will be
revisited after outcome measures exist. Governance: tax client data waits for the ai-governance decision. Now: owner,
charter, data rule. Next: curriculum and champions. Later: library at scale, outcome measures.

## 10. Output

- **`enablement/program.md`**, section 2: the charter (fields in §1 and §7).
- **`enablement/measures.yaml`**: every charter measure defined, including at least one `embedded` and one `outcome`.
- Frontmatter: `step_completed: 2`, `next_step: 3`, `links` updated, `updated`.

## 11. Sources

- `BCG-ATWORK-2025`: *AI at Work: Momentum Builds, but Gaps Remain*, BCG, June 2025. https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain
- `BCG-VALUEGAP-2025`: *The Widening AI Value Gap*, BCG, October 2025. https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf
- `BETTERUP-2025`: *Workslop: The Hidden Cost of AI-Generated Busywork*, BetterUp Labs with Stanford Social Media Lab, September 2025. https://www.betterup.com/workslop
- `BLAW-KPMG-2025`: *KPMG Staff to Be Rated on AI Usage in Yearly Performance Reviews*, Bloomberg Law, 2025-10-31. https://news.bgov.com/health-law-and-business/kpmg-staff-to-be-rated-on-ai-usage-in-yearly-performance-reviews
- `BLAW-ROPES-2026`: *What Does It Take to Get Big Law Associates Excited About AI?*, Bloomberg Law, 2026-07-30. https://news.bgov.com/business-and-practice/what-does-it-take-to-get-big-law-associates-excited-about-ai
- `CIPD-2026`: *How a law firm introduced an AI legal assistant*, CIPD with Institute for the Future of Work, 2026-03-25. https://www.cipd.org/ae/knowledge/case-studies/ai-legal-assistant/
- `CPAPA-PWC-2026`: *PwC CEO Says Partners Who Resist AI "Have No Place at the Firm"*, CPA Practice Advisor citing the Financial Times, 2026-03-25. https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
- `DECRYPT-ACCENTURE-2026`: *Accenture Is Tracking Whether Employees Use AI, and Promotions Are on the Line*, Decrypt citing the Financial Times, 2026-02-19. https://decrypt.co/358616/accenture-tracking-employees-use-ai-promotions
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
