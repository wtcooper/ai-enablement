# Topic research: AI portfolio management

Skill fed: `ai-portfolio` (intake, screen and score, stage gates, portfolio review, stop or redirect, value tracking).
Researched 2026-10-20. Public sources only. Source refs follow `PUBLISHER-SHORT-YYYY`; the full list with URLs, dates and access is in section 9.

How to read the evidence tags used below:

- **self-reported**: the named organization reports its own figure.
- **vendor-published**: a vendor or consultancy published it about its own survey or product.
- **independent**: a party with no stake in the result measured it (rare here).
- **respondent-reported**: a survey of executives; the figure is what respondents said, not what was audited.
- **Grade A rule (2026-10-17)**: a figure counts as *measured* only when the named organization reports it as measured. Almost every statistic in this file is a survey of respondent perceptions, so none is treated as "measured" unless it says so. Only DBS-2026 and PARTNERS-2026 are organization-reported results, and both are self-reported.

---

## 1. Summary

- **Most AI initiatives do not reach scaled, P&L-visible value, and the published rates are survey perceptions, not audited outcomes.** Respondent-reported figures range from McKinsey's 37% reporting any enterprise EBIT impact (MCK-2026) to IBM's 25% of initiatives meeting expected ROI and 16% scaled enterprise-wide (IBM-2025). MIT NANDA's "5% of custom enterprise tools reach production" is interview-based and flagged by its own authors as "directionally accurate" only (MITNANDA-2025, p.6). Treat every rate as a range with a stated definition.
- **The portfolio discipline experts recommend is old stage-gate method adapted to AI.** Cooper's Stage-Gate gives the skeleton: stages of work, gates that are forward-looking resource decisions, outcomes of Go, Kill, Hold or Recycle, and gate criteria split into readiness and value (COOPER-STAGEGATE-n.d.). A January 2026 HBR piece adapts it to AI with four portfolio stages, Buy/Sell/Hold backlog scoring, and AI-specific gate tests (HBR-2026).
- **The gate questions that matter for AI are about data, process redesign and run cost, not model accuracy.** HBR-2026 lists: is data available, good enough and governed; are skills in place; does the process need redesigning; are ethics and security controls set; does the business case still hold. RAND's 65 interviews and BCG's 10-20-70 finding point the same way (RAND-2024; BCG-2024).
- **Value realization is slow and hard to attribute, so benefits tracking has to be designed at intake.** Deloitte's EMEA survey found most respondents expect satisfactory ROI on a typical AI use case in two to four years, against the seven to 12 months usually expected of technology investment (DELOITTE-2025). Google Cloud's survey of gen-AI-in-production users reports the opposite picture (74% report ROI within a year), a gap that is largely about who was surveyed and who published it (GOOGLE-2025).
- **Two organizations publish self-reported, controlled value measurement.** DBS reports about SGD 1 billion economic value from data analytics and AI/ML in 2025, derived by comparing customers offered AI-driven solutions with a control group (DBS-2026; FCC-2026). Partners Group reports 120 bps of EBITDA margin (USD 10 million) at one portfolio company from a data-first AI programme (PARTNERS-2026). Both are self-reported and neither shows the method in full.
- **Stopping is an expected output, not a failure.** Gartner forecasts at least 30% of gen-AI projects abandoned after proof of concept by end of 2025 and over 40% of agentic projects cancelled by end of 2027 (forecasts, not measurements) (GARTNER-2024; GARTNER-2025). S&P Global's survey, as reported by CIO Dive, found the average organization scrapped 46% of proofs of concept before production (CIODIVE-2025). Government frameworks build in the stop: NIST has decommissioning and a go/no-go determination; OMB requires a plan to discontinue under-performing high-impact AI (NIST-2023; OMB-2025).
- **A central AI function should start as a gate-and-intake body and plan to become an advisory one.** Microsoft's CoE guidance assigns intake and prioritization workflows to the CoE and says to watch for approval delays, expert bottlenecks and CoE-versus-product-team friction as the signal to move to an advisory model (MSFT-COE-2026).
- **Knowledge-work specifics are thin.** Most evidence is cross-industry, government or banking. Professional-services portfolio data (utilization, pricing, realization) is absent from the public record found here (see Gaps).

---

## 2. Core concepts in plain language

**Portfolio as a funnel plus a dashboard.** HBR-2026 describes the portfolio through two lenses: a pipeline of gated stages, and a whole-portfolio view balanced across risk and return, time horizon, capability areas and mission alignment. *For AI:* individual projects are judged against competing opportunities and dependencies, not only on their own merits. *For knowledge work:* the same lens lets a practice leader see that three teams are building near-identical drafting assistants.

**Intake is a register, not an inbox.** The UK AI Playbook suggests a use cases register for capturing use cases and prioritising which to explore first, and recommends capturing opportunities by feasibility and business value (UKGOV-2025, "Identifying use cases for AI" and organisational support sections). Microsoft's CoE guidance says to keep a prioritized AI initiative backlog with consistent criteria for value, feasibility and resources (MSFT-COE-2026). *For AI:* every item needs one-sentence problem, expected result and owner before it is scored.

**Screening is two questions: is it worth it, is it ready.** Cooper separates *business value* criteria from *project readiness* criteria at every gate and uses a risk-adjusted financial model (Expected Commercial Value) plus a scorecard because financial models alone rest on uncertain or biased data (COOPER-STAGEGATE-n.d., "The Gates"). *For AI:* readiness is mostly data, skills, process-change capacity and control readiness (HBR-2026; MSFT-PLAN-2026 maturity table).

**A gate is a funding decision about the next stage, not a status review.** Cooper: gates are "forward-looking, where resource commitments are made"; a Go confirms budget, headcount, timeline and the date of the next gate, which avoids "approval without resources" (COOPER-STAGEGATE-n.d.). *For AI:* a Go on a pilot should name who releases capacity and what evidence is needed at the next gate.

**Stop, pivot, scale are three real outcomes.** Cooper's outputs are Go, Kill, Hold or Recycle; HBR-2026 says regular reviews should add promising initiatives, scale successful pilots, redirect struggling efforts and retire misaligned projects; Lloyds is described as accepting that rapid technology change can justify abandoning projects and switching to new use cases. *For AI:* a model-capability shift can obsolete a build mid-gate, so a "recycle to buy" outcome belongs in the vocabulary.

**Pilot success is not production success.** MIT NANDA reports that generic chat tools show high pilot-to-implementation (about 83%) while task-specific enterprise tools show 5% successfully implemented, using its own definition of "marked and sustained productivity and/or P&L impact" and interview evidence (MITNANDA-2025, §3.2). *For knowledge work:* roll-out of a seat-based assistant and redesign of a workflow are different portfolio items with different evidence thresholds.

**Benefits are owned, registered, harvested and compared with forecast.** The IVI maturity model for benefits harvesting asks for a named benefits owner, reviews after go-live, and a "benefit success rate" (share of targeted benefits actually achieved) (IVI-ITCMF-n.d.). The Australian Gateway Gate 5 review checks benefits against the business case and benefits realisation plan, with an owner for each benefit and measurement and collection timing (AUSGOV-2013). *For AI:* these are the template fields for a benefits register.

**Attribution is the hard part for AI.** Deloitte's interviewees list "AI is entangled with broader transformation" and siloed data that makes before-and-after tracking hard (DELOITTE-2025, "five key reasons"). DBS's CEO says that as AI is embedded in daily workflows it will be harder to isolate its economic value (FCC-2026). *For AI:* decide the counterfactual (control group, baseline, or stated assumption) before launch.

**The central function changes over time.** Microsoft's AI CoE guidance: centralize early, then move to an advisory model once governance is embedded in platform operations (MSFT-COE-2026, "Evolve AI CoE operations"). *For AI:* the portfolio office should have a planned exit from gatekeeper to guardrail-setter.

