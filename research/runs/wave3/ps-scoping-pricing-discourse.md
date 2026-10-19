# professional-services / scoping-pricing / discourse

Prepared 2026-10-19. Archetype: professional-services. Module: scoping-pricing (estimating, scoping and pricing engagements; pricing models; fee proposals; budgets; pricing response to AI efficiency). Angle: discourse (what practitioners say). Method: `curl`, `pdftotext` and the r.jina.ai text mirror in a private working folder; 14 web searches. Every source cited below was opened and read unless the Sources table says otherwise. In-house or shared-service examples are tagged `in-house`.

## 1. Summary

The public discourse on AI and pricing is loud and consistent in direction, but thin on measurement. Practitioners across law, accounting and consulting agree the billable hour is under pressure because AI breaks the link between effort and value. They disagree on speed, and almost nobody publishes what changed in fees or margins. There is no grade A evidence in this module: no named organization has published a tracked pricing outcome attributable to AI.

- **Pressure comes from the client side, and is not yet delivering savings.** A June-July 2025 ACC/Everlaw survey (about 650 in-house and legal-operations respondents) found nearly 60% had seen no noticeable savings yet from outside counsel's GenAI use (ACCEVERLAW-BL-2025). At Legalweek 2026, firm and in-house speakers said clients now ask matter-level questions about AI savings, some ask for AI line items, and some state they will not pay for AI-done work, while firms say they are 'still gathering the data' (TRI-LEGALWEEK-2026).
- **Firms mostly still price the old way.** A BigHand survey of 800+ legal-finance professionals (UK and North America, reported 2026-09-17) found 35% say lawyers default to standard hourly rates and 28% copy a past matter's price without adjusting; 1% use templates inside a pricing tool (BIGHAND-LF-2026). On AI savings, 30% keep prices and take the margin, 30% are still evaluating, 25% offer discounts when clients permit AI use.
- **Consulting is the furthest along on non-hourly models, and the causal story is contested.** McKinsey said about a quarter of its global fees now come from outcome-based pricing, yet its own AI leader told the same reporter the model predates AI and quoted 20% (BI-MCKINSEY-2025). PwC says it will offer alternatives to hours-based billing, with PwC One's pricing 'may involve' subscription or consumption elements (ACCTODAY-PWC-2026; PWC-ONE-2026). The Stanford Digital Economy Lab framework (August 2026) argues the destination for most engagements is hybrid, not pure outcome pricing, because attribution risk cannot be removed by telemetry (STANFORD-DEL-2026).
- **Accounting is debating the same shift, with more data on pricing models than on AI.** RSM, KPMG and PwC partners describe value and outcome pricing as under development; one mid-size firm (RKL) reports onboarding several dozen clients on a value-based model (BLAW-ACCT-2026). Thomson Reuters Institute data shows hourly billing used by 78% of tax firms (TRI-CHARGING-2026).
- **Regulators have set guardrails on billing, not on pricing models.** California's 2026 guidance says hourly bills must reflect time actually spent, flat fees may build in AI savings, and matter-specific AI costs need disclosure and no markup without informed written consent (CALBAR-GENAI-2026, p.8).

Two most important insights: (1) the unresolved question is who keeps the productivity dividend, and the evidence for either answer is anecdotal; (2) the gating capability is not a pricing model but matter-level cost and outcome data, which most firms lack (BIGHAND-LF-2026; MONDAQ-GGI-2026; STANFORD-DEL-2026, Rule 3).

## 2. Use cases

