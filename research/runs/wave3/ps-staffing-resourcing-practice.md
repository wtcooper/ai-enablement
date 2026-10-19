# Staffing and resourcing: practice angle (professional services)

Prepared 2026-10-19. Archetype: professional-services. Module: staffing-resourcing. Angle: practice (what firms and in-house teams actually do). Public sources only. Method: curl and a text mirror to open pages, `pdftotext` for the one PDF, and a handful of rationed web searches. Items marked search-only were seen only in search results.

## 1. Summary

- **What exists.** 39 sources are listed, 37 of them opened and read (by type: academic 2, conference 1, firm 1, job-posting 1, press 9, regulator 2, survey 4, vendor 17). Evidence is dominated by vendor material. Almost every figure on staffing outcomes is a vendor claim with no stated method, no sample and no baseline. There is no grade A entry: no named firm publishes a measured staffing result for an AI tool.
- **Named uses are few.** The only named deployment of an AI staffing agent with a press description is Basware's services organisation using a Kantata agent (KANTATA-BASWARE-2026), and it publishes no staffing figure. Deutsche Telekom's Eightfold project-staffing story describes a planned pilot of about 1,000 people (EIGHTFOLD-DT-2025). McKinsey has said it plans to use agents to help pick consultants for client teams (BLOOMBERGLAW-MCKINSEY-2026). No law-firm or in-house legal staffing deployment was found.
- **Product activity is high.** Certinia (Veda: Resourcing, Shortlisting, Work Reallocation agents), Kantata (Expertise Agent, Staffing Optimizer), Deltek (Polaris with Dela), Planview (Agent Resource Management, available from Fall 2026), Rocketlane, Cinode and Wolters Kluwer (CCH Axcess Workflow) all ship or announce staffing recommendations. Recommendations are advisory in every description read.
- **The only independent measurement points to a limit.** In a randomised trial in a Peruvian enforcement agency, replacing manager assignment of cases with an optimisation algorithm lowered on-time completion by about 5 percentage points (IPA-PERU-2026). It is adjacent evidence (a government agency, not a firm) but it is the one test of automated work allocation found, and it favours keeping people in the matching step.
- **The pain is real and measured by benchmarks.** Average billable utilisation fell to 66.4% in 2025, the lowest in SPI's survey history (DELTEK-SPIBENCH-2026). Over 66% of leaders in a Kantata-sponsored survey of 200 say they have turned down work because of resourcing constraints (KANTATA-STATE-2026).
- **Readiness is low.** In the RMI study of 44 organisations, 39% were still in traditional staffing mode, 52.7% were not equipped to manage hybrid human-agent teams, and 7.3% routinely used outcome data in staffing (KANTATA-RMI-2026).
- **Use cases:** 17 candidates. Grades: A: 0, B: 3, C: 13, D: 1.

## 2. Use cases

Ids follow `professional-services-staffing-resourcing-NN`. Dates are ISO. Where a vendor page carries no date, the retrieval date (2026-10-19) is shown and the title says so. In every entry, figures are labelled with what they measure and who published them.

