# Professional services, delivery-management, practice angle

## 1. Summary

Prepared 2026-10-19. Archetype: professional-services. Module: delivery-management (running engagements: planning, status and risk, client reporting, change control and engagement economics). Angle: practice.

Method: 37 sources opened and read (pages by `curl`, the `r.jina.ai` text mirror for sites that refused `curl`, the public Greenhouse job-board feed for Thoughtworks, and the Ashby feeds for Harvey and Legora, which held only vendor roles and were not used). Ten web searches were used; most returned vendor pages. Items tagged **in-house** are examples from a company's own team rather than a services firm.

- **The public record is mostly vendor-published.** Nearly every outcome figure comes from a PSA or AI vendor (Certinia, Kantata, Deltek, Rocketlane, Harvey) or a firm selling its own offering (PwC). Named deployments are few and small: Nextview, Diabsolut, Spaulding Ridge, zeb, Automation Consultants and Basware, plus one Siemens sentence. Evidence grades across 16 use cases: no A, 8 B, 7 C, 1 D.
- **What changes first is the administrative layer of delivery.** The documented changes are assembling status and steering-committee reports, turning calls into documentation, drafting architecture and plan documents, and answering project questions in natural language. Scope and change control, risk judgment and client conversations have product descriptions only.
- **There is no independent quality evidence.** No source gives an error rate, correction rate, override rate or parallel run for an AI-drafted status report, plan or alert. The nearest independent-style data are survey results on whether AI pays off at all: only 38% of A&E firms report measurable benefit (Deltek) and only 20% of surveyed services leaders say AI results exceeded expectations (Certinia-commissioned).
- **Perception gaps are the clearest measured caution.** In the Certinia-commissioned survey, leaders rate their AI success 16 points and forecasting confidence 24 points higher than practitioners do (CERTINIA-GSD-2026).
- **The best-documented build is a consultancy writing its own agents.** Automation Consultants reports a 12-agent PMO estate with an orchestrating agent and a human approval gate, claiming roughly 25% of delivery capacity released (conference abstract, self-reported).
- **Legal delivery management is announced, not evidenced.** Harvey launched matter orchestration with reusable templates and review gates on 2026-10-15 and says rollout has begun; no law firm or in-house team is named as using it. Matter-budget tools (BigHand, Planning Blox) are product listings.
- **Roles.** The project manager moves toward reviewing and approving agent output; Thoughtworks postings make AI-agent orchestration part of the engagement lead's job. Resource managers say they are not ready for hybrid human-agent teams (44-organisation study).

## 2. Use cases

