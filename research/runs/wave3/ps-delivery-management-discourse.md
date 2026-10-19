# professional-services / delivery-management / discourse

Prepared 2026-10-19. Archetype: professional-services. Module: delivery-management (running engagements: project planning, status and risk tracking, client reporting, change control and engagement economics during delivery). Angle: discourse (what practitioners are saying). Method: `curl`, `pdftotext` and the r.jina.ai text mirror in a private `mktemp -d` working folder; 18 web searches. Every source below was opened and read unless the Sources table marks it `search-only`. Podcast entries are episode descriptions only; no audio or transcript was available. In-house or shared-service examples are tagged `in-house`.

## 1. Summary

The public discourse on AI in engagement delivery is dominated by two voices: professional-services-automation (PSA) vendors announcing agents, and conference and trade-press accounts of firms that are still working out what AI costs and what it saves. Practitioner voices on the actual running of engagements (project managers, PMO leads, legal project managers) are thin. Where they speak, they say AI is an assistant for admin and reporting, and that agentic monitoring is aspirational. There is no grade A evidence in this module: no named organization has published a tracked delivery outcome (hours, overrun rate, margin) attributable to AI.

- **Reporting and monitoring are the first targets, and the claims are vendor claims.** PwC published a solution page for AI-generated PMO status reports (24 Mar 2026) that estimates "approximately 40%" less administrative project overhead (PWC-STATUS-2026). Certinia, Kantata, Rocketlane and Harvey all announced or extended agents for project health, anomaly flagging, plan generation or matter orchestration between Dec 2025 and Oct 2026 (IA-CERTINIA-2025; ERPTODAY-KANTATA-2026; TANDEM-2026; HARVEY-ORCH-2026). Only Certinia names customers (Siemens, Diabsolut), and only as unmeasured testimonials (CERTINIA-VEDA-2026).
- **The baseline the tools address is weak delivery economics.** The SPI Research 2026 benchmark (500+ firms, published via Deltek 30 Jul 2026) reports billable utilization of 66.4% in 2025 (record low), on-time project delivery of 73.8%, and project overrun of 10.7%, above the 10% level SPI says harms client relationships (DELTEK-SPI-2026). Kantata's sponsored survey of 200 leaders reports 54% say at least 10% of their projects miss budget goals (KANTATA-SOPSI-2026).
- **Data trust is the stated constraint.** In the same Kantata survey only 12% of leaders fully trust their systems' data (down from 24%), and 89% say they spend significant time verifying AI outputs (KANTATA-SOPSI-2026). An independent interview study of 12 Finnish IT project-management consultants found GenAI use "fragmented and peripheral", limited mainly by organisational policies rather than individual resistance, with agents seen as assistants rather than peers (EINF-2026).
- **Engagement economics is where the new discussion is.** At ILTACON 2026 firms began to count usage-based AI costs and asked how to attribute them to a client (TRI-METER-2026). At Legalweek 2026 clients asked for matter-level proof of AI savings, and firm speakers said they were "still gathering the data" (TRI-LEGALWEEK-2026). At an ILTACON 2026 panel of over 50 attendees, none said their team had a strong measure of AI ROI (TRI-IMPL-2026).
- **Governance language is converging on reversibility and audit trails.** An ILTACON 2026 panel framed delegation as a "two-way door" test: an agent summarizing client emails and drafting an action plan is reversible, an agent replying to clients without review is not (TRI-AGENTIC-2026). PMI published a standard for AI in project work on 9 Jun 2026; it covers governing AI initiatives, not using AI to run projects (PMI-AISTD-2026).

Two most important insights: (1) the agent claims cluster on admin-heavy steps (status drafts, anomaly flags, plan generation, meeting actions) where a person can still review, while the high-value steps (scope judgment, client conversation, margin decisions) are described as human; (2) the missing capability is measurement: matter-level cost, time and outcome data. Without it neither the vendors' savings claims nor clients' savings demands can be tested.

## 2. Use cases

