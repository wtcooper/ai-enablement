# Staffing and resourcing: governance and evidence (professional services)

Archetype: professional-services. Module: staffing-resourcing. Angle: governance (what constrains and measures the work). Prepared 2026-10-19. Public sources only. Method: curl, pdftotext and a text mirror for page dates; seven web searches. Quotations are under 25 words.

## 1. Summary

- **What the evidence is.** 38 sources are listed; 37 were opened and read and one (the ISQM 1 resource requirement) is search-only. By type: 10 regulator, 3 professional-body, 1 standard-setter (search-only), 6 academic, 5 survey, 5 vendor, 7 press and 1 conference coverage. There are 13 use cases: 0 at grade A, 4 at B (two of them capped because the measured process is adjacent), 4 at C and 5 at D (ideas, labelled). No grade A exists because no named professional services organization publishes a measured result for AI in staffing.
- **Task allocation is now named in law.** EU AI Act Annex III point 4(b) lists AI used to allocate tasks based on individual behaviour or personal traits or characteristics, and to monitor and evaluate worker performance, as high-risk (EU-AIACT-OJ-2024). Those obligations apply from 2 December 2027 after the AI Omnibus (EC-AIACT-2026). California's CCPA regulations list "allocation or assignment of work for employees" as a significant decision, with ADMT compliance due by 1 January 2027 (CPPA-CCPAREGS-2026, s.7001(ddd)(4)(B), s.7200).
- **Practitioners are not looking at it.** In the Kantata-commissioned RMI study, 4% of respondents named ethical or compliance concerns about AI in resource management as a gap, and 20% named unclear ownership of AI decisions (KANTATA-RMI-REPORT-2026, Q19). Whether a given skills-and-availability matcher falls under either rule is not settled by the texts read; each tool needs its own assessment.
- **Bar and professional-body guidance is about client work, not staffing.** ABA Formal Opinion 512, California's 2026 guidance, the SRA warning notice and the ICMCI code cover competence, supervision, confidentiality and fees. They touch staffing only indirectly: supervision duties scale with autonomy (CALBAR-GENAI-2026), California warns of bias when AI is used in employment actions (CALBAR-GENAI-2026, p. 9), and ICMCI treats uses that may materially affect employment as high-risk (ICMCI-AICODE-2026, s.1.3). Hourly-billing rules stop AI-saved hours being billed as worked (ABA-OP512-2024, p. 12).
- **The only independent quality measurement is adjacent and cautionary.** A randomised trial of automated case-to-analyst assignment at Peru's environmental enforcement agency found about 5 points lower on-time completion than manager assignment (control about 40%), with no difference in fines or appeals; suggested completion dates added about 4 points (FERREIRA-PERU-2026). It is a working paper on public-sector enforcement, not professional services. No override, acceptance or accuracy rate for AI staffing recommendations was found anywhere.
- **Benchmarks show the problem, not the fix.** Average billable utilization fell to 66.4% in 2025, the lowest in SPI's history (DELTEK-SPIBENCH-2026); A&E utilization is just under 60% (DELTEK-CLARITY-2026); 55% of firms in a Dayshape survey miss, delay or turn down work for capacity reasons and 39% staff by availability rather than best fit (DAYSHAPE-ONREC-2026). All three are vendor-published.
- **Demand has not fallen.** Citi data quoted by Bloomberg Law shows demand for Big Law hours up 4.2% in H1 2026 against about 1.5% normal growth (BLOOMBERGLAW-BILLABLE-2026), so capacity plans cannot assume AI savings have reduced workload.
- **Hybrid human-agent staffing is a stated intent without practice.** 0% of respondents have agents operationalised as assignable resources, 10.7% are piloting, and only 4% feel well equipped to manage hybrid teams (KANTATA-RMI-REPORT-2026, Q8, Q9).
- **Enforcement is thin.** The New York State Comptroller found New York City's Local Law 144 enforcement ineffective (OSC-LL144-2025). Colorado's AI act was stayed in April 2026 and then repealed and reenacted on 14 May 2026 (NATLAW-AIHIRING-2026; COLORADO-SB26189-2026). No US federal AI employment statute exists (NATLAW-AIHIRING-2026).

## 2. Use cases

