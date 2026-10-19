# Billing and collections: discourse angle (professional-services)

Prepared 2026-10-19. Angle: what practitioners are saying about AI from time capture to cash (time entry, narratives, pre-bill review, e-billing and guidelines, write-downs, realization, collections), from conference coverage, practitioner articles, trade press, vendor announcements and customer stories, mostly dated 2025-10 to 2026-10. In-house legal-operations examples are tagged "in-house".

## 1. Summary

**Evidence grades:** 0 A, 2 B, 8 C, 3 D across 13 candidate use cases. **Sources:** 49 distinct, all opened and read (none search-only): 7 conference, 1 podcast, 15 press, 4 survey, 1 regulator, 3 professional-body, 18 vendor.

**What the field is saying**

- **Time capture is moving from recollection to a system record, and the money argument is made by vendors.** Laurel, Billables AI, Ajax and Litify sell passive capture with drafted narratives; Legora and Aderant now tie AI-platform work to draft entries (LEGORA-LAUREL-2026; ADERANT-HARVEY-2026; LITIFY-LAWSITES-2026). The only named deployment with figures is a vendor customer story (about 15 minutes of billable time recovered per attorney per day; LAUREL-BERGER-2026). The sizing claims for unrecorded time do not agree with each other (about 11%, 10-30%, up to 30%) and none is independent.
- **Billing is becoming a contest between automated reviewers.** Elite reports invoice rejection rates rising from 11% to 18% in 2025 and links this to corporate legal departments using AI to review invoices; 71% of the firms it studied still manage guideline compliance by hand (ELITE-REJECT-2026). The same release says average days to payment fell from 62 to 50 for its eBillingHub customers, so faster payment and more rejections moved together (ELITE-REJECT-2026).
- **AI raises new billing questions that practitioners have not settled.** Clients ask for line-item AI transparency while others say they will not pay for work done by AI (TRI-LEGALWEEK-2026); California says hourly billing must reflect time actually spent and that general AI subscriptions are overhead (CALBAR-GENAI-2026, p. 8); ILTACON 2026 practitioners asked whether metered token spend becomes a passed-through line item (TRI-ILTACON-METER-2026).
- **Write-down and realization are the sober numbers.** Partners write down time before bills go out, and TRI sees realization against standard rates eroding since 2021 even as rates rise (TRI-WRITEDOWNS-2023; TRI-PROSPERITY-2025). TRI proposes pointing AI at the tasks that cause write-downs (an idea, not a deployment; TRI-ROI-2025).
- **Collections is the least evidenced step.** Oddr announced AI-drafted follow-ups and a collections agent still in development (ODDR-COLLECTIONS-2026).

**Quality evidence:** none independent. The one accuracy comparison is a vendor's (ONIT-SPEND-2026). No error, override or parallel-run figures exist for AI time capture, narrative drafting or invoice review in the sources read. Discourse is also skewed to vendors and vendor-adjacent publishers: the Legalweek panels were Thomson Reuters-sponsored, and Oddr refers to the Elite report as Thomson Reuters Elite research.

## 2. Use cases

