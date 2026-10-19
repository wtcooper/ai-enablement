# Professional services, staffing and resourcing: discourse angle

Prepared 2026-10-19. Archetype: professional-services. Module: staffing-resourcing (matching people to work: resource planning, capacity forecasting, skills inventories, utilization, scheduling and bench management). Angle: discourse (what practitioners are saying, last 12 to 18 months). Method: `curl` through a private working folder, the r.jina.ai text mirror for one blocked page, and 15 web searches from the shared budget. Sources marked `search-only` were not readable in full. Quotations are under 25 words. Items tagged **in-house** come from corporate legal departments. Public sources only.

## 1. Summary

**What practitioners are saying.** Resource management is being re-described, mostly by the vendors that sell it, as a strategic capacity function that must plan people and AI agents together. Independent practitioner voices on staffing are scarce. The discourse sits in four places: PSA and resourcing vendors (Kantata, Certinia, Rocketlane, Accelo, BigHand), the industry association TSIA, a handful of legal trade columns and podcasts, and one COO roundtable.

- **Readiness is low and the measurable bits are vendor-published.** In Kantata's study of 44 organizations, 39% are still in traditional staffing mode and 31% are beyond experimentation; 52.7% say they are not equipped to manage hybrid human and agent teams; 7.3% routinely use outcome data in staffing (KANTATA-RMI-2026). TSIA research, reported by Accelo, finds 97% of organizations track utilization but fewer than 2% use AI for scheduling and allocation (ACCELO-TSIA-2026).
- **Quality evidence is absent.** No source reports error rates, override rates, acceptance rates or parallel-run results for AI staffing recommendations. The closest are trust numbers from a vendor survey: 12% of leaders fully trust their system data, and 89% spend significant time verifying AI outputs (KANTATA-STATE-2026).
- **Named AI-staffing examples are thin.** McKinsey plans to use agents to supplement the staff who match consultants to client teams (BLOOMBERGLAW-MCK-2026, paywalled). Basware describes an agent helping its services managers staff projects, without staffing metrics (KANTATA-BASWARE-2026). The only named, figured resourcing deployments are two law firms using a non-AI resourcing platform (DLA Piper, Womble Bond Dickinson), with figures published by the vendor (BIGHAND-DLAPR-2026; BIGHAND-WBD-2026).
- **The law-firm conversation is about allocation fairness and the talent pipeline, not algorithms.** Partner-led, relationship-based allocation is described as the problem (BIGHAND-DLA-2026; BIGHAND-WBD-2026). A columnist warns that capacity freed by AI gets refilled with more work (TRI-LAWPROF-2026), and a legal staffing provider says associates choose billable work over AI training even when offered credit (GEEK-LATITUDE-2026).
- **Conference discourse on staffing was not found at the big legal events.** The Legalweek and ILTACON recaps read for this run contain no staffing or resourcing content (TRI-LEGALWEEK-2026; EDISCOVERYTODAY-ILTACON-2026). The conference signals are from vendor-run events: the Resource Management Global Symposium, BigHand Conference, Kantata Converge and a Technology & Services World session in Las Vegas scheduled for 2026-10-20.

**Use cases.** 15 candidates: 3 grade B, 11 grade C, 1 grade D. No grade A: no organization publishes a measured staffing outcome for an AI tool. The three B entries rest on four named organizations (Basware; DLA Piper and Womble Bond Dickinson together; Reed Smith). One B entry describes a non-AI platform and one predates the 18-month window.

## 2. Use cases

