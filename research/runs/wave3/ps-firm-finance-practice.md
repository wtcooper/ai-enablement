# Deep dive: professional-services / firm-finance / practice

- **Archetype:** professional-services
- **Module:** firm-finance. Firm-level finance and performance: rate setting, realization, profitability and partner economics, AI investment and ROI, outside capital and private equity, consumption-based AI costs.
- **Angle:** practice. What firms and in-house teams actually do: case studies, named deployments, firm announcements, vendor deployments with named customers, product documentation, job postings that show real use.
- **Prepared:** 2026-10-19. **Inputs:** `research/runs/wave3/landscape-professional-services.md`, `research/briefs/templates/vocabulary.md`.
- **Method note.** Pages were opened with `curl` (PDFs with `pdftotext`; a few JavaScript-rendered or bot-blocked pages through the `r.jina.ai` text mirror). Eight web searches were used as leads; the shared search budget then ran out, so the last two planned searches (Big Four FY26 results and UK listed law-firm results) were not run. Items seen only in search results are marked and kept out of grade A and B outcomes.

---

## 1. Summary

- **Evidence is thick on commentary, surveys and vendor product pages, and thin on measured results.** 22 candidate use cases: A 0, B 11, C 9, D 2. No named firm publishes a measured effect of AI on rates, realization, profit per partner or return on AI spend. The closest items are self-reported thresholds or ratios: Holland & Hart's 70% weekly-active-user marker for a real pilot (TRI-ILTACON-IMPL-2026), McKinsey's "about a quarter" of fees on outcomes (BUSINESSINSIDER-MCKINSEY-2025), and Ogletree's remark that firms are settling on AI at about 1% of revenue (TRI-METER-2026).
- **Spending is ahead of proof.** US law firms raised technology spending by nearly 11% and knowledge management by about 10% in 2025 (TRI-SOTLM-2026); PwC reports $3 billion invested across its network in AI and other capabilities (AT-PWC-2026); Kirkland's $500 million commitment came without ROI benchmarks (BLOOMBERGLAW-KIRKLAND-2026). Only 18% of surveyed professionals say their organisation tracks AI ROI (TRI-AIPS-2026), and no one in a 50-plus ILTACON audience claimed a strong measure (TRI-ILTACON-IMPL-2026).
- **Variable AI cost is the new finance problem.** Legora moved its Agent Pro product to consumption pricing with matter-level attribution on 2026-06-23 (LEGORA-CBP-2026); Harvey's tokens processed rose fourteen-fold in six months (ARTLAW-HARVEY14X-2026); ILTACON sessions turned to "reading the meter" (TRI-METER-2026). Firms are debating whether to absorb the cost or bill it, within California's rule that general subscriptions are overhead (CALBAR-GENAI-2026). No firm is reported to bill token cost through.
- **Pricing change is further along at consulting firms than at law firms in this evidence.** McKinsey says about a quarter of fees are outcome-based (BUSINESSINSIDER-MCKINSEY-2025) and PwC plans subscription services (CPAPA-PWC-2026). In law, about 90% of legal dollars still flow through hourly arrangements (TRI-SOTLM-REPORT-2026) and almost two-thirds of law firm professionals say pricing is unchanged (TRI-FOP-LAW-2026), while BigHand's survey finds 89% of firms reporting rising write-offs despite 96% raising rates (BIGHAND-FINANCE-2026).
- **Outside capital is real in accounting and early in law.** Crowe closed a KKR investment in August 2026 earmarked for talent, technology and innovation (AT-CROWE-2026). In law, MSO structures are the route, with a reported $700 million letter of intent for Wood Smith (BESTLAW-WSHB-2026) and new state restrictions (Colorado, Illinois).
- **Quality evidence is almost absent.** No error rate, override rate or parallel-run result was found for AI in rate setting, profitability analytics or billing analytics. The nearest thing to third-party validation is that bankruptcy fee examiners disclose Legal Decoder's tool as their methodology (LAWSITES-DECODER-2026).
- **In-house is thin.** One unnamed general counsel's account (BLOOMBERGLAW-BILLABLE-2026), Legal Decoder's work for UBS (LAWSITES-DECODER-2026) and a TRI report on legal operations (TRI-LDOR-2026) are the sources. No named in-house team publishes AI finance results.
- **Evidence count:** 22 use cases (A: 0, B: 11, C: 9, D: 2). 55 sources, 54 read in full. Types: press 19, vendor 14, survey 12, conference 3, firm 2, professional-body 1, regulator 1, academic 1, community 1, podcast 1. No job posting was opened directly; Bloomberg Law's report of Kirkland's roughly 40 AI openings is the only job-posting evidence.

---

## 2. Use cases

Conventions used below:

- **Grades.** A needs a figure the named organization reports as measured. No entry meets that bar. B is a named organization described as running the work, without a measured result. C is a vendor or firm announcement or product page, or survey/analyst evidence with no named user. D is an idea practitioners discuss; each D entry says so.
- **Provenance.** `self-reported` is the organization describing its own use. `vendor-published` is a vendor or a firm describing something it sells, or a vendor-run survey. `independent` is a third-party survey or press report of third-party data; Thomson Reuters Institute surveys are marked `independent` for that reason even though the Institute sits inside a vendor group.
- **Dates.** A source date of `2026-10` marks a page with no publication date; it is the retrieval month (retrieved 2026-10-19) and the source note says so.
- **Cap rule.** Evidence from adjacent processes (time capture, tax pricing surveys, A&E benchmarks) is capped at B or C and flagged in `notes`.
- **Ladder and scope** are the analyst's reading of what the source describes.
- **In-house.** Entries 11 and 21 are tagged in-house; entry 1 serves both firms and in-house teams.

