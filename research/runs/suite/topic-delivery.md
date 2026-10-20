# Topic research: AI solution delivery

Skill fed: `ai-solution-delivery` (frame the problem, build or buy, design brief, evaluation plan, production readiness, launch and post-launch review).
Prepared 2026-10-20. Public sources only. Tools are described by runtime class (personal assistant, shared team skills, workflow automation, background agent, managed agent runtime); no vendor is recommended.

Conventions used below:

- Source refs are `PUBLISHER-SHORT-YYYY` and resolve in section 9. Locators are section names, question headings, action IDs or page numbers (pdftotext of PDFs gives unreliable page numbers, so section names are used for most).
- "Grade A rule" (2026-10-17): a figure counts as measured only when the named organization reports it as measured. Every figure in section 6 carries a flag: `measured` (named organization reports it as measured), `estimate` (rough estimate, recollection or self-reported interview figure), or `claim` (stated without method).
- "Advisor default" marks a threshold or rule that I propose as a starting point. It is not from a source. Sourced thresholds say so and name the source.
- Journey stages used in the question bank (my labels): **Explore** (idea, no build yet), **Pilot** (building or testing with a small group), **Scale** (rolling out), **Embed** (in routine operation).

---

## 1. Summary

- **Most delivery failure is framing and fit, not model quality.** RAND's 65 practitioner interviews put leadership misunderstanding of the problem, and data limits, as the two most-cited root causes. BCG's survey of 1,000 executives attributes about 70% of implementation challenges to people and process, 20% to technology and 10% to algorithms (RAND-2024; BCG-2024). Both are interview or survey data, not measured outcomes.
- **Start with the simplest runtime that could work and add autonomy only when evidence demands it.** Vendor engineering guides (Anthropic, OpenAI), Google's Rules of ML and RAND all say to try rules, a single call with retrieval, or a fixed workflow before an agent. A Berkeley-led study of 86 deployed agent systems found constrained autonomy is the norm: 68% run at most 10 steps before a human steps in (ANTHROPIC-2024; OPENAI-2025; GOOGLE-RULES; BERKELEY-2026).
- **Build versus buy is a differentiation and maintenance question more than a capability question.** Practitioner guides say do not build general features you can buy; an investor survey of 100 CIOs reports a shift toward buying apps, except in regulated or high-risk sectors; an MIT NANDA report says external partnerships reached deployment about twice as often as internal builds, though the report itself flags confounding and self-reported data (APPLIEDLLMS-2024; A16Z-2025; MITNANDA-2025).
- **Evaluation is the center of the delivery loop.** Converging practitioner advice: begin with real failures (20-50 tasks is a start), have a domain expert do error analysis on traces, use binary pass/fail checks per failure mode, calibrate any LLM judge against human labels, test consistency (pass^k) not just best-of-k, and keep regression suites near 100% (ANTHROPIC-2026; HUSAIN-2024; HUSAIN-2026; SIERRA-2024; SHANKAR-2024).
- **Vendor claims need testing on your own tasks.** An independent preregistered study found legal research tools marketed as reducing or eliminating hallucination hallucinated 17% to 33% of the time on its query set; a separate study of consultants found AI helped on tasks inside the capability frontier and hurt on one task outside it (STANFORD-2024; HBS-2023).
- **Regulated and professional-services settings change the evidence you keep, not the method.** Bank model-risk guidance asks for independent validation, an inventory, ongoing monitoring including override analysis, and documentation; the UK audit regulator expects proportionate documentation of how an AI tool was developed, tested and known to work; the ABA says the lawyer stays fully responsible and the right amount of verification depends on the tool and task, and can be informed by testing it on a smaller sample first (FRB-2011; BOE-2023; FRC-2025; ABA-2024).
- **Production readiness is operational, not just technical.** Named owners, logged inputs and outputs, daily or weekly trace sampling, managed releases that can be rolled back, cost monitoring, human-escalation triggers and feedback loops recur across NIST, UK government guidance, Google MLOps and practitioner guides (NIST-2024; UKGDS-2025; GOOGLE-2021; APPLIEDLLMS-2024).
- **Published quality evidence from live knowledge-work deployments is thin.** Override, escalation and error rates measured by a named organization on a production system are almost absent from public sources. The strongest measured public data point found is the UK Government Digital Service's expert-rated 80% answer accuracy for GOV.UK Chat, which it judged insufficient to launch on (UKGDS-2025).

---

## 2. Core concepts in plain language

**Workflow before technology.** Delivery starts from the work: who does what, with which inputs, to what quality bar, and where the pain is. UK government guidance says use cases must be led by user needs and pain points, not what the technology can do (UKGDS-2025, building AI solutions: identifying use cases). For knowledge work this means mapping the actual steps and checking the real error and rework pattern first. For AI it means the solution is a change to a step or a flow, not a chatbot bolted onto a role.

**Fit before build (the "simplest thing" ladder).** Anthropic and OpenAI both advise finding the simplest solution, and treat a deterministic or single-call solution as a legitimate answer. The ladder runs: rules or existing software, a single model call with retrieval and examples, a fixed multi-step workflow, an agent that picks its own steps, then multiple agents (ANTHROPIC-2024, When and when not to use agents; OPENAI-2025, When should you build an agent and Orchestration). I map the ladder onto runtime classes in section 8 (advisor mapping, not from a source). Higher rungs cost more latency, money and testing effort.

**Build, buy or configure.** The decision rests on differentiation (is this where the organization wins?), maintenance burden (models are the least durable component), switching cost (agent workflows tuned to one model are expensive to move), data boundaries and total cost. Practitioners advise buying general capabilities and building around proprietary workflows, data and evaluation (APPLIEDLLMS-2024, section 3.2; A16Z-2025, items 10 and 12).

**The eval set is the specification.** An eval is a test: input, grading logic, pass/fail. Anthropic notes that writing eval tasks tests whether product requirements are concrete enough to build, and that two experts should reach the same verdict on a good task (ANTHROPIC-2026, Steps 0 and 2). For knowledge work the "gold answer" often comes from a senior practitioner, and the first discovery is usually that seniors disagree.

**Error analysis beats generic metrics.** Hamel Husain and Shreya Shankar argue that you read real traces, write open-ended notes, build a taxonomy of failure modes, and only then build evaluators. Criteria drift (people define "good" only after seeing outputs) means you cannot write the rubric purely up front (HUSAIN-2026, error analysis answers; SHANKAR-2024, abstract and section 7.3.1).

**Reliability is consistency, not best case.** LLM agents vary run to run. pass@k asks if any of k tries works; pass^k asks if all k succeed. A 75% per-trial success rate gives about 42% over three trials (ANTHROPIC-2026, non-determinism section; SIERRA-2024, section on pass^k). For client-facing or audit-evidenced work, the second number is the relevant one.

**Human oversight is a designed control, not a hope.** Escalate on failure thresholds and on high-risk, irreversible actions; track overrides as a health signal (OPENAI-2025, Plan for human intervention; FRB-2011, Ongoing Monitoring; NIST-2024, MS-4.2-004). In professional services this is also where professional-responsibility rules attach (ABA-2024; FRC-2025).

**Production is a lifecycle.** After launch there are model and data changes, silent failures, drift, cost creep and shifting user behavior. Google's MLOps guide and Rules of ML, and Sculley et al.'s technical-debt paper, say that building is cheap relative to maintaining (GOOGLE-2021; GOOGLE-RULES, Rules 9 and 10; GOOGLE-2015, abstract).

**Documentation and auditability.** In regulated settings the output of delivery includes evidence: purpose, design choices, test results, change history, monitoring outputs and accountable owners. The FRC wants firms to record what an AI tool does, when it is appropriate, how it was developed and tested, and how the firm knows it works as intended, including for third-party tools (FRC-2025, news page, key features; search summary corroborates, see Gaps).

---

## 3. Expert moves

Format: **move** — when to use it — what it reveals — source ref.

### Framing and fit

