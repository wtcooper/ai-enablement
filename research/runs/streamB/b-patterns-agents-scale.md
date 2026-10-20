# Agentic patterns at scale: `end-to-end-case-agent` and `bulk-transformation`

Kind: agentic patterns (shared backbone library). Written 2026-10-20. Sources were read by `curl`, `pdftotext` or the r.jina.ai mirror unless marked `search-only` in section 7. Evidence grades, provenance values and ladder values are the controlled vocabulary. Where a statement is my own inference rather than a sourced fact, it is marked "(advisor inference)".

---

## 1. Summary

- **Both patterns work in public evidence only when a deterministic check sits next to the model.** Bulk transformation reports its best results where tests, linters, type checks or sampled expert review gate each output (Google, Airbnb, Amazon: GOOGLE-2025 §III-IV; AIRBNB-2025 "File Validation"; AMAZON-2024). The model alone is weak: in an IBM/Illinois study, correct code translations ranged from 2.1% to 47.3% across models on 1,700 samples (IBM-2024 abstract).
- **Bulk transformation is the more mature pattern.** Five measured, self-reported results from technology, public-sector and healthcare-research organizations (Google, Airbnb, Amazon, UK i.AI Consult, University of Kentucky) report how much AI output was completed or accepted without human change or matched expert review (60% to 97%, measured differently in each), with a human step for the rest. No source reports a rate of silent errors found after cutover; that evidence is absent.
- **End-to-end case agents have deployments, but almost no published quality measurements.** The named deployments (Allianz Project Nemo, UK i.AI planning prototype) publish speed figures or none, and keep a human at the decision (ALLIANZ-2025; IAI-PLANNING-2026). Independent benchmarks of agents on multi-step work show low reliability: best agent completing 30% of simulated-company tasks (CMU-2024), 2.5% automation rate on real freelance projects (CAIS-2025), pass^8 below 25% in a retail policy task (SIERRA-2024). Those use 2024-2025 models, so they set a floor, not a current score.
- **Human review becomes the bottleneck and then the weak link.** Google throttled weekly migration output so reviewers were not overwhelmed (GOOGLE-2025 §V, §VIII.D). Regulators name automation bias as a risk (NIST-2024 §2.7; IMDA-2026 para 3; EUR-2024 Art 14). Design the checkpoint, its sample size and its reviewer capacity, not just its existence.
- **The ladder is set by reversibility and by who is affected, not by model capability.** Allianz keeps payout decisions human by design (ALLIANZ-2025). Replit's agent deleted a production database during a stated freeze (OECD-2025, user account). Decisions that affect individuals' rights meet GDPR Art 22 and, for high-risk uses, EU AI Act Art 14 and 26 (EUR-2016; EUR-2024).
- **The EU timetable moved.** The AI Omnibus entered into force on 27 July 2026, and the Commission says Annex III high-risk rules apply from 2 December 2027 and Annex I from 2 August 2028 (EC-2026).
- **Savings claims rest on contested baselines.** Asana's "five years / $6M" baseline was a back-of-envelope estimate, per Asana's own developer-productivity lead quoted in a practitioner article (PRAGMATIC-2026). Ask what the counterfactual was.
- **Evidence gaps are large for manufacturing, healthcare operations and retail case agents.** I found no named manufacturer, no named health system running a case agent with published measurements, and no published silent-error rate for any bulk migration (section 6).

---

## 2. Item profiles

### 2.1 `end-to-end-case-agent`

**What it does and where it fits.** An agent takes a case from intake to resolution across several systems, with human checkpoints at key decisions and before anything irreversible (library index §3, working definition). Anthropic describes agents as suited to open-ended problems where the number of steps cannot be predicted and a fixed path cannot be hard-coded, "in trusted environments" (ANTHROPIC-2024, "When to use agents"). Its two promising applications, customer support and coding agents, share these traits: conversation and action together, clear success criteria, feedback loops and meaningful human oversight (ANTHROPIC-2024, Appendix 1).
- *Work types:* mainly `transaction-processing`; also `coordination-scheduling` and `review-assurance` (advisor inference from the library index).
- *Cues in a user's description of work:* "a claim / ticket / return / return-filing / alert arrives, someone pulls data from three systems, checks a policy, decides, updates the systems and tells the customer"; high volume of low-value cases; policy written down; systems with APIs; cases waiting in queues during peaks. Allianz describes the cue itself: a simple food-spoilage claim that took four days or more because claims teams were busy with complex claims during a storm (ALLIANZ-2025, paragraph "From a customer's perspective").
- *Do not offer it when* the user describes judgment under ambiguity with no written criteria, or one-off cases (see anti-patterns).

**Ladder range and runtime class.**
- *augment* (agent prepares each case; person decides each one): `workflow-automation`. Allianz Nemo is the clearest public example: seven agents prepare the claim and an audit agent writes a summary "and passes it to a human agent to make the payment decision" (ALLIANZ-2025, "Nemo works like this"). The chain is multi-step, so on the library's definition it is `delegate` with a per-case human approval.
- *automate* (no person on the normal path for a defined, reversible step; exceptions go to people): `workflow-automation` or `background-agent`, for example Klarna's assistant resolving refunds, returns and disputes in chat, with live agents still available (KLARNA-2024).
- *delegate* (agent owns the multi-step outcome, started by events, with checkpoints): `managed-agent-runtime`. Anthropic's production notes explain why: agents are stateful, errors compound, and they needed resumption from the point of failure, regular checkpoints, full tracing and "rainbow deployments" so running agents are not broken by releases (ANTHROPIC-2025, "Production reliability and engineering challenges"). Mapping these needs to the runtime class is advisor inference.

**How it is built.**
- *Inputs:* the case event, the case record across systems, the written policy, and customer-supplied evidence. Tool design matters as much as prompts: Anthropic recommends investing in the agent-computer interface as much as in human-computer interfaces (ANTHROPIC-2024, Appendix 2).
- *AI role:* plans, calls tools and gets "ground truth" from the environment at each step (tool results, code execution) to judge progress; it can pause for human feedback at checkpoints or blockers, and stopping conditions such as a maximum number of iterations keep control (ANTHROPIC-2024, "Agents"). Multi-agent designs split work into specialists: Allianz uses planner, cyber (data security), coverage, weather, fraud, payout and audit agents (ALLIANZ-2025). Anthropic reports multi-agent systems fit parallel, breadth-first work and fit badly where agents share one context or have many dependencies; most coding tasks have fewer parallelizable parts (ANTHROPIC-2025, "Benefits of a multi-agent system").
- *Human checkpoints:* IMDA's framework asks organizations to define "significant checkpoints at which human approval is required" and to limit agents' autonomy and access to tools and data (IMDA-2026, para 5). FINRA lists where to put "human in the loop" oversight, how to track agent actions and how to restrict agent behaviors as questions for firms (FINRA-2025, GenAI section "Agents"). Allianz limits Nemo to low-value food-spoilage claims (threshold AUD 500) and never automates the payout decision (ALLIANZ-2025).
- *Thresholds and sampling:* scope by claim value and reversibility (Allianz); for auto-resolved cases, post-hoc sampling uses standard acceptance-sampling logic: single, double, multiple and sequential plans, with an acceptable quality level and a limiting defect level (NIST-HANDBOOK §6.2.2). Applying lot-acceptance sampling to agent-closed cases is advisor inference; I found no deployment that publishes its sampling plan.
- *Logging and audit trail:* Anthropic added full production tracing and monitors agent decision patterns without reading conversation contents (ANTHROPIC-2025). Allianz's audit agent summarises every agent decision for the human (ALLIANZ-2025). Under the EU AI Act, deployers of high-risk systems keep automatically generated logs for at least six months unless other law says otherwise (EUR-2024, Art 26(6)).

