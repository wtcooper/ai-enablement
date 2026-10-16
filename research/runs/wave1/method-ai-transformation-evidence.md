# Method topic: ai-transformation-frameworks-evidence

Research date: 2026-10-16. Stream M (method topic). Feeds the advisor phases: onboarding, frame, reimagine, prioritize.

**Scope:** current frameworks and hard evidence on enterprise AI transformation, 2024 to 2026. The questions are what separates organizations capturing value from those stuck in pilots, workflow redesign versus tool rollout, operating model choices (central CoE versus federated), governance, where value shows up by function, and how leaders set ambition.

**How to read the evidence tags used throughout.**

| Tag | Meaning |
|---|---|
| `M-exp` | Measured: randomized trial, field experiment, matched administrative or payroll data |
| `M-tel` | Measured: platform telemetry (Anthropic usage data). It records behavior on one vendor's platform, not outcomes |
| `S` | Survey of self-reported attributions, perceptions or practices. Respondents judge their own results |
| `F` | Forecast or stated expectation |
| `G` | Guidance, framework or opinion, including heuristics such as 10-20-70 |

**Access notes.** The `curl`/`pdftotext` route worked for most sources. mckinsey.com, pwc.com, bcg.com web pages, gartner.com, rand.org and hbs.edu all refused or failed from this environment. The McKinsey State of AI 2025 PDF was read through a third-party copy. PwC's CEO Survey was read through the distributed press release. The web-search budget ran out partway through the run, so some planned book and practitioner sources were not reached (see Gaps). Sources marked `search-only` in section 9 appear only in notes and never carry an A or B claim.

**A caution on moves.** The sources report what organizations did and what correlates with value. Section 3 turns those findings into advisor moves. The source ref marks the evidence behind a move. It does not mean the source prescribes the move word for word.

---

## 1. Summary

- **Breadth is far ahead of depth, and most of the evidence agrees.** McKinsey's 2025 survey (n=1,993) finds 88% of respondents report regular AI use in at least one function, but only 7% are fully scaled and 31% are scaling. 39% attribute any EBIT impact to AI, and most of those say under 5%. PwC's 2026 CEO survey (n=4,454) finds 12% of CEOs report both cost and revenue gains and 56% report neither. BCG (n=1,250) classes 5% of firms as "future-built" and 60% as getting no material value. [MCKINSEY-STATEOFAI-2025; PWC-CEO-2026; BCG-VALUEGAP-2025]
- **The most consistent differentiator is a redesigned workflow, plus ambition set by senior leaders.** McKinsey's high performers (about 6% of respondents) were 55% likely to report fundamentally redesigned workflows against 20% for others. They were far more likely to set growth and innovation objectives alongside efficiency (about 80% versus about 50%). BCG says the biggest value comes from reshaping core workflows end to end, not from pilots or isolated use cases. All of this is correlational and self-reported. [MCKINSEY-STATEOFAI-2025 Exh. 10, 11; BCG-VALUEGAP-2025 p. 4]
- **Tool rollout alone mostly improves individual productivity, not P&L.** MIT NANDA's interview-based study says general-purpose chat tools are widely used while task-specific enterprise tools rarely reach production. Deloitte's 2026 survey found education, not role or workflow redesign, was the most common talent adjustment. Controlled studies show real task-level gains (14% in customer support) and real null results (no earnings or hours effect in Denmark; a 19% slowdown in an RCT of experienced developers). [MIT-NANDA-2025; DELOITTE-STATEAI-2026; NBER-BRYNJOLFSSON-2023; BFI-HUMLUM-2025; METR-2025]
- **Operating model evidence is thin and mostly correlational.** BCG finds exclusive IT ownership is a marker of stagnating firms, and future-built firms favour shared business-IT ownership with central steering and decentralized execution. MIT says successful buyers decentralize implementation authority while keeping accountability. The practitioner guide (Microsoft CAF) says to centralize early, then shift the CoE to an advisory role. No source here measures outcomes for CoE versus federated models directly. [BCG-VALUEGAP-2025 pp. 12-15; MIT-NANDA-2025 §6.1; MSFT-CAF-COE]
- **Value shows up first in structured, measurable work.** Software engineering, IT, manufacturing and service operations lead reported cost decreases. Marketing and sales, strategy and corporate finance, and product development lead reported revenue increases (McKinsey, self-reported). Stanford's 2026 AI Index summarises studies with gains of 14-15% in customer support and 26% in software development, smaller for deeper reasoning. MIT and BCG disagree on whether front-office or back-office has the better returns, and the two measure different things. [MCKINSEY-STATEOFAI-2025 Exh. 7, 8; STANFORD-AIINDEX-2026; MIT-NANDA-2025 §6.3; BCG-VALUEGAP-2025 p. 7]
- **Governance is lagging the move to agents.** Deloitte reports only about one in five companies has a mature governance model for autonomous agents. BCG reports 72% of companies have unmanaged AI-security risks. McKinsey reports 51% of AI-using respondents experienced at least one negative consequence. [DELOITTE-STATEAI-2026; BCG-VALUEGAP-2025 p. 10; MCKINSEY-STATEOFAI-2025 Exh. 19]
- **"10-20-70" is a BCG rule of thumb, not a measured law.** It says 70% of strategic focus should go to people and processes, 20% to technology and 10% to algorithms. BCG's supporting data is a list of challenges respondents named, with people and process items among the most frequent. [BCG-VALUEGAP-2025 pp. 17-18]
- **Headline ROI numbers conflict, mostly because of who answers and how success is defined.** EY (n=500 US senior leaders) reports 97% of AI-investing leaders see positive ROI. Wharton/GBK reports 74%. IBM's CEO study reports 25% of initiatives delivered expected ROI. PwC reports 12% with both cost and revenue gains. The advisor should always ask for the definition and base before quoting any of them.

---

## 2. Core concepts in plain language

1. **Adoption is not transformation.** "We use AI" means people or functions have tried tools. Transformation means work changed and a business measure moved. Across McKinsey, MIT, PwC and BCG the gap between these two is the central finding. For knowledge work, the common failure is a licence rollout (assistants for drafting and summarizing) that raises individual output a little while the process, handoffs and review steps stay the same. For the advisor, every status claim should be split into who uses it, which workflows changed, and what measure moved.

2. **The workflow is the unit of value.** BCG calls workflows "the core unit of value creation" and says agents bolted onto legacy processes underperform. McKinsey's survey ranks intentional workflow redesign among the strongest of the factors it tested. Hammer's classic 1990 HBR argument ("don't automate, obliterate") is the same idea applied to older technology. In knowledge work, this means mapping a piece of work end to end (intake, research, drafting, review, delivery) before deciding where AI goes. It also means being willing to remove steps rather than speed them up.

3. **Ambition decides how much of the workflow gets reconsidered.** McKinsey's high performers set growth and innovation objectives alongside efficiency. BCG's future-built firms have a multiyear, CEO-sponsored ambition with explicit cost and revenue targets. An efficiency-only target tends to produce step improvements. A growth target gives permission to redesign. Leaders who delegate AI to middle management with no stated value ambition are BCG's typical laggard. This is the survey correlation. It does not prove that raising ambition causes value.

4. **Operating model: shared ownership, central standards, decentralized execution.** The recurring pattern in BCG, McKinsey and MIT is business and IT sharing accountability, a central platform and set of standards, and execution close to the work. Centralized expertise (a CoE) is common early. Microsoft's guide says it should become an advisory function as adoption matures, once governance is built into the platform. Whether this beats a fully federated model has not been measured in these sources.

5. **The learning loop.** MIT NANDA's central claim is that enterprise tools stall because they do not retain feedback, adapt to context or improve with use. This is the authors' interpretation of interviews and a survey of 153 leaders. Its practical form for an advisor is to ask how a workflow's corrections, edge cases and exceptions flow back into the system.

6. **The jagged frontier and human-in-the-loop design.** AI is strong on some tasks and unreliable on others that look similar. The Harvard/BCG experiment showed large gains on tasks inside the frontier. METR's trial showed a slowdown on experienced developers' own mature codebases, even though they believed they were faster. McKinsey's high performers were much more likely to have defined processes for when outputs need human validation. For knowledge work, testing on real work samples beats trusting demos or user perceptions.

7. **Measurement and the J-curve.** Self-reported ROI, productivity and EBIT attribution differ a lot across surveys. Brynjolfsson, Rock and Syverson argue general-purpose technologies require complementary intangible investments (new processes, skills, business models) before gains appear in measured productivity. That is a theory with historical evidence for earlier technologies. It is consistent with the lag in the AI data, but the AI-specific evidence is not yet conclusive.