```yaml
- id: professional-services-staffing-resourcing-01
  title: Staffing recommendation and shortlist agent inside the PSA platform
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Resource managers hunt across systems for who has the skills, is free and fits the budget. Basware's chief customer officer
    described the services organization before the change as low-margin, slow to scope and slow to staff (KANTATA-BASWARE-2026).
  solution: >-
    An agent in the services platform surfaces consultant background and history, accounts for schedule conflicts and availability,
    and drafts candidate shortlists, so the resource manager decides rather than searches (CERTINIA-VEDA-2026). Basware says
    a Kantata Expertise Engine agent helps its services managers decide how to staff projects as timelines and requirements
    change (KANTATA-BASWARE-2026).
  outcomes:
  - lever: speed
    description: >-
      No staffing metric published. The Basware release reports gains in customer-success research time and support tickets,
      not staffing.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: KANTATA-BASWARE-2026
  prerequisites:
  - Skills, availability and cost held in one system (TSIA-RM-2026).
  - >-
    Connected CRM, PSA and HR data so demand, supply and past performance can be read together (TSIA-RM-2026).
  risks_and_guardrails:
  - >-
    TSIA says AI amplifies broken operational data, so unreliable inputs produce unreliable staffing recommendations (TSIA-RM-2026).
  - >-
    In Kantata's survey 12% of leaders fully trust the data in their systems, down from 24% a year earlier (KANTATA-STATE-2026).
  human_checkpoints:
  - >-
    The resource manager makes the final assignment; the Icon Cloud Consulting architect describes the agent as removing the
    hunt for information so managers can 'make the right call' (CERTINIA-VEDA-2026).
  role_evolution: >-
    TSIA describes the resource management office evolving into what it calls a 'hybrid workforce command center' rather than
    a scheduling team (TSIA-RM-2026). In Kantata's study 72% of respondents said resource management is primarily or solely
    operational in their organization (KANTATA-RMI-2026).
  evidence_grade: B
  sources:
  - ref: KANTATA-BASWARE-2026
    title: Kantata takes Basware from AI Experimentation to Results
    publisher: Kantata press release
    type: vendor
    url: >-
      https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results
    date: '2026-10-13'
    access: full
    locator: '''Smarter Resource Management'' paragraph and Johnston''s opening quote'
  - ref: CERTINIA-VEDA-2026
    title: Certinia AI / Veda agents for professional services (product page)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: >-
      Plan agents list (Resourcing, Shortlisting); customer quote from Icon Cloud Consulting solution architect
  - ref: TSIA-RM-2026
    title: Professional Services Resource Management in the PS 2.0 Era (Bo DiMuccio)
    publisher: TSIA
    type: professional-body
    url: https://www.tsia.com/blog/professional-services-resource-management
    date: '2026-05-27'
    access: full
    locator: >-
      Sections 'The PS 2.0 Transformation Paradox' and 'From Resource Management Office to Hybrid Workforce Command Center'
  - ref: KANTATA-STATE-2026
    title: >-
      87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce (State of the Professional Services
      Industry survey, Censuswide, 200 leaders)
    publisher: Kantata press release via CFO Dive
    type: survey
    url: >-
      https://www.cfodive.com/press-release/20260108-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-thei/
    date: '2026-01-08'
    access: full
    locator: Paragraph on trust in data
  - ref: KANTATA-RMI-2026
    title: >-
      New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional
      Services (study: Resource Management in the Age of AI)
    publisher: Kantata, reporting a Resource Management Institute study it commissioned
    type: survey
    url: >-
      https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraph on operational versus strategic role
  last_reviewed: '2026-10-19'
  notes: >-
    Grade B is borderline. Both the Basware release and the Certinia page are vendor-published, and the Basware release is
    ambiguous on tense: it says the company 'is expanding into' three areas and then describes the staffing agent in the present
    tense, without stating that it is in production. Set to piloting for that reason. Basware sells invoice software, so this
    is an internal services organization. The Certinia page shows an animated counter labelled 'faster staffing decisions';
    the number is not in the page text and the page source holds three counter values (50, 75, 24) whose mapping to labels
    is not stated, so no figure is used. The page also claims automatic re-matching when resources shift; no customer data
    accompanies that claim.
- id: professional-services-staffing-resourcing-02
  title: Agents supplement the staff who match consultants to client teams (McKinsey, announced)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Bloomberg reports that as McKinsey grew to almost 40,000 employees, the matching of consultants to clients, done behind
    the scenes by professional development staff for decades, became more complex (BLOOMBERGLAW-MCK-2026).
  solution: >-
    McKinsey plans to use AI agents to supplement those staff when choosing consultants for client teams. The firm's North
    America chief people officer said AI will help ensure the best people are in the right situations (BLOOMBERGLAW-MCK-2026).
  outcomes:
  - lever: speed
    description: No outcome published; this is a stated plan.
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: BLOOMBERGLAW-MCK-2026
  prerequisites:
  - Not stated in the readable part of the article.
  risks_and_guardrails:
  - >-
    The article's opening says the move may surprise some of the firm's customers (BLOOMBERGLAW-MCK-2026).
  human_checkpoints:
  - >-
    The agents supplement the professional development staff rather than replace them, according to the opening paragraphs
    (BLOOMBERGLAW-MCK-2026).
  role_evolution: >-
    Professional development staff keep the matching role, with agents added to their work (BLOOMBERGLAW-MCK-2026).
  evidence_grade: C
  sources:
  - ref: BLOOMBERGLAW-MCK-2026
    title: >-
      McKinsey Plans to Use AI Agents to Help Select Client Teams (paywalled; opening paragraphs only)
    publisher: Bloomberg Law
    type: press
    url: >-
      https://news.bloomberglaw.com/financial-accounting/mckinsey-plans-to-use-ai-agents-to-help-select-client-teams
    date: '2026-05-01'
    access: search-only
    locator: Opening paragraphs (paywalled after that); published 2026-05-01
  last_reviewed: '2026-10-19'
  notes: >-
    Only the opening paragraphs were readable, so access is recorded as search-only and the entry cannot support grade A or
    B. The 'agentify our staffing' quote is truncated in the teaser. Other outlets give differing counts of McKinsey AI agents
    (12,000 vs 25,000); those secondary figures are not used. The word 'plans' is the source's.
- id: professional-services-staffing-resourcing-03
  title: Continuous re-matching and work reallocation when people or demand shift
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Without pipeline visibility, resource managers scramble when projects close or people move, which TSIA says causes delayed
    starts, overbooked top performers and underused staff (TSIA-RM-2026).
  solution: >-
    Certinia describes an agent that proposes replacements for work in flight and re-matches staff when resources shift (CERTINIA-VEDA-2026).
    Rocketlane describes a Resource Management Agent that monitors allocation continuously, flags people nearing over-capacity
    and ranks reallocation options by delivery impact and margin fit; the vendor says it is 'currently in active rollout'
    (ROCKETLANE-2026).
  outcomes:
  - lever: capacity
    description: No measured outcome published for reallocation agents.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: ROCKETLANE-2026
  prerequisites:
  - >-
    Live allocation and timesheet data. Rocketlane lists automated allocation-accuracy checks (for example, flagging anyone
    booked above 100% across weeks) as the data-integrity layer (ROCKETLANE-2026).
  risks_and_guardrails:
  - >-
    DLA Piper's senior resource manager says the software helps find cover but the resource manager supplies the context (BIGHAND-DLA-2026).
  - >-
    Rocketlane gives no customer data on the agent's recommendations being accepted or overridden (ROCKETLANE-2026).
  human_checkpoints:
  - >-
    Agents 'propose' or 'surface' options; a person confirms (CERTINIA-VEDA-2026; ROCKETLANE-2026).
  role_evolution: >-
    Resource managers move from weekly staffing calls toward reviewing ranked options, in the vendor's description (ROCKETLANE-2026).
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: Certinia AI / Veda agents for professional services (product page)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Plan agents list (Work Reallocation Agent); 'Staff with confidence' panel
  - ref: ROCKETLANE-2026
    title: 'AI for PS resource allocation: the 2026 guide for professional services leaders'
    publisher: Rocketlane
    type: vendor
    url: https://rocketlane.com/blogs/ai-for-ps-resource-allocation
    date: '2026-07-22'
    access: full
    locator: Section 'How does Rocketlane Nitro reshape PS resource allocation?', Level 3 Workforce AI
  - ref: TSIA-RM-2026
    title: Professional Services Resource Management in the PS 2.0 Era (Bo DiMuccio)
    publisher: TSIA
    type: professional-body
    url: https://www.tsia.com/blog/professional-services-resource-management
    date: '2026-05-27'
    access: full
    locator: '''Staffing Decisions Become Reactive'''
  - ref: BIGHAND-DLA-2026
    title: >-
      A Global Firm Needs a Global View: DLA Piper Scales Legal Resourcing Excellence with BigHand Resource Management (case
      study)
    publisher: BigHand
    type: vendor
    url: >-
      https://www.bighand.com/en-us/resources/case-studies/dla-piper-bighand-resource-management/
    date: '2026-06-17'
    access: full
    locator: Alix Love quote, 'The Solution' section
  last_reviewed: '2026-10-19'
  notes: >-
    No named customer, override rate or accuracy figure was found for either product. Both claims are product descriptions.
- id: professional-services-staffing-resourcing-04
  title: Statement of work converted into a draft plan with suggested assignments
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Kickoff preparation, including building the plan and finding people, takes days once a deal closes (ROCKETLANE-2026).
  solution: >-
    Rocketlane's Workforce Agent turns a statement of work into a draft plan with suggested resource assignments (ROCKETLANE-2026).
    Certinia lists agents that draft statements of work, build implementation plans and hand deals from sales to delivery
    (CERTINIA-VEDA-2026).
  outcomes:
  - lever: speed
    description: >-
      Vendor says kickoff preparation 'compresses from days to hours'; no baseline or customer given.
    figure: days to hours (qualitative)
    measures: Vendor's description of kickoff prep time; no numerator or denominator
    provenance: vendor-published
    source_ref: ROCKETLANE-2026
  prerequisites:
  - Signed SOW in structured form and a queryable skills matrix (ROCKETLANE-2026).
  risks_and_guardrails:
  - >-
    Suggested assignments rest on skills data that TSIA says is often self-reported and stale (TSIA-RM-2026).
  human_checkpoints:
  - >-
    The output is a draft with suggested assignments; the vendor does not describe an automatic booking (ROCKETLANE-2026).
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
  - ref: ROCKETLANE-2026
    title: 'AI for PS resource allocation: the 2026 guide for professional services leaders'
    publisher: Rocketlane
    type: vendor
    url: https://rocketlane.com/blogs/ai-for-ps-resource-allocation
    date: '2026-07-22'
    access: full
    locator: Level 3 Workforce AI paragraph
  - ref: CERTINIA-VEDA-2026
    title: Certinia AI / Veda agents for professional services (product page)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Plan and Deliver agent lists
  - ref: TSIA-RM-2026
    title: Professional Services Resource Management in the PS 2.0 Era (Bo DiMuccio)
    publisher: TSIA
    type: professional-body
    url: https://www.tsia.com/blog/professional-services-resource-management
    date: '2026-05-27'
    access: full
    locator: '''Skills Data Becomes Outdated'''
  last_reviewed: '2026-10-19'
  notes: >-
    Overlaps delivery-management (kickoff planning); kept here for the suggested-assignment step only.
- id: professional-services-staffing-resourcing-05
  title: Pipeline-driven demand and capacity forecasting with what-if scenarios
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Forecasting is a weak point. In Kantata's resource-management study the barriers named most were limited understanding
    of where AI applies (49%), poor or fragmented data on skills, outcomes, demand and capacity (47%), and tools not ready
    for AI-driven staffing (41%) (KANTATA-RMI-2026).
  solution: >-
    Link the sales pipeline to the capacity model before deals close and test cases such as two deals closing in the same
    month to see the capacity map, utilization and margin effect (ROCKETLANE-2026). TSIA describes demand, supply and performance
    signals feeding a move from reactive to predictive planning (TSIA-RM-2026); Accelo describes forecasting demand from pipeline
    before deals close (ACCELO-TSIA-2026).
  outcomes:
  - lever: quality
    description: >-
      Among organizations using AI to optimize essential processes, a share report improved forecast accuracy or utilization.
    figure: 52%
    measures: >-
      Share of respondents (from 200 professional services leaders surveyed by Censuswide for Kantata) who report improved
      forecast accuracy or utilization; the release does not give the exact denominator for this subset
    provenance: vendor-published
    source_ref: KANTATA-STATE-2026
  prerequisites:
  - Pipeline (CRM), PSA, finance and HR data connected (TSIA-RM-2026; ACCELO-TSIA-2026).
  - >-
    A single view of skills and capacity; Accelo notes data often sits in the PSA, CRM, HR systems and spreadsheets (ACCELO-TSIA-2026).
  risks_and_guardrails:
  - >-
    Accelo's CEO said AI 'amplifies' whatever foundation exists, and layering it on fragmented systems gives faster confusion
    (ACCELO-TSIA-2026).
  - >-
    Only 12% of leaders fully trust their system data, and 89% say they spend significant time verifying AI outputs (KANTATA-STATE-2026).
  human_checkpoints:
  - >-
    Planners decide what to hire or reassign from the scenarios; sources describe the forecast as decision support (TSIA-RM-2026).
  role_evolution: >-
    TSIA frames resource management as a strategic capability that forecasts demand rather than filling open roles (TSIA-RM-2026).
  evidence_grade: C
  sources:
  - ref: KANTATA-RMI-2026
    title: >-
      New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional
      Services (study: Resource Management in the Age of AI)
    publisher: Kantata, reporting a Resource Management Institute study it commissioned
    type: survey
    url: >-
      https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraph on barriers to AI-augmented resource management
  - ref: ROCKETLANE-2026
    title: 'AI for PS resource allocation: the 2026 guide for professional services leaders'
    publisher: Rocketlane
    type: vendor
    url: https://rocketlane.com/blogs/ai-for-ps-resource-allocation
    date: '2026-07-22'
    access: full
    locator: What-if scenario modeling section
  - ref: TSIA-RM-2026
    title: Professional Services Resource Management in the PS 2.0 Era (Bo DiMuccio)
    publisher: TSIA
    type: professional-body
    url: https://www.tsia.com/blog/professional-services-resource-management
    date: '2026-05-27'
    access: full
    locator: '''Create a Unified Resource Intelligence Layer'''
  - ref: ACCELO-TSIA-2026
    title: >-
      How AI Is Reshaping Resource Utilization and Capacity Management (write-up of a TSIA and Accelo conversation)
    publisher: Accelo
    type: vendor
    url: https://www.accelo.com/blog/ai-era-resource-utilization-capacity-management
    date: '2026-06-03'
    access: full
    locator: '''What Good Capacity Management Looks Like Today'''
  - ref: KANTATA-STATE-2026
    title: >-
      87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce (State of the Professional Services
      Industry survey, Censuswide, 200 leaders)
    publisher: Kantata press release via CFO Dive
    type: survey
    url: >-
      https://www.cfodive.com/press-release/20260108-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-thei/
    date: '2026-01-08'
    access: full
    locator: Paragraphs on AI performance gains and trust in data
  last_reviewed: '2026-10-19'
  notes: >-
    Rocketlane also cites SPI 2026 benchmarks (AI-wide users 81.5% on-time delivery and 17.9% EBITDA versus 70.8% and 6.0%
    for non-users). That is a secondhand vendor citation of a paywalled report, and it is not specific to staffing, so it
    is not used as an outcome.
- id: professional-services-staffing-resourcing-06
  title: AI-maintained skills inventory (profiles updated from project and delivery data)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Self-reported skills profiles say little about how recently a skill was used, how complex the work was or the proficiency
    level (TSIA-RM-2026). In BigHand's survey 45% of law firms had only partial data on associates' skill sets (BIGHAND-DLAPR-2026).
  solution: >-
    TSIA's first maturity level has AI continuously update consultant profiles from project data, certifications and delivery
    artifacts, and extends the same register to AI tools (capabilities, reliability, limits, oversight needed) (TSIA-RM-2026).
  outcomes:
  - lever: quality
    description: No outcome published.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: TSIA-RM-2026
  prerequisites:
  - Project history and delivery artifacts accessible to the system (TSIA-RM-2026).
  - A structured schema for proficiency, recency, industry and certifications (TSIA-RM-2026).
  risks_and_guardrails:
  - >-
    EU AI Act high-risk obligations for AI used in employment and management of workers apply from 2 December 2027, so profile
    inference about people needs a compliance check for EU-facing staff (EC-AIACT-2026).
  human_checkpoints:
  - Not specified; TSIA does not say who confirms inferred skills.
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: TSIA-RM-2026
    title: Professional Services Resource Management in the PS 2.0 Era (Bo DiMuccio)
    publisher: TSIA
    type: professional-body
    url: https://www.tsia.com/blog/professional-services-resource-management
    date: '2026-05-27'
    access: full
    locator: >-
      'Skills Data Becomes Outdated'; 'Build the Skills Genome'; 'How AI Improves Professional Services Resource Management'
      Level 1
  - ref: BIGHAND-DLAPR-2026
    title: >-
      DLA Piper Reports More Than 600 Hours Saved at Half-Year End with BigHand Resource Management (press release)
    publisher: BigHand
    type: vendor
    url: >-
      https://www.bighand.com/en-us/resources/news/dla-piper-bighand-resource-management-press-release/
    date: '2026-06-18'
    access: full
    locator: Paragraph citing the Navigating the Million Dollar Problem report
  - ref: EC-AIACT-2026
    title: 'AI Act: regulatory framework for AI (living page, read 2026-10-19)'
    publisher: European Commission
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: 2026-10
    access: full
    locator: High-risk use cases list and timeline section
  last_reviewed: '2026-10-19'
  notes: >-
    The 45% figure measures firms with only partial visibility into associate skill sets, as reported in BigHand's own report;
    the sample is not given in the sources read. No source documents a deployed AI-inferred skills inventory in a professional
    services firm.
- id: professional-services-staffing-resourcing-07
  title: Bench-gap detection and redeployment against open pipeline
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Underused staff are found late, and bench time and overbooking sit side by side (TSIA-RM-2026).
  solution: >-
    Rocketlane describes an agent that surfaces a bench gap when confirmed allocation falls below target for the next two
    to three weeks and checks open pipeline and internal project needs against that person's skill profile (ROCKETLANE-2026).
    Certinia says its matching reduces bench time in real time (CERTINIA-VEDA-2026).
  outcomes:
  - lever: capacity
    description: No outcome published.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: ROCKETLANE-2026
  prerequisites:
  - >-
    Confirmed allocation data, pipeline data and skill profiles in one place (ROCKETLANE-2026).
  risks_and_guardrails:
  - >-
    Utilization targets differ widely; TSIA's DiMuccio says most firms run between 55% and 65% utilization, so thresholds
    need local setting (ACCELO-TSIA-2026).
  human_checkpoints:
  - The agent surfaces a gap and candidate work; a manager redeploys (ROCKETLANE-2026).
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: ROCKETLANE-2026
    title: 'AI for PS resource allocation: the 2026 guide for professional services leaders'
    publisher: Rocketlane
    type: vendor
    url: https://rocketlane.com/blogs/ai-for-ps-resource-allocation
    date: '2026-07-22'
    access: full
    locator: Level 3 Workforce AI paragraph
  - ref: CERTINIA-VEDA-2026
    title: Certinia AI / Veda agents for professional services (product page)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: '''Staff with confidence, not guesswork'' panel'
  - ref: ACCELO-TSIA-2026
    title: >-
      How AI Is Reshaping Resource Utilization and Capacity Management (write-up of a TSIA and Accelo conversation)
    publisher: Accelo
    type: vendor
    url: https://www.accelo.com/blog/ai-era-resource-utilization-capacity-management
    date: '2026-06-03'
    access: full
    locator: '''The New Capacity Management Equation'''
  - ref: TSIA-RM-2026
    title: Professional Services Resource Management in the PS 2.0 Era (Bo DiMuccio)
    publisher: TSIA
    type: professional-body
    url: https://www.tsia.com/blog/professional-services-resource-management
    date: '2026-05-27'
    access: full
    locator: '''Staffing Decisions Become Reactive'''
  last_reviewed: '2026-10-19'
  notes: Vendor product descriptions only; no customer named.
- id: professional-services-staffing-resourcing-08
  title: Hybrid human and agent capacity planning (agents as schedulable, measurable capacity)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: emerging
  problem: >-
    Capacity planning assumed people. In Kantata's 2026 survey 87% plan to use AI agents as part of their workforce, and managing
    and integrating agents into delivery was named the top resource and project management challenge (KANTATA-STATE-2026).
    In the Resource Management Institute study 52.7% of respondents said they are not equipped to manage hybrid teams, and
    4% feel well equipped (KANTATA-RMI-2026).
  solution: >-
    Separate work that is structured and repeatable (status reports, reconciliations, documentation) from work that needs
    people when staffing, and plan agents as capacity that is allocated and measured (ACCELO-TSIA-2026; KANTATA-FORBES-2026).
    TSIA's third maturity level optimizes work across consultants, subcontractors, partners and AI agents in one model (TSIA-RM-2026).
  outcomes:
  - lever: capacity
    description: >-
      Illustration only: a 200-hour engagement with 60 'agent-eligible' hours would need 140 human hours.
    figure: 200 to 140 hours (hypothetical)
    measures: A hypothetical engagement used by Accelo to explain the idea; not measured
    provenance: vendor-published
    source_ref: ACCELO-TSIA-2026
  - lever: capacity
    description: Accelo says one unnamed agency cut time spent on resource planning by half.
    figure: 50%
    measures: >-
      Reduction in time spent on resource planning at one unnamed Accelo customer; baseline and method not given
    provenance: vendor-published
    source_ref: ACCELO-TSIA-2026
  prerequisites:
  - >-
    A register of agent capabilities, reliability and oversight needs, alongside human skills (TSIA-RM-2026).
  - >-
    Systems able to attribute work, cost and value across people and agents; 90% of leaders say this will be needed (KANTATA-STATE-2026).
  risks_and_guardrails:
  - >-
    Edwards asks how to schedule an agent, measure it beside consultants and keep hybrid delivery accountable; the article
    gives no answers, only the questions (KANTATA-FORBES-2026).
  - >-
    TSIA research cited by Accelo finds 97% of organizations track utilization but fewer than 2% use AI to support scheduling
    and allocation (ACCELO-TSIA-2026).
  human_checkpoints:
  - >-
    Humans keep judgment, client relationships and strategic guidance in the sources' split of work (ACCELO-TSIA-2026).
  role_evolution: >-
    Accelo's CEO says the aim is for highly skilled professionals to spend more time on work only they can do (ACCELO-TSIA-2026).
    Kantata's Edwards says nobody yet knows the answers on talent mix and how to bill agents (UNITEAI-KANTATA-2026).
  evidence_grade: C
  sources:
  - ref: KANTATA-STATE-2026
    title: >-
      87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce (State of the Professional Services
      Industry survey, Censuswide, 200 leaders)
    publisher: Kantata press release via CFO Dive
    type: survey
    url: >-
      https://www.cfodive.com/press-release/20260108-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-thei/
    date: '2026-01-08'
    access: full
    locator: Paragraphs on agents in the workforce and on attribution across humans and agents
  - ref: KANTATA-RMI-2026
    title: >-
      New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional
      Services (study: Resource Management in the Age of AI)
    publisher: Kantata, reporting a Resource Management Institute study it commissioned
    type: survey
    url: >-
      https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraph on readiness for hybrid teams
  - ref: ACCELO-TSIA-2026
    title: >-
      How AI Is Reshaping Resource Utilization and Capacity Management (write-up of a TSIA and Accelo conversation)
    publisher: Accelo
    type: vendor
    url: https://www.accelo.com/blog/ai-era-resource-utilization-capacity-management
    date: '2026-06-03'
    access: full
    locator: >-
      'The Future of Capacity Is Work Allocation'; '200-Hour Engagement' section; TSIA research callout
  - ref: TSIA-RM-2026
    title: Professional Services Resource Management in the PS 2.0 Era (Bo DiMuccio)
    publisher: TSIA
    type: professional-body
    url: https://www.tsia.com/blog/professional-services-resource-management
    date: '2026-05-27'
    access: full
    locator: Maturity Level 3; 'Build the Skills Genome'
  - ref: KANTATA-FORBES-2026
    title: >-
      Professional Services 2026: When AI Becomes A Billable Team Member (Sarah Edwards, Forbes Technology Council post)
    publisher: Kantata (republished from Forbes Councils)
    type: vendor
    url: >-
      https://www.kantata.com/blog/article/professional-services-2026-when-ai-becomes-a-billable-team-member
    date: '2026-01-16'
    access: full
    locator: Prediction 1
  - ref: UNITEAI-KANTATA-2026
    title: Sarah Edwards, Chief Product and Strategy Officer, Kantata - Interview Series
    publisher: Unite.AI
    type: press
    url: >-
      https://www.unite.ai/sarah-edwards-chief-product-and-strategy-officer-kantata-interview-series/
    date: '2026-06-16'
    access: full
    locator: Answer to the first question
  last_reviewed: '2026-10-19'
  notes: >-
    Most evidence is vendor prediction or survey. The 87% and 52.7% figures come from vendor-sponsored or vendor-commissioned
    samples (200 leaders; 44 organizations). No named firm has published capacity data for agents as scheduled resources.
- id: professional-services-staffing-resourcing-09
  title: 'Outcome-aware staffing: using results data on which people and agent combinations work'
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Resource managers are asked to support outcome-oriented delivery without outcome data. Only 7.3% say outcome data is easily
    accessible and routinely used in staffing; 24.6% say only major wins or failures are known informally and 24.6% say outcomes
    are not available to them (KANTATA-RMI-2026).
  solution: >-
    Feed delivery outcomes back into staffing so recommendations reflect which combinations of people or agents produce strong
    results for specific clients or projects. 73.4% of respondents say knowing this would be very or extremely valuable, and
    50.9% say outcome experience already has high or very high influence on staffing recommendations for prospective deals
    (KANTATA-RMI-2026). TSIA calls the historical-delivery input a 'performance signal' (TSIA-RM-2026).
  outcomes:
  - lever: quality
    description: Survey data on the gap; no outcome from using outcome-aware staffing.
    figure: 7.3%
    measures: >-
      Share of 44 surveyed organizations' respondents saying outcome data is easily accessible and routinely used in staffing
      decisions
    provenance: vendor-published
    source_ref: KANTATA-RMI-2026
  prerequisites:
  - Outcome data captured at project close and linked to team composition (KANTATA-RMI-2026).
  - Integrated PSA, CRM and HR data (TSIA-RM-2026).
  risks_and_guardrails:
  - >-
    One in two respondents is unsure whether the organization will adopt outcome-based pricing, so the business case is not
    settled (KANTATA-RMI-2026).
  - >-
    Small, vendor-commissioned sample of 44 organizations across several industries (KANTATA-RMI-2026).
  human_checkpoints:
  - Not described.
  role_evolution: >-
    If outcome pricing spreads, respondents expect resource management to move from filling hours to maximizing delivery success
    and take on more responsibility for team composition and delivery risk (KANTATA-RMI-2026).
  evidence_grade: C
  sources:
  - ref: KANTATA-RMI-2026
    title: >-
      New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional
      Services (study: Resource Management in the Age of AI)
    publisher: Kantata, reporting a Resource Management Institute study it commissioned
    type: survey
    url: >-
      https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraphs on outcome data and on strategic role
  - ref: TSIA-RM-2026
    title: Professional Services Resource Management in the PS 2.0 Era (Bo DiMuccio)
    publisher: TSIA
    type: professional-body
    url: https://www.tsia.com/blog/professional-services-resource-management
    date: '2026-05-27'
    access: full
    locator: '''Create a Unified Resource Intelligence Layer'''
  last_reviewed: '2026-10-19'
  notes: >-
    Percentages are the release's. The denominator for each is the study's respondents (professionals from 44 organizations);
    the release does not give respondent count. Landscape file listed the 7.3% as 'resource managers'; the release describes
    executives, resource managers, RMO leaders, project managers and delivery leaders.
- id: professional-services-staffing-resourcing-10
  title: >-
    Law-firm resourcing platform replaces partner-led phone-round allocation (skills matrix, opportunities board, forecasting)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Work was allocated by partners calling around. Womble Bond Dickinson's resource manager says a lawyer might agree to work
    and then lack capacity when a deadline moved, so the partner restarted the process (BIGHAND-WBD-2026). At DLA Piper, associates
    working closely with particular partners could be more visible for new matters (BIGHAND-DLA-2026). BigHand's survey figures:
    43% of resourcing decisions are lawyer-led (BIGHAND-DLAPR-2026), 37% of firms say partners resource on personal preference
    and 40% have only partial data on work allocated (BIGHAND-DLA-2026).
  solution: >-
    Firms use a central skills and sectors matrix to find lawyers with relevant experience, an opportunities board where practice
    groups post open requests so associates can volunteer, and forecasting tools to compare workloads and anticipate demand
    (BIGHAND-DLA-2026; BIGHAND-WBD-2026). Dedicated resource managers run the process (BIGHAND-WBD-2026).
  outcomes:
  - lever: speed
    description: >-
      DLA Piper reports time saved finding resources at half-year end across its UK and Australian offices.
    figure: 600+ hours (about GBP 673,000 in stated value)
    measures: >-
      Hours saved on finding resources at half-year end, as reported by DLA Piper through BigHand; basis of the GBP value
      is not stated
    provenance: vendor-published
    source_ref: BIGHAND-DLAPR-2026
  - lever: capacity
    description: >-
      Womble Bond Dickinson reports a utilization increase over two years since adopting the platform.
    figure: 10%
    measures: >-
      Increase in utilization over two years since implementation; baseline and definition not given in the case study
    provenance: vendor-published
    source_ref: BIGHAND-WBD-2026
  - lever: experience
    description: Womble Bond Dickinson reports higher staff retention within one practice group.
    figure: 33.3%
    measures: >-
      Increase in staff retention in data captured within a practice group using the platform; counts not given
    provenance: vendor-published
    source_ref: BIGHAND-WBD-2026
  prerequisites:
  - >-
    Lawyers forecast their own workload weekly; WBD tells lawyers the forecast need not be perfect, it is a starting point
    for conversation (BIGHAND-WBD-2026).
  - >-
    Dedicated resource managers and buy-in from practice groups; WBD configures the system differently for different teams
    (BIGHAND-WBD-2026).
  risks_and_guardrails:
  - >-
    DLA Piper's resource manager says you still need people to understand the nuance of allocation and development (BIGHAND-DLA-2026).
  - >-
    Both outcome sets are published by the vendor in case studies, with no independent measurement (BIGHAND-DLA-2026; BIGHAND-WBD-2026).
  human_checkpoints:
  - >-
    Resource managers hold a strategic conversation with requesters on the opportunities board to ensure fair distribution
    (BIGHAND-WBD-2026).
  role_evolution: >-
    Resourcing professionals become strategic partners balancing wellbeing and workforce planning (BIGHAND-DLA-2026). Associates
    can volunteer for matters they would not have seen under a partner-led model (BIGHAND-WBD-2026).
  evidence_grade: B
  sources:
  - ref: BIGHAND-DLA-2026
    title: >-
      A Global Firm Needs a Global View: DLA Piper Scales Legal Resourcing Excellence with BigHand Resource Management (case
      study)
    publisher: BigHand
    type: vendor
    url: >-
      https://www.bighand.com/en-us/resources/case-studies/dla-piper-bighand-resource-management/
    date: '2026-06-17'
    access: full
    locator: '''The Challenge: Mapping the Wild West''; ''The Solution''; ''Success by the Numbers'''
  - ref: BIGHAND-DLAPR-2026
    title: >-
      DLA Piper Reports More Than 600 Hours Saved at Half-Year End with BigHand Resource Management (press release)
    publisher: BigHand
    type: vendor
    url: >-
      https://www.bighand.com/en-us/resources/news/dla-piper-bighand-resource-management-press-release/
    date: '2026-06-18'
    access: full
    locator: Paragraphs 1-3 (figures and survey findings)
  - ref: BIGHAND-WBD-2026
    title: >-
      Womble Bond Dickinson Improves Utilization & Retention with BigHand Resource Management (case study)
    publisher: BigHand
    type: vendor
    url: >-
      https://www.bighand.com/en-us/resources/case-studies/womble-bond-dickinson-bighand-resource-management/
    date: '2026-03-16'
    access: full
    locator: '''Success by the Numbers''; ''The Challenge''; ''The Solution'''
  - ref: BIGHAND-AI-2026
    title: Why Strategic Resource Management is Essential for AI in the Practice of Law (Alex Tring)
    publisher: BigHand
    type: vendor
    url: https://www.bighand.com/en-us/resources/blog/resource-management-and-ai-in-law-practice/
    date: '2026-03-19'
    access: full
    locator: Section 'The Role of Resource Management in the AI Equation'
  last_reviewed: '2026-10-19'
  notes: >-
    These sources do not claim AI is used in the allocation. The entry is included because practitioners and the vendor treat
    this data layer as the foundation for AI-era workforce planning (BIGHAND-AI-2026), and because it is the only named, figured
    law-firm resourcing deployment found. The grade is capped at B because the process is the module's but the technology
    is not AI and all figures are vendor-published. The 33.3% retention figure covers one practice group and is not a firm-wide
    measure.
- id: professional-services-staffing-resourcing-11
  title: AI resourcing agent added to a law-firm resource management product (early preview)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Law firms hold resource data but lack decision-time intelligence; the vendor's CEO says AI amplifies blind spots when
    firms do not understand their work, people and financial performance (BIGHAND-CONF-2026).
  solution: >-
    At its June 2026 conference BigHand showed next-generation dashboards, advanced scheduling and an early preview of an
    AI resourcing agent in its Resource Management product (BIGHAND-CONF-2026).
  outcomes:
  - lever: speed
    description: No outcome; early preview only.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: BIGHAND-CONF-2026
  prerequisites:
  - >-
    A populated resourcing data set (skills, capacity, demand), which is what BigHand's customers describe building first
    (BIGHAND-WBD-2026).
  risks_and_guardrails:
  - No limits or controls for the agent were described in the release (BIGHAND-CONF-2026).
  human_checkpoints:
  - Not described.
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: BIGHAND-CONF-2026
    title: >-
      BigHand Conference Signals a New Priority for Law Firms: Intelligence Before the Point of Decision (post-event release,
      19th BigHand Conference, London)
    publisher: BigHand
    type: conference
    url: >-
      https://www.bighand.com/en-us/resources/news/bighand-conference-2026-post-event-press-release/
    date: '2026-06-05'
    access: full
    locator: Highlights list ('early preview of its AI resourcing agent'); CEO quote
  - ref: BIGHAND-WBD-2026
    title: >-
      Womble Bond Dickinson Improves Utilization & Retention with BigHand Resource Management (case study)
    publisher: BigHand
    type: vendor
    url: >-
      https://www.bighand.com/en-us/resources/case-studies/womble-bond-dickinson-bighand-resource-management/
    date: '2026-03-16'
    access: full
    locator: '''The Solution'' section'
  last_reviewed: '2026-10-19'
  notes: >-
    The release says the conference was 'yesterday' and is dated 2026-06-05. Announced only; the agent's behavior is not described.
- id: professional-services-staffing-resourcing-12
  title: >-
    In-house decision support for client engagement staffing with skills-development flags (Reed Smith Smart Resourcing)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    The firm wanted the right lawyers allocated to the right work at the right time, with insight into client, business and
    personnel situations (REEDSMITH-SMARTRES-2023).
  solution: >-
    Smart Resourcing uses processes and AI toolsets for decision support on staffing client engagements, with in-house technology
    to allocate and track work requests, identify skills-development areas and calculate diversity, equity and inclusion metrics.
    Lawyers can check whether their skills are underused (REEDSMITH-SMARTRES-2023).
  outcomes:
  - lever: quality
    description: Qualitative claim of better outcomes for clients, business and personnel; no figures.
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: REEDSMITH-SMARTRES-2023
  prerequisites:
  - >-
    Close work between IT, practice and legal support groups, in the global director of Smart Resourcing's description (REEDSMITH-SMARTRES-2023).
  risks_and_guardrails:
  - No guardrails are described in the announcement (REEDSMITH-SMARTRES-2023).
  human_checkpoints:
  - >-
    The tool is described as decision support, so staffing decisions stay with people (REEDSMITH-SMARTRES-2023).
  role_evolution: The firm created a global director role for Smart Resourcing (REEDSMITH-SMARTRES-2023).
  evidence_grade: B
  sources:
  - ref: REEDSMITH-SMARTRES-2023
    title: Reed Smith Smart Resourcing team selected to CIO 100
    publisher: Reed Smith
    type: firm
    url: https://www.reedsmith.com/news/reed-smith-smart-resourcing-team-selected-to-cio-100/
    date: '2023-03-27'
    access: full
    locator: Paragraphs 1-4
  last_reviewed: '2026-10-19'
  notes: >-
    Outside the 12 to 18 month window: the CIO 100 announcement is dated 2023-03-27 (page metadata shows a 2026-07-16 modification).
    Current status in 2026 was not confirmed. Included as the only named law-firm in-house staffing decision-support tool
    found. Predates the generative AI agent wave.
- id: professional-services-staffing-resourcing-13
  title: Early-warning workload forecasting for accounting-firm busy seasons
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Capacity planning in accounting firms is 'usually too late': signals about open jobs, slow client documents and deadlines
    sit in different systems (ENTERPRISEDNA-2026). A sponsored practitioner article says firms adjust staffing and tools after
    the core team is already stretched (CPAPA-SAAH-2026).
  solution: >-
    A vendor describes AI that forecasts workload by client, deadline, service line, staff availability and job stage so a
    manager can move work early (ENTERPRISEDNA-2026). The CPA Practice Advisor piece recommends an early capacity analysis,
    contract talent as a planned component, and AI for routine work such as extracting data and tracking missing information
    (CPAPA-SAAH-2026).
  outcomes:
  - lever: capacity
    description: >-
      No outcome measured. The vendor estimates yearly capacity leakage for firms of USD 1M to 25M revenue, with no method
      given.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: ENTERPRISEDNA-2026
  prerequisites:
  - >-
    Job status, task history, document receipt and due dates available to the forecast (ENTERPRISEDNA-2026).
  risks_and_guardrails:
  - >-
    The source is a vendor how-to and a sponsored article, not a deployment report (ENTERPRISEDNA-2026; CPAPA-SAAH-2026).
  human_checkpoints:
  - >-
    The vendor says the tool does not replace the practice manager or team lead (ENTERPRISEDNA-2026).
  role_evolution: >-
    Partners and senior managers jumping in to clear work that less-seasoned staff could do is named as a sign of a stretched
    staffing model (CPAPA-SAAH-2026).
  evidence_grade: C
  sources:
  - ref: ENTERPRISEDNA-2026
    title: Best AI Software for Accounting Capacity Planning
    publisher: Enterprise DNA
    type: vendor
    url: https://enterprisedna.co/resources/blog/accounting-ai-capacity-planning/
    date: '2026-08-30'
    access: full
    locator: Opening sections and 'What capacity planning needs to forecast'
  - ref: CPAPA-SAAH-2026
    title: >-
      Avoiding 'Too Little, Too Late': How to Give Core Teams at CPA Firms Ample Support This Tax Season (sponsored content,
      Steve Saah)
    publisher: CPA Practice Advisor
    type: press
    url: >-
      https://www.cpapracticeadvisor.com/2026/01/27/avoiding-too-little-too-late-how-to-give-core-teams-at-cpa-firms-ample-support-this-tax-season/176902/
    date: '2026-01-27'
    access: full
    locator: Steps 1, 3 and 4
  last_reviewed: '2026-10-19'
  notes: >-
    Vendor claim only. Search-only snippets also mention a CPA Trendlines Busy Season Barometer; the pages opened did not
    give a usable AI-and-staffing figure, so none is used. Tax and audit technical work is out of scope.
- id: professional-services-staffing-resourcing-14
  title: Flexible experienced talent used for overflow work and for AI-tool training and review
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Associates under billable pressure choose client work over AI training and innovation work even when offered credit, and
    knowledge management teams lack subject-matter experts to train tools, review output and build use cases (GEEK-LATITUDE-2026).
    The hosts and guests also cite inconsistent demand and hesitation around layoffs, which in law firms often signal weakness
    (GEEK-LATITUDE-2026).
  solution: >-
    Firms bring in experienced attorneys on engagement terms to cover overflow, leave and projects, and to help train internal
    AI tools and review AI-generated work. Latitude's Alex Su calls this 'outsourced leverage' for the middle layer of legal
    work (GEEK-LATITUDE-2026).
  outcomes:
  - lever: capacity
    description: >-
      Provider says one law firm has dozens of its attorneys working for one rainmaker on high-volume work; no firm named
      and no metrics.
    figure: dozens of attorneys (one firm)
    measures: Provider's statement in the podcast; not independently confirmed
    provenance: vendor-published
    source_ref: GEEK-LATITUDE-2026
  prerequisites:
  - Remote and distributed working accepted by the firm (GEEK-LATITUDE-2026).
  risks_and_guardrails:
  - The speakers are a staffing provider with a commercial interest (GEEK-LATITUDE-2026).
  - >-
    Practitioners disagree on whether AI will cut or raise associate demand while firms still recruit first-year students
    early (GEEK-LATITUDE-2026; BLOOMBERGLAW-BAKER-2026).
  human_checkpoints:
  - Flexible lawyers review AI-generated work and do quality control (GEEK-LATITUDE-2026).
  role_evolution: >-
    Su says premium partner rates are unlikely to fall because of AI; the pressure lands on how firms structure the work beneath
    them (GEEK-LATITUDE-2026).
  evidence_grade: C
  sources:
  - ref: GEEK-LATITUDE-2026
    title: >-
      Alex Su and Andy Chagui on Flexible Legal Talent, AI Pressure, and the Future of Law Firm Leverage (The Geek in Review
      podcast, with transcript)
    publisher: Legal Tech Monitor / The Geek in Review
    type: podcast
    url: >-
      https://www.legaltechmonitor.com/2026/05/alex-su-and-andy-chagui-on-flexible-legal-talent-ai-pressure-and-the-future-of-law-firm-leverage/
    date: '2026-05-18'
    access: full
    locator: Episode summary and transcript passages on AI, associate credit and 'outsourced leverage'
  - ref: CPAPA-SAAH-2026
    title: >-
      Avoiding 'Too Little, Too Late': How to Give Core Teams at CPA Firms Ample Support This Tax Season (sponsored content,
      Steve Saah)
    publisher: CPA Practice Advisor
    type: press
    url: >-
      https://www.cpapracticeadvisor.com/2026/01/27/avoiding-too-little-too-late-how-to-give-core-teams-at-cpa-firms-ample-support-this-tax-season/176902/
    date: '2026-01-27'
    access: full
    locator: Step 3 on contract talent
  - ref: BLOOMBERGLAW-BAKER-2026
    title: Baker Botts Leader Says AI Threatens Rivals' Associates, Not His
    publisher: Bloomberg Law
    type: press
    url: >-
      https://news.bloomberglaw.com/esg/big-law-leader-says-ai-threatens-rivals-associates-not-his
    date: '2026-06-29'
    access: full
    locator: Opening paragraphs on associate hiring
  last_reviewed: '2026-10-19'
  notes: >-
    Maturity is set to emerging because the AI-support use is described only by the provider, with no named client. Contract
    talent as a busy-season lever is also recommended in the accounting piece (CPAPA-SAAH-2026). A related in-house note:
    CLOC's 2025 data says alternative legal service providers are expanding into legal staffing (CLOC-SOTI-2025).
- id: professional-services-staffing-resourcing-15
  title: 'Idea: track realized workload after AI adoption so freed capacity is not silently refilled'
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    A Thomson Reuters Institute columnist, citing a Berkeley study at a 200-person technology company, argues AI intensifies
    work: people take on broader tasks, extend hours and multitask, so capacity freed by AI gets refilled (TRI-LAWPROF-2026).
  solution: >-
    Idea: audit whether associate hours actually fell after AI adoption, and build governance that accounts for how people
    behave with the tools (TRI-LAWPROF-2026). Resourcing and timesheet data would be the natural place to see it; the source
    does not name such a tool.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a
    provenance: independent
    source_ref: TRI-LAWPROF-2026
  prerequisites:
  - Hours and allocation data from before and after AI adoption (TRI-LAWPROF-2026).
  risks_and_guardrails:
  - >-
    The cited study covers one technology company, not a professional services firm; the columnist extends it to law by analogy
    (TRI-LAWPROF-2026).
  human_checkpoints:
  - >-
    Firm leaders review whether reclaimed time went to rest, development or more work (TRI-LAWPROF-2026).
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: TRI-LAWPROF-2026
    title: 'The AI Law Professor: When AI makes lawyers work more, not less (Tom Martin)'
    publisher: Thomson Reuters Institute
    type: press
    url: >-
      https://www.thomsonreuters.com/en/institute/articles/ai-law-professor-ai-makes-lawyers-work-more-not-less
    date: '2026-03-03'
    access: full
    locator: Sections 'Three forms of intensification' and 'From productivity to purposeful practice'
  last_reviewed: '2026-10-19'
  notes: >-
    Idea. The source is a column that cites an academic study (the 'independent' provenance label is a placeholder for the
    cited Berkeley study, which was not opened; only the column was read). No professional services firm measurement was found.
```