```yaml
- id: professional-services-staffing-resourcing-01
  title: Ranked staff recommendations for open roles inside the services-automation platform
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: 'Resource managers match people to roles from memory, spreadsheets and phone calls. Familiarity and recency
    shape who gets picked, and people with the right skills elsewhere in the firm are overlooked (PROJECTWORKS-2026).
    One RMI figure quoted on a vendor page: 71% of organisations rely on spreadsheets for resource-management processes
    such as skills tracking, forecasting and workload planning (KANTATA-FORECAST-2026).'
  solution: 'An agent or recommender inside the services-automation (PSA) platform reads project, people, skills
    and availability data and proposes ranked candidates, with reasoning, for a resource manager to confirm. Named
    examples: Basware services managers use an agent built on the Kantata Expertise Engine to decide how to staff
    projects as timelines and requirements change (KANTATA-BASWARE-2026); Kantata describes ranked recommendations
    with reasoning (KANTATA-AGENT-2026); Certinia lists Resourcing and Shortlisting agents (CERTINIA-VEDA-2026);
    Deltek describes skills-based matching with Dela in Polaris (DELTEK-POLARIS-2026).'
  outcomes:
  - lever: capacity
    description: Certinia says Veda returns up to 10 hours of capacity per month to resource managers across staffing
      analysis, bench matching and work reallocation. The press report attributes this to its lighthouse customers;
      no customer is named.
    figure: up to 10 hours per month
    measures: Hours of resource-manager capacity returned per month, per Certinia; the source does not say how it
      was measured, for how many users, or against what baseline (the same article also covers bench matching and
      work reallocation, use cases 05 and 06)
    provenance: vendor-published
    source_ref: CPAPA-CERTINIA-2026
  - lever: quality
    description: Kantata states that its customers see a 40% improvement in resource planning accuracy.
    figure: 40%
    measures: Stated on the product page as improvement in resource planning accuracy; the page gives no baseline,
      sample or definition
    provenance: vendor-published
    source_ref: KANTATA-AGENT-2026
  - lever: speed
    description: Deltek states 40% improvement in time-to-hire with skills-based resource matching and real-time
      availability insight, for firms running on the Deltek platform. This is a hiring measure, not a staffing-speed
      measure.
    figure: 40%
    measures: Improvement in time-to-hire, as the Polaris page words it; no baseline or sample given
    provenance: vendor-published
    source_ref: DELTEK-POLARIS-2026
  - lever: speed
    description: 'Basware: no staffing figure published. The release says its services organisation was slow to
      scope and slow to staff and that an agent now helps services managers staff projects.'
    figure: none published for staffing
    measures: n/a
    provenance: vendor-published
    source_ref: KANTATA-BASWARE-2026
  prerequisites:
  - Skills, availability, project budgets and the CRM in one connected system; Projectworks says AI can help little
    if they sit in different places (PROJECTWORKS-2026)
  - 'Usable data: 47% of RMI respondents named poor or fragmented data across skills, outcomes, demand and capacity
    as the biggest gap (KANTATA-RMI-2026)'
  - Basware began with the fundamentals (automating billing) before adding the resource agent (KANTATA-BASWARE-2026)
  risks_and_guardrails:
  - Recommendations are advisory; Projectworks says the best tools today advise and do not change assignments themselves,
    and that client dynamics and personal fit are not captured by any model (PROJECTWORKS-2026)
  - Only 12% of leaders in a Kantata-sponsored survey fully trust their systems data and 89% say they spend significant
    time verifying AI outputs (KANTATA-STATE-2026)
  - An RCT of automated case assignment in a government agency found worse on-time completion than manager assignment
    (see use case 17; IPA-PERU-2026)
  human_checkpoints:
  - Resource manager confirms or overrides each recommendation (KANTATA-AGENT-2026; DIGINOMICA-CERTINIA-2026 quotes
    Certinia saying users stay in control)
  role_evolution: Resource managers move from searching for candidates to choosing among ranked options; RMI reports
    72% of respondents say the function is primarily or solely operational and that respondents want skills intelligence
    and forecasting accuracy to become part of a more strategic role (KANTATA-RMI-2026).
  evidence_grade: B
  sources:
  - ref: KANTATA-BASWARE-2026
    title: Kantata takes Basware from AI experimentation to results (press release)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results
    date: '2026-10-13'
    access: full
    locator: Section "Smarter Resource Management" and the Johnston quote opening the release
  - ref: KANTATA-AGENT-2026
    title: Expertise Agent and Workflows (product page; page carries no publication date, date shown is the retrieval
      date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/ai/expertise-agent-and-workflows
    date: '2026-10-19'
    access: full
    locator: Section "Proactive Resourcing" and the 40% statement
  - ref: CPAPA-CERTINIA-2026
    title: Certinia Unveils Veda, an AI Operations Engine for Professional Services
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/04/15/certinia-unveils-veda-an-ai-operations-engine-for-professional-services/181702/
    date: '2026-04-15'
    access: full
    locator: Paragraph beginning "For resource managers, Veda automates staffing analysis"
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (product page; page carries no publication date,
      date shown is the retrieval date)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Meet the Veda agent team, Plan row (Resourcing Agent, Shortlisting Agent)
  - ref: DELTEK-POLARIS-2026
    title: Deltek Polaris (product page; page carries no publication date, date shown is the retrieval date)
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/en/products/polaris/
    date: '2026-10-19'
    access: full
    locator: Results panel and Intelligent Resource Management section
  - ref: PROJECTWORKS-2026
    title: How AI Is Changing Resource Planning for Consulting Firms
    publisher: Projectworks
    type: vendor
    url: https://www.projectworks.com/blog/how-ai-changes-resource-planning
    date: '2026-06-25'
    access: full
    locator: Sections on matching people to roles and on where AI resource planning is still early
  - ref: KANTATA-FORECAST-2026
    title: Resource Forecasting and Staffing (product page; page carries no publication date, date shown is the
      retrieval date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/solutions/resource-forecasting-and-staffing
    date: '2026-10-19'
    access: full
    locator: Opening statistic on spreadsheet reliance (attributed to RMI Research)
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services (press release on the Resource Management Institute study 'Resource Management in the
      Age of AI')
    publisher: Kantata (study by Resource Management Institute, commissioned by Kantata)
    type: survey
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraphs on barriers (49%, 47%, 41%) and on 72% operational
  - ref: KANTATA-STATE-2026
    title: Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their
      Workforce (press release on the State of the Professional Services Industry report; Censuswide survey of 200
      leaders)
    publisher: Kantata
    type: survey
    url: https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce
    date: '2026-01-08'
    access: full
    locator: Paragraph on data trust (12%, 88%, 89%)
  - ref: DIGINOMICA-CERTINIA-2026
    title: Certinia unveils Veda, its AI engine for Professional Services Automation
    publisher: diginomica
    type: press
    url: https://diginomica.com/certinia-unveils-veda-ai-engine-professional-services-automation
    date: '2026-04-15'
    access: full
    locator: Closing "My take" section and Malhotra quote on human accountability
  - ref: KELLOGG-INFOSYS-2022
    title: 'Tapping into a Digital Brain: AI-Powered Talent Management at Infosys (teaching case summary)'
    publisher: Kellogg School of Management
    type: academic
    url: https://www.kellogg.northwestern.edu/academics-research/research/detail/2022/tapping-into-a-digital-brain-ai-powered-talent-management/
    date: '2022-07-14'
    access: full
    locator: 'Case summary: manual talent allocation team, delivery managers rejecting matches (foundation, 2017
      events)'
  - ref: IPA-PERU-2026
    title: 'Automated Assignment and Bureaucrat Productivity: Evidence from a Field Experiment in Peru (working
      paper, Ferreira and Cermeno Leon)'
    publisher: Innovations for Poverty Action / Southern Methodist University
    type: academic
    url: https://poverty-action.org/sites/default/files/2026-07/main_assignment_enforcement_peru_2025.pdf
    date: '2026-06-11'
    access: full
    locator: Abstract (page 1)
  - ref: KANTATA-RESAGENT-2025
    title: Kantata Expands Agentic AI Capabilities with New Resourcing Agent Supercharging Professional Services
      Delivery (press release; BusinessWire blocked, seen in search results only)
    publisher: Kantata via Business Wire
    type: vendor
    url: https://www.businesswire.com/news/home/20250924498182/en/Kantata-Expands-Agentic-AI-Capabilities-with-New-Resourcing-Agent-Supercharging-Professional-Services-Delivery
    date: '2025-09-24'
    access: search-only
    locator: Search-result snippet only; not used for any outcome
  last_reviewed: '2026-10-19'
  notes: Grade B rests on Basware, a named customer whose release (a Kantata press release, with Basware executive
    quotes) describes an agent in use for project staffing. It publishes no staffing result. Basware is a software
    company; this is its customer services organisation. All figures are vendor claims with no stated method. No
    independent measurement found. Kantata Resourcing Agent (Sept 2025) is search-only (KANTATA-RESAGENT-2025).
    The Infosys case is foundation material only; its summary does not report outcomes.
- id: professional-services-staffing-resourcing-02
  title: Compatibility-scored staff suggestions in an accounting-firm workflow tool
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Workflow tools give structure and visibility but the decision of who does the work (preparer, reviewer)
    is still made from familiarity, perceived availability and individual judgment, which gets harder as firms grow
    (WK-CCHSTAFF-2026).
  solution: In the staffing dropdown of CCH Axcess Workflow, the system shows recommended staff with a compatibility
    score built from historical assignments, client familiarity, role alignment and current workload, plus a justification
    view. Firms can weight the criteria (for example client familiarity versus workload balancing in peak season).
    The user can pick anyone regardless of recommendation (WK-CCHSTAFF-2026).
  outcomes:
  - lever: speed
    description: Wolters Kluwer expects fewer last-minute reassignments, less manager time spent evaluating options
      and more consistent assignments over time; no figure and no customer is cited.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: WK-CCHSTAFF-2026
  prerequisites:
  - Historical assignment, client and workload data held in the workflow tool (WK-CCHSTAFF-2026)
  risks_and_guardrails:
  - Recommendations are advisory and can be overridden, because client relationships and development goals can affect
    the final choice (WK-CCHSTAFF-2026)
  - Annex III of the EU AI Act lists AI used to allocate tasks based on individual behaviour or personal traits
    or characteristics as high-risk; whether a given staffing tool falls in scope needs legal review (AIACT-ANNEX3-2024)
  human_checkpoints:
  - The person assigning staff selects the preparer and reviewer; a justification pop-up is available before choosing
    (WK-CCHSTAFF-2026)
  role_evolution: The article says managers spend less time evaluating options; it does not discuss role changes
    (WK-CCHSTAFF-2026).
  evidence_grade: C
  sources:
  - ref: WK-CCHSTAFF-2026
    title: The staffing challenge most workflow systems don't solve (CCH Axcess Workflow AI-powered staff recommendations)
    publisher: Wolters Kluwer Tax and Accounting
    type: vendor
    url: https://www.wolterskluwer.com/en/expert-insights/the-staffing-challenge-most-workflow-systems-dont-solve
    date: '2026-08-12'
    access: full
    locator: Key Takeaways; sections on how recommendations are generated, maintaining control, and configuring
      behaviour
  - ref: AIACT-ANNEX3-2024
    title: 'Annex III: High-Risk AI Systems Referred to in Article 6(2) (text of Regulation (EU) 2024/1689, as mirrored
      on artificialintelligenceact.eu)'
    publisher: European Union (text mirrored by Future of Life Institute)
    type: regulator
    url: https://artificialintelligenceact.eu/annex/3/
    date: '2024-06-13'
    access: full
    locator: Point 4(b)
  last_reviewed: '2026-10-19'
  notes: Product documentation from the vendor; no named customer, adoption figure or measurement found. The vendor
    frames the feature as available now ("we have introduced"); use is not evidenced, so maturity is announced.
    Page was reachable only through the text mirror. Generic staffing step in an accounting firm; no tax or audit
    technical content.
- id: professional-services-staffing-resourcing-03
  title: One skills-based staffing pool across business units and borders (Deutsche Telekom with Eightfold)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Deutsche Telekom ran several standalone project-staffing tools, each business with its own process. Project
    managers could only tap their local employee base, so best-fit people were overlooked and external hires were
    sometimes made when qualified internal candidates existed. Finding people by skills and availability took too
    many manual steps (EIGHTFOLD-DT-2025).
  solution: Apply a talent-intelligence platform's skills-based matching, already used for its internal opportunity
    marketplace and recruiting, to project staffing across the group. The story says staffing would be piloted in
    a technology delivery organisation with around 1,000 employees (mostly system engineers, devops engineers and
    product managers), with later use for agile teams and, over a longer period, client projects in its consulting
    businesses (EIGHTFOLD-DT-2025).
  outcomes:
  - lever: speed
    description: The story lists expected benefits (faster project staffing, group-wide visibility of resources,
      use of people on the bench) and says the platform "is expected to deliver" them. No measured result is given.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: EIGHTFOLD-DT-2025
  prerequisites:
  - An existing skills-based talent platform (customer since 2021) and a skills taxonomy used for recruiting and
    internal mobility (EIGHTFOLD-DT-2025)
  risks_and_guardrails:
  - 'Skills inference on individuals is under legal challenge in hiring: a January 2026 class action alleges Eightfold
    built hidden candidate scores that fall under consumer-reporting law. The suit concerns applicants, not staffing,
    and is unresolved (FISHERPHILLIPS-EIGHTFOLD-2026)'
  - Annex III of the EU AI Act lists AI used to allocate tasks based on individual behaviour or personal traits
    or characteristics as high-risk; whether a given staffing tool falls in scope needs legal review (AIACT-ANNEX3-2024);
    the Commission states Annex III rules apply from 2 December 2027 (EC-AIACT-2026)
  human_checkpoints:
  - Resource managers see availability and skills and decide; the story does not describe approvals in detail (EIGHTFOLD-DT-2025)
  role_evolution: Projects become another career-development avenue for employees, who can apply for best-fit projects
    in the internal opportunity marketplace (EIGHTFOLD-DT-2025).
  evidence_grade: C
  sources:
  - ref: EIGHTFOLD-DT-2025
    title: Deutsche Telekom seizes opportunity to apply AI to project staffing with Eightfold Resource Management
      (vendor customer story; the PDF is undated, 2025-03 is its file creation date)
    publisher: Eightfold AI
    type: vendor
    url: https://eightfold.ai/wp-content/uploads/deutsche-telekom-seizes-opportunity-ai-project-staffing-eightfold-resource-management.pdf
    date: 2025-03
    access: full
    locator: 'Pages 2-4: challenge, solution, results (expected benefits) and the future pilot'
  - ref: FISHERPHILLIPS-EIGHTFOLD-2026
    title: 'Job Applicants Sue AI Screening Company for FCRA Violations: 5 Key Takeaways for Employers'
    publisher: Fisher Phillips LLP
    type: firm
    url: https://www.fisherphillips.com/en/news-insights/job-applicants-sue-ai-screening-company-for-fcra-violations.html
    date: '2026-01-26'
    access: full
    locator: Opening paragraphs on the 20 January filing and core legal theory
  - ref: AIACT-ANNEX3-2024
    title: 'Annex III: High-Risk AI Systems Referred to in Article 6(2) (text of Regulation (EU) 2024/1689, as mirrored
      on artificialintelligenceact.eu)'
    publisher: European Union (text mirrored by Future of Life Institute)
    type: regulator
    url: https://artificialintelligenceact.eu/annex/3/
    date: '2024-06-13'
    access: full
    locator: Point 4(b)
  - ref: EC-AIACT-2026
    title: 'AI Act: regulatory framework page (timelines after the AI Omnibus)'
    publisher: European Commission
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: Section on AI Omnibus timelines (Annex III from 2 December 2027)
  last_reviewed: '2026-10-19'
  notes: Vendor customer story with a quoted Deutsche Telekom executive; the pilot is described as upcoming, and
    the story is undated (2025-03 is the PDF creation date). I found no later confirmation of the pilot or its results,
    so grade C and maturity announced. Deutsche Telekom is a telecom group with consulting businesses; included
    because it describes a project-staffing change for internal and consulting teams.
- id: professional-services-staffing-resourcing-04
  title: Agents supplement professional-development staff in choosing consultants for client teams (McKinsey)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: McKinsey professional-development staff have matched consultants to clients behind the scenes for decades.
    As the firm has grown to almost 40,000 employees, that process has become more complex (BLOOMBERGLAW-MCKINSEY-2026).
  solution: Bloomberg Law reports that McKinsey plans to use AI agents to help choose the consultants assigned to
    client teams, supplementing the professional-development employees. Its chief people officer for North America
    is quoted saying the aim is to ensure "we get the best people in the right situations" and that the firm is
    looking to "agentify" its staffing (BLOOMBERGLAW-MCKINSEY-2026).
  outcomes:
  - lever: quality
    description: None published. The article describes a plan; no result, pilot size or timeline was readable.
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: BLOOMBERGLAW-MCKINSEY-2026
  prerequisites:
  - Not described in the readable part of the article
  risks_and_guardrails:
  - The article says the shift may surprise some of the firm's customers around the globe (BLOOMBERGLAW-MCKINSEY-2026)
  - Annex III of the EU AI Act lists AI used to allocate tasks based on individual behaviour or personal traits
    or characteristics as high-risk; whether a given staffing tool falls in scope needs legal review (AIACT-ANNEX3-2024)
  human_checkpoints:
  - Agents "supplement" rather than replace the professional-development staff (BLOOMBERGLAW-MCKINSEY-2026)
  role_evolution: Professional-development staff continue to do the matching with agent support; no headcount or
    role change is stated (BLOOMBERGLAW-MCKINSEY-2026).
  evidence_grade: C
  sources:
  - ref: BLOOMBERGLAW-MCKINSEY-2026
    title: McKinsey Plans to Use AI Agents to Help Select Client Teams (paywalled; only the opening paragraphs were
      readable)
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/financial-accounting/mckinsey-plans-to-use-ai-agents-to-help-select-client-teams
    date: '2026-05-01'
    access: full
    locator: Opening three paragraphs (dateline 2026-05-01 from page metadata)
  - ref: AIACT-ANNEX3-2024
    title: 'Annex III: High-Risk AI Systems Referred to in Article 6(2) (text of Regulation (EU) 2024/1689, as mirrored
      on artificialintelligenceact.eu)'
    publisher: European Union (text mirrored by Future of Life Institute)
    type: regulator
    url: https://artificialintelligenceact.eu/annex/3/
    date: '2024-06-13'
    access: full
    locator: Point 4(b)
  last_reviewed: '2026-10-19'
  notes: Only the unpaywalled opening paragraphs were read. This is the only named large-firm staffing announcement
    found. It is a plan reported by the press ("plans to"), with no evidence of use, so maturity announced and grade
    C. Worth following up for how it is built and whether it has launched.
- id: professional-services-staffing-resourcing-05
  title: Reallocation agent finds replacements for people on work already in flight
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: Replacing a resource mid-project means finding every assignment, then searching for a match on the same
    criteria and timeframes; it is slow and complex (CPAPA-CERTINIA-2026).
  solution: Certinia's Reallocation Agent identifies all of the person's assignments, searches for best-match replacements
    using the same criteria and timeframes, and proposes them to resource managers (CPAPA-CERTINIA-2026). Certinia's
    product page lists a Work Reallocation Agent that "identifies and proposes replacements for work in flight"
    (CERTINIA-VEDA-2026).
  outcomes:
  - lever: capacity
    description: Included in Certinia's "up to 10 hours per month" claim for resource managers (staffing analysis,
      bench matching and work reallocation combined); the claim is not broken out by task.
    figure: up to 10 hours per month (combined)
    measures: Hours of capacity returned per month to resource managers, per Certinia; no method or sample given
    provenance: vendor-published
    source_ref: CPAPA-CERTINIA-2026
  prerequisites:
  - Assignment, skills and availability data in the Certinia platform (CPAPA-CERTINIA-2026)
  risks_and_guardrails:
  - diginomica notes that humans are still needed to verify that agent-recommended actions are correct, and quotes
    Certinia saying accountability stays with humans (DIGINOMICA-CERTINIA-2026)
  human_checkpoints:
  - The agent proposes; resource managers decide (CPAPA-CERTINIA-2026)
  role_evolution: Resource managers review proposals instead of building replacement searches by hand; no role change
    is described.
  evidence_grade: C
  sources:
  - ref: CPAPA-CERTINIA-2026
    title: Certinia Unveils Veda, an AI Operations Engine for Professional Services
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/04/15/certinia-unveils-veda-an-ai-operations-engine-for-professional-services/181702/
    date: '2026-04-15'
    access: full
    locator: Bullet "Reallocation Agent"
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (product page; page carries no publication date,
      date shown is the retrieval date)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Plan row, Work Reallocation Agent
  - ref: DIGINOMICA-CERTINIA-2026
    title: Certinia unveils Veda, its AI engine for Professional Services Automation
    publisher: diginomica
    type: press
    url: https://diginomica.com/certinia-unveils-veda-ai-engine-professional-services-automation
    date: '2026-04-15'
    access: full
    locator: Paragraphs on the 10 beta agents, over 20 lighthouse customers and the "My take" closing
  - ref: CONSTELLATION-CERTINIA-2026
    title: Certinia launches System of Action, scales Veda AI agents, intelligent actions
    publisher: Constellation Research
    type: press
    url: https://www.constellationr.com/insights/news/certinia-launches-system-action-scales-veda-ai-agents-intelligent-actions
    date: '2026-09-09'
    access: full
    locator: Opening paragraphs on 14 new agents and 135 intelligent actions (published 2026-09-09)
  last_reviewed: '2026-10-19'
  notes: The 10 packaged agents were in beta at launch on 2026-04-15 with 64 intelligent actions generally available
    (DIGINOMICA-CERTINIA-2026); Certinia said in September 2026 that it had added 14 agents and 135 intelligent
    actions (CONSTELLATION-CERTINIA-2026). No named customer for this agent was found.
- id: professional-services-staffing-resourcing-06
  title: Matching bench staff to open and unsold work, with soft-booking before contracts are signed
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Consultants sit idle between projects while the person staffing work does not see them; the same people
    get tapped repeatedly (PROJECTWORKS-2026). Planning for work not yet sold is hard because pipeline and capacity
    data live apart.
  solution: The system matches people who are unassigned to internal work, learning, pre-sales support or short
    fills (PROJECTWORKS-2026). Kantata's "Skills Profiling on Unsold Work" lets firms pre-plan and soft-book resources
    before contracts are signed and see skills gaps early (KANTATA-FORECAST-2026). Certinia says Veda matches skills,
    availability and cost to the work and re-matches when resources shift, to reduce bench time (CERTINIA-VEDA-2026).
    The Deutsche Telekom story expects people "on the bench" to be used where needed (EIGHTFOLD-DT-2025).
  outcomes:
  - lever: capacity
    description: No measured bench or utilisation result published for this step. Certinia states "reducing bench
      time in real time" as a benefit; no figure.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Pipeline, skills and availability data connected in one system (PROJECTWORKS-2026)
  risks_and_guardrails:
  - Bench rules are a management lever with employee effects. TCS (a non-AI example) required associates to have
    been allocated at least 225 business days in the last 12 months, which cuts permitted bench time to about 35
    days (CXODP-TCS-2025)
  human_checkpoints:
  - Ops leader or resource manager makes the call (PROJECTWORKS-2026)
  role_evolution: Bench becomes a planning lever rather than a line item (PROJECTWORKS-2026); the source is a vendor
    blog.
  evidence_grade: C
  sources:
  - ref: PROJECTWORKS-2026
    title: How AI Is Changing Resource Planning for Consulting Firms
    publisher: Projectworks
    type: vendor
    url: https://www.projectworks.com/blog/how-ai-changes-resource-planning
    date: '2026-06-25'
    access: full
    locator: Sections on bench management and on how AI changes resource planning
  - ref: KANTATA-FORECAST-2026
    title: Resource Forecasting and Staffing (product page; page carries no publication date, date shown is the
      retrieval date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/solutions/resource-forecasting-and-staffing
    date: '2026-10-19'
    access: full
    locator: '"Skills Profiling on Unsold Work" in the How Kantata Can Help list'
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (product page; page carries no publication date,
      date shown is the retrieval date)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: '"Staff with confidence, not guesswork" panel'
  - ref: EIGHTFOLD-DT-2025
    title: Deutsche Telekom seizes opportunity to apply AI to project staffing with Eightfold Resource Management
      (vendor customer story; the PDF is undated, 2025-03 is its file creation date)
    publisher: Eightfold AI
    type: vendor
    url: https://eightfold.ai/wp-content/uploads/deutsche-telekom-seizes-opportunity-ai-project-staffing-eightfold-resource-management.pdf
    date: 2025-03
    access: full
    locator: Results page, first benefit
  - ref: CXODP-TCS-2025
    title: TCS Rolls Out Strict Talent Deployment Policy Amid AI Push and Cost Pressures
    publisher: CXO Digitalpulse
    type: press
    url: https://www.cxodigitalpulse.com/tcs-rolls-out-strict-talent-deployment-policy-amid-ai-push-and-cost-pressures/
    date: '2025-06-23'
    access: full
    locator: Opening paragraphs on the 225-day rule (not an AI example)
  last_reviewed: '2026-10-19'
  notes: 'Evidence is product and vendor-blog description only. The TCS item is context for bench pressure: the
    article itself says the policy does not explicitly mandate AI (attributed there to a Forrester analyst) and
    was published 2025-06-23. A search result reported industry bench ratios falling (TeamLease Digital data); that
    page returned 403 and is not used as evidence.'
- id: professional-services-staffing-resourcing-07
  title: Rolling demand and capacity forecast from pipeline, by role and skill
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
  maturity: in-production
  problem: The pipeline says work is coming, but nobody turns that signal into hiring or contracting decisions early
    enough. Pipeline lives in the CRM, capacity in a spreadsheet, and forecasting happens quarterly at best (PROJECTWORKS-2026).
    71% of organisations use spreadsheets for resource processes (RMI Research, quoted by KANTATA-FORECAST-2026).
  solution: Connect the CRM and capacity plan into a rolling forecast that applies win rates and seasonal patterns
    and shows where demand will exceed supply by role, skill and period, updating when deals move (PROJECTWORKS-2026).
    Hakkoda moved from forecasting four weeks ahead to three to six months ahead with Kantata, aligning headcount
    growth with revenue growth (KANTATA-FORECAST-2026).
  outcomes:
  - lever: quality
    description: 'Hakkoda (customer quote): forecasting out 3-6 months instead of 4 weeks; the page lists 10% absolute
      improvement in average project margin and about 5% improvement in allocated resource utilisation rate.'
    figure: 10% absolute improvement in average project margin; about 5% improvement in allocated resource utilization
      rate
    measures: Improvements as listed on Kantata's product page beside the Hakkoda quote; baseline, period and the
      exact meaning of "about 5%" (points or relative) are not stated
    provenance: vendor-published
    source_ref: KANTATA-FORECAST-2026
  - lever: quality
    description: Deltek states 20% improvement in forecast accuracy by connecting people, projects and financials
      in one application.
    figure: 20%
    measures: Improvement in forecast accuracy as worded on the Polaris page; no baseline or sample given
    provenance: vendor-published
    source_ref: DELTEK-POLARIS-2026
  prerequisites:
  - Pipeline (CRM), resource plan and financials connected (PROJECTWORKS-2026; DELTEK-POLARIS-2026)
  - Win-rate history to weight opportunities (PROJECTWORKS-2026)
  risks_and_guardrails:
  - The Hakkoda figures sit on a vendor page and the source does not show whether the forecasting was AI-driven;
    treat as adjacent evidence for PSA forecasting (KANTATA-FORECAST-2026)
  - 'Data quality is the main barrier: 47% of RMI respondents cite poor or fragmented data (KANTATA-RMI-2026)'
  human_checkpoints:
  - Ops leader reviews the forecast and decides hiring and contracting (PROJECTWORKS-2026)
  role_evolution: Forecasting moves from a quarterly exercise to a weekly one for the ops leader (PROJECTWORKS-2026).
    RMI respondents most wanted AI to refine demand and capacity forecasts (72%; KANTATA-RMIPAGE-2026).
  evidence_grade: B
  sources:
  - ref: KANTATA-FORECAST-2026
    title: Resource Forecasting and Staffing (product page; page carries no publication date, date shown is the
      retrieval date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/solutions/resource-forecasting-and-staffing
    date: '2026-10-19'
    access: full
    locator: Hakkoda quote and results list; spreadsheet statistic
  - ref: PROJECTWORKS-2026
    title: How AI Is Changing Resource Planning for Consulting Firms
    publisher: Projectworks
    type: vendor
    url: https://www.projectworks.com/blog/how-ai-changes-resource-planning
    date: '2026-06-25'
    access: full
    locator: Section on forecasting demand from pipeline
  - ref: DELTEK-POLARIS-2026
    title: Deltek Polaris (product page; page carries no publication date, date shown is the retrieval date)
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/en/products/polaris/
    date: '2026-10-19'
    access: full
    locator: Results panel
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services (press release on the Resource Management Institute study 'Resource Management in the
      Age of AI')
    publisher: Kantata (study by Resource Management Institute, commissioned by Kantata)
    type: survey
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraph on barriers
  - ref: KANTATA-RMIPAGE-2026
    title: Ready for AI Resource Management? Survey Says... Not Yet (insights page for the same RMI study; page
      carries no date, date shown is the retrieval date)
    publisher: Kantata (study by Resource Management Institute)
    type: survey
    url: https://www.kantata.com/resource/resource-management-in-the-age-of-ai
    date: '2026-10-19'
    access: full
    locator: Section "The real AI ask"
  last_reviewed: '2026-10-19'
  notes: 'Grade B (named customer, vendor-published figures, adjacent to AI: the sources describe forecasting in
    PSA software, not shown to be machine-learning based). The RMIPAGE figure 72% is the share of the 44 surveyed
    firms who asked for AI to refine demand and capacity forecasts; the question wording is not available.'
- id: professional-services-staffing-resourcing-08
  title: Staffing scenarios across projects with margin impact shown at the point of decision
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Staffing choices are made with the financial consequence invisible until a later review (PROJECTWORKS-2026).
    Comparing options across several projects, or internal versus external resources, is hard by hand.
  solution: Kantata's Staffing Optimizer uses AI-driven optimisation to model staffing scenarios across multiple
    projects and resource permutations "beyond human capacity", and Candidate Assignments compares internal and
    external resources side by side on skills, availability and margin impact (KANTATA-FORECAST-2026). Projectworks
    describes margin impact appearing when a contractor is added or seniority mix changed (PROJECTWORKS-2026).
  outcomes:
  - lever: quality
    description: None published.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: KANTATA-FORECAST-2026
  prerequisites:
  - Rates, costs and budgets in the same system as resource plans (PROJECTWORKS-2026)
  risks_and_guardrails:
  - The one independent field test of an optimisation-based allocation rule found worse on-time completion than
    manager discretion in its setting (IPA-PERU-2026; see use case 17)
  human_checkpoints:
  - Ops leader or resource manager chooses among scenarios (KANTATA-FORECAST-2026; PROJECTWORKS-2026)
  role_evolution: Resource managers weigh cost and margin as well as availability; RMI says that under outcome-based
    pricing the role would shift from filling hours to maximising delivery success and profitability (KANTATA-RMI-2026).
  evidence_grade: C
  sources:
  - ref: KANTATA-FORECAST-2026
    title: Resource Forecasting and Staffing (product page; page carries no publication date, date shown is the
      retrieval date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/solutions/resource-forecasting-and-staffing
    date: '2026-10-19'
    access: full
    locator: '"Staffing Optimizer" and "Candidate Assignments" entries'
  - ref: PROJECTWORKS-2026
    title: How AI Is Changing Resource Planning for Consulting Firms
    publisher: Projectworks
    type: vendor
    url: https://www.projectworks.com/blog/how-ai-changes-resource-planning
    date: '2026-06-25'
    access: full
    locator: Section on utilisation and margin at the point of decision
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services (press release on the Resource Management Institute study 'Resource Management in the
      Age of AI')
    publisher: Kantata (study by Resource Management Institute, commissioned by Kantata)
    type: survey
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraph on outcome-based pricing and the shift from filling hours
  - ref: IPA-PERU-2026
    title: 'Automated Assignment and Bureaucrat Productivity: Evidence from a Field Experiment in Peru (working
      paper, Ferreira and Cermeno Leon)'
    publisher: Innovations for Poverty Action / Southern Methodist University
    type: academic
    url: https://poverty-action.org/sites/default/files/2026-07/main_assignment_enforcement_peru_2025.pdf
    date: '2026-06-11'
    access: full
    locator: Abstract and introduction
  last_reviewed: '2026-10-19'
  notes: Product-page description only; no named customer or measurement.
- id: professional-services-staffing-resourcing-09
  title: Staffing requests read from client emails and portals, turned into roles, matched and booked
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - document-production
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Consulting firms receive a constant stream of requests by email, competency portals and RFPs. Someone
    reads the email, copies it into the pipeline, compares it with available consultants and checks with managers,
    and may not answer the same day (CINODE-2026).
  solution: Cinode's MailMatch reads incoming emails, follows links to procurement portals and interprets PDF and
    Word attachments to extract roles, skills and proficiency, dates, scope, location and sales owner. It creates
    a pipeline project with one role per position, runs semantic matching (Scrum matches an Agile requirement) weighted
    for must-haves, and lets the user book directly. A tailored CV and proposal are generated from the profile data
    (CINODE-2026).
  outcomes:
  - lever: speed
    description: None published. The post claims "more won assignments, higher utilization, and happier consultants"
      with no figure.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: CINODE-2026
  prerequisites:
  - Maintained consultant profiles with skills, certifications and availability (CINODE-2026)
  - A shared inbox and a pipeline in the same system (CINODE-2026)
  risks_and_guardrails:
  - The user "keeps the same flow" and can enter assignments manually and decide when AI becomes part of the process
    (CINODE-2026)
  human_checkpoints:
  - Staffer reviews matches and decides booking (CINODE-2026)
  role_evolution: Staffers stop re-keying emails and searching spreadsheets; no role change described.
  evidence_grade: C
  sources:
  - ref: CINODE-2026
    title: 'The entire matching flow in Cinode: From email to booked consultant with AI'
    publisher: Cinode
    type: vendor
    url: https://cinode.com/en/blog/cinode-en/the-entire-matching-flow-in-cinode-from-email-to-booked-consultant-with-ai/
    date: '2026-05-13'
    access: full
    locator: Steps 1 to 3 of the flow and the full-flow summary
  last_reviewed: '2026-10-19'
  notes: Vendor product walkthrough (a Swedish consulting-staffing platform); no named customer or result. Included
    because it is the clearest description found of request-to-role intake. Ework's Verama portal and Wise Group's
    Folq integration surfaced in a search but were not opened.
- id: professional-services-staffing-resourcing-10
  title: Planning, allocating and costing AI agents alongside people as assignable capacity
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Firms are starting to run blended teams of people and agents, but resource managers lack tools and playbooks.
    RMI found 52.7% of respondents not equipped to manage hybrid human-agent teams (KANTATA-RMI-2026). Leaders also
    say systems will need to attribute work, cost and value across humans and agents (KANTATA-STATE-2026).
  solution: 'Planview announced Agent Resource Management to plan, govern and cost human and agent capacity, including
    scenario modelling of the human-to-agent mix and tracking agent spend and accountability; availability is stated
    as beginning Fall 2026 with early access (SDTIMES-PLANVIEW-2026). Kantata and Certinia describe the same direction:
    agents treated as capacity that is planned, allocated and measured (KANTATA-FORBES-2026; DIGINOMICA-CERTINIA-2026).'
  outcomes:
  - lever: capacity
    description: 'None published. The evidence is adoption readiness: 11% of RMI respondents were implementing formal
      pilots for planning and assigning AI agents, 57% had it on the roadmap, 32% did not.'
    figure: 11% / 57% / 32%
    measures: Shares of the 44 firms in the RMI study in implementation, not yet operational but on the roadmap,
      and not on the roadmap, for AI agents as part of the assignable workforce
    provenance: vendor-published
    source_ref: KANTATA-RMIPAGE-2026
  - lever: experience
    description: 52.7% of RMI respondents said they were not equipped to manage hybrid teams; another 28.4% only
      slightly equipped; 4% well equipped.
    figure: 52.7% / 28.4% / 4%
    measures: Shares of the 44 organisations surveyed, in the study's words "not equipped", "only slightly equipped"
      and "well equipped" to manage hybrid human and AI teams
    provenance: vendor-published
    source_ref: KANTATA-RMI-2026
  prerequisites:
  - A shared register of agents with cost and ownership; Planview says leaders lack insight into whether resources
    are allocated to the right work and who is accountable (SDTIMES-PLANVIEW-2026)
  - Playbooks and skills enablement before hybrid staffing is routine (KANTATA-RMI-2026)
  risks_and_guardrails:
  - 'Governance is the open question: which actions agents take on their own, which need approval, how AI work is
    costed and how decisions are audited (ERPTODAY-KANTATA-2026)'
  - 'Sample is small and vendor-commissioned: 44 organisations (KANTATA-RMI-2026)'
  human_checkpoints:
  - Accountability stays with humans, per Certinia (DIGINOMICA-CERTINIA-2026)
  role_evolution: Resource management takes on team composition, delivery risk and economics rather than filling
    hours, if outcome-based pricing spreads; 1 in 2 RMI respondents were unsure their firm will adopt it (KANTATA-RMI-2026).
  evidence_grade: C
  sources:
  - ref: SDTIMES-PLANVIEW-2026
    title: Planview Launches Agent Resource Management, Redefining Portfolio Resource Management for the AI Era
    publisher: SD Times
    type: press
    url: https://sdtimes.com/agentic-ai/planview-launches-agent-resource-management-redefining-portfolio-resource-management-for-the-ai-era/
    date: '2026-05-04'
    access: full
    locator: Announcement paragraphs and availability statement
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services (press release on the Resource Management Institute study 'Resource Management in the
      Age of AI')
    publisher: Kantata (study by Resource Management Institute, commissioned by Kantata)
    type: survey
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraphs on hybrid teams, outcome-based pricing and the sample (44 organisations)
  - ref: KANTATA-RMIPAGE-2026
    title: Ready for AI Resource Management? Survey Says... Not Yet (insights page for the same RMI study; page
      carries no date, date shown is the retrieval date)
    publisher: Kantata (study by Resource Management Institute)
    type: survey
    url: https://www.kantata.com/resource/resource-management-in-the-age-of-ai
    date: '2026-10-19'
    access: full
    locator: Chart "Organizations Expecting to Use AI Agents as Part of Assignable Workforce"
  - ref: KANTATA-STATE-2026
    title: Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their
      Workforce (press release on the State of the Professional Services Industry report; Censuswide survey of 200
      leaders)
    publisher: Kantata
    type: survey
    url: https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce
    date: '2026-01-08'
    access: full
    locator: Paragraph on resourcing and attributing work, cost and value to humans and agents (90%)
  - ref: KANTATA-FORBES-2026
    title: 'Professional Services 2026: When AI Becomes A Billable Team Member (Forbes Technology Council post by
      Kantata Chief Product Strategy Officer, republished by Kantata)'
    publisher: Forbes Technology Council
    type: press
    url: https://www.kantata.com/blog/article/professional-services-2026-when-ai-becomes-a-billable-team-member
    date: '2026-01-16'
    access: full
    locator: Prediction 1, AI agents as billable team members
  - ref: DIGINOMICA-CERTINIA-2026
    title: Certinia unveils Veda, its AI engine for Professional Services Automation
    publisher: diginomica
    type: press
    url: https://diginomica.com/certinia-unveils-veda-ai-engine-professional-services-automation
    date: '2026-04-15'
    access: full
    locator: Malhotra quotes on hybrid teams and accountability
  - ref: ERPTODAY-KANTATA-2026
    title: Kantata's Expertise Agent Targets the Professional Services Delivery Crunch (ERP Today article, republished
      on kantata.com; date from page metadata)
    publisher: ERP Today
    type: press
    url: https://www.kantata.com/blog/article/erp-today-kantatas-expertise-agent-targets-the-professional-services-delivery-crunch
    date: '2026-06-19'
    access: full
    locator: Section "Agentic PSA Tests New Operating Model"
  last_reviewed: '2026-10-19'
  notes: Announced products and survey readiness data only. Planview content is a press release repeated by SD Times.
    The same area overlaps delivery-management and firm-finance (costing agents).
- id: professional-services-staffing-resourcing-11
  title: 'Conversational resourcing assistant: ask who has the skills and capacity, get an answer and a drafted
    plan'
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Answering "who has this experience and capacity in July" takes a morning of phone calls and spreadsheet
    checks (PROJECTWORKS-2026).
  solution: Natural-language queries over the PSA data, and multi-step actions such as flagging a resource conflict
    or generating a project plan from an SOW. Kantata launched Expertise Agent on 2026-06-16 as a superagent for
    project, resource and financial questions (ERPTODAY-KANTATA-2026; KANTATA-AGENT-2026); Rocketlane markets a
    Nitro Resource Management Agent (ROCKETLANE-2026); Projectworks describes the query use (PROJECTWORKS-2026);
    Certinia lists an Ask Veda Agent and Project Assistant (CERTINIA-VEDA-2026).
  outcomes:
  - lever: speed
    description: Projectworks says a query that took a morning of calls returns in seconds; this is an illustration,
      not a measurement.
    figure: seconds versus a morning
    measures: Illustrative example of time to answer a skills-and-capacity question, not a measured result
    provenance: vendor-published
    source_ref: PROJECTWORKS-2026
  prerequisites:
  - Connected data across projects, people, financials and communications; Kantata says its knowledge graph links
    these (ERPTODAY-KANTATA-2026)
  risks_and_guardrails:
  - Kantata's own CEO warns of "fast, mediocre decisions" if firms rely on generic tools without context (KANTATA-SUPERAGENT-2026)
  - 'Users must be able to see why: Kantata stresses recommendations with reasoning (KANTATA-AGENT-2026)'
  human_checkpoints:
  - The person asking decides; agents act within guardrails the firm defines once (KANTATA-AGENT-2026)
  role_evolution: Resource managers and ops leaders query the system directly instead of relying on one person who
    holds the staffing map (PROJECTWORKS-2026; ROCKETLANE-2026).
  evidence_grade: C
  sources:
  - ref: ERPTODAY-KANTATA-2026
    title: Kantata's Expertise Agent Targets the Professional Services Delivery Crunch (ERP Today article, republished
      on kantata.com; date from page metadata)
    publisher: ERP Today
    type: press
    url: https://www.kantata.com/blog/article/erp-today-kantatas-expertise-agent-targets-the-professional-services-delivery-crunch
    date: '2026-06-19'
    access: full
    locator: Opening paragraphs and analysis sections (launch on 16 June)
  - ref: KANTATA-AGENT-2026
    title: Expertise Agent and Workflows (product page; page carries no publication date, date shown is the retrieval
      date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/ai/expertise-agent-and-workflows
    date: '2026-10-19'
    access: full
    locator: Expertise Agent and Agent Studio panels
  - ref: KANTATA-SUPERAGENT-2026
    title: 'More Agents Won''t Fix Unpredictable Projects: Why We Built a Superagent Instead (vendor blog summarising
      a podcast episode)'
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead
    date: '2026-06-16'
    access: full
    locator: Sections on fast versus accurate and on one agent for the whole business
  - ref: ROCKETLANE-2026
    title: 'AI for PS Resource Allocation: 2026 Guide'
    publisher: Rocketlane
    type: vendor
    url: https://blog.rocketlane.com/blogs/ai-for-ps-resource-allocation
    date: '2026-07-22'
    access: full
    locator: Persona table naming the Nitro Resource Management Agent; example queries
  - ref: PROJECTWORKS-2026
    title: How AI Is Changing Resource Planning for Consulting Firms
    publisher: Projectworks
    type: vendor
    url: https://www.projectworks.com/blog/how-ai-changes-resource-planning
    date: '2026-06-25'
    access: full
    locator: Section on finding people for a role
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: System of Action for Professional Services (product page; page carries no publication date,
      date shown is the retrieval date)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Deliver and Manage rows
  last_reviewed: '2026-10-19'
  notes: All vendor sources. Rocketlane customer stories (Hapi Cloud 85% billable utilisation; Fluxx 83%) credit
    automation in general, not the agent, and were not used as outcomes.
- id: professional-services-staffing-resourcing-12
  title: 'Idea: staffing on delivery outcomes (which people and agent combinations produce good results)'
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Resource managers are asked to support outcome-oriented delivery without outcome data. Only 7.3% of RMI
    respondents said outcome data is easily accessible and routinely used in staffing decisions; 24.6% said only
    major wins or failures are known informally and another 24.6% said outcomes are not available at all (KANTATA-RMI-2026).
  solution: 'Idea: feed delivery outcomes (margin, client result, delivery risk) into staffing recommendations so
    that team composition, including the human-agent mix, is chosen for results. 73.4% of respondents said knowing
    which combinations of people or agents consistently produce strong outcomes would be very or extremely valuable;
    50.9% said outcome experience already has a high or very high influence on staffing recommendations for prospective
    deals (KANTATA-RMI-2026). Kantata''s Expertise Engine release describes a planned Sales Accelerator that would
    use delivery history to propose proposals with risks and "optimal human-AI resource mixes" (KANTATA-ENGINE-2025).'
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: KANTATA-RMI-2026
  prerequisites:
  - Outcome data routinely linked to who delivered; only 7.3% have this in staffing today (KANTATA-RMI-2026)
  risks_and_guardrails:
  - Annex III of the EU AI Act lists AI used to allocate tasks based on individual behaviour or personal traits
    or characteristics as high-risk; whether a given staffing tool falls in scope needs legal review (AIACT-ANNEX3-2024)
  human_checkpoints:
  - Not described
  role_evolution: RMI respondents describe an aspiration for resource management to become more data-driven, outcome-aware
    and strategically influential (KANTATA-RMI-2026).
  evidence_grade: D
  sources:
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services (press release on the Resource Management Institute study 'Resource Management in the
      Age of AI')
    publisher: Kantata (study by Resource Management Institute, commissioned by Kantata)
    type: survey
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraphs on outcome data (7.3%, 24.6%, 73.4%, 50.9%)
  - ref: KANTATA-ENGINE-2025
    title: Kantata Unveils the Kantata Expertise Engine (press release)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/kantata-unveils-the-kantata-expertise-engine-the-first-ai-platform-purpose-built-for-professional-services-transformation
    date: '2025-10-09'
    access: full
    locator: Paragraph on the Sales Accelerator planned for early 2026
  - ref: AIACT-ANNEX3-2024
    title: 'Annex III: High-Risk AI Systems Referred to in Article 6(2) (text of Regulation (EU) 2024/1689, as mirrored
      on artificialintelligenceact.eu)'
    publisher: European Union (text mirrored by Future of Life Institute)
    type: regulator
    url: https://artificialintelligenceact.eu/annex/3/
    date: '2024-06-13'
    access: full
    locator: Point 4(b)
  last_reviewed: '2026-10-19'
  notes: Idea. Discussed by survey respondents and on the vendor roadmap (the Sales Accelerator was "planned for
    early 2026" in a 2025-10-09 release; its release status was not checked). No firm was found using outcome data
    in staffing. Sample of 44 organisations; vendor-commissioned.
- id: professional-services-staffing-resourcing-13
  title: Continuous utilisation and overallocation monitoring with early alerts
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: 'Utilisation problems are found in last month''s report, after they started six weeks earlier (PROJECTWORKS-2026).
    Benchmarks show a real utilisation problem: SPI reports average billable utilisation fell to 66.4% in 2025,
    the lowest in its survey history, against 68.9% in 2024 and a 75% level it treats as optimal (DELTEK-SPIBENCH-2026).'
  solution: 'A background process monitors allocation and flags risks early: for example hours above target for
    two consecutive weeks, or a team''s utilisation below a threshold (PROJECTWORKS-2026); Rocketlane describes
    allocation-accuracy checks that flag anyone booked over 100% capacity across several weeks (ROCKETLANE-2026);
    Kantata''s Expertise Agent monitors project-portfolio health and routes alerts (closer to delivery-management),
    and a Resourcing Agent (September 2025) was reported to flag overallocation (KANTATA-AGENT-2026; KANTATA-RESAGENT-2025,
    search-only); Deltek says Dela uses machine learning on past project performance and resource utilisation (DELTEK-DELA-2026).'
  outcomes:
  - lever: capacity
    description: 'No measured result for the monitoring step. Context benchmark: SPI reports average billable utilisation
      of 66.4% in 2025, down from 68.9% in 2024.'
    figure: 66.4% (2025)
    measures: Average billable utilisation across the 500+ firms in the 2026 SPI Professional Services Maturity
      Benchmark (2025 results); billable utilisation is the percentage of available consultant time charged to clients
    provenance: independent
    source_ref: DELTEK-SPIBENCH-2026
  - lever: capacity
    description: SPI reports Level 5 (Optimized) firms exceed 80% billable utilisation.
    figure: above 80%
    measures: Billable utilisation of Level 5 (Optimized) organisations in the same benchmark
    provenance: independent
    source_ref: DELTEK-SPIKPI-2026
  prerequisites:
  - Accurate time and allocation data; Kantata's survey finds only 12% fully trust their systems data (KANTATA-STATE-2026)
  risks_and_guardrails:
  - Utilisation targets can push burnout and quality risk; SPI advises aiming for 70-75% or more balanced against
    burnout and quality (DELTEK-SPIKPI-2026)
  human_checkpoints:
  - Ops leader acts on the alerts (PROJECTWORKS-2026)
  role_evolution: Ops leaders move from waiting for monthly reports to acting on alerts; described by a vendor,
    not evidenced (PROJECTWORKS-2026).
  evidence_grade: C
  sources:
  - ref: PROJECTWORKS-2026
    title: How AI Is Changing Resource Planning for Consulting Firms
    publisher: Projectworks
    type: vendor
    url: https://www.projectworks.com/blog/how-ai-changes-resource-planning
    date: '2026-06-25'
    access: full
    locator: Section on utilisation and margin monitoring
  - ref: ROCKETLANE-2026
    title: 'AI for PS Resource Allocation: 2026 Guide'
    publisher: Rocketlane
    type: vendor
    url: https://blog.rocketlane.com/blogs/ai-for-ps-resource-allocation
    date: '2026-07-22'
    access: full
    locator: Section on AI governance and allocation accuracy checks
  - ref: KANTATA-AGENT-2026
    title: Expertise Agent and Workflows (product page; page carries no publication date, date shown is the retrieval
      date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/ai/expertise-agent-and-workflows
    date: '2026-10-19'
    access: full
    locator: '"Predictive Portfolio Health" panel'
  - ref: KANTATA-RESAGENT-2025
    title: Kantata Expands Agentic AI Capabilities with New Resourcing Agent Supercharging Professional Services
      Delivery (press release; BusinessWire blocked, seen in search results only)
    publisher: Kantata via Business Wire
    type: vendor
    url: https://www.businesswire.com/news/home/20250924498182/en/Kantata-Expands-Agentic-AI-Capabilities-with-New-Resourcing-Agent-Supercharging-Professional-Services-Delivery
    date: '2025-09-24'
    access: search-only
    locator: 'Search-result snippet only: Resourcing Agent flags overallocations and suggests redistributing hours'
  - ref: DELTEK-DELA-2026
    title: Dela, the Deltek AI orchestrator (product page; page carries no publication date, date shown is the retrieval
      date)
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/en/products/platform/dela/
    date: '2026-10-19'
    access: full
    locator: Paragraph on machine learning and resource utilisation
  - ref: DELTEK-SPIBENCH-2026
    title: '2026 PSO Benchmarks: What We Learned and What is Next from the SPI Maturity Benchmark Report (Deltek
      article reporting the SPI Research benchmark; Deltek sponsors the report)'
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/resources/articles/professional-services-benchmarks/
    date: '2026-07-30'
    access: full
    locator: Section 2, Operational Inefficiencies Persist
  - ref: DELTEK-SPIKPI-2026
    title: 5 KPIs from the SPI Professional Services Maturity Benchmark Report Every PSO Must Track for Sustainable
      Growth
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/en/resources/articles/5-kpis-from-the-spi-professional-services-maturity-benchmark-report-every-pso-must-track-for-sustainable-growth
    date: '2026-07-15'
    access: full
    locator: Section 1, Billable Utilization
  - ref: KANTATA-STATE-2026
    title: Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their
      Workforce (press release on the State of the Professional Services Industry report; Censuswide survey of 200
      leaders)
    publisher: Kantata
    type: survey
    url: https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce
    date: '2026-01-08'
    access: full
    locator: Paragraph on data trust
  last_reviewed: '2026-10-19'
  notes: The SPI figures are a survey-based benchmark published by Deltek, which sponsors the report and sells related
    software; they describe the problem, not the effect of monitoring. The 66.4% figure is independent of any monitoring
    tool. The search-only Resourcing Agent source is not used for any outcome.
- id: professional-services-staffing-resourcing-14
  title: Keeping the skills inventory current from profiles, project history and role descriptions
  archetype: professional-services
  module: staffing-resourcing
  function: people-hr
  work_types:
  - data-reporting
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: 'Skills data is thin and stale: only 40% of respondents in an earlier RMI survey were happy with skills
    tracking, and 47% of 2026 respondents name poor or fragmented data across skills, outcomes, demand and capacity
    as the biggest gap (KANTATA-RMI-2026; KANTATA-RMIPAGE-2026 for the 2026 figure).'
  solution: AI suggests skills for a role from its title and description (Cinode), matches semantically related
    skills rather than exact keywords (CINODE-2026), and builds a skills-based view of people across recruiting,
    mobility and staffing (EIGHTFOLD-DT-2025). Deltek describes certification tracking with skill-based matching
    (DELTEK-POLARIS-2026). Respondents asked most for AI to enhance skills intelligence (68%; KANTATA-RMIPAGE-2026).
  outcomes:
  - lever: quality
    description: None published for skills-inventory upkeep.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: CINODE-2026
  prerequisites:
  - A skills taxonomy and profile data per person (CINODE-2026; EIGHTFOLD-DT-2025)
  risks_and_guardrails:
  - Skills inference about individuals is being tested in court in hiring (FISHERPHILLIPS-EIGHTFOLD-2026)
  - Evidence on employee consent and visibility of inferred skills was not found in the sources read
  human_checkpoints:
  - Not described
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: CINODE-2026
    title: 'The entire matching flow in Cinode: From email to booked consultant with AI'
    publisher: Cinode
    type: vendor
    url: https://cinode.com/en/blog/cinode-en/the-entire-matching-flow-in-cinode-from-email-to-booked-consultant-with-ai/
    date: '2026-05-13'
    access: full
    locator: Step 3, what the matching engine takes into account
  - ref: EIGHTFOLD-DT-2025
    title: Deutsche Telekom seizes opportunity to apply AI to project staffing with Eightfold Resource Management
      (vendor customer story; the PDF is undated, 2025-03 is its file creation date)
    publisher: Eightfold AI
    type: vendor
    url: https://eightfold.ai/wp-content/uploads/deutsche-telekom-seizes-opportunity-ai-project-staffing-eightfold-resource-management.pdf
    date: 2025-03
    access: full
    locator: Solution section on becoming skills-based
  - ref: DELTEK-POLARIS-2026
    title: Deltek Polaris (product page; page carries no publication date, date shown is the retrieval date)
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/en/products/polaris/
    date: '2026-10-19'
    access: full
    locator: Polaris FAQ on resource management
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services (press release on the Resource Management Institute study 'Resource Management in the
      Age of AI')
    publisher: Kantata (study by Resource Management Institute, commissioned by Kantata)
    type: survey
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Barriers paragraph
  - ref: KANTATA-RMIPAGE-2026
    title: Ready for AI Resource Management? Survey Says... Not Yet (insights page for the same RMI study; page
      carries no date, date shown is the retrieval date)
    publisher: Kantata (study by Resource Management Institute)
    type: survey
    url: https://www.kantata.com/resource/resource-management-in-the-age-of-ai
    date: '2026-10-19'
    access: full
    locator: Section "The real AI ask"
  - ref: FISHERPHILLIPS-EIGHTFOLD-2026
    title: 'Job Applicants Sue AI Screening Company for FCRA Violations: 5 Key Takeaways for Employers'
    publisher: Fisher Phillips LLP
    type: firm
    url: https://www.fisherphillips.com/en/news-insights/job-applicants-sue-ai-screening-company-for-fcra-violations.html
    date: '2026-01-26'
    access: full
    locator: Opening paragraphs
  last_reviewed: '2026-10-19'
  notes: The "40% happy with skills tracking" figure comes from a 2023 RMI report as summarised in a search result
    and is not used as an outcome. Evidence for automated CV-to-profile building (Ework Verama) is search-only and
    not cited. Function set to people-hr because skills data sits with HR/talent systems in many firms; the use
    feeds service-delivery staffing.
- id: professional-services-staffing-resourcing-15
  title: One matching view across employees, subcontractors, candidates and partner consultants
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
  problem: Many systems match only internal employees, while firms use subcontractors and partners to fill gaps.
    SPI reports subcontractor contributions to revenue at 10.4% in 2025 (DELTEK-SPIBENCH-2026).
  solution: Cinode matches across employees, subcontractors, candidates and partner consultants in one view, lets
    candidates be booked without first converting them, and can post unfilled roles to partners (CINODE-2026). Kantata
    lets firms compare internal and external resources side by side on skills, availability and margin impact (KANTATA-FORECAST-2026)
    and add external roles, rates and calendars (KANTATA-RM-2026).
  outcomes:
  - lever: capacity
    description: None published.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: CINODE-2026
  prerequisites:
  - External resources held as profiles with cost rates and availability (KANTATA-RM-2026)
  risks_and_guardrails:
  - Not described in the sources
  human_checkpoints:
  - Staffer chooses and books (CINODE-2026)
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: CINODE-2026
    title: 'The entire matching flow in Cinode: From email to booked consultant with AI'
    publisher: Cinode
    type: vendor
    url: https://cinode.com/en/blog/cinode-en/the-entire-matching-flow-in-cinode-from-email-to-booked-consultant-with-ai/
    date: '2026-05-13'
    access: full
    locator: Step 4, match your entire capacity
  - ref: KANTATA-FORECAST-2026
    title: Resource Forecasting and Staffing (product page; page carries no publication date, date shown is the
      retrieval date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/solutions/resource-forecasting-and-staffing
    date: '2026-10-19'
    access: full
    locator: '"Candidate Assignments" entry'
  - ref: KANTATA-RM-2026
    title: Resource Management, Scheduling and Forecasting (product page; page carries no publication date, date
      shown is the retrieval date)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/psa/resource-management-software
    date: '2026-10-19'
    access: full
    locator: Section "Managing your talent network"
  - ref: DELTEK-SPIBENCH-2026
    title: '2026 PSO Benchmarks: What We Learned and What is Next from the SPI Maturity Benchmark Report (Deltek
      article reporting the SPI Research benchmark; Deltek sponsors the report)'
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/resources/articles/professional-services-benchmarks/
    date: '2026-07-30'
    access: full
    locator: Section 3, Talent Dynamics
  last_reviewed: '2026-10-19'
  notes: Product descriptions only. The subcontractor share is context (percentage of revenue contributed by subcontractors,
    across the SPI sample), not evidence of the use case.
- id: professional-services-staffing-resourcing-16
  title: 'Employee-facing project marketplace: staff see and apply for best-fit projects'
  archetype: professional-services
  module: staffing-resourcing
  function: people-hr
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Resource decisions rest on a few people's memory, and junior staff miss stretch opportunities because
    nobody looked beyond the usual names (PROJECTWORKS-2026).
  solution: Projects are added to an internal growth hub where employees can apply for best-fit projects, as Deutsche
    Telekom plans (EIGHTFOLD-DT-2025). Projectworks describes development goals as a searchable field next to skills
    and availability so staffing with growth in mind becomes routine (PROJECTWORKS-2026).
  outcomes:
  - lever: experience
    description: None published. Deutsche Telekom expects projects to become a more frequent and flexible growth
      opportunity than a new full-time role.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: EIGHTFOLD-DT-2025
  prerequisites:
  - An internal opportunity marketplace and skills data (EIGHTFOLD-DT-2025)
  risks_and_guardrails:
  - Annex III of the EU AI Act lists AI used to allocate tasks based on individual behaviour or personal traits
    or characteristics as high-risk; whether a given staffing tool falls in scope needs legal review (AIACT-ANNEX3-2024);
    an unresolved January 2026 class action targets applicant scoring by a skills platform (FISHERPHILLIPS-EIGHTFOLD-2026)
  human_checkpoints:
  - Resource manager and project lead still approve staffing; not detailed (EIGHTFOLD-DT-2025)
  role_evolution: Employees take a more active role in finding assignments; managers see candidates they would not
    have thought of (PROJECTWORKS-2026).
  evidence_grade: C
  sources:
  - ref: EIGHTFOLD-DT-2025
    title: Deutsche Telekom seizes opportunity to apply AI to project staffing with Eightfold Resource Management
      (vendor customer story; the PDF is undated, 2025-03 is its file creation date)
    publisher: Eightfold AI
    type: vendor
    url: https://eightfold.ai/wp-content/uploads/deutsche-telekom-seizes-opportunity-ai-project-staffing-eightfold-resource-management.pdf
    date: 2025-03
    access: full
    locator: Results page, "More growth opportunities for employees"
  - ref: PROJECTWORKS-2026
    title: How AI Is Changing Resource Planning for Consulting Firms
    publisher: Projectworks
    type: vendor
    url: https://www.projectworks.com/blog/how-ai-changes-resource-planning
    date: '2026-06-25'
    access: full
    locator: Section on finding people for a role
  - ref: AIACT-ANNEX3-2024
    title: 'Annex III: High-Risk AI Systems Referred to in Article 6(2) (text of Regulation (EU) 2024/1689, as mirrored
      on artificialintelligenceact.eu)'
    publisher: European Union (text mirrored by Future of Life Institute)
    type: regulator
    url: https://artificialintelligenceact.eu/annex/3/
    date: '2024-06-13'
    access: full
    locator: Point 4(b)
  - ref: FISHERPHILLIPS-EIGHTFOLD-2026
    title: 'Job Applicants Sue AI Screening Company for FCRA Violations: 5 Key Takeaways for Employers'
    publisher: Fisher Phillips LLP
    type: firm
    url: https://www.fisherphillips.com/en/news-insights/job-applicants-sue-ai-screening-company-for-fcra-violations.html
    date: '2026-01-26'
    access: full
    locator: Opening paragraphs
  last_reviewed: '2026-10-19'
  notes: Overlaps talent-learning (development). Kept here because it changes how work is allocated.
- id: professional-services-staffing-resourcing-17
  title: Algorithmic allocation of cases to analysts replacing manager assignment (randomised trial in a government
    agency)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - transaction-processing
  pattern: other
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: Assigning cases to analysts is a matching problem between case complexity and worker skill. Managers
    use soft information about who fits which case, which is hard to put in data (IPA-PERU-2026).
  solution: Peru's environmental enforcement agency (OEFA) tested replacing manager assignment with lists produced
    by a linear-optimisation (knapsack) algorithm that selects and orders cases given analyst capacity and expected
    stage times. Not machine learning; included as the one randomised test of automated work allocation found (IPA-PERU-2026).
  outcomes:
  - lever: speed
    description: Analysts given algorithm-selected case lists were about 5 percentage points less likely to conclude
      a case on time than analysts whose cases managers assigned; the control rate was about 40%.
    figure: minus 5 percentage points (control about 40%)
    measures: Share of cases concluded on time (timely case completion), across 1,405 enforcement cases handled
      by 95 analysts in eight sectors, algorithm assignment versus manager assignment
    provenance: independent
    source_ref: IPA-PERU-2026
  - lever: quality
    description: Fines, appeal rates and appeal outcomes were statistically indistinguishable across groups.
    figure: no difference found
    measures: 'Enforcement quality proxies: fines assigned, probability of appeal and appeal outcomes, same sample'
    provenance: independent
    source_ref: IPA-PERU-2026
  - lever: speed
    description: Suggested (non-binding) completion dates raised timely completion by about 4 percentage points,
      mostly where managers still chose the cases.
    figure: plus 4 percentage points
    measures: Share of cases completed on time, comparing cases shown a suggested completion date with those not
      shown one, same sample
    provenance: independent
    source_ref: IPA-PERU-2026
  prerequisites:
  - Capacity parameters per analyst and case-level complexity and expected processing times (IPA-PERU-2026)
  risks_and_guardrails:
  - The authors say the result does not speak to algorithmic support with manager override, which may do differently
    (IPA-PERU-2026)
  - Algorithm produced more equal workloads and may improve fairness perceptions, but removed manager knowledge
    of worker-case fit (IPA-PERU-2026)
  human_checkpoints:
  - 'None in the treatment arm: the algorithm replaced manager selection. The authors point to hybrid designs (IPA-PERU-2026).'
  role_evolution: Manager discretion in matching cases to analysts proved valuable in this setting; the paper recommends
    keeping it with light-touch process support (IPA-PERU-2026).
  evidence_grade: B
  sources:
  - ref: IPA-PERU-2026
    title: 'Automated Assignment and Bureaucrat Productivity: Evidence from a Field Experiment in Peru (working
      paper, Ferreira and Cermeno Leon)'
    publisher: Innovations for Poverty Action / Southern Methodist University
    type: academic
    url: https://poverty-action.org/sites/default/files/2026-07/main_assignment_enforcement_peru_2025.pdf
    date: '2026-06-11'
    access: full
    locator: Abstract (page 1) and introduction (pages 2-4)
  last_reviewed: '2026-10-19'
  notes: 'Grade capped at B: the measurement comes from a government agency''s casework, not a professional-services
    firm, and the algorithm is optimisation, not AI in the generative sense. Working paper (pre-registered), not
    yet peer reviewed as far as the source shows. The one independent measurement of automated work allocation found;
    it points to keeping people in the matching step.'
```