1. **Restate the goal as the business metric the owner actually needs, and get the business owner to confirm it in writing** (RAND's example: the price that maximizes profit, not the price that sells the most) — at the start of framing, and again at design review — reveals proxy-metric errors and an owner who is not actually available to the team — RAND-2024 (Findings: Optimizing for the Wrong Business Problem).
2. **Ask "would a few if-then rules do this?" and have the team try the rule version first** — in framing, before any build estimate — reveals AI applied to a simple problem, and gives a baseline to beat — RAND-2024 (Using AI to Solve Simple Problems); GOOGLE-RULES (Rule 1, Rule 3); OPENAI-2025 (When should you build an agent: if the criteria are not met, a deterministic solution may suffice).
3. **Check the three agent-fit signals: nuanced judgment or exceptions, rules too tangled to maintain, heavy unstructured data** — when someone proposes an agent — reveals whether the workflow has resisted prior automation for a reason that an agent can address, or whether a workflow or single call is enough — OPENAI-2025 (When should you build an agent).
4. **Run the intern test: give the exact input and context to a competent graduate in the field and ask if they would succeed, and how long it would take** — in framing and in diagnosing poor results — reveals missing context (enrich it), tasks too hard for current models, or tasks that need decomposing — APPLIEDLLMS-2024 (section 1.4.3).
5. **Test by task type, not by role** — before committing to a role-wide rollout — reveals tasks inside versus outside the jagged capability frontier; in the BCG field experiment one task outside the frontier saw AI users 19% less likely to be correct — HBS-2023 (abstract).
6. **Ask what people already do with personal AI tools for this work, and what they like about it** — early discovery in a knowledge-work unit — reveals the demand signal, the flexibility users expect, and what a sanctioned solution must match; the NANDA report found workers at over 90% of surveyed companies used personal AI tools while only 40% of companies had purchased an LLM subscription (self-reported, see section 6) — MITNANDA-2025 (section 3.3).

### Build or buy

7. **Ask "is this where we differentiate, or a general problem many firms have?"** — at the build-or-buy gate — reveals whether internal build effort goes to commodity capability; practitioners cite text-to-SQL, a documentation chatbot and knowledge-base support bots as examples not worth building in a product company — APPLIEDLLMS-2024 (section 3.2.4).
8. **Price maintenance, not just build: ask who re-evaluates models each quarter and who retunes prompts and guardrails when the model changes** — at build-or-buy and again at production readiness — reveals the hidden recurring cost and switching cost; CIOs interviewed said agent workflows tuned for one model are hard to move — A16Z-2025 (item 10); APPLIEDLLMS-2024 (2.2.2, 2.2.3, 3.2.1); GOOGLE-2015 (abstract).
9. **Put a lock-in and exit strategy in the requirements, and give suppliers dummy data and a problem statement, not a solution spec** — at procurement — reveals whether suppliers can demonstrate on your data and what leaving costs; UK government lists "consider strategies to avoid vendor lock-in", "start with your problem statement" and "budget to consider hidden costs" — UKGDS-2025 (Specifying your requirements).
10. **Treat vendor accuracy claims as hypotheses; run your own test set on the vendor tool** — at selection — reveals the gap between marketing and your tasks; in the legal-research study each tested tool hallucinated 17% to 33% on the study's queries despite "hallucination-free" or "avoid" language in vendor statements — STANFORD-2024 (abstract, sections 1 and 5); A16Z-2025 (item 11: external benchmarks are one input, buyers still trial).
11. **Baseline against the human or legacy process on the same tasks before claiming improvement** — at pilot design — reveals whether the AI beats the current standard; Vals' legal study used a lawyer control group and found AI tools beat it on four tasks and not on others, whereas in the Berkeley survey only 39% of respondents compared their agent to a non-agentic baseline — VALS-2025 (summary); BERKELEY-2026 (section 6.1).

### Design

12. **Climb the autonomy ladder one rung at a time and write down what evidence moves you up** — in the design brief — reveals whether the extra complexity buys measured improvement — ANTHROPIC-2024 (Combining and customizing); OPENAI-2025 (Orchestration: incremental approach).
13. **Draw the human checkpoints on the flow: failure thresholds and high-risk actions** — in solution design — reveals where a wrong output becomes an irreversible action (cancel, pay, send, file); OpenAI names failure thresholds and high-risk actions as the two triggers; Huyen's example is that write queries should not run without human approval — OPENAI-2025 (Plan for human intervention); HUYEN-2024 (Step 2, input guardrails).
14. **Design the UX so the human reviews a suggestion and edits it, and capture the edit as feedback** — in design — reveals a built-in feedback loop and a clear locus of accountability — APPLIEDLLMS-2024 (2.3.2, 3.2.5); YAN-2023 (defensive UX and user feedback patterns).
15. **Layer guardrails and map them to the OWASP LLM risks relevant to the runtime** (for example prompt injection, excessive agency, improper output handling) — at security review — reveals which risks are real for this integration and permission set — OWASP-2025 (LLM01, LLM05, LLM06); OPENAI-2025 (Guardrails); HUYEN-2024 (Step 2).
16. **Start with read-only tool permissions; require approval for write or delete** — when integrating with existing systems — reveals blast radius; the LangChain survey found few respondents let agents read, write and delete freely, with most using read-only or human approval for writes — LANGCHAIN-2024 (tool permissions section; vendor survey).

### Evaluation

17. **Seed the eval set from real failures and from what the team already checks by hand: 20-50 tasks is a good start** — as soon as there is a prototype or an existing process with errors — reveals what "good" means in the team's own terms, and surfaces requirement ambiguity — ANTHROPIC-2026 (Steps 0 and 1).
18. **Two-expert test: could two domain experts independently reach the same pass/fail verdict on this task? Make someone pass it themselves** — when drafting gold answers — reveals ambiguous tasks and rubrics that will add noise; in professional services this is where partners and managers disagree on "correct" — ANTHROPIC-2026 (Step 2).
19. **One accountable domain expert reviews 20-50 outputs for about 30 minutes, then work up to about 100 diverse traces, noting the first failure in each, until new traces stop revealing new failure modes** — at pilot start and after every significant change — reveals the failure taxonomy that should drive which evaluators you build — HUSAIN-2026 (error analysis and "how many examples" answers; practitioner guidance, not a measured result).
20. **Decide the evaluator per failure mode: code check for objective rules, LLM judge for judgment calls, and label roughly 100-200 examples per judged failure mode with enough passes and fails** — when building automated evals — reveals which failures merit judge investment — HUSAIN-2026 (examples-needed answer).
21. **Validate the judge against human labels and track precision and recall, not raw agreement, when classes are imbalanced; give the judge an "Unknown" option; judge one dimension at a time** — before trusting LLM-graded scores — reveals judge bias and drift; the original MT-Bench study reported over 80% agreement between a strong judge and human preferences but also position, verbosity and self-enhancement biases, and Thoughtworks moved LLM-as-a-judge to "Assess" in Nov 2025 citing reliability concerns — HUSAIN-2024 (Level 2); ANTHROPIC-2026 (Step 5); LMSYS-2023 (abstract); THOUGHTWORKS-2025.
22. **Use binary pass/fail per check and report a "pass-all" rate with drill-down** — when reporting eval results to stakeholders — reveals which checks drive failure and avoids arguments about the difference between a 3 and a 4 — HUSAIN-2026 (binary evaluations; combining evals); APPLIEDLLMS-2024 (1.4.5).
23. **Run multiple trials and report pass^k for flows where users expect it to work every time** — for client-facing or evidence-producing flows — reveals consistency problems hidden by a single-run score — ANTHROPIC-2026 (non-determinism); SIERRA-2024 (pass^k; best tested agent under 50% of tasks and pass^8 under 25% on its retail domain with 2024 models).
24. **Treat a 0% pass rate across many trials as a likely broken task or grader, and read transcripts before believing any score** — when scores look too low, too high or flat — reveals grading bugs; Anthropic reports one benchmark score moving from 42% to 95% after grader and task-spec fixes — ANTHROPIC-2026 (Steps 2, 5, 6).
25. **Build balanced sets that include cases where the behavior should not trigger** — for routing, search-or-answer and escalation behaviors — reveals over-triggering that one-sided tests reward — ANTHROPIC-2026 (Step 3).
26. **Test your verification effort empirically: check a tool on a small, manually reviewed subset, then set how much of the rest to review** — in professional-services deployments where a lawyer, auditor or partner remains responsible — reveals a defensible, documented review level; ABA Opinion 512 gives the example of testing a contract-summary tool on a smaller set before relying on it for many — ABA-2024 (Competence discussion, Rule 1.1).
27. **Red-team before launch with a scorecard (attack categories and success rate) and re-run on a schedule; use reviewers who did not build the system** — in the evaluation plan for any external-facing or tool-using solution — reveals vulnerabilities that functional tests do not; NIST asks that structured human feedback exercises use people not directly involved in development — NIST-2024 (MS-1.3-002, MS-1.3-003, MS-4.2-001); MSFT-REDTEAM (overview).

### Production and post-launch

28. **Log every input and output, then sample: read traces daily at pilot, then 10-20 per week plus 100+ fresh traces per review cycle** — from first users onward — reveals new failure modes and distribution shift; the cadence is practitioner guidance and Hamel suggests review cycles of 2-4 weeks — APPLIEDLLMS-2024 (2.1.2); HUSAIN-2026 (how often to re-run error analysis); UKGDS-2024 (Testing and operational data).
29. **Track overrides, escalations and rework as monitoring metrics, and investigate if the rate is high** — in monitoring design — reveals where users do not trust or cannot use the output; bank guidance says high override rates or overrides that consistently improve results signal a need to revise the model — FRB-2011 (Ongoing Monitoring); NIST-2024 (MS-4.2-004).
30. **Define the managed-release and rollback path before launch: a quantitative validation step in change control, and a way to revert** — in production readiness — reveals whether a model, prompt or retrieval change can be shipped safely; UK guidance requires a quantitative testing and validation process in change control and that releases can be withdrawn — UKGDS-2025 (Validation of AI; Operational monitoring); APPLIEDLLMS-2024 (2.2.3, version and pin models).
31. **Watch for silent failures: monitor input coverage, data freshness and retrieval health, not only outputs** — in operation — reveals gradual decay such as stale tables or dropped feature coverage that does not trigger errors — GOOGLE-RULES (Rule 10); GOOGLE-2021 (continuous monitoring).
32. **Track cost per task and usage from the eval bank and in production** — at readiness and monthly after — reveals cost creep and whether a smaller model passes the same evals; OpenAI advises setting a baseline with the best model, then swapping in smaller ones — ANTHROPIC-2026 (why build evaluations: latency, tokens, cost per task); OPENAI-2025 (Selecting your models); UKGDS-2024 (FinOps data).
33. **Retire or demote evals that always pass, and re-baseline when the product changes** — in post-launch iteration — reveals stale gold sets and saturated capability evals; Anthropic suggests graduating high-pass capability evals into a regression suite — ANTHROPIC-2026 (capability versus regression; Step 7); HUSAIN-2026 (stale gold dataset answer).

---

## 4. Question bank

Tags: scope level `[team]`, `[unit]`, `[org]`; journey stage `Explore`, `Pilot`, `Scale`, `Embed`.

### Frame the problem

- Describe the last real instance of this work, start to finish. What came in, who touched it, what went out, how long did it take? [team] Explore
- Give me last month's actual volume, not a typical week, and the share that needed rework or escalation. [team] Explore
- Which step do people dislike or get wrong most often, and how do you know? [team] Explore
- What metric would the owner of this process use to say it improved? Is that the metric the pilot will track? [team/unit] Explore (RAND-2024)
- What would a rule-based or manual-checklist version of this step look like, and why is it not enough? [team] Explore (GOOGLE-RULES Rule 1; OPENAI-2025)
- Does the work need judgment on exceptions, unstructured documents, or a rule set nobody can maintain? [team] Explore (OPENAI-2025)
- What do people already do with personal AI tools on this task? [team/unit] Explore (MITNANDA-2025 section 3.3)
- Who is the single accountable owner, and are they available weekly to review outputs? [team/unit] Explore (RAND-2024: leaders not available to check intent)
- What are the cases where an error is costly or irreversible (client advice, filing, payment)? [team/unit] Explore (UKGDS-2025: use cases to avoid)
- Across the units in scope, which share the same workflow and which are different enough to need separate solutions? [org] Explore
- Which candidate solutions are general problems many firms face, and which rely on our proprietary data or method? [org] Explore (APPLIEDLLMS-2024)

### Build, buy or configure

- Is this a place we differentiate, or a general capability? [unit/org] Explore/Pilot (APPLIEDLLMS-2024)
- Have we tried a sanctioned off-the-shelf tool on a sample of real tasks, and what did it get wrong? [team/unit] Pilot (A16Z-2025; STANFORD-2024)
- Who will own the system after the builder moves on: prompts, retrieval, tool integrations, evals, vendor relationship? [unit/org] Pilot
- What does it cost to switch models or vendors in a year, and what would we have to retest? [unit/org] Pilot (A16Z-2025 item 10)
- What data leaves our boundary, under which contract terms, and can the vendor use it for secondary purposes? [unit/org] Pilot (NIST-2024 GV-6.2-007; UKGDS-2025)
- What is the total run cost at expected volume, including review time, support and re-evaluation? [unit/org] Pilot/Scale (UKGDS-2024 FinOps; GOOGLE-2015)
- How does the vendor handle incidents, model changes and notification, and is it in the SLA? [org] Scale (NIST-2024 GV-6.2-007)
- Would the vendor run our evals and show results by task type? [unit] Pilot

### Solution design

- What is the simplest rung on the ladder (rule, single call with retrieval, fixed workflow, agent) that could meet the quality bar? [team/unit] Pilot (ANTHROPIC-2024)
- Which systems does it read from and write to, with what permissions, and what is the worst thing it could do with those permissions? [team/unit] Pilot (OWASP-2025 LLM06)
- Where does the human review or approve, and what triggers an escalation? [team/unit] Pilot (OPENAI-2025)
- What is the source of truth for retrieval, how is it kept current, and who owns it? [unit] Pilot (UKGDS-2025 GOV.UK Chat: RAG chosen because content changes)
- What client or personal data is in scope, and what is the access model? [unit/org] Pilot (UKGDS-2025 data protection; HUYEN-2024 input guardrails)
- What happens when the system does not know? Does it say so? [team] Pilot (APPLIEDLLMS-2024 1.4.7)
- Which runtime class fits: personal assistant, shared team skills, workflow automation, background agent or managed agent runtime, and why? [unit] Pilot (advisor mapping)

### Evaluation plan

- What would two senior practitioners independently agree is a correct output for these 20 real cases? Where do they disagree? [team] Pilot (ANTHROPIC-2026 Step 2)
- What are the real failures from the last few months that should become test cases? [team] Pilot (ANTHROPIC-2026 Step 1)
- Who is the single domain expert who decides what "good" means? [team/unit] Pilot (HUSAIN-2026)
- What failure modes have we seen in the first 30-100 traces? [team] Pilot (HUSAIN-2026)
- What pass rate on which test set would we accept, and what failure types are unacceptable at any rate? [unit] Pilot (HUSAIN-2024: pass rate is a product decision)
- Does it need to work every time (pass^k) or is one good attempt among several enough? [team/unit] Pilot (ANTHROPIC-2026)
- How will we check an LLM judge against human labels, and how often will we recheck? [team] Pilot/Scale (HUSAIN-2024; SHANKAR-2024)
- Who outside the build team will test it adversarially before launch? [unit/org] Pilot (NIST-2024 MS-1.3-003)
- What does the regulator, client or professional body expect to see as evidence of testing? [unit/org] Pilot (FRC-2025; BOE-2023; ABA-2024)
- What is the human or legacy baseline on the same tasks? [team/unit] Pilot (VALS-2025; BERKELEY-2026)

### Production readiness

- Who is on the hook when it fails at 6pm on a Friday? Is there a runbook? [team/unit] Scale
- How do we pause or roll back, and who can? [team/unit] Scale (UKGDS-2025)
- What is logged, for how long, who can read it, and how does that meet client confidentiality? [unit/org] Scale (UKGDS-2024; ABA-2024)
- What are the monitoring metrics: override rate, escalation rate, error categories, cost per task, usage by team? [team/unit] Scale (FRB-2011; NIST-2024)
- What is the change-control rule when the model, prompt, retrieval index or tools change? [unit/org] Scale (UKGDS-2025)
- What is the adoption plan: who is trained, what do they do differently on day one, and what do they do when the tool is wrong? [team/unit] Scale (ABA-2024 training; BCG-2024)
- Is the system recorded in the model or AI inventory, with owner and risk tier? [org] Scale (FRB-2011; BOE-2023)

### Launch and post-launch review

- What did we say success would look like at 30, 90 and 180 days? Did it happen? [team/unit] Embed
- What is the override and rework rate this month versus pilot, and what do the overrides tell us? [team/unit] Embed (FRB-2011)
- Which eval cases now always pass and which new failures need cases? [team] Embed (ANTHROPIC-2026; HUSAIN-2026)
- What changed in the inputs or users since we built the test set? [team/unit] Embed (APPLIEDLLMS-2024 2.1.1)
- What did the incident or near-miss review find, and did we update evals, guardrails or training? [unit/org] Embed (NIST-2024 MG-4.2-002)
- Should this solution move up or down the autonomy ladder? What evidence supports that? [unit] Embed (ANTHROPIC-2024)
- Which solution patterns from this unit can be reused by others, and which were local? [org] Embed

---

## 5. Common traps

| Trap | Why it happens | Evidence | How to avoid |
|---|---|---|---|
| **Optimizing the wrong problem or metric** | Technical staff translate a vague business goal; owners are not available to check intent | RAND interviews: leadership-driven failures were the most-cited cause, with 84% of interviewees citing one or more as the primary reason projects fail (RAND-2024, Leadership-Driven Failures) | Move 1; named business owner reviewing outputs weekly |
| **Using AI where rules would do** | AI is treated as a buzzword; senior leaders demand it | RAND (Using AI to Solve Simple Problems); GOOGLE-RULES Rule 1 | Build and measure a rule or single-call baseline first |
| **Automating waste** (speeding up a step that should not exist or that hides rework) | The workflow was not mapped or diagnosed before the build | No source found that measured this directly. Adjacent evidence: NANDA found interview-reported failures from brittle workflows and misalignment with day-to-day operations; BCG says leaders prioritize workflow optimization and change management (MITNANDA-2025 executive summary; BCG-2024) | Run the workflow discovery questions first; ask for last month's actual volume and rework share; baseline the current process |
| **Chasing technology over the user problem** | Engineers want the newest tools; resume incentives | RAND: 16 of 50 industry interviewees described bottom-up, technology-driven failures (RAND-2024, Bottom-Up-Driven Failures) | Tie every design choice to the problem statement and eval results |
| **Demo-to-production gap** | A demo works on a few inputs; production needs reliability, edge cases and maintenance | Yan (2023) quotes this as a general pattern; Sculley et al.: building is fast and cheap but maintaining ML systems is hard and expensive (YAN-2023, intro; GOOGLE-2015, section 1) | Eval set from real failures; budget for iteration (the practitioner experience is 60-80% of development time on error analysis and evaluation, HUSAIN-2026) |
| **Vibe checks only** | Early progress through prompting hides plateaus; fixing one failure creates another | Rechat's assistant plateaued with whack-a-mole failures before an eval system was built (HUSAIN-2024, case study); Anthropic: teams "flying blind" without evals (ANTHROPIC-2026, Why build evaluations) | Start evals before scale; error analysis on traces |
| **Generic metrics and Likert scales** | Platforms nudge toward off-the-shelf scores; 1-5 scales feel richer | Practitioner guidance favors binary checks per failure mode and task-specific evals (HUSAIN-2026; APPLIEDLLMS-2024 1.4.5; YAN-2023, How to apply evals) | Use failure taxonomy; binary checks; pass-all rate |
| **Trusting an uncalibrated LLM judge** | Cheap, scalable, plausible | MT-Bench: over 80% agreement with human preferences but position, verbosity and self-enhancement biases; EvalGen study: judges inherit LLM problems and criteria drift; Thoughtworks Radar moved the technique to Assess (LMSYS-2023; SHANKAR-2024; THOUGHTWORKS-2025) | Calibrate to human labels; track precision and recall; human review of samples |
| **Saturated or broken evals** | 100% pass gives no signal; grader bugs depress scores | Anthropic reports a score of 42% moving to 95% after grader and task fixes; Hamel warns that passing 100% suggests the evals are not challenging enough (ANTHROPIC-2026; HUSAIN-2026) | Read transcripts; separate capability and regression suites |
| **Believing vendor accuracy claims** | Marketing language ("hallucination-free"), closed systems | Independent preregistered test: 17% to 33% hallucination for tested legal research tools (STANFORD-2024) | Test on your tasks (move 10); require evidence by task type |
| **Verifying the conclusions but not the citations** | Output looks authoritative; review effort is spent elsewhere | Australian DEWR report: fabricated references and a made-up court-case reference were reported by press; a partial refund followed (GUARDIAN-2025). Legal AI hallucination documented (STANFORD-2024); ABA notes nonexistent opinions cited in court filings (ABA-2024, candor to tribunal) | Automated reference-existence checks; sample verification; named reviewer |
| **Too much autonomy too early** | Agents are exciting; errors compound across steps | Anthropic: autonomy costs more and errors compound; production survey: 68% of deployed agents run at most 10 steps before human intervention (ANTHROPIC-2024; BERKELEY-2026) | Climb the ladder; human checkpoints on high-risk actions |
| **Build-everything and fine-tune-too-early** | FOMO, "not just a wrapper" pressure | Practitioners: finetuning is driven more by fear of missing out than strategy and many regret it; models are the least durable component (APPLIEDLLMS-2024, 3.1.2, 3.2.1). a16z survey: fine-tuning viewed as less necessary as models improve (A16Z-2025 item 6; investor view) | Prompt, retrieve, eval first; fine-tune only with proof |
| **Model and prompt lock-in** | Prompts, guardrails and tests are tuned to one model | CIO quote and analysis in a16z; "migrating prompts across models is a pain" in Applied LLMs; Berkeley: newer models do not guarantee better agent performance and can break workflows (A16Z-2025 item 10; APPLIEDLLMS-2024 2.2.2; BERKELEY-2026 section 5.1) | Eval suite as the portability asset; pin and version models |
| **No owner, support or runbook after launch** | Project ends at go-live; accountability unclear | Evidence on this is mostly guidance not measurement: NIST asks for defined ownership of incident response and regular rehearsal; UK guidance asks for named senior responsible owners (NIST-2024 GV-6.2-003; UKGDS-2025) | Named owner, runbook, on-call review rotation |
| **Silent decay** | ML and LLM systems degrade gracefully, so nobody notices | Google: a stale table caused months of gradual decay; a refresh gave a 2% install-rate gain at one product (GOOGLE-RULES Rule 10) | Monitor inputs, coverage, freshness; trace review cadence |
| **Ignoring people and process** | Algorithms get the attention | BCG survey: around 70% of challenges people and process, 20% technology, 10% algorithms; leaders put resources roughly 10/20/70 (BCG-2024) | Plan adoption, training and workflow change as part of delivery |

---

## 6. Evidence

Provenance codes: `independent` (academic or regulator, not selling the thing), `self-reported` (survey or interview of participants), `vendor-published` (published by a company with a product interest), `named-org measured` (the named organization reports a measurement). Grade A flag as defined at the top.

| # | Data point | What it measures (source's words, paraphrased) | Provenance | Grade A flag | Source and locator |
|---|---|---|---|---|---|
| 1 | 95% of organizations getting zero return; only 5% of integrated pilots extracting millions in value | NANDA says it reviewed over 300 public AI initiatives, interviewed 52 organizations and surveyed 153 senior leaders; the report states its figures are directional, based on individual interviews rather than official company reporting, and success definitions vary | self-reported, MIT NANDA (preliminary findings) | estimate | MITNANDA-2025, Executive Summary and section 3.2 (research limitations note) |
| 2 | For task-specific or embedded GenAI tools: about 60% investigated, 20% reached pilot, 5% reached production ("successfully implemented" defined as users or executives remarking on a marked, sustained productivity or P&L impact) | Share of organizations at each stage | self-reported interviews | estimate | MITNANDA-2025, section 3.2 |
| 3 | External partnerships reached deployment about 67% of the time versus about 33% for internal builds | Share of builds that reached deployment in the authors' sample; they say this is self-reported, may not account for confounders, and may reflect organizational capability rather than approach | self-reported | estimate | MITNANDA-2025, p. 20 (partnerships vs internal builds; limitation note on the same page) |
| 4 | More than 80% of AI projects fail, twice the rate of non-AI IT projects | RAND cites this as "by some estimates", from a secondary source (Kahn); it is not RAND's measurement. RAND's own work is 65 interviews, and its scope covers ML, not projects that simply used pretrained LLMs via prompting | secondary estimate cited by RAND | estimate | RAND-2024, Summary and footnote c |
| 5 | Leadership misunderstanding as the primary reason: 84% of interviewees cited one or more leadership-driven root causes | Share of interviewees in the industry findings section (50 industry and 15 academic interviews in total; the report does not restate the denominator at this sentence) who cited a leadership-driven cause as primary reason projects fail; "failure" defined as perceived failure by the organization | independent (RAND); interviews | measured as an interview tally | RAND-2024, Leadership-Driven Failures |
| 6 | Data quality issues raised by 30 of 50 industry interviewees | Count of interviewees discussing persistent data-quality problems | independent; interviews | measured as an interview tally | RAND-2024, Data-Driven Failures |
| 7 | 26% of companies have capabilities to move beyond proofs of concept and generate tangible value (4% cutting-edge, 22% leaders); 74% have yet to show tangible value | Based on a BCG survey of 1,000 CxOs and senior executives in 59 countries, who rated their companies' maturity on 30 capabilities | self-reported survey run by a consultancy | claim (survey result) | BCG-2024, press release |
| 8 | Around 70% of AI implementation challenges are people and process, 20% technology, 10% algorithms | Survey finding as stated by BCG | self-reported survey | claim | BCG-2024, "70-20-10" section |
| 9 | 68% of surveyed deployed agent systems run at most 10 steps before human intervention (N=60); 74% rely primarily on human-in-the-loop evaluation (N=31, multi-select); 70% of 20 interviewed case studies use off-the-shelf models without weight tuning | Berkeley-led study: 20 interviews and a survey of 306 practitioners, filtered to 86 deployed (production or pilot) systems; denominators vary by question | independent academic (UC Berkeley with IBM Research, Intesa Sanpaolo and others) | measured by the study | BERKELEY-2026, abstract; Figures 7 and 8; section 5.2 |
| 10 | Only 39% compare their agent to a non-agentic baseline; 26% report no meaningful baseline exists; reliability is the top development challenge, with 38% ranking core technical performance first | Survey of deployed agent practitioners | independent academic | measured by the study | BERKELEY-2026, section 6.1 and section 7 |
| 11 | About 51% of respondents say they have agents in production; offline evaluation cited by 39.8% versus online evaluation by 32.5%; performance quality is the top limitation | LangChain survey of over 1,300 professionals (2024 survey; page carries a 2026 date stamp, see Gaps) | vendor-published, self-reported | claim | LANGCHAIN-2024, insights sections |
| 12 | Legal research tools Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI each hallucinated between 17% and 33% of the time; Lexis+ AI answered 65% of queries accurately, Westlaw AI-AR 42%; Ask Practical Law AI gave incomplete answers (refusals or ungrounded) on more than 60% | Preregistered manual evaluation of over 200 legal queries; hallucination defined by the paper's typology; 2024 product versions | independent academic (Stanford, Yale) | measured by the study | STANFORD-2024, abstract and section 1 |
| 13 | AI tools beat a lawyer control group on four of seven legal tasks (document analysis, retrieval, data extraction), matched it on one, and none beat it on the EDGAR research task; Document Q&A: lawyer baseline 70.1% (plus or minus 5.2) versus 94.8% for the best tool | Vals Legal AI Report, 2025: four vendors, each choosing which tasks to opt into; scores against predefined criteria per task | vendor-participating third-party benchmark | measured by Vals; caveat on opt-in | VALS-2025, summary and results table |
| 14 | 758 BCG consultants: on 18 tasks inside the frontier, AI users completed 12.2% more tasks, 25.1% faster, with higher quality; on one task outside the frontier, AI users were 19% less likely to produce a correct solution | Preregistered field experiment with GPT-4; abstract figures | independent academic (HBS, with BCG collaboration) | measured by the study | HBS-2023, abstract |
| 15 | Best tested agent succeeded on under 50% of tasks; pass^8 under 25% on the retail domain | tau-bench: simulated user and agent with tools and policy; database end-state compared with goal; 2024 models | benchmark paper from an agent vendor's research team | measured by the benchmark | SIERRA-2024, abstract; Figure 4 |
| 16 | GOV.UK Chat first experiment: answer accuracy 80%, judged by the team to need improvement before a public pilot; nearly 70% of surveyed testers found responses useful, about 65% satisfied; tested by hundreds of users in a controlled environment | GDS measured accuracy through expert (content designer) assessment; satisfaction through post-use surveys | named-org measured (UK Government Digital Service) | measured | UKGDS-2025, GOV.UK Chat case study |
| 17 | Enterprise LLM spend: innovation budgets fell from about a quarter of LLM spending to 7%; 37% of respondents use five or more models versus 29% a year earlier; over 90% of respondents testing customer-support apps were testing third-party apps | a16z survey of 100 CIOs across 15 industries (as of 8 May 2025) plus interviews with over two dozen buyers | investor-published, self-reported | claim | A16Z-2025, items 2, 3 and 12 |
| 18 | Opus 4.5 CORE-Bench score moved from 42% to 95% after correcting grading and task issues | Anthropic researcher's audit of the benchmark | vendor-published, self-reported | measured by the named org (anecdote on a benchmark, not a delivery outcome) | ANTHROPIC-2026, Step 5 |
| 19 | 75% per-trial success gives about 42% pass^3 | Arithmetic example given by Anthropic (0.75 cubed) | vendor-published; illustrative | not a measurement | ANTHROPIC-2026, non-determinism |
| 20 | Gartner prediction that over 40% of agentic AI projects will be canceled by end of 2027 (June 2025); wording of "cancelled" varies in coverage | Analyst forecast | analyst forecast, search-only | claim; not read in primary (see Gaps) | GARTNER-2025 (search-only; secondary coverage) |

Quality evidence absent from public sources I could reach: independently measured override rates, escalation rates, and parallel-run results from production knowledge-work deployments. The closest items are guidance that says to track overrides (FRB-2011; NIST-2024) and the GOV.UK Chat expert-rated accuracy (UKGDS-2025).

---

## 7. Worked examples

### A. GOV.UK Chat (public-sector information retrieval; real, published by the UK Government Digital Service)

Source: UKGDS-2025, case studies "GOV.UK Chat: experimenting with generative AI" and "doing user research for AI products".

- **Problem framing.** Help users navigate more than 700,000 GOV.UK pages; the first focus area was "business" because it spans many departments' content.
- **Design choice.** Retrieval-augmented generation rather than fine-tuning, because content is edited and published regularly. First retrieval returned whole pages, which sometimes exceeded token limits; the team then explored chunking, embedding models, re-ranking and few-shot examples.
- **Evaluation.** Phased experiments of a couple of weeks each. Content designers assessed answers for question intent, retrieved pages, factual accuracy and completeness. In a separate study, subject-matter experts rated LLM and human-written answers without knowing which was which, on Likert scales; agreement between experts was high and the LLM answers were rated on par with the human model answers.
- **Result.** Answer accuracy of 80%; the team concluded accuracy gains were needed before a public pilot. Nearly 70% of testers found responses useful and about 65% were satisfied. Hallucinated responses occurred.
- **Controls.** Data protection impact assessment, removal of personal data from pages the model could read, and red teaming with cyber security experts.
- **Next step named.** Quality assurance does not scale if manual, so the team proposed a knowledge base of quality-assessed questions for semi-automated QA.
- **What it teaches.** Set the launch threshold from expert-rated accuracy, not from user satisfaction; plan the QA mechanism before scaling; keep the knowledge-base owner in the loop.

### B. Fabricated references in a consultancy report for a government department (professional-services failure; real, press-reported)

Source: GUARDIAN-2025 (6 Oct 2025). Facts as reported: Deloitte was commissioned by the Australian Department of Employment and Workplace Relations to review a compliance framework and its IT system. The report, first published 4 July, was re-uploaded after the Australian Financial Review reported errors including nonexistent references and citations. The department confirmed Deloitte would repay the final instalment under a contract of about A$440,000. The revised report added an appendix stating that part of the work used an Azure OpenAI GPT-4o based tool chain licensed by the department. Deloitte did not state AI as the reason for the errors and said the substantive findings were unaffected.

- **Advisor's reading (inference, not from the source).** The delivery controls that would address this failure are: a named reviewer accountable for every citation, an automated check that each cited source exists and says what is claimed, disclosure of AI use in the engagement terms, and a sampling-based verification procedure (compare ABA-2024 on independent verification and FRC-2025 on documentation of how tools are tested and known to work).
- **Limits.** The Guardian article is a secondary report; Deloitte's own account of the cause is not in the source.

### C. Rechat's "Lucy" assistant: building the eval loop (SaaS practitioner case, written by the consultant who worked on it)

Source: HUSAIN-2024 (case study, Level 1 and Level 2 sections). Real-estate software, not professional services; use it for the pattern.

- **Situation.** A conversational assistant covering contacts, listings, appointments and creative assets. Prompt engineering made fast early progress, then plateaued: fixing one failure caused others, there was no view of effectiveness beyond vibe checks, and prompts grew long.
- **What they did.** Scoped unit tests by feature and scenario (for example listing search returning exactly one, several or zero results); synthetic test inputs generated by an LLM and refined with real usage; generic assertions (for example no internal IDs in output); trace logging; a custom review tool that put everything a reviewer needed on one screen; binary good/bad labels; periodic model-versus-human alignment of an LLM critic; tracking test results over time in an analytics dashboard.
- **Outcome as reported.** The post describes the system and the flywheel; I found no headline outcome percentages in it.
- **Limits.** Single case, self-described, no independent measurement. The LLM-critic alignment example used a roughly balanced dataset and the post warns raw agreement misleads when classes are imbalanced.

### D. Illustrative composite: contract-review assistant in a legal or professional-services practice (NOT a real case; assembled from the cited sources to show how the steps fit)

1. **Frame.** Practice lead and two senior reviewers describe last month's actual contract batches: volumes, review time, rework, what errors escaped. Success metric: reviewer time per contract at a fixed error-catch rate, not "AI usage".
2. **Build or buy.** Test one sanctioned off-the-shelf tool on 30 real contracts with partner-approved gold answers (VALS-2025 baseline idea; ANTHROPIC-2026 20-50 tasks). Decide to buy and configure unless the firm's playbook of clause positions is the differentiator, in which case build the playbook and checks around a bought capability (APPLIEDLLMS-2024).
3. **Design.** A shared team skill with retrieval over the firm's playbook; read-only access to the document store; the assistant proposes, a reviewer approves; nothing is sent to the client automatically (OPENAI-2025 human-intervention triggers).
4. **Evaluate.** Domain expert annotates traces; binary checks for clause identified, risk flagged, citation to the playbook present; two-expert agreement check on gold answers; run three trials per contract and report pass-all and pass^3 (HUSAIN-2026; ANTHROPIC-2026). Verification level set by checking the tool on a manually reviewed subset first (ABA-2024).
5. **Ready.** Named owner, runbook, logged inputs and outputs under the engagement's confidentiality terms, weekly trace sampling, rollback to manual process, documentation of purpose, testing and review levels (FRC-2025 style).
6. **Post-launch.** Track reviewer overrides and rework; add every escaped error to the eval set; review monthly (FRB-2011; HUSAIN-2026).

---

## 8. Mapping to steps

### 8.1 Frame the problem

**Checklist**
- Work described from a real recent instance with actual volumes and rework (not a typical week).
- Business owner named and available; success metric stated in the owner's terms.
- Rule-based or manual baseline considered and, ideally, measured.
- Fit test: judgment and exceptions, unmaintainable rules, unstructured data (OPENAI-2025).
- Stakes screen: irreversible or high-impact decisions flagged (UKGDS-2025: use cases to avoid).
- Existing informal AI use noted (MITNANDA-2025 section 3.3).

**Template (problem frame): fields**
Problem statement; process owner; unit and scope level; current process steps with volumes and time; error and rework pattern (last month); proposed change type (improve the step, automate the flow, delegate the outcome, reinvent the work); success metric and baseline; stakes and irreversibility; data sources and sensitivity; constraints (regulatory, client, contractual); simplest-rung hypothesis.

**Decision rules**
- If a rule, template or existing tool meets the quality bar on a sample, do not build a model-based solution (GOOGLE-RULES Rule 1; OPENAI-2025).
- If the work involves fully automated significant decisions or high-risk outcomes, do not proceed at autonomy levels without human decision-making (UKGDS-2025).

### 8.2 Build or buy

**Checklist**
- Differentiation: proprietary workflow, data or method versus general capability (APPLIEDLLMS-2024).
- Maintenance owner and cadence for model changes, prompts, guardrails and evals (A16Z-2025; APPLIEDLLMS-2024).
- Lock-in and exit: switching cost, data portability, contract terms on incidents and model changes (UKGDS-2025; NIST-2024 GV-6.2-007).
- Total cost: licenses or inference, integration, review time, evaluation, support (UKGDS-2024; GOOGLE-2015).
- Data boundaries and secondary-use terms.
- Evidence on your tasks, not vendor benchmarks (STANFORD-2024; A16Z-2025 item 11).

**Template (build-buy-configure options table): fields**
Option (buy as-is, configure a bought tool, build on a bought model, build custom); fit to workflow; evaluation result on the sample; one-year cost including support and re-evaluation; switching cost; data handling; differentiation value; owner after launch; recommendation and revisit date.

**Decision rules**
- Default for general capabilities: buy or configure; build only for proprietary workflows, data or method, and build evals, guardrails and data loops around whatever model is used (APPLIEDLLMS-2024, 3.2.1 and 3.2.4).
- Treat the NANDA 67% versus 33% result as a prompt for caution about internal builds, not a decision rule: it is self-reported and the authors say it may reflect capability differences (MITNANDA-2025).
- Regulated or high-risk sector: a16z reports build-to-buy has not played out there; assume more in-house control is needed and require stronger evidence (A16Z-2025 item 12).
- Advisor default: if no one can name the post-launch owner, do not start a build.

### 8.3 Design brief

**Checklist**
- Autonomy rung chosen with the evidence needed to move up (ANTHROPIC-2024).
- Runtime class chosen (advisor mapping below).
- Data and retrieval: sources, freshness, ownership, chunking and retrieval evaluation plan (UKGDS-2025 GOV.UK Chat; APPLIEDLLMS-2024 section 1.2).
- Integrations: read and write permissions, approval points (OPENAI-2025; LANGCHAIN-2024).
- Security: OWASP LLM risk screen, sensitive-data handling, access controls (OWASP-2025; HUYEN-2024; UKGDS-2025).
- Human oversight: failure thresholds, high-risk actions, who reviews (OPENAI-2025).
- Logging and observability design (HUYEN-2024 observability; UKGDS-2024).
- Fallback and rollback (UKGDS-2025; NIST-2024 GV-6.2-006 rollover and fallback may be manual).

**Template (design brief): sections**
Purpose and non-goals; users and review roles; runtime class and autonomy rung; architecture sketch (inputs, retrieval, model calls, tools, outputs); data sources and owners; integration and permission table; security and privacy controls; human checkpoints and escalation triggers; failure behavior ("I don't know", fallback); logging and retention; cost envelope; open risks; evaluation plan link.

**Advisor mapping of runtime classes (not from a source)**

| Runtime class | Typical fit | Main risk to design for |
|---|---|---|
| Personal assistant | Individual drafting, summarizing, analysis with a person reviewing every output | Unmanaged data handling; inconsistent practice |
| Shared team skills | Repeatable team tasks with agreed prompts, templates and reference material | Version drift; no shared evals |
| Workflow automation | Fixed multi-step flows through existing systems | Silent failure; brittle integrations |
| Background agent | Latency-tolerant tasks (Berkeley found 66% of surveyed deployed agents tolerate minutes or longer) with review at the end | Compounding errors; permissions |
| Managed agent runtime | Tool-using agents needing logging, permissions, isolation and rollback | Cost; lock-in; complexity |

(Latency-tolerance figure: BERKELEY-2026, Introduction RQ1.)

### 8.4 Evaluation plan

**Checklist**
- Eval set: 20-50 real or realistic tasks to start, with reference solutions where possible; balanced (should and should-not cases) (ANTHROPIC-2026).
- Gold answers confirmed by two experts independently where judgment is involved.
- Single named domain expert for quality decisions (HUSAIN-2026).
- Error analysis plan: about 100 diverse traces, taxonomy, evaluator per failure mode.
- Grader choice: code checks first, LLM judge where needed, human review sample (ANTHROPIC-2026).
- Judge calibration against human labels; precision and recall for imbalanced classes (HUSAIN-2024).
- Consistency: number of trials; pass@k versus pass^k.
- Regression suite separate from capability suite (ANTHROPIC-2026).
- Red-teaming plan with reviewers independent of the build team (NIST-2024).
- Baseline: manual or legacy process on the same set.
- Online monitoring metrics defined: override, escalation, error categories, cost, usage.

**Template (evaluation plan): sections**
Scope and acceptance criteria; task inventory (source, difficulty, reference answer, adjudication notes); graders (code, model, human) with calibration plan; trial count and consistency metric; acceptance thresholds by failure class; baseline comparison; red-team plan and scorecard; regression suite policy; monitoring metrics and review cadence; evidence retained for audit.

**Thresholds**

| Item | Value | Basis |
|---|---|---|
| Starter eval set size | 20-50 tasks | Anthropic experience (ANTHROPIC-2026, Step 0) |
| Regression suite pass rate | near 100% | Anthropic (ANTHROPIC-2026, capability vs regression) |
| Capability suite | starts at low pass rate | Anthropic (same) |
| Annotated traces before suggesting automation | at least 30 yourself; about 100 diverse traces for discovery | Hamel Husain (HUSAIN-2026), practitioner guidance |
| Labeled examples per LLM-judge failure mode | roughly 100-200 | HUSAIN-2026 |
| Weekly production trace review | 10-20 traces; 100+ fresh traces per cycle of 2-4 weeks | HUSAIN-2026 |
| Acceptance pass rate | set as a product decision by failure tolerance; 100% on all evals suggests evals are too easy | HUSAIN-2024; HUSAIN-2026 |
| Launch accuracy bar | no universal number; GDS judged 80% expert-rated accuracy insufficient for a public pilot of an information service | UKGDS-2025 |
| Advisor default | for any failure class that is irreversible or client-facing, require a stated tolerance (including zero) and a mitigating control before launch | advisor default, not from a source |

### 8.5 Production readiness

**Checklist**
- Named owner and backup; runbook; support route; on-call or review rotation including trace review (APPLIEDLLMS-2024 2.1.2).
- Change control: quantitative validation for any model, prompt or retrieval change; managed release; rollback (UKGDS-2025).
- Monitoring: output quality, override and escalation, input coverage and freshness, latency, cost per task, usage (FRB-2011; GOOGLE-RULES; UKGDS-2024).
- Incident process: ownership, rehearsal, post-mortems (NIST-2024 GV-6.2-003; MG-4.2-002).
- Model and AI inventory entry; documentation; independent validation where required (FRB-2011; BOE-2023; FRC-2025).
- Security and privacy sign-off; access control review (UKGDS-2025; OWASP-2025).
- Adoption plan: training on capabilities, limits and review expectations; what to do when wrong (ABA-2024; BCG-2024).
- Feedback loop: how user corrections and failures reach the eval set.

**Template (readiness review): fields**
Owner, backup, support hours; runbook link; alert thresholds and responders; change-control rule; rollback test date; monitoring dashboard; data retention and access; documentation pack list; independent review (who, when); training completed; go/no-go decision and conditions.

**Decision rules**
- No go-live without a named owner, a rollback path, logging and a first review date (advisor default, consistent with UKGDS-2025 and NIST-2024).
- Go/no-go decisions should explicitly use red-team and structured-feedback results (NIST-2024 MS-4.2-005).
- In regulated settings, validation should be independent of development (FRB-2011; BOE-2023 Principle 4; NIST-2024 MS-1.3-003).

### 8.6 Launch and post-launch review

**Checklist**
- Staged launch: small group, then widen; human review level reduced only with evidence (ABA-2024 sample-testing logic; OPENAI-2025 human intervention early in deployment).
- 30/90/180-day review dates fixed at launch.
- Review metrics: override rate, escalation rate, rework, error categories, cost per task, adoption by user group.
- Failure review: new failure modes added to eval set; guardrails and training updated.
- Eval suite health: graduate saturated capability evals to regression; retire evals that always pass and cost a lot (ANTHROPIC-2026; HUSAIN-2026).
- Decision: continue, tighten, loosen autonomy, retire (NIST-2024 GV-1.7 decommissioning).

**Template (post-launch review): sections**
What was promised versus achieved; metrics with trend; override and escalation analysis; incidents and near misses; eval-set changes; cost and usage; user feedback themes; changes made and validation evidence; decision on autonomy level and next review date; lessons for other units.

**Decision rules**
- High or rising override rate, or overrides that consistently beat the system, means revise or redevelop (FRB-2011, Ongoing Monitoring).
- Advisor default: loosen human review only after a measured sample shows stable quality across at least one full review cycle; tighten immediately after an incident.

---

## 9. Sources

All accessed 2026-10-20. Access: `full` means the document or page text was read; `partial` means only part was readable; `search-only` means only search-result summaries were seen.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| HUSAIN-2024 | Your AI Product Needs Evals | Hamel Husain | practitioner article | https://hamel.dev/blog/posts/evals/ | 2024-03-29 | full |
| HUSAIN-2026 | LLM Evals: Everything You Need to Know (FAQ) | Hamel Husain (and Shreya Shankar, per page) | practitioner guide | https://hamel.dev/blog/posts/evals-faq/ | page shows published 2026-09-18, updated 2026-09-21 | full |
| APPLIEDLLMS-2024 | What We've Learned From A Year of Building with LLMs | Yan, Bischof, Frye, Husain, Liu, Shankar | practitioner guide | https://applied-llms.org/ | 2024-06-08 | full |
| YAN-2023 | Patterns for Building LLM-based Systems and Products | Eugene Yan | practitioner article | https://eugeneyan.com/writing/llm-patterns/ | 2023 (exact date not shown on fetched page) | full |
| HUYEN-2024 | Building A Generative AI Platform | Chip Huyen | practitioner article | https://huyenchip.com/2024/07/25/genai-platform.html | 2024-07-25 | full |
| ANTHROPIC-2024 | Building effective agents | Anthropic (Engineering) | vendor engineering guide | https://www.anthropic.com/engineering/building-effective-agents | 2024-12-19 (page carries a later note that tooling has changed) | full |
| ANTHROPIC-2026 | Demystifying evals for AI agents | Anthropic (Engineering) | vendor engineering guide | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | 2026-01-09 | full |
| OPENAI-2025 | A practical guide to building agents | OpenAI | vendor guide (PDF) | https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf | April 2025 (PDF metadata date 2025-04-07) | full |
| MSFT-REDTEAM | AI Red Teaming Agent | Microsoft Learn | vendor product documentation | https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-red-teaming-agent | undated page | full (overview) |
| OWASP-2025 | OWASP Top 10 for LLM Applications 2025 | OWASP GenAI Security Project | standards-body project list | https://genai.owasp.org/llm-top-10/ | 2025 edition (list read; per-risk detail not read) | partial |
| GOOGLE-RULES | Rules of Machine Learning | Google for Developers (M. Zinkevich) | practitioner guide | https://developers.google.com/machine-learning/guides/rules-of-ml | undated page | full |
| GOOGLE-2015 | Hidden Technical Debt in Machine Learning Systems | Sculley et al., Google (NeurIPS) | academic paper | https://papers.nips.cc/paper_files/paper/2015/file/86df7dcfd896fcaf2674f757a2463eba-Paper.pdf | 2015 | full |
| GOOGLE-2021 | Practitioners guide to MLOps | Google Cloud (Salama, Kazmierczak, Schut) | white paper | https://services.google.com/fh/files/misc/practitioners_guide_to_mlops_whitepaper.pdf | May 2021 | partial (overview, capabilities, monitoring read) |
| RAND-2024 | The Root Causes of Failure for Artificial Intelligence Projects and How They Can Succeed | RAND Corporation | research report | https://www.rand.org/pubs/research_reports/RRA2680-1.html | 2024-08-13 | full (via r.jina.ai mirror) |
| MITNANDA-2025 | The GenAI Divide: State of AI in Business 2025 | MIT Project NANDA (Challapally, Pease, Raskar, Chari) | research report (preliminary) | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf | July 2025 (mirror header 2025-08-20) | full (via r.jina.ai mirror of a copy hosted at mlq.ai) |
| BCG-2024 | AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value | Boston Consulting Group | consultancy press release (report: Where's the Value in AI?) | https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value | 2024-10-24 | full (press release; underlying report not read) |
| A16Z-2025 | How 100 Enterprise CIOs Are Building and Buying Gen AI in 2025 | Andreessen Horowitz | investor survey and article | https://a16z.com/ai-enterprise-2025/ | 2025-06-10 | full |
| LANGCHAIN-2024 | State of AI Agents | LangChain | vendor survey report | https://www.langchain.com/stateofaiagents | 2024 survey; page carries a 2026-06-12 stamp | full |
| THOUGHTWORKS-2025 | LLM as a judge (Technology Radar) | Thoughtworks | consultancy radar entry | https://www.thoughtworks.com/radar/techniques/llm-as-a-judge | last updated 2025-11-05; Nov 2025 edition status Assess (moved from Trial) | full |
| BERKELEY-2026 | Measuring Agents in Production (MAP) | Pan, Arabzadeh et al., UC Berkeley, IBM Research, Intesa Sanpaolo and others | academic paper (arXiv 2512.04123; v4 dated 2026-06-04; ICML 2026 proceedings header) | https://arxiv.org/pdf/2512.04123 | 2026-06-04 (v4) | full |
| SIERRA-2024 | tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | Yao, Shinn, Razavi, Narasimhan (Sierra) | benchmark paper (arXiv 2406.12045) | https://arxiv.org/pdf/2406.12045 | 2024-06-17 | full |
| LMSYS-2023 | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | Zheng et al. | academic paper (arXiv 2306.05685) | https://arxiv.org/pdf/2306.05685 | 2023 | full |
| SHANKAR-2024 | Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences | Shankar et al. (UC Berkeley) | academic paper (arXiv 2404.12272) | https://arxiv.org/pdf/2404.12272 | 2024-04-18 (v1) | full |
| STANFORD-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools | Magesh, Surani, Dahl, Suzgun, Manning, Ho (Stanford, Yale) | academic preprint (arXiv 2405.20362, v1) | https://arxiv.org/pdf/2405.20362 | 2024-05-30 (manuscript dated 2024-06-03) | full |
| HBS-2023 | Navigating the Jagged Technological Frontier | Dell'Acqua, McFowland, Mollick, Lifshitz-Assaf, Kellogg, Rajendran, Krayer, Candelon, Lakhani | working paper (HBS 24-013) | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | September 2023 | partial (abstract and citation page; full PDF blocked) |
| VALS-2025 | Vals Legal AI Report (VLAIR) | Vals AI with Legaltech Hub | third-party benchmark report | https://www.vals.ai/vlair | updated 2025-02-27 | full (page summary and first results table) |
| GUARDIAN-2025 | Deloitte to pay money back to Albanese government after using AI in $440,000 report | The Guardian Australia | news report | https://www.theguardian.com/australia-news/2025/oct/06/deloitte-to-pay-money-back-to-albanese-government-after-using-ai-in-440000-report | 2025-10-06 | full |
| ABA-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools | American Bar Association Standing Committee on Ethics and Professional Responsibility | professional-body opinion | https://www.mcle.org/ePrograms/2250081P01/1--aba-formal-opinion-512.pdf (copy of the ABA PDF; the americanbar.org URL returned 403) | 2024-07-29 | full |
| FRC-2025 | FRC publishes landmark guidance providing clarity to audit profession on the uses of AI | UK Financial Reporting Council | regulator news release (guidance and thematic review linked, not read) | https://www.frc.org.uk/news-and-events/news/2025/06/frc-publishes-landmark-guidance-providing-clarity-to-audit-profession-on-the-uses-of-ai/ | 2025-06-26 | partial (release only; the guidance PDF returned 403) |
| FRB-2011 | SR 11-7 Attachment: Supervisory Guidance on Model Risk Management | Federal Reserve Board and Office of the Comptroller of the Currency | regulator guidance | https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf | 2011-04-04 | full |
| BOE-2023 | SS1/23 Model risk management principles for banks | Bank of England, Prudential Regulation Authority | regulator supervisory statement | https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss | published 2023-05-17, effective 2024-05-17 | partial (landing page: five principles named; full statement not read) |
| NIST-2024 | NIST AI 600-1: Artificial Intelligence Risk Management Framework: Generative AI Profile | NIST | standards-body profile | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | July 2024 | full (actions read for GV-6.2, MS-1.3, MS-2.5, MS-4.2, MG-4.1) |
| UKGDS-2024 | Generative AI Framework for HMG | UK Government Digital Service and partners | government guidance (withdrawn 2025-02-10, superseded by the AI Playbook) | https://www.gov.uk/government/publications/generative-ai-framework-for-hmg/generative-ai-framework-for-hmg-html | published 2024-01-18 | full |
| UKGDS-2025 | Artificial Intelligence Playbook for the UK Government | UK Government (GDS, with departments and industry contributors) | government guidance with case studies | https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government/artificial-intelligence-playbook-for-the-uk-government-html | 2025-02-10 | full |
| GARTNER-2025 | Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 | Gartner | analyst press release | https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027 | 2025-06-25 (per URL) | search-only (page returned 403) |

Source types (35 listed; 34 read in full or part, 1 search-only): practitioner articles and guides 7 (HUSAIN-2024, HUSAIN-2026, APPLIEDLLMS-2024, YAN-2023, HUYEN-2024, GOOGLE-RULES, GOOGLE-2021); vendor engineering and product guides 4 (ANTHROPIC-2024, ANTHROPIC-2026, OPENAI-2025, MSFT-REDTEAM); academic and working papers 7 (GOOGLE-2015, BERKELEY-2026, SIERRA-2024, LMSYS-2023, SHANKAR-2024, STANFORD-2024, HBS-2023); research, consultancy, investor and vendor surveys and reports 6 (RAND-2024, MITNANDA-2025, BCG-2024, A16Z-2025, LANGCHAIN-2024, THOUGHTWORKS-2025) plus 1 third-party benchmark (VALS-2025); professional-body, regulator and standards guidance 8 (ABA-2024, FRC-2025, FRB-2011, BOE-2023, NIST-2024, OWASP-2025, UKGDS-2024, UKGDS-2025); news case report 1 (GUARDIAN-2025); analyst forecast, search-only 1 (GARTNER-2025).

---

## 10. Gaps

- **Measured quality in production knowledge-work deployments.** I found no public, independently measured override, escalation or error rates from named organizations on live knowledge-work systems, and no published parallel-run results. GOV.UK Chat is a pilot with expert-rated accuracy, not a production system.
- **Build versus buy total cost.** No source I read gives measured total-cost-of-ownership comparisons. The only deployment-rate comparison (MITNANDA-2025) is self-reported interview data with acknowledged confounding, and its internal numbers are inconsistent in places (for example "7 of 9" sectors in one section and "2 of 8" in the summary, and about 50% versus about 70% of budget to sales and marketing in different places). Treat it as directional.
- **Blocked or not reached.** McKinsey's state of AI, Gartner's press release (search summaries only, which also vary on "canceled" versus "paused or restructured"), Deloitte and other Big Four AI delivery or assurance publications, ISO/IEC 42001 text, the Law Society guidance, the FRC guidance PDF and thematic review (only the release was read), the full BOE SS1/23 statement, the Dell'Acqua PDF (abstract only), the BCG underlying report, and the OCC copy of SR 11-7 (the Federal Reserve copy was read). The FRC and ABA material was read from the FRC release and an mcle.org copy of the ABA PDF.
- **Books.** I could not read publisher pages for any book. O'Reilly's AI Engineering page (403) and the HBR article on prediction economics (paywalled) were not usable. The practitioner guide APPLIEDLLMS-2024 and the Huyen and Yan articles stand in for book-style practitioner material; they are articles, not books. Book summaries from reputable reviews were not retrieved.
- **Conference talks and webinars.** None retrieved. Anthropic and Hamel material cites talks but I did not read them.
- **Professional-services specifics.** No published firm-level acceptance thresholds, sampling plans or documentation templates from a named professional-services firm. Regulator and professional-body guidance (ABA, FRC) is principle-level. ISA-level audit standards on use of tools were not reached.
- **Date uncertainty.** YAN-2023 has no date on the fetched page; LANGCHAIN-2024 shows both a 2024 title and a 2026 date stamp (treated as a 2024 survey republished); GOOGLE-RULES and MSFT-REDTEAM are undated pages; OWASP-2025 page dates relate to translations; HUSAIN-2026 dates are as displayed on the page.
- **Currency.** Several empirical results use 2023-2024 models (STANFORD-2024, SIERRA-2024, HBS-2023). Products have changed since; they show method and order of magnitude, not current performance. ANTHROPIC-2024 itself notes the tooling landscape has changed since publication.
- **Runtime-class guidance.** The mapping of the autonomy ladder to runtime classes in section 8.3 is my synthesis. No source maps delivery decisions to these classes.
- **Thresholds.** Most numeric starting points in section 8.4 are practitioner guidance (Anthropic, Hamel Husain) rather than validated standards. Those marked "advisor default" are mine.
- **Grade A candidates.** Under the 2026-10-17 rule, the clearest named-organization-measured figures are UKGDS-2025 (GOV.UK Chat 80% expert-rated accuracy), the academic and benchmark measurements (STANFORD-2024, HBS-2023, SIERRA-2024, BERKELEY-2026), and VALS-2025 with its opt-in caveat. None is a measured outcome of a production AI delivery in a professional-services firm.