```yaml
- id: professional-services-delivery-management-01
  title: Draft engagement status reports and client updates from project data and team communications
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [data-reporting, document-production, coordination-scheduling]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Project managers spend hours each week pulling notes, documents and tool data into weekly client updates and internal status packs, with one-off formatting that is hard to keep consistent across workstreams."
  solution: "A model grounded in the engagement's own sources (project tool data, documents, channel messages, calendar) drafts the status report or client update in a standard format; the project manager edits and sends. PwC describes a solution that combines open-source language models with retrieval-augmented generation over 'semi-structured project data'. A vendor guide describes a scheduled agent that drafts a weekly client email from team channels, the shared drive and the calendar. Certinia lists configurable AI project summaries in an early-adopter release."
  outcomes:
    - lever: capacity
      description: "PwC's published estimate of reduced administrative effort from automating PMO status reporting"
      figure: "approximately 40% lower administrative project overhead; estimated 120 hours saved annually per resource; USD 7,000 to 24,000 projected annual savings per resource"
      measures: "PwC's wording: reduction in 'administrative project overhead' from manual status reporting, with hours and dollars 'estimated' or 'projected' per resource; baseline, sample, customers and period are not stated"
      provenance: vendor-published
      source_ref: PWC-STATUS-2026
  prerequisites:
    - "Project data in accessible systems or channels the drafting tool is permitted to read (PWC-STATUS-2026; EDNA-STATUS-2026)"
    - "A defined report format and tone written down so the draft can follow it (EDNA-STATUS-2026)"
    - "Client and security policies that allow engagement data to reach the model; interviewees avoided sharing confidential material with GenAI tools under NDAs (EINF-2026, Table 6, p.14)"
  risks_and_guardrails:
    - "Grounding in source data is PwC's stated mechanism for 'more accurate, explainable updates'; no accuracy or error rate is published (PWC-STATUS-2026)"
    - "Drafting a summary is a reversible step, but sending a client reply with no human review is a one-way door (TRI-AGENTIC-2026)"
    - "Interviewees found GenAI email drafts needed substantial editing, and one reported low-quality output that had to be abandoned for manual work (EINF-2026, §4.2 p.8 and §4.4.5 p.11)"
  human_checkpoints:
    - "Project manager reads and edits the draft before it is sent (EDNA-STATUS-2026)"
    - "Experienced project managers keep delivery oversight, risk management and issue resolution (PWC-STATUS-2026)"
  role_evolution: "PwC says automation frees experienced project managers for delivery oversight, risk management and proactive issue resolution (PWC-STATUS-2026). A PM-profession newsletter argues PMO value moves from producing reports to interpreting them, and that PMs who mainly consolidate reports 'should be concerned' (VARGAS-NEWS-2026). Both are opinion or vendor statements; no measured role change was found."
  evidence_grade: C
  sources:
    - { ref: PWC-STATUS-2026, title: "Manual PMO Status Reporting Is Draining 40% of Project Management Hours. This AI Automates It.", publisher: PwC US, type: firm, url: "https://www.pwc.com/us/en/tech-effect/innovation/automate-pmo-status-reporting.html", date: 2026-03-24, access: full, locator: "intro paragraphs; 'What this delivers for PMO leaders and teams'" }
    - { ref: EDNA-STATUS-2026, title: "How to Cut Status Update Time by 70% in Consulting", publisher: Enterprise DNA, type: vendor, url: "https://enterprisedna.co/resources/guides/consulting-reduce-time-status-updates", date: 2026-10-19, access: full, locator: "'The Real Cost of Manual Status Updates'; 'What an AI Agent Does Differently' (page undated; accessed date shown)" }
    - { ref: IA-CERTINIA-2025, title: "Certinia Announces Winter 2026 Release", publisher: Insightful Accountant, type: press, url: "https://blog.insightfulaccountant.com/certinia-announces-winter-2026-release", date: 2025-12-10, access: full, locator: "bullet 'Customize Generative AI Summaries (PS Cloud)'; early-adopter note" }
    - { ref: EINF-2026, title: "Realising the Role of Generative AI Among Project Management Professionals", publisher: e-Informatica Software Engineering Journal 20(1), type: academic, url: "https://www.e-informatyka.pl/EISEJ/papers/2026/1/4/eInformatica2026Art04.pdf", date: 2026-04-23, access: full, locator: "§4.4.1 'Report automation' p.10; §4.2 p.8; Table 6 p.14" }
    - { ref: VARGAS-NEWS-2026, title: "Issue #32 - Are AI Agents the Future of Project Management?", publisher: Ricardo Vargas newsletter, type: community, url: "https://ricardo-vargas.com/newsletter/issue-32-are-ai-agents-the-future-of-project-management/", date: 2026-06-29, access: full, locator: "sections on PMO effort and the value of the project manager" }
    - { ref: TRI-AGENTIC-2026, title: "ILTACON 2026: Who's leading the flock? Balancing agentic AI automation and human oversight", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-agentic-ai-automation", date: 2026-09-14, access: full, locator: "section 'Reversibility and the one- or two-way door test'" }
  last_reviewed: 2026-10-19
  notes: "Vendor-guide figures (6-8 hours a week per PM; 45 minutes cut to about 2) are illustrative scenarios from an unnamed 12-person firm, not measurements, and are not used as outcomes. PwC's page does not say whether the solution runs on PwC's own engagements or only on client engagements."

- id: professional-services-delivery-management-02
  title: Project assistant agent that flags missing time cards, overdue items and slipping milestones for the project manager
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [coordination-scheduling, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: "Project managers chase status and hygiene by hand: missing time entries, overdue tasks, milestones heading for trouble. Problems surface late, after margin or schedule is already hit."
  solution: "A PSA-resident agent scans project records on a schedule and surfaces data anomalies and variances to the project manager. Certinia describes a Project Assistant Agent for missing time cards, overdue project items and milestones nearing critical status, and an agent that produces digests on financials, risks and timeline variances. Siemens Digital Industries's customer-success leader says Certinia's Project Agent is helping identify deliverable discrepancies early. Kantata describes an agent aimed at spotting at-risk projects before margins erode."
  outcomes:
    - lever: risk
      description: "none published; customer statements are testimonials without figures"
      figure: "none"
      measures: "not applicable"
      provenance: vendor-published
      source_ref: CERTINIA-VEDA-2026
  prerequisites:
    - "Time, task and financial data kept in the PSA; Kantata's survey says only 12% of leaders fully trust their systems' data (KANTATA-SOPSI-2026)"
    - "Time-entry discipline: the agent flags gaps but does not create the entries (IA-CERTINIA-2025)"
  risks_and_guardrails:
    - "An agent acts only on what the PSA contains; decisions and warning signs held in calls, chat and email are invisible to it (TANDEM-2026, a competitor's argument)"
    - "Most 2026 'agentic' PSA launches are, in one vendor's assessment, summarization or scoring dressed as execution (TANDEM-2026)"
  human_checkpoints:
    - "Project manager acts on the flag; the agent surfaces anomalies but does not change records (IA-CERTINIA-2025)"
  role_evolution: "Certinia says the agent 'elevates' project managers by reducing administrative overhead (IA-CERTINIA-2025). No data on changed workload was found."
  evidence_grade: B
  sources:
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI solutions (Veda agents)", publisher: Certinia, type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10-19, access: full, locator: "agent catalogue (Project Assistant; PMO Quality); customer quotes (Siemens, Diabsolut). Page undated; accessed date shown" }
    - { ref: IA-CERTINIA-2025, title: "Certinia Announces Winter 2026 Release", publisher: Insightful Accountant, type: press, url: "https://blog.insightfulaccountant.com/certinia-announces-winter-2026-release", date: 2025-12-10, access: full, locator: "bullet 'Improve project health and margins with AI (PS Cloud)'; early-adopter note" }
    - { ref: ERPTODAY-KANTATA-2026, title: "Kantata's Expertise Agent Targets the Professional Services Delivery Crunch", publisher: ERP Today, type: press, url: "https://erp.today/kantata-expertise-agent-psa-ai/", date: 2026-06-19, access: full, locator: "paragraphs 1-4 (launch 16 Jun 2026; example use cases)" }
    - { ref: KANTATA-SOPSI-2026, title: "Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce", publisher: Kantata (survey by Censuswide, 200 leaders), type: survey, url: "https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce", date: 2026-01-08, access: full, locator: "paragraph on data trust; methodology note" }
    - { ref: TANDEM-2026, title: "Agentic PSA in 2026: what execution agents actually change, and a buyer's guide to who delivers", publisher: Tandem, type: vendor, url: "https://usetandem.ai/blog/agentic-psa-buyers-guide-2026", date: 2026-08-19, access: full, locator: "'The four capability levels hiding under one label'; 'What execution agents actually change'" }
  last_reviewed: 2026-10-19
  notes: "Grade B rests on named customer testimonials (Siemens Digital Industries customer success, `in-house`; Diabsolut professional services) on a vendor page. They do not state production status or give figures. Certinia's Dec 2025 release note lists the Project Assistant Agent under its early-adopter programme, so 'piloting' is the conservative maturity. The page names the Siemens product 'Project Agent'; whether this is the same agent as 'Project Assistant' is not stated."

- id: professional-services-delivery-management-03
  title: Score project health and client sentiment from scope scans and communications for PMO leaders
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [data-reporting, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "PMO leaders learn that a project is in trouble from late status reports or a client escalation; RAG ratings depend on each project manager's judgment."
  solution: "An agent regularly scans project scope and activity and assigns a health or sentiment score, so PMO leaders can steer before risks materialize. Certinia describes automated scope scans and real-time sentiment scoring (PMO Quality Agent). Another PSA vendor is described as scoring project risk with a retrieval-based coach. A competing vendor says most such launches are summarization or scoring rather than execution."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "not applicable"
      provenance: vendor-published
      source_ref: CERTINIA-VEDA-2026
  prerequisites:
    - "Consistent project records for the scan to read; where decisions live in calls and chat, a PSA-only scan sees a partial picture (TANDEM-2026)"
    - "A PMO that owns the scoring method and acts on it (VARGAS-NEWS-2026)"
  risks_and_guardrails:
    - "Scores are only as good as the underlying data; Kantata's survey reports 12% of leaders fully trust their systems' data (KANTATA-SOPSI-2026)"
    - "A competing vendor advises asking which capability level each named agent operates at, in production, for named customers (TANDEM-2026)"
  human_checkpoints:
    - "PMO leader decides on intervention; the score informs, it does not trigger action (CERTINIA-VEDA-2026)"
  role_evolution: "A PM-profession newsletter expects PMOs to spend less time gathering information and more on interpretation and decisions, without data (VARGAS-NEWS-2026)."
  evidence_grade: C
  sources:
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI solutions (Veda agents)", publisher: Certinia, type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10-19, access: full, locator: "'Margin protection & risk management'; agent list (PMO Quality Agent). Page undated; accessed date shown" }
    - { ref: TANDEM-2026, title: "Agentic PSA in 2026: what execution agents actually change, and a buyer's guide to who delivers", publisher: Tandem, type: vendor, url: "https://usetandem.ai/blog/agentic-psa-buyers-guide-2026", date: 2026-08-19, access: full, locator: "'The four capability levels'; buyer's guide entries for GUIDEcx and Kantata" }
    - { ref: KANTATA-SOPSI-2026, title: "Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce", publisher: Kantata (survey by Censuswide, 200 leaders), type: survey, url: "https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce", date: 2026-01-08, access: full, locator: "paragraph on data trust" }
    - { ref: VARGAS-NEWS-2026, title: "Issue #32 - Are AI Agents the Future of Project Management?", publisher: Ricardo Vargas newsletter, type: community, url: "https://ricardo-vargas.com/newsletter/issue-32-are-ai-agents-the-future-of-project-management/", date: 2026-06-29, access: full, locator: "sections on the PMO of the future" }
  last_reviewed: 2026-10-19
  notes: "No accuracy test of any health score against later project outcomes was found. Change scope is set to process because scoring replaces periodic self-reported ratings with continuous scans; the sources do not describe a redesigned governance flow."

- id: professional-services-delivery-management-04
  title: Generate project plans from the SOW and hand over from sale to delivery
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [coordination-scheduling, document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Delivery teams start from a signed SOW and a salesperson's recollection; plans are rebuilt by hand and context is lost at the sales-to-delivery handoff. Deltek's summary of the SPI benchmark lists streamlining the sales-to-delivery handoff as a way to convert pipeline into delivered work."
  solution: "Agents turn the SOW and sales briefing into a draft project plan and connect closed deals to delivery kickoff. Certinia lists Implementation Plan and Sales-to-Delivery Handoff agents; Kantata says its agent can generate project plans from SOWs and briefings and preserve knowledge during handoffs. Interviewed IT project managers use GenAI to structure work phases, though one test with Gemini on a migration framework was not put into practice."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none"
      measures: "not applicable"
      provenance: vendor-published
      source_ref: ERPTODAY-KANTATA-2026
  prerequisites:
    - "SOWs and sales notes written in a form the agent can use; the plan draws on the firm's delivery history (ERPTODAY-KANTATA-2026)"
    - "A PSA or equivalent system to receive the plan (CERTINIA-VEDA-2026)"
  risks_and_guardrails:
    - "Interviewees said GenAI struggles to grasp organisational context and can hallucinate, so plans need human review (EINF-2026, Table 6 p.14)"
  human_checkpoints:
    - "Project manager reviews and approves the plan before kickoff (EINF-2026, §5.5 p.15: assistant tasks that can be controlled and verified)"
  role_evolution: "No source describes a role change for this step."
  evidence_grade: C
  sources:
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI solutions (Veda agents)", publisher: Certinia, type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10-19, access: full, locator: "agent list: Sales-to-Delivery Handoff Agent; Implementation Plan. Page undated; accessed date shown" }
    - { ref: ERPTODAY-KANTATA-2026, title: "Kantata's Expertise Agent Targets the Professional Services Delivery Crunch", publisher: ERP Today, type: press, url: "https://erp.today/kantata-expertise-agent-psa-ai/", date: 2026-06-19, access: full, locator: "paragraph 'Kantata is positioning Expertise Agent...' (example use cases)" }
    - { ref: DELTEK-SPI-2026, title: "2026 PSO Benchmarks: What We Learned and What's Next from the SPI Maturity Benchmark Report", publisher: Deltek (SPI Research data), type: survey, url: "https://www.deltek.com/resources/articles/professional-services-benchmarks/", date: 2026-07-30, access: full, locator: "'Continuing the Focus on Conversion'" }
    - { ref: EINF-2026, title: "Realising the Role of Generative AI Among Project Management Professionals", publisher: e-Informatica Software Engineering Journal 20(1), type: academic, url: "https://www.e-informatyka.pl/EISEJ/papers/2026/1/4/eInformatica2026Art04.pdf", date: 2026-04-23, access: full, locator: "§4.2 'Planning and strategy' p.8; Table 6 p.14; §5.5 p.15" }
  last_reviewed: 2026-10-19
  notes: "SOW drafting itself is a scoping step and is routed to scoping-pricing. Vendor pages describe capability, not use at a named customer."

- id: professional-services-delivery-management-05
  title: Detect scope drift in client requests and prompt a change order
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [coordination-scheduling, client-interaction, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "Scope expands through chat messages, hallway asks and emails that start 'quick question'. Change orders are often written after the extra work is done, and the in-scope call is subjective."
  solution: "An agent holds the SOW, plan and deliverable list, reads client requests as they arrive and compares them with agreed scope. Clear in-scope requests pass; clearly out-of-scope ones notify the project manager; ambiguous ones are surfaced with context for a human decision. It also tracks cumulative drift against the plan and alerts the engagement lead when margin is at risk. A vendor guide describes this; a competing vendor suggests testing for it by introducing a scope change agreed by email and watching which system notices."
  outcomes:
    - lever: cost
      description: "Illustrative scenario in a vendor guide (not a measured result): scope growth that the monitoring is meant to catch"
      figure: "USD 120,000 project scoped at 400 hours that ran to 520 hours, described as USD 36,000 of margin given back"
      measures: "vendor's worked example of a single hypothetical project; no firm, sample or period"
      provenance: vendor-published
      source_ref: EDNA-SCOPE-2026
  prerequisites:
    - "Structured SOW and deliverable list the agent can compare against (EDNA-SCOPE-2026)"
    - "Permitted read access to client-facing channels (chat, email, project tool); client confidentiality terms must allow it (EINF-2026, Table 6 p.14)"
    - "A firm view of what counts as in scope: the guide says partners interpret SOW wording differently (EDNA-SCOPE-2026)"
  risks_and_guardrails:
    - "Scope judgment is subjective; ambiguous cases go to a person (EDNA-SCOPE-2026)"
    - "Manual change-control boards trade margin protection against client responsiveness; the guide claims the agent avoids that trade, with no evidence (EDNA-SCOPE-2026)"
    - "One project-management vendor says unrecovered scope creep is one of four leak points in delivery margin (TEAMWORK-2026)"
  human_checkpoints:
    - "Project manager makes the final call on every flagged request (EDNA-SCOPE-2026)"
    - "Engagement lead decides whether to open a scope conversation with the client, re-resource or push back (EDNA-SCOPE-2026)"
  role_evolution: "The guide says project managers keep the decision but make it earlier and with fuller information (EDNA-SCOPE-2026). No data."
  evidence_grade: C
  sources:
    - { ref: EDNA-SCOPE-2026, title: "How to Reduce Consulting Project Scope Creep with AI", publisher: Enterprise DNA, type: vendor, url: "https://enterprisedna.co/resources/guides/consulting-reduce-scope-creep", date: 2026-10-19, access: full, locator: "intro; 'What AI Monitoring Looks Like in Practice'; 'Automated Alerts That Protect Margin' (page undated; accessed date shown)" }
    - { ref: TANDEM-2026, title: "Agentic PSA in 2026: what execution agents actually change, and a buyer's guide to who delivers", publisher: Tandem, type: vendor, url: "https://usetandem.ai/blog/agentic-psa-buyers-guide-2026", date: 2026-08-19, access: full, locator: "'Running the evaluation', step 3 'Break something on purpose'" }
    - { ref: TEAMWORK-2026, title: "Margin erosion in professional services: how to fix it", publisher: Teamwork.com, type: vendor, url: "https://www.teamwork.com/blog/margin-erosion-professional-services/", date: 2026-09-24, access: full, locator: "summary bullets ('four leak points'); 'The margin erosion gap'" }
    - { ref: EINF-2026, title: "Realising the Role of Generative AI Among Project Management Professionals", publisher: e-Informatica Software Engineering Journal 20(1), type: academic, url: "https://www.e-informatyka.pl/EISEJ/papers/2026/1/4/eInformatica2026Art04.pdf", date: 2026-04-23, access: full, locator: "Table 6 p.14 (confidentiality)" }
  last_reviewed: 2026-10-19
  notes: "Grade C: vendor guides only. The guide cites 'one advisory firm in our network' without a name. No false-positive or missed-scope rate is published anywhere. Closest practitioner voice is the Finnish PM study, whose interviewees wanted deviation alerts but had not used them (EINF-2026, §4.4.4 p.11)."

- id: professional-services-delivery-management-06
  title: See engagement margin and budget burn while the work is under way
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "Margin leaks during delivery (underbids, unrecovered scope, wrong-rate staffing, unlogged time) but leadership sees it in a report after month-end, when it cannot be recovered."
  solution: "PSA vendors position AI on live project, resource and financial data to give delivery leaders current cost and margin and early warning of slippage. Certinia describes conversational visibility into financials, risk and task status in place of status-chasing; Kantata describes finding at-risk projects before margins erode. Teamwork frames the problem as an 'erosion gap' between when margin is lost and when leadership can see it."
  outcomes:
    - lever: risk
      description: "Baseline the tools address: project overrun and on-time delivery across surveyed firms (not an AI result)"
      figure: "project overrun 10.7% in 2025 (11.3% in 2024); on-time project delivery 73.8% (73.4% in 2024); project margin 37.7%"
      measures: "SPI Research 2026 Professional Services Maturity Benchmark, 500+ firms; metrics as defined by SPI (overrun relative to plan; on-time delivery rate); SPI treats overrun above 10% as damaging to client relationships and bookings"
      provenance: vendor-published
      source_ref: DELTEK-SPI-2026
    - lever: risk
      description: "Self-reported budget misses in a vendor-sponsored survey"
      figure: "54% report that at least 10% of their projects miss budget goals"
      measures: "share of 200 surveyed professional-services leaders who say at least 10% of projects miss budget goals (Censuswide survey for Kantata)"
      provenance: vendor-published
      source_ref: KANTATA-SOPSI-2026
  prerequisites:
    - "Time, expense and cost data captured promptly; billable utilization of 66.4% suggests substantial unrecorded or unbillable time (DELTEK-SPI-2026)"
    - "Integrated systems: SPI reports firms on a project-based ERP had faster revenue growth and higher EBITDA, and disconnected tools give weaker visibility (DELTEK-SPI-2026)"
  risks_and_guardrails:
    - "SPI links deeper AI use with revenue growth, headcount growth and on-time delivery, but publishes no figure for the link in the article, and it is a survey association, not a controlled test (DELTEK-SPI-2026)"
    - "Teamwork says AI compresses billable hours faster than it cuts cost, which widens the erosion problem (TEAMWORK-2026)"
  human_checkpoints:
    - "Delivery leader decides intervention (re-scope, re-staff, change order) (CERTINIA-VEDA-2026)"
  role_evolution: "No source describes a role change for this step."
  evidence_grade: C
  sources:
    - { ref: DELTEK-SPI-2026, title: "2026 PSO Benchmarks: What We Learned and What's Next from the SPI Maturity Benchmark Report", publisher: Deltek (SPI Research data), type: survey, url: "https://www.deltek.com/resources/articles/professional-services-benchmarks/", date: 2026-07-30, access: full, locator: "sections 2, 4, 5 and 6 of 'Zooming Out'" }
    - { ref: KANTATA-SOPSI-2026, title: "Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce", publisher: Kantata (survey by Censuswide, 200 leaders), type: survey, url: "https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce", date: 2026-01-08, access: full, locator: "paragraph beginning 'Those gains are becoming increasingly critical'" }
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI solutions (Veda agents)", publisher: Certinia, type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10-19, access: full, locator: "'Run the business behind every engagement': 'See the business as it actually is'. Page undated; accessed date shown" }
    - { ref: TEAMWORK-2026, title: "Margin erosion in professional services: how to fix it", publisher: Teamwork.com, type: vendor, url: "https://www.teamwork.com/blog/margin-erosion-professional-services/", date: 2026-09-24, access: full, locator: "summary bullets; 'The margin erosion gap'" }
    - { ref: ERPTODAY-KANTATA-2026, title: "Kantata's Expertise Agent Targets the Professional Services Delivery Crunch", publisher: ERP Today, type: press, url: "https://erp.today/kantata-expertise-agent-psa-ai/", date: 2026-06-19, access: full, locator: "paragraph 'Kantata is positioning Expertise Agent...'" }
  last_reviewed: 2026-10-19
  notes: "The 27.1% of projects using GenAI in 2025 (SPI benchmark via Deltek) and the 23.1% to 43.6% figures on the SPI AI study page come from two different SPI studies and should not be combined. Teamwork's 35%-to-18% margin example is illustrative, not measured."

- id: professional-services-delivery-management-07
  title: Run a matter or engagement from a reusable template with agent-executed tasks and named review gates
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [coordination-scheduling, document-production, review-assurance]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "Each new matter's process is rebuilt from a checklist, a previous deal or someone's memory. Lawyers gather documents, write instructions for each AI step and carry outputs between steps; partners ask associates to reconstruct status from email."
  solution: "Harvey's Legal Work Orchestration (announced 15 Oct 2026) captures a recurring matter type as a template of phases, tasks, playbooks, agents, collaborators and review gates. Each task carries its scope, inputs and reviewer; an agent runs the task (for example a change-of-control review producing a consent matrix); the designated partner is notified and approves; the next step opens. Tasks can go to another lawyer or the client, and a workspace shows current status. Tasks, comments and notifications are rolling out; templates are in early access."
  outcomes:
    - lever: capacity
      description: "Harvey's own forecast of the share of workflow steps agents will take on (an expectation, not a measurement)"
      figure: "expects agents to take on an additional 20% of workflow steps over six months, and that share to triple within a year"
      measures: "Harvey's stated expectation of the share of workflow steps executed by agents instead of prompted by lawyers; no baseline or customer data"
      provenance: vendor-published
      source_ref: HARVEY-ORCH-2026
  prerequisites:
    - "Innovation or knowledge teams define the template once; Harvey says this lets teams follow a consistent process without rebuilding (HARVEY-ORCH-2026)"
    - "Governed data, documented processes and clear integrations: agents are less forgiving than GenAI of undocumented workflows (TRI-PREMORTEM-2026)"
  risks_and_guardrails:
    - "Harvey says agent work stays transparent and auditable and lawyers remain in control through review gates (HARVEY-ORCH-2026)"
    - "Panel advice: define permissible use cases that allow reversibility, require an audit trail and decision tracing, and do not let individual lawyers create new agents on their own (TRI-AGENTIC-2026)"
    - "A commentary scenario shows human review turning into 'theater' when reviewers approve workflows they cannot parse (TRI-PREMORTEM-2026, a fictional premortem)"
  human_checkpoints:
    - "Designated partner or reviewer approves each task at its review gate before the next step begins (HARVEY-ORCH-2026)"
  role_evolution: "Harvey says lawyers can focus more on directing the matter, reviewing consequential outputs and exercising judgment as agents take on execution (HARVEY-ORCH-2026). An Artificial Lawyer guest post forecasts that agents able to orchestrate workflow erode the mid-level associate role, which it calls the legal world's project managers; this is a forecast from the author of a green paper (AL-LADDER-2026)."
  evidence_grade: C
  sources:
    - { ref: HARVEY-ORCH-2026, title: "Making Harvey the Orchestration Layer for Legal Work", publisher: Harvey, type: vendor, url: "https://www.harvey.ai/blog/legal-work-orchestration", date: 2026-10-15, access: full, locator: "sections 'How Legal Orchestration Works' and closing paragraphs" }
    - { ref: TRI-AGENTIC-2026, title: "ILTACON 2026: Who's leading the flock? Balancing agentic AI automation and human oversight", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-agentic-ai-automation", date: 2026-09-14, access: full, locator: "section 'Reversibility and the one- or two-way door test'" }
    - { ref: TRI-PREMORTEM-2026, title: "Premortem: Your 2028 agentic AI pilot program failed", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/spotlight/premortem-your-2028-agentic-ai-pilot-program-failed", date: 2026-02-18, access: full, locator: "'Premortem No. 1: The eager overreacher'" }
    - { ref: ILTA-RISE-2025, title: "The Rise of AI Agents in Legal", publisher: ILTA (Pulse, ILTACON 2025), type: professional-body, url: "https://iltanet.org/resources/publications/pulse/iltacon/2025/rise-ai", date: 2025, access: full, locator: "paragraphs 4-5 (chain of agents across matter context, staffing, time, billing; audit logging)" }
    - { ref: AL-LADDER-2026, title: "Broken Ladder: Are Lawyers Sleepwalking into a Competence Crisis?", publisher: Artificial Lawyer (guest post by James Tuke, AI Futures Forum), type: press, url: "https://www.artificiallawyer.com/2026/01/30/broken-ladder-are-lawyers-sleepwalking-into-a-competence-crisis/", date: 2026-01-30, access: full, locator: "section 'The Competence Trap' and 'Age of the Digital Worker'" }
  last_reviewed: 2026-10-19
  notes: "Announced, not evidenced in use: no named firm or in-house team is reported using Legal Work Orchestration. The Legalweek 2026 session 'Agentic Ops: Building a Self-Orchestrating Legal Department' (Tue 9 Mar 2026, 3:30-4:30pm) is the `in-house` counterpart; only the session title and a one-line preview were read (EDRM-LEGALWEEK-2026). The ILTA article proposes a chain of agents from staffing to billing as a concept, not a deployment."

- id: professional-services-delivery-management-08
  title: Turn meeting transcripts and workshops into action items, decisions and follow-ups
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [document-production, coordination-scheduling]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Meeting minutes, action lists and workshop outputs are written by hand after the fact, and commitments slip."
  solution: "Project managers use the transcription and summary tools in their organisation's licensed assistant to record meetings, draft action points and group workshop outputs. In an interview study of 12 Finnish IT project-management consultants, two used meeting transcription and notes, one used AI to create action points from transcripts, and two used AI in whiteboard or Miro tools to categorize workshop results."
  outcomes:
    - lever: speed
      description: "Interviewee-reported effects, not measurements"
      figure: "none"
      measures: "participant P9 said action points from transcripts were sometimes better than manual ones but needed verification; two participants said workshop-result processing took less time; two said meeting-note quality varied with meeting complexity (EINF-2026, §4.2 pp.7-8)"
      provenance: independent
      source_ref: EINF-2026
  prerequisites:
    - "Client or employer approval of the transcription tool: client organisations largely decide which tools consultants may use (EINF-2026, §5.5 p.15)"
  risks_and_guardrails:
    - "Quality varies; interviewees treat outputs as needing verification and avoid sharing confidential material (EINF-2026, Table 6 p.14)"
  human_checkpoints:
    - "Project manager verifies action points before they are circulated (EINF-2026, §4.2 p.8)"
  role_evolution: "Interviewees converged on AI as an 'assistant not replacement' that preserves human authority (EINF-2026, abstract)."
  evidence_grade: C
  sources:
    - { ref: EINF-2026, title: "Realising the Role of Generative AI Among Project Management Professionals", publisher: e-Informatica Software Engineering Journal 20(1), type: academic, url: "https://www.e-informatyka.pl/EISEJ/papers/2026/1/4/eInformatica2026Art04.pdf", date: 2026-04-23, access: full, locator: "Table 3 p.7; §4.2 'Workshop and meeting support' p.8; §5.5 p.15" }
    - { ref: VARGAS-NEWS-2026, title: "Issue #32 - Are AI Agents the Future of Project Management?", publisher: Ricardo Vargas newsletter, type: community, url: "https://ricardo-vargas.com/newsletter/issue-32-are-ai-agents-the-future-of-project-management/", date: 2026-06-29, access: full, locator: "paragraph listing meeting documentation and action tracking" }
  last_reviewed: 2026-10-19
  notes: "Grade C is a judgment call: the evidence is an independent peer-reviewed interview study (not a vendor claim), but participants are anonymous and nothing is measured. Interviews took place Aug-Sep 2025 with Finnish IT project managers who consult across client organisations, so the process is adjacent to the legal, accounting and consulting engagements this archetype covers."

- id: professional-services-delivery-management-09
  title: Automate stakeholder reminders, calendar coordination and tool setup for project managers
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [coordination-scheduling]
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: "Project managers lose time chasing stakeholders for time sheets, agendas and deadlines, scheduling across time zones, and configuring project tools."
  solution: "Idea. Interviewees most often named calendar and meeting management as the capability they most wanted, followed by automated reminders to steering groups and partners and automation of tool configuration such as Jira setup."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none"
      measures: "not applicable"
      provenance: independent
      source_ref: EINF-2026
  prerequisites:
    - "Calendar, task and time-sheet systems that an assistant is permitted to read and act on (EINF-2026, §4.4.1 p.10)"
  risks_and_guardrails:
    - "Interviewees want control kept with the human PM and only controllable, verifiable tasks given to AI (EINF-2026, §5.5 p.15)"
  human_checkpoints:
    - "Not specified in the source beyond human control of assistant tasks"
  role_evolution: "No change described beyond relief from repetitive follow-ups."
  evidence_grade: D
  sources:
    - { ref: EINF-2026, title: "Realising the Role of Generative AI Among Project Management Professionals", publisher: e-Informatica Software Engineering Journal 20(1), type: academic, url: "https://www.e-informatyka.pl/EISEJ/papers/2026/1/4/eInformatica2026Art04.pdf", date: 2026-04-23, access: full, locator: "Table 5 p.9; §4.4.1 'Administrative automation' p.10" }
    - { ref: VARGAS-NEWS-2026, title: "Issue #32 - Are AI Agents the Future of Project Management?", publisher: Ricardo Vargas newsletter, type: community, url: "https://ricardo-vargas.com/newsletter/issue-32-are-ai-agents-the-future-of-project-management/", date: 2026-06-29, access: full, locator: "paragraph on following up overdue tasks" }
  last_reviewed: 2026-10-19
  notes: "Idea (grade D): discussed by researchers' interviewees and a PM commentator, no public deployment found for this step. Pattern set to `other`: scheduled reminders and calendar actions by a personal assistant, not covered by the listed patterns."

- id: professional-services-delivery-management-10
  title: Predictive monitoring of dependencies, deviations and risks from historical project data
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [data-reporting, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: "External project managers find dependency management and early-warning signals hard to keep up by hand; progress is analysed against baselines only when someone compiles the data."
  solution: "Idea. Interviewees envisioned an assistant that watches multi-source data against baselines, detects when dependencies cannot be met on schedule, proposes coordination actions, and drafts risk assessments from historical project data. One interviewee tested Gemini on a migration-project framework and found it identified typical risks, but had not put this into practice. A PM-profession commentator describes portfolio agents that look for patterns across hundreds of projects."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none"
      measures: "not applicable"
      provenance: independent
      source_ref: EINF-2026
  prerequisites:
    - "Historical project data and consistent baselines (EINF-2026, §4.4.4 p.11)"
    - "Integration across the tools where project truth lives (EINF-2026, abstract: integration and data protection over bottom-up experimentation)"
  risks_and_guardrails:
    - "Interviewees say human verification stays mandatory for error detection (EINF-2026, §4.4.3 and §4.4.4)"
    - "Multi-step agent reliability falls with repeated runs; one vendor cites a benchmark of about 61% single-attempt task success falling to about 25% consistency by the eighth trial (TANDEM-2026, citing Sierra tau-bench; not opened here)"
  human_checkpoints:
    - "Project manager reviews alerts and recommended actions"
  role_evolution: "Vargas argues project managers' value moves toward judgment, context and leadership as monitoring is automated (VARGAS-NEWS-2026). Interviewees see agents as supportive assistants, not peer project managers (EINF-2026, §5.5 p.15)."
  evidence_grade: D
  sources:
    - { ref: EINF-2026, title: "Realising the Role of Generative AI Among Project Management Professionals", publisher: e-Informatica Software Engineering Journal 20(1), type: academic, url: "https://www.e-informatyka.pl/EISEJ/papers/2026/1/4/eInformatica2026Art04.pdf", date: 2026-04-23, access: full, locator: "§4.2 'Planning and strategy' p.8; §4.4.4 'Intelligent monitoring' p.11" }
    - { ref: VARGAS-NEWS-2026, title: "Issue #32 - Are AI Agents the Future of Project Management?", publisher: Ricardo Vargas newsletter, type: community, url: "https://ricardo-vargas.com/newsletter/issue-32-are-ai-agents-the-future-of-project-management/", date: 2026-06-29, access: full, locator: "paragraphs imagining monitoring, meeting and portfolio agents" }
    - { ref: TANDEM-2026, title: "Agentic PSA in 2026: what execution agents actually change, and a buyer's guide to who delivers", publisher: Tandem, type: vendor, url: "https://usetandem.ai/blog/agentic-psa-buyers-guide-2026", date: 2026-08-19, access: full, locator: "'What execution agents actually change, and what they don't'" }
  last_reviewed: 2026-10-19
  notes: "Idea (grade D). Overlaps in aim with use case 03 (vendor health scoring) but differs: this is schedule and dependency analysis and risk drafting at planning, as practitioners imagine it."

- id: professional-services-delivery-management-11
  title: Attribute AI cost and agent work to a specific matter or engagement
  archetype: professional-services
  module: delivery-management
  function: finance-accounting
  work_types: [data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Firms bought AI tools by the seat but are increasingly billed by usage, across many tools and background agents nobody watches. A flat subscription cannot be traced to a client, so AI cost does not show up in matter economics."
  solution: "Idea. Metering AI use per matter makes its cost attributable to a client, so it can be budgeted, controlled, and possibly passed through like e-discovery charges. A PSA survey adds the same need on the people side: 90% of leaders expect their systems to attribute work, cost and value across humans and AI agents."
  outcomes:
    - lever: cost
      description: "Reported budgeting norm for AI spend, stated by one firm's chief data and AI officer"
      figure: "roughly 1% of revenue"
      measures: "AI cost as a share of firm revenue; the speaker said most people are settling on it and his own firm was not there yet; a panel remark, not a survey"
      provenance: self-reported
      source_ref: TRI-METER-2026
    - lever: cost
      description: "Survey expectation that systems will need to attribute work, cost and value across humans and AI agents"
      figure: "90% of leaders"
      measures: "share of 200 surveyed professional-services leaders who say their systems will need to do this 'in the near future' (Censuswide survey for Kantata)"
      provenance: vendor-published
      source_ref: KANTATA-SOPSI-2026
  prerequisites:
    - "Usage-level metering from tool vendors and a way to tag usage to a matter or client code (TRI-METER-2026)"
    - "A policy on pass-through versus overhead for AI cost"
  risks_and_guardrails:
    - "Lawyers cannot see how many tokens they spend, and reach for the largest model for small tasks (TRI-METER-2026)"
    - "Whether and how to pass AI cost through to clients is a billing-ethics question, routed to billing-collections"
    - "Law firm AI leaders surveyed by the American Lawyer see a slowdown in AI adoption as a bigger risk than price rises (AMLAW-CONSUMPTION-2026, teaser only)"
  human_checkpoints:
    - "Pricing and finance leaders decide what is passed through to clients (TRI-METER-2026)"
  role_evolution: "No source describes a role change; knowledge and innovation managers take on cost control (TRI-METER-2026)."
  evidence_grade: D
  sources:
    - { ref: TRI-METER-2026, title: "Ferraris for emails: At ILTACON 2026, the industry starts reading the meter", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter", date: 2026-09-09, access: full, locator: "sections 'The receipt is not the cost' and 'The $2 PowerPoint' and closing paragraphs" }
    - { ref: KANTATA-SOPSI-2026, title: "Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce", publisher: Kantata (survey by Censuswide, 200 leaders), type: survey, url: "https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce", date: 2026-01-08, access: full, locator: "third paragraph (attribution across humans and agents)" }
    - { ref: AMLAW-CONSUMPTION-2026, title: "AI Utilization Is 'Skyrocketing,' but Law Firms Aren't Sweating Consumption Pricing", publisher: The American Lawyer, type: press, url: "https://www.law.com/americanlawyer/2026/10/13/ai-utilization-is-skyrocketing-but-law-firms-arent-sweating-consumption-pricing-/", date: 2026-10-13, access: search-only, locator: "teaser bullet only; body paywalled" }
  last_reviewed: 2026-10-19
  notes: "Idea (grade D): discussed at ILTACON 2026, no deployed attribution found. Function set to finance-accounting because the change sits in engagement cost accounting. The Ballard Spahr speaker's point is that metering 'makes AI cost attributable to a specific client'; other speakers worried about hidden agent-to-agent spend. The American Lawyer teaser (search-only) is a counter-signal and supports no figure."

- id: professional-services-delivery-management-12
  title: Report AI use and savings to clients at matter level
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [client-interaction, data-reporting]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: "Clients, including in-house legal teams, now ask what AI is used on their matters and how much it saves; firms say they are still gathering data. Some clients ask for AI line items on invoices, others state they will not pay for work done by AI."
  solution: "Idea. Capture which tasks on a matter were done with AI and the time or cost effect, and include that in matter reporting, so the firm can answer client questions with matter-level evidence and negotiate how value is shared. Speakers also proposed changing the form of the bill. No tool or deployment is described."
  outcomes:
    - lever: experience
      description: "none published"
      figure: "none"
      measures: "not applicable"
      provenance: self-reported
      source_ref: TRI-LEGALWEEK-2026
  prerequisites:
    - "Matter-level data on how AI was used and its effect (TRI-LEGALWEEK-2026)"
    - "A firm AI strategy: a Thomson Reuters speaker said firms with one were 3.9 times more likely to achieve ROI, yet only 22% of firms had one (TRI-LEGALWEEK-2026)"
  risks_and_guardrails:
    - "Clients send both 2026 savings demands and 2023-style bans or bias warranties, often in the same inbox (TRI-LEGALWEEK-2026)"
    - "A BigHand survey reports 35% of firms cite partner discomfort in discussing AI with clients as the biggest obstacle to communicating technology use (AL-BIGHAND-2026, sponsored)"
  human_checkpoints:
    - "Partner and pricing leaders decide what is disclosed and how value is split (TRI-LEGALWEEK-2026)"
  role_evolution: "Pricing and innovation officers become the client-facing owners of AI value conversations (TRI-LEGALWEEK-2026: Greenberg Traurig's chief pricing and innovation officer speaking)."
  evidence_grade: D
  sources:
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "sections 'Proving AI's path to saving clients money', 'The contradictions in the room', 'The pressure hasn't yet found a release valve'" }
    - { ref: TRI-IMPL-2026, title: "ILTACON 2026: Does it make the boat faster? How legal teams are finding AI implementation success", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-finding-ai-implementation-success", date: 2026-08-31, access: full, locator: "section 'Metrics that matter'" }
    - { ref: AL-BIGHAND-2026, title: "AI Is Forcing Law Firms To Get Serious About Matter Economics", publisher: Artificial Lawyer (sponsored article by BigHand), type: press, url: "https://www.artificiallawyer.com/2026/09/28/ai-is-forcing-law-firms-to-get-serious-about-matter-economics/", date: 2026-09-28, access: full, locator: "section 'Don't be shy of the commercial conversation'" }
    - { ref: EDRM-LEGALWEEK-2026, title: "Legalweek 2026 select educational sessions preview", publisher: EDRM, type: conference, url: "https://edrm.net/2026/03/legalweek-2026-select-educational-sessions-preview/", date: 2026-03-06, access: full, locator: "metrics sessions: 'Measuring What Matters', 'Data That Speaks' (preview text only)" }
  last_reviewed: 2026-10-19
  notes: "Idea (grade D). Includes `in-house` voices: GSK's chief of staff for legal and compliance asked outside firms how AI generates savings (TRI-LEGALWEEK-2026). In TRI-IMPL-2026, none of an audience of over 50 said their legal team had a strong AI-ROI measure. Pricing aspects are routed to scoping-pricing. Pattern set to `other`: client-facing reporting of AI effect."

- id: professional-services-delivery-management-13
  title: Agents that execute repeatable billable delivery tasks inside the PSA (migrations, configuration, documentation, testing)
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [software-systems, document-production, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Implementation and services teams are asked to deliver more go-lives with the same headcount; billable utilization is at a record low in SPI's benchmark."
  solution: "Vendors position agents inside the PSA that do the work itself, not only track it: Rocketlane describes agents that identify risks early, rebalance resources and execute repeatable billable tasks such as migrations, configurations, documentation and testing. Kantata describes self-executing workflows and agents that create further agents. Trade press says consulting firms are repositioning around agents and subscription-style products."
  outcomes:
    - lever: capacity
      description: "Vendor-reported effort reduction in early deployments, quoted second-hand by a competitor"
      figure: "up to 50% lower delivery effort"
      measures: "Rocketlane's claim, as characterised by Tandem and attributed to an Insight Partners press piece (not opened); 'early deployments'; baseline, customers and task mix not stated"
      provenance: vendor-published
      source_ref: TANDEM-2026
  prerequisites:
    - "Rule-heavy, repeatable task types in a PSA that the agent can run end to end with approval (TANDEM-2026)"
    - "Governance on which actions agents take autonomously, which need approval, how AI work is costed and how decisions are audited (ERPTODAY-KANTATA-2026)"
  risks_and_guardrails:
    - "Ask what happens when the agent is wrong and who approves before an agent touches a customer environment (TANDEM-2026)"
    - "Per-seat pricing plus consumption credits can change total cost as agent usage grows (TANDEM-2026)"
  human_checkpoints:
    - "Human gate and audit trail for every agent action touching a customer environment (TANDEM-2026, vendor's evaluation criterion)"
  role_evolution: "ERP Today says firms will need governance models for mixed human-and-agent workforces (ERPTODAY-KANTATA-2026). Trade press reports the Big Four hiring technologists and PwC creating an engineering career track in early 2026, citing Business Insider (MARKETSCALE-2026, secondary)."
  evidence_grade: C
  sources:
    - { ref: TANDEM-2026, title: "Agentic PSA in 2026: what execution agents actually change, and a buyer's guide to who delivers", publisher: Tandem, type: vendor, url: "https://usetandem.ai/blog/agentic-psa-buyers-guide-2026", date: 2026-08-19, access: full, locator: "TL;DR; 'What is an agentic PSA?'; 'What execution agents actually change, and what they don't'" }
    - { ref: ERPTODAY-KANTATA-2026, title: "Kantata's Expertise Agent Targets the Professional Services Delivery Crunch", publisher: ERP Today, type: press, url: "https://erp.today/kantata-expertise-agent-psa-ai/", date: 2026-06-19, access: full, locator: "sections 'Agentic PSA Tests New Operating Model' and 'Professional Services Firms Face AI Workforce Shift'" }
    - { ref: MARKETSCALE-2026, title: "Consulting is turning into agent delivery, not decks, as big firms chase 'AI-native' work", publisher: MarketScale, type: press, url: "https://www.marketscale.com/industries/business-services/consulting-is-turning-into-agent-delivery-not-decks-as-big-firms-chase-ai-native-work.md", date: 2026-08-23, access: full, locator: "sections on AI-native delivery models and 'What changes in SOWs'" }
    - { ref: DELTEK-SPI-2026, title: "2026 PSO Benchmarks: What We Learned and What's Next from the SPI Maturity Benchmark Report", publisher: Deltek (SPI Research data), type: survey, url: "https://www.deltek.com/resources/articles/professional-services-benchmarks/", date: 2026-07-30, access: full, locator: "section 2 (utilization 66.4%)" }
  last_reviewed: 2026-10-19
  notes: "Adjacent to work-production: this is about the PSA vendor view of agents doing delivery tasks for implementation firms. Substantive work production by law, audit or consulting agents belongs to work-production. Tandem is itself a vendor with a competing product, so its comparisons are marketing. No named customer measurement was found."

- id: professional-services-delivery-management-14
  title: Ask the PSA for portfolio and financial status in plain language instead of building reports
  archetype: professional-services
  module: delivery-management
  function: service-delivery
  work_types: [data-reporting, coordination-scheduling]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "PMO and delivery leaders compile dashboards and ask analysts for cuts of project, resource and financial data."
  solution: "PSA vendors describe natural-language access to engagement data: Certinia lists a Project Assistant digest of financials, risks and timeline variances and a PMO Leadership agent for portfolio oversight; Kantata describes an Expertise Agent that answers cross-functional business questions across project, resource and financial systems. Harvey describes a matter workspace where partners see where work stands without asking an associate to reconstruct status."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none"
      measures: "not applicable"
      provenance: vendor-published
      source_ref: CERTINIA-VEDA-2026
  prerequisites:
    - "A single, trusted data foundation: SPI reports firms on a project-based ERP grew revenue about 20% faster year over year than those without, although the article cites this as a vendor-promoted correlation (DELTEK-SPI-2026)"
    - "Only 12% of leaders fully trust the data in their systems (KANTATA-SOPSI-2026)"
  risks_and_guardrails:
    - "89% of surveyed leaders say they spend significant time verifying AI outputs, which offsets the speed claim (KANTATA-SOPSI-2026)"
  human_checkpoints:
    - "Leader interprets the answer and decides; the agent provides a digest (CERTINIA-VEDA-2026)"
  role_evolution: "A PM-profession newsletter says PMO analysts shift from collecting data to interpreting it (VARGAS-NEWS-2026). No data."
  evidence_grade: C
  sources:
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI solutions (Veda agents)", publisher: Certinia, type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10-19, access: full, locator: "agent list (Project Assistant, PMO Leadership Agent); 'See the business as it actually is'. Page undated; accessed date shown" }
    - { ref: ERPTODAY-KANTATA-2026, title: "Kantata's Expertise Agent Targets the Professional Services Delivery Crunch", publisher: ERP Today, type: press, url: "https://erp.today/kantata-expertise-agent-psa-ai/", date: 2026-06-19, access: full, locator: "paragraphs 1-3 and 'Gap Between Insight and Execution'" }
    - { ref: HARVEY-ORCH-2026, title: "Making Harvey the Orchestration Layer for Legal Work", publisher: Harvey, type: vendor, url: "https://www.harvey.ai/blog/legal-work-orchestration", date: 2026-10-15, access: full, locator: "section 'Keep Reviews and Next Steps Moving'" }
    - { ref: KANTATA-SOPSI-2026, title: "Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce", publisher: Kantata (survey by Censuswide, 200 leaders), type: survey, url: "https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce", date: 2026-01-08, access: full, locator: "data-trust paragraph" }
    - { ref: DELTEK-SPI-2026, title: "2026 PSO Benchmarks: What We Learned and What's Next from the SPI Maturity Benchmark Report", publisher: Deltek (SPI Research data), type: survey, url: "https://www.deltek.com/resources/articles/professional-services-benchmarks/", date: 2026-07-30, access: full, locator: "section 6 'AI Adoption Accelerates'" }
    - { ref: VARGAS-NEWS-2026, title: "Issue #32 - Are AI Agents the Future of Project Management?", publisher: Ricardo Vargas newsletter, type: community, url: "https://ricardo-vargas.com/newsletter/issue-32-are-ai-agents-the-future-of-project-management/", date: 2026-06-29, access: full, locator: "paragraphs on the PMO of the future" }
  last_reviewed: 2026-10-19
  notes: "Vendor capability descriptions only; no named customer measurement. Kantata's own nav page lists 'Agentic Business Intelligence' but was not read as a source."
```