```yaml
- id: professional-services-billing-collections-01
  title: Ambient time capture with AI-drafted narratives, reviewed by the timekeeper
  archetype: professional-services
  module: billing-collections
  function: service-delivery
  work_types:
  - transaction-processing
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: Lawyers record time by reconstructing it from memory at the end of a day or week, so short tasks are
    missed and narratives approximate the work; recording time is itself unbillable work (LEGORA-LAUREL-2026). A
    defense-firm COO says the tedium of capturing time in tenth-of-an-hour entries is driving talent out of defense
    work (TRI-KOPKA-2026).
  solution: 'Software observes work across email, documents, calls and other applications (some products read whatever
    window is active), uses a language model to assign activity to a client and matter, and drafts a narrative.
    The timekeeper reviews, edits and submits the draft to the billing system. Products named in the sources: Laurel,
    Billables AI (inside Litify), Ajax, and Querious (client conversations) (LAUREL-TIMESHEETS-2026; LAWSITES-AJAX-2025;
    LITIFY-LAWSITES-2026; QUERIOUS-LAWSITES-2025).'
  outcomes:
  - lever: capacity
    description: Average billable time recovered per attorney per day at a firm that then extended the rollout to
      all six offices
    figure: nearly 15 minutes per day
    measures: average billable time recovered by attorneys each day, as stated in the vendor customer story for
      Berger Singerman; baseline, sample and method are not stated
    provenance: vendor-published
    source_ref: LAUREL-BERGER-2026
  - lever: speed
    description: Time entries that could previously stay outstanding for days were completed faster
    figure: approximately two days faster
    measures: time-entry completion time at the same firm, per the vendor customer story; baseline and sample not
      stated
    provenance: vendor-published
    source_ref: LAUREL-BERGER-2026
  - lever: growth
    description: Laurel says firms using AI timekeeping capture more revenue than firms relying on manual entry
    figure: 4-11% more revenue
    measures: revenue captured by firms using AI timekeeping versus firms relying on manual entry, per Laurel; comparison
      group and method not given
    provenance: vendor-published
    source_ref: LAUREL-TIMESHEETS-2026
  - lever: growth
    description: Ajax says some customer case studies show more recorded hours
    figure: 42% to 61% upticks in recorded hours
    measures: increase in recorded hours in some case studies the vendor shared with LawSites; customers not named
    provenance: vendor-published
    source_ref: LAWSITES-AJAX-2025
  prerequisites:
  - Native integration with the firm billing system so entries are not re-keyed; Laurel names Aderant, Elite 3E
    and Clio (LAUREL-TIMESHEETS-2026). Berger Singerman integrated Laurel with its Aderant billing system (LAUREL-BERGER-2026)
  - Content-level capture (which email, which document, which matter) rather than window-level logging, because
    Laurel says only the former produces entries detailed enough to bill without rewriting (LAUREL-TIMESHEETS-2026)
  - Narratives that meet client billing guidelines at the point of entry (LAUREL-TIMESHEETS-2026)
  - 'Security attestation: Laurel calls SOC 2 Type II the minimum bar and says ISO 42001 is increasingly relevant
    (LAUREL-TIMESHEETS-2026)'
  - A way for timekeepers to pause capture for personal matters; Ajax describes a pause function (LAWSITES-AJAX-2025)
  - 'Adoption measured by behaviour, not go-live: Laurel says the gap between deployment and ROI is almost always
    an adoption problem (LAUREL-TIMESHEETS-2026)'
  risks_and_guardrails:
  - Capture tools touch privileged client communications, so vendor data handling needs scrutiny (LAUREL-TIMESHEETS-2026)
  - California guidance says hourly billing must reflect time actually spent on the matter (CALBAR-GENAI-2026, p.
    8); a draft entry is a proposal, not a record of billable time
  - 'Review burden is a live design question: Ajax says Laurel needs 50-75 activities reviewed per day against 10-20
    for Ajax. This is one competitor''s claim about another and was not verified (LAWSITES-AJAX-2025)'
  - Vendor revenue claims differ in basis and are not independently verified (see notes)
  human_checkpoints:
  - Timekeeper reviews, edits and submits each draft entry (LEGORA-LAUREL-2026; LAWSITES-AJAX-2025)
  - Firm approval process for time continues unchanged where integrated (ADERANT-HARVEY-2026)
  role_evolution: The timekeeper moves from recalling and typing entries to reviewing drafts (LEGORA-LAUREL-2026).
    Berger Singerman says reduced time-entry administration frees professional staff for other work (LAUREL-BERGER-2026).
  evidence_grade: B
  sources:
  - ref: LAUREL-BERGER-2026
    title: 'Berger Singerman and Laurel: A practical approach to AI adoption'
    publisher: Laurel (customer story)
    type: vendor
    url: https://www.laurel.ai/press/berger-singermanand-laurel-a-practical-approach-to-ai-adoption
    date: '2026-09-28'
    access: full
    locator: customer story, paragraph beginning "Laurel's platform automates time capture" (15 minutes, two days;
      Aderant integration; six offices)
  - ref: LAUREL-TIMESHEETS-2026
    title: 'Automated timesheets for law firms: A complete 2026 guide'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/blog/automated-timesheets-law-firms
    date: '2026-09-17'
    access: full
    locator: opening paragraphs (4-11%); buying-criteria sections on capture depth, OCG rules, integrations, security,
      adoption
  - ref: LAWSITES-AJAX-2025
    title: 'The Smart Screen Reader: How Ajax Is Automating Legal Timekeeping with AI-Powered Activity Tracking'
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2025/09/the-smart-screen-reader-how-ajax-is-automating-legal-timekeeping-with-ai-powered-activity-tracking.html
    date: '2025-09-09'
    access: full
    locator: paragraphs on 42-61% case studies, the 50-75 vs 10-20 review claim and the pause function
  - ref: LITIFY-LAWSITES-2026
    title: Litify Launches AI-Powered Time Capture with Billables AI to Recover Lost Time (press release carried
      by LawSites)
    publisher: Litify and Billables AI (via LawSites)
    type: vendor
    url: https://www.lawnext.com/2026/05/litify-launches-ai-powered-time-capture-with-billables-ai-to-recover-lost-time.html
    date: '2026-05-19'
    access: full
    locator: paragraphs 1-3 (Litify AI Time Capture with Billables AI; up to 30% of billable work unrecorded)
  - ref: QUERIOUS-LAWSITES-2025
    title: Querious Joins Clio's App Directory to Help Law Firms Capture More Billable Time with AI (press release
      carried by LawSites)
    publisher: Querious (via LawSites)
    type: vendor
    url: https://www.lawnext.com/2025/08/querious-joins-clios-app-directory-to-help-law-firms-capture-more-billable-time-with-ai.html
    date: '2025-08-27'
    access: full
    locator: opening paragraphs (conversation-to-entry capture, Clio integration)
  - ref: LAUREL-FOSTERS-2026
    title: Fosters Solicitors selects Laurel as its AI time platform
    publisher: Laurel (press release; date from page metadata, shared by several Laurel releases)
    type: vendor
    url: https://www.laurel.ai/press/fosters-solicitors-selects-laurel-as-its-ai-time-platform
    date: '2026-08-19'
    access: full
    locator: paragraph 1 (selected, deploying across 100 fee earners)
  - ref: ALA-TIMEAI-2026
    title: Time-Tracking in the AI Era (webcast abstract, 3 Feb 2026; speaker from Billables AI)
    publisher: ALA Legal Marketplace (Webvent)
    type: professional-body
    url: https://solution-series.alanet.org/webinar/5775
    date: '2026-02-03'
    access: full
    locator: abstract (shift from manual, timer-based tracking to automated capture)
  - ref: LAUREL-SOW-2025
    title: The State of Work 2025 (report landing page; no publication date shown)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/state-of-work-2025
    date: '2025'
    access: full
    locator: 'highlights: approximately 11% of unsubmitted time should have been billed'
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora (press release)
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: paragraph 2 (reconstruction from memory)
  - ref: TRI-KOPKA-2026
    title: How one law firm is challenging a broken status quo around billing
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing
    date: '2026-04-30'
    access: full
    locator: section quoting COO Donna Markus on talent leaving because of time capture
  - ref: REINVENTING-KAPLAN-2025
    title: How Law Firms Can Use AI to Capture More Time (Reinventing Professionals; show notes only)
    publisher: Reinventing Professionals (Ari Kaplan)
    type: podcast
    url: https://reinventingprofessionals.podbean.com/e/how-law-firms-can-use-ai-to-capture-more-time
    date: '2025-02-12'
    access: full
    locator: show-note abstract only (AI-native time tracking for hourly billers); February 2025, outside the 18-month
      window, used as foundation
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026'
    access: full
    locator: p. 8, "Charging for Work Produced by Generative AI"
  last_reviewed: '2026-10-19'
  notes: 'No independent measurement of capture accuracy, entry edit rates or revenue recovery was found. Vendor
    sizing claims do not share a basis: Laurel says about 11% of unsubmitted time is work that should have been
    billed (LAUREL-SOW-2025) and that 10-30% of billable work never reaches an invoice (TR-LAUREL-2026); Litify
    says up to 30% of billable work goes unrecorded in many firms (LITIFY-LAWSITES-2026); Querious says average
    improved realization of $36,000 per lawyer (QUERIOUS-LAWSITES-2025). Berger Singerman is the one named deployment
    with figures, and the figures come from the vendor customer story. Fosters Solicitors (100 fee earners) is announced,
    not yet reporting. Grade B because the named deployment has no firm-published measurement.'
- id: professional-services-billing-collections-02
  title: Work done inside AI platforms logged automatically as draft time entries
  archetype: professional-services
  module: billing-collections
  function: service-delivery
  work_types:
  - transaction-processing
  - data-reporting
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: As more of the working day moves into AI platforms, that work is hard to capture and easy to leave off
    the timesheet; firm leaders also want to see what return the AI work produces (LEGORA-LAUREL-2026).
  solution: 'The AI platform passes completed tasks to the timekeeping system, which creates a draft entry with
    matter context, duration and an AI-generated narrative; the lawyer reviews, edits and submits it through the
    firm''s normal approval process. Announced pairings: Harvey with Aderant iTimekeep ("now live" for firms using
    both), Legora with Laurel (first phase to come), Thomson Reuters tools (CoCounsel Legal, Westlaw, Practical
    Law, HighQ) with Laurel (ADERANT-HARVEY-2026; LEGORA-LAUREL-2026; TR-LAUREL-2026).'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: not applicable
    provenance: self-reported
    source_ref: ADERANT-HARVEY-2026
  prerequisites:
  - Firm uses both the AI platform and the timekeeping product (ADERANT-HARVEY-2026; LEGORA-LAUREL-2026)
  - Existing billing controls and approval workflow retained (ADERANT-HARVEY-2026)
  risks_and_guardrails:
  - The sources do not say how the duration on an auto-created entry is measured (lawyer time or system run time);
    California guidance says hourly billing must reflect time actually spent (CALBAR-GENAI-2026, p. 8). This is
    an open question for any firm adopting this pattern, not a finding of the sources
  - Entry quality and compliance with client billing rules are asserted by the vendors and not measured publicly
    (LEGORA-LAUREL-2026; ADERANT-HARVEY-2026)
  human_checkpoints:
  - Lawyer reviews, edits and submits the draft (ADERANT-HARVEY-2026; LEGORA-LAUREL-2026)
  role_evolution: Timekeepers review entries generated by the work itself rather than reconstructing them; Legora
    and Laurel say phase two will add measures of AI usage and value (LEGORA-LAUREL-2026).
  evidence_grade: C
  sources:
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora (press release)
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: paragraphs 1-4 and the two-phase list
  - ref: LAWSITES-LAUREL-2026
    title: Legora and Laurel Partner to Enable Automatic Time Capture; Will Later Develop Measures of Legora's Value
      to Firms
    publisher: LawSites (Bob Ambrogi)
    type: press
    url: https://www.lawnext.com/2026/10/legora-and-laurel-partner-to-enable-automatic-time-capture-will-later-develop-measures-of-legoras-value-to-firms.html
    date: '2026-10-13'
    access: full
    locator: paragraphs 1-6
  - ref: ADERANT-HARVEY-2026
    title: Aderant Launches iTimekeep Integration with Harvey, Turning AI-Powered Legal Work into Billable Time
    publisher: Aderant (press release)
    type: vendor
    url: https://www.aderant.com/news-pr/aderant-launches-itimekeep-integration-with-harvey/
    date: '2026-08-17'
    access: full
    locator: paragraphs 1-3 ("now live"; draft with matter context, duration and narrative)
  - ref: TR-LAUREL-2026
    title: Thomson Reuters and Laurel connect legal AI to ROI
    publisher: Thomson Reuters (legal blog)
    type: vendor
    url: https://legal.thomsonreuters.com/blog/thomson-reuters-and-laurel-help-law-firms-connect-legal-ai-to-business-outcomes/
    date: '2026-08-05'
    access: full
    locator: section describing Laurel Time capturing CoCounsel Legal, Westlaw, Practical Law and HighQ activity
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026'
    access: full
    locator: p. 8
  last_reviewed: '2026-10-19'
  notes: 'Vendor announcements only. Legora and Laurel describe what firms "will" get and say availability details
    follow at rollout; Aderant says the integration is live but names no adopting firm. Dates: Aderant 2026-08-17,
    Thomson Reuters-Laurel 2026-08-05, Legora-Laurel 2026-10-13. The value-measurement phase of Legora-Laurel is
    routed to firm-finance.'
- id: professional-services-billing-collections-03
  title: Bulk checking of time-entry narratives before billing (WIP review)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - review-assurance
  - document-production
  pattern: full-population-testing
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: Reviewing narrative time entries for wrong workstream, typos and non-compliance with client requirements
    is laborious (NONBILLABLE-LINKLATERS-2025).
  solution: Linklaters' Narrative Checker is an Excel plugin that sends narratives to the firm's in-house chatbot,
    Laila, to find common time-recording issues and propose corrections that the user reviews quickly. It was built
    by a managing associate and developed with the in-house development team (NONBILLABLE-LINKLATERS-2025).
  outcomes:
  - lever: speed
    description: Processing speed of the tool as described by its product owner
    figure: around a thousand narratives a minute
    measures: narratives processed per minute, as stated by the managing associate who built it; test conditions
      not given
    provenance: self-reported
    source_ref: NONBILLABLE-LINKLATERS-2025
  - lever: capacity
    description: Early use after global launch
    figure: used over 300 times across 13 offices in just over a week
    measures: number of tool uses, as stated by the product owner; users and entries per use not given
    provenance: self-reported
    source_ref: NONBILLABLE-LINKLATERS-2025
  prerequisites:
  - An in-house, data-secure chatbot the firm already trusts (Laila) (NONBILLABLE-LINKLATERS-2025)
  - Senior sponsorship and a six-month internal GenAI secondment plus in-house developers to turn a prototype into
    an enterprise version (NONBILLABLE-LINKLATERS-2025)
  - A global pilot over the summer before release to the whole firm on 1 September (NONBILLABLE-LINKLATERS-2025;
    article dated 2025-10-09)
  risks_and_guardrails:
  - No accuracy, false-positive or override data are published; the product owner says the user reviews each suggestion
    and the aim is to keep humans in the loop (NONBILLABLE-LINKLATERS-2025)
  - Linklaters states an aim of saving hundreds or thousands of hours a year; that is a goal, not a result (NONBILLABLE-LINKLATERS-2025)
  human_checkpoints:
  - User accepts or rejects each suggested correction (NONBILLABLE-LINKLATERS-2025)
  role_evolution: The firm says the tool should free lawyers, PAs and secretaries for more valuable work (NONBILLABLE-LINKLATERS-2025).
  evidence_grade: B
  sources:
  - ref: NONBILLABLE-LINKLATERS-2025
    title: Linklaters' new AI time recording tool started as one associate's side project (interview with James
      Phoenix)
    publisher: Non-Billable
    type: press
    url: https://www.nonbillable.co.uk/news/linklaters-ai-time-recording-tool-associate-side-project
    date: '2025-10-09'
    access: full
    locator: interview answers on what the tool does, build and rollout, and adoption; closing "Bigger picture"
      paragraphs
  last_reviewed: '2026-10-19'
  notes: Named firm, in production firmwide (3,000+ lawyers able to use it), but the figures are usage and speed
    statements by the builder, not outcome measurement, so B rather than A. Interview published 2025-10-09, about
    12 months before this review.
- id: professional-services-billing-collections-04
  title: Client-guideline compliance checked at time entry and before invoice submission (firm side)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - review-assurance
  - transaction-processing
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Clients' outside counsel guidelines (OCGs) are enforced more quickly and consistently than before, while
    71% of the firms in Elite's study still manage OCG compliance mainly by hand and fix problems after an invoice
    has been rejected (ELITE-REJECT-2026; ELITE-IDEA-2026).
  solution: Rules and AI checks run at entry and again before the invoice leaves the firm, so vague descriptions,
    unapproved rates, excessive time and similar issues are corrected upstream. Elite markets Validate for this;
    Fulcrum GT markets e-billing validation to cut rejected invoices and AI-assisted time capture with cleaner narratives;
    Laurel markets billing agents that catch guideline violations and scope overages before bills reach clients
    (ELITE-REJECT-2026; FULCRUM-ILTACON-2026; LAUREL-FOSTERS-2026).
  outcomes:
  - lever: speed
    description: Elite eBillingHub customers' average payment time fell in 2025 (not tied by the source to Validate)
    figure: 62 to 50 days
    measures: average days to payment for eBillingHub customers in 2025 versus the prior period, per Elite
    provenance: vendor-published
    source_ref: ELITE-REJECT-2026
  - lever: risk
    description: Rejection rate across Elite's billing data rose, which Elite links to client AI review
    figure: 11% to 18% in 2025
    measures: invoice rejection rate in Elite billing data for about 400 firms; the release does not define numerator
      and denominator
    provenance: vendor-published
    source_ref: ELITE-REJECT-2026
  - lever: quality
    description: Largest categories of fee reductions in the same data
    figure: rate deviation or unapproved rate 23.88%; vague description or entry quality 7.57%; excessive or unsupported
      time 7.33%
    measures: each category's share of fee reductions, per Elite's e-billing report; whether shares are by count
      or value is not stated
    provenance: vendor-published
    source_ref: ELITE-IDEA-2026
  prerequisites:
  - Client billing rules managed inside the e-billing system (FULCRUM-ILTACON-2026)
  - Connected financial workflows; Elite says firms with embedded intelligence and connected workflows move cash
    faster (ELITE-REJECT-2026)
  risks_and_guardrails:
  - Elite sells the tooling it recommends, and its report ties the rise in rejections to client AI review as an
    inference ("the data suggests") rather than a measured cause (ELITE-REJECT-2026; ELITE-IDEA-2026)
  - The report notes that client AI decisions can be opaque to the firm, so rules learned from rejections may be
    incomplete (ELITE-IDEA-2026)
  human_checkpoints:
  - The sources do not describe the review step; Elite's wording implies firm staff act on flagged issues before
    an invoice reaches the client (ELITE-REJECT-2026)
  role_evolution: Elite says billing teams should move from reactive correction after rejection to proactive revenue
    protection (ELITE-REJECT-2026).
  evidence_grade: C
  sources:
  - ref: ELITE-REJECT-2026
    title: 'New Elite Research: Law Firms See 64% Climb in Rejection Rates as Client AI Billing Scrutiny Advances'
    publisher: Elite (press release)
    type: vendor
    url: https://www.elite.com/insights/news/new-elite-research-law-firms-see-64-climb-in-rejection-rates-as-client-ai-billing-scrutiny-advances
    date: '2026-05-14'
    access: full
    locator: release headline bullets and paragraphs 3-4 (rejection 11% to 18%, 71% manual, 62 to 50 days)
  - ref: ITBRIEF-ELITE-2026
    title: AI invoice checks drive law firms' rejection rates up
    publisher: IT Brief Australia
    type: press
    url: https://itbrief.com.au/story/ai-invoice-checks-drive-law-firms-rejection-rates-up
    date: '2026-05-20'
    access: full
    locator: paragraphs 1-4
  - ref: ELITE-IDEA-2026
    title: Your Clients' AI Is Reviewing Every Invoice. Does Your Firm Know What It's Looking For?
    publisher: Elite (blog)
    type: vendor
    url: https://www.elite.com/insights/ideas/clients-ai-is-reviewing-every-invoice
    date: '2026-06-15'
    access: full
    locator: section on fee-reduction categories; section on opacity of client review
  - ref: FULCRUM-ILTACON-2026
    title: ILTACON 2026 (Fulcrum GT event page; product descriptions, no session content; page date not shown)
    publisher: Fulcrum GT
    type: vendor
    url: https://iltacon.fulcrumgt.com/
    date: '2026'
    access: full
    locator: product list ("Cut rejected invoices..."; "AI-assisted time capture")
  - ref: LAUREL-FOSTERS-2026
    title: Fosters Solicitors selects Laurel as its AI time platform
    publisher: Laurel (press release; date from page metadata, shared by several Laurel releases)
    type: vendor
    url: https://www.laurel.ai/press/fosters-solicitors-selects-laurel-as-its-ai-time-platform
    date: '2026-08-19'
    access: full
    locator: Laurel Billing blurb in page header
  - ref: LAUREL-TIMESHEETS-2026
    title: 'Automated timesheets for law firms: A complete 2026 guide'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/blog/automated-timesheets-law-firms
    date: '2026-09-17'
    access: full
    locator: 'criteria section: enforce OCG rules at the point of entry'
  last_reviewed: '2026-10-19'
  notes: Strongest measured data point in this module is Elite's rejection series, but it describes the problem,
    not the outcome of the fix. Elite's release calls its report "E-Billing After AI" and its blog calls it the
    "2025 E-Billing Intelligence Report"; the same figures appear in both. No named firm reports results from pre-submission
    validation. Not graded higher because the outcomes are vendor-published market data, not results of the use
    case.
- id: professional-services-billing-collections-05
  title: Client-side AI review of every outside-counsel invoice against billing guidelines (in-house)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - review-assurance
  - transaction-processing
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Manual bill review is a retrospective exercise that samples high-value bills and rarely prevents overspend
    (WK-LEGALSPEND-2026). Insurers employ large departments and vendors to review, audit and cut defense bills (TRI-KOPKA-2026).
  solution: 'AI checks outside counsel invoices line by line against the client''s billing guidelines before they
    reach the legal team and audits every invoice rather than a sample. Products named: Onit Spend Agent, Wolters
    Kluwer legal bill review, Milliman Datalytics-Defense for insurer litigation management (ONIT-SPEND-2026; WK-LEGALSPEND-2026;
    MILLIMAN-BILLREVIEW-2026). In-house/legal-operations use.'
  outcomes:
  - lever: quality
    description: Onit says its Spend Agent beats experienced lawyers at flagging invoice problems
    figure: 92% invoice-level and 81% line-item accuracy versus 72% and 43% for experienced lawyers
    measures: accuracy of the tool and of experienced lawyers in Onit's published research; test set, ground truth
      and definition of accuracy are not on the page
    provenance: vendor-published
    source_ref: ONIT-SPEND-2026
  - lever: cost
    description: Wolters Kluwer says automatically enforcing billing guidelines typically reduces legal spend
    figure: up to 10%
    measures: legal spend reduction organisations typically see, per the vendor; basis and sample not given
    provenance: vendor-published
    source_ref: WK-LEGALSPEND-2026
  - lever: risk
    description: Wolters Kluwer says billing compliance by law firms often rises once firms know invoices are audited
    figure: up to 20%
    measures: increase in billing compliance, per the vendor; measure and sample not given
    provenance: vendor-published
    source_ref: WK-LEGALSPEND-2026
  prerequisites:
  - Written billing guidelines that can be applied line by line (WK-LEGALSPEND-2026; ONIT-SPEND-2026)
  - Invoices in structured form (the sources describe PDF and e-billing inputs) (ONIT-SPEND-2026)
  risks_and_guardrails:
  - Law-firm side reports that client AI decisions can be opaque and inconsistent in how rationale is communicated
    (ELITE-IDEA-2026)
  - Clients using AI to cut bills sit alongside clients refusing to pay for AI-assisted work, which firms describe
    as leverage in fee negotiations (TRI-LEGALWEEK-2026)
  human_checkpoints:
  - The sources read do not describe who handles flagged lines or disputes; Onit mentions two operating modes without
    detail (ONIT-SPEND-2026)
  role_evolution: Wolters Kluwer describes a move from reviewing a sample of bills to auditing all invoices (WK-LEGALSPEND-2026).
  evidence_grade: C
  sources:
  - ref: ONIT-SPEND-2026
    title: 'Spend Agent: AI-Powered Invoice Review for Legal Teams (product page; no publication date shown)'
    publisher: Onit
    type: vendor
    url: https://www.onit.com/?p=18328
    date: '2026'
    access: full
    locator: 'page text: accuracy comparison'
  - ref: WK-LEGALSPEND-2026
    title: 'AI in legal spend management: A CFO''s guide'
    publisher: Wolters Kluwer (expert insights)
    type: vendor
    url: https://www.wolterskluwer.com/en/expert-insights/ai-in-legal-spend-management-a-cfos-guide
    date: '2026-02-03'
    access: full
    locator: sections on sampling to total audit coverage and measurable benefits
  - ref: MILLIMAN-BILLREVIEW-2026
    title: 'Legal bill review: AI vs manual invoice audit (insight page; no publication date shown)'
    publisher: Milliman
    type: vendor
    url: https://ae.milliman.com/en/insight/legal-bill-review-ai-manual-invoice-audit
    date: '2026'
    access: full
    locator: comparison of manual, rules-based and AI-enabled bill review
  - ref: ELITE-REJECT-2026
    title: 'New Elite Research: Law Firms See 64% Climb in Rejection Rates as Client AI Billing Scrutiny Advances'
    publisher: Elite (press release)
    type: vendor
    url: https://www.elite.com/insights/news/new-elite-research-law-firms-see-64-climb-in-rejection-rates-as-client-ai-billing-scrutiny-advances
    date: '2026-05-14'
    access: full
    locator: paragraphs 3-4 (client AI scrutiny; rejection 11% to 18%)
  - ref: ELITE-IDEA-2026
    title: Your Clients' AI Is Reviewing Every Invoice. Does Your Firm Know What It's Looking For?
    publisher: Elite (blog)
    type: vendor
    url: https://www.elite.com/insights/ideas/clients-ai-is-reviewing-every-invoice
    date: '2026-06-15'
    access: full
    locator: sections on client-side AI review and gray-area judgments
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: 'section on billing conversation (Blair: some clients'' guidelines say they will not pay for work done
      by AI)'
  - ref: TRI-KOPKA-2026
    title: How one law firm is challenging a broken status quo around billing
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing
    date: '2026-04-30'
    access: full
    locator: section on insurer bill-review departments
  last_reviewed: '2026-10-19'
  notes: in-house. No named in-house team or insurer reports results; all outcome figures are vendor-published and
    could not be verified. Elite's data show rejections rising across several legal spend management platforms (ELITE-REJECT-2026,
    ELITE-IDEA-2026), which is indirect evidence that this is in use. Maturity is recorded as announced because
    no named user was found.
- id: professional-services-billing-collections-06
  title: Outside-counsel spend analytics across firms, practice areas and timekeepers (in-house)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Unstructured invoice data leaves finance without visibility of spend by firm, practice area or timekeeper
    (WK-LEGALSPEND-2026).
  solution: AI turns invoice text into structured data so finance and legal operations can compare firms and timekeepers,
    optimise the panel and negotiate rate structures; Milliman describes attorney-level and firm-level benchmarking
    and pattern detection across matters for insurer litigation management (WK-LEGALSPEND-2026; MILLIMAN-BILLREVIEW-2026).
    In-house/legal-operations use.
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: not applicable
    provenance: self-reported
    source_ref: WK-LEGALSPEND-2026
  prerequisites:
  - Consistent invoice data over time and across matters (WK-LEGALSPEND-2026; MILLIMAN-BILLREVIEW-2026)
  risks_and_guardrails:
  - Vendor descriptions only; no results published (WK-LEGALSPEND-2026; MILLIMAN-BILLREVIEW-2026)
  human_checkpoints:
  - Finance and legal operations decide on panel changes and rate negotiations (WK-LEGALSPEND-2026)
  role_evolution: Milliman says litigation management and claims teams can move beyond transactional invoice approval
    toward proactive oversight of legal spend and attorney behaviour (MILLIMAN-BILLREVIEW-2026).
  evidence_grade: C
  sources:
  - ref: WK-LEGALSPEND-2026
    title: 'AI in legal spend management: A CFO''s guide'
    publisher: Wolters Kluwer (expert insights)
    type: vendor
    url: https://www.wolterskluwer.com/en/expert-insights/ai-in-legal-spend-management-a-cfos-guide
    date: '2026-02-03'
    access: full
    locator: section on visibility and structured intelligence
  - ref: MILLIMAN-BILLREVIEW-2026
    title: 'Legal bill review: AI vs manual invoice audit (insight page; no publication date shown)'
    publisher: Milliman
    type: vendor
    url: https://ae.milliman.com/en/insight/legal-bill-review-ai-manual-invoice-audit
    date: '2026'
    access: full
    locator: section on Datalytics-Defense benchmarking
  last_reviewed: '2026-10-19'
  notes: in-house. Thin, vendor-only evidence. Included because legal-operations spend management is the client-side
    counterpart of firm billing and the landscape names CLOC spend data as a lead (members-only, not reached).
- id: professional-services-billing-collections-07
  title: Early alerts when fixed-fee or capped matters run past their scope
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  - coordination-scheduling
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: announced
  problem: Firms often learn about profitability problems only when a matter closes; extra research, drafting and
    review hours accumulate on a fixed-fee engagement until the write-down is already locked in (TR-LAUREL-2026).
  solution: Time data and AI usage data feed a live view of matter performance so scope creep is flagged while there
    is still time to adjust staffing, renegotiate scope or raise the issue with the client; Laurel describes agents
    that catch scope overages before bills reach clients (TR-LAUREL-2026; LAUREL-FOSTERS-2026).
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: not applicable
    provenance: self-reported
    source_ref: TR-LAUREL-2026
  prerequisites:
  - Complete, timely time capture, since alerts depend on time data (TR-LAUREL-2026)
  - Matters priced or budgeted in advance so overruns can be compared; the Thomson Reuters-Laurel scenario assumes
    a fixed-fee engagement (TR-LAUREL-2026)
  risks_and_guardrails:
  - The Thomson Reuters-Laurel scenario is hypothetical ("picture a fixed-fee engagement"), not a reported case
    (TR-LAUREL-2026)
  human_checkpoints:
  - Matter partner decides whether to adjust staffing, renegotiate scope or tell the client (TR-LAUREL-2026)
  role_evolution: Firm leaders see matter performance while a matter runs rather than after it closes (TR-LAUREL-2026).
  evidence_grade: C
  sources:
  - ref: TR-LAUREL-2026
    title: Thomson Reuters and Laurel connect legal AI to ROI
    publisher: Thomson Reuters (legal blog)
    type: vendor
    url: https://legal.thomsonreuters.com/blog/thomson-reuters-and-laurel-help-law-firms-connect-legal-ai-to-business-outcomes/
    date: '2026-08-05'
    access: full
    locator: section on profitability problems and Laurel Signal; the fixed-fee scenario
  - ref: LAUREL-FOSTERS-2026
    title: Fosters Solicitors selects Laurel as its AI time platform
    publisher: Laurel (press release; date from page metadata, shared by several Laurel releases)
    type: vendor
    url: https://www.laurel.ai/press/fosters-solicitors-selects-laurel-as-its-ai-time-platform
    date: '2026-08-19'
    access: full
    locator: Laurel Billing blurb
  - ref: TRI-MIDSIZE-2026
    title: 'AI execution for midsize law firms: Why the most obvious AI use case is often the wrong one'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/spotlight/midsize-firms-obvious-ai-use-cases
    date: '2026-07-23'
    access: full
    locator: section on fixed-fee work and margin
  last_reviewed: '2026-10-19'
  notes: TRI notes that on fixed-fee work an efficiency gain goes straight to margin (TRI-MIDSIZE-2026), which raises
    the value of catching overruns. Overlaps with delivery-management; kept here because the output is a billing
    and write-down decision.
- id: professional-services-billing-collections-08
  title: Aim AI at the tasks that cause write-downs to lift realization (idea)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  - expert-judgment
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: Partners write down time before the client sees the bill, mostly because the work took too long or became
    too expensive (TRI-ROI-2025). In TRI's 2023 survey of 245 respondents from firms with 11 or more attorneys,
    partners wrote off over 300 hours of their own potentially billable time after it was reported, nearly $190,000
    of fees (TRI-WRITEDOWNS-2023, p. 12); TRI's later summaries describe this as about 300 hours a year per partner
    (TRI-AIEFF-2025).
  solution: 'Idea discussed by TRI: start with a revenue-leakage analysis of where write-downs occur (for example
    the junior-associate learning curve, tasks that take longer than expected, online legal research) and point
    AI at those tasks, so the business case rests on fewer write-offs rather than a change in billing model. TRI
    adds that for midsize firms with high write-offs this may justify AI by itself (TRI-AIEFF-2025; TRI-ROI-2025;
    TRI-MIDSIZE-2026).'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: not applicable
    provenance: self-reported
    source_ref: TRI-ROI-2025
  prerequisites:
  - Write-down data by task, timekeeper and client (TRI-AIEFF-2025; TRI-ROI-2025)
  - 'A pre-AI baseline: TRI cites market-standard realization of around 85% (TRI-MIDSIZE-2026)'
  risks_and_guardrails:
  - Time is often unbilled because the client would not want to pay for it; the aim is to avoid spending the time,
    not to bill it (TRI-AIBOL-2025)
  - Verification burden can absorb the time saved on some tasks (TRI-MIDSIZE-2026)
  - TRI's 2023 write-down data predate current AI tools and were not re-measured in the sources read (TRI-WRITEDOWNS-2023)
  human_checkpoints:
  - Partners keep the pre-bill decision to reduce a bill (TRI-ROI-2025)
  role_evolution: The sources do not describe role changes. TRI's white paper was written with the chief legal operations
    officer of Miles & Stockbridge (TRI-AIEFF-2025).
  evidence_grade: D
  sources:
  - ref: TRI-AIEFF-2025
    title: 'The AI-driven future of legal efficiency: How can law firms reclaim millions in lost revenue while enhancing
      client value? (white paper summary)'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en-us/posts/legal/ai-driven-legal-efficiency-white-paper-2025/
    date: '2025-04-14'
    access: full
    locator: paragraphs on 300 hours and five areas of lost billable hours
  - ref: TRI-ROI-2025
    title: Finding a quicker ROI on law firms' investment in AI
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/law-firm-roi-ai-investment
    date: '2025-05-19'
    access: full
    locator: paragraphs on write-downs, fee erosion and revenue leakage
  - ref: TRI-AIBOL-2025
    title: How AI is continuing to change the business of law
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en-us/posts/legal/ai-business-of-law/
    date: '2025-08-20'
    access: full
    locator: paragraphs on looking for efficiencies and ROI
  - ref: TRI-MIDSIZE-2026
    title: 'AI execution for midsize law firms: Why the most obvious AI use case is often the wrong one'
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/spotlight/midsize-firms-obvious-ai-use-cases
    date: '2026-07-23'
    access: full
    locator: 'section on pricing model: market-standard realization and write-off reduction'
  - ref: TRI-WRITEDOWNS-2023
    title: Law Firm Billing Efficiency and Write Downs (report; foundation, outside the 18-month window)
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2024/04/Law-Firm-Billing-Write-Downs-2023-1.pdf
    date: '2023'
    access: full
    locator: executive summary pp. 2-3 and p. 12
  last_reviewed: '2026-10-19'
  notes: Idea. Practitioners and TRI discuss it, but no firm reports doing it or any result. TRI-WRITEDOWNS-2023
    is foundation material, 3 years old and outside the window.
- id: professional-services-billing-collections-09
  title: Show clients how AI was used and what it saved, matter by matter, at billing time (idea)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - document-production
  - client-interaction
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: Clients are asking whether AI was used on a task and how much time or money it saved, and are rarely
    given an answer; firms report they are still gathering data (TRI-LEGALWEEK-2026). In TRI's 2026 survey, 68%
    of corporate legal professionals did not know whether their outside firms use AI, and one in-house respondent
    feared firms would bill for the time a task would have taken without AI (TRI-GREATDISCONNECT-2026).
  solution: 'Idea discussed at Legalweek 2026: line-item transparency on invoices about AI use and savings, and
    a fee agreement or billing narrative that explains how AI factors into rates and costs. TRI advises firms to
    develop an AI billing strategy and be ready to explain bills in terms of value (TRI-LEGALWEEK-2026; TRI-GREATDISCONNECT-2026;
    CALBAR-GENAI-2026).'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: not applicable
    provenance: self-reported
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - Time entries that record AI use (use cases 1-2) and some measure of time saved, which firms said they do not
    yet have (TRI-LEGALWEEK-2026)
  risks_and_guardrails:
  - Clients also issue guidelines that say they will not pay for services performed by AI, so disclosure can invite
    fee cuts (TRI-LEGALWEEK-2026)
  - California guidance says fee agreements should explain how fees and costs are calculated and how generative
    AI factors into rates (CALBAR-GENAI-2026, p. 8)
  - Texas ethics guidance, as reported by Bloomberg Law, says lawyers cannot charge for time saved by generative
    AI but gives little detail on how to account for AI on bills (BLOOMBERGLAW-TEXAS-2026)
  human_checkpoints:
  - Billing partner decides what is shown to the client (TRI-LEGALWEEK-2026)
  role_evolution: Pricing and innovation leaders take on client AI-value conversations; the Greenberg Traurig chief
    pricing and innovation officer and DLA Piper's head of AI innovation spoke on this at Legalweek (TRI-LEGALWEEK-2026).
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: section on the billing conversation (Polak, Blair, Kaplan)
  - ref: TRI-GREATDISCONNECT-2026
    title: 'The great AI disconnect: Firms and legal departments are not communicating about AI usage'
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect
    date: '2026-03-18'
    access: full
    locator: survey findings and the "develop an AI billing strategy" recommendation
  - ref: BLOOMBERGLAW-CORP-2026
    title: Corporate Teams Expect an Edge Over Law Firms on AI Savings
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/business-and-practice/corporate-teams-expect-an-edge-over-law-firms-on-ai-savings
    date: '2026-03-23'
    access: full
    locator: paragraphs on clients expecting lower bills; ABA reasonable-fee comment
  - ref: BLOOMBERGLAW-TEXAS-2026
    title: AI, Billing Emerge as Crossroads for Texas Law Firms and Clients
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/antitrust/ai-billing-emerge-as-crossroads-for-texas-law-firms-and-clients
    date: '2026-04-21'
    access: full
    locator: paragraphs on Norton Rose billing policy and the Texas opinion
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026'
    access: full
    locator: p. 8
  last_reviewed: '2026-10-19'
  notes: Idea. Panelists describe client requests; no firm reports an implemented AI line item. Norton Rose says
    it bills for hours actually worked and passes AI time savings to the client (BLOOMBERGLAW-TEXAS-2026); that
    is a billing policy rather than an AI tool and is routed to scoping-pricing.
- id: professional-services-billing-collections-10
  title: Meter AI usage by client and matter for cost allocation and possible pass-through (idea)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Seat-based AI subscriptions give way to token-based billing, and firms realise they cannot yet attribute
    AI cost to a client; one speaker said metering makes cost attributable in a way a flat subscription cannot (TRI-ILTACON-METER-2026).
  solution: 'Idea discussed at ILTACON 2026: consumption metering creates a traceable cost line per matter, and
    the open question is whether token spend becomes a passed-through line item as e-discovery did. An opinion piece
    circulated by a state bar association argues that ordinary AI use should be absorbed as overhead and that pass-through
    suits only extraordinary single-matter consumption or client-directed tools (TRI-ILTACON-METER-2026; ISBA-ELEFANT-2026).'
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: not applicable
    provenance: self-reported
    source_ref: TRI-ILTACON-METER-2026
  prerequisites:
  - Vendor usage data tagged to matters (TRI-ILTACON-METER-2026)
  - Engagement-letter terms disclosing any separate AI charges (CALBAR-GENAI-2026, p. 8)
  risks_and_guardrails:
  - 'California guidance: general AI subscriptions are overhead; matter-specific costs may be charged only if disclosed
    in the fee agreement, at actual cost, with no markup without informed written consent (CALBAR-GENAI-2026, p.
    8)'
  - The ISBA-circulated commentary says lawyers who cannot isolate actual cost for a matter may not charge for it,
    and that traceability alone does not justify billing (ISBA-ELEFANT-2026)
  - One litigation boutique treats AI as overhead for now and says that may change (BLOOMBERGLAW-TEXAS-2026)
  human_checkpoints:
  - Billing partner approves any pass-through and its disclosure (CALBAR-GENAI-2026, p. 8)
  role_evolution: The sources do not describe role changes; at ILTACON 2026 knowledge and innovation managers were
    the ones doing the cost arithmetic (TRI-ILTACON-METER-2026).
  evidence_grade: D
  sources:
  - ref: TRI-ILTACON-METER-2026
    title: 'Ferraris for emails: At ILTACON 2026, the industry starts reading the meter'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter
    date: '2026-09-09'
    access: full
    locator: paragraphs quoting Mayo Haynes on attributable line items and the closing question on pass-through
  - ref: ISBA-ELEFANT-2026
    title: The One About Passing AI Costs Through to Clients (MyShingle Ethics Opinion, Carolyn Elefant; commentary,
      not a regulator opinion)
    publisher: Illinois State Bar Association (Rural Practice newsletter)
    type: professional-body
    url: https://www.isba.org/node/104199
    date: 2026-07
    access: full
    locator: summary of overhead versus client-expense treatment
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version)
    publisher: State Bar of California, COPRAC
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026'
    access: full
    locator: p. 8
  - ref: BLOOMBERGLAW-TEXAS-2026
    title: AI, Billing Emerge as Crossroads for Texas Law Firms and Clients
    publisher: Bloomberg Law
    type: press
    url: https://news.bloomberglaw.com/antitrust/ai-billing-emerge-as-crossroads-for-texas-law-firms-and-clients
    date: '2026-04-21'
    access: full
    locator: paragraph on AZA Law treating AI as overhead
  last_reviewed: '2026-10-19'
  notes: Idea. Shares ground with firm-finance (AI cost as a variable cost); kept here because the output is an
    invoice line. A Lawyers Weekly interview with Keypoint's CEO on clients being "annoyed" by pass-through was
    seen as a standfirst only and is not used.
- id: professional-services-billing-collections-11
  title: AI-drafted collection follow-ups and a collections agent that prioritises overdue accounts
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - transaction-processing
  - client-interaction
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: 'Collections is still manual: teams spend hours each week drafting follow-ups, deciding whom to chase
    and what tone to use (ODDR-COLLECTIONS-2026). Oddr argues that firms do not know whether a client has opened
    an invoice and rank accounts from aging reports alone (ODDR-82CENTS-2026).'
  solution: Oddr released AI-drafted collection emails with tone controls and automated follow-up sequences; a Collections
    Agent, "in development", would monitor the accounts-receivable portfolio, surface the accounts with most impact
    on cash and prepare a drafted email, call brief or note to the attorney for the collector (ODDR-COLLECTIONS-2026).
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: not applicable
    provenance: self-reported
    source_ref: ODDR-COLLECTIONS-2026
  prerequisites:
  - Billing, payment and status data in one platform; Oddr says it integrates with Elite, Aderant and Intapp (ODDR-COLLECTIONS-2026)
  risks_and_guardrails:
  - Oddr states finance teams stay in control of every decision (ODDR-COLLECTIONS-2026)
  - Sector averages in Oddr's article (firms invoice about 88% of billable work and collect about 93% of invoices;
    43 days to bill and 32 to collect) are attributed to the Clio Legal Trends Report and were not checked at source
    (ODDR-82CENTS-2026)
  human_checkpoints:
  - Oddr says finance teams stay in control of every decision, with the agent preparing the draft email, call brief
    or attorney note (ODDR-COLLECTIONS-2026)
  role_evolution: Oddr says collectors should spend less time chasing and more on relationships and judgment calls
    (ODDR-COLLECTIONS-2026).
  evidence_grade: C
  sources:
  - ref: ODDR-COLLECTIONS-2026
    title: Oddr Announces AI-Powered Collections for Law Firms. Collections Turns Agentic.
    publisher: Oddr (press release)
    type: vendor
    url: https://www.oddr.com/news/oddr-announces-ai-powered-collections-for-law-firms-collections-turns-agentic
    date: '2026-08-19'
    access: full
    locator: paragraphs on available features and the Collections Agent
  - ref: ODDR-82CENTS-2026
    title: Law Firms Collect About 82 Cents on the Dollar. The Rest Is an Architecture Problem.
    publisher: Oddr (article)
    type: vendor
    url: https://www.oddr.com/news/law-firms-collect-about-82-cents-on-the-dollar-the-rest-is-an-architecture-problem
    date: '2026-09-09'
    access: full
    locator: paragraphs on Clio-attributed figures and the three places leakage occurs
  last_reviewed: '2026-10-19'
  notes: Vendor only; email drafting is "available now", the agent was in development and due in early access before
    general availability later in the year. No customer results. Searches also surfaced Aderant's AI-assisted accounts-receivable
    offer (webinar abstract not read) and generic vendor collection blogs, none usable.
- id: professional-services-billing-collections-12
  title: 'Accounting firms: automated time capture, WIP anomaly flags and faster invoicing'
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - transaction-processing
  - data-reporting
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Time capture, work-in-progress review, billing and collections in many accounting firms still run on
    spreadsheets, email and legacy systems, and few managing partners can pull realization, write-down rate and
    bill-to-collect cycle on demand (AIWYN-2026).
  solution: Aiwyn's general manager says AI already changes the mechanics of time and billing through automated
    time capture, anomaly detection that flags WIP problems early, and predictive billing that surfaces engagement-level
    profitability. In a Blue J/CPA.com survey of tax practitioners, adopters of AI are weighing hourly billing against
    alternatives (AIWYN-2026; ACCTODAY-BLUEJ-2026).
  outcomes:
  - lever: speed
    description: Aiwyn says AI-era visibility helped one unnamed leading firm shorten the gap between finishing
      work and sending the bill; the article credits visibility of the metric, not AI
    figure: 29 to 18 days in a single month
    measures: WIP-to-invoice time at one unnamed firm, per the vendor; sample of one
    provenance: vendor-published
    source_ref: AIWYN-2026
  prerequisites:
  - Realization, write-down rate, bill-to-collect cycle and WIP-to-invoice time defined and visible by partner and
    service line (AIWYN-2026)
  risks_and_guardrails:
  - The article warns that AI efficiency will not fix an opaque billing process and may speed up client confusion
    (AIWYN-2026)
  - Hourly billing is deeply entrenched; changing it is a major change-management task (ACCTODAY-BLUEJ-2026)
  human_checkpoints:
  - Partners review WIP and approve invoices (AIWYN-2026)
  role_evolution: Firms are asked to decide where people should spend time that AI frees (AIWYN-2026); in the Blue
    J/CPA.com poll of tax practitioners, 28% said they plan to keep hourly billing but increase realization (ACCTODAY-BLUEJ-2026).
  evidence_grade: C
  sources:
  - ref: AIWYN-2026
    title: 'Time & Billing for Accounting Firms: What AI Is About to Change (The dirty secret about time billing
      and what AI is about to expose)'
    publisher: Aiwyn (article by its general manager of experience)
    type: vendor
    url: https://www.aiwyn.ai/resources/articles/the-dirty-secret-about-time-billing-and-what-ai-is-about-to-expose/
    date: '2026-04-27'
    access: full
    locator: sections on five metrics, WIP-to-invoice time and what AI is changing
  - ref: ACCTODAY-BLUEJ-2026
    title: Tax research AI usage doubles, more considering alternative billing models
    publisher: Accounting Today
    type: press
    url: https://www.accountingtoday.com/news/tax-research-ai-usage-doubles-more-considering-alternative-billing-models
    date: '2026-06-09'
    access: full
    locator: paragraphs on 69% considering alternatives and 28% keeping hourly with higher realization
  - ref: JOFA-CAS-2026
    title: Simple but effective AI use cases for CAS
    publisher: Journal of Accountancy (AICPA)
    type: professional-body
    url: https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/
    date: 2026-01
    access: full
    locator: section on lowering error rates and rework (fewer mistakes mean fewer write-offs)
  - ref: KARBON-ENGAGE-2026
    title: 23 must-see sessions at AICPA & CIMA ENGAGE 2026 (session preview)
    publisher: Karbon Magazine
    type: conference
    url: https://karbonhq.com/resources/aicpa-cima-engage-2026/
    date: '2026-05-21'
    access: full
    locator: 'session list: no billing or collections session among the 23 previewed'
  last_reviewed: '2026-10-19'
  notes: 'Accounting billing evidence is thin: one vendor article, a survey of tax practitioners about billing models
    (scoping-pricing territory), and a generic Journal of Accountancy piece. The 29-to-18-day figure is one unnamed
    firm and is attributed by the vendor to visibility rather than to AI, so it is not treated as evidence for the
    use case. The Blue J/CPA.com survey sample size and denominators for 69% and 28% were not stated in the article.'
- id: professional-services-billing-collections-13
  title: 'Consulting and services firms: agents that take over timesheet and delivery admin'
  archetype: professional-services
  module: billing-collections
  function: service-delivery
  work_types:
  - transaction-processing
  - coordination-scheduling
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: Professional services staff spend time on documentation, resourcing and entering billable time that they
    would rather spend with customers (ITBRIEF-KANTATA-2026).
  solution: Kantata's Agent Studio lets practice leads and PMO owners describe in plain language the work an agent
    should do, with validation checks before publishing; Basware, a vendor of invoice lifecycle management software,
    is named as using it to reduce administration and internal process work. Certinia's chief product officer says
    its Veda agents apply determinism to policies such as how a timecard should look (ITBRIEF-KANTATA-2026; SILICONANGLE-CERTINIA-2026).
  outcomes:
  - lever: capacity
    description: none published
    figure: none published
    measures: not applicable
    provenance: self-reported
    source_ref: ITBRIEF-KANTATA-2026
  prerequisites:
  - Delivery standards written down so an agent can follow them (ITBRIEF-KANTATA-2026)
  - A system of record holding project, time and financial data (SILICONANGLE-CERTINIA-2026)
  risks_and_guardrails:
  - The Basware quote is a statement of intent about billable-time entry, not a reported result (ITBRIEF-KANTATA-2026)
  - Certinia says models are probabilistic and needs a reasoning layer for determinism (SILICONANGLE-CERTINIA-2026)
  human_checkpoints:
  - A person triggers each agent or an automated workflow does (ITBRIEF-KANTATA-2026)
  role_evolution: Kantata says its aim is firms that compound expertise, not just cut cost (ITBRIEF-KANTATA-2026).
  evidence_grade: C
  sources:
  - ref: ITBRIEF-KANTATA-2026
    title: Kantata launches Agent Studio for professional services
    publisher: IT Brief UK
    type: press
    url: https://itbrief.co.uk/story/kantata-launches-agent-studio-for-professional-services-6f2e3b71-a9d6-4b5d-9ddb-8be3ee77fe5a
    date: '2026-10-07'
    access: full
    locator: paragraphs on Agent Studio, Basware and the quote on billable time
  - ref: SILICONANGLE-CERTINIA-2026
    title: Certinia powers professional services with AI (interview with Certinia's chief product and technology
      officer)
    publisher: SiliconANGLE
    type: press
    url: https://siliconangle.com/2026/04/16/professional-services-ai-certinia/
    date: '2026-04-16'
    access: full
    locator: passage on timecard policies and the reasoning layer
  last_reviewed: '2026-10-19'
  notes: 'Weakest case: consulting-specific billing practice (invoice generation from milestones, T&M versus outcome
    billing, revenue recognition) was not found in public discourse. Certinia says Veda agents could save a project
    manager up to 20 hours a month (SILICONANGLE-CERTINIA-2026), which is not billing-specific.'
```