## 3. Module notes

### Processes and key steps (work types)

1. **Demand capture:** turning a signed or likely deal, SOW or client request into roles, skills, dates and load (coordination-scheduling; document-production when read from emails and attachments). See use cases 07, 09.
2. **Demand and capacity forecasting:** pipeline-weighted view of where demand will exceed supply by role and skill (data-reporting). Use cases 07, 06.
3. **Skills inventory:** profiles, certifications, project history, development goals (data-reporting). Use case 14.
4. **Matching and booking:** shortlist, check availability and cost, negotiate with project leads, book tentatively then firmly (coordination-scheduling, expert-judgment). Use cases 01, 02, 03, 04, 08, 11, 15.
5. **Reallocation and cover:** replace people on work in flight (coordination-scheduling). Use case 05.
6. **Bench and utilisation management:** place unassigned staff, monitor over- and under-allocation (data-reporting, coordination-scheduling). Use cases 06, 13.
7. **Capacity supply decisions:** hire, contract or subcontract (coordination-scheduling). Use cases 07, 15.
8. **Reporting to leadership:** utilisation, forecast and outcome views (data-reporting). Use cases 12, 13.

### Common pain points

- **Spreadsheets and memory.** 71% of organisations use spreadsheets for resource processes such as skills tracking, forecasting and workload planning, per RMI Research as quoted on a Kantata page (KANTATA-FORECAST-2026). Projectworks describes staffing as dependent on one or two people who hold the map of who is free and who is good at what (PROJECTWORKS-2026).
- **Familiarity and recency bias.** The same people are tapped repeatedly and qualified people elsewhere are missed (PROJECTWORKS-2026). Deutsche Telekom's project managers could only tap their local employee base (EIGHTFOLD-DT-2025).
- **Poor data.** 47% of RMI respondents named poor or fragmented data across skills, outcomes, demand and capacity as the biggest gap; 49% cited limited understanding of where AI applies; 41% cited technology limitations (KANTATA-RMI-2026).
- **Lost work.** More than 66% of 200 surveyed leaders turned down work due to resourcing constraints; 68% cite skill availability as a barrier, up from 45% a year earlier (KANTATA-STATE-2026).
- **Low strategic standing.** 72% of RMI respondents say the function is primarily or solely operational (KANTATA-RMI-2026).
- **Distrust of recommendations (older evidence).** At Infosys, delivery managers often rejected matches from the talent team and held on to staff for their own projects, which was the stated reason for building an AI-based allocation system in 2017 (KELLOGG-INFOSYS-2022; case summary only, no outcomes reported).