## 3. Module notes

**Processes and key steps (with work types)**

- Mobilise: sales-to-delivery handoff, kickoff, project plan from SOW (coordination-scheduling, document-production). Use cases 04.
- Plan and schedule the work: phases, tasks, dependencies, staffing of tasks (coordination-scheduling). Use cases 04, 07, 10.
- Run the work: task assignment, review gates, tool configuration, reminders (coordination-scheduling, review-assurance). Use cases 07, 09, 13.
- Track status and risk: time and task hygiene, health ratings, deviation alerts (data-reporting). Use cases 02, 03, 10.
- Report to the client and leadership: weekly updates, steering packs, portfolio views (data-reporting, document-production, client-interaction). Use cases 01, 08, 12, 14.
- Control change: compare requests with scope, raise change orders (client-interaction, expert-judgment). Use case 05.
- Manage engagement economics: budget burn, margin, utilization, AI cost (data-reporting). Use cases 06, 11.
- Close out and learn: retrospective, lessons learned (routed to knowledge-management).

**Common pain points**

- Reporting and status chasing consume time: one interviewed consultant named reporting the primary pain point (EINF-2026, §4.4.1 p.10); a vendor guide puts it at 6 to 8 hours a week per project manager, illustratively (EDNA-STATUS-2026).
- Margin leaks inside delivery and is seen late (TEAMWORK-2026). Unrecovered scope creep is a named leak point (TEAMWORK-2026; EDNA-SCOPE-2026).
- Data cannot be trusted: 12% of leaders fully trust their systems' data (KANTATA-SOPSI-2026).
- Law-firm PMOs are overloaded with technology projects: panelists at ILTACON 2025 said AI added projects and raised the PMO's importance; Ropes & Gray's director estimated about 20% of annual projects are ad hoc (TRI-PMO-ILTACON-2025).
- Talent and skills limit delivery capacity: 68% of surveyed leaders cite skill availability as a barrier, up from 45% (KANTATA-SOPSI-2026); A&E staff growth 1.2% with turnover above 13% (DELTEK-CLARITY-2026).

