# Billing and collections: practice evidence (professional services)

Prepared 2026-10-19. Module: billing-collections (time capture to cash). Angle: practice. Method: curl, a text mirror (r.jina.ai) for pages that block direct access, `pdftotext` for the California guidance and the Virginia petition, and about 14 rationed web searches used mainly to find named deployments and vendor releases. All sources listed below were opened and read; items seen only in search results are described in Gaps and are not used in any outcome.

## 1. Summary

**17 candidate use cases: 0 grade A, 6 grade B, 10 grade C, 1 grade D (idea).** No entry reaches A because every outcome figure sits on a vendor-authored page with no stated baseline or method, and the one controlled comparison (a Big Four tax division with a random control group) is unnamed.

What the practice evidence shows:

- **Time capture is the one step with named, live deployments.** Lerners, Obermayer, Tonkon Torp and Berger Singerman (law) and Warren Averett and GHJ (accounting) describe replacing recollection-based time entry with AI-drafted entries that a person reviews. All of these come from the vendor, Laurel. Intapp and Aderant sell comparable tools but publish no measured, named-firm outcome for their AI features. Law firms at Allens and Wilson Sonsini are reported as selecting Laurel, with no results.
- **Guideline compliance is the second area with a named user.** Foley Mansfield went live firmwide with Verify for pre-bill review (2024-05-15); Intapp Terms customers (Dickinson Wright, Fredrikson & Byron) describe faster review of client obligations. Aderant signed a deal on 2025-08-07 to acquire HerculesAI's legal technology assets (billing-compliance AI), a sign that the capability is moving into the billing system vendors.
- **Everything downstream of the pre-bill is early.** Appeals, collections, rates and proforma-prioritisation agents (Aderant Agent Center early access, 2026-08-25; Elite Intelligence, 2026-02-27; Laurel Billing, announced 2026-09-17 as coming soon) are announcements with no customer results.
- **AI work is becoming a billing input.** Aderant with Harvey (live 2026-08-17), Legora with Laurel (2026-10-13) and Litify with Billables AI (2026-05-19) turn AI-platform work into draft time entries. Clients are asking for line-item AI transparency and some say they will not pay for AI-performed work (TRI-LEGALWEEK-2026).
- **Regulators constrain the hourly bill, and they differ on non-hourly fees.** California (2026) and Texas (2025) say hourly bills must reflect time actually spent; Virginia's LEO 1901 says value-based fees may reflect efficiency gains.
- **Quality evidence is essentially absent.** No source publishes an override or edit rate for AI-drafted entries, a rejection rate before and after, a parallel run, or an independent measurement. The strongest design found is the unnamed Big Four control-group comparison (LAUREL-BIGFOURTAX-2026), reported by the vendor.
- **In-house examples are thin:** one named case (Albertsons, Thomson Reuters Legal Tracker, a recollected figure) and Brightflag product pages. These are tagged in-house in the notes.

**Source count:** 50 distinct sources, all opened: vendor 37, press 6, regulator 4, conference 2, survey 1. There are no academic, standard-setter, professional-body or job-posting sources; see Gaps.

## 2. Use cases