## 3. Module notes

### Processes and key steps (with work types)

1. **Time capture and entry** (transaction-processing). Moves from recollection at day's end to passive capture and drafts reviewed by the timekeeper (use cases 1-2; LEGORA-LAUREL-2026, para 2).
2. **Narrative drafting and client-guideline compliance** (document-production, review-assurance). Narratives are rewritten to meet each client's billing rules, now checked in bulk by Linklaters' tool and promised by billing vendors (use cases 3-4; NONBILLABLE-LINKLATERS-2025; ELITE-REJECT-2026).
3. **Work-in-progress and pre-bill review** (expert-judgment, review-assurance). The partner reviewing the pre-bill often adjusts it downward, usually because the fees feel too high for the client (TRI-ROI-2025, write-down explanation).
4. **Invoice generation and e-billing submission** (transaction-processing). Rate deviation, vague descriptions and excessive time are the leading reasons for fee reductions in Elite's data (ELITE-IDEA-2026, fee-reduction section).
5. **Client-side invoice review, reductions, rejections and appeals** (review-assurance, reconcile-exceptions). Clients and insurers use departments, vendors and now AI to review and cut bills; firms staff payment and appeals teams in response (TRI-KOPKA-2026, section on administrative overhead; use case 5). In-house legal operations owns the client side.
6. **Collections and accounts receivable** (transaction-processing, client-interaction). Follow-up drafting, prioritisation and payment status (use case 11).
7. **Realization, leakage and profitability reporting** (data-reporting). Scope-overage alerts, write-down analysis and spend analytics (use cases 6-8).
8. **AI-specific billing decisions** (expert-judgment): whether to show clients AI use and savings, and whether AI cost is overhead or an expense (use cases 9-10).