## 3. Module notes

### Processes and key steps (work types)

1. **Capture demand**: pipeline, signed statements of work, renewals, leave and expected churn (`data-reporting`). TSIA calls pipeline the "demand signal" (TSIA-RM-2026).
2. **Maintain the supply picture**: availability, cost, skills, certifications, recency of use, and partners and subcontractors (`data-reporting`). TSIA proposes extending the same record to AI tools (TSIA-RM-2026).
3. **Forecast and plan capacity**: decide whether to hire, use contract talent, subcontract, or reassign (`coordination-scheduling`). Accounting commentary stresses doing the capacity analysis before busy season (CPAPA-SAAH-2026).
4. **Match and assign**: shortlist candidates, check conflicts and availability, agree with the project lead and the person (`coordination-scheduling`; senior and partner staffing is `expert-judgment`).
5. **Rebalance**: cover leave, absorb moved deadlines, replace people on work in flight (`coordination-scheduling`).
6. **Monitor utilization and bench**: overbooking, bench time, margin effect of an assignment (`data-reporting`).
7. **Align assignments to development and retention**: opportunities boards and development goals (BIGHAND-WBD-2026).
8. **Emerging step: orchestrate people and agents** as one capacity pool (TSIA-RM-2026; KANTATA-FORBES-2026).