```yaml
- id: professional-services-firm-finance-01
  title: Model how much of each type of work AI will compress, to plan rates, capacity and alternative fee arrangements
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: 'Firms set rates and fee arrangements on averages, without a view of which kinds of work AI will shorten and by how much. In-house teams have the mirror problem: they do not know what they should stop expecting to pay for.'
  solution: Legal Decoder, a legal spend analytics vendor, says it is about to release a module (AI Replaceability, or AIR) that sorts legal work into eight archetypes and applies expected AI-driven compression ratios to each. A law firm can model how much of its work may be compressed; an in-house team can see what it should no longer expect to pay for. A second planned module builds alternative fee arrangements around clusters of similar work (for example, low, medium and high complexity depositions) rather than averages. Both sit on Legal Decoder's existing billing-narrative analytics (see use case 11).
  outcomes:
  - lever: cost
    description: No outcome published for AIR or the AFA builder; both were described as due to roll out 'in the coming weeks' on 2026-07-15.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: LAWSITES-DECODER-2026
  prerequisites:
  - LEDES-format billing data exports (6, 12 or 24 months) down to timekeeper level
  - A defensible mapping of the firm's matters to the vendor's work archetypes
  - Agreement on who owns the compression assumptions (pricing team, finance or practice leaders)
  risks_and_guardrails:
  - The compression ratios are the vendor's expected values, not measured results at a named firm; treating them as forecasts could mis-set rates or fixed fees.
  - Under California's guidance, hourly bills must reflect time actually spent, so modelled compression cannot be used to bill hours that were not worked (CALBAR-GENAI-2026).
  human_checkpoints:
  - Pricing or finance leadership reviews the assumptions before rates or AFAs change
  - Partners review the work clusters before they become fee schedules
  role_evolution: Pricing professionals move from comparing averages to testing scenarios by work type, if the modules ship as described (LAWSITES-DECODER-2026).
  evidence_grade: C
  sources:
  - ref: LAWSITES-DECODER-2026
    title: Legal Decoder Introduces Aperture, A Natural Language Interface for Querying Legal Billing Data
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/07/legal-decoder-introduces-aperture-a-natural-language-interface-for-querying-legal-billing-data.html
    date: '2026-07-15'
    access: full
    locator: section 'What's Ahead' (AIR and AFA builder)
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: page 8, 'Charging for Work Produced by Generative AI and Generative AI Costs'
  last_reviewed: '2026-10-19'
  notes: Announced products only; no customer is named for AIR or the AFA builder. Tagged for both firms and in-house teams. Matter-level pricing tools (Aderant Virtual Pricing Director, Certinia estimate agents) are routed to scoping-pricing.
- id: professional-services-firm-finance-02
  title: Re-price AI-compressed legal work with fixed, value-based or hybrid fees instead of hours
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: piloting
  problem: When AI shortens a task, an hourly bill shows fewer hours and the firm earns less for the same result; clients meanwhile ask what AI saved them. The firm needs a pricing basis that does not depend on time spent.
  solution: Firm pricing leads move parts of their work to fixed or value-based fees, and keep hourly billing for the uncertain part. Keypoint Law's chief executive says the firm has priced this way 'since the start' and expects hybrid models, with the known part of a matter fixed and the uncertain part hourly. At Legalweek 2026, a Zarwin Baum managing director proposed a return to a single 'services rendered' line item, and Greenberg Traurig's chief pricing and innovation officer reported clients asking how AI is used on their matters. California's 2026 guidance expressly allows flat fees that build in AI time savings.
  outcomes:
  - lever: cost
    description: Almost two-thirds of law firm professionals say their firm's pricing structure is unchanged despite client demand for pricing that reflects AI efficiencies.
    figure: almost two-thirds
    measures: share of the 736 law firm professionals surveyed who say their firm's pricing structure remains unchanged despite clients' demand for new models reflecting AI-driven efficiencies
    provenance: independent
    source_ref: TRI-FOP-LAW-2026
  - lever: cost
    description: About 90% of legal dollars still flow through hourly billing arrangements.
    figure: 90%
    measures: share of legal dollars flowing through hourly billing arrangements, per the State of the US Legal Market report summary
    provenance: independent
    source_ref: TRI-SOTLM-REPORT-2026
  - lever: quality
    description: Of the firms BigHand surveyed, 31% say AI is currently supporting changes to pricing structures for AI-augmented work.
    figure: 31%
    measures: share of firms saying AI is currently supporting changes to pricing structures for AI-augmented work, as reported by a BigHand solutions manager citing BigHand's 2026 finance report
    provenance: vendor-published
    source_ref: LEGALFUTURES-BIGHAND-2026
  prerequisites:
  - Cost-to-deliver data by matter and task, so a fixed fee can be set with a known margin
  - A pricing function or officer (Greenberg Traurig has a chief pricing and innovation officer)
  - A way to separate the scopeable part of a matter from the uncertain part
  - Client agreement on how AI savings are shared
  risks_and_guardrails:
  - Fee agreements should say how fees and costs are calculated and the extent to which generative AI factors into rates (CALBAR-GENAI-2026).
  - 'Clients are not uniform: some demand AI use and savings targets, others still issue guidelines banning AI work without permission (TRI-LEGALWEEK-2026).'
  - Leading with price cuts can train clients to expect discounts (TRI-STANDOUT-2026).
  human_checkpoints:
  - Pricing leads and partners set the fixed or hybrid price
  - Clients agree the scope and the adjustment trigger
  role_evolution: Partners become the people who explain value and price it; the TRI 2026 Stand-out Lawyers Survey finds only about one-third of heavy-AI-user partners have discussed AI with 60% or more of their clients (TRI-STANDOUT-2026).
  evidence_grade: B
  sources:
  - ref: LAWYERSWEEKLY-KEYPOINT-2026
    title: '''Clients will get annoyed'' if firms pass on AI costs, says Keypoint''s CEO'
    publisher: Lawyers Weekly (Australia)
    type: press
    url: https://www.lawyersweekly.com.au/biglaw/44659-clients-will-get-annoyed-if-firms-pass-on-ai-costs-says-keypoint-s-ceo
    date: '2026-07-15'
    access: full
    locator: 'visible portion: Kalinko on value and fixed-price billing and hybrid models'
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: sections 'Proving AI's path to saving clients money' and 'The contradictions in the room'
  - ref: TRI-FOP-LAW-2026
    title: What the '2026 Future of Professionals Report' says law firm leaders should be doing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/future-of-professionals-law-firms-paper-2026
    date: '2026-07-21'
    access: full
    locator: key takeaways and section on pricing models
  - ref: TRI-SOTLM-REPORT-2026
    title: '2026 Report on the State of the US Legal Market: Peak prosperity and the fault lines below (executive summary page)'
    publisher: Thomson Reuters Institute with Georgetown Law Center on Ethics and the Legal Profession
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/state-of-the-us-legal-market-2026
    date: '2026-01-07'
    access: full
    locator: '''Structural business model conflict'''
  - ref: LEGALFUTURES-BIGHAND-2026
    title: Navigating the legal AI productivity-profitability paradox (Alec Koster, BigHand)
    publisher: Legal Futures
    type: press
    url: https://www.legalfutures.co.uk/blog/navigating-the-legal-ai-productivity-profitability-paradox/print/
    date: '2026-03-17'
    access: full
    locator: section 'The reality of the AI efficiency gap'
  - ref: BIGHAND-FINANCE-2026
    title: 'BigHand 2026 Annual Law Firm Finance Report: Profitability, Cash Flow & AI Insights (landing page)'
    publisher: BigHand
    type: vendor
    url: https://www.bighand.com/en-us/resources/whitepapers/2026-annual-law-firm-finance-report/
    date: '2026-01-21'
    access: full
    locator: 'landing page: headline findings on billable hours and write-offs'
  - ref: TRI-STANDOUT-2026
    title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: section 'How to talk to clients about AI'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: page 8
  last_reviewed: '2026-10-19'
  notes: Grade B rests on Keypoint's stated practice and named Legalweek panellists; no firm publishes a measured margin or realization result from AI-linked repricing. The BigHand landing page gives a different headline (nearly two-thirds of firms report a decrease in billable hours, and 99% plan to raise billable-hour targets) from the Legal Futures post (29% report a reduction in billable hours); the two are not reconciled (BIGHAND-FINANCE-2026).
- id: professional-services-firm-finance-03
  title: Tax and accounting firms move from hourly pricing toward value and retainer pricing as AI automates compliance work
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Compliance preparation is the work AI is best placed to speed up, yet hourly billing remains the dominant pricing model, and advisory work, which clients value, earns lower margins than routine preparation.
  solution: Firms redirect time freed by AI into proactive advice and price it by value or retainer. TRI argues that tax, audit and accounting firms will need to stop billing by the hour and price their judgment; it describes firms that have already moved as treating tax strategy as a year-round relationship with value-based or retainer pricing. No firm is named.
  outcomes:
  - lever: cost
    description: Hourly billing is used by 78% of firms.
    figure: 78%
    measures: share of firms using hourly billing as their pricing model, per TRI's 2026 State of Tax Professionals Report as summarised in the article
    provenance: independent
    source_ref: TRI-CHARGING-2026
  - lever: cost
    description: Firms with the highest profit margins use value-based pricing 61% of the time, against 54% in the lowest-margin tier.
    figure: 61% vs 54%
    measures: share of the time value-based pricing is used by firms in the highest-margin tier versus the lowest-margin tier, per the survey as summarised in the article; correlation only
    provenance: independent
    source_ref: TRI-CHARGING-2026
  - lever: cost
    description: Individual return preparation carries a 28% profit margin; advisory services sit at 20-24%.
    figure: 28% vs 20-24%
    measures: profit margin by service line reported by surveyed tax firms
    provenance: independent
    source_ref: TRI-CHARGING-2026
  prerequisites:
  - A view of true cost of delivery by client and service line
  - Proactive-advice capability to absorb freed capacity
  - Clients willing to pay for advisory retainers
  risks_and_guardrails:
  - The article notes that freed-up time is not itself billable; drifting between several strategies while still billing hourly is the failure it names (TRI-CHARGING-2026).
  - The margin comparison is a correlation in survey data and does not show that repricing causes higher margins.
  human_checkpoints:
  - Firm leaders set the pricing model and retainer scope
  - Partners hold the client conversation on what the fee covers
  role_evolution: Staff time shifts from preparation toward advice; TRI says clients complain of errors, poor communication and lack of proactive planning rather than fees (TRI-CHARGING-2026).
  evidence_grade: C
  sources:
  - ref: TRI-CHARGING-2026
    title: If AI can do the work, then what are you actually charging for?
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/what-are-you-actually-charging-for
    date: '2026-10-02'
    access: full
    locator: '''Compliance work is commoditizing'' and ''Clients are already grading firms on this'''
  last_reviewed: '2026-10-19'
  notes: No named firm; the grade reflects survey data and analyst argument only. Practice-specific tax technical work is out of scope here and belongs to the tax archetype.
- id: professional-services-firm-finance-04
  title: Charge consulting fees against outcomes rather than effort for AI-enabled transformation work
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: When AI changes how much human effort a deliverable takes, hours stop being a reliable proxy for the work, and clients push to pay for results.
  solution: McKinsey says clients now often start from the outcome they want, and that the fee is mostly contingent on the performance McKinsey can deliver, with some fixed components remaining. EY's global managing partner for growth and innovation told Business Insider earlier in 2025 that AI agents may call for a 'service-as-a-software' approach where clients pay by outcome. A Stanford Digital Economy Lab paper argues that AI tends to push consulting toward hybrid and asset-based pricing, and that attribution risk limits how far outcome-based pricing can go.
  outcomes:
  - lever: growth
    description: McKinsey said about a quarter of its global fees come from outcomes-based pricing.
    figure: about a quarter
    measures: McKinsey's stated share of global fees from outcomes-based pricing, given by its UK, Ireland and Israel managing partner at a London media briefing in November 2025; period and calculation not stated. A McKinsey technology leader also referred to a proportion of '20%' as 'probably more recent'.
    provenance: self-reported
    source_ref: BUSINESSINSIDER-MCKINSEY-2025
  prerequisites:
  - Outcomes that can be measured and attributed to the firm's work (the Stanford paper treats attribution as the binding constraint)
  - A scorecard agreed with the client, for example investor targets, revenue or profit goals, operational measures and satisfaction scores
  - Willingness to bear delivery risk
  risks_and_guardrails:
  - 'Attribution risk: where the consultant''s contribution is confounded with everything else the client does, the paper expects hybrid rather than pure outcome contracts (STANFORD-DEL-2026).'
  - The McKinsey share appears elsewhere as 'roughly a third' in a secondary summary (RESULTSENSE-2026); the Business Insider report of the briefing says a quarter.
  human_checkpoints:
  - Partners and client executives agree the outcome scorecard before work starts
  role_evolution: McKinsey's technology leader said straight strategy advice is now under 20% of the firm's work, with more deep implementation and multi-year transformation (BUSINESSINSIDER-MCKINSEY-2025).
  evidence_grade: B
  sources:
  - ref: BUSINESSINSIDER-MCKINSEY-2025
    title: AI is reshaping how McKinsey makes money (Polly Thompson), read via Yahoo Finance syndication
    publisher: Business Insider
    type: press
    url: https://finance.yahoo.com/news/ai-reshaping-mckinsey-makes-money-195132745.html
    date: '2025-11-17'
    access: full
    locator: 'article body: Birshan and Smaje quotations; EY''s Sharma remark'
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson, Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: section 5.1 (page 14) and abstract
  - ref: RESULTSENSE-2026
    title: AI threatens Big Four scale advantage as UK boutiques attack
    publisher: Resultsense (summarising FT and City AM)
    type: press
    url: https://www.resultsense.com/news/2026-05-28-ai-consulting-big-four-reckoning/
    date: '2026-05-28'
    access: full
    locator: paragraph beginning 'What AI is actually undoing' (secondary)
  last_reviewed: '2026-10-19'
  notes: 'Graded B, not A: ''about a quarter'' is a rounded statement at a media briefing, not a published metric. McKinsey also says outcomes-based pricing did not start because of AI, but that the work AI transformation demands suits it. The AI link is therefore partial.'
- id: professional-services-firm-finance-05
  title: Sell parts of the firm's expertise as AI-powered, subscription-priced services used without a professional in the loop
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - expert-judgment
  - client-interaction
  pattern: service-agent-escalation
  ladder: automate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: Hourly consulting and tax work cannot be scaled without adding people, and AI threatens the junior-hours model that funds partners.
  solution: PwC's US chief executive told the Financial Times that some tax and consulting services would become AI-powered automated tools that clients could use 'without a PwC person in the loop', potentially paid for on an annual subscription. PwC has launched PwC One, which a trade report describes as an AI platform giving clients access to six automated services, with more promised. PwC's network results say the firms invested $3 billion in AI and other capabilities in the fiscal year to 30 June 2026, including the initial rollout of PwC One.
  outcomes:
  - lever: growth
    description: PwC says its network invested $3 billion in AI and other capabilities in fiscal 2026, including the initial PwC One rollout; global revenue was $60.2 billion.
    figure: $3 billion invested; $60.2 billion revenue
    measures: PwC network spend on AI and other capabilities in the year to 30 June 2026, as reported by Accounting Today from PwC's results statement; the split between AI and 'other capabilities' is not given
    provenance: self-reported
    source_ref: AT-PWC-2026
  prerequisites:
  - Codified firm expertise and standards in a platform (PwC describes PwC One as uniting knowledge, standards and expertise)
  - A pricing model for subscription or consumption use
  - Professional oversight arrangements for automated outputs
  risks_and_guardrails:
  - Subscription pricing was described as a possibility ('potentially paid for'); PwC's own announcement, per the Stanford paper, stops short of pricing specifics (STANFORD-DEL-2026).
  - Clients may do more in-house instead of buying (CPAPA-PWC-2026).
  human_checkpoints:
  - Professional oversight of the automated services (per PwC, as summarised by Stanford)
  role_evolution: The US chief executive said partners who resist AI 'have no place at the firm' and that senior staff not 'paranoid about being AI-first' would probably be replaced (CPAPA-PWC-2026).
  evidence_grade: B
  sources:
  - ref: CPAPA-PWC-2026
    title: PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'
    publisher: CPA Practice Advisor (reporting the Financial Times)
    type: press
    url: https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
    date: '2026-03-25'
    access: full
    locator: paragraphs 2-3 and PwC One paragraph (second-hand from the FT)
  - ref: AT-PWC-2026
    title: PwC grows 2026 global revenue to $60.2B
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/pwc-grows-2026-global-revenue-to-60-2b
    date: '2026-10-19'
    access: full
    locator: paragraph 3 (investment and PwC One)
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson, Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: section 5.2, PwC One discussion (page 15-16)
  last_reviewed: '2026-10-19'
  notes: 'Grade B: a named platform in initial rollout, with no published usage, pricing or revenue figure for PwC One. The subscription model is a stated intention.'
- id: professional-services-firm-finance-06
  title: AI vendors move from per-seat licences to consumption pricing with usage attributed to the matter
  archetype: professional-services
  module: firm-finance
  function: procurement-supply-chain
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Agentic tools run many model calls per task, so a flat per-seat fee can leave the vendor bearing unpredictable cost, and the firm cannot trace cost to a client.
  solution: Legora announced on 2026-06-23 that its most capable product, Agent Pro, is priced by consumption, with a dashboard tracking usage by organisation, user or project, attribution of every run to a matter, thresholds, spending controls and notifications before a limit. The standard Legora Agent stays at no extra cost under existing contracts. Harvey's president reported a 14-fold rise in tokens processed over six months, and Artificial Lawyer understands Harvey is developing a new pricing model.
  outcomes:
  - lever: cost
    description: Tokens processed on the Harvey platform rose fourteen-fold in six months, per its co-founder and president; costs of that growth were not published.
    figure: 14x
    measures: increase in the number of tokens processed on the Harvey platform over the last six months, excluding embedding tokens
    provenance: vendor-published
    source_ref: ARTLAW-HARVEY14X-2026
  - lever: cost
    description: Legora says consumption can be attributed per matter, giving law firms per-client cost transparency.
    figure: none published
    measures: n/a (product capability, no measured result)
    provenance: vendor-published
    source_ref: LEGORA-CBP-2026
  prerequisites:
  - Matter-coded usage so that AI cost can be allocated to clients
  - Spend controls and alert thresholds set by an administrator
  - Contract terms that allow for price and model changes
  risks_and_guardrails:
  - Law360 reports experts saying any benefit for law firms will not be automatic or immediate, and that it raises the question whether clients will be charged new AI fees (LAW360-LEGORA-2026).
  - Baker Donelson's guide says at least one major model vendor changed rates in ten of the last 13 months, so contracts need flexibility (BAKERDONELSON-TOKENS-2026).
  human_checkpoints:
  - Administrators set limits and review the usage dashboard
  - Finance decides whether to allocate or absorb the cost
  role_evolution: Law firm finance and knowledge teams take on vendor-usage monitoring that licence renewals did not require.
  evidence_grade: C
  sources:
  - ref: LEGORA-CBP-2026
    title: Introducing Consumption-Based Pricing
    publisher: Legora
    type: vendor
    url: https://legora.com/blog/consumption-based-pricing
    date: '2026-06-23'
    access: full
    locator: '''At a glance'' and body'
  - ref: LAW360-LEGORA-2026
    title: Legora's New AI Pricing Model May Usher In Larger Changes
    publisher: Law360 Pulse
    type: press
    url: https://www.law360.com/articles/2494404
    date: '2026-06-26'
    access: full
    locator: opening paragraphs
  - ref: ARTLAW-HARVEY14X-2026
    title: Harvey Increases Token Use 14X in Just 6 Months
    publisher: Artificial Lawyer
    type: press
    url: https://artificiallawyer.com/2026/07/08/harvey-increases-token-use-14x-in-just-6-months
    date: '2026-07-08'
    access: full
    locator: body
  - ref: BAKERDONELSON-TOKENS-2026
    title: 'AI Tokenomics Guide: Understanding Token-Based AI Pricing for Legal Technology (Justin Daniels)'
    publisher: Baker Donelson
    type: firm
    url: https://www.bakerdonelson.com/webfiles/Bios/Token-Pricing-Guide-for-Clients-August-2026.pdf
    date: '2026-08-20'
    access: full
    locator: section 4, 'Subscription vs. Metered Pricing'
  last_reviewed: '2026-10-19'
  notes: The 14x figure comes from a Harvey executive's public post as relayed by Artificial Lawyer, which notes that the data exclude embedding tokens and do not show cost. No law firm customer is named for Agent Pro consumption billing.
- id: professional-services-firm-finance-07
  title: 'Firms set up AI cost governance: see token spend by user and matter, route work to cheaper models, and negotiate usage terms'
  archetype: professional-services
  module: firm-finance
  function: procurement-supply-chain
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Firms budgeted per-seat AI fees, but usage-based charges depend on how lawyers prompt, which model they choose, and how many agent steps run. Lawyers cannot see the spend and tend to choose the strongest model for small tasks.
  solution: At ILTACON 2026, knowledge and AI leads from named firms described reading consumption bills and the behaviour behind them. Littler's knowledge management counsel checked a bill and found a single PowerPoint had cost $2. Barnes & Thornburg's knowledge and AI manager described lawyers choosing the largest model for the smallest task. Ogletree's chief data and AI officer said the industry seemed to be settling on AI costing roughly 1% of revenue, and that his firm was not there yet. Taft's innovation manager urged firms to ask whether an agent eliminates specific line items. Baker Donelson published a guide for general counsel on token pricing, and NetDocuments' applied AI team argued that firms should track and train for token usage.
  outcomes:
  - lever: cost
    description: An Ogletree Deakins executive said firms are settling on AI costing about 1% of revenue and that his firm has not reached that level.
    figure: about 1% of revenue
    measures: AI cost as a share of firm revenue, stated by Ogletree's chief data and AI officer in a conference session; not a measured or audited figure
    provenance: self-reported
    source_ref: TRI-METER-2026
  prerequisites:
  - Usage data by user, matter and model from each AI tool (about 1 in 6 attendees in one ILTACON session said they had 20 or more AI tools in use or under evaluation)
  - Approval of model-routing rules or defaults
  - Training for lawyers on prompting and model choice
  - Contracts with transparency on model usage, allowances, overages and price-change rights (BAKERDONELSON-TOKENS-2026)
  risks_and_guardrails:
  - 'Cutting back can reduce quality: Artificial Lawyer notes lawyers will pick the more accurate, more expensive option when accuracy matters (ARTLAW-HARVEY14X-2026).'
  - '''You cannot tell a client you ran out of tokens'' was the point made by the Barnes & Thornburg speaker (TRI-METER-2026).'
  - Strong profits and rate growth make it easy to ignore the meter (TRI-METER-2026).
  human_checkpoints:
  - Knowledge and AI leads review spend by tool and user
  - Finance approves budgets and contract terms
  role_evolution: Knowledge management and innovation roles add AI financial operations; the TRI report names roles such as head of innovation and AI, chief data and AI officer, and knowledge and AI solutions manager (TRI-METER-2026).
  evidence_grade: B
  sources:
  - ref: TRI-METER-2026
    title: 'Ferraris for emails: At ILTACON 2026, the industry starts reading the meter'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter
    date: '2026-09-09'
    access: full
    locator: sections 'The receipt is not the cost', 'The $2 PowerPoint' and 'Ferraris for emails'
  - ref: EDISCOVERYTODAY-ILTACON-2026
    title: 'My Five ILTACON 2026 Takeaways: Legal Technology Trends'
    publisher: eDiscovery Today (Doug Austin)
    type: press
    url: https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/
    date: '2026-09-04'
    access: full
    locator: section 'Is tokengeddon looming for AI pricing?'
  - ref: BAKERDONELSON-TOKENS-2026
    title: 'AI Tokenomics Guide: Understanding Token-Based AI Pricing for Legal Technology (Justin Daniels)'
    publisher: Baker Donelson
    type: firm
    url: https://www.bakerdonelson.com/webfiles/Bios/Token-Pricing-Guide-for-Clients-August-2026.pdf
    date: '2026-08-20'
    access: full
    locator: executive summary and sections 2 and 5
  - ref: NETDOCUMENTS-TOKENS-2026
    title: Lawyer Tokenomics
    publisher: NetDocuments (ndMAX Studio, Applied AI Team)
    type: vendor
    url: https://studio.netdocuments.com/post/lawyer-tokenomics
    date: '2026-08-12'
    access: full
    locator: body
  - ref: ARTLAW-HARVEY14X-2026
    title: Harvey Increases Token Use 14X in Just 6 Months
    publisher: Artificial Lawyer
    type: press
    url: https://artificiallawyer.com/2026/07/08/harvey-increases-token-use-14x-in-just-6-months
    date: '2026-07-08'
    access: full
    locator: analysis section
  - ref: RADIANT-TOKENS-2026
    title: Legal has a token problem, and the industry is just starting to notice
    publisher: Radiant Law
    type: vendor
    url: https://www.radiantlaw.com/resources/legal-has-a-token-problem-and-the-industry-is-just-starting-to-notice
    date: 2026-10
    access: full
    locator: opening paragraphs (secondary, vendor commentary)
  last_reviewed: '2026-10-19'
  notes: 'Grade B: named firm staff describe practice at a conference; no firm publishes a measured saving. HIKE2''s director said she has seen companies switch AI services off because usage was not producing revenue (TRI-METER-2026); this is an anecdote and the companies are unnamed. A Radiant Law marketing page reports Uber''s CTO saying the company used its 2026 AI budget in four months (RADIANT-TOKENS-2026, secondary, not verified at source).'
- id: professional-services-firm-finance-08
  title: 'Recover AI costs from clients: treat licences as overhead, or pass through matter-specific usage'
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: As AI costs become variable and attributable to a matter, firms must decide whether to absorb them in rates or bill them, and clients are already pressing for lower bills.
  solution: 'Idea under discussion, no named firm doing it. California''s guidance treats general AI subscriptions as overhead absorbed in the fee, allows per-use charges for tools incurred specifically for a client''s matter if the fee agreement discloses them, at actual cost, with no markup without informed written consent. Practitioners disagree: Keypoint''s chief executive says clients will be annoyed by pass-through; a Ballard Spahr speaker said metering makes cost traceable to a client and ''a line item you can trace is a line item you can bill''; Harvey''s president said pass-through might become more common.'
  outcomes:
  - lever: cost
    description: none published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: TRI-METER-2026
  prerequisites:
  - Matter-level usage metering (see use cases 6 and 7)
  - Fee-agreement language disclosing AI costs
  - Client acceptance, which the sources say is uncertain
  risks_and_guardrails:
  - No markup or profit element without the client's informed written consent (CALBAR-GENAI-2026).
  - Hourly billing must reflect time actually spent (CALBAR-GENAI-2026).
  - Clients may refuse to pay for work done with AI, or ask for AI line items (TRI-LEGALWEEK-2026).
  human_checkpoints:
  - Billing partner and client agree AI cost terms in the engagement letter
  role_evolution: Billing and pricing teams add AI cost as a recoverable-expense category, if firms choose to bill it.
  evidence_grade: D
  sources:
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: page 8, cost treatment paragraphs
  - ref: LAWYERSWEEKLY-KEYPOINT-2026
    title: '''Clients will get annoyed'' if firms pass on AI costs, says Keypoint''s CEO'
    publisher: Lawyers Weekly (Australia)
    type: press
    url: https://www.lawyersweekly.com.au/biglaw/44659-clients-will-get-annoyed-if-firms-pass-on-ai-costs-says-keypoint-s-ceo
    date: '2026-07-15'
    access: full
    locator: visible portion
  - ref: TRI-METER-2026
    title: 'Ferraris for emails: At ILTACON 2026, the industry starts reading the meter'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter
    date: '2026-09-09'
    access: full
    locator: '''Ferraris for emails'' section, Ballard Spahr remark'
  - ref: ARTLAW-HARVEY14X-2026
    title: Harvey Increases Token Use 14X in Just 6 Months
    publisher: Artificial Lawyer
    type: press
    url: https://artificiallawyer.com/2026/07/08/harvey-increases-token-use-14x-in-just-6-months
    date: '2026-07-08'
    access: full
    locator: paragraph quoting Pereyra on pass-through
  - ref: LAW360-LEGORA-2026
    title: Legora's New AI Pricing Model May Usher In Larger Changes
    publisher: Law360 Pulse
    type: press
    url: https://www.law360.com/articles/2494404
    date: '2026-06-26'
    access: full
    locator: e-discovery comparison paragraph
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: section 'The contradictions in the room'
  last_reviewed: '2026-10-19'
  notes: 'Labelled an idea: discussed by practitioners and a regulator; no firm is reported to bill token costs through. E-discovery costs are cited as the precedent for pass-through.'
- id: professional-services-firm-finance-09
  title: 'Measure AI adoption and return at firm level: weekly active users, tool usage by rank, and value tied to time and matter data'
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: Firms are spending heavily on AI and cannot show clients or their own finance teams what it returns. Few organisations track ROI at all.
  solution: Firms use proxy measures during pilots. Holland & Hart's enterprise applications director described a threshold of more than 70% weekly active users as the marker of real adoption, running pilots on real matters through the document management system. Laurel markets a Signal module that tracks tool usage by department and rank across tools such as Copilot and Harvey and shows how adoption shifts billable output. Legora and Laurel plan a second phase to measure use and value of Legora from joint data.
  outcomes:
  - lever: quality
    description: Holland & Hart uses a 70% weekly-active-user level as the sign that a pilot is real adoption rather than shelfware.
    figure: 70% threshold
    measures: share of lawyers in an AI trial who are weekly active users, used by the firm as an adoption marker; a threshold, not a measured result
    provenance: self-reported
    source_ref: TRI-ILTACON-IMPL-2026
  - lever: cost
    description: Only 18% of professionals say their organisations track ROI on AI, and another 40% do not know whether ROI is measured.
    figure: 18% track; 40% do not know
    measures: share of the 1,500+ professionals surveyed across legal, tax, accounting, risk, fraud and government who say their organisation tracks AI ROI; the share who do not know whether it is measured
    provenance: independent
    source_ref: TRI-AIPS-2026
  prerequisites:
  - Usage telemetry from each AI tool
  - Time and matter data to relate usage to billable output
  - Agreed definitions of success before a pilot starts
  - Baselines such as manual effort estimates for tasks (TR's strategist suggested junior associates estimate this)
  risks_and_guardrails:
  - 'Usage is an input metric: Laurel itself says ROI should be measured ''beyond input metrics'' (LAUREL-SIGNAL-2026).'
  - Speakers at ILTACON said no one in a room of 50+ attendees claimed a strong measurement of AI ROI (TRI-ILTACON-IMPL-2026).
  - Kirkland did not provide return-on-investment benchmarks for its $500 million commitment (BLOOMBERGLAW-KIRKLAND-2026).
  human_checkpoints:
  - Innovation or knowledge leads and finance review adoption and return before renewal
  role_evolution: Innovation, knowledge and finance teams share ownership of AI value measurement; vendors offer to help calculate ROI (TRI-ILTACON-IMPL-2026).
  evidence_grade: B
  sources:
  - ref: TRI-ILTACON-IMPL-2026
    title: 'ILTACON 2026: ''Does it make the boat faster?'' How legal teams are finding AI implementation success'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-finding-ai-implementation-success
    date: '2026-08-31'
    access: full
    locator: sections 'Metrics that matter' and 'The definition of success'
  - ref: TRI-AIPS-2026
    title: 2026 AI in Professional Services Report (landing page)
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/2026-ai-in-professional-services-report
    date: 2026-10
    access: full
    locator: executive summary, 'AI's ROI remains elusive'
  - ref: LAUREL-SIGNAL-2026
    title: Laurel Signal (platform page)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/signal
    date: 2026-10
    access: full
    locator: '''AI & Technology ROI'' section'
  - ref: LAWSITES-LAUREL-2026
    title: Legora and Laurel Partner to Enable Automatic Time Capture; Will Later Develop Measures of Legora's Value to Firms
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/legora-and-laurel-partner-to-enable-automatic-time-capture-will-later-develop-measures-of-legoras-value-to-firms.html
    date: '2026-10-13'
    access: full
    locator: paragraphs on the second phase
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: section 'Proving AI's path to saving clients money' ('still gathering the data')
  - ref: BLOOMBERGLAW-KIRKLAND-2026
    title: Kirkland's $500 Million AI Gambit Requires a Cast of Hundreds
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/kirklands-500-million-ai-gambit-requires-a-cast-of-hundreds
    date: '2026-06-15'
    access: full
    locator: 'final paragraph: no ROI benchmarks provided'
  last_reviewed: '2026-10-19'
  notes: Holland & Hart's use is a stated practice and threshold, so B. The TRI cross-profession survey statistic is not specific to law firms, so it is context rather than a grade driver.
- id: professional-services-firm-finance-10
  title: Track engagement profitability, partner-to-associate leverage and write-downs from passively captured work data
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Firms learn that a matter lost money after the bill is out. Recorded time differs from time worked, and the cost of delivering fixed fees is a guess.
  solution: Laurel Signal turns captured activity (by application, rank, client and project) into firm-level insight, comparing recorded with actual time to find leakage, showing billable and non-billable work to price fixed fees, comparing cost with revenue as projects run, and showing where partners do routine work and where associates are at capacity. Aprio's CFO and partner says it shows hidden write-downs and how partner and senior time affects leverage, so the firm can staff more effectively, protect margins and plan. The Bonadio Group's CIO says Laurel gives objective visibility into how work happens and its true cost of delivery.
  outcomes:
  - lever: capacity
    description: 'Laurel headline claims: up to 30 minutes recovered daily, a 4-11% profit increase, and 2.88 more time entries daily; no basis, sample or customer is attached.'
    figure: up to 30 min/day; 4-11%; 2.88 entries/day
    measures: 'unstated on the page: the claim appears next to an ROI calculator without a population or method'
    provenance: vendor-published
    source_ref: LAUREL-HOME-2026
  prerequisites:
  - Passive capture across the firm's applications
  - A taxonomy (workmap) of tasks and projects built with the vendor
  - Defined KPIs and their systems of record
  - Staff and partner acceptance of activity monitoring
  risks_and_guardrails:
  - Capture of work activity raises employee privacy and trust concerns; the vendor states single-tenant AI, no public LLMs and bring-your-own-key, but customers should verify (LAUREL-WORKSTUDIO-2026).
  - The workmap classification of activities to tasks and projects is itself AI-derived and needs checking against the firm's records.
  human_checkpoints:
  - Finance and practice leaders review profitability flags
  - Partners decide on pricing, staffing and fixed-fee change orders
  role_evolution: Firm finance moves from month-end reporting to in-flight margin management; partners see their own routine work surfaced as a leverage issue.
  evidence_grade: B
  sources:
  - ref: LAUREL-SIGNAL-2026
    title: Laurel Signal (platform page)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/signal
    date: 2026-10
    access: full
    locator: sections 'Profitability & Pricing', 'Leverage & Resources' and Aprio quotation
  - ref: LAUREL-WORKSTUDIO-2026
    title: Laurel Work Studio (platform page)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/work-studio
    date: 2026-10
    access: full
    locator: Bonadio quotation, 'Pricing' and 'Outcome metrics' sections
  - ref: LAUREL-HOME-2026
    title: AI Timekeeping & Work Intelligence Platform (home page)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/
    date: 2026-10
    access: full
    locator: ROI claims block
  - ref: LAUREL-PROOF-2026
    title: 'Proof 2026 recap: AI in professional services starts with the work itself'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/blog/proof-2026-recap-ai-in-professional-services
    date: '2026-10-13'
    access: full
    locator: '''Work intelligence comes before the AI strategy'''
  last_reviewed: '2026-10-19'
  notes: Graded B because Aprio and The Bonadio Group are named users; both statements are testimonials on the vendor's pages and neither gives a measured result. The matter-profitability angle overlaps with scoping-pricing (fixed-fee estimates).
- id: professional-services-firm-finance-11
  title: Analyse legal bills line by line with ML and an LLM query layer to police fees and manage panels (in-house and firm)
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - review-assurance
  - data-reporting
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: shared-team-skills
  maturity: in-production
  problem: Billing codes (UTBMS) are unreliable, so reviewing invoices for block billing, skill-set mismatches or excessive time depends on narrative reading. Non-specialists find dashboard-based tools hard to query.
  solution: Legal Decoder takes LEDES exports, re-categorises every line item from its narrative using a library of more than 411,000 legal concepts, and applies 45 analytics flags (block billing, skill-set mismatch, multi-staffed meetings, excessive time, vague entries). A new LLM layer, Aperture, lets users ask questions in plain language while the numbers come from the underlying engine; identifying markers (firm, timekeeper, matter and client names) are replaced with session-specific tokens before the LLM sees data, and any finding can be exported to line items. Federal bankruptcy fee examiners in named cases (PG&E, Toys 'R' Us, Spirit Airlines, Purdue Pharma) disclose in public filings that the tool is their methodology. Legal Decoder won the Association of Corporate Counsel Value Champion award in 2025 for a partnership with UnitedLex to review UBS's highest-cost matters after its acquisition of Credit Suisse and realign staffing models.
  outcomes:
  - lever: quality
    description: The company says fee examiners in four named bankruptcy cases rely on its methodology; the CEO says courts and trustees have accepted it.
    figure: 4 named cases
    measures: bankruptcy matters the CEO cited in which fee examiners disclose Legal Decoder as the methodology behind their analysis; not a count of all uses
    provenance: vendor-published
    source_ref: LAWSITES-DECODER-2026
  prerequisites:
  - LEDES billing data exports via secure FTP or API
  - An e-billing system alongside it (the vendor says it complements Brightflag or Legal Tracker, and does not process payments)
  - Agreement with firms on how findings are used
  risks_and_guardrails:
  - LLM answers can vary between runs; the vendor says only the narrative varies and the numbers do not (LAWSITES-DECODER-2026).
  - 'Data protection: the tokenization step keeps identifiable client data from the LLM, per the vendor.'
  - '''Validated in federal court proceedings'' means approved for use by fee examiners, not a performance measure.'
  human_checkpoints:
  - Skeptical users can check findings against the underlying invoices via CSV export
  - Legal ops or the fee examiner decides what to dispute
  role_evolution: Legal ops and pricing teams review flagged exceptions across all lines rather than sample invoices. Legal Decoder won the True Value Partnering Institute's Legal Pricing Vendor of the Year award in 2025 and 2026; the institute's members include pricing professionals at large law firms (LAWSITES-DECODER-2026).
  evidence_grade: B
  sources:
  - ref: LAWSITES-DECODER-2026
    title: Legal Decoder Introduces Aperture, A Natural Language Interface for Querying Legal Billing Data
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/07/legal-decoder-introduces-aperture-a-natural-language-interface-for-querying-legal-billing-data.html
    date: '2026-07-15'
    access: full
    locator: sections 'AI Layered on Machine Learning', 'Tokenization Before the LLM', 'Court-Validated Analytics' and 'Complement to E-Billing'
  last_reviewed: '2026-10-19'
  notes: In-house (and firm pricing teams). The core ML engine is in use; the Aperture LLM layer launched 2026-07-15. No published error rate or override rate for the flags; the court use is disclosure of methodology and is the closest thing to independent validation. Single source, interview-based.
- id: professional-services-firm-finance-12
  title: Finance-operations agents inside the billing system for rates, general-ledger forecasting, appeals and collections
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - data-reporting
  - transaction-processing
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Finance teams spend time assembling context across billing, receivables, time and rate data, and on spreadsheet work to forecast, track rate changes and chase deductions.
  solution: Aderant's Agent Center offers agents that use data already in licensed Aderant products. The Rates Agent explains which rates apply, tracks changes and supports governed requests, approvals and opt-outs. The GL Forecasting Agent combines recent actuals with forward estimates, confidence ranges and variance analysis and explains the main drivers. The Appeals Agent ranks e-bill deduction appeal opportunities and drafts appeals. The Collections Agent prioritises receivables and drafts outreach. Aderant says agents prepare, prioritise and draft, and the team reviews and decides.
  outcomes:
  - lever: capacity
    description: No outcome published; the page states aims such as recovering more deductions, forecasting faster and drafting follow-up.
    figure: none published
    measures: n/a
    provenance: vendor-published
    source_ref: ADERANT-AGENTS-2026
  prerequisites:
  - Licensed Aderant products holding billing, receivables, time, rate and financial data
  - Permissions and firm controls configured so agents respect them
  risks_and_guardrails:
  - Aderant says agents follow product permissions and leave a record of information used and work prepared; no independent evaluation is published.
  - A forecast agent's explanations of drivers need verification against ledger data.
  human_checkpoints:
  - Finance staff review drafts of appeals and outreach
  - Rate requests go through governed approvals
  role_evolution: Billing, rates and collections staff review agent drafts rather than assemble information.
  evidence_grade: C
  sources:
  - ref: ADERANT-AGENTS-2026
    title: 'Aderant Agent Center: AI Agents for Legal Business Operations'
    publisher: Aderant
    type: vendor
    url: https://www.aderant.com/aderant-agent-center/
    date: 2026-10
    access: full
    locator: '''Meet the Aderant Agents'' section'
  last_reviewed: '2026-10-19'
  notes: Product documentation only; no customer, date of availability or result. The Time Agent, Appeals Agent and Collections Agent belong with billing-collections (see Routed). The Rates and GL Forecasting agents are the firm-finance elements.
- id: professional-services-firm-finance-13
  title: Capture time automatically and draft entries from what lawyers actually did, to reduce unrecorded work and speed collection
  archetype: professional-services
  module: firm-finance
  function: finance-accounting
  work_types:
  - transaction-processing
  - data-reporting
  pattern: intake-triage
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Timekeepers reconstruct their day from memory, so billable work is missed, narratives are thin, and bills draw write-downs or disputes.
  solution: Laurel captures activity across applications and drafts review-ready time entries. At Tonkon Torp, a Portland law firm, Laurel is said to capture 21 extra minutes a day per lawyer and about $20,000 a year more revenue per timekeeper; the firm's managing partner says analytical work shows more time captured each day. Warren Averett, an accounting firm of 750+ professionals, rolled Laurel out in its AI programme; its CIO said staff had to submit the prior day's time by 9:00 a.m. On 2026-10-13 Legora and Laurel announced that Laurel will turn tasks completed in Legora into draft time entries with client, matter and narrative; availability details are to follow. In ILTA's 2026 survey, 51% of respondent firms listed Laurel as being tested or piloted.
  outcomes:
  - lever: capacity
    description: 'Tonkon Torp: 21 extra minutes captured per lawyer per day, about $20,000 more revenue per timekeeper a year, a 20% faster collection cycle and 18% more entries released per day.'
    figure: 21 min/day; ~$20,000; 20%; 18%
    measures: 'from Laurel''s customer story on Tonkon Torp: average extra minutes captured per attorney per day; approximate additional annual revenue per timekeeper; speed-up of the collection cycle; increase in entries released per day. The firm''s managing partner is quoted on ''analytical work'', but the page does not attribute the figures to a firm analysis'
    provenance: vendor-published
    source_ref: LAUREL-TONKON-2026
  - lever: experience
    description: 51% of ILTA survey respondent firms listed Laurel among products being tested or piloted.
    figure: 51%
    measures: share of respondent firms (508 firms in the survey) listing Laurel as tested or piloted, as reported by LawSites; deployment or outcomes not measured
    provenance: independent
    source_ref: LAWSITES-ILTASURVEY-2026
  prerequisites:
  - Capture agents across email, documents, calendar and legal applications
  - A mapping from activity to client and matter
  - Review step for timekeepers before release
  - Integration with the time and billing system
  risks_and_guardrails:
  - Entries must reflect time actually spent on the matter (CALBAR-GENAI-2026).
  - More captured time can raise write-downs if clients dispute it; Laurel's own billing product exists to catch guideline breaches before bills go out (LAUREL-BILLING-2026).
  human_checkpoints:
  - The timekeeper reviews, groups and releases drafted entries
  role_evolution: Lawyers review drafted entries instead of reconstructing the day; billing teams get cleaner narratives and codes.
  evidence_grade: B
  sources:
  - ref: LAUREL-TONKON-2026
    title: Tonkon Torp LLP embraces Laurel for superior client service and timekeeper happiness (customer story)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/tonkon-torp
    date: 2026-10
    access: full
    locator: '''After Laurel'' summary and ''Building trust with clients'''
  - ref: LAUREL-WARREN-2026
    title: How Warren Averett turned time entry into a competitive advantage (customer story)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/warren-averett
    date: 2026-10
    access: full
    locator: problem and rollout sections
  - ref: LAWSITES-LAUREL-2026
    title: Legora and Laurel Partner to Enable Automatic Time Capture; Will Later Develop Measures of Legora's Value to Firms
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/legora-and-laurel-partner-to-enable-automatic-time-capture-will-later-develop-measures-of-legoras-value-to-firms.html
    date: '2026-10-13'
    access: full
    locator: body
  - ref: LAWSITES-ILTASURVEY-2026
    title: Which AI Product Is Most Popular Among Law Firms? Findings of ILTA's Tech Survey May Surprise You
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/09/which-ai-product-is-most-popular-among-law-firms-findings-of-iltas-tech-survey-may-surprise-you.html
    date: '2026-09-14'
    access: full
    locator: list of products firms are testing or piloting
  - ref: LAUREL-BILLING-2026
    title: 'Coming Soon: Laurel Billing - Defend every bill before it goes out'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/blog/coming-soon-laurel-billing
    date: '2026-09-17'
    access: full
    locator: section 'Laurel Billing - your rules, enforced by an agent'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: page 8
  last_reviewed: '2026-10-19'
  notes: 'Grade B, not A: the Tonkon Torp figures are in a vendor customer story and are not attributed to the firm''s own tracked data, and time capture is an adjacent process (billing-collections). Outcomes are therefore not independent. The story gives 20 minutes in its summary and 21 in the text. The Legora-Laurel entries are announced, not live. Primary home for time capture and pre-bill review is billing-collections (see Routed).'
- id: professional-services-firm-finance-14
  title: Fund a proprietary, firm-owned AI platform as a multi-year capital investment instead of renting vendor tools
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - software-systems
  - expert-judgment
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: piloting
  problem: Large firms worry that licensing the same tools as rivals yields no advantage, that vendor prices keep rising, and that vendors become competitors to clients.
  solution: Kirkland & Ellis has said it will build its own AI platform; the Financial Times and Bloomberg Law report a $500 million commitment, with more than $100 million in the first year, and a multi-year relationship with Palantir. Its first tool is a fund formation engine. Bloomberg Law reports the firm has more than 180 AI engineers and data scientists, about 50 dedicated engineers engaged (roughly 35 through partners and more than 15 in-house), and more than 250 attorneys, including about 100 equity partners, in 'AI Pods' and custom builds. The platform is model-agnostic. The firm had nearly 40 AI and legal-technology openings, including an 'AI Infrastructure Director'. AI Weekly (summarising the FT) adds that Clifford Chance launched an AI knowledge-management system with Microsoft and Epiq Advisory in July 2026 and A&O Shearman is co-developing tools with Microsoft and Harvey, while Ropes & Gray's CIO said building proprietary tools did not appear to make sense for the firm at present.
  outcomes:
  - lever: growth
    description: Kirkland committed $500 million, with more than $100 million scheduled for year one; it did not provide return-on-investment benchmarks.
    figure: $500 million; >$100 million in year one
    measures: commitment reported by the Financial Times and Bloomberg Law and treated by Kirkland as a standing commitment (it declined to give ROI benchmarks); not actual spend or return
    provenance: self-reported
    source_ref: BLOOMBERGLAW-KIRKLAND-2026
  prerequisites:
  - A revenue base able to fund a multi-year build
  - Engineers and data scientists alongside lawyers
  - Infrastructure for models and data (the job postings mention on-premise GPU clusters and Azure AI services)
  - Architecture that avoids lock-in to a single provider
  risks_and_guardrails:
  - Kirkland did not say what would make leadership reassess if AI capabilities commoditised faster than expected (BLOOMBERGLAW-KIRKLAND-2026).
  - A Radiant Law piece argues a $500 million build only works for a firm of Kirkland's size (RADIANT-TOKENS-2026, vendor commentary).
  human_checkpoints:
  - Equity partners participate in AI Pods that define custom builds
  role_evolution: Engineering roles appear inside the firm, including infrastructure leadership; partners join product pods.
  evidence_grade: B
  sources:
  - ref: BLOOMBERGLAW-KIRKLAND-2026
    title: Kirkland's $500 Million AI Gambit Requires a Cast of Hundreds
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/kirklands-500-million-ai-gambit-requires-a-cast-of-hundreds
    date: '2026-06-15'
    access: full
    locator: first four paragraphs and 'Now Hiring' section
  - ref: AIWEEKLY-KIRKLAND-2026
    title: Kirkland Bets $500M on In-House AI, Partners With Palantir
    publisher: AI Weekly
    type: press
    url: https://aiweekly.co/alerts/kirkland-bets-500m-on-in-house-ai-partners-with-palantir
    date: '2026-09-03'
    access: full
    locator: body (Ropes & Gray remark; Clifford Chance and A&O Shearman examples)
  - ref: RADIANT-TOKENS-2026
    title: Legal has a token problem, and the industry is just starting to notice
    publisher: Radiant Law
    type: vendor
    url: https://www.radiantlaw.com/resources/legal-has-a-token-problem-and-the-industry-is-just-starting-to-notice
    date: 2026-10
    access: full
    locator: 'section ''BigLaw''s answer: own the infrastructure'' (vendor commentary)'
  last_reviewed: '2026-10-19'
  notes: 'Grade B: a named firm with a disclosed budget and team, no measured return. Maturity is ''piloting'': the fund formation tool was reported as launched in early June 2026 (headline in Bloomberg Law related stories), but no usage was seen. The nearly 40 job postings are reported by Bloomberg Law; the postings themselves were not opened.'
- id: professional-services-firm-finance-15
  title: License or sell firm-built AI tools to other firms and clients as a new revenue line
  archetype: professional-services
  module: firm-finance
  function: product-service-development
  work_types:
  - software-systems
  - document-production
  pattern: other
  ladder: augment
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: Firms that invest heavily in AI look for ways to recover the cost and monetise their knowledge.
  solution: Bloomberg Law reports that A&O Shearman plans to sell its AI tools, in part focused on fund formation, to other firms, that Fried Frank is considering client use of its proprietary fund formation AI tool, and that Kirkland has emphasised exclusivity.
  outcomes:
  - lever: growth
    description: none published
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: BLOOMBERGLAW-KIRKLAND-2026
  prerequisites:
  - Owned or licensable technology
  - Separation of confidential client data from the tool
  - A commercial and support model unlike legal services
  risks_and_guardrails:
  - Selling tools to competitors changes the firm's competitive position; Kirkland's exclusivity stance is the contrast.
  human_checkpoints:
  - Firm leadership decides what is offered externally
  role_evolution: Product management and commercialisation roles appear in firms.
  evidence_grade: C
  sources:
  - ref: BLOOMBERGLAW-KIRKLAND-2026
    title: Kirkland's $500 Million AI Gambit Requires a Cast of Hundreds
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/kirklands-500-million-ai-gambit-requires-a-cast-of-hundreds
    date: '2026-06-15'
    access: full
    locator: paragraph beginning 'That question has direct competitive relevance'
  last_reviewed: '2026-10-19'
  notes: One sentence in one article; wording is 'plans' and 'contemplating'. No product, price or customer.
- id: professional-services-firm-finance-16
  title: Accounting firms take private equity capital to fund talent, technology and innovation, and share ownership with staff
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: A partnership distributes most profit annually and has little capital for technology and talent; AI raises the investment needed while threatening the hours that fund the pyramid.
  solution: Crowe, ranked No. 12 on Accounting Today's 2026 Top 100 with $1.4 billion in revenue, 539 partners and 5,600+ employees, announced an investment from KKR in June 2026 that closed in August, and said it plans to use the capital on talent, technology and innovation. It has since introduced CroweONE, a shared-ownership plan for employees with no upfront investment. Blake Oliver argues that AI undermines the PE roll-up model, pointing to CBIZ, the only US-listed accounting firm, whose stock was around $35 in June 2026 against about $90 in early 2025.
  outcomes:
  - lever: growth
    description: Crowe says it plans to use KKR capital on talent, technology and innovation; no AI-specific amount or result is given.
    figure: none published
    measures: n/a
    provenance: self-reported
    source_ref: AT-CROWE-2026
  prerequisites:
  - Partner agreement on outside capital
  - Governance that preserves independence rules for assurance work
  - A plan for how technology spend turns into pricing and margin
  risks_and_guardrails:
  - Blake Oliver argues PE finds efficiencies within an existing model but is not designed to reinvent it, and that hourly billing makes AI productivity cut revenue (BLAKEOLIVER-PE-2026, commentary).
  - A CPA Trendlines headline makes a similar point; only the standfirst was readable (CPATRENDLINES-PE-2026).
  human_checkpoints:
  - Partners vote on the transaction; leadership sets how capital is allocated
  role_evolution: Employees receive a share-ownership programme (CroweONE); the article does not describe AI-related role changes.
  evidence_grade: B
  sources:
  - ref: AT-CROWE-2026
    title: Crowe launches shared ownership plan
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/crowe-launches-esop-with-kkr-investment
    date: '2026-10-19'
    access: full
    locator: body
  - ref: BLAKEOLIVER-PE-2026
    title: The Private Equity Accounting Bet Is Starting to Look Shaky (Blake Oliver)
    publisher: Blake Oliver (The Accounting Podcast)
    type: community
    url: https://www.blakeoliver.com/blog/private-equity-bet-on-accounting
    date: '2026-06-11'
    access: full
    locator: sections 'What Is the Market Saying?' and 'The Billing Model Problem'
  - ref: CPATRENDLINES-PE-2026
    title: Private Equity's Big Bet Faces an AI Shake-Up
    publisher: CPA Trendlines Research
    type: press
    url: https://cpatrendlines.com/2026/06/19/private-equitys-big-bet-on-law-and-accounting-faces-an-ai-shake-up/
    date: '2026-06-19'
    access: search-only
    locator: standfirst only (paywalled)
  last_reviewed: '2026-10-19'
  notes: B for a named, closed deal, but AI is only implied by 'technology and innovation'. Search results also named Grant Thornton (New Mountain Capital, January 2025) and Baker Tilly (Hellman & Friedman, February 2024) as earlier PE deals; these were not opened and carry no weight here.
- id: professional-services-firm-finance-17
  title: Law firms use management-services-organisation structures to bring in outside capital for technology, AI and expansion
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: US rules bar non-lawyer ownership of law practices and fee sharing, and partnerships keep little retained cash for technology, so firms cannot easily fund AI.
  solution: In an MSO, the 'business of law' (technology, HR, marketing, finance, real estate) sits in a separate entity that an investor can own, and the law firm pays it fees. Winston & Strawn's alert lists technology and AI investment among four pillars of value creation and notes realization below 85% as an improvement opportunity for investors. Best Law Firms reports that Charlesbank Capital Partners reportedly signed a letter of intent for a stake in the 570-lawyer insurance-defence firm Wood Smith Henning & Berman at a reported $700 million, through an MSO, and that Tyson & Mendes was in similar talks. Lawfront Group, a PE-backed UK consolidator that has acquired seven regional firms in four years, brought seven technology stacks with them; its head of innovation and AI spoke at ILTACON about token costs.
  outcomes:
  - lever: growth
    description: Reported valuation for the Wood Smith stake of about 15x (FT) to 18x (other reports) earnings; letter of intent, not a closed deal.
    figure: 15x-18x
    measures: multiple of earnings implied by the reported $700 million stake, using the Financial Times' $46 million profit estimate or other reports' roughly $38 million EBITDA
    provenance: independent
    source_ref: BESTLAW-WSHB-2026
  prerequisites:
  - A state regime that permits the MSO structure
  - Separation of legal judgment from management control
  - A management services agreement fixing fees
  risks_and_guardrails:
  - Colorado enacted a ban on lawyers sharing fees with non-lawyers and with alternative business structures in August (2026), and Illinois restricted non-lawyer interference and requires MSO disclosure to clients (BESTLAW-WSHB-2026).
  - ABA Model Rule 5.4 remains the main barrier (BESTLAW-WSHB-2026).
  - Best Law Firms notes that states are increasing scrutiny of non-lawyer investment rules and that large firms are 'taking meetings' to learn what peers are doing (BESTLAW-WSHB-2026).
  human_checkpoints:
  - Lawyers retain exclusive control over legal matters (WINSTON-PE-2026)
  role_evolution: Operational management shifts to a professional business-side team; lawyers' pay and incentives are renegotiated with the MSO.
  evidence_grade: C
  sources:
  - ref: WINSTON-PE-2026
    title: 'Law firms: The next frontier for private equity in professional services?'
    publisher: Winston & Strawn (now Winston Taylor)
    type: firm
    url: https://www.winston.com/en/insights-news/law-firms-the-next-frontier-for-private-equity-in-professional-services
    date: '2026-03-19'
    access: full
    locator: sections 'The Core Tension of Law Firm Economics', key metrics table and 'Four Pillars of Value Creation'
  - ref: BESTLAW-WSHB-2026
    title: 'Private Equity''s Biggest Law Firm Bet Yet: Inside the $700M Charlesbank-WSHB Deal (David L. Brown)'
    publisher: Best Law Firms
    type: press
    url: https://www.bestlawfirms.com/articles/private-equity-law-firm-charlesbank-wood-smith-700-million/8482
    date: '2026-09-16'
    access: full
    locator: sections on the MSO structure and 'Expansion Plans'
  - ref: TRI-METER-2026
    title: 'Ferraris for emails: At ILTACON 2026, the industry starts reading the meter'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter
    date: '2026-09-09'
    access: full
    locator: paragraph quoting Lawfront's James Grice
  last_reviewed: '2026-10-19'
  notes: 'Grade C: the evidence is law-firm commentary and a reported letter of intent. AI funding is a stated rationale, not shown by a use. A search summary also named Orion Legal MSO (January 2026) and a Rafi Law Group MSO with $125 million from an unnamed PE backer; those were seen only in search results and are not relied on. Holland & Knight pages on the topic returned 403.'
- id: professional-services-firm-finance-18
  title: Start AI-native firms whose staffing and ownership are built around agents, not the traditional pyramid
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
  maturity: in-production
  problem: Incumbent firms are tied to hourly billing and junior leverage; new entrants claim they can deliver at lower cost without that structure.
  solution: General Legal, founded by Casetext's former chief technology officer after the CoCounsel sale, is described as an AI-native law firm that works through an MSO structure so that an investable technology company can operate alongside the law firm. Six months out of Y Combinator it has about 400 clients, a new venture financing practice and an MCP server for clients' AI agents. Its chief executive, who is not a lawyer, says an AI-native firm paradoxically depends on hiring highly experienced lawyers. In consulting, the Financial Times (via Resultsense) reports AI-native firms such as Queen's Tower Advisory targeting teams that are '20 per cent humans, 80 per cent AI agents'.
  outcomes:
  - lever: growth
    description: General Legal reports about 400 clients six months after leaving Y Combinator.
    figure: about 400 clients
    measures: client count stated in the LawNext episode summary, in the founder's account
    provenance: self-reported
    source_ref: LAWSITES-GENERAL-2026
  prerequisites:
  - Experienced lawyers to review agent work
  - An MSO or equivalent structure for investment
  - Technology built around the firm's workflows
  risks_and_guardrails:
  - The founder's claim that AI can automate 95% of routine legal work is an opinion, not a measured result.
  - MSO structures face growing state restrictions (BESTLAW-WSHB-2026).
  human_checkpoints:
  - Experienced lawyers review and take responsibility (as described by the founder)
  role_evolution: The founder says an AI-native firm hires more experienced lawyers rather than supercharging juniors (LAWSITES-GENERAL-2026).
  evidence_grade: B
  sources:
  - ref: LAWSITES-GENERAL-2026
    title: 'LawNext: From Product to Practice - Why Casetext''s Former CTO Founded General Legal, An AI Native Law Firm (episode description)'
    publisher: LawSites / LawNext podcast
    type: podcast
    url: https://www.lawnext.com/2026/07/lawnext-from-product-to-practice-why-casetexts-former-cto-founded-general-legal-an-ai-native-law-firm.html
    date: '2026-07-27'
    access: full
    locator: episode summary paragraphs 1-2
  - ref: RESULTSENSE-2026
    title: AI threatens Big Four scale advantage as UK boutiques attack
    publisher: Resultsense (summarising FT and City AM)
    type: press
    url: https://www.resultsense.com/news/2026-05-28-ai-consulting-big-four-reckoning/
    date: '2026-05-28'
    access: full
    locator: paragraph on Queen's Tower Advisory (secondary, FT)
  - ref: BESTLAW-WSHB-2026
    title: 'Private Equity''s Biggest Law Firm Bet Yet: Inside the $700M Charlesbank-WSHB Deal (David L. Brown)'
    publisher: Best Law Firms
    type: press
    url: https://www.bestlawfirms.com/articles/private-equity-law-firm-charlesbank-wood-smith-700-million/8482
    date: '2026-09-16'
    access: full
    locator: sections on MSO regulation
  last_reviewed: '2026-10-19'
  notes: Audio not listened to. Grade B for the operating firm; the consulting challenger is a stated target, not evidence of operation.
- id: professional-services-firm-finance-19
  title: Set partner expectations and recognition around AI adoption, and give partners a plan to monetise it
  archetype: professional-services
  module: firm-finance
  function: people-hr
  work_types:
  - coordination-scheduling
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: announced
  problem: Firm AI strategies exist on paper, but partners, who decide billing and staffing, do not link them to their economics; those who use AI daily see far more impact than those who do not.
  solution: 'PwC''s US chief executive said partners who resist AI ''have no place at the firm'' and that no one gets a free pass. The TRI 2026 Stand-out Lawyers Survey describes partners as the commercial transmission mechanism of the firm and finds a gap between having an AI strategy and a plan to monetise it. It recommends practical leadership support: accuracy information, use-case training and feedback loops.'
  outcomes:
  - lever: growth
    description: Only 25% of stand-out lawyers strongly agree their firm has a plan for monetising AI usage; those embedded with AI are nine times more likely than minimal users to report significant efficiency and quality impact.
    figure: 25%; 9x
    measures: share of client-nominated stand-out lawyers (2,527 interviews) who strongly agree their firm has a monetisation plan; relative likelihood of reporting significant AI impact for embedded versus minimal-use partners
    provenance: independent
    source_ref: TRI-STANDOUT-2026
  prerequisites:
  - Partner-level data on AI use
  - Training based on real use cases
  - Clear information on tool accuracy and verification
  risks_and_guardrails:
  - Time to experiment alone is unlikely to raise adoption (TRI-STANDOUT-2026).
  - TRI reports that perceived misalignment between a professional's AI preferences and the firm's strategy raises the risk of attrition (TRI-FOP-LAW-2026).
  human_checkpoints:
  - Firm leadership sets expectations; practice leaders review use
  role_evolution: PwC says senior staff not 'paranoid about being AI-first' would probably be replaced (CPAPA-PWC-2026).
  evidence_grade: C
  sources:
  - ref: CPAPA-PWC-2026
    title: PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'
    publisher: CPA Practice Advisor (reporting the Financial Times)
    type: press
    url: https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/
    date: '2026-03-25'
    access: full
    locator: opening paragraphs (second-hand from the FT)
  - ref: TRI-STANDOUT-2026
    title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: key takeaways and 'AI strategy is visible, but confidence is weak'
  - ref: TRI-FOP-LAW-2026
    title: What the '2026 Future of Professionals Report' says law firm leaders should be doing now
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/future-of-professionals-law-firms-paper-2026
    date: '2026-07-21'
    access: full
    locator: section on dealing with AI-driven challenges
  last_reviewed: '2026-10-19'
  notes: Statement of intent plus survey; no named firm reports compensation or promotion changes. Talent-pipeline effects are routed to talent-learning.
- id: professional-services-firm-finance-20
  title: Report AI-enabled savings and value to clients matter by matter, and negotiate how gains are shared
  archetype: professional-services
  module: firm-finance
  function: sales-marketing-bd
  work_types:
  - client-interaction
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Clients ask for AI-use disclosure, AI line items on invoices and proof of savings; most firms say they are still gathering data.
  solution: 'Firm leads at Legalweek 2026 described clients asking how AI is used on their matters and how it generates savings; Ropes & Gray''s director of technology innovation said clients are beginning to ask for line-item transparency on invoices; DLA Piper''s AI innovation head advised firms to lead the AI ROI conversation. Legora and Laurel plan a second phase to measure use and value of Legora to firms. TRI suggests a sequence for client conversations: what changed about the work, what changed for the client, what value that created, and how pricing should reflect it.'
  outcomes:
  - lever: experience
    description: 'Share of surveyed firms reporting client demand: greater use of technology for efficiencies 37%; increased financial transparency 36%; increased visibility of resourcing 36%; greater demonstration of investment value 30%.'
    figure: 30-37%
    measures: percentage of firms reporting each client request, per BigHand's 2026 finance report as relayed by a BigHand manager
    provenance: vendor-published
    source_ref: LEGALFUTURES-BIGHAND-2026
  prerequisites:
  - Matter-level data on how AI was used and what it changed
  - A shared framework with the client for measuring savings
  - Partners willing to hold the conversation
  risks_and_guardrails:
  - Some clients issue guidelines refusing to pay for AI-done work while also demanding AI adoption (TRI-LEGALWEEK-2026).
  - Disclosure terms should match fee agreements (CALBAR-GENAI-2026).
  human_checkpoints:
  - Partners agree the AI value narrative with each client
  role_evolution: Pricing and client-development roles take on AI value reporting; TRI notes that only about one-third of heavy-AI-user partners have discussed AI with 60% or more of their clients.
  evidence_grade: C
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: sections 'Proving AI's path to saving clients money' and 'The contradictions in the room'
  - ref: LEGALFUTURES-BIGHAND-2026
    title: Navigating the legal AI productivity-profitability paradox (Alec Koster, BigHand)
    publisher: Legal Futures
    type: press
    url: https://www.legalfutures.co.uk/blog/navigating-the-legal-ai-productivity-profitability-paradox/print/
    date: '2026-03-17'
    access: full
    locator: table of client requests
  - ref: TRI-STANDOUT-2026
    title: 'Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: '''How to talk to clients about AI'''
  - ref: LAWSITES-LAUREL-2026
    title: Legora and Laurel Partner to Enable Automatic Time Capture; Will Later Develop Measures of Legora's Value to Firms
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/legora-and-laurel-partner-to-enable-automatic-time-capture-will-later-develop-measures-of-legoras-value-to-firms.html
    date: '2026-10-13'
    access: full
    locator: second-phase paragraph
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: page 8
  last_reviewed: '2026-10-19'
  notes: Demand is documented; supply (a firm reporting AI savings at matter level) is not. The client-development detail is routed to client-development.
- id: professional-services-firm-finance-21
  title: 'In-house: pay a baseline price for repeat deal work built from past data, with time kept only to trigger variance adjustments'
  archetype: professional-services
  module: firm-finance
  function: procurement-supply-chain
  work_types:
  - data-reporting
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Under hourly billing, AI efficiency lowers the client's bill and makes AI investment irrational for the firm, so firms may under-invest or absorb gains without saying so.
  solution: An unnamed general counsel at a PE portfolio company proposed that, for repeat work (more than 250 acquisitions with one firm over 15 years), the parties use the shared dataset to set a baseline price for a defined scope; the firm still tracks time, but only to trigger an adjustment, for example a 25% variance from scoped hours (offered as illustrative); unfamiliar work would be fixed-price. The author says the team introduced one AI platform in December and now reports an average of 8 hours saved per week.
  outcomes:
  - lever: capacity
    description: The in-house team reports averaging 8 hours saved per week since adopting one AI platform in December, with the most senior attorney logging 15.
    figure: 8 hours per week
    measures: average hours saved per week reported by the author's own legal team; self-reported estimate, no method stated
    provenance: self-reported
    source_ref: BLOOMBERGLAW-BILLABLE-2026
  prerequisites:
  - A shared dataset of past matters with cost and complexity
  - A trusted long-term outside firm
  - Engagement-letter language fixing the variance trigger
  risks_and_guardrails:
  - The author cites ABA Formal Opinion 512 for the point that billing for time not spent is a problem; that opinion was not opened in this run.
  - The 25% trigger is an example, not an industry rule, per the author.
  human_checkpoints:
  - Client and firm agree the baseline and trigger at engagement
  role_evolution: In-house legal operations and outside counsel pricing leads manage a dataset-backed price rather than rates.
  evidence_grade: D
  sources:
  - ref: BLOOMBERGLAW-BILLABLE-2026
    title: The Billable Hour Isn't Dead Yet, But AI Should Reshape Pricing (opinion by a general counsel)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/the-billable-hour-isnt-dead-yet-but-ai-should-reshape-pricing
    date: '2026-06-29'
    access: full
    locator: body (the three 'asks')
  last_reviewed: '2026-10-19'
  notes: Labelled an idea (opinion piece by a practitioner). In-house. The author also says the ACC and Everlaw survey found nearly a quarter will 'very likely' push for change to the billable hour; not opened.
- id: professional-services-firm-finance-22
  title: Reprice or resell the hours AI saves, and redirect freed capacity into new or advisory work
  archetype: professional-services
  module: firm-finance
  function: strategy-planning
  work_types:
  - expert-judgment
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: AI saves time but few firms turn the hours into revenue ('the leak'), and profit tracks foundations, not tool use.
  solution: 'SPI Research''s 2026 study (245 professional services firms) says 43.6% of projects now use AI, that higher profit goes only to firms with the right foundations, and that AI saves time but few firms turn those hours into revenue. TRI makes the same point for tax and accounting: the freed time is not itself billable, but what a firm does with it is. TRI''s Q2 2026 Law Firm Financial Index reports associates and non-equity partners carrying most of the incremental workload, with the non-equity to equity partner hours ratio at its highest since late 2018.'
  outcomes:
  - lever: growth
    description: 84.8% of surveyed firms say AI saves them time; the share who say it generates revenue is hidden on the landing page.
    figure: 84.8% (time) vs not shown (revenue)
    measures: share of respondents (245 PSOs and ESOs) who say AI saves them time, versus the share who say it generates revenue
    provenance: independent
    source_ref: SPI-AI-2026
  - lever: growth
    description: Ratio of hours worked by non-equity partners to equity partners reached its highest level since late 2018.
    figure: highest since late 2018
    measures: ratio of non-equity partner to equity partner hours worked, from the Q2 2026 Law Firm Financial Index; not attributed to AI by the source
    provenance: independent
    source_ref: TRI-LFFI-Q2-2026
  prerequisites:
  - Pricing flexibility
  - Advisory or new-service capability to absorb capacity
  - Measurement of where saved hours go
  risks_and_guardrails:
  - The SPI report is paid and was not read; only the landing-page headline is used.
  - The LFFI leverage shift is not attributed to AI by TRI.
  human_checkpoints:
  - Practice leaders decide how freed capacity is redeployed
  role_evolution: Leverage is shifting toward non-equity partners and associates (TRI-LFFI-Q2-2026).
  evidence_grade: C
  sources:
  - ref: SPI-AI-2026
    title: The 2026 Impact of AI on Professional Services (report landing page)
    publisher: SPI Research
    type: survey
    url: https://spiresearch.com/reports/2026-ai-professional-services-survey/
    date: 2026-10
    access: full
    locator: 'headline numbers: 43.6%, and ''The Leak'''
  - ref: TRI-CHARGING-2026
    title: If AI can do the work, then what are you actually charging for?
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/what-are-you-actually-charging-for
    date: '2026-10-02'
    access: full
    locator: key insights
  - ref: TRI-LFFI-Q2-2026
    title: 'Q2 2026 LFFI: A heavier load, yet a faster crossing'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed
    date: '2026-08-10'
    access: full
    locator: section 'Who's actually doing the rowing'
  last_reviewed: '2026-10-19'
  notes: Framework and survey signal, no named firm.
```

