# Design the program (step 2)

Read this on entering step 2. It turns the baseline into a program charter: goals tied to business outcomes, an owner,
leader expectations, protected learning time, links to governance, and a measurement plan. Source keys in brackets
are listed in §6.

## 1. Goal and exit criteria

**Goal.** A program people can see is about their work and the firm's results, with someone accountable for it, and
the conditions that make sustained use likely: time, expectations, safe tools and a reason to share.

**Exit when all of these are true:** a goal tied to business outcomes (quality, turnaround, client responsiveness,
capacity, growth, risk) with one to three target workflows per role; an owner by role with budget and authority, and a
sponsor who uses AI visibly; the operating model and when the central team steps back (§3); learning time and whether
it counts toward billable or utilisation targets; leader and manager expectations in writing, saying whether usage
tracking is for measurement or policing (§4); what happens to time saved: redeploy, reduce or not yet decided (core
rule 2); governance links (approved tools, data rules, training before access, the intake gate for new uses); every
charter measure defined in `measures.yaml`; Now, Next and Later by dependency, each with an owner (core rule 9).

## 2. How to run it

1. **Start from the business problem:** "If this works, what will be different for clients and for the firm's results,
   not only for tool use?" Training alone rarely moves value: BCG finds 5% of 1,250 firms get value at scale and 60%
   little, and recommends 70% of effort on people and processes (its recommendation; vendor-published)
   [BCG-VALUEGAP-2025]. Individual gains need changes to how work is organized [MOLLICK-LAB-2025].
2. **Target workflows:** "For each role, which one workflow would make success obvious if people did it the new way?"
   "AI literacy" is not a goal.
3. **Owner:** "Who owns this, with what budget, and what can they decide?" In Section's survey, 53.2% said their
   organization had no Head of AI or were unsure; workers with a full-time Head of AI scored 42 against 33
   (correlational, vendor-published) [SECTION-2026].
4. **Learning time and expectations** (§4): "How much working time can people spend learning, and does it count?"
5. **Time saved:** "If people save time, what happens to it? Has anyone told staff?" Workers want clear answers on
   layoffs versus growth [MOLLICK-LAB-2025]; 15% of US employees said AI would likely eliminate their job within five
   years [GALLUP-2025]. If undecided, say so, and what the decision depends on.
6. **Governance:** cite `overlay/policy.md` and `overlay/tool-catalog.yaml` if they exist; if not, hand off to
   ai-governance before any curriculum covers client data. Ask what has been tried already, and what happened.
7. **Measures:** "What would the sponsor accept as proof?" Define them with the layers in `measure-adoption.md` §4,
   including at least one `embedded` and one `outcome`. Sequence Now, Next, Later, play back and write.

## 3. The operating model

**Leadership, Lab, Crowd:** leaders set direction and incentives, a small central "lab" turns discoveries into shared
assets and measures them, and the crowd finds the use cases [MOLLICK-LAB-2025]. In a firm: the sponsor and practice
leaders, an enablement or knowledge team, and the champions (step 4). In law firms the knowledge team often runs it
(`professional-services-knowledge-management-18`, grade B). Start central and move to an advisory role as capability
embeds (vendor guidance) [MSLEARN-COE-ND]; write the condition for stepping back ("each practice has an active
champion group and its own library reviewer"), not a date. Training before access is common in large firms and rare in
small ones: ILTA's 2026 survey of 508 law firms found 11% of firms under 50 lawyers and 72% of those over 700 require it
[ILTA-2026] (`professional-services-talent-learning-01`, grade B; `professional-services-work-production-22`, grade B).

## 4. Leader expectations, learning time and incentives

- **Expectations work when stated.** Only 7% of managers in Section's survey required AI use and tied it to reviews;
  employees whose managers expect and require use scored 1.5 times higher on proficiency (correlational) [SECTION-2026].
  22% of US employees said their organization had a clear plan; those who strongly agreed were three times as likely
  to feel very prepared [GALLUP-2025].
- **What firms report** (no outcome data): KPMG will assess staff on AI objectives in 2026 reviews, saying monitoring is
  not for policing [BLAW-KPMG-2025] (`professional-services-talent-learning-15`, grade B). Shoosmiths tied GBP 1 million
  of its bonus pool to one million prompts (`professional-services-talent-learning-16`, grade A): activity, not quality.
- **Write expectations by role**, as behaviours and outputs ("each manager demonstrates one real use a month and names
  one target workflow"), never as ratings of people. Performance reviews run through the firm's own HR process.
- **Decide the credit rule, even if it is no.** Ropes & Gray lets first-years put 20% of billable hours toward learning
  AI [BLAW-ROPES-2026] (`professional-services-talent-learning-03`, grade B); Polsinelli gives no billing credit
  [POLSINELLI-2026]; under ABA Formal Opinion 512 a lawyer may not bill a client for gaining AI competence unless the
  client asks (secondary) [LAWNEXT-2024]. Without protected time, expect weaker take-up: UK trial users said work
  capacity limited their participation [UKGDS-2025].
- **Pair training with a named workflow and a manager expectation:** regular use was sharply higher with at least five
  hours of training and in-person coaching (correlational) [BCG-ATWORK-2025].
- **Never tie a login or prompt target to reward without a quality check;** mandates without value produce "workslop"
  that shifts rework to colleagues [BETTERUP-2025]. Set only consequences the firm will apply.
- **Expect adoption gains before outcome gains:** in Danish data, employer encouragement nearly doubled take-up (47% to
  83%), yet users saved about 3% of hours, with no measurable effect on earnings or recorded hours (independent working
  paper) [HUMLUM-BFI-2025].

## 5. Worked example and output

*Illustrative (invented).* The accounting firm's director of knowledge owns it; a three-person central team steps
back once each practice has a champion group and a library reviewer. Learning time: two hours a week, counted toward
targets. Time saved goes to the advisory backlog; no role reductions now, revisited once outcome measures exist.

**Output:** `program.md` section 2 (the charter, fields in §1); every charter measure in `measures.yaml`; frontmatter
`step_completed: 2`, `next_step: 3`, `links` updated, `updated`.

## 6. Sources

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
- Archetype use cases (grades as recorded): `../../transformation-advisor/references/archetypes/index.md`.
