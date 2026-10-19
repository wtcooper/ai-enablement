# Scoping and pricing: governance and evidence (professional services)

Archetype: professional-services. Module: scoping-pricing. Angle: governance (what constrains and measures the work). Prepared 2026-10-19. Public sources only. Method: curl, pdftotext and one text-mirror call for page dates; eight web searches before the shared search budget ran out.

## 1. Summary

- **What the evidence is.** 37 sources were opened and read (list in section 5): 3 regulator, 4 professional-body, 1 standard-setter, 4 academic, 7 survey, 2 conference-coverage, 4 vendor and 12 press items. There is no measured outcome at grade A. Six use cases are grade B (named organisation, no published measurement), five are C and seven are D (ideas, labelled).
- **Hourly billing is the most tightly governed pricing model.** Texas, DC, North Carolina and California all say an hourly fee must reflect time actually spent, so time saved by AI cannot be billed (DCBAR-OP388-2024; TXETHICS-OP705-2025; NCBAR-FEO1-2024; CALBAR-GENAI-2026). ABA Formal Opinion 512 is quoted to the same effect (TRI-ABA512-2025; the opinion text was blocked).
- **Fixed and value fees are where regulators diverge.** ABA 512, as quoted, says the same flat fee may be unreasonable if a tool makes the work much quicker; Virginia LEO 1901 (approved 24 Nov 2025) says Rule 1.5 does not equate reduced time with proportionally reduced fees and criticises that line (VSB-LEO1901-2025). California says flat fees may build in the savings (CALBAR-GENAI-2026). A firm quoting AI-assisted flat fees needs the state's position, not a general rule.
- **Accounting has a harder pricing rule.** The AICPA Code bars contingent fees for audit, review and certain other clients, and for tax-return preparation for any client (AICPA-CODE-2026, 1.510.001). Outcome-linked pricing therefore cannot simply be copied from consulting into accounting (BLOOMBERGTAX-PRICING-2026 shows firms exploring value-based pricing).
- **Clients, not regulators, are the faster-moving constraint.** Nearly 60% of surveyed in-house counsel saw no noticeable savings yet from outside counsel's AI use (BLOOMBERGLAW-ACC-2025). At Legalweek 2026 firms said they were still gathering data on AI savings while clients asked for line-item AI transparency and some said they would not pay for AI-performed work (TRI-LEGALWEEK-2026). Public-sector buyers are adding AI-use declarations and recourse (CANBERRATIMES-APSAI-2025; CTV-DELOITTE-2025).
- **Measurement is the weak link.** SPI's 2026 study of 245 firms reports 84.8% say AI saves them time; the matching share saying it generates revenue is withheld on the landing page (SPI-AI-2026). Only 38% of A&E firms in Deltek's study reported measurable positive business impact (DELTEK-CLARITY-2026). No published error, override or parallel-run rate for AI-generated estimates or fee proposals was found.
- **Academic work is conceptual.** The only 2026 academic paper on AI and consulting pricing is a principal-agent framework, not an empirical test; its authors say the fit to practice is qualitative plausibility (STANFORD-DEL-2026, Section 2).

## 2. Use cases