```yaml
- id: professional-services-staffing-resourcing-01
  title: Skills, availability and cost shortlist for a resource request, with the resource manager making the call
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Resource managers search skills, schedules and cost data by hand for each request. A vendor-sponsored
    survey of 400 UK and US leaders found 39% regularly staff projects by availability rather than best-fit skills
    (DAYSHAPE-ONREC-2026, Key figures).
  solution: 'A PSA-embedded agent compiles consultant background and history, schedule conflicts and availability,
    and produces a candidate shortlist; the resource manager chooses (CERTINIA-VEDA-2026, Plan-stage agent list
    and Icon Cloud Consulting quote). Pattern is other: a matching step, not an agent that owns an outcome.'
  outcomes:
  - lever: speed
    description: Vendor headline counter on its AI page, labelled 'faster staffing decisions'; baseline, sample
      and period are not stated. Value read from the page markup (50, shown with a '+').
    figure: 50%+
    measures: Vendor page label 'faster staffing decisions'; no numerator, denominator or baseline given
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  - lever: quality
    description: Baseline problem the tool targets, not a result of the tool
    figure: 39%
    measures: Share of surveyed firms that 'regularly staff projects by availability rather than best-fit skills'
      (Dayshape survey of 400 C-suite and senior leaders at mid-to-enterprise firms, UK and US)
    provenance: vendor-published
    source_ref: DAYSHAPE-ONREC-2026
  - lever: quality
    description: No acceptance, override or fit-quality rate for AI shortlists was found in any source read
    figure: none
    measures: n/a
    provenance: self-reported
    source_ref: n/a
  prerequisites:
  - Skills, availability and cost data held in one system; 47.1% of respondents named poor or fragmented data (skills,
    outcomes, demand, capacity) as a top gap in AI-augmented resource management (KANTATA-RMI-REPORT-2026, Q19 and
    Key Observations, pp. 4 and 21)
  - A defined rule for who may accept or change a shortlist, because the EU and California texts turn on human involvement
    (see guardrails)
  risks_and_guardrails:
  - EU AI Act Annex III point 4(b) lists AI systems intended to 'allocate tasks based on individual behaviour or
    personal traits or characteristics' among high-risk uses; obligations for Annex III systems apply from 2 December
    2027 (EU-AIACT-OJ-2024, Annex III 4(b); EC-AIACT-2026, Application timeline). The sources read do not say whether
    a skills-and-availability matcher is inside that wording, so each tool needs its own assessment.
  - California's CCPA regulations list 'allocation or assignment of work for employees' as a significant decision;
    a business using automated decisionmaking technology for one must comply by 1 January 2027 (CPPA-CCPAREGS-2026,
    s.7001(ddd)(4)(B), p. 11; s.7200(b), p. 91). The regulation defines human involvement as a reviewer who knows
    how to interpret the output, reviews it with other relevant information, and has authority to change the decision
    (s.7001(e)(1), pp. 4-5).
  - Where the user is a lawyer, California guidance says AI in connection with employment actions or screening of
    candidates may present a risk of unlawful or unethical bias, and firms should set policies to identify bias
    (CALBAR-GENAI-2026, Prohibition on Discrimination, p. 9).
  - Only 4% of respondents named ethical or compliance concerns about AI in resource management as a gap (KANTATA-RMI-REPORT-2026,
    Q19, p. 21), so these rules may not yet be on resource managers' radar.
  human_checkpoints:
  - The resource manager 'making the right call' from the candidate set (CERTINIA-VEDA-2026, Icon Cloud Consulting
    quote)
  - Whether engagement leads or the individual also confirm the assignment is not described in the sources read
  role_evolution: The Icon Cloud Consulting quote says resource managers can focus on the decision rather than hunting
    for information (CERTINIA-VEDA-2026). In the Kantata-commissioned study, 72% described resource management as
    primarily or solely operational, the baseline the role is moving from (KANTATA-RMI-2026, press release).
  evidence_grade: B
  sources:
  - ref: CERTINIA-VEDA-2026
    title: Veda AI agents for professional services (AI solutions page)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: 'AI solutions page: ''Staff with confidence'' and outcome counters; Plan-stage agent list (Resourcing,
      Work Reallocation, Shortlisting); customer quote from Icon Cloud Consulting'
  - ref: DAYSHAPE-ONREC-2026
    title: 'Professional services firms lose work as capacity planning falls behind demand (Onrec summary of Dayshape''s
      ''Professional services: Navigating a new operating era'', 400 senior leaders, UK and US)'
    publisher: Onrec
    type: press
    url: https://www.onrec.com/node/129428
    date: '2026-10-13'
    access: full
    locator: Key figures panel
  - ref: KANTATA-RMI-REPORT-2026
    title: Resource Management in the Age of AI (full survey report; 44 organizations)
    publisher: Resource Management Institute (RTM Consulting, a Belcan company) for Kantata
    type: vendor
    url: https://get.kantata.com/rs/677-LEJ-696/images/AI_in_Resource_Management_Survey.pdf
    date: 2026-04
    access: full
    locator: Key Observations p. 4; Q19 p. 21
  - ref: EU-AIACT-OJ-2024
    title: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal text
    publisher: European Parliament and Council of the European Union (EUR-Lex)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
    date: '2024-07-12'
    access: full
    locator: Annex III, point 4(b); Recital 57
  - ref: EC-AIACT-2026
    title: AI Act (regulatory framework page, incl. application timeline and AI Omnibus)
    publisher: European Commission, Shaping Europe's digital future
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: Application timeline section
  - ref: CPPA-CCPAREGS-2026
    title: California Consumer Privacy Act Regulations, effective 1/1/2026 (includes Article 11, Automated Decisionmaking
      Technology)
    publisher: California Privacy Protection Agency
    type: regulator
    url: https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf
    date: '2026-01-01'
    access: full
    locator: s.7001(e), s.7001(ddd)(4)(B), s.7200
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Prohibition on Discrimination, Harassment, and Retaliation, p. 9
  last_reviewed: '2026-10-19'
  notes: Grade B rests on one vendor-hosted customer quote that describes use, with no outcome from the customer.
    The quote calls the tool the 'Staffing Agent' while the page's agent list names Resourcing and Shortlisting
    agents; the mapping is the vendor's. The 50%+ figure is vendor-published with no basis stated and is not independent.
- id: professional-services-staffing-resourcing-02
  title: Demand and capacity forecast refined from pipeline and delivery patterns
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Firms cannot see capacity gaps early enough. 55% of firms in a Dayshape survey miss, delay or turn down
    client work because of capacity constraints, and only a small minority can forecast workforce capacity more
    than 12 months ahead (DAYSHAPE-ONREC-2026).
  solution: 'AI refines demand and capacity forecasts from pipeline and delivery patterns so that resourcing and
    hiring decisions are made earlier. This was the most-selected way respondents wanted AI to support resource
    management (KANTATA-RMI-REPORT-2026, Q16, p. 18). Pattern is other: forecasting, not agentic action.'
  outcomes:
  - lever: quality
    description: Share who report improved forecast accuracy or utilization, among organizations using AI to optimize
      essential processes; the base of that group is not stated
    figure: 52%
    measures: Respondents reporting 'improved forecast accuracy or utilization' (Kantata-sponsored survey of 200
      professional services leaders, conducted by Censuswide)
    provenance: vendor-published
    source_ref: CPAPA-KANTATASOPS-2026
  - lever: quality
    description: Leaders saying AI already improves resource-planning and allocation decisions
    figure: 76%
    measures: '''Say AI is already improving resource-planning and allocation decisions'' (Dayshape survey of 400
      senior leaders, UK and US). The article gives no count for the ''small minority'' able to forecast capacity
      beyond 12 months'
    provenance: vendor-published
    source_ref: DAYSHAPE-ONREC-2026
  - lever: capacity
    description: 'Baseline: organizations turning down work for resourcing reasons'
    figure: More than 66%
    measures: '''Professional services organizations report turning down work due to resourcing constraints'' (Kantata-sponsored
      survey of 200 leaders)'
    provenance: vendor-published
    source_ref: CPAPA-KANTATASOPS-2026
  - lever: capacity
    description: Respondents selecting forecast refinement as a desired AI support
    figure: 72.1%
    measures: Share of respondents selecting 'Refining demand and capacity forecasts based on pipeline and delivery
      patterns' (multi-select, Q16; 44 organizations)
    provenance: vendor-published
    source_ref: KANTATA-RMI-REPORT-2026
  prerequisites:
  - 'Pipeline, staffing and finance data connected: a vendor analysis of the SPI benchmark says staffing delay can
    become a revenue issue and poor forecasts a hiring issue (CERTINIA-SPIBENCH-2026)'
  - 'Trusted data: only 12% of leaders fully trust the data in their systems, down from 24% a year earlier (CPAPA-KANTATASOPS-2026)'
  risks_and_guardrails:
  - 88% say they trust AI outputs enough to use them in operational decisions, yet 89% say they spend significant
    time verifying them (CPAPA-KANTATASOPS-2026; same 200-leader survey)
  - In the Deltek Government Contracting findings, 29% named the potential for inaccurate forecasts among the top
    AI concerns (the release gives no base for this figure; adjacent population) (DELTEK-CLARITY-2026)
  - No error rate, backtest or forecast-accuracy measure for AI capacity forecasts was found in any source read
  human_checkpoints:
  - Resource and delivery leaders decide on hiring, contractor use and bids; the sources describe AI as supporting
    these decisions and none describes forecasts triggering them automatically
  role_evolution: Respondents want resource management to become more data-driven, with forecasting accuracy as
    critical as capacity and utilization (KANTATA-RMI-REPORT-2026, Executive Summary, p. 2).
  evidence_grade: C
  sources:
  - ref: DAYSHAPE-ONREC-2026
    title: 'Professional services firms lose work as capacity planning falls behind demand (Onrec summary of Dayshape''s
      ''Professional services: Navigating a new operating era'', 400 senior leaders, UK and US)'
    publisher: Onrec
    type: press
    url: https://www.onrec.com/node/129428
    date: '2026-10-13'
    access: full
    locator: Key figures; 'Capacity constraints are costing firms work'
  - ref: CPAPA-KANTATASOPS-2026
    title: 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce (Kantata State
      of the Professional Services Industry report, 200 leaders, conducted by Censuswide)
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/02/17/87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce/178201/
    date: '2026-02-17'
    access: full
    locator: Paragraphs on performance gains, resourcing and data trust
  - ref: KANTATA-RMI-REPORT-2026
    title: Resource Management in the Age of AI (full survey report; 44 organizations)
    publisher: Resource Management Institute (RTM Consulting, a Belcan company) for Kantata
    type: vendor
    url: https://get.kantata.com/rs/677-LEJ-696/images/AI_in_Resource_Management_Survey.pdf
    date: 2026-04
    access: full
    locator: Q16, p. 18; Executive Summary, p. 2
  - ref: CERTINIA-SPIBENCH-2026
    title: Analyzing the 2026 SPI Research Professional Services Maturity Benchmark Report (page shows no publication
      date; text refers to the midpoint of 2026)
    publisher: Certinia (relaying SPI Research data)
    type: vendor
    url: https://certinia.com/blog/analyzing-the-2026-spi-research-professional-services-maturity-benchmark-report/
    date: '2026'
    access: full
    locator: Section 'Profitability is stable' (connected decisions)
  - ref: DELTEK-CLARITY-2026
    title: The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity
      Pressures (47th Clarity A&E study, 896 firms; 17th Clarity Government Contracting study, 917 firms)
    publisher: Deltek
    type: survey
    url: https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/
    date: '2026-05-12'
    access: full
    locator: Key Findings, 17th Government Contracting report
  last_reviewed: '2026-10-19'
  notes: Maturity is emerging because the evidence is anonymous survey responses; no named organization describes
    its forecasting deployment. Every figure is from a vendor-sponsored or vendor-run survey.
- id: professional-services-staffing-resourcing-03
  title: Skills inferred from completed work and adjacent skills surfaced for staffing (idea)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - research-synthesis
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: 'Skills data is a blocker: 47.1% of respondents in the RMI study cite poor or fragmented data across
    skills, outcomes, demand and capacity, and ''skills intelligence'' was the second-most selected AI support wanted
    (67.7%) after forecasting (KANTATA-RMI-REPORT-2026, Key Observations, p. 4).'
  solution: 'Idea: AI infers skills from the work people have done and highlights adjacencies, keeping the skills
    inventory current without manual self-reporting. No public deployment by a named professional services firm
    was found.'
  outcomes:
  - lever: quality
    description: none published (survey of what respondents want)
    figure: 68%
    measures: Share of respondents selecting 'Enhancing skills intelligence (inferring skills from work, highlighting
      adjacencies)' (multi-select, Q16; 44 organizations)
    provenance: vendor-published
    source_ref: KANTATA-RMI-REPORT-2026
  prerequisites:
  - Work records (time entries, project roles, outcomes) linked to individuals
  - 'Skills data that is not fragmented: 47.1% named poor or fragmented skills, outcomes, demand and capacity data
    as a top gap (KANTATA-RMI-REPORT-2026, Q19, p. 21)'
  risks_and_guardrails:
  - 'Inferring attributes about people is a data-protection risk: the ICO''s audit of AI recruitment tools found
    tools inferring gender and ethnicity from names and collecting more personal information than necessary (ICO-AIRECRUIT-2024;
    adjacent, recruitment not staffing)'
  - In the EU, deployers who are employers must inform workers and their representatives before putting a high-risk
    system into use at the workplace (EU-AIACT-OJ-2024, Art. 26(7)); whether a skills inventory is high-risk is
    not settled by the sources read
  human_checkpoints:
  - Not described in any source read; a person confirming inferred skills would be a design choice, not a documented
    practice
  role_evolution: none published
  evidence_grade: D
  sources:
  - ref: KANTATA-RMI-REPORT-2026
    title: Resource Management in the Age of AI (full survey report; 44 organizations)
    publisher: Resource Management Institute (RTM Consulting, a Belcan company) for Kantata
    type: vendor
    url: https://get.kantata.com/rs/677-LEJ-696/images/AI_in_Resource_Management_Survey.pdf
    date: 2026-04
    access: full
    locator: Q16, p. 18; Q19, p. 21
  - ref: ICO-AIRECRUIT-2024
    title: ICO intervention into AI recruitment tools leads to better data protection for job seekers
    publisher: UK Information Commissioner's Office
    type: regulator
    url: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/ico-intervention-into-ai-recruitment-tools-leads-to-better-data-protection-for-job-seekers/
    date: '2024-11-06'
    access: full
    locator: '''About the audits'' section'
  - ref: EU-AIACT-OJ-2024
    title: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal text
    publisher: European Parliament and Council of the European Union (EUR-Lex)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
    date: '2024-07-12'
    access: full
    locator: Article 26(7)
  last_reviewed: '2026-10-19'
  notes: 'Grade D, labelled idea: the only evidence is a survey of what resource managers say they want.'
- id: professional-services-staffing-resourcing-04
  title: Automated case-to-analyst assignment replacing manager discretion (adjacent public-sector evidence)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Manager-led allocation of legally complex, deadline-bound cases across analysts risked unbalanced workloads
    and missed statutory deadlines (FERREIRA-PERU-2026, Introduction, p. 2).
  solution: 'Peru''s environmental enforcement agency (OEFA) introduced in 2023 a system that selects and orders
    cases for each analyst by optimisation under capacity and expected-completion-time constraints, replacing managers''
    selection. A randomised field experiment compared algorithm-assigned with manager-assigned analysts. Process
    is adjacent: public-sector enforcement, not professional services staffing.'
  outcomes:
  - lever: speed
    description: Automated assignment reduced timely case completion relative to manager assignment
    figure: about 5 percentage points lower; control-group completion about 40%
    measures: Analysts whose cases were selected by the algorithm were about 5 points less likely to conclude a
      case on time than analysts whose cases were assigned by managers; 1,405 enforcement cases, 95 analysts, eight
      sectors
    provenance: independent
    source_ref: FERREIRA-PERU-2026
  - lever: quality
    description: Enforcement quality measures did not differ
    figure: no difference
    measures: Fines, appeal rates and appeal outcomes were statistically indistinguishable across groups (same sample)
    provenance: independent
    source_ref: FERREIRA-PERU-2026
  prerequisites:
  - Agency-set capacity parameters per analyst and case-level complexity, prescription risk and expected processing
    times (FERREIRA-PERU-2026, p. 3)
  - A setting where case complexity and worker skill can be encoded; the authors say key dimensions of worker skill
    and fit are hard to observe in administrative data (p. 2)
  risks_and_guardrails:
  - The algorithm removed managers' soft information about worker-case fit; the authors report that managers use
    discretion to match complex cases to experienced analysts and that automated assignment breaks this link (abstract;
    p. 3)
  - The authors note the experiment did not test algorithmic support with managerial override, which 'may yield
    different outcomes' (p. 3), and was run under high workload and temporary staffing expansion
  - A tool of this kind would fall under the California 'allocation or assignment of work' rule if no human involvement
    meets the regulation's test (CPPA-CCPAREGS-2026, s.7001(e)(1) and (ddd)(4)(B)); EU Annex III 4(b) applies if
    allocation is based on individual behaviour or traits (EU-AIACT-OJ-2024)
  human_checkpoints:
  - None on the normal path in the automated arm by design; managers kept assignment in the control arm
  role_evolution: Manager discretion over who works which case was removed in the automated arm; the paper reports
    workloads became more equalised (compressed distribution across analysts), which it says may improve perceived
    fairness (FERREIRA-PERU-2026, pp. 3-4).
  evidence_grade: B
  sources:
  - ref: FERREIRA-PERU-2026
    title: 'Automated Assignment and Bureaucrat Productivity: Evidence from a Field Experiment in Peru (working
      paper)'
    publisher: Southern Methodist University and Innovations for Poverty Action (Ferreira, Cermeno Leon)
    type: academic
    url: https://poverty-action.org/sites/default/files/2026-07/main_assignment_enforcement_peru_2025.pdf
    date: '2026-06-11'
    access: full
    locator: Abstract; Introduction pp. 2-4
  - ref: CPPA-CCPAREGS-2026
    title: California Consumer Privacy Act Regulations, effective 1/1/2026 (includes Article 11, Automated Decisionmaking
      Technology)
    publisher: California Privacy Protection Agency
    type: regulator
    url: https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf
    date: '2026-01-01'
    access: full
    locator: s.7001(e)(1), s.7001(ddd)(4)(B)
  - ref: EU-AIACT-OJ-2024
    title: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal text
    publisher: European Parliament and Council of the European Union (EUR-Lex)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
    date: '2024-07-12'
    access: full
    locator: Annex III, point 4(b)
  last_reviewed: '2026-10-19'
  notes: 'Measurement is independent and pre-registered, but the process is case assignment in a public enforcement
    agency, so the grade is capped at B under the grade-scope rule. The paper is a working paper (11 June 2026),
    not peer reviewed. The authors argue the setting resembles legal, consulting, audit and compliance work; that
    is their claim. Partial replication in a professional services firm: none found.'
- id: professional-services-staffing-resourcing-05
  title: AI-suggested completion dates layered on manager-led assignment (adjacent public-sector evidence)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Analysts working a backlog of deadline-bound cases need cues on sequencing; managers kept the assignment
    decision but lacked a scheduling prompt (FERREIRA-PERU-2026, Introduction).
  solution: The same OEFA system displayed suggested completion dates on randomly chosen cases, leaving selection
    with managers or the algorithm. The nudge is a light-touch scheduling aid that preserves human discretion.
  outcomes:
  - lever: speed
    description: Suggested completion dates raised timely completion
    figure: about 4 percentage points higher
    measures: Cases showing suggested completion dates were about 4 points more likely to be completed on time;
      effect concentrated among manager-assigned cases (1,405 cases, 95 analysts); fines and appeals unaffected
    provenance: independent
    source_ref: FERREIRA-PERU-2026
  prerequisites:
  - Case-level expected processing times for the main procedural stages (FERREIRA-PERU-2026, p. 3)
  risks_and_guardrails:
  - The nudge did not offset the negative effect of algorithmic case selection (p. 3)
  - Effect shown for one agency and one case type; the paper does not test professional services work
  human_checkpoints:
  - Managers keep case selection in the manager-assigned arm; the dates are displayed as suggestions
  role_evolution: The authors read the result as favouring hybrid designs that keep managerial discretion (FERREIRA-PERU-2026,
    p. 4).
  evidence_grade: B
  sources:
  - ref: FERREIRA-PERU-2026
    title: 'Automated Assignment and Bureaucrat Productivity: Evidence from a Field Experiment in Peru (working
      paper)'
    publisher: Southern Methodist University and Innovations for Poverty Action (Ferreira, Cermeno Leon)
    type: academic
    url: https://poverty-action.org/sites/default/files/2026-07/main_assignment_enforcement_peru_2025.pdf
    date: '2026-06-11'
    access: full
    locator: Abstract; Introduction pp. 3-4
  last_reviewed: '2026-10-19'
  notes: 'Capped at B: independent randomised measurement, but of an adjacent process (public-sector case scheduling).
    Working paper, not peer reviewed.'
- id: professional-services-staffing-resourcing-06
  title: Re-matching and reallocating work in flight when resources shift
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
  problem: When a consultant leaves, is delayed or is pulled to other work, replacements are found by hand, leaving
    gaps and idle capacity.
  solution: A vendor agent 'identifies and proposes replacements for work in flight', and the vendor says its matching
    'automatically re-matches the moment resources shift' to protect capacity and cut bench time (CERTINIA-VEDA-2026,
    Plan-stage list; 'Staff with confidence' text).
  outcomes:
  - lever: capacity
    description: none published
    figure: none
    measures: n/a
    provenance: self-reported
    source_ref: n/a
  prerequisites:
  - Live skills, availability, cost and assignment data in the PSA
  - Rules for who approves a proposed replacement (not described in the sources read)
  risks_and_guardrails:
  - EU Annex III point 4(b) also lists systems that 'monitor and evaluate the performance and behaviour' of workers;
    an agent that reallocates work based on performance data may touch both limbs (EU-AIACT-OJ-2024, Annex III 4(b))
  - Employers must inform workers and their representatives before using a high-risk system at the workplace (EU-AIACT-OJ-2024,
    Art. 26(7)); deployers must keep automatically generated logs for at least six months where under their control
    (Art. 26(6))
  - The vendor page states 'proposes', so the decision step is not automated by the vendor's own description
  human_checkpoints:
  - 'Approval of proposed replacements: not described by the vendor'
  role_evolution: none published
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: Veda AI agents for professional services (AI solutions page)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: Plan-stage agent list (Work Reallocation Agent); 'Staff with confidence, not guesswork'
  - ref: EU-AIACT-OJ-2024
    title: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal text
    publisher: European Parliament and Council of the European Union (EUR-Lex)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
    date: '2024-07-12'
    access: full
    locator: Annex III 4(b); Article 26(6) and 26(7)
  last_reviewed: '2026-10-19'
  notes: Vendor claim only; no named customer, usage or outcome for this agent was found.
- id: professional-services-staffing-resourcing-07
  title: Planning and assigning AI agents as resources alongside people, with cost and capacity tracked
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
  maturity: emerging
  problem: Resource management assumes human capacity and hourly rates. Firms that put agents into delivery have
    no agreed way to plan, price or attribute agent work.
  solution: Treat agents as assignable resources with defined capacity and cost or rate, and orchestrate mixed human-agent
    teams (the question the Resource Management Institute asked in Q8 and Q9).
  outcomes:
  - lever: capacity
    description: Respondents whose agents are 'already operationalized' as assignable resources
    figure: 0%
    measures: Share of respondents choosing that status in Q8 (44 organizations)
    provenance: vendor-published
    source_ref: KANTATA-RMI-REPORT-2026
  - lever: capacity
    description: Respondents actively implementing pilots that formalise how agents are planned and assigned
    figure: 10.7%
    measures: Share of respondents choosing that status in Q8; a further 25.3% describe exploratory experiments
      and 32% say agents are not on the roadmap
    provenance: vendor-published
    source_ref: KANTATA-RMI-REPORT-2026
  - lever: capacity
    description: Leaders expecting their systems to attribute work, costs and value across humans and AI agents
      in the near future
    figure: 90%
    measures: '''Leaders say'' (Kantata-sponsored survey of 200 leaders); also 87% plan to use AI agents as part
      of the workforce'
    provenance: vendor-published
    source_ref: CPAPA-KANTATASOPS-2026
  prerequisites:
  - A rate, cost and capacity model for agents; 10% of respondents named unclear economics and value measurement
    of AI use as a gap (KANTATA-RMI-REPORT-2026, Q19, p. 21)
  - Clear ownership of who decides where AI is used; 20% named unclear ownership as a gap (same, Q19)
  risks_and_guardrails:
  - 'Readiness is low: 52.7% not equipped to manage hybrid human-AI teams, 28.4% slightly equipped, 4% well equipped
    (KANTATA-RMI-2026, press release; Q9, p. 11)'
  - Open questions remain over who manages AI agents and how human-AI team performance is evaluated (TRI-TEAMS-2025,
    section on risks)
  - California's guidance says that the greater a system's autonomy, the greater the lawyer's duty to implement
    oversight so that professional judgment stays with the lawyer (CALBAR-GENAI-2026, Competence and Diligence,
    p. 5)
  - ICMCI's code says individual consultants and firms remain accountable and that firms should document significant
    AI-supported decisions (ICMCI-AICODE-2026, s.3.6)
  human_checkpoints:
  - Lawyer or consultant review of agent output remains required by the bar and ICMCI texts above; how a resource
    manager signs off agent assignments is not described in any source
  role_evolution: Respondents say playbooks, skills enablement and workflow changes are needed before hybrid staffing
    becomes routine (KANTATA-RMI-2026). TR Institute reports that traditional HR metrics do not fit human-AI teams
    (TRI-TEAMS-2025).
  evidence_grade: C
  sources:
  - ref: KANTATA-RMI-REPORT-2026
    title: Resource Management in the Age of AI (full survey report; 44 organizations)
    publisher: Resource Management Institute (RTM Consulting, a Belcan company) for Kantata
    type: vendor
    url: https://get.kantata.com/rs/677-LEJ-696/images/AI_in_Resource_Management_Survey.pdf
    date: 2026-04
    access: full
    locator: Key Observations p. 4; Q8 p. 10; Q9 p. 11; Q19 p. 21
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services (press release, updated 16 Sep 2026)
    publisher: Kantata (study by the Resource Management Institute)
    type: vendor
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraph on hybrid-team readiness
  - ref: CPAPA-KANTATASOPS-2026
    title: 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce (Kantata State
      of the Professional Services Industry report, 200 leaders, conducted by Censuswide)
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/02/17/87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce/178201/
    date: '2026-02-17'
    access: full
    locator: Paragraphs on workforce plans and attribution of work
  - ref: TRI-TEAMS-2025
    title: How companies are fostering the creation of human & AI agent teams
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/creating-human-ai-agent-teams
    date: '2025-10-22'
    access: full
    locator: Section on challenges of merging HR and IT
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Competence and Diligence, p. 5
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version
      1.0
    publisher: International Council of Management Consulting Institutes (ICMCI)
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: s.3.6 Accountability and documentation
  last_reviewed: '2026-10-19'
  notes: 'Maturity emerging: the survey shows no organization operating assignable agents. Survey is vendor-commissioned
    and small (44 organizations); percentages in the report text and press release differ slightly (for example
    30% versus 30.4%).'
- id: professional-services-staffing-resourcing-08
  title: Outcome data from past team combinations used to staff deals (idea)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Resource managers are asked to staff for outcomes but rarely have outcome data. Only 7.3% say outcome
    data is easily accessible and routinely used in staffing decisions, and 24.6% say it is not available to resource
    management at all (KANTATA-RMI-2026, press release).
  solution: 'Idea: AI links delivery outcomes to the people (and agents) who produced them, and surfaces ''proof
    of outcome'' for staffing recommendations on prospective deals. No named firm was found doing this.'
  outcomes:
  - lever: quality
    description: none published (survey of need and wants)
    figure: 73.4%
    measures: Respondents saying it would be very or extremely valuable to know which combinations of people or
      agents consistently produce strong outcomes (RMI study, 44 organizations)
    provenance: vendor-published
    source_ref: KANTATA-RMI-2026
  - lever: quality
    description: Respondents wanting outcome 'proof' surfaced for deal staffing
    figure: 37%
    measures: Share selecting 'Surfacing proof of outcome' in Q16 (multi-select)
    provenance: vendor-published
    source_ref: KANTATA-RMI-REPORT-2026
  prerequisites:
  - Outcome capture per engagement and per team, visible in resource management workflows (14% say outcomes are
    available but hard to access; KANTATA-RMI-REPORT-2026, Q13, p. 15)
  risks_and_guardrails:
  - 'Linking outcomes to named individuals creates people analytics that fall under the same worker-facing rules
    as other staffing AI: EU Annex III 4(b) (monitoring and evaluating performance), Art. 26(7) worker information,
    and Art. 86 right to an explanation of decisions with significant adverse effect (EU-AIACT-OJ-2024)'
  - ICMCI's code says firms should, where practicable, test AI outputs for disparate impact and be cautious where
    data may not be representative (ICMCI-AICODE-2026, s.3.2)
  - The press release and the report text give slightly different shares for outcome experience having high influence
    on deal staffing (50.9% in the release; 47.8% high plus 2.9% very high in the report)
  human_checkpoints:
  - Not described; the staffing recommendation for a deal stays with resource managers in the source's framing
  role_evolution: Respondents say that under outcome-based pricing resource management moves from 'filling hours'
    to maximising delivery success, taking on team composition and delivery risk (KANTATA-RMI-2026).
  evidence_grade: D
  sources:
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape
      Professional Services (press release, updated 16 Sep 2026)
    publisher: Kantata (study by the Resource Management Institute)
    type: vendor
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: Paragraphs on outcome intelligence and outcome-based pricing
  - ref: KANTATA-RMI-REPORT-2026
    title: Resource Management in the Age of AI (full survey report; 44 organizations)
    publisher: Resource Management Institute (RTM Consulting, a Belcan company) for Kantata
    type: vendor
    url: https://get.kantata.com/rs/677-LEJ-696/images/AI_in_Resource_Management_Survey.pdf
    date: 2026-04
    access: full
    locator: Q13 p. 15; Q15 p. 17; Q16 p. 18
  - ref: EU-AIACT-OJ-2024
    title: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal text
    publisher: European Parliament and Council of the European Union (EUR-Lex)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
    date: '2024-07-12'
    access: full
    locator: Annex III 4(b); Articles 26(7) and 86
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version
      1.0
    publisher: International Council of Management Consulting Institutes (ICMCI)
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: s.3.2 Fairness and non-discrimination
  last_reviewed: '2026-10-19'
  notes: 'Grade D, labelled idea: discussed in the study as a wish and a gap; no deployment found.'
- id: professional-services-staffing-resourcing-09
  title: Forward utilization and bench-risk monitoring against target bands (idea)
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
  maturity: emerging
  problem: Utilization is falling and is usually reviewed after the fact. SPI's benchmark puts average billable
    utilization at 66.4% for 2025, the lowest in its history, and Deltek reports A&E utilization just under 60%
    (DELTEK-SPIBENCH-2026; DELTEK-CLARITY-2026).
  solution: 'Idea: monitor assigned work, pipeline and leave against utilization bands per role and flag weeks ahead
    where people will be under- or over-used, so staffing moves happen before margin is lost. A Certinia analysis
    says utilization has to be managed earlier, not only reported monthly (CERTINIA-SPIBENCH-2026).'
  outcomes:
  - lever: capacity
    description: 'Baseline: average billable utilization fell to its lowest level in SPI''s survey history'
    figure: 66.4% in 2025 (Level 5 firms above 80%)
    measures: Percentage of available consultant time charged to clients, across benchmarked organizations (509
      firms per the Certinia analysis); relayed by vendors from SPI Research
    provenance: vendor-published
    source_ref: DELTEK-SPIBENCH-2026
  - lever: capacity
    description: 'Baseline: A&E firm utilization'
    figure: just under 60%
    measures: As reported in the Deltek Clarity A&E study of 896 firms
    provenance: vendor-published
    source_ref: DELTEK-CLARITY-2026
  prerequisites:
  - Reliable assignment, leave and pipeline data (47.1% of respondents cite fragmented data; KANTATA-RMI-REPORT-2026,
    Q19)
  risks_and_guardrails:
  - Deltek's reading of SPI says to aim for 70-75% or more, balanced against burnout and quality (DELTEK-SPIBENCH-2026);
    utilization targets applied to individuals are performance monitoring, which EU Annex III 4(b) lists as high-risk
    where AI evaluates performance and behaviour (EU-AIACT-OJ-2024)
  human_checkpoints:
  - Resource managers decide staffing moves; alert-to-action practice is not described in any source
  role_evolution: none published
  evidence_grade: D
  sources:
  - ref: DELTEK-SPIBENCH-2026
    title: 5 KPIs from the SPI Professional Services Maturity Benchmark Report Every PSO Must Track for Sustainable
      Growth
    publisher: Deltek (relaying SPI Research data)
    type: vendor
    url: https://www.deltek.com/en/resources/articles/5-kpis-from-the-spi-professional-services-maturity-benchmark-report-every-pso-must-track-for-sustainable-growth
    date: '2026-07-15'
    access: full
    locator: Section 1, Billable Utilization
  - ref: CERTINIA-SPIBENCH-2026
    title: Analyzing the 2026 SPI Research Professional Services Maturity Benchmark Report (page shows no publication
      date; text refers to the midpoint of 2026)
    publisher: Certinia (relaying SPI Research data)
    type: vendor
    url: https://certinia.com/blog/analyzing-the-2026-spi-research-professional-services-maturity-benchmark-report/
    date: '2026'
    access: full
    locator: Section 'Utilization is becoming harder to protect'
  - ref: DELTEK-CLARITY-2026
    title: The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity
      Pressures (47th Clarity A&E study, 896 firms; 17th Clarity Government Contracting study, 917 firms)
    publisher: Deltek
    type: survey
    url: https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/
    date: '2026-05-12'
    access: full
    locator: Key Findings, 47th A&E report
  - ref: EU-AIACT-OJ-2024
    title: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal text
    publisher: European Parliament and Council of the European Union (EUR-Lex)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
    date: '2024-07-12'
    access: full
    locator: Annex III 4(b)
  last_reviewed: '2026-10-19'
  notes: 'Grade D, labelled idea: the benchmarks establish the problem, not an AI monitoring deployment. Benchmark
    figures come from vendor relays of SPI data and a vendor''s own survey.'
- id: professional-services-staffing-resourcing-10
  title: Decision logging, override tracking, disparate-impact testing and explanations for AI-assisted work allocation
    (idea)
  archetype: professional-services
  module: staffing-resourcing
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Rules that name work allocation and assignment are arriving, yet resource managers barely register compliance
    as a gap (4% in the RMI study) and no source reports override or acceptance rates for staffing recommendations.
  solution: 'Idea: record each AI-assisted staffing recommendation and the human decision, test outcomes for disparate
    impact, and be able to explain the AI''s role to an affected person. The controls are drawn from the legal texts
    and codes below; no firm was found operating this for staffing.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: n/a
    provenance: self-reported
    source_ref: n/a
  prerequisites:
  - An inventory of which staffing tools use AI and what decisions they influence (the National Law Review lists
    inventorying AI tools across the employment lifecycle first; NATLAW-AIHIRING-2026)
  - A reviewer who meets California's three-part human-involvement test (CPPA-CCPAREGS-2026, s.7001(e)(1))
  risks_and_guardrails:
  - 'EU: deployers keep automatically generated logs for at least six months where under their control (Art. 26(6));
    inform workers and representatives before use (Art. 26(7)); affected persons can obtain explanations of the
    AI system''s role in certain Annex III decisions (Art. 86(1)) (EU-AIACT-OJ-2024). Annex III employment obligations
    apply from 2 December 2027 (EC-AIACT-2026).'
  - 'California: ADMT for a significant decision, which includes allocation or assignment of work, must meet the
    regulation''s requirements by 1 January 2027; the regulation has pre-use notice, opt-out and access provisions
    (CPPA-CCPAREGS-2026, Article 11, ss.7200-7222).'
  - 'UK: the Data (Use and Access) Act 2025 replaces UK GDPR Article 22 with Articles 22A-22D. A decision is solely
    automated if there is no meaningful human involvement; safeguards include information, representations, human
    intervention and the right to contest (UK-DUAA-2025, s.80). Commencement status was not checked.'
  - 'Illinois: from 1 January 2026 it is a civil rights violation to use AI that has the effect of discrimination
    in employment matters including ''terms, privileges, or conditions of employment'', and to fail to give employees
    notice (ILGA-HB3773-2024, s.2-102(L)). The text read does not say whether work assignment is covered.'
  - 'Colorado: SB26-189 (signed 14 May 2026) repeals and reenacts the state''s AI act for automated decision-making
    technology in consequential decisions including employment; developer documentation duties start 1 January 2027
    and the Attorney General must adopt post-adverse-outcome disclosure rules by 1 January 2027 (COLORADO-SB26189-2026,
    bill summary). An earlier law-firm article on the superseded Act (stayed by a federal court on 27 April 2026,
    per that article) is NATLAW-AIHIRING-2026.'
  - 'New York City: bias audit within a year of use, published summary and candidate or employee notice for automated
    employment decision tools (NYC-LL144-2023). The state Comptroller found enforcement ineffective: nine of 12
    test calls to 311 to file a complaint were not connected to the enforcing agency, and the agency''s own review
    of 32 companies found one issue where the auditors found at least 17 (OSC-LL144-2025, Findings, pp. 1 and 8).
    Scope of LL144 over work assignment was not established in the pages read.'
  - ICMCI's code defines high-risk AI use to include uses that may materially affect individuals' employment (s.1.3);
    for high-risk uses a qualified individual must be able to intervene, override or discontinue the system (s.3.1);
    firms should test outputs for disparate impact where practicable (s.3.2) and document significant AI-supported
    decisions (s.3.6). Section 11.4 tells consultants advising clients to warn against oversight that is nominal
    because of volume, speed or incentives (ICMCI-AICODE-2026).
  human_checkpoints:
  - Reviewer who can interpret, review and change the decision (CPPA-CCPAREGS-2026, s.7001(e)(1)); a qualified individual
    able to intervene in, override or discontinue a high-risk AI system (ICMCI-AICODE-2026, s.3.1)
  role_evolution: none published
  evidence_grade: D
  sources:
  - ref: EU-AIACT-OJ-2024
    title: Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal text
    publisher: European Parliament and Council of the European Union (EUR-Lex)
    type: regulator
    url: https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689
    date: '2024-07-12'
    access: full
    locator: Annex III 4(b); Article 26(6), 26(7); Article 86(1)
  - ref: EC-AIACT-2026
    title: AI Act (regulatory framework page, incl. application timeline and AI Omnibus)
    publisher: European Commission, Shaping Europe's digital future
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: '2026-10-19'
    access: full
    locator: Application timeline
  - ref: CPPA-CCPAREGS-2026
    title: California Consumer Privacy Act Regulations, effective 1/1/2026 (includes Article 11, Automated Decisionmaking
      Technology)
    publisher: California Privacy Protection Agency
    type: regulator
    url: https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf
    date: '2026-01-01'
    access: full
    locator: s.7001(e), s.7001(ddd)(4), s.7200
  - ref: UK-DUAA-2025
    title: Data (Use and Access) Act 2025, section 80 (automated decision-making; new UK GDPR Articles 22A-22D)
    publisher: UK Parliament (legislation.gov.uk)
    type: regulator
    url: https://www.legislation.gov.uk/ukpga/2025/18/section/80
    date: '2025-06-19'
    access: full
    locator: s.80, new Articles 22A-22C
  - ref: ILGA-HB3773-2024
    title: 'Public Act 103-0804 (HB 3773): use of artificial intelligence in employment, amending the Illinois Human
      Rights Act (effective 1 January 2026; page gives the effective date, not the signing date)'
    publisher: Illinois General Assembly
    type: regulator
    url: https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=103-0804
    date: '2026-01-01'
    access: full
    locator: Section 2-102(L), Use of artificial intelligence
  - ref: COLORADO-SB26189-2026
    title: SB26-189, Automated Decision-Making Technology (signed 14 May 2026; repeals and reenacts SB24-205)
    publisher: Colorado General Assembly
    type: regulator
    url: https://leg.colorado.gov/bills/sb26-189
    date: '2026-05-14'
    access: full
    locator: Bill summary (as enacted); status table
  - ref: NATLAW-AIHIRING-2026
    title: Patchwork AI Hiring Laws Create Rising Compliance Risks for Employers (Andrew Adams, Darrow Everett LLP;
      written before Colorado SB26-189 was signed)
    publisher: The National Law Review
    type: press
    url: https://natlawreview.com/article/patchwork-ai-hiring-laws-create-rising-compliance-risks-employers
    date: '2026-05-12'
    access: full
    locator: Sections on Illinois, Colorado and New York City; recommended steps
  - ref: NYC-LL144-2023
    title: Automated Employment Decision Tools (AEDT), Local Law 144 of 2021
    publisher: New York City Department of Consumer and Worker Protection
    type: regulator
    url: https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
    date: 2023-07
    access: full
    locator: Page text on bias audit, publication and notice
  - ref: OSC-LL144-2025
    title: Enforcement of Local Law 144 - Automated Employment Decision Tools (Report 2024-N-6)
    publisher: Office of the New York State Comptroller, Division of State Government Accountability
    type: regulator
    url: https://www.osc.ny.gov/files/state-agencies/audits/pdf/sga-2026-24n6.pdf
    date: 2025-12
    access: full
    locator: Audit Highlights p. 1; Findings p. 8
  - ref: ICMCI-AICODE-2026
    title: Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version
      1.0
    publisher: International Council of Management Consulting Institutes (ICMCI)
    type: professional-body
    url: https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf
    date: 2026-05
    access: full
    locator: s.1.3 (high-risk AI use); s.3.1; s.3.2; s.3.6; s.11.4 'Designing for human oversight'
  - ref: KANTATA-RMI-REPORT-2026
    title: Resource Management in the Age of AI (full survey report; 44 organizations)
    publisher: Resource Management Institute (RTM Consulting, a Belcan company) for Kantata
    type: vendor
    url: https://get.kantata.com/rs/677-LEJ-696/images/AI_in_Resource_Management_Survey.pdf
    date: 2026-04
    access: full
    locator: Q19, p. 21
  last_reviewed: '2026-10-19'
  notes: 'Grade D, labelled idea: a control set derived from legal and professional texts, not a described deployment.
    Legal texts are cited for what they say; whether any text applies to a given staffing tool needs legal advice.
    The Colorado repeal-and-reenact came two days after the National Law Review article, so that article''s Colorado
    detail is superseded.'
- id: professional-services-staffing-resourcing-11
  title: Capacity plans re-based on AI-adjusted effort per task and role, tested against observed demand (idea)
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: emerging
  problem: Capacity models convert demand into hours per role. If AI changes hours per task but clients' demand
    for hours does not fall, plans built on assumed savings under-staff; if savings are real and unresold, plans
    over-staff. Evidence on the real effect is thin.
  solution: 'Idea: capacity planners estimate effort per task with AI assistance, check it against measured hours
    and demand, and reset leverage assumptions. Practitioners frame the gap between hours saved and hours resold
    as ''the leak'' (SPI-AI-2026) and note clients are not yet seeing savings (ACCEVERLAW-2025).'
  outcomes:
  - lever: capacity
    description: Demand for lawyer time rose rather than fell in the first half of 2026
    figure: 4.2%, against about 1.5% normal growth
    measures: Growth in demand for law firm hours, as reported by Citi's law firm banking group and quoted by Bloomberg
      Law
    provenance: independent
    source_ref: BLOOMBERGLAW-BILLABLE-2026
  - lever: capacity
    description: Share of in-house respondents seeing no GenAI savings from their law firms yet
    figure: 59%
    measures: '''Report no GenAI savings from their law firms yet'' (ACC/Everlaw survey of 657 in-house legal professionals
      in 30 countries; in-house)'
    provenance: vendor-published
    source_ref: ACCEVERLAW-2025
  - lever: capacity
    description: Share of firms reporting AI saves time versus revenue (the revenue share is withheld on the landing
      page)
    figure: 84.8% say AI saves them time
    measures: SPI 2026 survey of 245 organizations; the matching revenue share is behind the paywall
    provenance: vendor-published
    source_ref: SPI-AI-2026
  prerequisites:
  - Time-entry data by task and role with and without AI assistance (not described in any source)
  - A view of whether freed hours are resold, repriced or redeployed (SPI-AI-2026, Part III 'The Leak')
  risks_and_guardrails:
  - Associates and non-equity partners absorbed most extra work in Q2 2026 and the ratio of non-equity-partner to
    equity-partner hours is the highest since late 2018, per Thomson Reuters Institute market data (TRI-LFFI-Q2-2026)
  - Hourly billing must reflect time actually spent under ABA Formal Opinion 512, so AI-saved hours cannot be billed
    as if worked (ABA-OP512-2024, Fees, p. 12; see the scoping-pricing module)
  human_checkpoints:
  - Planners and practice leaders agree effort assumptions; not described in the sources
  role_evolution: Thomson Reuters's 'Scale' pathway describes AI addressing a capacity question without proportional
    headcount growth, with mid-career professionals taking management responsibility earlier (TR-FOP-2026, AI to
    Scale).
  evidence_grade: D
  sources:
  - ref: BLOOMBERGLAW-BILLABLE-2026
    title: Big Law AI Cost Savings Remain a Mystery as Billable Hours Jump (Big Law Business column, Roy Strom)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/big-law-ai-cost-savings-remain-a-mystery-as-billable-hours-jump
    date: '2026-09-03'
    access: full
    locator: Paragraphs on Citi demand data
  - ref: ACCEVERLAW-2025
    title: 64% of In-House Counsel Expect GenAI to Reduce Reliance on Outside Counsel, 50% Expect Lower Outside
      Counsel Costs, ACC/Everlaw Survey Finds
    publisher: Everlaw and the Association of Corporate Counsel
    type: survey
    url: https://www.everlaw.com.au/press/release/acc-report-2025
    date: '2025-10-14'
    access: full
    locator: '''Clients will challenge the billable hour'' paragraph'
  - ref: SPI-AI-2026
    title: The 2026 Impact of AI on Professional Services (report landing page; report itself not opened)
    publisher: SPI Research
    type: survey
    url: https://spiresearch.com/reports/2026-ai-professional-services-survey/
    date: 2026-10
    access: full
    locator: '''The Leak'' and Part III contents'
  - ref: TRI-LFFI-Q2-2026
    title: 'Q2 2026 LFFI: A heavier load, yet a faster crossing'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed
    date: '2026-08-10'
    access: full
    locator: Key takeaways; demand-by-title section
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools (copy hosted by LawSites; the americanbar.org
      copy returned 403)'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Fees section (Rule 1.5), p. 12
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026 (AI to Scale pathway)
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: '2026-09-30'
    access: full
    locator: AI to Scale section
  last_reviewed: '2026-10-19'
  notes: 'Grade D, labelled idea: the demand data is independent but describes the market, not an AI capacity-planning
    practice; the plan re-basing itself is discussed, not documented in a named firm. Hours-demand growth does not
    show that AI saved no time, only that demand rose.'
- id: professional-services-staffing-resourcing-12
  title: 'Right-sizing teams: one professional with AI in place of a two-person team (adjacent field experiment)'
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: personal-assistant
  maturity: piloting
  problem: Team composition rules (who pairs with whom) assume AI is absent. If AI replaces some collaboration benefits,
    staffing two people on a task may add cost without adding quality.
  solution: Staff a single professional with AI where a pair would have been used. A pre-registered field experiment
    at Procter & Gamble randomly assigned 776 professionals to work with or without AI, individually or in two-person
    teams on product-development challenges.
  outcomes:
  - lever: capacity
    description: Individuals with AI matched the performance of teams without AI
    figure: performance matched (no ratio published in the abstract)
    measures: 776 professionals at Procter & Gamble randomly assigned to work with or without AI, alone or in pairs,
      on real product innovation challenges
    provenance: independent
    source_ref: NBER-DELLACQUA-2025
  prerequisites:
  - Tasks resembling the experiment's (real product-innovation challenges); not tested on client service delivery
  risks_and_guardrails:
  - 'Expertise erosion: in a three-month trial with 133 patent lawyers at 11 US IP firms, treated lawyers'' judgment
    advantage without AI was 0.32 SD but concentrated in senior lawyers (0.45 SD); juniors showed no average gain
    and their scores bifurcated (NBER-AUTOR-2026, abstract). The study was largely funded by Google and several
    authors work for it (NBER disclosures).'
  - Early-career employment in AI-exposed occupations was 19% below the less-exposed trend by June 2026 in ADP payroll
    data, driven by reduced hiring; the authors call this descriptive, not causal (STANFORD-CANARIES-2026, abstract)
  - A Danish study found no earnings or recorded-hours effects larger than 2% two years after ChatGPT's launch,
    while employers reorganised tasks (NBER-HUMLUM-2025, abstract)
  human_checkpoints:
  - Not described; the experiment compares conditions, it does not describe a staffing policy
  role_evolution: AI-using professionals produced balanced solutions across R&D and commercial backgrounds, reducing
    functional silos (NBER-DELLACQUA-2025, abstract). The pyramid implications are in the talent-learning module.
  evidence_grade: B
  sources:
  - ref: NBER-DELLACQUA-2025
    title: 'The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise (NBER
      Working Paper 33641; Organization Science, online June 2026)'
    publisher: National Bureau of Economic Research (Dell'Acqua et al.)
    type: academic
    url: https://www.nber.org/papers/w33641
    date: 2025-04
    access: full
    locator: Abstract
  - ref: NBER-AUTOR-2026
    title: Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent
      Drafting (NBER Working Paper 35720)
    publisher: National Bureau of Economic Research (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere)
    type: academic
    url: https://www.nber.org/papers/w35720
    date: 2026-09
    access: full
    locator: Abstract and disclosures
  - ref: STANFORD-CANARIES-2026
    title: Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence (August
      2026 version)
    publisher: Stanford Digital Economy Lab / NBER (Brynjolfsson, Chandar, Chen)
    type: academic
    url: https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf
    date: 2026-08
    access: full
    locator: Abstract
  - ref: NBER-HUMLUM-2025
    title: 'Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI (NBER Working Paper
      33777; earlier title ''Large Language Models, Small Labor Market Effects'')'
    publisher: National Bureau of Economic Research (Humlum, Vestergaard)
    type: academic
    url: https://www.nber.org/papers/w33777
    date: 2025-05
    access: full
    locator: Abstract
  last_reviewed: '2026-10-19'
  notes: 'Capped at B: independent randomised evidence from a named organization, but in consumer-goods product
    development, not professional services staffing. The field experiment was published in Organization Science
    in June 2026 (per the NBER page). Where the unit of work is an NPD challenge, extrapolation to client work is
    the reader''s judgement.'
- id: professional-services-staffing-resourcing-13
  title: 'In-house: reallocating work between the internal team and outside counsel as AI lifts internal capacity'
  archetype: professional-services
  module: staffing-resourcing
  function: service-delivery
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: In-house legal teams decide what to do internally and what to send to outside counsel; AI changes what
    internal teams can absorb. (in-house)
  solution: Corporate legal departments insource work that GenAI makes manageable internally and reduce reliance
    on outside counsel for it. The survey records expectations, not a measured shift.
  outcomes:
  - lever: capacity
    description: In-house respondents expecting to rely less on outside counsel
    figure: 64%
    measures: Share of 657 in-house legal professionals in 30 countries expecting to rely less on outside counsel
      (up from 58% in 2024, US respondents)
    provenance: vendor-published
    source_ref: ACCEVERLAW-2025
  - lever: capacity
    description: Respondents seeing an opportunity to insource drafting
    figure: 78%
    measures: Share citing insourcing of drafting as an opportunity (also contract management 71%, research 62%);
      same survey
    provenance: vendor-published
    source_ref: ACCEVERLAW-2025
  prerequisites:
  - 'Active GenAI use in the department: 52% in 2025 versus 23% in 2024 (US respondents) per the survey'
  risks_and_guardrails:
  - Only 9% said company policy prohibits GenAI use, down from 29% (ACCEVERLAW-2025)
  - Supervision and confidentiality duties follow the lawyer wherever the work sits (ABA-OP512-2024, Part E, pp.
    10-11; CALBAR-GENAI-2026, Duty to Supervise, p. 7)
  human_checkpoints:
  - The decision to insource or outsource a matter stays with the legal department; the survey does not describe
    a workflow
  role_evolution: 61% of respondents plan to push for change in how legal services are delivered and priced from
    law firms that use GenAI (ACCEVERLAW-2025); no source read describes changed roles inside legal departments.
  evidence_grade: C
  sources:
  - ref: ACCEVERLAW-2025
    title: 64% of In-House Counsel Expect GenAI to Reduce Reliance on Outside Counsel, 50% Expect Lower Outside
      Counsel Costs, ACC/Everlaw Survey Finds
    publisher: Everlaw and the Association of Corporate Counsel
    type: survey
    url: https://www.everlaw.com.au/press/release/acc-report-2025
    date: '2025-10-14'
    access: full
    locator: 'Survey results: ''Reliance on outside counsel is shrinking''; ''Barriers are falling fast'''
  - ref: ABA-OP512-2024
    title: 'Formal Opinion 512: Generative Artificial Intelligence Tools (copy hosted by LawSites; the americanbar.org
      copy returned 403)'
    publisher: American Bar Association, Standing Committee on Ethics and Professional Responsibility
    type: professional-body
    url: https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf
    date: '2024-07-29'
    access: full
    locator: Part E Supervisory Responsibilities, pp. 10-11
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Duty to Supervise, p. 7
  last_reviewed: '2026-10-19'
  notes: 'In-house example. Grade C: survey of expectations co-run with a vendor; no named department described.'
```

