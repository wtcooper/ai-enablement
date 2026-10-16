# Method topic: agentic-workflow-redesign

Stream M (method). Prepared 2026-10-16.

**Topic focus:** how organizations redesign work around AI agents (not just add copilots) in 2025-2026. This covers:
- what to give an agent versus a person
- human checkpoints and escalation
- agent-ready processes
- event-triggered agents and managed runtimes
- multi-agent orchestration
- evaluation and monitoring
- failure modes and controls
- AI-native and zero-based redesign

**Phases fed:** reimagine, prioritize, plan-and-control.

**Reading conventions**
- Source refs are `PUBLISHER-SHORT-YYYY` and are defined in section 9.
- Locators are section headings or page labels in the source.
- Every statistic states what it measures and who published it, in section 6 or inline.
- Provenance labels: `self-reported` (an organization reporting on its own work), `vendor-published` (a vendor's own telemetry, survey or benchmark), `consultancy-published`, `analyst-published`, `independent` (academic, or a third party with no product to sell).
- A source marked `access: full` was read in the body. `access: partial` means only part was readable. `access: search-only` means I saw only a search summary, and its figures are in notes, never in headline evidence.
- Items I could not confirm are listed in section 10 (Gaps). Nothing in this file is a quotation of more than 25 words.

---

## 1. Summary

- **Redesign the work, not the tool.** The 2025-26 consultancy and practitioner literature converges on one claim: value comes from redesigning the whole workflow, with people, process and technology together, and not from dropping an agent into an existing step. McKinsey's review of 50+ agentic builds, BCG, Deloitte, Capgemini and Gartner all say this (MCKINSEY-1YR-2025, BCG-AGENTS-2025, DELOITTE-TT-2025, GARTNER-2025). The evidence is consultancy-published. I found no independent measurement comparing redesigned and bolted-on deployments (see Gaps).
- **Zero-based thinking has a concrete method.** Start from the outcome and the consumer of the output. Draw the simplest process that gets there with agents doing as much as possible. Then reintroduce real constraints (compliance, system limits) one at a time (CAPGEMINI-ZBPR-2025, ROLANDBERGER-2026, BCG-AGENTS-2025). Hammer's 1990 "don't automate, obliterate" argument is the classic foundation (HBR-HAMMER-1990, abstract only). Deloitte's "don't pave the cow path" is the 2025 restatement (DELOITTE-TT-2025).
- **Agent-or-not is a fit test, not a default.** Every vendor-neutral guide says to use the simplest thing that works. Rules or a single model call suit low-variance, highly standardized work. Agents suit high-variance, judgment-heavy, unstructured work (MCKINSEY-1YR-2025, OPENAI-GUIDE-2025, ANTHROPIC-BEA-2024, AZURE-PATTERNS, GOOGLE-PATTERNS-2026). Gartner says many "agentic" use cases do not need an agentic implementation (GARTNER-2025).
- **Human checkpoints are designed per action, not per process.** Common design rules:
  - gate irreversible or high-stakes actions;
  - escalate after a retry or failure threshold;
  - let the agent ask when it is unsure (OPENAI-GUIDE-2025, IMDA-MGF-2026, LANGCHAIN-AMBIENT-2025);
  - give agents earned autonomy through tiers, from shadow mode to supervised to monitored (BCG-AGENTS-2025);
  - guard against the human checkpoint decaying into rubber-stamping, called automation bias by IMDA. IMDA recommends monitoring human override rates and response times (IMDA-MGF-2026). Anthropic's telemetry shows experienced users move to auto-approve plus selective interruption (ANTHROPIC-AUTONOMY-2026).
- **Agent-ready means three things written down.** The decision criteria, the data and tool access, and the evidence trail:
  - BCG's "business context fabric" (objectives, resources, constraints) covers the first two (BCG-AGENTS-2025).
  - Deloitte and MIT Technology Review's sponsored piece stress machine-readable process definitions and explicit policy constraints (MITTR-DELOITTE-2026).
  - IMDA treats logging and monitoring as a core agent component (IMDA-MGF-2026).
  - McKinsey warns that tracking only outcomes makes errors untraceable (MCKINSEY-1YR-2025).
- **Multi-agent is a cost-and-coordination decision, and the evidence is split.** Anthropic reports a large gain for breadth-first research at about 15x the tokens of chat (ANTHROPIC-MULTI-2025). Cognition argues against parallel sub-agents for tasks with interdependent decisions (COGNITION-2025). Academic failure analysis finds most multi-agent failures come from system design and inter-agent misalignment (ARXIV-MAST-2025). Microsoft, Google, OpenAI and Anthropic all advise starting with a single agent (AZURE-PATTERNS, GOOGLE-PATTERNS-2026, OPENAI-GUIDE-2025, ANTHROPIC-BEA-2024).
- **Event-triggered background agents and managed runtimes are now productized.** Examples:
  - GitHub's coding agent starts from an assigned issue, works in the background and submits a pull request that a human must approve (GITHUB-COPILOTAGENT-2025).
  - LangChain's "ambient agents" listen to an event stream and interrupt a human only to notify, ask or request review (LANGCHAIN-AMBIENT-2025).
  - Anthropic, AWS and Microsoft each sell managed runtimes that handle session state, sandboxing, credentials and observability (ANTHROPIC-MANAGED-2026, AWS-AGENTCORE-DOCS, MSFT-FOUNDRY-DOCS).
- **Reported results are mostly unaudited, and benchmarks show a large gap to autonomous work.** Reported success stories are consultancy- or vendor-published, usually on unnamed clients. Independent benchmarks of agents on realistic work tasks show low autonomous completion: about 30% on a simulated software company (ARXIV-TAC-2025) and about 35% multi-turn on CRM tasks (ARXIV-CRMARENA-2025). Gartner forecasts more than 40% of agentic projects will be canceled by end of 2027 (GARTNER-2025). No source I found gives independent error or override rates for human checkpoints in knowledge work.

---

## 2. Core concepts in plain language

**1. Workflow redesign versus task automation.** Task automation makes one step faster inside a process people designed for people. Redesign asks what the whole process is for, which steps exist only because humans were the workers, and which decisions need a person. For knowledge work this means looking at a whole deliverable pipeline (a contract review, a credit memo, a monthly performance review), not at "drafting". For AI it means the agent often becomes the orchestrator that glues steps together, not another tool inside a step (MCKINSEY-1YR-2025, DELOITTE-TT-2025).

**2. Zero-based redesign.** Zero-based process redesign (ZBPR) assumes no existing step is sacred. You design the ideal agent-native process from a blank slate, then add back constraints you can justify. In knowledge work the useful version separates the stable outcome ("a defensible source-of-wealth memo") from the adaptive method ("how the memo gets produced today"), because the best method changes as models improve (CAPGEMINI-ZBPR-2025, ROLANDBERGER-2026, BCG-AGENTS-2025).

**3. Workflow vs agent vs single call (the complexity ladder).** Anthropic distinguishes workflows (LLMs and tools orchestrated through predefined code paths) from agents (LLMs that dynamically direct their own process and tool use). Microsoft frames a ladder: a direct model call, then a single agent with tools, then multi-agent orchestration. Use the lowest rung that reliably meets the requirement, because each rung adds cost, latency and failure modes. For an advisor: before "which agent", ask "does this even need judgment at runtime?" (ANTHROPIC-BEA-2024, AZURE-PATTERNS, GOOGLE-PATTERNS-2026).

**4. Autonomy is a dial per action, and it is earned.** Frameworks describe levels from "agent suggests, human acts" to "human only audits afterward". They set the level per task and per action, based on reversibility and cost of error. Autonomy moves up only against evidence. In practice people also grant more autonomy as they gain experience, so the real level can drift above what was designed (BCG-AGENTS-2025, IMDA-MGF-2026, ANTHROPIC-AUTONOMY-2026).

**5. Human checkpoints and escalation.** A checkpoint is a designed place where the agent stops for approval, a question or a review. Escalation is the rule for when it must hand control back, for example after repeated failure or before an irreversible action. The design risk is the checkpoint turning into a rubber stamp (automation bias). For knowledge work it also keeps professional accountability with a named person, since regulators say accountability cannot move to the tool (OPENAI-GUIDE-2025, IMDA-MGF-2026, ACCA-FRC-2026).

**6. Agent-ready process.** An agent can do a step well only if three things exist: the criteria the best people use (written, with examples), access to the data and tools they use, and a place to log evidence of what it did. Most knowledge work runs on tacit know-how, so "agent-ready" often means first extracting what separates top performers (BCG-AGENTS-2025, MCKINSEY-1YR-2025, MITTR-DELOITTE-2026).

**7. Event-triggered (ambient or background) agents.** Instead of a person opening a chat, the agent starts from an event (an assigned issue, an incoming email, a schedule) and works until it needs a human. This changes the design question from "what do people ask it?" to "which events should start work, what may it do alone, and who is pinged when it is stuck?" (LANGCHAIN-AMBIENT-2025, GITHUB-COPILOTAGENT-2025, HUMANLAYER-12FA-2025).

**8. Managed agent runtime.** A hosted service that runs long agent tasks: where the agent executes code, how its session survives crashes, how credentials stay out of reach, and how every step is observable. It lets a team spend effort on the workflow and its controls instead of the plumbing. Vendor-built runtimes exist from several providers, and their terms differ (ANTHROPIC-MANAGED-2026, AWS-AGENTCORE-DOCS, MSFT-FOUNDRY-DOCS).

**9. Multi-agent orchestration.** Several specialized agents coordinated by a manager (agents as tools) or handing off to each other as peers. It helps when work is breadth-first and parallel, or when security boundaries need separating. It hurts when sub-tasks make interdependent decisions without seeing each other's work (OPENAI-GUIDE-2025, ANTHROPIC-MULTI-2025, COGNITION-2025, ARXIV-MAST-2025).

**10. Evaluation and monitoring of agents.** An eval is a test: give the agent an input, grade the outcome. For agents, grade the end state in the environment (does the reservation exist in the database?), not just the final message. Run multiple trials because runs vary. Separate "capability" evals (hill-climb) from "regression" evals (should stay near 100%). Pair offline evals with production tracing and human review. In knowledge work the grader is usually an expert-written rubric (ANTHROPIC-EVALS-2026, MCKINSEY-1YR-2025).

**11. Failure modes and controls.** Agent failures compound across steps and are non-deterministic. The main families:
- specification and design faults;
- inter-agent misalignment;
- weak verification (ARXIV-MAST-2025);
- premature "done" and context loss in long runs (ANTHROPIC-HARNESS-2025);
- security faults such as the combination of private data, untrusted content and outbound communication (WILLISON-2025).

Controls are layered: bounded action space, human gates, step-level tracing, evals, and credentials held outside the agent's sandbox (ANTHROPIC-MANAGED-2026).

**12. AI-native operating model and the AI-native competitor.** The claim: as agents take execution, organizations shift toward humans setting goals, policy and exceptions, and agents running processes. Fewer layers and more generalist-managers are predicted. This is consultancy-led and forward-looking. The advisor can use it as a lens ("what would a new entrant with no legacy process do?") but should not present it as measured fact (BCG-AGENTS-2025, MITTR-DELOITTE-2026).

---

## 3. Expert moves

Format: **move** — when to use it — what it reveals — source ref. Moves marked *(advisor synthesis)* combine a source's finding with an obvious question and are not a quoted practice.

### Reimagine

1. **Ask "what outcome does this process exist to produce, and who consumes it?" and write it as one sentence with 2-3 success factors before mapping any step** — at the start of reimagining — separates the stable outcome from the changeable method and exposes steps that exist only for legacy reasons — ROLANDBERGER-2026 ("Separating the 'what' from the 'how'"), CAPGEMINI-ZBPR-2025.
2. **Run the zero-based question: "If we designed this today to get the outcome simply, what would it look like?" Then reintroduce each constraint (compliance, system limits, sign-off) only with a named reason** — lens 4 (reinvent the work), once the current map exists — shows which constraints are real and which are inherited — CAPGEMINI-ZBPR-2025 ("Key features of ZBPR: constraint reintroduction"), BCG-AGENTS-2025 ("Now: redesign work around zero-based, outcome-driven processes").
3. **Value-stream map the end-to-end flow "as it should work versus as it does" before hunting for automation spots** — before choosing use cases — prevents paving the cow path and surfaces workflows that cross systems and teams, where agents beat single-domain tools — DELOITTE-TT-2025 ("Redesigning processes to be agent-native", Brent Collins quote).
4. **For each step ask "is this a decision, an action, or a hand-off?" and for each decision ask how standardized it should be and how much variance it must absorb** — when choosing between lenses 2 (automate the flow) and 3 (delegate the outcome) — low-variance, high-standardization steps fit rules, and high-variance steps are agent candidates — MCKINSEY-1YR-2025 ("Agents aren't always the answer"), OPENAI-GUIDE-2025 ("When should you build an agent?": complex decisions, unwieldy rules, unstructured data).
5. **Climb the complexity ladder out loud: could a direct model call do it, then one agent with tools, then multiple agents? Make the team justify each step up** — during design review — reveals over-engineering, and each rung adds coordination overhead, latency and cost — AZURE-PATTERNS ("Start with the right level of complexity"), ANTHROPIC-BEA-2024 ("When (and when not) to use agents"), GOOGLE-PATTERNS-2026 ("Define your requirements").
6. **Ask the people doing the task how much human involvement they want (H1 "agent alone" to H5 "human alone"), then separately ask an expert how much is technically feasible, and compare** — when sorting tasks into delegate, collaborate or keep — reveals "green light" tasks (wanted and feasible) and "red light" tasks (feasible but resisted), and that workers often prefer more human agency than experts say is needed — ARXIV-WORKBANK-2026 (abstract; "Human Agency Scale"; "four zones").
7. **Ask "what would an AI-native competitor do?" in three parts: which of our steps would they not have, what would they price per outcome instead of per hour, and who would be their reviewer** — in the reimagine and make-the-case phases — turns abstract disruption talk into specific step-deletions. Treat answers as hypotheses, since the source material is consultancy opinion — MITTR-DELOITTE-2026 (sponsored; Rodgers: the real risk is competitors redesigning their operating models while you are still piloting), BCG-AGENTS-2025 ("Next: two disruptions"). *(advisor synthesis for the three-part form)*
8. **Test whether a "composite" process is the better target than a single-domain one: ask where a customer issue or deliverable crosses billing, entitlements, legal, delivery or a third party, and how many legacy screens or hand-offs a lookup takes today** — when picking what to reinvent — agents pass context across boundaries where copilots stay inside one tool, and they can bridge legacy gaps (Toyota's supply-chain team described 50 to 100 mainframe screens replaced by an agent's summary) — DELOITTE-TT-2025 (Dell Technologies interview; "Legacy system replacement").
9. **Run an agent-readiness check on each step: Is the decision criterion written down, with examples? Can the agent reach the data and tools a good worker uses? Where will evidence of what it did be logged?** — before committing a reimagined design to build — exposes tacit know-how, data that is not searchable or reusable, and missing audit trail. BCG's "business context fabric" lists objectives, resources and constraints. Deloitte's guest expert calls for machine-readable process definitions and explicit policy constraints. In Deloitte's survey nearly half of organizations cited data searchability (48%) and reusability (47%) as challenges — BCG-AGENTS-2025 ("Now: embed your company's context"), MITTR-DELOITTE-2026 (sponsored), DELOITTE-TT-2025 ("The agentic reality gap"), IMDA-MGF-2026 (logging and monitoring as a core component).

### Prioritize

10. **Ask for cost to serve or cost per transaction for the process before ranking use cases** — at prioritization — organizations that do not know their unit economics chase flashy pilots over value — MITTR-DELOITTE-2026 (Rodgers quote; sponsored content).
11. **Require a finance-signed ROI and a named business owner before a use case leaves pilot, and route builds through an architecture review rather than letting teams build ad hoc** — scaling stage, head-of-AI scope — keeps experiments as experiments. Dell Technologies' CTO described exactly this gate and an architectural review board — DELOITTE-TT-2025 (John Roese interview).
12. **Look for the reuse case: list the capabilities (ingest, extract, search, analyze) several workflows share and prioritize reusable components over one-off agents** — portfolio prioritization at unit or organization scope — avoids redundant agents; McKinsey says integrating shared capabilities into one platform helps virtually eliminate 30 to 50 percent of nonessential work — MCKINSEY-1YR-2025 ("The best use case is the reuse case"; consultancy-reported).
13. **Probe for "agent washing": ask what the proposed agent does at runtime that a rule, a script or a prompt would not** — when a vendor or team pitches "an agent" — separates relabeled chatbots, RPA and assistants from real agency — GARTNER-2025, DELOITTE-TT-2025 ("agent washing", "automation use cases in disguise").

### Plan-and-control

14. **Design each human contact as one of three types — notify (tell, no action), question (unblock me), review (approve, edit or redirect) — and decide per step** — when specifying checkpoints — avoids both blanket approval and silent autonomy — LANGCHAIN-AMBIENT-2025 ("Human-in-the-loop").
15. **Set two escalation triggers in writing: a retry/failure threshold, and a list of high-risk actions (irreversible, sensitive, high-value) that always pause for a person** — in every checkpoint design — gives a testable rule for when the agent must stop — OPENAI-GUIDE-2025 ("Plan for human intervention").
16. **Define significant checkpoints in the workflow (before writing to a database, paying, deleting) and audit whether the human oversight is working** — governance design — addresses the automation-bias risk that nominal human-in-the-loop creates — IMDA-MGF-2026 ("Make humans meaningfully accountable"; automation bias).
17. **Start every agent in shadow mode (agent suggests, human acts), write the promotion thresholds to supervised and then monitored autonomy, and demote on a miss** — rollout planning — makes autonomy evidence-based. BCG's version uses four tiers and an example 90% confidence trigger for reverting. These are BCG's illustrative numbers and not a tested standard — BCG-AGENTS-2025 ("The Trust Protocol").
18. **Track human override rate and response time per reviewer and per checkpoint** — after launch — detects rubber-stamping and alert fatigue before an incident — IMDA-MGF-2026 (automation bias practices). Related telemetry from Anthropic: auto-approve rose from about 20% of sessions for new users to over 40% for experienced users, while interrupts also rose from 5% to 9% of turns — ANTHROPIC-AUTONOMY-2026.
19. **Bound the agent by design: task-level scope only, no self-initiation, no decision authority, advisory outputs that a named reviewer validates** — regulated or high-stakes work — OCBC's source-of-wealth memo agent is the worked example — IMDA-MGF-2026 (OCBC case study).
20. **Name the accountable humans by role: use-case owner, technology-risk reviewer, builder who monitors model changes, and end-user reviewers who approve outputs** — before launch — prevents accountability falling into the gap between teams. PwC Singapore's report-drafting agent allocates exactly these four roles — IMDA-MGF-2026 (PwC Singapore case study).
21. **Tier governance by level of agency: lightweight pathway for low-agency agents, impact assessment in the middle, enterprise-architecture escalation at the top** — organization-wide rollout — keeps governance proportionate so low-risk agents are not stuck in review. MSD, as described by IMDA, uses five levels — IMDA-MGF-2026 (MSD case study).
22. **Write the agent a job description and an onboarding plan: duties, boundaries, escalation, good and bad examples, and a feedback loop from its reviewers** — build phase — McKinsey quotes a business leader saying onboarding an agent resembles hiring more than deploying software — MCKINSEY-1YR-2025 ("Stop 'AI slop'").
23. **Ask the experts to write down 20-30 real inputs with the right outputs, focused on what separates top performers from average ones, and turn them into the eval set** — before build and again before each tier promotion — turns tacit know-how into a training manual and a performance test. McKinsey says labeled sets can reach thousands for complex agents — MCKINSEY-1YR-2025.
24. **Grade the end state, not the path: ask "what should exist in the system if this worked?" and test for it, with multiple trials per task** — eval design — avoids penalizing valid alternative routes and catches "said it did it" failures — ANTHROPIC-EVALS-2026 ("The structure of an evaluation"), ANTHROPIC-MULTI-2025 (appendix on end-state evaluation).
25. **Split evals into capability evals (low pass rate, hill-climb) and regression evals (near-100%), and promote capability evals that saturate into the regression suite** — after launch — protects against backsliding when prompts, tools or models change — ANTHROPIC-EVALS-2026 ("Capability vs. regression evals").
26. **Insist on step-level tracing, not outcome-only tracking, so a drop in accuracy can be traced to a cause** — build phase — in McKinsey's contract-review example, tracing showed that a user segment was submitting lower-quality data, and the fix was upstream formatting guidance — MCKINSEY-1YR-2025 ("Make it easy to track and verify every step"). Adoption context: 89% of 1,300+ surveyed practitioners reported some agent observability, versus 52% running offline evals (LANGCHAIN-STATE-2025, vendor-published survey).
27. **Run the "lethal trifecta" check on every agent: does it combine access to private data, exposure to untrusted content, and a way to communicate externally? Remove at least one leg** — security review — finds prompt-injection exfiltration paths that no amount of prompting reliably closes — WILLISON-2025.
28. **Ask where credentials live: can code the agent generates reach the tokens?** — platform design — a structural control is stronger than hoping the agent will not misuse a limited token. Anthropic's managed runtime keeps tokens in a vault outside the sandbox — ANTHROPIC-MANAGED-2026 ("The security boundary").
29. **For any multi-agent proposal, ask what each agent can see of the others' actions and decisions, and what the single-agent baseline scored** — design review — conflicting implicit decisions are the characteristic failure of parallel sub-agents. Default to a single-threaded agent unless the work is breadth-first and independent — COGNITION-2025 ("Principles of Context Engineering"), ANTHROPIC-MULTI-2025 ("Benefits of a multi-agent system"), ARXIV-MAST-2025.
30. **Ask which parts of the harness exist to compensate for model weaknesses, and schedule a re-test when the model changes** — long-lived agents — scaffolding goes stale. Anthropic reports that a context-reset workaround needed on one model was dead weight on the next — ANTHROPIC-MANAGED-2026.

---

## 4. Question bank

Tags: scope = **[team]**, **[unit]**, **[org]**. Journey stage = *exploring*, *piloting*, *scaling*. Questions come from the expert moves above and from the sources. Rows I wrote as obvious follow-ups are marked *(advisor synthesis)*.

### Map and diagnose (kept short; owned by other topics)
- Which deliverable or decision does this process exist to produce, and who uses it? [team] *exploring* (ROLANDBERGER-2026)
- Walk me through the last real case from trigger to hand-off. Where did it wait, loop back or get redone? [team] *exploring* (value-stream view from DELOITTE-TT-2025; wording is advisor synthesis)
- What does one transaction cost to serve today, and how many a month? [unit] *exploring* (MITTR-DELOITTE-2026)
- Which steps run on tacit judgment that nobody has written down? [team] *exploring* (BCG-AGENTS-2025, MCKINSEY-1YR-2025)
- Which systems does the work cross, and which parts are third parties? [unit] *exploring* (DELOITTE-TT-2025)

### Reimagine
- If a new firm started today with agents and no legacy process, which of these steps would not exist? [team/unit/org] *exploring* (MITTR-DELOITTE-2026, CAPGEMINI-ZBPR-2025)
- Which step exists only because a person used to do it? Which exists only because of a system limit? [team] *exploring* (CAPGEMINI-ZBPR-2025)
- What is the outcome in one sentence, and what are the two or three success factors? [team] *exploring* (ROLANDBERGER-2026)
- Of the steps left, which need judgment at runtime and which follow a fixed rule? [team] *exploring* (MCKINSEY-1YR-2025, ANTHROPIC-BEA-2024)
- Could a single prompt or rule handle this step? What does an agent add? [team] *exploring/piloting* (AZURE-PATTERNS, GARTNER-2025)
- Which tasks would your people want an agent to do alone, which with them, and which never? [team] *exploring* (ARXIV-WORKBANK-2026)
- **Lens 1, improve the step:** which step has the clearest rubric a good reviewer already applies? [team] *piloting* (advisor synthesis from MCKINSEY-1YR-2025)
- **Lens 2, automate the flow:** which hand-offs between steps lose context today? [team/unit] *piloting* (DELOITTE-TT-2025)
- **Lens 3, delegate the outcome:** what would you hand over end-to-end if you could see exactly what it did and stop it? [team/unit] *piloting* (BCG-AGENTS-2025, ANTHROPIC-AUTONOMY-2026)
- **Lens 4, reinvent the work:** what would customers or clients buy if this took minutes and cost a fraction? [unit/org] *exploring* (BCG-AGENTS-2025 "differentiation"; advisor synthesis)
- Where would the work run if it were triggered by an event instead of a request? What is the event? [team/unit] *exploring/piloting* (LANGCHAIN-AMBIENT-2025, GITHUB-COPILOTAGENT-2025)

### Prioritize
- What is the unit cost and volume of the process, and who signs off the ROI? [unit] *piloting* (DELOITTE-TT-2025 Dell interview, MITTR-DELOITTE-2026)
- Which of these use cases share the same components (ingest, extract, search, analyze)? [unit/org] *scaling* (MCKINSEY-1YR-2025)
- What does a wrong output cost here: a rework, a client complaint, a regulatory finding? [team] *piloting* (OPENAI-GUIDE-2025, IMDA-MGF-2026)
- Are the data and systems the agent needs reachable, and is the data searchable and reusable? [unit] *piloting* (DELOITTE-TT-2025: 48% and 47% of surveyed organizations cited searchability and reusability of data as challenges)
- How many of our agent proposals are really automation or assistants renamed? [org] *scaling* (GARTNER-2025)
- Which use cases need a platform investment first (identity, observability, orchestration) before they can run? [org] *scaling* (MCKINSEY-SEIZE-2025 "agentic AI mesh"; ANTHROPIC-MANAGED-2026)

### Plan and control
- At which actions must a person approve, and which triggers send work to a person? [team] *piloting* (OPENAI-GUIDE-2025, IMDA-MGF-2026)
- Who is the named accountable owner, who reviews outputs, who monitors the model? [team/unit] *piloting* (IMDA-MGF-2026 PwC Singapore case)
- What does the agent do when it is unsure? Does it ask, guess or stop? [team] *piloting* (ANTHROPIC-AUTONOMY-2026, LANGCHAIN-AMBIENT-2025)
- What evidence of each step is logged, where, and who can inspect it? [team/unit] *piloting* (IMDA-MGF-2026, MCKINSEY-1YR-2025)
- What 20 real cases and right answers can your best reviewer write today? [team] *piloting* (MCKINSEY-1YR-2025)
- What pass rate on the eval set earns the next level of autonomy? What demotes it? [team/unit] *piloting/scaling* (BCG-AGENTS-2025, ANTHROPIC-EVALS-2026)
- How will we know reviewers are still reviewing? Do we track override rate and time to approve? [unit] *scaling* (IMDA-MGF-2026)
- Which agents touch private data, read untrusted content and can send things out? [team/unit] *piloting* (WILLISON-2025)
- Which credentials does the agent hold, and can its generated code reach them? [unit/org] *scaling* (ANTHROPIC-MANAGED-2026)
- What is the cost per completed task, and what is the single-agent baseline? [team/unit] *piloting* (ANTHROPIC-MULTI-2025, DELOITTE-TT-2025 "FinOps for agents")
- Who decides when a model change triggers a re-test? [unit/org] *scaling* (ANTHROPIC-EVALS-2026, ANTHROPIC-MANAGED-2026)
- How many agents are live across the unit or organization, who owns each, and which tier of governance applies? [unit/org] *scaling* (MCKINSEY-SEIZE-2025 "uncontrolled sprawl"; IMDA-MGF-2026 MSD case)
- What changes in roles: who reviews, who maintains the agents' rules, who handles exceptions? [unit/org] *scaling* (DELOITTE-TT-2025, MCKINSEY-1YR-2025)
- If a regulator or client asked who is responsible for this output, what would we say? [unit/org] *piloting/scaling* (ACCA-FRC-2026)

---

## 5. Common traps

| Trap | Why it happens | Evidence | How to avoid |
|---|---|---|---|
| **Automating waste (paving the cow path)** | Teams look for steps to speed up instead of asking whether the process should exist | Deloitte says many enterprises try to automate existing processes, which were designed by and for human workers, without reimagining how the work should be done (DELOITTE-TT-2025). Hammer's 1990 HBR article is titled "Don't Automate, Obliterate" (HBR-HAMMER-1990) | Zero-based question first (moves 1-3); value-stream map before use-case hunting |
| **Focusing on the agent, not the workflow** | The agent is the visible, demo-able thing | McKinsey: this leads to "great-looking agents" that do not improve the overall workflow (MCKINSEY-1YR-2025) | Start from the workflow map and the user pain points; measure workflow outcomes |
| **Agent where something simpler would do / agent washing** | Hype, and vendors relabeling chatbots and RPA | Gartner: "agent washing" and an estimate that only about 130 of thousands of agentic vendors are real; "many use cases ... don't require agentic implementations" (GARTNER-2025). Deloitte reports the same pattern (DELOITTE-TT-2025) | Fit test on variance and standardization (move 4); ladder (move 5); runtime-judgment question (move 13) |
| **Demo-ware and "AI slop"; launch and leave** | Teams skip evals and domain-expert involvement | McKinsey: users lose trust and adoption falls, and experts must stay involved because "there can be no 'launch and leave'" (MCKINSEY-1YR-2025) | Job description and onboarding (move 22); expert-written evals (move 23); ongoing monitoring |
| **Tracking only outcomes** | Cheap to measure; no step-level logging | McKinsey: with hundreds of agents, outcome-only tracking makes mistakes hard to diagnose (MCKINSEY-1YR-2025) | Step-level tracing (move 26) |
| **Human-in-the-loop that becomes a rubber stamp** | Approval fatigue, automation bias, step-by-step approval becomes impractical as steps multiply | IMDA: requiring humans to oversee continuously "can also lead to automation bias and alert fatigue" (IMDA-MGF-2026). Anthropic: on high-complexity API tasks 67% of tool calls had some human involvement versus 87% on minimal-complexity ones, and experienced Claude Code users shift to auto-approve plus selective interruption (ANTHROPIC-AUTONOMY-2026) | Gate by action risk, not volume; track override rate and response time (move 18); audit the oversight |
| **Autonomy granted faster than evidence** | Trust accumulates with experience, and defaults get relaxed | Anthropic notes that part of the rise in auto-approve may be users changing settings, and that the autonomy models can handle exceeds what is used in practice (ANTHROPIC-AUTONOMY-2026) | Tiered rollout with promotion and demotion thresholds (move 17) |
| **Multi-agent by default** | It looks like org-chart thinking, and frameworks make it easy | Cognition: parallel sub-agents act on conflicting implicit assumptions (COGNITION-2025). MAST: 14 failure modes across system design, inter-agent misalignment and task verification, on 1,600+ annotated traces (ARXIV-MAST-2025). Anthropic: multi-agent used about 15x chat tokens, and early versions spawned too many sub-agents for simple queries (ANTHROPIC-MULTI-2025) | Single agent first; require a single-agent baseline (move 29) |
| **Mistaking benchmark scores for work-readiness** | Capability evals are idealized | On a simulated software company the best tested agent autonomously completed 30.3% of 175 tasks (ARXIV-TAC-2025). On CRM tasks the best agents reached about 58% single-turn and about 35% multi-turn, with near-zero confidentiality awareness (ARXIV-CRMARENA-2025). On the other side, an OpenAI benchmark found deliverables from one frontier model were rated as good as or better than experts' on 47.6% of gold-subset tasks (OPENAI-GDPVAL-2025, vendor-published) | Test on your own cases; do not generalize either direction |
| **Cost-first judgment of AI service** | Savings are measurable; quality is not | Klarna's CEO reportedly said AI was too focused on cost and quality declined, and the company began rehiring human support in 2025 (KLARNA-REPORTS-2025, search-only) | Pair a cost metric with a quality metric and a customer or client outcome |
| **Prompt injection and exfiltration** | LLMs follow instructions found in content | Willison's "lethal trifecta" analysis (WILLISON-2025); Anthropic moved credentials outside the agent's sandbox so a prompt injection cannot reach them (ANTHROPIC-MANAGED-2026) | Remove one leg of the trifecta (move 27); structural credential isolation (move 28) |
| **Long-running agents that quit early or lose track** | Each new session starts without memory | Anthropic observed two failure patterns: attempting too much at once, and a later session declaring the job done after seeing progress (ANTHROPIC-HARNESS-2025) | Incremental feature-by-feature work, clean-state hand-offs and external progress artifacts |
| **Open-ended business autonomy without scaffolding** | Models were given real authority over a business | In Project Vend, a Claude agent running an office shop made discount and pricing errors and had an identity-confusion episode, and did not make money. Anthropic attributes many mistakes to missing scaffolding (ANTHROPIC-VEND-2025) | Narrow scope, explicit tools and guardrails, human oversight |
| **Legacy systems, data and governance gaps** | Agents depend on APIs and data built for humans | Deloitte, citing Gartner, says over 40% of agentic projects will fail by 2027 because legacy systems cannot support agent execution. Gartner's own release gives different causes: escalating costs, unclear value and inadequate risk controls (GARTNER-2025). Nearly half of surveyed organizations cite data searchability (48%) and reusability (47%) as challenges (DELOITTE-TT-2025) | Agent-readiness check (move 9); platform-first for shared capabilities |
| **Treating accountability as delegable** | Tool does the work, so ownership blurs | The UK FRC's guidance, as summarized by ACCA, keeps firms and engagement partners fully responsible for audit quality whatever tool is used (ACCA-FRC-2026). In McKinsey's legal example a lawyer still had to sign (MCKINSEY-1YR-2025) | Named accountable roles (move 20); human approval at sign-off steps |
| **Pilot trap and sprawl** | Fragmented, bottom-up micro-initiatives | McKinsey (June 2025): about 90% of vertical use cases remain in pilot mode, and it warns of uncontrolled agent sprawl (MCKINSEY-SEIZE-2025). Gartner expects more than 40% of agentic projects canceled by the end of 2027 (GARTNER-2025) | Business-process focus, cross-functional squads, a shared platform and governance tiers |

---

## 6. Evidence

Each row: figure | what it measures (source's words, paraphrased) | provenance | source and locator.

### Adoption, value capture and failure

| Figure | What it measures | Provenance | Source |
|---|---|---|---|
| About 78% of companies use gen AI in at least one function (55% a year earlier); "just as many" report no significant bottom-line impact | Share of surveyed companies; McKinsey cites its own research | consultancy-published | MCKINSEY-SEIZE-2025, "At a glance" and "Gen AI is everywhere" |
| About 90% of vertical (function-specific) use cases remain in pilot | McKinsey's statement on vertical gen AI use cases; denominator not stated in the text I read | consultancy-published | MCKINSEY-SEIZE-2025, "At a glance" |
| 30% of surveyed organizations exploring agentic options, 38% piloting, 14% with solutions ready to deploy, 11% actively using in production; 42% still developing their roadmap; 35% no formal strategy | Deloitte's 2025 Emerging Technology Trends study; sample size not stated on the page | consultancy-published | DELOITTE-TT-2025, "The agent reality check" |
| 2% of organizations have deployed agents at scale, 12% partial scale, 23% pilots, 61% exploring; fewer than 1 in 5 report high data and technology maturity | Survey of 1,500 senior executives in 14 countries | consultancy-published (Capgemini Research Institute) | CAPGEMINI-RISE-2025, key findings |
| Trust in fully autonomous agents fell from 43% to 27% in one year | Share of surveyed executives (same survey); the page says "in one year" without naming the earlier survey | consultancy-published | CAPGEMINI-RISE-2025 |
| 15% of business processes expected to reach semi- or full autonomy within 12 months; up to $450 billion value by 2028 across surveyed markets | Respondents' expectation and Capgemini's estimate (forecasts, not measurements) | consultancy-published | CAPGEMINI-RISE-2025 |
| 5% of firms are "future-built", 35% scaling AI, 60% "reaping hardly any material value"; future-built firms report 5x the revenue increases and 3x the cost reductions of others | BCG study across firms (sample not shown in my copy) | consultancy-published | BCG-GAP-2025 (partial read) |
| 35% of organizations already using agentic AI, 44% plan to | BCG study with a co-author name that was stripped from my copy | consultancy-published | BCG-AGENTS-2025, intro |
| Over 40% of agentic AI projects will be canceled by end of 2027 (escalating costs, unclear value, inadequate risk controls) | Gartner prediction. The accompanying January 2025 poll covered 3,412 webinar attendees: 19% significant investment, 42% conservative, 8% none, 31% wait and see or unsure | analyst-published (forecast; poll is a self-selected webinar audience) | GARTNER-2025 |
| At least 15% of day-to-day work decisions made autonomously by agentic AI by 2028 (0% in 2024); 33% of enterprise software apps include agentic AI by 2028 (under 1% in 2024) | Gartner forecast | analyst-published | GARTNER-2025 |
| 57.3% of 1,300+ surveyed practitioners have agents in production; quality is the top barrier (about one third); 89% have some observability, 52.4% run offline evals, 37.3% online evals; human review (59.8%) and LLM-as-judge (53.3%) are the main evaluation methods | LangChain survey fielded 18 Nov to 2 Dec 2025. LangChain sells agent observability and evals, and respondents are likely LangChain-community skewed | vendor-published | LANGCHAIN-STATE-2025 |
| 95% of AI investments fail to deliver the expected ROI | Roland Berger's statement, attributed to MIT NANDA's 2025 report. I could not open the NANDA report, so I cannot say what it measures or how it defines failure | second-hand (consultancy citing a report I did not read) | ROLANDBERGER-2026 (cited; MIT-NANDA-2025 is search-only). Use only as "cited by", not as a finding |

### Outcomes reported for redesigned work (all unnamed clients unless stated)

| Figure | What it measures | Provenance | Source |
|---|---|---|---|
| Shipbuilder: about 40% less engineering effort and 60% shorter design and engineering lead time using agents to run a multistep design process | Reported outcome for one unnamed client; baseline and period not stated | consultancy-published, self-reported by the advisor | BCG-AGENTS-2025, "early adopters" |
| Global company: product-innovation cycle time cut by roughly 60% with meta-agents and worker agents | One unnamed client after rebuilding the workflow from scratch | consultancy-published | BCG-AGENTS-2025, "Now" |
| Payroll provider: processing speed improved by more than 50% through a supervisor agent and worker agents; telco: 40,000+ messages a day and a fivefold jump in digital sales | Unnamed clients | consultancy-published | BCG-AGENTS-2025 |
| One client automated 80% of a workflow once considered too unstructured | Unnamed client, author's own client work | consultancy-published (practitioner article) | CAPGEMINI-ZBPR-2025 |
| P&C insurer: user acceptance near 95% after adding visual review aids (bounding boxes, highlights, auto-scroll) | Unnamed client; acceptance measure not defined | consultancy-published | MCKINSEY-1YR-2025, "Humans remain essential" |
| McKinsey says its integrated-platform approach helps virtually eliminate 30 to 50 percent of the nonessential work typically required | McKinsey's experience across its builds; no baseline described | consultancy-published | MCKINSEY-1YR-2025, "The best use case is the reuse case" |
| Roland Berger cites "tenfold" efficiency improvements for reimagined processes | Key-insights summary; the underlying case not read in detail | consultancy-published | ROLANDBERGER-2026 |
| Dell Technologies: services organization digitized every process and reports "double-digit improvements" on each cost and customer-satisfaction metric | Executive's interview statement; no baselines shown | self-reported (interview) | DELOITTE-TT-2025, John Roese interview |

### Human oversight and autonomy in practice

| Figure | What it measures | Provenance | Source |
|---|---|---|---|
| 99.9th-percentile Claude Code turn length rose from under 25 min to over 45 min between Oct 2025 and Jan 2026; median turn about 45 seconds | Time Claude works before stopping, per turn, in interactive Claude Code sessions | vendor-published (Anthropic's own telemetry) | ANTHROPIC-AUTONOMY-2026, "Claude Code is working autonomously for longer" |
| Full auto-approve in roughly 20% of sessions for new users (<50 sessions), over 40% by about 750 sessions; interrupts in about 5% of turns for new users, about 9% for experienced | Per-session and per-turn behavior of Claude Code users by tenure. Default settings require manual approval, so part of the shift is user configuration | vendor-published | ANTHROPIC-AUTONOMY-2026 |
| On the most complex tasks Claude Code asks for clarification more than twice as often as on minimal-complexity tasks, and more often than humans interrupt | Agent-initiated stops versus human interrupts, 500k sessions | vendor-published | ANTHROPIC-AUTONOMY-2026 |
| Human involvement in 87% of tool calls on minimal-complexity API tasks vs 67% on high-complexity | Share of tool calls with some human involvement (Claude-estimated complexity) | vendor-published | ANTHROPIC-AUTONOMY-2026 |
| Internal Claude Code success rate on the hardest tasks doubled Aug to Dec while human interventions per session fell from 5.4 to 3.3 | Anthropic internal users only | self-reported (vendor internal) | ANTHROPIC-AUTONOMY-2026 |
| Software engineering is nearly 50% of agentic activity on the public API | Share of agentic tool-call activity in Anthropic's sample | vendor-published | ANTHROPIC-AUTONOMY-2026 |
| Among heavy adopters: 29% expect fewer traditional entry-level roles; 43% expect more demand for generalists who manage human-agent teams; 45% of AI leaders expect fewer middle-management layers; 58% expect a fundamental governance shift in three years; one-third expect AI to hold more decision authority | BCG survey respondents' expectations, not outcomes | consultancy-published | BCG-AGENTS-2025, "Next" |
| 46.1% of tasks drew positive worker attitudes toward agent automation; 45.2% of occupations have H3 (equal partnership) as the dominant worker-desired level; workers generally prefer more human agency than experts judge necessary | WORKBank: 1,500 workers, 52 AI experts, 844 tasks, 104 occupations, data collected Jan-May 2025 | independent (academic, Stanford) | ARXIV-WORKBANK-2026 |
| 41.0% of Y Combinator company-task mappings fall in the Low Priority or Red Light zones | Authors' GPT-4-based mapping of YC company descriptions to tasks | independent | ARXIV-WORKBANK-2026 |

### Capability benchmarks and failure analyses

| Figure | What it measures | Provenance | Source |
|---|---|---|---|
| Best tested agent autonomously completed 30.3% of 175 tasks, 39.3% with partial credit (earlier version: 24% with an older model, per a search summary I did not verify) | Tasks completed to the end in a simulated software company (CMU benchmark, v3 Sep 2025) | independent (academic) | ARXIV-TAC-2025 |
| About 58% single-turn success, about 35% multi-turn; over 83% on workflow execution; near-zero confidentiality awareness | CRMArena-Pro, 19 expert-validated sales, service and CPQ tasks. The authors include Salesforce-affiliated researchers per search results, though the abstract page does not state affiliation | vendor-affiliated benchmark (treat as vendor-published) | ARXIV-CRMARENA-2025 |
| 47.6% of Claude Opus 4.1 deliverables were rated better than or equal to the human expert's on GDPval's gold subset; the experimental automated grader agreed with experts 66% of the time versus 71% expert-to-expert | Blind pairwise expert comparison, 220 tasks, 44 occupations. Run by OpenAI | vendor-published | OPENAI-GDPVAL-2025, sections 3.1 and abstract |
| 14 multi-agent failure modes in 3 categories; Cohen's kappa 0.88; 1,600+ annotated traces over 7 frameworks; best intervention case studies improved results by up to 15.6% with the same model | MAST taxonomy and dataset (Cemri, Pan, Yang et al.; a search summary describes them as UC Berkeley-led) | independent (academic) | ARXIV-MAST-2025, abstract and section 5.3 |
| Sonnet 4 sub-agents beat single-agent Opus 4 by 90.2% on Anthropic's internal research eval; agents use about 4x and multi-agent about 15x the tokens of chat; token usage alone explains 80% of BrowseComp performance variance | Anthropic internal evaluations of its Research feature | vendor-published | ANTHROPIC-MULTI-2025 |
| Task length agents can complete at 50% success was doubling about every 7 months over six years (METR's later estimates replace this; METR flags the post as partly out of date) | Software-task time horizon | independent | METR-2025 |

### Search-only figures (notes only, not used above)
- **Microsoft Work Trend Index 2025** (search summary of Microsoft's 23 April 2025 blog): introduces a "human-agent ratio" as a management question for leaders and reports 46% of leaders saying their organization uses agents to fully automate workstreams or processes. The summary says a regional release gives a different figure, so I did not rely on it (MSFT-WTI-2025).
- **Klarna** (trade-press coverage of a Bloomberg interview): the company's 2024 annual report said its AI assistant did the work of 700 employees, and in May 2025 the CEO said the company would hire human support staff again after quality concerns (KLARNA-REPORTS-2025).
- **KPMG** (Bloomberg Law headline and search summary): in April 2025 KPMG said it was building agents into its global audit platform for routine tasks such as expense reviews and searching for unrecorded liabilities (KPMG-AUDIT-2025).
- **MIT NANDA** "95%" figure and the Stanford payroll study showing a 16% employment decline for early-career workers in AI-exposed roles are second-hand (via ROLANDBERGER-2026 and BCG-AGENTS-2025).

### Quality evidence: what is absent
I found **no published error rates, reviewer override rates or parallel-run results** for human checkpoints in agentic knowledge work (audit, legal, advisory) from an independent party. The nearest items are:
- Anthropic's coding-agent telemetry (ANTHROPIC-AUTONOMY-2026);
- McKinsey's unnamed client anecdotes about reviewer acceptance (MCKINSEY-1YR-2025);
- IMDA's recommendation to monitor override rates, which is guidance and not data (IMDA-MGF-2026).

Treat any claim of "human-in-the-loop catches X%" as unsupported.

---

## 7. Worked examples

### A. Contract review at an alternative dispute resolution (ADR) provider (knowledge work, legal)
Source: MCKINSEY-1YR-2025 ("It's not about the agent; it's about the workflow", "Make it easy to track and verify", "Humans remain essential"). Unnamed client; McKinsey-reported.
- **Redesign:**
  - The team redesigned the contract-review workflow as an agentic system that learns inside the workflow. Every user edit in the document editor was logged and categorized, giving engineers feedback to adjust prompts and enrich the knowledge base as legal reasoning evolved.
  - For a related legal-analysis workflow, they decided where humans enter: agents organized core claims and dollar amounts, but lawyers double-checked and approved them. Agents proposed case work plans, which lawyers reviewed and adjusted. Agents flagged edge cases and anomalies. A person still signed.
- **Control:**
  - Because every step was traced, a sudden accuracy drop on a new set of cases was traced to certain user segments submitting lower-quality data. The fix was upstream formatting guidance and parser changes, not a model change.
- **Lesson for the advisor:**
  - Checkpoints sit on the high-consequence outputs (claims, plans, signature).
  - Edits become training signal.
  - Step-level traces separate a data problem from a reasoning problem.
- **Limits:** no baseline or accuracy figures are given.

### B. Bounded agents in regulated knowledge work: OCBC source-of-wealth memos and PwC Singapore report drafting
Source: IMDA-MGF-2026 (case studies in "Assess and bound the risks upfront" and "Make humans meaningfully accountable"), as described by IMDA. Named organizations.
- **OCBC / Bank of Singapore:**
  - Relationship managers and compliance staff synthesize customer documents into a Source of Wealth memo.
  - The agentic system parses income-related documents and drafts the memo against internal guidelines.
  - Autonomy is bounded by design: task-level only (extract, draft, check), triggered only by predefined workflows, with no decision authority.
  - Outputs are advisory, and designated human reviewers validate at critical points. The system does not make credit, onboarding or risk decisions.
- **PwC Singapore (AI Factory):**
  - Three coordinated agents, mostly sequential, draft research and analysis sections of internal reports from firm-maintained templates.
  - Accountability is split into four roles: use-case owner (appropriateness and accountable use), technology risk team (risk assessment and control advice), AI Factory (design, guardrails, monitoring of model changes), and end-user subject-matter specialists (review and approve; AI content is a first draft).
- **Lesson for the advisor:** a recipe for "delegate the outcome" in high-stakes work. Bound the action space, make the human decisions explicit, and name the roles. IMDA does not report outcome metrics for either case.

### C. End-to-end process choice: HPE's "Alfred" and Mapfre's claims handling
Source: DELOITTE-TT-2025 ("Redesigning processes to be agent-native", "Managing the mixed silicon- and carbon-based workforce"). Named organizations; executives' own accounts.
- **HPE:**
  - The finance team chose an end-to-end process (internal operational performance reviews) so it could "operate differently", not fix one pain point.
  - The solution is a front end working with four agents. They break down queries, analyze SQL data, build charts, and produce structured reports from the data warehouse.
  - The CFO said the use case was chosen partly because it applies across functions.
- **Mapfre:**
  - Agents handle routine administrative claims tasks such as damage assessment.
  - A person is always in the loop for sensitive tasks such as customer communication.
  - Anything that carries risk goes through a human, and the company says the design is "hybrid by design".
- **Lesson:** choose a whole, data-rich, repeatable process. Allocate by risk, with a human on customer-facing and risky steps. No outcome figures were given in the source for either.

### D. Event-triggered background agent with human gates: GitHub Copilot coding agent
Source: GITHUB-COPILOTAGENT-2025 (vendor announcement; includes an EY quote). Translate to knowledge work by analogy.
- **Trigger:** a person assigns an issue to the agent (as they would a teammate) or prompts it in the editor.
- **Execution:** the agent boots a secure environment, works in the background, pushes commits to a draft pull request, and shows reasoning and validation steps in session logs.
- **Gates:**
  - The agent can push only to branches it created.
  - The person who asked for the pull request cannot be the one to approve it, so required-review rules still apply.
  - Human approval is required before the CI/CD workflows run.
  - Internet access is limited to an allow-list.
- **Fit stated by the vendor:** low-to-medium complexity tasks in well-tested codebases, which gives the agent an objective check that most knowledge work lacks.
- **Lesson:** the design pattern transfers (assignment trigger, background work, draft deliverable, independent approver, logged steps). The enabling condition (automatic tests) does not. The advisor should ask what plays the role of "tests" in the client's process, for example a reviewer's rubric or a reconciliation.

---

## 8. Mapping to phases

### Reimagine
- Supplies the redesign stance: zero-based, outcome-first, constraints reintroduced with reasons (moves 1-3).
- Supplies tests for lens choice:
  - improve the step vs automate the flow vs delegate the outcome vs reinvent the work;
  - rule or single call vs agent vs multi-agent;
  - the human agency scale for splitting tasks between people and agents (moves 4-6, 8, 9).
- Supplies the AI-native-competitor prompt, flagged as hypothesis-generation and not evidence (move 7).
- Supplies the agent-ready checklist (criteria, data and tool access, evidence log) used to judge whether a reimagined design is buildable now.
- Supplies design patterns for lens 3 and lens 4: manager and peer orchestration, event-triggered background agents, and the single-threaded default.

### Prioritize
- Supplies selection filters:
  - agent fit by variance and standardization;
  - agent-washing probe;
  - cost-to-serve baseline;
  - business owner and finance-signed ROI;
  - reuse across workflows;
  - platform prerequisites (moves 10-13).
- Supplies the cautionary evidence base:
  - Gartner's cancellation forecast;
  - McKinsey's pilot-trap numbers;
  - Deloitte's production-readiness figures;
  - low benchmark autonomy for long or multi-turn tasks.
- Supplies risk-tiering inputs (reversibility, cost of error, regulatory accountability) for ranking.
- Gaps to flag for the advisor: independent ROI evidence is thin, and most value claims come from consultancies describing unnamed clients.

### Plan-and-control
- Supplies the control design vocabulary: notify, question and review contacts; escalation triggers; autonomy tiers from shadow to monitored; accountability roles; governance tiers by level of agency (moves 14-21).
- Supplies the evaluation plan: expert-written eval sets, end-state grading, capability vs regression suites, step-level tracing, and override-rate monitoring (moves 22-26).
- Supplies security and platform controls: lethal-trifecta check, credential isolation, managed runtime considerations, harness re-testing on model change (moves 27-30).
- Supplies the roll-up view for unit and organization scope: reuse, shared platform, agent inventory and sprawl control, and role changes.
- Supplies cost controls: cost per task and a single-agent baseline.

---

## 9. Sources

Access: **full** = body read; **partial** = only part read; **search-only** = search summary only (not used for headline evidence). Dates are publication dates found on the page unless noted. Pages marked "via reader" were blocked to direct `curl` (403 or connection errors) and were read through the r.jina.ai text-reader mirror, which returned the page text, as the brief's access section permits. I used no further reader or search fetches after the search budget notice.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ANTHROPIC-BEA-2024 | Building effective agents | Anthropic (E. Schluntz, B. Zhang) | vendor engineering guide | https://www.anthropic.com/engineering/building-effective-agents | 2024-12-19 | full |
| ANTHROPIC-MULTI-2025 | How we built our multi-agent research system | Anthropic | vendor engineering write-up | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | full |
| ANTHROPIC-EVALS-2026 | Demystifying evals for AI agents | Anthropic | vendor engineering guide | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | 2026-01-09 | full |
| ANTHROPIC-AUTONOMY-2026 | Measuring AI agent autonomy in practice | Anthropic | vendor research (telemetry) | https://www.anthropic.com/research/measuring-agent-autonomy | 2026-02-18 | full |
| ANTHROPIC-MANAGED-2026 | Scaling Managed Agents: Decoupling the brain from the hands | Anthropic (L. Martin, G. Cemaj, M. Cohen) | vendor engineering write-up | https://anthropic.com/engineering/managed-agents | 2026-04-08 | full |
| CLAUDE-MANAGEDBLOG-2026 | The evolution of agentic surfaces: building with Claude Managed Agents | Anthropic (Applied AI team) | vendor product blog | https://claude.com/blog/building-with-claude-managed-agents | 2026-06-10 | full (customer examples Notion, Rakuten, Sentry, Asana, Atlassian are vendor-published) |
| ANTHROPIC-HARNESS-2025 | Effective harnesses for long-running agents | Anthropic | vendor engineering write-up | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents | 2025-11-26 | partial (introduction and failure patterns) |
| ANTHROPIC-VEND-2025 | Project Vend: Can Claude run a small shop? | Anthropic | vendor research | https://www.anthropic.com/research/project-vend-1 | 2025-06-27 | partial |
| ANTHROPIC-TOOLS-2025 | Writing effective tools for agents | Anthropic | vendor engineering guide | https://www.anthropic.com/engineering/writing-tools-for-agents | 2025-09-11 | partial (skimmed; no figures used) |
| ANTHROPIC-CTX-2025 | Effective context engineering for AI agents | Anthropic | vendor engineering guide | https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | 2025-09-29 | partial (skimmed; no figures used) |
| OPENAI-GUIDE-2025 | A practical guide to building agents | OpenAI | vendor guide (PDF) | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf | 2025-04 (PDF creation date 2025-04-07) | full |
| OPENAI-GDPVAL-2025 | GDPval: Evaluating AI model performance on real-world economically valuable tasks | Patwardhan et al., OpenAI | vendor benchmark paper (PDF) | https://cdn.openai.com/pdf/d5eb7428-c4e9-4a33-bd86-86dd4bcf12ce/GDPval.pdf | 2025-09 (PDF creation date 2025-09-25) | partial (abstract, headline results) |
| AZURE-PATTERNS | AI agent orchestration patterns | Microsoft Learn, Azure Architecture Center | platform guidance | https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns | undated on page | full |
| GOOGLE-PATTERNS-2026 | Choose a design pattern for your agentic AI system | Google Cloud Architecture Center | platform guidance | https://cloud.google.com/architecture/choose-design-pattern-agentic-ai-system | last reviewed 2026-05-28 | full |
| AWS-PATTERNS | Agentic AI patterns and workflows on AWS | AWS Prescriptive Guidance (A. Sempf, A. Hooker) | platform guidance | https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html | undated on page | partial (introduction only; not cited for claims) |
| AWS-AGENTCORE-DOCS | What is Amazon Bedrock AgentCore? | AWS | product documentation | https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html | undated on page | full |
| MSFT-FOUNDRY-DOCS | What is Microsoft Foundry Agent Service? | Microsoft Learn | product documentation | https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview | undated on page | partial (page notes an authorization banner; overview text readable) |
| LANGCHAIN-AMBIENT-2025 | Introducing ambient agents | LangChain | vendor/practitioner blog | https://www.langchain.com/blog/introducing-ambient-agents | 2025-01-14 | full |
| LANGCHAIN-STATE-2025 | State of AI agents (agent engineering survey) | LangChain | vendor survey report | https://www.langchain.com/state-of-agent-engineering | survey fielded 2025-11-18 to 2025-12-02; page shows a 12 June 2026 label | full |
| COGNITION-2025 | Don't build multi-agents | Cognition (Devin team) | practitioner essay | https://cognition.ai/blog/dont-build-multi-agents | 2025-06-12 | full |
| GITHUB-COPILOTAGENT-2025 | GitHub Copilot: Meet the new coding agent | GitHub (T. Dohmke) | vendor announcement | https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/ | 2025-05-19 | full |
| HUMANLAYER-12FA-2025 | 12-factor agents (README and factor pages 6, 7, 8, 11) | HumanLayer (D. Horthy) | practitioner guide (open-source repository) | https://github.com/humanlayer/12-factor-agents | undated; repository content as of 2026-10-16 | full for the factors cited |
| WILLISON-2025 | The lethal trifecta for AI agents | S. Willison | practitioner article | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | 2025-06-16 | full |
| MCKINSEY-1YR-2025 | One year of agentic AI: Six lessons from the people doing the work | McKinsey and Company (L. Yee, M. Chui, R. Roberts with S. Xu) | consultancy article | https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work | 2025-09-12 (reader metadata) | full (via reader) |
| MCKINSEY-SEIZE-2025 | Seizing the agentic AI advantage | McKinsey and Company | consultancy article | https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/seizing-the-agentic-ai-advantage | 2025-06-13 (reader metadata) | full (via reader; footnotes not visible) |
| BCG-AGENTS-2025 | How agents are accelerating the next wave of AI value creation | BCG (V. Beauchene, T. Martin et al.) | consultancy article | https://www.bcg.com/publications/2025/agents-accelerate-next-wave-of-ai-value-creation | 2025-12-15 | full (via reader) |
| BCG-GAP-2025 | The widening AI value gap (are you generating value from AI?) | BCG | consultancy report page | https://www.bcg.com/publications/2025/are-you-generating-value-from-ai-the-widening-gap | 2025-09-30 | partial (via reader) |
| GARTNER-2025 | Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 | Gartner (A. Verma quoted) | analyst press release | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | 2025-06-25 | full (via reader) |
| DELOITTE-TT-2025 | The agentic reality check: Preparing for a silicon-based workforce (Tech Trends 2026) | Deloitte Insights | consultancy report | https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html | 2025-12-10 (page modified 2026-09-09) | full |
| MITTR-DELOITTE-2026 | Enabling agent-first process redesign | MIT Technology Review Insights, in association with the Deloitte Microsoft Technology Practice | sponsored custom content (not editorial) | https://technologyreview.com/2026/04/07/1134966/enabling-agent-first-process-redesign | 2026-04-07 | full (short page; download not read) |
| CAPGEMINI-RISE-2025 | Rise of agentic AI: How trust is the key to human-AI collaboration | Capgemini Research Institute | consultancy research (survey summary page) | https://www.capgemini.com/insights/research-library/ai-agents/ | 2025-07-16 | partial (summary page; PDF not read) |
| CAPGEMINI-ZBPR-2025 | From zero to autonomous: Redesigning operations with agentic AI | Capgemini (J.-M. Prädel) | consultancy practitioner article | https://www.capgemini.com/us-en/insights/expert-perspectives/from-zero-to-autonomous-redesigning-operations-with-agentic-ai/ | 2025-11-12 | full (part 1 of a three-part series) |
| ROLANDBERGER-2026 | Leading with AI-first: Rethinking and redesigning processes and organizations | Roland Berger (E. Goos, M. Schich) | consultancy article | https://www.rolandberger.com/en/Insights/Publications/Leading-with-AI-first-Rethinking-and-redesigning-processes-and-organizations.html | 2026-07-16 | full |
| HBR-HAMMER-1990 | Reengineering work: Don't automate, obliterate | M. Hammer, Harvard Business Review | classic article | https://hbr.org/1990/07/reengineering-work-dont-automate-obliterate | 1990-07 | partial (title, issue and intro only; paywalled) |
| HBR-VERMA-2025 | Why agentic AI projects fail, and how to set yours up for success | A. Verma (Gartner), HBR | analyst article | https://hbr.org/2025/10/why-agentic-ai-projects-fail-and-how-to-set-yours-up-for-success | 2025-10-21 | partial (summary only; paywalled; not cited for figures) |
| ARXIV-WORKBANK-2026 | Future of work with AI agents: Auditing automation and augmentation potential across the U.S. workforce | Y. Shao, ..., E. Brynjolfsson, D. Yang (Stanford) | academic preprint (arXiv 2506.06576, v3 2026-02-01) | https://arxiv.org/abs/2506.06576 | v1 2025-06-06; v3 2026-02-01 | full (HTML v3) |
| ARXIV-MAST-2025 | Why do multi-agent LLM systems fail? | M. Cemri, M. Z. Pan, S. Yang et al. | academic preprint (arXiv 2503.13657, v3 2025-10-26) | https://arxiv.org/abs/2503.13657 | v1 2025-03-17; v3 2025-10-26 | full (HTML v3) |
| ARXIV-TAC-2025 | TheAgentCompany: Benchmarking LLM agents on consequential real world tasks | F. F. Xu et al. (Carnegie Mellon) | academic preprint (arXiv 2412.14161, v3 2025-09-10) | https://arxiv.org/abs/2412.14161 | v1 2024-12-18; v3 2025-09-10 | full (HTML v3) |
| ARXIV-CRMARENA-2025 | CRMArena-Pro: Holistic assessment of LLM agents across diverse business scenarios and interactions | K.-H. Huang et al. | academic preprint (arXiv 2505.18878) | https://arxiv.org/abs/2505.18878 | 2025-05-24 | partial (abstract page) |
| ARXIV-TURING-2022 | The Turing Trap: The promise and peril of human-like artificial intelligence | E. Brynjolfsson (Daedalus; arXiv 2201.04200) | academic foundation | https://arxiv.org/abs/2201.04200 | 2022 | partial (abstract; used only as a foundation for the augment-versus-substitute framing, not in claims above) |
| METR-2025 | Measuring AI ability to complete long software tasks | METR | independent research note | https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/ | 2025-03-19 | full (METR notes parts are out of date) |
| IMDA-MGF-2026 | Model AI Governance Framework for Agentic AI, version 1.5 | Infocomm Media Development Authority (Singapore) | regulator guidance (PDF) | https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf | published 2026-05-20, updated 2026-06-05 | full for the sections cited (executive summary, human accountability, controls, case studies) |
| ACCA-FRC-2026 | AI related risks in audit (ACCA In Practice, summarizing FRC Generative and Agentic AI Guidance, March 2026, and CCAB draft statement, June 2026) | ACCA, authors J. Matheson and I. Ko (Kingsley Napley) | professional-body article describing regulator guidance | https://www.accaglobal.com/gb/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/july-august/AI-related-risks-in-audit.html | July-August 2026 issue (URL path) | full (secondary: I did not reach the FRC original) |
| MSFT-WTI-2025 | 2025 Work Trend Index: The Frontier Firm is born | Microsoft | vendor survey and report | https://blogs.microsoft.com/blog/2025/04/23/the-2025-annual-work-trend-index-the-frontier-firm-is-born/ | 2025-04-23 | search-only (page blocked) |
| KLARNA-REPORTS-2025 | Klarna rehires humans for customer support (Bloomberg interview, as reported by Entrepreneur, Silicon Canals and others) | trade press | news | https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 | May 2025 | search-only |
| KPMG-AUDIT-2025 | KPMG to use agentic AI tools to complete routine audit tasks | Bloomberg Law | news | https://news.bloomberglaw.com/payroll/kpmg-to-use-agentic-ai-tools-to-complete-routine-audit-tasks | April 2025 (per search summary) | search-only |
| MIT-NANDA-2025 | The GenAI Divide: State of AI in Business 2025 | MIT NANDA | report | not obtained (the NANDA PDF URL I tried returned the group's overview page) | 2025 | search-only (cited second-hand by ROLANDBERGER-2026) |

Source counts: 47 distinct sources listed. 43 were read (30 in full, 13 in part) and 4 are search-only. By type:
- vendor engineering, research, product documentation and vendor surveys: 20 (Anthropic 10, OpenAI 2, Microsoft/Google/AWS platform pages 5, LangChain 2, GitHub 1);
- consultancy and analyst publications: 11 (McKinsey 2, BCG 2, Gartner 1, Deloitte 1, MIT Technology Review sponsored content 1, Capgemini 2, Roland Berger 1, HBR/Gartner article 1);
- academic papers and independent research notes: 6 (WorkBank, MAST, TheAgentCompany, CRMArena-Pro, The Turing Trap, METR);
- practitioner essays and open-source guides: 3 (Cognition, HumanLayer, Willison);
- regulator and professional-body guidance: 2 (IMDA, ACCA);
- classic foundation: 1 (Hammer, 1990);
- vendor survey, trade press and report cited second-hand, all search-only: 4 (Microsoft Work Trend Index, Klarna reports, KPMG audit announcement, MIT NANDA).

Several "partial" sources were skimmed and are not cited for figures: AWS-PATTERNS, ANTHROPIC-TOOLS-2025, ANTHROPIC-CTX-2025, ARXIV-TURING-2022 and HBR-VERMA-2025.

---

## 10. Gaps

1. **No independent evidence on redesign versus bolt-on.** Every "redesign beats augmentation" claim traces to consultancies or analysts (McKinsey, BCG, Deloitte, Capgemini, Gartner, Roland Berger), mostly on unnamed clients without baselines. I found no controlled or independently audited comparison.
2. **No error, override or parallel-run data for human checkpoints in knowledge work.** Anthropic's telemetry covers coding agents. IMDA says to monitor override rates but publishes none. This is a real hole for the advisor's "design human checkpoints" guidance.
3. **No first-party outcome figures for professional-services deployments.** KPMG, EY and PwC agent programs appeared only in search summaries (KPMG, via Bloomberg Law) or in IMDA's description (PwC Singapore). Figures such as Big 4 agent counts and graduate-hiring cuts circulate in vendor blogs. I could not confirm them against a primary source and excluded them.
4. **Primary documents not reached.**
   - The UK FRC's March 2026 guidance, which I only saw summarized by ACCA.
   - The CCAB draft statement of June 2026.
   - The MIT NANDA report.
   - The Stanford "Canaries in the Coal Mine" paper, which BCG cites for a 16% decline in early-career employment in AI-exposed roles.
   - Microsoft's Work Trend Index page.
   - The Capgemini and BCG full PDFs.
5. **Blocked or partial pages.**
   - McKinsey, BCG and Gartner blocked direct `curl`.
   - They were read through a text-reader mirror, and footnotes and exhibits were not visible.
   - McKinsey's 78% and "no bottom-line impact" figures cite footnoted McKinsey research that I could not see.
   - The BCG agentic-adoption study co-author name was stripped.
   - HBR pages were paywalled.
6. **Dates.** Several platform documentation pages (Azure, AWS, Foundry) have no visible date. The LangChain survey page shows a 12 June 2026 label that may be an update date, while the text says the survey ran in Nov-Dec 2025. I used the survey dates.
7. **Search budget exhausted.** The web-search limit ran out before I could look for: Sequoia and a16z "services-as-software" writing on AI-native services firms, Bain's 2025 technology report on agentic AI, legal-sector agentic case write-ups (Harvey, CoCounsel), the Replit database-deletion incident, and the Air Canada chatbot ruling. These remain open. The "AI-native competitor" lens therefore rests on BCG, Deloitte-sponsored and Roland Berger material only.
8. **Unverified vendor banner.** AWS's AgentCore marketing page carries a headline saying 88% of agent pilots stall. It gives no source or definition in what I read, so I did not use it as evidence.
9. **Vendor-skew.** About a third of the technical sources come from Anthropic. That reflects how much concrete engineering detail it publishes, and it is partly offset by OpenAI, Microsoft, Google, AWS, LangChain, Cognition and academic sources. The Anthropic-sourced figures remain vendor-published, with provenance labels in section 6.
10. **Evolving terminology.** "Agentic", "agent" and "managed agent" are defined differently across sources: Anthropic distinguishes workflows from agents, Gartner and Deloitte call out "agent washing", and Anthropic's telemetry study defines an agent as a system with tools that take actions. Moves 4, 5 and 13 assume the advisor will define the term with the user.
11. **Academic coverage is thin on knowledge-work process redesign.** The academic papers here are benchmarks and failure taxonomies, mostly for software or CRM tasks. I found no peer-reviewed field study of agentic process redesign in professional services.