---

## 3. Module notes

### Processes and key steps, with work types

- **Rate setting and annual rate rounds** (expert-judgment, data-reporting). Standard rates, discounts and worked rates; BigHand's survey finds 96% of firms raised rates in the past 12 months (BIGHAND-FINANCE-2026). Large firms raised standard rates faster than worked rates and accepted deeper discounts, while midsize firms did the reverse (TRI-LFFI-Q1-2026).
- **Work capture, billing and collection** (transaction-processing, data-reporting). Time capture, pre-bill review, appeals and collections feed realization (LAUREL-BILLING-2026, ADERANT-AGENTS-2026). Home module is billing-collections; this module covers the firm-level view.
- **Realization and matter profitability** (data-reporting). Comparing recorded to actual time, cost to revenue as a matter runs, leverage by rank (LAUREL-SIGNAL-2026).
- **Budgeting, forecasting and general ledger** (data-reporting). Forecasts from actuals plus forward estimates (ADERANT-AGENTS-2026).
- **Partner economics and leverage** (expert-judgment). Hours ratio of non-equity to equity partners at its highest since late 2018 (TRI-LFFI-Q2-2026).
- **AI investment, procurement and spend monitoring** (data-reporting, coordination-scheduling). Seat licences giving way to usage-based terms, usage by user and matter (TRI-METER-2026, BAKERDONELSON-TOKENS-2026).
- **AI value measurement** (data-reporting). Adoption thresholds, usage by rank, value tied to time and matter data (TRI-ILTACON-IMPL-2026, LAUREL-SIGNAL-2026).
- **Capital structure and ownership** (expert-judgment). PE capital, shared ownership, MSOs (AT-CROWE-2026, WINSTON-PE-2026).
- **Client commercial conversations about AI** (client-interaction). Disclosure, savings, line items and how gains are shared (TRI-LEGALWEEK-2026).