## 3. Module notes

### Processes and key steps (work types are the analyst's mapping)

- Demand capture and capacity forecasting from pipeline and delivery data: `data-reporting`, `coordination-scheduling` (use case 02, 11).
- Skills inventory upkeep: `data-reporting`, `research-synthesis` (03).
- Resource request intake, matching and shortlisting: `coordination-scheduling` (01).
- Assignment and scheduling of cases or tasks to people: `coordination-scheduling` (04, 05).
- Re-matching and reallocation of in-flight work: `coordination-scheduling` (06).
- Utilization and bench monitoring: `data-reporting` (09).
- Hybrid human-agent team planning and cost attribution: `coordination-scheduling`, `data-reporting` (07).
- Outcome capture feeding staffing decisions: `data-reporting` (08).
- Control layer over AI-assisted allocation: `review-assurance` (10).
- In-house: insource versus outside-counsel allocation: `coordination-scheduling` (13).

### Common pain points

- Capacity limits cost work: 55% of firms in the Dayshape survey miss, delay or turn down client work; Kantata's 200-leader survey reports more than 66% turn down work for resourcing reasons (DAYSHAPE-ONREC-2026; CPAPA-KANTATASOPS-2026).
- Staffing by availability: 39% regularly staff by availability rather than best-fit skills (DAYSHAPE-ONREC-2026).
- Data: 47.1% cite fragmented skills, outcome, demand and capacity data; only 12% fully trust the data in their systems (KANTATA-RMI-REPORT-2026, Q19; CPAPA-KANTATASOPS-2026).
- Resource management is seen as operational: 72% say primarily or solely operational; main limits are competing operational demands (49%) and lack of executive mandate (48%) (KANTATA-RMI-2026).
- Outcomes are invisible to staffers: 7.3% have outcome data routinely used; 24.6% say it is not available (KANTATA-RMI-2026).
- Talent supply: A&E firms report staff growth of 1.2% against forecast revenue growth of 9.5%, with turnover above 13% (DELTEK-CLARITY-2026).

