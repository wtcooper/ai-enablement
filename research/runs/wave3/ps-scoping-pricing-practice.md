# Scoping and pricing engagements: practice evidence (professional services)

Prepared 2026-10-19. Archetype: professional-services. Module: scoping-pricing. Angle: practice. Method: curl and the r.jina.ai text mirror for pages, `pdftotext` for PDFs, and 8 web searches (the search budget ran out before the last planned search). Every source below was opened and read unless marked otherwise. Quotations are under 25 words.

## 1. Summary

- **What is actually changing.** The public record for this module is mostly about pricing models, not about AI tools that do the estimating. Named firms report moving some work from hours to outcome-linked, fixed-fee, subscription or gain-share structures (McKinsey, PwC, TCS, Cognizant, RSM, RKL, Falcon, Crosby). Tools that help produce the estimate or fee proposal are thinner: one law-firm deployment (Goodwin with PERSUIT benchmarking), PSA vendor agents (Certinia Estimate Creation and SOW Drafter), and pricing-team job postings that name AI use.
- **No grade A.** No named organisation published a measured result for AI-assisted estimating, scoping or pricing. Numbers that exist are vendor-published rates of time saved on adjacent documents (Certinia customers), approximate share-of-fees figures stated by executives (McKinsey about 25%; TCS about 80% of one segment's contracts), or survey headlines (SPI 84.8%). Estimate-versus-actual accuracy, win-rate or margin-recovery data for AI-built estimates was not found anywhere.
- **Clients drive the repricing.** At Legalweek 2026 firms said they were still gathering data on AI savings while clients asked for line-item AI transparency or refused to pay for AI-done work (TRI-LEGALWEEK-2026). Reuters reports IT services clients asking for the same work for 25% to 30% less and providers guaranteeing prices on assumed productivity gains of 70% to 80% (REUTERS-ITSERVICES-2026). The risk side (margin loss on fixed prices set before gains are proven) is stated by providers themselves.
- **Regulators allow flat-fee capture of AI savings but not hidden hours.** California's 2026 guidance says hourly bills must reflect time actually spent and flat fees may build AI savings in; general AI subscriptions are overhead, matter-specific AI costs need disclosure and no markup without informed written consent (CALBAR-GENAI-2026).
- **New roles, not new tools, are the visible workforce signal.** Pricing managers and analysts at McDermott Will & Schulte, Husch Blackwell and Pillsbury are hired to advise partners, build AFA models and use AI and analytics; Greenberg Traurig has a Chief Pricing and Innovation Officer; Goodwin has a Managing Director, Client Value.

Use cases: 17 (A: 0, B: 8, C: 6, D: 3). Sources: 36, all opened (access: full).

## 2. Use cases

```yaml
- id: professional-services-scoping-pricing-01
  archetype: professional-services
  module: scoping-pricing
  title: Law firm benchmarks fixed-fee quotes against anonymised market ranges before pricing a matter
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - expert-judgment
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Pricing teams answer client requests for fixed fees and budgets from internal precedent and judgment, which makes quotes slow to produce and hard to defend as market-tested.
  solution: Goodwin announced a global rollout of PERSUIT's Fixed-Fee Price Benchmarking. The vendor describes it as AI-powered and built on anonymised, aggregated data from historical proposals and matters (subject to minimum data thresholds). It returns a range of typical fixed fees for comparable scopes. The vendor says it does not set or recommend prices; lawyers and the pricing team still decide.
  outcomes:
  - lever: speed
    description: Goodwin says it can respond to pricing and budgeting requests more quickly and give clients confidence that fees are market-tested. No measurement was published.
    figure: none
    measures: n/a (qualitative statement by Goodwin's Managing Director, Client Value)
    provenance: self-reported
    source_ref: GOODWIN-PERSUIT-2025
  prerequisites:
  - Enough historical proposal and matter data in the vendor dataset to clear its minimum thresholds for the scope in question
  - A pricing function (Goodwin names a Managing Director, Client Value) that owns the fixed-fee quoting process
  risks_and_guardrails:
  - Benchmarks are shown as ranges and never reveal firm- or client-specific pricing; the vendor states it does not set or recommend prices [GOODWIN-PERSUIT-2025, body]
  - Per the press release, firms and clients can both access the same benchmark data, so it may narrow rather than widen a firm's pricing advantage [GOODWIN-PERSUIT-2025, VP quote]
  human_checkpoints:
  - Lawyers and pricing staff choose the price within or outside the range; the client negotiates independently
  role_evolution: Pricing and client-value roles gain a data input to partner conversations; Goodwin's release names a Managing Director, Client Value as its spokesperson [GOODWIN-PERSUIT-2025].
  evidence_grade: B
  sources:
  - ref: GOODWIN-PERSUIT-2025
    title: Goodwin Advances Legal Pricing with Global Rollout of PERSUIT's Fixed Fee Benchmarking
    publisher: Goodwin Procter LLP (press release)
    type: firm
    url: https://www.goodwinlaw.com/en/news-and-events/news/2025/12/announcements-otherindustries-goodwin-advances-legal-pricing-with-global-rollout
    date: '2025-12-17'
    access: full
    locator: Press release body (all four paragraphs)
  - ref: LTHUB-PERSUIT-2026
    title: PERSUIT vendor profile (read 2026-10-19)
    publisher: Legaltech Hub
    type: vendor
    url: https://www.legaltechnologyhub.com/vendors/persuit/
    date: 2026-10
    access: full
    locator: Vendor profile paragraph
  notes: Single press release is the only evidence of use; no accuracy, adoption or time-saving data. Rollout wording is 'roll out ... on a global scale' (dated 2025-12-17); extent of lawyer use inside Goodwin is not stated. The 'AI-powered' label is the press release's; the model behind the benchmark is not described.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-02
  archetype: professional-services
  module: scoping-pricing
  title: In-house team scopes matters, structures alternative fees and compares law firm proposals with AI support (in-house)
  function: procurement-supply-chain
  work_types:
  - research-synthesis
  - document-production
  pattern: document-to-decision
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Corporate legal departments compare outside-counsel fee proposals by hand, and AI-driven efficiency makes hourly estimates harder to judge.
  solution: PERSUIT (a platform for corporate legal departments) supports matter scoping, alternative fee structuring, rate benchmarking and RFP workflows. Its profile lists a generative AI proposal-analysis tool that helps legal teams evaluate and compare law firm submissions. [In-house example.]
  outcomes:
  - lever: speed
    description: none published
    figure: none
    measures: n/a
    source_ref: LTHUB-PERSUIT-2026
  prerequisites:
  - A competitive RFP or panel process for outside counsel
  - Historical proposal data for benchmarking (vendor-held)
  risks_and_guardrails:
  - Vendor-described capability only; no named in-house customer, accuracy data or error rates were found
  human_checkpoints:
  - Legal department decision-makers choose firms and approve fee structures (not described in the source; stated here as the normal path)
  role_evolution: Legal operations teams take on fee structuring and proposal evaluation as data tasks; the source does not describe changes in roles.
  evidence_grade: C
  sources:
  - ref: LTHUB-PERSUIT-2026
    title: PERSUIT vendor profile (read 2026-10-19)
    publisher: Legaltech Hub
    type: vendor
    url: https://www.legaltechnologyhub.com/vendors/persuit/
    date: 2026-10
    access: full
    locator: Vendor profile paragraph
  - ref: GOODWIN-PERSUIT-2025
    title: Goodwin Advances Legal Pricing with Global Rollout of PERSUIT's Fixed Fee Benchmarking
    publisher: Goodwin Procter LLP (press release)
    type: firm
    url: https://www.goodwinlaw.com/en/news-and-events/news/2025/12/announcements-otherindustries-goodwin-advances-legal-pricing-with-global-rollout
    date: '2025-12-17'
    access: full
    locator: 'Quote from PERSUIT VP: both sides can access the same data'
  notes: 'Tag: in-house. Grade C because the evidence is a directory description of vendor features. The Goodwin release is the only named customer and it is a law firm (see 01).'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-03
  archetype: professional-services
  module: scoping-pricing
  title: Law firm pricing teams use AI and analytics to estimate matters, forecast profitability and model alternative fees (job-posting evidence)
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Pricing analysts build matter budgets, estimates and alternative-fee models largely in spreadsheets from historical billing data.
  solution: Three US firms' pricing job postings ask staff to use AI or analytics in this work. McDermott Will & Schulte's Pricing Manager is to use AI and data analytics tools to identify pricing trends and forecast matter profitability. Husch Blackwell's Senior Pricing Analyst is to leverage AI-powered tools to improve forecasting, to evaluate and implement AI-driven tools for predictive pricing and cost estimation, and to research AI's effect on pricing models. Pillsbury's Pricing Analyst role lists experience configuring AI tools as desirable.
  outcomes:
  - lever: quality
    description: none published
    figure: none
    measures: n/a
    source_ref: HUSCH-JOB-2026
  prerequisites:
  - Time-and-billing and pricing systems the tools can read (postings name Elite 3E, Iridium, Aderant and Clocktimizer)
  - Historical matter data and a pricing repository
  risks_and_guardrails:
  - Postings describe expectations of the role, not tools in production or results [HUSCH-JOB-2026; MCDERMOTT-JOB-2026]
  human_checkpoints:
  - Pricing managers advise partners on pricing strategy and structure; partners own the client conversation [MCDERMOTT-JOB-2026]
  role_evolution: Pricing roles combine financial modelling with AI-tool use and advisory work with partners; Husch Blackwell's posting also asks the analyst to train attorneys on pricing technology [HUSCH-JOB-2026].
  evidence_grade: C
  sources:
  - ref: MCDERMOTT-JOB-2026
    title: Pricing Manager (job posting, read 2026-10-19; posting date not shown)
    publisher: McDermott Will & Schulte via Built In NYC
    type: job-posting
    url: https://www.builtinnyc.com/job/pricing-manager/10074034
    date: 2026-10
    access: full
    locator: Responsibilities list, final bullet
  - ref: HUSCH-JOB-2026
    title: Senior Pricing Analyst (job posting, read 2026-10-19; posting date not shown)
    publisher: Husch Blackwell LLP via Built In Austin
    type: job-posting
    url: https://www.builtinaustin.com/job/senior-pricing-analyst/9648474
    date: 2026-10
    access: full
    locator: 'Essential job functions: AI-related bullets'
  - ref: PILLSBURY-JOB-2026
    title: Pricing Analyst, Nashville (job posting, read 2026-10-19; posting date not shown)
    publisher: Pillsbury Winthrop Shaw Pittman via Talentify
    type: job-posting
    url: https://www.talentify.io/pricing-analyst-nashville-us-pillsbury-winthrop-shaw-pittman
    date: 2026-10
    access: full
    locator: Summary and 'Required education, knowledge and experience'
  notes: 'Grade note: the vocabulary has no grade for job-posting-only evidence. Postings show a named firm expects AI use in pricing work, but not which tool, what it does or what results it gives, so scored C (not B). Posting dates are not shown on the pages read (read 2026-10-19). Postings were opened on aggregator sites, not the firms'' careers pages.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-04
  archetype: professional-services
  module: scoping-pricing
  title: AI computes flat fees from a firm's own historical invoices and billing data
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Firms hesitate to quote fixed fees because they cannot easily see what comparable work has cost them in billed time.
  solution: August's Genius Mode takes uploaded invoices, accounting documents and prior client bills, calculates flat fees based on billable hours, builds a branded presentation from the firm's materials and a spreadsheet of client insights to support a client-facing email, per the vendor's demo summary.
  outcomes:
  - lever: speed
    description: none published
    figure: none
    measures: n/a
    source_ref: ARTLAW-AUGUST-2026
  prerequisites:
  - Accessible prior invoices and billing records for comparable work
  risks_and_guardrails:
  - Fees derived from historical billable hours inherit past inefficiency and carry no allowance for AI-driven change unless the lawyer adjusts them (inference from the source's method; the source does not discuss this)
  human_checkpoints:
  - A lawyer drafts and sends the client email; the source describes the output as equipping the lawyer
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: ARTLAW-AUGUST-2026
    title: 'Product Walk Through: August - Genius Mode'
    publisher: Artificial Lawyer (vendor-supplied demo)
    type: press
    url: https://www.artificiallawyer.com/2026/04/15/product-walk-through-august-genius-mode/
    date: '2026-04-15'
    access: full
    locator: Article body (August explanation quote)
  notes: Vendor-supplied demo on Artificial Lawyer (2026-04-15). August's named firm customer in the same article (Hughes Hubbard & Reed) is quoted on firmwide deployment, not on this feature. No error or accuracy data.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-05
  archetype: professional-services
  module: scoping-pricing
  title: AI-native law firms sell fixed-price bundles or per-document rates instead of hours
  function: service-delivery
  work_types:
  - document-production
  - review-assurance
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: Routine commercial contract work is priced by the hour at traditional firms, which Falcon's founders say can cost SMEs EUR 3,000 to 4,000 per piece of straightforward work and take days or weeks.
  solution: Falcon (Belgium; co-founded by former Allen & Overy senior partner Wim Dejonghe; reported 2026-10-02) offers review of six contracts a month for a flat EUR 1,000, each signed off by a qualified lawyer and returned the same day. Crosby's site advertises fixed rates by the document, with human attorneys reviewing all work and malpractice insurance carried. Non-Billable also names Moritz and Blackstone-backed Norm Law as AI-native firms.
  outcomes:
  - lever: cost
    description: Falcon states its flat price; the founders' comparison figure is their own estimate of traditional-firm cost.
    figure: EUR 1,000 per month for six contracts (Falcon); EUR 3,000-4,000 per straightforward piece of work at a traditional firm (founders' estimate)
    measures: Falcon's published offer price; founders' statement of what straightforward commercial work 'could cost' at a traditional firm. Not a measured outcome.
    provenance: self-reported
    source_ref: NONBILLABLE-FALCON-2026
  prerequisites:
  - Standardised, high-volume document types (Falcon starts with NDAs, data processing agreements, customer and supplier agreements)
  - Qualified lawyer sign-off on each piece of work
  risks_and_guardrails:
  - Fixed price puts delivery-cost risk on the firm; neither source discloses delivery cost or margin
  - Crosby states it carries full malpractice insurance [CROSBY-SITE-2026]
  human_checkpoints:
  - Qualified lawyer signs off each piece of work (Falcon); human attorneys review all work (Crosby)
  role_evolution: Lawyers act as reviewers and agent managers per Crosby's site; Falcon keeps 'a qualified lawyer accountable for every piece of work' (founder quote) [NONBILLABLE-FALCON-2026; CROSBY-SITE-2026].
  evidence_grade: B
  sources:
  - ref: NONBILLABLE-FALCON-2026
    title: Former A&O boss launches AI-native law firm, minus the billable hour
    publisher: Non-Billable
    type: press
    url: https://www.nonbillable.co.uk/news/wim-dejonghe-launches-ai-native-law-firm-falcon
    date: '2026-10-02'
    access: full
    locator: Opening paragraphs, founder-cost paragraph, and AI-native firms paragraph
  - ref: CROSBY-SITE-2026
    title: 'Crosby: The Agentic Law Firm Built for Execution (home page, read 2026-10-19)'
    publisher: Crosby
    type: firm
    url: https://www.crosby.ai/
    date: 2026-10
    access: full
    locator: '''Don''t buy hours. Buy outcomes. Fixed rates by the document'' section; ''Human attorneys review all work'''
  notes: Falcon is newly launched (announced); Crosby is selling now but publishes no prices or usage data on the page read. Garfield.Law (SRA-authorised, claims up to 10,000 GBP) was opened but no price was visible, so it is not used. No quality, margin or volume figures for any of these firms.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-06
  archetype: professional-services
  module: scoping-pricing
  title: Big Four firm packages expertise into AI-delivered services priced by subscription or consumption instead of hours
  function: product-service-development
  work_types:
  - expert-judgment
  - document-production
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: Hourly billing ties the firm's revenue to staff time that AI is compressing, and PwC's US CEO says some services can run without a person in the loop.
  solution: PwC introduced PwC One on 2026-03-19, 'currently being introduced' in select US teams and client engagements. Per the FT as reported by CPA Practice Advisor, it offers clients access to six automated services, with more promised, and some tax and consulting services may be converted into AI-powered tools clients access directly 'without a PwC person in the loop', potentially paid by annual subscription. Stanford's paper cites the FT interview as indicating subscription or consumption pricing in some cases.
  outcomes:
  - lever: growth
    description: none published
    figure: none
    measures: n/a
    source_ref: PWC-ONE-2026
  prerequisites:
  - Productisable service content (PwC cites proprietary methodologies, compliance frameworks and domain expertise)
  - Client-facing platform and security/data-privacy controls (per the press release)
  risks_and_guardrails:
  - PwC's release frames the AI as working under professional oversight and says it amplifies rather than replaces judgment [PWC-ONE-2026]
  - The press release gives no pricing specifics; pricing detail comes only from FT-sourced reporting [PWC-ONE-2026; STANFORD-DEL-2026 section 5.2]
  human_checkpoints:
  - Not described for the subscription tools; the release says professional oversight remains in the platform
  role_evolution: PwC's US CEO said partners who resist AI 'have no place at the firm' (CPAPA/FT) and that senior staff unwilling to be AI-first would probably be replaced [CPAPA-PWC-2026].
  evidence_grade: B
  sources:
  - ref: PWC-ONE-2026
    title: PwC Introduces PwC One as Part of Its Vision for AI-Enabled Professional Services
    publisher: PwC US newsroom
    type: firm
    url: https://www.pwc.com/us/en/about-us/newsroom/press-releases/pwc-one.html
    date: '2026-03-19'
    access: full
    locator: 'Press release: opening paragraph and the paragraph stating PwC One is being introduced in select teams'
  - ref: CPAPA-PWC-2026
    title: PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' (reporting the Financial Times)
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
    date: '2026-03-25'
    access: full
    locator: 'Article body: Griggs FT paragraphs and the paragraph on six automated services'
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives (Brynjolfsson and Petropoulos)'
    publisher: Stanford Digital Economy Lab
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section 5.2 (pp.16-17)
  notes: No published price, uptake or client results. Landscape file had PwC One launch with 'six automated services'; that count is from the FT via CPA Practice Advisor, not from PwC's own release.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-07
  archetype: professional-services
  module: scoping-pricing
  title: Management consultancy ties a share of fees to client outcomes as AI cuts billable effort
  function: sales-marketing-bd
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: AI compresses the analytical work the billable hour prices, making hours a weaker proxy for value; clients increasingly arrive with a result they want rather than a defined scope.
  solution: McKinsey's UK managing partner said in a November 2025 briefing that the firm is doing more performance-based arrangements, and McKinsey disclosed that roughly a quarter of global fees come from outcome-based pricing (as reported by Business Insider, cited by Stanford, and by AI Weekly summarising the WSJ). A May 2026 FT/City AM summary instead says roughly a third of McKinsey's work is tied to performance-based fees.
  outcomes:
  - lever: growth
    description: Share of global fees from outcome-based pricing, as stated by McKinsey and reported in the press.
    figure: about 25%
    measures: Share of McKinsey's global fees that come from outcome-based pricing, per reporting from late 2025 (AI Weekly summary of WSJ; Stanford citing Business Insider). A different secondary source says roughly a third of work.
    provenance: self-reported
    source_ref: AIWEEKLY-MCK-2026
  prerequisites:
  - Measurable client outcomes and agreed baselines (the source notes mechanics are not spelled out)
  - 'Stanford''s rule: measurement infrastructure before outcome-linked pricing; attribution can still bind [STANFORD-DEL-2026 section 7, rule 3]'
  risks_and_guardrails:
  - The reporting does not say how baselines are set, who judges whether a target was hit, or whether partner pay changes [AIWEEKLY-MCK-2026]
  - Figures come from firm statements at media events, not audited disclosures [AIWEEKLY-MCK-2026]
  human_checkpoints:
  - Not described
  role_evolution: Not described in the sources beyond partner-led negotiation; Stanford notes outcome pricing spreads only as far as attribution is clean.
  evidence_grade: B
  sources:
  - ref: AIWEEKLY-MCK-2026
    title: McKinsey Ties 25% of Fees to Outcomes as AI Erodes Billable Hours (summary of a WSJ report)
    publisher: AI Weekly
    type: press
    url: https://aiweekly.co/alerts/mckinsey-ties-25-of-fees-to-outcomes-as-ai-erodes-billable-hours
    date: '2026-06-29'
    access: full
    locator: TL;DR bullet 1; McKinsey paragraph; caveat paragraph
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives (Brynjolfsson and Petropoulos)'
    publisher: Stanford Digital Economy Lab
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section 5.1 (p.14)
  - ref: RESULTSENSE-2026
    title: AI dismantles consulting scale advantage as boutiques target Big Four (summary of FT and City AM)
    publisher: Resultsense
    type: press
    url: https://www.resultsense.com/news/2026-05-28-ai-consulting-big-four-reckoning/
    date: '2026-05-28'
    access: full
    locator: Paragraph beginning 'Three structural pillars' ('roughly a third')
  - ref: FORRESTER-BLOG-2025
    title: The Future Of AI Consulting Services Is Disruptively Bright (analyst blog)
    publisher: Forrester
    type: press
    url: https://www.forrester.com/blogs/the-future-of-ai-consulting-services-is-disruptively-bright
    date: '2025-09-15'
    access: full
    locator: Bullet 'Modify their economic models to share more risk'
  notes: 'Grade B, not A: the primary source (McKinsey''s own briefing / Business Insider / WSJ) was not opened; the figure is a disclosed approximate share relayed by secondary summaries, and one secondary source gives a conflicting ''a third''. BCG (AI-tied work about 20% of 2024 revenue, 40% projected by 2026) and Bain (about 30% of consulting business, projected toward 50%) figures in the same summary are AI-work share, not pricing, and are excluded from outcomes.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-08
  archetype: professional-services
  module: scoping-pricing
  title: IT services providers move contracts from hours to outcome measures and pass AI productivity to clients
  function: sales-marketing-bd
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Clients demand price cuts and more productivity as AI lifts delivery efficiency, and the billable-hour model for large offshore workforces loses its logic.
  solution: Reuters (2026-08-21) reports TCS, Infosys, Wipro, HCLTech and Cognizant are increasingly tying fees to performance outcomes instead of hours worked. TCS's CEO told Reuters about 80% of contracts in its finance, human resources and other business services segment are now based on outcome performance measures. Persistent's CEO said clients were demanding the same work for 25% to 30% less. Accenture was reported on 2026-10-01 to have said its prices were lower in many areas.
  outcomes:
  - lever: cost
    description: Share of contracts in one TCS segment that use outcome performance measures.
    figure: about 80%
    measures: Share of TCS contracts within its finance, human resources and other business services segment that are based on outcome performance measures, as stated by TCS's CEO to Reuters. The doubling since late 2023 comes from an unnamed person with knowledge of the matter.
    provenance: self-reported
    source_ref: REUTERS-ITSERVICES-2026
  - lever: cost
    description: Client price expectation reported by a provider.
    figure: 25% to 30% less
    measures: 'What Persistent Systems'' CEO said clients were demanding: the same work for 25% to 30% less, with faster delivery. A demand statement, not a realised price change.'
    provenance: self-reported
    source_ref: REUTERS-ITSERVICES-2026
  prerequisites:
  - Contractable outcome metrics in the client's operations (TCS segment is business-process work)
  - 'Enough new work to offset deflation: TCS''s CEO said so far it has offset the AI-related downward pressure on revenue with new work'
  risks_and_guardrails:
  - Tech Mahindra's CEO said some rivals factor in productivity gains of 70% to 80% over five to seven years and guarantee prices, and that his company chose not to take that risk [REUTERS-ITSERVICES-2026]
  - Infosys told analysts it walked away from contracts that were no longer economically viable [REUTERS-ITSERVICES-2026]
  human_checkpoints:
  - Not described
  role_evolution: TCS is increasing engineers embedded with clients; executives say traditional hiring of large entry-level cohorts may wind down (former Infosys CFO quoted) [REUTERS-ITSERVICES-2026].
  evidence_grade: B
  sources:
  - ref: REUTERS-ITSERVICES-2026
    title: AI reshapes India's IT services sector contracts as clients demand more for less (Reuters, syndicated copy)
    publisher: Reuters via WHBL
    type: press
    url: https://whbl.com/2026/08/20/ai-reshapes-indias-it-services-sector-contracts-as-clients-demand-more-for-less/
    date: '2026-08-21'
    access: full
    locator: Opening paragraphs; TCS CEO passage; Persistent, Tech Mahindra, Infosys passages; closing paragraphs
  - ref: RESULTSENSE-ACCENTURE-2026
    title: Accenture's forecast lifts IT services stocks hit by AI fears (summary of Reuters)
    publisher: Resultsense
    type: press
    url: https://www.resultsense.com/news/2026-10-02-accenture-forecast-it-services-rally/
    date: '2026-10-02'
    access: full
    locator: Paragraph 1 and commentary paragraph on price cuts
  notes: 'Grade B not A: the 80% is a CEO''s approximate statement in an interview, not a published tracked metric. Accenture ''lower prices'' is a secondary summary of Reuters; the Accenture primary statement was not opened. IT outsourcing is adjacent to professional-services consulting; included because the pricing response is the same mechanism.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-09
  archetype: professional-services
  module: scoping-pricing
  title: Outsourcing deals split AI-driven savings or defer payment until efficiency is proven
  function: sales-marketing-bd
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Clients want AI efficiency reflected in what they pay, and providers need a way to share the benefit without giving away margin.
  solution: Reuters, citing people familiar with the terms, says a February 2026 AI and automation deal between Cognizant and Daimler Truck stipulates that AI-related cost savings are split between vendor and client, and that a June 2025 cloud management deal between HCLTech and E.ON means HCLTech is not paid in year one, with payments from year two tied to efficiency gains and business outcomes.
  outcomes:
  - lever: cost
    description: none published
    figure: none
    measures: n/a
    source_ref: REUTERS-ITSERVICES-2026
  prerequisites:
  - Agreed baseline of current cost and a method to attribute savings to AI (not described in the source)
  risks_and_guardrails:
  - Terms are reported by unnamed sources; Cognizant declined to comment on specific contracts [REUTERS-ITSERVICES-2026]
  - 'Stanford: attribution risk is not removed by measurement, so outcome-linked components need clean attribution [STANFORD-DEL-2026 section 7, rule 3]'
  human_checkpoints:
  - Not described
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: REUTERS-ITSERVICES-2026
    title: AI reshapes India's IT services sector contracts as clients demand more for less (Reuters, syndicated copy)
    publisher: Reuters via WHBL
    type: press
    url: https://whbl.com/2026/08/20/ai-reshapes-indias-it-services-sector-contracts-as-clients-demand-more-for-less/
    date: '2026-08-21'
    access: full
    locator: Paragraphs on Cognizant-Daimler Truck and HCLTech-E.ON
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives (Brynjolfsson and Petropoulos)'
    publisher: Stanford Digital Economy Lab
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section 7, rule 3 (pp.21-22)
  notes: Grade C because the contract terms rest on anonymous sources and the named parties did not confirm them in the article. No outcome data.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-10
  archetype: professional-services
  module: scoping-pricing
  title: Accounting and advisory firms pilot value-based and mixed pricing as AI shortens the hours behind a deliverable
  function: finance-accounting
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: AI can halve the time to produce a client report, forcing a choice between keeping the saving as margin or passing it to the client as a lower price.
  solution: Bloomberg Law (2026-03-05) reports KPMG, PwC and RSM are developing pricing models based on value and outcomes. RSM's enterprise digital leader gave an example of tax advisory reports falling from 20 hours to 10 with generative AI and checking, and said RSM can cut prices in some areas but not others and uses multiple pricing models. PwC's tax leader said early brainstorming may suit time-based pricing and later phases value-based. RKL is piloting an alternative value-based model created by consultancy Fore LLC and has onboarded several dozen clients on it.
  outcomes:
  - lever: growth
    description: Clients onboarded under RKL's pilot of a value-based pricing model.
    figure: several dozen
    measures: Number of new clients RKL says it onboarded under the alternative pricing model created by Fore LLC, as quoted from an RKL partner.
    provenance: self-reported
    source_ref: BLOOMBERGLAW-ACCTPRICING-2026
  - lever: cost
    description: Illustrative time saving given by RSM.
    figure: 20 hours to 10 hours
    measures: An RSM partner's example of the time to create certain tax advisory reports with generative AI and checking; offered as an illustration, not a measured study.
    provenance: self-reported
    source_ref: BLOOMBERGLAW-ACCTPRICING-2026
  prerequisites:
  - Compensation and performance metrics that do not reward hours billed (Wipfli's practice chief said metrics from a decade ago conflict with AI adoption)
  - 'Cost tracking: KPMG''s vice chair noted AI investment cost cannot usually be attributed to individual projects'
  risks_and_guardrails:
  - Firms differ on whether to pass savings to clients; RSM said it can cut price in some areas but not in others [BLOOMBERGLAW-ACCTPRICING-2026]
  human_checkpoints:
  - Partners negotiate price with each client; PwC's tax leader described asking whether a fee is a fair price for value generated
  role_evolution: Firm leaders say AI frees time for advisory work; AICPA's firm-services lead says client advisory work suits value-based models [BLOOMBERGLAW-ACCTPRICING-2026].
  evidence_grade: B
  sources:
  - ref: BLOOMBERGLAW-ACCTPRICING-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: 'Article body: opening paragraphs; RSM, KPMG, PwC, RKL, AICPA and Wipfli passages'
  notes: 'Context datum: AICPA 2025 survey of more than 1,000 firms (most with net client fees below USD 5 million) found median net hourly billing rate rose nearly 7% over two years to USD 170 and recommended firms consider accelerating the move away from hourly billing (as reported by Bloomberg Law; AICPA report not opened).'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-11
  archetype: professional-services
  module: scoping-pricing
  title: PSA estimation agent builds engagement estimates grounded in actuals from prior projects
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - document-production
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Estimates for services engagements are built from templates or judgment, which Certinia says leaves cost and risk exposure uncaught and margin lost.
  solution: Certinia's Veda suite lists an Estimate Creation Agent (builds complex estimates and manages creation workflows) and an Estimation Agent (tracks complex estimates alongside tied expenses and risks). The page says estimates and pricing are grounded in the actuals of prior engagements rather than templates or gut instinct.
  outcomes:
  - lever: speed
    description: Vendor headline on its page for time to create a proposal or SOW; not specific to the estimate agent and no customer named.
    figure: 8 hours to 1 hour
    measures: Time to create a proposal or SOW, as labelled on Certinia's page; baseline, sample and customer not stated.
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Salesforce-native Certinia PSA holding prior engagement actuals (the agents run on engagement context)
  - Clean historical project and cost data
  risks_and_guardrails:
  - No accuracy or estimate-versus-actual data published for the agents
  - Certinia advises customers to baseline documentation and admin time before deploying agents [CERTINIA-CUSTOMERS-2026]
  human_checkpoints:
  - Not described
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: agentic intelligence for professional services (solutions page, read 2026-10-19)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: 2026-10
    access: full
    locator: Agent list ('Estimate Creation Agent', 'Estimation Agent'); 'Protect margin before it's lost'; 'More gains across the lifecycle'
  - ref: CPAPA-CERTINIA-2026
    title: Certinia Unveils Veda, an AI Operations Engine for Professional Services
    publisher: CPA Practice Advisor
    type: press
    url: https://www.cpapracticeadvisor.com/2026/04/15/certinia-unveils-veda-an-ai-operations-engine-for-professional-services/181702/
    date: '2026-04-15'
    access: full
    locator: Launch article quote on 'estimation and resourcing'
  notes: Veda launch reported 2026-04-15. A search found no published customer figure specific to the estimation agents. The 11-23% margin and ~50% admin figures on the page are unattributed vendor claims and are not used.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-12
  archetype: professional-services
  module: scoping-pricing
  title: Agent drafts the statement of work from sales context, handing scope to delivery
  function: sales-marketing-bd
  work_types:
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Sales and delivery teams re-key deal context into statements of work by hand, slowing proposals and weakening the handoff.
  solution: Certinia's SOW Drafter Agent generates a Statement of Work from project context; its page says SOWs are produced directly from sales context so delivery starts aligned. Certinia's customer blog says Neocol brought its entire sales team live on a SOW-drafting workflow within nine days of launch.
  outcomes:
  - lever: speed
    description: Neocol rollout speed (no drafting-time measurement published).
    figure: nine days
    measures: Time from launch to the whole Neocol sales team being live on the SOW-drafting workflow, per Certinia's customer blog.
    provenance: vendor-published
    source_ref: CERTINIA-CUSTOMERS-2026
  prerequisites:
  - Sales and delivery data in one Salesforce-native PSA
  - Defined SOW templates and approval path
  risks_and_guardrails:
  - No quality data (errors, rework, legal review rates) published for drafted SOWs
  human_checkpoints:
  - Not described; Certinia's page calls outputs 'polished' drafts
  role_evolution: Not described.
  evidence_grade: B
  sources:
  - ref: CERTINIA-CUSTOMERS-2026
    title: Certinia Customers Are Proving Veda AI Agents Deliver Real Results (blog; no byline date shown, refers to Dreamforce 14-17 Sep 2026 as upcoming)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/blog/certinia-customers-are-proving-veda-ai-agents-deliver-real-results/
    date: '2026'
    access: full
    locator: '''The results don''t stop at just two customers'' list, Neocol bullet'
  - ref: CERTINIA-VEDA-2026
    title: 'Veda AI: agentic intelligence for professional services (solutions page, read 2026-10-19)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: 2026-10
    access: full
    locator: SOW Drafter Agent entry; 'Seamless sales, handoff and alignment'
  notes: Named deployment, vendor-published. The only drafting-time figure (8 hours to 1 hour for proposal or SOW) is an unattributed page headline and is recorded under 11, not here.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-13
  archetype: professional-services
  module: scoping-pricing
  title: Consultancy automates pre-sale requirements capture and solution-architecture drafting, shortening scoping documents
  function: sales-marketing-bd
  work_types:
  - document-production
  - research-synthesis
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Senior consultants spend hours writing technical plans and turning transcripts and requirements into scope documents instead of working with clients.
  solution: Per Certinia's customer blog, Spaulding Ridge cut solution-architecture drafting time from roughly 80 hours to under 20, and Diabsolut says it automated 'transcripts, requirements, backlogs, and scoping' with Veda agents in Slack, cutting documentation time 70%. Certinia's blog summary says Diabsolut is shifting to fixed-fee, outcomes-based contracts; the body text describes time-and-materials contracts not matching client conversations.
  outcomes:
  - lever: speed
    description: Solution-architecture drafting time at Spaulding Ridge.
    figure: roughly 80 hours to under 20
    measures: Hours to draft a solution architecture, per Certinia's customer blog; sample size and method not stated.
    provenance: vendor-published
    source_ref: CERTINIA-CUSTOMERS-2026
  - lever: speed
    description: Documentation time at Diabsolut.
    figure: 70% cut
    measures: Reduction in documentation time at Diabsolut after deploying Veda agents; baseline and method not stated.
    provenance: vendor-published
    source_ref: CERTINIA-CUSTOMERS-2026
  prerequisites:
  - Meeting transcripts and requirements captured in the PSA/Slack environment
  - Baseline of documentation time (Certinia's own advice)
  risks_and_guardrails:
  - Solution architecture and documentation are adjacent to, not the same as, estimating or pricing; the figures do not measure estimate accuracy or win rate
  human_checkpoints:
  - Diabsolut says outcomes architects focus on outcomes rather than paperwork; review steps not described
  role_evolution: Diabsolut's quoted architecture director says automation freed 'outcomes architects' to focus on outcomes, not paperwork [CERTINIA-CUSTOMERS-2026].
  evidence_grade: B
  sources:
  - ref: CERTINIA-CUSTOMERS-2026
    title: Certinia Customers Are Proving Veda AI Agents Deliver Real Results (blog; no byline date shown, refers to Dreamforce 14-17 Sep 2026 as upcoming)
    publisher: Certinia
    type: vendor
    url: https://certinia.com/blog/certinia-customers-are-proving-veda-ai-agents-deliver-real-results/
    date: '2026'
    access: full
    locator: Diabsolut section (paragraphs 2-3); 'Spaulding Ridge' bullet; summary bullets
  notes: 'Grade capped at B: figures are vendor-published and measure an adjacent process (documentation and solution-architecture drafting), not pricing or estimating. A search summary attributed the 80-to-20-hour result to a different tool in another profile; the vendor''s own blog attributes it to Certinia agents. Treat attribution as unresolved.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-14
  archetype: professional-services
  module: scoping-pricing
  title: Firm plans how to reprice or resell the hours AI frees, rather than losing them as unbilled time
  function: finance-accounting
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: AI saves delivery time, but if price stays tied to hours the saving is lost or handed to the client, and few firms turn saved hours into revenue.
  solution: 'SPI Research''s 2026 study of 245 professional services firms treats this as ''the leak'': it reports that 84.8% of firms say AI saves them time against a (gated) share saying it generates revenue, and sells the report as guidance on how to reprice or resell the hours AI saves. Practitioner commentary describes the same choice: RSM asks whether a halved task is ''all margin'' or ''all price reduction''.'
  outcomes:
  - lever: capacity
    description: Share of surveyed firms saying AI saves them time.
    figure: 84.8%
    measures: Share of the 245 surveyed professional services organisations that say AI saves them time (SPI landing page, 'The Leak'). The comparison figure for those saying AI generates revenue is gated and shows as a placeholder.
    provenance: independent
    source_ref: SPI-AI-2026
  prerequisites:
  - Matter- or project-level cost and time tracking to know what the saved hours were worth (SPI says profit goes only to firms with four foundations; the foundations are behind the paywall)
  risks_and_guardrails:
  - 'Cal Bar guidance: hourly billing must reflect time actually spent, so savings cannot be hidden inside hours; flat fees may build AI savings into rates [CALBAR-GENAI-2026, Rule 1.5 row]'
  human_checkpoints:
  - Partners and pricing leads decide whether savings become margin or price reduction
  role_evolution: Not described in the free portion of the report.
  evidence_grade: C
  sources:
  - ref: SPI-AI-2026
    title: The 2026 Impact of AI on Professional Services (report landing page; 245 firms; report listed as published Oct 2026, page dated July 2026)
    publisher: SPI Research
    type: survey
    url: https://spiresearch.com/reports/2026-ai-professional-services-survey/
    date: '2026-07-14'
    access: full
    locator: '''Part III: The Leak'' and ''Protect margin as AI saves time'''
  - ref: BLOOMBERGLAW-ACCTPRICING-2026
    title: AI Efficiency Gains Push Accounting Firms to Reimagine Pricing
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing
    date: '2026-03-05'
    access: full
    locator: RSM partner quote on margin versus price reduction
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version replacing Nov 2023)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Table row 'Charging for Work Produced by Generative AI and Generative AI Costs', p.8
  notes: 'Grade C: survey headline from a paid report; the revenue-side figure and method were not accessible. The 43.6% of projects using AI (23.1% in 2025) is the same study''s adoption headline.'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-15
  archetype: professional-services
  module: scoping-pricing
  title: 'Idea: firms give clients matter-level evidence of AI savings to anchor fee and value-sharing conversations (client-side demand also noted from in-house)'
  function: sales-marketing-bd
  work_types:
  - data-reporting
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Clients ask how AI generates savings on their matters; firm panellists at Legalweek 2026 said they were still gathering the data and described return measurement as anecdotal and based on conventional wisdom.
  solution: Panellists discussed clients asking for line-item invoice transparency on whether AI was used and how much time or money it saved; GSK's chief of staff (in-house) said GSK wants to partner with outside firms on use cases and measuring savings; DLA Piper's AI innovation head advised firms to lead the AI-ROI conversation rather than wait for the client to set terms.
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: n/a
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - Time and cost data at matter level, tagged by AI use (Legora and Laurel announced work toward AI-value measurement; see routed items)
  risks_and_guardrails:
  - Some clients issue guidelines that they will not pay for certain services if AI performs them, using adoption as leverage to cut costs (DLA Piper panellist) [TRI-LEGALWEEK-2026]
  human_checkpoints:
  - Not applicable (idea)
  role_evolution: Firms have roles such as Chief Pricing and Innovation Officer (Greenberg Traurig) and AI innovation heads (DLA Piper) driving this conversation [TRI-LEGALWEEK-2026].
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: Sections 'Proving AI's path to saving clients money' and 'The contradictions in the room'
  - ref: TRI-STANDOUT-2026
    title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: 'Paragraph: clients want insight into the expected commercial impact on pricing, talent and staffing'
  notes: 'Labelled idea: practitioners discuss it and clients ask for it, but no firm publicly reports a working matter-level AI savings report. Tag: includes in-house (GSK) viewpoint. TRI cited that law firms with a GenAI strategy are 3.9 times more likely to achieve ROI, and only 22% have one (TRI speaker at Legalweek).'
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-16
  archetype: professional-services
  module: scoping-pricing
  title: 'Idea: replace itemised hourly invoices with a single ''services rendered'' line item when AI compresses the work'
  function: finance-accounting
  work_types:
  - document-production
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: As AI compresses work from hours to minutes, an itemised hourly bill can undersell the value delivered.
  solution: Zarwin Baum's managing director proposed at Legalweek 2026 returning to the single line-item 'services rendered' bill that predated the billable hour, and asked whether clients would accept it.
  outcomes:
  - lever: experience
    description: none published
    figure: none
    measures: n/a
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - Client acceptance (raised as an open question by the speaker)
  risks_and_guardrails:
  - Cal Bar guidance requires hourly billing to reflect time actually spent and fee agreements to explain how fees are calculated [CALBAR-GENAI-2026, Rule 1.5 row]
  human_checkpoints:
  - Not applicable (idea)
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: Paragraph beginning 'Meanwhile, Zarwin Baum's Kaplan'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version replacing Nov 2023)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: 2026-05
    access: full
    locator: Table row on charging for GenAI work, p.8
  notes: Labelled idea. Only one practitioner proposal found; no firm reported adopting it.
  last_reviewed: '2026-10-19'
- id: professional-services-scoping-pricing-17
  archetype: professional-services
  module: scoping-pricing
  title: 'Idea: pick consulting price model by outcome observability and input-cost observability, moving toward hybrid structures'
  function: strategy-planning
  work_types:
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: Consultancies choose time-based, project, subscription or outcome pricing by convention; AI breaks the link between hours and effort and, when deployed in client operations, raises outcome measurability.
  solution: 'Brynjolfsson and Petropoulos propose a pricing strategy map using two dimensions and four decision rules: match contract power to signal quality; let internal-augmentation versus client-embedded AI set the direction of change; invest in measurement before outcome pricing but check attribution; treat hybrid as the equilibrium. They conclude AI tends to push consulting firms toward hybrid and asset-based pricing.'
  outcomes:
  - lever: risk
    description: none published
    figure: none
    measures: n/a (theoretical framework; examples drawn from public firm practices)
    provenance: independent
    source_ref: STANFORD-DEL-2026
  prerequisites:
  - Telemetry or agreed ground-truth metrics for outcome-linked components; clean attribution (randomised holdouts or controlled rollouts) where outcomes are entangled with client actions
  risks_and_guardrails:
  - The authors note a gift from Accenture to the Lab (general support, not for this study) and conversations with three Accenture executives that motivated the framework [STANFORD-DEL-2026, footnote p.1-2]
  human_checkpoints:
  - Not applicable (idea)
  role_evolution: Executives must build hybrid-pricing capability as a strategic competence (rule 4) [STANFORD-DEL-2026 section 7].
  evidence_grade: D
  sources:
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives (Brynjolfsson and Petropoulos)'
    publisher: Stanford Digital Economy Lab
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Abstract; sections 5.1-5.2 and 7 (pp.13-22)
  - ref: SALESFORCE-AGENTFORCE-2026
    title: Salesforce Launches Agentforce Help Agent That Deploys in Minutes and Only Charges for Resolutions
    publisher: Salesforce
    type: vendor
    url: https://www.salesforce.com/news/press-releases/2026/06/25/agentforce-help-agent-announcement/
    date: '2026-06-25'
    access: full
    locator: Paragraph 'And you only pay when it works'
  notes: 'Labelled idea: research framework, not a deployment. Cited cases (Palantir, Salesforce Agentforce) are software vendors, adjacent to professional services. Salesforce''s own release (2026-06-25) confirms pay-per-resolution pricing for its Help Agent [SALESFORCE-AGENTFORCE-2026, ''And you only pay when it works'' paragraph].'
  last_reviewed: '2026-10-19'
```

## 3. Module notes

### Processes and key steps (with work types)

1. **Scope capture and assumptions** (client-interaction, research-synthesis): turning a client request, RFP or call into scope, assumptions and exclusions. AI use seen: transcript-to-requirements and scoping drafts at Diabsolut (CERTINIA-CUSTOMERS-2026).
2. **Estimate build** (data-reporting): effort by phase and staffing mix from historical actuals. AI use seen: Certinia Estimate Creation and Estimation agents (vendor description only); pricing-analyst postings (use cases 03, 11).
3. **Price-model choice and fee proposal** (expert-judgment, document-production): hourly, fixed, capped, blended, success fee, subscription, outcome, hybrid. Benchmarking inputs: PERSUIT at Goodwin (use case 01); Stanford decision rules (use case 17).
4. **Negotiation, discount and rate approval** (client-interaction, expert-judgment): pricing managers coach partners (McDermott posting); client guidelines on AI-done work (TRI-LEGALWEEK-2026).
5. **SOW or engagement-letter drafting** (document-production): Certinia SOW Drafter; Neocol live in nine days (use case 12). In regulated legal work the fee agreement must explain how fees and AI costs are calculated (CALBAR-GENAI-2026).
6. **Budget tracking, post-matter profitability and rate setting** (data-reporting, coordination-scheduling): Husch Blackwell and McDermott postings include matter estimates, profitability and post-matter analysis; Pillsbury names Iridium and Clocktimizer for pricing reports.

### Common pain points

- Hours stop being a reliable proxy for effort once AI is used internally; clients see only the deliverable (STANFORD-DEL-2026 section 5.1).
- A time-based price that falls with the hours (a task cut from 1 hour to 0.2 hours) removes 80% of that revenue, in the TRI author's arithmetic (TRI-AFA-2024).
- Firms cannot yet quantify AI savings per matter (TRI-LEGALWEEK-2026: 'anecdotal phase').
- AI investment cost cannot usually be attributed to individual projects (KPMG US advisory vice chair, BLOOMBERGLAW-ACCTPRICING-2026).
- Compensation and performance metrics still reward hours (Wipfli practice chief, same source; TR-FOP-2026 makes the same point about billing models and performance frameworks).
- Outcome contracts: baselines, adjudication and partner-pay effects are not public (AIWEEKLY-MCK-2026).

### Metrics and benchmarks (with sources; what each measures)

- **TR-FOP-2026** (survey of 1,816 professionals, 62 countries, Mar-Apr 2026): 78% of corporate clients say AI-enabled quality improvements from their firms are very important or essential; 6% say most or all of their providers deliver it; 32% have reconsidered or plan to reconsider firm relationships within 12 months.
- **TRI-LEGALWEEK-2026**: law firms with a GenAI strategy are 3.9 times more likely to achieve ROI; only 22% of firms have one (TR speaker's figures).
- **TRI-AFA-2024** (author's account): alternative fee arrangements rose to roughly 20% of law firm revenue after the financial crisis and plateaued around 2014; nearly half of GCs surveyed in the 2024 corporate law department report cited a growing preference for AFAs.
- **TRI-LFFI-Q1-2026**: Am Law 100 worked-rate growth near 10% in Q1 2026 (12%-plus at the largest firms) with the index flat at 55; **TRI-SOTLM-2026**: the report says most of the growth in profit per lawyer (8.4% above pre-2022 levels by end of 2025) and in fees worked per lawyer (16.8%) came from rate rises, and the report warns against using AI mainly to justify higher billing.
- **AICPA 2025 survey as reported by BLOOMBERGLAW-ACCTPRICING-2026**: median net hourly billing rate up nearly 7% over two years to USD 170 (1,000+ firms).
- **SPI-AI-2026** (245 firms): 43.6% of projects use AI (23.1% in 2025); 84.8% say AI saves time (revenue-side figure gated).
- **KANTATA-RMI-2026** (44 organisations; vendor-commissioned): one in two respondents unsure whether their organisation will meaningfully adopt outcome-based pricing; 52.7% not equipped to manage hybrid human-agent teams.
- **CMS-TRENDS-2026**, citing Clio UK Legal Trends 2025-26 (Clio not opened): 54% of UK law firms expect fixed-fee billing to increase over the next 12 months.
- **Quality evidence for AI-built estimates:** none found. No error rate, override rate, estimate-versus-actual comparison or parallel run for AI-generated estimates, quotes or SOWs was published by any source read. The only quality-adjacent items are risk statements (Tech Mahindra on irrational price guarantees; Infosys exiting uneconomic contracts).

### Guardrails and regulatory points

- California Rule 1.5 guidance: bill only time actually spent; flat fees may include AI savings; general AI subscriptions are overhead; matter-specific AI costs only with disclosure, at actual cost, no markup without informed written consent (CALBAR-GENAI-2026, p.8). ABA Opinion 512 was not accessible this run.
- Client outside-counsel guidelines: some clients bar AI use without permission, others refuse to pay for AI-done services (TRI-LEGALWEEK-2026).
- Benchmark tools: PERSUIT states data are anonymised and aggregated with minimum thresholds, benchmarks never reveal firm or client pricing, and it does not set or recommend prices (GOODWIN-PERSUIT-2025).
- Outcome pricing needs measurement and clean attribution first (STANFORD-DEL-2026 section 7, rule 3).
- In-house: client-side data and AI governance limits are described in TRI-STANDOUT-2026 (GC interviews: tool proliferation without governance, security constraints); no in-house pricing-specific rule was found.

### Frontier signals (dated, sourced)

- 2025-12-17: Goodwin announces global rollout of fixed-fee benchmarking (GOODWIN-PERSUIT-2025).
- 2026-03-05: KPMG, PwC and RSM described as developing value and outcome pricing models (BLOOMBERGLAW-ACCTPRICING-2026).
- 2026-03-19 and 2026-03-25: PwC One introduced; PwC US CEO says some services may become subscription tools (PWC-ONE-2026; CPAPA-PWC-2026).
- 2026-04-15: August launches flat-fee calculator from billing history; Certinia launches Veda agent suite (ARTLAW-AUGUST-2026; CPAPA-CERTINIA-2026).
- 2026-06-25: Salesforce charges only for resolved cases on its Help Agent (software comparator, SALESFORCE-AGENTFORCE-2026).
- 2026-08-21: Reuters reports outcome-based contracts spreading in Indian IT services (REUTERS-ITSERVICES-2026).
- 2026-08-23: Stanford pricing framework (STANFORD-DEL-2026).
- 2026-09-04: seat-based versus consumption-based pricing of legal AI was a hallway topic at ILTACON, with vendors reluctant to discuss it (EDISCOVERYTODAY-ILTACON-2026). Cost of AI tools becoming a variable cost per matter is the landscape file's reading, not this source's.
- 2026-10-01: Accenture reported to say prices are lower in many areas (RESULTSENSE-ACCENTURE-2026, secondary).
- 2026-10-02: Falcon launches flat-fee AI-native firm (NONBILLABLE-FALCON-2026).

### Workforce and role effects

- Pricing professionals: analyst and manager roles combine modelling, AFA design and partner coaching, with AI/analytics skills requested (MCDERMOTT-JOB-2026, HUSCH-JOB-2026, PILLSBURY-JOB-2026).
- Leadership roles named at firms: Chief Pricing and Innovation Officer (Greenberg Traurig), Senior Managing Director of AI Innovation (DLA Piper), Managing Director, Client Value (Goodwin) (TRI-LEGALWEEK-2026; GOODWIN-PERSUIT-2025).
- Partners are the 'commercial transmission mechanism' for billing strategy and staffing; many cannot yet connect firm AI strategy to their client value proposition (TRI-STANDOUT-2026).
- Pyramid: Reuters quotes a former Infosys CFO saying the big IT firms will no longer need large ranks of entry-level engineers (REUTERS-ITSERVICES-2026); Forrester expects hiring and organisational redesign (FORRESTER-BLOG-2025).
- Resource managers are mostly operational (72%) and lack outcome data when asked to support outcome-oriented pricing (KANTATA-RMI-2026).

### Objections and concerns practitioners raise

- Attribution: outcome pricing works only where results can be tied to the consultant's work (STANFORD-DEL-2026).
- Margin race: rivals guarantee prices on assumed 70-80% productivity gains (Tech Mahindra CEO, REUTERS-ITSERVICES-2026).
- Revenue arithmetic of cheaper-as-faster under a labour theory of value (TRI-AFA-2024).
- Rate rises as the main profit driver, which could expose firms if client budgets tighten (TRI-SOTLM-2026).
- Client contradiction: demand AI adoption, then use it to cut price (TRI-LEGALWEEK-2026).
- Compensation misalignment (BLOOMBERGLAW-ACCTPRICING-2026).
- A survey respondent quoted in the ILTA executive summary says GenAI will compress document review, research and drafting work and put pressure on the billable hour (ILTA-TECHSURVEY-2026).

### Interview probes for an advisor

1. Which share of your fee proposals last year were hourly, capped, fixed, subscription or outcome-linked, and which share is moving? Who decides when AI-reduced effort goes into the price rather than margin?
2. How do you estimate effort today on work where AI is used, and have you compared AI-assisted estimates with actuals? What data would you need to trust them?
3. When a client asks what AI saved on their matter, what do you show them, and from which system does the number come?
4. Where fees are tied to outcomes, who sets the baseline and decides whether a target was hit, and how are partners paid?
5. How do pricing, finance and delivery teams share estimate and actuals data, and who owns the pricing repository?

## 4. Routed to other modules

- Laurel and Legora automatic time entries, with a second phase to measure AI usage and value (LEGORA-LAUREL-2026, 2026-10-13): **billing-collections**; AI-value measurement also relevant to **firm-finance**.
- Harvey Legal Work Orchestration (reusable matter templates with phases, tasks and review gates) (HARVEY-ORCH-2026, 2026-10-15) and Certinia PMO Quality scope scans (CERTINIA-VEDA-2026): **delivery-management**.
- Certinia Staffing Agent at Nextview (scans 150 colleagues for skills and availability) and the Kantata hybrid-team readiness data (CERTINIA-CUSTOMERS-2026; KANTATA-RMI-2026): **staffing-resourcing**.
- Rate setting, worked-rate growth, realisation and AI investment return (TRI-LFFI-Q1-2026; TRI-LFFI-Q2-2026; TRI-SOTLM-2026): **firm-finance**.
- Partners not discussing AI with clients; 32% of clients reconsidering firms (TRI-STANDOUT-2026; TR-FOP-2026): **client-development**.
- Cal Bar billing, cost-recovery and markup rules in detail (CALBAR-GENAI-2026): **billing-collections** (governance angle).
- Certinia RFP Responder and Deal Coach agents (CERTINIA-VEDA-2026): **pursuit-proposals**.

## 5. Sources

All opened and read in full (access: full) unless noted. Types: academic 1, conference 2, firm 4, job-posting 3, press 13, professional-body 1, regulator 1, survey 4, vendor 7. Total: 36.

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives (Brynjolfsson and Petropoulos) | Stanford Digital Economy Lab | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version replacing Nov 2023) | State Bar of California, Standing Committee on Professional Responsibility and Conduct | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 |
| EDISCOVERYTODAY-ILTACON-2026 | My Five ILTACON 2026 Takeaways: Legal Technology Trends | eDiscovery Today (Doug Austin) | conference | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 executive summary | International Legal Technology Association | professional-body | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 |
| PWC-ONE-2026 | PwC Introduces PwC One as Part of Its Vision for AI-Enabled Professional Services | PwC US newsroom | firm | https://www.pwc.com/us/en/about-us/newsroom/press-releases/pwc-one.html | 2026-03-19 |
| GOODWIN-PERSUIT-2025 | Goodwin Advances Legal Pricing with Global Rollout of PERSUIT's Fixed Fee Benchmarking | Goodwin Procter LLP (press release) | firm | https://www.goodwinlaw.com/en/news-and-events/news/2025/12/announcements-otherindustries-goodwin-advances-legal-pricing-with-global-rollout | 2025-12-17 |
| CROSBY-SITE-2026 | Crosby: The Agentic Law Firm Built for Execution (home page, read 2026-10-19) | Crosby | firm | https://www.crosby.ai/ | 2026-10 |
| CMS-TRENDS-2026 | The Trends Redefining Legal Service Delivery | CMS (law firm) | firm | https://cms.law/en/gbr/publication/the-trends-redefining-legal-service-delivery | 2026-02-12 |
| CERTINIA-VEDA-2026 | Veda AI: agentic intelligence for professional services (solutions page, read 2026-10-19) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10 |
| CERTINIA-CUSTOMERS-2026 | Certinia Customers Are Proving Veda AI Agents Deliver Real Results (blog; no byline date shown, refers to Dreamforce 14-17 Sep 2026 as upcoming) | Certinia | vendor | https://certinia.com/blog/certinia-customers-are-proving-veda-ai-agents-deliver-real-results/ | 2026 |
| CPAPA-CERTINIA-2026 | Certinia Unveils Veda, an AI Operations Engine for Professional Services | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/15/certinia-unveils-veda-an-ai-operations-engine-for-professional-services/181702/ | 2026-04-15 |
| KANTATA-RMI-2026 | New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services | Kantata (study by Resource Management Institute, 44 organisations) | vendor | https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services | 2026-04-09 |
| LTHUB-PERSUIT-2026 | PERSUIT vendor profile (read 2026-10-19) | Legaltech Hub | vendor | https://www.legaltechnologyhub.com/vendors/persuit/ | 2026-10 |
| ARTLAW-AUGUST-2026 | Product Walk Through: August - Genius Mode | Artificial Lawyer (vendor-supplied demo) | press | https://www.artificiallawyer.com/2026/04/15/product-walk-through-august-genius-mode/ | 2026-04-15 |
| NONBILLABLE-FALCON-2026 | Former A&O boss launches AI-native law firm, minus the billable hour | Non-Billable | press | https://www.nonbillable.co.uk/news/wim-dejonghe-launches-ai-native-law-firm-falcon | 2026-10-02 |
| CPAPA-PWC-2026 | PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm' (reporting the Financial Times) | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/ | 2026-03-25 |
| AIWEEKLY-MCK-2026 | McKinsey Ties 25% of Fees to Outcomes as AI Erodes Billable Hours (summary of a WSJ report) | AI Weekly | press | https://aiweekly.co/alerts/mckinsey-ties-25-of-fees-to-outcomes-as-ai-erodes-billable-hours | 2026-06-29 |
| RESULTSENSE-2026 | AI dismantles consulting scale advantage as boutiques target Big Four (summary of FT and City AM) | Resultsense | press | https://www.resultsense.com/news/2026-05-28-ai-consulting-big-four-reckoning/ | 2026-05-28 |
| FORRESTER-BLOG-2025 | The Future Of AI Consulting Services Is Disruptively Bright (analyst blog) | Forrester | press | https://www.forrester.com/blogs/the-future-of-ai-consulting-services-is-disruptively-bright | 2025-09-15 |
| REUTERS-ITSERVICES-2026 | AI reshapes India's IT services sector contracts as clients demand more for less (Reuters, syndicated copy) | Reuters via WHBL | press | https://whbl.com/2026/08/20/ai-reshapes-indias-it-services-sector-contracts-as-clients-demand-more-for-less/ | 2026-08-21 |
| RESULTSENSE-ACCENTURE-2026 | Accenture's forecast lifts IT services stocks hit by AI fears (summary of Reuters) | Resultsense | press | https://www.resultsense.com/news/2026-10-02-accenture-forecast-it-services-rally/ | 2026-10-02 |
| BLOOMBERGLAW-ACCTPRICING-2026 | AI Efficiency Gains Push Accounting Firms to Reimagine Pricing | Bloomberg Law | press | https://news.bloomberglaw.com/financial-accounting/ai-efficiency-gains-push-accounting-firms-to-reimagine-pricing | 2026-03-05 |
| TRI-AFA-2024 | Pricing AI-driven legal services: Alternative fee arrangements are almost inevitable | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/pricing-ai-driven-legal-services-alternative-fee-arrangements | 2024-06-03 |
| TRI-SOTLM-2026 | State of the US Legal Market 2026 analysis: Will the AI bubble burst? A crucial warning for law firms | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 |
| TRI-LFFI-Q1-2026 | Q1 2026 LFFI: Strong inputs, average output - and the first drops of rain | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output | 2026-05-13 |
| TRI-LFFI-Q2-2026 | Q2 2026 LFFI: A heavier load, yet a faster crossing | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed | 2026-08-10 |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 |
| TR-FOP-2026 | Future of Professionals Report 2026 (survey of 1,816 professionals, conducted Mar-Apr 2026; page shows no publication date) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/future-of-professionals-2026/report | 2026 |
| SPI-AI-2026 | The 2026 Impact of AI on Professional Services (report landing page; 245 firms; report listed as published Oct 2026, page dated July 2026) | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-07-14 |
| MCDERMOTT-JOB-2026 | Pricing Manager (job posting, read 2026-10-19; posting date not shown) | McDermott Will & Schulte via Built In NYC | job-posting | https://www.builtinnyc.com/job/pricing-manager/10074034 | 2026-10 |
| HUSCH-JOB-2026 | Senior Pricing Analyst (job posting, read 2026-10-19; posting date not shown) | Husch Blackwell LLP via Built In Austin | job-posting | https://www.builtinaustin.com/job/senior-pricing-analyst/9648474 | 2026-10 |
| PILLSBURY-JOB-2026 | Pricing Analyst, Nashville (job posting, read 2026-10-19; posting date not shown) | Pillsbury Winthrop Shaw Pittman via Talentify | job-posting | https://www.talentify.io/pricing-analyst-nashville-us-pillsbury-winthrop-shaw-pittman | 2026-10 |
| LEGORA-LAUREL-2026 | Legora and Laurel partner to capture the time lawyers spend in Legora as they work | Legora (newsroom) | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 |
| HARVEY-ORCH-2026 | Making Harvey the Orchestration Layer for Legal Work | Harvey | vendor | https://www.harvey.ai/blog/legal-work-orchestration | 2026-10-15 |
| SALESFORCE-AGENTFORCE-2026 | Salesforce Launches Agentforce Help Agent That Deploys in Minutes and Only Charges for Resolutions | Salesforce | vendor | https://www.salesforce.com/news/press-releases/2026/06/25/agentforce-help-agent-announcement/ | 2026-06-25 |

## 6. Gaps

- **Search budget.** The shared web-search budget ran out after 8 searches; planned searches on in-house outside-counsel budgeting tools with named users, A&E and architecture fee proposals, and more named firm pricing deployments were not run.
- **Search-only items (not used for grades).** Dentons Pricing Analyst and Troutman Senior Pricing Analyst postings, the posting date for Pillsbury (reported as 2026-07-23 in a search summary), a Law Gazette commentary on charging for AI-assisted work, Mondaq/GGI commentary on AI pricing, Forrester Wave Q2 2026 claim that all ten providers will put fees at risk, and the Clio UK Legal Trends figure (reached only via CMS-TRENDS-2026). The Deloitte Australia refund is a quality incident, not a pricing practice, and was not opened.
- **Primary sources not reached.** McKinsey's own statements and the WSJ/Business Insider originals for the 25% figure (WSJ blocked; Business Insider URL returned not found); the FT originals behind PwC and Resultsense summaries; Accenture's Q4 FY26 results; AICPA 2025 survey; ABA Formal Opinion 512; Legalweek and ILTACON session recordings.
- **Conflicting figure.** McKinsey outcome-fee share: about 25% (AIWEEKLY-MCK-2026; Stanford citing Business Insider) versus roughly a third (RESULTSENSE-2026). Both secondary.
- **No measurement of AI-built estimates.** No source gave accuracy, override, win-rate or estimate-versus-actual data. Certinia's page headlines (8 hours to 1 hour for a proposal or SOW; 11-23% less margin lost) are unattributed and were not used as outcomes beyond the stated C-grade entry.
- **Undated pages.** Job postings (read 2026-10-19, posting dates not shown), Certinia customer blog (no byline date), TR Future of Professionals page (survey fielded Mar-Apr 2026, publication date not shown), CalBar PDF (printed date absent; file created 2026-05-15), Crosby, Certinia solutions page and Legaltech Hub profile (dated by read month).
- **Under-covered areas.** Architecture and engineering fee proposals, small-firm practice, in-house shared-service teams outside legal, consulting firms' own scoping tools (McKinsey, BCG, Deloitte, EY, KPMG primary pages), and any independent (non-vendor) measurement of AI effect on estimates or margins.
- **Landscape corrections.** AIWEEKLY item is dated 2026-06-29 (landscape said late 2025; the 25% share itself comes from late-2025 reporting). The 'six automated services' for PwC One comes from the FT via CPA Practice Advisor, not from PwC's press release.
