# Assess and segment (step 1)

Read this on entering step 1. It finds out who uses what, how deeply and why not, by practice and level, so the
program aims at the real gaps rather than the sponsor's impression. Source keys in brackets are listed in §6.

## 1. Goal and exit criteria

**Goal.** A baseline of adoption by depth, not by login, and five to seven segments, each with its main barrier and a
first move.

**Exit when all of these are true:** population and denominator (everyone in scope, users or not, with the source of
the count); usage relabelled by rung (licensed, activated, active with the window, weekly, embedded); an estimate of
hidden use and why people hide it; manager behaviour by group; depth by group on the ladder (§3), from sampled work,
not self-rating; a fluency check designed (and run, if the user can) with results by group only (§4); the leader
versus frontline gap; segments, each with groups, a size range, depth, main barrier, manager behaviour and a first
move; baseline measures in `enablement/measures.yaml`.

## 2. How to run it

One question at a time, in this order; ask for aggregates by team, practice and level, never per-person exports.

1. **What numbers exist?** "Last month, how many people used the tools weekly, how many monthly, how many only once,
   by team and level?" If the only figure is a licence count, say so and plan how to get a better one.
2. **Relabel each number** by rung: "When your numbers say 'active', what does that mean, and over what window?" One
   vendor dashboard counts a user as active after one action in 28 days [MSLEARN-VIVA-2026].
3. **Hidden use:** "Who is using AI that you cannot see, and why might they keep quiet?" Suggest an anonymous survey
   that rewards disclosure.
4. **Barriers:** "For the groups not using it: no access, no use case, no time, no permission, a security worry, or no
   belief?" Keep non-users in the denominator; treat an unknown group as unmapped, not zero.
5. **Managers:** "When did each manager last use AI in front of their team, and what do they expect of people?"
6. **Depth:** "Among regular users, who has a repeatable workflow someone else could reuse?" Ask for two or three real
   examples per group.
7. **Senior experts** separately: their use and their stance vary independently (input to step 6). Ask how leaders'
   and frontline staff's experience differ, and what people have heard about AI and their jobs.
8. **Design the fluency check** (§4), then **build the segments** (§3), play them back, correct them and write them.

## 3. The depth ladder and default segments

**Depth ladder** (`depth` in `measures.yaml`), built on published four-level fluency models such as Section's
[SECTION-2026]: 1 `not-using` (no use, or access never taken up); 2 `one-off` (occasional prompts); 3 `repeatable` (a
workflow the person runs the same way each time); 4 `builder` (builds and shares workflows for colleagues). The jump
that matters most is from occasional prompts to a repeatable workflow. Most knowledge workers sit on rung 2: in
Section's June 2026 survey of 5,026 US knowledge workers, 5.5% met its "proficient" bar, 73.5% were "experimenters"
and 20.9% were novices (vendor-published; skills tested hands-on) [SECTION-2026].

| Default segment (rename to fit) | Typical barrier | Typical first move |
|---|---|---|
| Builders and power users | None; often unrecognised | Champion network, library review (steps 4, 5) |
| Regular one-off users | No repeatable use case | Role workflows (step 3) |
| Occasional or lapsed | Use case or time | A named workflow plus manager expectation |
| Blocked by access, permission or data rules | Access, security | Governance answer first, then training |
| Skeptics by belief or fear | Belief, fear | Step 6; honest role communication |
| Senior experts | Status, time, accuracy | Step 6; private practice; peer demonstration |

## 4. The fluency check

Self-ratings overstate skill: 32% of about 800 senior decision-makers at large US companies called themselves
"Expert" [WHARTON-GBK-2025], while Section's hands-on tests found 21% of US knowledge workers wrote an effective
prompt (vendor-published) [SECTION-2026]. **Design (illustrative):** one short, sanitized task from the role's real
work: frame the instruction; split a harder version into steps; find the error planted in a sample AI output and say
how to verify it. Score each part missing, partial or sound. Results by group only; suppress groups below the minimum
size the firm's HR or privacy lead sets; voluntary or anonymous, and say so.