```yaml
- id: professional-services-delivery-management-01
  title: Agent-drafted project status and steering-committee reports from live project data
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - document-production
  - data-reporting
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Project managers assemble status packs by hand from budgets, task lists, emails and notes, then reformat
    them for each client or committee. Wellingtone's report summary states that 72% spend half a day or more collating
    reports every month; the page does not define the base (WELLINGTONE-SOPM-2026).
  solution: An agent reads the project's budget, risk and health data and drafts the report; the project manager
    checks and sends it. Nextview, a Salesforce consulting partner in Northern Europe, runs a Project Assistant
    Agent in Slack that assembles steering-committee reports with budget, risk and project health (CERTINIA-PROVING-2026).
    Automation Consultants lists status reporting among the tasks of its 12-agent PMO estate (ATLASSIAN-TEAM26-AC-2026).
    PwC US markets an Intelligent Status Insights offering that combines open-source language models with retrieval
    over raw project inputs to produce standardized, client-ready status reports (PWC-STATUS-2026). Oracle describes
    AI-generated program summaries that highlight metrics and flag risks (ORACLE-PPM-2026).
  outcomes:
  - lever: speed
    description: Nextview says steering-committee reports that used to take hours of manual assembly now generate
      with a click. No time figure is given.
    figure: none published (qualitative)
    measures: 'Certinia''s wording about one customer: reports ''used to take hours'' and now generate with a click;
      no baseline, sample or period stated.'
    provenance: vendor-published
    source_ref: CERTINIA-PROVING-2026
  - lever: capacity
    description: PwC states its offering can lower administrative project overhead by approximately 40%, an estimated
      120 hours saved a year per resource, and a projected USD 7,000 to 24,000 in annual savings per resource depending
      on role and billing structure. The page names no client and describes these as estimates and projections.
    figure: about 40%; 120 hours a year per resource; USD 7,000-24,000 a year per resource (projected)
    measures: 'PwC''s wording: reduction in ''administrative project overhead'' for strategic PMO environments;
      the denominator, sample and measurement method are not stated.'
    provenance: vendor-published
    source_ref: PWC-STATUS-2026
  prerequisites:
  - Project, budget and risk data held in a system the agent can read; Certinia ties its results to a single connected
    data foundation (CERTINIA-SOA-2026, opening section).
  - A defined report template or committee format (Nextview's pack covers budget, risk and project health; CERTINIA-PROVING-2026).
  - A time-spent baseline before deployment; Certinia's own tip is to baseline documentation and admin time so there
    is a real number to measure against (CERTINIA-PROVING-2026, Pro Tips).
  risks_and_guardrails:
  - No error rate, correction rate or override rate has been published for agent-drafted status reports in any source
    read.
  - PwC says it grounds reports in source data through retrieval so updates are more explainable (PWC-STATUS-2026);
    this is a design claim, not a measured result.
  - Automation Consultants places a human approval gate before any output reaches Jira, Confluence or a client inbox
    (ATLASSIAN-TEAM26-AC-2026).
  human_checkpoints:
  - Project manager reviews the generated report before it goes to the steering committee or client.
  - Approval gate before anything is sent to a client (ATLASSIAN-TEAM26-AC-2026).
  role_evolution: Nextview's delivery director describes the project manager's steering-committee preparation as
    becoming a 'quality information gathering exercise' rather than digging for information (CERTINIA-PROVING-2026).
    PwC says the time freed goes to oversight, risk management and issue resolution (PWC-STATUS-2026).
  evidence_grade: B
  sources:
  - ref: CERTINIA-PROVING-2026
    title: Certinia Customers Are Proving Veda AI Agents Deliver Real Results
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-customers-are-proving-veda-ai-agents-deliver-real-results/
    date: '2026-09-03'
    access: full
    locator: Section 'Nextview Puts Agents to Work in Slack'
  - ref: ATLASSIAN-TEAM26-AC-2026
    title: 'The agentic PMO: Scaling delivery with Rovo and Claude (sponsored session, Hassan Khadra, Automation
      Consultants; Team ''26 Europe, Amsterdam)'
    publisher: Atlassian
    type: conference
    url: https://events.atlassian.com/teameurope/session/4417894/the-agentic-pmo-scaling-delivery-with-rovo-and-claude
    date: '2026-10-08'
    access: full
    locator: Session abstract, paragraph 2
  - ref: PWC-STATUS-2026
    title: Manual PMO Status Reporting Is Draining 40% of Project Management Hours. This AI Automates It. (Intelligent
      Status Insights)
    publisher: PwC US
    type: firm
    url: https://www.pwc.com/us/en/tech-effect/innovation/automate-pmo-status-reporting.html
    date: '2026-03-24'
    access: full
    locator: Opening paragraphs and 'What this delivers for PMO leaders and teams'
  - ref: WELLINGTONE-SOPM-2026
    title: The State of Project Management Report 2026 (landing page summary)
    publisher: Wellingtone
    type: survey
    url: https://www.wellingtone.co.uk/state-of-project-management/
    date: '2026-03-12'
    access: full
    locator: Headline statistics list
  - ref: ORACLE-PPM-2026
    title: Oracle Fusion Cloud Project Management (product page)
    publisher: Oracle
    type: vendor
    url: https://www.oracle.com/erp/project-management/
    date: '2026-10-19'
    access: full
    locator: Program management section, AI-generated summaries
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (agent catalogue and results panel)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: 'Manage column: Project Assistant'
  - ref: CERTINIA-SOA-2026
    title: Certinia Unveils the System of Action for Services, and the Largest Expansion of Veda AI to Date
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-unveils-system-of-action-for-services-and-largest-expansion-of-veda-ai-to-date/
    date: '2026-09-09'
    access: full
    locator: Opening section on the unified data foundation
  last_reviewed: '2026-10-19'
  notes: Grade B rests on Nextview (named, qualitative only). PwC figures are a firm's own projections for a sold
    offering, not client results. Certinia also lists a Project Assistant that gives instant digests on financials,
    risks and timeline variances (CERTINIA-VEDA-2026, Manage column).
- id: professional-services-delivery-management-02
  title: Self-built PMO agent estate with an orchestrating agent and a human approval gate
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  - document-production
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: 'Portfolio reporting is described in the session abstract as one of the last manual processes in many
    delivery organisations: assembled by hand, often late, and open to challenge (ATLASSIAN-TEAM26-AC-2026).'
  solution: 'Automation Consultants built a 12-agent estate across Jira, Confluence, Loom and Tempo, with Rovo at
    the centre and Anthropic''s Claude as the reasoning layer. The agents cover knowledge capture, risk and issue
    management, budget tracking, status reporting, lessons learnt, resourcing, project provisioning and proposal
    drafting. A single orchestrating ''super agent'' screens every finding, and a human-in-the-loop approval gate
    sits before anything reaches Jira, Confluence or a client inbox. Agent memory is kept in state files rather
    than conversation history so the set-up can be rebuilt or moved between models (ATLASSIAN-TEAM26-AC-2026). Productive
    and Kantata sell configurable agent builders: Productive with permissions, schedules and approval before output
    goes out, Kantata with Agent Studio (PRODUCTIVE-AGENTS-2026; KANTATA-EXPERTAGENT-2026).'
  outcomes:
  - lever: capacity
    description: The presenting firm reports roughly 25% of delivery capacity released and tripled throughput without
      adding headcount, across 11 concurrent client engagements.
    figure: roughly 25% of delivery capacity; throughput tripled
    measures: 'Session abstract wording: ''releasing roughly 25% of delivery capacity, and tripling throughput without
      adding headcount''. Basis, baseline and period are not stated in the abstract; the talk itself was not reviewed.'
    provenance: self-reported
    source_ref: ATLASSIAN-TEAM26-AC-2026
  prerequisites:
  - Delivery data already in Jira, Confluence, Loom and Tempo (ATLASSIAN-TEAM26-AC-2026).
  - An orchestration layer and state-file memory design so agents can be retired or rebuilt (ATLASSIAN-TEAM26-AC-2026).
  - 'Agent permissions: Productive lets each agent be given defined access to read and change parts of the platform
    (PRODUCTIVE-AGENTS-2026).'
  risks_and_guardrails:
  - The session lists which PMO disciplines are safest to automate first as a topic; the answer is not in the abstract
    (ATLASSIAN-TEAM26-AC-2026).
  - Sponsored session; the capacity and throughput figures are the presenter's own and no independent check was
    found.
  - Kantata's CEO warns that fast agent answers without full business context risk 'fast, mediocre decisions' (KANTATA-SUPERAGENT-2026,
    section 'Fast Doesn't Always Mean Accurate').
  human_checkpoints:
  - Human approval gate before output reaches Jira, Confluence or a client inbox.
  - Orchestrating agent screens findings for severity and scope before they reach the gate (ATLASSIAN-TEAM26-AC-2026).
  role_evolution: The PMO moves from compiling reports to designing, governing and approving an agent estate. The
    presenter is a senior project manager at the consultancy (ATLASSIAN-TEAM26-AC-2026).
  evidence_grade: B
  sources:
  - ref: ATLASSIAN-TEAM26-AC-2026
    title: 'The agentic PMO: Scaling delivery with Rovo and Claude (sponsored session, Hassan Khadra, Automation
      Consultants; Team ''26 Europe, Amsterdam)'
    publisher: Atlassian
    type: conference
    url: https://events.atlassian.com/teameurope/session/4417894/the-agentic-pmo-scaling-delivery-with-rovo-and-claude
    date: '2026-10-08'
    access: full
    locator: Session abstract, paragraphs 1-4
  - ref: PRODUCTIVE-AGENTS-2026
    title: AI Agents for Project Management & Operations (product page)
    publisher: Productive
    type: vendor
    url: https://productive.io/agents
    date: '2026-10-19'
    access: full
    locator: Agent builder, permissions and approval sections
  - ref: KANTATA-EXPERTAGENT-2026
    title: Expertise Agent & Workflows (product page)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/ai/expertise-agent-and-workflows
    date: '2026-10-19'
    access: full
    locator: Sections 'Agent Studio' and 'Set it in Motion'
  - ref: KANTATA-SUPERAGENT-2026
    title: 'More Agents Won''t Fix Unpredictable Projects: Why We Built a Superagent Instead'
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead
    date: '2026-06-16'
    access: full
    locator: Sections 'Fast Doesn't Always Mean Accurate' and 'One Agent that Sees the Whole Business'
  last_reviewed: '2026-10-19'
  notes: Session held 2026-10-08 (page shows the slot). Only the abstract was read. The best-documented named build
    in this module, but self-reported and sponsored. Grade B, not A, because the figures are rough and unaudited.
- id: professional-services-delivery-management-03
  title: Conversational access to project status, budget consumption and anomalies over ERP or PSA data
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: At zeb, project managers had to navigate the right paths and apps in SAP to find project information,
    often in a different context from their question (NTTDATA-ZEB-2026).
  solution: zeb, a European financial-services consultancy, worked with NTT DATA to build an orchestrator agent
    and specialist agents on SAP. A project-information agent answers natural-language questions on owners, timelines
    and current status from S/4HANA project data. It also gives forecasts on budget consumption and flags potential
    anomalies. Financial agents answer cost and invoice questions for a project (NTTDATA-ZEB-2026). Comparable assistants
    are described by Certinia (Ask Veda, Project Assistant), Deltek (Ask Dela) and Oracle (CERTINIA-VEDA-2026; DELTEK-DELA-2026;
    ORACLE-PPM-2026).
  outcomes:
  - lever: speed
    description: zeb's head of SAP solutions says the implementation took only a few weeks and delivered excellent
      results. No outcome figure is published.
    figure: none published
    measures: Quote from zeb's Head of SAP Solutions on the build time; no measure of the agents' effect on delivery
      is given.
    provenance: vendor-published
    source_ref: NTTDATA-ZEB-2026
  - lever: capacity
    description: The case study says the agents reduce manual effort and free consultants to focus more on strategic
      activities. No figure.
    figure: none published (qualitative)
    measures: Integrator's description of the effect; no baseline or sample.
    provenance: vendor-published
    source_ref: NTTDATA-ZEB-2026
  prerequisites:
  - Project, timesheet and finance data consolidated in the ERP (NTTDATA-ZEB-2026).
  - Integration layer between the agents and the ERP; zeb used SAP BTP, an AI foundation layer and S/4HANA services
    (NTTDATA-ZEB-2026).
  risks_and_guardrails:
  - Answers depend on ERP data quality; the case study publishes no accuracy or error rate.
  - In Deltek's GovCon survey the top AI concerns among IT and security respondents included inaccurate forecasts
    (29%) and difficulty validating AI-provided insights (26%) (DELTEK-CLARITY-2026, GovCon key findings).
  human_checkpoints:
  - The project manager reads and acts on the answer; the agent only retrieves and forecasts. The case study does
    not describe formal review steps.
  role_evolution: Project managers ask questions instead of navigating apps. zeb says consultants spend more time
    on strategic work (NTTDATA-ZEB-2026).
  evidence_grade: B
  sources:
  - ref: NTTDATA-ZEB-2026
    title: 'zeb: putting agentic AI into action'
    publisher: NTT DATA
    type: vendor
    url: https://nttdata-solutions.com/br/success-stories/zeb-putting-agentic-ai-into-action/
    date: '2026-05-07'
    access: full
    locator: Sections 'Improving project outcomes...' to 'Operating more dynamically...'
  - ref: DELTEK-DELA-2026
    title: Deltek Dela (AI product page)
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/en/products/platform/dela/
    date: '2026-05-27'
    access: full
    locator: 'Feature list: Ask Dela, summaries, predictions'
  - ref: ORACLE-PPM-2026
    title: Oracle Fusion Cloud Project Management (product page)
    publisher: Oracle
    type: vendor
    url: https://www.oracle.com/erp/project-management/
    date: '2026-10-19'
    access: full
    locator: Reporting and program management sections
  - ref: DELTEK-CLARITY-2026
    title: The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity
      Pressures for Project-Based Businesses
    publisher: Deltek
    type: survey
    url: https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/
    date: '2026-05-12'
    access: full
    locator: GovCon report key findings
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (agent catalogue and results panel)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: 'Deliver and Manage columns: Ask Veda Agent, Project Assistant'
  last_reviewed: '2026-10-19'
  notes: zeb is the client of NTT DATA, and the page is NTT DATA's own success story; first published 2026-05-07,
    modified 2026-09-08. The same case includes a timesheet agent and a staffing agent that proposes and pre-books
    people (routed to staffing-resourcing and billing-collections).
- id: professional-services-delivery-management-04
  title: Meeting and call capture turned into summaries, decisions, requirements and project documentation
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - document-production
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Consultants spend hours writing technical plans, requirements and call notes. Diabsolut, a Salesforce
    and Certinia implementer, says senior consultants spent hours writing technical plans and chasing spreadsheets
    (CERTINIA-PROVING-2026).
  solution: Agents inside Slack, connected to project data, turn transcripts into requirements, backlogs and scoping
    documents. Diabsolut deployed a Project Assistant and a combined Customer Success and Staffing Agent. Its technical-architecture
    director says the automated steps were 'transcripts, requirements, backlogs, and scoping'. The project-management
    team that onboards new franchise stores at EarthWise Pet uses Rocketlane's AI Fills to generate call summaries
    and action items (in-house team, not a services firm). Deloitte lists a meeting-insights and status-update agent
    in its Agent Fleet, sold through AWS Marketplace (CERTINIA-PROVING-2026; ROCKETLANE-EARTHWISE-2026; DELOITTE-AWS-2026).
  outcomes:
  - lever: speed
    description: Diabsolut cut documentation time by 70%, according to Certinia's account of the deployment.
    figure: 70% less documentation time
    measures: 'Certinia''s wording: ''cut documentation time by 70%''. Baseline, sample, task definition and period
      are not stated.'
    provenance: vendor-published
    source_ref: CERTINIA-PROVING-2026
  - lever: speed
    description: Diabsolut deployed eight agents in six months, a project it expected to take about a year and a
      half, and is adding two to four a month.
    figure: 8 agents in 6 months vs expected ~18 months
    measures: Count of agents deployed versus the firm's own expected timeline, as reported by Certinia.
    provenance: vendor-published
    source_ref: CERTINIA-PROVING-2026
  - lever: experience
    description: EarthWise Pet's project-management VP says AI call summaries save time and remove 'he said, she
      said' disputes because commitments are documented. No figure.
    figure: none published (qualitative)
    measures: One customer's statement; no sample or baseline.
    provenance: vendor-published
    source_ref: ROCKETLANE-EARTHWISE-2026
  prerequisites:
  - Call or meeting recordings and transcripts captured in the tools the team already uses (Slack in Diabsolut's
    case).
  - Baseline of documentation time before deployment (Certinia tip, CERTINIA-PROVING-2026).
  - Moonnox, acquired by Certinia on 2026-07-21, adds context capture across Salesforce, Google, Microsoft 365,
    Jira, Confluence and Zoom (CERTINIA-MOONNOX-2026).
  risks_and_guardrails:
  - Certinia asserts that generic AI tools can leave teams spending as much time verifying and correcting output
    as they save (CERTINIA-MOONNOX-2026). This is a vendor claim with no data.
  - A testimonial quoted on Rocketlane's page about its documentation agent is conditional ('could automatically
    pull key decisions'), so it is not evidence of use; it does state that complex implementations take 10-15 hours
    of decision and requirements documentation, speaker not identified (ROCKETLANE-AGENTIC-2026).
  - Recording and transcribing client calls raises consent and confidentiality questions that none of these sources
    discuss.
  human_checkpoints:
  - Consultant or project manager reviews generated documents before they are shared; Productive-style agents require
    approval before output goes out (PRODUCTIVE-AGENTS-2026).
  role_evolution: Diabsolut's director says the automation frees outcomes architects to focus on outcomes rather
    than paperwork (CERTINIA-PROVING-2026).
  evidence_grade: B
  sources:
  - ref: CERTINIA-PROVING-2026
    title: Certinia Customers Are Proving Veda AI Agents Deliver Real Results
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-customers-are-proving-veda-ai-agents-deliver-real-results/
    date: '2026-09-03'
    access: full
    locator: Section 'Diabsolut Turns AI Into a New Business Model'; Pro Tips
  - ref: ROCKETLANE-EARTHWISE-2026
    title: 'How EarthWise Pets Did It (customer story: AI Fills call summaries in franchise onboarding)'
    publisher: Rocketlane
    type: vendor
    url: https://www.rocketlane.com/customers/how-earthwise-pets-captures-100-of-franchise-commitments-with-rocketlanes-ai-teammate
    date: '2026-10-14'
    access: full
    locator: Sections on AI Fills and call summaries
  - ref: DELOITTE-AWS-2026
    title: Meeting Data analyzer Agent (Deloitte Agent Fleet, Innovation Support Agent Suite) AWS Marketplace listing
    publisher: Deloitte / AWS Marketplace
    type: firm
    url: https://aws.amazon.com/marketplace/pp/prodview-obfkw4hi57r3i
    date: '2026-09-30'
    access: full
    locator: Product description
  - ref: CERTINIA-MOONNOX-2026
    title: Certinia Acquires Moonnox to Power AI-Native Services Delivery
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-acquires-moonnox-to-power-ai-native-services-delivery/
    date: '2026-07-21'
    access: full
    locator: Section 'Trusted, Real-Time Context Your Services Teams Can Act On'
  - ref: ROCKETLANE-AGENTIC-2026
    title: Rocketlane agentic PSA platform (Nitro) product page
    publisher: Rocketlane
    type: vendor
    url: https://www.rocketlane.com/agentic-psa
    date: '2026-10-14'
    access: full
    locator: Customer quote on documentation agent
  - ref: CERTINIA-DIABSOLUT-2026
    title: Diabsolut Customer Success Story
    publisher: Certinia
    type: vendor
    url: https://certinia.com/customer-success-stories/diabsolut/
    date: '2026-10-19'
    access: full
    locator: Impact section on invoice ageing
  - ref: PRODUCTIVE-AGENTS-2026
    title: AI Agents for Project Management & Operations (product page)
    publisher: Productive
    type: vendor
    url: https://productive.io/agents
    date: '2026-10-19'
    access: full
    locator: Section on approving output before it goes out
  last_reviewed: '2026-10-19'
  notes: 'Do not confuse metrics: the Certinia customer-story page for Diabsolut separately reports invoice ageing
    reduced by over 40% in six months from Customer Success Cloud scorecards, which is a non-agent result (CERTINIA-DIABSOLUT-2026).
    The blog''s ''invoice turnaround 40% faster'' is a different claim (routed to billing-collections). The blog
    date (3 September) has no year on the page; 2026 is inferred from its references to the 2026 report and Dreamforce.'
- id: professional-services-delivery-management-05
  title: Drafting solution-architecture documents and implementation plans from requirements, transcripts and the
    SOW
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - document-production
  - expert-judgment
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Architects and consultants spend large blocks of time writing solution-design and plan documents before
    delivery can start.
  solution: An agent drafts the architecture document or phased implementation plan from captured context. Spaulding
    Ridge, a cloud advisory and implementation firm, deployed a Moonnox agent for drafting solution architecture
    documents (CERTINIA-MOONNOX-2026). Certinia sells Solution Architect and Implementation Plan agents, and Rocketlane
    and Kantata describe generating a project plan from a SOW (CERTINIA-VEDA-2026; ROCKETLANE-AGENTIC-2026; KANTATA-EXPERTAGENT-2026).
  outcomes:
  - lever: speed
    description: Spaulding Ridge's executive chair says the agent made drafting solution architecture documents
      four times faster, from about 80 hours to under 20.
    figure: about 80 hours to under 20 hours per document (4x)
    measures: 'The founder''s statement in Certinia''s press release: ''approximately 80 hours to under 20 hours''.
      Number of documents, period and measurement method are not stated, so this is an estimate.'
    provenance: self-reported
    source_ref: CERTINIA-MOONNOX-2026
  prerequisites:
  - Captured requirements, call transcripts and SOW text in an accessible store (Moonnox context capture, CERTINIA-MOONNOX-2026).
  - A standard document template or phased roadmap structure (Certinia describes 'structured, phased implementation
    roadmaps', CERTINIA-VEDA-2026).
  risks_and_guardrails:
  - No review-time, correction-rate or defect data accompany the 80-to-20-hour figure. Certinia's own text says
    teams must be able to trust output 'without manual rework' (CERTINIA-MOONNOX-2026, CEO quote).
  - Architecture is expert judgment; the draft must be checked by the architect before it commits scope or price.
  human_checkpoints:
  - Solution architect reviews and signs off the draft before it goes to the client or the delivery team.
  role_evolution: Spaulding Ridge's chair says consultants are freed to focus on high-value work (CERTINIA-MOONNOX-2026).
    Certinia says Penrod cut seller prep time in half (routed to client-development).
  evidence_grade: B
  sources:
  - ref: CERTINIA-MOONNOX-2026
    title: Certinia Acquires Moonnox to Power AI-Native Services Delivery
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-acquires-moonnox-to-power-ai-native-services-delivery/
    date: '2026-07-21'
    access: full
    locator: Section 'Customers Are Already Unlocking Proven Value' (Jay Laabs quote)
  - ref: CERTINIA-PROVING-2026
    title: Certinia Customers Are Proving Veda AI Agents Deliver Real Results
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-customers-are-proving-veda-ai-agents-deliver-real-results/
    date: '2026-09-03'
    access: full
    locator: Section 'More Customers, More Wins'
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (agent catalogue and results panel)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Plan and Deliver agent lists
  - ref: ROCKETLANE-AGENTIC-2026
    title: Rocketlane agentic PSA platform (Nitro) product page
    publisher: Rocketlane
    type: vendor
    url: https://www.rocketlane.com/agentic-psa
    date: '2026-10-14'
    access: full
    locator: Project Delivery capability line
  - ref: KANTATA-EXPERTAGENT-2026
    title: Expertise Agent & Workflows (product page)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/ai/expertise-agent-and-workflows
    date: '2026-10-19'
    access: full
    locator: Section 'Tackle What Matters'
  last_reviewed: '2026-10-19'
  notes: Grade B because the figure is an executive's approximation quoted in a vendor release, which the 2026-10-17
    rule treats as a rough estimate, not a tracked metric. Spaulding Ridge is a customer of both Certinia and Moonnox,
    per the quote.
- id: professional-services-delivery-management-06
  title: Sales-to-delivery handoff and new-joiner project briefs built from the SOW, notes and history
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - document-production
  - coordination-scheduling
  - research-synthesis
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Context is lost between the deal team and the delivery team, and each new team member has to be briefed
    by hand. Kantata's chief product strategy officer says firms can no longer afford to rely on one experienced
    20-year project manager to know the customer and spot risk (KANTATA-SUPERAGENT-2026).
  solution: Certinia's Sales-to-Delivery Handoff Agent connects a closed deal to delivery kickoff, and its Moonnox-based
    agents generate SOWs from sales context so delivery starts aligned. Kantata says its Expertise Agent holds SOWs,
    meeting notes, past decisions and client history so every new resource gets a role-specific brief and project
    plans on day one (CERTINIA-VEDA-2026; CERTINIA-MOONNOX-2026; KANTATA-EXPERTAGENT-2026).
  outcomes:
  - lever: quality
    description: No handoff-specific measure is published. Certinia's aggregate list includes '60% faster client
      onboarding' under its Manage and Expand agents.
    figure: none published for handoff
    measures: The 60% figure is an unattributed aggregate in the vendor's results panel; baseline, sample and the
      agents behind it are not stated.
    provenance: vendor-published
    source_ref: CERTINIA-SOA-2026
  prerequisites:
  - Deal, SOW and meeting data in the same platform the delivery team uses (Certinia and Kantata both position the
    single record as the foundation).
  risks_and_guardrails:
  - No named customer or error data for handoff briefs was found; a brief that omits a commitment could reset client
    expectations.
  human_checkpoints:
  - Delivery lead reads and corrects the brief at kickoff.
  role_evolution: Delivery leads receive a structured brief instead of reconstructing it; senior-PM tacit knowledge
    moves into the platform (KANTATA-SUPERAGENT-2026).
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (agent catalogue and results panel)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: 'Deliver column: Sales-to-Delivery Handoff Agent'
  - ref: CERTINIA-MOONNOX-2026
    title: Certinia Acquires Moonnox to Power AI-Native Services Delivery
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-acquires-moonnox-to-power-ai-native-services-delivery/
    date: '2026-07-21'
    access: full
    locator: Capability list 'Seamless Sales, Handoff & Alignment'
  - ref: KANTATA-EXPERTAGENT-2026
    title: Expertise Agent & Workflows (product page)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/ai/expertise-agent-and-workflows
    date: '2026-10-19'
    access: full
    locator: Section 'Perfect Project Handoffs'
  - ref: KANTATA-SUPERAGENT-2026
    title: 'More Agents Won''t Fix Unpredictable Projects: Why We Built a Superagent Instead'
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead
    date: '2026-06-16'
    access: full
    locator: Section 'Predicting What You Couldn't See Before'
  - ref: CERTINIA-SOA-2026
    title: Certinia Unveils the System of Action for Services, and the Largest Expansion of Veda AI to Date
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-unveils-system-of-action-for-services-and-largest-expansion-of-veda-ai-to-date/
    date: '2026-09-09'
    access: full
    locator: Section 'New Veda Agents...' (aggregate results)
  last_reviewed: '2026-10-19'
  notes: Vendor product descriptions only. Certinia states these agents are available now; no customer deployment
    is named for handoff specifically.
- id: professional-services-delivery-management-07
  title: Agents that watch project and portfolio data for deliverable discrepancies and emerging delivery risk
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - data-reporting
  - review-assurance
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Risk is found in periodic reviews, after margin has already eroded. Siemens Digital Industries' SVP of
    global customer success says the imperative is to identify deliverable discrepancies early across thousands
    of projects and a workforce of 4,500 (CERTINIA-VEDA-2026, customer quote).
  solution: Agents continuously scan project data and route alerts. Siemens' SVP says Certinia's Project Agent,
    built on Salesforce, is making early discrepancy identification a reality. Kantata describes continuous portfolio
    monitoring that routes alerts to the right people; Certinia's PMO Quality and PMO Leadership agents score project
    health and give portfolio oversight; Deltek and Rocketlane describe surfacing risks early (CERTINIA-VEDA-2026;
    KANTATA-EXPERTAGENT-2026; DELTEK-POLARIS-2026; ROCKETLANE-AGENTIC-2026).
  outcomes:
  - lever: quality
    description: Deltek says firms running on its platform see a 16% increase in on-time project delivery by surfacing
      risks early. The page does not say how it was measured.
    figure: 16% increase in on-time project delivery
    measures: Deltek's wording on the Polaris page; unnamed firms, no baseline, period or sample; not specific to
      AI.
    provenance: vendor-published
    source_ref: DELTEK-POLARIS-2026
  - lever: risk
    description: Certinia's results panel lists 11-23% less margin lost to rework and quality issues. No basis is
      given.
    figure: 11-23% less margin lost to rework and quality issues
    measures: Vendor aggregate; the denominator and sample are not stated.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Clean, connected project, time and finance data. IDC's analyst quote in Certinia's release says AI deployed
    without a unified data environment produces unreliable output and eroding trust (CERTINIA-GSD-2026).
  risks_and_guardrails:
  - 'Alert quality is unmeasured: no false-positive or missed-risk rates were found in any source.'
  - Kantata warns that agents deployed in silos each optimise one team's view while the business-wide picture fragments
    (KANTATA-SUPERAGENT-2026).
  - The EU AI Act lists AI used to monitor and evaluate the performance and behaviour of workers as high-risk (EC-AIACT-2026,
    Annex III point 4(b)); no source read addresses whether delivery-health sentiment scoring is in scope.
  human_checkpoints:
  - PMO leaders review alerts and decide on action; Certinia says PMO leaders 'steer projects' using the scores
    (CERTINIA-VEDA-2026).
  role_evolution: PMO leaders move from periodic reviews to responding to continuous alerts; senior-PM pattern recognition
    is meant to be encoded and shared (KANTATA-SUPERAGENT-2026).
  evidence_grade: B
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (agent catalogue and results panel)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Customer quote block (Siemens) and results panel
  - ref: KANTATA-EXPERTAGENT-2026
    title: Expertise Agent & Workflows (product page)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/ai/expertise-agent-and-workflows
    date: '2026-10-19'
    access: full
    locator: Section 'Predictive Portfolio Health'
  - ref: DELTEK-POLARIS-2026
    title: Deltek Polaris (PSA product page)
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/en/products/polaris/
    date: '2026-05-27'
    access: full
    locator: '''Results Teams Deliver with Polaris'''
  - ref: ROCKETLANE-AGENTIC-2026
    title: Rocketlane agentic PSA platform (Nitro) product page
    publisher: Rocketlane
    type: vendor
    url: https://www.rocketlane.com/agentic-psa
    date: '2026-10-14'
    access: full
    locator: Capability lines on risks
  - ref: CERTINIA-GSD-2026
    title: New Global Study Finds AI Success Three Times More Likely at Fully Integrated Organizations (2026 Global
      Service Dynamics Report; fieldwork by Sapio Research for Certinia)
    publisher: Certinia
    type: survey
    url: https://www.certinia.com/blog/new-global-study-finds-ai-success-three-times-more-likely-at-fully-integrated-organizations/
    date: '2026-08-25'
    access: full
    locator: IDC analyst quote
  - ref: EC-AIACT-2026
    title: EU AI Act, Annex III (high-risk systems) and Article 113 as displayed with amended dates (unofficial
      reproduction by the Future of Life Institute)
    publisher: European Union / artificialintelligenceact.eu
    type: regulator
    url: https://artificialintelligenceact.eu/annex/3/
    date: '2024-07-12'
    access: full
    locator: Annex III, point 4(b)
  - ref: KANTATA-SUPERAGENT-2026
    title: 'More Agents Won''t Fix Unpredictable Projects: Why We Built a Superagent Instead'
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead
    date: '2026-06-16'
    access: full
    locator: Section 'The Problem Isn't a Lack of AI'
  - ref: CERTINIA-SIEMENS-2026
    title: Siemens standardizes global services initiating 450 monthly projects with Certinia (customer story)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/customer-success-stories/siemens/
    date: '2026-10-19'
    access: full
    locator: Challenge and Results sections (platform results, not agent results)
  last_reviewed: '2026-10-19'
  notes: Grade B rests on one customer sentence (Siemens) that does not state what is in production or what changed.
    Treat as thin. The Siemens customer-story page on certinia.com reports platform results (utilization, margin),
    not agent results.
- id: professional-services-delivery-management-08
  title: Scope-change detection and change-control support (scope scans against the SOW)
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - review-assurance
  - document-production
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Out-of-scope requests slip into delivery unrecorded, and effort is absorbed instead of being raised as
    a change. Certinia frames margin protection as a PMO concern (CERTINIA-VEDA-2026).
  solution: Certinia's PMO Quality Agent scans project scope on a regular basis and scores health sentiment; its
    margin-protection capability executes automated scope scans so PMO leaders can steer before risks arrive. Oracle
    mentions AI-driven change management in its project product; the page does not say whether this covers client
    change requests (CERTINIA-VEDA-2026; CERTINIA-MOONNOX-2026; ORACLE-PPM-2026).
  outcomes:
  - lever: risk
    description: No outcome published for scope or change control.
    figure: none published
    measures: No figure or customer example found.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - A machine-readable SOW or scope baseline and a record of requests and effort against it.
  risks_and_guardrails:
  - False flags could create client friction; false negatives leave leakage unaddressed. No accuracy data exist
    in sources read.
  - Raising a change order is a commercial and relationship decision for a person.
  human_checkpoints:
  - Project manager or engagement lead decides whether a flagged item is a change and raises it with the client.
  role_evolution: The project manager receives scope-drift flags rather than spotting drift unaided.
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (agent catalogue and results panel)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: 'Plan column: PMO Quality Agent'
  - ref: CERTINIA-MOONNOX-2026
    title: Certinia Acquires Moonnox to Power AI-Native Services Delivery
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-acquires-moonnox-to-power-ai-native-services-delivery/
    date: '2026-07-21'
    access: full
    locator: Capability 'Margin Protection & Risk Management'
  - ref: ORACLE-PPM-2026
    title: Oracle Fusion Cloud Project Management (product page)
    publisher: Oracle
    type: vendor
    url: https://www.oracle.com/erp/project-management/
    date: '2026-10-19'
    access: full
    locator: Section on embedded AI and change management
  last_reviewed: '2026-10-19'
  notes: 'Weakest-evidenced part of the module: only product descriptions. A web search for named scope-creep detection
    deployments returned vendor guides and early-stage products with no customer names.'
- id: professional-services-delivery-management-09
  title: 'Matter or project orchestration: templated phases, tasks and review gates with agents executing tasks'
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - coordination-scheduling
  - document-production
  - review-assurance
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: For recurring work such as an M&A transaction, the process is reconstructed for each matter from a checklist,
    a previous deal or someone's memory, and lawyers carry context between steps and track progress themselves (HARVEY-ORCH-2026).
  solution: 'Harvey''s Legal Work Orchestration connects a matter''s phases, tasks, people and review points. A
    reusable template pre-loads phases, tasks, playbooks, agents, collaborators and review gates. Each task carries
    its scope, inputs and reviewer. In Harvey''s example an agent assigned a change-of-control review produces a
    consent matrix, the designated partner is notified, and approval completes the task and starts the next. Lawyers
    can update tasks by email, and partners see progress without asking an associate to reconstruct it (HARVEY-ORCH-2026).
    Pattern is ''other'': template-driven task orchestration with human review gates.'
  outcomes:
  - lever: speed
    description: Harvey says it expects agents to take on an additional 20% of workflow steps over six months and
      for that share to triple within a year. This is a forecast.
    figure: expects +20% of steps in six months; triple within a year (forecast)
    measures: Harvey's forward-looking statement about the share of workflow steps lawyers prompt versus agents
      execute; not a measurement.
    provenance: vendor-published
    source_ref: HARVEY-ORCH-2026
  prerequisites:
  - Innovation or knowledge teams define the template once (HARVEY-ORCH-2026).
  - Playbooks and agents already configured in the Harvey workspace.
  risks_and_guardrails:
  - Harvey says work by agents will remain transparent and auditable and lawyers stay in control through defined
    review gates (HARVEY-ORCH-2026). No audit or error data are published.
  - Harvey says lawyers still actively prompt the majority of steps today (HARVEY-ORCH-2026).
  human_checkpoints:
  - Designated reviewer (for example the partner) approves each gated task before the next step begins.
  role_evolution: Harvey says lawyers will focus on directing the matter, reviewing consequential outputs and exercising
    judgment as agents take more execution; innovation and knowledge teams author the templates (HARVEY-ORCH-2026).
  evidence_grade: C
  sources:
  - ref: HARVEY-ORCH-2026
    title: Making Harvey the Orchestration Layer for Legal Work
    publisher: Harvey
    type: vendor
    url: https://www.harvey.ai/blog/legal-work-orchestration
    date: '2026-10-15'
    access: full
    locator: Sections 'How Legal Orchestration Works', 'Give Every Task the Context it Needs', 'Keep Reviews and
      Next Steps Moving', 'The Future of Legal Work Orchestration'
  last_reviewed: '2026-10-19'
  notes: Announced 2026-10-15; tasks, comments and notifications are rolling out across workspaces, and templates
    are in an early access programme. No named customer. The quality-review module covers the review gates. Harvey
    says the same structure fits any matter or project a team runs more than once, with a quarterly compliance review
    as its second example (HARVEY-ORCH-2026).
- id: professional-services-delivery-management-10
  title: Law-firm matter budgets, plans and budget-versus-actual alerts with AI-assisted generation and chat queries
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Matter budgets and plans are built by hand and overruns are seen late, which leads to write-offs and
    weaker margin control (BIGHAND-MATTERPRICING-2026).
  solution: 'BigHand Matter Pricing is marketed as an AI-enabled budgeting and tracking tool: top-down and bottom-up
    budgets, near-real-time actual-versus-budget monitoring, AI analysis of raw time entries, what-if scenarios,
    matter cloning from historic matters, and automated overrun alerts. Planning Blox lists AI-assisted generation
    of plans and budgets from standardized work packages, firm-branded reports and alerts, and agentic requests
    for matter financials and task status through conversational prompts (BIGHAND-MATTERPRICING-2026; LTH-PLANNINGBLOX-2026).'
  outcomes:
  - lever: risk
    description: BigHand states the intended result as reduced write-offs and better margin control. No figure.
    figure: none published
    measures: Vendor marketing statement; no customer, baseline or sample.
    provenance: vendor-published
    source_ref: BIGHAND-MATTERPRICING-2026
  prerequisites:
  - Integration with the firm's practice-management, time and billing systems (both listings).
  risks_and_guardrails:
  - No evidence on forecast accuracy or alert precision in either listing.
  human_checkpoints:
  - Lawyer and pricing professional agree the budget with the client and respond to alerts.
  role_evolution: Pricing professionals and legal project managers get generated first-draft plans and can query
    matter data in natural language (LTH-PLANNINGBLOX-2026).
  evidence_grade: C
  sources:
  - ref: BIGHAND-MATTERPRICING-2026
    title: Matter Pricing by BigHand (marketplace listing)
    publisher: BigHand / SoftwareOne Marketplace
    type: vendor
    url: https://platform.softwareone.com/product/matter-pricing/PCP-7252-7893
    date: '2026-10-19'
    access: full
    locator: Product description and feature list
  - ref: LTH-PLANNINGBLOX-2026
    title: Planning Blox vendor profile
    publisher: Legaltech Hub
    type: vendor
    url: https://www.legaltechnologyhub.com/vendors/planning-blox/
    date: '2026-10-19'
    access: full
    locator: Entries 'AI-Enabled Plan and Budget Development' and 'Agentic AI for Matter Data Requests'
  last_reviewed: '2026-10-19'
  notes: Product listings only; pages are undated and the date shown is the read date. No law-firm customer named.
    Pricing-side use of budgets is covered by scoping-pricing.
- id: professional-services-delivery-management-11
  title: Engagement margin, burn and forecast monitoring with agent alerts on unbilled time and budget overruns
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Margin surprises appear after the work is done. Billable utilization hit a historic low of 66.4% in SPI's
    2026 benchmark, as quoted by Certinia (CERTINIA-MOONNOX-2026); Deltek's A&E study shows utilization just under
    60% and operating profit falling to 16.7% (DELTEK-CLARITY-2026).
  solution: Agents watch actuals against plan and flag exceptions early. Rocketlane describes agents that hunt for
    missing timesheets, un-invoiced hours and budget overruns before they become margin surprises. Certinia's Project
    Assistant digests financials, risks and timeline variances. Deltek's Polaris page claims better forecast accuracy
    from connecting people, projects and financials (ROCKETLANE-AGENTIC-2026; CERTINIA-VEDA-2026; DELTEK-POLARIS-2026).
  outcomes:
  - lever: quality
    description: Deltek says a 20% improvement in forecast accuracy comes from connecting people, projects and financials
      in one application. The claim is about integration, not AI specifically.
    figure: 20% improvement in forecast accuracy
    measures: Deltek's wording; unnamed firms, no baseline or sample.
    provenance: vendor-published
    source_ref: DELTEK-POLARIS-2026
  - lever: quality
    description: In a Certinia-commissioned survey, 78% of fully integrated organisations report high confidence
      in resource, demand and revenue forecasts, against 38% of partially aligned ones.
    figure: 78% vs 38% high forecast confidence
    measures: Share of organisations in each alignment group reporting high confidence in their forecasts; 1,000
      services and IT leaders surveyed in June 2026 by Sapio Research for Certinia. Self-assessed confidence, not
      forecast error; the same survey finds 75% of fully siloed organisations also report high confidence.
    provenance: vendor-published
    source_ref: CERTINIA-GSD-2026
  prerequisites:
  - Timesheet, billing and plan data in one system; Rocketlane and Certinia both position unified data as the base.
  risks_and_guardrails:
  - Forecast agents inherit data-quality problems; among GovCon respondents 29% worry about inaccurate forecasts
    (DELTEK-CLARITY-2026).
  - Certinia's survey finds leaders rate their forecasting confidence 24 points higher than practitioners do (CERTINIA-GSD-2026),
    so confidence is a weak proxy for accuracy.
  human_checkpoints:
  - Project or finance lead acts on the alert; invoicing decisions stay with people.
  role_evolution: Project managers receive exception lists instead of reconciling actuals by hand.
  evidence_grade: C
  sources:
  - ref: ROCKETLANE-AGENTIC-2026
    title: Rocketlane agentic PSA platform (Nitro) product page
    publisher: Rocketlane
    type: vendor
    url: https://www.rocketlane.com/agentic-psa
    date: '2026-10-14'
    access: full
    locator: Back-office operations capability text
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (agent catalogue and results panel)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: 'Manage column: Project Assistant; results panel'
  - ref: DELTEK-POLARIS-2026
    title: Deltek Polaris (PSA product page)
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/en/products/polaris/
    date: '2026-05-27'
    access: full
    locator: '''Results Teams Deliver with Polaris'''
  - ref: CERTINIA-GSD-2026
    title: New Global Study Finds AI Success Three Times More Likely at Fully Integrated Organizations (2026 Global
      Service Dynamics Report; fieldwork by Sapio Research for Certinia)
    publisher: Certinia
    type: survey
    url: https://www.certinia.com/blog/new-global-study-finds-ai-success-three-times-more-likely-at-fully-integrated-organizations/
    date: '2026-08-25'
    access: full
    locator: Findings paragraphs on forecasting confidence
  - ref: DELTEK-CLARITY-2026
    title: The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity
      Pressures for Project-Based Businesses
    publisher: Deltek
    type: survey
    url: https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/
    date: '2026-05-12'
    access: full
    locator: A&E key findings
  - ref: CERTINIA-MOONNOX-2026
    title: Certinia Acquires Moonnox to Power AI-Native Services Delivery
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-acquires-moonnox-to-power-ai-native-services-delivery/
    date: '2026-07-21'
    access: full
    locator: Opening paragraphs quoting the SPI benchmark
  last_reviewed: '2026-10-19'
  notes: All figures are vendor-published or vendor-commissioned. Time capture and invoice speed are routed to billing-collections.
- id: professional-services-delivery-management-12
  title: Engagement leads who plan and run advisory engagements as human-plus-agent teams
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - coordination-scheduling
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Delivery planning assumes work is divided among people; a firm that uses AI for analysis, scenario modelling
    and documentation must decide what goes to agents and who checks it.
  solution: 'Thoughtworks'' postings for an Engagement Lead (Singapore) and a Principal Engagement Lead (London)
    call them the delivery and solution leaders for ''AI-native advisory engagements''. They structure each engagement
    across team members, AI agents and client stakeholders, design how AI is used for analysis, scenario modelling,
    code and workflow generation and documentation, delegate to AI while keeping quality and judgment, and capture
    reusable delivery patterns and AI workflows in a shared library (TW-JOB-8138525-2026; TW-JOB-7995201-2026).
    Pattern is ''other'': engagement design with agents as team members.'
  outcomes:
  - lever: capacity
    description: No outcome published; the postings describe expectations, not results.
    figure: none published
    measures: Job postings state role requirements only.
    provenance: self-reported
    source_ref: TW-JOB-8138525-2026
  prerequisites:
  - Engagement leads comfortable using AI and evaluating the confidence of its output (TW-JOB-7995201-2026).
  - A library of repeatable engagement models and AI workflows (both postings).
  risks_and_guardrails:
  - The Singapore posting expects leads to know when to trust AI and when not to; the London posting expects human
    oversight to move past 'anodyne' outputs (TW-JOB-8138525-2026; TW-JOB-7995201-2026). No quality data are given.
  human_checkpoints:
  - The engagement lead is accountable for output accuracy, relevance and readiness for decision (TW-JOB-8138525-2026).
  role_evolution: The engagement manager role adds AI workflow design and agent supervision. Postings first published
    2026-07-03 (London) and 2026-08-19 (Singapore), both still listed in the public feed on 2026-10-19.
  evidence_grade: B
  sources:
  - ref: TW-JOB-8138525-2026
    title: Engagement Lead (Singapore) job posting
    publisher: Thoughtworks
    type: job-posting
    url: https://www.thoughtworks.com/careers/jobs/8138525?gh_jid=8138525
    date: '2026-08-19'
    access: full
    locator: Role description paragraphs on AI-native delivery and reusable patterns
  - ref: TW-JOB-7995201-2026
    title: Principal Engagement Lead (Technology Advisory), London, job posting
    publisher: Thoughtworks
    type: job-posting
    url: https://www.thoughtworks.com/careers/jobs/7995201?gh_jid=7995201
    date: '2026-07-03'
    access: full
    locator: Responsibilities and requirements on AI workflows and human oversight
  last_reviewed: '2026-10-19'
  notes: Grade B on the strength of a named firm's public postings; they show intent and role design, not outcomes.
    'In-production' is inferred from the postings describing current engagements.
- id: professional-services-delivery-management-13
  title: 'Idea: tracking agent cost, output and margin per engagement alongside human hours'
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: When agents do part of the delivery, utilization and time-and-materials metrics no longer describe who
    did the work or what it cost. Resource managers say they lack the readiness and outcome data to manage blended
    teams (KANTATA-RMI-2026).
  solution: 'Practitioners and vendors are starting to discuss managing agents as team members with their own margin.
    Basware''s chief customer officer and Kantata''s CEO are scheduled to speak on 2026-10-20 at Technology & Services
    World in a session titled ''Congratulations, You Hired an AI Agent! Now Who''s Managing Its Margin?'' (KANTATA-BASWARE-2026).
    Certinia says it is committing to every workflow in its system being executable by an agentic capability or
    a human by year-end (CERTINIA-SOA-2026). Label: idea.'
  outcomes:
  - lever: cost
    description: none published
    figure: none published
    measures: No deployment or figure found; the signal is a scheduled session and survey readiness data.
    provenance: vendor-published
    source_ref: KANTATA-BASWARE-2026
  prerequisites:
  - Outcome data tied to the people and agents that produced it; only 7.3% of the RMI respondents say outcome data
    are easily accessible and routinely used in staffing decisions (KANTATA-RMI-2026).
  risks_and_guardrails:
  - The RMI study covered 44 organisations and was commissioned by Kantata; treat as indicative (KANTATA-RMI-2026).
  human_checkpoints:
  - Not described.
  role_evolution: 'RMI: 52.7% of respondents say they are not equipped to manage hybrid human and AI teams and 4%
    feel well equipped (KANTATA-RMI-2026).'
  evidence_grade: D
  sources:
  - ref: KANTATA-BASWARE-2026
    title: Kantata takes Basware from AI Experimentation to Results
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results
    date: '2026-10-13'
    access: full
    locator: Final paragraph on the scheduled TSW fireside chat
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services (Resource Management Institute study commissioned by Kantata)
    publisher: Kantata / Resource Management Institute
    type: survey
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraphs on hybrid teams and outcome data
  - ref: CERTINIA-SOA-2026
    title: Certinia Unveils the System of Action for Services, and the Largest Expansion of Veda AI to Date
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-unveils-system-of-action-for-services-and-largest-expansion-of-veda-ai-to-date/
    date: '2026-09-09'
    access: full
    locator: Section 'Committing to 100% Agentic Capability Coverage by Year End'
  last_reviewed: '2026-10-19'
  notes: Idea, not a deployment. The conference session was scheduled for 2026-10-20, so it supports a signal only.
    Pricing consequences belong to scoping-pricing and firm-finance.
- id: professional-services-delivery-management-14
  title: Agent project manager that keeps the plan current and chases tasks as milestones move
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: Plans go stale when milestones slip, and a project manager must reconcile data by hand.
  solution: Certinia lists a Project Manager Agent that keeps teams organised, on schedule and driving forward.
    Kantata says project plans update automatically when milestones shift and that timesheet compliance can be checked
    against calendars. Rocketlane says plans stay current and updates are sent automatically (CERTINIA-VEDA-2026;
    KANTATA-SUPERAGENT-2026; ROCKETLANE-AGENTIC-2026).
  outcomes:
  - lever: capacity
    description: Certinia's aggregate claim is that about 50% of project time historically lost to admin is recovered.
      No basis is given.
    figure: about 50% of project time historically lost to admin recovered
    measures: Vendor aggregate in the results panel; the denominator (project time) and method are not stated.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Integrated task, calendar and project data.
  risks_and_guardrails:
  - A published 20-month case study of ChatGPT acting as sole project manager for six projects at an unnamed European
    software firm reports deadlines were largely met but ambiguous or domain-specific requests were misread, producing
    misprioritised tasks or scheduling errors (IPM-CHATGPT-PM-2026, section 4). No figures are given and the firm
    is not named.
  - Rocketlane says agents do the heavy work while the team approves and intervenes when needed (ROCKETLANE-AGENTIC-2026).
  human_checkpoints:
  - Team approves and intervenes on agent actions (ROCKETLANE-AGENTIC-2026).
  role_evolution: Kantata argues the project manager's role shifts toward amplified expertise while routine reconciliation
    moves to the system (KANTATA-SUPERAGENT-2026).
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (agent catalogue and results panel)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: 'Deliver column: Project Manager Agent; results panel'
  - ref: KANTATA-SUPERAGENT-2026
    title: 'More Agents Won''t Fix Unpredictable Projects: Why We Built a Superagent Instead'
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead
    date: '2026-06-16'
    access: full
    locator: Section 'Predicting What You Couldn't See Before'
  - ref: ROCKETLANE-AGENTIC-2026
    title: Rocketlane agentic PSA platform (Nitro) product page
    publisher: Rocketlane
    type: vendor
    url: https://www.rocketlane.com/agentic-psa
    date: '2026-10-14'
    access: full
    locator: Platform capability text
  - ref: IPM-CHATGPT-PM-2026
    title: Can ChatGPT Replace a Human Project Manager? (case study of an unnamed software firm)
    publisher: Institute of Project Management
    type: press
    url: https://instituteprojectmanagement.com/blog/can-chatgpt-replace-human-pm/
    date: '2026-02-11'
    access: full
    locator: Sections 3.2, 4.1 and 4.2
  last_reviewed: '2026-10-19'
  notes: The IPM article is by a training provider about an unnamed firm and gives no data. It is cited as a limit
    signal, not as deployment evidence.
- id: professional-services-delivery-management-15
  title: Retrospective and lessons-learned drafting at project close
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Lessons from completed projects are rarely written up or reused.
  solution: Certinia's Retrospective Drafter Agent captures learnings and outcomes from completed projects, its
    Knowledge Base agent organises documentation into a searchable resource, and a Customer Stories agent shapes
    outcomes into success stories. Automation Consultants lists lessons learnt among its agents' tasks (CERTINIA-VEDA-2026;
    CERTINIA-MOONNOX-2026; ATLASSIAN-TEAM26-AC-2026).
  outcomes:
  - lever: quality
    description: No outcome published.
    figure: none published
    measures: No customer figure found.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Project artefacts and communications captured during delivery.
  risks_and_guardrails:
  - Drafted retrospectives may carry client-confidential detail into a firm-wide knowledge base; none of the sources
    discusses controls.
  human_checkpoints:
  - Project lead reviews and edits the retrospective before it is filed.
  role_evolution: The project manager reviews a drafted retrospective instead of writing one.
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (agent catalogue and results panel)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: 'Manage column: Retrospective Drafter, Knowledge Base'
  - ref: CERTINIA-MOONNOX-2026
    title: Certinia Acquires Moonnox to Power AI-Native Services Delivery
    publisher: Certinia
    type: vendor
    url: https://www.certinia.com/blog/certinia-acquires-moonnox-to-power-ai-native-services-delivery/
    date: '2026-07-21'
    access: full
    locator: Capability 'Value Capture & Knowledge Transfer'
  - ref: ATLASSIAN-TEAM26-AC-2026
    title: 'The agentic PMO: Scaling delivery with Rovo and Claude (sponsored session, Hassan Khadra, Automation
      Consultants; Team ''26 Europe, Amsterdam)'
    publisher: Atlassian
    type: conference
    url: https://events.atlassian.com/teameurope/session/4417894/the-agentic-pmo-scaling-delivery-with-rovo-and-claude
    date: '2026-10-08'
    access: full
    locator: Session abstract, paragraph 2
  last_reviewed: '2026-10-19'
  notes: Reuse of the captured knowledge belongs to knowledge-management.
- id: professional-services-delivery-management-16
  title: Delegating standard implementation tasks and customer documentation to AI inside a PSA platform (in-house
    services organisation)
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types:
  - coordination-scheduling
  - document-production
  - software-systems
  pattern: other
  ladder: delegate
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: Basware's chief customer officer described a services organisation that was low-margin, slow to scope,
    slow to staff, and unsure whether its own software was working (KANTATA-BASWARE-2026).
  solution: 'Basware, a software company whose own services organisation delivers customer implementations (in-house;
    SPI calls such teams embedded service organisations, SPI-AI-2026), implemented Kantata''s PSA, automated billing
    first, and is expanding into three areas: an agent that helps services managers staff projects as timelines
    change, AI embedded across the platform to take on the repetitive work standard to every implementation, and
    AI that generates and sends project documentation to customers (KANTATA-BASWARE-2026). Pattern is ''other'':
    delegation of repeatable implementation tasks to platform AI.'
  outcomes:
  - lever: capacity
    description: Customer success managers who spent four to five hours a day on research before customer calls
      now spend that time on the phone; Basware's CCO says this could let it double revenue with the existing CSM
      team. This is a customer-success result, not an implementation result.
    figure: 4-5 hours a day of pre-call research redeployed
    measures: Basware CCO's statement as reported in Kantata's release; no sample size, baseline method or period.
    provenance: self-reported
    source_ref: KANTATA-BASWARE-2026
  prerequisites:
  - PSA platform already in place with billing automated (KANTATA-BASWARE-2026).
  risks_and_guardrails:
  - The release does not say what review applies to documentation sent to customers; no quality data are given.
  human_checkpoints:
  - Not described for documentation or implementation; the release says people handle tasks unique to each customer.
  role_evolution: Basware's CCO says the aim is to scale the expertise of its people across every project, with
    AI doing the routine work (KANTATA-BASWARE-2026).
  evidence_grade: B
  sources:
  - ref: KANTATA-BASWARE-2026
    title: Kantata takes Basware from AI Experimentation to Results
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results
    date: '2026-10-13'
    access: full
    locator: Sections 'From Chaos to Control', 'Where AI Meets Expertise' and 'From Efficiency to Impact'
  - ref: SPI-AI-2026
    title: Impact of AI on Professional Services 2026 (report landing page)
    publisher: SPI Research
    type: survey
    url: https://spiresearch.com/reports/2026-ai-professional-services-survey/
    date: 2026-10
    access: full
    locator: FAQ on who took part (PSOs and ESOs)
  last_reviewed: '2026-10-19'
  notes: Maturity 'piloting' because the release says Basware is expanding into these areas, not that they are in
    routine production. Vendor press release (updated 2026-10-12; dated 2026-10-13). The customer-success and support
    results in the release belong to other modules.
```