```yaml
- id: professional-services-scoping-pricing-01
  title: AI-assisted fee proposals and matter budgets built from comparable historic matters
  archetype: professional-services
  module: scoping-pricing
  function: sales-marketing-bd
  work_types: [data-reporting, document-production]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Fee proposals are priced by habit: standard hourly rates or a copy of a past matter. Firms have no good answer when clients ask how AI will change the estimate."
  solution: "A pricing agent finds comparable past matters in the firm's own matter, time and financial records, adjusts for current staffing, scope and fee assumptions, and lets the pricing team test scenarios before a proposal goes to the client. Two vendors describe this (Ayora, now part of BigHand; Narrative); one also says it factors in how AI tooling changes the cost of the work."
  outcomes:
    - lever: quality
      description: "Baseline the tools address: how lawyers price matters today"
      figure: "35% default to standard hourly rates; 28% copy a past matter's pricing unchanged; 1% use pre-made templates in a pricing tool"
      measures: "share of survey respondents (800+ senior legal finance professionals, UK and North America) reporting what lawyers 'most commonly do' when pricing a matter"
      provenance: vendor-published
      source_ref: BIGHAND-LF-2026
    - lever: growth
      description: "Vendor claim of better realization and win rate for firms using its product"
      figure: "realization up 2-4%; about 10% more new work won"
      measures: "Narrative's statement about 'firms using Narrative'; baseline, sample size, customers and period are not stated"
      provenance: vendor-published
      source_ref: NARRATIVE-ILTA-2026
  prerequisites:
    - "Clean matter, time and financial history (Ayora describes enriching and classifying time-entry narratives and matter coding first)"
    - "A pricing team or function that owns the tool and reviews outputs"
    - "Willingness to treat past matters as a starting point, not the answer, when delivery is changing"
  risks_and_guardrails:
    - "Carrying forward old staffing or pricing assumptions can give the wrong result if AI changes delivery (Guajardo, quoted in BIGHAND-LF-2026)"
    - "Time-entry narratives contain client information; Ayora says it anonymizes them with a self-hosted small model before any third-party model sees them and does not train third-party models on customer data (AYORA-LTH-2026)"
    - "Real-time pricing capability reported by firms fell in every scenario measured versus 2025 (for example 30% to 17% under competitive pressure), so tools may not reach the lawyer when a price is set (BIGHAND-LF-2026)"
  human_checkpoints:
    - "Pricing team tests scenarios before a proposal is shared with the client (AYORA-LTH-2026)"
    - "Partner approves the fee arrangement"
  role_evolution: "Pricing professionals move toward a more commercial, client-facing role: testing value with clients, pricing legal-technology offerings iteratively, and educating partners; some firms hired extra pricing staff for this (TRI-PRICINGPROS-2024, written Nov 2024)."
  evidence_grade: C
  sources:
    - { ref: AYORA-LTH-2026, title: "Ayora by BigHand", publisher: Legaltech Hub, type: vendor, url: "https://www.legaltechnologyhub.com/vendors/ayora-by-bighand/", date: 2026-10-19, access: full, locator: "product description; acquisition note (4 Aug 2026)" }
    - { ref: NARRATIVE-ILTA-2026, title: "Narrative", publisher: ILTA (Startup 2026 profile), type: vendor, url: "https://www.iltanet.org/resources/publications/pulse/startup26/narrative", date: 2026-10-19, access: full, locator: "paragraphs 2, 4 and 6" }
    - { ref: BIGHAND-LF-2026, title: "AI is changing legal delivery, but 63% of firms default to standard rates or past matter pricing, BigHand research finds", publisher: Legal Futures, type: survey, url: "https://www.legalfutures.co.uk/associate-news/ai-is-changing-legal-delivery-but-63-of-firms-default-to-standard-rates-or-past-matter-pricing-bighand-research-finds", date: 2026-09-17, access: full, locator: "paragraphs 2-3 and 'Key findings'" }
    - { ref: TRI-PRICINGPROS-2024, title: "Pricing legal technology and the impact on the role of the pricing professional", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/legal-technology-pricing-professionals-changing-roles", date: 2024-11-19, access: full, locator: "sections 'Changing roles' and 'Changing skills'" }
  last_reviewed: 2026-10-19
  notes: "Dates for AYORA-LTH-2026 and NARRATIVE-ILTA-2026 are the access date; both pages are undated. No customer is named for either product and no accuracy, override or estimate-error data was found. Aderant Virtual Pricing Director was named in search results but its page was blocked (403), so it is not cited. BigHand sells matter pricing software, so the survey is vendor-published."

- id: professional-services-scoping-pricing-02
  title: PSA agents that draft estimates and statements of work from prior engagement actuals
  archetype: professional-services
  module: scoping-pricing
  function: sales-marketing-bd
  work_types: [document-production, data-reporting]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Estimates and SOWs for project-based services work are built by hand from templates or gut feel, which loses margin to cost and risk exposure that was not caught up front."
  solution: "Certinia's Veda agents inside a Salesforce-native PSA include an Estimate Creation agent (builds complex estimates and manages creation workflows), an Estimation agent (tracks estimates with tied expenses and risks) and an SOW Drafter agent (generates statements of work from project context). The vendor says estimates are grounded in the actuals of prior engagements."
  outcomes:
    - lever: speed
      description: "Vendor claim of time to create a proposal or SOW"
      figure: "8 hours to 1 hour"
      measures: "Certinia's stated time to create a proposal or SOW; no customer, sample size or period is named on the page"
      provenance: vendor-published
      source_ref: CERTINIA-VEDA-2026
  prerequisites:
    - "Engagement history (sales, delivery and account) held in the same PSA"
    - "Estimation and risk practices a person can review the output against"
  risks_and_guardrails:
    - "Vendor-reported time saving only; no estimate-accuracy or margin-outcome data published"
    - "Fixed-price risk sits with the firm if the agent's estimate is wrong; the page describes no review controls"
  human_checkpoints:
    - "Not described on the vendor page; assumed review by the engagement lead before issue"
  role_evolution: "Vendor positions experts as spending time on judgment calls rather than paperwork (CERTINIA-VEDA-2026); no firm has described role change."
  evidence_grade: C
  sources:
    - { ref: CERTINIA-VEDA-2026, title: "Certinia AI solutions (Veda agents)", publisher: Certinia, type: vendor, url: "https://certinia.com/solutions/ai", date: 2026-10-19, access: full, locator: "agent catalogue (Sell and Plan groups); 'More gains across the lifecycle' panel" }
    - { ref: KANTATA-RMI-2026, title: "New Study Finds Resource Management at a Strategic Crossroads", publisher: Kantata (Resource Management Institute study), type: vendor, url: "https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services", date: 2026-04-09, access: full, locator: "paragraphs 6-8 (outcome-pricing uncertainty)" }
  last_reviewed: 2026-10-19
  notes: "Date for CERTINIA-VEDA-2026 is the access date; the page is undated. Kantata study is cited only for context: 1 in 2 respondents were unsure their organization will meaningfully adopt outcome-based pricing, so firms may not yet price in ways that need these estimates."

- id: professional-services-scoping-pricing-03
  title: Client AI-savings terms, line-item AI transparency and matter-level proof of savings (in-house demand side)
  archetype: professional-services
  module: scoping-pricing
  function: procurement-supply-chain
  work_types: [client-interaction, data-reporting]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Clients (in-house) cannot tell what AI savings they are getting, and firms cannot show them. Clients respond with questions, guideline provisions and, in some cases, refusals to pay for AI-done work."
  solution: "In-house teams ask outside firms what AI they use and how it generates savings on specific matters, ask for AI line items on invoices, and add outside-counsel-guideline provisions asking that lower-risk tasks be done with AI and the time saved be reflected in billed hours. Firms respond by building matter-level evidence of savings. No tool is specified in the sources."
  outcomes:
    - lever: cost
      description: "Survey of in-house counsel on savings seen so far from outside counsel's GenAI use"
      figure: "nearly 60% 'no noticeable savings yet'; of those who saw gains, 13% cited fewer billable hours and 20% cited faster turnaround"
      measures: "share of ACC/Everlaw survey respondents (about 650 in-house counsel and legal-operations staff, fielded 18 June to 18 July 2025) reporting no noticeable savings from outside counsel's GenAI use; 13% and 20% are shares of the respondents who saw a positive result, as reported by Bloomberg Law"
      provenance: vendor-published
      source_ref: ACCEVERLAW-BL-2025
  prerequisites:
    - "Matter-level cost and AI-use data on the firm side (most firms are 'still gathering the data' per TRI-LEGALWEEK-2026)"
    - "Willingness on both sides to agree how savings are measured"
  risks_and_guardrails:
    - "Clients are not consistent: some demand AI use and savings targets, others still send 2023-style bans on AI without permission (Blair, DLA Piper, in TRI-LEGALWEEK-2026)"
    - "A client that refuses to pay for paralegal time because it assumes AI replaces them can push work up to costlier timekeepers (TRI-LEADFOLLOW-2025, midsize-firm roundtable story, May 2024)"
    - "Hourly bills must reflect time actually spent (CALBAR-GENAI-2026, p.8; ABA Opinion 512 as quoted in TRI-ABA512-2025)"
  human_checkpoints:
    - "Client general counsel or legal operations agrees guideline provisions"
    - "Billing partner reviews AI-related line items"
  role_evolution: "Firm-side chief pricing and innovation officers are asked client-facing AI value questions (TRI-LEGALWEEK-2026)."
  evidence_grade: C
  sources:
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "sections 'Proving AI's path to saving clients money' and 'The contradictions in the room'" }
    - { ref: ACCEVERLAW-BL-2025, title: "AI Does Little to Reduce Law Firm Billable Hours, Survey Shows", publisher: Bloomberg Law (reporting an ACC/Everlaw survey), type: survey, url: "https://news.bgov.com/business-and-practice/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows", date: 2025-10-14, access: full, locator: "paragraphs 1-3, 8-9" }
    - { ref: TRI-LEADFOLLOW-2025, title: "Pricing AI-driven legal services: Lead or follow, there is no 'out of the way'", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/pricing-ai-driven-legal-services-lead-or-follow", date: 2025-01-30, access: full, locator: "section 'Managing expectations'" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026, access: full, locator: "p.8, 'Charging for Work Produced by Generative AI and Generative AI Costs'" }
  last_reviewed: 2026-10-19
  notes: "In-house demand-side example. The statement that more companies are adding outside-counsel-guideline provisions comes from Gartner's Weston Wicks as reported by Bloomberg Law, not from a named client's guideline. The ACC/Everlaw survey is co-published by a vendor (Everlaw) and a professional body (ACC); I used the Bloomberg Law report, not the survey itself. TRI-LEGALWEEK-2026 quotes Steven Petrie (Thomson Reuters) that firms with a GenAI strategy are 3.9 times more likely to achieve ROI and that only 22% have one; the TR-FOP-2026 report uses 22% differently (share of professionals saying AI meets expectations where there is no active strategy), so treat the 22% with care."

- id: professional-services-scoping-pricing-04
  title: Flat-fee and alternative-fee offers for repeatable work, with AI-driven effort savings priced in
  archetype: professional-services
  module: scoping-pricing
  function: sales-marketing-bd
  work_types: [expert-judgment, document-production]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Under hourly billing, an AI-driven efficiency gain reduces the firm's own revenue, and clients doubt that the hourly bill reflects value delivered."
  solution: "Firms move predictable, repeatable matters to flat or other alternative fees and build expected AI time savings into the price. Practitioners point to commoditized or high-volume work as the likely first ground. Mature versions use phase-based scoping, milestone holdbacks and bonuses, and re-scoping. The sources do not name a firm that has done this with measured AI effects."
  outcomes:
    - lever: growth
      description: "Survey of how firms are pricing AI efficiencies"
      figure: "30% keep existing pricing and take the profit; 30% still evaluating; 25% offer discounts when clients permit AI use; 49% saw increased demand for AFAs"
      measures: "shares of BigHand survey respondents (800+ senior legal finance professionals, UK and North America); the 49% is the share of firms reporting increased client demand for alternative fee arrangements"
      provenance: vendor-published
      source_ref: BIGHAND-LF-2026
  prerequisites:
    - "Clear scoping, historical benchmarks and willingness to share risk (LEGALIO-AFA-2025)"
    - "Partners trained in scoping and project management, and compensation not based mainly on utilization (TRI-ILTACON-2025)"
    - "Client and firm agree what success and value mean under the fee (TRI-ILTACON-2025)"
  risks_and_guardrails:
    - "California guidance: flat fees may build in AI savings, and fee agreements should say how fees are calculated and how far AI factors into rates (CALBAR-GENAI-2026, p.8)"
    - "ABA Opinion 512 says it may be unreasonable under Rule 1.5 to charge the same flat fee when AI makes the work much faster; a Thomson Reuters Institute op-ed argues this risks client buyer's remorse (TRI-ABA512-2025)"
    - "Panel debate: a $100,000 AFA for work that would have cost $80,000 hourly may leave the client unhappy (Cohen) or satisfied if outcome and predictability were achieved (McPherson) (TRI-ILTACON-2025)"
    - "Billable hour expected to persist for at least five years; shift expected to be client-driven, slower, and hybrid (TRI-ILTACON-2025; LEGALIO-AFA-2025)"
  human_checkpoints:
    - "Partner and pricing team set scope, fee and re-scoping triggers"
    - "Client agrees success measures before the engagement"
  role_evolution: "Recruitment and compensation built on utilization are named as the main barrier (TRI-ILTACON-2025). Under AFAs the incentive moves to assigning work to the cheapest effective resource, which can reduce junior training unless designed for (ILTA-PULSE-2025)."
  evidence_grade: C
  sources:
    - { ref: TRI-ILTACON-2025, title: "ILTACON 2025: Pricing the future - AI's impact on the billable hour", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/iltacon-2025-billable-hour", date: 2025-09-02, access: full, locator: "sections 'Client value and billing' and 'Will GenAI kill the billable hour in five years?'" }
    - { ref: ILTA-PULSE-2025, title: "Bill(AI)ble Hour", publisher: ILTA (Pulse, ILTACON 2025), type: professional-body, url: "https://iltanet.org/resources/publications/pulse/iltacon/2025/billaible-hour", date: 2025, access: full, locator: "paragraphs 2-7 and 9" }
    - { ref: LEGALIO-AFA-2025, title: "AI Adoption Pushes Law Firms Toward Alternative Fees, But Change Will Be Incremental", publisher: Legal.io, type: press, url: "https://www.legal.io/articles/5771590/AI-Adoption-Pushes-Law-Firms-Toward-Alternative-Fees-But-Change-Will-Be-Incremental", date: 2025-12-23, access: full, locator: "paragraphs 2-4 and 6" }
    - { ref: BIGHAND-LF-2026, title: "AI is changing legal delivery, but 63% of firms default to standard rates or past matter pricing, BigHand research finds", publisher: Legal Futures, type: survey, url: "https://www.legalfutures.co.uk/associate-news/ai-is-changing-legal-delivery-but-63-of-firms-default-to-standard-rates-or-past-matter-pricing-bighand-research-finds", date: 2026-09-17, access: full, locator: "'Key findings', AI pricing paragraph" }
    - { ref: TRI-ABA512-2025, title: "Is ABA Formal Opinion 512 off the mark? And if so, what can law firms and GCs do about it?", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/aba-formal-opinion-512", date: 2025-04-02, access: full, locator: "sections on hourly fees and fixed-fee reasonableness" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026, access: full, locator: "p.8" }
  last_reviewed: 2026-10-19
  notes: "ILTA-PULSE-2025 is undated on the page (ILTACON 2025 recap). Baker McKenzie executives are reported by Legal.io as saying client AFA interest is 'persistent' - a secondary report of an American Lawyer piece I did not open. The ABA opinion itself was not opened (ABA site blocked in the landscape run); TRI-ABA512-2025 quotes it."

- id: professional-services-scoping-pricing-05
  title: KPI-based monthly retainer and portfolio billing in place of hourly billing for repeat insurance-defense work
  archetype: professional-services
  module: scoping-pricing
  function: sales-marketing-bd
  work_types: [expert-judgment, data-reporting]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Hourly billing penalizes efficiency, and in insurance defense it generates heavy bill-audit and appeals overhead on both sides; clients also refuse to pay for software or AI costs while expecting the efficiency gains."
  solution: "Kopka Law (insurance defense) moves clients to a monthly retainer or portfolio-based 'alternative billing' model judged on KPIs - cycle time and case disposition, early evaluation and consistent communication, indemnity outcomes relative to injury type, and collaboration - using the insurer's frequency and severity data and the firm's litigation-category data."
  outcomes:
    - lever: cost
      description: "none published (qualitative claim of freed capital and administrative resources for firm and client)"
      figure: "none published"
      measures: "not applicable; no figures stated in the article"
      provenance: self-reported
      source_ref: TRI-KOPKA-2026
  prerequisites:
    - "Client willingness (insurers) to negotiate away from line-item bill review"
    - "Shared data on frequency, severity, and litigation categories"
    - "Agreed KPIs that reward results, not low cost alone"
  risks_and_guardrails:
    - "Firm's COO says alternative fee arrangements designed solely to save the client money are 'destined to fail' because they push firms to cut corners (TRI-KOPKA-2026)"
    - "Fear of being underpaid and not knowing how to measure value other than by the clock slow adoption (TRI-KOPKA-2026)"
  human_checkpoints:
    - "Firm and carrier agree KPI definitions and review performance against them"
  role_evolution: "Firm says time capture in six-minute increments is driving talent out of defense practice; billing and appeals departments exist only to manage hourly billing (TRI-KOPKA-2026)."
  evidence_grade: B
  sources:
    - { ref: TRI-KOPKA-2026, title: "How one law firm is challenging a broken status quo around billing", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing", date: 2026-04-30, access: full, locator: "sections 'Why the billable hour hates AI' and 'Data as the solution'" }
    - { ref: ATL-DEFENSE-2026, title: "The Defense Bar In The Age Of AI: Running A Red Queen's Race?", publisher: Above the Law, type: press, url: "https://abovethelaw.com/2026/10/the-defense-bar-in-the-age-of-ai-running-a-red-queens-race/", date: 2026-10-19, access: full, locator: "sections on billing incentives and recommendation for carriers" }
  last_reviewed: 2026-10-19
  notes: "AI is a stated reason in the article but the model is not AI-specific; grade B reflects a named firm describing a real billing model without published results. The Above the Law column (author not captured) argues that contingency-fee plaintiffs' firms gain from AI efficiency while hourly defense firms lose, and suggests carriers move to flat or value-based arrangements; it comes from a practitioner who says he has done flat-fee work with a carrier."

- id: professional-services-scoping-pricing-06
  title: Outcome-linked and performance-based fees in strategy and transformation consulting
  archetype: professional-services
  module: scoping-pricing
  function: sales-marketing-bd
  work_types: [expert-judgment, client-interaction]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Clients arrive with a result they want rather than a defined scope, and AI-compressed analytical work makes hours harder to defend."
  solution: "McKinsey prices part of its work against client-defined outcomes (a scorecard such as investor targets, revenue or profit goals, operational measures and customer satisfaction), with some fixed components. A Forrester analyst note says management consultancies have moved toward putting fees at risk and expects the practice to expand as enterprises negotiate AI consulting contracts."
  outcomes:
    - lever: growth
      description: "Share of McKinsey's fees tied to outcomes"
      figure: "about a quarter of global fees (the same article also quotes McKinsey's global AI leader using 20%)"
      measures: "share of McKinsey's global fees from outcome-based pricing, as stated by McKinsey representatives at a November 2025 London media event and in an interview; not audited, basis and date of measurement not stated"
      provenance: self-reported
      source_ref: BI-MCKINSEY-2025
  prerequisites:
    - "Agreed scorecard and success measures with the client"
    - "Clean attribution of results to the consultant's work (STANFORD-DEL-2026, pp.15-16)"
    - "Measurement infrastructure in place before outcome pricing (STANFORD-DEL-2026, Rule 3)"
  risks_and_guardrails:
    - "McKinsey's own leader says the pricing model predates AI and AI-transformation work suits it, so the AI link is not established by the firm (BI-MCKINSEY-2025)"
    - "Secondary coverage notes the reporting does not explain baselines, who adjudicates a target, or whether partner pay changes (AIWEEKLY-MCK-2025)"
    - "Outcome pricing spreads only as far as attribution is clean; hybrid is the resting point elsewhere (STANFORD-DEL-2026, p.16 and Conclusion)"
  human_checkpoints:
    - "Partner and client agree scorecard; client signs off results"
  role_evolution: "Not described in the primary sources."
  evidence_grade: B
  sources:
    - { ref: BI-MCKINSEY-2025, title: "AI is reshaping how McKinsey makes money", publisher: Business Insider (read via Yahoo Finance syndication), type: press, url: "https://finance.yahoo.com/news/ai-reshaping-mckinsey-makes-money-195132745.html", date: 2025-11-17, access: full, locator: "paragraphs 1-8" }
    - { ref: STANFORD-DEL-2026, title: "Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives", publisher: Stanford Digital Economy Lab (Brynjolfsson, Petropoulos), type: academic, url: "https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf", date: 2026-08-23, access: full, locator: "p.14 (McKinsey, PwC US Tax Leader), pp.15-16, Rule 3 (pp.21-22)" }
    - { ref: FORRESTER-BLOG-2025, title: "The Future Of AI Consulting Services Is Disruptively Bright", publisher: Forrester, type: press, url: "https://www.forrester.com/blogs/the-future-of-ai-consulting-services-is-disruptively-bright", date: 2025-09-15, access: full, locator: "section on sharing risk (paragraph beginning 'Modify their economic models')" }
    - { ref: AIWEEKLY-MCK-2025, title: "McKinsey Ties 25% of Fees to Outcomes as AI Erodes Billable Hours", publisher: AI Weekly (summarising a WSJ report), type: press, url: "https://aiweekly.co/alerts/mckinsey-ties-25-of-fees-to-outcomes-as-ai-erodes-billable-hours", date: 2026-06-29, access: full, locator: "paragraphs 3-4" }
  last_reviewed: 2026-10-19
  notes: "Grade B, not A, because the figure is a statement to reporters, not published data. The landscape listed AIWEEKLY-MCK-2025 as 'late 2025'; the page's own metadata says published 2026-06-29, so the ref keeps the landscape key but the date is corrected. The landscape's 'about a third' McKinsey figure (Resultsense, May 2026) is unverified and I did not use it. BCG and Bain AI-share figures in AIWEEKLY-MCK-2025 are the firms' own characterisations per that article and measure AI-related revenue, not outcome fees, so they are not used as outcomes here. The Business Insider article also says EY's global growth and innovation partner told it AI agents may call for a 'service-as-a-software' outcome approach (month given as January, year not stated)."

- id: professional-services-scoping-pricing-07
  title: Productized AI-enabled services sold by subscription or consumption (PwC One)
  archetype: professional-services
  module: scoping-pricing
  function: product-service-development
  work_types: [expert-judgment, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: "Hours-based billing, built on large teams of junior staff doing routine tasks, is threatened when AI can do much of that work, and clients may do more in-house."
  solution: "PwC launched PwC One on 19 March 2026, an AI-enabled environment being introduced in the US within select PwC teams and client engagements, spanning tax analysis, financial reporting, sustainability assurance, deal diligence and operating-model work. Press coverage of the CEO's Financial Times interview says some tax and consulting services would be offered as automated tools clients can use 'without a PwC person in the loop', possibly on annual subscription; Accounting Today says pricing will evolve and may involve subscription or consumption elements. PwC's own release does not state pricing."
  outcomes:
    - lever: growth
      description: "none published"
      figure: "none published"
      measures: "not applicable; PwC has not published client counts, revenue or pricing for PwC One in the sources read"
      provenance: self-reported
      source_ref: PWC-ONE-2026
  prerequisites:
    - "Platform of automated services under professional oversight"
    - "A fee model for access rather than hours (not specified publicly)"
  risks_and_guardrails:
    - "Secondary coverage says the early-access period will test whether clients pay for subscription tools in place of bespoke advisory (RESULTSENSE-PWC-2026)"
    - "PwC states the AI is meant to sharpen professional judgment and that clients should have the oversight they expect (PWC-ONE-2026)"
  human_checkpoints:
    - "Professional oversight stated by PwC; some services are described as having no PwC person in the loop (CPAPA-PWC-2026)"
  role_evolution: "CEO told the FT partners who resist AI 'have no place at the firm' (CPAPA-PWC-2026). Resultsense reports senior-staff bonuses will track revenue and margin per professional rather than hours billed (secondary report; RESULTSENSE-PWC-2026). PwC's US Tax Leader said 'time's becoming less and less of relevance' in pricing talks (quoted in STANFORD-DEL-2026, p.14)."
  evidence_grade: B
  sources:
    - { ref: PWC-ONE-2026, title: "PwC Introduces PwC One as Part of Its Vision for AI-Enabled Professional Services", publisher: PwC US, type: firm, url: "https://www.pwc.com/us/en/about-us/newsroom/press-releases/pwc-one.html", date: 2026-03-19, access: full, locator: "paragraphs on rollout scope and 'continuous insight' (read via mirror; site returns 403 to curl)" }
    - { ref: ACCTODAY-PWC-2026, title: "PwC CEO: You cannot opt out of AI", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/pwc-ceo-you-cannot-opt-out-of-ai", date: 2026-03-20, access: full, locator: "paragraphs 1 and 4 (pricing model sentence)" }
    - { ref: CPAPA-PWC-2026, title: "PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'", publisher: CPA Practice Advisor (reporting the Financial Times), type: press, url: "https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/", date: 2026-03-25, access: full, locator: "paragraphs 1-6" }
    - { ref: RESULTSENSE-PWC-2026, title: "PwC Warns Partners: Adopt AI or Face Exit", publisher: Resultsense, type: press, url: "https://www.resultsense.com/news/2026-03-19-pwc-ai-overhaul-partners-resist-technology/", date: 2026-03-19, access: full, locator: "section 'From Hours to Outcomes'" }
    - { ref: STANFORD-DEL-2026, title: "Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives", publisher: Stanford Digital Economy Lab, type: academic, url: "https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf", date: 2026-08-23, access: full, locator: "pp.14, 15 and 17" }
  last_reviewed: 2026-10-19
  notes: "The Financial Times original was not opened; all pricing statements are from secondary coverage and the Stanford paper's citation of it. The landscape says PwC One launched 'with six automated services'; CPA Practice Advisor says six automated services at launch, with more promised. Stanford's paper says PwC's own announcement stops short of pricing specifics, which matches what I found. Dated 2026-03-19 (PwC release) versus 2026-03-25 (CPAPA article)."

- id: professional-services-scoping-pricing-08
  title: Choosing the fee structure by locating each engagement on an outcome-observability and input-cost-observability map
  archetype: professional-services
  module: scoping-pricing
  function: strategy-planning
  work_types: [expert-judgment, data-reporting]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Pricing models are chosen by convention. AI augmentation makes hours a poor proxy for effort, and it is unclear when outcome pricing is sound."
  solution: "The Stanford framework (idea) asks two questions per engagement: can the client verify results and attribute them to the firm (outcome observability), and can the client see the firm's true cost of delivery (input-cost observability)? It then maps time-based, project, hybrid, subscription and outcome pricing onto the answers, with four rules: match contract power to signal informativeness; let internal versus productized AI decide direction; measure before moving to outcome pricing but check whether attribution is the binding constraint; treat hybrid as the equilibrium under partial information."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "not applicable; the paper says its consistency with observed pricing is 'qualitative plausibility' and not confirmatory validation (p.5)"
      provenance: independent
      source_ref: STANFORD-DEL-2026
  prerequisites:
    - "Engagement-level data on outcome measurement and attribution"
    - "Telemetry and agreed ground-truth metrics where outcome pricing is considered"
  risks_and_guardrails:
    - "Attribution risk sets a floor that telemetry cannot lower; where a firm's contribution is confounded with the client's other initiatives hybrid contracts are the destination (STANFORD-DEL-2026, p.3 and p.16)"
    - "Measured parties may act on the metrics rather than the work (STANFORD-DEL-2026, p.16)"
    - "Authors disclose informal confidential conversations with three Accenture executives as motivation only and a general gift from Accenture to the lab (STANFORD-DEL-2026, p.1 footnote)"
  human_checkpoints:
    - "Executive locates engagement on the map and approves structure"
  role_evolution: "Authors say firms should build hybrid pricing capability as a strategic competence (Rule 4, p.22)."
  evidence_grade: D
  sources:
    - { ref: STANFORD-DEL-2026, title: "Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives", publisher: Stanford Digital Economy Lab (Brynjolfsson, Petropoulos), type: academic, url: "https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf", date: 2026-08-23, access: full, locator: "Abstract; pp.3-4; Section 7 rules (pp.20-22)" }
  last_reviewed: 2026-10-19
  notes: "Idea: a theoretical framework with illustrative cases (McKinsey, Deloitte, Accenture, Palantir, Salesforce Agentforce). The Palantir and Salesforce cases concern software and platform pricing, not consulting fees. Labelled idea."

- id: professional-services-scoping-pricing-09
  title: Automatic capture of AI-platform work as time entries, with AI-value measures for pricing conversations
  archetype: professional-services
  module: scoping-pricing
  function: finance-accounting
  work_types: [data-reporting]
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Firms cannot show clients, or themselves, what AI use is saving or earning on a matter; time is reconstructed from memory and AI work is hard to capture."
  solution: "Laurel and Legora announced (13 October 2026) that each task a lawyer completes in Legora becomes a draft time entry on the right client and matter for the lawyer to review. A second phase will develop, with customers, measures of how Legora is used and the value AI-powered work brings."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "not applicable; announcement only, availability details to follow"
      provenance: vendor-published
      source_ref: LEGORA-LAUREL-2026
  prerequisites:
    - "Firm uses both platforms"
    - "Agreement on which value measures matter and how to calculate them"
  risks_and_guardrails:
    - "Only firms using both platforms; AI-usage and value measures are not yet defined"
    - "Time entries must still reflect time actually spent (CALBAR-GENAI-2026, p.8)"
  human_checkpoints:
    - "Lawyer reviews each draft time entry"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: LEGORA-LAUREL-2026, title: "Legora and Laurel partner to capture the time lawyers spend in Legora as they work", publisher: Legora, type: vendor, url: "https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work", date: 2026-10-13, access: full, locator: "paragraphs 2-5" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "section 'Proving AI's path to saving clients money'" }
    - { ref: ATL-LITERA-2026, title: "Avoiding The AI Efficiency Trap: What Biglaw Needs To Get Right", publisher: Above the Law (Litera-sponsored webinar promotion), type: vendor, url: "https://abovethelaw.com/2026/08/avoiding-the-ai-efficiency-trap-what-biglaw-needs-to-get-right/", date: 2026-08-18, access: full, locator: "agenda list (tracking 'RoAI'; whether firms adjust the billable hour)" }
  last_reviewed: 2026-10-19
  notes: "Billing-collections is the primary home for time capture (see Routed). It is kept here because the second-phase aim is AI-value evidence for pricing. The Above the Law item is a sponsored promotion for a 9 September 2026 webinar; I did not find a recap of what was said."

- id: professional-services-scoping-pricing-10
  title: Predictive budget-overrun alerts and live work-in-progress against matter budget
  archetype: professional-services
  module: scoping-pricing
  function: finance-accounting
  work_types: [data-reporting, coordination-scheduling]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "Budgets are set, but few firms manage them actively, so overruns become write-offs."
  solution: "Ayora monitors budgets, work in progress, billing and collections against benchmarks from a firm's own historic matters and issues predictive alerts on matters at risk of exceeding budget. Narrative describes live WIP against budget, automated outside-counsel-guideline compliance and catching overruns before write-off."
  outcomes:
    - lever: quality
      description: "Survey baseline on budget management"
      figure: "63% track budgets against actuals in a structured way (40% review at key milestones); 23% actively monitor and update throughout the matter; of firms assigning matter budgets, 99% report some increase in billing realization"
      measures: "shares of BigHand survey respondents (800+ legal finance professionals); the 99% is among firms that assign matter budgets and counts any increase in billing realization, not an amount"
      provenance: vendor-published
      source_ref: BIGHAND-LF-2026
  prerequisites:
    - "Enriched historic matter data for benchmarks"
    - "Clear owners for acting on alerts"
  risks_and_guardrails:
    - "Vendor-described only; no customer or accuracy data"
    - "Budget realization figure is not specific to AI"
  human_checkpoints:
    - "Matter team acts on alerts and agrees re-scoping with client"
  role_evolution: "Not described."
  evidence_grade: C
  sources:
    - { ref: AYORA-LTH-2026, title: "Ayora by BigHand", publisher: Legaltech Hub, type: vendor, url: "https://www.legaltechnologyhub.com/vendors/ayora-by-bighand/", date: 2026-10-19, access: full, locator: "feature list" }
    - { ref: NARRATIVE-ILTA-2026, title: "Narrative", publisher: ILTA (Startup 2026 profile), type: vendor, url: "https://www.iltanet.org/resources/publications/pulse/startup26/narrative", date: 2026-10-19, access: full, locator: "paragraph 5" }
    - { ref: BIGHAND-LF-2026, title: "AI is changing legal delivery, but 63% of firms default to standard rates or past matter pricing, BigHand research finds", publisher: Legal Futures, type: survey, url: "https://www.legalfutures.co.uk/associate-news/ai-is-changing-legal-delivery-but-63-of-firms-default-to-standard-rates-or-past-matter-pricing-bighand-research-finds", date: 2026-09-17, access: full, locator: "'Budgeting is widespread, but active management remains limited'" }
  last_reviewed: 2026-10-19
  notes: "Overlaps delivery-management. Kept here because budget setting and re-scoping are part of the pricing cycle. Narrative also claims firms write off close to 18% of work they bill, a vendor figure with no stated source."

- id: professional-services-scoping-pricing-11
  title: Client-initiated fee renegotiation citing AI efficiency (KPMG and its auditor Grant Thornton)
  archetype: professional-services
  module: scoping-pricing
  function: procurement-supply-chain
  work_types: [client-interaction]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Buyers of professional services expect AI savings to show up in the fee; suppliers have no agreed way to price them."
  solution: "As reported by the Financial Times and repeated in trade coverage, KPMG pressed its own auditor, Grant Thornton, to reduce its fee because of AI-driven efficiencies, reportedly threatening to change auditor. Reported result: the audit fee fell from about $416,000 to about $357,000."
  outcomes:
    - lever: cost
      description: "Reported reduction in KPMG's audit fee from its auditor"
      figure: "14% (about $416,000 in 2024 to about $357,000 in 2025)"
      measures: "reported change in the fee KPMG paid Grant Thornton for audit services, 2024 to 2025, per trade coverage of an FT report; neither firm's own statement was read"
      provenance: independent
      source_ref: YAHOO-KPMG-2026
  prerequisites:
    - "A buyer with a credible alternative supplier"
    - "A shared belief that AI lowers the supplier's cost"
  risks_and_guardrails:
    - "Commentators say the precedent hands KPMG's own audit clients the same argument (YAHOO-KPMG-2026; ONLYCFO-KPMG-2026)"
    - "Sources disagree on which KPMG entity was involved (KPMG International in one; Grant Thornton UK in another)"
    - "Another view: fees should not fall if AI improves the product (reported in MYCPE-KPMG-2026 summary)"
  human_checkpoints:
    - "Fee negotiated between buyer and supplier"
  role_evolution: "Not described."
  evidence_grade: B
  sources:
    - { ref: YAHOO-KPMG-2026, title: "Big Four accounting firm's bold demand is a warning about AI adoption", publisher: Yahoo Finance, type: press, url: "https://finance.yahoo.com/news/big-four-accounting-firms-bold-015348056.html", date: 2026-02-10, access: full, locator: "paragraphs 1-4" }
    - { ref: ONLYCFO-KPMG-2026, title: "AI is Coming for Audit Fees: KPMG Just Proved It", publisher: OnlyCFO (newsletter), type: community, url: "https://www.onlycfo.io/p/ai-is-coming-for-audit-fees-kpmg", date: 2026-02-13, access: full, locator: "paragraphs 1-4" }
    - { ref: MYCPE-KPMG-2026, title: "How a Big Four audit fee cut raises a bigger AI question", publisher: MYCPE ONE Insights, type: press, url: "https://my-cpe.com/insights/news-and-insights/accounting-and-taxes/how-a-big-four-audit-fee-cut-raises-a-bigger-ai-question", date: 2026-02-09, access: full, locator: "opening summary (article body paywalled)" }
  last_reviewed: 2026-10-19
  notes: "Grade B at most: the figure is press-reported (the FT original, behind a paywall, was not read) and no party confirmed it in a source I read. This is a fee negotiation between two accounting firms, not an audit-method change. Dollar figures are as reported, in US dollars, and are small."

- id: professional-services-scoping-pricing-12
  title: Disclosed pass-through of matter-specific AI costs, with general AI subscriptions treated as overhead
  archetype: professional-services
  module: scoping-pricing
  function: finance-accounting
  work_types: [document-production, data-reporting]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Firms invest heavily in AI and look for ways to recover cost, but clients resist and ethics rules limit what can be billed."
  solution: "Idea from regulator guidance and practitioner commentary: treat general AI subscriptions as overhead absorbed in rates; bill matter-specific costs (per-use fees for specialized tools, custom implementations) only at actual cost, with fee-agreement disclosure, and with no markup without informed written consent. Practitioners suggest firms instead look for new revenue mechanisms rather than cost recovery."
  outcomes:
    - lever: cost
      description: "none published"
      figure: "none published"
      measures: "not applicable"
      provenance: independent
      source_ref: CALBAR-GENAI-2026
  prerequisites:
    - "Fee agreement language that discloses AI costs may be billed separately"
    - "Cost tracking per matter"
  risks_and_guardrails:
    - "No markup or profit element without informed written consent (CALBAR-GENAI-2026, p.8)"
    - "Client resistance and ethical considerations make traditional cost recovery hard for AI tools (TRI-AIBIZ-2025)"
    - "Insurance-defense clients are described as refusing to pay for software or AI costs (TRI-KOPKA-2026)"
  human_checkpoints:
    - "Billing partner confirms disclosure and client consent"
  role_evolution: "Not described."
  evidence_grade: D
  sources:
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: 2026, access: full, locator: "p.8" }
    - { ref: TRI-AIBIZ-2025, title: "How AI is continuing to change the business of law", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/ai-business-of-law", date: 2025-08-20, access: full, locator: "section 'Focusing on new methods of cost recovery'" }
    - { ref: EDISCOVERYTODAY-ILTACON-2026, title: "My Five ILTACON 2026 Takeaways", publisher: eDiscovery Today, type: press, url: "https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/", date: 2026-09-04, access: full, locator: "section 'Is tokengeddon looming for AI pricing?'" }
  last_reviewed: 2026-10-19
  notes: "Idea: no firm was found describing a disclosed pass-through in practice. The eDiscovery Today author reports a hallway topic at ILTACON 2026: a possible move from seat-based to consumption-based AI vendor pricing, with vendors reluctant to discuss it unless asked. If vendor pricing becomes usage-based, per-matter AI cost becomes variable, which would matter for fixed-fee margins (no source quantifies this)."

- id: professional-services-scoping-pricing-13
  title: Tiered packages and subscription pricing for tax, accounting and advisory clients
  archetype: professional-services
  module: scoping-pricing
  function: sales-marketing-bd
  work_types: [expert-judgment, client-interaction]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Hourly billing ties price to time while AI compresses compliance work; RSM's tax-advisory example: a 20-hour client report could take 10 hours with generative AI and review, and it is unclear whether the gain is margin or price reduction."
  solution: "Firms package services into basic, standard and premium tiers with modular add-ons and bill monthly or quarterly. RKL (a named firm) is piloting an alternative pricing model built on value-based tenets by consultancy Fore, and onboarded several dozen new clients under it. RSM, KPMG and PwC leaders describe working toward value and outcome pricing."
  outcomes:
    - lever: quality
      description: "Pricing-confidence gap between subscription-first and hourly firms (not AI-specific)"
      figure: "nearly one-third highly confident in subscription-first firms versus less than 20% in hourly firms"
      measures: "share of tax professionals who say they are highly confident their pricing aligns with value delivered, in firms using subscription billing for most clients versus firms using hourly pricing, from Thomson Reuters Institute's 2025 Tax Firm Pricing Report as summarised by TRI"
      provenance: vendor-published
      source_ref: TRI-ALTPRICING-2025
    - lever: growth
      description: "Client onboarding under a pilot value-based model at a named firm"
      figure: "several dozen new clients"
      measures: "RKL tax partner's statement of clients onboarded under the alternative pricing model during the firm's pilot; count, period and revenue not given"
      provenance: self-reported
      source_ref: BLAW-ACCT-2026
  prerequisites:
    - "Productized service catalogue with defined add-ons"
    - "Value narrative and ROI examples for clients"
    - "Performance metrics that no longer reward hours alone (Wipfli adding client satisfaction and cycle time, BLAW-ACCT-2026)"
  risks_and_guardrails:
    - "Only a small portion of engagements are subscription-based today (TRI-ALTPRICING-2025)"
    - "Conflict if staff are asked to adopt AI but are judged on decade-old metrics (Wipfli, BLAW-ACCT-2026)"
    - "AI tool investment is hard to attribute to individual projects (KPMG US advisory vice chair, BLAW-ACCT-2026)"
  human_checkpoints:
    - "Partner sets price and value narrative per client"
    - "Early phases of advisory work may stay time-based; value pricing applied when options are identified (PwC, BLAW-ACCT-2026)"
  role_evolution: "Professionals must learn to scope, articulate value and negotiate with confidence; compensation and origination credit must stop rewarding hours alone (MONDAQ-GGI-2026). Value-based firms can use revenue-based bonus metrics (Big 4 Transparency founder, BLAW-ACCT-2026)."
  evidence_grade: B
  sources:
    - { ref: BLAW-ACCT-2026, title: "AI Efficiency Gains Push Accounting Firms to Reimagine Pricing", publisher: Bloomberg Tax, type: press, url: "https://news.bgov.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing", date: 2026-03-05, access: full, locator: "paragraphs 1-6, 8-15" }
    - { ref: TRI-ALTPRICING-2025, title: "From hours to outcomes: How alternative pricing models are redefining tax firm profitability", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/alternative-pricing-models", date: 2025-09-25, access: full, locator: "sections 'The confidence advantage of subscriptions' and 'A practical path to transition'" }
    - { ref: MONDAQ-GGI-2026, title: "Still Selling Judgment: How Law Firms And Accounting Firms Must Prepare For AI-driven Pricing Change", publisher: GGI Global Alliance via Mondaq, type: press, url: "https://www.mondaq.com/unitedstates/management/1814268/still-selling-judgment-how-law-firms-and-accounting-firms-must-prepare-for-ai-driven-pricing-change", date: 2026-07-09, access: full, locator: "paragraphs 4-9" }
    - { ref: BAKER-PODCAST-2026, title: "How AI Will Kill the Billable Hour in CPA Firms | Ron Baker (Growing Your Firm podcast)", publisher: Podwise (episode summary), type: podcast, url: "https://podwise.ai/episodes/8845213", date: 2026-09-06, access: full, locator: "episode summary (machine summary only; audio and transcript not read)" }
  last_reviewed: 2026-10-19
  notes: "Grade B because RKL is a named firm with a described pilot, but no outcome is quantified beyond the client count. The AICPA 2025 survey (1,000+ firms) found median net hourly billing rate up nearly 7% over two years to $170 and recommended firms consider accelerating the shift from hourly billing, as reported in BLAW-ACCT-2026; I did not open the AICPA report. TRI-ALTPRICING-2025 is written for tax, audit and accounting firms and its confidence figure is not about AI effects. The podcast is cited only as a signal of the argument."

- id: professional-services-scoping-pricing-14
  title: Repricing freed capacity toward proactive advisory and judgment in tax and accounting
  archetype: professional-services
  module: scoping-pricing
  function: strategy-planning
  work_types: [expert-judgment, client-interaction]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Routine compliance is commoditizing, yet advisory work, which clients value, is priced and earns less than routine return preparation."
  solution: "Firms shift the service mix from time-billed compliance toward year-round advisory priced on value or retainer, using AI to release capacity. TRI describes three paths: redeploy people to advisory, serve more clients with the same headcount, or rebuild around continuous insight. SPI's 2026 study says the unresolved 'leak' is that hours AI saves are rarely resold or repriced."
  outcomes:
    - lever: growth
      description: "Margin and pricing-model data from the TRI State of Tax Professionals and Year-Round Tax Advisor reports as summarised by TRI"
      figure: "78% of firms use hourly billing; individual return preparation 28% profit margin versus 20-24% for advisory services; highest-margin firms use value-based pricing 61% of the time versus 54% for the lowest-margin tier"
      measures: "78% is the share of surveyed tax firms using hourly billing; margins are survey-reported profit margins by service line; 61% and 54% are the share of the time value-based pricing is used, by margin tier; sample sizes not stated in the article"
      provenance: vendor-published
      source_ref: TRI-CHARGING-2026
  prerequisites:
    - "Year-round client relationship and proactive outreach"
    - "A deliberate choice among redeploy, scale or rebuild paths (TRI-CHARGING-2026)"
    - "Leadership that plans how to reprice or resell hours AI saves (SPI-AI-2026)"
  risks_and_guardrails:
    - "Freed-up time is not itself billable; the sales case rests on what the firm does with it (TRI-CHARGING-2026)"
    - "Drifting between paths while still billing hourly is flagged as the failure mode (TRI-CHARGING-2026)"
  human_checkpoints:
    - "Partners decide which services to productize and how to price them"
  role_evolution: "Moves professionals from preparation toward proactive planning and judgment; TR-FOP-2026 notes tax professionals expect trusted-judgment timelines to shorten by one year while legal professionals expect them to lengthen by nearly two (pipeline question)."
  evidence_grade: C
  sources:
    - { ref: TRI-CHARGING-2026, title: "If AI can do the work, then what are you actually charging for?", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/what-are-you-actually-charging-for", date: 2026-10-02, access: full, locator: "sections 'Compliance work is commoditizing' and 'Clients are already grading firms'" }
    - { ref: SPI-AI-2026, title: "2026 AI in Professional Services Survey", publisher: SPI Research, type: survey, url: "https://spiresearch.com/reports/2026-ai-professional-services-survey/", date: 2026-07-14, access: full, locator: "'The Leak' panel and Chapter 6 title (report is paid; page figures partly masked)" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report", date: 2026, access: full, locator: "'Elevate', 'Scale' and 'Reimagine' path sections; methodology note" }
  last_reviewed: 2026-10-19
  notes: "The correlation between value-based pricing and margin is not shown to be caused by AI or pricing. SPI's page shows a teaser contrast ('84.8% vs. 00.0%' with the second value masked) of respondents saying AI saves time versus generates revenue; I did not rely on those numbers. SPI-AI-2026 is dated by the page's published timestamp (2026-07-14); the landscape had 'Oct 2026'. TR-FOP-2026 date is the year only: the page shows no publication date; fieldwork March-April 2026."

- id: professional-services-scoping-pricing-15
  title: Client-proposed data-baselined fixed price with a time-tracked variance trigger
  archetype: professional-services
  module: scoping-pricing
  function: procurement-supply-chain
  work_types: [data-reporting, client-interaction]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Under hourly billing every AI efficiency lowers the client's bill, which makes AI investment irrational for the firm; so firms invest quietly or not at all."
  solution: "In-house general counsel's proposal (idea): for a repeat relationship, set a baseline price for a defined scope using a shared dataset of past matters (for example 250 acquisitions handled by one firm); the firm still tracks time but only to trigger adjustments (an illustrative 25% variance from scoped hours opens a conversation); for new firms ask for a fixed price. The author also asks firms to disclose how they use AI."
  outcomes:
    - lever: cost
      description: "none published"
      figure: "none published"
      measures: "not applicable. The author separately says his team reported averaging 8 hours saved per week after introducing one AI platform; this is a recollection by the client team and is not an outcome of the proposed fee model"
      provenance: self-reported
      source_ref: BLAW-ROBB-2026
  prerequisites:
    - "Dataset of comparable past matters shared by client and firm"
    - "Trust between client and firm; engagement letter stating the variance trigger"
  risks_and_guardrails:
    - "Cites ABA Opinion 512 as barring billing for time not actually spent (BLAW-ROBB-2026)"
    - "The 25% variance trigger is explicitly an illustration, not an industry rule"
  human_checkpoints:
    - "General counsel and firm agree baseline and adjustment mechanism"
  role_evolution: "Author expects firms that track and communicate AI use to build trust and associates' development rather than only hours (BLAW-ROBB-2026)."
  evidence_grade: D
  sources:
    - { ref: BLAW-ROBB-2026, title: "The Billable Hour Isn't Dead Yet, But AI Should Reshape Pricing", publisher: Bloomberg Law (opinion by Tim Robb, general counsel), type: community, url: "https://news.bgov.com/business-and-practice/the-billable-hour-isnt-dead-yet-but-ai-should-reshape-pricing", date: 2026-06-29, access: full, locator: "sections 'Tell me you're using it', 'Price our work based on what we both know' and 'Charge me a fixed price'" }
  last_reviewed: 2026-10-19
  notes: "In-house practitioner opinion; the author's byline is a general counsel at a private-equity portfolio company, and the article says it does not reflect Bloomberg's view. The ACC/Everlaw figure the author cites (nearly a quarter 'very likely' to push for a change to the billable hour) is reported second-hand and was not checked at source."

- id: professional-services-scoping-pricing-16
  title: Joint firm-client AI value-sharing conversations and co-designed pilots on key accounts
  archetype: professional-services
  module: scoping-pricing
  function: sales-marketing-bd
  work_types: [client-interaction, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: emerging
  problem: "Firms and clients are each designing AI-era pricing and work allocation without talking to each other; two-thirds of general counsel say they do not know how their outside firms approach AI."
  solution: "Idea discussed by practitioners: firms open the AI value conversation first, pick a few key clients, propose use cases and co-design them, and agree how productivity gains are shared. Speakers urge firms to 'lead the conversation' and set the meeting. Five questions are proposed for joint agendas: value and pricing, where work lives, trust and transparency, talent pipeline, ecosystem standards."
  outcomes:
    - lever: experience
      description: "none published"
      figure: "none published"
      measures: "not applicable; context figure: 'two-thirds of GCs say they do not know how their outside firms are approaching AI' (Thomson Reuters Institute research, as cited in TRI-INTERDEP-2026; basis not stated in the article)"
      provenance: vendor-published
      source_ref: TRI-INTERDEP-2026
  prerequisites:
    - "Partners willing to discuss AI with clients (35% of surveyed firms cite partner discomfort as the most common barrier, BIGHAND-LF-2026)"
    - "Matter-level evidence of savings"
  risks_and_guardrails:
    - "Firms 'still gathering the data' cannot yet answer client savings questions (TRI-LEGALWEEK-2026)"
    - "Client postures are inconsistent (TRI-LEGALWEEK-2026)"
  human_checkpoints:
    - "Client general counsel and firm leadership agree pilot terms"
  role_evolution: "Chief pricing and innovation officers and AI innovation heads become client-facing negotiators of value (TRI-LEGALWEEK-2026)."
  evidence_grade: D
  sources:
    - { ref: TRI-INTERDEP-2026, title: "Interdependent by design: The AI conversation law firms and legal departments need to be having now", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/needed-ai-conversation", date: 2026-06-11, access: full, locator: "sections 'Addressing 5 critical questions together' and communication-gap paragraph" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "sections 'Proving AI's path...' and 'The contradictions in the room'" }
    - { ref: TRI-LEADFOLLOW-2025, title: "Pricing AI-driven legal services: Lead or follow, there is no 'out of the way'", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/institute/articles/pricing-ai-driven-legal-services-lead-or-follow", date: 2025-01-30, access: full, locator: "section 'The importance of setting whose terms will control'" }
    - { ref: BIGHAND-LF-2026, title: "AI is changing legal delivery, but 63% of firms default to standard rates or past matter pricing, BigHand research finds", publisher: Legal Futures, type: survey, url: "https://www.legalfutures.co.uk/associate-news/ai-is-changing-legal-delivery-but-63-of-firms-default-to-standard-rates-or-past-matter-pricing-bighand-research-finds", date: 2026-09-17, access: full, locator: "paragraph 3" }
  last_reviewed: 2026-10-19
  notes: "Idea: widely recommended, no firm-client agreement on value sharing was found published. GSK's Chief of Staff (in-house) said at Legalweek 2026 that GSK wants to partner with outside firms on use cases and agree savings together (TRI-LEGALWEEK-2026)."
```

