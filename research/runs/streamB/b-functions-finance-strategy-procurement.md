# Function cards research: finance-accounting, strategy-planning, procurement-supply-chain

Research date: 2026-10-20. Stream B, shared backbone library. Items: `finance-accounting`, `strategy-planning`, `procurement-supply-chain`.
Scope: in-house functions in any organization. Archetype use cases are cited by id and grade only (section 3); they are not re-researched.
Source refs use `PUBLISHER-SHORT-YYYY`; full list in section 7. Grades follow the vocabulary (A = a figure the named organization reports as measured; B = named deployment without published measurement; C = vendor claim or analyst estimate; D = idea). Two conventions used here: (1) a measurement from an adjacent process is capped at B and says so; (2) a randomized or lab experiment with no deployment is graded D and labelled "idea (experiment only)", because the vocabulary has no grade for it.

## 1. Summary

- Adoption is broad but shallow. Gartner's 2025 finance survey (183 CFOs and senior finance leaders) reports 59% of finance functions using AI, up from 58% in 2024 and 37% in 2023, and 91% of respondents reporting low or moderate impact initially (GARTNER-2025). Gartner's 2026 procurement survey (101 CPOs) reports only 36% very confident they can redesign roles and processes around AI, and describes individual gains that fade at team level (GARTNER-2026). McKinsey's 2026 survey reports 37% of respondents seeing positive EBIT contribution and 6% as AI high performers (MCKINSEY-2026).
- The best measured in-house evidence is narrow and step-level: Microsoft finance reconciliation (minutes saved per account), US Treasury payment-integrity machine learning (dollars recovered), Walmart and UPS routing optimization (dollars and miles). All are self-reported by the deploying organization; none is a controlled trial. Two of the three are not generative AI (Walmart and UPS use optimization).
- For finance there is one independent field dataset: 79 small and mid-sized firms using AI accounting tools (Choi and Xie, via STANFORD-2025): month-end close 7.5 days faster, 8.5% less time on routine back-office work. Junior staff accepted AI outputs flagged as uncertain more often than seniors did. This is bookkeeping services, not in-house finance, so it is graded B.
- The strongest quality evidence is a parallel run: one unnamed mega-cap treasury ran legacy and machine-learning cash forecasts side by side for about seven months, then ran "reverse parallel" for three months before switching (NEUGROUP-2025). Almost no other source publishes parallel-run, error, override or escalation rates. COSO's 2026 guidance names override percentages as a monitoring indicator (DELOITTE-DART-2026) but publishes no benchmark.
- Strategy-planning has the thinnest deployment evidence. The measured items are consultation analysis in a government (F1 0.76 against a human reviewer, 60% of responses unchanged by reviewers: IAI-2025) and experiments (LLM-written business plans rated 0.14 SD higher by investors: CSASZAR-2024; consultants 19% less likely to be correct on a task outside the AI frontier: HBS-2023). No named corporate strategy team with a measured outcome was found.
- Procurement's one widely cited AI-agent case is Walmart and Pactum negotiating with tail suppliers: figures (68% of negotiations closed, 3% average savings) are vendor-published and reported second-hand (PYMNTS-2023). Experiments show a competitive-prompted buyer chatbot gets better price and payment terms but is trusted less by suppliers (HEROLD-2025), and LLM agents bargain more concessionarily than humans (QIAN-2025).
- Payment authorization is the sharpest guardrail across finance and procurement: the FBI recorded $2.77 billion in business email compromise losses in 2024 (FBI-2025), and Arup confirmed a $25 million deepfake video-call fraud on a finance worker (CNN-2024).
- The common design lesson across the three functions: per-task speed-ups do not shorten an end-to-end process unless the handoffs and roles are redesigned (GARTNER-2026; KOGNITOS-2026, a vendor argument; MCKINSEY-2026 says high performers redesign workflows, nearly three-quarters versus about one-quarter of others).

## 2. Item profiles

### 2.1 finance-accounting

**Scope.** The in-house finance function of any organization. Firms that sell accounting, audit or tax services are covered by other archetypes.

**Main processes and key steps (with work types).** The process names below are the author's plain-language grouping of what an in-house finance function runs; APQC describes its Process Classification Framework as a taxonomy of the processes performed in an organization, with key measures per process (APQC-2026, page text). The category files themselves were not read (see Gaps).

| Process | Key steps | Work types |
|---|---|---|
| Procure-to-pay (accounts payable) | Invoice capture and coding; matching to order and receipt; approval; exception handling; payment run | `transaction-processing`, `review-assurance` |
| Order-to-cash (receivables, collections) | Billing; cash application; dispute handling; collections follow-up | `transaction-processing`, `client-interaction` |
| Record-to-report (close and reporting) | Journal entries and accruals; reconciliations; intercompany; consolidation; flux and variance review; disclosures | `data-reporting`, `review-assurance`, `document-production` |
| Planning, budgeting and forecasting (FP&A) | Driver models; rolling forecasts; variance commentary; scenario runs | `data-reporting`, `expert-judgment` |
| Treasury | Cash positioning and forecasting; FX exposure and hedging; payments | `data-reporting`, `coordination-scheduling`, `transaction-processing` |
| Controls, audit support and payments integrity | Control testing; segregation of duties; payment authorization and verification; fraud screening | `review-assurance`, `transaction-processing` |
| Tax and statutory reporting inside the company | Provision, returns, local filings | Routed to the tax archetype |

Sources for the grouping: author's synthesis; the AI use cases that the Gartner survey names (knowledge management, accounts payable automation, error and anomaly detection) map to rows 1, 3 and 6 (GARTNER-2025, use-case paragraph).

**Typical pain points.**
- Close cycle time driven by waiting and handoffs, not working time. KOGNITOS-2026 (vendor blog) says task-level AI gains did not shorten the close and attributes the days to handoffs; it cites an APQC median of "roughly 6.4 calendar days" for trial balance to consolidated statements, which was not checked against APQC.
- Manual reconciliation across systems and spreadsheets (CFODIVE-2024: reconciliation was a top Microsoft use case).
- Legacy forecast processes that depend on many people submitting numbers: about 180 forecasters submitting monthly, described as "extremely painful and inaccurate" by the treasury lead (NEUGROUP-2025).
- Data quality and skills: data literacy/technical skills and data quality/availability are the largest adoption obstacles (GARTNER-2025, "Challenges Remain" section).
- Verification burden after AI: Datarails' survey (270 US finance leaders, vendor) reports an average 26% of work time verifying or correcting AI outputs (DATARAILS-2026).
- Payment fraud and impersonation (FBI-2025; CNN-2024).

**Top AI opportunities (ladder, scope, pattern, best evidence).**

| Opportunity | Ladder | Scope | Pattern | Best evidence and grade |
|---|---|---|---|---|
| Policy, standards and procedure Q&A for finance staff | assist | step | `grounded-knowledge-assistant` | Knowledge management is the most common finance AI use case among adopters, 49% (survey; GARTNER-2025). No measured named deployment found in this run. Grade C. |
| Reconciliation of data across sources and working the breaks | augment | step | `reconcile-exceptions` | Microsoft: average 20 minutes saved per account (AR reconciliation); an FP&A team's weekly reconciliation from 1-2 hours to 10 minutes (CFODIVE-2024). Grade A (self-reported, method unpublished). |
| Variance analysis and commentary | augment | step | `draft-review-loop` | Microsoft finance "testing" with "promising results so far" (CFODIVE-2024). Grade B. |
| Transaction classification and close acceleration | augment | process | `bulk-transformation` | Independent platform data, 79 small and mid-sized firms: close 7.5 days faster, 8.5% less time on routine work (STANFORD-2025). Grade B (adjacent). |
| Accounts payable automation, anomaly and error detection | automate | process | `full-population-testing`, `intake-triage` | Adopted by 37% and 34% of adopters in Gartner's survey (GARTNER-2025); named measured cases are in archetype entries (section 3). Grade C here. |
| Payment-integrity screening | automate | step | `monitor-diagnose-act` | US Treasury: machine learning to identify check fraud tied to $1 billion recovery in FY2024 (TREASURY-2024). Grade A. |
| Cash and FX forecasting | automate | process | `monitor-diagnose-act` | Unnamed mega-cap: about 25% accuracy improvement, under 10% average variance at 12-18 months, about 3,000 hours a year, 7-month parallel run (NEUGROUP-2025). Grade C (organization unnamed). AIA: "up to 90% more accurate" on specific items (TREASURYTODAY-2024). Grade B. |
| Code generation for analysts (custom automations) | assist | step | `bulk-transformation` | Ranked highest for impact by finance leaders in Gartner's survey (GARTNER-2025, quote on code generation). Grade C. |
| Agent runs close steps end to end with deterministic checks between steps | delegate | process | `end-to-end-case-agent` | Argued in a vendor blog (KOGNITOS-2026). KPMG's 2026 survey (n=1,013) says organizations deploying agentic AI report stronger performance on key finance metrics, a perception measure (KPMG-2026, executive summary). Grade C. |