### Common pain points

- Time is reconstructed from memory, so short tasks are missed and narratives are approximate (LEGORA-LAUREL-2026, para 2).
- Time capture is tedious enough that a defense-firm COO links it to talent leaving the defense side (TRI-KOPKA-2026).
- Partners write down time before the client sees it; in TRI's 2023 survey 43% of partners reported reducing a bill because the time spent exceeded their own expectations, and 46% reduced by a dollar amount rather than a percentage (TRI-WRITEDOWNS-2023, pp. 2-3).
- Client AI review rejects invoices faster than manual compliance can respond (ELITE-REJECT-2026).
- Firms cannot show clients the savings they ask for. At Legalweek 2026 firm speakers said they were "still gathering the data" and described ROI measurement as anecdotal (TRI-LEGALWEEK-2026).
- Billing and collections run on separate tools, so no one sees where a dollar is (ODDR-82CENTS-2026).
- Efficiency is penalised by the hour: a defense firm argues the billable hour punishes a firm that finishes sooner (TRI-KOPKA-2026), and an in-house columnist says firms are banking AI gains as margin (BLOOMBERGLAW-GCXAI-2026).

### Metrics and benchmarks (with provenance)

- **Invoice rejection rate** rose from 11% to 18% in 2025 across Elite's billing data for about 400 firms, roughly half the Am Law 200; the release does not define numerator and denominator. Vendor-published (ELITE-REJECT-2026).
- **Days to payment** for Elite eBillingHub customers fell from 62 to 50 in 2025; 71% of firms in the study manage OCG compliance mainly by hand; 48% of Global 200 CFOs call e-billing their most significant revenue-cycle challenge. Vendor-published (ELITE-REJECT-2026).
- **Fee-reduction categories** in the same data: rate deviation or unapproved rate 23.88%, vague description or entry quality 7.57%, excessive or unsupported time 7.33% (shares of fee reductions; count or value not stated). Vendor-published (ELITE-IDEA-2026).
- **Collection realization against standard rates** was 84.5% in Q4 2021 and 81.9% in Q2 2024; in Q1 2024 firms collected 89.6% of worked fees. TRI survey data, older than the window (TRI-RATES-2024). TRI later reported a slow decline in the percentage of standard rates actually collected since 2021, with an unseasonal dip in Q2 2025 (TRI-PROSPERITY-2025; figure not given).
- **Market-standard realization** is about 85% in a TRI commentary, with more than 90% of legal fees still billed by the hour (TRI-MIDSIZE-2026; source of the 85% not stated).
- **Partner write-offs**: over 300 hours of their own time after it had been reported, nearly $190,000 of fees, in a 2023 TRI survey of 245 respondents (TRI-WRITEDOWNS-2023, p. 12). 94% of partners named hourly billing their primary model (TRI-WRITEDOWNS-2023, p. 2).
- **Unrecorded time** (vendor sizing, not comparable): about 11% of unsubmitted time should have been billed (LAUREL-SOW-2025); 10-30% of billable work never reaches an invoice (TR-LAUREL-2026); up to 30% unrecorded in many firms (LITIFY-LAWSITES-2026).
- **AI visibility and measurement**: 68% of corporate legal professionals did not know whether outside firms use AI; 85% of law-firm and 75% of corporate-department respondents were not collecting AI ROI data or were unsure (TRI-GREATDISCONNECT-2026). Firms with a GenAI strategy were 3.9 times more likely to achieve ROI, and 22% of firms had one, as presented by a Thomson Reuters speaker (TRI-LEGALWEEK-2026).
- **Sector cycle times** attributed by Oddr to the Clio Legal Trends Report: 88% of billable work invoiced, 93% of invoices collected, 43 days to bill and 32 to collect. Second-hand; not checked at source (ODDR-82CENTS-2026).
- **Quality evidence**: only vendor accuracy claims (Onit: 92% invoice-level and 81% line-item accuracy against 72% and 43% for experienced lawyers, ONIT-SPEND-2026). No independent error, override or parallel-run data on AI time capture, narrative drafting or invoice review was found.