### Common pain points

- Partner-led, relationship-driven allocation: 43% of law-firm resourcing decisions are lawyer-led and 37% of firms say partners resource on personal preference, per BigHand's report (BIGHAND-DLAPR-2026; BIGHAND-DLA-2026).
- Partial data: 45% of firms have only partial visibility of associate skill sets and 40% only partial data on work allocated (BIGHAND-DLA-2026).
- Stale, self-reported skills and reactive staffing (TSIA-RM-2026).
- Fragmented data. Barriers named in the Kantata and Resource Management Institute study: limited understanding of where AI applies (49%), poor or fragmented data (47%), tools not ready for AI-driven staffing and hybrid teams (41%) (KANTATA-RMI-2026).
- Capacity limits work won: more than 66% of surveyed organizations report turning down work because of resourcing constraints, and the share citing skill availability as a barrier rose to 68% from 45% (KANTATA-STATE-2026).
- Resource management is seen as operational: 72% say so in their organization (KANTATA-RMI-2026).
- Busy-season staffing starts late, so core teams are stretched before help arrives (CPAPA-SAAH-2026).

### Metrics and benchmarks (provenance stated)

- Utilization: TSIA's DiMuccio said most firms run between 55% and 65% (ACCELO-TSIA-2026, spoken remark). Deltek's A&E study reports utilization "just under 60%" and operating profit of 16.7%, from 896 firms (DELTEK-CLARITY-2026, vendor-published survey). A Deltek article, quoting an SPI report not opened here, gives 68.9% utilization, down from 73.2% a few years earlier, and revenue per consultant of $199K versus $207K (DELTEK-RM-2025, secondary).
- A&E staffing: staff growth of 1.2% against forecast revenue growth of 9.5%, turnover above 13%, AI adoption up from 53% to 70%, and 38% reporting measurable positive impact (DELTEK-CLARITY-2026).
- Readiness: 39% traditional staffing mode, 30% experimenting, 31% beyond experimentation; 52.7% not equipped for hybrid teams, 28.4% slightly equipped, 4% well equipped; outcome data easily accessible and routinely used by 7.3%; 73.4% say knowing which combinations of people or agents produce outcomes would be very or extremely valuable (KANTATA-RMI-2026, vendor-commissioned, 44 organizations).
- Agents in the workforce: 87% plan to use AI agents; 89% say future revenue growth depends more on scaling AI than headcount; 90% say systems will need to attribute work, costs and value across people and agents; 54% report at least 10% of projects missing budget goals; 12% fully trust system data (down from 24%) (KANTATA-STATE-2026, Censuswide survey of 200 leaders, vendor-sponsored).
- AI in scheduling: fewer than 2% use AI to support resource scheduling and allocation, against 97% tracking utilization (TSIA research via ACCELO-TSIA-2026).
- Legal talent and profit: talent capacity is the leading constraint on profitability for 35% of respondents to the 2026 Blickstein law firm COO survey, with lack of strategic consensus second at 15%; 9% expect administrative headcount to rise and 28% to fall (WESTERNALLIANCE-COO-2026). BigHand reports associate departures rose from 9% to 16% between 2024 and 2025 (BIGHAND-DLAPR-2026).
- In-house (CLOC 2025 data, 186 organizations, older than the 18-month window): 83% of legal departments expect demand to increase, 63% name workload and resource bandwidth as the top challenge, and alternative legal service providers are expanding into legal staffing (CLOC-SOTI-2025).
- Named-organization figures (vendor-published): DLA Piper 600+ hours saved finding resources at half-year end (BIGHAND-DLAPR-2026); Womble Bond Dickinson 10% utilization increase over two years (BIGHAND-WBD-2026).
- Rocketlane cites SPI 2026 figures (75.0% billable utilization for high performers against 64.9% for others; AI-wide users 81.5% on-time delivery and 17.9% EBITDA against 70.8% and 6.0%) (ROCKETLANE-2026). These are secondhand vendor citations of a paywalled report and are listed here only as claims to check.
- **Quality evidence: none found.** No error rate, override rate, recommendation acceptance rate, parallel run, or independent evaluation of AI staffing tools was published in the sources read.

