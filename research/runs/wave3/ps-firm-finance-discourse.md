# Firm finance and performance: discourse angle (professional-services)

## 1. Summary

**Angle:** what practitioners said about firm-level finance and AI over roughly the last 12-18 months (conference recaps, trade press, podcasts, practitioner and academic essays, recruiter postings). Prepared 2026-10-19. 22 candidate use cases; **no entry reaches grade A** because no named firm publishes a measured financial result from AI in this module.

**What the field is saying**

- **Prosperity now, unproven return.** Law-firm financial data are strong (worked rates +7.1% in Q2 2026; technology and knowledge-management spend +11.6% in Q2 2026), but TRI says most of the 2025 profit growth came from rate rises rather than operational improvement, and the Q1 2026 index stayed flat at 55 despite near-record inputs (TRI-SOTLM-2026; TRI-LFFI-COSTS-2026; TRI-LFFI-Q1-2026). At Legalweek, firm leaders said they were "still gathering the data" on AI savings (TRI-LEGALWEEK-2026).
- **Savings are being banked as margin, and clients are noticing.** An in-house columnist wrote that firms are banking AI productivity as margin (BLOOMBERGLAW-GCXAI-2026). TRI's 2026 survey: 68% of corporate legal professionals do not know whether their outside firms use AI, and most firms and departments collect no AI ROI data or are unsure (TRI-GREATDISCONNECT-2026).
- **The billable hour is not dead, but the pricing conversation moved.** Panelists at Legalweek and ILTACON, and accounting leaders at RSM, PwC and KPMG, discuss value, hybrid and outcome pricing; the firms reporting actual use are mostly small or mid-sized (MahoneySabol, Kopka Law, RKL), RSM, PwC and KPMG describe exploring it, and McKinsey's disclosed outcome-fee share is relayed second-hand in a Stanford paper (HBJ-BILLABLE-2026; TRI-KOPKA-2026; STANFORD-DEL-2026).
- **AI cost is turning variable.** ILTACON 2026 practitioners talked about "tokenomics", premium-model overuse and a norm of about 1% of revenue; vendors are moving agent products to consumption billing, which raises the unresolved question of overhead versus client expense (TRI-ILTACON-METER-2026; ISBA-ELEFANT-2026; RADIANT-TOKEN-2026).
- **Outside capital is being justified partly by AI spend.** Crowe took KKR capital for talent, technology and innovation; law firms are exploring MSO structures, with academics warning that governance is not ready (AT-CROWE-2026; COLUMBIA-BREYDO-2026).

**Evidence grades:** 12 B, 4 C, 6 D, 0 A. **Source count:** 53 distinct sources listed, all opened except one search-only item, a paywalled standfirst (see Sources).

## 2. Use cases