### Common pain points

- **Reported profit and realized profit diverge.** BigHand reports 89% of surveyed firms with year-over-year increases in write-offs, half citing aged work in progress as the main cash-flow pressure, and 26% naming cash-flow predictability as their top concern (BIGHAND-FINANCE-2026).
- **Strong inputs, flat output.** The Q1 2026 Law Firm Financial Index stood at 55, equal to its long-run average, despite worked-rate growth near 10% at the Am Law 100 and 2.7% demand growth (TRI-LFFI-Q1-2026); Q2 rose sharply (TRI-LFFI-Q2-2026).
- **AI efficiency under hourly billing.** A BigHand manager calls the gap between efficiency and financial results the "AI productivity and profitability paradox" (LEGALFUTURES-BIGHAND-2026). Keypoint's chief executive says licence fees cut into margins while saved hours reduce revenue (LAWYERSWEEKLY-KEYPOINT-2026).
- **Cost opacity.** Lawyers cannot see token spend and tend to choose the largest model for small tasks (TRI-METER-2026). The ILTA 2026 summary says the "high cost of technology" has surged among leadership concerns (ILTA-TECHSURVEY-2026).
- **Weak measurement.** Firms say they are "still gathering the data" on savings (TRI-LEGALWEEK-2026).
- **Strategy not reaching the partner.** Only 25% of stand-out lawyers strongly agree their firm has a plan to monetise AI use (TRI-STANDOUT-2026).