### Guardrails and regulatory points

- EU AI Act: high-risk use cases include AI tools for employment and management of workers; the Commission page says rules for such systems apply from 2 December 2027 under the AI Omnibus (EC-AIACT-2026). Whether a staffing recommender is in scope depends on its use; the page's wording is broad and this note does not decide the question.
- Data trust is the practical guardrail: only 12% of leaders fully trust system data (KANTATA-STATE-2026); TSIA says AI "amplifies" broken processes (TSIA-RM-2026).
- Fair allocation: the problem practitioners describe is human favoritism and visibility (BIGHAND-DLA-2026); Reed Smith's tool calculates diversity, equity and inclusion metrics for staffing (REEDSMITH-SMARTRES-2023). No source describes bias testing of an AI staffing recommender.
- Hybrid accountability: Edwards poses unanswered questions on scheduling and measuring agents next to consultants (KANTATA-FORBES-2026).
- Workload effects: the TRI column recommends auditing whether AI actually reduced hours (TRI-LAWPROF-2026).

### Frontier signals (dated)

- 2026-01-08: Kantata survey says 87% plan to use AI agents as part of their workforce (KANTATA-STATE-2026). 2026-01-16: Edwards predicts agents will be planned, allocated, measured and priced like capacity (KANTATA-FORBES-2026).
- 2026-04-09: Resource Management Institute study released; a session, "The End of 'Who's Available?': What Resource Management Will Look Like in 2028", was announced for the Resource Management Global Symposium in Indianapolis on 20 to 22 April 2026 (KANTATA-RMI-2026). The symposium page lists no session content (RMGS-2026).
- 2026-05-01: McKinsey plans to use AI agents to help choose client teams (BLOOMBERGLAW-MCK-2026).
- 2026-05-14 (date from a search-result summary; the page text shows no date) and 2026-05-27: TSIA webinar on closing the utilization gap with AI, and TSIA's maturity model for resource management (TSIA-WEBINAR-2026; TSIA-RM-2026).
- 2026-06-05: BigHand shows an early preview of an AI resourcing agent (BIGHAND-CONF-2026).
- 2026-06-16: Kantata describes its Expertise Agent as a "superagent" spanning projects, resources, financials and systems (KANTATA-SUPERAGENT-2026).
- 2026-07-22: Rocketlane describes a Resource Management Agent "currently in active rollout" (ROCKETLANE-2026).
- 2026-10-05: a Kantata headline announces Agent Studio; the page was not readable (KANTATA-PRESS-2026, search-only).
- Scheduled: a fireside chat with Basware and Kantata, "Congratulations, You Hired an AI Agent! Now Who's Managing Its Margin?", at Technology & Services World in Las Vegas, 2026-10-20 (KANTATA-BASWARE-2026); Kantata Converge, London, 2026-11-17 (KANTATA-CONVERGE-2026). These are announcements, not reports of what was said.
- 2027-12-02: EU high-risk obligations for employment-related AI (EC-AIACT-2026).