## 3. Module notes

### Processes and key steps (with work types)

1. Sales-to-delivery handoff and kickoff briefing (coordination-scheduling, document-production).
2. Planning: SOW to project plan, solution architecture, phased roadmap (document-production, expert-judgment).
3. Meeting capture, requirements and project documentation (document-production).
4. Periodic status and steering-committee reporting to clients and sponsors (data-reporting, document-production, client-interaction).
5. Risk, issue and portfolio-health tracking (review-assurance, data-reporting).
6. Scope and change control against the SOW (review-assurance, client-interaction).
7. Budget, burn, margin and forecast monitoring; engagement economics (data-reporting).
8. Plan upkeep and task follow-up as milestones move (coordination-scheduling).
9. Close-out, retrospectives and lessons learned (document-production, research-synthesis).

### Common pain points

- Manual report assembly: 72% spend half a day or more collating reports every month (WELLINGTONE-SOPM-2026, summary list; base not defined on the page).
- Late delivery: only 36% of organisations always or mostly complete projects on time (WELLINGTONE-SOPM-2026).
- Low utilization: billable utilization hit a historic low of 66.4% in SPI's 2026 benchmark, as quoted by Certinia (CERTINIA-MOONNOX-2026); A&E utilization is just under 60% (DELTEK-CLARITY-2026).
- Administrative load: Certinia says about 50% of project time has historically been lost to admin (CERTINIA-VEDA-2026, results panel; vendor claim).
- Reconstructing status: Harvey says a partner often cannot see where work stands without asking an associate to rebuild it from email and checklists (HARVEY-ORCH-2026).
- Fragmented systems: Siemens and Diabsolut both describe disconnected regional or business-unit systems before consolidating onto one PSA platform (CERTINIA-DIABSOLUT-2026; CERTINIA-SIEMENS-2026).
- Tacit knowledge held by senior project managers (KANTATA-SUPERAGENT-2026).