## 3. Module notes

**Processes and key steps (with work types)**
- Understand the opportunity and the client's goal, including what success is (research-synthesis; client-interaction).
- Estimate effort, staffing and risk, usually from past matters or templates (data-reporting). This is the step vendors target with AI.
- Choose a fee structure: hourly, capped, fixed, hybrid, subscription, outcome-linked (expert-judgment).
- Draft the fee proposal, SOW or engagement letter, with AI disclosure and cost terms (document-production).
- Negotiate and have the value conversation, including client guidelines and RFP pricing (client-interaction).
- Set the matter budget, then monitor, re-scope and handle change requests (coordination-scheduling; data-reporting).
- Review realization and pricing after the matter (data-reporting). Firm-level rates and realization route to firm-finance.
- Price the firm's own AI-enabled products and services (expert-judgment). The pricing function moves toward a product-style role (TRI-PRICINGPROS-2024, Nov 2024).

**Common pain points**
- Efficiency lowers revenue under hourly billing; billing time actually spent is also required by ethics guidance (TRI-KOPKA-2026; CALBAR-GENAI-2026, p.8).
- Firms cannot evidence AI savings by matter and are 'still gathering the data' (TRI-LEGALWEEK-2026).
- Pricing relies on habit: 35% hourly default, 28% copy of a past matter, 1% template use (BIGHAND-LF-2026).
- Scoping fixed-fee work is risky for partners not trained in project management, and scope changes send parties back to the table (TRI-ILTACON-2025).
- Partner pay and recruiting built on utilization discourage non-hourly pricing (TRI-ILTACON-2025; MONDAQ-GGI-2026).
- Clients send mixed signals: demand AI use, then refuse to pay for it, or send blanket bans (TRI-LEGALWEEK-2026).