### Metrics and benchmarks

- **Law firm financial index.** Q1 2026 LFFI 55; Am Law 100 worked-rate growth almost 10%, above 12% at the largest firms; demand growth 2.7% (TRI-LFFI-Q1-2026). Q2 2026: index climbed, Am Law 100 revenue per FTE grew strongly and profit per FTE faster (TRI-LFFI-Q2-2026).
- **2025 market year.** Average firm profit growth 13%, worked rates up 7.3% (TRI-SOTLM-REPORT-2026); technology spend up nearly 11% and KM spend about 10%; fees worked per lawyer up 16.8% and profit per lawyer 8.4% above pre-2022 levels; firms with a clear AI strategy almost four times more likely to see ROI (TRI-SOTLM-2026). At Legalweek, TRI's Petrie said only 22% of firms have such a strategy (TRI-LEGALWEEK-2026).
- **Finance survey.** 800+ senior finance and legal leaders: 96% raised rates, 89% report higher write-offs, 90% report higher lockup, only 46% use advanced business intelligence (BIGHAND-FINANCE-2026); 32% of firms say they offer development for commercial conversations (BIGHAND-FINANCE-2026).
- **AI cost.** Ogletree's executive: AI about 1% of revenue as the converging level (TRI-METER-2026). Output tokens cost about four to six times input tokens, and one vendor changed rates in ten of the last 13 months (BAKERDONELSON-TOKENS-2026).
- **ROI tracking.** 18% of 1,500+ professionals say their organisation tracks AI ROI (TRI-AIPS-2026).
- **Adoption.** 94% of ILTA survey firms using or exploring GenAI, up from 80% (LAWSITES-ILTASURVEY-2026); 43.6% of projects now use AI at 245 services firms (SPI-AI-2026).
- **Pricing models.** 90% of legal dollars hourly (TRI-SOTLM-REPORT-2026); 78% of tax and accounting firms bill hourly (TRI-CHARGING-2026); McKinsey about a quarter of fees on outcomes (BUSINESSINSIDER-MCKINSEY-2025).
- **MSO screening metrics.** Winston & Strawn lists revenue per lawyer, profit per equity partner, leverage (4:1 or higher is favourable) and realization below 85% as improvement potential (WINSTON-PE-2026).
- **Adjacent benchmarks (architecture and engineering, not law).** Deltek: AI adoption 53% to 70%, only 38% report measurable positive impact, utilization just under 60%, operating profit 16.7% (DELTEK-CLARITY-2026).