```yaml
- id: professional-services-firm-finance-01
  title: AI usage threshold as the gate for converting pilots into firm licences
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Lawyers testing AI tools do so on top of billable work, and few legal teams can show a reliable return on AI spend, so licences risk becoming unused ("shelfware").
  solution: Run pilots on real matters with the firm's document management system connected, and use weekly active use of the tool as a go/no-go signal when ROI cannot yet be calculated. Holland & Hart describes a threshold of more than 70% weekly active users for a trial.
  outcomes:
  - lever: cost
    description: Used as a purchase test to avoid buying unused licences
    figure: more than 70% weekly active users (a trial threshold the firm uses, not a measured result)
    measures: share of trial users active in a given week; the article gives no result for any named tool
    provenance: self-reported
    source_ref: TRI-ILTACON-IMPL-2026
  prerequisites:
  - A pilot long enough and on real matters (a Holland & Hart speaker said a trial that asks lawyers to work unpaid cannot be done in under eight weeks)
  - Document management system integration so the trial uses firm documents
  - A shared definition of the outcome the tool is meant to achieve before evaluation
  risks_and_guardrails:
  - Usage is an adoption signal, not a return signal; the same panel reported that no attendee (audience of 50+) said their team had a strong AI ROI measure
  - Trial time is taken from billable work, which has a cost the firm has to accept
  human_checkpoints:
  - Innovation or technology lead decides to buy, extend or stop based on trial usage
  - Business owner confirms the goal the tool serves
  role_evolution: Enterprise applications and innovation staff become owners of adoption metrics; early-access 'champions' are used to build buy-in.
  evidence_grade: B
  sources:
  - ref: TRI-ILTACON-IMPL-2026
    title: 'ILTACON 2026: "Does it make the boat faster?" How legal teams are finding AI implementation success'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-finding-ai-implementation-success
    date: '2026-08-31'
    access: full
    locator: sections 'Metrics that matter' and 'Meet them where they are'
  last_reviewed: '2026-10-19'
  notes: Adoption measure only. Adjacent to the ROI question; no firm in the source reports a financial return from AI. Panel speaker is from Holland & Hart (550 attorneys, eight practice groups per the article).
- id: professional-services-firm-finance-02
  title: 'Hourly matters: bill actual time with AI savings passed to the client, and redirect recovered time'
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - document-production
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: personal-assistant
  maturity: in-production
  problem: Large corporate clients ask how firms use AI to lower the cost of work and what firms do with the saved time; hourly billing penalises efficiency.
  solution: Norton Rose Fulbright says that on hourly matters it bills the hours actually worked, not what the work might have taken without AI, and expects lawyers to redirect recovered time to higher-value work on the same matter or to other client matters. Its lawyers have access to Harvey, Legora and Microsoft Copilot, with about 1,000 licences.
  outcomes:
  - lever: risk
    description: Billing policy that follows the time actually spent
    figure: none published (about 1,000 AI licences; two-thirds of lawyers use the tools regularly, per the firm)
    measures: licences held by the firm; share of lawyers who 'touch tech regularly' as reported by the firm's officials by email
    provenance: self-reported
    source_ref: BLOOMBERGLAW-TEXAS-2026
  prerequisites:
  - Time records that show the real time spent
  - A client-value or pricing lead who sets the policy (Norton Rose names a chief client value and innovation officer)
  - A plan for where recovered time is redeployed
  risks_and_guardrails:
  - The article notes it is unclear whether any large clients are seeing smaller bills
  - Bloomberg Law reports the State Bar of Texas ethics committee said lawyers cannot charge for time saved by using generative AI
  human_checkpoints:
  - Billing partner reviews the pre-bill against time actually worked
  - Practice leaders decide where recovered time goes
  role_evolution: Lawyers are expected to turn recovered time into other billable or higher-value work rather than into shorter bills alone.
  evidence_grade: B
  sources:
  - ref: BLOOMBERGLAW-TEXAS-2026
    title: AI, Billing Emerge as Crossroads for Texas Law Firms and Clients
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/antitrust/ai-billing-emerge-as-crossroads-for-texas-law-firms-and-clients
    date: '2026-04-21'
    access: full
    locator: paragraphs on Norton Rose Fulbright statements (Shishima and Bentz) and on the Texas bar ethics opinion
  last_reviewed: '2026-10-19'
  notes: 'Firm statement by email to Bloomberg Law; no published measure of savings or of fee outcomes. Pairs with use case 12 (capacity capture). Pattern ''other'': a billing-policy decision applied at pre-bill review, not a document pipeline.'
- id: professional-services-firm-finance-03
  title: Value-based or premium pricing for AI-assisted accounting and tax work
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - expert-judgment
  - document-production
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: personal-assistant
  maturity: piloting
  problem: Hourly pricing under-rewards work that AI compresses; firm leaders ask whether time saved is margin for the firm or a price cut for the client.
  solution: MahoneySabol (a 70-person CPA firm) began charging a premium billing rate in early 2026 for work done with AI-powered research systems. RSM US says it uses multiple pricing models and increasingly works with clients to bill on value. RKL LLP has onboarded several dozen new clients under an alternative, value-based pricing model created with Fore LLC. PwC's US Tax Leader and KPMG's US Vice Chair of Advisory both say publicly that value or outcome pricing matters as AI changes the work.
  outcomes:
  - lever: growth
    description: Premium rate for AI-assisted research; research tasks reported at 15 minutes instead of 90
    figure: 90 minutes to 15 minutes (research tasks, per co-founder); premium rate level not stated
    measures: time for a research task before and after AI tools, as stated by the firm's co-founder
    provenance: self-reported
    source_ref: HBJ-BILLABLE-2026
  - lever: growth
    description: RKL pilot of value-based pricing
    figure: several dozen new clients onboarded under the model
    measures: clients onboarded under the alternative pricing model during RKL's pilot, per an RKL partner
    provenance: self-reported
    source_ref: BLOOMBERGLAW-ACCTG-2026
  prerequisites:
  - Matter or engagement cost data, so a fixed or value price is known to be profitable
  - Training for staff in scoping and value conversations
  - Internal incentives that do not reward hours alone (see use case 17)
  risks_and_guardrails:
  - Clients may not accept a price that does not fall with effort; RSM says it can cut prices in some areas but not others
  - The AICPA 2025 survey (via Bloomberg Law) recommended firms consider accelerating a shift away from hourly billing; median net hourly rate rose nearly 7% over two years to $170
  human_checkpoints:
  - Partner sets the price for the engagement and signs the value case
  - Client agrees the scope and the value measure
  role_evolution: Accountants shift from selling time to selling judgment and proactive advice; pricing and client-advisory roles gain weight.
  evidence_grade: B
  sources:
  - ref: HBJ-BILLABLE-2026
    title: AI-driven efficiencies force law, accounting firms to rethink the billable hour
    publisher: Hartford Business Journal
    type: press
    url: https://hartfordbusiness.com/article/ai-driven-efficiencies-force-law-accounting-firms-to-rethink-the-billable-hour/
    date: '2026-06-01'
    access: full
    locator: paragraphs on MahoneySabol (Michael Sabol) and Whittlesey
  - ref: BLOOMBERGLAW-ACCTG-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/esg/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: sections 'Pricing Dilemma' and 'New Pricing Options'
  - ref: TRI-CHARGING-2026
    title: If AI can do the work, then what are you actually charging for?
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/what-are-you-actually-charging-for
    date: '2026-10-02'
    access: full
    locator: section 'Compliance work is commoditizing' (78% hourly; 61% vs 54% value-pricing use)
  last_reviewed: '2026-10-19'
  notes: 'TRI-CHARGING-2026 (tax, audit and accounting firms): hourly billing is the dominant model for 78% of firms; the highest-margin firms use value-based pricing 61% of the time versus 54% for the lowest-margin tier (TRI 2026 State of Tax Professionals Report, as summarised; denominators not given in the article). Self-reported by firms; no independent measure of margin effect of AI-specific pricing. Pattern ''other'': a pricing decision for work that AI has shortened.'
- id: professional-services-firm-finance-04
  title: KPI-based billing arrangement in place of hourly billing (insurance defense litigation)
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: workflow-automation
  maturity: in-production
  problem: Hourly billing penalises a firm that finishes sooner with AI, and insurer clients review and cut bills, so both sides carry heavy billing administration.
  solution: Kopka Law uses monthly-retainer or portfolio-based alternative billing arrangements measured against key performance indicators (cycle time and case disposition, early evaluation and communication, indemnity outcomes relative to injury type, strategic collaboration). The firm argues that clients already hold frequency and severity data to price this way, and says many insurance clients refuse to pay for AI or software costs while expecting the efficiency.
  outcomes:
  - lever: cost
    description: none published
    figure: none
    measures: not applicable
    provenance: self-reported
    source_ref: TRI-KOPKA-2026
  prerequisites:
  - Client data on frequency and severity, and the firm's own data on litigation categories
  - A client willing to negotiate a portfolio arrangement
  - Agreed KPIs
  risks_and_guardrails:
  - Source is the firm's own account in a Thomson Reuters Institute feature; no outcome figures
  - Firm itself says conventional AFAs designed only to save clients money tend to fail
  human_checkpoints:
  - Client and firm agree the KPI set and review it
  - Firm leadership monitors whether the arrangement is profitable
  role_evolution: Billing staff and appeal teams shrink in importance; lawyers are judged on KPIs rather than time entries.
  evidence_grade: B
  sources:
  - ref: TRI-KOPKA-2026
    title: How one law firm is challenging a broken status quo around billing
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing
    date: '2026-04-30'
    access: full
    locator: sections 'Why the billable hour hates AI' and 'Data as the solution'
  last_reviewed: '2026-10-19'
  notes: 'AI link is argued rather than measured. Routed in part to scoping-pricing (matter-level fee design). Pattern ''other'': a contract and pricing redesign measured on client KPIs.'
- id: professional-services-firm-finance-05
  title: Outcome-based and hybrid pricing at consulting firms as AI shortens the work
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - expert-judgment
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: When AI augments consultants internally, hours become a weaker proxy for effort and clients see only the deliverable, so time-and-materials pricing loses its footing.
  solution: 'Consulting firms move toward hybrid structures: a base fee with outcome-linked components, and subscription or usage components where AI agents run in client environments. The Stanford paper reports McKinsey said in November 2025 that roughly a quarter of its global fees come from outcome-based pricing, and PwC''s US Tax Leader said "time''s becoming less and less of relevance". PwC US also launched PwC One, offering six automated services.'
  outcomes:
  - lever: growth
    description: Share of fees from outcome-based pricing at McKinsey
    figure: roughly a quarter of global fees
    measures: share of McKinsey's global fees from outcome-based pricing, as disclosed by McKinsey and reported second-hand in the Stanford paper citing a 2025 press report; landscape records a conflicting 'about a third' (secondary)
    provenance: self-reported
    source_ref: STANFORD-DEL-2026
  prerequisites:
  - Measurement infrastructure before outcome pricing (telemetry, agreed ground-truth metrics, third-party verification)
  - Credible attribution of the result to the firm's work
  - Matter-level cost tracking including AI cost
  risks_and_guardrails:
  - The paper says attribution risk caps outcome pricing and that hybrid pricing is the expected destination where the firm's contribution is confounded with the client's other initiatives
  - The authors say their evidence is qualitative and consistent with, not a confirmation of, the framework; the Lab has received a general gift from Accenture
  human_checkpoints:
  - Engagement partner and client agree the outcome definition and fee split
  - Firm finance approves risk-bearing fee structures
  role_evolution: Leaders need a pricing competence for hybrid contracts; consultants spend less effort on hour recording and more on proving results.
  evidence_grade: B
  sources:
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson, Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section 5.1 (McKinsey and PwC examples) and Section 7 (decision rules)
  - ref: CPAPA-PWC-2026
    title: PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
    date: '2026-03-25'
    access: full
    locator: paragraphs on PwC One and subscription services
  - ref: BLOOMBERGLAW-ACCTG-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/esg/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: opening and 'Pricing Dilemma' (PwC tax leader quote)
  last_reviewed: '2026-10-19'
  notes: 'McKinsey figure is second-hand (not read at McKinsey source). Grade B and not A because the figure is a disclosure relayed by a paper, not a study. Overlaps scoping-pricing at deal level; here the firm-level mix of fees is what matters. Pattern ''other'': a firm-level pricing-mix decision.'
- id: professional-services-firm-finance-06
  title: Productised AI subscription built from the firm's own know-how
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - document-production
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: automate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: Hourly advice on recurring client questions is repetitive for partners, and clients want direct access to the firm's accumulated work.
  solution: Debevoise built a client-facing AI portal (STAAR, built on the Legora platform) trained on its AI-risk work, sold by subscription to a limited number of clients at $150,000 a year, in beta through year end with about 10 clients including Blackstone, Capital One, Evercore, GSK and New York Life. PwC launched PwC One, an AI platform giving clients access to six automated services with more promised.
  outcomes:
  - lever: growth
    description: Subscription revenue line from firm knowledge
    figure: $150,000 a year per subscription (beta, about 10 clients)
    measures: annual subscription price quoted by Debevoise for the STAAR beta; number of clients is from the article
    provenance: self-reported
    source_ref: BLOOMBERGLAW-DEBEVOISE-2026
  prerequisites:
  - Partners willing to contribute documents (the article ties this to Debevoise's lockstep culture)
  - Client consent to use anonymised documents
  - Knowledge management capacity to keep content current (the partner calls himself the gatekeeper and says it takes a lot of time)
  risks_and_guardrails:
  - Licence terms and security testing were still to be worked out at the time of the article
  - Content currency and accuracy depend on continuing partner effort
  human_checkpoints:
  - Partner approves what enters the portal
  - Client questions that fall outside the portal still go to lawyers, billed hourly
  role_evolution: Partners become curators of firm knowledge; a 'software play' inside a law firm calls for new hires; the presiding partner floated, as a theory, that partners may find it harder to move between firms.
  evidence_grade: B
  sources:
  - ref: BLOOMBERGLAW-DEBEVOISE-2026
    title: Debevoise Banks on Partner Loyalty to Build Curated AI Products
    publisher: Bloomberg Law (Big Law Business, Roy Strom)
    type: press
    url: https://news.bloomberglaw.com/business-and-practice/debevoise-banks-on-partner-loyalty-to-build-curated-ai-products
    date: '2026-08-06'
    access: full
    locator: paragraphs on STAAR subscription, beta clients, licence and KM caveats
  - ref: CPAPA-PWC-2026
    title: PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
    date: '2026-03-25'
    access: full
    locator: paragraph on PwC One
  - ref: AT-PWC-2026
    title: PwC grows 2026 global revenue to $60.2B
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/pwc-grows-2026-global-revenue-to-60-2b
    date: '2026-10-19'
    access: full
    locator: paragraph on PwC One initial rollout
  last_reviewed: '2026-10-19'
  notes: Beta; no usage or revenue result reported. Routed to knowledge-management for the content-maintenance burden.
- id: professional-services-firm-finance-07
  title: Automatic time capture from AI platform work, with AI usage and value measures
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - document-production
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Timekeeping is unbillable work, entries are often rebuilt from memory, short tasks are missed, and firm leaders cannot see what return AI work produces.
  solution: Laurel will turn each task completed in Legora into a time entry with client, matter and narrative for lawyer review; a second phase is planned to measure Legora usage and the value of AI-powered work, with measures to be chosen in consultation with customers.
  outcomes:
  - lever: growth
    description: Fewer unrecorded short tasks (claim)
    figure: none published
    measures: not applicable; the release makes no quantified claim
    provenance: vendor-published
    source_ref: LEGORA-LAUREL-2026
  prerequisites:
  - Both platforms in use at the firm
  - Matter and client mapping so entries land on the right matter
  - Lawyers review entries before submission
  risks_and_guardrails:
  - Vendor announcement; availability details to follow; the AI value measures are still to be defined
  - Time entries generated from AI tasks may make AI-assisted effort visible to clients and feed client scrutiny of bills (see use case 21)
  human_checkpoints:
  - Lawyer reviews and submits each generated entry
  role_evolution: Less time spent reconstructing timesheets; firm leaders get usage data by lawyer and matter.
  evidence_grade: C
  sources:
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora (press release)
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: paragraphs on phase one and phase two
  - ref: ARTLAW-LEGORA-2026
    title: Legora Seeks 'Centrality' With 30+ Integrations Ecosystem
    publisher: Artificial Lawyer
    type: press
    url: https://www.artificiallawyer.com/2026/10/15/legora-seeks-centrality-with-30-integrations-ecosystem/
    date: '2026-10-15'
    access: full
    locator: '''Time and billing'' item in the integrations list'
  last_reviewed: '2026-10-19'
  notes: Date taken from the landscape and LawNext listing; the opened page body carries no date. Routed to billing-collections (time capture to cash); the AI-value measurement phase is the firm-finance link.
- id: professional-services-firm-finance-08
  title: Metering, budgeting and model-tier guidance for AI token consumption
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: Per-seat AI budgets are giving way to usage-based bills; lawyers choose the largest model for trivial tasks, and agents can spend tokens unobserved.
  solution: Firms read consumption bills, train users to pick the right model and prompt economically, and ask whether each agent removes specific line items or saves specific money. Practitioners at ILTACON 2026 described reading a consumption bill (Littler), lawyers reaching for premium models for small tasks (Barnes & Thornburg), hidden agent-to-agent spend and multiple tool stacks after acquisitions (Lawfront Group, a PE-backed UK consolidator), and an emerging budget norm of about 1% of revenue (Ogletree Deakins).
  outcomes:
  - lever: cost
    description: Emerging norm for AI spend
    figure: roughly 1% of revenue (stated by Ogletree Deakins's Chief Data and AI Officer as where most people are settling; his firm is not there yet)
    measures: AI spend as a share of revenue; speaker's characterisation of what 'most people' are converging on, not a surveyed figure
    provenance: self-reported
    source_ref: TRI-ILTACON-METER-2026
  prerequisites:
  - Visibility of token use per user, tool or matter
  - Training on model choice and prompting
  - An inventory of AI tools and agents (about half the room had 10 or more tools in use or under evaluation)
  risks_and_guardrails:
  - 'Anecdotes: Littler''s single PowerPoint cost $2; panelists say typical waste is hidden'
  - Spend is concentrated where vendors still subsidise tokens; NetDocuments (a vendor) says vendors currently absorb token costs under subscriptions and that this will not last long
  human_checkpoints:
  - Knowledge management or innovation lead reviews usage reports
  - Firm finance sets the AI budget line
  role_evolution: Innovation and knowledge managers take on cost management; lawyers are asked for restraint, which one speaker called harder than adoption.
  evidence_grade: B
  sources:
  - ref: TRI-ILTACON-METER-2026
    title: 'Ferraris for emails: At ILTACON 2026, the industry starts reading the meter'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter
    date: '2026-09-09'
    access: full
    locator: sections 'The receipt is not the cost', 'The $2 PowerPoint' and 'Ferraris for emails'
  - ref: NETDOCUMENTS-TOKENOMICS-2026
    title: Lawyer Tokenomics
    publisher: NetDocuments ndMAX Studio (Applied AI Team)
    type: vendor
    url: https://studio.netdocuments.com/post/lawyer-tokenomics
    date: '2026-08-12'
    access: full
    locator: sections 'Why AI Pricing Is Nothing Like Software Licensing' and 'What This Means for the P&L'
  - ref: CONSULTANCYUK-BONE-2026
    title: Faster work doesn't automatically mean a more profitable professional services firm
    publisher: Consultancy.uk (contributed by Andrew Bone, co-founder and VP of product; employer not stated in the page text)
    type: press
    url: https://www.consultancy.uk/news/45863/faster-work-doesnt-automatically-mean-a-more-profitable-professional-services-firm
    date: '2026-10-15'
    access: full
    locator: paragraph on AI cost varying with usage and being hard to attribute
  last_reviewed: '2026-10-19'
  notes: Named practitioners describe practice at conference sessions; no firm reports a deployed chargeback system. The NetDocuments piece is vendor content.
- id: professional-services-firm-finance-09
  title: 'Idea: recover metered AI costs from clients only when attributable to a matter'
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: As AI moves to metered pricing, firms must decide whether AI costs are overhead (absorbed) or client expenses (billable).
  solution: 'Practitioner guidance (not a deployment): subscriptions and platform licences are overhead; metered charges can be billed only if attributable to a single matter, at actual cost, disclosed in advance and not duplicative; the author recommends absorbing ordinary AI use as overhead and raising rates or using flat fees instead of itemising tokens. Radiant reports that clients say some AI cost is reaching what firms charge; Keypoint Law''s CEO is quoted as expecting clients to object to separate charges.'
  outcomes:
  - lever: cost
    description: none published
    figure: none
    measures: not applicable
    provenance: self-reported
    source_ref: ISBA-ELEFANT-2026
  prerequisites:
  - Per-matter cost attribution from the AI platform
  - Engagement-letter disclosure language
  risks_and_guardrails:
  - Rule 1.5 reasonableness and overhead-versus-expense treatment under ABA Formal Opinion 93-379, as discussed in the source
  - The opinion records exceptions (North Carolina permits an administrative fee; a New York task force would allow a surcharge if stated in the engagement letter)
  human_checkpoints:
  - Billing partner approves any pass-through and its disclosure
  role_evolution: Billing and ethics staff add AI cost classification to their work.
  evidence_grade: D
  sources:
  - ref: ISBA-ELEFANT-2026
    title: The One About Passing AI Costs Through to Clients (MyShingle Ethics Opinion, Carolyn Elefant), Rural Practice newsletter
    publisher: Illinois State Bar Association
    type: professional-body
    url: https://www.isba.org/node/104199
    date: 2026-07
    access: full
    locator: sections on overhead versus client expenses and the sample disclosure
  - ref: RADIANT-TOKEN-2026
    title: Legal has a token problem, and the industry is just starting to notice (page undated; text refers to June 2026 events)
    publisher: Radiant Law
    type: firm
    url: https://www.radiantlaw.com/resources/legal-has-a-token-problem-and-the-industry-is-just-starting-to-notice
    date: '2026'
    access: full
    locator: section 'In-house teams are caught in the squeeze'
  - ref: LAWYERSWEEKLY-KEYPOINT-2026
    title: '''Clients will get annoyed'' if firms pass on AI costs, says Keypoint''s CEO (standfirst only; premium content)'
    publisher: Lawyers Weekly
    type: press
    url: https://www.lawyersweekly.com.au/biglaw/44659-clients-will-get-annoyed-if-firms-pass-on-ai-costs-says-keypoint-s-ceo
    date: '2026-07-15'
    access: search-only
    locator: standfirst only
  last_reviewed: '2026-10-19'
  notes: 'Idea. Opinion piece by a practitioner, not a bar ruling; the Keypoint item was seen as a standfirst behind a paywall (search-only). Pattern ''other'': a cost-classification rule applied to billing.'
- id: professional-services-firm-finance-10
  title: Negotiating AI vendor contracts as seat pricing gives way to consumption pricing
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Contracts signed on flat per-seat terms in 2024-25 may not survive renewal as vendors move to consumption billing.
  solution: Firms and in-house teams benchmark actual usage against the original business case before renewal, press vendors for ROI tools and clarity on consumption terms, and weigh building in-house (Radiant cites Kirkland & Ellis's reported $500m platform spend). Legora's CEO told Bloomberg that consumption and outcome-based models will make sense for its clients, and Radiant reports Legora moving its Agent Pro product to consumption billing.
  outcomes:
  - lever: cost
    description: Vendor pricing shift
    figure: none published
    measures: not applicable
    provenance: vendor-published
    source_ref: BLOOMBERGLAW-TEXAS-2026
  prerequisites:
  - Usage data per tool and user
  - Awareness of renewal dates
  - Negotiating leverage (scale or alternatives)
  risks_and_guardrails:
  - Vendors 'didn't really have a lot of insight to share' on consumption pricing, per an ILTACON observer
  - Radiant's claims on Kirkland and Simmons & Simmons are second-hand and were not checked at source
  human_checkpoints:
  - CFO or managing partner approves AI contract terms and the AI budget
  role_evolution: Legal technology procurement and finance staff take on usage analytics.
  evidence_grade: C
  sources:
  - ref: EDISCOVERYTODAY-ILTACON-2026
    title: My Five ILTACON 2026 Takeaways
    publisher: eDiscovery Today (Doug Austin)
    type: conference
    url: https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/
    date: '2026-09-04'
    access: full
    locator: section 'Is tokengeddon looming for AI pricing?'
  - ref: RADIANT-TOKEN-2026
    title: Legal has a token problem, and the industry is just starting to notice (page undated; text refers to June 2026 events)
    publisher: Radiant Law
    type: firm
    url: https://www.radiantlaw.com/resources/legal-has-a-token-problem-and-the-industry-is-just-starting-to-notice
    date: '2026'
    access: full
    locator: sections 'The subsidy era is ending' and 'BigLaw's answer'
  - ref: BLOOMBERGLAW-TEXAS-2026
    title: AI, Billing Emerge as Crossroads for Texas Law Firms and Clients
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/antitrust/ai-billing-emerge-as-crossroads-for-texas-law-firms-and-clients
    date: '2026-04-21'
    access: full
    locator: paragraph quoting the Legora CEO
  - ref: ISBA-ELEFANT-2026
    title: The One About Passing AI Costs Through to Clients (MyShingle Ethics Opinion, Carolyn Elefant), Rural Practice newsletter
    publisher: Illinois State Bar Association
    type: professional-body
    url: https://www.isba.org/node/104199
    date: 2026-07
    access: full
    locator: paragraph noting Legora's consumption-based pricing for agentic models
  last_reviewed: '2026-10-19'
  notes: 'Vendor announcement as relayed by secondary sources; Legora''s own announcement was not found. Radiant is a law-sector services firm with its own commercial view. Pattern ''other'': a procurement and renewal negotiation.'
- id: professional-services-firm-finance-11
  title: Dedicated pricing function with margin models for AI-assisted matters
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Partners lack pricing training, clients ask how AI changes cost, and firms cannot easily model the margin of AI-assisted fixed fees.
  solution: Firms build or enlarge pricing teams that use AI and data to set rates and structure fixed, hybrid and value-based fees. Greenberg Traurig's Matthew Beekhuizen holds the title Chief Pricing and Innovation Officer. Two recruiter postings (February 2026) for unnamed global law firms describe building an AI pricing team, with duties to model margins and fee structures for GenAI-assisted matters.
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: not applicable
    provenance: self-reported
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - Matter-level cost and margin data
  - Partner willingness to take advice on structures
  - Skills in iterative, product-style pricing
  risks_and_guardrails:
  - A pricing team can look like a brake on innovation if handled badly (TRI 2024 piece)
  - Postings show intent, not results; employers are anonymous
  human_checkpoints:
  - Pricing lead and partner agree the fee structure
  - Finance reviews margin forecasts
  role_evolution: Pricing professionals become commercial and client-facing; a 2024 TRI piece reports pricing professionals saying their firms had hired additional pricing staff for this.
  evidence_grade: B
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: speaker title for Matthew Beekhuizen, Greenberg Traurig, and COO/CFO panel context
  - ref: TRI-COOCFO-AI-2025
    title: 'Law Firm COO & CFO Forum: As law firms push to offer solutions and demonstrate value, will AI get them there?'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/coo-cfo-forum-ai-solutions-demonstrating-value
    date: '2025-11-03'
    access: full
    locator: paragraph on pricing teams that use AI and data
  - ref: AMBITION-PRICINGADVISOR-2026
    title: Senior Pricing Advisor in London (Complex Matters and GenAI), recruiter posting for an unnamed global law firm
    publisher: Ambition (recruiter)
    type: job-posting
    url: https://www.ambition.co.uk/job/senior-pricing-advisor-556300-1770890369
    date: '2026-02-12'
    access: full
    locator: Key Responsibilities
  - ref: AMBITION-PRICINGMANAGER-2026
    title: Pricing Manager - Gen AI in City of London, recruiter posting for an unnamed global law firm
    publisher: Ambition (recruiter)
    type: job-posting
    url: https://www.ambition.co.uk/job/pricing-manager-gen-ai-556277-1770801372
    date: '2026-02-11'
    access: full
    locator: The Role
  - ref: TRI-PRICINGROLES-2024
    title: 'Pricing legal technology and the impact on the role of the pricing professional: Changing roles and skills'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/legal-technology-pricing-professionals-changing-roles
    date: '2024-11-19'
    access: full
    locator: sections 'Changing roles' and 'Changing skills' (foundation, older than 18 months)
  last_reviewed: '2026-10-19'
  notes: 'Named evidence is a job title and conference remarks; postings are from an anonymous recruiter. Dentons, Linklaters, Husch Blackwell and McDermott pricing postings appeared in a web search only and were not opened. Routed in part to scoping-pricing. Pattern ''other'': a pricing-team capability: margin modelling and fee-structure advice.'
- id: professional-services-firm-finance-12
  title: Track AI-freed capacity through to sold work or repriced revenue
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: AI saves hours, but unless the freed time is identified and sold, the firm is no more productive; time saved is spread thinly across a project.
  solution: 'Firms measure what happens to time AI saves (more work taken on, better margins, new services) rather than counting tools or licences. SPI''s 2026 study frames this as ''the leak'': hours saved but not resold or repriced. A Hartford accounting firm''s head says AI could let it grow its client base without as many hires.'
  outcomes:
  - lever: capacity
    description: Share of surveyed firms saying AI saves them time
    figure: 84.8% say AI saves them time (the matching 'generates revenue' figure is hidden on the public page)
    measures: share of 245 professional services organisations that say AI saves them time, per SPI's landing page
    provenance: vendor-published
    source_ref: SPI-AI-2026
  prerequisites:
  - Utilisation, margin and revenue-per-head data by project
  - Demand and visibility to allocate the freed capacity
  - AI cost attribution by project
  risks_and_guardrails:
  - SPI full report is paywalled (USD 1,495); only the headline figures on the landing page were read
  - Whittlesey's managing partner said it has not been shown that AI leads to lower client bills because firms incur new technology cost, and that the firm spends about $30,000 a year on AI products
  human_checkpoints:
  - Practice leaders decide how freed hours are used
  - Finance reviews revenue and margin per head
  role_evolution: Resource managers and finance partners track AI capacity; the firm's workforce blends staff, contractors, offshore teams and AI.
  evidence_grade: C
  sources:
  - ref: SPI-AI-2026
    title: The 2026 Impact of AI on Professional Services (survey landing page)
    publisher: SPI Research
    type: survey
    url: https://spiresearch.com/reports/2026-ai-professional-services-survey/
    date: 2026-10
    access: full
    locator: 'page headline figures: 43.6% of projects, 84.8% ''say AI saves them time'', ''The Leak'''
  - ref: CONSULTANCYUK-BONE-2026
    title: Faster work doesn't automatically mean a more profitable professional services firm
    publisher: Consultancy.uk (contributed by Andrew Bone, co-founder and VP of product; employer not stated in the page text)
    type: press
    url: https://www.consultancy.uk/news/45863/faster-work-doesnt-automatically-mean-a-more-profitable-professional-services-firm
    date: '2026-10-15'
    access: full
    locator: paragraphs on 'What happens to the time AI saves?'
  - ref: HBJ-BILLABLE-2026
    title: AI-driven efficiencies force law, accounting firms to rethink the billable hour
    publisher: Hartford Business Journal
    type: press
    url: https://hartfordbusiness.com/article/ai-driven-efficiencies-force-law-accounting-firms-to-rethink-the-billable-hour/
    date: '2026-06-01'
    access: full
    locator: Whittlesey paragraphs
  last_reviewed: '2026-10-19'
  notes: SPI 43.6% of projects now use AI (23.1% in 2025) also on the page. Survey from a research vendor with a paid report; the Consultancy.uk contributor is a co-founder and VP of product whose employer is not stated in the text.
- id: professional-services-firm-finance-13
  title: Firm-level AI investment portfolio, budget and return governance
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Law and accounting firms are raising technology spend sharply while ROI evidence is thin, and costs are hard to attribute to projects.
  solution: Firms set AI investment envelopes, test where returns appear first (for example inefficient workflows behind write-downs) and track technology cost against fee growth. RSM US announced in June 2025 a commitment of $1 billion over three years in AI tools; PwC says its firms invested $3 billion across the network in AI and other capabilities in its fiscal year to June 2026.
  outcomes:
  - lever: cost
    description: Law firm technology and knowledge management spend growth, 2025
    figure: technology up nearly 11%, knowledge management up about 10% (2025); technology and KM combined up 11.6% overall and 8.7% per lawyer in Q2 2026
    measures: change in law firm spending on technology and on knowledge management versus the prior year, in TRI's Financial Insights data
    provenance: independent
    source_ref: TRI-SOTLM-2026
  - lever: cost
    description: Investment by named firms
    figure: $3 billion (PwC network, fiscal year ended 30 June 2026); $1 billion over three years (RSM US, announced)
    measures: amounts the firms say they invested or committed; no return stated
    provenance: self-reported
    source_ref: AT-PWC-2026
  prerequisites:
  - A clear AI strategy (Thomson Reuters's Steven Petrie said strategy-led firms are 3.9 times more likely to achieve ROI, yet only 22% have one; the article gives no definition of the base)
  - Cost attribution by project or matter
  - Agreed return measures that clients accept
  risks_and_guardrails:
  - TRI warns of an AI-bubble risk for firms that use AI mainly to justify higher rates
  - KPMG's US Vice Chair of Advisory notes AI cost often cannot be attributed to individual projects
  - Independent returns evidence is absent in the sources read
  human_checkpoints:
  - Executive committee or CFO approves the AI budget and reviews return measures
  role_evolution: Chief innovation, pricing and knowledge roles share budget accountability with finance.
  evidence_grade: B
  sources:
  - ref: TRI-SOTLM-2026
    title: 'State of the US Legal Market 2026 analysis: Will the AI bubble burst? A crucial warning for law firms'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble
    date: '2026-01-14'
    access: full
    locator: paragraphs on technology and KM spend (nearly 11% and 10%; 39.3% and 37.2% since 2021)
  - ref: TRI-LFFI-COSTS-2026
    title: 'Q2 2026 LFFI analysis: The rising costs lurking beneath law firm momentum'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/q2-2026-lffi-analysis-rising-costs
    date: '2026-08-31'
    access: full
    locator: 'section ''Overhead expenses: Technology is in the lead'''
  - ref: AT-PWC-2026
    title: PwC grows 2026 global revenue to $60.2B
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/pwc-grows-2026-global-revenue-to-60-2b
    date: '2026-10-19'
    access: full
    locator: paragraph on the $3 billion
  - ref: BLOOMBERGLAW-ACCTG-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/esg/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: paragraphs on RSM US $1 billion and KPMG cost attribution
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: section 'The pressure hasn't yet found a release valve'
  - ref: TRI-ROI-2025
    title: Finding a quicker ROI on law firms' investment in AI
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/law-firm-roi-ai-investment
    date: '2025-05-19'
    access: full
    locator: section 'Understanding where the time goes' (foundation, May 2025)
  last_reviewed: '2026-10-19'
  notes: 'Spend is measured; return is not. No A grade for any ROI claim. TRI is part of Thomson Reuters, which sells legal AI. Compare TRI-GREATDISCONNECT-2026 (85% of law firm respondents and 75% of corporate legal respondents not collecting AI ROI data or unsure). Pattern ''other'': an investment-governance process.'
- id: professional-services-firm-finance-14
  title: Outside capital in an accounting firm to fund technology, talent and AI
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: in-production
  problem: Partnerships distribute most profit each year and have limited cash to invest in technology and talent.
  solution: Crowe, ranked No. 12 in Accounting Today's 2026 Top 100 with $1.4 billion revenue, announced an investment from KKR in June, which closed in August 2026, with plans to use the capital on talent, technology and innovation; it then launched CroweONE, a shared ownership plan for all employees. Other private equity deals with large accounting firms are listed in a law-firm client alert.
  outcomes:
  - lever: growth
    description: Scale of the deal
    figure: none published (deal value not stated in the article)
    measures: not applicable
    provenance: self-reported
    source_ref: AT-CROWE-2026
  prerequisites:
  - Governance that preserves partner control of professional matters
  - Independence and ethics review (SEC and PCAOB attention per a legal academic)
  - Employee ownership design
  risks_and_guardrails:
  - Accounting Today corrected an earlier version that called CroweONE an employee stock ownership plan
  - ICAEW's 2026 mid-tier research found fewer independent firms were considering PE than in previous years, citing culture, autonomy and long-term incentives
  - 'FT-reported investor commentary: PE investors are scrutinising how AI affects hourly-billed accounting revenue (see use case 18)'
  human_checkpoints:
  - Partners vote on the transaction and the governance terms
  role_evolution: Partners become part-owners alongside investors; broader employee ownership is used to retain staff.
  evidence_grade: B
  sources:
  - ref: AT-CROWE-2026
    title: Crowe launches shared ownership plan
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/crowe-launches-esop-with-kkr-investment
    date: '2026-10-19'
    access: full
    locator: paragraphs on the KKR investment, use of capital and CroweONE
  - ref: ICAEW-MIDTIER-2026
    title: Mid-tier firms focused on AI and consolidation
    publisher: ICAEW
    type: professional-body
    url: https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/mid-tier-firms-focused-on-ai-and-consolidation
    date: '2026-05-22'
    access: full
    locator: sections 'Consolidation activity remains high' and 'AI and operating models'
  - ref: WINSTON-PE-2026
    title: 'Law firms: The next frontier for private equity in professional services?'
    publisher: Winston & Strawn (client alert, pre-Winston Taylor combination)
    type: firm
    url: https://www.winston.com/en/insights-news/law-firms-the-next-frontier-for-private-equity-in-professional-services
    date: '2026-03-19'
    access: full
    locator: table of accounting PE transactions
  - ref: COLUMBIA-BREYDO-2026
    title: Private Equity Is Coming for Law Firms - and the Rules Aren't Ready
    publisher: Columbia Law School Blue Sky Blog (Lev Breydo, William & Mary Law School)
    type: academic
    url: https://clsbluesky.law.columbia.edu/2026/04/30/private-equity-is-coming-for-law-firms-and-the-rules-arent-ready/
    date: '2026-04-30'
    access: full
    locator: paragraphs on accounting and PE oversight
  last_reviewed: '2026-10-19'
  notes: 'AI is one of three named uses of the capital; the source does not say how much goes to AI. Outcome of the deal not yet observable. ICAEW survey: 35 mid-tier firms, 86% have a technology strategy that includes AI adoption. Pattern ''other'': a capital-structure decision.'
- id: professional-services-firm-finance-15
  title: Outside capital for law firms through a management services organisation (MSO) to fund AI
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: announced
  problem: Law partnerships pay out nearly all profit, leave little cash for AI and technology, and Rule 5.4 bars nonlawyer ownership.
  solution: An investor-owned MSO takes over operations (technology, billing, marketing, HR) while lawyers keep the practice. Dudley DeBosier (Louisiana personal injury) announced a partnership in January 2026 with the PE-backed Orion Legal; Cohen & Gresser was reported in talks and McDermott Will & Schulte was reported to be exploring an MSO deal. An American Lawyer article (summarised by Holland & Knight, which quotes its lawyer Joshua Porte) says AI platforms need substantial upfront investment and that the traditional law firm structure leaves little cash in reserve once partners are paid.
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: not applicable
    provenance: self-reported
    source_ref: COLUMBIA-BREYDO-2026
  prerequisites:
  - An MSO structure that complies with Rule 5.4 and state fee-sharing rules
  - Partner agreement to share economics with investors
  - Governance safeguards
  risks_and_guardrails:
  - The Columbia essay argues no state bar has issued model governance standards for law firm MSOs and that healthcare MSOs drifted toward investor control
  - Winston client alert cautions with UK ABS failures such as Slater and Gordon
  human_checkpoints:
  - Partners approve the MSO agreement; ethics counsel reviews separation of business and practice
  role_evolution: Business-side staff move to the MSO; partners may become employees of the practice under management agreements.
  evidence_grade: B
  sources:
  - ref: COLUMBIA-BREYDO-2026
    title: Private Equity Is Coming for Law Firms - and the Rules Aren't Ready
    publisher: Columbia Law School Blue Sky Blog (Lev Breydo, William & Mary Law School)
    type: academic
    url: https://clsbluesky.law.columbia.edu/2026/04/30/private-equity-is-coming-for-law-firms-and-the-rules-arent-ready/
    date: '2026-04-30'
    access: full
    locator: sections 'The Workaround' and 'The Governance Gap'
  - ref: HK-AMLAW-2026
    title: Firms Need Capital to Pay for AI Tools. Could PE Investment Be the Solution? (In the Headlines summary of an American Lawyer article)
    publisher: Holland & Knight
    type: firm
    url: https://www.hklaw.com/en/news/intheheadlines/2026/04/firms-need-capital-to-pay-for-ai-tools-could-pe-investment
    date: '2026-04-20'
    access: full
    locator: summary paragraph quoting Joshua Porte
  - ref: WINSTON-PE-2026
    title: 'Law firms: The next frontier for private equity in professional services?'
    publisher: Winston & Strawn (client alert, pre-Winston Taylor combination)
    type: firm
    url: https://www.winston.com/en/insights-news/law-firms-the-next-frontier-for-private-equity-in-professional-services
    date: '2026-03-19'
    access: full
    locator: sections on the MSO and key metrics
  last_reviewed: '2026-10-19'
  notes: 'Deals are announced or reported rather than evidenced; AI is cited as a reason for seeking capital, not as a measured use. The Winston alert lists MSO-friendly metrics (for example leverage of 4:1 or higher; realisation below 85% as an improvement opportunity); these are the firm''s view, not a benchmark. Pattern ''other'': a capital-structure and governance decision.'
- id: professional-services-firm-finance-16
  title: AI-native law firm formed with outside capital and non-hourly pricing
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - expert-judgment
  - document-production
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Established firm economics depend on leverage and hourly rates; investors and rainmakers see room for a different model.
  solution: A Bloomberg Law columnist (an in-house chief legal officer) writes that Norm Law, chaired by Sidley's former chair, is taking Big Law work from Wall Street clients with private equity behind it, and that Arceus (US) and Falcon (Europe) launched this fall, Falcon pledging to 'bury the billable hour'.
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: not applicable
    provenance: self-reported
    source_ref: BLOOMBERGLAW-GCXAI-2026
  prerequisites:
  - Capital
  - Expert lawyers without portable books who want a platform
  - Clients willing to buy work delivered with AI
  risks_and_guardrails:
  - Single column; claims about taking work were not checked against firm sources
  - Regulatory limits on nonlawyer ownership vary by state (see use case 15)
  human_checkpoints:
  - Lawyers supervise AI-produced work product
  role_evolution: The columnist reports lateral experts moving to AI-native firms and platforms; she also notes juniors face a training question.
  evidence_grade: C
  sources:
  - ref: BLOOMBERGLAW-GCXAI-2026
    title: 'GC x AI Retrospective: The Billable Hour, Like a Twinkie, Endures (column by Eric Dodson Greenberg, Cox Media Group; in-house)'
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/business-and-practice/gc-x-ai-retrospective-the-billable-hour-like-a-twinkie-endures
    date: '2026-10-19'
    access: full
    locator: section 'What Hasn't Happened - Yet'
  last_reviewed: '2026-10-19'
  notes: In-house author. Grade C because the evidence is one practitioner column; the Norm Law claim has no primary source here. The same column says firms are banking AI productivity gains as margin and that rates rose.
- id: professional-services-firm-finance-17
  title: Realign performance metrics and partner pay to AI use and value pricing
  archetype: professional-services
  module: firm-finance
  function: people-hr
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Staff are urged to adopt AI but judged on the same metrics as a decade ago; origination credit and write-off policies reward hours.
  solution: Wipfli is introducing client satisfaction and cycle time as non-traditional metrics; a compensation-data analyst says value-based firms can base bonuses on revenue generated. PwC's US CEO said partners who resist AI have no place at the firm. A GGI alliance article (by an Offit Kurman lawyer) urges reviewing origination credit, partner compensation and write-off policy for work priced by value, outcome or retainer.
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: not applicable
    provenance: self-reported
    source_ref: BLOOMBERGLAW-ACCTG-2026
  prerequisites:
  - Data on cycle time and satisfaction
  - Partner agreement on revised credit rules
  - Matter cost tracking
  risks_and_guardrails:
  - Law firm recruiting and pay depend heavily on utilisation and billable hours (TRI ILTACON 2025 panel), which resists change
  - PwC remark is a statement of intent reported through the FT
  human_checkpoints:
  - Compensation committee approves metric changes
  role_evolution: Partner tracks broaden toward operations, technology enablement and change management (INSIDE Public Accounting's prediction).
  evidence_grade: B
  sources:
  - ref: BLOOMBERGLAW-ACCTG-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/esg/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: section 'Employee Incentives'
  - ref: CPAPA-PWC-2026
    title: PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
    date: '2026-03-25'
    access: full
    locator: opening paragraphs
  - ref: MONDAQ-GGI-2026
    title: 'Still Selling Judgment: How Law Firms And Accounting Firms Must Prepare For AI-driven Pricing Change'
    publisher: GGI Global Alliance / Offit Kurman (via Mondaq)
    type: firm
    url: https://www.mondaq.com/unitedstates/management/1814268/still-selling-judgment-how-law-firms-and-accounting-firms-must-prepare-for-ai-driven-pricing-change
    date: '2026-07-09'
    access: full
    locator: section 'Redesign internal incentives in parallel'
  - ref: IPA-2026
    title: 'Perspectives from the Profession: 2026: The Year Accounting Firms Stop Talking About Change and Start Living It'
    publisher: INSIDE Public Accounting
    type: press
    url: https://insidepublicaccounting.com/2026/01/06/perspectives-from-the-profession-2026-the-year-accounting-firms-stop-talking-about-change-and-start-living-it/
    date: '2026-01-06'
    access: full
    locator: themes 1, 3 and 6
  - ref: TRI-ILTACON-HOUR-2025
    title: 'ILTACON 2025: Pricing the future - AI''s impact on the billable hour'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/iltacon-2025-billable-hour
    date: '2025-09-02'
    access: full
    locator: paragraph on recruiting and compensation tied to utilisation
  last_reviewed: '2026-10-19'
  notes: 'Wipfli is described as ''introducing'', so piloting. The GGI and IPA items are opinion or forecast, not deployments. Pattern ''other'': a performance-measurement and compensation redesign.'
- id: professional-services-firm-finance-18
  title: 'Idea: investor diligence and valuation that adjusts for AI exposure of hourly-billed revenue'
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Private capital has assumed professional-services revenue is recurring and sticky; AI may shrink hours-based revenue.
  solution: Per FT coverage of the SuperReturn conference in Berlin (as reported by a Dutch trade outlet), private-capital investors now look at AI effects on lawyers, consultants and accountants as well as software; an Apax co-CEO is quoted as calling bookkeeping-type accounting firms vulnerable when they bill by the hour and do no regulated audit work. The Dutch outlet adds its own comment that the value of an audit opinion rests on trust as well as hours.
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: not applicable
    provenance: self-reported
    source_ref: VANMORGEN-SUPERRETURN-2026
  prerequisites:
  - Revenue mix by pricing model
  - Evidence on how much work AI compresses
  risks_and_guardrails:
  - Second-hand report of FT reporting; original FT article not opened
  - Opinion of investors, not data
  human_checkpoints:
  - Investment committee reviews model assumptions
  role_evolution: Firm CFOs may need to present AI exposure and pricing mix to investors.
  evidence_grade: D
  sources:
  - ref: VANMORGEN-SUPERRETURN-2026
    title: AI zet private-equityrekensom in accountancy onder druk (AI puts the private-equity sum in accountancy under pressure; reports FT coverage of SuperReturn Berlin)
    publisher: Accountancy Vanmorgen
    type: press
    url: https://www.accountancyvanmorgen.nl/2026/06/16/ai-zet-private-equityrekensom-in-accountancy-onder-druk/
    date: '2026-06-16'
    access: full
    locator: paragraphs summarising the FT report on SuperReturn conversations
  last_reviewed: '2026-10-19'
  notes: 'Idea discussed by investors and trade press. Pattern ''other'': an investor valuation exercise.'
- id: professional-services-firm-finance-19
  title: 'Idea: remodel the leverage pyramid and associate economics for AI-compressed junior work'
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: Associates and non-equity partners carry most extra demand, yet AI compresses the high-volume work that built the pyramid.
  solution: Firm leaders ask how many juniors a firm needs. Independent TRI data show demand leverage rose to record levels through Q2 2026 'not because of layoffs'. DLA Piper's AI head said some financial-contract due diligence is already down to two hours from 15 to 20. Legalweek 2026 panels treated the associate, not the billable hour, as the open existential question.
  outcomes:
  - lever: capacity
    description: Leverage ratio, Q4 2025 and Q2 2026
    figure: associate demand leverage 1.55 (Q4 2025 record), 1.47 (Q1 and Q2 2026); non-equity partner demand leverage 0.91 (Q2 2026)
    measures: 'TRI ''demand leverage'': hours worked by associates (or by non-equity partners) relative to hours worked by equity partners, in TRI Financial Insights data; the article''s own definition is worded loosely'
    provenance: independent
    source_ref: TRI-LFFI-LEVERAGE-2026
  prerequisites:
  - Data on task-level time compression
  - A view on training pipeline
  risks_and_guardrails:
  - Leverage rose before any measured AI effect; the source does not attribute it to AI
  - Clients may bring junior-level work in-house
  human_checkpoints:
  - Executive committee sets associate hiring and non-equity partner policy
  role_evolution: Associate role redefined toward training, technological fluency and management skills (Legalweek panelists).
  evidence_grade: D
  sources:
  - ref: TRI-LFFI-LEVERAGE-2026
    title: 'Q2 2026 LFFI analysis: Law firm leverage just broke a 17-year record - and this time, it''s not because of layoffs'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/q2-2026-lffi-analysis-law-firm-leverage
    date: '2026-08-18'
    access: full
    locator: key insights and 'The value of leverage'
  - ref: TRI-LEGALWEEK-CRISIS-2026
    title: Move over, "Death of the billable hour," Legalweek 2026 has found a new existential crisis
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-new-existential-crisis
    date: '2026-03-19'
    access: full
    locator: sections 'The question nobody wanted to ask out loud' and quote from Barclay Blair
  - ref: TRI-LFFI-COSTS-2026
    title: 'Q2 2026 LFFI analysis: The rising costs lurking beneath law firm momentum'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/q2-2026-lffi-analysis-rising-costs
    date: '2026-08-31'
    access: full
    locator: paragraph on direct expenses and equity partner demand -1.2%
  last_reviewed: '2026-10-19'
  notes: 'Idea. Evidence of AI-driven change in leverage is absent; leverage data are context. Routed to talent-learning for the training question. Pattern ''other'': a workforce-structure decision.'
- id: professional-services-firm-finance-20
  title: 'Idea: aim AI at the workflows that cause write-downs and revenue leakage'
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - document-production
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: Partners routinely write down pre-bills because fees seem too high for the client; the aggregate loss is large.
  solution: A Thomson Reuters Institute piece suggests firms analyse where leakage occurs and apply AI to those inefficient workflows as a first return on AI investment.
  outcomes:
  - lever: cost
    description: none published
    figure: none
    measures: not applicable
    provenance: self-reported
    source_ref: TRI-ROI-2025
  prerequisites:
  - Write-down and realisation data by matter and timekeeper
  risks_and_guardrails:
  - Source is a Thomson Reuters Institute white-paper summary, not a deployment
  - A July 2025 TRI piece says realization rates (what clients agreed to versus what was collected) have stayed just above 90% for three years
  human_checkpoints:
  - Billing partner reviews the pre-bill
  role_evolution: Operations and finance staff target process leakage.
  evidence_grade: D
  sources:
  - ref: TRI-ROI-2025
    title: Finding a quicker ROI on law firms' investment in AI
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/law-firm-roi-ai-investment
    date: '2025-05-19'
    access: full
    locator: sections 'Understanding where the time goes' and the closing paragraphs
  - ref: TRI-RETHINKING-2025
    title: 'From billable hours to agentic outcomes: Rethinking legal value in the age of AI'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/rethinking-legal-value
    date: '2025-07-15'
    access: full
    locator: paragraph on realization rates above 90% (foundation)
  last_reviewed: '2026-10-19'
  notes: Idea. Pre-bill review specifics are not described in the source. Overlaps billing-collections.
- id: professional-services-firm-finance-21
  title: 'Idea: share matter-level AI usage and savings between firm and client'
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: Clients cannot see whether outside counsel uses AI or what it saves; firms cannot say what savings they achieve.
  solution: Clients ask for line-item transparency (was AI used on this task, and how much time or money did it save?), and some clients ask for AI usage disclosures. In-house legal teams report they do not know whether firms use AI and firms rarely collect ROI data. A DLA Piper leader advised firms to set the ROI conversation rather than wait for clients to set terms.
  outcomes:
  - lever: risk
    description: Visibility gap
    figure: 68% of corporate legal professionals do not know whether outside firms use AI; 85% of law firm and 75% of corporate legal respondents are not collecting AI ROI data or are unsure
    measures: share of respondents to TRI's 2026 AI in Professional Services Report who gave each answer, as reported in the article; sample size not stated
    provenance: vendor-published
    source_ref: TRI-GREATDISCONNECT-2026
  prerequisites:
  - Matter-level AI usage data (see use case 7)
  - A shared method for estimating manual-equivalent effort
  risks_and_guardrails:
  - 'Clients'' stances conflict: some demand AI use, others bar it or refuse to pay for AI-performed work'
  - One in-house respondent fears firms bill for the hypothetical time without AI
  human_checkpoints:
  - Client and firm agree measures; billing partner signs off
  role_evolution: In-house legal operations and outside-counsel managers negotiate AI terms (in-house).
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: sections 'The contradictions in the room' and 'Proving AI's path to saving clients money'
  - ref: TRI-GREATDISCONNECT-2026
    title: 'The great AI disconnect: Firms and legal departments are not communicating about AI usage'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect
    date: '2026-03-18'
    access: full
    locator: sections on visibility and measurement gaps
  - ref: BLOOMBERGLAW-GCXAI-2026
    title: 'GC x AI Retrospective: The Billable Hour, Like a Twinkie, Endures (column by Eric Dodson Greenberg, Cox Media Group; in-house)'
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/business-and-practice/gc-x-ai-retrospective-the-billable-hour-like-a-twinkie-endures
    date: '2026-10-19'
    access: full
    locator: section 'What Hasn't Happened - Yet' (in-house column)
  last_reviewed: '2026-10-19'
  notes: 'Idea (no firm reports a working client-facing AI savings report). Tag: in-house for the client side. TRI is part of Thomson Reuters. Pattern ''other'': a shared reporting arrangement between firm and client.'
- id: professional-services-firm-finance-22
  title: 'Idea: pick the pricing model by outcome observability and attribution, not by convention'
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: Firms apply time, fixed, retainer or outcome pricing by habit.
  solution: 'An academic framework locates each engagement on two axes (how well outcomes can be observed and attributed, and how well the client can observe input cost) and gives four decision rules: match contract power to signal quality, let internal versus external AI use set direction, invest in measurement before outcome pricing while checking attribution, and treat hybrid pricing as the usual resting point.'
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: not applicable
    provenance: self-reported
    source_ref: STANFORD-DEL-2026
  prerequisites:
  - Ability to measure outcomes and to attribute them
  risks_and_guardrails:
  - Theory-led with desk research; the authors say consistency with practice is qualitative plausibility, not confirmatory
  human_checkpoints:
  - Executives locate each engagement before choosing the structure
  role_evolution: Pricing leaders need hybrid-contract skills.
  evidence_grade: D
  sources:
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson, Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Sections 4, 5 and 7
  last_reviewed: '2026-10-19'
  notes: 'Idea from academics; examples in the paper include Palantir and Salesforce Agentforce, which are not professional-services firms. Pattern ''other'': a decision framework for choosing a fee structure.'
```