8. **Governance as an enabler that has to keep pace.** Deloitte reports that organizations where senior leaders shape AI governance get more business value than those that delegate it to technical teams (the page gives no figure). Its guidance is to integrate with existing risk structures, not to create a parallel function. The evidence for agent governance is that most organizations have not built it yet.

9. **Where the value sits depends on the measure.** McKinsey asks about use-case-level cost and revenue effects. BCG asks respondents to estimate where AI value potential sits (70% in core functions). MIT documents cases and finds large back-office savings alongside a bias of spending toward sales and marketing. These are not contradictions, but they are different questions. The advisor should state which question a figure answers.

---

## 3. Expert moves

Format: **move**, when to use it, what it reveals, source ref (with locator).

1. **Ask "what would you have to see in twelve months to call this a success, in P&L or KPI terms?"** When framing. Reveals whether the ambition is efficiency only or includes growth or innovation. McKinsey high performers: 84% efficiency, 82% growth, 79% innovation objectives versus 80%, 50%, 50% for others. BCG future-built firms set cost and revenue targets from top management. [MCKINSEY-STATEOFAI-2025 Exh. 10; BCG-VALUEGAP-2025 p. 3]

2. **Ask "which piece of work, from intake to delivery, would you rebuild if the tools were free?" before asking which tools they want.** When framing and early reimagine. Reveals whether the leader thinks in workflows or in tools. Redesign: 55% of high performers versus 20% of others reported fundamentally redesigned workflows. [MCKINSEY-STATEOFAI-2025 Exh. 11; BCG-VALUEGAP-2025 p. 4]

3. **Split every status claim into three numbers: who uses it, which workflows changed, what measure moved.** At onboarding. Reveals the adoption-versus-impact gap. 88% regular use but 39% with any EBIT attribution. [MCKINSEY-STATEOFAI-2025 p. 3, Exh. 6; MIT-NANDA-2025 §3]

4. **Ask which AI tools people actually use for work, including personal accounts.** At onboarding and when assessing the current state. Reveals shadow usage, likely champions and what good looks like to staff. MIT reports workers at over 90% of surveyed companies used personal AI tools while about 40% of companies had bought an official LLM subscription. [MIT-NANDA-2025 §3.3]

5. **Ask how much the senior sponsor personally uses AI in their own work.** At onboarding with a leader or head of a practice. Reveals real sponsorship versus delegation. BCG: nearly all C-level leaders at future-built firms actively use AI daily. McKinsey: high performers were three times as likely to strongly agree that senior leaders demonstrate ownership and commitment. [BCG-VALUEGAP-2025 p. 12; MCKINSEY-STATEOFAI-2025 Exh. 13]

6. **Ask who owns the outcome: the business, IT or both, and with what decision rights.** When framing the operating model. Reveals the stagnating pattern of IT-only ownership. More than 40% of future-built firms embed shared business-IT ownership in governance versus 19% of stagnating firms. [BCG-VALUEGAP-2025 p. 12, Exh. 7]

7. **Run a department-wide inventory of activities, volumes and resources, then rank candidates on a value-by-feasibility matrix.** When prioritizing. Reveals the few workflows worth redesigning, and avoids scattering effort. A BCG consumer-products case used a department-wide survey of campaigns and resources to build a feasibility matrix. BCG reports future-built and scaling firms match deployment to impact 76% better. [BCG-VALUEGAP-2025 p. 14]

8. **Place each candidate task on the "jagged frontier" with a quick trial on real work samples.** When prioritizing and choosing a lens. Reveals tasks where AI helps, where it fails quietly, and where staff over-trust it. In the Harvard/BCG experiment (758 consultants), performance was much better inside the frontier. [HBS-JAGGED-2023]

9. **Compare perceived and measured effect on a small before-and-after or A/B sample.** When a team says a tool "saves hours". Reveals perception gaps. METR's developers expected a 24% time reduction and believed afterwards they had saved 20%, but measured time rose 19%. [METR-2025 abstract]

10. **Ask frontline staff which tasks they would hand over, keep, or share, and how much human involvement they want.** When choosing between improve-the-step and automate-the-flow. Reveals green-light tasks (wanted and feasible) and red-light tasks (feasible but resisted). In the Stanford WORKBank audit workers had positive attitudes toward automation on 46.1% of tasks. For 45.2% of occupations, equal human-AI partnership (H3) was the dominant preferred level. [STANFORD-WORKBANK-2026 §1 findings 1, 3]

11. **Screen candidate tasks into four zones: wanted and feasible, feasible but unwanted, wanted but not yet feasible, neither.** When prioritizing. Reveals where investment would meet resistance or be premature. In the same audit, 41.0% of Y Combinator company-task mappings sat in the low-priority and red-light zones. [STANFORD-WORKBANK-2026 §1 finding 2]

12. **Start at the edge of a workflow with a narrow, simple-to-execute task and expand into the core.** When picking a first wave. Reveals a realistic first win. MIT's sample: narrow-scope, simple-execution tasks (spend categorization, contract review) were fast wins. Full procurement orchestration was at the failing end of its two-by-two. [MIT-NANDA-2025 §5.2.1]

13. **Ask "how will this learn from our corrections?"** When evaluating any tool or custom build. Reveals whether feedback loops exist. MIT's interviewees named "doesn't learn from our feedback" and "can't customize to our workflows" among the main barriers to using tools in core work. This is the authors' reading of interviews. [MIT-NANDA-2025 §4.3]

14. **Agree outcome metrics before the pilot starts, with leading indicators tied to one lagging financial KPI.** When prioritizing and before any pilot. Reveals whether value can ever be shown. BCG: more than 60% of future-built firms rigorously track AI value versus 17% of stagnating firms. KPMG: 78% of surveyed leaders say traditional business metrics do not capture AI's full impact. [BCG-VALUEGAP-2025 p. 14; KPMG-AIPULSE-Q3-2025]

15. **Ask "where does the saved time go?"** When a team reports efficiency gains. Reveals whether capacity is captured, redeployed or absorbed. Danish matched data show about 3% average reported time savings with no earnings or hours effect. A US survey puts time savings at 1.4% of total work hours. EY: of firms with gains, 17% cut headcount and 47% reinvested in existing AI capabilities. [BFI-HUMLUM-2025 abstract; NBER-BICK-2025 abstract; EY-AIPULSE-DEC-2025]

16. **Ask where in the workflow a person validates output, using what criteria.** When reimagining. Reveals missing quality gates. McKinsey names defined human-validation processes among the top factors separating high performers (chart labels read about 65% versus 23%). [MCKINSEY-STATEOFAI-2025 Exh. 14]

17. **Ask which risks the team has actually experienced, and which they mitigate.** When framing governance. Reveals the maturity of controls. 51% of AI-using McKinsey respondents reported at least one negative consequence, about one-third from inaccuracy. High performers reported more consequences and more mitigation. [MCKINSEY-STATEOFAI-2025 Exh. 19 and text]

18. **Ask whether the governance model reuses existing risk and oversight structures or sits beside them.** When setting up or reviewing governance, especially for agents. Reveals shadow governance. Deloitte's guidance favors integration with existing structures. About one in five companies has a mature agent governance model. [DELOITTE-STATEAI-2026]

19. **Ask whether the use case needs an agent at all, or whether simpler automation fits.** When someone proposes agents. Reveals fashion-driven choices. BCG says agents are the next step, not the starting point. It lists prerequisites as data foundations, scaled AI capabilities and clear governance. [BCG-VALUEGAP-2025 p. 9]

20. **Ask about data readiness for the specific workflow, especially unstructured documents.** When mapping candidates. Reveals the real blocker. 79% of BCG respondents named lack of expertise to manage unstructured data. 82% of KPMG's surveyed leaders named data quality as a critical barrier. Anthropic suggests dispersed, undigitized context may hold back enterprise deployment, as a hypothesis. [BCG-VALUEGAP-2025 Exh. 10; KPMG-AIPULSE-Q3-2025; ANTHROPIC-EI-SEP-2025 ch. on 1P API]

21. **Ask how central funding and local accountability are split.** When designing the operating model. Reveals whether the business has skin in the game. One BCG retail executive describes central capital allocation with business-carried amortization. This is a single case. [BCG-VALUEGAP-2025 p. 15]