### Guardrails and regulatory points

- California (2026): lawyers may charge for actual time spent crafting prompts and reviewing outputs; hourly billing must reflect time actually spent; flat fees may build in AI time savings; general AI subscriptions are overhead; matter-specific AI costs may be charged only if the fee agreement discloses it, at reasonable actual cost, with no markup without informed written consent (CALBAR-GENAI-2026, p. 8).
- Texas, as reported by Bloomberg Law: the ethics committee said lawyers cannot charge for time saved by generative AI, but gave little guidance on accounting for AI on bills; the ABA is reported to say fees should be reasonable and consistent with time saved (BLOOMBERGLAW-TEXAS-2026; BLOOMBERGLAW-CORP-2026). The Texas opinion and ABA Formal Opinion 512 were not read directly.
- Commentary circulated by an Illinois bar newsletter argues that ordinary AI cost should be absorbed as overhead and that only extraordinary or client-directed use should be passed through (ISBA-ELEFANT-2026). This is commentary, not a regulator opinion.
- Client contracts: some clients issue guidelines that they will not pay for work done by AI, while others ask for line-item AI transparency (TRI-LEGALWEEK-2026).
- Capture tools handle privileged communications; Laurel names SOC 2 Type II as the minimum and ISO 42001 as increasingly relevant (LAUREL-TIMESHEETS-2026).

