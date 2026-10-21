# FP&A and performance (advisory)

Sources checked 2026-10-20 and verified against the sources 2026-10-21. Use cases live in `../use-cases/fpa-performance.yaml` (14 entries). Ids are shortened
here: `#04` means `advisory-fpa-performance-04`; other modules' ids are in full. Source keys in brackets, such as
[ONESTREAM-FPATRENDS-2026], are in the YAML or in §10. **Public evidence is the thinnest in the advisory archetype.**
No entry is graded A; 2 of 14 are B (`#02`, `#05`), 11 are C and 1 is an idea (D). No advisory firm has published an
error rate, edit or override rate, parallel run, forecast-accuracy figure or cycle time for AI-assisted FP&A work.
Most material is firm service pages, vendor alliance announcements and vendor-sponsored surveys. Say so when you quote
a figure.

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

FP&A (financial planning and analysis: budgets, forecasts, variance analysis and management reporting) delivered to
private and middle-market clients, plus performance-improvement work (finding cost, pricing and driver problems) and
the technology advisory around it: selecting and implementing planning software (CPM, corporate performance
management platforms) and ERP (the core accounting system). Practitioners sit in top-100 and mid-market accounting
firms, PE-backed advisory platforms, Big Four and outsourcing providers selling managed FP&A, and client in-house
teams. Fractional CFO work and the CAS 13-week cash forecast are in client-accounting-services; controls over a
client's AI are in risk-controls; the firm's own pricing and staffing are in professional-services.

## 2. Processes and key steps