**Metrics and benchmarks (what each measures)**
- ACC/Everlaw (June-July 2025, about 650 in-house and legal-ops respondents): nearly 60% saw no noticeable savings yet; more than 60% said it is too early in the adoption cycle for cost reductions; 64% expect to bring more work in-house (ACCEVERLAW-BL-2025).
- BigHand (800+ legal-finance professionals): 56% saw increased demand for AI-driven efficiencies or AI-use transparency; 51% for financial transparency; 49% for AFAs; 35% name partner discomfort as the top communication barrier; 31% report better profitability per matter and 31% less repetitive work from AI (BIGHAND-LF-2026).
- TR-FOP-2026 (1,816 professionals, 62 countries, March-April 2026): 78% of corporate clients rate AI-enabled quality improvement very important or essential versus 6% saying most or all providers deliver it; 32% have reconsidered or plan to reconsider firm relationships within 12 months; among those, a third say more than $1 million a year is at risk.
- TRI tax data: hourly billing used by 78% of firms; individual return prep margin 28% versus 20-24% for advisory (TRI-CHARGING-2026).
- AICPA 2025 survey (as reported by Bloomberg Tax): median net hourly billing rate up nearly 7% over two years to $170 (BLAW-ACCT-2026).
- Law firm rates: Am Law 100 worked rates up almost 10% in Q1 2026 while demand grew 2.7% (TRI-LFFI-Q1-2026); fees worked per lawyer rose 16.8% and profit per lawyer 8.4% above pre-2022 levels by end-2025, mostly from rate increases (TRI-SOTLM-2026). These are rate and profit data, routed to firm-finance.
- RFP price outcomes: a Perkins Coie pricing manager said lowest bids on reverse-auction platforms lose 54% of the time and highest bids win 18%; this is a panelist's statement and the denominator was not given (TRI-ILTACON-2025).
- McKinsey: about a quarter of global fees from outcome-based pricing, with a 20% figure also quoted (BI-MCKINSEY-2025).
- Consulting cost lever: McKinsey's Lilli reportedly delivers up to 30% time savings in searching and synthesizing knowledge (cited in STANFORD-DEL-2026, p.13 from a McKinsey page).
- KPMG-Grant Thornton fee: 14% reported reduction (YAHOO-KPMG-2026).
- Quality evidence: none found. No source reports error rates, override rates, parallel-run results or independent measurement of AI-assisted estimates or fee proposals. Vendor figures (Narrative, Certinia) have no sample, baseline or customer named.

