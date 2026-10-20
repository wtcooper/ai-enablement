# Function cards, people-hr and technology-it

Stream B backbone library. Researched 2026-10-20. In-house functions in any organization; firms that sell these services as their product are covered by the archetypes. For `technology-it` this card covers the IT function's own work (service desk, operations, software delivery, architecture). Security operations belongs to the security archetype; its entries are cited by id only.

Conventions used below:

- Grades follow the vocabulary (A = a figure the named organization reports as measured; B = named real deployment or study without a usable measured figure, or measured but the organization is unnamed or the process is adjacent; C = announcement or vendor claim; D = idea). A figure that is a survey recollection or a rough estimate is B unless the same source also reports a tracked metric, in which case the note says which part carries the grade. Search-only sources never carry A or B.
- Provenance is `self-reported`, `vendor-published` or `independent`. "Independent" is used only for academic, regulator or court measurement where the authors are not the deploying organization.
- Process lists and step-to-work-type tags are the advisor's own synthesis of how the work is organized, informed by the APQC process classification framework (top-level categories 7.0 and 8.0; group names verified in APQC-PCF-PAYOR-2019, recruiting sub-processes verified in APQC-PCF-2026). They are not claims about any named organization and carry no framework ids. Anything not tied to a source ref is marked "synthesis".
- Statistics state what they measure in the source's terms. Quotations are under 25 words. Maturity words follow the source ("announced", "piloting", "in production").

---

## 1. Summary

- **People (HR) has one strong, well-measured automation story and one strong controlled-trial story, and a large amount of regulatory and litigation exposure.** IBM reports that 94% of 11.5 million employee-HR interactions in 2024 were contained in its virtual agent (IBM-THINK-2025), after a forced cutover in 2018 that first dropped employee satisfaction to a score of -35. A pre-registered field experiment with about 70,000 applicants (CHICAGO-JABARIAN-2026) found that AI voice interviews, with humans still deciding, led to 12% more offers and about 18% more job starts and one-month retention than human-led interviews.
- **Screening and ranking is where HR AI goes wrong in public.** An audit study of LLM-based resume retrieval found white-associated names preferred in up to 85.1% of cases (UW-WILSON-2024; gender-only results were later corrected, race results unaffected). The UK regulator found recruitment tools that filtered by protected characteristics and inferred gender and ethnicity from names (ICO-RECRUIT-2024). A US court preliminarily certified an age-discrimination collective action over an applicant-ranking product (HRDIVE-MOBLEY-2025; CLEARINGHOUSE-MOBLEY-2026). The EU AI Act lists recruitment, selection, promotion, termination and worker monitoring tools as high-risk (EU-AIACT-ANNEX3-2024).
- **Software delivery has the best controlled evidence of any function, and it points in different directions depending on what is measured.** Task-level trials show faster work (Google 21%, ANZ 42%, a 2023 lab task 55.8%), one 2025 trial of experienced open-source developers on their own codebases found tasks took 19% longer (METR-RCT-2025), and METR said in February 2026 that its follow-up data are unreliable because developers refuse to work without AI (METR-UPLIFT-2026). System-level data show individual output up but delivery instability up (DORA-2024, DORA-2025) and no company-level correlation in one vendor's telemetry (FAROS-2025).
- **The binding constraint moves downstream.** Review, testing and release absorb the faster coding: pull-request review time rose 91% in one vendor dataset (FAROS-2025) and DORA reports AI now raises throughput but still raises instability (DORA-2025). The measured wins are in bounded, verifiable work: Google reports 80% of code modifications in landed changes in one migration were fully AI-authored (GOOGLE-MIG-2025), and Microsoft reports a 10-20% median pull-request completion-time improvement from a first-pass AI reviewer across 5,000 repositories (MS-CODEREVIEW-2025).
- **IT service desk automation reports 25-45% deflection, all self-reported or vendor-published.** Oracle's own IT team reports 25-30% ticket deflection (ORACLE-AISD-2025); an unnamed bank reports 45% of level-1 contacts deflected (HCL-BANK-2026, grade C). No source in this research reports mis-resolution, reopen or override rates for either function's assistants.
- **Both functions share the same operating lesson: simplify the process before automating it, and keep a clean human exit.** IBM removed policies before automating (consolidating over 25 leave types into one; IBM-THINK-2025). Oracle's bot opens a ticket for a human engineer when the employee says the problem is not solved (ORACLE-AISD-2025). A city's business chatbot that gave wrong legal answers shows the cost of a grounded assistant with no content owner or checking (MARKUP-NYCBOT-2024).
- **Role effects are real but mostly reported by the deployers.** HR partners handle the 6% that is not contained (IBM-THINK-2025); recruiters keep evaluation (CHICAGO-JABARIAN-2026); service engineers move to knowledge-base work and tier-2 (ORACLE-AISD-2025); engineers report they can fully delegate only 0-20% of their work (ANTHROPIC-WORK-2025) and worry about the skill needed to supervise AI.
- **Two organization-model moves are announced but unmeasured:** Moderna combined HR and IT under one officer to plan "work" rather than workforce or technology separately (UNLEASH-MODERNA-2025), and a DORA foreword reports an Adidas pilot in which loosely coupled architecture and fast feedback loops went with larger gains (DORA-2025, Foreword).

---

## 2. Item profiles

### 2.1 people-hr

**Main processes and key steps (synthesis; top-level category "Develop and Manage Human Capital", group names from APQC-PCF-PAYOR-2019 §7.0; recruiting sub-processes 7.2.1-7.2.5 confirmed in APQC-PCF-2026).**

| Process | Key steps | Work types |
|---|---|---|
| HR planning, policy and strategy | Align staffing plan to workforce plan; set policies; define competencies and job descriptions | `expert-judgment`, `data-reporting`, `document-production` |
| Recruit, source and select | Manage requisitions; recruit and source candidates; screen and select; make offers and manage hires; maintain applicant information (APQC-PCF-2026, recruiting measure page) | `transaction-processing`, `coordination-scheduling`, `client-interaction`, `expert-judgment` |
| Manage employee onboarding, development and training | Onboard; learning and certification; performance management; career and skills | `document-production`, `client-interaction`, `expert-judgment` |
| Employee relations | Handle cases and queries on conduct, grievances, policy exceptions; keep records | `expert-judgment`, `review-assurance` |
| Reward and retain | Pay, benefits, recognition; retention actions | `transaction-processing`, `data-reporting`, `expert-judgment` |
| Redeploy and retire | Transfers, promotions, separations, workforce moves | `transaction-processing`, `coordination-scheduling` |
| Employee information, inquiries and analytics | Answer employee inquiries; maintain employee data and HR systems; time and attendance; metrics; communication and engagement surveys | `client-interaction`, `transaction-processing`, `data-reporting` |

**Typical pain points.**

- Employees and managers send high volumes of repetitive questions and transactions, and policies differ by region. IBM describes siloed processes, inconsistent regional policies and manual, repetitive work behind its AskHR program (IBM-ASKHR-2025, "Start of a new era" section). Self-reported.
- Compliance work was growing with new laws while budgets shrank (IBM-THINK-2025, "What it means to be an AI-first enterprise"). Self-reported.
- Candidate volume is high and slow to work. In Chipotle's restaurant hiring, the time from application to start was reported as 12 days before the assistant (NRN-CHIPOTLE-2025). In Canada's Treasury Board Secretariat, the HR division wrote that in-person structured interviews make it hard to interview all candidates in a reasonable time and cost, and that rater bias remains a concern (TBS-AIA-2024, project description). Both are self-reported statements.
- Interview quality varies between recruiters. In the PSG Global Solutions experiment, human recruiters had substantial flexibility to change topics, wording and follow-ups under the same guidelines (CHICAGO-JABARIAN-2026, §1).
- Existing talent databases go unused. AdventHealth reports its databases held talent qualified for over 80% of requisitions that it had not been able to identify proactively (WORKDAY-ADVENTHEALTH-2025, "Challenge"). Vendor-published.
- Time released by AI has no destination unless leaders decide one. A Gartner survey of 114 HR leaders reportedly found only 7% of organizations give guidance on using time saved (GARTNER-HR-2026, search-only; not opened).

**Top AI opportunities (ladder x change scope), with graded evidence.**