**Metrics and benchmarks (source, what it counts)**

- Billable utilization 66.4% in 2025 (68.9% in 2024; 73.2% in 2021; SPI target 75%); on-time project delivery 73.8%; project overrun 10.7%; project margin 37.7%; revenue per consultant USD 210K; EBITDA 9.9%. SPI Research 2026 benchmark, 500+ firms (DELTEK-SPI-2026). The article also reports GenAI used in 27.1% of projects in 2025, up from 19.3% in 2024.
- 43.6% of projects now use AI, up from 23.1% in 2025; 245 firms, fieldwork Jul-Sep 2026. A separate SPI study; the page also gives "84.8% vs." a masked figure for "say AI saves them time vs. say it generates revenue" (SPI-AI-2026). Full report is paid and was not read.
- A&E: AI adoption 53% to 70%; only 38% report measurable positive business impact; utilization just under 60%; operating profit 16.7%. Government contractors: 45% unclear on AI ROI; top AI concerns data privacy and security (37%), inaccurate forecasts (29%), difficulty validating AI insights (26%) (DELTEK-CLARITY-2026; respondents 896 A&E and 917 government contractors).
- 68% report team productivity gains but 16% see a direct effect on margin; nearly one in five cannot identify any measurable effect (NAPTA-2026, European professional-services report; sample size not stated on the post).
- Of leaders using AI to optimize essential processes, 54% report more efficient project execution and 52% better forecast accuracy or utilization; 54% of firms say at least 10% of projects miss budget (KANTATA-SOPSI-2026, vendor-sponsored, 200 leaders).
- Agentic AI use: in the Thomson Reuters 2026 survey of over 1,500 professionals, the top agentic use case is process automation and workflow management (TR-AIPS-2026, infographic 3, p.9).
- AI cost: a firm chief data and AI officer said most people are settling on roughly 1% of revenue; about half of the room had 10 or more AI tools in use or under evaluation (TRI-METER-2026).
- Adoption measure: Holland & Hart uses over 70% weekly active users as a pilot test; no one among 50+ attendees had a strong AI-ROI measure (TRI-IMPL-2026).