### Frontier signals (dated)

- 2026-10-13: Legora and Laurel announce automatic time entries for work done in Legora, with a second phase to measure AI value (LEGORA-LAUREL-2026; LAWSITES-LAUREL-2026).
- 2026-10-07: Kantata launches Agent Studio, naming Basware as a user for administration such as billable-time entry (ITBRIEF-KANTATA-2026).
- 2026-09-28: Berger Singerman story reports a firmwide Laurel rollout integrated with Aderant billing (LAUREL-BERGER-2026).
- 2026-09-23: Laurel's first conference, "Proof", in New York; the agenda lists partners from PwC Australia and EY on panels. No recap was found (LAUREL-PROOF-2026).
- 2026-09-09: ILTACON 2026 practitioners "read the meter": per-token metering raises the question of AI cost as a billed line (TRI-ILTACON-METER-2026).
- 2026-08-19: Oddr announces AI collection emails and says a Collections Agent is in development (ODDR-COLLECTIONS-2026).
- 2026-08-17: Aderant says work in Harvey now becomes draft iTimekeep entries for firms using both (ADERANT-HARVEY-2026).
- 2026-05-14 and 2026-06-15: Elite reports the rise in rejections and says client AI now reviews every invoice (ELITE-REJECT-2026; ELITE-IDEA-2026).
- 2026-03-13: Legalweek panels centre on AI line items, "will not pay" guidelines and a possible return to single line-item bills (TRI-LEGALWEEK-2026).
- Scheduled, not yet held: the TRI Law Firm COO & CFO Forum on 21-22 Oct 2026 (named in the landscape file); nothing from it is used here.