```yaml
- id: professional-services-scoping-pricing-01
  archetype: professional-services
  module: scoping-pricing
  title: 'Hourly-fee estimates and budgets re-based on actual AI-assisted time (idea: set by bar opinions rather than a measured deployment)'
  function: service-delivery
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Hourly budgets and quotes were built on how long tasks took before generative AI. Several bar opinions say an hourly fee must reflect time actually spent, so quoting or billing legacy task hours for AI-assisted work is a compliance risk.
  solution: 'Estimators build the hourly budget from the effort of AI-assisted work (writing prompts, reviewing and editing outputs), bill actual time, and state in the fee agreement how generative AI factors into rates and costs. Pattern is other: a rule-bound estimating step, not an agent.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: n/a
  prerequisites:
  - A fee agreement that says how fees and costs are calculated and how far generative AI factors into rates (CALBAR-GENAI-2026, Charging for Work section)
  - Time records that show actual time spent, including time spent crafting inputs and reviewing outputs (CALBAR-GENAI-2026; TXETHICS-OP705-2025, Fees)
  risks_and_guardrails:
  - A lawyer on an hourly agreement may not charge for hours saved by the tool; the DC opinion says the economies must go to the client (DCBAR-OP388-2024, section E; TXETHICS-OP705-2025, Fees)
  - 'North Carolina gives a worked example: three hours of drafting that now takes one hour cannot be billed as three (NCBAR-FEO1-2024, Opinion #6)'
  - ABA Formal Opinion 512, as quoted by a commentator, says a lawyer who bills hourly must bill actual time (TRI-ABA512-2025; the opinion text itself was not reachable)
  human_checkpoints:
  - The lawyer reviews, verifies and corrects AI outputs and remains responsible for them (CALBAR-GENAI-2026, Competence section)
  role_evolution: none published
  evidence_grade: D
  sources:
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Charging for Work Produced by Generative AI and Generative AI Costs, p. 8
  - ref: DCBAR-OP388-2024
    title: Ethics Opinion 388 (generative AI in client matters)
    publisher: District of Columbia Bar
    type: professional-body
    url: https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388
    date: 2024-04
    access: full
    locator: section E, Fees
  - ref: TXETHICS-OP705-2025
    title: Opinion 705 (generative AI)
    publisher: Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics
    type: professional-body
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Fees section
  - ref: NCBAR-FEO1-2024
    title: 2024 Formal Ethics Opinion 1 (use of artificial intelligence in a law practice)
    publisher: North Carolina State Bar
    type: professional-body
    url: https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/
    date: '2024-11-01'
    access: full
    locator: 'Inquiry and Opinion #6'
  - ref: TRI-ABA512-2025
    title: Is ABA Formal Opinion 512 off the mark? And if so, what can law firms and GCs do about it? (William Josten, Honigman; quotes the opinion)
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/aba-formal-opinion-512
    date: '2025-04-02'
    access: full
    locator: section "What Formal Opinion 512 says about attorneys' hourly fees"
  notes: 'Grade D (idea): the evidence is professional-conduct guidance, not a measured deployment, and the scale has no tier for binding guidance. Legal-profession rules; for accounting see AICPA fee rules in use case 06. Texas Opinion 705 (Feb 2025) cites DC 388 and Florida Opinion 24-1 for the same point; the Florida text was not opened.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-02
  archetype: professional-services
  module: scoping-pricing
  title: 'Flat-fee and value-based quotes for AI-assisted work with a documented reasonableness basis (idea: bar opinions diverge)'
  function: service-delivery
  work_types:
  - expert-judgment
  - document-production
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: When AI shortens a task, a fixed fee set at the old effort looks high. Bar bodies disagree on whether the same flat fee remains reasonable, leaving pricing teams unsure how much of the saving they must pass on.
  solution: Pricing teams quote a flat or value-based fee for predictable work and write down why the fee is reasonable (experience, skill in using the tool, value of the output) and explain it to the client, because regulators in some states test reasonableness against the speed gain.
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: n/a
  prerequisites:
  - 'Client consent to the billing structure (NCBAR-FEO1-2024, Opinion #6)'
  - An explanation of the fee basis to the client, including why experience and technical skill contribute value when time spent falls (VSB-LEO1901-2025, Rule 1.5(b) discussion)
  risks_and_guardrails:
  - California says flat fees may build AI time savings into rates, and fee agreements should say how far AI factors into the rates (CALBAR-GENAI-2026, p. 8)
  - ABA Formal Opinion 512, as quoted by a commentator, says it may be unreasonable to charge the same flat fee when a tool makes the task much quicker (TRI-ABA512-2025)
  - 'Virginia LEO 1901 takes a different line: Rule 1.5 does not equate reduced time with proportionally reduced fees, and it criticises the ABA and North Carolina positions (VSB-LEO1901-2025, petition p. 6-8)'
  - North Carolina allows a flat fee for AI-assisted drafting if it is not clearly excessive; the Virginia petition says it is unclear how far the fee must be adjusted (NCBAR-FEO1-2024; VSB-LEO1901-2025)
  human_checkpoints:
  - none published
  role_evolution: none published
  evidence_grade: D
  sources:
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p. 8
  - ref: NCBAR-FEO1-2024
    title: 2024 Formal Ethics Opinion 1 (use of artificial intelligence in a law practice)
    publisher: North Carolina State Bar
    type: professional-body
    url: https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/
    date: '2024-11-01'
    access: full
    locator: 'Opinion #6'
  - ref: VSB-LEO1901-2025
    title: Legal Ethics Opinion 1901, Reasonable Fees and the Use of Generative Artificial Intelligence (adopted page and petition to the Supreme Court of Virginia)
    publisher: Virginia State Bar
    type: regulator
    url: https://vsb.org/Site/news/rules-news/20250327-prop-1901-fees-ai.aspx
    date: '2025-11-25'
    access: full
    locator: petition summary and Summary section; Supreme Court approval 24 Nov 2025
  - ref: TRI-ABA512-2025
    title: Is ABA Formal Opinion 512 off the mark? And if so, what can law firms and GCs do about it? (William Josten, Honigman; quotes the opinion)
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/aba-formal-opinion-512
    date: '2025-04-02'
    access: full
    locator: section "Leaving room for alternatives"
  notes: 'Grade D (idea): guidance, not deployment. The legal-ethics split is itself the finding: ABA 512 and North Carolina are read by Virginia as taking a tougher view on flat fees than Virginia does.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-03
  archetype: professional-services
  module: scoping-pricing
  title: KPI-based monthly retainer or portfolio billing in place of hourly billing (Kopka Law)
  function: service-delivery
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Under hourly billing, finishing a task in 30 minutes rather than three hours cuts the firm's own revenue, and insurer clients audit and cut bills line by line, which costs both sides administrative effort.
  solution: Kopka Law describes moving defence-litigation clients to a monthly retainer or portfolio-based billing model judged on KPIs such as cycle time and case disposition, early evaluation and communication, indemnity outcome relative to injury type, and collaboration, rather than time entries.
  outcomes:
  - lever: cost
    description: Firm reports it avoids bill-audit overhead and rewards efficiency; no figures published
    figure: none
    measures: n/a
    provenance: self-reported
    source_ref: TRI-BILLING-2026
  prerequisites:
  - Client data on claim frequency and severity plus the firm's own data on litigation categories, which the firm says is enough to set an arrangement (TRI-BILLING-2026)
  - Client willingness to enter the negotiation; the firm is inviting carriers to do so (TRI-BILLING-2026)
  risks_and_guardrails:
  - The firm says alternative fee arrangements designed only to save the client money are likely to fail because they push firms to cut corners (TRI-BILLING-2026)
  - The firm says the main brake on others is fear of being underpaid or not knowing how to measure value other than by the clock (TRI-BILLING-2026)
  human_checkpoints:
  - KPI scorecard agreed with the client before the engagement (TRI-BILLING-2026, KPI list)
  role_evolution: The firm's COO says talent is leaving the defence side because of the tedious nature of capturing time (TRI-BILLING-2026)
  evidence_grade: B
  sources:
  - ref: TRI-BILLING-2026
    title: How one law firm is challenging a broken status quo around billing (Kopka Law)
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing
    date: '2026-04-30'
    access: full
    locator: sections "Why the billable hour hates AI" and "Data as the solution"
  notes: Named firm, no published results. The article is a Thomson Reuters Institute interview piece, not a client-verified result. Clients in this case are insurers (in-house claims functions). The article says AI and data analytics put the model within reach for most firms; it does not name AI tools or say how much AI the firm uses.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-04
  archetype: professional-services
  module: scoping-pricing
  title: Outcome-linked consulting fees tied to a client scorecard (McKinsey)
  function: sales-marketing-bd
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Consultants have traditionally billed on project scope and duration, but McKinsey says clients now arrive with the outcome they want and ask for a fee that depends on reaching it (BI-MCKINSEY-2025).
  solution: McKinsey says clients now bring a target outcome and the fee is mostly contingent on performance against a scorecard (investor targets, revenue or profit goals within a timeframe, operating measures, customer satisfaction), with some fixed components remaining.
  outcomes:
  - lever: growth
    description: Share of firm fees on this pricing model
    figure: about a quarter of global fees
    measures: Share of McKinsey global fees that come from the outcomes-based pricing model, as stated by its UK, Ireland and Israel managing partner at a London media event, November 2025
    provenance: self-reported
    source_ref: BI-MCKINSEY-2025
  prerequisites:
  - A client scorecard and a transformation-type engagement; the firm says the model suits multi-year, multidisciplinary transformation work (BI-MCKINSEY-2025)
  - Attribution that is clean enough to bear contractual weight; the Stanford framework says outcome fees only spread as far as attribution is clean (STANFORD-DEL-2026, Section 5.2 and Rule 3)
  risks_and_guardrails:
  - The firm's technology and AI leader said outcomes-based pricing did not start because of AI (BI-MCKINSEY-2025), so the share cannot be read as an AI effect
  - Accounting and audit variants face contingent-fee limits (AICPA-CODE-2026, 1.510.001); consulting has no equivalent in the sources reviewed
  human_checkpoints:
  - Scorecard agreed with the client's board-level targets before work starts (BI-MCKINSEY-2025)
  role_evolution: McKinsey says strategy advice is now under 20% of its work and clients want implementation expertise and multi-year support (BI-MCKINSEY-2025)
  evidence_grade: B
  sources:
  - ref: BI-MCKINSEY-2025
    title: AI is reshaping how McKinsey makes money (Polly Thompson)
    publisher: Business Insider
    type: press
    url: https://www.businessinsider.com/ai-reshapes-how-mckinsey-makes-money-consultancy-025-11
    date: '2025-11-17'
    access: full
    locator: paragraphs quoting Birshan (fee share) and Smaje (scorecard)
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson) and USC Marshall (Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section 5.1 and Section 7, Rule 3
  notes: 'Graded B, not A: "about a quarter" is a rough figure stated at a media briefing, not a published tracked metric. The Business Insider text also quotes Smaje referring to a proportion of 20% that is "probably more recent"; the context is unclear. The landscape file records a secondary report of "about a third" (not opened here). EY''s global managing partner for growth and innovation told Business Insider in January that agents may call for a "service-as-a-software" outcome approach (BI-MCKINSEY-2025).'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-05
  archetype: professional-services
  module: scoping-pricing
  title: Subscription or consumption-priced AI services delivered with a human reviewer (PwC One)
  function: product-service-development
  work_types:
  - document-production
  - expert-judgment
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: Hourly billing does not fit services where an agent does the first-line work and clients log in and describe a problem themselves; PwC leadership says some tax and consulting services will become tools clients use without a PwC person in the loop.
  solution: PwC One is a client-facing platform where autonomous agents perform the work and PwC professionals review outputs. The PwC US CEO described some services potentially being paid for on an annual subscription; PwC says it is rethinking pricing to reflect speed to insight and quality of outcomes.
  outcomes:
  - lever: growth
    description: Services available at launch
    figure: six automated services, with more promised
    measures: Count of automated services on the PwC One platform at launch, per the PwC US CEO interview reported by CPA Practice Advisor
    provenance: self-reported
    source_ref: CPAPA-PWC-2026
  prerequisites:
  - Human touches designed in deliberately where agents do not yet perform at professional grade or where professional expectations require review (NEWSTACK-PWC-2026)
  - Clean attribution if any outcome component is used; Stanford says hybrid pricing is the resting point where the contribution is confounded (STANFORD-DEL-2026, Section 5.2)
  risks_and_guardrails:
  - PwC says accountability sits with the firm and its professionals, with a human reviewer on every PwC One engagement (NEWSTACK-PWC-2026)
  - The platform was described as in beta in March 2026 (NEWSTACK-PWC-2026)
  - The New Stack headline frames pricing and liability as an open question; PwC gave no price specifics (NEWSTACK-PWC-2026; STANFORD-DEL-2026, Section 5.2)
  human_checkpoints:
  - A professional reviews outputs on every engagement, running in the background rather than driving the work (NEWSTACK-PWC-2026)
  role_evolution: The PwC CEO said senior staff who were not "paranoid about being AI-first" would probably be replaced (CPAPA-PWC-2026, reporting the FT)
  evidence_grade: B
  sources:
  - ref: NEWSTACK-PWC-2026
    title: PwC's AI agents are now your consultants, whether you're ready or not (Darryl K. Taft)
    publisher: The New Stack
    type: press
    url: https://thenewstack.io/pwcs-ai-agents-are-now-your-consultants-whether-youre-ready-or-not/
    date: '2026-03-24'
    access: full
    locator: sections "The consulting model question" and "Built for autonomy"
  - ref: CPAPA-PWC-2026
    title: PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' (reports an FT interview with Paul Griggs)
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
    date: '2026-03-25'
    access: full
    locator: paragraphs on subscription and six automated services
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson) and USC Marshall (Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section 5.2
  notes: Named firm, real clients (financial statement analysis, tax incentives, transfer pricing compliance, emissions anomaly detection, early-stage due diligence), but no price, adoption or quality figures published. The subscription language is "potentially paid for" per FT via CPA Practice Advisor; do not state subscription pricing as live. Ladder set to delegate because agents perform the work with reviewer oversight; change_scope model because the service is sold differently.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-06
  archetype: professional-services
  module: scoping-pricing
  title: Value-based and hybrid pricing pilots for accounting and tax advisory work
  function: sales-marketing-bd
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: AI shortens work such as report preparation, so an hourly price falls or margin rises. RSM asked whether the saving is margin or a price cut for the client, and KPMG said AI investment is cost that cannot usually be attributed to individual projects.
  solution: Firms are testing price set on value to the client, and mixing models by phase (time-based for early brainstorming, value-based once options are clear). RKL is piloting an alternative pricing model built on value-based tenets by an outside consultancy, Fore.
  outcomes:
  - lever: growth
    description: Clients onboarded under the pilot model
    figure: several dozen new clients
    measures: New clients RKL onboarded under the value-based alternative pricing model it is piloting, per an RKL tax partner quoted by Bloomberg Tax
    provenance: self-reported
    source_ref: BLOOMBERGTAX-PRICING-2026
  prerequisites:
  - Advisory services that can be tailored and continued through the year, which an AICPA vice president said lend themselves to value-based models (BLOOMBERGTAX-PRICING-2026)
  risks_and_guardrails:
  - 'AICPA Code 1.510.001: a member in public practice shall not take a contingent fee from an audit, review, certain compilation or prospective-financial-information client, or for preparing an original or amended tax return for any client; fees may vary with complexity (AICPA-CODE-2026, 1.510.001 .01 and .04)'
  - 'AICPA 1.230.030: other services to an attest client may not influence the attest fee, except that cost savings from experience on other services may be considered (AICPA-CODE-2026, 1.230.030 .02-.03)'
  - Staff incentives built on hours conflict with value pricing (BLOOMBERGTAX-PRICING-2026)
  human_checkpoints:
  - Partner prices on the value the client attaches to the work, for example by testing whether a proposed fee is fair against value created (PwC US Tax Leader, BLOOMBERGTAX-PRICING-2026)
  role_evolution: A Wipfli executive said firms that encourage technology use but judge people on decade-old metrics will see conflict (BLOOMBERGTAX-PRICING-2026)
  evidence_grade: B
  sources:
  - ref: BLOOMBERGTAX-PRICING-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing (Nicola Trentmann)
    publisher: Bloomberg Tax
    type: press
    url: https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: sections "Pricing Dilemma" and "New Pricing Options"
  - ref: AICPA-CODE-2026
    title: AICPA Code of Professional Conduct (updated for official releases through July 2026)
    publisher: AICPA
    type: standard-setter
    url: https://mn.gov/boa/assets/AICPA%20Code%20of%20Professional%20Conduct_tcm1233-764395.pdf
    date: 2026-07
    access: full
    locator: 1.510.001 and 1.230.030
  notes: Named firms (RSM, KPMG, PwC, RKL, Wipfli), no results published. The AICPA 2025 survey cited in the article (more than 1,000 firms; median net hourly billing rate up nearly 7% over two years to $170; report recommends considering a faster shift away from hourly billing) is context, not an outcome of the pilots. Audit-independence and tax-preparation detail belongs to the assurance and tax archetypes; only the pricing constraint is recorded here.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-07
  archetype: professional-services
  module: scoping-pricing
  title: Staff performance and bonus metrics re-based to cycle time and client satisfaction when pricing moves away from hours
  function: people-hr
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: When staff are paid and promoted on billed hours, efficiency from AI is not rewarded and value pricing meets internal resistance.
  solution: Wipfli is introducing non-traditional metrics, such as client satisfaction and cycle time, as pricing and technology change; a compensation-data analyst argues value pricing allows bonuses on revenue generated instead of hours.
  outcomes:
  - lever: capacity
    description: none published
    figure: none
    measures: n/a
  prerequisites:
  - Pricing model that does not depend on hours billed (BLOOMBERGTAX-PRICING-2026)
  - Cycle-time and client-satisfaction data per engagement (BLOOMBERGTAX-PRICING-2026)
  risks_and_guardrails:
  - Without changing metrics, workers are told to embrace technology but are judged on the same measures as a decade ago (BLOOMBERGTAX-PRICING-2026)
  - TR's 2026 survey says performance frameworks and billing models signal what an organisation values; mismatches with the stated AI strategy undermine it (TR-FOP-2026, "Measure behavior change" recommendation)
  human_checkpoints:
  - none published
  role_evolution: A Big 4 compensation-data founder said people "light up" at the prospect of firms with alternative pricing, because efficiency is not rewarded under hourly billing (BLOOMBERGTAX-PRICING-2026)
  evidence_grade: B
  sources:
  - ref: BLOOMBERGTAX-PRICING-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing (Nicola Trentmann)
    publisher: Bloomberg Tax
    type: press
    url: https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: section "Employee Incentives"
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: 2026-09
    access: full
    locator: Closing recommendations on measuring behaviour change
  notes: Named firm (Wipfli), statement of intent only, no results. In scope here because incentive design is a prerequisite for pricing change; route detail to talent-learning.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-08
  archetype: professional-services
  module: scoping-pricing
  title: Pricing-model choice by locating each engagement on an outcome-observability and input-cost-observability map (idea from academic framework)
  function: sales-marketing-bd
  work_types:
  - expert-judgment
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Pricing is chosen by convention or comfort. When internal AI hides the effort behind a deliverable, hours become a weaker basis for price, but outcomes may still be hard to verify.
  solution: Pricing leads would score an engagement on how well the client can verify results and see true delivery cost, then choose time-based, project-based, access (retainer), outcome-based or hybrid pricing, and apply four decision rules. Internal AI augmentation moves the price basis away from hours; AI embedded at the client raises outcome visibility.
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: n/a
  prerequisites:
  - Assess attribution separately from measurability; telemetry reduces measurement noise but not attribution risk (STANFORD-DEL-2026, Section 5.2 and Rule 3)
  - Measurement infrastructure before shifting to outcome-based pricing (STANFORD-DEL-2026, Rule 3)
  risks_and_guardrails:
  - The authors state the consistency with observed practice offers qualitative plausibility, not confirmatory validation (STANFORD-DEL-2026, Section 2)
  - Informal, unrecorded discussions with three Accenture executives motivated the framework, and the lab has received a general gift from Accenture; the authors say neither is evidence (STANFORD-DEL-2026, footnote and Section 2)
  - Where the consultant's contribution is confounded, hybrid contracts are the destination and not a stop on the way to outcome pricing (STANFORD-DEL-2026, Introduction)
  human_checkpoints:
  - none published
  role_evolution: The paper says firms should treat hybrid pricing capability as a strategic competence (STANFORD-DEL-2026, Rule 4)
  evidence_grade: D
  sources:
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson) and USC Marshall (Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Sections 4, 5, 7 (Rules 1-4) and Section 2
  notes: 'Grade D (idea): a conceptual principal-agent framework with desk-research examples (McKinsey, Deloitte, Accenture, PwC, Palantir, Salesforce), not an empirical test. The paper''s cases of Palantir and Salesforce Agentforce are software vendors, not professional services firms. It cites a Salesforce 2026 pay-per-resolution model as a pricing example (not opened at source).'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-09
  archetype: professional-services
  module: scoping-pricing
  title: Attribution and baseline design added to scoping before an outcome fee is accepted (idea)
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Outcome-based fees need agreed measures that can be attributed to the firm's work. Resource managers say outcome data is rarely available, and 1 in 2 respondents are unsure their organisation will adopt outcome-based pricing.
  solution: At scoping, the team agrees ground-truth metrics, baselines and, where possible, randomised holdouts or controlled rollouts, and decides whether measurement or attribution is the binding constraint before any fee is tied to outcomes.
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: n/a
  prerequisites:
  - Agreed ground-truth metrics, telemetry and third-party verification (STANFORD-DEL-2026, Rule 3)
  - Outcome data accessible to resource and pricing teams; only 7.3% of respondents in the Kantata-commissioned study said outcome data is easily accessible and routinely used in staffing (KANTATA-RMI-2026)
  risks_and_guardrails:
  - Telemetry cannot remove attribution risk; credible causal identification is needed (STANFORD-DEL-2026, Rule 3)
  - Parties may act on the metrics rather than the work once outcomes are metered and priced (STANFORD-DEL-2026, Section 5.2, citing Aaltonen and Stelmaszak 2024)
  human_checkpoints:
  - none published
  role_evolution: Resource managers expect their role to shift from filling hours to maximising delivery success if outcome-based pricing grows (KANTATA-RMI-2026)
  evidence_grade: D
  sources:
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson) and USC Marshall (Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Rule 3 and Section 5.2
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services (Resource Management Institute study commissioned by Kantata)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: paragraphs on outcome data accessibility and outcome-based pricing uncertainty
  - ref: FORRESTER-TECHSVCS-2026
    title: The State Of Technology Services, 2026 (abstract page; report paywalled)
    publisher: Forrester
    type: survey
    url: https://www.forrester.com/report/the-state-of-technology-services-2026/RES192217
    date: '2026-02-24'
    access: full
    locator: 'Summary: technology leaders lean into outcome-based pricing'
  notes: 'Grade D (idea): the framework is academic and the survey is vendor-commissioned (Kantata). RMI figures: 7.3% outcome data easily accessible and routinely used in staffing; 24.6% only informal knowledge of major wins or failures; 24.6% not available to resource management; about 1 in 2 unsure whether their organisation will adopt outcome-based pricing. Denominator is the study respondents (resource management practitioners); sample size not captured in the release. Forrester''s summary says leaders maximise provider value by leaning into outcome-based pricing; full report paywalled.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-10
  archetype: professional-services
  module: scoping-pricing
  title: Matter-level measurement of AI value (cycle time, hours, quality) to support pricing conversations with clients
  function: finance-accounting
  work_types:
  - data-reporting
  - client-interaction
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Clients ask firms to prove AI savings on their matters, and firms answer that they are still gathering data. Hours-saved measures also miss value such as faster turnaround and better risk identification.
  solution: Capture AI usage and value per matter (time entries from AI work, turnaround, quality) and report it to clients. Legora and Laurel announced a partnership whose first phase writes time entries from work done in Legora; the second phase will jointly develop ways to measure how Legora is used and the value of AI-powered legal work.
  outcomes:
  - lever: cost
    description: Clients seeing no savings yet
    figure: nearly 60%
    measures: Share of in-house counsel respondents (about 650 in-house counsel and legal-ops staff, fielded 18 June to 18 July 2025) reporting "no noticeable savings yet" from outside counsel's use of generative AI; ACC and Everlaw co-published (in-house view)
    provenance: independent
    source_ref: BLOOMBERGLAW-ACC-2025
  - lever: quality
    description: Firms with a GenAI strategy
    figure: 22% of firms; those with a strategy are 3.9 times more likely to achieve ROI
    measures: Share of law firms with a GenAI strategy, and relative likelihood of achieving ROI, as stated by a Thomson Reuters speaker at Legalweek 2026
    provenance: vendor-published
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - Time and matter data in systems that can tag AI-assisted work (LEGORA-LAUREL-2026)
  - A move from hours-saved metrics to value metrics such as turnaround, risk identification, consistency and client satisfaction (TRI-STANDOUT-2026, recommendations)
  risks_and_guardrails:
  - Panelists described ROI measurement as anecdotal or based on conventional wisdom rather than hard evidence (TRI-LEGALWEEK-2026)
  - The Legora-Laurel second phase is announced, not delivered; no results (LEGORA-LAUREL-2026)
  human_checkpoints:
  - Lawyer reviews the time entry drafted from the work before it is recorded (LEGORA-LAUREL-2026)
  role_evolution: Greenberg Traurig has a Chief Pricing and Innovation Officer and DLA Piper a head of AI innovation among the panelists (TRI-LEGALWEEK-2026)
  evidence_grade: C
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: sections "Proving AI's path to saving clients money" and "The pressure hasn't yet found a release valve"
  - ref: BLOOMBERGLAW-ACC-2025
    title: AI Does Little to Reduce Law Firm Billable Hours, Survey Shows (ACC-Everlaw survey)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows
    date: '2025-10-14'
    access: full
    locator: opening paragraphs
  - ref: TRI-STANDOUT-2026
    title: Turning law firm AI strategies into practice (2026 Stand-out Lawyers Survey)
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: Recommendations list, "Moving to more value-based measurement"
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: partnership announcement, phase descriptions
  notes: 'Graded C: the only firm-side evidence is a vendor announcement and panel remarks. ACC-Everlaw data are from in-house counsel: tag in-house. Among in-house respondents who did see a positive result, 13% pointed to fewer billable hours and 20% to better turnaround (BLOOMBERGLAW-ACC-2025). Time capture mechanics route to billing-collections.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-11
  archetype: professional-services
  module: scoping-pricing
  title: Outside counsel guidelines that require AI use on lower-risk tasks and savings reflected in billed hours (in-house)
  function: procurement-supply-chain
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: In-house teams do not know how to request fee reductions because AI tools exist, and firms do not know how to charge for them; guidelines are inconsistent, with some asking for AI use and others restricting it.
  solution: 'Corporate legal departments write AI terms into outside counsel guidelines: lower-risk work done by AI, time savings visible in billed hours, line-item AI transparency on invoices, and in some cases refusal to pay for certain AI-performed work.'
  outcomes:
  - lever: cost
    description: Respondents expecting to bring more work in-house
    figure: 64%
    measures: Share of ACC-Everlaw respondents (about 650 in-house counsel and legal ops) who expect to bring more work in-house, as reported by Bloomberg Law
    provenance: independent
    source_ref: BLOOMBERGLAW-ACC-2025
  prerequisites:
  - Legal ops infrastructure and governance; GCs described tool proliferation without governance and limited legal ops infrastructure (TRI-STANDOUT-2026)
  risks_and_guardrails:
  - 'Contradictory client directives: some demand AI savings, others require explicit permission before AI is used or ask for warranties that models are unbiased (TRI-LEGALWEEK-2026)'
  - A lawyer must follow client guidelines that restrict AI (CALBAR-GENAI-2026, Communication section)
  human_checkpoints:
  - none published
  role_evolution: ACC's outgoing CEO said clients, not firms, will most likely drive the next shift in legal pricing (BLOOMBERGLAW-ACC-2025)
  evidence_grade: C
  sources:
  - ref: BLOOMBERGLAW-ACC-2025
    title: AI Does Little to Reduce Law Firm Billable Hours, Survey Shows (ACC-Everlaw survey)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows
    date: '2025-10-14'
    access: full
    locator: paragraphs quoting Gartner's Weston Wicks and ACC's Veta Richardson
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: section "The contradictions in the room"
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: Communication Regarding Generative AI Use, p. 7
  notes: 'Graded C: the claim that more companies are adding such provisions comes from a Gartner analyst quoted by Bloomberg Law, not from a published guideline set. In-house client side; firm-side response is in use cases 02, 10 and 16.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-12
  archetype: professional-services
  module: scoping-pricing
  title: Final-instalment recourse and AI-use disclosure after AI-generated errors in a consulting deliverable (Deloitte Australia)
  function: risk-compliance-legal
  work_types:
  - review-assurance
  - document-production
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: A government-commissioned consulting report contained apparent AI-generated errors, including a fabricated quotation from a federal court judgment and references to nonexistent research papers.
  solution: Deloitte reviewed the 237-page report and a revised version was published that discloses use of a generative AI system; the department said Deloitte agreed to repay the final instalment under its contract.
  outcomes:
  - lever: risk
    description: Contract value and recourse
    figure: AUD 440,000 paid; final instalment repaid, amount to be made public
    measures: Contract amount paid by the Australian government for a 237-page report to the Department of Employment and Workplace Relations; the department said Deloitte agreed to repay the final instalment
    provenance: independent
    source_ref: CTV-DELOITTE-2025
  prerequisites:
  - A contract with staged payments so that a final instalment can be repaid (CTV-DELOITTE-2025)
  - Disclosure of AI use in the revised deliverable (CTV-DELOITTE-2025)
  risks_and_guardrails:
  - A Senator called for a full refund of the AUD 440,000 (CTV-DELOITTE-2025)
  - 'A later Canadian case: Newfoundland and Labrador''s premier demanded accountability and a review of AI use by consultants is ongoing (BNN-DELOITTE-2025)'
  human_checkpoints:
  - Deloitte reviewed the report and confirmed some footnotes and references were incorrect (CTV-DELOITTE-2025)
  role_evolution: none published
  evidence_grade: B
  sources:
  - ref: CTV-DELOITTE-2025
    title: Deloitte to partially refund Australian government for report with apparent AI-generated errors (Associated Press)
    publisher: CTV News
    type: press
    url: https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/
    date: '2025-10-07'
    access: full
    locator: body paragraphs on refund, disclosure and Senator Pocock
  - ref: BNN-DELOITTE-2025
    title: Feds defend $1.1-million Deloitte contract for AI advice after firm admitted mistakes (Canadian Press)
    publisher: BNN Bloomberg
    type: press
    url: https://www.bnnbloomberg.ca/business/company-news/2025/12/18/feds-defend-11-million-deloitte-contract-for-ai-advice-after-firm-admitted-mistakes/
    date: '2025-12-18'
    access: full
    locator: paragraphs on Newfoundland and Labrador and ESDC contract
  notes: Named incident, press-reported; final repaid amount not published at the time of the article. The AI system named in the revised report was Azure OpenAI. Quality-review module owns the error analysis; here it is evidence that payment terms and disclosure are how buyers recover.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-13
  archetype: professional-services
  module: scoping-pricing
  title: 'AI-use declaration in supplier quotes and model contract clauses under public-sector panels (idea: announced Australian policy)'
  function: procurement-supply-chain
  work_types:
  - document-production
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Government buyers cannot see whether a consultant's fee reflects AI use or whether AI-generated work is reliable.
  solution: The Australian Public Service AI plan says suppliers on whole-of-government management advisory services and people panels will have to advise of planned AI use when responding to requests for quotes, and new model clauses will state that consultants remain fully responsible for services regardless of generative AI use.
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: n/a
  prerequisites:
  - Supplier-side process to state planned AI use in each quote response (CANBERRATIMES-APSAI-2025)
  risks_and_guardrails:
  - Optional AI clauses already exist in the Digital Transformation Agency ClauseBank and state that a provider's use of AI is approved by the buyer (CANBERRATIMES-APSAI-2025)
  human_checkpoints:
  - none published
  role_evolution: none published
  evidence_grade: D
  sources:
  - ref: CANBERRATIMES-APSAI-2025
    title: New AI plan for the APS sets out expectations for contractors (Brittney Levinson)
    publisher: The Canberra Times
    type: press
    url: https://www.canberratimes.com.au/story/9110516/new-ai-plan-for-the-aps-sets-out-expectations-for-contractors/
    date: '2025-11-13'
    access: full
    locator: paragraphs on whole-of-government panels, RFQ responses and ClauseBank
  notes: 'Grade D (idea): the scale has no tier for an announced buyer policy; implementation was not confirmed. The article is partly paywalled. The plan was unveiled on Wednesday 12 Nov 2025 (Public Service Minister Katy Gallagher); the article is dated 13 Nov 2025 local time.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-14
  archetype: professional-services
  module: scoping-pricing
  title: AI disclosure, client approval and AI-cost treatment written into engagement terms
  function: risk-compliance-legal
  work_types:
  - document-production
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Fee agreements are silent on whether AI is used and how its cost is treated, while regulators distinguish general overhead from matter-specific costs.
  solution: Engagement letters say whether and how AI is used, whether client approval is required, and which AI costs are overhead and which are billed at cost with disclosure.
  outcomes:
  - lever: risk
    description: Firms requiring client approval before using generative AI
    figure: 8% (under 50 lawyers) to 38% (350-699 lawyers); 34% (over 700 lawyers)
    measures: Share of respondent firms in the ILTA 2026 survey, by firm size, reporting an official policy that requires client approval for generative AI tools (Q3.18); self-reported by firms and aggregated by ILTA
    provenance: independent
    source_ref: ILTA-TECHSURVEY-2026
  prerequisites:
  - A firm policy for generative AI (formal policy in place at 57% of firms under 50 lawyers and 80-98% of larger groups) (ILTA-TECHSURVEY-2026, Q3.18)
  risks_and_guardrails:
  - 'California: general AI subscriptions are overhead; per-matter AI costs can be charged only if the fee agreement discloses it, at actual cost, with no markup without informed written consent (CALBAR-GENAI-2026, p. 8)'
  - 'Texas: a lawyer will generally not be allowed to recover more than the amount actually paid to the AI provider (TXETHICS-OP705-2025, Fees)'
  - North Carolina allows billing AI expenses if accurate, not clearly excessive and consented to, preferably in writing (NCBAR-FEO1-2024)
  - California says disclosure of AI use may be appropriate where it materially affects decision-making (CALBAR-GENAI-2026, Communication section)
  human_checkpoints:
  - 'Lawyer decides on client disclosure case by case; ordinary tasks such as research generally need no disclosure (NCBAR-FEO1-2024, Opinion #5)'
  role_evolution: none published
  evidence_grade: C
  sources:
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p. 7-8
  - ref: TXETHICS-OP705-2025
    title: Opinion 705 (generative AI)
    publisher: Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics
    type: professional-body
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Fees section
  - ref: NCBAR-FEO1-2024
    title: 2024 Formal Ethics Opinion 1 (use of artificial intelligence in a law practice)
    publisher: North Carolina State Bar
    type: professional-body
    url: https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/
    date: '2024-11-01'
    access: full
    locator: 'Opinion #5 and Opinion #6'
  - ref: ILTA-TECHSURVEY-2026
    title: ILTA Technology Survey 2026 Executive Summary
    publisher: International Legal Technology Association
    type: professional-body
    url: https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf
    date: 2026-06
    access: full
    locator: Q3.18 table, p. 5
  notes: 'Graded C: policy survey data (aggregated, firm names withheld) plus guidance; no named deployment. Legal sector only.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-15
  archetype: professional-services
  module: scoping-pricing
  title: Pricing for variable AI cost per matter under consumption-based vendor pricing (idea)
  function: finance-accounting
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: If vendors move from seat-based to consumption-based pricing, AI becomes a variable cost per matter, which affects fixed-fee margin and what can be passed through.
  solution: Pricing teams model AI consumption per engagement type and decide which cost sits in the fee, which is a disclosed pass-through at cost, and which is capped.
  outcomes:
  - lever: cost
    description: none published
    figure: none
    measures: n/a
  prerequisites:
  - Vendor usage data per matter
  - Fee agreement terms that allow disclosed pass-through (CALBAR-GENAI-2026, p. 8)
  risks_and_guardrails:
  - Per-use fees can be charged only at actual cost, without markup absent informed written consent (CALBAR-GENAI-2026, p. 8; TXETHICS-OP705-2025)
  - Vendors were reluctant to discuss consumption pricing when asked (EDISCOVERYTODAY-ILTACON-2026)
  human_checkpoints:
  - none published
  role_evolution: none published
  evidence_grade: D
  sources:
  - ref: EDISCOVERYTODAY-ILTACON-2026
    title: My Five ILTACON 2026 Takeaways (Doug Austin)
    publisher: eDiscovery Today
    type: conference
    url: https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/
    date: '2026-09-04'
    access: full
    locator: section "Is tokengeddon looming for AI pricing?"
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p. 8
  notes: 'Grade D (idea): discussed at ILTACON 2026 as a press-colleague hallway topic, with no firm case. Wording of the source is speculative (the author says vendors are waiting to find out).'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-16
  archetype: professional-services
  module: scoping-pricing
  title: Structured AI-value conversation with the client before fee concessions
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Few partners discuss AI with their clients, and clients who are not told the value default to treating AI as a cost-cutter.
  solution: Partners lead with what changed for the client (faster, clearer, safer, more predictable), agree how AI will be used jointly with the client, and then discuss pricing, rather than opening with discounts.
  outcomes:
  - lever: growth
    description: Partner AI conversations with clients
    figure: about one-third of embedded AI partners have discussed AI with at least 60% of their clients
    measures: Share of embedded AI partners among 2,527 client-nominated stand-out lawyers (65 countries) who said they had discussed AI with at least 60% of clients; TRI also reports more than one-third of stand-out lawyers talked about AI with under 20% of clients
    provenance: vendor-published
    source_ref: TRI-STANDOUT-2026
  prerequisites:
  - Client data and competitive intelligence for partners, described as the top need regardless of AI use (TRI-STANDOUT-2026)
  - Approved talking points and guidance on billing implications (TRI-STANDOUT-2026)
  risks_and_guardrails:
  - Leading with price concessions can train clients to expect discounts (TRI-STANDOUT-2026)
  - A DLA Piper panelist advised firms to lead the conversation on how value gets shared before the client sets the terms (TRI-LEGALWEEK-2026)
  human_checkpoints:
  - Partner owns the client conversation (TRI-STANDOUT-2026)
  role_evolution: Partners are described as the commercial transmission mechanism of the firm (TRI-STANDOUT-2026)
  evidence_grade: C
  sources:
  - ref: TRI-STANDOUT-2026
    title: Turning law firm AI strategies into practice (2026 Stand-out Lawyers Survey)
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: sections "How to talk to clients about AI" and survey methodology
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: section "The contradictions in the room"
  notes: 'Graded C: survey of a vendor-affiliated institute; no firm outcomes. Overlaps client-development: route the conversation playbook there.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-17
  archetype: professional-services
  module: scoping-pricing
  title: 'Holding or raising rates on AI-enabled quality (idea: premium "Elevate" path)'
  function: sales-marketing-bd
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Firms want to keep AI savings; clients push for fee reductions. Rates are rising while profit signals stay flat, and TRI warns that using AI mainly to justify higher billing is risky.
  solution: Firms position AI as raising quality, reinvest freed time in deeper work, and hold or raise fees because clients receive better output. Thomson Reuters describes this as the Elevate path, preferred by 52% of surveyed professionals.
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: n/a
  prerequisites:
  - Clear evidence to clients that quality has improved (TRI-SOTLM-2026)
  risks_and_guardrails:
  - TRI says premium billing tied to AI adoption is sustainable only when clients clearly see value (TRI-SOTLM-2026)
  - Of 78% of corporate clients who say AI-enabled quality gains are very important or essential, 6% say most or all providers deliver them (TR-FOP-2026)
  - 32% of corporate clients have reconsidered or plan to reconsider firms in the next 12 months (TR-FOP-2026)
  human_checkpoints:
  - none published
  role_evolution: TR notes Elevate firms may serve a smaller market as price-sensitive clients leave, and newer professionals may find fewer chances to build foundational experience (TR-FOP-2026)
  evidence_grade: D
  sources:
  - ref: TR-FOP-2026
    title: Future of Professionals Report 2026
    publisher: Thomson Reuters
    type: survey
    url: https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report
    date: 2026-09
    access: full
    locator: '"AI to Elevate" description and client pressure findings'
  - ref: TRI-SOTLM-2026
    title: '2026 State of the US Legal Market: AI value vs AI bubble analysis'
    publisher: Thomson Reuters Institute with Georgetown Law Center on Ethics and the Legal Profession
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble
    date: '2026-01-14'
    access: full
    locator: sections on AI hype and assessing the payoff
  - ref: TRI-LFFI-Q1-2026
    title: 'Q1 2026 Law Firm Financial Index: strong inputs, average output'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output
    date: '2026-05-13'
    access: full
    locator: Am Law 100 worked-rate and demand figures
  - ref: BESTLAWFIRMS-CITI-2026
    title: AI Was Supposed to Kill the Billable Hour. Instead, Big Law Is Having Its Best Year in Decades (secondary report of Citi H1 2026 data)
    publisher: BestLawFirms (David L. Brown)
    type: press
    url: https://www.bestlawfirms.com/articles/ai-billable-hour-law-firm-revenue-2026/8427
    date: '2026-09-02'
    access: full
    locator: Citi H1 2026 summary
  notes: 'Grade D (idea): the path is a survey scenario; market data show rising rates but do not attribute them to AI. Market context: Am Law 100 worked rate growth near 10% and demand growth 2.7% in Q1 2026 with LFFI flat at 55 (TRI-LFFI-Q1-2026); revenue up nearly 12% and billable hours up more than 4% in H1 2026 per Citi, as reported secondhand (BESTLAWFIRMS-CITI-2026). Firm finance owns the economics.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-18
  archetype: professional-services
  module: scoping-pricing
  title: AI-drafted estimates and SOWs grounded in prior-engagement actuals (vendor agents)
  function: sales-marketing-bd
  work_types:
  - document-production
  - data-reporting
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Estimates and SOWs are slow to build and rely on templates or judgment rather than actuals, which exposes margin to cost and risk surprises.
  solution: Certinia describes agents (Estimate Creation, Estimation, SOW Drafter) inside a Salesforce-native professional services system that build estimates and SOWs from the actuals of prior engagements; the page does not describe the human review step.
  outcomes:
  - lever: speed
    description: Time to create a proposal or SOW
    figure: 8 hrs to 1 hr
    measures: Vendor headline claim for time to create a proposal or SOW; sample, baseline and definition not stated on the page
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Data on prior engagement actuals in one system; resource managers cite poor or fragmented data across skills, outcomes, demand and capacity (47%) as a barrier to AI in resource management (KANTATA-RMI-2026)
  risks_and_guardrails:
  - Vendor claims only; Deltek found 38% of A&E respondents reported measurable positive business impact from AI, and 39% said it was too early or still piloting (DELTEK-CLARITY-2026)
  - No published error rate or override rate for AI-generated estimates was found (see Gaps)
  human_checkpoints:
  - none published
  role_evolution: none published
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: Certinia AI solutions page (Veda agents)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: '2026-10-19'
    access: full
    locator: '"More gains across the lifecycle" and agent catalogue'
  - ref: KANTATA-RMI-2026
    title: New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services (Resource Management Institute study commissioned by Kantata)
    publisher: Kantata
    type: vendor
    url: https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services
    date: '2026-04-09'
    access: full
    locator: barrier percentages
  - ref: DELTEK-CLARITY-2026
    title: Deltek Clarity Industry Studies highlight AI challenges, talent strain and delivery capacity pressures (17th Government Contracting and 47th A&E studies)
    publisher: Deltek
    type: vendor
    url: https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/
    date: '2026-05-12'
    access: full
    locator: 47th A&E study findings
  notes: 'Graded C: vendor claim, no named customer found on the page. The Deltek and RMI figures are adjacent (A&E sector; resource management) and cap any grade at B. Practice-angle deep dive may add named customers.'
  last_reviewed: '2026-10-19'

```