**Quality evidence.** None found. No source publishes an error rate, override rate, parallel-run result, rework rate or independent test for AI status reports, health scores, scope-drift flags or project plans. What exists: a vendor-sponsored survey in which 89% say they spend significant time verifying AI outputs (KANTATA-SOPSI-2026); interviewees reporting inconsistent output, hallucination and the need for review (EINF-2026, Table 6); a vendor-cited benchmark of falling consistency over repeated agent runs, not opened here (TANDEM-2026); and a fictional premortem of failure modes (TRI-PREMORTEM-2026).

**Guardrails and regulatory points**

- PMI published The Standard for Artificial Intelligence in Portfolio, Program, and Project Management on 9 Jun 2026: eight principles, five performance domains, life-cycle framework, human-in-the-loop oversight. Its stated scope is delivering AI initiatives, so it governs AI projects, not AI used to run any project (PMI-AISTD-2026).
- Reversibility test for delegation: summaries and action plans are two-way doors; unreviewed client replies are one-way doors. Practical steps: permissible use cases, audit trail and decision tracing, no ad hoc creation of agents by individual lawyers (TRI-AGENTIC-2026).
- Confidentiality: client NDAs and security policies decide which tools consultants may use and what data they may share (EINF-2026, Table 6 p.14; §5.5 p.15). Agents with broad data access need boundaries drawn before deployment, including client-specific AI restrictions (TRI-AGENTIC-2026).
- Process readiness: agents expect governed data, documented processes and clear integrations; informal knowledge ('call Linda in accounting') breaks automation (TRI-PREMORTEM-2026, fictional).
- Billing ethics for AI-assisted time and cost pass-through and the EU AI Act timeline for AI used in staffing or worker monitoring are covered in the landscape file (CALBAR-GENAI-2026, EC-AIACT-2026) and were not re-opened here.