### Workforce and role effects

- Resource managers: from filling open roles toward a strategic, data-driven role (TSIA-RM-2026); Kantata's 2026 predictions say resource management in 2026 is less about filling seats and more about optimizing impact (KANTATA-TRENDS-2026); Womble Bond Dickinson recruited dedicated resource managers alongside the platform (BIGHAND-WBD-2026). In the study, 72% still call the function mainly operational (KANTATA-RMI-2026).
- Associates: AI is automating tasks of past junior associates and clients do not want to pay for them, according to TRI; a legal innovation consultant suggests junior rotations through knowledge management and technology functions (TRI-LAWYERDEV-2026). A TR paper says AI may reduce demand for some junior roles and raise it for hybrid tech-legal roles (TR-FOPLAW-2026).
- Associate hiring signals conflict: Baker Botts hired 84 entry-level associates against 86 a year earlier, while Firm Prospects data cited by Bloomberg shows the 100 largest firms hired 4,613 last year, down 22% from 5,917 in 2024 (BLOOMBERGLAW-BAKER-2026). The pyramid debate belongs to talent-learning.
- Administrative staff: roundtable COOs expect fewer billing administrators and more technology, data and AI enablement roles (WESTERNALLIANCE-COO-2026).
- Experienced contract talent is used for overflow and to staff AI training and review work (GEEK-LATITUDE-2026).