### Metrics and benchmarks

- Share of projects using AI: 43.6% in 2026, up from 23.1% in 2025; 245 firms surveyed July to September 2026 (SPI-AI-2026, headline). The same page shows 84.8% saying AI saves them time against a second, unreadable share saying it generates revenue.
- AI adoption versus benefit in A&E: adoption 53% to 70%, generative AI use 64% to 78%, only 38% report measurable positive business impact; 39% say it is too early or are still piloting; 896 A&E firms (DELTEK-CLARITY-2026).
- GovCon: 45% unclear on AI return on investment; top concerns include inaccurate forecasts (29%) and difficulty validating AI-provided insights (26%), asked of IT and security respondents; 917 firms (DELTEK-CLARITY-2026).
- Success by sector: among organisations that deployed AI, the share reporting moderate or significant success runs from 43% (accounting, tax and audit) to 74% (IT service providers); 98% deployed AI but only 20% say it exceeded expectations; 1,000 leaders, June 2026, fieldwork by Sapio Research for Certinia (CERTINIA-GSD-2026; CERTINIA-SOA-2026).
- Vendor-published results, all without stated baselines (treat as claims): proposal or SOW creation about 8 hours to 1; about 5 to 10 hours saved per person per month; 11-23% less margin lost to rework; 90% shorter allocation cycle; USD 400,000+ a year in savings and avoidance per customer (CERTINIA-SOA-2026); 16% more on-time delivery and 20% better forecast accuracy (DELTEK-POLARIS-2026); about 40% lower admin overhead on PMO status reporting, projected (PWC-STATUS-2026); 40% better resource planning accuracy (KANTATA-EXPERTAGENT-2026, vendor claim).
- Customer-reported: Diabsolut documentation time down 70% (CERTINIA-PROVING-2026); Spaulding Ridge architecture drafting about 80 hours to under 20 (CERTINIA-MOONNOX-2026); Automation Consultants roughly 25% of delivery capacity released (ATLASSIAN-TEAM26-AC-2026). All are unaudited.
- Quality evidence: none found for this module (no error, override, correction or parallel-run rates).