## 3. Module notes

### Processes and key steps (work types)

1. **Annual rate setting and discounting** (data-reporting, expert-judgment). Large law firms raised standard rates faster than worked rates, accepting deeper discounts; Midsize firms did the opposite and saw worked-rate growth of 5.3% against 9.8% for the Am Law 100 in Q1 2026 (TRI-LFFI-Q1-2026, 'The segments' strategy split'; TRI-LFFI-MIDSIZE-2026, 'Rates are the most consequential gap').
2. **Matter and portfolio pricing** (expert-judgment, data-reporting). Hourly, fixed, hybrid, retainer, KPI-based and outcome-based fees; deal-level design belongs to scoping-pricing. A pricing team now models margin for AI-assisted matters (AMBITION-PRICINGMANAGER-2026, 'Key Responsibilities').
3. **Billing, realization and collection monitoring** (data-reporting). Realization margin is the gap between actual realization and the level needed to collect the same fees given rate growth (TRI-RATES-2024, foundation, Oct 2024). Time capture to cash belongs to billing-collections.
4. **Profitability and leverage analysis** (data-reporting). Leverage by title, productivity, value per lawyer (TRI-LFFI-LEVERAGE-2026; TRI-LFFI-PRODUCTIVITY-2026, 'The divergence between hours and value').
5. **Partner economics: pay, origination credit, capital** (expert-judgment). Partners distribute most profit and fund little technology (HK-AMLAW-2026; WINSTON-PE-2026, table 'Core Tension').
6. **AI investment, vendor contracting and consumption governance** (data-reporting, coordination-scheduling). Budget, licences, token spend, model choice (TRI-ILTACON-METER-2026).
7. **Ownership and capital structure** (expert-judgment). Private equity in accounting, MSOs in law, employee ownership (AT-CROWE-2026; COLUMBIA-BREYDO-2026).
8. **Client value reporting** (client-interaction, data-reporting). Proving matter-level AI savings (TRI-LEGALWEEK-2026).

### Common pain points

- **No agreed way to show AI return.** No audience member at the ILTACON implementation panel (50+ present) said their team had a strong AI ROI measure (TRI-ILTACON-IMPL-2026, 'Metrics that matter'); 85% of law-firm and 75% of corporate-legal respondents collect no AI ROI data or are unsure (TRI-GREATDISCONNECT-2026).
- **Efficiency punished by hourly billing**, and clients simultaneously demand AI, line-item transparency and, in some guidelines, refuse to pay for AI-done work (TRI-LEGALWEEK-2026, 'The contradictions in the room').
- **Hidden variable AI cost**: premium models for trivial tasks, agents running unobserved, many tools (about half of one ILTACON room had 10+ tools in use or under evaluation) (TRI-ILTACON-METER-2026).
- **Cost not attributable to projects** (KPMG's Rob Fisher, BLOOMBERGLAW-ACCTG-2026; CONSULTANCYUK-BONE-2026).
- **Incentives and metrics still keyed to hours** (TRI-ILTACON-HOUR-2025; BLOOMBERGLAW-ACCTG-2026, 'Employee Incentives').
- **Midsize firms squeezed**: slower rate growth, fastest direct-expense growth, lowest tech investment growth among segments in Q1 2026 (TRI-LFFI-MIDSIZE-2026, key insights).
- **Pricing power rests on shown value.** TRI says rate rises of more than twice inflation (about 3%) in 2025 leave firms needing measurable value at each client stage (TRI-SOTLM-PRICING-2026).
- **Time saved is not automatically sold**: SPI frames the gap as "the leak" (SPI-AI-2026).

### Metrics and benchmarks (with provenance)

- Law Firm Financial Index: 55 in Q1 2026, equal to its long-run average since 2006 (TRI-LFFI-Q1-2026); 61 in Q4 2025, with Q4 worked-rate growth of 7.1%, the smallest quarter of 2025 (TRI-LFFI-ELASTICITY-2026). TRI Financial Insights data, labelled independent here; TRI belongs to Thomson Reuters, which sells legal AI.
- Q2 2026: the index rose sharply and demand was on pace for its strongest year since 2021 (TRI-LFFI-Q2-2026, 'A faster crossing'); direct expenses +8.3%, overhead +7.7%, technology plus KM +11.6% (8.7% per lawyer), worked rates +7.1% (TRI-LFFI-COSTS-2026, 'Key insights' and 'The masking effect').
- Q3 2025: demand +3.9%, worked rates +7.4%, direct costs +8.5% and overhead +7.5% year on year (TRI-PROSPERITY-2025, 'Tectonic pressures growing'). At the Oct 2025 COO & CFO Forum, realization and expenses were reported moving slowly in the wrong direction for the first time since 2008-09, and performance leaders were separating from laggards (TRI-COOCFO-MARKET-2025).
- 2025: technology spend up nearly 11% and KM about 10%; profit per lawyer 8.4% above pre-2022 levels; fees worked per lawyer 16.8% above (TRI-SOTLM-2026). The source says most of this came from rate rises.
- Q1 2026 productivity -0.4% while demand grew 2.7% (TRI-LFFI-PRODUCTIVITY-2026).
- Wells Fargo data via Bloomberg Law: the 200 largest US firms' revenue about +13% and expenses +10.2% in 2025; AI tools cost $50-$350 per attorney per month and add about 30% to the cost of existing tools (a Jackson Walker KM officer's estimate, year of the estimate not stated) (BLOOMBERGLAW-TEXAS-2026). Radiant cites a different Wells Fargo cut (12.6% revenue, 9.6% standard-rate growth) (RADIANT-TOKEN-2026); cohorts may differ, not reconciled.
- Accounting: AICPA 2025 survey of 1,000+ firms, median net hourly rate rose nearly 7% over two years to $170 (via BLOOMBERGLAW-ACCTG-2026). Tax firms: 78% rely mainly on hourly billing; individual return preparation margin 28% versus 20-24% for advisory (TRI-CHARGING-2026).
- AI spend norm: "roughly 1% of revenue" per an Ogletree Deakins officer (TRI-ILTACON-METER-2026); the Whittlesey firm spends about $30,000 a year on AI products (HBJ-BILLABLE-2026).
- Project-based firms: 43.6% of projects use AI in SPI's 245-firm study (23.1% in 2025) (SPI-AI-2026).
- Pilot threshold: more than 70% weekly active users (Holland & Hart) (TRI-ILTACON-IMPL-2026).
- Strategy and ROI: TR's Steven Petrie said strategy-led firms are 3.9 times more likely to achieve AI ROI and only 22% have a strategy (TRI-LEGALWEEK-2026); a vendor-side statistic with no stated base.
- Private equity screens (law-firm view, not a benchmark): leverage of 4:1 or higher, realization below 85%, overhead above 55% of revenue flagged as improvement opportunities (WINSTON-PE-2026, 'Key Metrics').
- Mid-tier UK accounting: 86% of 35 firms have a technology strategy including AI; 17% are confident in assessing workforce impact (ICAEW-MIDTIER-2026).
- **Quality evidence:** none found for this module. No error rates, override rates or independent measurement of AI's effect on realization, margin or partner profit. The nearest independent measures are TRI market data on spend and leverage, which do not isolate AI.

### Guardrails and regulatory points

- **Billing rules.** Texas ethics committee: cannot charge for time saved by generative AI (as reported, BLOOMBERGLAW-TEXAS-2026); California's State Bar guidance requires hourly billing to reflect time actually spent (landscape ref CALBAR-GENAI-2026, not re-read here).
- **AI cost as overhead or expense.** A practitioner opinion in an ISBA newsletter applies ABA Formal Op. 93-379: subscriptions are overhead; metered charges are billable only if attributable to the matter, at cost, with disclosure; the author recommends absorbing ordinary use (ISBA-ELEFANT-2026). North Carolina and a New York task force take looser views (same source).
- **Nonlawyer ownership.** Rule 5.4 stays the main barrier; MSOs avoid it by design but raise governance questions; no state bar had issued MSO governance standards at the time of the Columbia essay (COLUMBIA-BREYDO-2026; WINSTON-PE-2026, 'Critical Point'). The same essay says the SEC, PCAOB and AICPA are looking at PE in accounting (author's account).
- **Independence and confidentiality** in accounting PE deals (COLUMBIA-BREYDO-2026); third-party AI note-takers raise privilege questions (HBJ-BILLABLE-2026, Pullman & Comley).
- **Client AI terms** vary from "must use AI" to "may not use without permission" (TRI-LEGALWEEK-2026, DLA Piper remarks).

### Frontier signals (dated)

- 2026-10-19: Bloomberg Law column reports AI-native firms (Norm Law with PE backing; Arceus; Falcon, pledging to "bury the billable hour") (BLOOMBERGLAW-GCXAI-2026).
- 2026-10-19: Crowe launches CroweONE after KKR close in August (AT-CROWE-2026); PwC reports $3 billion invested network-wide in AI and other capabilities (AT-PWC-2026).
- 2026-10-13: Legora and Laurel announce AI-to-time-entry capture and a planned AI value measure (LEGORA-LAUREL-2026).
- 2026-10-02: TRI argues tax and accounting firms must price judgment, not hours (TRI-CHARGING-2026).
- 2026-09-09: ILTACON 2026 practitioners "reading the meter" on token cost (TRI-ILTACON-METER-2026).
- 2026-08-23: Stanford pricing framework: AI pushes consulting toward hybrid pricing (STANFORD-DEL-2026).
- 2026-08-06: Debevoise STAAR, $150,000 a year subscription in beta (BLOOMBERGLAW-DEBEVOISE-2026).
- 2026-08-18: Law firm demand leverage at record levels through Q2 2026 (TRI-LFFI-LEVERAGE-2026).
- 2026-07: MyShingle ethics opinion on AI cost pass-through, noting Legora's move to consumption pricing (ISBA-ELEFANT-2026).
- 2026-06-16: FT-reported SuperReturn discussion that PE is re-examining hourly-billed accounting exposure to AI (VANMORGEN-SUPERRETURN-2026).
- 2026-04-30: Legal academic warns MSO governance is not ready (COLUMBIA-BREYDO-2026).
- 2026-03-25 and 2026-03-05: PwC US CEO and RSM, PwC and KPMG leaders on subscription and value pricing (CPAPA-PWC-2026; BLOOMBERGLAW-ACCTG-2026).
- 2026-03-13: Legalweek clients demand proof of AI savings (TRI-LEGALWEEK-2026).
- Scheduled, not yet held at the date of this run: the 25th TRI Law Firm COO & CFO Forum (21-22 Oct 2026, per the landscape); no content used.

### Workforce and role effects

- **Pricing professionals** become commercial, client-facing and product-minded (TRI-PRICINGROLES-2024, foundation); firms advertise AI pricing roles (AMBITION-PRICINGADVISOR-2026).
- **Innovation and knowledge managers** gain cost-control duties (TRI-ILTACON-METER-2026).
- **Legal engineers** appear as a new profession building AI systems (BLOOMBERGLAW-GCXAI-2026).
- **Associates and non-equity partners** carry growing shares of demand (associates +4.3%, non-equity partners +6.0% in Q2 2026; equity partners -1.2%) (TRI-LFFI-COSTS-2026); Legalweek treated the associate's future as the open question (TRI-LEGALWEEK-CRISIS-2026).
- **Partners**: PwC's US CEO said resisters have no place (CPAPA-PWC-2026); INSIDE Public Accounting expects partner tracks in operations and technology (IPA-2026); Debevoise partners curate firm knowledge (BLOOMBERGLAW-DEBEVOISE-2026).
- **Accounting staff** under value pricing could be rewarded for revenue rather than hours (BLOOMBERGLAW-ACCTG-2026).

### Objections and concerns practitioners raise

- "The billable hour has been declared dead since the 1990s"; a Saul Ewing partner saw no meaningful client-driven move to AFAs (TRI-LEGALWEEK-CRISIS-2026).
- Clients still pay hourly bills, so firms have no real incentive to change (TRI-ILTACON-HOUR-2025).
- AI replaces personnel cost with technology cost, so bills may not fall (HBJ-BILLABLE-2026, Whittlesey).
- Possible AI bubble and rate-dependence (TRI-SOTLM-2026; TRI-LFFI-ELASTICITY-2026).
- Governance of PE and MSOs; partner culture and attrition (COLUMBIA-BREYDO-2026; ICAEW-MIDTIER-2026).
- "More output, same reviewer": strained human review (BLOOMBERGLAW-GCXAI-2026).
- Vendor opacity on consumption pricing (EDISCOVERYTODAY-ILTACON-2026).
- Fixed fees can turn unprofitable without delivery-cost data (CONSULTANCYUK-BONE-2026).

### Interview probes for an advisor

1. When a task now takes a fraction of the time, what happens to the time record, the bill and the freed capacity, and who decides?
2. What do you spend on AI across seats, tokens and agents, and can you attribute it to a client or matter?
3. Which of your fixed, capped or subscription fees would lose money if effort halved, and how would you know before the work starts?
4. What has changed in utilisation targets, origination credit or bonuses since AI arrived?
5. If an investor or lender looked at your revenue mix, what share would they call hours-based, and what evidence of AI return could you show them?

### Notes on the landscape file

- Accounting Today corrected its Crowe story: CroweONE is a shared ownership plan, not an ESOP, although the URL slug still says ESOP (AT-CROWE-2026).
- The landscape's "McKinsey 25% vs one third" question: the Stanford paper cites a November 2025 McKinsey statement of roughly a quarter, second-hand (STANFORD-DEL-2026, Section 5.1).
- The Legora-Laurel release body carries no date; 2026-10-13 comes from the landscape.

## 4. Routed to other modules

- **scoping-pricing:** Kopka Law KPI billing at matter level (TRI-KOPKA-2026); the Stanford strategy map as deal-level design (STANFORD-DEL-2026); Kerbis subscription pricing and Furlong on outcome pricing (LEGALLATENIGHT-49-2026; LAWYERIST-607-2026, show notes only); Norton Rose view that fixed fees are a "win-win" (BLOOMBERGLAW-TEXAS-2026).
- **billing-collections:** Laurel time capture (LEGORA-LAUREL-2026; ARTLAW-LEGORA-2026, Intapp Time and Laurel integrations); write-down and fee-erosion leakage (TRI-ROI-2025); billing rules on time saved (BLOOMBERGLAW-TEXAS-2026).
- **talent-learning:** associate training and AI simulations, the pyramid question (TRI-LEGALWEEK-CRISIS-2026); junior-lawyer training and legal engineer path (BLOOMBERGLAW-GCXAI-2026).
- **client-development:** advice to lead the AI-ROI conversation with clients (TRI-LEGALWEEK-2026); the visibility gap between firms and departments (TRI-GREATDISCONNECT-2026).
- **quality-review:** "more output, same reviewer" and AI slop (BLOOMBERGLAW-GCXAI-2026); human oversight as a cost of speed (CONSULTANCYUK-BONE-2026).
- **knowledge-management:** partner-as-gatekeeper burden of maintaining a client-facing knowledge portal (BLOOMBERGLAW-DEBEVOISE-2026).
- **staffing-resourcing:** blended workforce of staff, contractors, offshore and AI and capacity visibility (CONSULTANCYUK-BONE-2026).
- **In-house tag (shared service, legal department):** GSK's savings pressure on outside counsel (TRI-LEGALWEEK-2026); in-house columnist's view of firm economics (BLOOMBERGLAW-GCXAI-2026); departments' visibility gap (TRI-GREATDISCONNECT-2026).

## 5. Sources

Ref | title | publisher | type | URL | date | access. Dates come from article metadata or bylines. Foundation items older than 18 months are marked in the notes.

- `AMBITION-PRICINGADVISOR-2026` | Senior Pricing Advisor in London (Complex Matters and GenAI), recruiter posting for an unnamed global law firm | Ambition (recruiter) | job-posting | https://www.ambition.co.uk/job/senior-pricing-advisor-556300-1770890369 | 2026-02-12 | access: full
- `AMBITION-PRICINGMANAGER-2026` | Pricing Manager - Gen AI in City of London, recruiter posting for an unnamed global law firm | Ambition (recruiter) | job-posting | https://www.ambition.co.uk/job/pricing-manager-gen-ai-556277-1770801372 | 2026-02-11 | access: full
- `ARTLAW-LEGORA-2026` | Legora Seeks 'Centrality' With 30+ Integrations Ecosystem | Artificial Lawyer | press | https://www.artificiallawyer.com/2026/10/15/legora-seeks-centrality-with-30-integrations-ecosystem/ | 2026-10-15 | access: full
- `AT-CROWE-2026` | Crowe launches shared ownership plan | Accounting Today | press | https://www.accountingtoday.com/news/crowe-launches-esop-with-kkr-investment | 2026-10-19 | access: full
- `AT-PWC-2026` | PwC grows 2026 global revenue to $60.2B | Accounting Today | press | https://www.accountingtoday.com/news/pwc-grows-2026-global-revenue-to-60-2b | 2026-10-19 | access: full
- `BLOOMBERGLAW-ACCTG-2026` | AI Efficiency Gains Push Accounting Firms to Reimagine Pricing | Bloomberg Law | press | https://news.bloomberglaw.com/esg/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing | 2026-03-05 | access: full
- `BLOOMBERGLAW-DEBEVOISE-2026` | Debevoise Banks on Partner Loyalty to Build Curated AI Products | Bloomberg Law (Big Law Business, Roy Strom) | press | https://news.bloomberglaw.com/business-and-practice/debevoise-banks-on-partner-loyalty-to-build-curated-ai-products | 2026-08-06 | access: full
- `BLOOMBERGLAW-GCXAI-2026` | GC x AI Retrospective: The Billable Hour, Like a Twinkie, Endures (column by Eric Dodson Greenberg, Cox Media Group; in-house) | Bloomberg Law | press | https://news.bloomberglaw.com/business-and-practice/gc-x-ai-retrospective-the-billable-hour-like-a-twinkie-endures | 2026-10-19 | access: full
- `BLOOMBERGLAW-TEXAS-2026` | AI, Billing Emerge as Crossroads for Texas Law Firms and Clients | Bloomberg Law | press | https://news.bloomberglaw.com/antitrust/ai-billing-emerge-as-crossroads-for-texas-law-firms-and-clients | 2026-04-21 | access: full
- `COLUMBIA-BREYDO-2026` | Private Equity Is Coming for Law Firms - and the Rules Aren't Ready | Columbia Law School Blue Sky Blog (Lev Breydo, William & Mary Law School) | academic | https://clsbluesky.law.columbia.edu/2026/04/30/private-equity-is-coming-for-law-firms-and-the-rules-arent-ready/ | 2026-04-30 | access: full
- `CONSULTANCYUK-BONE-2026` | Faster work doesn't automatically mean a more profitable professional services firm | Consultancy.uk (contributed by Andrew Bone, co-founder and VP of product; employer not stated in the page text) | press | https://www.consultancy.uk/news/45863/faster-work-doesnt-automatically-mean-a-more-profitable-professional-services-firm | 2026-10-15 | access: full
- `CPAPA-PWC-2026` | PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/ | 2026-03-25 | access: full
- `EDISCOVERYTODAY-ILTACON-2026` | My Five ILTACON 2026 Takeaways | eDiscovery Today (Doug Austin) | conference | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 | access: full
- `HBJ-BILLABLE-2026` | AI-driven efficiencies force law, accounting firms to rethink the billable hour | Hartford Business Journal | press | https://hartfordbusiness.com/article/ai-driven-efficiencies-force-law-accounting-firms-to-rethink-the-billable-hour/ | 2026-06-01 | access: full
- `HK-AMLAW-2026` | Firms Need Capital to Pay for AI Tools. Could PE Investment Be the Solution? (In the Headlines summary of an American Lawyer article) | Holland & Knight | firm | https://www.hklaw.com/en/news/intheheadlines/2026/04/firms-need-capital-to-pay-for-ai-tools-could-pe-investment | 2026-04-20 | access: full
- `ICAEW-MIDTIER-2026` | Mid-tier firms focused on AI and consolidation | ICAEW | professional-body | https://www.icaew.com/insights/viewpoints-on-the-news/2026/may-2026/mid-tier-firms-focused-on-ai-and-consolidation | 2026-05-22 | access: full
- `IPA-2026` | Perspectives from the Profession: 2026: The Year Accounting Firms Stop Talking About Change and Start Living It | INSIDE Public Accounting | press | https://insidepublicaccounting.com/2026/01/06/perspectives-from-the-profession-2026-the-year-accounting-firms-stop-talking-about-change-and-start-living-it/ | 2026-01-06 | access: full
- `ISBA-ELEFANT-2026` | The One About Passing AI Costs Through to Clients (MyShingle Ethics Opinion, Carolyn Elefant), Rural Practice newsletter | Illinois State Bar Association | professional-body | https://www.isba.org/node/104199 | 2026-07 | access: full
- `LAWYERIST-607-2026` | The Future of Law Firm Business Models in the Age of AI, with Jordan Furlong (Lawyerist Podcast #607; show notes only) | Lawyerist Podcast | podcast | https://www.castfox.net/podcast/lawyerist-podcast-5099396/episode/the-future-of-law-firm-business-models-in-the-age-of-ai-with-jordan-furlong-381658 | 2026-03-12 | access: full
- `LAWYERSWEEKLY-KEYPOINT-2026` | 'Clients will get annoyed' if firms pass on AI costs, says Keypoint's CEO (standfirst only; premium content) | Lawyers Weekly | press | https://www.lawyersweekly.com.au/biglaw/44659-clients-will-get-annoyed-if-firms-pass-on-ai-costs-says-keypoint-s-ceo | 2026-07-15 | access: search-only
- `LEGALLATENIGHT-49-2026` | Ditching the Billable Hour: Law Firm Math, AI, and Subscriptions with Mathew Kerbis (Legal Late Night ep. 49; show notes only) | Legal Late Night | podcast | https://www.castfox.net/podcast/legal-late-night-7300081/episode/ditching-the-billable-hour-law-firm-math-ai-and-subscriptions-with-mathew-kerbis-1477853 | 2026-04-09 | access: full
- `LEGORA-LAUREL-2026` | Legora and Laurel partner to capture the time lawyers spend in Legora as they work | Legora (press release) | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 | access: full
- `MONDAQ-GGI-2026` | Still Selling Judgment: How Law Firms And Accounting Firms Must Prepare For AI-driven Pricing Change | GGI Global Alliance / Offit Kurman (via Mondaq) | firm | https://www.mondaq.com/unitedstates/management/1814268/still-selling-judgment-how-law-firms-and-accounting-firms-must-prepare-for-ai-driven-pricing-change | 2026-07-09 | access: full
- `NETDOCUMENTS-TOKENOMICS-2026` | Lawyer Tokenomics | NetDocuments ndMAX Studio (Applied AI Team) | vendor | https://studio.netdocuments.com/post/lawyer-tokenomics | 2026-08-12 | access: full
- `RADIANT-TOKEN-2026` | Legal has a token problem, and the industry is just starting to notice (page undated; text refers to June 2026 events) | Radiant Law | firm | https://www.radiantlaw.com/resources/legal-has-a-token-problem-and-the-industry-is-just-starting-to-notice | 2026 | access: full
- `SPI-AI-2026` | The 2026 Impact of AI on Professional Services (survey landing page) | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-10 | access: full
- `STANFORD-DEL-2026` | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives | Stanford Digital Economy Lab (Brynjolfsson, Petropoulos) | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | access: full
- `TRI-CHARGING-2026` | If AI can do the work, then what are you actually charging for? | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/what-are-you-actually-charging-for | 2026-10-02 | access: full
- `TRI-COOCFO-AI-2025` | Law Firm COO & CFO Forum: As law firms push to offer solutions and demonstrate value, will AI get them there? | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/coo-cfo-forum-ai-solutions-demonstrating-value | 2025-11-03 | access: full
- `TRI-COOCFO-MARKET-2025` | Law Firm COO & CFO Forum: As legal market shifts, the big questions still need answers | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/coo-cfo-forum-shifting-legal-market | 2025-10-24 | access: full
- `TRI-GREATDISCONNECT-2026` | The great AI disconnect: Firms and legal departments are not communicating about AI usage | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect | 2026-03-18 | access: full
- `TRI-ILTACON-HOUR-2025` | ILTACON 2025: Pricing the future - AI's impact on the billable hour | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2025-billable-hour | 2025-09-02 | access: full
- `TRI-ILTACON-IMPL-2026` | ILTACON 2026: "Does it make the boat faster?" How legal teams are finding AI implementation success | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-finding-ai-implementation-success | 2026-08-31 | access: full
- `TRI-ILTACON-METER-2026` | Ferraris for emails: At ILTACON 2026, the industry starts reading the meter | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter | 2026-09-09 | access: full
- `TRI-KOPKA-2026` | How one law firm is challenging a broken status quo around billing | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing | 2026-04-30 | access: full
- `TRI-LEGALWEEK-2026` | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | access: full
- `TRI-LEGALWEEK-CRISIS-2026` | Move over, "Death of the billable hour," Legalweek 2026 has found a new existential crisis | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-new-existential-crisis | 2026-03-19 | access: full
- `TRI-LFFI-COSTS-2026` | Q2 2026 LFFI analysis: The rising costs lurking beneath law firm momentum | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/q2-2026-lffi-analysis-rising-costs | 2026-08-31 | access: full
- `TRI-LFFI-ELASTICITY-2026` | Q4 2025 LFFI analysis: What a decade of law firm rate elasticity means for 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/lffi-q4-2025-analysis-rate-elasticity | 2026-03-02 | access: full
- `TRI-LFFI-LEVERAGE-2026` | Q2 2026 LFFI analysis: Law firm leverage just broke a 17-year record - and this time, it's not because of layoffs | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/q2-2026-lffi-analysis-law-firm-leverage | 2026-08-18 | access: full
- `TRI-LFFI-MIDSIZE-2026` | Q1 2026 LFFI analysis: The quiet rate erosion impacting Midsize law firms | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/q1-2026-lffi-analysis-midsize-law-firms | 2026-05-26 | access: full
- `TRI-LFFI-PRODUCTIVITY-2026` | Q1 2026 LFFI analysis: The productivity puzzle and the shift toward value per lawyer | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/q1-2026-lffi-analysis-productivity-puzzle | 2026-06-30 | access: full
- `TRI-LFFI-Q1-2026` | Q1 2026 LFFI: Strong inputs, average output - and the first drops of rain | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output | 2026-05-13 | access: full
- `TRI-LFFI-Q2-2026` | Q2 2026 LFFI: A heavier load, yet a faster crossing | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed | 2026-08-10 | access: full
- `TRI-PRICINGROLES-2024` | Pricing legal technology and the impact on the role of the pricing professional: Changing roles and skills | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/legal-technology-pricing-professionals-changing-roles | 2024-11-19 | access: full
- `TRI-PROSPERITY-2025` | The prosperity paradox: Record rate growth may mask rising vulnerabilities in law firms | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/law-firms-prosperity-paradox | 2025-12-10 | access: full
- `TRI-RATES-2024` | Law Firm Rates in 2024: The Bull, Bear & Base Case for rates and what it means for realization | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/law-firm-rates-bull-bear-base-case | 2024-10-17 | access: full
- `TRI-RETHINKING-2025` | From billable hours to agentic outcomes: Rethinking legal value in the age of AI | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/rethinking-legal-value | 2025-07-15 | access: full
- `TRI-ROI-2025` | Finding a quicker ROI on law firms' investment in AI | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/law-firm-roi-ai-investment | 2025-05-19 | access: full
- `TRI-SOTLM-2026` | State of the US Legal Market 2026 analysis: Will the AI bubble burst? A crucial warning for law firms | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 | access: full
- `TRI-SOTLM-PRICING-2026` | State of the US Legal Market 2026 analysis: How law firms can turn value into pricing power | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/state-of-the-us-legal-market-2026-analysis-value-pricing-power | 2026-01-26 | access: full
- `VANMORGEN-SUPERRETURN-2026` | AI zet private-equityrekensom in accountancy onder druk (AI puts the private-equity sum in accountancy under pressure; reports FT coverage of SuperReturn Berlin) | Accountancy Vanmorgen | press | https://www.accountancyvanmorgen.nl/2026/06/16/ai-zet-private-equityrekensom-in-accountancy-onder-druk/ | 2026-06-16 | access: full
- `WINSTON-PE-2026` | Law firms: The next frontier for private equity in professional services? | Winston & Strawn (client alert, pre-Winston Taylor combination) | firm | https://www.winston.com/en/insights-news/law-firms-the-next-frontier-for-private-equity-in-professional-services | 2026-03-19 | access: full

Count by type (distinct sources listed): academic 2, conference 8, firm 4, job-posting 2, podcast 2, press 17, professional-body 2, survey 14, vendor 2; total 53.

## 6. Gaps

- **No grade A evidence.** No named firm publishes a measured financial result of AI (realization, margin, profit per partner). All "hours saved" figures are recollections or estimates (for example MahoneySabol, 90 to 15 minutes).
- **No quality evidence** (error, override or parallel-run data) for this module; none was expected from conference and press material.
- **Not read or not reachable:** Above the Law (403); Legal Evolution (403); MyShingle original (403, read via the ISBA reprint); Kantata's "Fact or Fiction" outcome-pricing post (link returned 404); Bloomberg Law bodies beyond the free portion (the PE "cash cow" article, headline and opening only); Law.com / American Lawyer article behind the Holland & Knight summary; the FT articles behind the Dutch and CPA Practice Advisor items; Lawyers Weekly Keypoint interview (standfirst only); Hogan Lovells/McKinsey/Wells Fargo primaries; SPI full report (paid); CLOC, AICPA ENGAGE, MCA, PMI and Legal Geek session content (JavaScript-rendered or not reached).
- **Search-only leads, not used for any grade:** posting content for Dentons, Linklaters, Husch Blackwell and McDermott pricing roles; Illinois HB 5487 limits on non-lawyer-owned entities; a CPA Trendlines claim that PE holds stakes in 11 of the 30 largest US accounting firms; Houlihan Lokey's remarks on a *Behind the Buyouts* podcast (24 Jun 2026); Consultancy.uk headline on resourcing decisions eroding margins (14 Oct 2026).
- **Podcasts:** only show notes were read (Lawyerist #607; Legal Late Night ep. 49); audio was not heard.
- **Community discussion** (Reddit, LinkedIn, ALA/ACC forums): none found through the rationed searches.
- **Consulting firm primaries** (McKinsey, BCG, Bain, Deloitte, EY, KPMG, Accenture) on firm-level AI economics were not reachable; consulting evidence relies on a Stanford paper, PwC reports and Consultancy.uk.
- **Partner compensation changes with AI**: no firm-level data found; only intentions (Wipfli, PwC) and opinion.
- **Searches used:** 6 of the rationed web searches (law-firm PE and MSO; accounting PE; accounting pricing; podcasts; pricing job postings; token cost pass-through). All other material came from curl, r.jina.ai and the TRI topic pages.