**Frontier signals (dated, sourced)**

- 15 Oct 2026: Harvey announces Legal Work Orchestration; expects agents to take an additional 20% of workflow steps within six months and that share to triple within a year (HARVEY-ORCH-2026).
- 19 Aug 2026: a vendor publishes a buyer's guide defining the 'agentic PSA' category and a four-level capability scale; says most 2026 launches are levels one and two (TANDEM-2026). The guide reports Rocketlane raised USD 60 million in March 2026 (secondary, not verified).
- 16 Jun 2026: Kantata launches Expertise Agent (ERPTODAY-KANTATA-2026).
- 24 Mar 2026: PwC publishes Intelligent Status Insights (PWC-STATUS-2026).
- 10 Dec 2025 (press report date): Certinia's Winter '26 release adds a Project Assistant Agent, offered through its early-adopter programme (IA-CERTINIA-2025).
- 8 Jan 2026: Kantata survey: 87% of organizations plan to use AI agents as part of their workforce; 90% expect to need to attribute work, cost and value across humans and agents (KANTATA-SOPSI-2026).
- Sep 2026: ILTACON 2026 shifts from adoption to counting usage-based cost and asking whether AI pays (TRI-METER-2026; TRI-IMPL-2026).
- Scheduled: PMI Global Summit 2026, Detroit, 21-24 Oct 2026, lists AI as a key topic; programme content not read (PMI-SUMMIT-2026, search-only).