**AI value arrives late (the J-curve).** Brynjolfsson, Rock and Syverson model how complementary intangible investment (co-invented processes, business models, human capital) depresses measured productivity early and boosts it later for general purpose technologies including AI (NBER-2020, abstract). *For AI:* a portfolio review that expects an immediate step-change in P&L will kill the right projects too early. This is a model and historical analysis, not a measurement of any AI portfolio.

---

## 3. Expert moves

Format: **move** — when to use it — what it reveals — source ref. Moves marked *(derived)* combine a cited source with a straightforward inference; the source says the first part, not the application.

1. **Make every intake entry a one-sentence activity-plus-result statement ("help support agents answer from internal documents so resolution time drops") before scoring** — at intake — reveals vague ideas and whether the activity happens often enough to justify investment — MSFT-PLAN-2026 ("Translate problems into use cases").
2. **Start the scan from business problems, not from the technology** — at intake and in frame — reveals novelty-driven requests; the guidance is to look for where "results miss expectations" or people repeat manual work — MSFT-PLAN-2026; UKGOV-2025 ("Identifying use cases for AI": led by business and user needs, "not what the technology can do").
3. **Classify each item as individual-work improvement or business-automation/process change** — at intake — reveals which items will show up in P&L and which will mainly show up in individual productivity — MSFT-PLAN-2026 ("Classify use case"); MITNANDA-2025 §2 (widely adopted chat tools "primarily enhance individual productivity, not P&L performance"). *(derived: route the two classes to different evidence thresholds)*
4. **Ask "could a few if-then rules do this?"** — at screen — reveals AI applied to problems that do not need it; RAND interviewees described datasets with a handful of dominant patterns that simple rules could capture — RAND-2024 ("Using Artificial Intelligence to Solve Simple Problems"); UKGOV-2025 (focus on cases where traditional solutions cannot handle volume, complexity or real-time needs).
5. **Check that the metric the team optimizes is the metric the business cares about** — at screen and Gate 2 — reveals models built for the wrong objective; RAND's interviewees described leaders and technical staff failing to translate objectives and models "optimized for the wrong metrics" — RAND-2024 (Summary; "Optimizing for the Wrong Business Problem").
6. **Ask whether the problem is worth a year of team commitment** — at screen — reveals fashion-driven items; RAND's recommendation is to commit each product team to a specific problem for at least a year — RAND-2024 ("Choose enduring problems").
7. **Score every readiness gate on two separate axes, readiness and value, and keep both visible** — at screen and every gate — reveals attractive-but-unready items versus ready-but-trivial ones — COOPER-STAGEGATE-n.d. ("Gate criteria"); HBR-2026 (Buy/Sell/Hold scoring on strategic alignment, feasibility, risk-reward, resources).
8. **Rank the backlog with fixed scoring criteria, then pull the next item only when capacity opens** — at portfolio review — reveals whether priorities are set by loudest sponsor or by score; HBR-2026 describes advancement decided "by resource availability and objective scoring against fixed criteria" — HBR-2026 ("The Four Portfolio Stages", closing paragraphs).
9. **Use the gate decision vocabulary Go, Kill, Hold, Recycle, and write the next-stage resources and next gate date into every Go** — at every gate — reveals "approval without resources" — COOPER-STAGEGATE-n.d. ("Gate outputs").
10. **Ask the gate attendees to name whose resources they control** — at gate design — reveals missing gatekeepers; Cooper's gatekeepers are the senior managers who own or control the resources the project team needs next — COOPER-STAGEGATE-n.d. ("The Gates").
11. **Run the five AI progression tests at the pilot gate: data available and governed, skills sourced, process redesign needed, ethics and security controls set, business case still valid** — at prototype-to-pilot gate — reveals projects that are technically fine but organizationally unready — HBR-2026 ("Stage gates").
12. **Insist the proof of concept uses real data, not dummy data** — at prototype gate — reveals optimism that collapses on real data; Deloitte's interviewees say PoCs on unrealistic dummy data are a source of optimism and problems emerge when real data is loaded — DELOITTE-2025 (reason 2 of five).
13. **Frame experiments as learning journeys testing technical feasibility, enterprise viability and human desirability (will users adopt it)** — at prototype and pilot — reveals pilots that only validate the model, not the integration or the adoption — HBR-2026 (Stage 3, Experiment).
14. **Require red-team scrutiny and rigorous system testing at the gate before scale** — at pilot-to-production gate — reveals misuse and failure modes before cost rises; HBR-2026 notes production "usually entails a considerable increase in cost and development time" — HBR-2026 (Stage 3 gate; Stage 4).
15. **Ask for the realistic payback window by AI type and set hurdle rates accordingly** — at business-case gate — reveals unrealistic 12-month hurdles; Deloitte respondents mostly expect satisfactory ROI in two to four years and only 6% report payback under a year; 85% of its "ROI Leaders" use different frameworks or timeframes for generative and agentic AI — DELOITTE-2025 (Figure 2 text; leaders section). Contrast GOOGLE-2025 (see Evidence E14 for why the figures differ).
16. **Separate use-case-level financial impact from enterprise-level P&L impact in every benefits discussion** — at review and value tracking — reveals the gap McKinsey describes, where respondents report function-level cost or revenue effects without enterprise EBIT impact — MCK-2026 ("Despite broader use and individual results...").
17. **Ask what the counterfactual is: control group, A/B, baseline, or an explicit assumption, and agree it before launch** — at business-case gate — reveals unattributable benefits; DBS compares outcomes between customers offered AI-driven solutions and a control group — DBS-2026 as reported in FCC-2026 and FORRESTER-2026.
18. **Ask what other change is shipping alongside the AI and how its effect will be separated** — at business-case gate — reveals entangled attribution; Deloitte's interviewees say AI is typically rolled out alongside broader digital, operational or structural change — DELOITTE-2025 (reason 5).
19. **Define early-warning triggers (schedule slippage, cost overrun, performance shortfall) and review them at each portfolio review** — at review — reveals initiatives needing intervention before the next gate — HBR-2026 ("Regular reviews").
20. **Check the balance across time horizons and the investment in foundational capability, not only the ranking** — at portfolio review — reveals a portfolio of only quick wins or only moonshots, and missing foundations; HBR-2026 recommends a mix of near-, medium- and longer-term items and sequencing so earlier projects build capability later ones need — HBR-2026 ("The portfolio approach"); HBR-2018 (introduction: MD Anderson's Watson project, which the article reports was put on hold in 2017 after costs topped USD 62 million and before use on patients, contrasted with smaller cognitive projects).
21. **Look for CoE bottleneck signs: approval delays, experts who cannot support all teams, and recurring CoE-versus-product-team priority debates** — at operating-model review — reveals when the central function should shift to advisory — MSFT-COE-2026 ("Recognize organizational inflection points").
22. **Ask for the inventory of AI systems in use and the decommissioning procedure** — at onboard and governance — reveals shadow AI and no exit path; NIST lists mechanisms to inventory AI systems and processes for decommissioning; OMB requires an annual use case inventory and a plan to discontinue under-performing high-impact AI — NIST-2023 (GOVERN 1.6, 1.7); OMB-2025 (Overview; inventory and high-impact provisions).
23. **Tier the gate weight by risk and regulatory exposure, with a lighter path for low-risk items** — at gate design — reveals gate fatigue; the utility case in HBR-2026 says a lighter version suits industries with lower regulatory burden, and OMB says to streamline approvals for closely related use cases with similar risk profiles — HBR-2026 (utility example); OMB-2025 (high-impact determination provisions); UMBREX-n.d. (risk tiering, secondary).
24. **Ask who pays for run cost at scale and whether usage-cost limits already bind** — at scale gate — reveals total cost of ownership surprises; McKinsey reports about one in five respondents say AI operating costs (including tokens) constrained their AI use, and HBR-2026 says to track total cost of ownership and measure actual impact "rather than assuming benefits" — MCK-2026 ("While AI investments are increasing..."); HBR-2026 (Stage 4).
25. **Record the build-versus-buy-versus-partner decision right at Gate 2** — at business-case gate — reveals slow custom builds that a bought tool would cover; Lloyds is described as having clear decision rights on build or buy; MIT NANDA's interview-based finding is that external partnerships had twice the success rate of internal builds (with its stated limitations) — HBR-2026 (Lloyds); MITNANDA-2025 §2 and p.6 note.
26. **Do not count seat roll-outs as portfolio wins; track them in a separate "enablement" line** — at review — reveals inflated pilot-to-production rates, since generic chat tools show high implementation rates (about 83%) against 5% for task-specific tools — MITNANDA-2025 §3.2. *(derived)*
27. **Assign a named benefit owner in the business at intake and test the count at review** — at intake and value tracking — reveals orphan benefits; IVI measures "% of projects/programmes for which a benefits owner is identified" and the Gate 5 review expects the project owner of each benefit identified; NAO found 24 of 32 bodies with deployed AI always or usually named an accountable owner — IVI-ITCMF-n.d.; AUSGOV-2013 ("Business Case and Benefits Management"); NAO-2024 (Summary para 11).
28. **Record benefits expected but not achieved and keep them on the action plan** — at post-implementation review — reveals what to redeploy effort toward or write off — AUSGOV-2013 (benefits realisation plan review and close-out report: financial and non-financial benefits achieved, lessons learned); IVI-ITCMF-n.d. (benefit success rate).
29. **In a PE setting, trace each AI initiative to the EBITDA bridge in the value creation plan and ask what data asset it depends on** — at PE portfolio review — reveals AI work that cannot move the metric the fund underwrites; Bain's 2026 report says deals now "pencil out" only with EBITDA growth closer to 10%-12% a year versus about 5% in the past, and Partners Group's FRP case started from a clean policy-level dataset — BAIN-2026-PE (Outlook section); PARTNERS-2026. *(derived: the bridge link)*

---

## 4. Question bank

Tags: scope level `[team]`, `[unit]`, `[org]`; journey stage in parentheses: Onboard, Frame, Map, Diagnose, Reimagine, Prioritize, Make the case, Plan. Questions are drafted from the cited method sources; where a question rests on a specific source it is noted.

### Intake

- `[org]` (Onboard) Is there a single register of AI ideas, pilots and live systems, or does each practice keep its own? Who sees it? *(UKGOV-2025 use cases register; NIST-2023 GOVERN 1.6)*
- `[unit]` (Frame) Where do ideas come from today: top-down strategy, practice leaders, individual staff, vendors? What share of ideas are driven by what the technology can do versus a business pain point? *(UKGOV-2025; MSFT-PLAN-2026)*
- `[team]` (Map) Describe the activity and the result you expect in one sentence. How often does the activity happen? *(MSFT-PLAN-2026)*
- `[team]` (Diagnose) Is this a change to how individuals work in existing tools, or a change to how the work flows? *(MSFT-PLAN-2026 classification)*
- `[team]` (Diagnose) Could simpler rules or existing software handle this? *(RAND-2024; UKGOV-2025)*
- `[unit]` (Frame) Who in the business will own the benefit, by name? *(IVI-ITCMF-n.d.)*
- `[org]` (Onboard) Do you already have an AI governance board or CoE? What decisions does it make? What does it not? *(UKGOV-2025; MSFT-COE-2026)*

### Screen and score

- `[unit]` (Prioritize) What are your scoring criteria today? Who set them, and when were they last recalibrated? *(HBR-2026 regular reviews: "recalibrating objective scoring criteria")*
- `[unit]` (Prioritize) For each candidate: strategic alignment, feasibility, risk-reward, resource needs. Which has the weakest evidence? *(HBR-2026 Buy/Sell/Hold)*
- `[team]` (Prioritize) What data does this need, who owns it, and has anyone looked at it in its real state? *(HBR-2026; DELOITTE-2025; MSFT-PLAN-2026 data inventory)*
- `[team]` (Prioritize) Do the people who would build it have the skills, or would you source them? *(HBR-2026 gate test)*
- `[org]` (Prioritize) What is the risk and regulatory tier of this use case, and does that change the gate path? *(OMB-2025 high-impact; UKGOV-2025 use cases to avoid)*
- `[unit]` (Prioritize) What would have to be true for this to be worth a year of a team's time? *(RAND-2024)*
- `[unit]` (Prioritize) Are any of the proposed items duplicates of work in another practice? *(HBR-2026 portfolio dashboard view; derived)*

### Stage gates

- `[unit]` (Make the case) What evidence will you bring to the next gate, agreed in advance? Who are the gatekeepers and what do they control? *(COOPER-STAGEGATE-n.d.)*
- `[team]` (Make the case) Does the business case still hold on real data and real run costs? *(HBR-2026; DELOITTE-2025)*
- `[team]` (Plan) Does the business process the AI supports need redesign, and who owns that change? *(HBR-2026 gate test; MCK-2026 workflow redesign finding)*
- `[unit]` (Make the case) What is the counterfactual, and what other changes ship at the same time? *(DBS via FCC-2026; DELOITTE-2025 reason 5)*
- `[org]` (Plan) Who releases the people and budget for the next stage, and does the Go decision say so? *(COOPER-STAGEGATE-n.d. "approval without resources")*
- `[team]` (Plan) How will you test adoption, not just accuracy, in the pilot? *(HBR-2026 Stage 3; MITNANDA-2025 §4)*
- `[unit]` (Plan) Has anyone tried to break it (red team) before we scale? *(HBR-2026)*

### Portfolio review

- `[org]` (Plan) Who attends the portfolio review, what pack do they see, and what decisions does the meeting actually make? *(No source gives a standard attendee list; Lloyds' "GenAI Control Tower" is described as a cross-functional forum that prioritizes use cases, allocates resources and ensures strategic alignment: HBR-2026.)*
- `[org]` (Plan) Is the portfolio balanced across near-, medium- and long-term items, and does it include foundation work? *(HBR-2026)*
- `[unit]` (Plan) Which items have tripped an early-warning trigger (slippage, overrun, performance shortfall)? *(HBR-2026)*
- `[org]` (Plan) What is the AI spend as a share of technology budget, and what does the portfolio show for it? *(MCK-2026: 28% of respondents spend more than 10% of ICT budget on AI; DELOITTE-2025: 95% of ROI Leaders allocate more than 10%)*
- `[org]` (Onboard) Is the central team still adding value, or is it a queue? *(MSFT-COE-2026 inflection points)*

### Stop or redirect

- `[unit]` (Prioritize) What would make you stop this? Was that written down at the gate? *(derived from COOPER-STAGEGATE-n.d. Kill outcome)*
- `[team]` (Diagnose) Is this pilot stuck because of the model, the data, the workflow or the people? *(MITNANDA-2025 §4.1 barrier ranking; RAND-2024)*
- `[org]` (Plan) Do you have a procedure to decommission an AI system safely, and who triggers it? *(NIST-2023 GOVERN 1.7; OMB-2025)*
- `[unit]` (Prioritize) Has a technology change made this build unnecessary, so that switching to a bought or newer option is the right call? *(HBR-2026 on Lloyds)*
- `[unit]` (Prioritize) What do we learn and reuse from the stopped item? *(AUSGOV-2013 lessons learned; derived)*

### Value tracking

- `[unit]` (Make the case) What is the baseline, and who measured it? *(AUSGOV-2013 benefits realisation plan)*
- `[unit]` (Plan) When will benefits be reviewed after go-live, and by whom? *(IVI-ITCMF-n.d.; AUSGOV-2013)*
- `[org]` (Plan) How do we separate use-case-level savings from enterprise-level P&L impact? *(MCK-2026)*
- `[unit]` (Plan) What happens to time freed up: redeployed, absorbed, or removed from budget? *(GARTNER-2024 notes productivity is hard to translate directly into financial benefit; MCK-2026 workforce findings)*
- `[org]` (Plan) How many of last year's forecast benefits were actually achieved? *(IVI-ITCMF-n.d. "benefit success rate")*
- `[org]` (PE) Which initiatives map to a line in the value creation plan, and what is the EBITDA effect so far? *(BAIN-2026-PE; PARTNERS-2026)*

---

## 5. Common traps

| Trap | Why it happens | Evidence | How to avoid |
|---|---|---|---|
| **Pilot sprawl without coordinated oversight** | Pressure to do something with AI; departmental experiments | HBR-2026: "too many pilots with too little coordinated oversight". NAO: fewer than half of bodies with deployed AI (15 of 32) said use cases were always or usually identified at organisational level before deployment (NAO-2024, Summary para 11) | Single register; central intake; portfolio dashboard |
| **Optimizing for the wrong problem or metric** | Leaders and technical staff do not translate objectives | RAND-2024: leadership-driven failures cited by 84% of interviewees as a primary cause (65 interviews, Aug-Dec 2023, interviewee perceptions) | Problem statement and success metric agreed with the business owner at Gate 1 |
| **Applying AI where simple rules suffice** | AI as a buzzword; leaders far from implementation | RAND-2024 ("Using AI to Solve Simple Problems") | "Could rules do this?" screen |
| **Funding the visible functions over the high-ROI ones** | Budgets favor top-line functions | MITNANDA-2025 §2 and §3.4 (investment bias; the §3.4 takeaway says 50% of GenAI budgets go to sales and marketing while the text says about 70% in a hypothetical USD 100 allocation exercise, so the source is internally inconsistent; the authors say back-office automation often yields better ROI, with attribution ease as the stated reason) | Score on value and feasibility, not visibility; check budget split by function at review |
| **Dummy-data proofs of concept** | Real data is messy and not yet integrated | DELOITTE-2025 reason 2 | Gate 3 evidence on real data |
| **Treating adoption as the metric** | Easy to measure | MITNANDA-2025 §2 (over 80% explored or piloted general tools, "primarily enhance individual productivity, not P&L"); MCK-2026 (80% say AI improved individual productivity yet 37% report EBIT impact) | Report individual productivity and enterprise impact as separate lines |
| **Expecting short payback** | Technology investments typically expected to pay back in 7-12 months | DELOITTE-2025 (two to four years typical; 6% under one year) | Use AI-type-specific hurdles; hold decisions that allow for ramp-up; but see E14 for conflicting survey |
| **Unattributable benefits** | AI rolled out with other change; AI embedded in workflows | DELOITTE-2025 reason 5; FCC-2026 (DBS CEO) | Counterfactual agreed up front |
| **Ignoring the people and process share of the work** | Teams spend time on algorithms | BCG-2024: around 70% of implementation challenges are people and process, 20% technology, 10% algorithms (BCG survey of 1,000 CxOs); leaders put 10% of resources into algorithms, 20% into technology and data, 70% into people and processes | Weight gate criteria toward change readiness, owner, workflow |
| **CoE as permanent gatekeeper** | Centralization helps early, hurts later | MSFT-COE-2026 | Review CoE signals each half-year; plan the advisory transition |
| **Gates as status theater** | Gates become paper rituals | UMBREX-n.d. (secondary: "when gates become status theater or compliance rituals without real decisions"); COOPER-STAGEGATE-n.d. (gates are resource decisions, not status reviews) | Written Go/Kill/Hold/Recycle with resources and next gate date |
| **No exit path** | Systems accumulate; nobody owns retirement | NIST-2023 GOVERN 1.7; OMB-2025 | Decommissioning procedure and inventory at onboard |
| **Moonshot first** | Big ambition before capability | HBR-2018 intro (MD Anderson Watson project on hold after costs topped USD 62 million) | Balanced horizons; sequence foundation work |
| **Hype-driven agentic programmes** | "Agent washing", early-stage experiments | GARTNER-2025 (forecast; as reported by Outlook Business, quoting Gartner's Anushree Verma) | Apply the same gates to agentic items; require cost and risk evidence |
| **Ignoring the J-curve** | Intangible investment is invisible early | NBER-2020 | Use leading indicators (adoption quality, process change, error rates) at early review; do not kill purely on early P&L absence |

---

## 6. Evidence

Each row: what it measures, who measured it, provenance, source and locator. Rows E1-E24. "Grade note" applies the 2026-10-17 Grade A rule.

| # | Figure | What it measures (source's words) | Measured by / provenance | Source and locator | Grade note |
|---|---|---|---|---|---|
| E1 | 37% | Respondents who "attribute at least some EBIT impact to AI use"; "about the same share as last year" | McKinsey Global Survey, 1,719 participants in 97 nations, field 4 May-8 Jun 2026; weighted by national GDP share; respondent-reported, consultancy-published | MCK-2026, Key takeaways and "Despite broader use..." | Respondent perception, not org-measured |
| E2 | 6% | "AI high performers": respondents attributing 5% or more of EBIT to AI and reporting "significant" value; unchanged from 2025 | Same survey | MCK-2026, "High-performing organizations..." | As above |
| E3 | 44% (from 38%) | Respondents reporting AI "is scaling across their enterprise" | Same survey | MCK-2026, "Use of AI is deepening..." | As above |
| E4 | Nearly three-quarters vs one-quarter | High performers vs other respondents reporting "fundamentally redesigning workflows because of their AI use" | Same survey | MCK-2026, "High performers have bigger AI aspirations" | As above; association, not proof of cause |
| E5 | 2x | High performers twice as likely as others to say senior leaders demonstrate commitment and the organization has "defined processes to measure the impact" | Same survey | MCK-2026, "High-performing organizations..." | As above |
| E6 | 25% and 16% | Share of AI initiatives that "delivered expected ROI over the last few years" and share "scaled enterprise wide", as reported by CEOs | IBM Institute for Business Value with Oxford Economics, 2,000 CEOs, 33 countries, Feb-Apr 2025; respondent-reported, vendor-published | IBM-2025, "Other key findings" | Respondent perception; press release only (full study page not retrieved) |
| E7 | 5% (of 60% evaluated, 20% piloted) | Share of organizations that evaluated enterprise-grade/task-specific GenAI tools that reached production; defined as "marked and sustained productivity and/or P&L impact" remarked by users or executives | MIT NANDA, systematic review of 300+ initiatives, 52 org interviews, 153 survey responses, Jan-Jun 2025; authors say "directionally accurate based on individual interviews rather than official company reporting" | MITNANDA-2025, §2 and §3.2 with research notes (p.6) | Not org-measured; authors caveat sample and definitions |
| E8 | ~83% | Pilot-to-implementation for generic LLM chatbots (apparent rate) | MIT NANDA, same method | MITNANDA-2025, §3.2 | As E7 |
| E9 | 42% (up from 17%); 46% | Share of companies "abandoning most of their AI initiatives"; average share of proofs of concept scrapped before production | S&P Global Market Intelligence survey of more than 1,000 respondents in North America and Europe, as reported by CIO Dive (14 Mar 2025); respondent-reported | CIODIVE-2025 | Secondary report; original blocked |
| E10 | 30% | Forecast: "At least 30% of generative AI projects will be abandoned after proof of concept by the end of 2025" due to poor data quality, inadequate risk controls, escalating costs or unclear business value | Gartner forecast, 29 Jul 2024 | GARTNER-2024, opening paragraph | Prediction, not measurement |
| E11 | 40% | Forecast: more than 40% of agentic AI projects will be cancelled by end of 2027 due to escalating costs, unclear business value or inadequate risk controls | Gartner forecast (25 Jun 2025), read via Outlook Business report | GARTNER-2025 | Prediction; secondary report |
| E12 | 74% / 4% / 22% / 26% | 74% of companies "have yet to show tangible value"; 4% have cutting-edge capabilities and consistently generate significant value; 22% are "leaders" beginning to realize substantial gains | BCG survey of 1,000 CxOs and senior executives, 59 countries, 20+ sectors, assessed on 30 capabilities; press release 24 Oct 2024; consultancy-published | BCG-2024, paras 1-3 | Perception-plus-capability assessment, not P&L audit |
| E13 | 5% / 35% / 60% | Firms "AI future-built" (5%), "scaling AI, beginning to generate value" (35%), and "reaping hardly any material value" (60%) | BCG, "The Widening AI Value Gap", 30 Sep 2025; sample size not stated on the retrieved page | BCG-2025, introduction | Consultancy-published; sample not seen |
| E14 | 74% | Share of respondents (among those "using gen AI in production") who "report ROI within the first year (unchanged YoY)"; the underlying question text asks in what timeframe respondents "expect gen AI to deliver" ROI | Google Cloud with National Research Group, 3,466 senior leaders of enterprises with USD 10M+ revenue, field 18 Apr-3 Jun 2025; vendor-published | GOOGLE-2025, chapter "Where AI is delivering ROI" and footnote 21 | Vendor survey of production users; wording ambiguous; do not use as an expectation to set hurdles |
| E15 | 2-4 years; 6%; 13%; 10% | Most respondents achieved "satisfactory ROI on a typical AI use case within two to four years"; 6% payback under a year; 13% of the most successful projects returned within 12 months; 10% of agentic AI users report significant ROI | Deloitte survey of 1,854 senior executives in 14 EMEA countries, 15 Aug-5 Sep 2025, plus 24 interviews | DELOITTE-2025, summary and Figure 2; agentic section | Consultancy-published; respondent-reported |
| E16 | 72% / ~three in four | 72% of business leaders "report tracking structured, business-linked ROI metrics"; nearly three-quarters "already see positive ROI" | Wharton Human-AI Research and GBK Collective, ~800 US enterprise decision makers (1,000+ employees, over USD 50M revenue), 26 Jun-11 Jul 2025 | WHARTON-2025, Executive Summary (key takeaway 2, pp.8-9) | Academic-industry survey; respondent perception |
| E17 | >80%; 84% | ">80% of AI projects fail" is quoted from a prior source ("By some estimates"), not measured by RAND; RAND's own result is that 84% of 65 interviewees cited leadership-driven failure as a primary reason | RAND, 65 interviews with AI practitioners, Aug-Dec 2023 | RAND-2024, Summary and "Findings from Industry Interviews" | The 80% is a cited estimate; RAND's definition of failure is "perceived to be a failure by the organization" |
| E18 | 21% of 87; 15 of 32; 24 of 32; 37%; 70% | Government bodies that had an AI strategy; bodies with deployed AI where use cases were always or usually identified at organisational level before deployment; bodies with named accountable owner; share that had deployed AI; share piloting or planning AI | UK National Audit Office survey of 87 government bodies, autumn 2023 | NAO-2024, Summary paras 11-12 and Figure | Independent audit body; survey of bodies, small sample |
| E19 | SGD 1 billion (2025); SGD 750M (2024); SGD 370M (2023) | "Economic value" from data analytics and AI/ML initiatives; "over 2,000 models and more than 430 use cases" deployed in 2025; the figure "was derived by comparing outcomes between customers who were offered AI-driven solutions and those in a control group" | DBS Bank, self-reported (newsroom 20 Jul 2026); method as reported by Business Times (9 Feb 2026) and Forrester blog (22 Jan 2026) | DBS-2026; FCC-2026; FORRESTER-2026 | Organization reports the figure and states a control-group method; scope is analytics plus AI/ML, not generative AI alone; not independently audited |
| E20 | 120 bps; USD 10M; 94% | EBITDA margin uplift at Foundation Risk Partners; "USD 10 million of EBITDA impact"; "reduces the average policy processing cycle for new clients by 94%" | Partners Group press release, 3 Aug 2026; self-reported; delivered by a seven-person team augmented by a sister portfolio company | PARTNERS-2026 | Company-reported; no method or period given in release |
| E21 | 10%-12% vs ~5% | Annual EBITDA growth that "expensive deals" now need to generate a 2.5x MOIC over five years, versus about 5% in the past | Bain & Company, Global Private Equity Report 2026 | BAIN-2026-PE, Outlook section (around Figure 1) | Consultancy analysis with stated assumptions about leverage and multiples; context for value-creation, not an AI result |
| E22 | 15.8% / 15.2% / 22.6% | Average reported revenue increase, cost savings and productivity improvement from gen AI | Gartner survey of 822 business leaders, Sep-Nov 2023 | GARTNER-2024, "Realizing Business Value" | Respondent-reported; early-adopter survey |
| E23 | USD 5M-20M | Costs of different GenAI deployment approaches (Figure 1) | Gartner, July 2024 | GARTNER-2024 | Analyst estimate |
| E24 | 11.3% / 15.9% | Gap between adjusted total factor productivity and official measures at end 2004 and end 2017 | Brynjolfsson, Rock, Syverson, NBER Working Paper 25148 (rev. Jan 2020), model using intangibles from R&D, software and computer hardware; the authors find AI-related effects "small but growing" | NBER-2020, abstract | Academic working paper; not about AI portfolios |

Absence of evidence, stated plainly: no source found reports a stage-gate pass rate, kill rate or time-in-stage for an enterprise AI portfolio, and no independent audit of realized-versus-forecast AI benefits was found.

---

## 7. Worked examples

### 7.1 A utility's gated path from idea to production (regulated industry)

Source: HBR-2026, "How the Portfolio Runs" (example of an electric utility in the Northeast US, anonymized). The utility's AI CoE gathers use-case ideas from different teams. Step 1: CoE members assess whether the idea meets a business need. Step 2: if it passes, a proof of concept is built. Step 3: an evaluation by senior management, regulatory team, legal team and CoE members. Step 4: if approved, the CEO and CIO evaluate potential return on investment and take the use case into production. The article says the company values disciplined progression particularly because of regulatory issues, and that a lighter version suits industries with lower regulatory burden.
*What to take:* the order is business need, then proof, then risk and regulatory review, then return and production, with a different set of approvers at each gate. The article does not report volumes, pass rates or timings, so the example is a design pattern, not an outcome.

### 7.2 Lloyds Banking Group's "GenAI Control Tower"

Source: HBR-2026, "Portfolio Management in Practice". A cross-functional forum prioritizes use cases across the organization, allocates resources and ensures alignment with strategic priorities. Each initiative passes reviews (risk assessment, legal, ethics, bias, security) before production. A centralized playbook and clear build-or-buy decision rights are described. The model is said to balance long-term transformation with short-term value and to accept that rapid change in available technology can justify abandoning projects and switching.
*What to take:* the portfolio forum is where resource allocation and stop decisions live. No figures on projects, spend or outcomes were found in the source; do not quote any.

### 7.3 DBS: value tracking with a control group (banking)

Sources: DBS-2026 (self-reported newsroom release, 20 Jul 2026); FCC-2026 (Business Times reprint, 9 Feb 2026); FORRESTER-2026 (analyst blog, 22 Jan 2026). DBS reports over 2,000 models and more than 430 use cases deployed in 2025 and about SGD 1 billion of economic value from data analytics and AI/ML initiatives. Forrester reports the earlier ambition (SGD 1 billion in five years, stated by a former CIO), SGD 370 million at FY2023, and that value traces to revenue, cost savings and risk avoidance. The Business Times reports a figure of SGD 750 million for 2024 and says the SGD 1 billion was derived by comparing customers offered AI-driven solutions with a control group; the CEO said the bank may continue "A/B testing" but expects capacity-building value to be harder to isolate.
*What to take:* a long-running number tied to a stated counterfactual method, with a stated limit on how long the method will hold. The methodology is described only in press, not in DBS's own method note; the scope is analytics plus AI/ML.

### 7.4 Foundation Risk Partners: a PE operating-model example (insurance brokerage, knowledge work)

Source: PARTNERS-2026. Partners Group reports 120 bps of EBITDA margin uplift at Foundation Risk Partners (USD 10 million of financial impact) from an AI programme delivered with another portfolio company, Version 1. Two agentic solutions were built on a clean proprietary policy-level dataset: one reduces the average policy processing cycle for new clients by 94% (the release says this led to a doubling of close rates), the other automates a human-intensive policy-checking task. A seven-person team augmented by Version 1 delivered it. Release dated 3 August 2026.
*What to take:* sequence is data asset first, then targeted workflow solutions, then EBITDA claim. The figures are self-reported by the owner of both companies in a press release; no baseline, period or audit is given and it is a single case. Context on what PE fund economics demand is in BAIN-2026-PE (E21).

---

## 8. Mapping to steps

Thresholds below are sourced where a source is cited. Items marked **(proposed default)** are the research team's suggested starting values with no source behind the number; the advisor should present them as defaults to adapt, not as findings.

### Intake

**Checklist**
- One register for ideas, pilots and live systems (UKGOV-2025; NIST-2023 GOVERN 1.6).
- Entry describes the activity and the expected result in one sentence (MSFT-PLAN-2026).
- Entry classed as individual-work or business-automation (MSFT-PLAN-2026).
- Business-owner named (IVI-ITCMF-n.d.).
- Rules-or-AI check done (RAND-2024; UKGOV-2025).

**Template fields (intake card)**: id; submitting unit; problem statement; activity and expected result sentence; frequency/volume of the activity (last month's actual volume, not a typical week) **(proposed default for the volume prompt)**; value-creation class; AI type guess (generative vs non-generative, per MSFT-PLAN-2026); data sources and owners; named business benefit owner; risk/regulatory tier; build/buy/partner leaning; date; status.

**Decision rule**: items without owner, problem statement and data source stay in "outline" and are not scored.

### Screen and score

**Checklist**: score on strategic alignment, feasibility, risk-reward, resource requirements (HBR-2026 Buy/Sell/Hold); separate readiness and value (COOPER-STAGEGATE-n.d.); data inventory covering sources, formats, quality, accessibility (MSFT-PLAN-2026).

**Template fields**: criteria and weights; each score with evidence note; confidence; dependency list; time horizon (near, medium, long: HBR-2026); expected time to impact; data readiness (MSFT-PLAN-2026 maturity table: skills required, data readiness, feasible use cases); risk tier.

**Decision rules and thresholds**
- Rank by fixed criteria; when capacity opens, take the highest-scoring item that has passed its gate (HBR-2026).
- Weight toward readiness: BCG-2024 reports about 70% of implementation challenges are people and process; use this as a reason to give change readiness at least as much weight as technical feasibility **(proposed default for weights; BCG gives the challenge split, not a scoring weight)**.
- Payback hurdle: do not default to the seven to 12 months typical for technology investment; Deloitte respondents mostly expect two to four years for a typical AI use case (DELOITTE-2025). Use AI-type-specific hurdles (generative vs agentic: 85% of ROI Leaders do, per DELOITTE-2025).
- Spend thresholds that trigger heavier governance, taken from UK government practice as an example of a rule, not a universal number: a five-part business case typically for investment approaching GBP 10 million, and assurance for digital and technology spend above GBP 100,000 (public-facing) or GBP 1 million (other) (UKGOV-2025, "AI business cases").

### Stage gates

**Stages (HBR-2026)**: Opportunity (Outline), Design and Partnership (Partner), Experimental/Prototyping (Experiment), Scale and Operate (Navigate). Cooper's original stages for comparison: Discovery, Concept, Business Case, Development, Testing and Validation, Launch (COOPER-STAGEGATE-n.d.).

**Gate tests by stage (HBR-2026)**
- Gate 1 (after Outline): strategic fit and technical feasibility.
- Gate 2 (after Design and Partnership): data available and governed; skills in place or sourced; ethics and security controls defined; business case still compelling.
- Gate 3 (after Experiment): rigorous system testing and red-team scrutiny.
- Navigate stage: guardrails against misuse, cost-tracking for total cost of ownership, measure actual mission impact.

**Gate structure (COOPER-STAGEGATE-n.d.)**: deliverables defined in advance; criteria of readiness and value; outputs Go, Kill, Hold or Recycle; a Go confirms resources for the next stage, timeline, deliverables and next gate date; named gatekeepers who control the needed resources.

**Template fields (gate record)**: item; gate number; deliverables presented; criteria scores; decision (Go/Kill/Hold/Recycle/Redirect); resources released (budget, headcount, person-days); conditions; next gate date; kill or stop criteria agreed now **(proposed default)**; decision-log entry with actions, owners, dates (UMBREX-n.d., secondary).

**Decision rules**
- A Go without resources named is incomplete (COOPER-STAGEGATE-n.d.).
- Lighter path for low-risk items (UMBREX-n.d.; HBR-2026 utility example; OMB-2025 streamlining).
- For regulated or high-impact items, minimum practices and independent review as in OMB-2025 (high-impact determination; "Implementing Risk Management Practices and Termination of Non-Compliant AI") and NIST-2023 (MANAGE 1.1: determine whether the system achieves its intended purposes and whether development or deployment should proceed).

### Portfolio review

**Cadence**: no source prescribes a cadence for AI portfolio reviews. HBR-2026 says "regular reviews"; Microsoft's CoE guidance suggests monthly progress reviews with sponsors for the CoE's steering committee (MSFT-COE-2026, "Secure executive sponsorship"). A monthly review with a quarterly rebalance is **(proposed default)**.

**Attendees and decisions**: HBR-2026 describes Lloyds' forum as cross-functional; Microsoft recommends a steering committee of business and IT leaders. Decisions listed in HBR-2026: add promising initiatives, scale successful pilots, redirect struggling efforts, retire misaligned projects, recalibrate scoring criteria.

**Pack (fields)**: pipeline by stage with counts; items passing or failing gates since last review; early-warning flags (slippage, cost overrun, performance shortfall: HBR-2026); balance across time horizons, risk and return, capability areas (HBR-2026); capacity and dependencies; benefits to date versus forecast by item (IVI-ITCMF-n.d.); run-cost and cost constraints (MCK-2026: about 20% of respondents constrained by operating costs); inventory changes and decommissioning (NIST-2023).

### Stop or redirect

**Outcomes**: Kill, Hold, Recycle, Redirect (scope, approach or risk treatment) (COOPER-STAGEGATE-n.d.; UMBREX-n.d.), plus retire misaligned projects and switch use cases after a technology change (HBR-2026).

**Checklist**: reasons recorded in the gate log; dependencies and users notified; decommissioning procedure and fallback so critical services continue (UKGOV-2025 "fallback processes"; NIST-2023 GOVERN 1.7); lessons captured and reusable assets kept (AUSGOV-2013); benefits expected but not achieved recorded (IVI-ITCMF-n.d.).

**Evidence that should drive a stop (from the sources)**: data not available or not good enough, inadequate risk controls, escalating costs, unclear business value (the four causes in GARTNER-2024 and the three in GARTNER-2025); performance below an appropriate level for high-impact AI (OMB-2025); unacceptable risks or harms identified (UKGOV-2025 "review and change processes": make changes to or decommission AI systems).

**Decision rule (proposed default)**: no stop on early P&L absence alone before the planned review point, given the J-curve (NBER-2020) and the two-to-four-year payback finding (DELOITTE-2025); stop on repeated missed gate criteria or loss of a named owner.

### Value tracking

**Template fields (benefits register)**, drawn from AUSGOV-2013 (Gate 5 Key Focus: Business Case and Benefits Management) and IVI-ITCMF-n.d.: benefit id; description and link to project objective; type (interim, direct, indirect, disbenefit: AUSGOV-2013); financial or non-financial; owner; baseline value and source; target and date; measure and measurement method; counterfactual (control group, A/B, baseline; DBS approach in FCC-2026); collection method and timing; dependencies on other benefits; forecast versus actual by period; confidence; status; review dates; redeploy or reduce decision on freed capacity **(proposed default; sources only say productivity is hard to translate to financial benefit: GARTNER-2024)**.

**Portfolio-level metrics (IVI-ITCMF-n.d.)**: share of projects with a benefits owner; share reviewed after go-live; benefit success rate (share of targeted benefits actually achieved); share of business cases that are benefits-led.

**Review points**: post-implementation review within six months of completion is an IVI metric; the Australian Gate 5 review follows the post-implementation review (IVI-ITCMF-n.d.; AUSGOV-2013).

**PE variant**: link each initiative to the value creation plan line and the EBITDA bridge (BAIN-2026-PE sets the context: faster EBITDA growth is needed). PARTNERS-2026 gives the only quantified PE AI example found: 120 bps and USD 10 million EBITDA at one company, self-reported.

---

## 9. Sources

Access: **full** = the page or document was fetched and read (the source named is what I read). **mirror** = fetched through the r.jina.ai text mirror because the site blocked curl. **secondary** = I read a news report of the primary document, not the document. **search-only** = seen only as a search result; none of these figures are used as outcomes. **abstract** = abstract or metadata only.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| MCK-2026 | The state of AI in 2026: On the road to ROI | McKinsey & Company (QuantumBlack) | Consultancy survey report | https://www.mckinsey.com.br/en/our-insights/the-state-of-ai | 2026-08-25 (mirror header) | full (mirror) |
| BCG-2025 | The Widening AI Value Gap (Are You Generating Value from AI?) | Boston Consulting Group | Consultancy research | https://www.bcg.com/publications/2025/are-you-generating-value-from-ai-the-widening-gap | 2025-09-30 (mirror header) | full (mirror), introduction only |
| BCG-2024 | AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value (press release for "Where's the Value in AI?") | Boston Consulting Group | Consultancy press release | https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value | 2024-10-24 | full (mirror) |
| DELOITTE-2025 | AI ROI: The paradox of rising investment and elusive returns | Deloitte | Consultancy survey report | https://www.deloitte.com/global/en/issues/generative-ai/ai-roi-the-paradox-of-rising-investment-and-elusive-returns.html | 2025-10-22 (mirror header) | full (mirror) |
| IBM-2025 | IBM Study: CEOs Double Down on AI While Navigating Enterprise Hurdles | IBM Newsroom (IBM Institute for Business Value CEO study) | Vendor press release | https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles | 2025-05-06 | full (press release; the study page was not retrievable) |
| GOOGLE-2025 | The ROI of AI 2025 | Google Cloud with National Research Group | Vendor survey report (PDF) | https://services.google.com/fh/files/misc/google_cloud_roi_of_ai_2025.pdf | 2025 (fieldwork Apr-Jun 2025; month of publication not stated in text read) | full |
| WHARTON-2025 | Accountable Acceleration: Gen AI Fast-Tracks into the Enterprise (Year Three Full Report) | Wharton Human-AI Research and GBK Collective | Academic-industry survey report (PDF) | https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf | 2025-10 | full |
| MITNANDA-2025 | The GenAI Divide: State of AI in Business 2025 | Challapally, Pease, Raskar, Chari (MIT Project NANDA) | Research report (PDF, preliminary findings) | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf | 2025-07 | full (copy hosted by mlq.ai) |
| RAND-2024 | The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed | RAND Corporation (author names not captured in the fetched text) | Research report | https://www.rand.org/pubs/research_reports/RRA2680-1.html | 2024-08-13 | full (mirror) |
| GARTNER-2024 | Gartner Predicts 30% of Generative AI Projects Will Be Abandoned After Proof of Concept By End of 2025 | Gartner | Analyst press release | https://www.gartner.com/en/newsroom/press-releases/2024-07-29-gartner-predicts-30-percent-of-generative-ai-projects-will-be-abandoned-after-proof-of-concept-by-end-of-2025 | 2024-07-29 | full (mirror) |
| GARTNER-2025 | Over 40% of Agentic AI Projects Will Be Scrapped by 2027, Says Gartner (news report of Gartner's 25 Jun 2025 release) | Outlook Business | News report | https://www.outlookbusiness.com/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner | 2025-06-25 | secondary (Gartner original returned 403) |
| CIODIVE-2025 | AI project failure rates are on the rise: report (reporting S&P Global Market Intelligence) | CIO Dive (Lindsey Wilkinson) | News report | https://www.ciodive.com/news/ai-project-fail-data-SPGlobal/742590/ | 2025-03-14 | secondary (S&P original returned 403) |
| NAO-2024 | Use of artificial intelligence in government | UK National Audit Office | Audit report (PDF) | https://www.nao.org.uk/wp-content/uploads/2024/03/use-of-artificial-intelligence-in-government.pdf | 2024-03-15 | full |
| UKGOV-2025 | Artificial Intelligence Playbook for the UK Government (HTML) | UK Government Digital Service / DSIT | Government guidance | https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html | 2025 (Crown copyright 2025; month not read) | full |
| OMB-2025 | M-25-21, Accelerating Federal Use of AI through Innovation, Governance, and Public Trust | US Office of Management and Budget | Government memorandum (PDF) | https://www.whitehouse.gov/wp-content/uploads/2025/02/M-25-21-Accelerating-Federal-Use-of-AI-through-Innovation-Governance-and-Public-Trust.pdf | 2025-04-03 | full |
| NIST-2023 | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | US National Institute of Standards and Technology | Standard-setter framework (PDF) | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 2023-01 | full |
| MSFT-COE-2026 | Establish an AI Center of Excellence (Cloud Adoption Framework) | Microsoft Learn | Vendor practitioner guidance | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence | last updated 2026-04-10 | full |
| MSFT-PLAN-2026 | Plan for AI adoption (Cloud Adoption Framework) | Microsoft Learn | Vendor practitioner guidance | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/plan | last updated 2026-10-15 | full |
| HBR-2026 | Manage Your AI Investments Like a Portfolio (Nelson, Davenport, Scade) | Harvard Business Review (read via AAPL reprint) | Practitioner article | https://www.physicianleaders.org/articles/manage-your-ai-investments-like-a-portfolio (source link given there: https://hbr.org/2026/01/manage-your-ai-investments-like-a-portfolio) | HBR 2026-01 (URL path); reprint dated 2026-02-25 | full (reprint) |
| HBR-2018 | Artificial Intelligence for the Real World (Davenport and Ronanki) | Harvard Business Review | Practitioner article | https://hbr.org/2018/01/artificial-intelligence-for-the-real-world | Jan-Feb 2018 | full for the introduction only (paywalled) |
| COOPER-STAGEGATE-n.d. | The Stage-Gate Model: An Overview (Robert G. Cooper) | Stage-Gate International | Method source, author article | https://www.stage-gate.com/blog/the-stage-gate-model-an-overview/ | undated (cites works to 2023) | full |
| UMBREX-n.d. | Stage-gate project governance model | Umbrex | Secondary framework summary | https://umbrex.com/resources/frameworks/organization-frameworks/stage-gate-project-governance-model/ | undated | full; secondary |
| NBER-2020 | The Productivity J-Curve: How Intangibles Complement General Purpose Technologies (Brynjolfsson, Rock, Syverson), NBER WP 25148 | National Bureau of Economic Research | Academic working paper (PDF) | https://www.nber.org/system/files/working_papers/w25148/w25148.pdf | Oct 2018, rev. Jan 2020 | full (read abstract and front matter) |
| IVI-ITCMF-n.d. | Benefits Harvesting (IT-CMF 18.07, Value) | Innovation Value Institute | Maturity-model guidance | https://portal.ivi.ie/+itcmf/18.07/value/BAR/C/C3 | undated (framework version 18.07) | full |
| AUSGOV-2013 | Information Sharing Lessons Learned from Gateway Reviews: Gate 5, Benefits Realisation Review | Australian Government, Department of Finance | Government guidance (PDF) | https://www.finance.gov.au/sites/default/files/2019-11/Gate_5_-_Lessons_Learned.pdf | 2013-10 (file posted 2019-11-06) | full (mirror) |
| BAIN-2026-PE | Global Private Equity Report 2026 | Bain & Company | Consultancy report (PDF) | https://www.bain.com/globalassets/noindex/2026/bain-report_global-private-equity-report-2026.pdf | 2026 | full |
| BAIN-2026-TECH | Technology Report 2026 (landing page) | Bain & Company | Consultancy report summary | https://www.bain.com/insights/topics/technology-report/ | 2026 | full for the landing page only |
| PARTNERS-2026 | Partners Group drives EBITDA margin uplift through AI collaboration between private equity portfolio companies | Partners Group (via Deutsche Boerse press feed) | PE firm press release | https://live.deutsche-boerse.com/news/Partners-Group-drives-EBITDA-margin-uplift-through-AI-collaboration-between-private-equity-portfolio-companies-a1ffb3cd-e01e-4242-a263-2626ccb76132 | 2026-08-03 | full |
| DBS-2026 | DBS named Asia's Best Digital Bank by Euromoney, recognised for its AI leadership and responsible innovation | DBS Bank | Company newsroom release | https://www.dbs.com/newsroom/DBS_named_Asias_Best_Digital_Bank_by_Euromoney_recognised_for_its_AI_leadership_and_responsible_innovation | 2026-07-20 | full |
| FCC-2026 | DBS says AI push is paying off as it shifts from efficiency tool to growth engine (Business Times reprint) | Business Times via French Chamber of Commerce in Singapore | News report | https://www.fccsingapore.com/news/n/news/dbs-says-ai-push-is-paying-off-as-it-shifts-from-efficiency-tool-to-growth-engine.html | 2026-02-09 | secondary |
| FORRESTER-2026 | DBS Bank's Billion-Dollar AI Dream, Realized | Forrester (blog) | Analyst blog | https://www.forrester.com/blogs/dbs-banks-billion-dollar-ai-dream-realized | 2026-01-22 | full |
| AWS-CAF-2024 | AWS Cloud Adoption Framework for AI, ML and Generative AI | Amazon Web Services | Vendor whitepaper | https://docs.aws.amazon.com/whitepapers/latest/aws-caf-for-ai/aws-caf-for-ai.html | 2024-02-13 | full (landing page only; little portfolio content, not used for claims) |
| ARXIV-MCCLURE-2026 | Why AI Readiness Is an Organizational Learning Problem, Not a Technology Purchase (McClure, Gerdau) | arXiv 2604.16369 | Preprint, literature synthesis (not peer reviewed) | https://arxiv.org/abs/2604.16369 | 2026-03-22 | abstract |
| ARXIV-HUWYLER-2025 | The Risk-Adjusted Intelligence Dividend (Huwyler) | arXiv 2511.21975 | Preprint (not peer reviewed) | https://arxiv.org/abs/2511.21975 | 2025-11-26 | abstract |
| ARXIV-COSTA-2026 | The Deployment Wall (Costa) | arXiv 2607.29089 | Preprint (not peer reviewed) | https://arxiv.org/abs/2607.29089 | 2026-07-31 | abstract |
| MCK-2025 | The state of AI in 2025: Agents, innovation, and transformation | McKinsey & Company | Consultancy survey report | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 2025 | search-only (figures 39% EBIT impact, 6% high performers seen in a search summary; not used as outcomes) |
| CROSSREF-COOPER | Cooper and Sommer, "Dynamic Portfolio Management for New Product Development", Research-Technology Management 66(3), 2023; Cooper, "Expected Commercial Value...", IEEE EMR 51(2), 2023 | Taylor & Francis; IEEE (via Crossref metadata) | Academic papers | https://doi.org/10.1080/08956308.2023.2183004 ; https://doi.org/10.1109/EMR.2023.3267328 | 2023-04-20 ; 2023-06-01 | abstract (metadata only; papers not read; cited in COOPER-STAGEGATE-n.d.) |
| COOPER-RG | Cooper and Edgett, portfolio management studies ("Picking the Winners" and others) | ResearchGate listings | Academic / practitioner papers | https://www.researchgate.net/publication/237829790_Portfolio_Management_for_New_Products_Picking_The_Winners | n.d. | search-only (a search summary reported 76% of businesses with too many projects and 21% of portfolios with high-value projects; unverified and not used) |

Count of distinct sources read in full or substantially (access full or secondary): 31; plus 3 abstract-only preprints, 1 landing-page read (AWS), and 4 search-only or metadata items not used for claims.

Source types read: consultancy and research-firm publications (McKinsey, BCG x2, Deloitte, Gartner x2, Bain x2, Google Cloud, IBM); academic or academic-industry (Wharton, MIT NANDA, NBER, RAND, arXiv x3); government and standard-setter (NAO, UK Playbook, OMB, NIST, Australian Gateway); professional and practitioner method (Cooper Stage-Gate, HBR x2, IVI, Microsoft x2, Umbrex); company and case write-ups (DBS x3, Partners Group); news reports (Outlook Business, CIO Dive).

---

## 10. Gaps

- **Professional-body guidance.** PMI's portfolio standard, ISO 21504 and APM benefits guidance were not reachable (403, 404 or not found). I used UK government and Australian Gateway guidance as stand-ins; neither is AI-specific. The Australian Gate 5 text is from 2013.
- **Books.** The books named in the topic (Cooper's portfolio work and "Winning at New Products") were reached only through Cooper's own overview article. The Cooper portfolio studies (including the often-quoted share of businesses with too many projects) were seen only as a search summary and are not used.
- **Original publications blocked.** Gartner's agentic press release and S&P Global's survey were blocked; I used news reports of them (secondary), so the exact wording and sample details are not verified. McKinsey's 2025 report was blocked; the 2026 report was read in full through a regional mirror.
- **Missing evidence.** No source gives stage-gate pass rates, kill rates, time in stage, or benefits-realized-versus-forecast rates for an enterprise AI portfolio. No independent audit of AI benefits was found. Every pilot-to-production figure is a survey perception, an interview-based estimate or a forecast, each with different definitions of "production" and "success".
- **Portfolio review mechanics.** No source specifies a standard attendee list, pack contents or cadence. The HBR-2026 and Microsoft guidance are the only prescriptions found; cadence and the 10-20-70-style weights in section 8 are marked as proposed defaults.
- **Redeploy-or-reduce.** I found no source on how organizations decide between redeploying and reducing freed capacity after an AI launch. McKinsey 2026 reports that 14% of respondents saw an AI-related decline in workforce size in the past year versus 32% who had expected one the year before; that is workforce effect, not a decision method.
- **Knowledge-work and professional-services specifics.** None of the sources reports portfolio governance or value tracking at an audit, legal, consulting or advisory firm. DBS (banking), a utility, Lloyds (banking), and an insurance brokerage under PE ownership are the nearest cases.
- **PE value-creation tracking.** Only one quantified AI example (PARTNERS-2026, self-reported) and Bain's fund-economics context were found. How PE operating partners register, review and report AI initiatives across portfolio companies is not documented in the sources reached; several trade-press and vendor pages found in search made unsupported EBITDA claims and were not used.
- **Lloyds and the utility.** Both are known only from HBR-2026; the article gives no volumes or outcomes, and the utility is anonymized.
- **Discourse.** No conference session, panel, podcast or webinar was fetched; the discourse angle is represented only by HBR-2026, Forrester and Bain commentary. MIT SMR and BCG's "Emerging Agentic Enterprise" (Nov 2025) returned only front matter.
- **Preprints.** The three arXiv items are abstract-only, not peer reviewed, and mostly synthesize the same industry surveys; they are listed but not relied on for any figure.
- **Landing AI's AI Transformation Playbook** (Ng) was not reachable at the URLs tried.