22. **Probe the build, buy or partner split rather than prescribing one.** When prioritizing. Reveals the leader's assumptions and capability. The sources conflict. BCG: 11% rely primarily on in-house development and 4% on a single vendor. MIT: externally partnered tools reached deployment about 67% of the time versus about 33% for internal builds, with the authors warning of confounding. EY: more leaders (64% versus 56% a year earlier) are building custom solutions in-house. [BCG-VALUEGAP-2025 p. 16; MIT-NANDA-2025 §6.1; EY-AIPULSE-JUL-2025]

23. **Ask where champions already are: power users and budget holders close to the work.** When planning how to find use cases. Reveals bottom-up demand. MIT says strong deployments often began with power users and domain managers surfacing problems, not with a central lab. This is interview evidence from the authors' sample. [MIT-NANDA-2025 §6.2]

24. **Ask what happens to junior roles and how juniors will learn if AI takes the practice tasks.** In any knowledge-work unit. Reveals pipeline and skill-atrophy risk. 43% of leaders in Wharton's survey warn of skill atrophy. Payroll data show employment for ages 22-25 in AI-exposed occupations 19% below trend, concentrated where AI substitutes for tasks. That is descriptive, not causal. [WHARTON-GBK-2025 exec. summary; STANFORD-CANARIES-2026 abstract]

25. **Triangulate any ROI claim: ask who was surveyed, what "positive ROI" meant, and what the base was.** Whenever a benchmark is quoted. Reveals why numbers differ (see Evidence, rows on ROI). [EY-AIPULSE-JUL-2025; WHARTON-GBK-2025; IBM-CEO-2025; PWC-CEO-2026]

26. **Check that change plans include role and workflow redesign, not only training.** When reviewing a transformation plan. Reveals the "education only" trap. Deloitte: 53% educate the workforce to raise fluency, 48% upskill and reskill, 33% redesign career paths. Education, not role or workflow redesign, was the top adjustment. [DELOITTE-STATEAI-2026]

27. **Ask for last month's actual volumes and exception rates for the candidate workflow.** When mapping. Reveals variation and hidden rework that a "typical week" hides. This is a general practitioner move. The BCG marketing case's activity inventory supports the inventory step only, not this specific question. [BCG-VALUEGAP-2025 p. 14]

---

## 4. Question bank

Tags: scope `[team]` `[unit]` `[org]`; journey stage `explore` (no real use), `pilot` (some pilots), `scale` (scaling).

### Onboarding

- Which parts of your work already use AI, which tools, and who decided? Do people use personal accounts? `[team][unit]` explore/pilot. (Move 4)
- What do you want to be true about your team or unit in a year that is not true now? `[team][unit][org]` all. (Move 1)
- Who, above you, has asked for AI progress, and what exactly did they ask for? `[team][unit]` all. (Sponsorship; McKinsey Exh. 13)
- What is the leaders' own usage of AI in their daily work? `[unit][org]` all. (Move 5)
- What have you already tried that did not stick, and why? `[team][unit][org]` pilot. (MIT §3.2 pilot-to-production drop-off)
- What is measured about this work today (volume, cycle time, quality, cost, revenue)? `[team][unit]` all. (Move 14)
- Which numbers do you report upward about AI, and what do they count? `[unit][org]` pilot/scale. (Move 3)

### Frame

- What is the outcome you want: lower cost, higher quality, more revenue, a new offering? Which of these will leadership accept as proof? `[unit][org]` all. (McKinsey Exh. 10)
- Is there a stated multiyear ambition and target for AI, and who set it? `[org]` pilot/scale. (BCG pp. 3, 11)
- Who owns AI outcomes: business, IT, both? Who has decision rights over priorities, data and spend? `[unit][org]` all. (Move 6)
- What do funding and accountability look like: central budget, local budget, or both? `[unit][org]` scale. (Move 21)
- Where does AI governance sit today, and does it reuse existing risk and review structures? `[unit][org]` pilot/scale. (Move 18)
- Which risks has your team actually experienced (inaccuracy, privacy, IP, compliance)? `[team][unit]` pilot/scale. (Move 17)
- Is there a central AI team or CoE? What does it decide and what does it leave to the business? Is it a gatekeeper or an adviser in practice? `[unit][org]` pilot/scale. (MSFT-CAF-COE; BCG p. 15)
- How are decisions about build, buy or partner made today? `[unit][org]` pilot/scale. (Move 22)
- What is the current state of the data for the work you care about? Who can fix it? `[team][unit]` all. (Move 20)

### Reimagine

- Describe the piece of work from request to delivery. Where does time go, where does it wait, where is rework? `[team][unit]` all. (Moves 2, 27)
- If tools were free and quality guaranteed, which steps would you drop rather than speed up? `[team][unit]` all. (Hammer 1990; BCG p. 15)
- Which tasks would your people gladly hand over, which would they want to share, and which must stay human? `[team][unit]` all. (Move 10)
- Which tasks inside this work look similar but differ in how reliable AI would be on them? `[team][unit]` pilot. (Move 8)
- At which step does a person check output, using what criteria, and who is accountable for errors? `[team][unit]` all. (Move 16)
- How would corrections and exceptions feed back so that the tool improves? `[team][unit]` pilot/scale. (Move 13)
- Which parts could change the offering or open a new service rather than make the existing one cheaper? `[unit][org]` scale. (McKinsey growth/innovation; BCG "invent")
- Does this need an agent, or would simpler automation do? `[team][unit]` all. (Move 19)
- How will junior staff build judgment if AI does their practice tasks? `[team][unit]` all. (Move 24)

### Prioritize

- Which candidate workflows have both clear value and reasonable feasibility, according to a matrix the team built together? `[team][unit]` all. (Move 7)
- Which first-wave candidate is narrow, simple to execute and adjacent to a core process? `[team][unit]` explore/pilot. (Move 12)
- What metric will tell us it worked, how will we measure it before and after, and who signs off the number? `[team][unit][org]` all. (Move 14)
- If we save time, where will the time go, and who decides? `[team][unit][org]` pilot/scale. (Move 15)
- Which candidates would be funded in a year-two plan if first-year results were weak? `[unit][org]` scale. (BCG p. 14: prioritization and time-to-impact)
- How many parallel initiatives can the unit actually support? `[unit][org]` pilot/scale. (BCG p. 6: scattering across scores of workflows)
- Which initiatives can share platforms, prompts, data products or standards with other units? `[unit][org]` scale. (BCG p. 16)
- Which numbers from industry benchmarks does the leadership team quote, and how were they measured? `[org]` all. (Move 25)

---

## 5. Common traps

1. **Mistaking tool rollout for transformation.** Why: licences and training are visible and quick; redesign is slow and cross-functional. Evidence: MIT says widely adopted chat tools mostly improve individual productivity rather than P&L [MIT-NANDA-2025 exec. summary]. Deloitte reports education as the top talent adjustment, ahead of role and workflow redesign [DELOITTE-STATEAI-2026]. McKinsey says most organizations have not yet embedded AI deeply enough to realize material enterprise benefits [MCKINSEY-STATEOFAI-2025 intro]. Avoid by: anchoring every plan to one redesigned workflow with a named measure.

2. **Automating waste.** Why: AI makes an existing step faster without questioning the step. Evidence: BCG says integrating agents is not a matter of bolting them onto legacy processes [BCG-VALUEGAP-2025 p. 15]. Hammer's classic argument is the same [HBR-HAMMER-1990]. Avoid by: mapping first, dropping steps before automating them. The sources here give no measured rate of this trap.

3. **Efficiency-only ambition.** Why: cost cases are easy to write and defend. Evidence: McKinsey high performers set growth and innovation objectives about 80% of the time versus about 50% for others [MCKINSEY-STATEOFAI-2025 Exh. 10]. Avoid by: adding a growth or quality objective and asking what the unit could sell or do that it cannot now. Caution: correlational, self-reported.

4. **Pilot sprawl and a "GenAI burden."** Why: no central priority-setting, spread across many workflows. Evidence: BCG describes laggards spreading effort over scores of workflows and a portfolio of siloed proofs of concept [BCG-VALUEGAP-2025 pp. 6, 16]. IBM: 50% of surveyed CEOs say rapid investment left disconnected technology [IBM-CEO-2025]. Avoid by: a sequenced roadmap with a small number of end-to-end workflows.

5. **Delegating AI to middle management with no top-level ownership.** Evidence: BCG describes laggard top management that does not articulate a value ambition [BCG-VALUEGAP-2025 p. 6]. Nearly 100% of future-built firms report deeply engaged C-suites versus 8% of laggards [BCG-VALUEGAP-2025 p. 11]. McKinsey: high performers three times as likely to strongly agree leaders demonstrate ownership [MCKINSEY-STATEOFAI-2025 Exh. 13]. Avoid by: finding the actual sponsor early and asking what they personally do.