**Workforce and role effects**

- Project managers and PMOs: from compiling and chasing to interpretation, judgment and stakeholder work, per a PM commentator and PwC's own statement; unmeasured (VARGAS-NEWS-2026; PWC-STATUS-2026). Finnish consultants insist AI is an assistant that preserves human authority (EINF-2026, abstract).
- Legal project management was already growing before agentic AI: about half of LPM professionals surveyed in 2024 were client-facing, and the role was expected to use AI for deadlines and budget forecasting. This is a Dec 2024 article, outside the 18-month window, used as foundation (TRI-LPM-2024).
- Mid-level pyramid: one guest post forecasts agents eroding the mid-level associate role, 'the project managers of the legal world', as agents orchestrate workflow; the post reports TR data of about 190 billable hours saved per lawyer a year, which was not verified (AL-LADDER-2026). A buyer-side sourcing firm expects fewer junior hours and smaller team sizes on SOWs (BRIGHTFIELD-2026).
- In-house legal ops: legal operations professionals handle legal project management and technology, and AI pressure lands on them first; GC naming technology a strategic priority doubled 2025 to 2026 (TRI-LDOR-2026, `in-house`).

**Objections and concerns practitioners raise**

- No one can prove the saving: 'still gathering the data' (TRI-LEGALWEEK-2026); no strong AI-ROI measure among 50+ attendees (TRI-IMPL-2026); only 16% see margin impact (NAPTA-2026).
- Time saved is not resold: SPI describes 'the leak', hours saved but not repriced or resold (SPI-AI-2026).
- Cost surprise: lawyers cannot see token spend; background agents spend unseen (TRI-METER-2026). Counter-view: firms see slowing adoption as the bigger risk (AMLAW-CONSUMPTION-2026, teaser only).
- Data and process readiness (TRI-PREMORTEM-2026; KANTATA-SOPSI-2026).
- Oversight: a law-firm attorney said agentic AI 'removes oversight a step too far' (TR-AIPS-2026, p.10).
- Hype labelling: a competitor says most 'agentic' PSA launches are summarization or scoring (TANDEM-2026).
- Client contradictions: simultaneous demands for AI savings and for bans on AI use (TRI-LEGALWEEK-2026).
- Policy as brake: IT project managers' GenAI use is limited by organisational policies more than personal resistance, and client organisations largely decide which tools consultants may use (EINF-2026, abstract; §5.5 p.15).

**Interview probes for an advisor**

1. Walk me through how a client status update is produced each week: which systems it pulls from, how long it takes, who reads it before it goes out, and what has gone wrong when it was wrong.
2. How do you find out that a client has asked for something out of scope, how long after the work starts, and who decides whether it triggers a change order?
3. If I asked you today for the time, cost and AI-tool spend on one specific engagement or matter, how long would it take to answer and how much would you trust it?
4. Which of your project data (time, plan, financials, risks) do you trust enough that an automated flag on it would be acted on, and which would you ignore?
5. If an agent produced a red flag or a draft client message, who would be accountable for acting on it, and what record of the agent's inputs would exist afterward?

## 4. Routed to other modules