| Step | What happens | Work type | Typical pain |
|---|---|---|---|
| Budget cycle | Collect inputs from departments, route approvals, consolidate, challenge targets | coordination-scheduling, data-reporting, expert-judgment | Budgets emailed as spreadsheets to dozens of people, consolidated by hand, no audit trail or role-based access [ARMANINO-FPAROADMAP-2025] |
| Rolling forecast | Update a baseline forecast (a rolling forecast keeps a fixed horizon ahead) from actuals and drivers | data-reporting | 44% can plan with high confidence only up to three months ahead [ONESTREAM-FPATRENDS-2026] |
| Scenario planning | What-if cases on price, headcount, demand, investment | expert-judgment | Only 19% of FP&A teams can run a scenario in real time or within a day [ONESTREAM-FPATRENDS-2026] |
| Variance and flux analysis; management and board reporting | Explain movements against budget or prior period (flux analysis), write the narrative | data-reporting, document-production | 47% of time on data collection and validation, 32% on insight [ONESTREAM-FPAWEBINAR-2026] |
| KPI views and ad hoc questions | Dashboards, answers for business users | data-reporting, client-interaction | Reports built by hand and answers buried in documentation (OneStream's account of Cox Enterprises) [ONESTREAM-FPAWEBINAR-2026] |
| Planning-model build and change | Dimensions, entities, drivers (a driver-based model links the numbers to operating drivers such as volume or headcount) | software-systems | Model changes have needed specialist administrators or consultants; RSM pitches building models without them [RSM-ABACUM-2026] |
| Performance improvement | Diagnose cost, pricing, working capital and driver issues | research-synthesis, expert-judgment | Gartner says many AI initiatives still aim at incremental improvements rather than hard-to-diagnose problems [GARTNER-FPALEADER-2026; GARTNER-AIREPORTCARD-2026] |
| Readiness, operating model and roadmap | Assess data, process and maturity; rank use cases | expert-judgment | Where AI pilots had moderate or limited success, 53% name data quality and 47% integration as barriers to scaling [RSM-MMAI-2026] |
| CPM and ERP selection and implementation | Choose, integrate, train, manage change | software-systems, coordination-scheduling | More than a quarter of organisations exceeded ERP project budgets [PANORAMA-ERP-2026]; 63% of finance organisations said AI implementation was slower than expected in 2025 [GARTNER-AIREPORTCARD-2026] |
| Managed or co-sourced FP&A | An outside team runs forecasting and reporting on a recurring basis | data-reporting, expert-judgment | Provider maturity varies from production to demonstrations [ISG-FAOFPA-2026] |

## 3. Where AI is changing the work

Lenses: improve (assist or augment a step; "(process)" marks entries that also redesign the flow), automate (no
person on the normal path), delegate (an agent owns a multi-step outcome), reinvent (the service or operating model
changes). Improve is crowded. Automate has one entry (`#04`, announced). Delegate has one (`#13`, announced, provider
claims relayed by an analyst). No automate-step entry and no delegate entry at step or process scope has evidence.

**Reporting and variance**
- Improve: `#01` AI drafts variance and flux commentary and board-pack narrative from the planning model; an analyst
  edits and a named reviewer signs off (Forvis Mazars and Armanino deliver Solver; an unnamed CFO recalls 40 people
  cut to five reviewers [KPMG-CFOREMODEL-2026]; grade C). Bookkeeping-based packages and ledger dashboards are in
  advisory-client-accounting-services-06.
- Improve: `#05` natural-language reporting, cited search of finance documentation and contract-reading agents in the
  planning platform (Cox Enterprises in-house, private preview; vendor-presented 90% less time per ad hoc report; grade B).
- Improve: `#06` (assist) governed planning data reaches Claude, ChatGPT or Slack through MCP (Model Context
  Protocol, a standard way to connect AI assistants to data) (Abacum, announced; grade C).

**Forecasting and scenarios**
- Improve: `#02` a machine baseline forecast that the adviser adjusts (Jirav in CAS and advisory firms: Creative
  Planning from 10 to over 200 clients, vendor release, 2024; grade B). The CAS 13-week forecast is in
  advisory-client-accounting-services-07.
- Improve (process): `#03` continuous, driver-based planning with AI-assisted scenarios in place of the annual
  budget (RSM, Grant Thornton and KPMG pitches and webcasts; grade C).

**Budget cycle**
- Automate: `#04` budget input collection and approval routing automated in the planning platform (Abacum claim; it
  does not say agents do it; Armanino pitches replacing emailed spreadsheets; grade C).

**Planning models and platforms**
- Improve: `#07` models built and changed in plain language, with agents cascading structural changes (Abacum via
  RSM; grade C). An adjacent test found frontier LLMs solved 42 to 63 of 100 synthetic LBO cases [SSRN-VIDAL-2026].
- Improve (process): `#10` firms add AI-embedded planning platforms to their implementation practice (RSM and CFGI
  with Abacum, CohnReznick with Workday Adaptive Planning, Forvis Mazars with Solver; announced; grade C).
- Improve: `#11` (assist) partners enable and govern native agents in Sage Intacct, Microsoft and NetSuite
  (Armanino, EisnerAmper, Rand Group; grade C).

**Performance improvement**
- Improve: `#08` AI and LLM analysis to find and size pricing and cost opportunities (an unnamed automotive company's
  $100 million savings in KPMG's article; grade C, the thinnest entry).

**Readiness and governance**
- Improve: `#09` (assist) readiness and data-foundation assessment with a ranked roadmap (CFGI's five-week Phase 0;
  CohnReznick data checks; Citrin Cooperman buying an AI implementation firm; grade C). CAS-level AI adoption advice is
  advisory-client-accounting-services-20.
- Idea: `#14` validation, back-testing (checking a forecast method against past actuals) and sign-off protocol for
  AI forecasts sold as a service (D). Controls before a client's agents go live are advisory-risk-controls-21.

**Service and operating model**
- Reinvent: `#12` partner-led implementation of an AI-native ERP (Rillet with Armanino and Wiss; vendor says as
  little as 4 weeks to implement; grade C).
- Delegate and reinvent: `#13` managed FP&A with agent-led forecasting and variance analysis, priced on outcomes
  (ISG profiles of PwC, EY, Deloitte, EXL, Sutherland; grade C). Not yet evidenced at mid-market accounting firms.

## 4. Interview probes

Ask in the person's setting (mid-market firm advisory group, PE-backed platform, Big Four or outsourcer, client FP&A).

1. **"Which FP&A deliverables (variance commentary, board pack, forecast, dashboard) does your team draft with AI now?
   What share survives review unchanged, and what do you log?"** Reveals the ladder position (`#01`, `#05`) and whether
   anyone tracks edit or override rates. No public source reports them.
2. **"Before you recommend a planning platform or an ERP agent, how do you test the client's data, and what happens
   when it fails?"** Reveals whether readiness work (`#09`) exists. Data quality is the barrier every survey names.
3. **"Do you back-test machine forecasts against actuals, and against the manual forecast they replace?"** Reveals
   whether `#02` claims can be checked. No accuracy figure for any tool was published.
4. **"How far ahead does your client plan with confidence, and how long does a new scenario take?"** Compare with 44%
   (three months) and 19% (a day) [ONESTREAM-FPATRENDS-2026]. Reveals the opening for `#03`.
5. **"How are budget inputs collected and approved today?"** Emailed spreadsheets point to `#04` and to platform work
   (`#10`) before any agent.
6. **"What evidence does a reviewer leave that AI output was checked, and could the client's auditor replay it?"**
   Reveals control maturity [CPAPA-AGENTSCLOSE-2026] and the opening for `#14` or advisory-risk-controls-21.
7. **"Which planning or ERP vendors are you partnered with, and what client result from your last implementation can
   you show?"** Reveals whether `#10` to `#12` are offers or delivered work. No firm has published a client result.
8. **"Which of these clients are audit clients of your firm or an affiliate, and who decides which FP&A or system
   services they can buy?"** Reveals independence handling (§6; assurance-acceptance-independence-15).
9. **"Are you selling, or competing with, managed FP&A or outcome-linked fees? For which clients?"** Reveals exposure
   to `#13` and the contingent-fee edge; the firm's own pricing goes to professional-services-scoping-pricing-19.
10. **"When AI cuts the hours behind a deliverable, what happens to the fee, the margin and junior analyst time?"**
    Route to professional-services-scoping-pricing-17 and professional-services-talent-learning-07.
11. **"Where are your clients putting their consulting and AI budget, and is any of it moving away from you?"**
    Among AI-using mid-market firms raising AI spend, 40% take budget from external consulting [RSM-MMAI-2026].
12. **"If a client asked tomorrow for proof of how you protect their data in AI tools, what would you hand over?"**
    Three in five accountants say clients ask always or frequently [INTUIT-ACCTTECH-2026].

## 5. Metrics and benchmarks

| Measure | Figure | Source and provenance |
|---|---|---|
| Active AI use in finance, 2024 to March 2026 (1,013 leaders, revenue $250M+; $500M+ in US) | 30% to 75% | [KPMG-AIFINANCE-2026] self-reported, firm survey |
| Reporting stronger forecast accuracy over the past year (same sample) | 64%; no measured error rate | [KPMG-AIFINANCE-2026] self-reported |
| Error-reduction improvement, assurance-ready versus other organisations | 33% vs 6% | [KPMG-AIFINANCE-2026] self-reported |
| Fully assurance-ready for AI-enabled finance; track where AI fails | 42%; 29% | [KPMG-AIFINANCE-2026] self-reported |
| AI implementation slower than expected in 2025 (Gartner report card; its chart draws on a March 2026 survey of 204 finance leaders) | 63%; forecasting and insight among the lowest-rated uses | [GARTNER-AIREPORTCARD-2026] independent |
| Finance teams deploying AI versus scaling it across the function | 84% vs 4% (sample not stated) | [GARTNER-FPALEADER-2026] independent |
| FP&A teams using generative AI / ML in forecasting (475 respondents) | 21% / 12% | [ONESTREAM-FPATRENDS-2026] vendor-published |
| Teams describing themselves as optimized or performing well | 22% | [ONESTREAM-FPATRENDS-2026] vendor-published |
| Forecast quality, AI users vs non-users (definition not stated; not causal) | 64% vs 35% | [ONESTREAM-FPAWEBINAR-2026] vendor-published |
| Formal AI governance ready to scale / informal or none | 19% / 59% | [ONESTREAM-FPAWEBINAR-2026] vendor-published |
| Work time spent verifying or correcting AI output (270 CFOs and leaders) | 26% average | [CFODIVE-DATARAILS-2026] vendor-published |
| Mid-market companies using genAI / operationalised at scale (sample not stated in the release) | 94% / 2% | [KAUFMANROSSIN-AIMIDMARKET-2026] self-reported, firm survey |
| AI-spend increasers reallocating from external consulting | 40% | [RSM-MMAI-2026] self-reported, firm survey |
| Accountants using AI for financial forecasting as a client service, one of the top three uses (725) | 51% | [INTUIT-ACCTTECH-2026] vendor-published |
| Planning and reporting cycle-time cut, firm page for a vendor platform | 50-70%; no baseline or method | [COHNREZNICK-WORKDAY-2026] vendor-published |
| Cox Enterprises ad hoc report / document lookup time | 10 min to 1 min / 8 min to 30 s | [ONESTREAM-FPAWEBINAR-2026] vendor-published |
| AI-native ERP implementation | as fast as 4 weeks vs 12 months (release); typically 4-6 weeks vs 3-12 months, led by the vendor's own team (FAQ, 2026-08-25); no sample | [RILLET-SERIESB-2025] vendor-published |
| GPs ranking operational improvements the top value creation lever (not AI) | 72% | [SPGLOBAL-PE-2026] survey |
| PE leaders still piloting AI / reporting revenue growth from AI | 45% / 24% (date not found) | [GT-PEAI-2026] firm survey |

Independent quality evidence is adjacent only: a Journal of Accounting Research field study links generative AI to
faster month-end close in SME bookkeeping and finds relying on non-consensus AI recommendations can raise error risk
[STANFORD-JAR-2026]; the LBO test above [SSRN-VIDAL-2026]. Neither covers FP&A. **What to measure in a pilot:** a
30-60 day pilot on one workflow measuring time saved, added review time and errors [JOFA-CASAI-2026]; forecast error
against actuals and against the manual forecast; share of drafted commentary edited or rejected; days from period end
to board pack; time to run a scenario.

## 6. Guardrails

- **Independence (the firm's own audit clients).** For SEC issuer audit clients, financial information systems design
  and implementation impairs independence unless the results will not be subject to audit procedures, and management
  functions (any decision-making, supervisory or ongoing monitoring function) are listed separately
  [SEC-RULE2-01-2026, (c)(4)(ii), (vi)]. Contingent fees on any service to such a client impair independence
  [SEC-RULE2-01-2026, (c)(5)]. The AICPA says developing or hosting an AI system for an attest client can raise
  independence concerns, and existing nonattest rules still apply [JOFA-ETHICSAI-2026]. IESBA treats hosting an audit
  client's data as assuming a management responsibility [IESBA-TECH-2023]. Whether a given FP&A, platform or managed
  scope crosses these lines was not analysed, and the AICPA Code text for private-company clients was not read. Use
  the gate in assurance-acceptance-independence-15.
- **Who can sell what.** CFGI (PE-backed, does not audit) markets "no audit restrictions" [CFGI-FINEFFECTIVENESS-2026].
  Firms in an alternative practice structure (APS: an investor-backed advisory entity beside a separate CPA firm) split
  attest and non-attest work, and Crowe notes some services may not be available to attest clients [CROWE-KKR-2026].
- **Internal control over generative AI.** COSO's 2026-02-23 publication maps AI capabilities, including insight
  generation, to the 17 principles of its framework [COSO-GENAI-2026; DELOITTE-DART-COSO-2026].
- **Practitioner control list.** Agent inventory with a named owner, replayable evidence, sign-off gates scaled to
  risk, third-party assurance read closely, monitoring with an exit threshold [CPAPA-AGENTSCLOSE-2026]. Its
  statement that AICPA had no SOC guidance on AI appears superseded [JOFA-PRACTICEAID-2026].
- **Deliverable quality.** Deloitte Australia agreed to repay the final instalment of a roughly AU$440,000 contract
  after a report contained incorrect references [CITYAM-DELOITTE-2025]. See professional-services-quality-review-04.
- **Client data.** The AICPA Code means asking whether client consent is needed before client data goes into an AI
  tool [JOFA-ETHICSAI-2026]. Only 21% of firms have an AI policy or strategy [KARBON-AISTATE-2026]. Pigment says
  customers choose what its AI can access and data is excluded from training [PIGMENT-AI-2026] (vendor statement).
- **Assurance expectations.** KPMG says regulators and external auditors increasingly require proof that AI-enabled
  finance processes are controlled and explainable [KPMG-AIFINANCE-2026].
- **Steps that need human judgment:** target-setting and challenge of assumptions; which variance explanation is true;
  scenario triggers and contingency actions; which opportunities to pursue; model structure; sign-off of anything
  that feeds financial statements, a board or a lender; for audit clients, every management decision.

## 7. Roles and how they evolve

- **Analysts move from producing to interpreting.** KPMG's Erin McShane sees talent needs moving from a reporting
  factory toward interpreting AI outputs and advising leaders [KPMG-CFOREMODEL-2026]. One unnamed company moved
  variance commentary from 40 producers to five reviewers (recalled figure, same source).
- **Pyramid to diamond.** Gartner says AI is turning the finance pyramid into a diamond by eliminating entry-level
  roles, and recommends upskilling analysts into citizen data scientists and adding AI product managers and knowledge
  engineers [GARTNER-FPALEADER-2026]. It also expects finance staff to become tool-building "catalysts"
  [GARTNER-TALENT-2026]. See professional-services-talent-learning-19 and -20.
- **New senior advisory roles.** CFGI sought a managing director to lead AI strategy assessments and take proprietary
  finance tools to market [CFGI-JOB-2026]. Aprio's manager posting asks for budgets, 13-week cash flow models and
  scenario analyses, and separately for AI-enabled workflows and delivery methods [APRIO-JOB-2026].
- **Hiring signals.** 38% of respondents name strategic judgment as the expertise they prioritise most in hiring and 22% AI
  fluency; 56% say a new
  entry-level hire needs six months or more to reach full billable capacity [INTUIT-ACCTTECH-2026].
- **Client workforces will change too.** 88% of mid-market respondents expect their workforce to look fundamentally
  different within two to three years [RSM-MMAI-2026].
- **Providers converge.** ISG says consulting and accounting firms are increasing their role in managed services, and
  experienced finance talent, industry context and data foundations drive differentiation [ISG-FAOFPA-2026].
- **Fractional CFOs** see AI making clients more comfortable with part-time finance leadership
  [CFODIVE-FRACTIONAL-2026]; that work sits in advisory-client-accounting-services-08.

## 8. Frontier

- 2026-02-23: COSO publishes guidance on internal control over generative AI [COSO-GENAI-2026].
- 2026-04-09: Abacum launches agents that flag anomalies, draft narratives, model scenarios and connect to Claude,
  ChatGPT and Slack through MCP [ABACUM-INTELLIGENCE-2026].
- 2026-05-28: EY and Microsoft run a CFO AI Lab on moving to agentic finance, FP&A among the examples (event page
  only) [EY-CFOAILAB-2026]; Gartner ranks forecasting among the lowest-rated uses [GARTNER-AIREPORTCARD-2026].
- 2026-06-22 and 2026-09-05: RSM and CFGI announce Abacum alliances [ABACUM-RSM-2026; ABACUM-CFGI-2026].
- 2026-07-08: the 10th FP&A Trends Survey is released [ONESTREAM-FPATRENDS-2026]; in the replay webinar (page dated
  2026-07-09), 15% expect to use AI agents within six months and 51% at some point [ONESTREAM-FPAWEBINAR-2026].
- 2026-07-29 and 2026-08-20: KPMG ("From Forecasting to Value Steering") and Grant Thornton (AI-enabled, continuous
  forecasting) CFO webcasts [KPMG-WEBCASTS-2026; GT-FORECASTWEBCAST-2026].
- 2026-08-12: Sage Intacct's Finance Intelligence Agent in phased rollout; partner agent marketplace announced
  [ARMANINO-INTACCTR3-2026].
- 2026-09: ISG lists expansion of managed FP&A and tax services, and commercial structures linked to transactions
  or outcomes, among leading indicators for finance outsourcing [ISG-FAOFPA-2026].
- 2026-09-29: KPMG describes a flux-analysis agent built in three weeks at an unnamed company [KPMG-CFOREMODEL-2026].
- 2026-10-01: Citrin Cooperman's acquisition of AI consulting firm Rosetree takes effect, aimed at middle-market AI
  implementation [ACCTODAY-ROSETREE-2026].
- 2026-10-19: AICPA and AIUC announce a CPA-led SOC 2 plus AIUC-1 engagement for AI systems; full launch expected
  early 2027 [JOFA-AIUC-2026] (assurance; advisory-risk-controls-17).
- 2026-12-06 to 09 (scheduled): Digital CPA, the CAS and advisory technology conference; agenda not read
  [CPACOM-DCPA-2026].

## 9. Common objections

- **"AI won't make our forecasts better."** Independent data agree so far: forecasting and insight generation are
  among the lowest-rated finance AI uses [GARTNER-AIREPORTCARD-2026]. KPMG's 64% is self-reported, and OneStream's
  presenter says AI compounds an existing advantage rather than creating one [ONESTREAM-FPAWEBINAR-2026]. Response:
  back-test any machine baseline against actuals before relying on it (`#02`); start with commentary and reporting.
- **"Our client's data isn't ready."** Usually true: data quality is the top barrier in every survey read, and
  OneStream's presenter warns that AI on poor data "automates the mess faster" (vendor view). Response: sell the
  readiness work first (`#09`) and the platform second (`#10`).
- **"We can't audit what the AI did."** 75% of surveyed CFOs and finance leaders cite lack of auditability, 71% accuracy and 54%
  compliance [CFODIVE-DATARAILS-2026]. Response: replayable evidence and risk-scaled sign-off gates
  [CPAPA-AGENTSCLOSE-2026]; agents that show their sources and steps built trust at Cox, per the vendor's
  presenter (`#05`).
- **"Checking AI eats the savings."** A vendor survey puts verification at 26% of work time [CFODIVE-DATARAILS-2026].
  Response: measure added review time in the pilot, not only time saved [JOFA-CASAI-2026].
- **"The vendor numbers are hype."** Correct: 50-70%, 4 weeks and 90% have no published method. GRF says the strongest
  parts of a 2026 ERP release were usability gains rather than headline AI [GRF-INTACCTR2-2026]. Response: reproduce
  claims on the client's own data before quoting them [CPAPA-AGENTSCLOSE-2026].
- **"Clients will do it themselves."** 40% of AI-spend increasers take budget from external consulting; the survey
  does not say what replaces it [RSM-MMAI-2026]. A consultant says clients already arrive having self-prepared work with AI
  tools, and firms outside advisory risk being caught on their heels [ACCTODAY-CATALYST-2026]; a fractional CFO says some clients could do the
  accounting with AI and some probably will, though he has been surprised by the lack of desire to do so
  [CFODIVE-FRACTIONAL-2026].
- **"Bigger firms will come down market."** Withum's Jim Bourke says they already are, "leveraging AI to do work
  faster" [ACCTODAY-CASKEYS-2026]. Response: the mid-market alliances in `#10` are the same move from the other side.
- **"Independence rules make this unsellable."** Only for the firm's own audit clients, and only for listed services
  [SEC-RULE2-01-2026]; most advisory clients are not audit clients. Check each case (§6).
- **"Outcome-priced managed FP&A is the future."** It is a stated direction [ISG-FAOFPA-2026], with no published firm
  results, and contingent fees are barred for issuer audit clients (`#13`).
- **"The ROI case is obvious."** An Accounting Today opinion piece models 40-60% workload cuts for a hypothetical
  company; it is an illustration, not data [ACCTODAY-AQUILA-2026].

## 10. Sources

Full details for keys used in the use cases are in the YAML. Keys cited above that are not in the YAML:

- ACCTODAY-AQUILA-2026: "Will AI replace accounting firms in the small biz market?" (opinion, August Aquila), Accounting Today, 2026-08-24, https://www.accountingtoday.com/opinion/will-ai-replace-accounting-firms-in-the-small-biz-market
- ACCTODAY-CATALYST-2026: "AI - the catalyst and solution to advisory", Accounting Today, 2026-07-13, https://www.accountingtoday.com/news/ai-the-catalyst-and-solution-to-advisory
- CFODIVE-FRACTIONAL-2026: "Fractional CFOs see demand surge in AI age", CFO Dive, 2026-08-06, https://www.cfodive.com/news/fractional-cfos-see-demand-surge-ai-age/827264/
- CPACOM-DCPA-2026: Digital CPA Conference 2026 (event page), CPA.com, scheduled 2026-12-06 to 09, https://www.cpa.com/dcpa25
- CROWE-KKR-2026: "Crowe closes strategic investment from KKR", Crowe, 2026-08-07, https://www.crowe.com/news/crowe-closes-strategic-investment-from-kkr
- EY-CFOAILAB-2026: "CFO AI LAB - AI-Driven Finance: How to scale from AI use cases to agentic finance" (event page), EY Finland with Microsoft, 2026-05-28, https://www.ey.com/en_fi/events/2026/05/cfo-ai-lab-ai-driven-finance-how-to-scale-from-ai-use-cases-to-agentic-finance
- GT-PEAI-2026: "Private equity insights: 2026 AI Impact Survey" (summary only; publication date not found), Grant Thornton, 2026, https://grantthornton.com/insights/survey-reports/private-equity/2026/private-equity-insights-2026-ai-impact-survey
- IESBA-TECH-2023: "Final Pronouncement: Technology-related Revisions to the Code" (606.3 A1), IESBA, 2023-04-11, https://www.ethicsboard.org/publications/final-pronouncement-technology-related-revisions-code
- JOFA-AIUC-2026: "AICPA partners on new offering that assures AI systems and agents", Journal of Accountancy, 2026-10-19, https://www.journalofaccountancy.com/news/2026/oct/aicpa-partners-on-new-offering-that-assures-ai-systems-and-agents/
- JOFA-ETHICSAI-2026: "Accounting ethics in the age of AI", Journal of Accountancy, 2026-08-05, https://www.journalofaccountancy.com/issues/2026/aug/accounting-ethics-in-the-age-of-ai/
- KARBON-AISTATE-2026: "2026 State of AI in Accounting Report" (vendor survey, about 600 respondents), Karbon, 2026-01-20, https://karbonhq.com/resources/state-of-ai-accounting-2026
- STANFORD-JAR-2026: "Human + AI in Accounting: Early Evidence from the Field" (Choi and Xie, abstract read), Journal of Accounting Research 64(3), 2026-06, https://www.gsb.stanford.edu/index%2ephp/node/629989