### Metrics and benchmarks

| Metric | Value | What it measures, in the source's terms | Source |
|---|---|---|---|
| Billable utilisation 2025 | 66.4% (68.9% in 2024; 73.2% high in 2021; 75% treated as optimal) | Average billable utilisation across the 2026 SPI Professional Services Maturity Benchmark (over 500 firms, 245,000 employees); Level 5 (Optimized) firms exceed 80% | DELTEK-SPIBENCH-2026; DELTEK-SPIKPI-2026 (survey run by SPI, published by Deltek, its sponsor) |
| Revenue per billable consultant | $210K in 2025 (up 6% from $199K) | Same benchmark | DELTEK-SPIBENCH-2026 |
| Attrition; headcount growth; subcontractor share | 11.3%; 2.8%; 10.4% of revenue | Same benchmark, 2025 | DELTEK-SPIBENCH-2026 |
| Share of projects using generative AI | 27.1% in 2025, up from 19.3% | Share of projects using generative AI, same benchmark | DELTEK-SPIBENCH-2026 |
| A&E firms: utilisation; staff growth; turnover | Utilisation just under 60%; 1.2%; above 13% | Deltek Clarity A&E study (47th edition) findings as stated in the press release | DELTEK-CLARITY-2026 |
| A&E firms: AI adoption and benefit | 70% adoption (53% prior year); 38% report measurable positive business impact | Respondents to the same study | DELTEK-CLARITY-2026 |
| Work turned down for lack of resources | More than 66% | Share of 200 surveyed professional-services leaders (Censuswide for Kantata) | KANTATA-STATE-2026 |
| AI users reporting better forecast accuracy or utilisation | 52% | Among organisations using AI to optimise essential processes, those reporting improved forecast accuracy or utilisation (survey of 200 leaders, Kantata-sponsored) | KANTATA-STATE-2026 |
| Hybrid team readiness | 52.7% not equipped; 28.4% slightly; 4% well equipped | Share of 44 surveyed organisations (RMI, commissioned by Kantata) | KANTATA-RMI-2026 |
| Outcome data in staffing | 7.3% easily accessible and routinely used | Share of the same 44 organisations | KANTATA-RMI-2026 |
| Staffing maturity | 39% traditional staffing; 30% exploring; 31% beyond experimentation | Share of the same 44 organisations | KANTATA-RMI-2026 |
| AI agents in the assignable workforce | 11% implementing pilots; 57% on roadmap; 32% not on roadmap | Share of the same 44 organisations | KANTATA-RMIPAGE-2026 |
| Resource managers using AI | About one in ten using; nearly half considering | Runn's own "Resource Management Unfiltered" survey; sample size not stated on the page | RUNN-2025 |
| Automated versus manager case assignment | About minus 5 percentage points on-time completion (control about 40%) | Cases concluded on time; 1,405 cases, 95 analysts; randomised trial | IPA-PERU-2026 |
| Bench rule (non-AI) | 225 billed days in 12 months, so about 35 days of permitted bench | TCS internal rule as reported; non-billable resources estimated at 8-10% of payroll in the article | CXODP-TCS-2025 |