**Metrics and benchmarks (with sources).**
- Adoption and impact: 59% using AI in finance; 91% low or moderate impact initially; organizations further along were over two times more likely to see moderate impact and nearly three times more likely to see high impact (survey, Gartner-measured, GARTNER-2025).
- Close: days to close; 7.5 days earlier close and 12% increase in general-ledger granularity among 79 firms using AI tools (independent, STANFORD-2025). APQC median 6.4 days is second-hand (KOGNITOS-2026).
- Forecast: average variance to actuals under 10% across 14 hedged currencies at 12-18 month horizon, as low as 5% for some; shorter horizons may be less accurate (self-reported at a peer-group meeting, NEUGROUP-2025).
- Review load: 26% average share of work time verifying or correcting AI outputs; 96% spend at least 10% (Datarails survey of 270 finance leaders at US organizations with over 1,000 employees and at least $100 million revenue; vendor-published, DATARAILS-2026).
- Trust: only 14% of 100 mid-market US CFOs completely trust AI to deliver accurate accounting data on its own; 86% report at least one inaccurate or hallucinated output (Wakefield Research for Maximor AI, vendor-commissioned, WAKEFIELD-2026).
- Control monitoring: COSO guidance points to transaction volume, transaction size and override percentages as indicators to detect model drift (DELOITTE-DART-2026, commentary on COSO's publication).
- Fraud exposure: 21,442 business email compromise complaints and $2,770,151,146 reported losses in 2024 (complaints to the FBI's IC3; FBI-2025, three-year comparison tables).

**Interview probes for a finance leader.** See section 4.1.

**Guardrails and decisions that need human judgment.**
- Internal control over financial reporting: COSO's February 2026 publication extends its 2013 framework to generative AI, with a six-step roadmap (govern, inventory, assess, design, implement, monitor) and a capability-based view; Deloitte's commentary says "set-and-forget" does not work when GenAI is used in financial reporting (DELOITTE-DART-2026; JOA-2026, which lists eight capability types).
- Payment release and bank-detail changes are the control point (author's inference from the incidents, not a source recommendation). Arup's finance worker paid HK$200 million (about $25.6 million) in 15 transactions after a video call with deepfaked colleagues (CNN-2024). The FBI's definition of business email compromise, which lists virtual meeting applications among the communication channels fraudsters compromise (FBI-2025, Appendix B).
- Accounting judgments (estimates, policy choices, final sign-off) stay with people: Stanford's write-up says the "final judgment call" remains human, and describes senior accountants stepping in when system confidence drops while juniors accepted flagged outputs (STANFORD-2025).
- Risk-management frameworks: NIST AI RMF 1.0 (released 2023-01-26) and its Generative AI Profile (NIST AI 600-1) (NIST-2023).
- EU AI Act: Annex III lists AI used to evaluate creditworthiness of natural persons as high-risk, excluding AI used to detect financial fraud (EUAIA-2024, Annex III, point 5). Most internal finance work is not on that list; consumer-credit work is.

**How roles change.**
- Capacity moves to client communication, quality assurance and advisory work: accountants spent 8.5% less time on routine back-office processing (STANFORD-2025).
- Seniors become reviewers of AI output, juniors gain less (STANFORD-2025).
- In Datarails' vendor survey, 60% of respondents are redeploying employees to higher-value work and 3% are cutting finance headcount because AI replaced work (DATARAILS-2026).
- KPMG's survey says most organizations are upskilling existing teams but only 28 percent are rethinking the types of talent they need (KPMG-2026, executive summary).

### 2.2 strategy-planning

**Scope.** The in-house strategy, corporate planning and performance-management function. Firm-level strategy of professional-services firms is in the archetype entries (section 3).

**Main processes and key steps (with work types).** No process framework file for strategy was read in this run (see Gaps); the grouping below is the author's.

| Process | Key steps | Work types |
|---|---|---|
| Strategy development | Environment scanning; option generation; evaluation and choice; articulation | `research-synthesis`, `expert-judgment`, `document-production` |
| Market and competitive intelligence | Source monitoring; synthesis; implications | `research-synthesis` |
| Annual planning, budgeting and target setting | Assumptions; targets; resource allocation; reconciliation of bottom-up and top-down | `data-reporting`, `coordination-scheduling`, `expert-judgment` |
| Scenario and capital-allocation analysis | Scenario design; modelling; investment cases | `data-reporting`, `expert-judgment` |
| Portfolio and transformation tracking | Initiative status; benefits tracking; course corrections | `coordination-scheduling`, `data-reporting` |
| Performance reporting to board and executives | Pack assembly; commentary; Q&A preparation | `document-production`, `data-reporting` |
| Stakeholder and public input analysis (public sector, regulated sectors) | Collect responses; theme; summarize for decision | `research-synthesis`, `transaction-processing` |

**Typical pain points.**
- Qualitative input at volume is slow to analyze: the UK government estimates about 75,000 days of manual analysis a year across consultations, costing £20 million (a projection, not a measurement; DSIT-2025).
- Strategic and executional decisions made in separate tools. Walmart describes a simulation platform built to connect "strategic and executional decision engines" (INFORMS-2024, abstract).
- Slow, subjective option evaluation: investor evaluators in an experiment disagreed with each other enough that an LLM's scores explained about 29% of variation in investor scores (CSASZAR-2024, section 3).
- Plans converge: AI-assisted stories were more similar to each other than human-only stories (a creative-writing experiment, adjacent; EXETER-2024).

**Top AI opportunities.**

| Opportunity | Ladder | Scope | Pattern | Best evidence and grade |
|---|---|---|---|---|
| Synthesize large volumes of qualitative input (consultations, comments) into themes | augment | step | `document-to-decision` | Consult, Scottish Government trial: F1 0.76, 60% of responses unchanged by reviewers, median 23 seconds to review a response (IAI-2025). Grade B (adjacent: policy consultation, public sector). |
| Draft and critique strategic options; second opinion | assist | step | `research-brief` | LLM-generated plans rated 0.14 SD higher than entrepreneurs' versions by 250 investor-experienced evaluators (CSASZAR-2024). Grade D (idea, experiment only). |
| Score or screen plans at scale | augment | step | `intake-triage` | LLM scores on 138 competition plans correlated with judges' scores; explained about 29% of variation (CSASZAR-2024). Grade D (idea, experiment only). |
| Link network or portfolio design to execution with optimization and simulation | augment | process | `monitor-diagnose-act` | Walmart: optimization-based network design and transformation plans approved for long-term investments "involving billions of dollars" (INFORMS-2024); no measured outcome of the network design is reported. Grade B. |
| Forecast and plan on full data instead of manual submissions | automate | process | `monitor-diagnose-act` | Treasury cash forecasting evidence (finance card). For earnings, a working paper reports an LLM outperforming the median analyst at predicting annual earnings (CHICAGOBOOTH-2024). Grade D (idea, experiment only). |
| Continuous competitive-intelligence monitoring | automate | process | `monitor-diagnose-act` | Described as an illustrative use by a corporate blog; no deployment or result (INDIAMART-2025, search-only). Grade D (idea). |
| Board and executive pack assembly | augment | step | `draft-review-loop` | No measured named case found. Grade D (idea). |
| Reshape the operating model, investment envelope or fee mix for AI | any | model | `other` | Archetype entries (section 3), professional-services firms. |

**Metrics and benchmarks.**
- Agreement with a human reviewer: F1 0.76 (95% CI 0.75 to 0.77) across responses; an earlier Consult evaluation with two reviewers found reviewer-to-reviewer F1 of 0.81, and the reviewers mapped exactly the same themes 62% of the time (IAI-2025, "Findings", Fig 2 text). Self-reported by the tool's builder.
- Review time: median 23 seconds per response; 77% of responses under a minute (IAI-2025).
- Theme ranking: differences had negligible effect on ranking of themes, which the report calls the key driver of policy recommendations (IAI-2025, executive summary).
- Task speed and quality inside the AI frontier: 12.2% more tasks completed, 25.1% faster, higher quality, among 758 BCG consultants on 18 tasks (HBS-2023, abstract; independent academic study).
- No benchmark was found for plan-to-actual variance, strategy cycle time or planning cost.

**Guardrails and decisions that need human judgment.**
- Choice of strategy, capital allocation and which options to pursue are the decisions the cited studies do not hand to AI: the Consult report says reviewers wanted to influence themes and needed more confidence before reviewing only a share of responses (IAI-2025, executive summary).
- Tasks outside the AI's competence: consultants using GPT-4 were 19% less likely to produce correct solutions on a managerial task selected to be outside the frontier (HBS-2023, abstract).
- Missed themes: "Consult struggled to identify missing themes" (IAI-2025, executive summary; paraphrase of the finding).
- Homogenization: AI-inspired outputs converged (EXETER-2024; adjacent).
- Risk frameworks: NIST AI RMF 1.0 and the Generative AI Profile (NIST-2023).

**How roles change.**
- The Consult evaluation says faster analysis "freed up time" to focus on implications, and reviewers felt Consult helped reduce reviewer bias (IAI-2025, executive summary).
- Csaszar et al. argue AI may change search, representation and aggregation in strategic decisions and enable "virtual strategy simulations"; this is a framework, not a measurement (CSASZAR-2024, abstract).

### 2.3 procurement-supply-chain

**Scope.** Procurement (sourcing, contracting, purchasing, supplier management) and supply chain planning and execution in any organization. SCOR describes seven process groupings: Orchestrate, Plan, Order, Source, Transform, Fulfill, Return (ASCM-2026, "SCOR DS" section).

**Main processes and key steps (with work types).**

| Process | Key steps | Work types |
|---|---|---|
| Plan (demand, supply, inventory) | Determine requirements; gather resource information; balance requirements and resources; identify actions to close gaps (ASCM-2026 definition) | `data-reporting`, `coordination-scheduling`, `expert-judgment` |
| Source (procure) | Procuring, ordering, scheduling orders, delivery, receipt, transfer of products and services (ASCM-2026 definition); in practice: spend analysis, sourcing events, negotiation, contracting | `research-synthesis`, `expert-judgment`, `document-production`, `transaction-processing` |
| Supplier management and risk | Onboarding; performance; risk monitoring; alternative sources | `review-assurance`, `research-synthesis`, `coordination-scheduling` |
| Transform and Fulfill (where in scope) | Scheduling production; picking, packing, shipping, invoicing (ASCM-2026) | `physical-field`, `coordination-scheduling`, `transaction-processing` |
| Return | Reverse flow of goods and services (ASCM-2026) | `transaction-processing`, `physical-field` |
| Orchestrate | Business rules, network design, contracts and agreements, regulations and compliance, risk mitigation (ASCM-2026) | `expert-judgment`, `review-assurance` |

**Typical pain points.**
- Buyers cannot negotiate fully with all suppliers: Walmart cannot run focused negotiations with its 100,000-plus suppliers, and around 20% signed agreements with terms that were often not negotiated (HBR-2022, opening; remainder paywalled).
- Siloed ways of working are the top-ranked barrier to value (57%), then competing priorities (46%), capability to support execution (40%), talent gap (34%) (Deloitte survey of over 250 CPOs; DELOITTE-2025).
- Long acquisition lead times in public-sector contracting: the NPS paper models reductions in procurement acquisition lead time (PALT) and lists baseline time bands by acquisition type (NPS-2026, section on baseline PALT by acquisition type).
- Gains stay at individual level: Gartner's survey of 101 CPOs says productivity gains are not yet translating to team or enterprise outcomes (GARTNER-2026).
- Fraud on supplier payments: business email compromise targets businesses working with suppliers and regularly making wire transfers (FBI-2025, Appendix B).

**Top AI opportunities.**

| Opportunity | Ladder | Scope | Pattern | Best evidence and grade |
|---|---|---|---|---|
| Negotiate with tail suppliers that were previously not negotiated | automate | process | `end-to-end-case-agent` (bounded) | Walmart and Pactum: 68% of negotiations closed, 3% average savings, vendor-published, via PYMNTS-2023. Grade B. |
| Optimize truck routing and loading; link network planning to daily execution | automate | process | `monitor-diagnose-act` | Walmart FY23: 108,000 routes and 33 million miles eliminated, $91.5 million saved (INFORMS-2024, abstract). Grade A (optimization, not generative AI). |
| Optimize delivery routes | automate | process | `monitor-diagnose-act` | UPS ORION: more than $320 million saved as of December 2015 (INFORMS-2016). Grade A (older, pre-generative). |
| Contract and document review in contracting (human in the loop) | augment | step | `document-to-decision` | 39th Contracting Squadron, Incirlik: prototype under development with a vendor; modelled PALT reductions are projections (NPS-2026). Grade B. |
| Scope RFPs and compare supplier or adviser proposals | augment | step | `document-to-decision` | Archetype entry (section 3). |
| Supplier risk monitoring and alternative sourcing | automate | process | `monitor-diagnose-act` | Top risk-mitigation strategies in Deloitte's survey: active alternative sources 74%, supply-chain visibility 64%, supplier information sharing 61% (survey, DELOITTE-2025); no measured AI deployment found. Grade C. |
| Demand forecasting and planning | automate | process | `monitor-diagnose-act` | One search-only consultancy proof of concept (about 150 stores, 500 products) reports 33% lower forecast error (SUPCHAINS-2025, search-only). Grade C. |
| Third-party AI due diligence and contracting | assist | process | `review-assurance` | Archetype entry (section 3). |
| Agents that plan across planning and logistics | delegate | process | `end-to-end-case-agent` | Unilever's plan described at a vendor event (search-only). Grade D (idea). |

**Metrics and benchmarks.**
- Negotiation outcomes (Pactum-reported): 68% of suppliers closed, 3% average savings, 83% found the chatbot easy to use, 2,000 suppliers negotiated at once; Bloomberg-reported: deals close in days rather than weeks, nearly three in four suppliers prefer the chatbot (PYMNTS-2023). Vendor-published and journalist-reported.
- Survey returns: "Digital Masters" (top quartile) report an average 3.2x return on GenAI, followers projected slightly above 1.5x; technology budget up to 24% for Digital Masters (self-reported by surveyed CPOs; DELOITTE-2025).
- Functions reporting AI cost reductions most often: supply chain management, service operations, manufacturing (McKinsey global survey; MCKINSEY-2026, Exhibit 6 text).
- Routing: 108,000 routes, 33 million miles, 98.6 million pounds CO2 and $91.5 million in FY23 (INFORMS-2024); the INFORMS award release gives 72 million pounds CO2 and $75 million for fiscal 2023 (INFORMS-2023). The two sources differ; the reasons are not stated in either.
- SCOR claims typical client results (2 to 6 times ROI in year one, among others); this is an ASCM statement about SCOR use, not about AI, and is not independently measured (ASCM-2026).
- No benchmark was found for contract cycle time, spend under management or savings rate from a source that could be opened.

**Guardrails and decisions that need human judgment.**
- Scope limits at Walmart: the chatbot negotiates only smaller contracts with suppliers of equipment rather than goods for sale, per Bloomberg as reported by PYMNTS-2023.
- Negotiation behavior: a competitively prompted buyer chatbot gets a higher discount, better payment terms and quicker negotiation, but suppliers trust a collaboratively prompted one more and report higher satisfaction and desire for future interaction (HEROLD-2025, abstract; experiments with students and professional negotiators, supplier role played by participants).
- Fairness and exploitation: in bargaining games LLMs favored conservative, concessionary proposals while humans proposed trades consistent with fairness norms; parity in aggregate surplus can mask procedural differences (QIAN-2025, abstract).
- Payment verification and bank-detail changes (FBI-2025; CNN-2024).
- EU AI Act: Annex III high-risk categories cover employment-related and credit-related uses; ordinary supplier negotiation and sourcing are not listed there (EUAIA-2024, Annex III).
- Human judgment: supplier strategy, critical or high-value contracts, trade-offs between price and relationship, exceptions that cross policy.

**How roles change.**
- Gartner recommends redesigning roles by separating "innately human" tasks from "AI-native" tasks, aligning gains to financial outcomes, and updating productivity measures (GARTNER-2026).
- Walmart's chatbot frees procurement teams to focus on larger contracts (Bloomberg via PYMNTS-2023).
- Deloitte's survey says people must stay "in the loop" and finds a correlation between combined technology and talent competencies and better enterprise performance (DELOITTE-2025; correlation, not causation).

## 3. Examples

Columns: organization (industry) | what changed in the work | ladder, scope | outcome and provenance | grade | source. "Experiment only" means no deployment; graded D per the convention at the top.

### 3.1 finance-accounting

| # | Organization (industry) | What changed in the work | Ladder, scope | Outcome and provenance | Grade | Source |
|---|---|---|---|---|---|---|
| F1 | Microsoft finance, a function of about 5,000 people (technology) | Finance staff use Copilot for Finance, in public preview at the time, to reconcile data in Excel; variance analysis being tested; a private library of about 300 finance prompts | augment, step | AR reconciliation in the global treasury and financial services team saved an average 20 minutes per account; an FP&A team's weekly reconciliation fell from an average 1-2 hours to 10 minutes. Self-reported internal case study results shared with a journalist; method unpublished; Microsoft also sells the tool. Variance analysis: "promising results so far" (no figure) | A | CFODIVE-2024 |
| F2 | US Department of the Treasury, Office of Payment Integrity (public sector) | Machine learning used to expedite identification of Treasury check fraud, alongside risk-based screening and prioritization of high-risk transactions | automate, step | FY2024: over $4 billion prevented and recovered in fraud and improper payments, up from $652.7 million in FY23; $1 billion recovery credited to machine-learning check-fraud identification; $2.5 billion to prioritizing high-risk transactions; $500 million to risk-based screening; $180 million to payment-schedule efficiencies. Self-reported by Treasury | A | TREASURY-2024 |
| F3 | AIA Group Treasury Operations (life insurance, financial services) | In-house machine-learning model forecasts major cash line items for operating entities; one-month forecasts feed the daily cash forecast; treasury overlays expected near-term flows; actual balances fed back | automate, process | Head of Treasury Operations says the group "observed up to 90% more accurate forecasts on specific cash flow items". Self-reported statement, "up to", no denominator. Pilot in Malaysia and Philippines (Phase 2 production), Singapore and Indonesia (model trained) | B | TREASURYTODAY-2024 |
| F4 | Unnamed mega-cap corporate treasury (industry not stated) | Custom ML models for each of 14 hedged currencies replace about 180 forecasters submitting monthly; five years of bank-statement tagging; one-time adjustment mechanism for known events; legacy and ML run in parallel about seven months, then "reverse parallel" three months | automate, process | About 25% accuracy improvement; average variance to actuals under 10% at 12-18 months across all 14 currencies, as low as 5% for some; about 3,000 hours a year saved. Statements by the senior manager at a peer-group meeting, reported by NeuGroup; organization unnamed | C | NEUGROUP-2025 |
| F5 | 79 small and mid-sized firms using AI-enabled accounting tools; survey of 277 accountants (accounting services) | AI takes over repetitive tasks such as transaction classification; accountants shift to communication, quality assurance, advisory | augment, process | Month-end statements finalized 7.5 days faster; 8.5% less time on routine back-office processing; 12% rise in reporting granularity; 62% of surveyed accountants concerned about AI-generated errors. Independent academic study, task-level platform data; adopters may differ from non-adopters | B (adjacent: services firms, not in-house) | STANFORD-2025 |
| F6 | Experiment on financial-statement analysis (research, no deployment) | General-purpose LLM given anonymized standardized statements and chain-of-thought prompts to forecast annual earnings | assist, step | Working paper reports the LLM outperforms the median analyst and is on par with a trained neural network; "preliminary" results. Independent academic | D (idea, experiment only) | CHICAGOBOOTH-2024 |
| F7 | Benchmark of finance-agent tasks (evaluation, no deployment) | Agents answer 537 entry-level financial-analyst questions (retrieval, market research, projections) | delegate, step | Top accuracy on the leaderboard as accessed 2026-10-20: 64.37%. Third-party evaluator; built with Stanford researchers, a G-SIB and industry experts | D (idea, evaluation only) | VALS-2026 |

Archetype use-case ids touching `finance-accounting` (id and grade only): assurance-sustainability-assurance-08 (C), assurance-sustainability-assurance-09 (C), assurance-sustainability-assurance-10 (C), assurance-sustainability-assurance-11 (C), assurance-sustainability-assurance-12 (C), professional-services-billing-collections-01 (B), professional-services-billing-collections-02 (C), professional-services-billing-collections-03 (C), professional-services-billing-collections-04 (B), professional-services-billing-collections-05 (B), professional-services-billing-collections-06 (C), professional-services-billing-collections-07 (C), professional-services-billing-collections-08 (D), professional-services-billing-collections-09 (C), professional-services-billing-collections-10 (C), professional-services-billing-collections-11 (C), professional-services-billing-collections-12 (B), professional-services-billing-collections-13 (B), professional-services-billing-collections-14 (D), professional-services-billing-collections-15 (D), professional-services-billing-collections-16 (C), professional-services-billing-collections-17 (C), professional-services-firm-finance-02 (C), professional-services-firm-finance-03 (B), professional-services-firm-finance-04 (B), professional-services-firm-finance-05 (C), professional-services-firm-finance-06 (C), professional-services-firm-finance-09 (C), professional-services-firm-finance-11 (B), professional-services-firm-finance-12 (C), professional-services-scoping-pricing-06 (B), professional-services-scoping-pricing-08 (C), professional-services-scoping-pricing-09 (C), security-human-risk-06 (C), security-human-risk-13 (D), tax-compliance-corporate-01 (C), tax-compliance-corporate-03 (C), tax-compliance-corporate-05 (C), tax-compliance-corporate-07 (B), tax-compliance-corporate-09 (C), tax-compliance-corporate-10 (B), tax-compliance-corporate-11 (C), tax-compliance-corporate-12 (C), tax-compliance-corporate-14 (C), tax-compliance-corporate-17 (C), tax-compliance-corporate-22 (D), tax-compliance-corporate-24 (D), tax-data-technology-01 (B), tax-data-technology-02 (C), tax-data-technology-03 (C), tax-data-technology-04 (B), tax-data-technology-05 (B), tax-data-technology-06 (B), tax-data-technology-07 (C), tax-data-technology-08 (B), tax-data-technology-09 (B), tax-data-technology-10 (D), tax-data-technology-11 (C), tax-data-technology-12 (C), tax-data-technology-13 (C), tax-data-technology-14 (C), tax-data-technology-15 (C), tax-data-technology-16 (D), tax-data-technology-17 (C), tax-data-technology-22 (B), tax-data-technology-23 (B), tax-data-technology-24 (C), tax-indirect-tax-10 (C), tax-indirect-tax-18 (C), tax-indirect-tax-20 (B), tax-provision-pillar-two-01 (C), tax-provision-pillar-two-02 (D), tax-provision-pillar-two-03 (C), tax-provision-pillar-two-04 (C), tax-provision-pillar-two-05 (C), tax-provision-pillar-two-06 (D), tax-provision-pillar-two-07 (C), tax-provision-pillar-two-08 (C), tax-provision-pillar-two-09 (C), tax-provision-pillar-two-10 (D), tax-provision-pillar-two-11 (C), tax-provision-pillar-two-12 (C), tax-provision-pillar-two-13 (C), tax-provision-pillar-two-14 (C), tax-provision-pillar-two-16 (C), tax-research-advisory-06 (C), tax-transfer-pricing-01 (C), tax-transfer-pricing-02 (C), tax-transfer-pricing-03 (C), tax-transfer-pricing-04 (C), tax-transfer-pricing-09 (B), tax-transfer-pricing-12 (B), tax-transfer-pricing-13 (C), tax-transfer-pricing-14 (C), tax-transfer-pricing-21 (B)

### 3.2 strategy-planning

| # | Organization (industry) | What changed in the work | Ladder, scope | Outcome and provenance | Grade | Source |
|---|---|---|---|---|---|---|
| S1 | Scottish Government, with the UK government's Incubator for AI (public sector) | Consult generated themes for six questions of a consultation (over 2,000 responses); government experts checked and refined themes; the tool mapped responses to themes; reviewers checked mappings. In the trial every response was also reviewed by hand | augment, step | F1 0.76 (95% CI 0.75-0.77); reviewers made no changes for 60% of responses; median 23 seconds to review a response; negligible effect on theme ranking; struggled to identify missing themes. Self-reported by the builders; single reviewer as ground truth | B (adjacent: policy consultation, not corporate strategy) | IAI-2025; DSIT-2025 |
| S2 | Walmart (retail), network planning and transformation | Optimization models produce long-term network design with step-by-step recommendations; a simulation platform links strategic and executional decision engines | augment, process | Network design and transformation plans "approved" for long-term investments involving billions of dollars (paper abstract); no measured outcome of the design itself. Self-reported | B | INFORMS-2024 |
| S3 | Startup accelerator in Europe; 250 evaluators with investing experience (venture capital) | GPT-3.5 wrote business plans from the entrepreneur's problem statement; evaluators scored LLM and original versions | assist, step | LLM versions rated 0.14 SD higher on average; evaluators 5 percentage points more likely to recommend acceptance (p = 0.003). Ten plans only; pre-registered; independent academic | D (idea, experiment only) | CSASZAR-2024 |
| S4 | Startup competition judges (venture capital) | LLM scored 138 text-only plans; compared with 541 evaluations by 137 judges | augment, step | LLM scores explained about 29% of variation in investor scores. Independent academic | D (idea, experiment only) | CSASZAR-2024 |
| S5 | 758 BCG consultants (management consulting) | Preregistered experiment: no AI, GPT-4, GPT-4 with prompt guidance on 18 realistic tasks plus one task outside the frontier | assist, step | Inside frontier: 12.2% more tasks, 25.1% faster, higher quality. Outside: 19% less likely to be correct. Independent academic study with BCG | D (idea, experiment only) | HBS-2023 |
| S6 | 300 writers, 600 evaluators (creative writing; adjacent) | Writers got LLM-generated story ideas | assist, step | AI-assisted stories more creative, but 10.7% more similar to each other with one AI idea than with none. Independent academic; adjacent to option generation | D (idea, experiment only) | EXETER-2024 |
| S7 | Chief strategy officers (generic) | Competitor monitoring with generative AI | automate, process | None published; illustrative description in a corporate blog (search-only) | D (idea) | INDIAMART-2025 |

Archetype use-case ids touching `strategy-planning` (id and grade only): assurance-acceptance-independence-09 (C), assurance-acceptance-independence-19 (C), professional-services-firm-finance-01 (B), professional-services-firm-finance-07 (B), professional-services-firm-finance-10 (B), professional-services-firm-finance-14 (D), professional-services-firm-finance-15 (B), professional-services-firm-finance-16 (C), professional-services-firm-finance-17 (B), professional-services-knowledge-management-23 (C), professional-services-scoping-pricing-14 (D), professional-services-scoping-pricing-17 (C), professional-services-talent-learning-19 (B), professional-services-talent-learning-20 (C), tax-transfer-pricing-19 (C)

### 3.3 procurement-supply-chain

| # | Organization (industry) | What changed in the work | Ladder, scope | Outcome and provenance | Grade | Source |
|---|---|---|---|---|---|---|
| P1 | Walmart with Pactum (retail) | A chatbot negotiates price, payment terms and other items with human supplier representatives for smaller contracts with equipment suppliers; the retailer supplies budget and needs; the system uses historical trends, competitor-price estimates and material costs | automate, process | Pactum release (Jan 2023): 68% of negotiations closed, 3% average savings, 83% found the chatbot easy to use, 2,000 suppliers at once. Bloomberg: deals closed in days, nearly three in four suppliers prefer it. Vendor-published, reported second-hand | B | PYMNTS-2023; HBR-2022 |
| P2 | Walmart, Load Planner (retail logistics) | Optimization decides truck routing and loading across the US grocery network; full network rollout in FY23 | automate, process | FY23: 108,000 routes and 33 million miles eliminated, 98.6 million pounds CO2 prevented, $91.5 million saved (paper); award release says 72 million pounds CO2 and $75 million. Self-reported; the two sources differ | A (optimization, not generative AI) | INFORMS-2024; INFORMS-2023 |
| P3 | UPS ORION (logistics) | Each morning ORION gives drivers an optimized delivery sequence; used by more than 35,000 of 55,000 US drivers as of Dec 2015 | automate, process | More than $320 million saved as of Dec 2015; $300-400 million a year expected at full deployment; 10 million gallons of fuel a year estimated. Self-reported, award submission summary. Foundation evidence, pre-generative AI | A (older) | INFORMS-2016 |
| P4 | 39th Contracting Squadron, Incirlik Air Base, with a vendor (defense, public sector) | Human-in-the-loop AI copilot for document validation and regulatory review in contracting; prototype under development | augment, step | Modelled PALT reductions bracketed in the paper: [31%] for simplified acquisitions, [43%] for source selection, 34% projected at scale. Vendor-authored projections; preliminary, not measured | B | NPS-2026 |
| P5 | Maersk, Wesco (shipping, distribution) | Pactum bot reported as negotiating contracts for them | automate, process | No outcome metrics in the source seen (search result only) | C (search-only) | none (not opened) |
| P6 | InnovaCare Health (healthcare services) | AI procurement tool for contracts | augment, process | Vendor release: contract cycle time down 60%, 18% of overlapping contracts consolidated. Vendor-authored; page not opened | C (search-only) | LEVELPATH-2025 |
| P7 | Grocery retailer, about 150 stores and 500 products (retail) | ML model forecasts demand 14 days ahead per product per store | automate, process | 33% lower forecast error than existing planning software; consultancy proof of concept; page blocked (search-only) | C (search-only) | SUPCHAINS-2025 |
| P8 | Buyer-supplier negotiation experiments (research) | Custom ChatGPT-based buyer chatbot against student and professional negotiators | automate, step | Competitive chatbot: higher discount, better payment terms, quicker; collaborative chatbot: more trust and satisfaction. Independent academic | D (idea, experiment only) | HEROLD-2025 |
| P9 | Bargaining-game experiment, 216 humans (research) | Humans, frontier LLMs and Bayesian agents in multi-player bargaining | automate, step | LLMs and humans reach comparable aggregate surplus with different strategies; LLMs concessionary. Independent academic | D (idea, experiment only) | QIAN-2025 |
| P10 | Retailer and supplier agents (research) | LLM agents negotiate order quantity and wholesale price | automate, step | Reported: more deals than humans, possible greater inequality. Search result only | D (idea, search-only) | KIRSHNER-2026 |

Archetype use-case ids touching `procurement-supply-chain` (id and grade only): assurance-quality-management-06 (C), professional-services-client-development-17 (C), professional-services-firm-finance-08 (B), professional-services-pursuit-proposals-20 (C), professional-services-scoping-pricing-11 (B), tax-compliance-corporate-15 (C)

## 4. Expert moves and probes

### 4.1 finance-accounting

1. "Show me the days-to-close and the number of manual journals for the last six closes. Where does the clock stop between steps?" Reveals whether the constraint is task time or handoffs. Basis: KOGNITOS-2026 argues the days sit in handoffs; verify with the user's own data, not the vendor's number.
2. "For each reconciliation, how many are matched without a person and how many breaks does a person clear?" Reveals the `reconcile-exceptions` baseline and who owns the exception queue. Basis: Microsoft's measure is minutes per account (CFODIVE-2024).
3. "How much of your team's week is spent checking AI output today?" Reveals hidden review load. Basis: survey average 26% (DATARAILS-2026, vendor survey).
4. "Who releases a payment, and what happens when a request arrives with new bank details or an urgent instruction from a senior person on a video call?" Reveals whether payment authorization is protected against impersonation. Basis: CNN-2024; FBI-2025.
5. "What would you run in parallel before switching, for how long, and who decides it passed?" Reveals readiness to prove quality. Basis: seven months parallel plus three months reverse parallel (NEUGROUP-2025).
6. "Do juniors and seniors review AI output differently on your team?" Reveals review-turns-into-rubber-stamp risk. Basis: STANFORD-2025.
7. "Which control in your ICFR inventory would an AI step touch, and who tracks override rates?" Reveals control ownership. Basis: DELOITTE-DART-2026.
8. "Is your data in one governed place or in spreadsheets?" Reveals data readiness; data quality is a top barrier. Basis: GARTNER-2025.
9. Heuristic: where the hours released go. Datarails' survey says 60% redeploy and 3% cut (vendor survey); ask for the named destination for any capacity claimed.
10. Heuristic: separate "AI interprets" from "software executes policy" in any design that runs several steps in sequence; compounding error is arithmetic, not measured (KOGNITOS-2026, 0.85 to the tenth power is about 19.7%, an illustration).

### 4.2 strategy-planning

1. "Which decisions did the last planning cycle change, and what input did each rely on?" Reveals where qualitative or analytic synthesis is actually decision-bearing. Basis: IAI-2025 treats theme ranking as the key driver of policy recommendations.
2. "How many documents, comments or responses do you read, and how many do you sample?" Reveals candidates for full-population synthesis. Basis: IAI-2025.
3. "Who would check the themes and what would they do about a missing theme?" Reveals the review design. Basis: Consult struggled to identify missing themes (IAI-2025).
4. "Where do your strategy and execution tools disconnect?" Reveals a model or process opportunity of the Walmart kind (INFORMS-2024).
5. "Would you use AI for options you generate or only to critique them?" Reveals homogenization exposure: AI-inspired output converged (EXETER-2024; adjacent).
6. "Which of your tasks is outside what current AI does reliably?" Reveals jagged-frontier awareness: 19% less likely to be correct outside the frontier (HBS-2023).
7. "How do you evaluate a plan today, and how much do evaluators agree with each other?" Reveals whether there is a stable standard to test an AI screen against. Basis: CSASZAR-2024.
8. "Which forecasts are built from manual submissions?" Reveals machine-learning forecast candidates (NEUGROUP-2025 for the pattern).
9. Heuristic: do not accept speed as the outcome; ask what the freed time buys (IAI-2025 "freed up time to focus on the implications").

### 4.3 procurement-supply-chain

1. "What share of suppliers or spend gets a negotiated deal, and what is left on standard terms?" Reveals tail-spend scope. Basis: about 20% of Walmart's suppliers on un-negotiated terms (HBR-2022).
2. "What are your guardrails on what a bot may agree to?" Reveals bounds and escalation. Basis: Walmart limited the chatbot to smaller contracts (PYMNTS-2023).
3. "Does your relationship with the supplier matter after the deal?" Reveals the trust trade-off of a competitive bot (HEROLD-2025).
4. "Who owns the redesign of buyer roles, and which tasks are innately human?" Reveals the gap between individual gains and team outcomes. Basis: GARTNER-2026.
5. "What is the lead time from request to contract by type of purchase?" Reveals baseline for cycle-time claims. Basis: NPS-2026 uses PALT by acquisition type.
6. "How do you verify a changed supplier bank detail?" Reveals payment-fraud exposure (FBI-2025).
7. "Where does planning sit relative to sourcing?" Reveals whether the process-level change in SCOR terms (Plan and Source) is in scope (ASCM-2026).
8. "What do you measure after go-live that is not hours?" Reveals value capture. Basis: Gartner suggests aligning gains to financial outcomes (GARTNER-2026).
9. "Which suppliers are critical and how do you find alternatives?" Reveals the risk-monitoring opportunity; 74% of surveyed CPOs call active alternative sources effective (DELOITTE-2025).

## 5. Evidence on what works and what fails

**Measured quality or error evidence**

| Evidence | What it measures | Population and provenance | Source and locator |
|---|---|---|---|
| Consult F1 0.76; 60% of responses unchanged by reviewers | Multi-label F1 of Consult themes against a single human reviewer's themes, per response; and share of responses where reviewers changed nothing | Scottish Government non-surgical cosmetic procedures consultation, over 2,000 responses; self-reported by builders; earlier two-reviewer F1 0.81, same themes 62% of the time | IAI-2025, "Findings" |
| Junior accountants accept flagged outputs | Qualitative finding: juniors more likely to accept AI outputs even when flagged uncertain, with smaller gains | 79 firms; survey of 277 accountants; independent | STANFORD-2025 |
| 81% incorrect or refused | GPT-4-Turbo with retrieval, share of questions incorrectly answered or refused | 150-case sample of FinanceBench (10,231 questions); 2023 models; academic/benchmark authors | PATRONUS-2023, abstract |
| Best 64.37% accuracy | Finance Agent v1.1 benchmark accuracy of the top model on 537 questions | Third-party leaderboard, accessed 2026-10-20; changes with each release | VALS-2026 |
| 19% less likely correct outside the frontier | Probability of a correct solution with GPT-4 vs without on one task selected to be outside AI capability | 758 BCG consultants; independent academic | HBS-2023, abstract |
| 26% of work time verifying AI output | Self-reported average share of work time verifying or correcting AI-generated finance outputs | 270 US finance leaders; vendor survey | DATARAILS-2026 |
| 86% saw at least one inaccurate output | Share of CFOs whose team encountered at least one inaccurate or hallucinated output | 100 mid-market US CFOs; vendor-commissioned | WAKEFIELD-2026 |
| Parallel run | Seven months legacy and ML in parallel, three months reverse parallel; about 25% better accuracy | One unnamed treasury; recollection | NEUGROUP-2025 |
| Supplier trust cost of a competitive bot | Trust and satisfaction ratings by prompt style in experiments | Students and professional negotiators; independent | HEROLD-2025, abstract |
| Concessionary LLM bargaining | Strategy differences with parity in aggregate surplus | 216 humans and frontier LLMs; independent | QIAN-2025, abstract |

**Incidents**
- Arup (engineering and design, Hong Kong): a finance worker sent HK$200 million (about $25.6 million) in 15 transactions after a video call in which people he believed were the CFO and colleagues were deepfake re-creations; Arup confirmed that fake voices and images were used (CNN-2024, paragraphs on police statement).
- FBI IC3 2024: business email compromise 21,442 complaints and $2,770,151,146 reported losses, compared with $2,946,830,270 in 2023 (FBI-2025, three-year comparison). Complaints reported to the FBI, not all incidents.

**Surveys on realized value (perception measures, mostly self-reported)**
- Finance: 91% reported low or moderate impact initially; further-along organizations more likely to see higher impact (GARTNER-2025). In KPMG's survey (n=1,013 senior finance leaders, fielded March 2026), 71% report AI is meeting or exceeding ROI expectations in finance and 23% report it exceeding them; these are perception measures (KPMG-2026, executive summary).
- Enterprise: 37% report positive EBIT contribution, unchanged from 2025; 6% are AI high performers (MCKINSEY-2026).
- Procurement: individual gains decline at team level; only 36% of CPOs very confident in redesign (GARTNER-2026). Digital Masters 3.2x GenAI return, followers projected about 1.5x (DELOITTE-2025).

**What works (consistent across sources)**
- Governance and tracking: KPMG's survey says organizations with stronger governance and controls report significantly better outcomes, in some cases three to six times the rate of significant improvement; this is a correlation in a survey (KPMG-2026).
- Workflow redesign: high performers more often fundamentally redesign workflows (MCKINSEY-2026).
- Parallel running and feedback loops: seven-month parallel run, then reverse parallel (NEUGROUP-2025); AIA feeds actual balances back into the model and lets treasury overlay expected flows (TREASURYTODAY-2024).
- Bounded scope for agents: Walmart limits the negotiation bot to smaller contracts (PYMNTS-2023).

**What fails or limits**
- Weak data and skills (GARTNER-2025).
- Per-task speed without process redesign (GARTNER-2026; vendor argument in KOGNITOS-2026).
- Outside-the-frontier tasks (HBS-2023).
- Missing-theme detection (IAI-2025).
- Impersonation of authority in payment flows (CNN-2024).

**Absence of evidence (stated plainly)**
- No named in-house organization publishes override, escalation or error rates for AI in finance, strategy or procurement in any source opened. COSO names override percentages as an indicator but gives no benchmark (DELOITTE-DART-2026).
- No controlled trial in an in-house finance or procurement function was found. The independent field dataset covers accounting services firms (STANFORD-2025).
- No named corporate strategy team with a measured result was found.
- Procurement chatbot figures come from the vendor and press, not from Walmart (PYMNTS-2023). The 64% closure and 1.5% savings of the earlier pilot, described in a search summary of a Harvard Program on Negotiation page, were not opened.

## 6. Gaps

- APQC PCF category and definition files (finance, strategy, procurement process lists and key measures) are behind downloads; only the framework overview page was read. The process tables above are the author's grouping.
- No process framework for strategy and planning was read.
- APQC's median close time (6.4 days) is second-hand through KOGNITOS-2026.
- HBR's Walmart article is paywalled; only the opening was read. The Pactum 68% and 3% come from a press report of a Pactum release.
- BusinessWire (InnovaCare/Levelpath), Medium (SupChains), Decision Sciences (Kirshner) and FT-linked pages about Maersk and Unilever could not be opened; they are search-only and cannot support A or B. A Kraft Heinz demand-planning claim (25% less excess inventory), seen only in a partner's marketing page in search results, is not used.
- Gartner's finance and procurement press releases were read in full (finance via a syndicated copy); the underlying reports are paywalled.
- No named case with measured results was found for: spend classification, supplier-risk monitoring, strategy competitive intelligence, board-pack assembly, AP touchless rates, month-end close in a named in-house team with a day count.
- Independent measurement of AI in procurement negotiation is limited to experiments; none was run on real suppliers by an independent party.
- Industries covered: technology, public sector (government, defense), financial services (insurance), retail, logistics, professional services (consultants, accounting firms), healthcare (search-only), engineering. Manufacturing has no opened measured case.
- The Datarails and Wakefield surveys are vendor-linked.

## 7. Sources

Access: full = opened and read; search-only = seen only in search results. Dates are publication dates unless "accessed".

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| HBR-2022 | How Walmart Automated Supplier Negotiations | Harvard Business Review; Van Hoek, DeWitt, Lacity, Johnson | press | https://hbr.org/2022/11/how-walmart-automated-supplier-negotiations | 2022-11-08 | search-only (paywalled; opening read) |
| PYMNTS-2023 | Walmart Reportedly Finds 75% of Vendors Prefer Negotiating With Chatbot | PYMNTS | press | https://www.pymnts.com/news/artificial-intelligence/2023/walmart-finds-75-percent-vendors-prefer-negotiating-with-chatbot/ | 2023-04-26 | full |
| GARTNER-2025 | Gartner Survey Shows Finance AI Adoption Remains Steady in 2025 (Gartner release of 2025-11-18, read as syndicated by CPA Practice Advisor) | Gartner | survey | https://www.cpapracticeadvisor.com/2025/11/18/gartner-survey-shows-finance-ai-adoption-remains-steady-in-2025/173371/ | 2025-11-18 | full |
| GARTNER-2026 | Gartner Survey Shows Just 36% of Chief Procurement Officers Are Very Confident in Ability to Redesign Function for AI | Gartner | survey | https://gcom.pdo.aws.gartner.com/en/newsroom/press-releases/2026-05-19-gartner-survey-shows-just-36-perecent-of-chief-procurement-officers-are-very-confident-in-ability-to-redesign-function-for-ai | 2026-05-19 | full |
| STANFORD-2025 | AI Is Reshaping Accounting Jobs by Doing the "Boring" Stuff (on Choi and Xie, Human + AI in Accounting) | Stanford GSB; S. Murray | academic | https://gsb.stanford.edu/insights/ai-reshaping-accounting-jobs-doing-boring-stuff | 2025-06-26 | full (working paper itself not opened) |
| IAI-2025 | Consult Evaluation: Scottish Government's Non-surgical cosmetic procedures consultation | Incubator for AI (UK government) | regulator | https://digitalgovernmenthub.org/wp-content/uploads/2026/02/Scot_Gov_NSCP_Evaluation_Report.pdf | 2025-03-20 | full |
| DSIT-2025 | Government-built "Humphrey" AI tool reviews responses to consultation for first time | UK Department for Science, Innovation and Technology | regulator | https://www.gov.uk/government/news/government-built-humphrey-ai-tool-reviews-responses-to-consultation-for-first-time-in-bid-to-save-millions | 2025-05-14 | full |
| CFODIVE-2024 | Microsoft finance team uses Copilot (CFO Dive) | CFO Dive; A. Alexis | press | https://www.cfodive.com/news/microsoft-finance-copilot-generativeai-software/727176/ | 2024-09-17 | full |
| DELOITTE-2025 | Procurement at the Tipping Point: Deloitte's 2025 Chief Procurement Officer Survey | Deloitte US | survey | https://deloitte.com/us/en/about/press-room/2025-chief-procurement-officer-survey.html | 2025-08-19 | full (press release; report not opened) |
| FBI-2025 | 2024 IC3 Annual Report | FBI Internet Crime Complaint Center | regulator | https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf | 2025 | full |
| CNN-2024 | British engineering giant Arup revealed as $25 million deepfake scam victim | CNN Business; K. Magramo | press | https://edition.cnn.com/2024/05/16/tech/arup-deepfake-scam-loss-hong-kong-intl-hnk | 2024-05-16 | full |
| NIST-2023 | AI Risk Management Framework (AI RMF 1.0, released 2023-01-26; Generative AI Profile NIST AI 600-1) | NIST | standard-setter | https://www.nist.gov/itl/ai-risk-management-framework | 2023-01-26 | full (overview page) |
| PATRONUS-2023 | FinanceBench: A New Benchmark for Financial Question Answering | Islam, Kannappan, Kiela, Qian, Scherrer, Vidgen (arXiv 2311.11944) | academic | https://arxiv.org/abs/2311.11944 | 2023-11-20 | full (abstract) |
| VALS-2026 | Finance Agent v1.1 Leaderboard and Methodology | Vals AI | academic | https://www.vals.ai/benchmarks/finance_agent | 2026-10-20 (accessed) | full |
| MCKINSEY-2026 | The state of AI (2026 global survey) | McKinsey | survey | https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai | 2026-08-25 | full (via text mirror) |
| APQC-2026 | Process Frameworks (Process Classification Framework overview) | APQC | professional-body | https://www.apqc.org/process-frameworks | 2026-10-20 (accessed) | full (overview page) |
| ASCM-2026 | SCOR Digital Standard | ASCM | professional-body | https://www.ascm.org/corporate-transformation/standards-tools/scor-ds/ | 2026-10-20 (accessed) | full (via text mirror) |
| EUAIA-2024 | EU AI Act, Annex III: High-Risk AI Systems (Regulation (EU) 2024/1689, unofficial text mirror) | Future of Life Institute site | regulator | https://artificialintelligenceact.eu/annex/3/ | 2024 | full |
| HBS-2023 | Navigating the Jagged Technological Frontier (HBS Working Paper 24-013) | Dell'Acqua et al., Harvard Business School | academic | https://www.hbs.edu/faculty/Pages/item.aspx?num=64700 | 2023-09 | full (abstract page) |
| CHICAGOBOOTH-2024 | Financial Statement Analysis with Large Language Models | Kim, Muhn, Nikolaev; Chicago Booth | academic | https://www.chicagobooth.edu/research/fama-miller/finance-research/funding/a-demand-system-approach-for-fixed-income/financial-statement-analysis-with-large-language-models | 2024-05 | full (abstract page; date from search listing) |
| EXETER-2024 | AI found to boost individual creativity but results in less varied content (on Doshi and Hauser, Science Advances) | University of Exeter | academic | https://news.exeter.ac.uk/?p=13749 | 2024-07-15 | full |
| DELOITTE-DART-2026 | COSO Releases Publication on Internal Controls Related to Generative AI (Heads Up) | Deloitte DART | professional-body | https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2026/coso-internal-controls-generative-ai | 2026-04-03 | full |
| JOA-2026 | COSO creates audit-ready guidance for governing generative AI | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/news/2026/feb/coso-creates-audit-ready-guidance-for-governing-generative-ai/ | 2026-02-26 | full |
| INFORMS-2016 | UPS On-Road Integrated Optimization and Navigation (ORION) Project | INFORMS | professional-body | https://www.informs.org/Impact/O.R.-Analytics-Success-Stories/UPS-On-Road-Integrated-Optimization-and-Navigation-ORION-Project | 2016 | full |
| INFORMS-2023 | Walmart Awarded the 2023 INFORMS Edelman Award | INFORMS | professional-body | https://www.informs.org/News-Room/INFORMS-Releases/Awards-Releases/Operations-Research-Enhances-Retail-Truck-Routing-and-Load-Planning-Walmart-Awarded-the-2023-INFORMS-Edelman-Award | 2023-04 | full |
| INFORMS-2024 | Optimizing Walmart's Supply Chain from Strategy to Execution | Mehrotra et al., INFORMS Journal on Applied Analytics 54(1) | academic | https://courses.ie.bilkent.edu.tr/ie479/wp-content/uploads/sites/16/2024/11/Optimizing-Walmarts-Supply-Chain-from-Strategy-to-Execution.pdf | 2024-01 | full |
| KOGNITOS-2026 | Why AI has not shortened the month-end close | Kognitos | vendor | https://www.kognitos.com/blog/why-ai-has-not-shortened-the-month-end-close/ | 2026-08-19 | full |
| CSASZAR-2024 | Artificial Intelligence and Strategic Decision-Making: Evidence from Entrepreneurs and Investors | Csaszar, Ketkar, Kim (arXiv 2408.08811) | academic | https://arxiv.org/abs/2408.08811 | 2024-08-16 | full |
| QIAN-2025 | Humans, LLMs and Bayesian agents in multi-player bargaining (arXiv 2509.09071) | Qian et al. | academic | https://arxiv.org/abs/2509.09071 | 2025-09 | full (abstract) |
| HEROLD-2025 | Brave new procurement deals: an experimental study of how generative AI chatbots negotiate | Herold et al., Journal of Purchasing and Supply Management | academic | https://cris.maastrichtuniversity.nl/en/publications/brave-new-procurement-deals-an-experimental-study-of-how-generati/ | 2025-10 | full (abstract) |
| TREASURY-2024 | Treasury Announces Enhanced Fraud Detection Processes, Including Machine Learning AI, Prevented and Recovered Over $4 Billion in Fiscal Year 2024 | US Department of the Treasury | regulator | https://home.treasury.gov/news/press-releases/jy2650 | 2024-10-17 | full |
| NEUGROUP-2025 | Working Cash Flow Forecast Magic With Data Wizards and ML Models | NeuGroup | community | https://connect.neugroup.com/public/blogs/working-cash-flow-forecast-magic-with-data-wizards-and-ml-models | 2025-09-24 | full |
| TREASURYTODAY-2024 | Best Cash Flow Forecasting Solution Winner: AIA | Treasury Today (Adam Smith Awards Asia) | press | https://treasurytoday.com/?p=93746 | 2024-01 | full |
| DATARAILS-2026 | AI verification eats up 26% of finance teams' workweek: Datarails (CFO Dive) | CFO Dive; Datarails survey | survey | https://www.cfodive.com/news/ai-verification-eats-26percent-finance-teams-workweek-datarails/832210/ | 2026-10-06 | full |
| WAKEFIELD-2026 | CFOs insist on human oversight for AI in accounting, study finds (CFO Dive) | CFO Dive; Wakefield Research for Maximor AI | survey | https://www.cfodive.com/news/massive-trust-gap-hinders-cfo-ai-ambitions-study-finds/810786/ | 2026-01-28 | full |
| KPMG-2026 | KPMG Global AI in Finance 2026: The Decision Advantage | KPMG International | survey | https://assets.kpmg.com/content/dam/kpmgsites/kz/pdf/2026/06/AI-in-Finance-ENG.pdf | 2026-06 (from URL path; fielded March 2026) | full |
| NPS-2026 | Augmented Acquisition: Operationalizing Human-in-the-Loop AI to Accelerate Warfighting Capabilities (SYM-AM-26-091) | Naval Postgraduate School Acquisition Research Program | academic | https://dair.nps.edu/bitstream/123456789/5528/1/SYM-AM-26-091.pdf | 2026-04-30 | full |
| LEVELPATH-2025 | Levelpath press release on InnovaCare Health (BusinessWire) | Levelpath | vendor | https://www.businesswire.com/news/home/20250909861036/en | 2025-09-09 (from URL) | search-only |
| SUPCHAINS-2025 | Retail demand forecasting: reducing the error by 33% | N. Vandeput (SupChains) | firm | https://nicolas-vandeput.medium.com/retail-demand-forecasting-reducing-the-error-by-33-3aeba728954f | 2025-06 | search-only |
| KIRSHNER-2026 | Talking terms: Agent information in LLM supply chain bargaining | Kirshner et al., Decision Sciences | academic | https://onlinelibrary.wiley.com/doi/10.1111/deci.70010 | 2026 | search-only |
| INDIAMART-2025 | The new C-suite ally: generative AI | IndiaMART corporate blog | press | https://corporate.indiamart.com/2025/07/29/the-new-c-suite-ally-generative-ai | 2025-07-29 | search-only |

Source counts: 41 sources (36 opened and read, 5 search-only). By type: academic 12, community 1, firm 1, press 6, professional-body 6, regulator 5, standard-setter 1, survey 7, vendor 2.