### Objections and concerns practitioners raise

- "Fast, mediocre decisions": Kantata's CEO warns that fast AI answers lacking business context are not the best decisions, and that point solutions in silos make staffing worse (KANTATA-SUPERAGENT-2026). This is also a sales argument for the vendor's superagent.
- Agent bloat and silos: Edwards describes agents slow, expensive or inaccurate through overload of tools (UNITEAI-KANTATA-2026).
- AI does not fix bad data: TSIA calls this the "PS 2.0 Transformation Paradox" (TSIA-RM-2026); Accelo's CEO says the same (ACCELO-TSIA-2026).
- Freed capacity gets refilled and may raise burnout (TRI-LAWPROF-2026).
- Associates under billable pressure choose billable work over development and AI-training credit (GEEK-LATITUDE-2026).
- Human nuance: DLA Piper's resource manager says the software helps but the manager supplies context (BIGHAND-DLA-2026).
- Measurement gap: few firms formally measure AI efficiency gains, per COOs at the roundtable (WESTERNALLIANCE-COO-2026).
- Strategic consensus among partners is hard, which slows any allocation redesign (WESTERNALLIANCE-COO-2026).
- Outcome pricing uncertainty: one in two respondents is unsure their organization will adopt it, which limits the case for outcome-aware staffing (KANTATA-RMI-2026).

### Interview probes for an advisor

1. Who decides who goes on which engagement today, how many calls or messages does one assignment take, and where do you find out that a person's skills have changed?
2. If a tool recommended a team, how would you know if the recommendation was good? Do you record when a recommendation is overridden, and what happens to engagements staffed that way?
3. What share of your delivery hours could be done by an agent, and would those agents appear in your capacity plan, your utilization figure or your pricing?
4. When AI saves time on a matter or project, what happens to the freed hours in your allocation data (more work, development time, lower headcount, lower fee)?
5. Which data would you trust to feed a staffing recommender (timesheets, skills profiles, pipeline, past outcomes), and which would you not?

## 4. Routed to other modules

- **delivery-management**: Kantata's description of new team members receiving a full briefing on assignment, timesheet compliance by comparing calendars with scheduled work, and Harvey's Legal Work Orchestration (KANTATA-SUPERAGENT-2026). Rocketlane's Timesheet Policy Agent (ROCKETLANE-2026).
- **billing-collections**: ambient time capture and conversational timekeeping that keep utilization data clean (KANTATA-SUPERAGENT-2026; CERTINIA-VEDA-2026).
- **knowledge-management**: Kantata's "expertise compounding" and knowledge-graph claims (UNITEAI-KANTATA-2026), and Basware's idea of making its best people's judgment available on every project (KANTATA-BASWARE-2026).
- **talent-learning**: associate hiring numbers and the pyramid debate (BLOOMBERGLAW-BAKER-2026; TRI-LAWYERDEV-2026); associates choosing billable work over AI training credit (GEEK-LATITUDE-2026); junior rotations (TRI-LAWYERDEV-2026).
- **scoping-pricing**: outcome-based pricing, fee models and how agents are billed (KANTATA-RMI-2026; UNITEAI-KANTATA-2026; TRI-FOP-2025; TR-FOPLAW-2026).
- **firm-finance**: profitability constraints, technology investment and measurement of AI gains from the COO roundtable (WESTERNALLIANCE-COO-2026).
- **acceptance-risk / delivery-management** (in-house): AI-automated intake triage by in-house legal operations teams (DOCUSIGN-LEGALOPS-2026); allocation of work between in-house and outside counsel (TRI-INTERDEP-2026).
- **client-development**: Kantata's note that RFP buyers now ask how the firm uses AI to reduce cost (UNITEAI-KANTATA-2026).

## 5. Sources