### Workforce and role effects

- Timekeepers shift from recording to reviewing drafts (LEGORA-LAUREL-2026). PAs, secretaries and professional staff are named as beneficiaries of narrative and time-entry automation (NONBILLABLE-LINKLATERS-2025; LAUREL-BERGER-2026).
- Elite says billing teams should move from correcting rejected invoices to preventing rejections (ELITE-REJECT-2026). Oddr says collectors should concentrate on relationship and judgment calls (ODDR-COLLECTIONS-2026).
- A pricing role is emerging at the interface: Greenberg Traurig has a chief pricing and innovation officer and DLA Piper a head of AI innovation, both speaking about client AI-billing conversations (TRI-LEGALWEEK-2026).
- Associate training and the pyramid are discussed in the same Legalweek coverage and belong to talent-learning (TRI-LEGALWEEK-CRISIS-2026).
- No source reports headcount cuts in billing or collections teams.

### Objections and concerns practitioners raise

- Clients suspect firms will bill hypothetical time: "It's dishonest, but so are many firms" (in-house CLO, TRI-GREATDISCONNECT-2026).
- The billable hour is durable: a Saul Ewing partner said his firm sees no meaningful client-driven move to alternative fee arrangements (TRI-LEGALWEEK-CRISIS-2026); an in-house columnist notes rates rose and firms are banking gains as margin (BLOOMBERGLAW-GCXAI-2026).
- Disclosure may invite fee cuts, since some clients use AI adoption as leverage to reduce fees (TRI-LEGALWEEK-2026).
- Token costs are variable and could become a billed line item clients object to (TRI-ILTACON-METER-2026).
- Opaque client AI review: firms often do not know why an invoice was cut (ELITE-IDEA-2026).
- Vendor claims are large and do not agree with each other (see use case 1 notes).
- Passive capture raises monitoring and privacy questions; vendor materials respond with pause functions and security attestations (LAWSITES-AJAX-2025; LAUREL-TIMESHEETS-2026). No practitioner-voiced objection from a firm was found in the sources read.

### Interview probes for an advisor

1. Take the last invoice that was cut or rejected. Who found the problem, how long after the work was done, and what did it cost in write-down and delay?
2. How much time goes unrecorded or rewritten today, and how do you know? Is anyone measuring edits to entries before and after any capture tool?
3. For each large client, what do the billing guidelines say about AI, and what share of your invoices go through client-side automated review?
4. When AI shortens a task, what does the invoice show and who decides? Is AI cost overhead, an expense, or neither under your engagement letters and the rules of your jurisdiction?
5. Where does your collections team lose time (chasing, prioritising, finding why a payment is stuck), and what would you need to see to trust a drafted follow-up?

## 4. Routed to other modules

- **firm-finance:** AI-value measurement in phase two of Legora-Laurel and Laurel Signal (LEGORA-LAUREL-2026; TR-LAUREL-2026); realization and rate trends (TRI-RATES-2024; TRI-PROSPERITY-2025; TRI-COOCFO-MARKET-2025); firms banking AI gains as margin (BLOOMBERGLAW-GCXAI-2026); AI cost as a variable cost (TRI-ILTACON-METER-2026).
- **scoping-pricing:** Kopka Law's KPI-based monthly or portfolio billing in place of hourly entries (TRI-KOPKA-2026); the Zarwin Baum suggestion of a return to a single services-rendered line item (TRI-LEGALWEEK-2026); Norton Rose's policy of billing hours actually worked and passing savings to clients, and its view of fixed fees as a "win-win" (BLOOMBERGLAW-TEXAS-2026); billing-model choices among tax practitioners (ACCTODAY-BLUEJ-2026); fixed-fee entry points for midsize firms (TRI-MIDSIZE-2026); the ILTACON 2025 debate on AFAs and the billable hour (TRI-ILTACON-HOUR-2025).
- **client-development:** Advice to lead the client AI-ROI conversation (TRI-LEGALWEEK-2026; TRI-GREATDISCONNECT-2026).
- **talent-learning:** Associate training in the AI era and the pyramid (TRI-LEGALWEEK-CRISIS-2026); talent leaving defense work because of time capture (TRI-KOPKA-2026).
- **delivery-management:** Kantata and Certinia agents for resourcing, status and project administration (ITBRIEF-KANTATA-2026; SILICONANGLE-CERTINIA-2026).
- **quality-review:** Verification burden as the determinant of AI return (TRI-MIDSIZE-2026).
- **In-house tag (legal operations, shared service):** client-side invoice review and spend analytics (use cases 5-6); GSK's and other clients' savings demands (TRI-LEGALWEEK-2026); the corporate view of AI savings (BLOOMBERGLAW-CORP-2026).

## 5. Sources

Format: ref | title | publisher | type | URL | date | access. Dates come from article metadata, bylines or page JSON where found; year-only dates mean no date was shown. Foundation items older than 18 months are labelled in the title.