Vendor outcome claims (no method, sample or baseline given): up to 10 hours per month returned to resource managers (CPAPA-CERTINIA-2026); 40% improvement in resource planning accuracy (KANTATA-AGENT-2026); 50%+ faster staffing decisions, shown as an unexplained headline figure on Certinia's page (CERTINIA-VEDA-2026, `data-count` 50 beside "faster staffing decisions"); 40% better time-to-hire and 20% better forecast accuracy (DELTEK-POLARIS-2026).

### Guardrails and regulatory points

- **EU AI Act, Annex III point 4(b).** High-risk list includes AI used to decide terms of work relationships, promotion or termination, to allocate tasks based on individual behaviour or personal traits or characteristics, or to monitor and evaluate performance and behaviour (AIACT-ANNEX3-2024). The Commission states Annex III obligations apply from 2 December 2027 after the AI Omnibus, which it says entered into force on 27 July 2026 (EC-AIACT-2026). Whether a skills-and-availability matcher falls in scope is a legal question these sources do not settle.
- **Skills inference litigation.** A proposed class action filed 20 January 2026 alleges Eightfold's AI scoring of job applicants created consumer reports without the safeguards of the US Fair Credit Reporting Act. It concerns hiring, is unresolved, and no ruling was found (FISHERPHILLIPS-EIGHTFOLD-2026).
- **Advisory design.** Wolters Kluwer's staff recommendations are advisory, show a justification view and let firms re-weight criteria (WK-CCHSTAFF-2026). Projectworks says today's best tools advise and do not change records (PROJECTWORKS-2026). Certinia says agents act within permissions, approval thresholds and auditability set by the firm (CERTINIA-VEDA-2026).
- **Accountability for agent capacity.** Planview frames the gap as not knowing whether resources are allocated to the right work and who is accountable (SDTIMES-PLANVIEW-2026). ERP Today says the practical test is which agent actions are autonomous, which need approval, how AI work is costed and how decisions are audited (ERPTODAY-KANTATA-2026).
- **Data trust.** Only 12% of leaders fully trust their systems data, 88% trust AI outputs enough to use them in operational decisions and 89% spend significant time verifying them (KANTATA-STATE-2026; Kantata-sponsored, 200 leaders).