Counts by type are given in the final reply. Sources read for this run but not cited in a use case (for example the Legalweek and ILTACON recaps) are listed because they were checked for staffing content and had none. `search-only` marks pages that could not be read beyond a headline or opening paragraphs.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ACCELO-TSIA-2026 | How AI Is Reshaping Resource Utilization and Capacity Management (write-up of a TSIA and Accelo conversation) | Accelo | vendor | https://www.accelo.com/blog/ai-era-resource-utilization-capacity-management | 2026-06-03 | full |
| BIGHAND-AI-2026 | Why Strategic Resource Management is Essential for AI in the Practice of Law (Alex Tring) | BigHand | vendor | https://www.bighand.com/en-us/resources/blog/resource-management-and-ai-in-law-practice/ | 2026-03-19 | full |
| BIGHAND-CONF-2026 | BigHand Conference Signals a New Priority for Law Firms: Intelligence Before the Point of Decision (post-event release, 19th BigHand Conference, London) | BigHand | conference | https://www.bighand.com/en-us/resources/news/bighand-conference-2026-post-event-press-release/ | 2026-06-05 | full |
| BIGHAND-DLA-2026 | A Global Firm Needs a Global View: DLA Piper Scales Legal Resourcing Excellence with BigHand Resource Management (case study) | BigHand | vendor | https://www.bighand.com/en-us/resources/case-studies/dla-piper-bighand-resource-management/ | 2026-06-17 | full |
| BIGHAND-DLAPR-2026 | DLA Piper Reports More Than 600 Hours Saved at Half-Year End with BigHand Resource Management (press release) | BigHand | vendor | https://www.bighand.com/en-us/resources/news/dla-piper-bighand-resource-management-press-release/ | 2026-06-18 | full |
| BIGHAND-WBD-2026 | Womble Bond Dickinson Improves Utilization & Retention with BigHand Resource Management (case study) | BigHand | vendor | https://www.bighand.com/en-us/resources/case-studies/womble-bond-dickinson-bighand-resource-management/ | 2026-03-16 | full |
| BLOOMBERGLAW-BAKER-2026 | Baker Botts Leader Says AI Threatens Rivals' Associates, Not His | Bloomberg Law | press | https://news.bloomberglaw.com/esg/big-law-leader-says-ai-threatens-rivals-associates-not-his | 2026-06-29 | full |
| BLOOMBERGLAW-MCK-2026 | McKinsey Plans to Use AI Agents to Help Select Client Teams (paywalled; opening paragraphs only) | Bloomberg Law | press | https://news.bloomberglaw.com/financial-accounting/mckinsey-plans-to-use-ai-agents-to-help-select-client-teams | 2026-05-01 | search-only |
| CERTINIA-VEDA-2026 | Certinia AI / Veda agents for professional services (product page) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 | full |
| CLOC-SOTI-2025 | 2025 CLOC State of the Industry Report: 83% of Legal Departments Face Rising Demand and AI Adoption Nearly Doubles | CLOC | professional-body | https://cloc.org/newsdesk/2025-state-of-the-industry-report | 2025-02-12 | full |
| CPAPA-SAAH-2026 | Avoiding 'Too Little, Too Late': How to Give Core Teams at CPA Firms Ample Support This Tax Season (sponsored content, Steve Saah) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/01/27/avoiding-too-little-too-late-how-to-give-core-teams-at-cpa-firms-ample-support-this-tax-season/176902/ | 2026-01-27 | full |
| DELTEK-CLARITY-2026 | The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures for Project-Based Businesses | Deltek | survey | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| DELTEK-RM-2025 | Transforming Professional Services Through Effective Resource Management (Best Practices for Resource Management in Professional Services) | Deltek | vendor | https://www.deltek.com/resources/articles/best-practices-for-resource-management-in-professional-services/ | 2025-12-04 | full |
| DOCUSIGN-LEGALOPS-2026 | How Legal Ops Teams Are Navigating the AI Transformation (in-house legal operations Q&A on CLOC 2026) | Docusign | vendor | https://www.docusign.com/blog/how-legal-ops-teams-are-navigating-the-ai-transformation | 2026-07-17 | full |
| EC-AIACT-2026 | AI Act: regulatory framework for AI (living page, read 2026-10-19) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10 | full |
| EDISCOVERYTODAY-ILTACON-2026 | My Five ILTACON 2026 Takeaways (read for staffing content: none found) | eDiscovery Today | conference | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 | full |
| ENTERPRISEDNA-2026 | Best AI Software for Accounting Capacity Planning | Enterprise DNA | vendor | https://enterprisedna.co/resources/blog/accounting-ai-capacity-planning/ | 2026-08-30 | full |
| GEEK-LATITUDE-2026 | Alex Su and Andy Chagui on Flexible Legal Talent, AI Pressure, and the Future of Law Firm Leverage (The Geek in Review podcast, with transcript) | Legal Tech Monitor / The Geek in Review | podcast | https://www.legaltechmonitor.com/2026/05/alex-su-and-andy-chagui-on-flexible-legal-talent-ai-pressure-and-the-future-of-law-firm-leverage/ | 2026-05-18 | full |
| HBS-D3-PWC-2022 | Who Me? For that Project? How AI is Changing the Consulting World (student post, HBS Digital Initiative) | Harvard Business School Digital Initiative | community | https://d3.harvard.edu/platform-digit/submission/who-me-for-that-project-how-ai-is-changing-the-consulting-world/index.html | 2022-11-30 | full |
| KANTATA-BASWARE-2026 | Kantata takes Basware from AI Experimentation to Results | Kantata press release | vendor | https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results | 2026-10-13 | full |
| KANTATA-CONVERGE-2026 | Kantata Converge: Where AI Meets Expertise (announcement of the 17 Nov 2026 London conference) | Kantata | conference | https://www.kantata.com/blog/article/kantata-converge-where-ai-meets-expertise | 2026-10-08 | full |
| KANTATA-FORBES-2026 | Professional Services 2026: When AI Becomes A Billable Team Member (Sarah Edwards, Forbes Technology Council post) | Kantata (republished from Forbes Councils) | vendor | https://www.kantata.com/blog/article/professional-services-2026-when-ai-becomes-a-billable-team-member | 2026-01-16 | full |
| KANTATA-PRESS-2026 | Kantata Media & Press listing (headline list only; individual pages for Agent Studio and 'Beyond AI Staffing' returned 404 or were blocked) | Kantata | vendor | https://www.kantata.com/press | 2026-10-19 | search-only |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services (study: Resource Management in the Age of AI) | Kantata, reporting a Resource Management Institute study it commissioned | survey | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| KANTATA-STATE-2026 | 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce (State of the Professional Services Industry survey, Censuswide, 200 leaders) | Kantata press release via CFO Dive | survey | https://www.cfodive.com/press-release/20260108-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-thei/ | 2026-01-08 | full |
| KANTATA-SUPERAGENT-2026 | More Agents Won't Fix Unpredictable Projects: Why We Built a Superagent Instead (write-up of a Professional Services Pursuit podcast episode) | Kantata | vendor | https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead | 2026-06-16 | full |
| KANTATA-TRENDS-2026 | 7 Trends & Predictions for Professional Services in 2026 | Kantata | vendor | https://www.kantata.com/blog/article/looking-ahead-7-trends-predictions-for-professional-services-in-2026 | 2026-01-20 | full |
| KARBON-ENGAGE-2026 | AICPA & CIMA ENGAGE 2026 session preview (includes 'The distributed firm: managing remote, hybrid, and offshore teams') | Karbon | conference | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | 2026-06 | full |
| REEDSMITH-SMARTRES-2023 | Reed Smith Smart Resourcing team selected to CIO 100 | Reed Smith | firm | https://www.reedsmith.com/news/reed-smith-smart-resourcing-team-selected-to-cio-100/ | 2023-03-27 | full |
| RMGS-2026 | Resource Management Global Symposium 2026 (RMGS) attendee page, Resource Management Institute | Resource Management Institute | conference | https://s2.goeshow.com/rtm/rmgs/2026/who_attends.cfm | 2026-04 | full |
| ROCKETLANE-2026 | AI for PS resource allocation: the 2026 guide for professional services leaders | Rocketlane | vendor | https://rocketlane.com/blogs/ai-for-ps-resource-allocation | 2026-07-22 | full |
| TR-FOPLAW-2026 | What the '2026 Future of Professionals Report' says law firm leaders should be doing now | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-law-firms-paper-2026 | 2026-07-21 | full |
| TRI-FOP-2025 | 'Future of Professionals' report analysis: Why AI will flip law firm economics | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en-us/posts/legal/future-of-professionals-report-analysis-law-firm-economics/ | 2025-10-16 | full |
| TRI-INTERDEP-2026 | Interdependent by design: The AI conversation law firms and legal departments need to be having now | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/needed-ai-conversation | 2026-06-11 | full |
| TRI-LAWPROF-2026 | The AI Law Professor: When AI makes lawyers work more, not less (Tom Martin) | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/ai-law-professor-ai-makes-lawyers-work-more-not-less | 2026-03-03 | full |
| TRI-LAWYERDEV-2026 | Rethinking lawyer development in future AI-enabled law firms | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en-us/posts/legal/lawyer-development-ai-enabled-law-firms/ | 2026-04-16 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: firms and clients confront the AI value divide (read for staffing content: none found) | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TSIA-RM-2026 | Professional Services Resource Management in the PS 2.0 Era (Bo DiMuccio) | TSIA | professional-body | https://www.tsia.com/blog/professional-services-resource-management | 2026-05-27 | full |
| TSIA-WEBINAR-2026 | TECH on Deck: Closing the Utilization Gap With AI (webinar sponsored by Accelo; 14 May 2026) | TSIA | conference | https://www.tsia.com/webinars/tech-on-deck-closing-the-utilization-gap-with-ai | 2026-05-14 | full |
| UNITEAI-KANTATA-2026 | Sarah Edwards, Chief Product and Strategy Officer, Kantata - Interview Series | Unite.AI | press | https://www.unite.ai/sarah-edwards-chief-product-and-strategy-officer-kantata-interview-series/ | 2026-06-16 | full |
| WESTERNALLIANCE-COO-2026 | AI Is Driving Change, but the Hard Decisions Are Still Human (law firm COO roundtable on the 2026 Blickstein Group Law Firm COO Survey, Chatham House Rule) | Western Alliance Bank | community | https://www.westernalliancebancorporation.com/insights/ai-driving-change-hard-decisions-are-still-human | 2026-07-31 | full |

Also read and not listed in the table because they were out of window or lacked usable content: Constellation Research's 2024 "pyramid to diamond" post, a Kantata podcast transcript from about 2021, and a Monetizely post on the talent pyramid whose statistics could not be traced to a source.

## 6. Gaps

- **No quality evidence.** No error rates, override rates, parallel runs, or independent evaluations of AI staffing tools were found. All outcome figures in this file are vendor-published or self-reported.
- **Conference sessions on staffing were not found at the large legal events.** The Legalweek (TRI) and ILTACON (eDiscovery Today, Artificial Lawyer day-two) recaps contain none; ILTACON and CLOC session catalogues are JavaScript-rendered or members-only. The RMGS 2026 agenda was not published on the pages reachable, and the Kantata TSW and Converge items are announcements. AICPA ENGAGE 2026 shows one relevant session title (offshore and distributed team workflow management), via Karbon's preview, with no content (KARBON-ENGAGE-2026).
- **Blocked or unreadable:** ILTA Spring 2026 Peer to Peer pages (search summaries only, now 404), Bloomberg Law's McKinsey article beyond the opening, ERP Today's Kantata Expertise Agent piece (Cloudflare), Kantata's "Beyond AI Staffing" and Agent Studio posts (404), Legal Geek 2026 agenda (403), PMI pages (403), Reddit (403), Workday podcast on AI resource management (search result, dated 2024, not opened).
- **Not reached:** the BigHand "Navigating the Million Dollar Problem" and Legal Talent and Resourcing reports (figures taken from case studies and a press release); SPI 2026 full report and TSIA benchmark data (paywalled; SPI figures appear only through vendor citations); Kantata's full State of the Professional Services Industry report; CLOC 2026 State of the Industry; TRI COO/CFO Forum recaps.
- **Primary Big Four and consulting-firm material on AI staffing** (Deloitte, EY, KPMG, PwC, Accenture, BCG, Bain): none found. McKinsey's plan rests on a paywalled Bloomberg opening. A PwC AI staffing-model proposal appears only in a 2022 student post, which is not independent confirmation (HBS-D3-PWC-2022).
- **Community discussion:** the only practitioner-forum item is a Chatham House roundtable summary (WESTERNALLIANCE-COO-2026); resource-manager communities and forums were not reachable.
- **Customer evidence for agent products** (Certinia Veda, Rocketlane Nitro, Kantata Expertise Agent) is limited to one-line testimonials and unnamed customers.
- **Non-legal in-house shared services** (finance, HR, global business services) and engineering or architecture staffing beyond Deltek's A&E study were not covered.
- **Landscape corrections:** the Kantata and Resource Management Institute study sampled 44 organizations, not only resource managers, and reports 30% experimenting alongside the 39% and 31% figures (KANTATA-RMI-2026).
