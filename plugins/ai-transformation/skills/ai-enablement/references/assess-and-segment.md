# Assess and segment (step 1)

Read this on entering step 1. It finds out who uses what, how deeply and why not, by practice and level, so the
program aims at the real gaps rather than the sponsor's impression. Source keys in brackets are listed in §11. Tags:
**[T]** team, **[U]** unit (practice, department), **[O]** organization.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Question bank](#3-question-bank)
4. [The depth ladder and default segments](#4-the-depth-ladder-and-default-segments)
5. [The fluency check](#5-the-fluency-check)
6. [Expert moves](#6-expert-moves)
7. [Checklist and decision rules](#7-checklist-and-decision-rules)
8. [Common traps](#8-common-traps)
9. [Worked example](#9-worked-example)
10. [Output](#10-output)
11. [Sources](#11-sources)

## 1. Goal and exit criteria

**Goal.** A baseline of adoption by depth, not by login, and a small set of segments, each with its main barrier
and a first move.

**Exit when all of these are true:**
- **Population and denominator:** everyone in scope, users or not, with the source of the count.
- **Usage relabelled by rung:** licensed, activated, active (with the window), weekly, embedded in a named workflow.
- **Hidden use:** an estimate of personal or unofficial tool use, and why people hide it.
- **Manager behaviour** by group: do managers expect use, show their own, and follow up?
- **Depth by group** on the four-rung ladder (§4), from sampled work or examples, not self-rating.
- **Fluency check** designed (and run, if the user can) with results by group only (§5).
- **Leader versus frontline gap** noted.
- **Five to seven segments**, each with groups, a size range, depth, main barrier, manager behaviour and a first move.
- **Baseline measures** written to `enablement/measures.yaml`.

## 2. How to run it

1. **Ask what numbers exist** (A1). Ask for aggregates by team, practice and level, never per-person exports (core
   rule 5). If the only figure is a licence count, say so and plan how to get a better one.
2. **Relabel each number** by the rung it measures before using it (A2). One vendor dashboard counts a user as
   "active" after one action in 28 days [MSLEARN-VIVA-2026].
3. **Ask about hidden use** (A3). Suggest an anonymous survey that rewards disclosure. Without it, "official tool
   logins" understate real use and misread the problem [MIT-NANDA-2025; MOLLICK-LAB-2025].
4. **Ask about managers** by role group (A5, A6): the last time a manager used AI in front of the team, and what they
   expect of people.
5. **Sample depth** (A7). Ask for two or three real examples per group: a repeatable workflow someone else could
   reuse, or something built for others.
6. **Design the fluency check** (§5) and agree how results stay anonymous.
7. **Place senior experts separately** (A9): their use and their stance vary independently.
8. **Build the segments** (§4), play them back, correct them, and write them.

Name the step and what comes next. Keep moving; skip what the user already knows.

## 3. Question bank

Core questions first. Ask one at a time, in this plain wording.

| # | Question | Scope | Notes |
|---|---|---|---|
| A1 | Last month, how many people used the tools weekly, how many monthly, how many only once? Can we see it by team and level? | [T][U][O] | Aggregates only. Licence counts are reach, not use |
| A2 | When your numbers say "active", what does that mean, and over what window? | [T][U][O] | Relabel before reporting |
| A3 | Who is using AI that you cannot see, on personal accounts or unofficial tools? Why might they keep quiet? | [T][U][O] | Hidden use and its incentives |
| A4 | For the groups not using it: is it no access, no use case, no time, no permission, a security worry, or no belief in it? | [T][U][O] | The main barrier per segment |
| A5 | When did each manager last use AI in front of their team? | [T][U] | Modelling. Ask for the last instance, not habits |
| A6 | What do managers expect of their people about AI, and what happens if nobody uses it? | [T][U] | Expectation and follow-up |
| A7 | Among regular users, who has a repeatable workflow someone else could reuse? Has anyone built something for others? | [T][U] | Depth: rungs 3 and 4 |
| A8 | How do leaders' and frontline staff's experience differ: access, training, tools that fit the work? | [U][O] | The two views of one program |
| A9 | Where do senior experts (partners, principals, specialists) sit: using it, skeptical, or avoiding it, and why? | [U] | Input to step 6 |
| A10 | How confident are people, by group? Which groups have been trained only on policy? | [U][O] | Targets coaching |
| A11 | What have people heard from leadership about AI and their jobs? | [T][U] | Fear as a barrier |
| A12 | Who are the quiet power users, and why are they quiet? | [T][U] | Future champions; hidden incentives |

## 4. The depth ladder and default segments

**Depth ladder** (`depth` in `measures.yaml`). Published fluency models use four levels with the same idea: Section's
Novice, Experimenter, Practitioner, Expert [SECTION-2026] and Zapier's Unacceptable, Capable, Adoptive,
Transformative [ZAPIER-2026].

| Rung | Id | What you see | The jump that matters |
|---|---|---|---|
| 1 | `not-using` | No use, or access never taken up | Finding one task worth doing |
| 2 | `one-off` | Occasional prompts, looking things up | From occasional prompts to a repeatable workflow |
| 3 | `repeatable` | A workflow the person runs the same way each time | Making it reusable by others |
| 4 | `builder` | Builds and shares workflows for colleagues | Feeding the library and teaching |

Most professionals sit on rung 2. In Section's June 2026 survey of 5,026 US knowledge workers, 5.5% met its
"proficient" bar, 73.5% were "experimenters" using AI for one-off tasks and 20.9% were novices (vendor-published;
the vendor tested skills hands-on) [SECTION-2026]. Gowling WLG tracks "adoption depth": how often and how naturally the
tool appears in regular work [HARVEY-GOWLING-2025].

**Default segments** (the advisor's working set; rename to fit the firm):

| Segment | Typical barrier | Typical first move |
|---|---|---|
| Builders and power users | None; often unrecognised | Champion network, library review (steps 4, 5) |
| Regular one-off users | No repeatable use case | Role workflows (step 3) |
| Occasional or lapsed | Use case or time | A named workflow plus manager expectation |
| Non-users blocked by access, permission or data rules | Access, security | Governance answer first, then training |
| Skeptics by belief or fear | Belief, fear | Step 6; honest role communication |
| Senior experts | Varies: status, time, accuracy | Step 6; private practice; peer demonstration |

## 5. The fluency check

Self-ratings overstate skill. Wharton's survey found 32% of respondents calling themselves "Expert" (a self-label)
[WHARTON-GBK-2025]; Section's hands-on tests found 21% wrote an effective prompt and 3.8% wrote workable assistant
instructions (vendor-published) [SECTION-2026].

**Design (illustrative, adapt per role):** one short task from the role's real work, sanitized.
1. **Frame:** write the instruction for the task, with context and the output wanted.
2. **Decompose:** split a complex version into steps with decision criteria [HARVEY-GOWLING-2025].
3. **Check:** find the error planted in a sample AI output, and say how it would be verified.

Score each part against a simple rubric (missing, partial, sound). **Results are reported by group only.** No
person's score is stored, shown to managers or used in any rating (core rule 1). Suppress groups below the minimum
size the firm's HR or privacy lead sets. Make it voluntary or anonymous, and say so in the invitation.

## 6. Expert moves

| Move | When | What it reveals |
|---|---|---|
| Ask for the weekly-versus-monthly split by team and level, not the licence count | Baseline | Whether "adopted" means a handful of heavy users. Lewis Silkin reports two-thirds of users engage monthly and about half of those weekly (firm-reported, definitions not given) [HARVEY-CHAMPIONS-2026] |
| Re-label every headline number by rung before it goes in a report | A sponsor quotes a usage figure | Which rung the number measures [SECTION-2026; ZAPIER-2026] |
| Test with a hands-on task, not a self-rating | Segmenting | The gap between confidence and capability (§5) |
| Ask who is using AI that you cannot see, and why they would hide it | Kickoff | Hidden use and the incentive problem. MIT NANDA found staff at over 90% of surveyed companies using personal AI tools while about 40% of companies had bought an official subscription (preliminary, anonymized) [MIT-NANDA-2025]; Mollick traces the same pattern to unclear incentives [MOLLICK-LAB-2025] |
| Interview managers before designing training | Any scope | Whether expectations and modelling exist. Only 21.3% of managers had demonstrated AI use to their team in the past 30 days, and 65% set no expectations or did not hold people accountable (vendor-published) [SECTION-2026] |
| Survey frontline and mid-level separately from leaders | Leader-sponsored programs | A distorted baseline. Executives were far more likely than individual contributors to call AI widely integrated (57% versus 18%) [SECTION-2026]; frontline regular use stalled at 51% while more than three quarters of leaders and managers used it several times a week (survey) [BCG-ATWORK-2025] |
| Ask confidence and familiarity by group, then target the low-confidence groups | Targeting | Where coaching pays. The UK cross-government trial found confidence and familiarity correlated with time saved [UKGDS-2025] |
| Ask non-users for their reasons and keep them in the denominator | Baseline | Barriers that training will not fix. In HMRC's evaluation, 46% of non-users cited security and data privacy concerns [HMRC-2026] |
| Check usage by grade, location and, where the firm already reports it in aggregate, gender | Equity | Uneven take-up. In Danish data the gender gap in chatbot adoption was 11.9 points, falling to 5 points where employers encouraged use (independent working paper) [HUMLUM-BFI-2025] |
| Segment by task fit and experience, not only by enthusiasm | Planning the curriculum | Who gains most. In a call-centre study gains were 34% for novices and minimal for experienced staff (adjacent process) [NBER-BRYNJOLFSSON-2023]; consultants gained inside AI's capability and not uniformly outside it [HBS-JAGGED-2023] |

## 7. Checklist and decision rules

**Checklist**
- [ ] Active counts by team, level and location; weekly, monthly, once; window stated.
- [ ] Unofficial use asked about, with safe disclosure.
- [ ] Managers interviewed or surveyed by role group.
- [ ] Depth sampled from real examples.
- [ ] Senior experts placed, with reasons.
- [ ] Fluency check designed; anonymity agreed.
- [ ] Non-users' reasons captured.

**Decision rules** (working rules drawn from the sources; tell the user they are rules of thumb)
- If official-tool use is under half but surveyed personal use is higher, treat it as an access and trust problem
  first, not a skills problem [MIT-NANDA-2025; MOLLICK-LAB-2025].
- If the sponsor's view and the frontline view differ widely (one working threshold: 25 points on use or on "AI is
  widely integrated"), treat the leadership view as unreliable and re-baseline [SECTION-2026; BCG-ATWORK-2025].
- Never report a login or licence metric alone; pair it with at least one depth indicator.
- Treat an unknown group as unmapped, not as zero.
- Report groups only; suppress small groups.

## 8. Common traps

| Trap | Why it happens | How to avoid it |
|---|---|---|
| Counting licences or logins as adoption | Easy to collect | Report the depth ladder; add workflow and outcome measures later [MSLEARN-VIVA-2026] |
| Designing from the leaders' view | Sponsors are the heaviest users | Separate frontline and mid-level views [BCG-ATWORK-2025] |
| A baseline of official logins only | Hidden use | Ask about personal tools safely [MIT-NANDA-2025] |
| Self-rated skill | Cheap to ask | Hands-on check, reported by group (§5) |
| Turning the baseline into a league table | Pressure to name names | Groups only; never per-person (core rule 1) |
| Asking for per-person exports | Habit | Ask for aggregates (core rule 5) |

## 9. Worked example

*Illustrative; the firm and figures are invented.* A 400-person accounting firm with audit, tax and advisory
practices. The COO opens with "78% adoption". Relabelled, that is the share activated in a 28-day window. Weekly use
is about a third of the population, concentrated in advisory and among managers. An anonymous survey finds tax
seniors using personal assistants for research summaries because the firm's tool is not approved for client data;
private client staff do not use it at all for the same reason. Two of six audit managers have shown the tool to their
teams; none has said what they expect. The fluency check (a sanitized engagement memo) shows most groups frame tasks
adequately and few check output well.

Segments: builders in advisory (a handful, unrecognised); regular one-off users across audit; tax seniors with hidden
use (barrier: permission); private client blocked by data rules (barrier: security); skeptical audit partners
(barrier: accuracy and status). First moves: a data rule from governance before any tax training (hand off to
ai-governance); audit managers briefed first; advisory builders invited to the champion network.

## 10. Output

- **`enablement/program.md`**, section 1: population, relabelled usage, hidden use, manager behaviour, fluency check
  results by group, the leader and frontline gap, and the segment table.
- **`enablement/measures.yaml`**: `population`, `segments`, and baseline `reach`, `activity` and `depth` measures
  (schema `schemas/measures.md`).
- Frontmatter: `step_completed: 1`, `next_step: 2`, `updated`.

## 11. Sources

- `BCG-ATWORK-2025`: *AI at Work: Momentum Builds, but Gaps Remain*, BCG, June 2025. https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain
- `HARVEY-CHAMPIONS-2026`: *Harvey Power Users: The Champions Network* (Lewis Silkin interview), Harvey blog, vendor-published, 2026-06-02. https://www.harvey.ai/blog/harvey-power-users-the-champions-network
- `HARVEY-GOWLING-2025`: *Al Hounsell on Driving Legal Transformation That Lasts* (Gowling WLG interview), Harvey blog, vendor-published, 2025-10-30. https://www.harvey.ai/blog/al-hounsell-on-driving-legal-transformation-that-lasts
- `HBS-JAGGED-2023`: *Navigating the Jagged Technological Frontier* (summary), Harvard D^3 Institute with BCG, 2023-09-21. https://d3.harvard.edu/navigating-the-jagged-technological-frontier/
- `HMRC-2026`: *Evaluating the impact of Microsoft Copilot in HMRC*, HM Revenue and Customs, 2026-07-09. https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot/evaluating-the-impact-of-microsoft-copilot-in-hmrc
- `HUMLUM-BFI-2025`: *Large Language Models, Small Labor Market Effects* (WP 2025-56), Humlum and Vestergaard, Becker Friedman Institute, 2025-05-09. https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf
- `MIT-NANDA-2025`: *The GenAI Divide: State of AI in Business 2025* (preliminary), MIT NANDA, July 2025. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `MOLLICK-LAB-2025`: *Making AI Work: Leadership, Lab, and Crowd*, Ethan Mollick, One Useful Thing, 2025-05-22. https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- `MSLEARN-VIVA-2026`: *Microsoft Copilot Dashboard in Viva Insights*, Microsoft Learn, product documentation, undated (mentions a February 2026 fix). https://learn.microsoft.com/en-us/viva/insights/org-team-insights/copilot-dashboard
- `NBER-BRYNJOLFSSON-2023`: *Generative AI at Work* (NBER WP 31161), Brynjolfsson, Li, Raymond, April 2023, revised November 2023. https://www.nber.org/system/files/working_papers/w31161/w31161.pdf
- `SECTION-2026`: *The AI Proficiency Report*, Section (AI training company), June 2026. https://www.sectionai.com/ai/the-ai-proficiency-report
- `UKGDS-2025`: *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, UK Government Digital Service, June 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf
- `WHARTON-GBK-2025`: *Accountable Acceleration: Gen AI Fast-Tracks into the Enterprise*, Wharton Human-AI Research and GBK Collective, October 2025. https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf
- `ZAPIER-2026`: *How to measure your AI fluency, and move to the next level*, Zapier, 2026-02-02. https://zapier.com/blog/ai-fluency/