- **billing-collections:** Legora and Laurel link AI work in Legora to draft time entries and plan to measure AI usage and value (LEGORA-LAUREL-2026, landscape item, not re-opened here). Agent review of pre-bill entries against outside counsel guidelines is described as a concept (ILTA-RISE-2025, paragraph 3). Conversational timekeeping and missing time-card flags (CERTINIA-VEDA-2026; IA-CERTINIA-2025).
- **scoping-pricing:** BigHand's survey of how firms price AI-augmented work (29% changed pricing; 30% keep price and bank the gain; 25% discount when clients allow AI use) and its argument that timesheets can ground AFA pricing (AL-BIGHAND-2026). Client demands for AI line items and 'will not pay for AI-done work' (TRI-LEGALWEEK-2026). Buyer-side view that 'a 12-week diagnostic that still takes 12 weeks' invites questions, with fixed-fee and milestone billing expected to grow (BRIGHTFIELD-2026). Subscription-style products (MARKETSCALE-2026).
- **staffing-resourcing:** Certinia Work Reallocation and Staffing agents; Kantata skill-matching examples; 66% of surveyed organizations turned down work because of resourcing constraints (CERTINIA-VEDA-2026; ERPTODAY-KANTATA-2026; KANTATA-SOPSI-2026).
- **knowledge-management:** Retrospective Drafter and lessons-learned base (CERTINIA-VEDA-2026); Kantata's 'preserving institutional knowledge during handoffs' (ERPTODAY-KANTATA-2026).
- **acceptance-risk:** the conflicts-check failure in the premortem, where informal knowledge was not in any record (TRI-PREMORTEM-2026).
- **client-development:** an Introhive speaker's example of an agent watching call and email patterns for a client-relationship change when a partner leaves (TRI-AGENTIC-2026).
- **quality-review:** the verification burden of agent output (89% spend significant time verifying; KANTATA-SOPSI-2026) and the 'review as theater' failure mode (TRI-PREMORTEM-2026).
- **talent-learning:** pipeline risk from automating junior and mid-level work (AL-LADDER-2026).
- **No clear module (firm-level AI programme management):** how PMOs prioritize and run firm technology projects, portfolio change management, hybrid waterfall and agile leadership for legal-tech projects (TRI-PMO-ILTACON-2025; KK-2026; PMI-AISTD-2026). Nearest fit is knowledge-management or talent-learning (adoption). These concern the firm's own AI rollout, not client engagements.

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 | full |
| CERTINIA-VEDA-2026 | Certinia AI solutions (Veda agents) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 (accessed; undated) | full |
| IA-CERTINIA-2025 | Certinia Announces Winter 2026 Release | Insightful Accountant | press | https://blog.insightfulaccountant.com/certinia-announces-winter-2026-release | 2025-12-10 | full |
| PWC-STATUS-2026 | Manual PMO Status Reporting Is Draining 40% of Project Management Hours. This AI Automates It. | PwC US | firm | https://www.pwc.com/us/en/tech-effect/innovation/automate-pmo-status-reporting.html | 2026-03-24 | full (via mirror; direct fetch returned 403) |
| ERPTODAY-KANTATA-2026 | Kantata's Expertise Agent Targets the Professional Services Delivery Crunch | ERP Today | press | https://erp.today/kantata-expertise-agent-psa-ai/ | 2026-06-19 | full |
| KANTATA-SOPSI-2026 | Kantata Survey Reveals that 87% of Professional Services Teams Plan to Manage AI Agents as Part of Their Workforce | Kantata (Censuswide survey, 200 leaders) | survey | https://www.kantata.com/blog/article/kantata-survey-reveals-that-87-of-professional-services-teams-plan-to-manage-ai-agents-as-part-of-their-workforce | 2026-01-08 | full |
| TANDEM-2026 | Agentic PSA in 2026: what execution agents actually change, and a buyer's guide to who delivers | Tandem | vendor | https://usetandem.ai/blog/agentic-psa-buyers-guide-2026 | 2026-08-19 | full |
| TEAMWORK-2026 | Margin erosion in professional services: how to fix it | Teamwork.com | vendor | https://www.teamwork.com/blog/margin-erosion-professional-services/ | 2026-09-24 | full |
| EDNA-STATUS-2026 | How to Cut Status Update Time by 70% in Consulting | Enterprise DNA | vendor | https://enterprisedna.co/resources/guides/consulting-reduce-time-status-updates | 2026-10-19 (accessed; undated) | full |
| EDNA-SCOPE-2026 | How to Reduce Consulting Project Scope Creep with AI | Enterprise DNA | vendor | https://enterprisedna.co/resources/guides/consulting-reduce-scope-creep | 2026-10-19 (accessed; undated) | full |
| DELTEK-SPI-2026 | 2026 PSO Benchmarks: What We Learned and What's Next from the SPI Maturity Benchmark Report | Deltek (SPI Research data) | survey | https://www.deltek.com/resources/articles/professional-services-benchmarks/ | 2026-07-30 | full |
| DELTEK-CLARITY-2026 | The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures | Deltek | survey | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 | full |
| SPI-AI-2026 | 2026 AI in Professional Services Survey (The 2026 Impact of AI on Professional Services) | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-10 (page shows 'Oct 2026 published') | full (sales page; report paid) |
| NAPTA-2026 | AI and professional services: turning potential into economic impact | Napta | survey | https://www.napta.io/blog/napta-report-2026-ai-and-professional-services-firms-moving-from-technological-potential-to-economic-limpact | 2026-06-30 | full |
| TR-AIPS-2026 | 2026 AI in Professional Services Report | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/content/dam/ewp-m/documents/thomsonreuters/en/pdf/reports/2026-ai-in-professional-services-report.pdf | 2026-01 (PDF creation date 2026-01-27; publication date not stated) | full |
| TRI-LDOR-2026 | 2026 Legal Department Operations Report (summary page) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/legal-department-operations-report-2026 | 2026-09-22 | full (summary; full report gated) |
| EINF-2026 | Realising the Role of Generative AI Among Project Management Professionals | e-Informatica Software Engineering Journal 20(1) (Sainio, Kettunen, Abrahamsson) | academic | https://www.e-informatyka.pl/EISEJ/papers/2026/1/4/eInformatica2026Art04.pdf | 2026-04-23 | full |
| PMI-AISTD-2026 | PMI Publishes World's First Global Standard for AI in Project Work | Project Management Institute | standard-setter | https://www.pmi.org/about/press-media/2026/pmi-publishes-worlds-first-global-standard-for-ai-in-project-work | 2026-06-09 | full (press release; standard itself not read) |
| TRI-PMO-ILTACON-2025 | ILTACON 2025: Proactive project management emerges as law firms' new secret tech weapon | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/proactive-project-management-iltacon-2025 | 2025-08-14 | full |
| TRI-METER-2026 | Ferraris for emails: At ILTACON 2026, the industry starts reading the meter | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter | 2026-09-09 | full |
| TRI-IMPL-2026 | ILTACON 2026: "Does it make the boat faster?" How legal teams are finding AI implementation success | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-finding-ai-implementation-success | 2026-08-31 | full |
| TRI-AGENTIC-2026 | ILTACON 2026: Who's leading the flock? Balancing agentic AI automation and human oversight | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-agentic-ai-automation | 2026-09-14 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 (date from landscape; page header shows fetch time) | full |
| EDRM-LEGALWEEK-2026 | Legalweek 2026 select educational sessions preview | EDRM | conference | https://edrm.net/2026/03/legalweek-2026-select-educational-sessions-preview/ | 2026-03-06 | full (session titles and previews only) |
| PMI-SUMMIT-2026 | PMI Global Summit 2026, Detroit (scheduled 21-24 Oct 2026; AI named a key topic in the call for speakers) | Project Management Institute | conference | https://www.pmi.org/events/speaking-opportunities/global-summit | 2026-10-21 | search-only |
| KK-2026 | The Road to ILTACON 2026: Why Legal Tech Projects Need a New Playbook | Kraft Kennedy | firm | https://www.kraftkennedy.com/the-road-to-iltacon-2026-why-legal-tech-projects-need-a-new-playbook/ | 2026-08-04 | full (pre-conference interview) |
| ILTA-RISE-2025 | The Rise of AI Agents in Legal | ILTA (Pulse, ILTACON 2025) | professional-body | https://iltanet.org/resources/publications/pulse/iltacon/2025/rise-ai | 2025 (month and author not shown) | full |
| CLOC-TALK126-2026 | CLOC Talk EPS 126: Spending in 2026: What Legal Operational Professionals Must Know | CLOC | podcast | https://cloc.org/podcast/spending-in-2026-what-legal-operational-professionals-must-know/ | 2026-08-06 | full (episode description only; audio not heard) |
| LAWYERSWEEKLY-LAWTECH-2026 | LawTech Talks: Delivering new types of work as law moves beyond experimentation | Lawyers Weekly (Australia) | podcast | https://www.lawyersweekly.com.au/podcast/44554-lawtech-talks-delivering-new-types-of-work-as-law-moves-beyond-experimentation | 2026-06-26 | full (episode description only; guest is Harvey's ANZ country manager) |
| VARGAS-NEWS-2026 | Issue #32 - Are AI Agents the Future of Project Management? | Ricardo Vargas newsletter | community | https://ricardo-vargas.com/newsletter/issue-32-are-ai-agents-the-future-of-project-management/ | 2026-06-29 (date shown on page) | full |
| AL-LADDER-2026 | Broken Ladder: Are Lawyers Sleepwalking into a Competence Crisis? | Artificial Lawyer (guest post, James Tuke, AI Futures Forum) | press | https://www.artificiallawyer.com/2026/01/30/broken-ladder-are-lawyers-sleepwalking-into-a-competence-crisis/ | 2026-01-30 | full |
| AL-BIGHAND-2026 | AI Is Forcing Law Firms To Get Serious About Matter Economics | Artificial Lawyer (sponsored, BigHand) | press | https://www.artificiallawyer.com/2026/09/28/ai-is-forcing-law-firms-to-get-serious-about-matter-economics/ | 2026-09-28 | full |
| TRI-PREMORTEM-2026 | Premortem: Your 2028 agentic AI pilot program failed | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/spotlight/premortem-your-2028-agentic-ai-pilot-program-failed | 2026-02-18 | full |
| TRI-LPM-2024 | The strategic rise of legal project management: Shaping the future of law firm success | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en-us/posts/legal/legal-project-management-shaping-future-success/ | 2024-12-20 | full (outside 18-month window; foundation) |
| BRIGHTFIELD-2026 | The Robot Surplus: Why AI Productivity Gains May Not Be Showing Up in Your Contracts | Brightfield (services procurement advisory) | firm | https://www.brightfield.com/resources/the-robot-surplus-why-ai-productivity-gains-may-not-be-showing-up-in-your-contracts | 2026 (page undated; earliest dated asset on page 2026-04-23) | full |
| MARKETSCALE-2026 | Consulting is turning into agent delivery, not decks, as big firms chase 'AI-native' work | MarketScale | press | https://www.marketscale.com/industries/business-services/consulting-is-turning-into-agent-delivery-not-decks-as-big-firms-chase-ai-native-work.md | 2026-08-23 | full (secondary; reports Business Insider and Forrester) |
| AMLAW-CONSUMPTION-2026 | AI Utilization Is 'Skyrocketing,' but Law Firms Aren't Sweating Consumption Pricing | The American Lawyer | press | https://www.law.com/americanlawyer/2026/10/13/ai-utilization-is-skyrocketing-but-law-firms-arent-sweating-consumption-pricing-/ | 2026-10-13 | search-only (teaser bullet; body paywalled) |

Source mix (37 distinct sources, 35 read in full): press 8, conference 7, survey 7, vendor 6, firm 3, podcast 2, academic 1, standard-setter 1, professional-body 1, community 1. All but TRI-LPM-2024 (foundation) date from April 2025 onward. Read and not cited: PMI GenAI report page (Sep 2024, gated), PMI Global Summit 2025 recap (Nov 2025; no AI-in-delivery content beyond a PMP exam refresh note), Certinia margin-leakage blog (undated, header only), Legora newsroom (index only), Rocketlane maturity benchmark page (cookie text only; the figures used appear only through TANDEM-2026 and DELTEK-SPI-2026).

## 6. Gaps

- **No quality evidence.** No error rates, override rates, parallel runs or independent measurement for AI status reports, health scores, scope-drift detection, plan generation or risk drafting. Every productivity number is a vendor claim (PwC about 40%, Rocketlane up to 50%) or a survey of self-reported use. No grade A.
- **Named deployments are almost absent.** Only Certinia names customers (Siemens Digital Industries, Diabsolut, Icon Cloud Consulting) and only as short testimonials. No law firm, accounting firm or consultancy was found describing an AI project-health, scope-drift or status-reporting tool in its own words with outcomes. PwC's page does not say where the tool is used.
- **Practitioner voices are thin.** Reddit (r/projectmanagement, r/consulting) was blocked by network policy; LinkedIn, Legal IT Insider, Above the Law and Legal Evolution were not reachable or not found. The practitioner views here come from conference coverage (mostly Thomson Reuters Institute), one academic interview study of 12 Finnish IT project managers, one newsletter and sponsored posts.
- **Conference content.** ILTACON 2026 and Legalweek 2026 are covered only through TRI articles and EDRM previews; session recordings are members-only. CLOC CGI 2026 (the CLOC Talk description only), AICPA ENGAGE 2026 (Karbon preview lists distributed-team workflow management but nothing on AI in engagement delivery), MCA and Legal Geek content were not retrievable. PMI Global Summit 2026 starts 21 Oct 2026, so there is no recap; only the call for speakers was seen (search-only).
- **Podcasts.** Only episode descriptions (CLOC Talk 126; LawTech Talks with Harvey's ANZ manager). No transcripts, and no podcast with a named delivery leader describing AI in engagement management.
- **Paywalled or gated:** SPI AI study body (USD 1,495), American Lawyer and Law.com Legaltech News body text, PMI GenAI report and the PMI AI standard, TR Legal Department Operations Report, BigHand's 2026 Pricing and Budgeting Trends Analysis, Kantata and Deltek full benchmark reports.
- **Sectors.** Architecture and engineering: only Deltek Clarity and a webinar listing (search result, not opened). Accounting: no practitioner discourse on AI in engagement management found beyond the Karbon ENGAGE preview and a vendor comparison page; Karbon's State of AI report page returned navigation only. Consulting: no primary McKinsey, BCG, Deloitte or Accenture statements about delivery-management AI; MarketScale is secondary and cites Business Insider and Forrester.
- **In-house and shared services.** Only legal in-house (GSK at Legalweek, TR Legal Department Operations Report, the Legalweek 'Agentic Ops' title). No finance, HR or global-business-services delivery management found.
- **Conflicts and cautions.** (1) SPI's 27.1% of projects using GenAI in 2025 (maturity benchmark) and 23.1% in 2025 (AI study page) come from different studies. (2) Date of the TRI Legalweek article: header shows the fetch time; 2026-03-13 is taken from the landscape file. (3) Brightfield, Enterprise DNA, Certinia and Teamwork pages carry no clear publication date for the article body; dates shown are either inferred or access dates. (4) Napta's sample size and the exact wording of its 68% and 16% questions were not on the post. (5) The Artificial Lawyer guest post cites 'approximately 190 billable hours per lawyer annually' from Thomson Reuters without a link; not verified. (6) The tau-bench figures are quoted through Tandem and were not opened.