## 3. Module notes

### Processes and key steps (work types)

1. Intake and scoping of the client need (client-interaction).
2. Effort estimate and budget, including expenses and risk (coordination-scheduling, data-reporting).
3. Pricing-model choice and margin or realisation check: hourly, fixed, value, outcome, subscription or hybrid (expert-judgment).
4. Drafting the fee proposal, engagement letter or SOW, including AI-use and AI-cost terms (document-production).
5. Fee negotiation and the AI-value conversation with the client (client-interaction).
6. Approval and fee-reasonableness or disclosure check (review-assurance).
7. In-flight budget monitoring and change control (data-reporting).
8. Post-matter review of realisation and of AI effect on effort (data-reporting).

### Common pain points

- Firms cannot show clients matter-level AI savings; the usual answer is "we are still gathering the data" (TRI-LEGALWEEK-2026).
- Under hourly billing, finishing a task faster cuts the firm's own revenue (TRI-BILLING-2026).
- Clients send conflicting instructions: some require AI savings, others require permission before any AI use (TRI-LEGALWEEK-2026).
- AI investment is a cost that cannot usually be attributed to individual projects (KPMG, BLOOMBERGTAX-PRICING-2026).
- Poor or fragmented data (47%) and limited understanding of where AI applies (49%) are top barriers in resource management, which feeds estimating (KANTATA-RMI-2026).
- Partners are not talking to clients about AI: more than one-third of stand-out lawyers discussed it with under 20% of clients (TRI-STANDOUT-2026).