### Guardrails and regulatory points

- Human approval before output leaves the firm: Automation Consultants gates every output to Jira, Confluence and client inboxes (ATLASSIAN-TEAM26-AC-2026); Productive requires approval of output before it goes out and lets each agent be given defined permissions (PRODUCTIVE-AGENTS-2026); Harvey uses designated review gates and says agent work stays transparent and auditable (HARVEY-ORCH-2026); Certinia says agents act within permissions, approval thresholds and auditability (CERTINIA-VEDA-2026).
- Deltek says customers can opt in to its Dela AI features (DELTEK-DELA-2026).
- EU AI Act Annex III point 4(b) lists AI used to allocate tasks based on individual behaviour or traits, or to monitor and evaluate worker performance and behaviour, as high-risk; the page shows Annex III obligations applying from 2 December 2027 (EC-AIACT-2026, Annex III and Article 113). Relevant to AI task allocation, utilization monitoring and sentiment scoring in delivery teams in EU-facing firms.
- Client confidentiality, call-recording consent and AI-use disclosure to clients are not discussed in any delivery-management source read; the governance angle covers professional-body rules.

### Frontier signals

- 2026-10-15: Harvey launches Legal Work Orchestration; it says it expects agents to take on an additional 20% of workflow steps within six months and for that share to triple within a year (HARVEY-ORCH-2026).
- 2026-10-08: Automation Consultants presents its 12-agent PMO estate at Atlassian Team '26 Europe (ATLASSIAN-TEAM26-AC-2026).
- 2026-10-05: Kantata's news list shows an Agent Studio launch for professional services (listing only; the article page was not readable) (KANTATA-PRESS-2026). The Expertise Agent page describes Agent Studio as a way to build agents to a firm's own processes and guardrails (KANTATA-EXPERTAGENT-2026).
- 2026-10-20: Basware and Kantata are scheduled to discuss managing an AI agent's margin at Technology & Services World (KANTATA-BASWARE-2026). Signal only; the talk had not yet been given on the date of this file.
- 2026-09-09: Certinia adds 14 agents, doubles its Veda Intelligent Actions library from 64 to 135, makes them callable from Slack, Claude and Microsoft Copilot over MCP, and commits to 100% agentic capability coverage by year-end (CERTINIA-SOA-2026).
- 2026-07-21: Certinia acquires Moonnox to capture context from meetings and tools (CERTINIA-MOONNOX-2026).
- 2026-07-03 and 2026-08-19: Thoughtworks first publishes the two engagement-lead postings for AI-native advisory engagements (TW-JOB-7995201-2026; TW-JOB-8138525-2026).
- 2026-03-24: PwC US publishes its Intelligent Status Insights PMO offering (PWC-STATUS-2026).