| # | Opportunity | Pattern | Ladder | Scope | Runtime class | Best evidence (grade) |
|---|---|---|---|---|---|---|
| H1 | Employee HR assistant that answers from policy and completes transactions (letters, leave, manager moves), routing the rest to HR partners | `service-agent-escalation`, `grounded-knowledge-assistant` | automate | process | `managed-agent-runtime` | IBM AskHR, 94% containment of 11.5M interactions in 2024 (A, IBM-THINK-2025); Bosch ROB in rollout, no figures (B, BOSCH-PT-2024) |
| H2 | Candidate assistant: answers questions, collects basics, schedules interviews, issues offers | `service-agent-escalation`, `intake-triage` | automate | step to process | `workflow-automation` | Chipotle, 12 to 4 days application-to-start (B, NRN-CHIPOTLE-2025; WORKDAY-CHIPOTLE-2026) |
| H3 | AI voice interviewer collects structured information; human recruiters evaluate and decide | `other` (information collection by an agent) | automate | step | `workflow-automation` | Randomized field experiment, about 70,000 applicants (A, CHICAGO-JABARIAN-2026) |
| H4 | Automated structured behavioural interview scoring as one input, with every candidate still reviewed and an in-person alternative | `intake-triage` | augment | step | `workflow-automation` | Government of Canada pilot, no outcome published (B, TBS-AIA-2024) |
| H5 | Rediscover past applicants for new requisitions | `intake-triage` | augment | process | `workflow-automation` | AdventHealth, vendor-published (B, WORKDAY-ADVENTHEALTH-2025) |
| H6 | Simplify the policy set first (eliminate, simplify, automate), then automate what remains | `other` | any | process | n/a | IBM consolidated over 25 leave types to one (A for the program results, B for this step; IBM-THINK-2025) |
| H7 | Combine HR and IT planning so work, people and technology are designed together | `other` | any | model | n/a | Moderna, announced and in place, no outcome published (B, UNLEASH-MODERNA-2025) |
| H8 | LLM ranking or screening of resumes without audit | `intake-triage` | augment | step | `personal-assistant` | Counter-evidence: bias audit study (UW-WILSON-2024), regulator findings (ICO-RECRUIT-2024), litigation (HRDIVE-MOBLEY-2025). Do not recommend without a bias audit and human review |

Archetype entries cover learning, onboarding, skills inventories, early-career redesign, AI-led graduate screening and performance-system changes (ids in section 3.1). No public evidence was found in this research for employee-relations case triage or investigation drafting; treat as an open question, not an idea with support.

**Metrics and benchmarks.**

- Personnel cost to perform the recruit, source and select group, per new hire: median $1,879, sample 1,251 companies, APQC open-standards benchmark, not flagged as a key indicator (APQC-PCF-2026, measure page). Company-submitted data collected by a benchmarking body.
- Containment of employee inquiries: IBM reports 94% of 11.5 million interactions in 2024 were contained in the platform, meaning only 6% were routed to an HR Partner (IBM-THINK-2025). The same IBM sources also describe it as the share of common questions resolved and report a 75% reduction in support tickets since 2016 (IBM-ASKHR-2025). Definitions differ between IBM pages; use the "contained, not routed" wording.
- Employee satisfaction: IBM reports a net promoter score of -35 after the 2018 cutover and +74 at the time of writing (IBM-THINK-2025). Self-reported.
- Manager transaction speed: IBM reports managers complete HR transactions 75% faster with the roughly 90 automations (IBM-THINK-2025). Self-reported; baseline not stated.
- Hiring funnel: applications nearly doubled and completion rose from about 50% to over 85% at Chipotle (NRN-CHIPOTLE-2025). Company statement via press.
- Hiring quality: offers, job starts, retention at 30 to 120 days, customer-handling time, customer satisfaction and quality-assurance scores of hired workers (CHICAGO-JABARIAN-2026, §1). Use retention and downstream performance as the quality check on any screening change, not only speed.
- Fairness: selection-rate comparisons across groups on identical inputs (UW-WILSON-2024); the Canadian pilot planned accuracy against human evaluation and score differences across demographic groups (TBS-AIA-2024, project description).
- Adoption versus value: a Gartner survey of 110 heads of HR reportedly found 95% had implemented AI in some form in the prior year and about one in five reported significant or transformational value (GARTNER-HR-2026, search-only).

**Guardrails and decisions that need human judgment.**

- High-risk classification: EU Annex III item 4(a) covers AI for recruitment or selection, including targeting job ads, analysing and filtering applications and evaluating candidates; item 4(b) covers decisions on terms of work, promotion or termination, task allocation by behaviour or traits, and monitoring and evaluating performance (EU-AIACT-ANNEX3-2024, item 4). As of a 2026-07-01 law-firm briefing, the AI Omnibus extends the deadline for standalone high-risk systems to 2 December 2027, with the text still to be published in the Official Journal (AG-OMNIBUS-2026, "High-risk AI"). Confirm the current date before advising.
- Prohibited practice: AI that infers emotions of a person in the workplace is prohibited, with exceptions defined in the Act (EU-AIACT-ART5-2024, Art. 5(1)(f)).
- Worker notice: employers deploying a high-risk system at the workplace must inform workers' representatives and affected workers before use (EU-AIACT-ART26-2024, Art. 26).
- New York City Local Law 144 bars use of an automated employment decision tool unless it had a bias audit within the prior year, a public summary and notices to candidates; enforcement began 2023-07-05 (NYC-DCWP-AEDT-2023).
- UK regulator audit of recruitment tools led to almost 300 recommendations on fairness, data minimization and transparency to candidates (ICO-RECRUIT-2024).
- Litigation: a federal court preliminarily certified a collective action under the Age Discrimination in Employment Act on 2025-05-16 over Workday's AI recommendation system, later held to include applicants scored by its HiredScore features; Workday says the case is without merit and merits are unresolved (HRDIVE-MOBLEY-2025; CLEARINGHOUSE-MOBLEY-2026).
- Human decisions to keep: hire or no-hire; promotion, discipline and termination; pay changes; accommodation requests and alternatives to automated assessment; investigations; policy exceptions; escalation of distressed or sensitive cases. In Canada's pilot, hiring managers review all candidates regardless of score and candidates can request an alternative in-person assessment (TBS-AIA-2024, project description). Bosch states its assistant does not make decisions for associates (BOSCH-PT-2024).
- Frameworks: NIST AI RMF organizes risk work as govern, map, measure and manage (NIST-AIRMF-2023, Part 2) and its generative AI profile lists confabulation, harmful bias and data privacy among the risks (NIST-AI600-1-2024, §2).

**How roles change.**

- HR partners handle the complex remainder: only 6% of 2024 AskHR interactions were routed to a specialized HR partner (IBM-THINK-2025). In 2018 IBM discontinued HR partner support by phone and email for 21,000 first-line managers at once, to force the shift (IBM-THINK-2025).
- Recruiters move from running first-round interviews to evaluating them: the human recruiters in the experiment evaluated both AI-led and human-led interviews (CHICAGO-JABARIAN-2026, §1).
- HR and IT leadership can merge: Moderna's Chief People and Digital Technology Officer describes moving to "work planning" instead of siloed workforce or technology planning (UNLEASH-MODERNA-2025).
- Entry-level pipeline: 22% of CHROs reportedly said a business leader had stopped hiring for entry-level roles because of AI automation (GARTNER-HR-2026, search-only). The archetype entries on junior development carry the evidence in professional services.
- The Canadian pilot states it is not designed to change HR staff roles (TBS-AIA-2024, project description).

### 2.2 technology-it

**Main processes and key steps (synthesis; top-level category "Manage Information Technology", group names from APQC-PCF-PAYOR-2019 §8.0, which numbers it 8.0 as does APQC-PCF-2026). Security operations is covered by the security archetype.**