6. **IT-only ownership.** Evidence: BCG calls exclusive IT ownership a key indicator of stagnating companies (chart annotation) [BCG-VALUEGAP-2025 Exh. 7]. Avoid by: naming a business owner with decision rights.

7. **Trusting perception over measurement.** Evidence: METR's developers believed they had saved 20% of their time but took 19% longer [METR-2025]. 90% of MIT's respondents preferred humans for complex multi-week work, though that is a stated preference [MIT-NANDA-2025 §4.3]. Avoid by: small controlled comparisons on real work before scaling.

8. **Ignoring the jagged frontier.** Evidence: in the Harvard/BCG study, tasks inside the frontier improved sharply, and the authors introduced the frontier concept because AI fails on some similar-looking tasks [HBS-JAGGED-2023]. Avoid by: classifying tasks before assigning AI, and testing each class.

9. **Measuring what is easy rather than what matters.** Evidence: MIT argues sales and marketing attract budget because outcomes are easier to measure, while back-office returns are less visible [MIT-NANDA-2025 §3.4]. KPMG: 78% say traditional metrics miss AI's value [KPMG-AIPULSE-Q3-2025]. Caution: MIT's own figures conflict (about 70% in the text of §3.4, about 50% in its heading and later text), and the per-use-case breakdown is described as directional at best. Avoid by: agreeing a metric tree early; asking what is measurable and what matters.

10. **Training as the whole change plan.** Evidence: see trap 1 (Deloitte). Wharton: investment in training softened 8 points year on year even as technical skill gaps persist [WHARTON-GBK-2025 exec. summary]. Avoid by: pairing training with protected time and redesigned roles. BCG says future-built firms are four times as likely to carve out time for structured learning [BCG-VALUEGAP-2025 p. 15].

11. **Governance that trails capability.** Evidence: about one in five companies has mature agent governance [DELOITTE-STATEAI-2026]. 72% report unmanaged AI-security risk [BCG-VALUEGAP-2025 p. 10]. High performers report more negative consequences and mitigate more, so negative experience alone is not a failure signal [MCKINSEY-STATEOFAI-2025 text near Exh. 19]. Avoid by: building controls into workflows and the platform at the start.

12. **Agent hype.** Evidence: McKinsey: no more than 10% of respondents report scaling agents in any single function, though 23% report scaling an agentic system somewhere [MCKINSEY-STATEOFAI-2025 Exh. 2]. Stanford's 2026 AI Index: agent deployment in the single digits across nearly all functions [STANFORD-AIINDEX-2026]. A Gartner forecast of over 40% of agentic projects cancelled by end of 2027 is search-only [GARTNER-AGENTIC-2025]. Avoid by: asking whether simpler automation fits.

13. **Treating cross-survey headlines as a single fact.** Evidence: the ROI rows in section 6 show 12% to 97% depending on respondent, definition and base. Avoid by: always asking for the base and the wording.

14. **Hollowing out the junior pipeline.** Evidence: see move 24. Caution: the Stanford canaries paper calls its facts early, descriptive indicators, not causal estimates [STANFORD-CANARIES-2026 abstract]. Avoid by: designing deliberate practice and review roles for juniors.

15. **Locking in a bespoke build without a learning path.** Evidence: MIT reports internal builds reached deployment less often, with the authors noting the difference may reflect capability or risk tolerance rather than approach [MIT-NANDA-2025 §6.1]. EY and BCG show the build-versus-buy picture is mixed. Avoid by: asking about learning, integration and support before choosing.

---

## 6. Evidence

Each row states what the figure measures, who measured it, and its provenance. "Self-reported" means respondents attributed results to their own organization. Locators use exhibit numbers where page numbers are unreliable.

### 6a. Adoption, scaling and value (surveys)