**Guardrails and regulatory points**
- California 2026 guidance (p.8): hourly billing reflects time actually spent; flat fees may include AI savings; fee agreements should say how fees and costs are calculated and the extent to which AI factors into rates; general AI subscriptions are overhead; matter-specific AI costs need disclosure at actual cost and no markup without informed written consent (CALBAR-GENAI-2026).
- ABA Opinion 512, as quoted by a Thomson Reuters Institute op-ed: lawyers billing hourly must bill actual time; it may be unreasonable to charge the same flat fee when AI makes the work much faster; the op-ed argues this creates risk of buyer's remorse on fixed fees (TRI-ABA512-2025, 2 April 2025). The opinion text itself was not opened.
- Disclosure of AI use to clients is an ethics and commercial question: 56% of firms see rising client demand for AI transparency (BIGHAND-LF-2026).
- Revenue and attribution discipline for outcome fees: no baseline, adjudicator or partner-pay detail published for McKinsey outcome contracts (AIWEEKLY-MCK-2025).

**Frontier signals (dated and sourced)**
- 2025-11-17: McKinsey says about a quarter of fees outcome-based (BI-MCKINSEY-2025).
- 2026-03-19/25: PwC One introduced; CEO says some services will be offered without a PwC person in the loop and billing alternatives will be offered (PWC-ONE-2026; CPAPA-PWC-2026).
- 2026-03-13: Legalweek: clients ask for line-item AI transparency; some refuse to pay for AI-done work (TRI-LEGALWEEK-2026).
- 2026-02: KPMG reportedly secures a 14% fee reduction from its auditor by citing AI (YAHOO-KPMG-2026).
- 2026-08-23: Stanford framework says AI tends to push consulting firms toward hybrid and asset-based pricing (STANFORD-DEL-2026).
- 2026-09-04: ILTACON 2026 hallway discussion of seat-based to consumption-based AI pricing; vendors reluctant to discuss it (EDISCOVERYTODAY-ILTACON-2026).
- 2026-09-17: BigHand: 63% of firms rely on habitual pricing approaches; no dominant approach to AI savings (BIGHAND-LF-2026).
- 2026-10-13: Laurel and Legora announce automatic time capture and phase-two AI-value measures (LEGORA-LAUREL-2026).
- 2026-10-19: Defense-side column argues hourly billing leaves insurance-defense firms exposed to contingency-fee plaintiffs' firms that gain from AI (ATL-DEFENSE-2026).
- Scheduled: Thomson Reuters Institute's 25th Law Firm COO & CFO Forum is listed for 21-22 October 2026 (from the landscape's TRI events list; not opened); I did not use it as evidence.