### Metrics and benchmarks (with sources and provenance)

- Average billable utilization 66.4% in 2025, lowest in SPI's survey history; Level 5 firms above 80%; revenue leakage averaged 4.5% (DELTEK-SPIBENCH-2026; CERTINIA-SPIBENCH-2026; sample of 509 firms per Certinia; vendor-relayed).
- A&E utilization just under 60%, operating profit 16.7%, turnover above 13% (DELTEK-CLARITY-2026; 896 firms; vendor-run survey).
- 43.6% of projects now use AI (23.1% in 2025); 84.8% say AI saves them time (the matching revenue share is withheld) (SPI-AI-2026; 245 firms; landing page only).
- 52% report improved forecast accuracy or utilization among AI-using organizations; 12% fully trust their data (CPAPA-KANTATASOPS-2026; 200 leaders).
- 76% say AI improves resource-planning and allocation decisions; only a small minority forecast capacity beyond 12 months (DAYSHAPE-ONREC-2026; 400 leaders).
- Demand for Big Law hours +4.2% in H1 2026 versus about 1.5% normal (BLOOMBERGLAW-BILLABLE-2026, citing Citi); non-equity-partner to equity-partner hours ratio at its highest since late 2018 (TRI-LFFI-Q2-2026).
- Quality evidence for AI in staffing: none at a named professional services organization. Adjacent: FERREIRA-PERU-2026 (assignment), NBER-DELLACQUA-2025 (team size), NBER-AUTOR-2026 (expertise), NBER-BRYNJOLFSSON-2025 (novices gained most: productivity up 14% on average and 34% for novice and low-skilled workers, in customer support, so not a professional services staffing result).

