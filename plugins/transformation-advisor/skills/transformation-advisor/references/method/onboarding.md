# Onboarding (phase 0)

Read this when no plan exists, or when the user asks to redo their profile. It tells you how to build the profile in
five to ten questions, detect the archetype, place the journey stage by evidence, and adapt the path. Source keys in
brackets are listed in §11. Tags: **[T]** individual or team scope, **[U/O]** unit or organization scope, **[all]** any scope.

## Contents

1. [Goal and exit criteria](#1-goal-and-exit-criteria)
2. [How to run it](#2-how-to-run-it)
3. [Profile questions](#3-profile-questions)
4. [Archetype detection](#4-archetype-detection)
5. [Journey stage: markers and diagnosis](#5-journey-stage-markers-and-diagnosis)
6. [Adapting the path](#6-adapting-the-path)
7. [Expert moves](#7-expert-moves)
8. [Common traps](#8-common-traps)
9. [Worked example](#9-worked-example)
10. [Output](#10-output)
11. [Sources](#11-sources)

## 1. Goal and exit criteria

**Goal.** Know who you are talking to, what kind of business it is, how far along it is with AI, why it wants to act
now, what limits apply, and what the user wants from the session. Then choose the path.

**Exit when all of these are true:**
- Role and scope level are known (individual, team, function, business unit, organization).
- An archetype and one to three focus modules are chosen, or the no-match route (§4) is agreed.
- A journey stage is placed **from observed markers**, per scope where they differ, with the binding constraint named.
- Goals, constraints, tools and the session goal are recorded in the user's words.
- The user has confirmed the played-back profile, and has had the once-per-session confidentiality reminder.
- The adapted path (§6) is stated: which phases go deep, which stay light, and what comes next.

## 2. How to run it

1. **Open with a short primer.** Say what the session is for, that answers shape the plan, and that everything can be
   corrected later. Ask what would make the conversation worthwhile [NNG-FLAHERTY-2020].
2. **Give the confidentiality reminder once:** no client-confidential data and no personal information beyond names and roles.
3. **Ask one question at a time**, broad to specific, and let each answer choose the next question. Sensitive topics
   (worries, unapproved tool use) come after rapport, not first [BISPO-2022]. Skip anything already known.
4. **Detect the archetype** from what the business delivers and how it is paid (§4). Load only that archetype's
   `ARCHETYPE.md` and its stage markers.
5. **Place the stage by evidence** (§5): ask to see or count, not to self-rate. Use two or three boundary probes, not all.
6. **Bring evidence in early.** Once the archetype is known, mention one real example from it, with its evidence grade.
7. **Play the profile back** in a few lines, including the stage and the reason for it. Ask what is wrong. Correct it.
8. **Write the profile** to the plan (§10), state the adapted path, and name the next phase.

Keep it to about 10–15 minutes. Short sessions keep people engaged; AI-led research interviews of this length worked
in practice [ANTHROPIC-INTERVIEWER-2025]. If the user wants speed, ask the five starred questions in §3 and infer the rest.

## 3. Profile questions

Ask in plain words. Core questions are starred; use the others when an answer is unclear.

| Profile element | Questions | Scope |
|---|---|---|
| Role and scope | ★ What is your role, and what are you responsible for: your own work, a team, a function, a business unit or the whole organization? | [all] |
| | Roughly how many people work in that scope, and doing what kind of work? | [U/O] |
| Archetype and modules | ★ What does your part of the business deliver, and to whom? | [all] |
| | How is that work paid for: by the hour, a fixed fee, a subscription, or an internal budget? | [all] |
| | Which parts of that work are you closest to, or most worried about? | [all] |
| Journey stage | ★ In the last two weeks, who in your scope used AI on real work, and for what? Could you show me one example? | [all] |
| | See §5 for the boundary probes. | |
| Goals and pressures | ★ Why look at AI now? What is pushing you: margins, growth, staff shortages, quality, clients, competitors or regulation? | [all] |
| | If this goes well, what will be different in a year, for your clients and for your people? | [all] |
| Constraints | What must not change, or must be protected: rules, client commitments, independence, confidentiality, data limits? | [all] |
| | What are you allowed and not allowed to do with AI today, and does everyone know? | [all] |
| Tools and data | Which AI tools can people use today, and which systems hold the work itself? | [all] |
| | Do people also use tools that have not been approved? Many do, and there is no wrong answer. | [all] |
| Session goal | ★ What would make this session worth your time: a few quick wins, a full plan, a case for leadership, or a look at what is possible? | [all] |
| Worries | Is anything about looking at AI here worrying you or your team? | [all] |

**Why these words.** Asking about unapproved use with normalising language matters: about a third of professionals in
one vendor survey used AI their organization had not approved [TR-2026], 78% of AI users in another brought their own
tools [MSFT-WTI-2024], and 69% of interviewees in a third mentioned stigma about using AI at work
[ANTHROPIC-INTERVIEWER-2025]. All three are vendor-published.

## 4. Archetype detection

1. **Match on the value chain, not the job title.** Use what the business delivers, to whom, how it is paid and who
   regulates it. Read `archetypes/index.md` for recognition cues, then confirm with the user.
2. **v1 archetypes.** Professional services is the base. Assurance and tax extend it. In-house internal audit teams
   use assurance; corporate tax departments use tax. Consulting teams use professional services, the function cards
   and, where one exists, their client's archetype.
3. **Pick focus modules** from the areas the user is closest to or worried about. Load only those module files.
4. **An overlay archetype wins.** If `overlay/archetypes/` has a match, use it (overlay > plan settings > archetype > backbone).
5. **No match.** Use the closest base archetype plus the relevant function cards. If the user agrees and web access
   exists, offer on-the-spot research with the `research-archetype` brief. Its output is labelled **provisional**.
   Without agreement or web access, say plainly that examples will be more generic.

## 5. Journey stage: markers and diagnosis

**Principles.**
- A stage is a way to choose questions and emphasis, not a score or a verdict. Five-level models are the most common
  design in the literature, with no standard terminology [SADIQ-2021]; no study found follows the same firms through the stages.
- **Place by evidence.** Self-placement runs high: 7% of leaders against 26% of individual contributors said they did
  not know whether their organization had implemented AI (independent poll) [GALLUP-2025].
- **Place each scope.** A person can be ahead of their team, and a team ahead of its firm. Plan against the weakest
  dimension that matters (strategy, data, governance, skills, ownership) [DELOITTE-STATEAI-2026].
- **Spend the most effort on the Experimenting-to-Adopting boundary.** Every model reviewed puts its sharpest break at
  the move from individual or pilot use to shared, owned, measured workflows [MITCISR-2024; BCG-GAP-2025; SAGE-2026].
- **Treat AI-native claims with scepticism.** Top tiers are small: 5% in BCG's study, 7% in MIT CISR's [BCG-GAP-2025; MITCISR-2024].
- Use the archetype's `ARCHETYPE.md` for field-specific markers (for example, what Adopting looks like in assurance).

### Stage cards

| Stage | Markers you can check | Typical blockers | Ready for the next stage when |
|---|---|---|---|
| **Curious** | Informal, individual use on consumer tools for emails and summaries; no shared workflow; no owner or budget; no policy, or only a ban; unapproved use likely [SAGE-2026; MIT-NANDA-2025] | Unclear fit to the work; confidentiality and accuracy worries; no policy or training [IRGLOBAL-2025; LITIFY-2026] | A few named people use AI weekly on real work; an acceptable-use rule exists; one quick win has been shown to peers |
| **Experimenting** | Several people or pilots, uncoordinated, mixed tools; licences issued on request; gains felt by individuals but no business measure moves; pilots stopped without lessons [ILTA-2025; LITIFY-2026] | Pilots that do not convert; tools outside the workflow; freed time absorbed unseen [MIT-NANDA-2025; SAGE-2026] | One workflow has a named owner, a baseline, a designed human check and an approved tool |
| **Adopting** | AI inside the system where work is recorded; a few owned workflows with measures; policy, training and an approved-tool list; financial return not yet proven [SAGE-2026; LITIFY-2026; MITCISR-2024] | Data quality; integration; measuring value; review burden; spreading across too many workflows [BCG-GAP-2025] | Two or more workflows in production; the second reused a part of the first; one place records value across workflows; a named central owner |
| **Scaling** | Shared platform and reusable components; value tracked across a portfolio; dedicated AI leader; shared business and technology ownership [MITCISR-2024; BCG-GAP-2025] | Operating model and decision rights; skills and training; governance for autonomy; data debt [BCG-GAP-2025; DELOITTE-STATEAI-2026] | Value is measured at P&L level, and leaders are asking what to sell, to whom and at what price |
| **AI-native** | Pricing, services or the cost base have changed because of AI; new services sold that were not possible before; work redesigned end to end with agents under oversight [MITCISR-2024; SAGE-2026] | Time-based pricing; advisory skills; professional accountability; skill atrophy | Re-diagnose each review; stages age quickly [BCG-GAP-2025] |

"Ready when" criteria are working heuristics from the maturity research, not tested thresholds.

### Delegation and the Adopting stage (decision)

The spec lists "the first delegated (agentic) workflows" under Adopting. The evidence puts broad delegation later:
BCG treats agents as the step after data foundations, scaled capabilities and clear governance [BCG-GAP-2025];
about one in five companies has a mature governance model for autonomous agents [DELOITTE-STATEAI-2026]; and no more
than 10% of McKinsey's respondents report scaling agents in any single function [MCKINSEY-SOAI-2025]. All are
self-reported surveys. Yet bounded delegation does run in teams that already own production workflows: internal audit
teams have agents testing defined control sets under reviewer sign-off (assurance controls-testing module, `#05`;
vendor-published, confirmed by the team). So:

- **Curious and Experimenting:** show delegate-level examples as inspiration and as the target picture. Do not plan one.
- **Adopting:** plan at most one or two **bounded** delegated workflows, and only when all five gates hold:
  (1) the workflow is already in production with an owner and a baseline; (2) decision criteria are written down with
  examples; (3) the agent's actions are reversible, or a person approves anything irreversible [OPENAI-GUIDE-2025];
  (4) it starts in shadow mode, with written rules for earning more autonomy [BCG-AGENTS-2025]; (5) a control plan
  tracks override rates so review does not become a rubber stamp [IMDA-MGF-2026]. If a gate fails, the missing gate
  becomes a foundation item and the delegated design waits.
- **Scaling:** delegated workflows as a portfolio, with tiered governance and shared components.
- **AI-native:** delegation is a default design option; the open questions are operating model and pricing.

### Boundary probes (pick two or three)

| Boundary | Ask | What decides it | Scope |
|---|---|---|---|
| Curious / Experimenting | Is there any task where AI is part of how the work is normally done, not just tried? | Sustained, repeated use on real work | [T] |
| | What was the last thing someone tried with AI, and what happened to it? | Whether trials happen at all | [all] |
| | What is holding you back from trying more? | The Curious blocker | [all] |
| Experimenting / Adopting | How many AI workflows run as part of normal work today? Who owns each, and how do you know they work? | Owned workflows with a measure [MITCISR-2024] | [U/O] |
| | Which pilots did you stop, and what did you learn? | A learning loop or pilot graveyard | [U/O] |
| | Where does the AI sit: beside the system where the work is recorded, or inside it? | Integration, not tool count [SAGE-2026] | [T] |
| | What happened to the hours AI saved last quarter? | Captured value or absorbed time [SAGE-2026] | [all] |
| | If an AI-assisted output turned out to be wrong, who would catch it, and how? | A designed human check | [T] |
| Adopting / Scaling | Has a second workflow reused anything from the first: a data connection, prompts, a review checklist? | Reuse | [U/O] |
| | Is there one place where value from all AI workflows is recorded? Who reads it? | Portfolio tracking [BCG-GAP-2025] | [U/O] |
| | Who owns AI at your level: the business, technology, both, or no one? | Ownership and decision rights | [U/O] |
| Scaling / AI-native | Has AI changed how you price, package or sell any service? | Commercial change [SAGE-2026] | [U/O] |
| | Have you launched anything you could not have delivered before? | New services [MITCISR-2024] | [U/O] |
| Individual user | Before a task, do you stop and ask whether AI could help? What do you never hand over, and how do you check output? | Personal fluency [MSFT-WTI-2024] | [T] |

## 6. Adapting the path

| Stage | Emphasis (spec §3.2, sharpened) |
|---|---|
| **Curious** | Inspiration tour of real archetype examples, with grades. Explain the ladder (assist, augment, automate, delegate). Two or three quick wins on low-risk, non-sensitive work with existing tools, made visible to peers [ROGERS-WIKI]. A minimal safe-use rule. Light mapping |
| **Experimenting** | Move from individual use to a shared team workflow. Find repeatable, high-volume steps. Fix a baseline and a success measure before any pilot. Use power users as champions [MSFT-WTI-2024]. Ask where saved time goes |
| **Adopting** | Full loop on a few processes. Data readiness, controls, measured value. Bounded delegation only behind the five gates above |
| **Scaling** | Portfolio thinking, shared platforms and components, operating model, governance, value tracked across workflows |
| **AI-native** | Business-model exposure, pricing, new services, AI-native competitors, workforce redesign |

| Scope | Adaptation |
|---|---|
| Individual or team | Run the loop on specific processes and steps. Output: a team plan with "start this week" actions |
| Function or business unit | Run Frame and Map on the value chain, then break down into units (`breakdown-and-rollup.md`) |
| Organization | As a unit, plus business-model exposure, a value tree, a 100-day plan and a value creation plan |

**Between two stages,** use the earlier stage's emphasis and add the later stage's first question. **Fee-based work**
(hourly or fixed-fee): put pricing into Frame from Experimenting on, because saved hours compress revenue or sit idle
unless pricing or services change [SAGE-2026]. **Resume:** if a plan exists, read `phase_completed` and `next_phase`,
summarise where things stand, and offer to continue.

## 7. Expert moves

| Move | When | What it reveals |
|---|---|---|
| **Ask to see the last real use** and look at the artifact | Any stage | Sustained use versus awareness; frequency and task type [MSFT-WTI-2024; GALLUP-2025] |
| **Split every status claim into three numbers:** who uses it, which workflows changed, what measure moved | "We use AI a lot" | The adoption-versus-impact gap: 88% of McKinsey respondents report regular use, 39% any EBIT effect (self-reported) [MCKINSEY-SOAI-2025] |
| **Count owned workflows in production**, each with an owner and a before-and-after measure | Experimenting vs Adopting | Pilot purgatory. Nearly 60% of law firms using one enterprise assistant were still piloting it [ILTA-2025] |
| **Ask which pilots stopped, and why** | Experimenting | Hidden blockers (data, trust, fit) and whether pilots teach anything |
| **Ask about unapproved tools**, with normalising words | Curious, Experimenting | Shadow use, real individual maturity, the policy gap; also a source of use cases [MIT-NANDA-2025; TR-2026] |
| **Triangulate the leader's view** against a team member or the archetype markers | A leader self-places high | Optimism bias; leaders hear about use second-hand [GALLUP-2025] |
| **Ask what happened to the saved hours** | Experimenting, Adopting | Capacity that was never captured; in fee work, margin at risk [SAGE-2026] |
| **Ask how much the sponsor uses AI personally** | Leader or practice head | Real sponsorship versus delegation; BCG links engaged leadership to its top tier (correlation) [BCG-GAP-2025] |
| **Ask for the policy, then ask what one staff member thinks it says** | Any stage | Paper versus lived governance [LITIFY-2026] |
| **Ask what managers do about AI:** encourage, permit or ignore | Team and unit | The main adoption lever below leadership [GALLUP-2025] |
| **Ask for the last AI error that was caught, and who caught it** | Adopting and above | Whether review is designed; whether people know where AI is unreliable [HBS-JAGGED-2023] |
| **Run a quick governance screen** (strategy, policy, risk, human checkpoints, monitoring, skills) | Before planning Adopting or above | Whether governance is ready for the target stage [ICAEW-GOV-2026] |
| **Count markers, place at the highest stage where most hold, and note exceptions** | End of onboarding | An audit trail the user can edit, instead of a label |

## 8. Common traps

| Trap | Why it happens | How to avoid it |
|---|---|---|
| Placing by tool count | Licences are easy to count; integration and outcomes are not | Ask for owned workflows, where AI sits relative to the system of record, and measured outcomes |
| Taking self-placement at face value | Leaders are further from daily use | Ask to see; triangulate; count markers [GALLUP-2025] |
| Treating efficiency as progress | Assisted productivity feels like success. 66% of Deloitte respondents report efficiency gains, 20% revenue growth (self-reported) [DELOITTE-STATEAI-2026] | Ask where saved time went and whether pricing or services changed |
| Skipping rungs, especially to agents | Ambition and vendor messages | Plan the next stage only; apply the five delegation gates |
| Ignoring shadow AI | Individuals move faster than organizations | Ask, without judgment; treat it as risk and as a source of ideas |
| One score for everything | Dimensions and scopes differ | Place per scope; name the binding constraint |
| Quoting headline numbers bare | Definitions and samples differ widely | Quote what was measured, by whom, and its provenance [MIT-NANDA-2025] |
| Interrogating instead of conversing | The question bank is long | Five to ten questions; skip what is known; infer and play back |
| Asking for confidential data | Wanting specifics | Ask for volumes, ranges and roles, never client or personal data |
| Using a vendor's maturity ladder | Vendor ladders lead to the vendor's product | Take the markers, not the prescription |

## 9. Worked example

*Illustrative, built from the spec's reference persona and the assurance controls-testing module.* An audit partner
leads a regional practice. The advisor learns, one question at a time: the practice audits mid-sized public and
private companies; fees are under pressure, staff are short, and recent inspections raised controls-testing points.
Firm policy allows an enterprise chat assistant but not client data in public tools. Asked who used AI in the last two
weeks, the partner says "most of the seniors". Asked for an example, the partner describes a manager using the firm's
evidence-matching tool on two engagements, and seniors drafting memos with the chat assistant. Asked how many
workflows run with AI as normal practice, with an owner and a measure: none yet. Asked what happened to time saved:
"No idea; it disappears into the next engagement."

*Placement.* Individuals: Experimenting, edging to Adopting for one manager. Practice: **Experimenting**; the binding
constraint is ownership and measurement, not tools. The advisor mentions that internal audit teams report large time
savings from agents testing defined controls, and that the figures are self- or vendor-reported (module `#05`).
*Path.* Experimenting emphasis plus the first Adopting question: pick one controls-testing workflow, set a baseline
(hours per control, review notes, rework) and design the human check. No delegated workflow yet: gates 1 and 2 fail.
*Playback.* "You lead a regional audit practice under fee and staffing pressure, with inspection findings in controls
testing. People use the firm's assistant individually and one manager is trialling evidence matching. Nothing is owned
or measured yet. You want a plan to take to the practice leadership. Did I get anything wrong?"

## 10. Output

Write the profile into the plan's frontmatter and add a **Profile** section to the body. Field names follow spec §5.3.

```yaml
scope: { name: "Regional audit practice", level: business-unit, parent: null }
author: { name: "<name>", role: "Audit partner" }
profile:
  archetype: assurance
  modules: [ controls-testing ]
  journey_stage: experimenting
  goals: [ "Protect margin under fee pressure", "Cover staff shortages", "Fewer inspection findings in controls testing" ]
  constraints: [ "Independence rules", "No client data in public AI tools" ]
  tools: [ "Enterprise chat assistant", "Audit platform", "Evidence-matching tool (pilot)" ]
  session_goal: "A plan to take to the practice leadership team"
status: in-progress
phase_completed: 0
next_phase: 1
updated: 2026-10-16
```

Use the module ids from the archetype's `ARCHETYPE.md`. The **Profile** body section holds: the played-back profile in
three to five lines; a stage table (scope, stage, markers seen, binding constraint); the adapted path; whether the
confidentiality reminder was given; and anything the user corrected. Then tick "Onboard" in the progress checklist.

## 11. Sources

- **ANTHROPIC-INTERVIEWER-2025**: Anthropic, *Introducing Anthropic Interviewer* (vendor research, 2025-12-04). https://www.anthropic.com/research/anthropic-interviewer
- **BCG-AGENTS-2025**: BCG, *How agents are accelerating the next wave of AI value creation* (consultancy, 2025-12-15). https://www.bcg.com/publications/2025/agents-accelerate-next-wave-of-ai-value-creation
- **BCG-GAP-2025**: BCG, *The Widening AI Value Gap: Build for the Future 2025* (consultancy survey, n=1,250, 2025-09). https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf
- **BISPO-2022**: Bispo Júnior, *Social desirability bias in qualitative health research*, Rev Saúde Pública (academic, 2022-11-18). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9749714/
- **DELOITTE-STATEAI-2026**: Deloitte AI Institute, *The State of AI in the Enterprise, 2026* (consultancy survey, n=3,235, 2026-01-20). https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html
- **GALLUP-2025**: Gallup, *AI Use at Work Rises* (polling report, n=23,068, 2025-12-14). https://www.gallup.com/workplace/699689/ai-use-at-work-rises.aspx
- **HBS-JAGGED-2023**: Dell'Acqua et al., *Navigating the Jagged Technological Frontier* (field experiment, HBS WP 24-013, 2023-09). https://www.hbs.edu/faculty/Pages/item.aspx?num=64700
- **ICAEW-GOV-2026**: ICAEW, *AI governance: 10 essential questions for responsible adoption* (professional body, 2026-07-03). https://www.icaew.com/technical/technology/artificial-intelligence/managing-risks/ai-governance-10-essential-questions-for-responsible-adoption
- **ILTA-2025**: Law360 Pulse on the ILTA 2025 Legal Technology Survey (trade press on industry survey, 2025-09-15). https://www.law360.com/articles/2387443/law-firms-embrace-ai-but-full-deployment-remains-rare
- **IMDA-MGF-2026**: IMDA Singapore, *Model AI Governance Framework for Agentic AI* v1.5 (regulator guidance, 2026-05-20). https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
- **IRGLOBAL-2025**: IR Global on Mondaq, *The Legal AI Adoption Curve* (practitioner article, 2025-05-13). https://www.mondaq.com/uk/new-technology/1623228/the-legal-ai-adoption-curve-where-your-law-firm-stands
- **LITIFY-2026**: Litify, *Legal AI Maturity Scale* (vendor blog, 2026-03-19). https://www.litify.com/blog/the-litify-legal-ai-maturity-scale
- **MCKINSEY-SOAI-2025**: McKinsey, *The state of AI in 2025* (consultancy survey, n=1,993, 2025-11; read via third-party copy). https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai
- **MIT-NANDA-2025**: MIT NANDA, *The GenAI Divide: State of AI in Business 2025* (preliminary, interview-based, not peer-reviewed, 2025-07). https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
- **MITCISR-2024**: Weill, Woerner, Sebastian, MIT CISR, *Building Enterprise AI Maturity* (academic briefing, 2024-12). https://cisr.mit.edu/publication/2024_1201_EnterpriseAIMaturityModel_WeillWoernerSebastian
- **MSFT-WTI-2024**: Microsoft and LinkedIn, *2024 Work Trend Index* (vendor survey, 2024-05-08). https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part
- **NNG-FLAHERTY-2020**: Nielsen Norman Group, *Contextual Inquiry* (practitioner article, 2020-12-06). https://www.nngroup.com/articles/contextual-inquiry/
- **OPENAI-GUIDE-2025**: OpenAI, *A practical guide to building agents* (vendor guide, 2025-04). https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf
- **ROGERS-WIKI**: Wikipedia, *Diffusion of innovations* (reference summary of Rogers, accessed 2026-10-16). https://en.wikipedia.org/wiki/Diffusion_of_innovations
- **SADIQ-2021**: Sadiq et al., *Artificial intelligence maturity model: a systematic literature review*, PeerJ CS (peer-reviewed, 2021-08-25). https://peerj.com/articles/cs-661
- **SAGE-2026**: Sage UK, *Where is your accounting firm on the AI maturity curve?* (vendor blog, 2026-04-08). https://www.sage.com/en-gb/blog/accounting-bookkeeping-ai-maturity-curve/
- **TR-2026**: Thomson Reuters, *Future of Professionals 2026* (vendor research page, undated). https://www.thomsonreuters.com/en/c/future-of-professionals
- Assurance example `#05`: `archetypes/assurance/modules/controls-testing.md` and its use-case YAML.