**Prerequisites.** Written policy and decision criteria; API access to the systems of record with scoped credentials; a reversible or approval-gated write path; an evaluation set built from real cases; named human owner for the exception queue; staff with "competence, training and authority" for oversight if the system is high-risk (EUR-2024, Art 26(2)). Anthropic evaluated agents that change state by checking the end state rather than each turn, with checkpoints where specific state changes should have occurred (ANTHROPIC-2025, Appendix, "End-state evaluation").

**Failure modes and controls.**
| Failure | Evidence | Control |
|---|---|---|
| Errors compound across steps; one failure sends the agent down a different path | ANTHROPIC-2025 ("Agents are stateful and errors compound"); ANTHROPIC-2024 ("compounding errors") | Resume and checkpoint, deterministic retry logic, sandbox tests, stopping conditions |
| Inconsistent behaviour on repeated runs | SIERRA-2024: pass^8 below 25% in retail for the best model tested | Report pass^k, not average success; test repeats before go-live |
| Taxonomy of multi-agent failure: design, inter-agent misalignment, task verification | BERKELEY-2025 (14 modes, 1,642 traces; 41% to 86.7% failure rates across 7 open-source systems) | Explicit verification step; clarification when unclear; reduce agent hand-offs |
| Destructive action against explicit instruction | OECD-2025 (Replit, user account) | Separate production from development; approval gate on irreversible writes |
| Acting beyond scope or authority; hard to trace multi-step reasoning | FINRA-2025 | Scoped identity and tool access; action log tied to a human owner |
| Over-reliance by reviewers (automation bias) | NIST-2024 §2.7; EUR-2024 Art 14(4)(b); IMDA-2026 | Seeded test cases, reviewer sampling, rotating review, measured override rate |
| Quality drops when cost dominates the design | ENTREPRENEUR-2025 (Klarna CEO, "lower quality") | Quality metric with equal weight to cost; human route preserved |
| Confidential data leakage | CRMArena-Pro found "near-zero" inherent confidentiality awareness (SALESFORCE-2025 abstract) | Data-scoped tools, no reliance on prompting for confidentiality |