| # | Data point | What it measures | Measured by / provenance | Type | Source and locator |
|---|---|---|---|---|---|
| 1 | 88% (78% a year earlier) | Respondents reporting their organization regularly uses AI in at least one business function. 1,993 participants, all levels, 105 countries (country count from search coverage; the PDF gives 1,993 and dates) | McKinsey survey, fielded 25 June to 29 July 2025. Self-reported | S | MCKINSEY-STATEOFAI-2025 p. 3, Exh. 1 |
| 2 | 7% fully scaled, 31% scaling, 30% piloting, 32% experimenting | Phase of AI use among organizations already using AI (shares of respondents) | McKinsey, self-reported | S | MCKINSEY-STATEOFAI-2025 Exh. 1 |
| 3 | 39% any EBIT impact; most of those under 5% of EBIT | Respondents attributing any level of enterprise EBIT impact to AI. Related outcome questions base n=1,753 | McKinsey, self-reported attribution | S | MCKINSEY-STATEOFAI-2025 p. 10, Exh. 6 |
| 4 | About 6% of respondents are "high performers" (n=109 versus 1,644 others) | Respondents attributing 5% or more of EBIT to AI and reporting "significant" value (text says "5 percent or more", footnotes say "more than 5%") | McKinsey definition, self-reported | S | MCKINSEY-STATEOFAI-2025 p. 13, Exh. 9 notes |
| 5 | 55% versus 20% (2.8x) | Respondents reporting fundamental redesign of workflows in AI deployment: high performers versus all others. Relative-weights analysis of 31 variables ranked redesign among the strongest contributors | McKinsey. Correlation, self-reported | S | MCKINSEY-STATEOFAI-2025 Exh. 11 and footnote |
| 6 | 84/82/79% versus 80/50/50% | Share naming efficiency / growth / innovation as AI objectives: high performers versus others | McKinsey, self-reported | S | MCKINSEY-STATEOFAI-2025 Exh. 10 |
| 7 | About 65% versus about 23% (chart labels) | Having defined processes for when model outputs need human validation: high performers versus others. The text calls it one of the top differentiating factors | McKinsey, self-reported. Values read from chart labels | S | MCKINSEY-STATEOFAI-2025 Exh. 14 |
| 8 | 23% scaling an agentic system somewhere; 39% experimenting; no more than 10% scaling agents in any one function | Share of respondents (agents by function n=1,933) | McKinsey, self-reported | S | MCKINSEY-STATEOFAI-2025 p. 4, Exh. 2 |
| 9 | Cost decreases reported by 56% (software engineering), 56% (manufacturing), 54% (IT), 53% (strategy and corporate finance), 51% (service operations), 51% (HR), 49% (marketing and sales), 45% (risk, legal, compliance), 44% (knowledge management). Most are 10% or less | Share of respondents in organizations using AI in that function reporting any cost decrease in business units over 12 months (sum of three bands) | McKinsey, self-reported | S | MCKINSEY-STATEOFAI-2025 Exh. 7 |
| 10 | Revenue increases reported by 67% (marketing and sales), 65% (strategy and corporate finance), 62% (product or service development), 59% (supply chain), 57% (service operations, software engineering), 52% (IT). Most are 5% or less | Same base, any revenue increase | McKinsey, self-reported | S | MCKINSEY-STATEOFAI-2025 Exh. 8 |
| 11 | 51% experienced at least one negative consequence; nearly one-third from inaccuracy | Respondents in AI-using organizations (n=1,753) | McKinsey, self-reported | S | MCKINSEY-STATEOFAI-2025 Exh. 19 and text |
| 12 | Nearly half of firms above $5B revenue are scaling, versus 29% under $100M | Phase of use by company revenue | McKinsey, self-reported | S | MCKINSEY-STATEOFAI-2025 Exh. 5 |
| 13 | 5% future-built, 35% scaling, 46% emerging, 14% stagnating (2024: 4/22/49/25) | Share of firms by BCG's 41-dimension AI maturity score. n=1,250 | BCG Build for the Future 2025 survey. Vendor-published. Maturity categories are BCG's | S | BCG-VALUEGAP-2025 p. 4, Exh. 1 |
| 14 | Future-built versus stagnating plus emerging: 1.7x revenue growth, 1.6x EBIT margin, 2.7x ROIC, 3.6x three-year TSR | Compared outcomes by maturity group. TSR from Capital IQ (external). Others are from the survey | BCG. Correlation | S/M | BCG-VALUEGAP-2025 Exh. 1 and footnotes |
| 15 | 70% of AI value potential in core functions (2024: 62%); R&D 15%, IT 13%, support functions 30% | BCG respondents' distribution of AI value potential across functions | BCG, estimate-based | S | BCG-VALUEGAP-2025 p. 7, Exh. 3 |
| 16 | 62% of workflows deployed at future-built versus 12% at laggards; typical full deployment 9-12 versus 12-18 months | Share of AI workflows at "deployed" stage; average months to fully deploy | BCG, self-reported | S | BCG-VALUEGAP-2025 p. 14, Exh. 8 |
| 17 | More than 60% versus 17% rigorously track AI value; nearly 100% versus 8% report a deeply engaged C-suite | Future-built versus stagnating (tracking); future-built versus laggards (C-suite) | BCG, self-reported | S | BCG-VALUEGAP-2025 pp. 11, 14 |
| 18 | Agents 17% of AI value in 2025, expected 29% by 2028 | Respondents' reported split of AI-driven value reaching the bottom line. The 2028 figure is an expectation | BCG | S/F | BCG-VALUEGAP-2025 p. 10, Exh. 5 |
| 19 | 11% rely primarily on in-house development; 4% on a single end-to-end vendor | Share of firms by AI stack sourcing | BCG, self-reported | S | BCG-VALUEGAP-2025 p. 16 |
| 20 | 77% people adapting to change, 74% talent shortage, 72% integration and security, 79% unstructured data expertise, 42% leadership support | Share naming each as a key challenge. BCG says people and process items are significantly higher for laggards. The 10-20-70 grouping is BCG's | BCG, self-reported | S/G | BCG-VALUEGAP-2025 Exh. 10 |
| 21 | 12% both cost and revenue gains; 33% either; 56% neither; 30% confident on revenue; 4,454 CEOs in 95 countries | CEOs' reports on AI financial benefit to date. Fielded 30 Sept to 10 Nov 2025. Weighted by GDP | PwC CEO Survey, self-reported | S | PWC-CEO-2026 |
| 22 | Three times as likely to report meaningful returns with strong AI foundations; 2-3x more likely with AI embedded across products, demand generation, decisions; separate PwC analysis: nearly four points higher margins with wide AI use | Comparison among CEO respondents. The margin analysis is a separate PwC analysis (method not in release) | PwC | S | PWC-CEO-2026 |
| 23 | n=3,235 leaders: 34% using AI to deeply transform, 30% redesigning key processes, 37% surface-level | Self-described use of AI. Fielded Aug to Sept 2025 | Deloitte AI Institute, self-reported | S | DELOITTE-STATEAI-2026 |
| 24 | 66% report productivity or efficiency gains; 20% already grow revenue through AI versus 74% hoping to | Share of organizations | Deloitte, self-reported | S | DELOITTE-STATEAI-2026 |
| 25 | Talent adjustments: 53% educate workforce, 48% upskill/reskill, 36% hire, 33% redesign career paths. Skills gap is the biggest barrier to integrating AI into workflows | Share of leaders | Deloitte, self-reported | S | DELOITTE-STATEAI-2026 |
| 26 | About one in five companies has a mature governance model for autonomous agents | Deloitte's classification | Deloitte, self-reported | S | DELOITTE-STATEAI-2026 |
| 27 | Agent deployment 42% (11% two quarters earlier); 78% say traditional metrics miss AI's impact; data quality a critical barrier for 82%; employee resistance 21% (47%) | n=130 US C-suite at firms with $1B+ revenue. Release dated 18 Sept 2025 | KPMG, self-reported. Small sample of large firms | S | KPMG-AIPULSE-Q3-2025 |
| 28 | 97% of leaders whose organizations invest in AI see positive ROI; 14% fully implemented agentic AI; 34% started | n=500 US senior leaders (SVP and above), margin of error plus or minus 4 points. Wave 3 | EY US AI Pulse, self-reported | S | EY-AIPULSE-JUL-2025 |
| 29 | 96% see productivity gains (57% significant); of those, 17% say gains led to reduced headcount, 47% reinvested in existing AI, 42% in new AI capabilities; 56% of those with positive ROI report significant financial improvement | n=500 US senior leaders. Wave 4, fielded 19 Sept to 16 Oct 2025 | EY, self-reported | S | EY-AIPULSE-DEC-2025 |
| 30 | Only 25% of AI initiatives delivered expected ROI; only 16% scaled enterprise-wide; 50% say rapid investment left disconnected technology; 52% realize value from GenAI beyond cost reduction | 2,000 CEOs, 33 countries, Feb to Apr 2025. Share of initiatives and share of CEOs | IBM Institute for Business Value with Oxford Economics. Vendor-published | S | IBM-CEO-2025 |
| 31 | 74% positive ROI; 72% formally measure ROI; Tier 1 ($2B+) more likely to say "too early"; CAIO in about 60% (PDF) or 61% (web page); about 30% of GenAI technology budget to internal R&D; 43% warn of skill atrophy | About 800 US senior decision-makers at firms with 1,000+ employees and over $50M revenue. Interviewed 26 June to 11 July 2025 | Wharton Human-AI Research and GBK Collective, self-reported | S | WHARTON-GBK-2025 exec. summary, pp. 10-12 |
| 32 | 78% of organizations used AI in 2024 (55% in 2023); GenAI in at least one function 71% (33%); most reporting cost savings put them under 10%, most reporting revenue gains put them under 5% | Summaries of McKinsey surveys, reproduced by the Index | Stanford HAI AI Index 2025. Not independent of McKinsey | S | STANFORD-AIINDEX-2025 Report Highlights ch. 4, items 4-5 |
| 33 | 88% of organizations use AI (2025); GenAI in at least one function 70%; agent deployment in single digits in nearly all functions; one-third expect workforce reductions | Organizational adoption data (source of survey not named on the page; the 88% matches McKinsey's 2025 figure) | Stanford HAI AI Index 2026 | S | STANFORD-AIINDEX-2026 economy page, highlights 5, 8 |

### 6b. MIT NANDA "GenAI Divide" (read in full; treat with caution)

Basis: systematic review of 300+ public AI initiatives, interviews with 52 organizations, survey of 153 senior leaders, January to June 2025. Described as "preliminary findings". The authors say figures are "directionally accurate" and based on interviews, not company reporting. Success is defined as users or executives remarking on a marked and sustained productivity or P&L impact. Not peer-reviewed.

| # | Data point | What it measures | Type | Locator |
|---|---|---|---|---|
| 34 | "95% of organizations are getting zero return"; "just 5% of integrated AI pilots are extracting millions" | Authors' headline, based on interviews and review. The report also says 5% of task-specific enterprise tools reach production. The headline mixes organizations, pilots and tools | S/G | MIT-NANDA-2025 exec. summary, §3.2 |
| 35 | General-purpose LLMs: 80% explored, 50% piloted, about 40% implemented. Task-specific or embedded tools: 60% investigated, 20% piloted, 5% implemented | Interview-based funnel by tool type | S | MIT-NANDA-2025 §3.2 exhibit |
| 36 | Workers at over 90% of surveyed companies use personal AI tools; about 40% of companies bought an LLM subscription | Reported usage versus procurement | S | MIT-NANDA-2025 §3.3 |
| 37 | Externally partnered tools reached deployment about 67% versus about 33% for internal builds | Share of deployments in the 52-organization sample. Authors warn it may reflect capability or risk tolerance and does not prove causation | S | MIT-NANDA-2025 §6.1 |
| 38 | Mid-market top performers: about 90 days from pilot to full implementation; large enterprises (over $100M revenue): nine months or longer | Interview-based timelines | S | MIT-NANDA-2025 §3.2 |
| 39 | 90% prefer a human for complex multi-week work; 70% prefer AI for quick tasks such as emails | Stated preference on "AI or junior colleague" | S | MIT-NANDA-2025 §4.3 |
| 40 | Back-office wins: $2-10M annual BPO savings; 30% lower agency spend. Front-office: 40% faster lead qualification, 10% better retention | "Best-in-class" examples, with no sample or audit stated | S (anecdotal) | MIT-NANDA-2025 §6.3 |

Internal inconsistencies to flag when quoting: the executive summary says "2 of 8 major sectors" show structural change, §3 says seven of nine sectors. The sales and marketing budget share is given as about 70% in one place and about 50% elsewhere. Professional services scores 1.5 of 5 on the authors' composite disruption index (range 1.2 to 2.1 under alternative weights), with the note "efficiency gains; client delivery remains largely unchanged". [MIT-NANDA-2025 §3.1, §3.4]

### 6c. Controlled and administrative evidence

| # | Data point | What it measures | Provenance | Type | Source |
|---|---|---|---|---|---|
| 41 | 14% more issues resolved per hour on average; 34% for novice and low-skilled workers; minimal effect on experienced workers | 5,179 customer support agents at one Fortune 500 enterprise software firm. Staggered rollout of a conversational assistant. Also better customer sentiment and retention | NBER working paper (not peer-reviewed per the paper's own notice), independent | M-exp | NBER-BRYNJOLFSSON-2023 abstract |
| 42 | Inside the frontier: speed up over 25%, human-rated performance up over 40%, task completion up over 12%. Two usage patterns, "centaur" and "cyborg" | 758 BCG consultants (7% of individual contributors), field experiment | HBS Digital Data Design Institute summary of the working paper (full paper not retrieved) | M-exp | HBS-JAGGED-2023 |
| 43 | AI allowed raised task completion time by 19%. Developers had forecast a 24% cut and later estimated a 20% cut | 16 experienced open-source developers, 246 tasks, Feb to June 2025 tools | METR RCT, independent. Small sample, one setting (mature repositories) | M-exp | METR-2025 abstract |
| 44 | No significant effect on earnings or recorded hours in any of 11 occupations; confidence intervals rule out effects over 1%; average time savings 3% | 25,000 workers at 7,000 workplaces in Denmark linked to employer-employee records. Surveys late 2023 and 2024 | BFI working paper, independent | M-exp | BFI-HUMLUM-2025 abstract |
| 45 | About 40% of US adults aged 18-64 use GenAI; 23% of employed used it for work last week; 9% daily; time savings equal 1.4% of total work hours | Nationally representative surveys, late 2024. Self-reported | Federal Reserve Bank of St. Louis authors, NBER working paper | S | NBER-BICK-2025 abstract |
| 46 | Employment of ages 22-25 in AI-exposed occupations 19% below the path of less-exposed peers; no economy-wide displacement found; declines concentrated where usage substitutes for tasks | ADP payroll data on millions of US workers through June 2026. Authors call these early, descriptive indicators, not causal | Stanford/NBER, independent | M-exp (observational) | STANFORD-CANARIES-2026 abstract |
| 47 | AI Index 2026 summarizes studies: 14-15% gains in customer support, 26% in software development, 50% in marketing output; gains smaller in tasks needing deeper reasoning | Studies selected by the AI Index | Stanford HAI | M-exp (secondary summary) | STANFORD-AIINDEX-2026 highlight 9 |
| 48 | Model: adjusted TFP 11.3% higher than official at end of 2004 | Historical analysis of complementary intangibles for earlier technologies. Not AI-specific | NBER, independent | G (theory plus history) | NBER-JCURVE-2020 abstract |

### 6d. Platform usage data (Anthropic Economic Index, vendor-published, own platform)

These describe what people do with Claude, not business outcomes. Anthropic's June 2026 survey is not representative, and about 30% of respondents are in computer and mathematical occupations.

| # | Data point | What it measures | Source |
|---|---|---|---|
| 49 | 77% of first-party API business uses involve automation patterns versus about 50% on Claude.ai; "directive" conversations rose from 27% to 39% between January and August 2025 | Share of sampled conversations or API records classified as automation | ANTHROPIC-EI-SEP-2025 key findings |
| 50 | Top 10 tasks are 24% of Claude.ai conversations and 32% of API traffic; augmentation 52% versus automation 45% on Claude.ai (Nov 2025); computer and mathematical tasks about one-third of Claude.ai and nearly half of API traffic; office and administrative tasks 13% of API records | Share of sampled records, November 2025 | ANTHROPIC-EI-JAN-2026 ch. 1 |
| 51 | Claude's success rate falls as human task time increases | Classifier-estimated task success | ANTHROPIC-EI-JAN-2026 key findings |
| 52 | 93% of chat and Cowork conversations produce an artifact; work conversations most often produce documents and reports (20%); Claude Code sessions show more AI autonomy (+0.37 on a 1-5 scale); median chat blog-writing has 13 rounds of back-and-forth versus a single prompt in Claude Code | Classifier results over sampled conversations (spring 2026) | ANTHROPIC-EI-JUN-2026 ch. 2 |
| 53 | Users who delegate most are the most optimistic about their labour market outcomes; early-career workers report AI can do the highest share of their work | Survey linked to usage, launched April 2026. Not representative | ANTHROPIC-EI-JUN-2026 ch. 3 |
| 54 | About 36% of occupations use AI for at least a quarter of their tasks; 57% augmentation, 43% automation; software development and writing about half of usage | Early-2025 Claude.ai sample (4+ million conversations) | ANTHROPIC-EI-FEB-2025 abstract |

### 6e. Forecasts and search-only items (notes only)

| # | Data point | Provenance | Type | Source |
|---|---|---|---|---|
| 55 | By 2030, 170 million jobs created and 92 million displaced (net 78 million); employers expect 39% of workers' core skills to change | Employer survey and ILO data, projections | F | WEF-FOJ-2025 §2.1, §3 |
| 56 | McKinsey Superagency (Jan 2025): only 1% of leaders call their companies "mature" in deployment | Search result excerpt only. Original not reached | S, search-only | MCKINSEY-SUPERAGENCY-2025 |
| 57 | Gartner: over 40% of agentic AI projects expected to be cancelled by end of 2027 | Forecast, reported through news coverage only. Press release not reached | F, search-only | GARTNER-AGENTIC-2025 |
| 58 | RAND (Aug 2024): "more than 80 percent of AI projects fail" by some estimates. The report cites this as an estimate. Its own sample was 65 interviews with experienced practitioners | Search snippets only | G/S, search-only | RAND-ROOTCAUSES-2024 |
| 59 | Accenture (Mar 2025): organizations that act on all five recommended actions are 2.5 times as likely to achieve enterprise-level results; based on 2,000+ client projects and 3,000+ executives. A "13% with measurable enterprise-wide impact" figure appeared only in a secondary summary and is not confirmed | Accenture page confirmed for 2.5x and sample description. The 13% figure is search-only | S | ACCENTURE-REINVENTION-2025 |
| 60 | Accenture (Sept 2024): the most mature operations were 3.3 times as likely to have scaled high-value GenAI use cases and reported 2.5 times higher revenue growth (2019-2023). Only 16% had the highest readiness. Sample size not stated on the page | Accenture Pulse of Change Index 2024, vendor-published. Correlation | S | ACCENTURE-OPS-2024 |

---

## 7. Worked examples

**A. Customer support copilot (knowledge-adjacent, measured).** The step that changed: agents handled chats with an assistant that suggested responses and guidance, which captures patterns from the best agents. Who: a Fortune 500 enterprise software firm's support operation, 5,179 agents. Outcome: 14% more issues resolved per hour on average, 34% for novices, minimal for experienced agents. Customer sentiment and retention also improved. Limits: one firm and a first-generation tool, with a working paper that is not peer-reviewed in the version retrieved. For the advisor: tools that spread the best performers' practice help the less experienced most, so the question for a professional-services team is which of its tacit know-how can be captured in this way and who learns from whom. [NBER-BRYNJOLFSSON-2023 abstract, introduction]

**B. Consumer-products marketing function (prioritization, BCG-published client case).** The step that changed: the function mapped all campaigns, activities and resources through a department-wide survey, then built a feasibility matrix to find the most promising workflows. AI was then integrated into those workflows, mostly cutting internal and external costs such as agency cost and process steps. Outcome as reported by BCG: 25-40% savings in time spent on content creation, brand planning and reporting, and a doubled speed to market for campaign activation. Limits: self-reported by a BCG client, anonymized, no baseline or audit given. The marketing function covers many brands and 50+ markets, which suits a portfolio-style inventory. For the advisor: this is the shape of a map-then-prioritize exercise at unit level. [BCG-VALUEGAP-2025 p. 14]

**C. Global bank, HR function rebuilt "hire to retire" (reimagine, BCG-published client case).** The step that changed: rather than optimizing isolated processes, the bank redefined employee journeys (apply and join, get feedback, get rewarded, leave) and asked three questions: which journeys matter, which parts can and should be done by AI, and which tasks stay with people. It set KPIs such as time-to-hire, 90-day retention and service-request cycle time. It launched targeted prototypes (for example summarizing feedback for line managers in the annual performance cycle). The case reports efficiency gains from these prototypes but gives no savings figure and says the work informed a business case. It is described as a pilot. Limits: an anonymized single case with no outcome data. For the advisor: a clean illustration of the "reinvent the work" lens driven by journeys and explicit AI-versus-human allocation. [BCG-VALUEGAP-2025 pp. 12-13]

**D. Testing before scaling: two experiments with opposite results (prioritize).** In the Harvard/BCG experiment, 758 consultants using GPT-4 on tasks inside the frontier ran over 25% faster with human-rated performance over 40% higher. In METR's trial, 16 experienced developers working on their own mature repositories took 19% longer with AI, while believing they had been faster. The two studies cover different tools, tasks and populations, so they do not contradict each other. Together they show why the advisor should have teams test candidate tasks on real samples and compare measured with perceived effect before committing a workflow to AI. [HBS-JAGGED-2023; METR-2025]

---

## 8. Mapping to phases

**Onboarding.** Use this topic to calibrate the user's starting point and claims. It supplies the standard split between adoption and impact (moves 3, 4, 5), questions about sponsorship, current usage including shadow use, and what is already measured. It also warns that benchmark numbers conflict, so the advisor should not quote one without its base (move 25). Scope tags: team leads need usage and sponsorship questions. Practice leaders and heads of AI need ownership, governance and funding questions.

**Frame.** The evidence says ambition, ownership and operating model are the main frame-level levers. The advisor should help the user state a value ambition that goes beyond efficiency where the unit can credibly support it (moves 1, 2, 6), identify the sponsor, and choose a scope at the workflow level. For a unit or organization scope, the advisor should surface who owns outcomes, how a CoE and the business split decisions, how funding works, and where governance sits (moves 18, 21, 22). Where an operating-model question has no measured answer, say so and offer the options the sources describe.

**Reimagine.** Supply the workflow-first stance and the cautions around it. Map and redesign instead of overlaying (move 2). Use staff preferences and the four-zone screen to choose between improving a step, automating the flow, delegating an outcome and reinventing the work (moves 10, 11). Build in human validation points (move 16) and the learning loop (move 13). Treat agents as a design choice with prerequisites (move 19). Use the BCG HR case as a reinvention pattern and the junior-pipeline question as a standard check (move 24).

**Prioritize.** Supply a value-by-feasibility matrix built on a real activity inventory (move 7), the narrow-first sequencing pattern (move 12), trial-before-scale testing (moves 8, 9), outcome metrics agreed in advance (move 14), and the question of where saved time goes (move 15). Warn that the evidence on first-wave function (front office versus back office) is contested, so choose by the unit's own data and measures rather than a generic rule. Flag that time-to-impact figures (9-12 versus 12-18 months in BCG) are self-reported.

---

## 9. Sources

Date column gives publication date where confirmed. "Retrieved" is 2026-10-16 for all. Access: `full` means the document text was read; `partial` means only part of the content was available; `search-only` means only search-result excerpts or secondary coverage were seen.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| MCKINSEY-STATEOFAI-2025 | The state of AI in 2025: Agents, innovation, and transformation | McKinsey and Company (QuantumBlack). Singla, Sukharevsky, Yee, Chui | Consultancy survey (n=1,993) | Original: https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai (not reachable here). Read via copy: https://www.rivista.ai/wp-content/uploads/2025/11/1762726272547.pdf | November 2025 (cover). Fielded 25 June to 29 July 2025 | full (third-party copy; not checked against mckinsey.com) |
| BCG-VALUEGAP-2025 | The Widening AI Value Gap: Build for the Future 2025 | Boston Consulting Group. Apotheker et al. | Consultancy survey (n=1,250) | https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf | September 2025 (cover); file name says October 2025 | full |
| MIT-NANDA-2025 | The GenAI Divide: State of AI in Business 2025 | MIT NANDA. Challapally, Pease, Raskar, Chari | Research-group report (preliminary, not peer-reviewed) | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf (copy hosted by a third party; original host not identified) | July 2025 | full |
| STANFORD-AIINDEX-2025 | Artificial Intelligence Index Report 2025 | Stanford HAI | Research-institute report | https://hai-production.s3.amazonaws.com/files/hai_ai_index_report_2025.pdf | April 2025 (publication month not shown in the extracted text) | full (read highlights and chapter 4 summary) |
| STANFORD-AIINDEX-2026 | AI Index Report 2026, Economy chapter page | Stanford HAI | Research-institute report page | https://hai.stanford.edu/ai-index/2026-ai-index-report/economy | 2026 (page undated in retrieved text; coverage in search results places release in April 2026) | partial (chapter highlights page only) |
| DELOITTE-STATEAI-2026 | The State of AI in the Enterprise, 2026 AI report | Deloitte AI Institute | Consultancy survey (n=3,235, Aug to Sept 2025) | https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html | Published 20 Jan 2026; page modified 23 Apr 2026 | partial (web page; full report not read) |
| KPMG-AIPULSE-Q3-2025 | Agent Deployment Accelerates as Organizations Build Confidence Through Early Wins (Q3 2025 AI Quarterly Pulse) | KPMG US | Consultancy survey press release (n=130) | https://kpmg.com/us/en/media/news/q3-ai-pulse.html | 18 Sept 2025 | full (press release) |
| ACCENTURE-REINVENTION-2025 | Making Reinvention Real with Gen AI | Accenture | Consultancy report page | https://www.accenture.com/us-en/insights/consulting/making-reinvention-real-with-gen-ai | 6 Mar 2025 | partial (page text; numeric callouts missing from extraction, only the 2.5x and sample description confirmed) |
| ACCENTURE-OPS-2024 | Generative AI in Operations for AI-Powered Reinvention | Accenture | Consultancy research page | https://www.accenture.com/us-en/insights/strategic-managed-services/reinvent-operations-with-genai | 17 Sept 2024 | full (page; sample size not stated) |
| PWC-CEO-2026 | PwC 29th Global CEO Survey, press release "CEO confidence in revenue outlook hits five-year low" | PwC | Consultancy survey (n=4,454) | https://www.aap.com.au/aapreleases/cision20260119ae63311 (distributed copy; pwc.com pages returned 403) | 20 Jan 2026 | full (press release) |
| EY-AIPULSE-JUL-2025 | AI investments surge, but agentic AI understanding and adoption lag behind (EY US AI Pulse, wave 3) | EY US | Consultancy survey press release (n=500) | https://www.ey.com/en_us/newsroom/2025/07/ai-investments-surge-but-agentic-ai-understanding-and-adoption-lag-behind | 29 Jul 2025 | full (press release) |
| EY-AIPULSE-DEC-2025 | AI-driven productivity is fueling reinvestment over workforce reductions (EY US AI Pulse, wave 4) | EY US | Consultancy survey press release (n=500) | https://www.ey.com/en_us/newsroom/2025/12/ai-driven-productivity-is-fueling-reinvestment-over-workforce-reductions | 9 Dec 2025 | full (press release) |
| IBM-CEO-2025 | IBM Study: CEOs double down on AI while navigating enterprise hurdles | IBM Institute for Business Value | Vendor survey press release (n=2,000 CEOs) | https://newsroom.ibm.com/2025-05-06-ibm-study-ceos-double-down-on-ai-while-navigating-enterprise-hurdles | 6 May 2025 | full (press release; full study not read) |
| WHARTON-GBK-2025 | Accountable Acceleration: Gen AI Fast-Tracks into the Enterprise (2025 AI Adoption Report) | Wharton Human-AI Research and GBK Collective | Academic-industry survey (about 800) | https://knowledge.wharton.upenn.edu/special-report/2025-ai-adoption-report/ ; full PDF https://ai.wharton.upenn.edu/wp-content/uploads/2025/10/2025-Wharton-GBK-AI-Adoption-Report_Full-Report.pdf | 28 Oct 2025 | full (executive summary and method read) |
| ANTHROPIC-EI-SEP-2025 | Anthropic Economic Index report: Uneven geographic and enterprise AI adoption | Anthropic | Vendor usage study (telemetry) | https://www.anthropic.com/research/anthropic-economic-index-september-2025-report | 15 Sept 2025 | full |
| ANTHROPIC-EI-JAN-2026 | Anthropic Economic Index report (January 2026; November 2025 data) | Anthropic | Vendor usage study (telemetry) | https://www.anthropic.com/research/anthropic-economic-index-january-2026-report | 15 Jan 2026 | full |
| ANTHROPIC-EI-JUN-2026 | Anthropic Economic Index report (June 2026, "Cadences") | Anthropic | Vendor usage study plus survey | https://www.anthropic.com/research/economic-index-june-2026-report | 26 Jun 2026 (page modified Sept 2026) | full |
| ANTHROPIC-EI-FEB-2025 | Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations | Handa, Tamkin et al., Anthropic | Working paper (arXiv 2503.04761) | https://arxiv.org/abs/2503.04761 | 11 Feb 2025 | full |
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work (NBER WP 31161) | Brynjolfsson, Li, Raymond | Academic working paper | https://www.nber.org/system/files/working_papers/w31161/w31161.pdf | April 2023, revised November 2023 | full |
| NBER-JCURVE-2020 | The Productivity J-Curve: How Intangibles Complement General Purpose Technologies (NBER WP 25148) | Brynjolfsson, Rock, Syverson | Academic working paper | https://www.nber.org/system/files/working_papers/w25148/w25148.pdf | October 2018, revised January 2020 | full (abstract and framing) |
| BFI-HUMLUM-2025 | Large Language Models, Small Labor Market Effects (BFI WP 2025-56) | Humlum, Vestergaard | Academic working paper | https://bfi.uchicago.edu/wp-content/uploads/2025/04/BFI_WP_2025-56-3.pdf | 9 May 2025 | full (abstract and introduction) |
| METR-2025 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | Becker, Rush, Barnes, Rein (METR) | Academic-style RCT (arXiv 2507.09089) | https://arxiv.org/pdf/2507.09089 | July 2025 | full (abstract and introduction) |
| HBS-JAGGED-2023 | Navigating the Jagged Technological Frontier (summary page) | HBS Digital Data Design Institute (now HBS AI Institute); Dell'Acqua, Lakhani et al. with BCG | Academic field-experiment summary | https://d3.harvard.edu/navigating-the-jagged-technological-frontier/ | 2023 (not stated on the page) | partial (summary page; paper not retrieved) |
| STANFORD-WORKBANK-2026 | Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce | Shao, Zope et al., Stanford | Academic paper (arXiv 2506.06576 v3) | https://arxiv.org/pdf/2506.06576v3 | First posted June 2025; v3 dated 1 Feb 2026 | full (abstract and findings) |
| NBER-BICK-2025 | The Rapid Adoption of Generative AI (NBER WP 32966) | Bick, Blandin, Deming | Academic working paper | https://www.nber.org/system/files/working_papers/w32966/w32966.pdf | September 2024, revised February 2025 | full (abstract) |
| STANFORD-CANARIES-2026 | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of AI | Brynjolfsson, Chandar, Chen | Academic working paper | https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf | August 2026 version (first documented August 2025) | full (abstract) |
| WEF-FOJ-2025 | The Future of Jobs Report 2025 | World Economic Forum | Professional-body/institutional report | https://www3.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf | January 2025 | full (sections 2.1 and 3 read) |
| NIST-AIRMF-2023 | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | NIST | Standard-setter guidance | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | January 2023 | partial (confirmed the four functions, Govern, Map, Measure, Manage; Govern cross-cutting; no more read) |
| MSFT-CAF-COE | Establish an AI Center of Excellence, Cloud Adoption Framework | Microsoft Learn | Vendor practitioner guide (opinion/guidance) | https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/center-of-excellence | Undated live page, retrieved 2026-10-16 | full |
| LANDINGAI-PLAYBOOK | AI Transformation Playbook | Landing AI (Andrew Ng) | Practitioner guide (opinion/guidance) | https://landing.ai/wp-content/uploads/2020/05/LandingAI_Transformation_Playbook_11-19.pdf | Date not stated in the text (file name suggests 2019, so it predates GenAI) | full (first pages) |
| HBR-HAMMER-1990 | Reengineering Work: Don't Automate, Obliterate | Michael Hammer, Harvard Business Review | Classic method article | https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate | 1990 (July-August issue per URL) | partial (opening paragraphs and title only) |
| HBR-DAVENPORT-2018 | Artificial Intelligence for the Real World ("Don't start with moon shots") | Davenport, Ronanki, Harvard Business Review | Practitioner article | https://hbr.org/2018/01/artificial-intelligence-for-the-real-world | January-February 2018 | partial (opening paragraphs only; cited for the MD Anderson Watson project: on hold in 2017 after costs topped $62 million) |
| PENGUIN-MOLLICK-2024 | Co-Intelligence: Living and Working with AI (publisher page) | Ethan Mollick, Portfolio/Penguin Random House | Book (publisher description) | https://www.penguinrandomhouse.com/books/741805/co-intelligence-by-ethan-mollick/ | 2024 (month not confirmed on the page) | partial (marketing description only; not used for any claim in sections 3 to 7) |
| MCKINSEY-SUPERAGENCY-2025 | Superagency in the workplace: Empowering people to unlock AI's full potential | McKinsey | Consultancy report | https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work | January 2025 | search-only |
| MCKINSEY-AGENTIC-2025 | One year of agentic AI: Six lessons from the people doing the work | McKinsey | Practitioner article (50+ builds) | https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work | 2025 (date not confirmed) | search-only (first lesson, workflow over agent, per excerpt) |
| GARTNER-AGENTIC-2025 | Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 | Gartner | Analyst forecast | Primary press release not reached (gartner.com returned 403). Coverage: https://www.outlookbusiness.com/deeptech/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner | June 2025 | search-only |
| RAND-ROOTCAUSES-2024 | The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed | Ryseff, De Bruhl, Newberry, RAND | Research report | https://www.rand.org/pubs/research_reports/RRA2680-1.html (403 from here) | 13 Aug 2024 | search-only |

Counts: 38 sources listed. 29 read with access `full` or `partial` that supported claims, plus `search-only` items used only in notes (4) and two practitioner or book pages read only in part (HBR-HAMMER-1990, PENGUIN-MOLLICK-2024). Types: consultancy or vendor surveys 12 (including press releases), research-institute reports 3, academic or working papers 10, vendor usage studies 4, practitioner guides and classic articles 5, standard-setter or institutional reports 2, book page 1, forecasts or search-only 4 (overlap with the above in the type of origin).

---

## 10. Gaps

- **Primary McKinsey pages and McKinsey's agentic and Superagency articles.** mckinsey.com was unreachable. State of AI 2025 was read through a third-party copy. Superagency and "One year of agentic AI" are search-only.
- **No 2026 editions of McKinsey State of AI or BCG's value-gap study** existed in what I could reach. The latest retrieved are November 2025 and September 2025. Check for newer releases.
- **Books not reached.** Agrawal, Gans and Goldfarb's *Power and Prediction* (point solutions versus system redesign), McKinsey's *Rewired* (six elements), and Iansiti and Lakhani's *Competing in the Age of AI* are the most relevant books. Publisher pages were unreachable and the search budget ran out. *Co-Intelligence* has only a marketing page. The Hammer and Davenport articles are paywalled beyond their openings. The "Core concepts" section therefore leans on surveys and practitioner guides, with Hammer used only for the title's argument.
- **Searches stopped partway.** The web-search budget was used up, so planned searches for CoE-versus-federated evidence, professional-services case studies, and Gartner, RAND and BCG-2024 primaries were not run.
- **No measured comparison of CoE versus federated operating models.** The sources give correlations (BCG shared ownership), a practitioner staging guide (Microsoft) and interview findings (MIT). I found no outcome study.
- **No causal evidence that workflow redesign produces value.** McKinsey's relative-weights result and BCG's comparisons are correlational and self-reported. No experiment compares redesign with overlay.
- **Professional-services-specific evidence is thin.** MIT's composite index scores professional services low on structural disruption. McKinsey's survey has professional-services respondents (n=259 for agents by industry) but I did not extract industry splits. Controlled evidence is mostly customer support, software, and consulting tasks.
- **The 10-20-70 split has no independent measurement.** BCG states it as a rule in its 2025 report and its Exhibit 10 lists challenges; I did not find the underlying effort-allocation data, and I did not trace its earlier origins.
- **MIT NANDA caveats.** The report is preliminary and non-peer-reviewed, with internal inconsistencies noted in section 6b. I found no independent replication or critique within the budget.
- **Accenture 2025 headline figures.** The "13%" figure and several multipliers were not recoverable from the retrieved page; only 2.5x and the sample description were confirmed.
- **Governance sources.** NIST AI RMF is cited for structure only. ISO/IEC 42001, OECD and sector regulators were not reached (iso.org and oecd.org returned 403). Deloitte's governance statement has no figure on the page.
- **Platform data limits.** Anthropic's index covers one vendor's users, skews to computer and mathematical work, and reports behavior, not business outcomes. The survey is non-representative by the authors' own statement.
- **Stanford AI Index figures are largely reproductions of McKinsey survey data**, so the two should not be counted as independent confirmation. The 2026 page was undated in the retrieved text.
- **Dell'Acqua et al.** was read through the HBS AI Institute summary only, so the outside-the-frontier result was not verified.