### Frontier signals (dated)

- 2026-01-08: Kantata/Censuswide survey: 87% plan to use AI agents as part of their workforce; 90% say systems will need to attribute work, cost and value across humans and agents (KANTATA-STATE-2026).
- 2026-01-16: Kantata's product strategy chief predicts AI agents become billable team members whose value is "planned, allocated, measured" like capacity (KANTATA-FORBES-2026; vendor executive post).
- 2026-04-09: RMI/Kantata study: respondents want skills intelligence, forecasting accuracy and proof of delivery impact to matter as much as capacity and utilisation (KANTATA-RMI-2026).
- 2026-04-15: Certinia launches Veda with 10 packaged agents in beta, including resourcing, and 64 intelligent actions (DIGINOMICA-CERTINIA-2026). 2026-09-09: 14 more agents and 135 intelligent actions, with a stated aim of more than 40 agents and 300 actions (CONSTELLATION-CERTINIA-2026).
- 2026-05-01: McKinsey reported to plan agent support for choosing client teams (BLOOMBERGLAW-MCKINSEY-2026).
- 2026-05-04: Planview announces Agent Resource Management, with availability stated as beginning Fall 2026 (SDTIMES-PLANVIEW-2026).
- 2026-06-16: Kantata launches Expertise Agent, a "superagent" (ERPTODAY-KANTATA-2026).
- Scheduled: Kantata Converge, London, 2026-11-17, with customer speakers from Hitachi Vantara, Lumanity, Hippo Digital, Anthesis and Scott Logic (KANTATA-CONVERGE-2026). A Technology and Services World fireside chat on 2026-10-20 between Basware and Kantata is titled "Congratulations, You Hired an AI Agent! Now Who's Managing Its Margin?" (KANTATA-BASWARE-2026). Both are scheduled events and support no grade.