### Guardrails and regulatory points

- **Billing.** California requires hourly bills to reflect time actually spent, treats general AI subscriptions as overhead, allows matter-specific AI costs with disclosure at actual cost and no markup without informed written consent, and notes flat fees may build in AI savings (CALBAR-GENAI-2026). The Board of Trustees approved the 2026 guidance on 2026-05-14 (CALBAR-GENAI-2026, source note).
- **Outside capital.** ABA Model Rule 5.4 is the main barrier to non-lawyer ownership; MSOs are designed around it; Colorado enacted a ban on lawyers sharing fees with non-lawyers and alternative business structures in August 2026, and Illinois restricts non-lawyer interference and requires disclosure to clients (BESTLAW-WSHB-2026). The ABA opinion was not opened here.
- **Data protection in analytics.** Legal Decoder tokenizes identifying names before data reach an LLM (LAWSITES-DECODER-2026). Laurel states no public LLMs and single-tenant AI (LAUREL-WORKSTUDIO-2026).
- **Activity monitoring.** Passive capture of work activity requires an employee-notice and privacy review; no regulator text on this was read.
- **Contracts.** Baker Donelson advises transparency on model usage, allowances, overages and price-change rights (BAKERDONELSON-TOKENS-2026).

### Frontier signals (dated)