| Process | Key steps | Work types |
|---|---|---|
| IT customer relationships and business strategy | Understand demand; set IT strategy and roadmap; assess service-level compliance | `expert-judgment`, `coordination-scheduling`, `data-reporting` |
| Architecture and design | Evaluate options; record decisions; review designs against standards | `expert-judgment`, `research-synthesis`, `document-production`, `software-systems` |
| Build and change (software delivery) | Plan; code; test; review; integrate; migrate and upgrade | `software-systems`, `review-assurance` |
| Deploy and release | Package; approve change; deploy; verify; roll back | `software-systems`, `coordination-scheduling` |
| Run and operate | Monitor; handle incidents and problems; capacity; infrastructure configuration and licences | `data-reporting`, `software-systems`, `transaction-processing` |
| Service desk and user support | Triage issues and requests; provide resolution; fulfil requests (access, devices); escalate; confirm resolution | `client-interaction`, `transaction-processing` |
| Resilience, risk and continuity | Resilience planning; continuity and recovery actions; access and directory management | `review-assurance`, `expert-judgment` |
| Information and knowledge management | Manage data and content; keep knowledge base current | `data-reporting`, `document-production` |

**Typical pain points.**

- Developers lose time outside coding. In a vendor survey of 3,500 developers and managers, 50% reported losing 10 or more hours a week to non-coding work and 90% lost six or more; the same survey reports 68% save more than 10 hours a week with AI, so the two roughly cancel (ATLASSIAN-DEVEX-2025, sections on time saved and lost). Vendor-published, self-reported.
- Review becomes the bottleneck. In telemetry from over 10,000 developers in 1,255 teams, teams with high AI adoption merged 98% more pull requests while review time rose 91% (FAROS-2025, finding 1). Vendor-published; correlational.
- Delivery stability worsens. DORA's 2024 report estimated a 1.5% reduction in delivery throughput and a 7.2% reduction in delivery stability for every 25% increase in AI adoption (DORA-2024, "Exploring the downstream impact of AI", Figure 10); the 2025 report found AI adoption now improves throughput but still increases instability (DORA-2025, Key findings, p.4). Survey-based, independent of any one organization.
- Trust is low even among heavy users. In the 2025 Stack Overflow survey, more developers distrust the accuracy of AI tools (46%) than trust it (33%), 66% cite "almost right, but not quite" answers as their biggest frustration, and 45% say debugging AI-generated code takes longer (STACKOVERFLOW-2025, AI section).
- Service desks carry high volumes of repetitive requests. Oracle's IT employee support team handles about 50,000 tickets a month with a peak near 5,000 a day, and its earlier rule-based bot struggled with context (ORACLE-AISD-2025). Self-reported.
- Large migrations and upgrades are slow and costly: Amazon describes upgrade campaigns as costly, often taking months or years (AWS-QTRANSFORM-2024).
- Evaluating tools and understanding AI-written code are getting harder. Thoughtworks' April 2026 radar names "codebase cognitive debt" as code generated by AI is adopted without the mental models to reason about it (TW-RADAR-2026, themes). Practitioner publication.

**Top AI opportunities (ladder x change scope), with graded evidence.**

| # | Opportunity | Pattern | Ladder | Scope | Runtime class | Best evidence (grade) |
|---|---|---|---|---|---|---|
| T1 | IDE coding assistants for individual developers | `draft-review-loop` | assist | step | `personal-assistant` | Mixed, see section 5: faster in task trials (A, GITHUB-PENG-2023; GOOGLE-RCT-2024; ANZ-COPILOT-2024), slower in one trial of experienced maintainers (METR-RCT-2025), no company-level gain in telemetry (FAROS-2025) |
| T2 | Large migrations and upgrades run as AI-led programs, with engineers verifying and owners reviewing | `bulk-transformation` | augment to automate | process | `background-agent` or `workflow-automation` | Google int32 to int64 migration, 80% of landed code modifications AI-authored (A, GOOGLE-MIG-2025); Amazon Java upgrades (B, AWS-QTRANSFORM-2024) |
| T3 | AI first-pass pull-request review | `draft-review-loop` | augment | step | `workflow-automation` | Microsoft, 10-20% median PR completion-time improvement across 5,000 repositories (A, MS-CODEREVIEW-2025) |
| T4 | Service desk assistant grounded in the knowledge base, with a human ticket as the exit | `grounded-knowledge-assistant`, `service-agent-escalation` | automate | step to process | `workflow-automation` | Oracle IT, 25-30% deflection (A, ORACLE-AISD-2025); unnamed bank 45% (C, HCL-BANK-2026) |
| T5 | Incident triage, root-cause hints and mitigation suggestions for on-call engineers | `research-brief`, `monitor-diagnose-act` | augment | step | `background-agent` | Microsoft RCACopilot, accuracy up to 0.766 on a year of incidents, collection component in use over four years (A, MS-RCACOPILOT-2023); rank-ordering of likely code changes (B, archetype security-incident-response-08) |
| T6 | Delivery-flow redesign: value stream management and platform engineering so local gains reach customers | `other` | any | process | n/a | DORA 2025 reports value stream management acts as a force multiplier and seven AI capabilities amplify AI's effect (survey-based, not an organization example; DORA-2025, Key findings) |
| T7 | Drafting architecture decision records from context | `draft-review-loop` | assist | step | `personal-assistant` | Idea. Exploratory academic study only; GPT-4 zero-shot decisions were relevant and accurate but below human level (D, IIITH-ADR-2024) |
| T8 | Knowledge and repository clean-up | `bulk-transformation` | augment | step | `workflow-automation` | Archetype professional-services-knowledge-management-07 (B) |

**Metrics and benchmarks.**

- DORA software delivery factors: throughput (lead time for changes, deployment frequency, failed deployment recovery time) and instability (change fail rate, rework rate) (DORA-2025, "Software delivery performance", p.13). Use all five; throughput alone will mislead.
- AI adoption and effects at company scale: DX reports adoption above 93% across close to 500 companies from 2025-10-17 to 2026-02-01, 3.9 hours a week saved on average (self-reported in a periodic survey) and 27.4% of merged code AI-authored (from system data); DX also says there is no "average experience" and some companies are speeding up as quality degrades (DX-AIIMPACT-2026, pp.2-5, Methodologies). Vendor-published.
- Acceptance as a quality signal: in the UK government trial, telemetry showed 15.8% of suggested code lines accepted for GitHub Copilot, and 39% of users reported committing suggested code (UK-GDS-AICA-2025, executive summary).
- Service desk: deflection rate, share of queries resolved by the AI, ticket volume, resolution time, employee satisfaction and support-engineer productivity are the metrics Oracle's IT team says it tracks (ORACLE-AISD-2025, "Results"). No cost-per-ticket or reopen benchmark was found from a source that could be opened.
- Code quality and security: the Veracode 2025 report found AI-generated code introduced security flaws in 45% of tests across over 100 models, with larger models not safer (VERACODE-2025). Vendor-published, tested on prompts chosen by the vendor.
- Review load: pull-request review time, pull-request size and bugs per developer rose in high-adoption teams (+91%, +154%, +9%) in vendor telemetry (FAROS-2025).

**Guardrails and decisions that need human judgment.**

- Framework: NIST AI RMF (govern, map, measure, manage; NIST-AIRMF-2023) and the generative AI profile, which names confabulation (confidently stated but false content), information security and value-chain risks (NIST-AI600-1-2024, §2).
- Agent actions and tool supply chain have produced real incidents. AWS reported that an over-scoped repository token let an attacker commit malicious code into an AI coding extension release (version 1.84.0); AWS said the code did not execute because of a syntax error (AWS-BULLETIN-2025, 2025-07-23). A SaaS founder reported that an AI coding service deleted a production database despite an instruction to freeze code; this is the user's account as reported by the press, not a vendor finding (REGISTER-REPLIT-2025).
- Human decisions to keep: release and rollback approval, destructive operations on production data, access grants and privileged scopes, acceptance of AI-written changes into critical systems, architecture trade-offs that need organizational context. Anthropic's engineers said they keep high-level design and "taste" decisions and delegate more verifiable work (ANTHROPIC-WORK-2025, interviews section).
- Review must stay real. Google engineers had to revert some model-made changes even after AI authored most of the change, and the program invested in AI verification to reduce that burden (GOOGLE-MIG-2025, §IV). Microsoft keeps human review and uses AI for a first pass (MS-CODEREVIEW-2025).
- EU AI Act: IT's internal tools are not high-risk by default; they become so if used for workforce decisions in Annex III item 4 (see people-hr). AI literacy and transparency duties are outside what was verified here.
- Data and IP: DX flags unmanaged "shadow AI" usage and the need for acceptable-use policies (DX-AIIMPACT-2026, "Shadow AI" section). The UK government trial notes that its central licence pool depended on sponsorship inside each organization (UK-GDS-AICA-2025, limitations).