### Metrics and benchmarks (what each measures)

- **Client-perceived savings.** Nearly 60% of ACC-Everlaw respondents (about 650 in-house counsel and legal-ops staff, fielded 18 June to 18 July 2025) reported "no noticeable savings yet" from outside counsel's generative AI use; 13% of those seeing a positive result pointed to fewer billable hours and 20% to better turnaround; 64% expect to bring more work in-house (BLOOMBERGLAW-ACC-2025). In-house view.
- **Client demand versus delivery.** 78% of corporate clients (Thomson Reuters Future of Professionals survey, 1,816 professionals, March to April 2026) say AI-enabled quality gains are very important or essential; 6% say most or all providers deliver them; 32% have reconsidered or plan to reconsider providers within 12 months (TR-FOP-2026).
- **Strategy and value.** 66% of professionals where a named AI strategy exists say AI meets or exceeds expectations, against 22% where there is none (TR-FOP-2026). A Thomson Reuters speaker said firms with a GenAI strategy are 3.9 times more likely to achieve ROI and that 22% of firms have one (TRI-LEGALWEEK-2026).
- **Shadow AI.** 34% of professionals use AI tools their organisation has not sanctioned (TR-FOP-2026).
- **Project-level AI use.** 43.6% of projects now use AI, up from 23.1% in 2025 (SPI Research, 245 professional services organisations, July to September 2026; SPI-AI-2026). 84.8% say AI saves them time; the figure for revenue generated is locked on the page (SPI-AI-2026).
- **Measurable impact.** 38% of A&E respondents (896 firms) reported measurable positive business impact from AI; AI adoption 70%, up from 53%; utilisation just under 60%; operating profit 16.7% (DELTEK-CLARITY-2026). Adjacent sector.
- **Outcome data for staffing.** 7.3% of respondents say outcome data is easily accessible and routinely used in staffing decisions; 52.7% are not equipped to manage hybrid human and agent teams (KANTATA-RMI-2026). Vendor-commissioned.
- **Rates.** Am Law 100 worked-rate growth near 10% and demand growth 2.7% in Q1 2026 with the Law Firm Financial Index flat at 55 (TRI-LFFI-Q1-2026); average rate growth above 7% in 2025 (TRI-LEGALWEEK-2026); Citi data reported secondhand: H1 2026 revenue up nearly 12%, billable hours up more than 4%, expenses up 9.7% (BESTLAWFIRMS-CITI-2026). None of these is attributed to AI by its source.
- **Accounting hourly rates.** AICPA 2025 survey of more than 1,000 firms: median net hourly billing rate up nearly 7% over two years to $170 (as reported by BLOOMBERGTAX-PRICING-2026).
- **Outcome-fee share.** About a quarter of McKinsey's global fees on the outcomes-based model (BI-MCKINSEY-2025).
- **Quality evidence (adjacent tasks only).** Legal research tools from LexisNexis and Thomson Reuters hallucinated between 17% and 33% of the time in a preregistered 2024 test (STANFORD-MAGESH-2024). Patent-drafting trial of 133 lawyers: AI raised work quality about 0.34 to 0.38 standard deviations, and the post-test advantage without AI was concentrated among senior lawyers (NBER-AUTOR-2026). Vals benchmarked four legal AI tools against a lawyer baseline on seven tasks (VALS-VLAIR-2025). None measures estimate accuracy, fee-proposal error, override rate or parallel-run outcomes; no such public measure was found.
- **UK small firms (older, vendor-commissioned).** 54% of 500 surveyed solicitors expected to use fixed fees more; 29% said AI helped save costs (Clio/Censuswide, LEGALFUTURES-CLIO-2024).