**Workforce and role effects**
- Pricing professionals gain visibility and move toward a commercial, product-style, client-facing role; some firms hired more pricing staff (TRI-PRICINGPROS-2024).
- Partner incentives: PwC reportedly ties senior staff bonuses to revenue and margin per professional, not hours (RESULTSENSE-PWC-2026, secondary). Wipfli adds client satisfaction and cycle time as metrics (BLAW-ACCT-2026).
- Firm compensation, origination credit and write-off policy must change if non-hourly pricing is to work (MONDAQ-GGI-2026).
- Under AFAs, work goes to the most efficient resource, which can limit junior training (ILTA-PULSE-2025). Routed to talent-learning.
- Skills: scoping, articulating value, and negotiating are learnable but need deliberate investment (MONDAQ-GGI-2026).

**Objections and concerns practitioners raise**
- The billable hour is 'the worst system except for all the others' and clients still pay it, so firms lack an incentive to change (Cohen, in TRI-ILTACON-2025).
- Outcome pricing needs attribution that many engagements cannot support (STANFORD-DEL-2026).
- McKinsey's leader says outcome pricing predates AI (BI-MCKINSEY-2025).
- Disagreement on whether fees should fall if AI improves quality (MYCPE-KPMG-2026 summary).
- AI-driven rate increases may be a bubble risk: firms using AI mainly to justify higher rates are more exposed if clients push back (TRI-SOTLM-2026).
- Defense firms bound by carrier rate controls cannot offset lost hours (ATL-DEFENSE-2026).
- Clients and firms disagree over who keeps the dividend; a client general counsel argues the firm should earn a higher effective margin on high-value work (BLAW-ROBB-2026).