**How roles change.**

- Engineers become orchestrators and reviewers. Faros describes developers initiating, unblocking and validating AI contributions across more parallel workstreams (FAROS-2025, finding 2). Vendor interpretation.
- Delegation remains narrow: more than half of surveyed Anthropic engineers said they can fully delegate only 0-20% of their work, and some worried that supervising AI needs coding skills that could atrophy (ANTHROPIC-WORK-2025, survey and interviews). Self-reported by a company that builds the tool.
- Migration work needs fewer coordinating people: a single engineer could generate all necessary changes in Google's int32 to int64 migration, which also cut communication overhead (GOOGLE-MIG-2025, §IV).
- Service engineers spend freed time on knowledge-base quality and specialized tier-2 support (ORACLE-AISD-2025).
- Junior effects: DX reports junior engineers use AI the most and daily-using juniors now match seniors in time savings (DX-AIIMPACT-2026, pp.9-10). Vendor-published.

---

## 3. Examples

### 3.1 people-hr

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| P-E1 | IBM (technology) | AskHR virtual agent became the front door for HR: phone and email support for 21,000 first-line managers was discontinued in 2018; the agent answers, runs about 90 automations, and routes the rest to HR partners; policies were simplified first (over 25 leave types merged into one). Described as moving to watsonx Orchestrate agents in 2025 | automate / process | In 2024, more than 11.5 million interactions, 94% contained in the platform (6% routed to an HR partner); over one million transactions; NPS -35 after the cutover and +74 now; managers complete HR transactions 75% faster; HR operating budget down 40% over four years (IBM says AskHR "contributed"; other causes not separated). Self-reported | A | IBM-THINK-2025; IBM-ASKHR-2025 |
| P-E2 | PSG Global Solutions, a Teleperformance subsidiary (business process outsourcing, customer-service recruiting in the Philippines) | AI voice agents conducted the structured interview for entry-level customer-service applicants; human recruiters evaluated all interviews and made all hiring decisions; applicants were randomly assigned to human or AI interviewers, and a third group could choose | automate / step | 70,884 applications. Offers 9.73% with AI vs 8.70% with humans (12% higher); job starts 18% higher and employment of at least one month 18% higher; no significant difference in customer-handling time, customer satisfaction or quality-assurance score of hires; when given a choice, 78% chose the AI, and those who did had lower language and analytical test scores. Independent academic study; the firm supplied data, and one author later took an unpaid role at the firm (disclosed) | A | CHICAGO-JABARIAN-2026, §1, §2, Disclosure note |
| P-E3 | Chipotle (restaurants, retail) | "Ava Cado" conversational assistant answers candidate questions, collects basics, schedules interviews and sends offers for in-restaurant roles | automate / step to process | Time from application to start down from 12 days to four; applications nearly doubled; completion up from about 50% to over 85%; company also says up to 75% reduction in time to hire (the two figures are different measures and were not reconciled). Company statements relayed by press and a vendor page; Chipotle's own release could not be opened | B | NRN-CHIPOTLE-2025; WORKDAY-CHIPOTLE-2026 |
| P-E4 | AdventHealth (healthcare) | Recruiters use a tool that resurfaces past applicants for each new requisition, including candidates who withdrew or applied to a different role | augment / process | 1,032 hires in critical roles; requisitions closed up 100%; 77% of nursing requisitions covered by past applicants; offer rate 50% higher for rediscovered candidates than other external candidates; an AdventHealth executive says about 655 nurses were recruited in the first year. Vendor-published page with an executive quote; baseline definitions not given | B | WORKDAY-ADVENTHEALTH-2025 |
| P-E5 | Treasury Board Secretariat, Government of Canada (public sector) | Pilot of an automated structured behavioural interview scored by a vendor tool for AS-01, AS-02 and EX-01 pools; results are one input; all candidates reviewed regardless of score; opt-out to an in-person assessment; planned testing of accuracy against human raters and score differences across demographic groups | augment / step | None published. The Algorithmic Impact Assessment, published 2024-02-28, lists project phase "Implementation", impact level 1, and intended benefits of speed and consistency that are objectives, not results. Self-reported | B | TBS-AIA-2024 |
| P-E6 | Bosch (manufacturing and technology) | ROB, a generative AI HR assistant for associates, guides users through self-service steps and points to specific HR policies from the My HR knowledge base; disclaimer that it is AI; conversations not recorded; said to be rolled out to the majority of Bosch countries | automate / step | None published. Bosch UK author says it does not make decisions on behalf of associates. Self-reported | B | BOSCH-PT-2024 |
| P-E7 | Moderna (biotechnology) | HR and digital technology combined into one People and Digital Technology department under one chief officer, to plan "work" across people, process and technology | any / model | None published. Interview with the officer; announced and in place as of 2025-06-27 | B | UNLEASH-MODERNA-2025 |

Archetype use-case ids with `function: people-hr` (id and grade only; not re-researched):
assurance-quality-management-10 B, -25 C;
professional-services-firm-finance-13 C; professional-services-scoping-pricing-13 B; professional-services-staffing-resourcing-10 C;
professional-services-talent-learning-01 B, -02 B, -03 B, -04 B, -05 B, -06 C, -07 B, -08 B, -09 C, -11 A, -12 C, -13 B, -14 B, -15 B, -16 A, -17 C, -18 C, -21 B, -22 B, -23 D, -24 D, -25 D;
security-governance-risk-20 C, -21 D; security-human-risk-12 B; tax-compliance-individual-business-20 B.

### 3.2 technology-it

| # | Organization (industry) | What changed in the work | Ladder / scope | Outcome and provenance | Grade | Ref |
|---|---|---|---|---|---|---|
| T-E1 | Google (technology; Ads product area) | Int32 to int64 ID migration across a 500-million-line code base: LLM-powered tooling finds locations, edits files, updates tests; the same engineer checks and fixes; changes are sharded to code owners for review | augment / process | 80% of code modifications in landed changes fully AI-authored, tracked by comparing the first AI-generated changelist with the committed version per character; total migration time reduced by an estimated 50% as reported by the engineers (an estimate, not tracked); humans often had to revert some model changes. Experience report, not a controlled study. Self-reported | A (80% is tracked; the 50% is an estimate) | GOOGLE-MIG-2025, §III, §IV |
| T-E2 | UK central government (public sector) | Trial of AI coding assistants for developers and engineers, 1,900 licences assigned in a trial of 2,500 across more than 50 organizations, November 2024 to February 2025 | assist / step | 56 minutes saved per working day on average, self-reported in 424 survey responses from 31 departments (report notes possible overestimation); Copilot telemetry showed 15.8% of suggested lines accepted; 58% of respondents would not want to go back; satisfaction 6.6 of 10; telemetry for one month was missing. Self-reported by the government team that ran the trial | A (telemetry is tracked; the time saving is survey-based) | UK-GDS-AICA-2025, executive summary, methodology and limitations |
| T-E3 | Oracle (technology; own IT employee support) | Slack-based AI service desk using retrieval over the internal knowledge base replaced a keyword bot; employees confirm "solved" or are routed to a form that opens a ticket for a human engineer; engineers use freed time on knowledge-base work and tier-2 | automate / step | Ticket deflection of 25-30%, equal to 3,100-4,000 tickets a week of about 50,000 a month; released early 2024. Self-reported by Oracle IT, which also sells the underlying cloud service | A | ORACLE-AISD-2025 |
| T-E4 | Microsoft (technology; internal engineering) | AI reviewer leaves comments on pull requests as a first pass before human reviewers; authors can configure it to run automatically | augment / step | Scaled from an experiment to over 90% of pull requests, over 600,000 per month; 10-20% median PR completion-time improvement across 5,000 onboarded repositories, per "early experiments and data science studies" (not a randomized trial; the post does not say how repositories were chosen). Self-reported | A | MS-CODEREVIEW-2025 |
| T-E5 | Microsoft (technology; cloud services) | On-call system matches incidents to handlers, gathers diagnostic data, predicts the root-cause category and writes an explanation for the on-call engineer | augment / step | Root-cause accuracy up to 0.766 on one year of real Microsoft incidents (offline evaluation); the diagnostic-collection component has been in use at Microsoft for over four years. Self-reported by researchers at the deploying organization | A | MS-RCACOPILOT-2023, abstract |
| T-E6 | ANZ Bank (financial services) | Six-week experiment with GitHub Copilot: Python challenges solved by randomly split groups that swapped, then reported early data from about 1,000 engineers using it at scale | assist / step | Copilot group completed tasks 42.36% faster than control; code quality improved and security impact was inconclusive; participants were not monitored, groups were not independent, and the tasks were algorithmic challenges rather than bank work. Self-reported | A (task measurement; scope limited) | ANZ-COPILOT-2024, abstract, results |
| T-E7 | Amazon (retail and technology) | Code-transformation agent upgrades applications from Java 8 or 11 to Java 17 across tens of thousands of production applications | automate / process | "Over 4,500 years" of developer work saved for over a thousand developers, estimated from the number of Java dependencies migrated; $260 million in annual cost savings from hosts removed. The blog calls both estimates conservative; they are estimates, not measured effort. Vendor-published, self-reported | B | AWS-QTRANSFORM-2024 |
| T-E8 | Adidas (retail and consumer goods) | Generative AI pilot across a development organization of nearly a thousand developers | assist / step | Per a foreword, teams with loosely coupled architectures and fast feedback loops saw 20-30% productivity gains "as measured by increases in commits, pull requests, and overall feature-delivery velocity" and a 50% increase in "Happy Time"; teams tightly coupled to ERP systems saw "little or no AI benefits". Quoted in a third-party report foreword; the primary source was not opened | B | DORA-2025, Foreword |
| T-E9 | A global consumer bank, unnamed (financial services) | AI-led omnichannel support: conversational self-service, agent assistance and workflow automation for employee support | automate / step | 45% of level-1 contacts deflected to self-service from over 60,000 tickets a month; the page also says first-contact resolution rose and handle time fell, with no figures. Vendor-published, client unnamed | C | HCL-BANK-2026 |
| T-E10 | Morgan Stanley (financial services) | Internal tool turns legacy code in COBOL and similar languages into plain-English specifications for engineers to rewrite | augment / process | Company reportedly said it saved about 280,000 hours since January 2025 (reports describe it as company-reported and unverified). Seen only in search results; article body not retrieved, so cannot carry a higher grade | C (search-only) | MS-DEVGEN-2025 |
| T-E11 | None found in production (idea) | Idea: drafting architecture decision records from the decision context | assist / step | None published. An exploratory study tested language models on generating the decision part of records from the context; GPT-4 zero-shot output was relevant and accurate but below human level, and smaller tuned models could be comparable. Idea | D | IIITH-ADR-2024, abstract |