```yaml
- id: professional-services-billing-collections-01
  title: Law firm lawyers review AI-drafted time entries built from captured email, document and call activity instead of reconstructing time from memory
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - transaction-processing
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Lawyers at Lerners described stopping work to log time, losing track of time spent after interruptions by email, and mixed manual methods (pink slips, Word, dictation). Legora and Laurel say entries are often reconstructed from memory at the end of a day or week and short tasks are missed.
  solution: 'Laurel (in use at Lerners, Obermayer, Tonkon Torp and Berger Singerman; selected or being rolled out at Allens and Wilson Sonsini) records activity in email, documents, calls, meetings and applications in the background, assigns it to a client and matter, and drafts time entries with narratives that the lawyer reviews and releases. At Lerners and Berger Singerman it is integrated with the firm''s billing system (Elite 3E and Aderant respectively). Intapp Time offers a comparable mix of automated capture, timer and direct entry. The pattern is ''other'': passive activity capture, classification and drafting, with a person reviewing the draft.'
  outcomes:
  - lever: capacity
    description: Lerners reports additional billable time captured per lawyer per day after adopting Laurel (baseline and method not stated on the page).
    figure: +0.48 billable hours captured per lawyer daily
    measures: '''billable hours captured per lawyer daily'' (Laurel''s key-facts wording; no baseline, period or sample stated)'
    provenance: vendor-published
    source_ref: LAUREL-LERNERS-2026
  - lever: speed
    description: Lerners' Firm Chair says docket review now takes about five minutes including clean-ups, against half an hour to 45 minutes before. This is a personal recollection, not a tracked metric.
    figure: about 5 minutes versus 30 to 45 minutes
    measures: time the Firm Chair says she spends on daily dockets (her own estimate)
    provenance: self-reported
    source_ref: LAUREL-LERNERS-2026
  - lever: quality
    description: Laurel's key facts say Lerners has had zero billing disputes because of AI-first time records clients can trust. No count of disputes before adoption is given.
    figure: zero billing disputes
    measures: '''billing disputes due to AI-first time records'' (Laurel''s key-facts wording; no baseline)'
    provenance: vendor-published
    source_ref: LAUREL-LERNERS-2026
  - lever: capacity
    description: 'Tonkon Torp: Laurel is said to capture extra time per timekeeper per day. The key-facts box says 21 minutes and the body text says 20 minutes.'
    figure: 21 minutes per day (key facts); about $20,000 more annual revenue per timekeeper; 18% more entries per day
    measures: '''average lift in daily billable hours per Laurel timekeeper'' (21 minutes); ''boost in annual revenue per Laurel timekeeper''; ''more entries per day'' (Laurel wording; firm''s Managing Partner refers to the firm''s own analytical work but the analysis is not shown)'
    provenance: vendor-published
    source_ref: LAUREL-TONKONTORP-2026
  - lever: speed
    description: 'Tonkon Torp: the page says the collection cycle is 20% faster (the key-facts box instead says 20% faster release velocity) and write-downs and discounts are reduced; no write-down figures are given.'
    figure: 20% faster collection cycle (body text) / 20% increase in release velocity (key facts)
    measures: '''collection cycle'' or ''release velocity'' (the page uses both; definition and baseline not stated)'
    provenance: vendor-published
    source_ref: LAUREL-TONKONTORP-2026
  - lever: capacity
    description: 'Berger Singerman: attorneys recovered an average of nearly 15 minutes of billable time per day, and entries that could stay outstanding for days were completed about two days faster.'
    figure: nearly 15 minutes of billable time per attorney per day; about 2 days faster entry completion
    measures: '''average of nearly 15 minutes of billable time each day'' per attorney; time entries ''approximately two days faster'' (Laurel press-release wording; method not stated)'
    provenance: vendor-published
    source_ref: LAUREL-BERGER-2026
  - lever: speed
    description: 'An unnamed Am Law 200 firm compared Laurel head to head with Intapp Time: 70% of users released more time, time entries released rose 24%, and release was more than 40% faster. The firm is not named.'
    figure: 70% of users released more time; 24% more entries; more than 40% faster release
    measures: '''users reported they were able to capture and release more time''; ''timesheet granularity rose by an average of 24%''; ''release velocity ... more than 40% faster than with Intapp Time'' (Laurel wording; firm unnamed, sample size not stated)'
    provenance: vendor-published
    source_ref: LAUREL-AMLAW200-2026
  prerequisites:
  - Integration with the firm time and billing system (Elite 3E at Lerners; Aderant at Berger Singerman) and with Microsoft tools [LAUREL-LERNERS-2026, section 3; LAUREL-BERGER-2026]
  - Switching off or removing the legacy timekeeping route so use becomes the default (Obermayer turned off the old system within weeks of a February firm-wide launch) [LAUREL-OBERMAYER-2026]
  - Training for every new lawyer on joining (Lerners trains partners, associates and students on day one) [LAUREL-LERNERS-2026]
  - Client-centric file and matter naming so activity can be linked to a matter (an Obermayer attorney changed his naming after seeing the activity log) [LAUREL-OBERMAYER-2026]
  - An internal committee including attorneys to select the tool and spread use (Obermayer) [LAUREL-OBERMAYER-2026]
  risks_and_guardrails:
  - Hourly billing must reflect the time actually spent, and AI-captured activity does not change that rule [CALBAR-GENAI-2026, p. 8; TXETHICS-OP705-2025]
  - Vendor states the platform runs with no public LLMs, single-tenant AI and customer-supplied keys; this is a vendor claim not independently tested [LAUREL-HOME-2026]
  - A rival vendor in a sponsored post argues that screen-monitoring approaches are imprecise and invasive and prefers integration-led capture; this is a competitor claim, not evidence [LAWSITES-BILLABLESAI-2025, factor 1]
  - Lerners' Firm Chair describes the tool as an assistant rather than a replacement and still reviews and finalises her dockets [LAUREL-LERNERS-2026, section 1 and section 5]
  human_checkpoints:
  - Each lawyer reviews, edits and releases the drafted entries [LEGORA-LAUREL-2026; LAUREL-LERNERS-2026]
  - Billing partners approve bills built from the entries
  role_evolution: Lawyers move from writing time from memory to reviewing a system record; at Obermayer the controller led the rollout and messaging [LAUREL-OBERMAYER-2026]. Lerners' Firm Chair described using the tool as the end-of-day step in an AI-first routine [LAUREL-LERNERS-2026].
  evidence_grade: B
  sources:
  - ref: LAUREL-LERNERS-2026
    title: How Lerners repaired client service issues, netting out to zero billing disputes (customer story)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/lerners
    date: 2026-08
    access: full
    locator: Key facts; section 1 (AI as assistant); Transformative results
  - ref: LAUREL-OBERMAYER-2026
    title: How Obermayer solved their timekeeping issue and reimagined how their attorneys work (customer story)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/obermayer
    date: 2026-08
    access: full
    locator: The process; getting change management right
  - ref: LAUREL-TONKONTORP-2026
    title: Tonkon Torp customer story
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/tonkon-torp
    date: 2026-08
    access: full
    locator: Key facts; Building trust with clients
  - ref: LAUREL-BERGER-2026
    title: 'Berger Singerman and Laurel: a practical approach to AI adoption'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/press/berger-singermanand-laurel-a-practical-approach-to-ai-adoption
    date: 2026-09
    access: full
    locator: Paragraphs 5 and 6
  - ref: LAUREL-AMLAW200-2026
    title: Am Law 200 top VC firm customer story (firm not named)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/am-law-200-top-vc-firm
    date: 2026-08
    access: full
    locator: Key facts; More time captured and more time released means higher revenue
  - ref: LAUREL-ALLENS-2026
    title: Laurel expands Asia-Pacific presence through firmwide partnership with Allens
    publisher: Laurel (press release)
    type: vendor
    url: https://www.laurel.ai/press/laurel-expands-asia-pacific-presence-through-firmwide-partnership-with-allens
    date: '2026-05-28'
    access: full
    locator: Paragraphs 1 and 2 (firmwide rollout; billing requirements)
  - ref: LAUREL-WSGR-2026
    title: Laurel brings AI-powered time intelligence to Wilson Sonsini Goodrich & Rosati
    publisher: Laurel (press release)
    type: vendor
    url: https://www.laurel.ai/press/laurel-brings-ai-powered-time-intelligence-to-wilson-sonsini-goodrich-rosati
    date: 2026-08
    access: full
    locator: Paragraphs 1 and 2
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora (press release)
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: Paragraph 2 (problem statement)
  - ref: LAUREL-TIMEKEEPING-2026
    title: 'Timekeeping: smarter timesheets (product page)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/timekeeping
    date: 2026-10
    access: full
    locator: 'Complete capture: email and calendar, document and web tracking, offline work detection'
  - ref: INTAPP-TIMEKEEPING-2026
    title: Compliant timekeeping (Intapp Time for law firms)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/legal/timekeeping/
    date: 2026-10
    access: full
    locator: 'Capture every minute: flexible timekeeping methods'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p. 8, Charging for Work Produced by Generative AI row
  - ref: TXETHICS-OP705-2025
    title: Opinion 705 (generative AI in the practice of law)
    publisher: Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics
    type: regulator
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Fees discussion
  - ref: LAUREL-HOME-2026
    title: AI Timekeeping & Work Intelligence Platform (home page)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai
    date: 2026-10
    access: full
    locator: Security block
  - ref: LAWSITES-BILLABLESAI-2025
    title: 'Billing in the age of AI: a practical guide for law firms (sponsored post by Billables AI)'
    publisher: LawSites (sponsored post)
    type: press
    url: https://www.lawnext.com/2025/10/billing-in-the-age-of-ai-a-practical-guide-for-law-firms.html
    date: '2025-10-07'
    access: full
    locator: Factor 1
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms (US, Canada, Australia). Graded B, not A: every figure sits on a vendor-authored page, with no stated baseline or method; the only controlled comparison in the Laurel set (a Big Four tax division, see 02) is unnamed. Laurel customer-story pages carry site metadata dated 2026-08, which may reflect a site update rather than the original story date; Allens and the Thomson Reuters partnership carry their own dates in the text. Allens (May 2026) and Wilson Sonsini (2026-08) are selections or firmwide rollouts announced by the vendor, with no outcome data. No override or edit rates for drafted entries are published by anyone, and no independent measure of accuracy was found.'
- id: professional-services-billing-collections-02
  title: Accounting and advisory firms replace next-morning timesheet reconstruction with AI-drafted entries and use the time record for utilization
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - transaction-processing
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Warren Averett required professionals to submit daily time by 9:00 a.m., so each day began with reconstructing the previous day from memory; GHJ's previous system made batch entry a chore for client-service staff and left firm-services staff untracked.
  solution: 'Laurel records work activity and proposes timesheet entries that the professional reviews at the end of the day. Warren Averett (750+ professionals, Birmingham, Alabama) used it as its first AI-powered solution outside Copilot; GHJ (250+ professionals, Los Angeles) piloted with client-services teams then extended firmwide and turned off its legacy system. A Big Four firm''s tax division (unnamed) rolled it out to 1,000 timekeepers. The pattern is ''other'': passive capture, classification and drafting, with the professional reviewing.'
  outcomes:
  - lever: capacity
    description: GHJ reports additional billable time recovered per timekeeper per day, an annual fee figure per timekeeper, and a very small change in days to time submission.
    figure: 0.42 billable hours recovered per timekeeper per day; $16,128 billable fees recovered per timekeeper annually; 0.02 fewer days to time submission
    measures: '''billable hours recovered per timekeeper per day''; ''billable fees recovered per timekeeper annually''; ''fewer days to time submission'' (Laurel key-facts wording; baseline and period not stated)'
    provenance: vendor-published
    source_ref: LAUREL-GHJ-2026
  - lever: capacity
    description: A Big Four tax division (firm not named) reports higher chargeable hours for its first 1,000 adopters than a random control group balanced by sub-service line and rank; Laurel says the firm independently audited and verified the method. Because the firm is unnamed, this figure is not used to raise the grade.
    figure: +2.3 chargeable hours per timekeeper per week; $17,092,134 total annual profit growth across 1,000 timekeepers
    measures: '''chargeable hours per timekeeper per week attributable to Laurel'' compared with a random control group (adopter cohort of 1,000); profit growth is Laurel''s projection from that uplift'
    provenance: vendor-published
    source_ref: LAUREL-BIGFOURTAX-2026
  - lever: experience
    description: Warren Averett's CIO and AI Strategy Manager say professionals now fill in their time in a few minutes at the end of the day; a pilot survey response said the respondent would quit if the tool were withdrawn (with a joking disclaimer). No usage or revenue figures are published.
    figure: none published
    measures: n/a (qualitative statements by Warren Averett staff in a Laurel case study)
    provenance: self-reported
    source_ref: LAUREL-WARRENAVERETT-2026
  prerequisites:
  - A rollout plan that treats early adopters, the majority and holdouts differently, with training framed around removing unwanted work (Warren Averett) [LAUREL-WARRENAVERETT-2026]
  - Turning off the legacy timekeeping system once the pilot is done (GHJ reported no pushback) [LAUREL-GHJ-2026]
  risks_and_guardrails:
  - The most rigorous published design (control group, firm-audited method) is unnamed and vendor-reported, so the size of the uplift cannot be checked [LAUREL-BIGFOURTAX-2026, methodology note]
  - Extra captured time raises more hours to bill; whether clients accept and pay them is a separate question the sources do not measure [LAUREL-GHJ-2026]
  human_checkpoints:
  - Professionals review and finalise their entries at day end [LAUREL-WARRENAVERETT-2026]
  role_evolution: Warren Averett has an AI Strategy Manager who described the rollout approach and the framing of its training sessions [LAUREL-WARRENAVERETT-2026]; GHJ's Chief of Staff used the data on her own non-client work [LAUREL-GHJ-2026].
  evidence_grade: B
  sources:
  - ref: LAUREL-WARRENAVERETT-2026
    title: How Warren Averett turned time entry into a competitive advantage (customer story)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/warren-averett
    date: 2026-08
    access: full
    locator: Hidden cost of manual time tracking; Getting it right from day one; The skeptics became the loudest advocates
  - ref: LAUREL-GHJ-2026
    title: How Laurel unlocked firmwide time intelligence for GHJ leadership (customer story)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/ghj
    date: 2026-08
    access: full
    locator: Key facts; The solution
  - ref: LAUREL-BIGFOURTAX-2026
    title: Laurel drives annual profit for a Big Four firm (customer story, firm not named)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/laurel-drives-annual-profit-for-big-four-firm
    date: 2026-09
    access: full
    locator: Key facts; A Note on Laurel's ROI Methodology
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: accounting and advisory firms (US). The Big Four division is unnamed; Laurel''s home page says ''Trusted by EY'' but the story does not say the division is EY, so do not assume it. GHJ''s ''0.02 fewer days'' is as published and is tiny. Consulting firms: Laurel''s consulting page claims scope creep ''surfaces immediately'' but no consulting customer story was found; Laurel and Dayshape (2026-06-02) cite 28 additional minutes per day for Laurel users and profit increases of 11% as vendor averages with no method.'
- id: professional-services-billing-collections-03
  title: Point-of-entry help with narratives and work codes so time entries are compliant before they reach the pre-bill
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - document-production
  - review-assurance
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Intapp says revenue leaks between work and time capture when entries are delayed, coded inconsistently or returned in billing review because narratives are incomplete.
  solution: Intapp's May 2026 Time release adds AI work-code prediction (phase, task and activity codes proposed from the narrative and matter coding history), configurable narrative tone and style enforcement and one-click narrative compliance; the product page also describes converting voice or text notes into structured entries. Aderant's Time Agent (early access, announced 2026-08-25) improves narratives, flags billing risk and recommends codes. Laurel's compliance feature generates narratives that already account for active client rules and gives inline feedback as the timekeeper types.
  outcomes:
  - lever: speed
    description: Intapp's product page states a headline for time entry release speed; no basis is given.
    figure: 75% faster time entry release
    measures: Intapp's heading '75% faster time entry release' (no numerator, denominator, sample or period stated)
    provenance: vendor-published
    source_ref: INTAPP-TIME-2026
  - lever: cost
    description: Intapp's compliant time and billing page lists revenue-cycle, time-entry and write-off improvements for Intapp Time plus Billstream; no basis is given.
    figure: 40% faster revenue cycles; 20% less time spent entering time; 10% reduction in write-offs
    measures: Intapp's 'high-ROI solution' labels (no sample, period or baseline stated)
    provenance: vendor-published
    source_ref: INTAPP-TIMEBILL-2026
  prerequisites:
  - Client billing rules held in a machine-readable form so the tool can check narratives (see 04)
  - Matter coding history to learn from (Intapp work-code prediction uses it, weighted by recency) [INTAPP-TIMERELEASE-2026]
  risks_and_guardrails:
  - Aderant describes users as the final decision makers in all agent workflows [ADERANT-AGENTSEAP-2026]
  - Narrative text still has to reflect the time actually spent on the matter [CALBAR-GENAI-2026, p. 8]
  human_checkpoints:
  - The timekeeper accepts or edits suggested codes and narratives before release [INTAPP-TIMERELEASE-2026]
  role_evolution: Timekeepers review suggestions instead of looking up codes; billing teams see fewer returned entries (stated aim, not measured) [INTAPP-TIMERELEASE-2026; ADERANT-AGENTSEAP-2026].
  evidence_grade: C
  sources:
  - ref: INTAPP-TIMERELEASE-2026
    title: New Intapp Time release brings AI deeper into the time entry workflow to capture more billable hours and protect earned revenue
    publisher: Intapp (press release via Nasdaq/Business Wire)
    type: vendor
    url: https://www.nasdaq.com/press-release/new-intapp-time-release-brings-ai-deeper-time-entry-workflow-capture-more-billable
    date: '2026-05-21'
    access: full
    locator: Paragraphs 3 to 6 (release features)
  - ref: INTAPP-TIME-2026
    title: 'Intapp Time: AI time tracking software'
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/time-tracking/
    date: 2026-10
    access: full
    locator: Protect earned revenue section; 75% heading
  - ref: INTAPP-TIMEBILL-2026
    title: AI-powered timekeeping and prebilling for maximum revenue (Intapp compliant time and billing)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/legal/ai-powered-timekeeping-compliant-billing/
    date: 2026-10
    access: full
    locator: A high-ROI solution
  - ref: INTAPP-TIMEKEEPING-2026
    title: Compliant timekeeping (Intapp Time for law firms)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/legal/timekeeping/
    date: 2026-10
    access: full
    locator: 'Capture every minute: AI-powered data capture, compliant language'
  - ref: ADERANT-AGENTSEAP-2026
    title: Aderant launches early access to AI agents built to enhance law firm operations
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-launches-early-access-to-ai-agents
    date: '2026-08-25'
    access: full
    locator: Time Agent bullet
  - ref: LAUREL-COMPLIANCE-2026
    title: 'Compliance: every billing guideline, applied automatically (product page)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/compliance
    date: 2026-10
    access: full
    locator: Generate compliant narratives; flag issues in real time
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p. 8, Charging for Work Produced by Generative AI row
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms. Graded C: vendor releases and headline claims; no named firm is reported as using the new AI features. Intapp''s release says it is ''available now'' but names no adopter; the Intapp Time page carries a testimonial from Johnson Winter & Slattery and the legal timekeeping page one from Gilbert + Tobin, both about Intapp Time in general, undated. Elite added generative narrative drafting to 3E in 2023 (seen in search results only; not opened).'
- id: professional-services-billing-collections-04
  title: Client billing guidelines are read by AI and turned into rules that can be checked at time entry and billing
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - research-synthesis
  - review-assurance
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Outside counsel guidelines (OCGs) arrive as documents that vary by client. Verify's product lead at Zero Systems says it is humanly impossible for attorneys to retain hundreds of clients' rules, and Elite describes OCG review as time-consuming and error-prone.
  solution: Intapp Terms uses Celeste to capture, match and categorise obligations when a guideline document arrives (including by sharing it from Outlook), lets reviewers ask questions answered with links to the source, and enforces the terms in Intapp Time and Billstream. Laurel extracts prohibited activities, restricted words, narrative requirements and entry-format limits, stores them at firm, parent-client, client or matter level, and an administrator reviews them before rules go live. Elite Validate reads OCGs into billing rules and learns further rules from past rejections and reductions.
  outcomes:
  - lever: speed
    description: Two Intapp Terms customers say review of terms is faster; no measurement is given.
    figure: none published
    measures: 'n/a (qualitative customer quotes: Fredrikson & Byron Risk Counsel; Dickinson Wright Risk Management Manager)'
    provenance: vendor-published
    source_ref: INTAPP-TERMS-2026
  prerequisites:
  - A central repository of client guideline documents and a named owner (the Intapp quotes are from risk management and risk counsel roles) [INTAPP-TERMS-2026]
  - Administrator review of extracted rules before they are enforced [LAUREL-COMPLIANCE-2026]
  risks_and_guardrails:
  - Rule extraction is reviewed by an administrator before it goes live [LAUREL-COMPLIANCE-2026]
  - Enforcement level is set per rule (block, acknowledge, warn or awareness) so a wrong rule need not block billing [LAUREL-COMPLIANCE-2026]
  - Elite Validate applies rules only after the firm has accepted the rules it created [ELITE-VALIDATE-2025]
  human_checkpoints:
  - Risk or billing administrators approve extracted terms and rules
  - Timekeepers and billers respond to warnings
  role_evolution: Risk and billing administrators move from reading and summarising guideline documents to approving machine-extracted rules [INTAPP-TERMS-2026; LAUREL-COMPLIANCE-2026].
  evidence_grade: B
  sources:
  - ref: INTAPP-TERMS-2026
    title: 'Intapp Terms: enforce client obligations everywhere'
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/terms/
    date: 2026-10
    access: full
    locator: Agentic obligation capture section; Dickinson Wright and Fredrikson & Byron quotes
  - ref: LAUREL-COMPLIANCE-2026
    title: 'Compliance: every billing guideline, applied automatically (product page)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/compliance
    date: 2026-10
    access: full
    locator: Rule extraction and application; Entry-level enforcement
  - ref: ELITE-VALIDATE-2025
    title: 'Elite launches Elite Validate: legal invoice compliance solution'
    publisher: Elite (press release)
    type: vendor
    url: https://www.elite.com/insights/news/press-releases/elite-launches-elite-validate
    date: '2025-02-11'
    access: full
    locator: Paragraphs 3 to 5 (key benefits)
  - ref: LEGALIT-FOLEY-2024
    title: Foley Mansfield goes live with Verify from Zero Systems for gen AI pre-bill review
    publisher: Legal IT Insider
    type: press
    url: https://legaltechnology.com/foley-mansfield-goes-live-with-verify-from-zero-systems-for-gen-ai-pre-bill-review/
    date: '2024-05-15'
    access: full
    locator: Hambarchyan quote on OCG volume
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms (US). Graded B: Intapp Terms names two firm users with qualitative quotes; no accuracy or time data. Page dates not shown; read 2026-10-19. Elite Validate was announced 2025-02-11 with no customers named in the release. The Intapp Terms page also says obligations are surfaced in Intake and Conflicts, which belongs to acceptance-risk.'
- id: professional-services-billing-collections-05
  title: AI checks pre-bills against client guidelines and billing history and proposes one-click fixes before invoices go out
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - review-assurance
  - transaction-processing
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Foley Mansfield's managing partner said partners spent an enormous amount of time reviewing pre-bills each month. The Legal IT Insider article says large firms lose millions of dollars a year to guideline non-compliance, and Verify's product lead says some partners spend up to a week a month cleaning up invoices.
  solution: Foley Mansfield went live firmwide with Verify (from Zero Systems), which reads outside counsel guidelines and historical billing data held in Elite and Aderant, flags pre-bill entries that break rules such as block billing, vague narratives or excessive time, and suggests fixes that can be accepted or rejected with one click. Aderant signed a deal on 2025-08-07 to acquire HerculesAI's legal technology assets, described in its release as AI-driven billing compliance, for its work-to-cash products (coverage seen in search results but not opened names Verify among those assets; the release names HerculesAI's founder and CEO as Alex Babin, who is also named as Zero Systems' CEO in the Foley article). Elite Validate (announced 2025-02-11) and Laurel Billing's compliance agent (announced as coming soon, 2026-09-17) take the same approach.
  outcomes:
  - lever: speed
    description: Foley's managing partner says reviewing the items the AI highlights replaced days of pre-bill review. This is a stage remark, not a tracked metric.
    figure: days to minutes (quote)
    measures: the managing partner's description of pre-bill review time before and after Verify (no figures)
    provenance: self-reported
    source_ref: LEGALIT-FOLEY-2024
  - lever: cost
    description: Zero Systems' CEO says Verify recovers about 6% of revenue that would otherwise be written off and cuts pre-bill review time by about 50%.
    figure: about 6% of revenue otherwise written off; about 50% less pre-bill review time
    measures: '''around 6% of revenue that would be written off recovered'' and ''reduces pre-bill review time by around 50%'' (vendor CEO''s statements to the publication; basis, sample and period not given)'
    provenance: vendor-published
    source_ref: LEGALIT-FOLEY-2024
  prerequisites:
  - Guideline documents and historical billing data available in the billing system (Elite or Aderant at Foley) [LEGALIT-FOLEY-2024]
  - Rules for the firm to accept before enforcement (Elite Validate) [ELITE-VALIDATE-2025]
  risks_and_guardrails:
  - Verify runs its models locally and, per the vendor, data does not leave the firm security perimeter [LEGALIT-FOLEY-2024]
  - Suggestions are accepted or rejected by a person; Laurel says nothing goes out without sign-off [LEGALIT-FOLEY-2024; LAUREL-BILLINGPAGE-2026]
  - Laurel Billing is not yet available; its page says coming soon with a waitlist [LAUREL-BILLINGPAGE-2026]
  human_checkpoints:
  - Billing partner or biller accepts or dismisses each flagged item before the invoice is released
  role_evolution: Partners review a short list of flagged items instead of whole pre-bills (Foley); Laurel describes billers preparing and billing partners approving in one workspace [LEGALIT-FOLEY-2024; LAUREL-BILLINGPAGE-2026].
  evidence_grade: B
  sources:
  - ref: LEGALIT-FOLEY-2024
    title: Foley Mansfield goes live with Verify from Zero Systems for gen AI pre-bill review
    publisher: Legal IT Insider
    type: press
    url: https://legaltechnology.com/foley-mansfield-goes-live-with-verify-from-zero-systems-for-gen-ai-pre-bill-review/
    date: '2024-05-15'
    access: full
    locator: Paragraphs 2 to 6
  - ref: ADERANT-HERCULES-2025
    title: Aderant signs deal to acquire HerculesAI legal technology assets
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-signs-deal-to-acquire-herculesai-legal-technology
    date: '2025-08-07'
    access: full
    locator: Paragraphs 1 to 3
  - ref: ELITE-VALIDATE-2025
    title: 'Elite launches Elite Validate: legal invoice compliance solution'
    publisher: Elite (press release)
    type: vendor
    url: https://www.elite.com/insights/news/press-releases/elite-launches-elite-validate
    date: '2025-02-11'
    access: full
    locator: Paragraphs 2 to 5
  - ref: LAUREL-BILLINGPAGE-2026
    title: 'Billing: the billing workspace, coming soon (product page and FAQ)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/billing
    date: 2026-10
    access: full
    locator: Compliance agent; Review-ready fixes; FAQ
  - ref: LAUREL-BILLINGBLOG-2026
    title: 'Laurel Billing: defend every bill before it goes out'
    publisher: Laurel (blog)
    type: vendor
    url: https://www.laurel.ai/blog/coming-soon-laurel-billing
    date: '2026-09-17'
    access: full
    locator: Opening section
  - ref: INTAPP-TIMEBILL-2026
    title: AI-powered timekeeping and prebilling for maximum revenue (Intapp compliant time and billing)
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/legal/ai-powered-timekeeping-compliant-billing/
    date: 2026-10
    access: full
    locator: AI helps enforce client guidelines
  - ref: INTAPP-BILLSTREAM-2026
    title: Intapp Billstream
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/billing/
    date: 2026-10
    access: full
    locator: Built-in client and firm compliance; prebill workflow
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms (US). Graded B on a single named firmwide go-live. The Foley article is from 2024-05-15, older than the 12 to 18 month window; kept because it is the only named firm pre-bill deployment found. Whether Foley still uses Verify after the 2025 Aderant deal is unknown, and the link between Verify and the HerculesAI assets rests on search-result coverage not opened. The CEO''s 6% and 50% are vendor claims reported by the trade press. The vendor representative''s line that firms receive only about 85% of an invoice is also a vendor estimate (not used as an outcome).'
- id: professional-services-billing-collections-06
  title: AI ranks proforma edits so reviewers spend time on high-impact bills
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - review-assurance
  - coordination-scheduling
  pattern: intake-triage
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Lawyers and billing teams review and adjust draft bills before invoices go out; Elite describes routine review decisions as repetitive.
  solution: Elite added 'Elite Intelligence' to the Proforma workflow in 3E (reported 2026-02-27). It prioritises edits, defers items flagged as low-value and highlights proformas it identifies as high-impact.
  outcomes:
  - lever: capacity
    description: Elite expects the feature to cut proforma review time; this is an expectation, not a measurement.
    figure: up to 4 hours per month per lawyer (expected)
    measures: '''expects the feature to cut pro forma review time by up to 4 hours per month per lawyer'' (CFOtech''s wording of Elite''s expectation; no measured basis)'
    provenance: vendor-published
    source_ref: CFOTECH-ELITE-2026
  prerequisites:
  - 3E cloud platform with the new release (the update is described as cloud-only functions) [CFOTECH-ELITE-2026]
  risks_and_guardrails:
  - Deferring items judged low-value is the tool's judgement; the source does not describe how reviewers can audit deferred items [CFOTECH-ELITE-2026]
  human_checkpoints:
  - Lawyers and billing teams still review and adjust draft bills; the feature supports routine review decisions [CFOTECH-ELITE-2026]
  role_evolution: Reviewers receive a prioritised queue rather than an undifferentiated list of proformas (described aim) [CFOTECH-ELITE-2026].
  evidence_grade: C
  sources:
  - ref: CFOTECH-ELITE-2026
    title: Elite adds AI tools to 3E to streamline work-to-cash
    publisher: CFOtech UK
    type: press
    url: https://cfotech.co.uk/story/elite-adds-ai-tools-to-3e-to-streamline-work-to-cash
    date: '2026-02-27'
    access: full
    locator: Billing workflow section
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms. Graded C: a single trade-press report of a vendor release; no customer named. Elite cites Law.com research that firms can lose up to 25% of potential revenue to work-to-cash inefficiency (Elite''s citation, not opened at source).'
- id: professional-services-billing-collections-07
  title: Fixed-fee matters get scope-creep flags while the bill is being assembled, so a change order can be raised before the matter closes
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  - review-assurance
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: On fixed-fee engagements, overruns are often absorbed quietly at close (Laurel's description).
  solution: Laurel Billing's Scope agent will track budget burn and flag work drifting outside the engagement as the bill comes together, totalled in dollars. Every flag will arrive with a proposed fix, and nothing goes out without sign-off. Laurel says each approved correction feeds back into its timekeeping models.
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a (product not yet available)
    provenance: vendor-published
    source_ref: LAUREL-BILLINGPAGE-2026
  prerequisites:
  - Fixed-fee budgets and scope definitions recorded against the matter
  - Work records tied to the engagement (Laurel timekeeping)
  risks_and_guardrails:
  - The agent is unreleased; claims such as a shorter bill review each month are statements of intent [LAUREL-BILLINGPAGE-2026, learning loop]
  human_checkpoints:
  - Billing partner approves or dismisses each flag and decides on a change order [LAUREL-BILLINGPAGE-2026]
  role_evolution: Billing partners are described as approving decisions rather than reading entries [LAUREL-BILLINGPAGE-2026].
  evidence_grade: C
  sources:
  - ref: LAUREL-BILLINGPAGE-2026
    title: 'Billing: the billing workspace, coming soon (product page and FAQ)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/billing
    date: 2026-10
    access: full
    locator: 'Scope agent; FAQ: How does it catch scope creep'
  - ref: LAUREL-BILLINGBLOG-2026
    title: 'Laurel Billing: defend every bill before it goes out'
    publisher: Laurel (blog)
    type: vendor
    url: https://www.laurel.ai/blog/coming-soon-laurel-billing
    date: '2026-09-17'
    access: full
    locator: Opening section (announcement 2026-09-17)
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms; Laurel''s consulting page makes a similar claim for engagement profitability. Graded C: product page and blog only; Laurel Billing is described as coming soon with a waitlist. Pricing of fixed fees from cost data belongs to scoping-pricing.'
- id: professional-services-billing-collections-08
  title: AI drafts appeals for rejected e-billing invoices and ranks which are worth pursuing
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - document-production
  - transaction-processing
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: A defense-litigation firm's COO and founder describe teams of billers trained on dozens of client platforms and appeals departments 'chasing payments on appeals', most of which they call unfair and unsuccessful.
  solution: Aderant's Appeals Agent identifies and prioritises high-value appeal opportunities after e-billing rejections and drafts supporting rationale for the billing team to review. It entered an early access programme for law firms (announced 2026-05-12; programme opened 2026-08-25).
  outcomes:
  - lever: cost
    description: none published
    figure: none published
    measures: n/a (early access)
    provenance: vendor-published
    source_ref: ADERANT-AGENTSEAP-2026
  prerequisites:
  - Aderant product data (the agents draw on licensed Aderant product data) [ADERANT-AGENTSEAP-2026]
  risks_and_guardrails:
  - Aderant says users remain final decision makers in all agent workflows [ADERANT-AGENTSEAP-2026]
  human_checkpoints:
  - Billing team reviews each drafted appeal before submission
  role_evolution: Billing teams draft fewer appeals from scratch and decide which to send [ADERANT-AGENTSEAP-2026].
  evidence_grade: C
  sources:
  - ref: ADERANT-AGENTSEAP-2026
    title: Aderant launches early access to AI agents built to enhance law firm operations
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-launches-early-access-to-ai-agents
    date: '2026-08-25'
    access: full
    locator: Appeals Agent bullet
  - ref: ADERANT-AGENTCENTER-2026
    title: 'Aderant introduces agentic law firm operations: AI Agent Center'
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-introduces-agentic-law-firm-operations-ai-agent-center
    date: '2026-05-12'
    access: full
    locator: 'Initial capabilities: Appeals Agent'
  - ref: TRI-KOPKA-2026
    title: How one law firm is challenging a broken status quo around billing
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing
    date: '2026-04-30'
    access: full
    locator: 'Section: The administrative-industrial complex'
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms (US). Graded C: vendor announcements; no firm named in the early access programme. Elite said in 2023 that eBillingHub could categorise rejected invoices using Azure OpenAI (search results only, not opened).'
- id: professional-services-billing-collections-09
  title: AI prioritises collections follow-up by payment risk and recommends next actions
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Aderant describes collections as work that needs prioritising by payment risk and aging trends; Certinia presents faster payment after delivery as a benefit of its agents.
  solution: Aderant's Collections Agent prioritises accounts, surfaces aging trends and payment risk, and recommends next-best actions and outreach (announced 2026-05-12, early access 2026-08-25). Certinia positions its Veda agents across estimate, staffing, invoice and renewal on a services-firm data foundation and shows headline claims about speed from delivery to payment.
  outcomes:
  - lever: speed
    description: Certinia's AI page shows days saved between delivery and payment as a headline stat; the basis is not stated.
    figure: 24 days faster from delivery to payment
    measures: Certinia page label 'days faster from delivery to payment' (no sample, baseline or period stated)
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  - lever: speed
    description: Certinia's AI page shows a time-to-invoice headline; the basis is not stated.
    figure: 75% faster time to invoice
    measures: Certinia page label 'faster time to invoice' (no sample, baseline or period stated)
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Receivables and billing data held in the vendor platform (Aderant product data; Certinia financials)
  risks_and_guardrails:
  - Aderant says the agents recommend and draft while users decide [ADERANT-AGENTSEAP-2026]
  human_checkpoints:
  - Collections staff decide which accounts to chase and send outreach
  role_evolution: Collections follow-up shifts from working an aging report to acting on a ranked, explained list (described aim) [ADERANT-AGENTSEAP-2026].
  evidence_grade: C
  sources:
  - ref: ADERANT-AGENTSEAP-2026
    title: Aderant launches early access to AI agents built to enhance law firm operations
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-launches-early-access-to-ai-agents
    date: '2026-08-25'
    access: full
    locator: Collections Agent bullet
  - ref: ADERANT-AGENTCENTER-2026
    title: 'Aderant introduces agentic law firm operations: AI Agent Center'
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-introduces-agentic-law-firm-operations-ai-agent-center
    date: '2026-05-12'
    access: full
    locator: 'Initial capabilities: Collections Agent'
  - ref: CERTINIA-VEDA-2026
    title: 'Veda: AI agents for professional services (Certinia AI page)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: 2026-10
    access: full
    locator: Headline stats tiles (24 days; 75%)
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms (Aderant) and project-based services firms (Certinia). Graded C: vendor claims and early-access announcements. No named firm reports using an AI collections tool. Collections for accounting firms: the only named example found (BGW with Anduin) dates from 2021 and is out of window.'
- id: professional-services-billing-collections-10
  title: Work done inside AI platforms is turned into draft time entries with a narrative, so AI-assisted work is still recorded
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - transaction-processing
  - document-production
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Laurel says AI work takes up a growing share of a lawyer's day and has been among the hardest to capture.
  solution: 'Several vendors link AI work to time entries: Aderant''s iTimekeep integration with Harvey (announced as live 2026-08-17) turns completed Harvey work into a draft entry with matter context, duration and an AI-generated narrative that the lawyer reviews in iTimekeep; Laurel and Legora (2026-10-13) will turn each Legora task into a draft entry, with automated time capture available first; Litify with Billables AI (2026-05-19) generates review-ready entries within Litify; Laurel and Thomson Reuters (2026-08-05) cover CoCounsel Legal activity.'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: n/a (announcements; no deployment results)
    provenance: vendor-published
    source_ref: ADERANT-ITIMEKEEPHARVEY-2026
  prerequisites:
  - Both products licensed (for example Harvey and iTimekeep) [ADERANT-ITIMEKEEPHARVEY-2026]
  - Existing firm approval process for time entries [ADERANT-ITIMEKEEPHARVEY-2026]
  risks_and_guardrails:
  - Hourly bills must reflect actual time, and efficiency from AI belongs to the client under the Texas opinion [CALBAR-GENAI-2026, p. 8; TXETHICS-OP705-2025]
  - Aderant says the integration preserves existing billing controls and approvals [ADERANT-ITIMEKEEPHARVEY-2026]
  human_checkpoints:
  - Lawyer reviews, edits and submits the draft; firm approval process applies [ADERANT-ITIMEKEEPHARVEY-2026]
  role_evolution: Lawyers confirm AI-generated drafts of their own AI-assisted work (described aim).
  evidence_grade: C
  sources:
  - ref: ADERANT-ITIMEKEEPHARVEY-2026
    title: Aderant launches iTimekeep integration with Harvey, turning AI-powered legal work into billable time
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-launches-itimekeep-integration-with-harvey
    date: '2026-08-17'
    access: full
    locator: Paragraphs 1 to 3
  - ref: ADERANT-HARVEY-2025
    title: Aderant and Harvey announce market-defining partnership
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-and-harvey-announce-market-defining-partnership
    date: '2025-12-15'
    access: full
    locator: Paragraphs 1 to 3 (partnership announcement)
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora (press release)
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: Paragraphs 2 to 5 and closing paragraph
  - ref: LAWSITES-LITIFY-2026
    title: Litify launches AI-powered time capture with Billables AI to recover lost time
    publisher: LawSites (Bob Ambrogi; vendor-supplied release)
    type: press
    url: https://www.lawnext.com/2026/05/litify-launches-ai-powered-time-capture-with-billables-ai-to-recover-lost-time.html
    date: '2026-05-21'
    access: full
    locator: Paragraphs 2 and 3
  - ref: LAUREL-TR-2026
    title: Laurel and Thomson Reuters partner to help law firms prove the business value of AI
    publisher: Laurel (press release)
    type: vendor
    url: https://www.laurel.ai/press/laurel-and-thomson-reuters
    date: '2026-08-05'
    access: full
    locator: Opening paragraphs
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p. 8, Charging for Work Produced by Generative AI row
  - ref: TXETHICS-OP705-2025
    title: Opinion 705 (generative AI in the practice of law)
    publisher: Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics
    type: regulator
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Fees discussion
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms. Graded C: four vendor announcements; none names a firm using the integration. The Lerners story shows one Laurel firm also using Harvey, but not the integration. The Litify release repeats a vendor claim that up to 30% of billable work goes unrecorded and ''up to 30% more billable time'' and ''up to 90%'' less narrative time; these are vendor ceilings. Measuring AI value from the same data is routed to firm-finance.'
- id: professional-services-billing-collections-11
  title: Recorded time is compared with time actually worked to show where revenue leaks, month by month and matter by matter
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Elite says many firms run the work-to-cash cycle across several systems and rely on end-of-month reporting; Laurel says scope creep and leakage surface only after an engagement closes.
  solution: Laurel Signal compares recorded time with time actually worked to find lost revenue, and tracks project profitability while it runs. Intapp Time pairs work activity with financial data to show realization and leakage patterns. Elite's Data Connect sends near-real-time 3E data (work in progress, billing progression, receivables movements, realisation trends) to a firm's Microsoft Fabric environment.
  outcomes:
  - lever: speed
    description: Elite says early pilots of Data Connect cut reporting time and removed a four-step routine process for some teams (pilot users not named).
    figure: 50% less reporting time (early pilots)
    measures: '''early pilots cut reporting time by 50%'' (CFOtech''s report of Elite; pilot sample and baseline not stated)'
    provenance: vendor-published
    source_ref: CFOTECH-ELITE-2026
  prerequisites:
  - Time and billing data in a cloud platform (3E cloud; Intapp Cloud) and a data environment such as Microsoft Fabric for Elite [CFOTECH-ELITE-2026]
  risks_and_guardrails:
  - Visible time data on individuals and after-hours patterns raises monitoring questions that the sources do not address [LAUREL-SIGNAL-2026]
  human_checkpoints:
  - Finance and billing leaders decide what to do about flagged leakage
  role_evolution: Finance teams get in-month rather than period-end views (described aim) [CFOTECH-ELITE-2026].
  evidence_grade: C
  sources:
  - ref: LAUREL-SIGNAL-2026
    title: 'Laurel Signal: firm insights (product page)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/signal
    date: 2026-10
    access: full
    locator: Profitability and pricing; Eliminate revenue leakage
  - ref: INTAPP-TIME-2026
    title: 'Intapp Time: AI time tracking software'
    publisher: Intapp
    type: vendor
    url: https://www.intapp.com/time-tracking/
    date: 2026-10
    access: full
    locator: Sharpen profitability decisions section
  - ref: CFOTECH-ELITE-2026
    title: Elite adds AI tools to 3E to streamline work-to-cash
    publisher: CFOtech UK
    type: press
    url: https://cfotech.co.uk/story/elite-adds-ai-tools-to-3e-to-streamline-work-to-cash
    date: '2026-02-27'
    access: full
    locator: Data layer section
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms, accounting and consulting firms (Laurel). Graded C: product pages and one trade-press report. AI-ROI reporting built from the same data is routed to firm-finance. Laurel''s firm-leadership page claims professional services firms write down 10 to 20% of billed time on average and fail to record an additional 3 hours of work on average; no source is given, so treat it as a vendor assertion.'
- id: professional-services-billing-collections-12
  title: Time capture is extended to executives and administrative staff who never tracked time, to show cost to serve
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: At GHJ, firm-services teams and executives had no time system at all, so leadership could not see how resources were allocated or whether workloads were sustainable.
  solution: 'After a firmwide rollout to client-services teams, GHJ is rolling out Laurel to firm-services teams and administrative staff who have never tracked time, intending to use the data for resource allocation and hiring evidence. The pattern is ''other'': passive capture of time for non-billable roles.'
  outcomes:
  - lever: experience
    description: GHJ's Chief of Staff says the data lets her see how her time is spent; no firm-level results are published for the extension.
    figure: none published
    measures: n/a (qualitative statement by GHJ Chief of Staff)
    provenance: self-reported
    source_ref: LAUREL-GHJ-2026
  prerequisites:
  - Legacy system switched off so everyone uses the new route [LAUREL-GHJ-2026]
  risks_and_guardrails:
  - Time data on non-billable staff is a new form of monitoring; the story frames it as understanding rather than evaluation [LAUREL-GHJ-2026]
  human_checkpoints:
  - Staff review their own entries
  role_evolution: Administrative and executive roles gain a time record; managers can see when they spend time on work that should be delegated (stated intent) [LAUREL-GHJ-2026].
  evidence_grade: B
  sources:
  - ref: LAUREL-GHJ-2026
    title: How Laurel unlocked firmwide time intelligence for GHJ leadership (customer story)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/ghj
    date: 2026-08
    access: full
    locator: Extending beyond billable teams; Visibility for non-traditional roles
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: accounting and advisory (US). Graded B: one named firm, described as rolling out; no measurements for this extension. Single vendor-authored story.'
- id: professional-services-billing-collections-13
  title: In-house teams use AI to audit outside counsel invoices against guidelines and flag line items for the reviewing attorney
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - review-assurance
  - transaction-processing
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Albertsons works with about 180 outside law firms and its legal operations program manager describes cutting outside counsel spend as a big push; she says invoices with hundreds of line items make it easy to gloss over problems.
  solution: Albertsons Companies uses Thomson Reuters Legal Tracker's AI-powered audit, which flags invoice line items for the attorney's attention, plus automated volume discounts applied on invoice submission. Brightflag describes AI that reads every invoice, emails the reviewer a summary of the work and any guideline violations, and allows approval from the inbox; its Invoice Summaries and review features were announced in beta on 2024-04-30.
  outcomes:
  - lever: cost
    description: Albertsons' Program Manager, Legal Operations, says the AI audit and volume discount together have saved 'probably almost $2 million' in outside counsel spend year to date. This is a recollection and the savings are not attributed separately to the AI audit.
    figure: close to $2 million year to date (nearly $2 million)
    measures: outside counsel spend saved year to date through Legal Tracker, AI audit and volume discount combined (program manager's estimate; period not specified)
    provenance: self-reported
    source_ref: ALBERTSONS-TR-2026
  prerequisites:
  - Outside counsel guidelines and rate agreements loaded in the e-billing system
  - Invoices submitted through the platform [ALBERTSONS-TR-2026]
  risks_and_guardrails:
  - Albertsons says security concerns made it hard to get the company on board with AI [ALBERTSONS-TR-2026]
  - Brightflag cites role permissions, workflow rules and a full audit trail [BRIGHTFLAG-AI-2026]
  human_checkpoints:
  - Attorneys review flagged items; reviewers approve invoices (Brightflag sends a summary and approval link)
  role_evolution: Legal-operations staff focus on strategic firm negotiations while the tool applies discounts and flags items [ALBERTSONS-TR-2026].
  evidence_grade: B
  sources:
  - ref: ALBERTSONS-TR-2026
    title: Albertsons Companies strengthens legal operations with Thomson Reuters Legal Tracker (case study)
    publisher: Thomson Reuters
    type: vendor
    url: https://legal.thomsonreuters.com/en/insights/case-studies/albertsons-companies-strengthens-legal-operations-with-thomson-reuters-legal-tracker
    date: '2026-05-19'
    access: full
    locator: Key results; Legal Tracker's AI-powered audit transforms invoice management
  - ref: BRIGHTFLAG-AI-2026
    title: The AI advantage in-house legal teams have been waiting for (Brightflag AI)
    publisher: Brightflag
    type: vendor
    url: https://brightflag.com/brightflag-ai/
    date: 2026-10
    access: full
    locator: Legal AI that makes your life easier
  - ref: BRIGHTFLAG-NEXTGEN-2024
    title: Brightflag launches next-gen AI for e-billing and matter management
    publisher: Brightflag (press release)
    type: vendor
    url: https://brightflag.com/press/next-gen-ai/
    date: '2024-04-30'
    access: full
    locator: Invoice Summaries paragraphs
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: GSK remarks on savings questions
  last_reviewed: '2026-10-19'
  notes: 'in-house. Firm kind: corporate legal department (retail). Graded B: a vendor-published case study with a named customer and a recollected figure; savings are not split between AI audit and volume discounts. Case study metadata date 2026-05-19. LexisNexis CounselLink SmartReview, Wolters Kluwer LegalVIEW BillAnalyzer and Epiq managed invoice review also offer AI invoice review but were seen in search results only (see Gaps).'
- id: professional-services-billing-collections-14
  title: In-house teams ask a conversational assistant questions about outside counsel spend and matters
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  - research-synthesis
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Brightflag says most legal teams hold spend data they cannot easily access.
  solution: Ask Brightflag, previewed on 2024-04-30 and described on 2025-04 as used by hundreds of in-house teams, lets users ask questions of their e-billing and matter data in plain language and draft emails to vendors, answering from Brightflag's system of record.
  outcomes:
  - lever: speed
    description: Brightflag says teams gain insight 'in seconds'; no measurement is given.
    figure: none published
    measures: n/a (vendor statement; no customer named)
    provenance: vendor-published
    source_ref: BRIGHTFLAG-ROADMAP-2025
  prerequisites:
  - Invoice and matter data held in the platform
  risks_and_guardrails:
  - Answers are grounded in the system of record, per the vendor; accuracy is not independently reported [BRIGHTFLAG-AI-2026]
  human_checkpoints:
  - Legal operations staff interpret answers before acting
  role_evolution: Legal-ops analysts query data directly instead of requesting reports (stated aim).
  evidence_grade: C
  sources:
  - ref: BRIGHTFLAG-ROADMAP-2025
    title: Brightflag launches new AI-powered spend management, matter management, and insights features for corporate legal teams
    publisher: Brightflag (press release)
    type: vendor
    url: https://brightflag.com/press/innnovation-roadmap/
    date: 2025-04
    access: full
    locator: Smarter GenAI insights for legal spend and matters
  - ref: BRIGHTFLAG-NEXTGEN-2024
    title: Brightflag launches next-gen AI for e-billing and matter management
    publisher: Brightflag (press release)
    type: vendor
    url: https://brightflag.com/press/next-gen-ai/
    date: '2024-04-30'
    access: full
    locator: Ask Brightflag paragraphs
  - ref: BRIGHTFLAG-AI-2026
    title: The AI advantage in-house legal teams have been waiting for (Brightflag AI)
    publisher: Brightflag
    type: vendor
    url: https://brightflag.com/brightflag-ai/
    date: 2026-10
    access: full
    locator: The power of general purpose AI inside Brightflag
  last_reviewed: '2026-10-19'
  notes: 'in-house. Graded C: vendor statements; no named customer or measurement for this feature. Lower relevance to the time-to-cash chain; included because it shows how client-side teams analyse the invoices firms send.'
- id: professional-services-billing-collections-15
  title: Invoices show where AI was used on a task and what it saved (idea)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - document-production
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Clients are asking firms to prove AI savings on specific matters, and some clients issue guidelines refusing to pay for work done by AI.
  solution: 'Idea (labelled): at Legalweek 2026 a Ropes & Gray innovation director said clients are starting to ask for line-item transparency on invoices, such as whether AI was used on a task and how much time or money it saved. A Zarwin Baum managing director floated a return to a single line-item ''services rendered'' bill. No firm was reported to have built either. Pattern ''other'': AI-use flags on invoice lines.'
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: n/a (idea; no deployment found)
    provenance: self-reported
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - AI usage tied to matters and time entries (see 10)
  - Agreement with clients on what disclosure and savings sharing mean
  risks_and_guardrails:
  - California says generative AI costs specific to a matter need disclosure in the fee agreement and no markup without informed written consent [CALBAR-GENAI-2026, p. 8]
  - Texas allows per-use AI fees at actual cost but not hours saved [TXETHICS-OP705-2025]
  - Virginia LEO 1901 (petition) says value-based fees may reflect efficiency gains, which differs from the hourly rule [VSB-LEO1901-2025, overview]
  human_checkpoints:
  - Billing partner decides how to present AI use and savings to each client
  role_evolution: Pricing and billing leads (Greenberg Traurig has a Chief Pricing and Innovation Officer) would manage client AI-value conversations [TRI-LEGALWEEK-2026].
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: 'Sections: The contradictions in the room; Proving AI''s path to saving clients money'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p. 8
  - ref: TXETHICS-OP705-2025
    title: Opinion 705 (generative AI in the practice of law)
    publisher: Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics
    type: regulator
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Fees discussion
  - ref: VSB-LEO1901-2025
    title: 'Petition of the Virginia State Bar to the Supreme Court of Virginia: proposed Legal Ethics Opinion 1901 (reasonable fees and generative AI)'
    publisher: Virginia State Bar
    type: regulator
    url: https://vsb.org/common/Uploaded%20files/docs/20250724-leo1901-petition.pdf
    date: 2025-07
    access: full
    locator: Overview of the issues
  last_reviewed: '2026-10-19'
  notes: 'IDEA: discussed by practitioners at a conference, no public deployment found. Firm kind: law firms (US), client view from in-house (GSK, DLA Piper remarks). Insurance clients refusing to pay for software or AI costs are also reported by TRI-KOPKA-2026 (Kopka Law).'
- id: professional-services-billing-collections-16
  title: A rates agent shows which billing rate applies to a matter, why, and how it changed
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - coordination-scheduling
  - data-reporting
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Aderant describes rate campaigns and requests handled by spreadsheet and email.
  solution: Aderant's Rates Agent gives firms an explainable view of which billing rates apply, why they apply and how they have changed, with a governed workflow for requests, approvals and supporting evidence. Early access opened at ILTACON 2026 (reported 2026-08-25).
  outcomes:
  - lever: quality
    description: none published
    figure: none published
    measures: n/a (early access)
    provenance: vendor-published
    source_ref: ADERANT-AGENTSEAP-2026
  prerequisites:
  - Rate data held in Aderant products
  risks_and_guardrails:
  - Users remain the final decision makers [ADERANT-AGENTSEAP-2026]
  human_checkpoints:
  - Rate approvals stay with the firm approvers
  role_evolution: Rate-setting staff work from a governed workflow rather than spreadsheets (described aim).
  evidence_grade: C
  sources:
  - ref: ADERANT-AGENTSEAP-2026
    title: Aderant launches early access to AI agents built to enhance law firm operations
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-launches-early-access-to-ai-agents
    date: '2026-08-25'
    access: full
    locator: Rates Agent bullet
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: law firms. Graded C: single vendor announcement. Rate strategy and pricing decisions sit with scoping-pricing; this entry covers rate application and approval records at billing.'
- id: professional-services-billing-collections-17
  title: Consultants log time by conversation instead of filling in a timesheet
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - transaction-processing
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Certinia describes timekeeping as a chronically low-adoption workflow, leading to less compliance and more unbilled time.
  solution: Certinia's Veda positions 'conversational timekeeping' to remove friction from time entry on its professional services automation platform. The page does not describe the mechanics or a customer.
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: n/a (page statement only)
    provenance: vendor-published
    source_ref: CERTINIA-VEDA-2026
  prerequisites:
  - Certinia PSA platform
  risks_and_guardrails:
  - Mechanics, review step and data handling are not described on the page [CERTINIA-VEDA-2026]
  human_checkpoints:
  - Not described
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: CERTINIA-VEDA-2026
    title: 'Veda: AI agents for professional services (Certinia AI page)'
    publisher: Certinia
    type: vendor
    url: https://certinia.com/solutions/ai
    date: 2026-10
    access: full
    locator: Make time capture a non-issue
  last_reviewed: '2026-10-19'
  notes: 'Firm kind: project-based services (consulting, technology services). Graded C: one marketing statement; a search for a Veda timekeeping agent found nothing more.'
```