### Guardrails and regulatory points

- EU AI Act: Annex III 4(b); Art. 26(2) human oversight assigned to people with competence, training and authority; Art. 26(6) logs of at least six months; Art. 26(7) inform workers and representatives; Art. 86 explanation right (EU-AIACT-OJ-2024). Annex III obligations from 2 December 2027; transparency rules and general application from 2 August 2026 (EC-AIACT-2026).
- California CCPA regulations effective 1 January 2026: ADMT definition and human-involvement test (s.7001(e)); "allocation or assignment of work" as a significant decision (s.7001(ddd)(4)(B)); compliance due 1 January 2027 (s.7200(b)) (CPPA-CCPAREGS-2026).
- California bar guidance, approved 14 May 2026: supervision scales with autonomy; policies and training for agentic tools; bias risk in employment actions (CALBAR-GENAI-2026, pp. 5, 7, 9).
- ABA Formal Opinion 512 (29 July 2024): supervisory duties (Part E) and hourly billing on actual time (Fees) (ABA-OP512-2024, pp. 10-12).
- SRA (England and Wales): warning notice after 42 reports of potential AI misuse between July 2025 and July 2026, including supervision; "individuals remain responsible" (LAWSOCIE-SRAWARN-2026; reported by the Law Society of Ireland Gazette, the SRA's own page was not reachable).
- ICMCI code (May 2026): high-risk AI use includes employment effects; qualified individual able to override; disparate-impact testing where practicable; documentation (ICMCI-AICODE-2026).
- UK Data (Use and Access) Act 2025 s.80: Articles 22A-22D; meaningful human involvement test; safeguards (UK-DUAA-2025). Commencement not checked.
- US states: Illinois HB 3773 effective 1 January 2026 (ILGA-HB3773-2024); Colorado SB26-189 signed 14 May 2026 (COLORADO-SB26189-2026); NYC Local Law 144 bias-audit regime (NYC-LL144-2023), whose enforcement the State Comptroller found ineffective (OSC-LL144-2025). The ICO's 2024 recruitment-tool audits gave almost 300 recommendations, all accepted or partly accepted (ICO-AIRECRUIT-2024). These concern hiring and employment decisions; whether work assignment is in scope was not confirmed.
- Client terms: clients are asking for matter-level proof of AI savings and some say they will not pay for services performed by AI (TRI-LEGALWEEK-2026). Government buyers are adding terms: Australian suppliers on people panels must advise planned AI use in quotes (CANBERRATIMES-APSAI-2025). I found no client outside-counsel guideline text that addresses staffing by AI.

### Frontier signals (dated)

- 2026-04-09: Kantata/RMI study: 39% still in "traditional staffing" mode; 31% beyond experimentation; agents as assignable resources not operational anywhere in the sample (KANTATA-RMI-2026; KANTATA-RMI-REPORT-2026).
- 2026-02-17: Kantata survey: 87% of professional services teams plan to manage AI agents as part of their workforce; 90% expect systems to attribute work and cost across humans and agents (CPAPA-KANTATASOPS-2026; plans, not practice).
- 2026-06-11: first randomised evidence on algorithmic versus manager assignment of expert work (FERREIRA-PERU-2026).
- 2026-10-13: Dayshape reports 76% of leaders say AI is improving planning, while long-range forecasting remains weak (DAYSHAPE-ONREC-2026).
- 2026-05-14: Colorado reenacts its AI law for ADMT in consequential decisions, including employment, with duties from 1 January 2027 (COLORADO-SB26189-2026).
- 2026-10-19 (page read): EU Annex III employment obligations scheduled for 2 December 2027 (EC-AIACT-2026).
- 2026-08: Canaries paper: employment of 22-25-year-olds in AI-exposed occupations 19% below trend, through reduced hiring; descriptive only (STANFORD-CANARIES-2026).

### Workforce and role effects

- Resource managers are expected to move from "who is available" to team composition, delivery risk and economics if outcome-based pricing spreads, though 50% are unsure their firm will adopt it (KANTATA-RMI-2026).
- Entry-level supply: reduced hiring of young workers in AI-exposed occupations (STANFORD-CANARIES-2026); AI's durable skill gain concentrated among seniors in patent drafting (NBER-AUTOR-2026). These shape the staffing pool (see Routed).
- Project variety is the leading driver of consultant job satisfaction in the MCA survey, a reminder that assignment is a retention lever, not only a utilization one (MCA-SURVEY-2026; survey of 1,060 consultants; not AI-specific).
- 34% of professionals use AI tools their organization has not sanctioned, which affects how much AI-assisted effort planners can see (TR-FOP-2026).

### Objections and concerns practitioners raise

- Data is not trusted: 12% fully trust their system data; 89% spend significant time verifying AI outputs (CPAPA-KANTATASOPS-2026).
- Readiness: 52.7% not equipped for hybrid teams; limited understanding of where AI applies (48.6%) (KANTATA-RMI-REPORT-2026).
- Discretion carries information managers hold: the Peru trial's authors say managers match complex cases to experienced analysts, and automation broke that link (FERREIRA-PERU-2026).
- Unresolved questions over who manages agents and how human-agent performance is evaluated (TRI-TEAMS-2025).
- Savings are unproven to clients: firms say they are still gathering the data (TRI-LEGALWEEK-2026).
- Evidence is vendor-sourced: most figures above come from vendor-commissioned or vendor-run surveys with small or undisclosed bases.

### Interview probes for an advisor

1. When your resource managers accept or change an AI shortlist, what do they see, who can overrule them, and is the decision and the reason recorded anywhere?
2. Which of your staffing tools allocate work using data about individual performance, behaviour or traits, and has legal reviewed them against the EU and California rules that name task allocation?
3. If AI-assisted tasks take less time but clients still buy as many hours, how do your capacity plans change, and who checks the plan against actual hours?
4. Do you have outcome data by team combination, and would you be comfortable using it to pick people for a deal, given the worker-facing notice and fairness duties?
5. Would you put an agent on a staffing plan with a rate and a capacity? Who owns its quality, and who signs off its work?

## 4. Routed to other modules

- **talent-learning:** Canaries employment trend and the junior skill-bifurcation result (STANFORD-CANARIES-2026; NBER-AUTOR-2026); pairing juniors with seniors on AI-assisted work.
- **scoping-pricing:** Australian government requirement that suppliers advise planned AI use in responses to requests for quotes (CANBERRATIMES-APSAI-2025); hourly-fee rules (ABA-OP512-2024, p. 12); outcome-based pricing assumptions (KANTATA-RMI-2026).
- **acceptance-risk (client terms):** clients that bar AI or require permission (TRI-LEGALWEEK-2026).
- **pursuit-proposals:** capacity-aware bid/no-bid decisions, given 55% of firms turning down or delaying work for capacity reasons (DAYSHAPE-ONREC-2026).
- **billing-collections:** time-capture quality as the data source for utilization and effort assumptions (landscape lead; not examined here).
- **quality-review:** supervision and verification of AI output; the SRA's 42 reports (LAWSOCIE-SRAWARN-2026); California supervision text (CALBAR-GENAI-2026).
- **firm-finance:** leverage, rates and profit signals (TRI-LFFI-Q2-2026; BLOOMBERGLAW-BILLABLE-2026).
- **assurance archetype:** ISQM 1 requires that engagement teams have appropriate competence, capabilities and sufficient time, and treats technological resources as part of the firm's quality system; I saw this only in search-result summaries of paragraph 32 and did not read the standard (IAASB-ISQM1-2020, search-only). The audit-specific staffing rules belong there.

## 5. Sources

Access is `full` unless marked. Dates are publication dates where the page shows one; the ILGA date is the effective date; the Certinia SPI blog and SPI landing-page dates are the best available (the SPI report page says "Oct 2026 published").

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABA-OP512-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools (copy hosted by LawSites; the americanbar.org copy returned 403) | American Bar Association, Standing Committee on Ethics and Professional Responsibility | professional-body | https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf | 2024-07-29 | full |
| ACCEVERLAW-2025 | 64% of In-House Counsel Expect GenAI to Reduce Reliance on Outside Counsel, 50% Expect Lower Outside Counsel Costs, ACC/Everlaw Survey Finds | Everlaw and the Association of Corporate Counsel | survey | https://www.everlaw.com.au/press/release/acc-report-2025 | 2025-10-14 | full |
| BLOOMBERGLAW-BILLABLE-2026 | Big Law AI Cost Savings Remain a Mystery as Billable Hours Jump (Big Law Business column, Roy Strom) | Bloomberg Law | press | https://news.bgov.com/business-and-practice/big-law-ai-cost-savings-remain-a-mystery-as-billable-hours-jump | 2026-09-03 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision) | State Bar of California, Standing Committee on Professional Responsibility and Conduct | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05-14 | full |
| CANBERRATIMES-APSAI-2025 | What the public service's new AI plan means for external contractors | The Canberra Times | press | https://www.canberratimes.com.au/story/9110516/new-ai-plan-for-the-aps-sets-out-expectations-for-contractors/ | 2025-11-12 | full |
| CERTINIA-SPIBENCH-2026 | Analyzing the 2026 SPI Research Professional Services Maturity Benchmark Report (page shows no publication date; text refers to the midpoint of 2026) | Certinia (relaying SPI Research data) | vendor | https://certinia.com/blog/analyzing-the-2026-spi-research-professional-services-maturity-benchmark-report/ | 2026 | full |
| CERTINIA-VEDA-2026 | Veda AI agents for professional services (AI solutions page) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 | full |
| COLORADO-SB26189-2026 | SB26-189, Automated Decision-Making Technology (signed 14 May 2026; repeals and reenacts SB24-205) | Colorado General Assembly | regulator | https://leg.colorado.gov/bills/sb26-189 | 2026-05-14 | full |
| CPAPA-KANTATASOPS-2026 | 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce (Kantata State of the Professional Services Industry report, 200 leaders, conducted by Censuswide) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/17/87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce/178201/ | 2026-02-17 | full |
| CPPA-CCPAREGS-2026 | California Consumer Privacy Act Regulations, effective 1/1/2026 (includes Article 11, Automated Decisionmaking Technology) | California Privacy Protection Agency | regulator | https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf | 2026-01-01 | full |
| DAYSHAPE-ONREC-2026 | Professional services firms lose work as capacity planning falls behind demand (Onrec summary of Dayshape's 'Professional services: Navigating a new operating era', 400 senior leaders, UK and US) | Onrec | press | https://www.onrec.com/node/129428 | 2026-10-13 | full |
| DELTEK-CLARITY-2026 | The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures (47th Clarity A&E study, 896 firms; 17th Clarity Government Contracting study, 917 firms) | Deltek | survey | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| DELTEK-SPIBENCH-2026 | 5 KPIs from the SPI Professional Services Maturity Benchmark Report Every PSO Must Track for Sustainable Growth | Deltek (relaying SPI Research data) | vendor | https://www.deltek.com/en/resources/articles/5-kpis-from-the-spi-professional-services-maturity-benchmark-report-every-pso-must-track-for-sustainable-growth | 2026-07-15 | full |
| EC-AIACT-2026 | AI Act (regulatory framework page, incl. application timeline and AI Omnibus) | European Commission, Shaping Europe's digital future | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10-19 | full |
| EU-AIACT-OJ-2024 | Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal text | European Parliament and Council of the European Union (EUR-Lex) | regulator | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202401689 | 2024-07-12 | full |
| FERREIRA-PERU-2026 | Automated Assignment and Bureaucrat Productivity: Evidence from a Field Experiment in Peru (working paper) | Southern Methodist University and Innovations for Poverty Action (Ferreira, Cermeno Leon) | academic | https://poverty-action.org/sites/default/files/2026-07/main_assignment_enforcement_peru_2025.pdf | 2026-06-11 | full |
| IAASB-ISQM1-2020 | International Standard on Quality Management (ISQM) 1 (IAASB publication page opened; resource requirements known only from search-result summaries) | International Auditing and Assurance Standards Board | standard-setter | https://www.iaasb.org/publications/international-standard-quality-management-isqm-1-quality-management-firms-perform-audits-or-reviews | 2020-12-17 | search-only |
| ICMCI-AICODE-2026 | Code of Responsible Use of Artificial Intelligence for the Management Consulting Profession, Version 1.0 | International Council of Management Consulting Institutes (ICMCI) | professional-body | https://www.cmc-global.org/sites/default/files/public/code_of_responsible_use_of_artificial_intelligence.pdf | 2026-05 | full |
| ICO-AIRECRUIT-2024 | ICO intervention into AI recruitment tools leads to better data protection for job seekers | UK Information Commissioner's Office | regulator | https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2024/11/ico-intervention-into-ai-recruitment-tools-leads-to-better-data-protection-for-job-seekers/ | 2024-11-06 | full |
| ILGA-HB3773-2024 | Public Act 103-0804 (HB 3773): use of artificial intelligence in employment, amending the Illinois Human Rights Act (effective 1 January 2026; page gives the effective date, not the signing date) | Illinois General Assembly | regulator | https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=103-0804 | 2026-01-01 | full |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services (press release, updated 16 Sep 2026) | Kantata (study by the Resource Management Institute) | vendor | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| KANTATA-RMI-REPORT-2026 | Resource Management in the Age of AI (full survey report; 44 organizations) | Resource Management Institute (RTM Consulting, a Belcan company) for Kantata | vendor | https://get.kantata.com/rs/677-LEJ-696/images/AI_in_Resource_Management_Survey.pdf | 2026-04 | full |
| LAWSOCIE-SRAWARN-2026 | SRA issues warning notice on use of AI (Law Society of Ireland Gazette report of the SRA notice) | Law Society of Ireland Gazette | press | https://www.lawsociety.ie/gazette/top-stories/2026/august/sra-issues-warning-notice-on-use-of-ai/ | 2026-08 | full |
| MCA-SURVEY-2026 | MCA Member Survey 2026 | Management Consultancies Association | professional-body | https://www.mca.org.uk/reports/mca-member-survey-2026 | 2026-01-20 | full |
| NATLAW-AIHIRING-2026 | Patchwork AI Hiring Laws Create Rising Compliance Risks for Employers (Andrew Adams, Darrow Everett LLP; written before Colorado SB26-189 was signed) | The National Law Review | press | https://natlawreview.com/article/patchwork-ai-hiring-laws-create-rising-compliance-risks-employers | 2026-05-12 | full |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER Working Paper 35720) | National Bureau of Economic Research (Autor, Rodchenko, Martin, Iscenko, Strand, Pearl, Ferere) | academic | https://www.nber.org/papers/w35720 | 2026-09 | full |
| NBER-BRYNJOLFSSON-2025 | Generative AI at Work (NBER Working Paper 31161; Quarterly Journal of Economics 140(2), 889-942) | National Bureau of Economic Research (Brynjolfsson, Li, Raymond) | academic | https://www.nber.org/papers/w31161 | 2025 | full |
| NBER-DELLACQUA-2025 | The Cybernetic Teammate: A Field Experiment on Generative AI Reshaping Teamwork and Expertise (NBER Working Paper 33641; Organization Science, online June 2026) | National Bureau of Economic Research (Dell'Acqua et al.) | academic | https://www.nber.org/papers/w33641 | 2025-04 | full |
| NBER-HUMLUM-2025 | Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI (NBER Working Paper 33777; earlier title 'Large Language Models, Small Labor Market Effects') | National Bureau of Economic Research (Humlum, Vestergaard) | academic | https://www.nber.org/papers/w33777 | 2025-05 | full |
| NYC-LL144-2023 | Automated Employment Decision Tools (AEDT), Local Law 144 of 2021 | New York City Department of Consumer and Worker Protection | regulator | https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page | 2023-07 | full |
| OSC-LL144-2025 | Enforcement of Local Law 144 - Automated Employment Decision Tools (Report 2024-N-6) | Office of the New York State Comptroller, Division of State Government Accountability | regulator | https://www.osc.ny.gov/files/state-agencies/audits/pdf/sga-2026-24n6.pdf | 2025-12 | full |
| SPI-AI-2026 | The 2026 Impact of AI on Professional Services (report landing page; report itself not opened) | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-10 | full |
| STANFORD-CANARIES-2026 | Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence (August 2026 version) | Stanford Digital Economy Lab / NBER (Brynjolfsson, Chandar, Chen) | academic | https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf | 2026-08 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 (AI to Scale pathway) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026-09-30 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-LFFI-Q2-2026 | Q2 2026 LFFI: A heavier load, yet a faster crossing | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed | 2026-08-10 | full |
| TRI-TEAMS-2025 | How companies are fostering the creation of human & AI agent teams | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/creating-human-ai-agent-teams | 2025-10-22 | full |
| UK-DUAA-2025 | Data (Use and Access) Act 2025, section 80 (automated decision-making; new UK GDPR Articles 22A-22D) | UK Parliament (legislation.gov.uk) | regulator | https://www.legislation.gov.uk/ukpga/2025/18/section/80 | 2025-06-19 | full |

## 6. Gaps

- No named professional services firm publishes a measured result (error, override, acceptance, time-to-staff, utilization change) for AI in staffing. Grade A is therefore empty, and the only independent trial is adjacent (public-sector case assignment).
- Vendor products named in the landscape were not opened beyond Certinia's page: Kantata's Expertise Agent, Agent Studio and "superagent" posts, Deltek and Rocketlane tooling.
- SPI's full 2026 reports are paywalled (only the landing page and two vendor relays were read); the Dayshape report itself was not opened (Onrec summary only); Kantata's State of the Professional Services Industry report was read through a CPA Practice Advisor article, not the report.
- americanbar.org returned 403; ABA Formal Opinion 512 was read from a LawSites-hosted copy of the PDF. The SRA's own pages and the BSB guidance were not reachable; the SRA warning notice is known through the Law Society of Ireland Gazette.
- Studies on bias in assignment of work at law firms (ABA Commission on Women, Minority Corporate Counsel Association) appeared in search results but could not be opened, so they are not cited. This evidence matters for allocation fairness.
- Scope questions unresolved in the sources read: whether NYC Local Law 144, Illinois HB 3773 and Colorado SB26-189 cover work assignment; whether skills-and-availability matchers are inside EU Annex III 4(b); commencement of the UK Data (Use and Access) Act ADM provisions. The Commission's Annex III classification guidance was not read. None of this is legal advice.
- The Mobley v. Workday docket (vendor liability for AI screening) appeared in search results with conflicting 2026 detail; only the National Law Review summary of the case (as of May 2026) is cited.
- No client outside-counsel guideline or consulting contract text was found that deals with named-staff or key-personnel commitments in the presence of AI.
- No AICPA, ICAEW, or state-bar opinion specific to AI in staffing or resource allocation was found; ISQM 1 text was not opened.
- Job postings for resource-management or capacity-planning AI roles, works-council or union positions, and CLOC/in-house staffing benchmarks (CLOC SOTI is members-only) were not examined.