Archetype use-case ids with `function: technology-it` that sit outside security operations (id and grade only; not re-researched):
professional-services-knowledge-management-07 B, -10 C; tax-compliance-corporate-20 C; tax-compliance-individual-business-10 D; tax-data-technology-18 C; tax-indirect-tax-16 C.

Archetype use-case ids with `function: technology-it` in the security archetype, cited by id and grade only (the security archetype owns them):
security-ai-security: -05 C, -06 B, -07 C, -08 A, -09 B, -10 A, -11 B, -12 B, -14 A, -16 D;
security-application-security: -01 B, -02 C, -04 A, -05 B, -06 B, -07 A, -08 B, -09 C, -10 A, -12 B, -13 B, -14 B, -15 B, -16 B;
security-cloud-infrastructure: -01 C, -02 B, -03 B, -04 C, -05 C, -06 B, -07 C, -08 C, -09 C, -10 C, -11 C, -12 D, -13 C, -14 C, -15 C, -16 B, -17 D, -18 C, -19 D, -20 D, -22 B, -23 C, -24 D;
security-data-privacy: -01 B, -02 A, -03 C, -04 C, -05 B, -06 C, -07 B, -08 C, -09 C, -10 C, -11 C, -12 C, -14 B, -16 D, -17 D, -18 D, -19 C, -21 B;
security-human-risk: -01 A, -02 B, -03 C, -04 B, -05 C, -07 B, -08 B, -09 D, -10 B, -14 B, -15 C, -16 C, -17 D, -18 D;
security-identity-access: -01 B, -02 C, -03 B, -04 C, -05 B, -06 B, -07 C, -08 C, -09 C, -10 C, -11 D, -12 B, -13 C, -14 C, -15 C, -16 C, -17 B, -18 B;
security-incident-response: -08 B;
security-operations: -01 A, -02 A, -03 B, -04 B, -06 C, -07 B, -08 B, -09 A, -10 B, -11 B, -12 A, -13 B, -14 B, -15 A, -16 B, -17 B, -18 B, -19 C, -20 C, -21 A, -23 B, -24 D;
security-threat-intelligence: -01 D, -02 B, -03 C, -04 C, -05 B, -06 B, -07 D, -08 C, -09 C, -10 B, -11 B, -12 B, -14 C, -15 B, -16 B, -17 C, -18 C, -19 B, -21 A, -22 A, -23 B;
security-vulnerability-exposure: -02 A, -03 A, -05 B, -06 B, -07 B, -08 B, -09 C, -10 C, -11 B, -13 A, -14 C, -15 C, -16 D, -21 B, -22 C, -24 D, -25 D;

---

## 4. Expert moves and probes

### 4.1 people-hr

1. **"Of the HR questions you get in a month, what share are lookups, what share are transactions, and what share need a person's judgment?"** Splits the work into the part an assistant can contain and the part it cannot, and shows whether the leader has counted. IBM's 94% containment rests on a long program that added about 90 automations and over a million transactions, not only answers (IBM-THINK-2025).
2. **"Which policies would you delete or merge before you automate anything?"** IBM's "eliminate, simplify, automate" rule consolidated over 25 leave types into one before automation (IBM-THINK-2025). Reveals whether complexity is a design problem the team can remove, and whether the process owner has authority to simplify.
3. **"When the assistant cannot answer, who picks it up, how fast, and how do you know it did not just frustrate the employee?"** Tests the exit. IBM's forced cutover dropped NPS to -35 before it recovered to +74 (IBM-THINK-2025); the Oracle IT design shows an explicit "still need help" route to a human (ORACLE-AISD-2025). Reveals whether the plan measures satisfaction and escalation, not only containment.
4. **"Where in hiring does a person decide, and what does that person see?"** The PSG study separated automated information collection from human evaluation (CHICAGO-JABARIAN-2026, §1); the Canadian pilot reviews every candidate (TBS-AIA-2024). Reveals whether the AI is a filter that removes candidates unseen, which is where regulation and litigation concentrate.
5. **"Show me the selection rates by group for last quarter, and who audited them."** NYC requires a bias audit within a year before use (NYC-DCWP-AEDT-2023); the UK regulator found tools filtering on protected characteristics (ICO-RECRUIT-2024); an audit study found strong name-based preferences in LLM retrieval (UW-WILSON-2024). Reveals whether fairness is measured on outcomes or assumed because the vendor says so.
6. **"What does a good hire look like 90 days later, and have you checked that the faster process keeps it?"** The PSG study tested retention at 30 to 120 days and downstream handling-time, satisfaction and quality scores (CHICAGO-JABARIAN-2026, §1). Chipotle reports speed and completion but not downstream quality (NRN-CHIPOTLE-2025). Reveals whether speed is being bought at the expense of fit.
7. **"Which of your HR tools score, rank or filter people, which jurisdictions do those people live in, and who owns the inventory?"** Annex III item 4 covers recruitment, selection, promotion, termination, task allocation and monitoring (EU-AIACT-ANNEX3-2024); Workday's product was pulled into litigation on how its recommendations scored applicants (HRDIVE-MOBLEY-2025). Reveals shadow tools and vendor features turned on by default.
8. **"If HR gets 30% of its time back, where does that time go, and who decided?"** Gartner reportedly found few organizations give guidance on using time saved (GARTNER-HR-2026, search-only). IBM asks the same of its own teams (IBM-THINK-2025). Reveals whether the business case has a destination for capacity.
9. **"Who owns the content the assistant answers from, and how often is it checked against current law and policy?"** A city's grounded business chatbot told users illegal things and was still live when reported (MARKUP-NYCBOT-2024). Reveals the stale-content and no-owner failure mode.

### 4.2 technology-it