- `KARBON-ENGAGE-2026` | 23 must-see sessions at AICPA & CIMA ENGAGE 2026 (session preview) | Karbon Magazine | conference | https://karbonhq.com/resources/aicpa-cima-engage-2026/ | 2026-05-21 | access: full
- `LAUREL-PROOF-2026` | Proof: Laurel's event for professional services firms (agenda page for the 23 Sep 2026 event; no recap found) | Laurel | conference | https://www.laurel.ai/proof | 2026-09-23 | access: full
- `TRI-COOCFO-MARKET-2025` | Law Firm COO & CFO Forum: As legal market shifts, the big questions still need answers | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/coo-cfo-forum-shifting-legal-market | 2025-10-24 | access: full
- `TRI-ILTACON-HOUR-2025` | ILTACON 2025: Pricing the future - AI's impact on the billable hour | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2025-billable-hour | 2025-09-02 | access: full
- `TRI-ILTACON-METER-2026` | Ferraris for emails: At ILTACON 2026, the industry starts reading the meter | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/iltacon-2026-reading-the-meter | 2026-09-09 | access: full
- `TRI-LEGALWEEK-2026` | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | access: full
- `TRI-LEGALWEEK-CRISIS-2026` | Move over, "Death of the billable hour," Legalweek 2026 has found a new existential crisis | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-new-existential-crisis | 2026-03-19 | access: full
- `REINVENTING-KAPLAN-2025` | How Law Firms Can Use AI to Capture More Time (Reinventing Professionals; show notes only) | Reinventing Professionals (Ari Kaplan) | podcast | https://reinventingprofessionals.podbean.com/e/how-law-firms-can-use-ai-to-capture-more-time | 2025-02-12 | access: full
- `ACCTODAY-BLUEJ-2026` | Tax research AI usage doubles, more considering alternative billing models | Accounting Today | press | https://www.accountingtoday.com/news/tax-research-ai-usage-doubles-more-considering-alternative-billing-models | 2026-06-09 | access: full
- `BLOOMBERGLAW-CORP-2026` | Corporate Teams Expect an Edge Over Law Firms on AI Savings | Bloomberg Law | press | https://news.bloomberglaw.com/business-and-practice/corporate-teams-expect-an-edge-over-law-firms-on-ai-savings | 2026-03-23 | access: full
- `BLOOMBERGLAW-GCXAI-2026` | GC x AI Retrospective: The Billable Hour, Like a Twinkie, Endures (column by an in-house counsel) | Bloomberg Law | press | https://news.bloomberglaw.com/business-and-practice/gc-x-ai-retrospective-the-billable-hour-like-a-twinkie-endures | 2026-10-19 | access: full
- `BLOOMBERGLAW-TEXAS-2026` | AI, Billing Emerge as Crossroads for Texas Law Firms and Clients | Bloomberg Law | press | https://news.bloomberglaw.com/antitrust/ai-billing-emerge-as-crossroads-for-texas-law-firms-and-clients | 2026-04-21 | access: full
- `ITBRIEF-ELITE-2026` | AI invoice checks drive law firms' rejection rates up | IT Brief Australia | press | https://itbrief.com.au/story/ai-invoice-checks-drive-law-firms-rejection-rates-up | 2026-05-20 | access: full
- `ITBRIEF-KANTATA-2026` | Kantata launches Agent Studio for professional services | IT Brief UK | press | https://itbrief.co.uk/story/kantata-launches-agent-studio-for-professional-services-6f2e3b71-a9d6-4b5d-9ddb-8be3ee77fe5a | 2026-10-07 | access: full
- `LAWSITES-AJAX-2025` | The Smart Screen Reader: How Ajax Is Automating Legal Timekeeping with AI-Powered Activity Tracking | LawSites (Bob Ambrogi) | press | https://www.lawnext.com/2025/09/the-smart-screen-reader-how-ajax-is-automating-legal-timekeeping-with-ai-powered-activity-tracking.html | 2025-09-09 | access: full
- `LAWSITES-LAUREL-2026` | Legora and Laurel Partner to Enable Automatic Time Capture; Will Later Develop Measures of Legora's Value to Firms | LawSites (Bob Ambrogi) | press | https://www.lawnext.com/2026/10/legora-and-laurel-partner-to-enable-automatic-time-capture-will-later-develop-measures-of-legoras-value-to-firms.html | 2026-10-13 | access: full
- `NONBILLABLE-LINKLATERS-2025` | Linklaters' new AI time recording tool started as one associate's side project (interview with James Phoenix) | Non-Billable | press | https://www.nonbillable.co.uk/news/linklaters-ai-time-recording-tool-associate-side-project | 2025-10-09 | access: full
- `SILICONANGLE-CERTINIA-2026` | Certinia powers professional services with AI (interview with Certinia's chief product and technology officer) | SiliconANGLE | press | https://siliconangle.com/2026/04/16/professional-services-ai-certinia/ | 2026-04-16 | access: full
- `TRI-AIBOL-2025` | How AI is continuing to change the business of law | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en-us/posts/legal/ai-business-of-law/ | 2025-08-20 | access: full
- `TRI-AIEFF-2025` | The AI-driven future of legal efficiency: How can law firms reclaim millions in lost revenue while enhancing client value? (white paper summary) | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en-us/posts/legal/ai-driven-legal-efficiency-white-paper-2025/ | 2025-04-14 | access: full
- `TRI-KOPKA-2026` | How one law firm is challenging a broken status quo around billing | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing | 2026-04-30 | access: full
- `TRI-MIDSIZE-2026` | AI execution for midsize law firms: Why the most obvious AI use case is often the wrong one | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/spotlight/midsize-firms-obvious-ai-use-cases | 2026-07-23 | access: full
- `TRI-ROI-2025` | Finding a quicker ROI on law firms' investment in AI | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/law-firm-roi-ai-investment | 2025-05-19 | access: full
- `TRI-GREATDISCONNECT-2026` | The great AI disconnect: Firms and legal departments are not communicating about AI usage | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/great-ai-disconnect | 2026-03-18 | access: full
- `TRI-PROSPERITY-2025` | The prosperity paradox: Record rate growth may mask rising vulnerabilities in law firms | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/law-firms-prosperity-paradox | 2025-12-10 | access: full
- `TRI-RATES-2024` | Law Firm Rates in 2024: The Bull, Bear & Base Case for rates and what it means for realization (foundation, outside the 18-month window) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/law-firm-rates-bull-bear-base-case | 2024-10-17 | access: full
- `TRI-WRITEDOWNS-2023` | Law Firm Billing Efficiency and Write Downs (report; foundation, outside the 18-month window) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2024/04/Law-Firm-Billing-Write-Downs-2023-1.pdf | 2023 | access: full
- `CALBAR-GENAI-2026` | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 version) | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026 | access: full
- `ALA-TIMEAI-2026` | Time-Tracking in the AI Era (webcast abstract, 3 Feb 2026; speaker from Billables AI) | ALA Legal Marketplace (Webvent) | professional-body | https://solution-series.alanet.org/webinar/5775 | 2026-02-03 | access: full
- `ISBA-ELEFANT-2026` | The One About Passing AI Costs Through to Clients (MyShingle Ethics Opinion, Carolyn Elefant; commentary, not a regulator opinion) | Illinois State Bar Association (Rural Practice newsletter) | professional-body | https://www.isba.org/node/104199 | 2026-07 | access: full
- `JOFA-CAS-2026` | Simple but effective AI use cases for CAS | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/jan/simple-but-effective-ai-use-cases-for-cas/ | 2026-01 | access: full
- `ADERANT-HARVEY-2026` | Aderant Launches iTimekeep Integration with Harvey, Turning AI-Powered Legal Work into Billable Time | Aderant (press release) | vendor | https://www.aderant.com/news-pr/aderant-launches-itimekeep-integration-with-harvey/ | 2026-08-17 | access: full
- `AIWYN-2026` | Time & Billing for Accounting Firms: What AI Is About to Change (The dirty secret about time billing and what AI is about to expose) | Aiwyn (article by its general manager of experience) | vendor | https://www.aiwyn.ai/resources/articles/the-dirty-secret-about-time-billing-and-what-ai-is-about-to-expose/ | 2026-04-27 | access: full
- `ELITE-IDEA-2026` | Your Clients' AI Is Reviewing Every Invoice. Does Your Firm Know What It's Looking For? | Elite (blog) | vendor | https://www.elite.com/insights/ideas/clients-ai-is-reviewing-every-invoice | 2026-06-15 | access: full
- `ELITE-REJECT-2026` | New Elite Research: Law Firms See 64% Climb in Rejection Rates as Client AI Billing Scrutiny Advances | Elite (press release) | vendor | https://www.elite.com/insights/news/new-elite-research-law-firms-see-64-climb-in-rejection-rates-as-client-ai-billing-scrutiny-advances | 2026-05-14 | access: full
- `FULCRUM-ILTACON-2026` | ILTACON 2026 (Fulcrum GT event page; product descriptions, no session content; page date not shown) | Fulcrum GT | vendor | https://iltacon.fulcrumgt.com/ | 2026 | access: full
- `LAUREL-BERGER-2026` | Berger Singerman and Laurel: A practical approach to AI adoption | Laurel (customer story) | vendor | https://www.laurel.ai/press/berger-singermanand-laurel-a-practical-approach-to-ai-adoption | 2026-09-28 | access: full
- `LAUREL-FOSTERS-2026` | Fosters Solicitors selects Laurel as its AI time platform | Laurel (press release; date from page metadata, shared by several Laurel releases) | vendor | https://www.laurel.ai/press/fosters-solicitors-selects-laurel-as-its-ai-time-platform | 2026-08-19 | access: full
- `LAUREL-SOW-2025` | The State of Work 2025 (report landing page; no publication date shown) | Laurel | vendor | https://www.laurel.ai/state-of-work-2025 | 2025 | access: full
- `LAUREL-TIMESHEETS-2026` | Automated timesheets for law firms: A complete 2026 guide | Laurel | vendor | https://www.laurel.ai/blog/automated-timesheets-law-firms | 2026-09-17 | access: full
- `LEGORA-LAUREL-2026` | Legora and Laurel partner to capture the time lawyers spend in Legora as they work | Legora (press release) | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 | access: full
- `LITIFY-LAWSITES-2026` | Litify Launches AI-Powered Time Capture with Billables AI to Recover Lost Time (press release carried by LawSites) | Litify and Billables AI (via LawSites) | vendor | https://www.lawnext.com/2026/05/litify-launches-ai-powered-time-capture-with-billables-ai-to-recover-lost-time.html | 2026-05-19 | access: full
- `MILLIMAN-BILLREVIEW-2026` | Legal bill review: AI vs manual invoice audit (insight page; no publication date shown) | Milliman | vendor | https://ae.milliman.com/en/insight/legal-bill-review-ai-manual-invoice-audit | 2026 | access: full
- `ODDR-82CENTS-2026` | Law Firms Collect About 82 Cents on the Dollar. The Rest Is an Architecture Problem. | Oddr (article) | vendor | https://www.oddr.com/news/law-firms-collect-about-82-cents-on-the-dollar-the-rest-is-an-architecture-problem | 2026-09-09 | access: full
- `ODDR-COLLECTIONS-2026` | Oddr Announces AI-Powered Collections for Law Firms. Collections Turns Agentic. | Oddr (press release) | vendor | https://www.oddr.com/news/oddr-announces-ai-powered-collections-for-law-firms-collections-turns-agentic | 2026-08-19 | access: full
- `ONIT-SPEND-2026` | Spend Agent: AI-Powered Invoice Review for Legal Teams (product page; no publication date shown) | Onit | vendor | https://www.onit.com/?p=18328 | 2026 | access: full
- `QUERIOUS-LAWSITES-2025` | Querious Joins Clio's App Directory to Help Law Firms Capture More Billable Time with AI (press release carried by LawSites) | Querious (via LawSites) | vendor | https://www.lawnext.com/2025/08/querious-joins-clios-app-directory-to-help-law-firms-capture-more-billable-time-with-ai.html | 2025-08-27 | access: full
- `TR-LAUREL-2026` | Thomson Reuters and Laurel connect legal AI to ROI | Thomson Reuters (legal blog) | vendor | https://legal.thomsonreuters.com/blog/thomson-reuters-and-laurel-help-law-firms-connect-legal-ai-to-business-outcomes/ | 2026-08-05 | access: full
- `WK-LEGALSPEND-2026` | AI in legal spend management: A CFO's guide | Wolters Kluwer (expert insights) | vendor | https://www.wolterskluwer.com/en/expert-insights/ai-in-legal-spend-management-a-cfos-guide | 2026-02-03 | access: full

Count by type (distinct sources listed): conference 7, podcast 1, press 15, survey 4, regulator 1, professional-body 3, vendor 18; total 49.

## 6. Gaps

- **No grade A evidence.** No named firm publishes a measured, outcome-level result for AI time capture, narrative checking, invoice validation or collections. The two best-evidenced use cases (1 and 3) rest on a vendor customer story and a builder's interview.
- **No independent quality evidence.** No error rates, edit or override rates, parallel runs or inspection findings were found for AI-drafted narratives, passive capture or client-side invoice review. The only accuracy figure is a vendor's (ONIT-SPEND-2026), and the only measured series (Elite rejections) is vendor data that describes the problem.
- **Not reached or not read:** Reddit (403), Hacker News search, LinkedIn and ALA or ACC community forums, so no community discussion is included; a metacast page for The 80/20 Principle episode 301 on AI timekeeping (CAPTCHA); Wolters Kluwer's Buying Legal NYC 2026 recap (blocked); Brightflag's 2026 benchmarking report (gated landing page); the Elite report itself (press release and two Elite blogs read instead); the Clio Legal Trends figures (second-hand through Oddr); Aderant's accounts-receivable webinar page and Intapp Time product detail (navigation text only); ABA Formal Opinion 512 and the Texas ethics opinion (reported by Bloomberg Law only).
- **Podcasts:** only show notes read (Reinventing Professionals, February 2025, outside the window); no billing-specific 2026 podcast was opened.
- **Conferences:** no CLOC Global Institute 2026 billing session content, Legal Geek, MCA, PMI or ENGAGE billing session was found (the ENGAGE preview lists no billing or collections session); the Laurel Proof agenda has no recap; ILTACON session recordings are members-only.
- **Search-only items, not used for any grade or outcome:** Epiq managed invoice review (said to deliver an average 6% savings on hourly bills), LexisNexis CounselLink SmartReview, CounselAudit.ai, HighRadius (30% reduction in past-due receivables), a Lawyers Weekly interview with Keypoint's CEO on AI pass-through, and a vendor-cited figure that 92% of firms mandate human review of AI work.
- **Accounting and consulting are thin.** Accounting billing evidence is one vendor article and a tax-practitioner survey; consulting-specific billing (invoice generation from milestones, T&M versus outcome billing) was not found.
- **Elite and Thomson Reuters.** Oddr's article calls the Elite report "Thomson Reuters Elite research" (ODDR-82CENTS-2026); TRI panels at Legalweek were Thomson Reuters-sponsored (TRI-LEGALWEEK-2026). Much of the discourse here therefore comes from vendors or vendor-adjacent publishers.
- **Searches used:** 13 of the rationed web searches (time-entry narratives; AI invoice review; TRI time capture; ILTACON billing; timekeeping podcasts; accounting WIP; Elite rejections; legal-ops invoice review podcasts; PSA invoicing; accounting trade press; UK time recording; collections; CLOC 2026). Everything else came from curl and the r.jina.ai mirror (which later refused requests).