**Interview probes for an advisor**
1. When AI cuts the effort on a repeatable engagement, who keeps the saving today, and who decided that? What does the client see?
2. How do you estimate effort now: past matters, templates or judgment? When did you last update the staffing assumptions for AI?
3. What matter-level data do you hold (cost, hours by phase, outcomes) and could a client or a tool use it to propose a baseline price?
4. Which pricing models do you use for which work, and how are partner pay and origination credit tied to them? What would block a move away from hours?
5. If you offered a subscription, packaged or outcome-linked option, how would you know the attribution is clean enough and who would own the downside?

## 4. Routed to other modules

- **firm-finance:** rate and realization strategy and AI ROI (TRI-RATES-2025: collected revenue between $553 and $580 an hour across three rate configurations; TRI-LFFI-Q1-2026; TRI-SOTLM-2026 AI-bubble warning and TRI-SOTLM-VALUE-2026 on pricing power); private equity and outside capital (Crowe, a Freshfields AI-unit spinoff report in ATL, 2026-10-19); AI vendor seat versus consumption pricing as a cost line.
- **billing-collections:** time capture to cash (Laurel-Legora), write-down reduction (a TRI-AIBIZ-2025 claim that the average partner loses roughly 300 hours a year to corrections and catch-up), AI line items on invoices.
- **pursuit-proposals / client-development:** RFP pricing analytics, partner discomfort discussing AI with clients (35%, BIGHAND-LF-2026), reverse-auction win rates (TRI-ILTACON-2025), Narrative's RFP response claims.
- **staffing-resourcing:** outcome data in staffing decisions and hybrid human-agent teams (KANTATA-RMI-2026: 52.7% not equipped to manage hybrid teams; 7.3% have outcome data routinely in staffing decisions).
- **talent-learning:** junior training under AFAs (ILTA-PULSE-2025); TR-FOP-2026 tax versus legal pipeline expectations.
- **quality-review / acceptance-risk:** supervision duties for agentic AI in the California guidance; AI error incidents.

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives | Stanford Digital Economy Lab | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative AI in the Practice of Law | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026 (PDF created 2026-05-15 per metadata) | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026 | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-ILTACON-2025 | ILTACON 2025: Pricing the future | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2025-billable-hour | 2025-09-02 | full |
| ILTA-PULSE-2025 | Bill(AI)ble Hour | ILTA | professional-body | https://iltanet.org/resources/publications/pulse/iltacon/2025/billaible-hour | 2025 (page undated) | full |
| EDISCOVERYTODAY-ILTACON-2026 | My Five ILTACON 2026 Takeaways | eDiscovery Today | press | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 | full |
| TRI-COOCFO-2025 | Law Firm COO & CFO Forum: As legal market shifts, the big questions still need answers | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/coo-cfo-forum-shifting-legal-market | 2025-10-24 | full |
| TRI-KOPKA-2026 | How one law firm is challenging a broken status quo around billing | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing | 2026-04-30 | full |
| TRI-INTERDEP-2026 | Interdependent by design | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/needed-ai-conversation | 2026-06-11 | full |
| TRI-CHARGING-2026 | If AI can do the work, then what are you actually charging for? | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/what-are-you-actually-charging-for | 2026-10-02 | full |
| TRI-ALTPRICING-2025 | From hours to outcomes: alternative pricing models and tax firm profitability | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/alternative-pricing-models | 2025-09-25 | full |
| TRI-AIBIZ-2025 | How AI is continuing to change the business of law | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/ai-business-of-law | 2025-08-20 | full |
| TRI-LEADFOLLOW-2025 | Pricing AI-driven legal services: Lead or follow | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/pricing-ai-driven-legal-services-lead-or-follow | 2025-01-30 | full |
| TRI-PRICINGPROS-2024 | Pricing legal technology and the impact on the role of the pricing professional | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/legal-technology-pricing-professionals-changing-roles | 2024-11-19 | full |
| TRI-ABA512-2025 | Is ABA Formal Opinion 512 off the mark? | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/aba-formal-opinion-512 | 2025-04-02 | full |
| TRI-RATES-2025 | Law Firm Rates Report 2026 analysis: What kind of jet engine is your firm? | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/law-firm-rates-report-2026-analysis-jet-engines | 2025-11-05 | full |
| TRI-LFFI-Q1-2026 | Q1 2026 LFFI analysis | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output | 2026-05-13 | full |
| TRI-SOTLM-2026 | State of the US Legal Market 2026 analysis: Will the AI bubble burst? | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 | full |
| TRI-SOTLM-VALUE-2026 | State of the US Legal Market 2026 analysis: How law firms can turn value into pricing power | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/state-of-the-us-legal-market-2026-analysis-value-pricing-power | 2026-01-26 | full |
| TR-FOP-2026 | Future of Professionals Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 (page undated; fieldwork Mar-Apr 2026) | full |
| ACCEVERLAW-BL-2025 | AI Does Little to Reduce Law Firm Billable Hours, Survey Shows | Bloomberg Law (ACC/Everlaw survey) | survey | https://news.bgov.com/business-and-practice/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows | 2025-10-14 | full |
| BIGHAND-LF-2026 | AI is changing legal delivery, but 63% of firms default to standard rates or past matter pricing | Legal Futures (BigHand research) | survey | https://www.legalfutures.co.uk/associate-news/ai-is-changing-legal-delivery-but-63-of-firms-default-to-standard-rates-or-past-matter-pricing-bighand-research-finds | 2026-09-17 | full |
| BLAW-ROBB-2026 | The Billable Hour Isn't Dead Yet, But AI Should Reshape Pricing | Bloomberg Law (op-ed, general counsel) | community | https://news.bgov.com/business-and-practice/the-billable-hour-isnt-dead-yet-but-ai-should-reshape-pricing | 2026-06-29 | full |
| LEGALIO-AFA-2025 | AI Adoption Pushes Law Firms Toward Alternative Fees, But Change Will Be Incremental | Legal.io | press | https://www.legal.io/articles/5771590/AI-Adoption-Pushes-Law-Firms-Toward-Alternative-Fees-But-Change-Will-Be-Incremental | 2025-12-23 | full |
| BLAW-ACCT-2026 | AI Efficiency Gains Push Accounting Firms to Reimagine Pricing | Bloomberg Tax | press | https://news.bgov.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing | 2026-03-05 | full |
| MONDAQ-GGI-2026 | Still Selling Judgment | GGI Global Alliance via Mondaq | press | https://www.mondaq.com/unitedstates/management/1814268/still-selling-judgment-how-law-firms-and-accounting-firms-must-prepare-for-ai-driven-pricing-change | 2026-07-09 | full |
| BAKER-PODCAST-2026 | How AI Will Kill the Billable Hour in CPA Firms (Ron Baker) | Growing Your Firm podcast, via Podwise summary | podcast | https://podwise.ai/episodes/8845213 | 2026-09-06 | full (summary page only) |
| ABA-BLS-PODCAST-2025 | The Billable Hour has Met Its Match in AI | ABA Business Law Section podcast (Fischer; Rapoport; Tiano) | podcast | https://www.americanbar.org/groups/business_law/resources/podcast/ai-vs-the-billable-hour/ | 2025-05-19 | full (episode description only, via mirror; audio not heard) |
| ATL-DEFENSE-2026 | The Defense Bar In The Age Of AI: Running A Red Queen's Race? | Above the Law | press | https://abovethelaw.com/2026/10/the-defense-bar-in-the-age-of-ai-running-a-red-queens-race/ | 2026-10-19 | full |
| ATL-LITERA-2026 | Avoiding The AI Efficiency Trap | Above the Law / Litera (sponsored promotion) | vendor | https://abovethelaw.com/2026/08/avoiding-the-ai-efficiency-trap-what-biglaw-needs-to-get-right/ | 2026-08-18 | full |
| PWC-ONE-2026 | PwC Introduces PwC One | PwC US | firm | https://www.pwc.com/us/en/about-us/newsroom/press-releases/pwc-one.html | 2026-03-19 | full (via mirror) |
| ACCTODAY-PWC-2026 | PwC CEO: You cannot opt out of AI | Accounting Today | press | https://www.accountingtoday.com/news/pwc-ceo-you-cannot-opt-out-of-ai | 2026-03-20 | full |
| CPAPA-PWC-2026 | PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/ | 2026-03-25 | full |
| RESULTSENSE-PWC-2026 | PwC Warns Partners: Adopt AI or Face Exit | Resultsense | press | https://www.resultsense.com/news/2026-03-19-pwc-ai-overhaul-partners-resist-technology/ | 2026-03-19 | full |
| RESULTSENSE-2026 | AI threatens Big Four scale advantage as UK boutiques attack | Resultsense | press | https://www.resultsense.com/news/2026-05-28-ai-consulting-big-four-reckoning/ | 2026-05-28 | full |
| BI-MCKINSEY-2025 | AI is reshaping how McKinsey makes money | Business Insider via Yahoo Finance | press | https://finance.yahoo.com/news/ai-reshaping-mckinsey-makes-money-195132745.html | 2025-11-17 | full |
| AIWEEKLY-MCK-2025 | McKinsey Ties 25% of Fees to Outcomes as AI Erodes Billable Hours | AI Weekly | press | https://aiweekly.co/alerts/mckinsey-ties-25-of-fees-to-outcomes-as-ai-erodes-billable-hours | 2026-06-29 (landscape said late 2025) | full |
| FORRESTER-BLOG-2025 | The Future Of AI Consulting Services Is Disruptively Bright | Forrester | press | https://www.forrester.com/blogs/the-future-of-ai-consulting-services-is-disruptively-bright | 2025-09-15 | full |
| FORRESTER-SOTS-2026 | The State Of Technology Services, 2026 | Forrester | survey | https://www.forrester.com/report/the-state-of-technology-services-2026/RES192217 | 2026-02-24 | full (abstract page only; report paywalled) |
| SPI-AI-2026 | 2026 AI in Professional Services Survey | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-07-14 | full (sales page; report paid) |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads | Kantata (Resource Management Institute study) | vendor | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 | full |
| CERTINIA-VEDA-2026 | Certinia AI solutions (Veda agents) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10-19 (accessed; undated) | full |
| AYORA-LTH-2026 | Ayora by BigHand | Legaltech Hub | vendor | https://www.legaltechnologyhub.com/vendors/ayora-by-bighand/ | 2026-10-19 (accessed; undated) | full |
| NARRATIVE-ILTA-2026 | Narrative | ILTA Startup 2026 profile | vendor | https://www.iltanet.org/resources/publications/pulse/startup26/narrative | 2026-10-19 (accessed; undated) | full |
| LEGORA-LAUREL-2026 | Legora and Laurel partner to capture the time lawyers spend in Legora | Legora | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 | full |
| YAHOO-KPMG-2026 | Big Four accounting firm's bold demand is a warning about AI adoption | Yahoo Finance | press | https://finance.yahoo.com/news/big-four-accounting-firms-bold-015348056.html | 2026-02-10 | full |
| ONLYCFO-KPMG-2026 | AI is Coming for Audit Fees: KPMG Just Proved It | OnlyCFO newsletter | community | https://www.onlycfo.io/p/ai-is-coming-for-audit-fees-kpmg | 2026-02-13 | full |
| MYCPE-KPMG-2026 | How a Big Four audit fee cut raises a bigger AI question | MYCPE ONE Insights | press | https://my-cpe.com/insights/news-and-insights/accounting-and-taxes/how-a-big-four-audit-fee-cut-raises-a-bigger-ai-question | 2026-02-09 | full (opening summary; body paywalled) |