1. **"Where does a pull request wait now, and how long?"** Review time rose 91% in high-adoption teams (FAROS-2025) and DORA says speed gains meet downstream limits (DORA-2025). Reveals whether coding speed is the real constraint or whether review, test and release are.
2. **"Do you measure instability (change fail rate, rework) next to throughput?"** DORA's 2024 and 2025 reports both found instability rising with AI use (DORA-2024; DORA-2025). Reveals whether a productivity story is being told from throughput alone.
3. **"Was that productivity number measured on tasks, on teams or on the company, and by whom?"** Task trials (21%, 42%, 55.8%) differ from METR's 2025 slowdown for experienced maintainers, and company-level correlation was absent in telemetry (GOOGLE-RCT-2024; ANZ-COPILOT-2024; GITHUB-PENG-2023; METR-RCT-2025; FAROS-2025). METR also found developers believed they were 20% faster when they were 19% slower (METR-RCT-2025, abstract). Reveals the gap between felt and measured gains.
4. **"Which of your migrations or upgrades are bounded, testable and repeated enough to run as a program?"** Google's and Amazon's results come from well-defined migrations with tests, reviewers and sharding (GOOGLE-MIG-2025; AWS-QTRANSFORM-2024). Reveals the best candidates for `bulk-transformation` and the ones that need human design.
5. **"What fraction of AI-suggested code is accepted, and what happens to what is rejected?"** The UK trial saw 15.8% of Copilot lines accepted (UK-GDS-AICA-2025). Reveals shallow use, trust problems and where review load comes from.
6. **"What share of service desk tickets would you let an assistant close without a person, what is the check, and what is the exit?"** Oracle reports 25-30% deflection with a human ticket as the exit (ORACLE-AISD-2025). Reveals the current containment ceiling and whether re-opens and wrong answers are counted.
7. **"Which actions can an agent take on production without approval, with what credentials?"** The over-scoped token in an AI extension and the reported database deletion show scope and permission failures (AWS-BULLETIN-2025; REGISTER-REPLIT-2025). Reveals least-privilege design and approval gates before any `delegate` step.
8. **"Who on the team can still explain the system without the AI?"** Thoughtworks names cognitive debt (TW-RADAR-2026) and Anthropic engineers describe a "paradox of supervision" (ANTHROPIC-WORK-2025). Reveals skill and comprehension risk behind faster delivery.
9. **"Where do developers lose their time outside coding, and has any of the AI saving been spent there?"** The Atlassian survey found time saved and time lost roughly equal (ATLASSIAN-DEVEX-2025). Reveals whether the savings are visible or absorbed by friction the organization has not fixed.

---

## 5. Evidence on what works and what fails

**Controlled and field measurements (software delivery)**

- **Experienced maintainers were slower in 2025.** Randomized controlled trial: 16 developers, 246 tasks in mature open-source projects they knew; allowing AI raised completion time by 19% while they predicted a 24% reduction beforehand and estimated 20% afterward; experts predicted 38-39% reductions. Independent (METR-RCT-2025, abstract). The authors say it does not mean AI is unhelpful in other settings.
- **The follow-up is unreliable.** In February 2026 METR reported that its second study (57 developers, from August 2025) gave "an unreliable signal" because many developers declined to work without AI; its raw estimates of the change in task time were -18% (interval -38% to +9%) for returning developers and -4% (interval -15% to +9%) for newly recruited ones, where negative means less time and both intervals include zero, and it said selection effects likely bias the estimate towards no speedup (METR-UPLIFT-2026). A May 2026 survey of 349 technical workers found a median 1.4-2x self-reported change in value of work, and METR itself says surveys tend to overstate relative to experiments (METR-SURVEY-2026). Independent.
- **Earlier trials found large task-level gains.** 55.8% faster on an HTTP-server task with Copilot (GITHUB-PENG-2023); about 21% faster on an enterprise task for 96 Google engineers, with a large confidence interval (GOOGLE-RCT-2024); 42.36% faster at ANZ on algorithmic tasks (ANZ-COPILOT-2024). All used constructed or constrained tasks.
- **Maintainability showed no signal either way.** A preregistered two-phase experiment with 151 participants found no significant difference in time or quality when other developers evolved AI-co-developed code without AI; the authors flag code bloat and "cognitive debt" as risks for later work (LUND-BORG-2025, abstract). Independent.
- **Company-level data show a gap.** DORA 2024 estimated -1.5% throughput and -7.2% stability per 25% increase in AI adoption (DORA-2024); DORA 2025 (nearly 5,000 respondents surveyed 2025-06-13 to 2025-07-21) found throughput now improves but instability still increases, 90% use AI, and 30% report little or no trust in AI-generated code (DORA-2025, p.4). Faros found no significant correlation between AI adoption and company-level outcomes across 10,000 developers, with 91% longer review times and 9% more bugs per developer in high-adoption teams (FAROS-2025). DX, with a different dataset, reports modest and varied quality effects and some companies degrading (DX-AIIMPACT-2026). DORA is a survey; Faros and DX are vendors.
- **Code security.** 45% of tests produced insecure code across over 100 models (VERACODE-2025, vendor-published); the 2022 and 2023 academic evidence on users writing less secure code with assistants is in the security archetype.
- **Self-reported gains inside builders.** Anthropic's survey of 132 engineers reported its tool used in about 60% of their work and a 50% self-reported productivity gain, alongside a 67% rise in merged pull requests per engineer per day after adoption; the company lists convenience sampling and social-desirability bias as limits (ANTHROPIC-WORK-2025, survey and limitations). Self-reported.

**Customer-support evidence adjacent to the IT service desk (grade cap B)**

- A staggered rollout of an AI assistant to 5,179 customer-support agents raised issues resolved per hour by 14% on average and 34% for novices and low-skilled workers, with minimal effect for experienced workers (NBER-BRYNJOLFSSON-2023, abstract). Independent academic study of customer support; adjacent to, not the same as, an internal IT service desk.

**HR evidence**

- **Controlled trial of AI interviews.** See P-E2. Quality held on retention and measured performance; interviews were rated less natural by applicants; applicants who chose AI had lower test scores, a negative sorting that matters if choice is offered (CHICAGO-JABARIAN-2026, §1).
- **Bias in LLM-based resume retrieval.** Over three million comparisons found white-associated names preferred in up to 85.1% of cases, and Black male names disadvantaged in up to 100% of intersectional comparisons; the authors disclosed on 2026-08-29 a code bug that inverts the gender-only comparisons, while race-only and intersectional results were replicated by another university (UW-WILSON-2024, v3 note and abstract). Do not cite the gender-only figures from the original abstract. Independent; a simulation, not a deployed tool.
- **Regulator findings.** The UK ICO's audits of recruitment-tool providers produced almost 300 recommendations; some tools let recruiters filter out candidates with protected characteristics, some inferred gender and ethnicity from names, and some retained data indefinitely; providers accepted or partly accepted all of them (ICO-RECRUIT-2024). Independent.
- **Litigation.** Preliminary collective certification (2025-05-16), extension to HiredScore (2025-07), notice plan (2025-12-02) and a 2026-06-22 order on a motion to dismiss; the case continues and no merits finding was found (CLEARINGHOUSE-MOBLEY-2026, docket; HRDIVE-MOBLEY-2025).
- **Containment and satisfaction at scale.** IBM's AskHR is the only HR program in this research with year-over-year tracked containment and satisfaction; IBM says no employees used it in 2017 and it forced the shift in 2018 by shutting the phone and email routes (IBM-THINK-2025). Self-reported.
- **Grounded-assistant failure.** NYC's business chatbot told users employers may take workers' tips and that landlords need not accept housing vouchers, both wrong, per investigative testing in March 2024 (MARKUP-NYCBOT-2024). Not an HR tool, but the same grounded-answer pattern applies to employee policy questions.

**Absence of evidence, stated plainly**

- No source gave error rates, override rates, escalation-then-reopen rates or independent audits of an employee-facing HR or IT assistant.
- No parallel-run results were found for either function's assistants.
- No independent measurement of IT service desk deflection exists in the sources read; every figure is the deploying organization's or its vendor's.
- No public evidence was found for AI in HR employee-relations case work or in IT architecture practice beyond one exploratory academic study.

---

## 6. Gaps