### Guardrails and regulatory points

- California (revised guidance approved 14 May 2026): hourly billing must reflect time actually spent; flat fees may build in AI savings; general AI subscriptions are overhead; per-matter AI costs need fee-agreement disclosure, must reflect actual cost and carry no markup without informed written consent; a lawyer must follow client guidelines restricting AI; supervision and verification scale with system autonomy (CALBAR-GENAI-2026, pp. 2-3, 7-8; CALBAR-ETHICSHUB-2026).
- Texas Opinion 705 (Feb 2025): an hourly lawyer may charge for actual time using the tool but not for time "saved"; per-use AI fees may be recovered only at amounts actually paid (TXETHICS-OP705-2025, Fees).
- DC Opinion 388 (Apr 2024): where the fee agreement is based only on time spent, the lawyer can bill only time spent; AI expense must be communicated if billed (DCBAR-OP388-2024, section E).
- North Carolina 2024 FEO 1 (1 Nov 2024): billing three hours when one was worked is not allowed; a flat fee may be used if not clearly excessive and the client consents; AI expenses billable if accurate, not clearly excessive and consented to (NCBAR-FEO1-2024, Opinion #6).
- Virginia LEO 1901 (Supreme Court approval 24 Nov 2025): value-based fees can reflect efficiency gains and skill and remain reasonable; the fee basis must be explained under Rule 1.5(b) (VSB-LEO1901-2025).
- ABA Formal Opinion 512 (2024): hourly billing on actual time; may be unreasonable to charge the same flat fee when a tool makes work much quicker; the basis for charging for AI tools must be explained before charging (TRI-ABA512-2025, quoting the opinion; not read at source).
- AICPA Code 1.510.001 contingent-fee rule and 1.230.030 attest-fee setting (AICPA-CODE-2026). Detail belongs to the assurance and tax archetypes.
- Public-sector buyers: Australia's APS AI plan (Nov 2025) will require panel suppliers to advise planned AI use in quote responses and adds clauses on supplier responsibility (CANBERRATIMES-APSAI-2025).
- Firm policy baseline: 57% of firms under 50 lawyers have a formal generative AI policy against 80% to 98% of larger groups; 8% to 38% require client approval before use (ILTA-TECHSURVEY-2026, Q3.18).

### Frontier signals (dated)

- 2025-10-07: Deloitte Australia to repay part of an AUD 440,000 contract after AI-generated errors; revised report discloses AI use (CTV-DELOITTE-2025).
- 2025-11-13: Australian Public Service AI plan sets AI-use declarations for consulting panel suppliers (CANBERRATIMES-APSAI-2025).
- 2025-11-17: McKinsey says about a quarter of global fees are outcome-based and it is doing more performance-based arrangements (BI-MCKINSEY-2025).
- 2025-11-24: Virginia Supreme Court approves LEO 1901 on reasonable fees with generative AI (VSB-LEO1901-2025).
- 2026-02-24: Forrester says AI and outcome-based pricing lead the services story (FORRESTER-TECHSVCS-2026, abstract only).
- 2026-03-05: Bloomberg Tax reports top US accounting firms developing future pricing models; PwC's US tax leader says time is becoming less relevant (BLOOMBERGTAX-PRICING-2026).
- 2026-03-13: Legalweek 2026 panels on the firm and client AI value divide (TRI-LEGALWEEK-2026).
- 2026-03-24 and 25: PwC One launched in beta; PwC US CEO says some services may move to subscription (NEWSTACK-PWC-2026; CPAPA-PWC-2026).
- 2026-05-14: California approves guidance revision covering agentic AI and fees (CALBAR-ETHICSHUB-2026).
- 2026-08-23: Stanford and USC pricing framework for consulting (STANFORD-DEL-2026).
- 2026-09-04: Seat-to-consumption AI pricing discussed at ILTACON ("tokengeddon") (EDISCOVERYTODAY-ILTACON-2026).
- 2026-10: SPI reports 43.6% of projects use AI and highlights the gap between time saved and revenue (SPI-AI-2026).
- 2026-10-13: Legora and Laurel announce a second phase to measure the value of AI-powered legal work (LEGORA-LAUREL-2026).

### Workforce and role effects

- Greenberg Traurig has a Chief Pricing and Innovation Officer; DLA Piper has a senior managing director of AI innovation; both spoke on client AI value at Legalweek (TRI-LEGALWEEK-2026).
- Partners are the commercial transmission mechanism for billing and staffing strategy, and gaps between partners hamper policy (TRI-STANDOUT-2026).
- Resource management is seen as mainly operational by 72% of respondents; practitioners say they want to shift from filling hours to outcome delivery if outcome pricing grows (KANTATA-RMI-2026).
- 24% of professionals who see an AI value gap are considering leaving within two years; 48% fear a negative effect on independent judgment development (TR-FOP-2026).
- Incentive conflict: staff encouraged to use AI but judged on hours (BLOOMBERGTAX-PRICING-2026).
- Junior outcomes in the patent trial bifurcated: fewer mediocre scores, more poor and more good (NBER-AUTOR-2026). Adjacent task.

### Objections and concerns practitioners raise

- ABA 512 reasonableness test for flat fees is criticised as treating time taken as the benchmark of value and inviting buyers' remorse (William Josten, TRI-ABA512-2025).
- Kopka Law argues that alternative fees designed only to save clients money fail because they push firms to cut corners (TRI-BILLING-2026).
- An itemised hourly bill undersells value when AI compresses hours into minutes; one panelist proposed a return to a single line-item services bill and doubted client acceptance (TRI-LEGALWEEK-2026).
- Using AI mainly to justify higher billing leaves firms exposed if client budgets tighten; a $2,000-per-hour associate rate could cause sticker shock (TRI-SOTLM-2026).
- Attribution risk limits outcome fees however well outcomes are measured (STANFORD-DEL-2026, Section 5.2).
- RSM's question: when AI halves a 20-hour report, is it margin or a price cut for the client (BLOOMBERGTAX-PRICING-2026).
- Leading with price concessions may train clients to expect discounts (TRI-STANDOUT-2026).

### Interview probes for an advisor

1. When AI shortens a task you quote, who decides how much of the saving goes to the client, on what evidence, and where is that written down in the fee agreement or engagement letter?
2. Which state or country rules apply to your fee arrangements (for example hourly versus flat fee reasonableness, or contingent-fee limits on audit and tax work), and who checks proposals against them before they are issued?
3. Can you show a client, for one recent matter, what AI changed in hours, turnaround or quality? What data would you need that you do not have?
4. Which of your clients have outside counsel or supplier guidelines on AI (use, permission, pass-through, disclosure), and how do you handle clients who give opposite instructions?
5. Where outcome-linked fees have been proposed, how did you decide whether the result could be attributed to your work, and who owns the baseline?

## 4. Routed to other modules

- **billing-collections:** Legora-Laurel automatic time entries (first phase of LEGORA-LAUREL-2026); AI line items on invoices and single line-item services bills (TRI-LEGALWEEK-2026); time-versus-fee billing rules in the Cal Bar, Texas and DC texts after the fee is agreed.
- **firm-finance:** Rate growth and flat LFFI (TRI-LFFI-Q1-2026; TRI-LFFI-Q2-2026); AI bubble and rate-justification warning (TRI-SOTLM-2026); Citi H1 2026 revenue, hours and expense data (BESTLAWFIRMS-CITI-2026); SPI's time-saved versus revenue gap (SPI-AI-2026); consumption-based AI cost as a margin item (EDISCOVERYTODAY-ILTACON-2026).
- **quality-review:** Deloitte Australia and the Newfoundland and Labrador review (CTV-DELOITTE-2025; BNN-DELOITTE-2025); hallucination rates and Vals benchmark (STANFORD-MAGESH-2024; VALS-VLAIR-2025); supervision and verification duties (CALBAR-GENAI-2026).
- **talent-learning:** NBER patent-drafting trial on expertise and juniors (NBER-AUTOR-2026); TR-FOP findings on early-career development; Wipfli metrics (BLOOMBERGTAX-PRICING-2026).
- **client-development:** Partner-client AI conversation data (TRI-STANDOUT-2026).
- **staffing-resourcing:** Hybrid team readiness and outcome data in staffing (KANTATA-RMI-2026).
- **acceptance-risk:** Confidentiality, agentic access and client-approval policies (CALBAR-GENAI-2026, Confidentiality section; ILTA-TECHSURVEY-2026).
- **pursuit-proposals:** AI-use declaration in quote responses to public-sector panels (CANBERRATIMES-APSAI-2025); Certinia RFP Responder and Estimate Creation agents (CERTINIA-VEDA-2026).
- **Assurance and tax archetypes:** Contingent-fee and attest-fee rules for audit, review and tax-return preparation (AICPA-CODE-2026, 1.510.001 and 1.230.030) are recorded here only as pricing constraints; substantive treatment belongs there.

## 5. Sources

Access is `full` for every source below (opened and read); notes mark paywalled or partly shown pages. Dates are publication dates from page metadata or the byline unless noted.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| AICPA-CODE-2026 | AICPA Code of Professional Conduct (updated for official releases through July 2026) | AICPA | standard-setter | https://mn.gov/boa/assets/AICPA%20Code%20of%20Professional%20Conduct_tcm1233-764395.pdf | 2026-07 |
| BESTLAWFIRMS-CITI-2026 | AI Was Supposed to Kill the Billable Hour. Instead, Big Law Is Having Its Best Year in Decades (secondary report of Citi H1 2026 data) | BestLawFirms (David L. Brown) | press | https://www.bestlawfirms.com/articles/ai-billable-hour-law-firm-revenue-2026/8427 | 2026-09-02 |
| BI-MCKINSEY-2025 | AI is reshaping how McKinsey makes money (Polly Thompson) | Business Insider | press | https://www.businessinsider.com/ai-reshapes-how-mckinsey-makes-money-consultancy-025-11 | 2025-11-17 |
| BLOOMBERGLAW-ACC-2025 | AI Does Little to Reduce Law Firm Billable Hours, Survey Shows (ACC-Everlaw survey) | Bloomberg Law | press | https://news.bgov.com/business-and-practice/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows | 2025-10-14 |
| BLOOMBERGTAX-PRICING-2026 | AI Efficiency Gains Push Accounting Firms to Reimagine Pricing (Nicola Trentmann) | Bloomberg Tax | press | https://news.bloombergtax.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing | 2026-03-05 |
| BNN-DELOITTE-2025 | Feds defend $1.1-million Deloitte contract for AI advice after firm admitted mistakes (Canadian Press) | BNN Bloomberg | press | https://www.bnnbloomberg.ca/business/company-news/2025/12/18/feds-defend-11-million-deloitte-contract-for-ai-advice-after-firm-admitted-mistakes/ | 2025-12-18 |
| CALBAR-ETHICSHUB-2026 | Ethics and technology resources (notes Board of Trustees approval of revised guidance on 14 May 2026) | State Bar of California | regulator | https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Ethics/Ethics-Technology-Resources | 2026-05-14 |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision) | State Bar of California, Standing Committee on Professional Responsibility and Conduct | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05-14 |
| CANBERRATIMES-APSAI-2025 | New AI plan for the APS sets out expectations for contractors (Brittney Levinson) | The Canberra Times | press | https://www.canberratimes.com.au/story/9110516/new-ai-plan-for-the-aps-sets-out-expectations-for-contractors/ | 2025-11-13 |
| CERTINIA-VEDA-2026 | Certinia AI solutions page (Veda agents) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 |
| CPAPA-PWC-2026 | PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' (reports an FT interview with Paul Griggs) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/ | 2026-03-25 |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors (Associated Press) | CTV News | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 |
| DCBAR-OP388-2024 | Ethics Opinion 388 (generative AI in client matters) | District of Columbia Bar | professional-body | https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388 | 2024-04 |
| DELTEK-CLARITY-2026 | Deltek Clarity Industry Studies highlight AI challenges, talent strain and delivery capacity pressures (17th Government Contracting and 47th A&E studies) | Deltek | vendor | https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/ | 2026-05-12 |
| EDISCOVERYTODAY-ILTACON-2026 | My Five ILTACON 2026 Takeaways (Doug Austin) | eDiscovery Today | conference | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 |
| FORRESTER-TECHSVCS-2026 | The State Of Technology Services, 2026 (abstract page; report paywalled) | Forrester | survey | https://www.forrester.com/report/the-state-of-technology-services-2026/RES192217 | 2026-02-24 |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 Executive Summary | International Legal Technology Association | professional-body | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services (Resource Management Institute study commissioned by Kantata) | Kantata | vendor | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 |
| LEGALFUTURES-CLIO-2024 | Small law firms embracing AI as they move away from hourly billing (Clio/Censuswide UK survey of 500 solicitors) | Legal Futures | press | https://www.legalfutures.co.uk/latest-news/small-law-firms-embracing-ai-as-they-move-away-from-hourly-billing | 2024-11-07 |
| LEGORA-LAUREL-2026 | Legora and Laurel partner to capture the time lawyers spend in Legora as they work | Legora | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 |
| NBER-AUTOR-2026 | Does AI Assistance Enhance or Erode Expertise? Evidence from a Three-Month Field Experiment in Patent Drafting (NBER WP 35720) | NBER | academic | https://www.nber.org/papers/w35720 | 2026-09 |
| NCBAR-FEO1-2024 | 2024 Formal Ethics Opinion 1 (use of artificial intelligence in a law practice) | North Carolina State Bar | professional-body | https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/ | 2024-11-01 |
| NEWSTACK-PWC-2026 | PwC's AI agents are now your consultants, whether you're ready or not (Darryl K. Taft) | The New Stack | press | https://thenewstack.io/pwcs-ai-agents-are-now-your-consultants-whether-youre-ready-or-not/ | 2026-03-24 |
| SPI-AI-2026 | 2026 Impact of AI on Professional Services (report landing page) | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-10 |
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives | Stanford Digital Economy Lab (Brynjolfsson) and USC Marshall (Petropoulos) | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 |
| STANFORD-MAGESH-2024 | Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools (arXiv 2405.20362) | Stanford RegLab / HAI (Magesh et al.) | academic | https://arxiv.org/abs/2405.20362 | 2024-05-30 |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026-09 |
| TRI-ABA512-2025 | Is ABA Formal Opinion 512 off the mark? And if so, what can law firms and GCs do about it? (William Josten, Honigman; quotes the opinion) | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/aba-formal-opinion-512 | 2025-04-02 |
| TRI-BILLING-2026 | How one law firm is challenging a broken status quo around billing (Kopka Law) | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing | 2026-04-30 |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 |
| TRI-LFFI-Q1-2026 | Q1 2026 Law Firm Financial Index: strong inputs, average output | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output | 2026-05-13 |
| TRI-LFFI-Q2-2026 | Q2 2026 LFFI: A heavier load, yet a faster crossing | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed | 2026-08-10 |
| TRI-SOTLM-2026 | 2026 State of the US Legal Market: AI value vs AI bubble analysis | Thomson Reuters Institute with Georgetown Law Center on Ethics and the Legal Profession | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice (2026 Stand-out Lawyers Survey) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 |
| TXETHICS-OP705-2025 | Opinion 705 (generative AI) | Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics | professional-body | https://www.legalethicstexas.com/resources/opinions/opinion-705/ | 2025-02 |
| VALS-VLAIR-2025 | Vals Legal AI Report | Vals AI | academic | https://www.vals.ai/vlair | 2025-02-27 |
| VSB-LEO1901-2025 | Legal Ethics Opinion 1901, Reasonable Fees and the Use of Generative Artificial Intelligence (adopted page and petition to the Supreme Court of Virginia) | Virginia State Bar | regulator | https://vsb.org/Site/news/rules-news/20250327-prop-1901-fees-ai.aspx | 2025-11-25 |