**Value levers and metrics.** `speed` (cycle time: Allianz "several days to one day or hours" for claims under AUD 500; Klarna resolution under 2 minutes vs 11 minutes, both self-reported); `capacity` (Klarna's "equivalent work of 700 full-time agents", self-reported); `quality` (repeat-inquiry rate, Klarna: 25% drop; override rate and escalation rate, which none of the deployments I found publish); `cost` (Klarna estimated $40M profit improvement for 2024, an estimate); `experience` (CSAT parity claimed by Klarna). Metrics an advisor should require that sources do not publish: share of cases closed with no human edit, share escalated, share overturned on appeal or complaint, error rate in a sampled audit, cost per resolved case including tokens. Anthropic reports agents use about four times the tokens of chat and multi-agent systems about fifteen times, so unit cost must include inference (ANTHROPIC-2025, "Benefits of a multi-agent system").

**Governance points.**
- *NIST AI RMF:* GOVERN 3.2 (roles and responsibilities for human-AI configurations and oversight), MAP 3.5 (human oversight processes defined, assessed and documented), MANAGE 2.4 (mechanisms to "supersede, disengage, or deactivate" systems that perform inconsistently with intended use) (NIST-2023, Core tables). The generative-AI profile adds automation bias and confabulation as risks (NIST-2024 §2.2, §2.7).
- *EU AI Act:* high-risk systems must be designed to be effectively overseen by natural persons, with measures to understand capacity, stay aware of automation bias, interpret output, decide not to use or override, and intervene or stop (EUR-2024, Art 14). Art 6(3) lets a provider show that an Annex III system is not high-risk where it performs, for example, a narrow procedural task or a preparatory task, but profiling of natural persons is always high-risk (EUR-2024, Art 6(3)). Deployers must assign oversight, monitor and keep logs (Art 26). Timing: Annex III obligations from 2 December 2027 (EC-2026).
- *GDPR Art 22:* a right not to be subject to a decision based solely on automated processing with legal or similarly significant effects, with safeguards of at least human intervention, expressing a view and contesting the decision where the Article's exceptions apply (EUR-2016, Art 22(1), 22(3)).
- *Sector:* FINRA's 2026 report lists autonomy, scope and authority, auditability, data sensitivity, domain knowledge and reward design as agent risks for broker-dealers (FINRA-2025). Singapore's agentic framework adds lifecycle controls such as baseline testing and whitelisted services (IMDA-2026 para 5). The Robodebt Royal Commission recommended a clear path of review for those affected by automated decisions, public disclosure that automation is used, availability of business rules and algorithms for scrutiny, and a monitoring and audit body (ROBODEBT-2023, Recs 17.1, 17.2). OWASP published a Top 10 for agentic applications on 2025-12-09 (OWASP-2025; I read only the landing page).
- *ISO/IEC 42001:* I could not retrieve the standard (paywalled); no claim made (section 6).

**How it evolves up the ladder.** Per-case approval (augment) leads, as the evaluation set and the logged override rate justify it, to approval only above a value or risk threshold (automate for the low tier), then to delegation of whole case types with sampled audit. Evidence for the step from augment to automate is thin: Klarna moved to automation and then reinstated human capacity, saying quality had fallen (ENTREPRENEUR-2025). Anthropic's own guidance is to find the simplest solution possible and add complexity only when needed (ANTHROPIC-2024, "When (and when not) to use agents"). Role change: Allianz says claims staff spend less time on routine checks and more on complex or emotionally sensitive cases (ALLIANZ-2025). Human oversight skill erodes when automation handles the routine, leaving the person the hard cases (BAINBRIDGE-1983, "second irony").

**Anti-patterns.**
- Giving an agent write access to production without an approval gate or backups (OECD-2025).
- Using a solely automated decision for individuals with significant effects with no route to human review (EUR-2016 Art 22; ROBODEBT-2023 Recs 17.1; court record in AFS-2026 on algorithmic denials).
- Judging the agent by average success when the process needs consistency every time (SIERRA-2024).
- Multi-agent design for tightly coupled work or low-value tasks (ANTHROPIC-2025).
- Cutting the human route to save cost before quality is measured (ENTREPRENEUR-2025).
- Relabelling an RPA flow or chatbot as an "agent": Gartner reportedly calls this "agent washing" (GARTNER-2025, search-only).

### 2.2 `bulk-transformation`

**What it does and where it fits.** Converts, migrates or rewrites large volumes of content, data or code, with sampled quality checks and sign-off before cutover (library index §3). Cross-industry cases cover code migration (Google, Airbnb, Amazon, Nubank), catalog and product data (Walmart, Amazon), unstructured text into structured data (UK i.AI Consult and Extract; University of Kentucky chart extraction). Best fit is a repeated, well-defined transformation with many instances, a checkable result and a baseline cost that is large (GOOGLE-2025 §III; AIRBNB-2025 "How We Did It").
- *Work types:* `software-systems`, `document-production`, `data-reporting` (library index §2).
- *Cues:* "we have thousands of files / records / documents to move, reformat, reclassify or upgrade"; "this has sat on the backlog for years"; "every team has to do the same change". Google notes migrations that had been stalled for several years were completed (GOOGLE-2025 §I). Asana ran its Enzyme migration as a low-priority backlog item (PRAGMATIC-2026, Asana comment).

**Ladder range and runtime class.**
- *assist:* a person converts a file with an assistant; `personal-assistant`.
- *augment:* the model drafts each conversion and a person reviews every output; Consult reviewers checked themes at a median of 23 seconds per response (IAI-SCOT-2025, Exec summary); `shared-team-skills` or `workflow-automation`.
- *automate:* a per-file pipeline runs with validators and retries; people handle failures and sample results. Airbnb modelled it as a state machine with steps for Enzyme refactor, Jest fix, lint and type-check fix (AIRBNB-2025). `workflow-automation` or `background-agent`.
- *delegate:* an agent owns the campaign: finds locations, generates changes, repairs failures, shards changes to owners for review. Google's ID migration did this with a human expert triggering the toolkit and checking before sharding to reviewers (GOOGLE-2025 §III-IV); Nubank's account of Devin has humans "just to manage the project and approve changes" (COGNITION-2024). `managed-agent-runtime`. Mapping classes to rungs is advisor inference.

**How it is built.**
- *Inputs:* the source population (files, records, documents), the target specification, worked examples, and test or validation tooling. Airbnb's prompts grew to 40,000-100,000 tokens, pulling in up to 50 related files, few-shot examples and passing sibling tests; the authors say choosing the right related files mattered more than prompt wording (AIRBNB-2025 "Increasing the Context").
- *AI's role:* Google states the LLM role "is focused on the edit generation"; locating change sites and validating results are handled mostly by deterministic AST techniques, with some LLM support (GOOGLE-2025 §III). The loop iterates on tests and validations until the change is deemed good; failed validations can trigger an ML repair step (GOOGLE-2025 §III-IV).
- *Human checkpoints:* Google: humans review LLM-generated code the same way as any other change and add missing tests; landing and rollout "still require a human operator" (GOOGLE-2025 §VIII.D). Airbnb: retained manual completion for the last ~3% of files (AIRBNB-2025 "Results"). Consult: reviewers could change themes; no change was made to 73% of responses in the DWP evaluation (IAI-DWP-2025, Exec summary).
- *Thresholds and sampling:* Airbnb capped retries per step (most simple files finished by 10 attempts), then ran a "sample, tune, sweep" loop on 5-10 failing files at a time, and stopped automating when files had been retried 50-100 times (AIRBNB-2025 §2, §4). Google limited weekly changes generated to avoid overwhelming reviewers (GOOGLE-2025 §V). University of Kentucky benchmarked extraction on 100 expert-annotated patients and described a quality-control review of 10% of charts by an independent reviewer for the manual baseline (UKY-2025, Results and Discussion). Formal acceptance-sampling designs (accept/reject a lot by defects found in a sample) are standard quality practice (NIST-HANDBOOK §6.2.2); applying them to cutover sign-off is advisor inference.
- *Logging and audit trail:* Airbnb stamped each file with an automatic comment recording the status of each migration step, and allowed re-runs of a single file or path filtered by the stuck step (AIRBNB-2025 §4). Google measured AI-authored share by comparing the first LLM-generated changelist version against the committed version per character (GOOGLE-2025 §IV).

**Prerequisites.** A validator the team trusts (tests, type checks, schema checks, a gold set); a reviewer pool with capacity and code ownership; a campaign tool that can re-run subsets; a rollback or gradual rollout path (Google: gradual and responsible rollouts, GOOGLE-2025 §VIII.D); a baseline estimate honestly stated (PRAGMATIC-2026). For data: an expert-annotated benchmark and an agreed definition (UKY-2025 found that billing codes selected patients of whom only 51% truly had traumatic spinal cord injury).

**Failure modes and controls.**
| Failure | Evidence | Control |
|---|---|---|
| Silent semantic errors that compile and pass weak tests | IBM-2024 (15 categories of translation bugs); GOOGLE-2025 §VI (Joda to java.time: AI-generated comment warns "Interval is NOT a drop in replacement") | Stronger tests; domain-expert review for semantically risky classes; staged rollout |
| Plain prompting fails beyond simple cases | GOOGLE-2025 §I ("not sufficient for anything but the simplest of migrations") | Combine deterministic analysis, LLM edits and validation |
| Human review becomes the throttle | GOOGLE-2025 §V and §VIII.D | Shard to code owners; cap weekly output; reduce review load with LLM-driven verification |
| Reviewers revert changes the model got wrong | GOOGLE-2025 §IV ("in most cases, the human needed to revert at least some changes") | Expert pre-check before sharding |
| Long tail | AIRBNB-2025 §4 (3% left after 50-100 retries) | Breadth-first tuning, then accept manual work using the failed baseline |
| Gold standard itself wrong | UKY-2025 Discussion (some false positives were mislabeled in the expert set); IAI-SCOT-2025 note 2 (two reviewers disagreed on exact mappings 40% of the time in an earlier unpublished evaluation) | Measure LLM-vs-reviewer against reviewer-vs-reviewer agreement (IAI-DWP-2025: 0.816 vs 0.710 F1) |
| Hidden bias by group | IAI-DWP-2025 (no difference in performance by self-reported disability status) | Test performance across subgroups before relying on it |

**Value levers and metrics.** `capacity` and `cost` (developer-days: Amazon average Java 17 upgrade "50 developer-days to just a few hours", estimated; Google >50% time saving by engineer estimate); `speed` (Airbnb 6 weeks vs 1.5-year estimate); `quality` (share accepted unchanged: Google ~87% JUnit, 80% ID migration, Amazon 79%; F1 against reviewers); `risk` (Amazon says upgrades "enhanced security and reduced infrastructure costs"). Google insists on end-to-end time saved, including finding locations, review and rollout, not code-generation speed alone (GOOGLE-2025 §III).

**Governance points.**
- *NIST AI RMF 1.0/600-1:* MANAGE 2.4 (disengage on inconsistent performance) and the GenAI profile on confabulation and information integrity apply to AI-generated records and code (NIST-2023; NIST-2024 §2.2, §2.8).
- *EU AI Act:* many internal conversions will not be high-risk; where an Annex III system performs a "narrow procedural task" or "preparatory task", Art 6(3) allows a provider to document that it is not high-risk, but profiling of natural persons is always high-risk (EUR-2024, Art 6(3)). The applicability for a given bulk job is a legal question to check, not something the sources settle.
- *Sector/public:* in the UK, Consult received a "Social Readiness Advisory Label" from Nesta's approach (IAI-CONSULT-2026). Data-protection duties when converting personal data (for example patient records) apply but I did not retrieve sector texts (section 6).
- *Software supply chain:* code quality remains assured by the normal review process; Google says the long-term effect on quality "remains to be seen" (GOOGLE-2025 §III).

**How it evolves up the ladder.** From assisted one-off conversion, to a reviewed pipeline, to a validator-gated pipeline with sampled review (Airbnb, Google), to a campaign agent that finds, edits, repairs and shards work. Google states that tooling will be needed "to further reduce or accelerate human involvement" because review and rollout still need a person (GOOGLE-2025 §VIII.D). Roles shift from doing conversion to defining rules, building validators, tuning and reviewing. In the Ads ID migration Google reports reduced communication overhead because "a single engineer could generate all necessary changes" (GOOGLE-2025 §IV).

**Anti-patterns.**
- Using a general chat model on a many-file migration with no validators (IBM-2024; GOOGLE-2025 §I).
- Migrating where the equivalence criterion is judgment, not testable, without domain review (GOOGLE-2025 §VI example).
- Claiming savings against an inflated manual baseline (PRAGMATIC-2026).
- Cutover without a sample large enough to find rare errors; or ignoring that human reviewers cannot keep pace (GOOGLE-2025 §VIII.D).
- A transformation that changes decisions about people (for example, bulk re-scoring of individuals) described as "data cleaning" (advisor inference; see EUR-2024 Art 6(3) profiling rule).

---

## 3. Examples

Each row: organization (industry), what changed, ladder, change scope, outcome with provenance, grade, source ref. Dates are in section 7.

### 3.1 `end-to-end-case-agent`

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Source |
|---|---|---|---|---|---|---|
| 1 | Allianz Australia / Allianz Technology (insurance, Australia) | Project Nemo: seven agents handle coverage, weather, fraud, payout and audit steps for food-spoilage claims under AUD 500; human makes the payment decision | delegate / process | "80% reduction in claim processing and settlement time" stated by a chief transformation officer (self-reported; no measurement basis given); "less than five minutes" from filing to human review in the worked example; launched July 2025; built "in under 100 days" | B | ALLIANZ-2025, "Nemo works like this" and para quoting Janssen |
| 2 | Klarna (payments / fintech, global) | AI assistant handles customer-service chats including refunds, returns, disputes; live agents still available | automate / process | In its first month: 2.3 million conversations, two-thirds of chats; "equivalent work of 700 full-time agents"; 25% drop in repeat inquiries; resolution under 2 minutes vs 11 minutes; estimated $40M profit improvement for 2024 (self-reported; the estimate is an estimate) | B (adjacent: `service-agent-escalation`) | KLARNA-2024 |
| 3 | Klarna (payments / fintech) | CEO told Bloomberg the company is hiring human customer-service staff again; said cost had been too dominant and had produced "lower quality" | automate to hybrid / process | Quality statement by the CEO, no metric (self-reported, reported by Entrepreneur; Bloomberg original not read) | B | ENTREPRENEUR-2025 |
| 4 | Anthropic (technology) | Research feature: lead agent plans and spawns parallel subagents; citation agent attributes claims | delegate / process | Multi-agent system with Opus 4 lead and Sonnet 4 subagents outperformed single-agent Opus 4 by 90.2% on an internal research eval; agents use ~4x and multi-agent ~15x chat tokens (self-reported; vendor internal eval) | B (read-only research task; adjacent) | ANTHROPIC-2025 |
| 5 | UK Incubator for AI, Augmented Planning Decisions (public sector, UK) | Prototype triages householder planning applications, summarises key information and gives officers an initial assessment | augment / process | "Prototype"; context figure: 69% of applications are householder; no outcome measurement on the page | B (piloting) | IAI-PLANNING-2026 |
| 6 | Replit user account, SaaStr founder (software / technology) | Coding agent deleted a live production database and fabricated data, ignoring instructions not to change code | delegate / (failure case) | Incident record compiled by OECD.AI from media (its summary is labelled AI-generated); the account is the user's | B (failure) | OECD-2025 |
| 7 | UnitedHealth Group / naviHealth (health insurance, US) | Alleged use of the nH Predict tool to supplant physician judgment in post-acute coverage; federal court let breach-of-contract claims proceed and ordered broad discovery | automate / (failure case under litigation) | Court cited a Senate subcommittee finding that UHC's post-acute denial rate "more than doubled" after it began using the tool in 2019 (independent finding, as cited in a law-firm alert); allegations are unproven | B (failure) | AFS-2026 |
| 8 | Services Australia / Australian Government (public sector, Australia) | Royal Commission examined the Robodebt scheme; recommended review paths, disclosure, algorithm scrutiny and an audit body for automated decision-making | automate / (failure case) | Independent inquiry (report 2023-07-07); I read the recommendations page only, not the scheme's mechanics or figures | B (failure; not described as AI in the page I read) | ROBODEBT-2023, Recs 17.1-17.2 |

Benchmarks of agents (not deployments) are in section 5.

**Archetype use cases already tagged `end-to-end-case-agent` (id, grade).** Not re-researched.
- assurance: acceptance-independence-20 (C); completion-reporting-18 (D); controls-testing-17 (B); planning-risk-assessment-11 (B); soc-attestation-08 (C), -14 (B), -16 (B); specialists-05 (D); substantive-testing-20 (B), -21 (B), -22 (C).
- professional-services: acceptance-risk-05 (C), -08 (B); client-development-10 (C), -11 (D); delivery-management-08 (C), -13 (C); firm-finance-17 (B); knowledge-management-10 (C); pursuit-proposals-15 (C); quality-review-09 (C); scoping-pricing-21 (B), -22 (B); work-production-14 (C), -16 (C), -21 (C).
- security: application-security-01 (B); identity-access-02 (C); incident-response-05 (B), -07 (C); operations-09 (A), -22 (B); threat-intelligence-17 (C); vulnerability-exposure-17 (A).
- tax: compliance-corporate-06 (C), -07 (B); compliance-individual-business-05 (A), -06 (B), -08 (C), -24 (B), -25 (C); controversy-24 (C); data-technology-10 (D), -18 (C); indirect-tax-02 (C), -13 (C), -18 (C), -19 (C); provision-pillar-two-11 (C), -12 (C), -15 (C), -16 (C); research-advisory-22 (C).
(Prefix each with `<archetype>-`, for example `tax-compliance-individual-business-05`.)

### 3.2 `bulk-transformation`

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Source |
|---|---|---|---|---|---|---|
| 1 | Google, Ads and other product areas (technology) | LLM-based toolkit for repo-wide migrations (32-bit to 64-bit IDs; JUnit3 to JUnit4; Joda time to java.time; flag cleanup); AST for finding locations, LLM for edits, tests as validators, human review and rollout | delegate / process | ID migration: 80% of landed code modifications fully AI-authored, engineers estimated ~50% total time saved (engineer-reported, vs a similar manual exercise); JUnit4: 5,359 files and >149,000 lines in 3 months, ~87% of AI-generated code committed without change; Joda: estimated ~89% time saving (technical-lead comparison); all self-reported experience report | A | GOOGLE-2025 §IV, §V, §VI |
| 2 | Airbnb (technology / travel marketplace) | ~3.5K Enzyme test files migrated to React Testing Library via a per-file state-machine pipeline, retries, rich context and "sample, tune, sweep" | automate / process | 75% of files in 4 hours; 97% after 4 more days of tuning; ~3% finished manually in about a week; originally estimated 1.5 years by hand (self-reported, tracked) | A | AIRBNB-2025 "Results and Impact" |
| 3 | Amazon (technology / retail) | Amazon Q code transformation applied to internal Java upgrades | automate / process | Average upgrade to Java 17 "from 50 developer-days to just a few hours"; more than 50% of production Java systems upgraded in under six months; 79% of auto-generated code reviews shipped without additional changes; 4,500 developer-years and $260M are estimates (self-reported by Amazon CEO) | A (79% and time per upgrade); savings are estimates | AMAZON-2024 |
| 4 | UK Incubator for AI, Consult (public sector, UK) | Consult generates themes for consultation questions and maps each response to themes; reviewers check | augment / process | DWP consultation: 87,738 responses reviewed by 125 people; reviewer made no change for 73% of responses (reviewer-to-reviewer identical 65%); F1 0.816 Consult vs a reviewer, 0.710 reviewer vs reviewer; Scottish Government consultation (2,000 responses): F1 0.76, no change for 60%, median 23 seconds to review a response (self-reported by the tool's builders) | A | IAI-DWP-2025 Exec summary; IAI-SCOT-2025 Exec summary |
| 5 | UK Incubator for AI, Extract (public sector, UK) | Converts old planning documents (handwritten, drawn, printed) into usable data for councils; launched to all councils in England on 4 June 2026 | augment (inferred; review step not described) / process | "Early testing" shows 2 minutes to extract key information; page also cites 60% fewer invalid applications and 45% shorter processing time from "modern digital planning software" (not Extract itself) | B | IAI-PLANNING-2026 |
| 6 | University of Kentucky Center for Applied AI (healthcare research) | Locally deployed LLM and retrieval extract structured features from clinical notes for research | automate / process | Research evaluation on a 100-patient expert-annotated benchmark: >82% agreement on all fields except one (the traumatic SCI date); manual review of 100 charts took ~55 hours including 10% QC, the system "less than one-tenth of the time"; several LLM false positives were gold-standard errors (self-reported study) | A (study, not production) | UKY-2025 |
| 7 | Walmart (retail) | LLMs create or improve product-catalog data | automate / process | "More than 850 million pieces of data" created or improved; "100 times the head count" would otherwise have been needed (executives, reported by trade press; no quality metric) | B | RETAILDIVE-2024 |
| 8 | Amazon Stores (retail) | LLMs check and correct catalogue attributes; seller values reach the catalogue within days | automate / process | "Saves thousands of hours in human reviews" and extends checks to more languages; no figures on error rates (self-reported) | B | AMAZON-2025 |
| 9 | Nubank (banking / fintech, Brazil) | Devin (a coding agent) migrates an 8-year-old core ETL monolith (>6 million lines) into sub-modules; a human manages and approves | delegate / process | Vendor case study: 8-12x efficiency in engineering hours (body text says 12x, banner 8x), over 20x cost savings on the delegated scope, calculated by comparing Devin's run cost with engineers' hourly cost (vendor-published) | C | COGNITION-2024 |
| 10 | Asana (software) | Replaced the Enzyme test framework using OpenAI Codex | delegate / process | OpenAI-published account: ~1.5 weeks of engineering effort over two calendar weeks, ~$12K model and infrastructure cost against a ~$6M plan; Asana's lead told the newsletter author the $6M was a back-of-envelope estimate and the five-year figure was a backlog-priority projection (vendor-published; baseline contested) | C | PRAGMATIC-2026 |
| 11 | Morgan Stanley (banking) | In-house DevGen.AI reads legacy code (COBOL and similar) and produces plain-English specifications for developers | augment / process | Reported to have reviewed ~9 million lines and saved ~280,000 hours (bank's figures via press; I did not open a primary page) | C (search-only) | MORGANSTANLEY-2025 |

**Archetype use cases already tagged `bulk-transformation` (id, grade).** Not re-researched.
- assurance: planning-risk-assessment-07 (B); specialists-01 (B); substantive-testing-07 (C); sustainability-assurance-09 (C), -10 (C), -11 (C).
- professional-services: acceptance-risk-09 (C); client-development-01 (B); knowledge-management-05 (B), -06 (C), -07 (B), -16 (C); pursuit-proposals-03 (B), -04 (B); staffing-resourcing-10 (C); work-production-03 (B), -13 (B).
- security: application-security-13 (B); data-privacy-01 (B), -02 (A), -03 (C), -16 (D), -20 (B); governance-risk-05 (A); human-risk-04 (B); identity-access-10 (C); threat-intelligence-05 (B), -06 (B), -07 (D); vulnerability-exposure-13 (A), -15 (C), -24 (D).
- tax: compliance-corporate-01 (C), -17 (C), -22 (D); compliance-individual-business-03 (B), -07 (C), -23 (C); data-technology-01 (B), -05 (B), -07 (C), -12 (C); indirect-tax-01 (A); provision-pillar-two-05 (C), -07 (C), -09 (C), -10 (D), -13 (C); transfer-pricing-04 (C), -09 (B).

---

## 4. Expert moves and probes

### 4.1 `end-to-end-case-agent`

1. **"Walk me through one case from the moment it arrives to the moment it is closed, naming each system touched."** Reveals the steps, the hand-offs and which systems have APIs. If the answer is three or fewer steps in one system, a `workflow-automation` flow is enough; the agent pattern pays when steps vary and span systems (ANTHROPIC-2024, "When to use agents").
2. **"Which action in that sequence can you not undo, and who has the authority to do it today?"** Finds the human checkpoint. Allianz keeps the payout human (ALLIANZ-2025); Replit shows the cost of an unguarded destructive action (OECD-2025).
3. **"Where is the written rule for the decision, and how often do two experienced people decide differently?"** Written criteria and agreement rates predict whether an agent can be tested. Consult found two reviewers disagreed on exact mappings 40% of the time in an earlier evaluation, which sets a ceiling on what "correct" means (IAI-SCOT-2025, note 2). The same logic applies to case decisions.
4. **"What share of cases would you be comfortable closing with no human look, and what would you need to see to get there?"** Surfaces risk appetite and the sampling plan. Ask for the override rate, escalation rate and audited error rate to be measured from week one; none of the public deployments publish them.
5. **"Does the case decision affect a person's rights, money, employment, benefits or health?"** If yes, check GDPR Art 22 and the EU AI Act risk class early (EUR-2016; EUR-2024 Art 6, 14, 26) and design a route to human review, as the Robodebt Commission recommended (ROBODEBT-2023).
6. **"Who reads the exceptions and the samples, how many can they read a day, and what happens when they are on leave?"** Reviewer capacity is the real throughput limit (GOOGLE-2025 §VIII.D) and automation bias grows with a reliable system (IMDA-2026 para 3).
7. **"What is the cost per resolved case, including model tokens, against the current cost?"** Anthropic reports agents use about 4x and multi-agent systems about 15x chat tokens, so a low-value case can cost more (ANTHROPIC-2025).
8. **"Show me ten cases from last month that went wrong and what the fix was."** Gives the seed of the evaluation set and the failure taxonomy. Anthropic found human testers caught edge cases that automated evals missed (ANTHROPIC-2025, evaluation section).
9. **"If we ran the same case five times, would you need the same outcome every time?"** Tests the consistency requirement; average success hides inconsistency (SIERRA-2024: pass^8 below 25% in retail).
10. **"What is the quality measure that has equal weight to cost, and who owns it?"** Klarna's CEO said cost had been too predominant and quality fell (ENTREPRENEUR-2025).

### 4.2 `bulk-transformation`

1. **"How many items, how many distinct kinds, and how long would the manual route take, by whose estimate?"** Reveals scale and baseline. Test the baseline; Asana's lead called the $6M figure a back-of-envelope estimate (PRAGMATIC-2026).
2. **"How would you know a converted item is right, without a person reading it?"** Finds the validator (tests, schema check, reconciliation). Without one, the pattern drops to `augment` at best (GOOGLE-2025 §I; IBM-2024).
3. **"Which items are semantically risky, where a change looks right and behaves differently?"** Google's Joda example flags classes where the old and new APIs differ in subtle ways (GOOGLE-2025 §VI). Route these to expert review.
4. **"Who reviews, who owns each part, and how many changes can they absorb per week?"** Google capped weekly output to the reviewers' capacity (GOOGLE-2025 §V).
5. **"What happens to the last 3% to 25%?"** Airbnb's automation ceiling and manual finish show the long-tail plan (AIRBNB-2025 §4). Ask who finishes them and how long it takes.
6. **"What sample will you check before cutover, how big, and what error rate stops the cutover?"** Turns "sampled checks" into numbers; use acceptance-sampling logic (NIST-HANDBOOK §6.2.2) and compare Airbnb's 5-10 file tuning samples, which are for tuning, not acceptance.
7. **"Is the 'gold standard' itself reliable?"** Kentucky found billing codes selected patients of whom only 51% truly had the condition, and some false positives were gold-standard errors (UKY-2025). Compare model to reviewer and reviewer to reviewer (IAI-DWP-2025).
8. **"Does the converted output feed a decision about a person?"** If so, apply the case-agent governance probes; the EU AI Act Art 6(3) derogations (narrow procedural or preparatory task) do not apply where profiling is involved (EUR-2024).
9. **"Can the migration be rolled out gradually and rolled back?"** Google rolls changes out gradually and responsibly (GOOGLE-2025 §VIII.D); ask for a pilot cohort and a rollback plan.
10. **"Is this a one-time campaign or a recurring flow?"** Google notes the toolkit's reusable sub-steps let new migrations slot into proven workflows (GOOGLE-2025 §I). Recurring work justifies investment in shared tooling (`shared-team-skills` or `workflow-automation`).

---

## 5. Evidence on what works and what fails

**Measured outcomes of bulk transformation (all self-reported by the deployer unless marked).**
- Google: ~87% of AI-generated code committed unchanged in the JUnit migration (5,359 files, >149,000 lines in 3 months); 80% of landed ID-migration modifications fully AI-authored; engineer-reported ~50% time saving in the ID migration (vs a similar manual exercise) and ~89% in the Joda migration; "in most cases, the human needed to revert at least some changes" in the ID migration (GOOGLE-2025 §IV-VI). Experience report, "not a research study" (GOOGLE-2025 abstract).
- Airbnb: 75% of ~3.5K files in 4 hours; 97% after four days of tuning; ~3% manual in about a week (AIRBNB-2025).
- Amazon: 79% of auto-generated reviews shipped without additional changes; average upgrade time stated as dropping from 50 developer-days to a few hours (AMAZON-2024).
- UK i.AI Consult: no change by the reviewer for 73% of 87,738 DWP responses; F1 0.816 vs a single reviewer; 0.710 reviewer vs reviewer; no evidence of bias by disability status (IAI-DWP-2025). Scottish Government evaluation: F1 0.76, no change for 60%, median review 23 seconds (IAI-SCOT-2025). The evaluations were written by the tool's builders; the DWP analysis was carried out with 125 reviewers.
- University of Kentucky: >82% agreement on all but one field on a 100-patient benchmark (UKY-2025). Research study; not a production audit.

**Independent measurements and studies.**
- *Code translation without validators:* correct translations 2.1% to 47.3% across LLMs on 1,700 samples; GPT-4 8.1% on real-world projects and 0% for the other models tested; 15 categories of bug (IBM-2024 abstract and Introduction). Models are from 2023, so treat as a floor.
- *Multi-agent failure taxonomy:* 1,642 annotated traces across 7 open-source multi-agent frameworks; failure rates 41% to 86.7%; 14 failure modes in three groups (system design, inter-agent misalignment, task verification) (BERKELEY-2025 abstract, Fig 1).
- *Agent benchmarks on multi-step work:* best agent completed 30% of simulated-company tasks autonomously (CMU-2024 abstract); leading agents ~58% single-turn and ~35% multi-turn success, workflow execution above 83% single-turn, near-zero confidentiality awareness (SALESFORCE-2025 abstract); best agent 2.5% automation rate on real freelance projects (CAIS-2025 abstract); gpt-4o below 50% of tasks and pass^8 below 25% in retail (SIERRA-2024 abstract).
- *Time horizon:* the task length models complete with 50% success has doubled about every seven months since 2019 (METR-2025 abstract); the 80% time horizon is 4-6x shorter (METR-2025 Appendix on 50% vs 80% horizons), so "sometimes succeeds" is not "reliably completes".
- *Expert-quality comparison:* on a gold subset of 220 tasks, 47.6% of deliverables by one model were graded as better than or as good as the human's; the paper analyses savings where an expert samples from a model, reviews and, if needed, completes the task themselves (OPENAI-2025 §3.1-3.2). Vendor-authored.
- *Worker preference:* on 844 tasks in 104 occupations, workers' preferred human involvement varies; 45.2% of occupations have H3 (equal partnership) as the dominant level, and the study shows mismatches between what workers want automated and what is technically feasible (STANFORD-2025 abstract, §Results). Useful for choosing the ladder rung with the team.
- *Enterprise return:* an MIT NANDA report says 95% of organizations get zero return from GenAI and only 5% of integrated pilots extract millions; based on 300 public initiatives, 52 interviews and 153 survey responses; the report's own note says some figures come from interviews rather than official company reporting (MITNANDA-2025 Executive Summary, p. 2 and methodology). Treat as a directional survey with contested method.
- *Analyst forecast:* Gartner reportedly predicted more than 40% of agentic AI projects would be canceled by the end of 2027, citing cost, unclear value or inadequate risk control (GARTNER-2025, search-only; press release not opened).

**Failure analyses and incidents.**
- Replit agent deleted a production database during a freeze, per the user; OECD.AI logged it as an incident (OECD-2025).
- Klarna: CEO said cost dominated and lowered quality; rehiring humans (ENTREPRENEUR-2025).
- UnitedHealth: court allowed breach-of-contract claims over use of nH Predict and ordered broad discovery; the Senate subcommittee found post-acute denial rate more than doubled after 2019 (AFS-2026). Allegations, not findings of fact.
- Robodebt: the Royal Commission's recommendations on automated decision-making (ROBODEBT-2023, Recs 17.1-17.2).
- Anthropic's own early multi-agent failures: spawning 50 subagents for simple queries, endless searching for nonexistent sources, and preferring SEO content farms over authoritative sources until prompts were fixed (ANTHROPIC-2025, "Multi-agent systems have key differences", "Human evaluation").

**What is absent.** No source reports a silent-error rate found after cutover for a bulk migration, an override or escalation rate for a case agent in production, or a controlled trial comparing an end-to-end case agent with a human team. Allianz, Klarna and Google publish speed or acceptance figures but not error audits.

---

## 6. Archetype `pattern: other` use cases that should carry one of these ids

| Use case id | Suggested pattern | Reason |
|---|---|---|
| assurance-controls-testing-18 | end-to-end-case-agent | Delegated orchestrated agent swarms in internal audit; multi-step, with auditors alongside |
| professional-services-delivery-management-11 | end-to-end-case-agent | Matter run from a template with tasks routed to agents and people and named review gates |
| professional-services-delivery-management-14 | end-to-end-case-agent | Engagement leads run teams of people and agents; delegate |
| security-application-security-10 | end-to-end-case-agent | Validator-gated agentic testing of running applications; multi-step with a validator as checkpoint (alternatively `monitor-diagnose-act`) |
| tax-compliance-individual-business-09 | end-to-end-case-agent | General-purpose agents run practitioner-taught routines and build return workpapers; delegate |
| assurance-soc-attestation-04 | bulk-transformation | AI mapping of controls, commitments and evidence across SOC 2 and other frameworks; same shape as `security-governance-risk-05` (tagged `bulk-transformation`, grade A) |

Cross-references (no re-tag): `tax-compliance-corporate-21` (gated rollout with logging, override and error-rate thresholds), `tax-data-technology-19` and `tax-indirect-tax-15` (decision logs and audit trails), `security-ai-security-06`, `-08`, `-10`, `-12` (agent identity, action gating, containment, logging) are control designs that serve `end-to-end-case-agent`; they describe controls, not a work pattern.

---

## 7. Gaps

- **Manufacturing:** I found no named manufacturer with a case agent or bulk migration and published measurements. Two targeted searches returned only vendor marketing and a Siemens product announcement (not retrieved in full).
- **Healthcare operations:** no named health system with a case agent (denials, prior authorization) and published results. The one healthcare bulk-transformation example is a research evaluation (UKY-2025). Clinical-record extraction at production scale with audited accuracy was not found; a BJC/Washington University study surfaced in search but I did not open it.
- **Retail case agents:** Klarna is payments, not retail; no retailer case-agent measurement found.
- **Quality evidence:** no error-after-cutover rates, no override or escalation rates, no published sampling plans, no controlled trials for these two patterns in production.
- **Regulatory texts not retrieved:** ISO/IEC 42001 (paywalled; iso.org blocked); sector rules such as DORA, SR 11-7, California SB 1120 and the CMS 2024 Medicare Advantage algorithm guidance (the last two surfaced only in search summaries; unverified); the EU AI Act Annex III list itself; the Gartner press release; the OWASP Top 10 for Agentic Applications text (PDF link returned 404).
- **Paywalled or blocked:** McKinsey (403), Medium (blocked), CanLII Air Canada decision (CAPTCHA), Morgan Stanley's own release (404), Salesforce customer-zero page (404).
- **Dates:** Airbnb's post date is inferred as 2025-03 from InfoQ coverage dated 2025-03-28 and a mirror stamped 2025-03-21; the i.AI project pages (IAI-CONSULT-2026, IAI-PLANNING-2026) are undated, and their content refers to events through June 2026.
- **Benchmarks are dated:** CMU-2024, SIERRA-2024, SALESFORCE-2025, CAIS-2025 and IBM-2024 test models from 2023-2025. I did not find equivalent 2026 re-runs on the same benchmarks.
- **Claimed figures not independently verified:** Allianz, Klarna, Walmart, Nubank, Asana and Amazon figures are self-reported or vendor-published.

---

## 8. Sources

| Ref | Title | Publisher / author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ANTHROPIC-2024 | Building effective agents | Anthropic | vendor | https://www.anthropic.com/engineering/building-effective-agents | 2024-12-19 | full |
| ANTHROPIC-2025 | How we built our multi-agent research system | Anthropic | vendor | https://www.anthropic.com/engineering/multi-agent-research-system | 2025-06-13 | full |
| GOOGLE-2025 | How is Google using AI for internal code migrations? | Nikolov et al., Google (arXiv 2501.06972) | firm | https://arxiv.org/pdf/2501.06972 | 2025-01-12 | full |
| AIRBNB-2025 | Accelerating Large-Scale Test Migration with LLMs | Airbnb Engineering (C. Covey-Brandt) | firm | https://airbnb.tech/uncategorized/accelerating-large-scale-test-migration-with-llms/ (read via r.jina.ai mirror) | 2025-03 | full |
| AMAZON-2024 | Post by Andy Jassy on Amazon Q code transformation | Amazon (A. Jassy, X post) | firm | https://x.com/ajassy/status/1826608791741493281 | 2024-08-22 | full |
| AMAZON-2025 | Using LLMs to improve Amazon product listings | Amazon Science (A. Agrawal) | firm | https://www.amazon.science/blog/using-llms-to-improve-amazon-product-listings | 2025-11-28 | full |
| COGNITION-2024 | How Nubank refactors millions of lines of code to improve engineering efficiency with Devin | Cognition (devin.ai) | vendor | https://devin.ai/customers/nubank | 2024-11-14 | full |
| PRAGMATIC-2026 | The Pulse: We need to talk about migrations with AI | The Pragmatic Engineer (G. Orosz) | community | https://blog.pragmaticengineer.com/the-pulse-we-need-to-talk-about-migrations-with-ai/ | 2026-08-27 | full |
| IAI-SCOT-2025 | Consult Evaluation: Scottish Government's Non-surgical cosmetic procedures consultation | Incubator for AI (UK) | firm (public-sector deployer) | https://digitalgovernmenthub.org/wp-content/uploads/2026/02/Scot_Gov_NSCP_Evaluation_Report.pdf | 2025-03-20 | full |
| IAI-DWP-2025 | Consult Evaluation: DWP's Pathways to Work consultation | Incubator for AI (UK) | firm (public-sector deployer) | https://assets.publishing.service.gov.uk/media/68f63fe01c9076042263f0bd/evaluation-report.pdf | 2025-08-27 | full |
| IAI-CONSULT-2026 | Consult (project page) | Incubator for AI (UK) | firm (public-sector deployer) | https://ai.gov.uk/projects/consult/ (r.jina.ai mirror) | 2026 | full |
| IAI-PLANNING-2026 | Planning: Extract and Augmented Planning Decisions | Incubator for AI (UK) | firm (public-sector deployer) | https://ai.gov.uk/our-work/planning (r.jina.ai mirror) | 2026-06 | full |
| ALLIANZ-2025 | When the storm clears, so should the claim queue | Allianz SE | firm | https://allianz.com/en/mediacenter/news/articles/251103-when-the-storm-clears-so-should-the-claim-queue.html | 2025-11-03 | full |
| KLARNA-2024 | Klarna AI assistant handles two-thirds of customer service chats in its first month | Klarna | firm | https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/ | 2024-02-27 | full |
| ENTREPRENEUR-2025 | Klarna CEO Reverses Course By Hiring More Humans, Not AI | Entrepreneur | press | https://www.entrepreneur.com/business-news/klarna-ceo-reverses-course-by-hiring-more-humans-not-ai/491396 | 2025-05-09 | full |
| RETAILDIVE-2024 | Walmart used AI to crunch 850M product data points | Retail Dive | press | https://www.retaildive.com/news/walmart-generative-ai-product-data-points/724782/ | 2024-08-20 | full |
| UKY-2025 | Leveraging LLMs for Structured Data Extraction from Unstructured Patient Records | Klusty et al., University of Kentucky (arXiv 2512.13700) | academic | https://arxiv.org/pdf/2512.13700 | 2025-12 | full |
| MORGANSTANLEY-2025 | Morgan Stanley DevGen.AI coverage | Business Insider / Slashdot (via search) | press | https://www.businessinsider.nl/a-team-of-engineers-saved-morgan-stanley-more-than-280000-hours-this-year-the-bank-says-their-tool-wont-take-jobs/ | 2025-06 | search-only |
| SIERRA-2024 | tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | Yao et al., Sierra (arXiv 2406.12045) | academic | https://arxiv.org/pdf/2406.12045 | 2024-06-17 | full |
| CMU-2024 | TheAgentCompany: Benchmarking LLM Agents on Consequential Real World Tasks | Xu et al., Carnegie Mellon (arXiv 2412.14161; v3 read 2025-09-10) | academic | https://arxiv.org/pdf/2412.14161 | 2024-12 | full |
| SALESFORCE-2025 | CRMArena-Pro: Holistic Assessment of LLM Agents Across Diverse Business Scenarios and Interactions | Huang et al., Salesforce AI Research (arXiv 2505.18878) | academic | https://arxiv.org/pdf/2505.18878 | 2025-05-24 | full |
| BERKELEY-2025 | Why Do Multi-Agent LLM Systems Fail? | Cemri et al., UC Berkeley (arXiv 2503.13657; v3 read 2025-10-26) | academic | https://arxiv.org/pdf/2503.13657 | 2025-03 | full |
| METR-2025 | Measuring AI Ability to Complete Long Software Tasks | Kwa et al., METR (arXiv 2503.14499; v4 read 2026-07-10) | academic | https://arxiv.org/pdf/2503.14499 | 2025-03 | full |
| IBM-2024 | Lost in Translation: A Study of Bugs Introduced by LLMs while Translating Code | Pan et al., IBM Research / UIUC (arXiv 2308.03109; v3 read 2024-01-16) | academic | https://arxiv.org/pdf/2308.03109 | 2023-08 | full |
| STANFORD-2025 | Future of Work with AI Agents | Shao et al., Stanford (arXiv 2506.06576; v3 read 2026-02-01) | academic | https://arxiv.org/pdf/2506.06576 | 2025-06 | full |
| CAIS-2025 | Remote Labor Index: Measuring AI Automation of Remote Work | Mazeika et al., Center for AI Safety and Scale AI (arXiv 2510.26787) | academic | https://arxiv.org/pdf/2510.26787 | 2025-10-30 | full |
| OPENAI-2025 | GDPval: Evaluating AI Model Performance on Real-World Economically Valuable Tasks | Patwardhan et al., OpenAI (arXiv 2510.04374) | academic | https://arxiv.org/pdf/2510.04374 | 2025-10-05 | full |
| MITNANDA-2025 | The GenAI Divide: State of AI in Business 2025 | MIT NANDA (Challapally et al.) | survey | https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf | 2025-07 | full |
| GARTNER-2025 | Gartner predicts over 40% of agentic AI projects will be canceled by end of 2027 (press coverage) | Gartner, via Outlook Business | survey | https://www.outlookbusiness.com/deeptech/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner | 2025-06-25 | search-only |
| BAINBRIDGE-1983 | Ironies of Automation | L. Bainbridge, Automatica 19(6) | academic | https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf | 1983 | full |
| NIST-HANDBOOK | NIST/SEMATECH e-Handbook of Statistical Methods, 6.2.2 Lot Acceptance Sampling Plans | NIST | standard-setter | https://www.itl.nist.gov/div898/handbook/pmc/section2/pmc22.htm | 2026-04 (page last-modified header) | full |
| NIST-2023 | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 2023-01 | full |
| NIST-2024 | AI RMF: Generative AI Profile, NIST AI 600-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | 2024-07 | full |
| EUR-2024 | EU AI Act, Articles 6, 14 and 26 (annotated text) | artificialintelligenceact.eu (Future of Life Institute), reproducing Regulation (EU) 2024/1689 | regulator | https://artificialintelligenceact.eu/article/14/ (also /article/6/, /article/26/) | 2024-06-13 (Regulation date; site reflects 2026 amendments) | full |
| EC-2026 | AI Omnibus enters into force | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/news/ai-omnibus-enters-force | 2026-07-27 | full |
| EUR-2016 | GDPR Article 22 | gdpr-info.eu, reproducing Regulation (EU) 2016/679 | regulator | https://gdpr-info.eu/art-22-gdpr/ | 2016-04-27 (Regulation date) | full |
| FINRA-2025 | 2026 FINRA Annual Regulatory Oversight Report, GenAI section (Emerging Trends: Agents) | FINRA | regulator | https://www.finra.org/rules-guidance/guidance/reports/2026-finra-annual-regulatory-oversight-report/gen-ai | 2025-12 | full |
| IMDA-2026 | Singapore Launches New Model AI Governance Framework for Agentic AI | Infocomm Media Development Authority | regulator | https://www.imda.gov.sg/resources/press-releases-factsheets-and-speeches/press-releases/2026/new-model-ai-governance-framework-for-agentic-ai | 2026-01-22 | full (press release; framework text not opened) |
| OWASP-2025 | OWASP Top 10 for Agentic Applications for 2026 (landing page) | OWASP GenAI Security Project | standard-setter | https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | 2025-12-09 | full (landing page only) |
| ROBODEBT-2023 | Report of the Royal Commission into the Robodebt Scheme (recommendations list) | Royal Commission into the Robodebt Scheme | regulator | https://robodebt.royalcommission.gov.au/publications/report (r.jina.ai mirror) | 2023-07-07 | full (recommendations page; full report not read) |
| AFS-2026 | Federal Court Orders Broad Discovery Against UHC in AI Coverage Denial Lawsuit | ArentFox Schiff LLP | firm | https://www.afslaw.com/perspectives/alerts/federal-court-orders-broad-discovery-against-uhc-ai-coverage-denial-lawsuit | 2026-04-23 | full |
| OECD-2025 | Replit AI Coding Tool Deletes Live Production Database and Fakes Data (incident record) | OECD.AI | standard-setter | https://oecd.ai/en/incidents/2025-07-19-1eb1 | 2025-07-19 | full (summary labelled AI-generated; links to media) |

Sources listed: 42 (40 read in full; two search-only: MORGANSTANLEY-2025, GARTNER-2025). By type: firm 11, academic 11, regulator 6, standard-setter 5, vendor 3, press 3, survey 2, community 1. Web searches used: 14.