### Workforce and role effects

- McKinsey says agents will supplement professional-development staff, not replace them (BLOOMBERGLAW-MCKINSEY-2026).
- RMI expects resource management to shift from filling hours to team composition, delivery risk and delivery economics if outcome-based pricing spreads; 1 in 2 respondents are unsure their firm will adopt it (KANTATA-RMI-2026).
- Certinia reports time savings for resource managers and project managers (10 and 20 hours a month, vendor claim) and argues hybrid teams remove the limit that firms can only bid on what humans can deliver (DIGINOMICA-CERTINIA-2026; CPAPA-CERTINIA-2026).
- Projectworks says junior consultants miss stretch opportunities when staffing runs on familiarity, and that development goals can become a searchable field (PROJECTWORKS-2026).
- Basware reports customer success managers who spent four to five hours a day researching before calls now spend that time on calls; this is the executive's account, in a vendor release, and is about customer success, not staffing (KANTATA-BASWARE-2026).

### Objections and concerns raised

- **Context and judgment.** Client dynamics, internal politics and whether two people work well together are real staffing inputs no model captures yet (PROJECTWORKS-2026). In the Peruvian trial, managers matched complex cases to experienced analysts, a link the algorithm broke (IPA-PERU-2026).
- **Speed without accuracy.** Kantata's CEO warns of "fast, mediocre decisions" when generic AI lacks business context (KANTATA-SUPERAGENT-2026).
- **Autonomy overclaimed.** diginomica says Certinia may be overdoing talk of autonomous operation because humans must still verify recommended actions (DIGINOMICA-CERTINIA-2026).
- **Silos.** Kantata says firms are adding point agents that do not see each other's decisions, so a staffing change that touches timelines, revenue recognition and capacity is not seen in whole (KANTATA-SUPERAGENT-2026; vendor argument for its own product).
- **Data and change management.** People must trust the system enough to act on it, and that takes time (PROJECTWORKS-2026).

### Interview probes for an advisor

1. When a role opens, how do you find candidates today, and what share of staffing decisions start from a person you already know rather than a search? What would you want a recommendation to show before you trusted it?
2. Which staffing inputs are not in any system (client chemistry, development intentions, partner preferences, personal circumstances)? How would those get into a recommendation, or do they stay with you?
3. If an agent proposed a team including AI agents, who is accountable for the outcome, and where is agent cost recorded? Do you plan and book agents the way you book people?
4. How current is your skills data, who maintains it, and what would staff and works councils say about inferring skills from their work history?
5. What outcome data (margin, client result, rework) is available to you at staffing time, and who owns the link between who delivered and how it went?

## 4. Routed to other modules

- **billing-collections:** automated or conversational time capture feeding utilisation actuals (CERTINIA-VEDA-2026, "Make time capture a non-issue"; KANTATA-SUPERAGENT-2026, calendar-based timesheet completion; DELTEK-DELA-2026, agents that automate timesheet entry).
- **delivery-management:** project health monitoring, PMO and project-manager agents, sales-to-delivery handoff and role-specific briefs for new team members (CERTINIA-VEDA-2026; KANTATA-AGENT-2026; SDTIMES-PLANVIEW-2026 for PM and backlog agents).
- **talent-learning:** Aderant's talent evaluation agent that aggregates matter-level feedback into structured evaluations (LEGALIT-ADERANT-2026); manager skills for hybrid teams (KANTATA-RMI-2026); stretch assignments for juniors (PROJECTWORKS-2026).
- **scoping-pricing:** estimate creation and SOW drafting agents (CERTINIA-VEDA-2026); outcome-based pricing effects on staffing (KANTATA-RMI-2026).
- **pursuit-proposals:** Kantata Sales Accelerator planned to draft proposals with case studies, risks and human-AI resource mixes (KANTATA-ENGINE-2025); tailored CV and proposal generation from profile data (CINODE-2026).
- **knowledge-management:** capturing expert judgment and institutional memory (KANTATA-SUPERAGENT-2026; KANTATA-ENGINE-2025).
- **firm-finance:** Certinia's claim that a 1% utilisation gain translates to a 1.5% EBITDA improvement is a vendor statement (CPAPA-CERTINIA-2026); costing agents and compute spend (SDTIMES-PLANVIEW-2026).

## 5. Sources