- **Blocked or not opened.** Gartner press releases (search results only: GARTNER-HR-2026), SHRM's 2026 State of AI in HR full report (landing page only), ISO/IEC 42001 (blocked), Chipotle's own investor release (access denied), Business Insider's Morgan Stanley article (body not returned), the Puerto Rico Oversight Board hiring-platform pilot page (blocked), and the SSRN version of the multi-company Copilot field experiments (blocked; its 26% throughput figure appears only as cited in GOOGLE-RCT-2024).
- **Unverified claims left out.** A reported Bank of America figure of a 50% fall in IT service-desk calls from its employee assistant was not found in any source that could be opened. A reported 90% reduction in time to hire at Unilever appears in a vendor case study with no date and conflicts with 75% in other Unilever-linked sources; it was left out. Siemens's HR chatbot and Walmart's employee assistant surfaced in search but had no dated, measured source.
- **Jurisdiction coverage.** Colorado's AI Act, Illinois' amendment on AI in employment and California's regulations on automated-decision systems in employment were not opened. Only the EU, New York City, the UK regulator and US litigation are cited.
- **EU timing.** The deadline shift for high-risk obligations rests on a law firm's 2026-07-01 briefing; the Official Journal publication was not checked.
- **People-hr evidence is thin outside recruiting and the employee assistant.** Nothing measured was found for employee-relations triage, workforce planning with AI, performance-review drafting or benefits administration outside the professional-services archetype entries.
- **Technology-it evidence is thin outside software delivery.** Service desk numbers are single-source and unaudited; no non-security operations agent with published results; architecture review has only an exploratory study; no data on change approval or release management with AI.
- **METR 2026 data.** The follow-up study's raw numbers are published but described by its authors as unreliable; a redesigned study was announced and no results had been published in the pages read.
- **Quality evidence missing for both functions.** See "Absence of evidence" in section 5.
- **Dates inferred.** The Oracle service-desk blog shows no byline date; 2025-10 is inferred from the upload paths of its images. IBM and Workday dates come from page metadata. DORA 2024 is dated by year only because the report shows no release date.

---

## 7. Sources

All accessed 2026-10-20. Access is `full` unless stated. Keys reused from the archetype YAML: NBER-BRYNJOLFSSON-2023, EU-AIACT-ANNEX3-2024, AG-OMNIBUS-2026, ICO-RECRUIT-2024.