### Workforce and role effects

- Project managers shift from assembling information to checking it and handling the client conversation (CERTINIA-PROVING-2026; PWC-STATUS-2026).
- Engagement leads are asked to design how AI is used across an engagement and to supervise output quality (TW-JOB-8138525-2026; TW-JOB-7995201-2026).
- PMO staff become designers and approvers of agent estates (ATLASSIAN-TEAM26-AC-2026).
- Resource managers: 52.7% say they are not equipped to manage hybrid human-agent teams (44 organisations; KANTATA-RMI-2026).
- Hiring and headcount: 82% name AI and data specialists their top hiring priority and 82% expect to grow revenue without proportional billable headcount (CERTINIA-GSD-2026).
- 67% of respondents see PMO scope and responsibilities increasing (WELLINGTONE-SOPM-2026).

### Objections and concerns practitioners raise

- Speed is not accuracy: Kantata's CEO warns of fast, mediocre decisions and of agents optimising in silos (KANTATA-SUPERAGENT-2026).
- Data readiness: an IDC analyst quoted by Certinia says unreliable output and eroding trust follow deployment without a unified data environment (CERTINIA-GSD-2026).
- Return is unclear or unmeasured: 45% of GovCon respondents unclear on AI return; 38% of A&E firms report measurable benefit (DELTEK-CLARITY-2026).
- Leaders overrate results relative to practitioners (CERTINIA-GSD-2026).
- Verification cost: Certinia asserts teams can spend as much time correcting generic AI output as they save (CERTINIA-MOONNOX-2026); no data.
- Saved hours are not converted into revenue: SPI's report parts include "The Leak" (every hour saved must be resold or repriced) (SPI-AI-2026, report outline).
- Ambiguity limits agents: an unnamed firm's 20-month agent-PM experiment reports misprioritised tasks and scheduling errors on unclear requests (IPM-CHATGPT-PM-2026).

