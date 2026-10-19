# Staffing and resourcing (professional services)

Sources checked 2026-10-19. Use cases live in `../use-cases/staffing-resourcing.yaml` (21 entries: A 0, B 6, C 12,
D 3). Ids are shortened here: `#05` means `professional-services-staffing-resourcing-05`; other modules' and
archetypes' ids are in full. Source keys in brackets are in the YAML or in §10. **Read this first:** no named firm
publishes a measured result for AI in staffing. Named AI deployments are a handful of consulting and implementation
firms on PSA platforms (professional services automation: the system holding projects, people, time and billing).
The best-measured law-firm examples use a resourcing platform not described as AI. The only randomised test of
automated work allocation is in a public agency, and it favoured the managers. Say so when you quote a figure.

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

Matching people (and now AI agents) to work: capturing demand, forecasting capacity, keeping skills data current,
shortlisting and booking, reallocating work in flight, managing bench and utilisation (the share of available time
charged to clients), and deciding whether to hire, contract, subcontract or insource. It is the shared layer for law,
consulting, accounting and other advisory firms and in-house teams. People development is talent-learning; running
the engagement once staffed is delivery-management; audit team selection and independence rules sit in the assurance
archetype.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Capture demand | Client requests, RFPs, pipeline deals and signed SOWs (statements of work) turned into roles, skills, dates and load | coordination-scheduling, document-production | Requests re-keyed from email; may not be answered the same day [CINODE-2026] |
| Forecast demand and capacity | Pipeline weighted by win rates against supply, by role, skill and period | data-reporting | Pipeline in the CRM, capacity in a spreadsheet, quarterly at best [PROJECTWORKS-2026]; 55% miss, delay or turn down work for capacity [DAYSHAPE-ONREC-2026] |
| Keep the supply picture | Skills, certifications, recency, availability, cost; external and partner resources | data-reporting | Self-reported, stale skills [TSIA-RM-2026]; 47% cite fragmented data [KANTATA-RMI-2026] |
| Match, shortlist, book | Find candidates, check availability and cost, agree with the project lead, book tentatively then firmly | coordination-scheduling, expert-judgment | Familiarity and recency bias [PROJECTWORKS-2026]; 39% staff by availability, not fit [DAYSHAPE-ONREC-2026]; 37% of law firms say partners resource on preference [BIGHAND-DLA-2026] |
| Reallocate and cover | Replace people on work in flight; absorb moved deadlines and leave | coordination-scheduling | Delayed starts, overbooked top performers, underused staff [TSIA-RM-2026] |
| Bench and utilisation | Place unassigned staff; watch over- and under-allocation | data-reporting, coordination-scheduling | Problems found in last month's report [PROJECTWORKS-2026] |
| Supply decisions | Hire, contract, subcontract, insource or send to outside counsel | expert-judgment | Busy-season help arrives after the core team is stretched [CPAPA-SAAH-2026] |
| Fair access and development | Opportunity boards, development goals, stretch work | coordination-scheduling | Associates close to particular partners are more visible for new matters [BIGHAND-DLA-2026] |
| Emerging: plan people and agents | Agents as capacity with cost and owner | coordination-scheduling, data-reporting | 52.7% not equipped for hybrid teams [KANTATA-RMI-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step), automate (no person on the normal path), delegate (an agent owns a
multi-step outcome with checkpoints), reinvent (`change_scope: model`, or a process that stops existing).
**Coverage:** assist 7, augment 13, automate 1, delegate 0; step 10, process 8, model 3. **Delegate has no
evidence:** every staffing agent read "proposes", "surfaces" or "recommends"; zeb's agent proposes and pre-books
people, and no source describes an agent owning a staffing outcome end to end. **Automate has one entry**, an optimisation algorithm in a public agency (`#13`), and it did worse than
managers. Reinvent rests on announcements, surveys and one podcast.