| Ref | Title | Publisher or author | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| METR-RCT-2025 | Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity | METR; Becker, Rush, Barnes, Rein (arXiv 2507.09089) | academic | https://arxiv.org/pdf/2507.09089 (summary: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | 2025-07-25 | full |
| METR-UPLIFT-2026 | We are Changing our Developer Productivity Experiment Design | METR | academic | https://metr.org/blog/2026-02-24-uplift-update/ | 2026-02-24 | full |
| METR-SURVEY-2026 | Measuring the Self-Reported Impact of Early-2026 AI on Technical Worker Productivity | METR; Becker | academic | https://metr.org/blog/2026-05-11-ai-usage-survey/ | 2026-05-11 | full |
| DORA-2025 | 2025 State of AI-assisted Software Development | Google Cloud, DORA | survey | https://services.google.com/fh/files/misc/2025_state_of_ai_assisted_software_development.pdf (announcement: https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) | 2025-09-23 | full |
| DORA-2024 | Accelerate State of DevOps 2024 | Google Cloud, DORA | survey | https://services.google.com/fh/files/misc/2024_final_dora_report.pdf | 2024 | full |
| NBER-BRYNJOLFSSON-2023 | Generative AI at Work (NBER Working Paper 31161), revised Nov 2023 | NBER; Brynjolfsson, Li, Raymond | academic | https://www.nber.org/papers/w31161 (PDF read: https://www.nber.org/system/files/working_papers/w31161/w31161.pdf) | 2023-11 | full |
| GOOGLE-MIG-2025 | How is Google using AI for internal code migrations? | Google; Nikolov et al. (arXiv 2501.06972) | firm | https://arxiv.org/pdf/2501.06972 | 2025-01-12 | full |
| GOOGLE-RCT-2024 | How much does AI impact development speed? An enterprise-based randomized controlled trial | Google; Paradis et al. (arXiv 2410.12944) | firm | https://arxiv.org/pdf/2410.12944 | 2024-11-11 | full |
| GITHUB-PENG-2023 | The Impact of AI on Developer Productivity: Evidence from GitHub Copilot | Microsoft Research, GitHub, MIT Sloan; Peng et al. (arXiv 2302.06590) | academic | https://arxiv.org/pdf/2302.06590 | 2023-02-13 | full |
| MS-INCIDENT-2023 | Recommending Root-Cause and Mitigation Steps for Cloud Incidents using Large Language Models | UC Davis, Microsoft; Ahmed et al. (arXiv 2301.03797) | academic | https://arxiv.org/pdf/2301.03797 | 2023-02-09 | full |
| MS-RCACOPILOT-2023 | Automatic Root Cause Analysis via Large Language Models for Cloud Incidents | Microsoft and universities; Chen et al. (arXiv 2305.15778) | academic | https://arxiv.org/pdf/2305.15778 | 2023-11-13 | full |
| IIITH-ADR-2024 | Can LLMs Generate Architectural Design Decisions? An Exploratory Empirical Study | IIIT Hyderabad; Dhar, Vaidhyanathan, Varma (arXiv 2403.01709) | academic | https://arxiv.org/pdf/2403.01709 | 2024-03-04 | full |
| LUND-BORG-2025 | Echoes of AI: Investigating the Downstream Effects of AI Assistants on Software Maintainability | Lund University, CodeScene, Equal Experts; Borg et al. (arXiv 2507.00788) | academic | https://arxiv.org/pdf/2507.00788 | 2026-02-26 | full |
| UK-GDS-AICA-2025 | AI coding assistant trial: UK public sector findings report | Government Digital Service, UK government | regulator | https://www.gov.uk/government/publications/ai-coding-assistant-trial/ai-coding-assistant-trial-uk-public-sector-findings-report | 2025-09-12 | full |
| ANZ-COPILOT-2024 | The Impact of AI Tool on Engineering at ANZ Bank: An Empirical Study on GitHub Copilot within Corporate Environment | ANZ; Chatterjee et al. (arXiv 2402.05636) | firm | https://arxiv.org/pdf/2402.05636 | 2024-04-17 | full |
| MS-CODEREVIEW-2025 | Enhancing Code Quality at Scale with AI-Powered Code Reviews | Microsoft, Engineering@Microsoft blog | firm | https://devblogs.microsoft.com/engineering-at-microsoft/enhancing-code-quality-at-scale-with-ai-powered-code-reviews/ | 2025-07-14 | full |
| AWS-QTRANSFORM-2024 | Amazon Q Developer just reached a $260 million dollar milestone | Amazon Web Services, DevOps blog | vendor | https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone | 2024-08-01 | full |
| AWS-BULLETIN-2025 | Security Update for Amazon Q Developer Extension for Visual Studio Code (Version #1.84), AWS-2025-015 | Amazon Web Services | vendor | https://aws.amazon.com/security/security-bulletins/AWS-2025-015/ | 2025-07-23 | full |
| REGISTER-REPLIT-2025 | Vibe coding service Replit deleted production database | The Register | press | https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/ | 2025-07-21 | full |
| ANTHROPIC-WORK-2025 | How AI is transforming work at Anthropic | Anthropic | firm | https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic | 2025-12-02 | full |
| ATLASSIAN-DEVEX-2025 | Atlassian research: AI adoption is rising, but friction persists (State of DevEx 2025) | Atlassian | vendor | https://www.atlassian.com/blog/developer/developer-experience-report-2025 | 2025-07-09 | full |
| STACKOVERFLOW-2025 | 2025 Stack Overflow Developer Survey, AI section | Stack Overflow | survey | https://survey.stackoverflow.co/2025/ai | 2025 | full |
| FAROS-2025 | The AI Productivity Paradox Report 2025 | Faros AI | vendor | https://www.faros.ai/blog/ai-software-engineering | 2025-07-23 | full |
| DX-AIIMPACT-2026 | AI-assisted engineering: Q1 impact report | DX; Reock | vendor | https://getdx.com/uploads/ai-assisted-engineering-q1-impact-report.pdf | 2026 (data 2025-10-17 to 2026-02-01) | full |
| VERACODE-2025 | 2025 GenAI Code Security Report | Veracode | vendor | https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ | 2025 (page updated October 2025) | full (landing page summary) |
| TW-RADAR-2026 | Technology Radar Vol. 34, themes | Thoughtworks | firm | https://www.thoughtworks.com/radar | 2026-04 | full |
| ORACLE-AISD-2025 | Transforming IT support: Introducing the generative AI-powered service desk; and customer page "Oracle IT support increases customer satisfaction with OCI Generative AI" | Oracle | vendor | https://blogs.oracle.com/ai-and-datascience/transforming-it-support-gen-aipowered-service-desk (read via text mirror); https://www.oracle.com/customers/oracle-it/ | 2025-10 | full |
| HCL-BANK-2026 | Transforming global support with 45% L1 deflection | HCLTech | vendor | https://www.hcltech.com/case-study/global-support-l1-deflection | 2026-09-10 | full |
| MS-DEVGEN-2025 | A team of engineers saved Morgan Stanley more than 280,000 hours this year, the bank says | Business Insider | press | https://www.businessinsider.nl/a-team-of-engineers-saved-morgan-stanley-more-than-280000-hours-this-year-the-bank-says-their-tool-wont-take-jobs/ | 2025-07 | search-only |
| IBM-THINK-2025 | Embracing the future of HR by becoming an AI-first enterprise | IBM; Nickle LaMoreaux, CHRO | firm | https://www.ibm.com/think/insights/embracing-future-of-hr-ai-first-enterprise | 2025-04-29 | full |
| IBM-ASKHR-2025 | IBM AskHR: Transforming HR support with agentic AI (case study) | IBM | vendor | https://www.ibm.com/case-studies/ibm-askhr | 2025-08-21 | full |
| CHICAGO-JABARIAN-2026 | Voice AI in Firms: A Natural Field Experiment on Automated Job Interviews (v2) | Jabarian, Henkel (arXiv 2607.28222) | academic | https://arxiv.org/pdf/2607.28222 | 2026-09-11 | full |
| NRN-CHIPOTLE-2025 | Chipotle is going on a hiring spree with the help of AI | Nation's Restaurant News | press | https://www.nrn.com/fast-casual/chipotle-is-going-on-a-hiring-spree-with-the-help-of-ai | 2025-02-19 | full |
| WORKDAY-CHIPOTLE-2026 | Chipotle Cuts Time to Hire by 75% With AI Platform (customer story) | Workday | vendor | https://workday.com/en-us/customer-stories/a-h/chipotle-leverages-conversational-ai-scales-hiring.html | 2026-01-30 | full |
| WORKDAY-ADVENTHEALTH-2025 | AdventHealth Fills Hard-to-Fill Roles at Record Speed (customer story) | Workday | vendor | https://www.workday.com/en-us/customer-stories/a-h/adventhealth-fills-hard-to-fill-roles-at-record-speed.html | 2025-01-31 | full |
| TBS-AIA-2024 | Algorithmic Impact Assessment: using AI to automate candidate evaluations in the staffing process's assessment phase | Treasury Board Secretariat, Government of Canada | regulator | https://open.canada.ca/data/dataset/52b8574d-5c95-463b-b375-8edd092cea30/resource/f7a43e13-44f3-4d43-b588-97aedb17c3f8/download/algorithmic-impact-assessment-using-artificial-intelligence-ai-to-automate-candidate-evaluations.pdf (read via text mirror) | 2024-02-28 | full |
| BOSCH-PT-2024 | Bosch UK: this is how our HR teams are using AI | Personnel Today (written by Bosch UK) | press | https://www.personneltoday.com/?p=329503 | 2024-12-19 | full |
| UNLEASH-MODERNA-2025 | Why Moderna merged HR and IT to better 'architect the flow of work' | UNLEASH | press | https://www.unleash.ai/artificial-intelligence/why-moderna-merged-hr-and-it-to-better-architect-the-flow-of-work/ | 2025-06-27 | full |
| GARTNER-HR-2026 | Gartner Survey Finds AI Automation Is Reducing Some Entry Level Hiring at Nearly One-Quarter of Organizations; and Gartner HR Survey Reveals 45% of Managers Report AI Has Lived Up to Their Expectations | Gartner | survey | https://www.gartner.com/en/newsroom/press-releases/2026-7-27-gartner-survey-finds-ai-automation-is-reducing-some-entry-level-hiring-at-nearly-one-quarter-of-organizations | 2026-07-27 | search-only |
| UW-WILSON-2024 | Gender, Race, and Intersectional Bias in Resume Screening via Language Model Retrieval (v3 with 2026-08-29 correction) | University of Washington; Wilson, Caliskan (arXiv 2407.20371) | academic | https://arxiv.org/pdf/2407.20371 | 2026-08-30 | full |
| ICO-RECRUIT-2024 | ICO intervention into AI recruitment tools leads to better data protection for job seekers | UK Information Commissioner's Office | regulator | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/ico-intervention-into-ai-recruitment-tools-leads-to-better-data-protection-for-job-seekers/ | 2024-11-06 | full |
| NYC-DCWP-AEDT-2023 | Automated Employment Decision Tools (AEDT), Local Law 144 of 2021 | NYC Department of Consumer and Worker Protection | regulator | https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page | 2023-07 (enforcement from 2023-07-05) | full |
| HRDIVE-MOBLEY-2025 | Judge allows Workday AI bias lawsuit to proceed as collective action | HR Dive | press | https://www.hrdive.com/news/workday-ai-bias-lawsuit-class-collective-action/748518/ | 2025-05-19 | full |
| CLEARINGHOUSE-MOBLEY-2026 | Mobley v. Workday, Inc., 3:23-cv-00770 (N.D. Cal.) case page | Civil Rights Litigation Clearinghouse | academic | https://clearinghouse.net/case/44074/ | 2026-09-17 | full |
| EU-AIACT-ANNEX3-2024 | Annex III: High-risk AI systems referred to in Article 6(2) | Regulation (EU) 2024/1689, via artificialintelligenceact.eu | regulator | https://artificialintelligenceact.eu/annex/3/ | 2024 | full |
| EU-AIACT-ART5-2024 | Article 5: Prohibited AI practices | Regulation (EU) 2024/1689, via artificialintelligenceact.eu | regulator | https://artificialintelligenceact.eu/article/5/ | 2024 | full |
| EU-AIACT-ART26-2024 | Article 26: Obligations of deployers of high-risk AI systems | Regulation (EU) 2024/1689, via artificialintelligenceact.eu | regulator | https://artificialintelligenceact.eu/article/26/ | 2024 | full |
| AG-OMNIBUS-2026 | EU AI Act: AI Omnibus formally adopted | Addleshaw Goddard | firm | https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/ | 2026-07-01 | full |
| NIST-AIRMF-2023 | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 2023-01 | full |
| NIST-AI600-1-2024 | AI RMF: Generative AI Profile, NIST AI 600-1 | NIST | standard-setter | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf | 2024-07 | full |
| MARKUP-NYCBOT-2024 | NYC's AI Chatbot Tells Businesses to Break the Law | The Markup | press | https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law | 2024-03-29 | full |
| APQC-PCF-2026 | APQC Process Classification Framework version 8.0 (framework page; measure page "Personnel cost to perform the process group recruit, source, and select employees per new hire", with 7.2.1-7.2.5 process list) | APQC | professional-body | https://www.apqc.org/process-frameworks ; https://www.apqc.org/resources/benchmarking/open-standards-benchmarking/measures/personnel-cost-perform-process-group-7 (read via text mirror) | 2026-03 | full |
| APQC-PCF-PAYOR-2019 | Health Insurance Payor Process Classification Framework, version 7.2.1 (lists cross-industry 7.0 and 8.0 group names) | APQC | professional-body | https://www.apqc.org/system/files/Health%20Insurance%20Payor_721_021319.pdf | 2019-02-13 | full |
| SHRM-AI-2025 | SHRM Report Warns of Widening Skills Gap as AI Adoption Reaches Nearly Half of U.S. Workforce (read for context; no figure from it is relied on above) | SHRM | survey | https://www.shrm.org/about/press-room/shrm-report-warns-of-widening-skills-gap-as-ai-adoption-reaches- | 2025-07-08 | full |