### Interview probes for an advisor

1. Which parts of your weekly status pack are still assembled by hand, who reviews the numbers before the client sees them, and how often does that reviewer change something?
2. Where do hours saved on reporting and documentation go: more billable work, lower write-offs, or nowhere you can see? What baseline did you capture first?
3. How do you decide that a client request is out of scope, and how many such requests are caught late today?
4. If agents did part of an engagement, how would you record their work and cost against the engagement margin, and who would own that?
5. Which delivery data (time, budget, risks, notes) sits in one system the agents can read, and which lives in email and heads?


## 4. Routed to other modules

- **staffing-resourcing**: Nextview's Staffing Agent scanning 150 colleagues for skills and availability in seconds (CERTINIA-PROVING-2026); Certinia Resourcing, Work Reallocation and Shortlisting agents (CERTINIA-VEDA-2026); zeb's staffing agent that proposes and pre-books people (NTTDATA-ZEB-2026); Kantata's proactive resourcing and the 44-organisation RMI study (KANTATA-EXPERTAGENT-2026; KANTATA-RMI-2026); Deltek's claim of 40% better time-to-hire with skills-based matching (DELTEK-POLARIS-2026).
- **billing-collections**: Diabsolut's invoice turnaround reported 40% faster (CERTINIA-PROVING-2026); conversational time capture and timesheet compliance (CERTINIA-VEDA-2026; KANTATA-SUPERAGENT-2026; DELTEK-DELA-2026); zeb's timesheet agent (NTTDATA-ZEB-2026).
- **scoping-pricing**: Diabsolut's move to fixed-fee, outcomes-based contracts (CERTINIA-PROVING-2026, summary); Certinia's estimate and SOW agents and the claim of proposal creation from about 8 hours to 1 (CERTINIA-SOA-2026); Neocol's SOW-drafting workflow live across its sales team within nine days (CERTINIA-PROVING-2026); 75% of surveyed organisations expect to increase outcome-based pricing in the next 12 months (CERTINIA-GSD-2026).
- **pursuit-proposals**: Certinia's RFP Responder and the claim of handling 15 times more RFPs (CERTINIA-SOA-2026); Kantata's Expertise Engine at FOIL, where a customer says proposals practically build themselves (KANTATA-CONSULTANCYUK-2025).
- **client-development**: Penrod's seller prep cut in half (CERTINIA-PROVING-2026); Basware customer success managers redeploying 4-5 hours a day of pre-call research (KANTATA-BASWARE-2026).
- **acceptance-risk** (in-house): Legora Intake turns requests from the business in Slack into tracked tasks with an owner and due date, logs task type and turnaround times, and lets a team approve full completion of routine requests such as a standard NDA (LEGORA-INTAKE-2026).
- **firm-finance**: Harvey Command Center adoption analytics and benchmarking, with customer quotes from firms including Foley and Mallesons (HARVEY-CC-2026); AI value measurement through time-capture links is covered in the landscape file under Legora-Laurel.
- **knowledge-management**: Certinia's Knowledge Base agent and Kantata's institutional-memory framing (CERTINIA-VEDA-2026; KANTATA-EXPERTAGENT-2026).
- **work-production** (in-house): BMW Group's legal department rolling out Legora for research, litigation management support, contract review, regulatory monitoring and first drafts, announced 2026-10-08 (LEGORA-BMW-2026).
- **talent-learning**: PMI's hub offers an AI-based project guidance tool grounded in PMI standards and an AI certification for project professionals (PMI-AI-2026, hub page).


## 5. Sources