Date notes: TR-FOP-2026 page metadata shows 30 Sep 2026 (survey fielded March to April 2026); SPI-AI-2026 page says published October 2026 (page modified 2026-10-12); NBER-AUTOR-2026 issue date September 2026, revised October 2026; CANBERRATIMES-APSAI-2025 article first published 13 Nov 2025 local time (plan unveiled 12 Nov 2025); TXETHICS-OP705-2025 and DCBAR-OP388-2024 give month only; AICPA-CODE-2026 is the edition updated through July 2026; CERTINIA-VEDA-2026 is a live page read 2026-10-19. FORRESTER-TECHSVCS-2026, BLOOMBERGTAX-PRICING-2026, BI-MCKINSEY-2025, CPAPA-PWC-2026 and SPI-AI-2026 are partly paywalled: only the visible text was used.

Quoted or relayed but not opened at source: ABA Formal Opinion 512 (via TRI-ABA512-2025, TXETHICS-OP705-2025 and the Virginia petition), Florida Bar Opinion 24-1 (via TXETHICS-OP705-2025), the Financial Times Griggs interview (via CPAPA-PWC-2026), Citi H1 2026 data (via BESTLAWFIRMS-CITI-2026), Salesforce and Palantir pricing (via STANFORD-DEL-2026), the AICPA 2025 pricing survey (via BLOOMBERGTAX-PRICING-2026), the Gartner remarks (via BLOOMBERGLAW-ACC-2025).