## 5. Evidence, rules of thumb and output

Tell the user these are working rules drawn from the sources.
- **Hidden use is common.** MIT NANDA (52 organizations interviewed, 153 senior leaders surveyed; preliminary) found
  workers at over 90% of companies using personal AI tools, while only 40% of companies had bought an official
  subscription [MIT-NANDA-2025]; Mollick traces this to unclear incentives [MOLLICK-LAB-2025]. If official use is
  under half but personal use is higher, treat it as an access and trust problem first, not a skills problem.
- **Managers rarely model use.** In Section's survey, 21.3% of managers had shown their own AI use to their team in
  the past 30 days, and 65% set no expectations or encouraged use without holding people accountable
  (vendor-published) [SECTION-2026].
- **Leaders see a different program.** Executives were far more likely than individual contributors to call AI widely
  integrated (57% versus 18%) [SECTION-2026]; in BCG's survey of more than 10,600 employees, frontline regular use
  stalled at 51% while over three quarters of leaders and managers used it several times a week [BCG-ATWORK-2025]. If
  the views differ widely (one working threshold: 25 points), re-baseline from the frontline.
- **Confidence and reasons.** The UK cross-government trial found confidence correlated with time saved [UKGDS-2025];
  in HMRC's trial, 46% of non-users named security and data privacy as the main reason [HMRC-2026].
- **Traps:** logins reported as adoption; designing from the leaders' view; self-rated skill; a league table.

*Illustrative example (invented).* A 400-person accounting firm's "78% adoption" is the share activated in 28 days;
weekly use is about a third. Tax seniors use personal assistants because the firm's tool is not approved for client
data (barrier: permission), so a data rule from ai-governance comes before any tax training.

**Output:** `program.md` section 1; `enablement/measures.yaml` with `population`, `segments` and baseline `reach`,
`activity` and `depth` measures; frontmatter `step_completed: 1`, `next_step: 2`, `updated`.

## 6. Sources

- `BCG-ATWORK-2025`: *AI at Work: Momentum Builds, but Gaps Remain*, BCG, June 2025. https://www.bcg.com/publications/2025/ai-at-work-momentum-builds-but-gaps-remain
- `HMRC-2026`: *Evaluating the impact of Microsoft Copilot in HMRC*, HM Revenue and Customs, 2026-07-09. https://www.gov.uk/government/publications/evaluation-report-phase-3-trial-of-microsoft-copilot/evaluating-the-impact-of-microsoft-copilot-in-hmrc
- `MIT-NANDA-2025`: *The GenAI Divide: State of AI in Business 2025* (preliminary), MIT NANDA, July 2025. https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- `MOLLICK-LAB-2025`: *Making AI Work: Leadership, Lab, and Crowd*, Ethan Mollick, One Useful Thing, 2025-05-22. https://www.oneusefulthing.org/p/making-ai-work-leadership-lab-and
- `MSLEARN-VIVA-2026`: *Microsoft Copilot Dashboard in Viva Insights*, Microsoft Learn, product documentation, undated (mentions a February 2026 fix). https://learn.microsoft.com/en-us/viva/insights/org-team-insights/copilot-dashboard
- `SECTION-2026`: *The AI Proficiency Report*, Section (AI training company), June 2026. https://www.sectionai.com/ai/the-ai-proficiency-report
- `UKGDS-2025`: *Microsoft 365 Copilot Experiment: Cross-Government Findings Report*, UK Government Digital Service, June 2025. https://assets.publishing.service.gov.uk/media/683db42bd23a62e5d32680d0/M365_Copilot_Experiment_Findings_Report.pdf
- `WHARTON-GBK-2025`: *Accountable Acceleration: Gen AI Fast-Tracks into the Enterprise*, Wharton Human-AI Research and GBK Collective, October 2025. https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf
