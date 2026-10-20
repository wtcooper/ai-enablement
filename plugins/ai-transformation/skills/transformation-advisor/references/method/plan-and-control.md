# Plan and control (phase 7)

Read this on entering phase 7. It tells you how to turn the chosen opportunities into actions, owners,
KPIs, a control plan and a review rhythm: next steps sequenced by dependency for a team (Now, Next, Later),
or workstreams, a value creation plan and cadence for a unit or organization. Steps are ordered by what they
depend on, not by calendar deadlines such as 30/60/90 days or 100 days; with AI, steps can move far faster
than those manual-era time boxes assume. Keys in brackets are listed in §9.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [What the plan contains](#3-what-the-plan-contains)
4. [Question bank](#4-question-bank)
5. [Expert moves](#5-expert-moves)
6. [Common traps](#6-common-traps)
7. [Worked example: the audit practice](#7-worked-example-the-audit-practice)
8. [Output](#8-output)
9. [Sources](#9-sources)

## 1. Goal and exit criteria

**Goal.** A plan that can start now and notices when it drifts. A pilot with no baseline, no owner and
no control plan is the typical stall; the plan exists to prevent it.

**Exit criteria.**

- Every chosen opportunity has a `next_step` (`action`, `owner`, `depends_on`), and at least one action can start now.
- Team scope: next steps sequenced by dependency (Now, Next, Later). Unit or organization scope: workstreams
  sequenced the same way, a value creation plan (the bridge from `business-case.md`) and a review cadence.
- A control plan for each live opportunity: metric, baseline, normal range, owner, review rhythm, and what
  happens when the metric moves out of range. Automated and delegated steps are included (§3.4).
- Three to five KPIs per opportunity, with a quality guardrail, and a way to report realized against expected value.
- Go/no-go and promotion rules written before each pilot starts.
- A people plan drawn from `people-and-change.md`: what staff are told and when, training by role, manager
  readiness, commitments and who owns them.
- The next journey stage named with three observable exit criteria, re-checked at the regular review.

## 2. How to run it

1. **Name the phase.** "Last phase: turning this into a plan with owners and a rhythm."
2. **Owners first.** For each opportunity ask: "Who will own this, and do they have the authority it needs?"
   Owners are named by role, or by name where the user offers it; never assess individuals.
3. **Start now.** Ask for one action per opportunity that needs nobody else's approval.
4. **Sequence** using the Prioritize order: foundations and quick wins first, big bets in shadow mode once
   their foundations are in place. Order steps by what they depend on, not by calendar deadlines.
5. **Write the control plan** with the user, one opportunity at a time (§3.3, §3.4).
6. **Set KPIs and the rhythm** (§3.5, §3.6). Ask: "Who will look at this, how often, and what will they do
   if it moves?"
7. **Add the people plan** (read `people-and-change.md` if not already done this session).
8. **Play back** the plan in one screen. Write the output (§8), mark the plan complete, and tell the user
   which files to share and how; sharing is their choice.

**Adapt by journey stage.** Curious: a one-page plan of two or three quick wins, a safe-use rule and a
check-in after the first real uses. Experimenting: one shared workflow with a baseline, owner and human check. Adopting:
control plans for production workflows; at most one or two bounded delegated workflows, in shadow mode.
Scaling: governance tiers, shared platform, an inventory of live agents, portfolio reviews. AI-native: add
pricing and service-model milestones and workforce redesign checkpoints.

## 3. What the plan contains

### 3.1 Team scope: Now, Next, Later

- **Now:** one to three actions, each needing no one else's approval (record baseline numbers, pick the
  pilot cases, draft the checklist, tell the team what is happening).
- **Next** (once the Now steps are done): foundations under way; quick wins live on a few cases with a
  comparison; go/no-go on the quick wins when their stopping condition is met; extend or stop.
- **Later** (once foundations are in place): first value review against the case; decide the next big bet;
  re-check the journey stage.

### 3.2 Unit or organization scope: workstreams, value creation plan, cadence

- **Workstreams:** the highest-conviction levers become workstreams, each with one owner, a target range
  and early wins, sequenced by dependency. Install the management system early: operating reviews, a KPI dashboard and
  clear decision rights [SBI-2025]. Name one person ultimately accountable [GT-2013]. In a 2013 survey,
  almost 90% of private-equity firms used a 100-day plan, often drafted during diligence (self-reported,
  dated) [GT-2013].
- **Value creation plan:** the bridge from `business-case.md`, one bar per initiative with owner, baseline,
  target range and the step it depends on, reconciled every quarter [BDEMERSON-2026].
- **Substitutes for missing forcing functions.** A unit leader lacks a private-equity owner's board control,
  equity incentives and exit date [ACHARYA-2009]. Build substitutes: a named sponsor, funded targets,
  incentives that reward the plan, and a regular review.
- **Units:** set `wave` and `status` for each child unit; plan later waves after the first wave's evidence.

### 3.3 Control plan for every live opportunity

For each opportunity write: metric · baseline · normal range · owner · review rhythm · response when out
of range. Plot metrics over time with limits before reacting to one bad week; a single point outside the
limits signals a cause worth finding, movement inside them is usually noise [NIST-CTRL-ND]. Include
automated steps: they drift unobserved when inputs or systems change [WIKI-DMAIC-2025; LEI-ETHINGTON-2026].
Automations need an owner and a maintenance budget: in a vendor-sponsored survey of RPA users, 69% had bots
break at least weekly [IDM-ROBOCORP-2022]. Stabilise and write down the standard way first; improvements
fade without one [LEI-KAIZEN-ND; GLOVER-2015].

### 3.4 Controls for automated and delegated steps

| Control | What to write down | Source |
|---|---|---|
| Autonomy tiers | Start in shadow mode (agent suggests, person acts), then supervised (person approves each action), then guided (person monitors and spot-checks). BCG keeps a fourth tier, full autonomy, for mature, low-risk work only. Write promotion thresholds; demote on a miss | [BCG-AGENTS-2025]; its example thresholds (such as 90% confidence) are illustrative |
| Human contacts | For each step: notify (tell), question (unblock me) or review (approve, edit, redirect) | [LANGCHAIN-AMBIENT-2025] |
| Escalation | A retry or failure threshold, and a list of high-risk actions (irreversible, sensitive, high-value) that always pause for a person | [OPENAI-GUIDE-2025] |
| Rubber-stamp watch | Track override rate and time to approve, per checkpoint and reviewer; audit whether review is real. No published benchmark exists for a healthy rate in knowledge work, so set the baseline in the parallel run | [IMDA-MGF-2026] |
| Accountable roles | Use-case owner, risk reviewer, the builder who monitors model changes, and reviewers who approve outputs | [IMDA-MGF-2026], PwC Singapore case |
| Evaluation set | Start with 20–50 real cases drawn from real failures, with reference answers written by the best reviewers; grade the end state, run several trials; keep capability tests separate from regression tests | [ANTHROPIC-EVALS-2026; MCKINSEY-1YR-2025] |
| Tracing | Step-level logs, not outcome-only, so a drop can be traced to data or reasoning | [MCKINSEY-1YR-2025] |
| Security | Remove one of: private data, untrusted content, outbound communication. Keep credentials out of reach of agent-generated code | [WILLISON-2025; ANTHROPIC-MANAGED-2026] |
| Change triggers | Re-run the evaluation set when the model, tool version or input systems change; design assumptions go stale as models change | [ANTHROPIC-EVALS-2026; ANTHROPIC-MANAGED-2026] |
| Governance tier | Light path for low-agency tools, impact assessment in the middle, architecture review for high agency | [IMDA-MGF-2026], MSD case |

For a quick governance screen, use ICAEW's top-level questions: strategy, policy, proportionate risk
management, human interaction points, monitoring and oversight, and staff skills [ICAEW-GOV-2026].

### 3.5 KPIs and benefit tracking

- Three to five KPIs per opportunity: leading and lagging, each efficiency KPI paired with a quality
  guardrail, plus cost per outcome where consumption matters.
- Report realized against expected value; counts of pilots, tools rolled out or use cases in production are
  activity, not impact [GARTNER-CFO1-2026]. Mark every benefit realized or expected.
- Adoption indicators the team can read monthly (advisor heuristic): share of people using it weekly,
  workflows in production, share with a measured baseline, time from pilot to production, reuse count.
- People indicators: quality of AI-assisted work, use by group, manager confidence, junior learning.
- Re-baseline when the model, prices or the process change.

### 3.6 Rhythm

| Scope | Weekly | Monthly | Quarterly | Mid-point |
|---|---|---|---|---|
| Team | 15-minute check while pilots run | Review with the sponsor: KPIs, go/no-go | Written value review against the case | Re-plan once the first items have landed |
| Unit or organization | Owner check-ins while the first workstreams start | Steering: portfolio KPIs, blockers, decisions | Written value review: what landed, slipped, changed [BDEMERSON-2026] | Reset: re-underwrite, fund winners, stop laggards [BAIN-MIDYEAR-2026] |

Interview data on 66 UK buyouts found 92% of sponsors in contact with the CEO weekly or more in the first
100 days, and 68% holding at least monthly board meetings (independent, dated) [ACHARYA-2009]. Re-check the
journey stage at each quarterly review: placements age fast.

## 4. Question bank

Tags: **[T]** team, **[U/O]** unit or organization. Core questions first.

**Core**
- Who will own each of these, and do they have the authority it needs? [T][U/O]
- What can you start right now without anyone else's approval? [T][U/O]
- What number would tell you this is slipping, and what would you do then? [T][U/O]
- Who will look at the results, how often, and in which meeting? [T][U/O]
- What will you tell your people, and when? [T][U/O]

**Follow-ups**
- Which cases are in the pilot, and what are the same kinds of cases doing the old way? [T]
- What has to be true to carry on, and what would make you stop? [T][U/O]
- Where will a person check the work, and what happens to the things they correct? [T]
- If the tool or the systems around it change, who notices and who re-tests? [T][U/O]
- What does it cost per month to run, and who sees that number? [U/O]
- Who is the visible sponsor, and what will they do that others can see? [U/O]
- When will you re-plan, and who decides to stop something? [U/O]
- How do the units report so the same benefit is not counted twice? [U/O] *Scaling*
- What three things would show you have reached the next stage? [T][U/O]

## 5. Expert moves

1. **Baseline before switch-on.** Record cycle time, touches, rework and errors on real cases before any tool
   runs [WIKI-DMAIC-2025; METR-2025].
2. **Test the measurement.** Have two people classify the same ten items as defect or not before counting
   defects (adapted from DMAIC measurement checks) [WIKI-DMAIC-2025].
3. **Staged rollout with a comparison.** Start small, one case set each, then widen; at Wipro, 8 of 10 first
   lean projects showed over 10% efficiency gain before the wider rollout [HBSWK-2007].
4. **Write the agent a job description**: duties, limits, escalation, good and bad examples, and a feedback
   loop from reviewers [MCKINSEY-1YR-2025].
5. **"Would you let it run without a check?"** Map the checkpoints before any delegation [BCG-GAP-2025].
6. **Go/no-go before the pilot**, with a defined review point [GARTNER-CSO-2026].
7. **Pre-mortem on controllable failure**: planning and resourcing, over-optimistic targets, poor buy-in.
   A 2025 survey of private-equity investors attributed 67% of initiative failures to controllable causes
   (self-reported) [SIMONK-2025].
8. **Plan to the next stage only**, with three observable exit criteria (advisor heuristic) [MITCISR-2024].
9. **Anchor visible early wins** and communicate them; they build credibility with the sponsor [SBI-2025].
10. **Shorten the review cycle when conditions shift**; the share of private-equity firms reviewing value
    creation plans every 3–6 months is expected to rise from 20% to 39% (self-reported intentions) [SIMONK-2025].

## 6. Common traps

| Trap | How the advisor avoids it |
|---|---|
| **Pilot with no baseline, owner or control plan** | Exit criteria require all three before go-live |
| **Artificial deadlines** | Sequence steps by dependency; avoid 30/60/90-day or 100-day time boxes carried over from manual-era planning |
| **A plan without an execution engine** | Owners with authority, a rhythm and a regular review; substitutes for missing forcing functions |
| **Activity reported as impact** | Realized against expected value; usage is a leading indicator only |
| **Rubber-stamp checkpoints** | Override rate and time to approve tracked; review audited |
| **Autonomy granted faster than evidence** | Written promotion thresholds; demote on a miss |
| **No AI KPIs** | In one survey, 36% of PE firms with an AI strategy had no AI milestones or KPIs (vendor-published) [FTI-PLAYS-2024]; every bar gets a KPI and an owner |
| **Set and forget automation** | Maintenance owner; re-test on model, tool or system change |
| **Stale plan** | Quarterly value review and a mid-point reset |
| **People plan missing** | Communication, training by role and commitments are part of the plan, not an appendix |

## 7. Worked example: the audit practice

Continuing the audit partner's practice (team-level plan; at unit scope the same content becomes the
first workstream). Illustrative.

- **Now:** the partner tells the practice what is being tried and why, in a "what we know, what
  we don't, what we commit to" note (`people-and-change.md`); the pilot lead pulls last season's matching
  hours from time records for five engagements; a senior manager drafts the review checklist for the three
  most common control types (F1).
- **Next:** F1 covers ten control types; evidence-request templates rewritten for the top chase reasons;
  `ct-07` runs on five engagements with a re-performed sample; roll-forward rule written into the
  methodology note; two-hour training for staff.
- **Then:** go/no-go on `ct-07` once the five engagements are done; extend to all engagements if met; `ct-10` starts on files that use F1.
- **Later:** value review against the case; choose the client for `ct-08`; re-check the stage against the
  Experimenting exit criteria in `onboarding.md` (one workflow with a named owner, a baseline, a designed human
  check and an approved tool).

| KPI (`ct-07`) | Baseline | Normal range | Owner | Rhythm | If out of range |
|---|---|---|---|---|---|
| Net hours per engagement | 50–80 h matching (last season) | At or above the low case | Pilot lead | Per engagement, then monthly | Find the cause: unreadable documents, training, or a control type to exclude |
| Re-performed matches that disagree | Set in the first five engagements | Within control limits; no serious miss | Engagement manager | Each engagement | Stop use for that document type; root cause before restarting |
| Review notes on evidence per file | Last season | No higher than last season | Quality reviewer | Monthly | Check checklist use and reviewer load |
| Files with complete tool documentation | — | 100% | Engagement manager | At file review | Fix before sign-off |

*Rhythm:* weekly 15-minute pilot check; monthly practice leadership review; quarterly value review;
re-perform a sample whenever the tool version changes. *Later:* if `ct-16` returns after the stage gate, it
starts in shadow mode with written thresholds for supervised and then monitored use.

## 8. Output

In `transformation-plan.md`, write a Plan section with: Now · Next · Later, each step with its owner and
what it depends on (team), or workstreams sequenced the same way, value creation plan and review cadence
(unit or organization) · control plan table per live
opportunity · KPIs and benefit tracking · people and change plan · next stage and its exit criteria ·
leadership summary (pasteable). In frontmatter set `phase_completed: 7`, `next_phase: null`, `updated`,
and `status: complete` (or `in-progress` while child units are still planning); keep `units` with `wave`
and `status`. In `opportunities.yaml`, every chosen item has `next_step: { action, owner, depends_on }` and its
`human_checkpoints` match the control plan. Close by naming the files to share and suggesting how.

## 9. Sources

- `ACHARYA-2009` — Acharya, Hahn, Kehoe, *Corporate governance and value creation: evidence from private equity* (66 UK deals), working paper, 2009-01-02. https://archive.nyu.edu/bitstream/2451/27878/4/Corporate%20governance%20and%20value%20creation%20-%20viral%20acharya.pdf
- `ANTHROPIC-EVALS-2026` — Anthropic, *Demystifying evals for AI agents*, vendor guide, 2026-01-09. https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- `ANTHROPIC-MANAGED-2026` — Anthropic, *Scaling managed agents*, vendor write-up, 2026-04-08. https://anthropic.com/engineering/managed-agents
- `BAIN-MIDYEAR-2026` — Bain & Company, *Private equity midyear report 2026*, consultancy, 2026-06-08. https://www.bain.com/insights/private-equity-midyear-report-2026/
- `BCG-AGENTS-2025` — BCG, *How agents are accelerating the next wave of AI value creation*, consultancy, 2025-12-15. https://www.bcg.com/publications/2025/agents-accelerate-next-wave-of-ai-value-creation
- `BCG-GAP-2025` — BCG, *The widening AI value gap*, consultancy survey, 2025-09. https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf
- `BDEMERSON-2026` — BD Emerson, *Private equity value creation plan*, practitioner article, 2026-08-16. https://www.bdemerson.com/article/private-equity-value-creation-plan
- `FTI-PLAYS-2024` — FTI Consulting, *AI in private equity: three plays*, consultancy, 2024-12-04 (updated 2026-05-22). https://www.fticonsulting.com/insights/articles/ai-private-equity-three-plays-driving-value-creation-2025
- `GARTNER-CFO1-2026` — Gartner, *CFOs must stop mistaking finance AI deployment for value creation*, analyst release, 2026-05-28. https://www.gartner.com/en/newsroom/press-releases/2026-05-28-gartner-says-cfos-must-stop-mistaking-finance-ai-deployment-for-value-creation
- `GARTNER-CSO-2026` — Gartner, *31% of chief sales officers cited difficulty proving ROI of AI-driven tools* (Q&A), analyst, 2026-05-19. https://www.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-survey-shows-thirty-one-percent-of-chief-sales-officers-cited-difficulty-proving-roi-of-ai-driven-tools-as-a-top-challenge-for-sales-objectives-in-two-thousand-twenty-si
- `GLOVER-2015` — Glover, Farris, Van Aken, *The relationship between continuous improvement and rapid improvement sustainability* (65 kaizen events, manufacturing), IJPR, 2015. https://ideas.repec.org/a/taf/tprsxx/v53y2015i13p4068-4086.html
- `GT-2013` — Grant Thornton with PitchBook, *What can be done in 100 days?*, consultancy survey, 2013-10. https://www.grantthornton.in/globalassets/1.-member-firms/india/assets/pdfs/pe-100-day-plan-survey-what-can-be-done.pdf
- `HBSWK-2007` — HBS Working Knowledge, *Bringing lean principles to service industries* (Wipro), 2007-10-22. https://www.library.hbs.edu/working-knowledge/bringing-lean-principles-to-service-industries
- `ICAEW-GOV-2026` — ICAEW, *AI governance: 10 essential questions for responsible adoption*, professional body, 2026-07-03. https://www.icaew.com/technical/technology/artificial-intelligence/managing-risks/ai-governance-10-essential-questions-for-responsible-adoption
- `IDM-ROBOCORP-2022` — IDM, *Broken bots challenge RPA users* (Robocorp-sponsored survey), 2022-07-08. https://idm.net.au/node/13957
- `IMDA-MGF-2026` — IMDA Singapore, *Model AI governance framework for agentic AI* v1.5, regulator guidance, 2026-05-20. https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
- `LANGCHAIN-AMBIENT-2025` — LangChain, *Introducing ambient agents*, vendor blog, 2025-01-14. https://www.langchain.com/blog/introducing-ambient-agents
- `LEI-ETHINGTON-2026` — Lean Enterprise Institute, *Automation, AI, and the risk of doing things efficiently that should not be done at all*, 2026-03-05. https://www.lean.org/the-lean-post/articles/automation-ai-and-the-risk-of-doing-things-efficiently-that-should-not-be-done-at-all/
- `LEI-KAIZEN-ND` — Lean Enterprise Institute, *Kaizen* (lexicon), updated 2023-02-02. https://www.lean.org/lexicon-terms/kaizen/
- `MCKINSEY-1YR-2025` — McKinsey, *One year of agentic AI: six lessons*, consultancy, 2025-09-12. https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work
- `METR-2025` — METR, *Impact of early-2025 AI on experienced open-source developer productivity*, RCT, 2025-07. https://arxiv.org/abs/2507.09089
- `MITCISR-2024` — Weill, Woerner, Sebastian (MIT CISR), *Building enterprise AI maturity*, research briefing, 2024-12. https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian
- `NIST-CTRL-ND` — NIST/SEMATECH, *What are control charts?* (e-Handbook 6.3.1), undated (accessed 2026-10-16). https://www.itl.nist.gov/div898/handbook/pmc/section3/pmc31.htm
- `OPENAI-GUIDE-2025` — OpenAI, *A practical guide to building agents*, vendor guide, 2025-04. https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- `SBI-2025` — SBI Growth, *100-day execution: the make-or-break period*, consultancy, 2025-10-20. https://sbigrowth.com/insights/100-day-execution-the-make-or-break-period-for-pe-value-creation
- `SIMONK-2025` — Simon-Kucher, *The operational era of value creation accelerates*, consultancy survey, 2025-09-22. https://www.simon-kucher.com/en/insights/private-equity-operational-era-value-creation-accelerates
- `WIKI-DMAIC-2025` — Wikipedia, *DMAIC*, reference, modified 2025-10-08. https://en.wikipedia.org/wiki/DMAIC
- `WILLISON-2025` — S. Willison, *The lethal trifecta for AI agents*, practitioner article, 2025-06-16. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/