## 3. Module notes

**Processes and key steps (work type in brackets)**

- Time capture and entry [transaction-processing]: recall or log activity; assign client, matter, phase and task codes. Changed by use cases 01, 02, 10, 12, 17.
- Narrative writing and coding [document-production]: write a description that meets the client's format rules. Use case 03.
- Interpreting client billing guidelines (OCGs) [research-synthesis]: read each client's document, translate it into rules. Use case 04.
- Pre-bill or proforma assembly and partner review [review-assurance]: check, edit, write down, approve. Use cases 05, 06, 07.
- Invoice submission, e-billing rejections and appeals [transaction-processing]. Use case 08.
- Collections follow-up and rate application [coordination-scheduling]. Use cases 09, 16.
- Leakage and realization reporting [data-reporting]. Use case 11.
- In-house side: outside-counsel invoice review and spend analysis [review-assurance, data-reporting]. Use cases 13, 14.

**Common pain points**

- Time is reconstructed from memory, and short tasks are missed [LEGORA-LAUREL-2026, paragraph 2]. Warren Averett required daily time by 9:00 a.m. [LAUREL-WARRENAVERETT-2026]. Lerners lawyers used pink slips, Word files and dictation [LAUREL-LERNERS-2026].
- Partners spent days on pre-bills each month (Foley Mansfield's managing partner) [LEGALIT-FOLEY-2024].
- Billing departments carry billers trained on dozens of client platforms and appeals teams (Kopka Law, a defense-litigation firm) [TRI-KOPKA-2026].
- Efficiency is penalised under hourly billing; carriers refuse to pay for software or AI costs while expecting the savings [TRI-KOPKA-2026].
- Clients want proof of AI savings by matter; firms say they are still gathering data [TRI-LEGALWEEK-2026].

**Metrics and benchmarks (all vendor-published or self-reported; none independent)**

- Lerners +0.48 billable hours per lawyer per day [LAUREL-LERNERS-2026]; GHJ +0.42 per timekeeper per day [LAUREL-GHJ-2026]; Berger Singerman nearly 15 minutes per attorney per day [LAUREL-BERGER-2026]; Tonkon Torp 21 minutes [LAUREL-TONKONTORP-2026]. Laurel's home page gives "up to 30 minutes recovered daily" and a "4-11% profit increase" with no basis; the Thomson Reuters partnership release calls the same range a "revenue lift" [LAUREL-HOME-2026; LAUREL-TR-2026]. The mismatch between "profit" and "revenue" is unexplained.
- Big Four tax division (unnamed): +2.3 chargeable hours per timekeeper per week versus a random control group, firm-audited method per Laurel [LAUREL-BIGFOURTAX-2026].
- Intapp headline claims (40% faster revenue cycles, 20% less time entering time, 10% fewer write-offs, 75% faster time entry release) have no stated basis [INTAPP-TIMEBILL-2026; INTAPP-TIME-2026].
- Verify: about 6% of revenue otherwise written off recovered; about 50% less pre-bill review time (vendor CEO) [LEGALIT-FOLEY-2024].
- Market context: Am Law 100 worked rates grew almost 10% in Q1 2026 while the Law Firm Financial Index stayed flat at 55 [TRI-LFFI-Q1-2026]. Only 22% of firms have a GenAI strategy, and those that do are 3.9 times as likely to achieve ROI (a Thomson Reuters speaker at Legalweek) [TRI-LEGALWEEK-2026].
- Laurel's firm-leadership page says professional services firms write down 10 to 20% of billed time on average and miss 3 hours of unrecorded work; Elite cites Law.com research that firms can lose up to 25% of potential revenue across work-to-cash. Neither figure is sourced on the page [LAUREL-FIRMLEADERSHIP-2026; CFOTECH-ELITE-2026].
- Dayshape research cited by Laurel: 42% of firms missed revenue targets last year (vendor research, not opened at source) [LAUREL-DAYSHAPE-2026].

**Guardrails and regulatory points**

- California (guidance approved by the Board of Trustees 2026-05-14): hourly billing must reflect time actually spent; flat fees may build in AI savings; general AI subscriptions are overhead; matter-specific AI costs need fee-agreement disclosure, must reflect actual cost, and carry no markup without informed written consent [CALBAR-GENAI-2026, p. 8; CALBAR-ETHICS-2026].
- Texas Opinion 705 (February 2025): an hourly lawyer may not bill for hours saved by AI; per-use AI fees may pass through at actual cost [TXETHICS-OP705-2025].
- Virginia LEO 1901: approved by the State Bar Council 62-1 on 2025-06-12; hourly fees must reflect actual time but value-based billing remains appropriate for efficient AI-assisted work. The State Bar page heading says the Supreme Court of Virginia approved it; the petition is what was read [VSB-LEO1901-2025, overview].
- ABA Formal Opinion 512 was blocked (HTTP 403) and not read.
- Vendor controls: Laurel states no public LLMs, single-tenant AI, bring-your-own-key; Verify runs models locally inside the firm perimeter [LAUREL-HOME-2026; LEGALIT-FOLEY-2024]. These are vendor claims.

**Frontier signals (dated and sourced)**

- 2026-10-13: Legora and Laurel announce automatic time entries from work done in Legora, with a second phase to measure AI value; automated time capture is to be available first [LEGORA-LAUREL-2026].
- 2026-09-17: Laurel announces Laurel Billing (compliance and scope agents) as coming soon [LAUREL-BILLINGBLOG-2026].
- 2026-08-25: Aderant opens early access to Appeals, Collections, Talent and Time agents, with Compliance, GL Forecasting and Rates agents added at ILTACON [ADERANT-AGENTSEAP-2026]. 2026-08-17: Aderant's iTimekeep integration with Harvey announced as live [ADERANT-ITIMEKEEPHARVEY-2026].
- 2026-05-21: Intapp Time adds AI work-code prediction and narrative compliance, and says it will share agentic workflows for Intapp Time that summer [INTAPP-TIMERELEASE-2026]. 2026-05-19: Litify adds AI time capture with Billables AI [LAWSITES-LITIFY-2026]. 2026-02-27: Elite Intelligence in Proforma [CFOTECH-ELITE-2026].
- 2025-08-07: Aderant signs a deal to acquire HerculesAI's legal technology assets, described as AI-driven billing compliance [ADERANT-HERCULES-2025].
- 2026-09-04: Press at ILTACON discussed a possible move from seat-based to consumption-based AI pricing ("tokengeddon"), which would make AI cost variable per matter [EDISCOVERYTODAY-ILTACON-2026].

**Workforce and role effects**

- Billing partners are described as approving decisions, not line by line entries, in Laurel's planned billing workspace [LAUREL-BILLINGPAGE-2026]. Foley's partners review items the AI highlights [LEGALIT-FOLEY-2024].
- Warren Averett has an AI Strategy Manager who described the rollout approach [LAUREL-WARRENAVERETT-2026]; Obermayer's controller led the rollout and messaging [LAUREL-OBERMAYER-2026]; Greenberg Traurig has a Chief Pricing and Innovation Officer [TRI-LEGALWEEK-2026].
- Kopka Law's COO says talent is leaving the defense side because of tedious time capture (self-reported opinion) [TRI-KOPKA-2026].
- Laurel's Proof 2026 recap says the final session raised the question of the billable hour and the talent pipeline, with few firms having settled it [LAUREL-PROOF-2026].

**Objections and concerns practitioners raise**

- Hourly billing: if AI shortens tasks, itemised hourly bills understate value; one panelist proposed a single line-item bill [TRI-LEGALWEEK-2026].
- Clients are issuing guidelines that refuse payment for AI-performed work and, at the same time, expect AI to be used [TRI-LEGALWEEK-2026].
- Monitoring and accuracy of screen-based capture (competitor argument) [LAWSITES-BILLABLESAI-2025].
- Adoption takes effort: Lerners' Firm Chair calls Laurel an up-front investment with a getting-used-to period [LAUREL-LERNERS-2026].
- Evidence is vendor-authored; ILTACON press found vendors reluctant to discuss consumption pricing [EDISCOVERYTODAY-ILTACON-2026].

**Interview probes for an advisor**

1. Walk me through how a day of work becomes a line on a client invoice. At which steps does someone rewrite, recode or write down an entry, and who?
2. Which client billing guidelines cause the most rejections or reductions, how do billers hear about changes, and what happens to the rejected invoice?
3. When AI shortens a task, what happens to the bill? What do your engagement letters and your jurisdiction's ethics rules say about time saved and about AI costs?
4. If a system drafts your time entries, how would you know they are right? What do reviewers change, and does anyone track it?
5. Where do write-down decisions actually get made, by the billing team or the partner, and what data would change that decision?

## 4. Routed to other modules

- **firm-finance:** measuring AI value and ROI from time data (Laurel Signal "AI and technology ROI", Legora and Laurel phase two, Laurel and Thomson Reuters partnership) [LAUREL-SIGNAL-2026; LEGORA-LAUREL-2026; LAUREL-TR-2026]. Q1 2026 rate and profit context [TRI-LFFI-Q1-2026].
- **scoping-pricing:** Kopka Law's move to retainer and KPI-based billing [TRI-KOPKA-2026]; flat-fee and value-based pricing rules in California, Texas and Virginia [CALBAR-GENAI-2026; TXETHICS-OP705-2025; VSB-LEO1901-2025]; Laurel Signal's pricing of fixed fees from actual cost [LAUREL-SIGNAL-2026].
- **staffing-resourcing:** Laurel and Dayshape linking captured time to resource planning and utilization [LAUREL-DAYSHAPE-2026].
- **talent-learning:** Aderant's Talent Agent, which draws on time narratives for associate evaluation [ADERANT-AGENTSEAP-2026].
- **acceptance-risk:** Intapp Terms obligations surfaced in Intake and Conflicts [INTAPP-TERMS-2026].
- **delivery-management:** Harvey Legal Work Orchestration was not read for this module.

## 5. Sources

All 50 listed sources were opened and read (access: full). Counts by type: vendor 37, press 6, regulator 4, conference 2, survey 1.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ADERANT-AGENTCENTER-2026 | Aderant introduces agentic law firm operations: AI Agent Center | Aderant (press release) | vendor | https://www.aderant.com/news-pr/aderant-introduces-agentic-law-firm-operations-ai-agent-center | 2026-05-12 | full |
| ADERANT-AGENTSEAP-2026 | Aderant launches early access to AI agents built to enhance law firm operations | Aderant (press release) | vendor | https://www.aderant.com/news-pr/aderant-launches-early-access-to-ai-agents | 2026-08-25 | full |
| ADERANT-HARVEY-2025 | Aderant and Harvey announce market-defining partnership | Aderant (press release) | vendor | https://www.aderant.com/news-pr/aderant-and-harvey-announce-market-defining-partnership | 2025-12-15 | full |
| ADERANT-HERCULES-2025 | Aderant signs deal to acquire HerculesAI legal technology assets | Aderant (press release) | vendor | https://www.aderant.com/news-pr/aderant-signs-deal-to-acquire-herculesai-legal-technology | 2025-08-07 | full |
| ADERANT-ITIMEKEEPHARVEY-2026 | Aderant launches iTimekeep integration with Harvey, turning AI-powered legal work into billable time | Aderant (press release) | vendor | https://www.aderant.com/news-pr/aderant-launches-itimekeep-integration-with-harvey | 2026-08-17 | full |
| ALBERTSONS-TR-2026 | Albertsons Companies strengthens legal operations with Thomson Reuters Legal Tracker (case study) | Thomson Reuters | vendor | https://legal.thomsonreuters.com/en/insights/case-studies/albertsons-companies-strengthens-legal-operations-with-thomson-reuters-legal-tracker | 2026-05-19 | full |
| BRIGHTFLAG-AI-2026 | The AI advantage in-house legal teams have been waiting for (Brightflag AI) | Brightflag | vendor | https://brightflag.com/brightflag-ai/ | 2026-10 | full |
| BRIGHTFLAG-NEXTGEN-2024 | Brightflag launches next-gen AI for e-billing and matter management | Brightflag (press release) | vendor | https://brightflag.com/press/next-gen-ai/ | 2024-04-30 | full |
| BRIGHTFLAG-ROADMAP-2025 | Brightflag launches new AI-powered spend management, matter management, and insights features for corporate legal teams | Brightflag (press release) | vendor | https://brightflag.com/press/innnovation-roadmap/ | 2025-04 | full |
| CALBAR-ETHICS-2026 | Ethics and Technology Resources | State Bar of California | regulator | https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Ethics/Ethics-Technology-Resources | 2026-05-14 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version) | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05-14 | full |
| CERTINIA-VEDA-2026 | Veda: AI agents for professional services (Certinia AI page) | Certinia | vendor | https://certinia.com/solutions/ai | 2026-10 | full |
| CFOTECH-ELITE-2026 | Elite adds AI tools to 3E to streamline work-to-cash | CFOtech UK | press | https://cfotech.co.uk/story/elite-adds-ai-tools-to-3e-to-streamline-work-to-cash | 2026-02-27 | full |
| EDISCOVERYTODAY-ILTACON-2026 | My five ILTACON 2026 takeaways | eDiscovery Today (Doug Austin) | press | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 | full |
| ELITE-VALIDATE-2025 | Elite launches Elite Validate: legal invoice compliance solution | Elite (press release) | vendor | https://www.elite.com/insights/news/press-releases/elite-launches-elite-validate | 2025-02-11 | full |
| INTAPP-BILLSTREAM-2026 | Intapp Billstream | Intapp | vendor | https://www.intapp.com/billing/ | 2026-10 | full |
| INTAPP-TERMS-2026 | Intapp Terms: enforce client obligations everywhere | Intapp | vendor | https://www.intapp.com/terms/ | 2026-10 | full |
| INTAPP-TIME-2026 | Intapp Time: AI time tracking software | Intapp | vendor | https://www.intapp.com/time-tracking/ | 2026-10 | full |
| INTAPP-TIMEBILL-2026 | AI-powered timekeeping and prebilling for maximum revenue (Intapp compliant time and billing) | Intapp | vendor | https://www.intapp.com/legal/ai-powered-timekeeping-compliant-billing/ | 2026-10 | full |
| INTAPP-TIMEKEEPING-2026 | Compliant timekeeping (Intapp Time for law firms) | Intapp | vendor | https://www.intapp.com/legal/timekeeping/ | 2026-10 | full |
| INTAPP-TIMERELEASE-2026 | New Intapp Time release brings AI deeper into the time entry workflow to capture more billable hours and protect earned revenue | Intapp (press release via Nasdaq/Business Wire) | vendor | https://www.nasdaq.com/press-release/new-intapp-time-release-brings-ai-deeper-time-entry-workflow-capture-more-billable | 2026-05-21 | full |
| LAUREL-ALLENS-2026 | Laurel expands Asia-Pacific presence through firmwide partnership with Allens | Laurel (press release) | vendor | https://www.laurel.ai/press/laurel-expands-asia-pacific-presence-through-firmwide-partnership-with-allens | 2026-05-28 | full |
| LAUREL-AMLAW200-2026 | Am Law 200 top VC firm customer story (firm not named) | Laurel | vendor | https://www.laurel.ai/customer-stories/am-law-200-top-vc-firm | 2026-08 | full |
| LAUREL-BERGER-2026 | Berger Singerman and Laurel: a practical approach to AI adoption | Laurel | vendor | https://www.laurel.ai/press/berger-singermanand-laurel-a-practical-approach-to-ai-adoption | 2026-09 | full |
| LAUREL-BIGFOURTAX-2026 | Laurel drives annual profit for a Big Four firm (customer story, firm not named) | Laurel | vendor | https://www.laurel.ai/customer-stories/laurel-drives-annual-profit-for-big-four-firm | 2026-09 | full |
| LAUREL-BILLINGBLOG-2026 | Laurel Billing: defend every bill before it goes out | Laurel (blog) | vendor | https://www.laurel.ai/blog/coming-soon-laurel-billing | 2026-09-17 | full |
| LAUREL-BILLINGPAGE-2026 | Billing: the billing workspace, coming soon (product page and FAQ) | Laurel | vendor | https://www.laurel.ai/platform/billing | 2026-10 | full |
| LAUREL-COMPLIANCE-2026 | Compliance: every billing guideline, applied automatically (product page) | Laurel | vendor | https://www.laurel.ai/platform/compliance | 2026-10 | full |
| LAUREL-DAYSHAPE-2026 | Laurel and Dayshape partner to help professional services firms tackle hidden revenue leakage | Laurel (press release) | vendor | https://www.laurel.ai/press/laurel-dayshape-partner-professional-services-revenue-leakage | 2026-06-02 | full |
| LAUREL-FIRMLEADERSHIP-2026 | Laurel for firm leadership (page at /solutions/laurel-for-big-four) | Laurel | vendor | https://www.laurel.ai/solutions/laurel-for-big-four | 2026-10 | full |
| LAUREL-GHJ-2026 | How Laurel unlocked firmwide time intelligence for GHJ leadership (customer story) | Laurel | vendor | https://www.laurel.ai/customer-stories/ghj | 2026-08 | full |
| LAUREL-HOME-2026 | AI Timekeeping & Work Intelligence Platform (home page) | Laurel | vendor | https://www.laurel.ai | 2026-10 | full |
| LAUREL-LERNERS-2026 | How Lerners repaired client service issues, netting out to zero billing disputes (customer story) | Laurel | vendor | https://www.laurel.ai/customer-stories/lerners | 2026-08 | full |
| LAUREL-OBERMAYER-2026 | How Obermayer solved their timekeeping issue and reimagined how their attorneys work (customer story) | Laurel | vendor | https://www.laurel.ai/customer-stories/obermayer | 2026-08 | full |
| LAUREL-PROOF-2026 | Proof 2026 recap: AI in professional services starts with the work itself | Laurel (blog) | conference | https://www.laurel.ai/blog/proof-2026-recap-ai-in-professional-services | 2026-10-13 | full |
| LAUREL-SIGNAL-2026 | Laurel Signal: firm insights (product page) | Laurel | vendor | https://www.laurel.ai/platform/signal | 2026-10 | full |
| LAUREL-TIMEKEEPING-2026 | Timekeeping: smarter timesheets (product page) | Laurel | vendor | https://www.laurel.ai/platform/timekeeping | 2026-10 | full |
| LAUREL-TONKONTORP-2026 | Tonkon Torp customer story | Laurel | vendor | https://www.laurel.ai/customer-stories/tonkon-torp | 2026-08 | full |
| LAUREL-TR-2026 | Laurel and Thomson Reuters partner to help law firms prove the business value of AI | Laurel (press release) | vendor | https://www.laurel.ai/press/laurel-and-thomson-reuters | 2026-08-05 | full |
| LAUREL-WARRENAVERETT-2026 | How Warren Averett turned time entry into a competitive advantage (customer story) | Laurel | vendor | https://www.laurel.ai/customer-stories/warren-averett | 2026-08 | full |
| LAUREL-WSGR-2026 | Laurel brings AI-powered time intelligence to Wilson Sonsini Goodrich & Rosati | Laurel (press release) | vendor | https://www.laurel.ai/press/laurel-brings-ai-powered-time-intelligence-to-wilson-sonsini-goodrich-rosati | 2026-08 | full |
| LAWSITES-BILLABLESAI-2025 | Billing in the age of AI: a practical guide for law firms (sponsored post by Billables AI) | LawSites (sponsored post) | press | https://www.lawnext.com/2025/10/billing-in-the-age-of-ai-a-practical-guide-for-law-firms.html | 2025-10-07 | full |
| LAWSITES-LITIFY-2026 | Litify launches AI-powered time capture with Billables AI to recover lost time | LawSites (Bob Ambrogi; vendor-supplied release) | press | https://www.lawnext.com/2026/05/litify-launches-ai-powered-time-capture-with-billables-ai-to-recover-lost-time.html | 2026-05-21 | full |
| LEGALIT-FOLEY-2024 | Foley Mansfield goes live with Verify from Zero Systems for gen AI pre-bill review | Legal IT Insider | press | https://legaltechnology.com/foley-mansfield-goes-live-with-verify-from-zero-systems-for-gen-ai-pre-bill-review/ | 2024-05-15 | full |
| LEGORA-LAUREL-2026 | Legora and Laurel partner to capture the time lawyers spend in Legora as they work | Legora (press release) | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 | full |
| TRI-KOPKA-2026 | How one law firm is challenging a broken status quo around billing | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing | 2026-04-30 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-LFFI-Q1-2026 | Law Firm Financial Index Q1 2026: strong inputs, average output | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output | 2026-05-13 | full |
| TXETHICS-OP705-2025 | Opinion 705 (generative AI in the practice of law) | Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics | regulator | https://www.legalethicstexas.com/resources/opinions/opinion-705/ | 2025-02 | full |
| VSB-LEO1901-2025 | Petition of the Virginia State Bar to the Supreme Court of Virginia: proposed Legal Ethics Opinion 1901 (reasonable fees and generative AI) | Virginia State Bar | regulator | https://vsb.org/common/Uploaded%20files/docs/20250724-leo1901-petition.pdf | 2025-07 | full |

