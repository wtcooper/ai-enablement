# Delivery management (professional services)

Sources checked 2026-10-19. Use cases live in `../use-cases/delivery-management.yaml` (16 entries: A 0, B 7,
C 6, D 3). Ids are shortened here: `#05` means `professional-services-delivery-management-05`; other modules' and
archetypes' ids are in full. Source keys in brackets are in the YAML or in §10. The public record is thin and mostly
vendor-published: named deployments come from consulting and implementation firms on PSA platforms (professional
services automation: the system holding projects, time, resources and billing), plus one consultancy that built its
own agents. Legal delivery management is announced, not evidenced. No source publishes an error, override or
false-alarm rate for an AI status report, plan, health score or scope flag. Say so when you quote a figure.

## Contents

1. [What this module covers](#1-what-this-module-covers)
2. [Processes and key steps](#2-processes-and-key-steps)
3. [Where AI is changing the work](#3-where-ai-is-changing-the-work)
4. [Interview probes](#4-interview-probes)
5. [Metrics and benchmarks](#5-metrics-and-benchmarks)
6. [Guardrails](#6-guardrails)
7. [Roles and how they evolve](#7-roles-and-how-they-evolve)
8. [Frontier](#8-frontier)
9. [Common objections](#9-common-objections)
10. [Sources](#10-sources)

## 1. What this module covers

Running an engagement or matter once it is sold: the handoff from sale to delivery, planning, meeting records,
status and client reporting, risk and health tracking, scope and change control, budget and margin during delivery,
and close-out. It is the shared layer for law, consulting, accounting and implementation firms and in-house teams.
The substantive work itself is in work-production; audit, tax and security procedures are in their own archetypes.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Handoff and mobilise | Deal context, SOW (statement of work: the scope, deliverables and fees) and client terms passed to the delivery team; kickoff brief | coordination-scheduling, document-production | Context lost between sales and delivery; new joiners briefed by hand [KANTATA-SUPERAGENT-2026] |
| Plan | Work breakdown, phased plan, solution design, review points | document-production, expert-judgment | Plans rebuilt from the SOW and memory; one firm put a design document at about 80 hours [CERTINIA-MOONNOX-2026] |
| Meetings and documentation | Minutes, decisions, action items, requirements, backlogs | document-production | Written after the fact; commitments slip [ROCKETLANE-EARTHWISE-2026] |
| Status and client reporting | Weekly updates, steering-committee packs, portfolio views | data-reporting, document-production, client-interaction | 72% spend half a day or more a month collating reports (base not stated) [WELLINGTONE-SOPM-2026] |
| Risk and health tracking | Overdue tasks, missing time entries, slipping milestones, RAG (red-amber-green) ratings | data-reporting, review-assurance | Found in periodic reviews after margin is lost; ratings depend on each manager [CERTINIA-VEDA-2026] |
| Scope and change control | Compare requests with the SOW; raise change orders | review-assurance, client-interaction | Change orders written after the work is done [EDNA-SCOPE-2026] |
| Engagement economics | Budget against actuals, burn, margin, forecast, fee basis | data-reporting | Overrun 10.7% and on-time delivery 73.8% across 500+ firms [DELTEK-SPI-2026] |
| Run and coordinate | Task routing, reviews, reminders, plan upkeep | coordination-scheduling | Partners ask associates to rebuild status from email [HARVEY-ORCH-2026] |
| Close-out | Retrospective and lessons learned | document-production, research-synthesis | Lessons not written up where the next team can find them [CERTINIA-VEDA-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (`change_scope: model`, or a process that stops existing).
**Coverage:** assist 2, augment 8, automate 1, delegate 5; step 7, process 8, model 1. Automate has one entry, a
practitioner idea (`#09`). Delegate's named examples are a consultancy's self-reported agent estate (`#12`),
Thoughtworks' role design (`#14`) and Basware's plans (`#13`); the rest are announcements or ideas. Reinvent has one idea (`#16`). No firm reports a delivery step that has stopped
existing.

**Mobilise and plan**
- Improve: `#01` delivery plan, solution design and handoff brief drafted from the SOW, deal record and transcripts.
  Spaulding Ridge (consulting and implementation) puts design drafting at about 80 hours down to under 20, an
  executive's estimate. Scoping documents and SOW drafting: professional-services-scoping-pricing-01 and -05.

**Meetings and documentation**
- Improve: `#02` transcripts turned into summaries, decisions, action items, requirements and backlogs. Diabsolut
  (Salesforce implementer) reports 70% less documentation time (vendor-published); EarthWise Pet (in-house team)
  uses AI call summaries. Recording consent is the live risk.

**Status and client reporting**
- Improve: `#03` status reports and steering packs drafted from live project data (Nextview, consulting partner;
  PwC US sells an offering with a projected "about 40%" cut in admin overhead). Tax equivalent:
  tax-compliance-individual-business-15.
- Improve: `#04` ask for status, budget consumption and anomalies in plain language (zeb, financial-services
  consultancy, on SAP; Planning Blox for law firms).
- Process-level, client side: a client portal in place of email in an attestation practice is
  assurance-soc-attestation-07; shared client workspaces are professional-services-work-production-20.

**Monitoring, risk and change control**
- Improve, process scope: `#05` agents flag slipping milestones, missing time entries, deliverable discrepancies and
  health risk (Siemens Digital Industries customer success, in-house; one testimonial, no figures).
- Improve: `#06` scope-drift flags against the SOW with a prompt to raise a change order. Vendor guides only.
- Delegate: `#10` idea from practitioners: predict dependency and schedule risks from historical project data.

**Engagement economics**
- Improve, process scope: `#07` margin, burn and forecast monitoring with alerts on overruns and unbilled time
  (consulting PSAs; BigHand and Planning Blox for law firms). Budget setting and re-scoping:
  professional-services-scoping-pricing-08.
- Reinvent: `#16` idea: count agents and AI spend in engagement economics (agent margin, AI cost per matter, effort
  against fee basis). Pricing choices: professional-services-scoping-pricing-06, -14, -17; client proof of AI savings:
  professional-services-scoping-pricing-09.

**Running and coordinating the work**
- Improve, process scope: `#11` a matter run from a reusable template with tasks routed, named review gates and
  status visible without reconstruction (Harvey, announced 2026-10-15; no customer named). The agents doing the
  drafting inside the template: professional-services-work-production-15.
- Automate: `#09` idea: automated reminders, calendar coordination and tool setup (wanted by IT project managers).
- Delegate: `#08` an agent project manager keeps the plan current and chases tasks (Certinia, Kantata, Rocketlane,
  Planview announcements). `#12` Automation Consultants (IT consultancy) built 12 agents with an orchestrating
  agent and one human approval gate, reporting roughly 25% of delivery capacity released (self-reported, sponsored
  talk). `#13` agents take on repeatable implementation tasks and send routine documentation to customers (Basware's
  in-house services organisation, expanding; Rocketlane claims up to 50% less effort).
- Delegate, operating model: `#14` Thoughtworks engagement leads structure engagements across people, AI agents and
  client stakeholders. Workforce shape: professional-services-talent-learning-20.

**Close-out**
- Improve: `#15` retrospective and lessons-learned drafting (vendor descriptions). Reuse belongs to
  knowledge-management.

## 4. Interview probes

1. **"Walk me through last week's client status update: which systems it pulled from, how long it took, who read
   it before it went out, and what went wrong when it was wrong."** Reveals the size of `#03` and whether a review
   step already exists to absorb an AI draft.
2. **"Which delivery data (time, plan, budget, risks, notes) sits in one system an agent could read, and which lives
   in email, chat and people's heads?"** Reveals readiness for `#04`, `#05` and `#07`; only 12% of leaders fully
   trust their systems' data [KANTATA-SOPSI-2026].
3. **"Which flags would you act on today if a system raised them, and which would you ignore?"** Reveals whether
   alerts in `#05` would change behaviour or become noise; no source publishes false-alarm rates.
4. **"How do you find out a client asked for something out of scope, how long after the work starts, and who
   decides whether it becomes a change order?"** Reveals the leakage `#06` targets and who must own the decision.
5. **"When a project slips or burns budget, how many days pass before someone with authority knows?"** Reveals the
   gap `#07` closes; Teamwork calls it the "erosion gap" [TEAMWORK-2026].
6. **"How are meetings with clients recorded today, and who confirms consent and the permitted tool?"** Reveals
   exposure in `#02`; a 2025 class action alleges recording without consent [KJZZ-OTTER-2025].
7. **"Which of your clients have written AI terms (approval, banned tools, records, no payment for AI work), and how
   does the delivery team learn them mid-engagement?"** Reveals whether client instructions reach the work; see
   professional-services-acceptance-risk-11 and professional-services-work-production-25.
8. **"When an agent finishes a step, who is the named reviewer, and what record shows how often they change or
   reject its output?"** Reveals whether gates in `#11` and `#12` are real; this record exists nowhere in public.
9. **"Where do hours saved on reporting and documentation go: resold, redeployed, written down, passed to the
   client? What baseline did you capture first?"** Reveals "the leak" [SPI-AI-2026] and whether any claim can be
   tested; Certinia itself advises baselining first [CERTINIA-CUSTOMERS-2026].
10. **"If I asked for the time, cost and AI-tool spend on one engagement, how long would it take, and would you
    trust the answer?"** Reveals readiness for `#16`; firms at ILTACON were only starting to meter AI cost
    [TRI-METER-2026].
11. **"Which recurring engagement or matter types run the same way each time, and is that process written down?"**
    Reveals candidates for templates (`#11`) or agent estates (`#12`); agents fail on undocumented workflows
    [TRI-PREMORTEM-2026].
12. **"In-house: do you know which of your outside firms use AI on your matters, and what it saved?"** Reveals the
    client-side gap: 59% of in-house respondents do not know [ACC-TRANSPARENCY-2025].

## 5. Metrics and benchmarks

**Delivery baselines (not AI results)**
- SPI 2026 benchmark, 500+ firms, 2025 data: billable utilization 66.4% (SPI target 75%); on-time delivery 73.8%;
  project overrun 10.7% (SPI treats above 10% as damaging to client relationships); project margin 37.7%; GenAI in
  27.1% of projects [DELTEK-SPI-2026].
- SPI 2026 AI study, 245 firms: 43.6% of projects use AI, up from 23.1%; 84.8% say AI saves time, against a share
  saying it generates revenue that the public page hides [SPI-AI-2026]. Do not combine with the 27.1% above.
- Wellingtone 2026: 72% spend half a day or more a month collating reports; 36% of organisations always or mostly
  finish projects on time; the summary page does not define the base of the 72% [WELLINGTONE-SOPM-2026].
- Kantata-sponsored survey, 200 leaders: 54% say at least 10% of projects miss budget; 12% fully trust their data;
  89% spend significant time verifying AI outputs [KANTATA-SOPSI-2026].
- Deltek Clarity: architecture and engineering firms 70% AI adoption but 38% report measurable benefit; among
  government contractors, inaccurate forecasts (29%) and validating AI insights (26%) are top AI concerns
  [DELTEK-CLARITY-2026]. Napta: 68% report productivity gains, 16% a direct margin effect; sample not stated
  [NAPTA-2026].
- Perception gap: leaders rate AI success 16 points and forecasting confidence 24 points higher than practitioners
  (1,000 leaders, Certinia-commissioned) [CERTINIA-GSD-2026].

**Firm and customer figures (all unaudited)**
- Automation Consultants: roughly 25% of delivery capacity released, throughput tripled, 11 engagements
  (self-reported, sponsored session abstract) [ATLASSIAN-TEAM26-AC-2026].
- Spaulding Ridge: design documents about 80 hours to under 20 (executive estimate) [CERTINIA-MOONNOX-2026].
  Diabsolut: documentation time down 70% (vendor-published) [CERTINIA-CUSTOMERS-2026].

**Vendor claims (no baseline, sample or method)**
- PwC: about 40% less admin overhead, 120 hours a year and USD 7,000-24,000 per resource, all projected
  [PWC-STATUS-2026]. Certinia: about 50% of project time lost to admin recovered; 11-23% less margin lost to rework;
  60% faster onboarding [CERTINIA-VEDA-2026]; up to 20 hours a month per project manager [SILICONANGLE-CERTINIA-2026].
  Deltek: 16% more on-time delivery, 20% better forecast accuracy [DELTEK-POLARIS-2026]. Rocketlane: up to 50% less
  delivery effort, quoted by a competitor [TANDEM-2026].

**Measurement gap.** 85% of law-firm and 75% of corporate legal respondents are not collecting AI ROI data or are
unsure [TRI-DISCONNECT-2026]; no one among 50+ ILTACON attendees had a strong ROI measure [TRI-IMPL-2026].

**What to measure:** hours to produce each status pack; share of AI drafts sent unchanged, edited or rejected;
flags acted on versus dismissed and risks missed; days from slippage to escalation; change orders raised before
versus after the work; budget variance at close; AI and agent cost per engagement; where saved hours went.

## 6. Guardrails

- **Responsibility stays with the professional.** ABA Formal Opinion 512 (2024-07-29): consent before client data
  goes into a self-learning tool; consider telling clients about AI use; managers set policy and train; hourly bills
  reflect actual time [ABA-OP512-2024]. ICMCI code for consultants (May 2026): AI does not dilute accountability;
  disclose material AI use; follow client AI instructions; engagement terms should cover AI [ICMCI-AICODE-2026].
- **Supervision grows with autonomy.** California's guidance (approved 2026-05-14): more autonomy needs more
  oversight and periodic reassessment; agents must not send client data out without safeguards and review; follow
  client AI restrictions; matter-specific AI costs disclosed, at cost, no markup without written consent
  [CALBAR-GENAI-2026]. A secondary report says the SRA's June 2026 supervision guidance keeps AI output under human
  review [LAWYERMONTHLY-SRA-2026].
- **Clients set terms.** Australia's model clauses let government buyers require approval of supplier AI use,
  quality checks and records, and ban named systems [AGS-AIMODELCLAUSES-2025]. 82% of 468 general counsel expect
  providers to explain their AI use [LEGALBUSINESS-KPMGGC-2026]. Client organisations largely decide which tools
  consultants may use [EINF-2026].
- **Worker monitoring.** The EU AI Act lists AI that monitors or evaluates workers' performance as high-risk
  [EU-AIACT-ANNEX3-2024], applying from 2027-12-02 [EC-AIACT-2026]. Check health scoring and task allocation.
- **Recording.** Consent from every participant before meeting capture [KJZZ-OTTER-2025; CALBAR-GENAI-2026].
- **Reversibility test.** Summaries and action plans are two-way doors; an agent replying to a client unreviewed is
  a one-way door. Keep an audit trail and stop individuals creating agents ad hoc [TRI-AGENTIC-2026].
- **Insurance.** Professional indemnity policies tend not to cover AI errors explicitly [DACBEACHCROFT-PI-2026].
- **PMI's AI standard (2026-06-09)** governs AI projects, not AI used to run projects [PMI-AISTD-2026].

**Steps that stay with a person:** deciding whether a request is out of scope and raising it with the client;
approving anything that reaches a client; acting on a risk flag; changing fees or budgets; signing off plans and
designs; confirming recording consent and client AI terms; choosing which agent actions need no approval.

## 7. Roles and how they evolve

- **Project managers: from assembling to checking and interpreting.** Nextview's delivery director calls
  steering-committee preparation a "quality information gathering exercise" [CERTINIA-CUSTOMERS-2026]; PwC says freed
  time goes to oversight, risk and issue resolution [PWC-STATUS-2026]. A commentator says managers who mainly
  consolidate reports "should be concerned" (opinion) [VARGAS-NEWS-2026]. Finnish IT project managers see AI as an
  "assistant not replacement" [EINF-2026].
- **PMO: from compiling to designing and approving agent estates** [ATLASSIAN-TEAM26-AC-2026]; 67% of Wellingtone
  respondents see PMO scope increasing [WELLINGTONE-SOPM-2026].
- **Engagement leads add AI workflow design and agent supervision** (Thoughtworks postings) [TW-JOB-8138525-2026].
- **Resource managers are not ready:** 52.7% not equipped to manage hybrid human-agent teams, 4% well equipped
  [KANTATA-RMI-2026].
- **Legal:** Harvey says lawyers will direct matters and review consequential outputs [HARVEY-ORCH-2026]; a guest
  post forecasts erosion of mid-level associates, "the project managers of the legal world" [AL-LADDER-2026]. Pricing
  and innovation officers speak for firms on AI value [TRI-LEGALWEEK-2026]. In-house legal operations, which runs
  legal project management, takes AI pressure first [TRI-LDOR-2026].
- **Sourcing:** UK Big Four graduate cuts were reported alongside offshoring to India, Malaysia and the Philippines;
  causes are mixed [CITYAM-BIG4-2025]. Talk about roles and capacity, not headcount.

## 8. Frontier

- **2025-12-10** Certinia offers its Project Assistant agent through an early-adopter programme [IA-CERTINIA-2025].
- **2026-03-24** PwC US publishes Intelligent Status Insights [PWC-STATUS-2026].
- **2026-05-04** Planview announces Agent Resource Management, available from Fall 2026 [SDTIMES-PLANVIEW-2026].
- **2026-05-14** California approves guidance covering agentic AI [CALBAR-GENAI-2026]. **2026-05** ICMCI adopts its consulting AI code [ICMCI-AICODE-2026].
- **2026-06-09** PMI publishes its standard for AI in project work [PMI-AISTD-2026].
- **2026-06-16** Kantata launches Expertise Agent [ERPTODAY-KANTATA-2026]; **2026-07-21** Certinia buys Moonnox
  for meeting and tool context capture [CERTINIA-MOONNOX-2026].
- **2026-08-19** A vendor defines "agentic PSA" and says most launches are summarising or scoring [TANDEM-2026].
- **2026-09** ILTACON moves from adoption to metering AI cost per matter [TRI-METER-2026].
- **2026-09-09** Certinia adds 14 agents, doubles its Intelligent Actions library to 135 and makes them callable from
  Slack, Claude and Microsoft Copilot over MCP; it commits to every workflow being executable by an agent or a human
  by year-end [CERTINIA-SOA-2026].
- **2026-10-07** Kantata Agent Studio lets PMO owners describe agents in plain language [ITBRIEF-KANTATA-2026];
  **2026-10-08** Automation Consultants presents its 12-agent PMO [ATLASSIAN-TEAM26-AC-2026].
- **2026-10-13** Legora and Laurel plan a second phase measuring AI usage and value [LEGORA-LAUREL-2026].
- **2026-10-15** Harvey Legal Work Orchestration; Harvey expects agents to take on a further 20% of workflow steps
  in six months [HARVEY-ORCH-2026].
- **Scheduled:** 2026-10-20 Basware and Kantata on "who's managing [an agent's] margin" [KANTATA-BASWARE-2026];
  2026-10-21 to 24 PMI Global Summit with AI as a key topic [PMI-SUMMIT-2026]. Signals only.
- **2027-12-02** EU AI Act high-risk obligations for worker monitoring apply [EC-AIACT-2026].

## 9. Common objections

- **"The numbers are vendor marketing."** Mostly true: every outcome figure here is vendor-published or self-reported, and the
  best build (`#12`) is a sponsored talk. Answer: baseline your own hours first, as Certinia itself advises
  [CERTINIA-CUSTOMERS-2026], and track edits to AI drafts.
- **"Our data isn't good enough."** A fair worry: 47% cite fragmented data [KANTATA-RMI-2026], and an IDC analyst
  links unintegrated data to unreliable output [CERTINIA-GSD-2026]. Answer: start where data is already in one
  system (zeb on SAP, `#04`) or where a person reviews anyway (`#03`).
- **"We'll spend as long checking as we save."** 89% report significant verification time [KANTATA-SOPSI-2026];
  interviewees edited drafts heavily [EINF-2026]. Answer: pick steps already reviewed by a person, and record
  correction rates, which no one publishes yet.
- **"Agents will make bad calls."** An unnamed firm's agent project manager misread ambiguous requests
  [IPM-CHATGPT-PM-2026]; Kantata's chief executive warns of "fast, mediocre decisions" [KANTATA-SUPERAGENT-2026].
  Answer: delegate reversible steps and gate one-way doors [TRI-AGENTIC-2026], as `#12` does with one approval gate.
- **"Clients won't allow it."** Some won't, and their instructions bind [CALBAR-GENAI-2026; ICMCI-AICODE-2026].
  Answer: capture client AI terms at engagement opening (professional-services-acceptance-risk-11).
- **"We can't show what it saved."** Firms say they are "still gathering the data" [TRI-LEGALWEEK-2026]; SPI calls
  unsold saved hours "the leak" [SPI-AI-2026]. Answer: decide where saved hours go and measure it (`#16`;
  professional-services-scoping-pricing-09).
- **"It's just summarisation called agents."** A vendor says most launches are [TANDEM-2026]. Answer: ask which
  capability runs in production at a named customer.
- **"Policy stops us."** Finnish project managers' use is limited by policy more than resistance [EINF-2026].
  Answer: start from the tools the firm and the client have already approved.
- **"Leadership thinks it's working."** Leaders rate AI success 16 points higher than practitioners
  [CERTINIA-GSD-2026]. Ask the people who build the status packs.

## 10. Sources

Full details for YAML keys are in the YAML. Keys cited here but not in the YAML:
- ACC-TRANSPARENCY-2025: Association of Corporate Counsel, The Transparency Gap: In-house Counsel Lack Clarity on
  Law Firms' AI Use, 2025-11-05, https://docket.acc.com/node/4313
- CITYAM-BIG4-2025: City AM, Big Four slash graduate jobs as AI takes on entry level work, 2025-06-23,
  https://www.cityam.com/?p=2342067
- DACBEACHCROFT-PI-2026: DAC Beachcroft, Professional indemnity insurance: risk of AI hallucinations, 2026-09-28,
  https://www.dacbeachcroft.com/en/what-we-think/professional-indemnity-insurance-risk-of-ai-hallucinations
- LAWYERMONTHLY-SRA-2026: Lawyer Monthly, SRA Issues Post-Mazur Supervision Guidance (secondary report), 2026-06-12,
  https://www.lawyer-monthly.com/2026/06/sra-post-mazur-supervision-guidance-2026/
- LEGALBUSINESS-KPMGGC-2026: Legal Business, 'Be bold, be honest about it' - GCs demand AI transparency from law
  firms (KPMG survey of 468 GCs), 2026-04-29,
  https://www.legalbusiness.co.uk/in-house/be-bold-be-honest-about-it-gcs-demand-ai-transparency-from-law-firms/
- LEGORA-LAUREL-2026: Legora, Legora and Laurel partner to capture the time lawyers spend in Legora, 2026-10-13,
  https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
- NAPTA-2026: Napta, AI and professional services: turning potential into economic impact, 2026-06-30,
  https://www.napta.io/blog/napta-report-2026-ai-and-professional-services-firms-moving-from-technological-potential-to-economic-limpact
- PMI-AISTD-2026: PMI, PMI Publishes World's First Global Standard for AI in Project Work (press release),
  2026-06-09, https://www.pmi.org/about/press-media/2026/pmi-publishes-worlds-first-global-standard-for-ai-in-project-work
- PMI-SUMMIT-2026: PMI, Global Summit 2026, Detroit (call for speakers; search-only), 2026-10-21,
  https://www.pmi.org/events/speaking-opportunities/global-summit
- TRI-DISCONNECT-2026: Thomson Reuters Institute, The great AI disconnect, 2026-03-18,
  https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect
- TRI-IMPL-2026: Thomson Reuters Institute, ILTACON 2026: "Does it make the boat faster?", 2026-08-31,
  https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-finding-ai-implementation-success
- TRI-LDOR-2026: Thomson Reuters Institute, 2026 Legal Department Operations Report (summary), 2026-09-22,
  https://www.thomsonreuters.com/en/institute/reports/legal-department-operations-report-2026
- TRI-LEGALWEEK-2026: Thomson Reuters Institute, Couples counseling at Legalweek 2026: firms and clients confront the
  AI value divide, 2026-03-13, https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