- **2026-05-28 to 2026-06-15: Kirkland & Ellis $500 million AI platform**, with Palantir; first tool for fund formation; no ROI benchmarks (BLOOMBERGLAW-KIRKLAND-2026).
- **2026-06-23: Legora moves Agent Pro to consumption pricing** with matter-level attribution (LEGORA-CBP-2026); Law360 (2026-06-26) says the benefit for firms will not be automatic or immediate (LAW360-LEGORA-2026).
- **2026-07-08: Harvey reports fourteen-fold token growth in six months** and is understood to be developing a new pricing model (ARTLAW-HARVEY14X-2026).
- **2026-07-15: Legal Decoder announces Aperture and plans AIR and an AFA builder** (LAWSITES-DECODER-2026).
- **2026-07-16: Intapp makes Celeste generally available**, with playbooks including pricing, and early adopters BakerHostetler (intake and conflicts) and Hg (LAWSITES-CELESTE-2026).
- **2026-08: ILTACON "reading the meter"** sessions; Baker Donelson's token guide (2026-08-20) and NetDocuments' tokenomics post (2026-08-12) (TRI-METER-2026, BAKERDONELSON-TOKENS-2026, NETDOCUMENTS-TOKENS-2026).
- **2026-08: Colorado law restricting fee sharing; 2026-09-16: reported Charlesbank letter of intent for Wood Smith** at $700 million (BESTLAW-WSHB-2026).
- **2026-09-17: Laurel announces Laurel Billing** with a Compliance agent and a Scope agent for fixed fees (LAUREL-BILLING-2026).
- **2026-10: Aderant Agent Center** lists Rates, GL Forecasting, Appeals and Collections agents (ADERANT-AGENTS-2026); **2026-10-13: Legora and Laurel link AI work to time entries** and plan joint value measures (LAWSITES-LAUREL-2026).
- **2026-10-19: PwC reports FY26 revenue of $60.2 billion and $3 billion invested; Crowe launches CroweONE** after the KKR investment closed (AT-PWC-2026, AT-CROWE-2026).

### Workforce and role effects

- **Leverage shifts down the pyramid.** Associates and non-equity partners carry most extra demand; the non-equity to equity hours ratio is the highest since late 2018 (TRI-LFFI-Q2-2026).
- **New finance-adjacent roles.** Chief pricing and innovation officer (Greenberg Traurig), senior managing director of AI innovation (DLA Piper), head of innovation and AI (Lawfront), chief data and AI officer (Ogletree), knowledge counsel (Littler) (TRI-LEGALWEEK-2026, TRI-METER-2026). Kirkland had nearly 40 AI-related openings, including an AI infrastructure director (BLOOMBERGLAW-KIRKLAND-2026).
- **Legal operations moves to the front.** TRI says legal ops has become the default first line for AI pressure in legal departments, with twice as many GCs naming technology a top strategic priority as the year before (TRI-LDOR-2026). In-house.
- **Partner accountability.** PwC's US chief executive says partners who resist AI have no place at the firm (CPAPA-PWC-2026).
- **Commercial skills.** Only 32% of firms offer development for lawyers' commercial conversations (BIGHAND-FINANCE-2026).
- **Graduate hiring and pyramid effects** are routed to talent-learning.

### Objections and concerns raised

- **Clients will not accept pass-through.** Keypoint's chief executive: AI is a tool of the trade (LAWYERSWEEKLY-KEYPOINT-2026).
- **AI-bubble risk.** TRI warns that firms using AI mainly to justify higher rates are exposed if the AI bubble bursts (TRI-SOTLM-2026).
- **Efficiency makes AI investment irrational under hourly billing**, says a general counsel (BLOOMBERGLAW-BILLABLE-2026).
- **PE may not fit the new economics.** Blake Oliver argues PE roll-ups cannot reinvent a billing model (BLAKEOLIVER-PE-2026).
- **Hourly billing turns AI cost into a pass-through.** Radiant Law, a fixed-fee provider, argues that under hourly billing AI cost is something to mark up and pass on, and that uncapped token spend is a risk for in-house teams (RADIANT-TOKENS-2026, vendor commentary).
- **Cost control versus quality.** Lawyers choose the stronger, costlier option because accuracy matters (ARTLAW-HARVEY14X-2026).
- **Build or buy.** Ropes & Gray's CIO prefers buying while Kirkland builds (AIWEEKLY-KIRKLAND-2026).
- **Monitoring and privacy** of passive work capture is a concern implied by vendor security claims (LAUREL-WORKSTUDIO-2026); no practitioner source was found.

### Interview probes for an advisor

1. When AI saves hours on a matter, what happens to the bill, the write-down and the partner's credit? Who decides, and is it tracked at all?
2. What did AI cost per lawyer and per matter last quarter (seats, tokens, agents), who sees the meter, and what happens at renewal if a flat licence becomes usage-based?
3. How do you know an AI investment worked? Which measure do you use (weekly active users, hours, realization, margin), and who owns it?
4. What share of your work is priced off hours versus fixed or hybrid fees? Which clients have asked for AI line items or refused to pay for AI-done work, and how did you respond?
5. If outside capital were offered (an MSO or private equity), what would you spend it on, and what rules would you need on control and independence? For in-house teams: where do you see AI savings in outside counsel bills, and who owns that question?

---

## 4. Routed to other modules

- **billing-collections:** Laurel timekeeping and the Laurel Billing agents (LAUREL-BILLING-2026); Aderant Time, Appeals and Collections agents (ADERANT-AGENTS-2026); Legora-Laurel time entries (LAWSITES-LAUREL-2026); line-item AI billing demands (TRI-LEGALWEEK-2026). Intapp Billstream's product page was read; it gives an unattributed testimonial and no dated result, so it is not cited.
- **scoping-pricing:** Aderant Virtual Pricing Director for matter-level AI-assisted pricing, with an unnamed Am Law 100 pricing director's testimonial (ADERANT-VPD-2026, ADERANT-VPDWEB-2025); Legal Decoder's planned AFA builder; Stanford's pricing framework detail (STANFORD-DEL-2026).
- **staffing-resourcing:** Kantata and the Resource Management Institute: 52.7% of respondents not equipped to manage hybrid human-agent teams, 7.3% with outcome data routinely used in staffing, in a vendor-commissioned study of 44 organisations (KANTATA-RMI-2026); Laurel Signal's staffing forecasts (LAUREL-SIGNAL-2026).
- **talent-learning:** First-year hiring, PwC headcount down 5,600 and UK graduate cuts (RESULTSENSE-2026, secondary).
- **acceptance-risk:** Intapp Celeste's conflicts, intake and lateral-hiring playbooks and the BakerHostetler and Hg early adopters (LAWSITES-CELESTE-2026).
- **client-development:** Partners and clients not discussing AI (TRI-STANDOUT-2026); Paravo and Introhive items seen in the LawSites feed, not read.
- **knowledge-management and work-production:** Kirkland's fund formation engine and other firm-built tools as substantive work product (BLOOMBERGLAW-KIRKLAND-2026).
- **quality-review:** Cal Bar supervision duties (CALBAR-GENAI-2026) beyond billing.

---

## 5. Sources

55 sources, listed once each. Every source was opened and read except where marked `search-only`.