## 6. Gaps

- **Blocked or not reachable:** ABA Formal Opinion 512 text (americanbar.org challenge page), SRA and Law Society pages (403 or challenge), Wayback copies, SSRN and two law-review PDFs (challenge pages), HBS jagged-frontier page (error), Kantata "Fact or fiction: outcome-based pricing" post (404 at its listed URL).
- **Not found:** any published error rate, override rate, parallel run or inspection finding for AI-generated estimates, fee proposals or price recommendations; any peer-reviewed or working-paper empirical study of AI's effect on professional-services pricing (only the Stanford and USC conceptual paper); SRA or UK Law Society guidance on passing AI efficiency to clients; MCA guidance on pricing (the MCA 2026 member survey page has no pricing content); IESBA or ICAEW guidance on AI and fees; insurer or professional-indemnity terms for outcome-based or AI-delivered services; Gartner and Forrester full reports; SPI 2026 chapter on AI revenue and pricing (paywalled; one figure shown); published client outside-counsel-guideline text with AI terms; TRI Law Firm Rates Report 2026; primary Citi data.
- **Search budget:** the shared web-search allowance ran out after eight searches; follow-up searches on insurers, Gartner outcome-pricing forecasts and further state-bar opinions (Florida, New York, Pennsylvania) were not run.
- **Sector skew:** most governance material is US legal ethics. Consulting has no equivalent professional fee rule in the sources found; accounting evidence is one AICPA code edition and one press article; architecture and engineering is one vendor benchmark.
- **Provenance cautions:** the Stanford and USC paper discloses informal Accenture executive discussions and a general Accenture gift to the lab (STANFORD-DEL-2026, footnote and Section 2); the Kopka Law and Legora-Laurel items are self-described by the parties; ACC-Everlaw is co-published with a vendor; the McKinsey fee share is a stated approximation.