Source mix (48 distinct sources read, 40 of them cited in the use cases): press 23, survey 8, vendor 6, conference 3, community 2 (a general-counsel op-ed and a finance newsletter), podcast 2, academic 1, regulator 1, professional-body 1, firm 1. Sources read for notes and routing but not cited in a use case: TRI-COOCFO-2025, TRI-RATES-2025, TRI-LFFI-Q1-2026, TRI-SOTLM-2026, TRI-SOTLM-VALUE-2026, RESULTSENSE-2026, FORRESTER-SOTS-2026, ABA-BLS-PODCAST-2025.

Notes on three of these: TRI-COOCFO-2025 (24th Law Firm COO & CFO Forum, 24 October 2025) reports a panelist saying firms must have an implementation strategy for pricing because clients are already thinking about it, and that realization and expenses were moving slowly in the wrong direction. ABA-BLS-PODCAST-2025 (19 May 2025) is an episode on hybrid billing drawing on Rapoport and Tiano's interviews with law firms; only the episode description was read. RESULTSENSE-2026 reports (secondary, from the FT and City AM) that AI-native UK boutique Queen's Tower Advisory is targeting teams that are '20 per cent humans, 80 per cent AI agents' and that clients are increasingly demanding outcome-linked pricing; I treat this as a frontier signal, not an outcome.

## 6. Gaps

- **No quality evidence.** I found no error rates, override rates, parallel runs or independent measurement for AI-assisted estimating, scoping or fee proposals. All productivity figures on estimating are vendor claims without named customers (Certinia, Narrative). Firm-published pricing outcomes attributable to AI: none found.
- **Primary documents not reached:** the Financial Times and Wall Street Journal originals (paywalled; PwC, KPMG-Grant Thornton and McKinsey claims are secondary); McKinsey's own pages (the landscape reports 403); ABA Formal Opinion 512 and the AICPA pricing survey (cited only through secondary quotation); Forrester Wave Q2 2026 and State of Technology Services full text (abstract only); SPI report body (paid; page figures partly masked); the Rapoport/Tiano paper (SSRN blocked); Aderant Virtual Pricing Director and the Clio Legal Trends hub (403); Legal Evolution (403 to curl).
- **Kantata 'Fact or fiction: is outcome-based pricing for services firms a reality?'** is listed on Kantata's press page, but the link returned 404 and I did not find another copy.
- **Conferences:** no session content for CLOC, AICPA ENGAGE, MCA, PMI or Legal Geek pricing tracks was reachable. ILTACON 2026 pricing sessions: no recap found beyond one hallway note; the Litera/ATL webinar of 9 September 2026 has only a promotion. TRI's Law Firm COO & CFO Forum of 21-22 October 2026 had not yet occurred as of this run.
- **Podcasts:** I could read only episode summaries (Ron Baker, ABA Business Law); no transcripts. I did not find a legal-pricing podcast episode dated 2026 with a named pricing director.
- **In-house and shared-service examples:** only legal in-house (GSK at Legalweek, an ACC/Everlaw survey, a general counsel op-ed); no shared-service or global business services pricing practice outside legal.
- **Consulting beyond McKinsey and PwC:** no primary pricing statements from BCG, Bain, Deloitte, EY, KPMG or Accenture; the EY remark in the Business Insider article is undated by year.
- **Architecture and engineering, and PSA-based project firms:** no practitioner discourse on AI and scoping/pricing found beyond Certinia and Kantata marketing.
- **Conflicts to resolve if used:** McKinsey outcome share (25% versus 20% in the same article; 'about a third' in a secondary report); the 22% figure in TRI-LEGALWEEK-2026 versus TR-FOP-2026; KPMG entity in the Grant Thornton story; AIWEEKLY-MCK-2025 date (2026-06-29 on the page, 'late 2025' in the landscape).