Access: `full` means opened and read; the Bloomberg Law page was paywalled after its opening paragraphs, and only those were read. `search-only` entries were seen only in search results and support no outcome and no grade. Pages with no publication date show the retrieval date (2026-10-19) and say so in the title. The Deutsche Telekom PDF is undated; 2025-03 is its file creation date.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| AIACT-ANNEX3-2024 | Annex III: High-Risk AI Systems Referred to in Article 6(2) (text of Regulation (EU) 2024/1689, as mirrored on artificialintelligenceact.eu) | European Union (text mirrored by Future of Life Institute) | regulator | https://artificialintelligenceact.eu/annex/3/ | 2024-06-13 | full |
| BLOOMBERGLAW-MCKINSEY-2026 | McKinsey Plans to Use AI Agents to Help Select Client Teams (paywalled; only the opening paragraphs were readable) | Bloomberg Law | press | https://news.bloomberglaw.com/financial-accounting/mckinsey-plans-to-use-ai-agents-to-help-select-client-teams | 2026-05-01 | full |
| CERTINIA-VEDA-2026 | Veda AI: System of Action for Professional Services (product page; page carries no publication date, date shown is the retrieval date) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 | full |
| CINODE-2026 | The entire matching flow in Cinode: From email to booked consultant with AI | Cinode | vendor | https://cinode.com/en/blog/cinode-en/the-entire-matching-flow-in-cinode-from-email-to-booked-consultant-with-ai/ | 2026-05-13 | full |
| CONSTELLATION-CERTINIA-2026 | Certinia launches System of Action, scales Veda AI agents, intelligent actions | Constellation Research | press | https://www.constellationr.com/insights/news/certinia-launches-system-action-scales-veda-ai-agents-intelligent-actions | 2026-09-09 | full |
| CPAPA-CERTINIA-2026 | Certinia Unveils Veda, an AI Operations Engine for Professional Services | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/15/certinia-unveils-veda-an-ai-operations-engine-for-professional-services/181702/ | 2026-04-15 | full |
| CXODP-TCS-2025 | TCS Rolls Out Strict Talent Deployment Policy Amid AI Push and Cost Pressures | CXO Digitalpulse | press | https://www.cxodigitalpulse.com/tcs-rolls-out-strict-talent-deployment-policy-amid-ai-push-and-cost-pressures/ | 2025-06-23 | full |
| DELTEK-CLARITY-2026 | The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures for Project-Based Businesses (press release) | Deltek | vendor | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| DELTEK-DELA-2026 | Dela, the Deltek AI orchestrator (product page; page carries no publication date, date shown is the retrieval date) | Deltek | vendor | https://www.deltek.com/en/products/platform/dela/ | 2026-10-19 | full |
| DELTEK-POLARIS-2026 | Deltek Polaris (product page; page carries no publication date, date shown is the retrieval date) | Deltek | vendor | https://www.deltek.com/en/products/polaris/ | 2026-10-19 | full |
| DELTEK-SPIBENCH-2026 | 2026 PSO Benchmarks: What We Learned and What is Next from the SPI Maturity Benchmark Report (Deltek article reporting the SPI Research benchmark; Deltek sponsors the report) | Deltek | vendor | https://www.deltek.com/resources/articles/professional-services-benchmarks/ | 2026-07-30 | full |
| DELTEK-SPIKPI-2026 | 5 KPIs from the SPI Professional Services Maturity Benchmark Report Every PSO Must Track for Sustainable Growth | Deltek | vendor | https://www.deltek.com/en/resources/articles/5-kpis-from-the-spi-professional-services-maturity-benchmark-report-every-pso-must-track-for-sustainable-growth | 2026-07-15 | full |
| DIGINOMICA-CERTINIA-2026 | Certinia unveils Veda, its AI engine for Professional Services Automation | diginomica | press | https://diginomica.com/certinia-unveils-veda-ai-engine-professional-services-automation | 2026-04-15 | full |
| EC-AIACT-2026 | AI Act: regulatory framework page (timelines after the AI Omnibus) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-19 | full |
| EIGHTFOLD-DT-2025 | Deutsche Telekom seizes opportunity to apply AI to project staffing with Eightfold Resource Management (vendor customer story; the PDF is undated, 2025-03 is its file creation date) | Eightfold AI | vendor | https://eightfold.ai/wp-content/uploads/deutsche-telekom-seizes-opportunity-ai-project-staffing-eightfold-resource-management.pdf | 2025-03 | full |
| ERPTODAY-KANTATA-2026 | Kantata's Expertise Agent Targets the Professional Services Delivery Crunch (ERP Today article, republished on kantata.com; date from page metadata) | ERP Today | press | https://www.kantata.com/blog/article/erp-today-kantatas-expertise-agent-targets-the-professional-services-delivery-crunch | 2026-06-19 | full |
| EY-RESMGR-2026 | Resource Manager (Supervising Associate) - AI and Data, Technology Consulting, Sydney (posting; page expired, seen only in a search result that dated it 18 March 2026) | EY | job-posting | https://careers.ey.com/ey/job/Sydney-Resource-Manager-%28Supervising-Associate%29-AI-and-Data%2C-Technology-Consulting-NSW-2000/1374884033 | 2026-03-18 | search-only |
| FISHERPHILLIPS-EIGHTFOLD-2026 | Job Applicants Sue AI Screening Company for FCRA Violations: 5 Key Takeaways for Employers | Fisher Phillips LLP | firm | https://www.fisherphillips.com/en/news-insights/job-applicants-sue-ai-screening-company-for-fcra-violations.html | 2026-01-26 | full |
| IPA-PERU-2026 | Automated Assignment and Bureaucrat Productivity: Evidence from a Field Experiment in Peru (working paper, Ferreira and Cermeno Leon) | Innovations for Poverty Action / Southern Methodist University | academic | https://poverty-action.org/sites/default/files/2026-07/main_assignment_enforcement_peru_2025.pdf | 2026-06-11 | full |
| KANTATA-AGENT-2026 | Expertise Agent and Workflows (product page; page carries no publication date, date shown is the retrieval date) | Kantata | vendor | https://www.kantata.com/ai/expertise-agent-and-workflows | 2026-10-19 | full |
| KANTATA-BASWARE-2026 | Kantata takes Basware from AI experimentation to results (press release) | Kantata | vendor | https://www.kantata.com/blog/article/kantata-takes-basware-from-ai-experimentation-to-results | 2026-10-13 | full |
| KANTATA-CONVERGE-2026 | Kantata Converge: Where AI Meets Expertise (event announcement; event scheduled for 2026-11-17) | Kantata | conference | https://www.kantata.com/blog/article/kantata-converge-where-ai-meets-expertise | 2026-10-08 | full |
| KANTATA-ENGINE-2025 | Kantata Unveils the Kantata Expertise Engine (press release) | Kantata | vendor | https://www.kantata.com/blog/article/kantata-unveils-the-kantata-expertise-engine-the-first-ai-platform-purpose-built-for-professional-services-transformation | 2025-10-09 | full |
| KANTATA-FORBES-2026 | Professional Services 2026: When AI Becomes A Billable Team Member (Forbes Technology Council post by Kantata Chief Product Strategy Officer, republished by Kantata) | Forbes Technology Council | press | https://www.kantata.com/blog/article/professional-services-2026-when-ai-becomes-a-billable-team-member | 2026-01-16 | full |
| KANTATA-FORECAST-2026 | Resource Forecasting and Staffing (product page; page carries no publication date, date shown is the retrieval date) | Kantata | vendor | https://www.kantata.com/solutions/resource-forecasting-and-staffing | 2026-10-19 | full |
| KANTATA-RESAGENT-2025 | Kantata Expands Agentic AI Capabilities with New Resourcing Agent Supercharging Professional Services Delivery (press release; BusinessWire blocked, seen in search results only) | Kantata via Business Wire | vendor | https://www.businesswire.com/news/home/20250924498182/en/Kantata-Expands-Agentic-AI-Capabilities-with-New-Resourcing-Agent-Supercharging-Professional-Services-Delivery | 2025-09-24 | search-only |
| KANTATA-RM-2026 | Resource Management, Scheduling and Forecasting (product page; page carries no publication date, date shown is the retrieval date) | Kantata | vendor | https://www.kantata.com/psa/resource-management-software | 2026-10-19 | full |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services (press release on the Resource Management Institute study 'Resource Management in the Age of AI') | Kantata (study by Resource Management Institute, commissioned by Kantata) | survey | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| KANTATA-RMIPAGE-2026 | Ready for AI Resource Management? Survey Says... Not Yet (insights page for the same RMI study; page carries no date, date shown is the retrieval date) | Kantata (study by Resource Management Institute) | survey | https://www.kantata.com/resource/resource-management-in-the-age-of-ai | 2026-10-19 | full |
| KANTATA-STATE-2026 | Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce (press release on the State of the Professional Services Industry report; Censuswide survey of 200 leaders) | Kantata | survey | https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce | 2026-01-08 | full |
| KANTATA-SUPERAGENT-2026 | More Agents Won't Fix Unpredictable Projects: Why We Built a Superagent Instead (vendor blog summarising a podcast episode) | Kantata | vendor | https://www.kantata.com/blog/article/more-agents-wont-fix-unpredictable-projects-why-we-built-a-superagent-instead | 2026-06-16 | full |
| KELLOGG-INFOSYS-2022 | Tapping into a Digital Brain: AI-Powered Talent Management at Infosys (teaching case summary) | Kellogg School of Management | academic | https://www.kellogg.northwestern.edu/academics-research/research/detail/2022/tapping-into-a-digital-brain-ai-powered-talent-management/ | 2022-07-14 | full |
| LEGALIT-ADERANT-2026 | Aderant rolls out Agent Center at Momentum as part of Stridyn platform expansion | Legal IT Insider | press | https://legaltechnology.com/aderant-rolls-out-agent-center-at-momentum-as-part-of-stridyn-platform-expansion/ | 2026-05-12 | full |
| PROJECTWORKS-2026 | How AI Is Changing Resource Planning for Consulting Firms | Projectworks | vendor | https://www.projectworks.com/blog/how-ai-changes-resource-planning | 2026-06-25 | full |
| ROCKETLANE-2026 | AI for PS Resource Allocation: 2026 Guide | Rocketlane | vendor | https://blog.rocketlane.com/blogs/ai-for-ps-resource-allocation | 2026-07-22 | full |
| RUNN-2025 | 90% of Resource Managers Still Do Not Use AI (summary of Runn Resource Management Unfiltered survey) | Runn | survey | https://www.runn.io/blog/90-percent-of-resource-managers-still-dont-use-ai | 2025-09-12 | full |
| SDTIMES-PLANVIEW-2026 | Planview Launches Agent Resource Management, Redefining Portfolio Resource Management for the AI Era | SD Times | press | https://sdtimes.com/agentic-ai/planview-launches-agent-resource-management-redefining-portfolio-resource-management-for-the-ai-era/ | 2026-05-04 | full |
| VV-RESOURCEMGR-2026 | Resource Manager (remote; employer not named; aggregator listing reviewed 2026-06-09, now expired) | Virtual Vocations | job-posting | https://www.virtualvocations.com/job/resource-manager-3090201-i.html | 2026-06-09 | full |
| WK-CCHSTAFF-2026 | The staffing challenge most workflow systems don't solve (CCH Axcess Workflow AI-powered staff recommendations) | Wolters Kluwer Tax and Accounting | vendor | https://www.wolterskluwer.com/en/expert-insights/the-staffing-challenge-most-workflow-systems-dont-solve | 2026-08-12 | full |

## 6. Gaps

- **Named firm deployments with results.** None found beyond Basware (no staffing figure) and Deutsche Telekom (a planned pilot). The McKinsey item is a plan; the Bloomberg Law article was paywalled after its opening paragraphs. I did not find a Big Four, Accenture, BCG, Bain or Deloitte public description of AI staffing.
- **Legal.** No law-firm or in-house legal staffing deployment, case study or product was found. Aderant's agents (collections, appeals, talent evaluation) do not assign people to matters. Search results on law-firm staffing returned only surveys on junior hiring and generic matter-management pages.
- **Independent measurement.** Only the Peruvian trial and the SPI/Deltek benchmarks are independent of the tool vendors, and neither measures an AI staffing tool in a firm. No override rates, acceptance rates or parallel-run results were published by any source. Searches for published override or acceptance rates found none.
- **Job postings.** Real-use signals from postings were thin. An EY Sydney resource-manager posting (AI and Data, March 2026) had expired and appears search-only. One aggregator listing (employer unnamed, Big 4-style resourcing team, June 2026) asks only for AI tools to enhance reporting workflows (VV-RESOURCEMGR-2026). Other listings found through search (AHEAD, Egen, Unit4) had been removed.
- **Blocked or unavailable.** Business Wire (Kantata Resourcing Agent release of September 2025; IDC MarketScape for AI-enabled PSA, January 2026) returned 403 and are search-only or unused. An EXL/ServiceNow resource-management story and a TeamLease Digital bench-ratio report returned errors or 403 and were not used. Kantata's State of the Professional Services Industry full report and the RMI report body are gated; only press releases and landing pages were read, so the question wording is unknown.
- **Product claims not checked.** Eightfold's Resource Management module beyond the Deutsche Telekom story, Gloat and Cassidy vendor pages, Enterprise DNA's claim of 22 minutes versus four hours, Lyzr's targets, Rocketlane's Nitro agent beyond its own guide, Float, Productive and Resource Guru were not opened or not used.
- **Survey quality.** The RMI study has 44 organisations and was commissioned by a vendor; the Kantata survey has 200 leaders and was sponsored by the vendor; the Runn survey gives no sample size. SPI and Deltek reports are survey-based benchmarks sponsored by a software vendor.
- **Not covered.** Practice-specific staffing rules (audit rotation, independence-driven team selection, partner succession) belong to the assurance and tax archetypes. Conference programmes for CLOC, AICPA ENGAGE and the Resource Management Global Symposium were not retrieved.