Dates are publication dates where the page gives one. Where a page is undated, the date is the read date (2026-10-19) or a page-modified date, as noted in the use-case notes and Gaps.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ATLASSIAN-TEAM26-AC-2026 | The agentic PMO: Scaling delivery with Rovo and Claude (sponsored session, Hassan Khadra, Automation Consultants; Team '26 Europe, Amsterdam) | Atlassian | conference | https://events.atlassian.com/teameurope/session/4417894/the-agentic-pmo-scaling-delivery-with-rovo-and-claude | 2026-10-08 | full |
| BIGHAND-MATTERPRICING-2026 | Matter Pricing by BigHand (marketplace listing) | BigHand / SoftwareOne Marketplace | vendor | https://platform.softwareone.com/product/matter-pricing/PCP-7252-7893 | 2026-10-19 | full |
| CERTINIA-DIABSOLUT-2026 | Diabsolut Customer Success Story | Certinia | vendor | https://certinia.com/customer-success-stories/diabsolut/ | 2026-10-19 | full |
| CERTINIA-GSD-2026 | New Global Study Finds AI Success Three Times More Likely at Fully Integrated Organizations (2026 Global Service Dynamics Report; fieldwork by Sapio Research for Certinia) | Certinia | survey | https://www.certinia.com/blog/new-global-study-finds-ai-success-three-times-more-likely-at-fully-integrated-organizations/ | 2026-08-25 | full |
| CERTINIA-MOONNOX-2026 | Certinia Acquires Moonnox to Power AI-Native Services Delivery | Certinia | vendor | https://www.certinia.com/blog/certinia-acquires-moonnox-to-power-ai-native-services-delivery/ | 2026-07-21 | full |
| CERTINIA-PROVING-2026 | Certinia Customers Are Proving Veda AI Agents Deliver Real Results | Certinia | vendor | https://www.certinia.com/blog/certinia-customers-are-proving-veda-ai-agents-deliver-real-results/ | 2026-09-03 | full |
| CERTINIA-SIEMENS-2026 | Siemens standardizes global services initiating 450 monthly projects with Certinia (customer story) | Certinia | vendor | https://certinia.com/customer-success-stories/siemens/ | 2026-10-19 | full |
| CERTINIA-SOA-2026 | Certinia Unveils the System of Action for Services, and the Largest Expansion of Veda AI to Date | Certinia | vendor | https://www.certinia.com/blog/certinia-unveils-system-of-action-for-services-and-largest-expansion-of-veda-ai-to-date/ | 2026-09-09 | full |
| CERTINIA-VEDA-2026 | Veda AI: System of Action for Professional Services (agent catalogue and results panel) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 | full |
| DELOITTE-AWS-2026 | Meeting Data analyzer Agent (Deloitte Agent Fleet, Innovation Support Agent Suite) AWS Marketplace listing | Deloitte / AWS Marketplace | firm | https://aws.amazon.com/marketplace/pp/prodview-obfkw4hi57r3i | 2026-09-30 | full |
| DELTEK-CLARITY-2026 | The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures for Project-Based Businesses | Deltek | survey | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| DELTEK-DELA-2026 | Deltek Dela (AI product page) | Deltek | vendor | https://www.deltek.com/en/products/platform/dela/ | 2026-05-27 | full |
| DELTEK-POLARIS-2026 | Deltek Polaris (PSA product page) | Deltek | vendor | https://www.deltek.com/en/products/polaris/ | 2026-05-27 | full |
| EC-AIACT-2026 | EU AI Act, Annex III (high-risk systems) and Article 113 as displayed with amended dates (unofficial reproduction by the Future of Life Institute) | European Union / artificialintelligenceact.eu | regulator | https://artificialintelligenceact.eu/annex/3/ | 2024-07-12 | full |
| HARVEY-CC-2026 | Harvey Command Center (product page with customer quotes) | Harvey | vendor | https://www.harvey.ai/platform/command-center | 2026-10-19 | full |
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 | full |
| IPM-CHATGPT-PM-2026 | Can ChatGPT Replace a Human Project Manager? (case study of an unnamed software firm) | Institute of Project Management | press | https://instituteprojectmanagement.com/blog/can-chatgpt-replace-human-pm/ | 2026-02-11 | full |
| KANTATA-BASWARE-2026 | Kantata takes Basware from AI Experimentation to Results | Kantata | vendor | https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results | 2026-10-13 | full |
| KANTATA-CONSULTANCYUK-2025 | Kantata launches new AI platform for consulting workflow | Consultancy.uk | press | https://www.consultancy.uk/news/41834/kantata-launches-new-ai-platform-for-consulting-workflow | 2025-10-14 | full |
| KANTATA-EXPERTAGENT-2026 | Expertise Agent & Workflows (product page) | Kantata | vendor | https://www.kantata.com/ai/expertise-agent-and-workflows | 2026-10-19 | full |
| KANTATA-PRESS-2026 | Kantata News & Press listing | Kantata | vendor | https://www.kantata.com/press | 2026-10-19 | full |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services (Resource Management Institute study commissioned by Kantata) | Kantata / Resource Management Institute | survey | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| KANTATA-SUPERAGENT-2026 | More Agents Won't Fix Unpredictable Projects: Why We Built a Superagent Instead | Kantata | vendor | https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead | 2026-06-16 | full |
| LEGORA-BMW-2026 | Legora collaborates with BMW Group to advance AI-enabled legal services | Legora | vendor | https://legora.com/newsroom/legora-collaborates-with-bmw-group-to-advance-ai-enabled-legal-services | 2026-10-08 | full |
| LEGORA-INTAKE-2026 | Legora launches Intake: an agentic front door for in-house legal teams | Legora | vendor | https://legora.com/newsroom/legora-launches-intake-an-agentic-front-door-for-in-house-legal-teams | 2026-10-13 | full |
| LTH-PLANNINGBLOX-2026 | Planning Blox vendor profile | Legaltech Hub | vendor | https://www.legaltechnologyhub.com/vendors/planning-blox/ | 2026-10-19 | full |
| NTTDATA-ZEB-2026 | zeb: putting agentic AI into action | NTT DATA | vendor | https://nttdata-solutions.com/br/success-stories/zeb-putting-agentic-ai-into-action/ | 2026-05-07 | full |
| ORACLE-PPM-2026 | Oracle Fusion Cloud Project Management (product page) | Oracle | vendor | https://www.oracle.com/erp/project-management/ | 2026-10-19 | full |
| PMI-AI-2026 | Artificial Intelligence in Project Management (PMI hub page) | Project Management Institute | professional-body | https://www.pmi.org/learning/ai-in-project-management | 2026-10-19 | full |
| PRODUCTIVE-AGENTS-2026 | AI Agents for Project Management & Operations (product page) | Productive | vendor | https://productive.io/agents | 2026-10-19 | full |
| PWC-STATUS-2026 | Manual PMO Status Reporting Is Draining 40% of Project Management Hours. This AI Automates It. (Intelligent Status Insights) | PwC US | firm | https://www.pwc.com/us/en/tech-effect/innovation/automate-pmo-status-reporting.html | 2026-03-24 | full |
| ROCKETLANE-AGENTIC-2026 | Rocketlane agentic PSA platform (Nitro) product page | Rocketlane | vendor | https://www.rocketlane.com/agentic-psa | 2026-10-14 | full |
| ROCKETLANE-EARTHWISE-2026 | How EarthWise Pets Did It (customer story: AI Fills call summaries in franchise onboarding) | Rocketlane | vendor | https://www.rocketlane.com/customers/how-earthwise-pets-captures-100-of-franchise-commitments-with-rocketlanes-ai-teammate | 2026-10-14 | full |
| SPI-AI-2026 | Impact of AI on Professional Services 2026 (report landing page) | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-10 | full |
| TW-JOB-7995201-2026 | Principal Engagement Lead (Technology Advisory), London, job posting | Thoughtworks | job-posting | https://www.thoughtworks.com/careers/jobs/7995201?gh_jid=7995201 | 2026-07-03 | full |
| TW-JOB-8138525-2026 | Engagement Lead (Singapore) job posting | Thoughtworks | job-posting | https://www.thoughtworks.com/careers/jobs/8138525?gh_jid=8138525 | 2026-08-19 | full |
| WELLINGTONE-SOPM-2026 | The State of Project Management Report 2026 (landing page summary) | Wellingtone | survey | https://www.wellingtone.co.uk/state-of-project-management/ | 2026-03-12 | full |

## 6. Gaps

- **No independent quality measurement.** No error, override, correction, false-positive or parallel-run data for AI-drafted status reports, plans, risk alerts or scope flags. Every outcome figure is vendor-published or self-reported and unaudited.
- **Consulting majors.** McKinsey, BCG, Bain, Deloitte, EY, KPMG and Accenture primary pages held nothing on delivery management that was reachable. Accenture's newsroom (checked 2026-10-19) lists federal agent launchpads, a Workday forward-deployed engineering programme and acquisitions, none specific to delivery management. Infosys and TCS press pages were checked with no delivery-management content. PwC and Deloitte appear only as an offering page and a marketplace listing with no named client.
- **Law-firm and in-house delivery management.** No named law firm or legal department was found using AI for matter planning, budget tracking or status; Harvey orchestration is announced and BigHand and Planning Blox are listings. CLOC session content is JavaScript-rendered and unreadable. Intapp pages returned 403.
- **Pages not readable.** Salesforce AppExchange write-ups on Diabsolut and Nextview (JavaScript-rendered), ERP Today on Kantata's Expertise Agent (403), PMI Pulse and PMI research pages (403), Planview (403), a guessed URL for Gartner's older project-management prediction release (404), Microsoft's Project Manager agent documentation (404), and Kantata articles on Agent Studio, "5 metrics to prove your AI strategy's business value" and "Kantata Turns Expertise into Scalable AI Agents" (404 or mirror blocked).
- **Abstract-only reads.** The Automation Consultants talk (abstract only, recording not seen); SPI's 2026 report (paywalled, landing page only; one headline figure's partner share was not recoverable); Wellingtone's 2026 report (landing page only); the full Kantata/RMI report; Deltek Clarity reports.
- **Job postings.** The only services-firm postings read were two from Thoughtworks. A Deloitte PMO posting found by search had been filled and showed no content. Harvey and Legora postings are vendor roles and were not used as evidence of services-firm practice.
- **Podcasts and community.** Kantata's "Professional Services Pursuit" podcast episode and practitioner community threads were not accessed.
- **Dating.** Certinia's 3 September blog shows no year on the page; 2026 is inferred. Several product pages are undated and carry the read date or a page-modified date. Deloitte's AWS listing date is the page's published-time header.
- **Searches.** Ten web searches were used; most returned vendor marketing and no additional named deployments.
