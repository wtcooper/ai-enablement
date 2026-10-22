# Curriculum by role and level (step 3)

Read this on entering step 3. It builds learning around the real work of each role and level: hands-on practice,
task framing, decomposition and checking, with tracks for reviewers, builders, leaders and juniors. Source keys in
brackets are listed in §6.

## 1. Goal and exit criteria

**Goal.** Each role learns to do its own target workflows with AI, to check the output, and to know where AI is weak,
with practice on real (sanitized) work rather than a tool tour.

**Exit when all of these are true:** a role map (roles and levels, grouped where the work is alike); per role, three
tasks where AI helps and three where it does not, with examples from the user's own work; tiers chosen and modules
written on the module card (§3); reviewer content (what approvers must check in AI-assisted work); a junior route
(§4); an access rule (whether training comes before access) agreed with governance; refresh triggers (tool, model or
policy change); delivery order by segment and dependency, low-confidence and blocked groups first where data rules
allow.

## 2. How to run it

1. **Start from the segments and target workflows** of steps 1 and 2.
2. **Map roles:** "Which roles and levels are in scope, and where is the work alike enough to share a module?"
3. **Helps and does not help:** "For each role, what are three tasks where AI is most useful and three where it is
   not? Can you show one from your own files?" AI helps inside its capability and not uniformly outside it, even
   within one workflow [HBS-JAGGED-2023]; teach both sides.
4. **Pick tiers** (§3) and draft one module per target workflow. Ask who must learn to build shared workflows, not
   only use them, and how much time and which formats fit the credit rule from step 2.
5. **Reviewers:** "What does a reviewer need to check in AI-assisted work, and have they been taught?" Use the
   archetype's guardrails and any overlay policy.
6. **Juniors:** "What does a first-year need to learn now that AI does tasks that used to teach the craft?" (§4).
7. **Access:** "Is training required before access, and does that differ by risk?" If no policy exists, hand off to
   ai-governance. No module about client data until the data rule exists.
8. **Order delivery** by segment and dependency, and write the curriculum.

## 3. Tiers and module design

| Tier | Who | Content |
|---|---|---|
| Foundations | Everyone | Safe use and data rules from the overlay; a low-stakes first exercise; framing a task; checking output; where AI is weak |
| Role workflows | By role and level | The target workflows, practised on sanitized real work, with the role's checks |
| Builder | Champions, power users | Packaging a workflow for others, testing it, writing the library entry (step 5) |
| Leader and manager | Partners, managers | Modelling use, setting expectations, reviewing AI-assisted work, talking about roles honestly |

**Module card** (in `program.md`): role; tier; tasks in scope; an example from the user's own work (sanitized);
practice exercise; verification step; risk rule; time required; hands-on check; follow-up (clinic or champion).

**What to teach:** task framing, decomposition and checking, not prompt tricks. Mollick argues prompt techniques
matter less as models infer intent better [MOLLICK-LAB-2025], while Section found only 21% of US knowledge workers
wrote an effective prompt [SECTION-2026]; framing and checking are useful either way. **By role:** an audit
regulator's staff paper separates what preparers, reviewers and engagement partners need, and the UK audit regulator
says training should cover reviewing and overseeing a tool, automation bias and the tool's known weaknesses (both in
`assurance-quality-management-10`, grade B).

## 4. Juniors and the apprenticeship

Junior tasks often serve production and training at once; design a replacement learning route before the tasks go,
using the junior-task audit and explain-back in `../../transformation-advisor/references/method/people-and-change.md`
§6. Reviewers question juniors on the reasoning behind AI-assisted results (`professional-services-talent-learning-09`,
grade C); Duane Morris holds that a first draft is never an appropriate final submission
(`professional-services-talent-learning-02`, grade B). 43% of leaders in Wharton and GBK's survey warn of skill atrophy
without role design, coaching and practice time [WHARTON-GBK-2025]. Juniors may gain more: in a call-centre study gains
were 34% for novices and minimal for experienced staff (adjacent process) [NBER-BRYNJOLFSSON-2023].

## 5. Rules of thumb, example and output

- **Role-specific cases, not compliance-only content.** In Section's survey, 15% of those trained got only safety and
  compliance training (vendor-published) [SECTION-2026]; HMRC lists the need for practical, tailored training and time
  to learn [HMRC-2026].
- **A safe, low-stakes first phase:** Gowling WLG describes space for "silly poems and cats" before professional use
  [HARVEY-GOWLING-2025]. **Short, varied formats:** one law firm named lunch-and-learns, short videos and one-page
  handouts among its most successful [LAW360-2025]. **Training before access where risk warrants:** a CIPD case firm
  required it [CIPD-2026].
- **Target low-confidence groups early** (working rule: the UK trial's correlation between confidence and time saved
  does not show coaching causes savings) [UKGDS-2025].
- **Assess with a hands-on task**, reported by group (step 1 §4). Completion is reach, not skill.

*Illustrative (invented).* The tax practice: *Foundations* (90 minutes, all staff); *Seniors: research summary*
(verification: open every cited source; hands-on check: find the planted wrong citation); *Managers: reviewing
AI-assisted work*; *Builder* (champions package the notice-reply procedure for step 5); *Partners* (a private session).

**Output:** `program.md` section 3 (role map, helps and does-not-help lists, tiers, module table, reviewer track,
junior route, access rule, refresh triggers, delivery order); any module measures in `measures.yaml` as `reach` or
`depth`; frontmatter `step_completed: 3`, `next_step: 4`, `updated`.

## 6. Sources

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
- Archetype use cases (grades as recorded): `../../transformation-advisor/references/archetypes/index.md`.