## 6. Gaps

- **Independent evidence:** no regulator, academic or independent measurement of AI time capture, narrative accuracy, write-downs, e-billing rejections or collections was found. No override or edit rates, parallel runs or error rates are published by any source. A search for academic work returned only surveys and vendor material.
- **Job postings:** none showing real use were found. Two searches returned vendor blogs; the one posting opened (Laurel's own Controller role) is not relevant.
- **Blocked or not readable:** ABA Formal Opinion 512 (HTTP 403); Aderant's Verify product page (blocked); Clio Legal Trends 2026 (gated; the opened page says only that firms billing by the hour may see AI shrink revenue); LexisNexis CounselLink SmartReview, Wolters Kluwer LegalVIEW BillAnalyzer and Epiq managed invoice review pages (JavaScript-rendered or blocked; seen in search results only: Epiq case study https://www.epiqglobal.com/en-US/Resource-Center/Case-Study/epiq-expert-supported-invoice-review; Wolters Kluwer https://www.wolterskluwer.com/en/expert-insights/efficiency-unleashed-transforming-legal-bill-review-with-ai; LexisNexis https://www.lexisnexis.com/community/amp-insights/177/ai-legal-spend-management-counsellink). Their savings claims (for example 8%, 10%, 6%) were not verified and are not used.
- **Search-only leads not opened:** Elite generative AI time entry (2023) and eBillingHub rejection categorisation; EY AI collections assistant case (a client-facing service, not a firm's own receivables); Litify, Billables AI and PointOne customer evidence beyond the launch release.
- **Accounting and consulting billing:** the only collections example found for accounting firms (BGW with Anduin) is from 2021 and sponsored; no named consulting-firm billing deployment was found other than the unnamed Big Four tax division. Karbon's State of AI in Accounting 2026 page was opened but figures were not retrievable.
- **Dates:** Laurel customer-story and press pages carry site metadata dates in August to September 2026 that look like site updates (the $100 million funding release, dated 2025-06-10 in its text, carries August 2026 metadata). The month given for those pages is the metadata date and may be later than the original story. Intapp, Brightflag and Certinia product pages show no date and are dated by reading (2026-10).
- **Inconsistencies in sources:** Tonkon Torp's page gives 21 minutes in the key facts and 20 minutes in the body, and 20% faster collection cycle against 20% faster release velocity; Laurel's "4-11%" is a profit increase on its home page and a revenue lift in the Thomson Reuters release.
- **Not assessable:** whether Foley Mansfield still uses Verify after the 2025 Aderant deal; whether Laurel Billing, Aderant's agents or Elite Intelligence are used by any named firm; UK and EU firms (SRA and the Law Society's billing guidance were not reached).
- **Landscape leads not reached:** CLOC Harbor/SOTI spend data (members-only); Thomson Reuters Law Firm Rates Report 2026 realization data (not opened).