- **ADERANT-AGENTS-2026**. Aderant Agent Center: AI Agents for Legal Business Operations. Aderant. Type: vendor. https://www.aderant.com/aderant-agent-center/. Date: 2026-10. Access: full. Note: Undated product page; date is the retrieval month (2026-10-19).
- **ADERANT-VPD-2026**. Virtual Pricing Director: Accurate, AI-Assisted Pricing for Every Matter. Aderant. Type: vendor. https://www.aderant.com/solutions-vpd/. Date: 2026-10. Access: full. Note: Product page read through a text mirror, whose header gave 2026-10-12; date is the retrieval month.
- **ADERANT-VPDWEB-2025**. The Next Evolution of AI-Driven Law Firm Pricing: Technology, Governance, and Growth with Virtual Pricing Director (on-demand webinar page). Aderant. Type: vendor. https://www.aderant.com/webinar-on-demand/vpd-the-next-evolution-of-ai-driven-law-firm-pricing/. Date: 2025-11-20. Access: full. Note: Read through a text mirror.
- **AIWEEKLY-KIRKLAND-2026**. Kirkland Bets $500M on In-House AI, Partners With Palantir. AI Weekly. Type: press. https://aiweekly.co/alerts/kirkland-bets-500m-on-in-house-ai-partners-with-palantir. Date: 2026-09-03. Access: full. Note: Secondary summary of Financial Times reporting.
- **ARTLAW-HARVEY14X-2026**. Harvey Increases Token Use 14X in Just 6 Months. Artificial Lawyer. Type: press. https://artificiallawyer.com/2026/07/08/harvey-increases-token-use-14x-in-just-6-months. Date: 2026-07-08. Access: full.
- **AT-CROWE-2026**. Crowe launches shared ownership plan. Accounting Today. Type: press. https://www.accountingtoday.com/news/crowe-launches-esop-with-kkr-investment. Date: 2026-10-19. Access: full. Note: Editorial note on the page: an earlier version wrongly called CroweONE an ESOP.
- **AT-PWC-2026**. PwC grows 2026 global revenue to $60.2B. Accounting Today. Type: press. https://www.accountingtoday.com/news/pwc-grows-2026-global-revenue-to-60-2b. Date: 2026-10-19. Access: full.
- **BAKERDONELSON-TOKENS-2026**. AI Tokenomics Guide: Understanding Token-Based AI Pricing for Legal Technology (Justin Daniels). Baker Donelson. Type: firm. https://www.bakerdonelson.com/webfiles/Bios/Token-Pricing-Guide-for-Clients-August-2026.pdf. Date: 2026-08-20. Access: full. Note: Law firm guide written for general counsel.
- **BESTLAW-WSHB-2026**. Private Equity's Biggest Law Firm Bet Yet: Inside the $700M Charlesbank-WSHB Deal (David L. Brown). Best Law Firms. Type: press. https://www.bestlawfirms.com/articles/private-equity-law-firm-charlesbank-wood-smith-700-million/8482. Date: 2026-09-16. Access: full. Note: Reports deal terms from Pitchbook and the Financial Times as 'reportedly'.
- **BIGHAND-FINANCE-2026**. BigHand 2026 Annual Law Firm Finance Report: Profitability, Cash Flow & AI Insights (landing page). BigHand. Type: vendor. https://www.bighand.com/en-us/resources/whitepapers/2026-annual-law-firm-finance-report/. Date: 2026-01-21. Access: full. Note: Landing page only; full report not opened.
- **BLAKEOLIVER-PE-2026**. The Private Equity Accounting Bet Is Starting to Look Shaky (Blake Oliver). Blake Oliver (The Accounting Podcast). Type: community. https://www.blakeoliver.com/blog/private-equity-bet-on-accounting. Date: 2026-06-11. Access: full. Note: Commentary.
- **BLOOMBERGLAW-BILLABLE-2026**. The Billable Hour Isn't Dead Yet, But AI Should Reshape Pricing (opinion by a general counsel). Bloomberg Law. Type: press. https://news.bgov.com/business-and-practice/the-billable-hour-isnt-dead-yet-but-ai-should-reshape-pricing. Date: 2026-06-29. Access: full. Note: In-house. Author is an unnamed general counsel at a private-equity portfolio company; the page shows no byline.
- **BLOOMBERGLAW-KIRKLAND-2026**. Kirkland's $500 Million AI Gambit Requires a Cast of Hundreds. Bloomberg Law. Type: press. https://news.bgov.com/business-and-practice/kirklands-500-million-ai-gambit-requires-a-cast-of-hundreds. Date: 2026-06-15. Access: full. Note: Reports the firm's job postings; the postings themselves were not opened.
- **BUSINESSINSIDER-MCKINSEY-2025**. AI is reshaping how McKinsey makes money (Polly Thompson), read via Yahoo Finance syndication. Business Insider. Type: press. https://finance.yahoo.com/news/ai-reshaping-mckinsey-makes-money-195132745.html. Date: 2025-11-17. Access: full. Note: Outside the 12-18 month window by a few weeks; used because it is the primary report of the McKinsey figure.
- **CALBAR-GENAI-2026**. Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 edition). State Bar of California, COPRAC. Type: regulator. https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf. Date: 2026-05-14. Access: full. Note: Board of Trustees approved the updated guidance on 2026-05-14 (State Bar ethics-technology page); the PDF carries no date on its face.
- **CPAPA-PWC-2026**. PwC CEO Says Partners Who Resist AI 'Have No Place at the Firm'. CPA Practice Advisor (reporting the Financial Times). Type: press. https://www.cpapracticeadvisor.com/2026/03/25/pwc-ceo-says-partners-who-resist-ai-have-no-place-at-the-firm/180245/. Date: 2026-03-25. Access: full. Note: Second-hand account of an FT interview.
- **CPATRENDLINES-PE-2026**. Private Equity's Big Bet Faces an AI Shake-Up. CPA Trendlines Research. Type: press. https://cpatrendlines.com/2026/06/19/private-equitys-big-bet-on-law-and-accounting-faces-an-ai-shake-up/. Date: 2026-06-19. Access: search-only. Note: Paywalled; only the standfirst was readable.
- **DELTEK-CLARITY-2026**. The Latest Deltek Clarity Industry Studies Highlight AI Challenges, Talent Strain, and Delivery Capacity Pressures. Deltek. Type: survey. https://www.deltek.com/company/news/latest-deltek-clarity-industry-studies-highlight-ai-challenges/. Date: 2026-05-12. Access: full. Note: Architecture and engineering and government contracting; adjacent.
- **EDISCOVERYTODAY-ILTACON-2026**. My Five ILTACON 2026 Takeaways: Legal Technology Trends. eDiscovery Today (Doug Austin). Type: press. https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/. Date: 2026-09-04. Access: full.
- **ILTA-TECHSURVEY-2026**. The ILTA Technology Survey 2026: Executive Summary. ILTA. Type: professional-body. https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf. Date: 2026-08. Access: full. Note: PDF creation date 2026-08-14; file name suggests a June 2026 issue. 11-page executive summary.
- **KANTATA-RMI-2026**. New Study Finds Resource Management at a Strategic Crossroads as AI and Outcome-Based Delivery Reshape Professional Services. Kantata (study by Resource Management Institute). Type: survey. https://www.kantata.com/blog/article/new-study-finds-resource-management-at-a-strategic-crossroads-as-ai-and-outcome-based-delivery-reshape-professional-services. Date: 2026-04-09. Access: full. Note: Vendor-commissioned; 44 organisations.
- **LAUREL-BILLING-2026**. Coming Soon: Laurel Billing - Defend every bill before it goes out. Laurel. Type: vendor. https://www.laurel.ai/blog/coming-soon-laurel-billing. Date: 2026-09-17. Access: full.
- **LAUREL-HOME-2026**. AI Timekeeping & Work Intelligence Platform (home page). Laurel. Type: vendor. https://www.laurel.ai/. Date: 2026-10. Access: full. Note: Undated; retrieval month. Source of the 'up to 30 minutes, 4-11%, 2.88' headline claims, given without a stated basis.
- **LAUREL-PROOF-2026**. Proof 2026 recap: AI in professional services starts with the work itself. Laurel. Type: vendor. https://www.laurel.ai/blog/proof-2026-recap-ai-in-professional-services. Date: 2026-10-13. Access: full. Note: Vendor-run event on 2026-09-23 with speakers from PwC Australia, EY, Google and Freshfields; session content is summarised only in general terms.
- **LAUREL-SIGNAL-2026**. Laurel Signal (platform page). Laurel. Type: vendor. https://www.laurel.ai/platform/signal. Date: 2026-10. Access: full. Note: Undated product page; retrieval month.
- **LAUREL-TONKON-2026**. Tonkon Torp LLP embraces Laurel for superior client service and timekeeper happiness (customer story). Laurel. Type: vendor. https://www.laurel.ai/customer-stories/tonkon-torp. Date: 2026-10. Access: full. Note: Undated customer story; retrieval month. The story gives two slightly different figures: an average lift of 20 minutes a day in the summary and 21 extra minutes a day in the text.
- **LAUREL-WARREN-2026**. How Warren Averett turned time entry into a competitive advantage (customer story). Laurel. Type: vendor. https://www.laurel.ai/customer-stories/warren-averett. Date: 2026-10. Access: full. Note: Undated customer story; retrieval month.
- **LAUREL-WORKSTUDIO-2026**. Laurel Work Studio (platform page). Laurel. Type: vendor. https://www.laurel.ai/platform/work-studio. Date: 2026-10. Access: full. Note: Undated product page; retrieval month.
- **LAW360-LEGORA-2026**. Legora's New AI Pricing Model May Usher In Larger Changes. Law360 Pulse. Type: press. https://www.law360.com/articles/2494404. Date: 2026-06-26. Access: full. Note: Opening section read.
- **LAWSITES-CELESTE-2026**. Intapp Makes Celeste Generally Available, Calling It An 'AI Coworker' To Run the Business Side of Law Firms. LawSites (Bob Ambrogi). Type: press. https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html. Date: 2026-07-16. Access: full.
- **LAWSITES-DECODER-2026**. Legal Decoder Introduces Aperture, A Natural Language Interface for Querying Legal Billing Data. LawSites (Bob Ambrogi). Type: press. https://www.lawnext.com/2026/07/legal-decoder-introduces-aperture-a-natural-language-interface-for-querying-legal-billing-data.html. Date: 2026-07-15. Access: full.
- **LAWSITES-GENERAL-2026**. LawNext: From Product to Practice - Why Casetext's Former CTO Founded General Legal, An AI Native Law Firm (episode description). LawSites / LawNext podcast. Type: podcast. https://www.lawnext.com/2026/07/lawnext-from-product-to-practice-why-casetexts-former-cto-founded-general-legal-an-ai-native-law-firm.html. Date: 2026-07-27. Access: full. Note: Episode page and summary read; audio not listened to.
- **LAWSITES-ILTASURVEY-2026**. Which AI Product Is Most Popular Among Law Firms? Findings of ILTA's Tech Survey May Surprise You. LawSites (Bob Ambrogi). Type: press. https://www.lawnext.com/2026/09/which-ai-product-is-most-popular-among-law-firms-findings-of-iltas-tech-survey-may-surprise-you.html. Date: 2026-09-14. Access: full.
- **LAWSITES-LAUREL-2026**. Legora and Laurel Partner to Enable Automatic Time Capture; Will Later Develop Measures of Legora's Value to Firms. LawSites (Bob Ambrogi). Type: press. https://www.lawnext.com/2026/10/legora-and-laurel-partner-to-enable-automatic-time-capture-will-later-develop-measures-of-legoras-value-to-firms.html. Date: 2026-10-13. Access: full.
- **LAWYERSWEEKLY-KEYPOINT-2026**. 'Clients will get annoyed' if firms pass on AI costs, says Keypoint's CEO. Lawyers Weekly (Australia). Type: press. https://www.lawyersweekly.com.au/biglaw/44659-clients-will-get-annoyed-if-firms-pass-on-ai-costs-says-keypoint-s-ceo. Date: 2026-07-15. Access: full. Note: Premium-gated; the visible portion was read.
- **LEGALFUTURES-BIGHAND-2026**. Navigating the legal AI productivity-profitability paradox (Alec Koster, BigHand). Legal Futures. Type: press. https://www.legalfutures.co.uk/blog/navigating-the-legal-ai-productivity-profitability-paradox/print/. Date: 2026-03-17. Access: full. Note: Associate-sponsored blog by a BigHand solutions manager; date taken from the page text.
- **LEGORA-CBP-2026**. Introducing Consumption-Based Pricing. Legora. Type: vendor. https://legora.com/blog/consumption-based-pricing. Date: 2026-06-23. Access: full.
- **NETDOCUMENTS-TOKENS-2026**. Lawyer Tokenomics. NetDocuments (ndMAX Studio, Applied AI Team). Type: vendor. https://studio.netdocuments.com/post/lawyer-tokenomics. Date: 2026-08-12. Access: full.
- **RADIANT-TOKENS-2026**. Legal has a token problem, and the industry is just starting to notice. Radiant Law. Type: vendor. https://www.radiantlaw.com/resources/legal-has-a-token-problem-and-the-industry-is-just-starting-to-notice. Date: 2026-10. Access: full. Note: Undated page (references June 2026 events); date is the retrieval month. Fixed-fee legal services provider; marketing content. Figures it cites from Wells Fargo, Wakefield Research and others were not checked at source.
- **RESULTSENSE-2026**. AI threatens Big Four scale advantage as UK boutiques attack. Resultsense (summarising FT and City AM). Type: press. https://www.resultsense.com/news/2026-05-28-ai-consulting-big-four-reckoning/. Date: 2026-05-28. Access: full. Note: Secondary summary; figures not verified at the FT or City AM originals.
- **SPI-AI-2026**. The 2026 Impact of AI on Professional Services (report landing page). SPI Research. Type: survey. https://spiresearch.com/reports/2026-ai-professional-services-survey/. Date: 2026-10. Access: full. Note: Landing page; report is paid and was not read. Page date modified 2026-10-12.
- **STANFORD-DEL-2026**. Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives. Stanford Digital Economy Lab (Brynjolfsson, Petropoulos). Type: academic. https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf. Date: 2026-08-23. Access: full. Note: Footnote discloses a general-support gift from Accenture to the lab.
- **TRI-AIPS-2026**. 2026 AI in Professional Services Report (landing page). Thomson Reuters Institute. Type: survey. https://www.thomsonreuters.com/en/institute/reports/2026-ai-in-professional-services-report. Date: 2026-10. Access: full. Note: No publication date on the page; date is the retrieval month (2026-10-19).
- **TRI-CHARGING-2026**. If AI can do the work, then what are you actually charging for?. Thomson Reuters Institute. Type: survey. https://www.thomsonreuters.com/en/institute/articles/what-are-you-actually-charging-for. Date: 2026-10-02. Access: full. Note: Article summarising the Year-Round Tax Advisor Report (TRI and Jump), the 2026 State of Tax Professionals Report and the 2026 Future of Professionals Report.
- **TRI-FOP-LAW-2026**. What the '2026 Future of Professionals Report' says law firm leaders should be doing now. Thomson Reuters Institute. Type: survey. https://www.thomsonreuters.com/en/institute/articles/future-of-professionals-law-firms-paper-2026. Date: 2026-07-21. Access: full.
- **TRI-ILTACON-IMPL-2026**. ILTACON 2026: 'Does it make the boat faster?' How legal teams are finding AI implementation success. Thomson Reuters Institute. Type: conference. https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-finding-ai-implementation-success. Date: 2026-08-31. Access: full.
- **TRI-LDOR-2026**. 2026 Legal Department Operations Report (landing page). Thomson Reuters Institute. Type: survey. https://www.thomsonreuters.com/en/institute/reports/legal-department-operations-report-2026. Date: 2026-09-22. Access: full. Note: In-house.
- **TRI-LEGALWEEK-2026**. Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide. Thomson Reuters Institute. Type: conference. https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide. Date: 2026-03-13. Access: full.
- **TRI-LFFI-Q1-2026**. Q1 2026 LFFI: Strong inputs, average output - and the first drops of rain. Thomson Reuters Institute. Type: survey. https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output. Date: 2026-05-13. Access: full.
- **TRI-LFFI-Q2-2026**. Q2 2026 LFFI: A heavier load, yet a faster crossing. Thomson Reuters Institute. Type: survey. https://www.thomsonreuters.com/en/institute/reports/lffi-q2-2026-heavy-load-picking-up-speed. Date: 2026-08-10. Access: full.
- **TRI-METER-2026**. Ferraris for emails: At ILTACON 2026, the industry starts reading the meter. Thomson Reuters Institute. Type: conference. https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter. Date: 2026-09-09. Access: full.
- **TRI-SOTLM-2026**. State of the US Legal Market 2026 analysis: Will the AI bubble burst? A crucial warning for law firms. Thomson Reuters Institute. Type: survey. https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble. Date: 2026-01-14. Access: full.
- **TRI-SOTLM-REPORT-2026**. 2026 Report on the State of the US Legal Market: Peak prosperity and the fault lines below (executive summary page). Thomson Reuters Institute with Georgetown Law Center on Ethics and the Legal Profession. Type: survey. https://www.thomsonreuters.com/en/institute/reports/state-of-the-us-legal-market-2026. Date: 2026-01-07. Access: full.
- **TRI-STANDOUT-2026**. Turning law firm AI strategies into practice: Findings from the 2026 Stand-out Lawyers Survey. Thomson Reuters Institute. Type: survey. https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice. Date: 2026-08-06. Access: full.
- **WINSTON-PE-2026**. Law firms: The next frontier for private equity in professional services?. Winston & Strawn (now Winston Taylor). Type: firm. https://www.winston.com/en/insights-news/law-firms-the-next-frontier-for-private-equity-in-professional-services. Date: 2026-03-19. Access: full. Note: Client alert; republished after the 2026-06-01 Winston Taylor combination.

---

## 6. Gaps

- **No measured firm-level result.** No firm or in-house team publishes realization, margin, profit per partner or ROI measured before and after an AI change. Every ROI-like figure is a vendor claim, survey percentage or conference remark.
- **No job posting was opened directly.** Kirkland's careers page returned 403 and careers.kirkland.com could not be reached. The only job-posting evidence is Bloomberg Law's report of Kirkland's openings (BLOOMBERGLAW-KIRKLAND-2026). Firm finance, pricing and AI-cost roles could not be sampled.
- **Search budget ran out.** Two planned searches (Deloitte and EY FY26 results and AI investment; UK listed law firm results such as Knights and Gateley) were refused. EY, Deloitte and KPMG newsroom pages were opened but yielded no usable firm-finance AI statements. Accenture's Q4 FY26 release was read; it gave bookings and margins but no AI-specific revenue or pricing detail, so it is not cited.
- **Paywalled or blocked sources.** SPI's full 2026 report (paid), BigHand's full finance report (not opened), the ILTA full survey, Law360 and Financial Times originals, CPA Trendlines (standfirst only), Holland & Knight MSO pages (403), Aderant's own page by direct fetch (403; read through a text mirror), mckinsey.com.
- **Seen only in search results or secondary summaries, not relied on:** Orion Legal MSO (January 2026) and Rafi Law Group's $125 million MSO; Grant Thornton and Baker Tilly PE deals; Simmons & Simmons' Percy reaching 87% of fee earners and Wells Fargo's 2025 rate and revenue growth figures (both via a Radiant Law page); a Wakefield Research finding that 36% of CFOs are confident about AI outcomes and 77% of GCs report tension with their CFO (via Radiant Law); Uber's AI budget story (via Radiant Law); the ACC and Everlaw finding that nearly a quarter of in-house counsel will very likely push to change the billable hour (via a GC opinion piece).
- **McKinsey outcome share.** Business Insider reports about a quarter (and a technology leader's '20%' remark); a secondary summary says roughly a third (RESULTSENSE-2026). Only the quarter is used.
- **BigHand figures conflict between formats.** The landing page says nearly two-thirds of firms report fewer billable hours, while a BigHand manager's post says 29% report a reduction in billable hours (BIGHAND-FINANCE-2026, LEGALFUTURES-BIGHAND-2026). The full report was not opened to reconcile them.
- **In-house shared-service finance teams outside legal** (finance, HR, global business services acting like firms) were not found.
- **Rate-setting with AI.** Public evidence of AI used to set standard or worked rates is absent; the only items are rate administration (Aderant Rates Agent) and modelling products (Legal Decoder AIR). Rate-setting practice is documented by market data, not by AI deployments.
- **Partner compensation.** No source describes AI adoption entering partner compensation formulas; PwC's statement is the only item (CPAPA-PWC-2026).
- **Quality evidence.** No error rate, override rate, parallel-run or independent audit was found for AI in firm-finance tasks; the Tonkon Torp and McKinsey figures are the firms' or vendors' own.
- **Landscape refs not read.** TRI's Law Firm Rates Report 2026, the TRI 'Pricing AI-driven legal services' series, the COO and CFO Forum (scheduled for 2026-10-21 and 2026-10-22 per the landscape), Forrester's State of Technology Services, SPI maturity model detail and the Wells Fargo Legal Specialty Group survey.