**Capture demand**
- Improve, process scope: `#03` client emails, procurement portals and SOWs read into roles and suggested assignments
  (Cinode for consulting firms; Rocketlane says kickoff prep goes "from days to hours", vendor-published). Plan
  drafting from the SOW is professional-services-delivery-management-01.

**Forecast**
- Improve, process scope: `#04` rolling demand and capacity forecast from pipeline with what-if scenarios. Kantata
  customer Hakkoda went from four weeks to three to six months ahead; the vendor page lists 10% better project margin
  (B, vendor-published). Accounting busy-season forecasting is described by vendors only.
- Reinvent (idea): `#20` check whether AI actually freed hours and re-base plans; Big Law demand rose 4.2% in H1 2026
  [BLOOMBERG-AICOST-2026].

**Supply picture**
- Improve: `#10` skills inventory kept current from profiles and project history (vendor descriptions; TSIA model).
- Improve: `#11` one matching view across employees, subcontractors and partner consultants (Cinode, Kantata).

**Match, shortlist and book**
- Improve: `#01` ranked shortlists inside the PSA or workflow tool, the resource manager deciding. Named uses: Basware
  (software company's services organisation), Nextview (Salesforce consulting partner), Diabsolut (implementer), zeb
  (financial-services consultancy); products for accounting firms (CCH Axcess Workflow) and an early preview for law
  firms (BigHand). Audit equivalents: assurance-planning-risk-assessment-22, assurance-quality-management-11.
- Improve: `#02` McKinsey (consulting) plans agents to supplement its professional-development staff (announced).
- Improve: `#05` staffing scenarios with margin impact at the point of decision (vendor pages).
- Improve: `#09` conversational assistant: "who has these skills and is free in July?" (Kantata, Rocketlane, Certinia).
- Improve, process scope: `#12` central, skills-based resourcing with open opportunity boards in place of partner-led
  calls. DLA Piper reports 600+ hours saved finding resources at half-year end; Womble Bond Dickinson 10% higher
  utilisation (law firms; vendor-published; platform not described as AI). Reed Smith (law firm) uses AI decision
  support (2023 announcement). Development side: professional-services-talent-learning-04.
- Automate: `#13` algorithm assigns cases instead of managers (Peru public agency, randomised): about 5 points worse
  on-time completion, no quality difference. Treat as the main caution against removing the person.
- Improve: `#14` suggested completion dates while managers keep assignment: about 4 points better (same trial).

**Reallocate, bench and utilisation**
- Improve, process scope: `#06` agent re-matches and proposes replacements for work in flight (Certinia beta,
  Rocketlane "active rollout"). `#08` continuous utilisation and overallocation alerts.
- Improve: `#07` bench gaps flagged two to three weeks ahead and matched to open or unsold work, with soft-booking.

**Team shape and sourcing**
- Improve, process scope: `#15` one professional with AI staffed where a pair would have been; individuals with AI
  matched teams without AI at Procter & Gamble (adjacent, consumer goods).
- Reinvent: `#16` agents planned, allocated and costed as capacity (Planview announced; 0% of 44 surveyed
  organisations operate it). Engagement-level view: professional-services-delivery-management-14, -16.
- Reinvent: `#17` experienced flexible lawyers for overflow and to train and review AI tools (provider's account).
- Reinvent: `#18` in-house legal teams insource drafting as AI lifts capacity; 64% expect less outside counsel
  (in-house; survey of expectations).
- Reinvent (idea): `#19` staff on outcomes: which people-and-agent combinations deliver; 7.3% have outcome data.

**Controls**
- Improve (idea): `#21` decision log, override tracking, disparate-impact tests and explanations for AI-assisted
  allocation, drawn from EU, California, UK, US state and ICMCI texts.

## 4. Interview probes

1. **"When a role opens, how do you find candidates today, and how many calls or messages does one assignment take?"**
   Reveals the search effort `#01` and `#09` target and whether staffing runs on one person's memory.
2. **"What share of staffing decisions start from someone you already know? Who gets missed?"** Reveals familiarity
   bias and the fairness case for `#12`; BigHand reports 43% of law-firm resourcing is lawyer-led [BIGHAND-DLAPR-2026].
3. **"If a tool recommended a team, how would you know it was good? Do you record when a recommendation is
   overridden, and why?"** Reveals whether a quality signal exists; no source publishes override or acceptance rates.
4. **"Which staffing inputs are in no system: client chemistry, development goals, partner preference, personal
   circumstances?"** Reveals what must stay with a person; the Peru trial lost exactly this soft information
   [IPA-PERU-2026].
5. **"Where do pipeline, skills, availability and cost live, and would you trust them to feed a recommender?"**
   Reveals readiness; only 12% of leaders fully trust their systems data [KANTATA-SOPSI-2026].
6. **"How far ahead can you see a capacity gap, and what did you turn down last quarter for lack of people?"**
   Reveals the value of `#04`; 55% miss, delay or turn down work [DAYSHAPE-ONREC-2026].
7. **"When AI saves time on a matter or project, what happens to the freed hours in your allocation data?"** Reveals
   "the leak" [SPI-AI-2026] and whether plans assume savings that demand has not delivered (`#20`).
8. **"Would you put an agent on a staffing plan with a rate and a capacity? Who owns its quality and signs off its
   work?"** Reveals readiness for `#16`; 4% feel well equipped [KANTATA-RMI-2026].
9. **"What outcome data (margin, client result, rework) is visible at staffing time, and who links it to who
   delivered?"** Reveals whether `#19` is possible; 24.6% say outcomes are not available to them [KANTATA-RMI-2026].
10. **"Which tools allocate work or rate people using data about performance, behaviour or traits, and has legal
    reviewed them against the EU and California rules that name task allocation?"** Reveals exposure (§6).
11. **"How current is your skills data, who maintains it, and what would staff or works councils say about
    inferring skills from their work history?"** Reveals the consent question in `#10`.
12. **"In-house: which work have you brought back from outside counsel since adopting AI, and how do you decide?"**
    Reveals whether `#18` is happening or only expected.

## 5. Metrics and benchmarks

**Baselines (not AI results)**
- SPI benchmark, 500+ firms, 2025 data: billable utilisation 66.4%, lowest in its history (68.9% in 2024; 75% treated
  as optimal); Level 5 firms above 80%; revenue per billable consultant $210K; attrition 11.3%; subcontractors 10.4%
  of revenue [DELTEK-SPI-2026; DELTEK-SPIKPI-2026]. Published by Deltek, which sponsors the report.
- Architecture and engineering (A&E), 896 firms: utilisation just under 60%; staff growth 1.2% against forecast
  revenue growth of 9.5%; turnover above 13%; 70% AI adoption but 38% report measurable benefit [DELTEK-CLARITY-2026].
- TSIA research via Accelo: 97% track utilisation, fewer than 2% use AI for scheduling and allocation; TSIA's
  DiMuccio said most firms run at 55-65% (spoken remark) [ACCELO-TSIA-2026].
- Kantata-sponsored survey, 200 leaders: more than 66% turned down work for resourcing reasons; 68% cite skill
  availability as a barrier (45% a year earlier); 12% fully trust their data (24% a year earlier); 88% trust AI
  outputs for operational decisions yet 89% spend significant time verifying them [KANTATA-SOPSI-2026].
- Dayshape, 400 UK and US leaders: 55% miss, delay or turn down work for capacity; 39% staff by availability over fit;
  76% say AI already improves planning and allocation decisions [DAYSHAPE-ONREC-2026].
- Resource Management Institute for Kantata, 44 organisations: 39% traditional staffing, 30% exploring, 31% beyond
  experimentation; 72% call the function operational; 7.3% use outcome data in staffing; 0% run agents as assignable
  resources, 10.7% piloting [KANTATA-RMI-2026; KANTATA-RMI-REPORT-2026]. Runn: about one in ten resource managers use
  AI, sample not stated [RUNN-2025].
- Law firms: 43% of resourcing decisions lawyer-led; 45% have partial skills data; associate departures 9% to 16%,
  2024 to 2025 [BIGHAND-DLAPR-2026]. Talent capacity is the top profitability constraint for 35% of law-firm COOs
  [WESTERNALLIANCE-COO-2026]. In-house (2025, 186 organisations): 63% name workload and bandwidth the top challenge
  [CLOC-SOTI-2025].

**Measured results (independent, adjacent)**
- Algorithm versus manager case assignment: about 5 points lower on-time completion (control about 40%); suggested
  dates about 4 points higher; 1,405 cases, 95 analysts, public agency [IPA-PERU-2026].
- Individuals with AI matched two-person teams without AI; 776 professionals at Procter & Gamble [NBER-DELLACQUA-2025].

**Named organisations, vendor-published (unaudited)**
- DLA Piper 600+ hours saved finding resources at half-year end (about GBP 673,000 stated); Womble Bond Dickinson 10%
  utilisation gain over two years and 33.3% retention gain in one practice group [BIGHAND-DLAPR-2026; BIGHAND-WBD-2026].
- Hakkoda 10% absolute project-margin gain, about 5% utilisation gain [KANTATA-FORECAST-2026]. Nextview's agent scans
  150 colleagues "in seconds" [CERTINIA-CUSTOMERS-2026].

**Vendor claims (no baseline, sample or method):** up to 10 hours a month back to resource managers
[CPAPA-CERTINIA-2026]; 40% better planning accuracy [KANTATA-AGENT-2026]; 20% better forecast accuracy
[DELTEK-POLARIS-2026].

**Quality evidence: none.** No error, override, acceptance or parallel-run figure for an AI staffing recommendation was
found. **What to measure:** time to staff a role; recommendations accepted, changed or rejected and why; on-time start;
bench days; utilisation by band, not just average; forecast error by horizon; who got stretch work; where saved hours
went; agent cost and output per engagement.

## 6. Guardrails

- **Task allocation is named in law.** EU AI Act Annex III 4(b) lists AI used to allocate tasks based on individual
  behaviour or personal traits, or to monitor and evaluate workers, as high-risk [EU-AIACT-ANNEX3-2024]; obligations
  apply from 2027-12-02 [EC-AIACT-2026]. Deployers inform workers before use, keep logs for at least six months and owe
  explanations in some decisions (Art. 26(6), 26(7), 86) [EU-AIACT-OJ-2024]. California's CCPA regulations list
  "allocation or assignment of work" as a significant decision; automated decisionmaking technology (ADMT) used for one
  must comply by 2027-01-01, and human involvement means a reviewer with authority to change the decision
  [CPPA-CCPAREGS-2026]. Whether a skills-and-availability matcher is in scope is not settled; get legal advice.
- **Other employment AI rules:** Illinois from 2026-01-01 [ILLINOIS-HB3773-2024]; Colorado SB26-189 signed
  2026-05-14 [COLORADO-SB26189-2026]; NYC bias audits [NYC-AEDT-2023], with enforcement found ineffective
  [OSC-LL144-2025]; UK Articles 22A-22D, commencement not checked [UK-DUAA-2025]. Their reach over work assignment is
  unconfirmed. A 2026 class action over applicant scoring by a skills platform is unresolved
  [FISHERPHILLIPS-EIGHTFOLD-2026].
- **Professional texts.** California bar guidance: AI in employment actions may carry bias risk; oversight grows with
  autonomy [CALBAR-GENAI-2026]. ABA Formal Opinion 512: supervision duties; hourly bills reflect actual time
  [ABA-OP512-2024]. ICMCI code for consultants: employment effects are high-risk; a qualified person able to override;
  test for disparate impact; beware nominal oversight [ICMCI-AICODE-2026]. Audit firms: ISQM 1 requires teams with
  competence and time (seen in search summaries only) [IAASB-ISQM1-2020]; see the assurance archetype.
- **Not on the radar:** only 4% of resource-management respondents name compliance as a gap [KANTATA-RMI-REPORT-2026].
- **Design rules from the evidence:** keep recommendations advisory with reasons shown [PROJECTWORKS-2026;
  WK-CCHSTAFF-2026]; keep manager discretion where fit matters [IPA-PERU-2026]; record decisions and overrides (`#21`).

**Steps that stay with a person:** the final assignment, especially senior and client-facing roles; weighing client
chemistry, development and personal circumstances; overriding a recommendation; replacing someone mid-engagement;
utilisation targets for individuals; hire, contract or outsource decisions; deciding what an agent may book on its own.

## 7. Roles and how they evolve

- **Resource managers: from searching to choosing and composing teams.** 72% call the role operational today; under
  outcome-based pricing respondents expect it to own team composition, delivery risk and economics [KANTATA-RMI-2026].
  TSIA calls the future office a "hybrid workforce command center" [TSIA-RM-2026]. Womble Bond Dickinson recruited
  dedicated resource managers [BIGHAND-WBD-2026]; DLA Piper's case study says resourcing professionals become strategic
  partners balancing wellbeing and workforce planning [BIGHAND-DLA-2026]. Reed Smith created a global director of Smart Resourcing
  [REEDSMITH-SMARTRES-2023].
- **Central staffing teams keep the call.** McKinsey's agents supplement, not replace, professional-development staff
  [BLOOMBERGLAW-MCKINSEY-2026].
- **Ops leaders: from monthly reports to acting on alerts and forecasts** (vendor description) [PROJECTWORKS-2026].
- **Associates and consultants: from waiting to be picked to volunteering** for posted work [BIGHAND-WBD-2026]. Project
  variety is the leading driver of consultant job satisfaction in the MCA survey (not AI-specific) [MCA-SURVEY-2026].
- **Administrative roles:** law-firm COOs expect fewer billing administrators and more technology, data and AI
  enablement roles [WESTERNALLIANCE-COO-2026].
- **Flexible talent** covers overflow and AI review [GEEK-LATITUDE-2026]. Pyramid and junior-pipeline questions:
  professional-services-talent-learning-19, -20. Talk about roles and capacity, not headcount.

## 8. Frontier

- **2026-01-08** 87% of 200 leaders plan agents as part of the workforce [KANTATA-SOPSI-2026]; **2026-01-16** Kantata's
  product chief predicts agents planned and measured like capacity [KANTATA-FORBES-2026].
- **2026-04-09** Resource Management Institute study: hybrid teams and outcome data are the gaps [KANTATA-RMI-2026].
- **2026-04-15** Certinia launches Veda with resourcing agents in beta [DIGINOMICA-CERTINIA-2026]; **2026-09-09** adds
  14 agents and 135 intelligent actions [CONSTELLATION-CERTINIA-2026].
- **2026-05-01** McKinsey reported to plan agents for choosing client teams [BLOOMBERGLAW-MCKINSEY-2026].
- **2026-05-04** Planview announces Agent Resource Management, available from Fall 2026 [SDTIMES-PLANVIEW-2026].
- **2026-05-14** Colorado reenacts its AI act; duties from 2027-01-01 [COLORADO-SB26189-2026].
- **2026-06-05** BigHand previews an AI resourcing agent for law firms [BIGHAND-CONF-2026].
- **2026-06-11** First randomised evidence on algorithm versus manager assignment of expert work [IPA-PERU-2026].
- **2026-06-16** Kantata launches Expertise Agent [ERPTODAY-KANTATA-2026]; **2026-07-22** Rocketlane's resource agent
  "in active rollout" [ROCKETLANE-2026].
- **2026-10-13** Basware describes its staffing agent [KANTATA-BASWARE-2026]; Dayshape survey published
  [DAYSHAPE-ONREC-2026].
- **Scheduled:** 2026-10-20 Basware and Kantata on who manages an agent's margin [KANTATA-BASWARE-2026]; 2026-11-17
  Kantata Converge, London [KANTATA-CONVERGE-2026]. Signals only.
- **2027-01-01** California ADMT compliance [CPPA-CCPAREGS-2026]; **2027-12-02** EU high-risk employment rules
  [EC-AIACT-2026].

## 9. Common objections

- **"A model can't know who works well with whom."** A vendor says no model captures client dynamics or fit [PROJECTWORKS-2026], and in
  the Peru trial where removing managers lowered on-time completion [IPA-PERU-2026]. Answer: keep the person deciding;
  use AI to widen the shortlist and show reasons (`#01`), or nudge schedules (`#14`).
- **"Our skills data is rubbish."** Likely: 47% cite fragmented data [KANTATA-RMI-2026] and 45% of law firms have
  partial skills data [BIGHAND-DLAPR-2026]. Answer: firms with figures built the data layer first (`#12`); Basware
  automated billing first [KANTATA-BASWARE-2026].
- **"It will just be fast and wrong."** Kantata's own chief executive warns of "fast, mediocre decisions"
  [KANTATA-SUPERAGENT-2026]. Answer: track overrides and outcomes from day one; nobody publishes them yet.
- **"The numbers are vendor marketing."** True for nearly every figure here. Answer: baseline your own time-to-staff
  and utilisation before you start.
- **"Partners won't give up allocation."** Strategic consensus among partners is hard [WESTERNALLIANCE-COO-2026].
  Answer: law firms moved with opportunity boards and dedicated resource managers [BIGHAND-WBD-2026].
- **"AI will free capacity, so we need fewer people."** Not shown: Big Law demand rose [BLOOMBERG-AICOST-2026] and the
  extra load fell on associates and non-equity partners [TRI-LFFI-Q2-2026]. Answer: measure where hours went (`#20`).
- **"Isn't this regulated HR tech?"** Possibly (§6). Answer: inventory tools, keep a reviewer with authority, log
  decisions (`#21`).
- **"We'll staff agents next year."** None of 44 surveyed organisations runs agents as assignable
  resources yet [KANTATA-RMI-REPORT-2026]. Answer: start by
  costing agent use per engagement (professional-services-delivery-management-16).

## 10. Sources

Full details for YAML keys are in the YAML. Keys cited here but not in the YAML:
- CLOC-SOTI-2025: CLOC, 2025 State of the Industry Report (in-house legal operations), 2025-02-12,
  https://cloc.org/newsdesk/2025-state-of-the-industry-report
- CONSTELLATION-CERTINIA-2026: Constellation Research, Certinia launches System of Action, scales Veda AI agents,
  2026-09-09, https://www.constellationr.com/insights/news/certinia-launches-system-action-scales-veda-ai-agents-intelligent-actions
- IAASB-ISQM1-2020: IAASB, ISQM 1 (publication page; resource requirements seen in search summaries only), 2020-12-17,
  https://www.iaasb.org/publications/international-standard-quality-management-isqm-1-quality-management-firms-perform-audits-or-reviews
- KANTATA-CONVERGE-2026: Kantata, Kantata Converge: Where AI Meets Expertise (event 2026-11-17), 2026-10-08,
  https://www.kantata.com/blog/article/kantata-converge-where-ai-meets-expertise
- MCA-SURVEY-2026: Management Consultancies Association, MCA Member Survey 2026 (1,060 consultants), 2026-01-20,
  https://www.mca.org.uk/reports/mca-member-survey-2026
- RUNN-2025: Runn, 90% of Resource Managers Still Do Not Use AI (Resource Management Unfiltered survey), 2025-09-12,
  https://www.runn.io/blog/90-percent-of-resource-managers-still-dont-use-ai
- WESTERNALLIANCE-COO-2026: Western Alliance Bank, AI Is Driving Change, but the Hard Decisions Are Still Human (law
  firm COO roundtable on the 2026 Blickstein survey), 2026-07-31,
  https://www.westernalliancebancorporation.com/insights/ai-driving-change-hard-decisions-are-still-human
