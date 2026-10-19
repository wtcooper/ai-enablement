# Billing and collections: governance and evidence (professional services)

Archetype: professional-services. Module: billing-collections (time capture to cash: time entry and capture, invoicing, billing guidelines and e-billing, write-downs, realization, collections). Angle: governance (what constrains and measures the work). Prepared 2026-10-19. Public sources only. Method: curl, pdftotext and a text mirror for pages that blocked curl; eleven web searches. Quotations are under 25 words. Items marked in-house are client-side or legal-department examples.

## 1. Summary

- **What the evidence is.** 50 sources were opened and read, plus 1 seen only in a search result (list in section 5; types: 11 vendor, 9 regulator, 9 press, 7 survey, 6 professional-body, 3 conference, 3 academic, 2 standard-setter, 1 firm). The 12 use cases split as 0 grade A, 1 grade B, 7 grade C, 4 grade D. There is no grade A: every outcome figure for AI time capture, billing review or collections is published by the vendor. No error rate, override rate, parallel run or inspection finding for AI-drafted time entries, bill review or collection agents was found.
- **Hourly billing is bound to actual time, and every bar text read says so.** California, Texas, DC, North Carolina and the Australian regulators' joint statement all say billed time must reflect time actually spent, so time saved by AI cannot be billed under an hourly arrangement (CALBAR-GENAI-2026; TXETHICS-OP705-2025; DCBAR-OP388-2024; NCBAR-FEO1-2024; AUSLEG-AISTATEMENT-2024). ABA Formal Opinion 512 says the same, as quoted (TRI-ABA512-2025). Vendor material for time capture frames the gain as recovering time that went unrecorded, not as adding time (LEGORA-LAUREL-2026).
- **Regulators split on fixed fees.** ABA 512, as quoted, says the same flat fee may be unreasonable if a tool makes the work much quicker; Virginia's LEO 1901 (approved 24 Nov 2025) disagrees; California says flat fees may build in AI savings (TRI-ABA512-2025; VACOURTS-LEO1901-2025; CALBAR-GENAI-2026). Billing staff need the rule of the lawyer's state before an AI-assisted flat fee is invoiced.
- **Client terms move faster than bar rules.** Zscaler's published guidelines tell firms to note generative AI use in the time entry, not to pass on AI time and cost, and apply fixed reductions for block billing and late invoices (ZSCALER-OCG-2025). At Legalweek 2026 clients asked for line-item AI transparency while others refused to pay for AI-done work (TRI-LEGALWEEK-2026). Gartner's Weston Wicks said more companies are asking in their outside counsel guidelines for lower-risk tasks to be done by AI and for the time saved to be reflected in billable hours (BLOOMBERGLAW-ACC-2025).
- **Time capture is the best-evidenced AI use here; the evidence is vendor-sourced.** Laurel customer stories report extra captured time, faster collection cycles and, at one firm, zero billing disputes (LAUREL-TONKON-2026; LAUREL-LERNERS-2026). Governance questions that the stories do not answer: whether captured activity equals time actually spent, and how worker-monitoring and AI Act rules apply (ICO-MONITORING-2026; EU-AIACT-ANNEX3-2024).
- **The cash end is weakly evidenced.** Wells Fargo data for H1 2026, as reported secondhand, show inventories up 17.7% and collection cycles slowing by 5% (LAWFUEL-WF-2026). The only collections-automation evidence is a startup pitch (ABAJ-TECHSHOW-2026).
- **Standards and regulators are silent or unreachable in places.** The LEDES and UTBMS code-set index lists no AI-specific code set (LEDES-UTBMS-2026); SRA, ABA 512 and DCAA pages could not be opened; the Law Society of England and Wales page says the SRA has no specific generative AI guidance on client care (LAWSOC-GENAI-2026).

## 2. Use cases

```yaml
- id: professional-services-billing-collections-01
  title: Automatic time capture from email, documents, calls and applications, drafted as time entries for the timekeeper to review and release
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
  problem: Time is often written from memory at the end of a day or week. Short tasks are missed, lawyers spend unbillable time on timesheets, and entries are hard to defend when a client challenges them (LEGORA-LAUREL-2026; LAUREL-LERNERS-2026). At Warren Averett, an accounting firm, professionals had to submit daily time by 9:00 a.m., which meant reconstructing the previous day from memory (LAUREL-WARRENAVERETT-2026).
  solution: 'A capture layer records work across the tools people already use, maps it to client and matter, drafts a narrative and queues entries on a timeline. The timekeeper reviews, groups, edits and releases the entries (LAUREL-TONKON-2026: partner describes going back to ''review the entries, group them, and assign them to the right client matter''; LAUREL-LERNERS-2026: partner ''reviews and finalizes'' dockets at day end). Product names are from the sources: Laurel, integrated with Elite 3E and Microsoft tools at Lerners.'
  outcomes:
  - lever: capacity
    description: Average lift in daily billable hours per Laurel timekeeper at Tonkon Torp
    figure: 21 minutes
    measures: '''average lift in daily billable hours per Laurel timekeeper'' (customer-story headline); baseline, period and method are not stated. The story body says ''an average lift of 20 minutes per day''.'
    provenance: vendor-published
    source_ref: LAUREL-TONKON-2026
  - lever: capacity
    description: Revenue per timekeeper at Tonkon Torp
    figure: approximately $20,000 more per timekeeper per year
    measures: '''each timekeeper provides approximately $20,000 more to the firm''s revenue every year'' (managing partner''s quote and page text); how it was derived is not stated.'
    provenance: vendor-published
    source_ref: LAUREL-TONKON-2026
  - lever: quality
    description: Entry granularity at Tonkon Torp
    figure: 18% more entries per day
    measures: entries released per day by attorneys who use Laurel, described as 'greater timesheet granularity'; baseline not stated.
    provenance: vendor-published
    source_ref: LAUREL-TONKON-2026
  - lever: speed
    description: Collection cycle at Tonkon Torp
    figure: 20% faster
    measures: the firm's collection cycle; the headline says '20% increase in release velocity, expediting the collecting cycle' and the body says 'a collection cycle that's 20% faster'; method not stated.
    provenance: vendor-published
    source_ref: LAUREL-TONKON-2026
  - lever: capacity
    description: Billable time captured at Lerners
    figure: +0.48 billable hours captured per lawyer daily
    measures: '''key fact'' on the customer-story page; per lawyer per day; baseline and period not stated.'
    provenance: vendor-published
    source_ref: LAUREL-LERNERS-2026
  - lever: experience
    description: Billing disputes at Lerners
    figure: zero billing disputes
    measures: '''Zero billing disputes due to AI-first time records clients can trust'' (customer-story key fact); the period and the number of invoices covered are not stated.'
    provenance: vendor-published
    source_ref: LAUREL-LERNERS-2026
  prerequisites:
  - 'Integration with the email, document and calendar tools lawyers use and with the billing system (Lerners: Elite 3E and Microsoft tools) (LAUREL-LERNERS-2026).'
  - Training from the first day (Lerners trains every new partner, associate and student on Laurel on day one) (LAUREL-LERNERS-2026).
  - Matter and client reference data good enough for activity to be mapped to the right matter (implied by the product description; no source tests this).
  risks_and_guardrails:
  - 'Billed time must reflect time actually spent on the client''s matter: California guidance says hourly billing must reflect time actually spent (CALBAR-GENAI-2026, p.8); the Australian regulators'' joint statement says billed time and work items must accurately represent the work done (AUSLEG-AISTATEMENT-2024, p.1). The customer stories do not describe how captured activity is checked against effort.'
  - A Lerners partner is quoted as saying a challenged entry can be defended because it is 'literally AI saying how long I worked' (LAUREL-LERNERS-2026); the regulator texts above place the duty on the lawyer, so the lawyer's review step stays the control.
  - Capture reads email, documents and calls, so it monitors workers. The UK ICO has guidance on monitoring workers that is currently marked under review (ICO-MONITORING-2026). The EU AI Act lists AI systems intended to 'monitor and evaluate the performance and behaviour' of people in work relationships among high-risk uses (EU-AIACT-ANNEX3-2024, point 4(b)); the Commission page says Annex III obligations are extended to 2 December 2027 (EC-AIACT-2026). The sources do not say whether time-capture tools fall within that wording; it depends on the intended use.
  - On US federal time-and-materials contracts, vouchers must be substantiated by 'individual daily job timekeeping records' or other substantiation the contracting officer approves (FAR-52.232-7, paragraph (a) on vouchers). No source read addresses whether passively captured time satisfies that.
  - All outcome figures come from vendor-published customer stories; the Tonkon Torp story gives 20 and 21 minutes in different places, and no baselines.
  human_checkpoints:
  - Timekeeper reviews, edits and releases each entry (LAUREL-TONKON-2026; LAUREL-LERNERS-2026).
  - Billing partner review before the invoice goes out (existing step; not described in the stories).
  role_evolution: Lerners' firm chair says her dockets now take about five minutes, against 30 to 45 minutes before (LAUREL-LERNERS-2026, quote). A Kopka Law executive says talent is leaving defence practice because of the tedium of capturing time in six-minute increments (TRI-BILLING-2026, quote).
  evidence_grade: B
  sources:
  - ref: LAUREL-TONKON-2026
    title: Tonkon Torp LLP embraces Laurel for superior client service and timekeeper happiness (customer story; page date shown as Aug 21, 2026, the same date as the other customer stories)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/tonkon-torp
    date: '2026-08-21'
    access: full
    locator: Customer-story headline statistics; 'After Laurel' paragraph; 'Building trust with clients' section
  - ref: LAUREL-LERNERS-2026
    title: How Lerners repaired client service issues, netting out to zero billing disputes (customer story)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/lerners
    date: '2026-08-21'
    access: full
    locator: Key facts; 'Manual time entry created client service issues'; 'Transformative results'
  - ref: LAUREL-WARRENAVERETT-2026
    title: How Warren Averett turned time entry into a competitive advantage (customer story)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/customer-stories/warren-averett
    date: '2026-08-21'
    access: full
    locator: Opening section on daily 9:00 a.m. time submission
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: Paragraph 'Recording time is work that lawyers cannot bill for'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.8, 'Charging for Work Produced by Generative AI and Generative AI Costs'
  - ref: AUSLEG-AISTATEMENT-2024
    title: Statement on the Use of Artificial Intelligence in Australian Legal Practice
    publisher: Law Society of New South Wales, Legal Practice Board of Western Australia, Victorian Legal Services Board + Commissioner
    type: regulator
    url: https://www.lawsociety.com.au/sites/default/files/2024-12/LS4590_PSP_Statement_AI_LawSocietyVersion.pdf
    date: 2024-12
    access: full
    locator: p.1, 'Charging costs that are fair, reasonable and proportionate'
  - ref: ICO-MONITORING-2026
    title: 'Employment practices and data protection: monitoring workers (page marked under review)'
    publisher: UK Information Commissioner's Office
    type: regulator
    url: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/
    date: 2026-10
    access: full
    locator: Page introduction and contents list
  - ref: EU-AIACT-ANNEX3-2024
    title: 'Annex III: High-risk AI systems referred to in Article 6(2) (online text of Regulation (EU) 2024/1689)'
    publisher: artificialintelligenceact.eu
    type: regulator
    url: https://artificialintelligenceact.eu/annex/3/
    date: 2024-08
    access: full
    locator: Point 4(b)
  - ref: EC-AIACT-2026
    title: 'AI Act: regulatory framework for AI (application timeline)'
    publisher: European Commission
    type: regulator
    url: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
    date: 2026-10
    access: full
    locator: '''Application timeline'''
  - ref: FAR-52.232-7
    title: FAR 52.232-7 Payments under Time-and-Materials and Labor-Hour Contracts (Nov 2021 clause text)
    publisher: Acquisition.gov (US federal government)
    type: regulator
    url: https://www.acquisition.gov/far/52.232-7
    date: 2021-11
    access: full
    locator: Paragraph (a), vouchers, items (i)-(iii)
  - ref: TRI-BILLING-2026
    title: How one law firm is challenging a broken status quo around billing (Kopka Law)
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing
    date: '2026-04-30'
    access: full
    locator: Section 'Killing the profession 6 minutes at a time'
  last_reviewed: '2026-10-19'
  notes: Grade is B because every figure is published by the vendor in customer stories; the Tonkon Torp managing partner is quoted as saying the firm did 'analytical work' showing more time captured, but no independent measurement or method is published. Laurel's home page also states 'Up to 30min recovered daily', '4-11% profit increase' and '2.88 more time entries daily' with no denominators (LAURELSITE-2026); these are not used as outcomes. All customer stories carry the same page date (21 Aug 2026), so deployment dates are unknown. Older vendor survey claims about lost billable time (for example a 2012 LexisNexis survey and a Thomson Reuters self-report figure) were seen only in search results and are not used.
- id: professional-services-billing-collections-02
  title: Time entries generated from the tasks lawyers complete inside an AI platform
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - transaction-processing
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: As more of the working day moves into AI platforms, that work is hard to capture and firm leaders want a view of how it changes (LEGORA-LAUREL-2026).
  solution: Laurel will turn every task a lawyer completes in Legora into a time entry with client, matter and a specific narrative, 'ready for the lawyer to review'. Automated capture from Legora is to be available first; a second phase will develop measures of how Legora is used and the value it brings (LEGORA-LAUREL-2026).
  outcomes:
  - lever: quality
    description: Release claims fewer gaps in the record because work in Legora is logged as it happens; no figure given
    figure: none published
    measures: 'n/a: no figure published'
    provenance: vendor-published
    source_ref: LEGORA-LAUREL-2026
  prerequisites:
  - Firms using both Legora and Laurel; availability details to follow as the rollout begins (LEGORA-LAUREL-2026).
  risks_and_guardrails:
  - The release does not say whether an entry records the lawyer's time or the duration of the AI task. Sources set out that hourly billing must reflect actual time spent (CALBAR-GENAI-2026, p.8; DCBAR-OP388-2024, section E) and that a lawyer may not bill time 'saved' by the tool (TXETHICS-OP705-2025, 'Fees').
  - Lawyers may not charge a client for time spent learning an AI tool for use on matters generally, unless the client asks for that tool on the matter (ABA-BLT-2024, summary of Formal Opinion 512, Fees).
  - 'A client can bar pass-through of AI time: Zscaler''s guidelines say any time and cost associated with AI-generated work product shall not be passed on (ZSCALER-OCG-2025, section ''Artificial Intelligence (AI)'').'
  human_checkpoints:
  - Lawyer reviews each draft entry before release (LEGORA-LAUREL-2026).
  role_evolution: No source describes role change.
  evidence_grade: C
  sources:
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: Announcement text, phases one and two (13 Oct 2026)
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.8
  - ref: DCBAR-OP388-2024
    title: Ethics Opinion 388 (generative AI in client matters)
    publisher: District of Columbia Bar
    type: professional-body
    url: https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388
    date: 2024-04
    access: full
    locator: Section E, Fees
  - ref: TXETHICS-OP705-2025
    title: Opinion 705 (generative AI)
    publisher: Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics
    type: professional-body
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Section 'Fees'
  - ref: ABA-BLT-2024
    title: ABA Ethics Opinion on Generative AI Offers Useful Framework (summary of Formal Opinion 512, issued 29 July 2024)
    publisher: American Bar Association, Business Law Today
    type: professional-body
    url: https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-october/aba-ethics-opinion-generative-ai-offers-useful-framework/
    date: 2024-10
    access: full
    locator: Summary bullets, Fees (Model Rule 1.5)
  - ref: ZSCALER-OCG-2025
    title: Outside Counsel Billing Guidelines (revised April 7, 2025); a client (in-house) primary document
    publisher: Zscaler, Inc.
    type: firm
    url: https://www.zscaler.com/legal/outside-counsel-billing-guidelines
    date: '2025-04-07'
    access: full
    locator: Section 'Artificial Intelligence (AI)'
  last_reviewed: '2026-10-19'
  notes: Announcement only; the release says firms will receive availability details as the rollout begins. Product names are Legora and Laurel as stated in the source.
- id: professional-services-billing-collections-03
  title: Narrative, task-code and client-guideline checks at the point of time entry
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - review-assurance
  - document-production
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: 'Outside counsel guidelines can run 15 to 100 pages per client and the reviewer has to remember them (LAUREL-BILLING-2026). Clients enforce them hard: Zscaler rejects block-billed lines, which can be resubmitted at a 15% reduction or paid at a non-appealable 10% reduction at its discretion, and applies a 20% discount to invoices received more than 60 days after the due date (ZSCALER-OCG-2025, ''Block Billing'' and ''Invoicing''). Layer3''s guide says e-billing systems reject invoices that lack valid LEDES or UTBMS codes (LAYER3-OCG-2026).'
  solution: 'A rules engine holds each client''s guidelines once and checks each entry as it is written: narrative detail, block billing, task codes, prohibited work and staffing rules. Corrections made later on the bill feed back to the model that writes narratives and picks codes (LAUREL-BILLING-2026, ''How it works'' and ''learning compounds'' paragraphs). Brightflag runs a mirror-image check on the client side (see use case 06).'
  outcomes:
  - lever: speed
    description: Pre-bill review time at one unnamed Laurel customer
    figure: 30-40% reduction
    measures: pre-bill review time at one customer, which the vendor attributes to rules enforced at timekeeping 'from that alone'; baseline, period and method are not stated.
    provenance: vendor-published
    source_ref: LAUREL-BILLING-2026
  prerequisites:
  - Each client's guidelines codified in the rules engine and kept current; Zscaler states it may modify its guidelines at any time and that updates are written notice (ZSCALER-OCG-2025, 'Summary').
  - Integration between the timekeeping tool and the practice management or billing system (LAUREL-BILLING-2026).
  risks_and_guardrails:
  - 'Clients give conflicting instructions: some want AI used and savings shown, others still require permission before any AI use (TRI-LEGALWEEK-2026, DLA Piper panel). The rules engine needs per-client AI terms, not only billing-format rules.'
  - A narrative drafted to satisfy a client's guideline must still describe work actually done (AUSLEG-AISTATEMENT-2024, p.1).
  - UTBMS code sets are maintained by bodies such as the ABA and the LEDES Oversight Committee; the code-set index read lists no AI-specific set (LEDES-UTBMS-2026).
  human_checkpoints:
  - Timekeeper accepts or edits the drafted narrative and code.
  - Billing partner review of the assembled bill (use case 04).
  role_evolution: Billers and coordinators move from re-keying partner mark-ups to approving flagged fixes (LAUREL-BILLING-2026 describes a partner marking up a printed bill for a coordinator to re-key as the pain point).
  evidence_grade: C
  sources:
  - ref: LAUREL-BILLING-2026
    title: 'Coming Soon: Laurel Billing - Defend every bill before it goes out (Nick Bazley)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/blog/coming-soon-laurel-billing
    date: '2026-08-19'
    access: full
    locator: '''Careful billing is still done by hand''; ''How it works'''
  - ref: LAURELSITE-2026
    title: 'Laurel home page: AI Timekeeping and Work Intelligence Platform (read 19 Oct 2026)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai
    date: '2026-10-19'
    access: full
    locator: 'Compliance tile: ''Point of entry OCG enforcement'''
  - ref: ZSCALER-OCG-2025
    title: Outside Counsel Billing Guidelines (revised April 7, 2025); a client (in-house) primary document
    publisher: Zscaler, Inc.
    type: firm
    url: https://www.zscaler.com/legal/outside-counsel-billing-guidelines
    date: '2025-04-07'
    access: full
    locator: Sections 'Summary', 'Invoicing', 'Block Billing'
  - ref: LAYER3-OCG-2026
    title: 'Outside Counsel Billing Guidelines: plain-language guide (reviewed, updated 7 Jul 2026)'
    publisher: Layer3 Labs
    type: vendor
    url: https://www.layer3labs.io/guides/outside-counsel-billing-guidelines
    date: '2026-07-07'
    access: full
    locator: Sections on core requirements and how software enforces guidelines
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: DLA Piper panel, 'The contradictions in the room'
  - ref: AUSLEG-AISTATEMENT-2024
    title: Statement on the Use of Artificial Intelligence in Australian Legal Practice
    publisher: Law Society of New South Wales, Legal Practice Board of Western Australia, Victorian Legal Services Board + Commissioner
    type: regulator
    url: https://www.lawsociety.com.au/sites/default/files/2024-12/LS4590_PSP_Statement_AI_LawSocietyVersion.pdf
    date: 2024-12
    access: full
    locator: p.1
  - ref: LEDES-UTBMS-2026
    title: LEDES Oversight Committee site (ledes.org) and UTBMS.com code-set index, read 19 Oct 2026
    publisher: LEDES Oversight Committee
    type: standard-setter
    url: https://ledes.org/ ; https://www.utbms.com/
    date: 2026-10
    access: full
    locator: UTBMS.com code-set index
  last_reviewed: '2026-10-19'
  notes: One vendor-reported, unnamed customer; grade C. Zscaler's guidelines are the clearest public example of the rules a client enforces; they do not mention AI-based enforcement on the client side.
- id: professional-services-billing-collections-04
  title: Pre-bill review agent that checks the assembled bill against client guidelines and queues fixes for a billing partner to approve
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - review-assurance
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: Finding the few entries at risk of write-off means reading hundreds per cycle, usually under deadline. Laurel says firms told it of a bill that took 210 emails between partners and billing, and of a top-earning partner spending 12 hours every first Sunday of the month on a pre-bill that ran 1,000 pages (LAUREL-BILLING-2026, firm anecdotes relayed by the vendor).
  solution: A Compliance agent checks the whole bill against the client's guidelines and the underlying work record, including duplicate billing across timekeepers and excessive research time. Each flag arrives with the reason and a fix already written, so the billing partner approves decisions rather than reading every line; approved corrections feed back into timekeeping. 'Nothing goes out without your sign-off.' Laurel Billing was announced on 19 Aug 2026 as coming soon (LAUREL-BILLING-2026; LAUREL-BILLINGPAGE-2026).
  outcomes:
  - lever: speed
    description: Vendor says bill review gets shorter every cycle; no figure published for the billing product
    figure: none published
    measures: 'n/a: no figure published'
    provenance: vendor-published
    source_ref: LAUREL-BILLING-2026
  prerequisites:
  - Client guidelines codified in the rules engine and a working timekeeping feed (LAUREL-BILLING-2026).
  - A billing workflow with preparer, billing partner and finance stages (LAUREL-BILLINGPAGE-2026).
  risks_and_guardrails:
  - Billing must reflect actual time spent and fees must be reasonable (CALBAR-GENAI-2026, p.8); an agent that rewrites narratives risks drifting from the work done, so reviewers need the work record beside each fix (AUSLEG-AISTATEMENT-2024, p.1).
  - Georgetown's Perlin argues GenAI may help prepare bills that better conform to client guidelines and so cut the line items clients can dispute, while also letting sophisticated clients scrutinise invoices in new ways (LEGALFUTURES-PERLIN-2025).
  - No error, override or false-flag rate is published for any billing agent.
  human_checkpoints:
  - Billing partner approves or rejects each queued fix and signs off the bill (LAUREL-BILLINGPAGE-2026).
  role_evolution: The vendor describes the preparer, billing partner and finance roles working in one workspace, with partners 'approving decisions, not entries' (LAUREL-BILLINGPAGE-2026).
  evidence_grade: C
  sources:
  - ref: LAUREL-BILLING-2026
    title: 'Coming Soon: Laurel Billing - Defend every bill before it goes out (Nick Bazley)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/blog/coming-soon-laurel-billing
    date: '2026-08-19'
    access: full
    locator: Whole post (19 Aug 2026); 'The Billing Agents do the legwork'
  - ref: LAUREL-BILLINGPAGE-2026
    title: Laurel Billing product page ('Billing - coming soon'; read 19 Oct 2026)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/billing
    date: '2026-10-19'
    access: full
    locator: Compliance agent; 'Review-ready fixes'
  - ref: LEGALFUTURES-PERLIN-2025
    title: GenAI could 'reinforce rather than disrupt' the billable hour (report on the Perlin article)
    publisher: Legal Futures
    type: press
    url: https://www.legalfutures.co.uk/latest-news/genai-could-reinforce-rather-than-disrupt-the-billable-hour
    date: '2025-11-14'
    access: full
    locator: Paragraphs on write-offs
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.8
  - ref: AUSLEG-AISTATEMENT-2024
    title: Statement on the Use of Artificial Intelligence in Australian Legal Practice
    publisher: Law Society of New South Wales, Legal Practice Board of Western Australia, Victorian Legal Services Board + Commissioner
    type: regulator
    url: https://www.lawsociety.com.au/sites/default/files/2024-12/LS4590_PSP_Statement_AI_LawSocietyVersion.pdf
    date: 2024-12
    access: full
    locator: p.1
  last_reviewed: '2026-10-19'
  notes: Product described as coming soon with a waitlist; no customer deployment found. Anecdotes about 210 emails and 12 hours are the vendor's, not measurements.
- id: professional-services-billing-collections-05
  title: Scope agent that tracks fixed-fee budget burn and turns out-of-scope hours into a sized change order before close
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
  problem: On fixed-fee matters, work that drifts outside the engagement is absorbed as a write-down at close instead of raised as a change order (LAUREL-BILLING-2026).
  solution: The Scope agent tracks budget burn against the engagement and flags hours that have drifted outside it, totalled in dollars, so a change order can be raised while the matter is open. Laurel's consulting page makes the same point for consultants ('scope creep surfaces immediately, not at close') (LAUREL-BILLING-2026; LAURELSITE-2026).
  outcomes:
  - lever: risk
    description: Vendor positions the agent to avoid quiet write-downs on fixed fees; no figure published
    figure: none published
    measures: 'n/a: no figure published'
    provenance: vendor-published
    source_ref: LAUREL-BILLING-2026
  prerequisites:
  - A defined engagement scope and budget in the system of record (implied; the source does not list prerequisites).
  risks_and_guardrails:
  - Fee agreements should say how fees are calculated and the extent to which AI factors into rates (CALBAR-GENAI-2026, p.8).
  - 'Flat-fee rules differ by state: North Carolina allows a flat fee that is not clearly excessive with client consent (NCBAR-FEO1-2024, Opinion 6); ABA Formal Opinion 512, as quoted, says the same flat fee may be unreasonable if a tool makes the work much quicker (TRI-ABA512-2025); Virginia disagrees and says a value-based fee can stay reasonable (VACOURTS-LEO1901-2025, pp.2-4).'
  - A change order priced on hours that AI compressed invites the client question this opinion split addresses; see 'Routed to other modules' for scoping-pricing.
  human_checkpoints:
  - Partner decides whether to raise the change order (the agent flags; the source does not describe an automatic send).
  role_evolution: Not described.
  evidence_grade: C
  sources:
  - ref: LAUREL-BILLING-2026
    title: 'Coming Soon: Laurel Billing - Defend every bill before it goes out (Nick Bazley)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/blog/coming-soon-laurel-billing
    date: '2026-08-19'
    access: full
    locator: Description of the Scope agent
  - ref: LAUREL-BILLINGPAGE-2026
    title: Laurel Billing product page ('Billing - coming soon'; read 19 Oct 2026)
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/platform/billing
    date: '2026-10-19'
    access: full
    locator: '''Scope agent'''
  - ref: LAURELSITE-2026
    title: 'Laurel home page: AI Timekeeping and Work Intelligence Platform (read 19 Oct 2026)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai
    date: '2026-10-19'
    access: full
    locator: Consulting tile
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.8
  - ref: NCBAR-FEO1-2024
    title: 2024 Formal Ethics Opinion 1 (use of artificial intelligence in a law practice)
    publisher: North Carolina State Bar
    type: professional-body
    url: https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/
    date: '2024-11-01'
    access: full
    locator: Inquiry on a flat fee for estate documents
  - ref: TRI-ABA512-2025
    title: Is ABA Formal Opinion 512 off the mark? And if so, what can law firms and GCs do about it? (William Josten; quotes the opinion)
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/aba-formal-opinion-512
    date: '2025-04-02'
    access: full
    locator: Section on flat fees, quoting Formal Opinion 512
  - ref: VACOURTS-LEO1901-2025
    title: Order approving Legal Ethics Opinion 1901 (full opinion text)
    publisher: Supreme Court of Virginia
    type: regulator
    url: https://www.vacourts.gov/static/courts/scv/amendments/leo_1901.pdf
    date: '2025-11-24'
    access: full
    locator: Analysis, pp.2-4
  last_reviewed: '2026-10-19'
  notes: Announced product; no customer or figure.
- id: professional-services-billing-collections-06
  title: Client-side AI invoice review that reads narratives, applies outside counsel guidelines and routes exceptions to in-house reviewers (in-house)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - review-assurance
  - transaction-processing
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: 'Insurance clients employ large departments and third-party vendors to review, audit and cut legal bills, and defence firms such as Kopka Law have built payment and appeals teams in response (TRI-BILLING-2026, as described by Kopka Law). Clients also want AI savings to show up in bills: Gartner''s Weston Wicks says more companies are adding outside counsel guideline provisions asking that lower-risk tasks be done by AI and that the time savings be reflected in billable hours (BLOOMBERGLAW-ACC-2025).'
  solution: Brightflag says its system reads line-item narratives, classifies them into legal tasks, flags guideline violations and anomalies, and emails the reviewer a summary of the invoice so it can be approved or rejected from the inbox. Layer3's guide adds that AI review tools flag entries where billed time looks high for the task described (BRIGHTFLAG-AIINVOICE-2025; LAYER3-OCG-2026).
  outcomes:
  - lever: cost
    description: Brightflag says in-house teams save time and money and that hundreds of legal departments use its AI; no figure is published in the post
    figure: none published
    measures: 'n/a: no figure published'
    provenance: vendor-published
    source_ref: BRIGHTFLAG-AIINVOICE-2025
  prerequisites:
  - Invoices in LEDES format on an e-billing platform; Layer3 lists Legal Tracker, Brightflag, TyMetrix, SimpleLegal and BillingPoint as platforms that receive them (LAYER3-OCG-2026).
  - Written, current outside counsel guidelines (ZSCALER-OCG-2025 is a public example).
  risks_and_guardrails:
  - Brightflag describes supervised machine learning with human analysts correcting low-confidence cases, not an unsupervised generative reviewer (BRIGHTFLAG-AIINVOICE-2025); no accuracy, false-rejection or override rate is published.
  - Firms can face reductions and penalties for lines the client's rules reject (ZSCALER-OCG-2025, 'Block Billing'); automated enforcement makes that consistent across invoices.
  - Perlin notes sophisticated clients may use GenAI to scrutinise invoices in new ways or demand additional discounts (LEGALFUTURES-PERLIN-2025).
  human_checkpoints:
  - In-house reviewer approves, rejects or amends flagged invoices (BRIGHTFLAG-AIINVOICE-2025).
  role_evolution: Reviewers move from reading every line to handling flagged exceptions (BRIGHTFLAG-AIINVOICE-2025, vendor statement).
  evidence_grade: C
  sources:
  - ref: BRIGHTFLAG-AIINVOICE-2025
    title: Legal AI Invoice Review Explained (Sinead Kenny; updated 24 Jul 2025)
    publisher: Brightflag
    type: vendor
    url: https://brightflag.com/resources/ai-invoice-review-how-it-works/
    date: '2025-07-22'
    access: full
    locator: Benefits 1-5 and 'How Does AI Invoice Review Work?'
  - ref: LAYER3-OCG-2026
    title: 'Outside Counsel Billing Guidelines: plain-language guide (reviewed, updated 7 Jul 2026)'
    publisher: Layer3 Labs
    type: vendor
    url: https://www.layer3labs.io/guides/outside-counsel-billing-guidelines
    date: '2026-07-07'
    access: full
    locator: Sections 'How Software Enforces Billing Guidelines' and 'How AI Now Factors into Billing Rules'
  - ref: ZSCALER-OCG-2025
    title: Outside Counsel Billing Guidelines (revised April 7, 2025); a client (in-house) primary document
    publisher: Zscaler, Inc.
    type: firm
    url: https://www.zscaler.com/legal/outside-counsel-billing-guidelines
    date: '2025-04-07'
    access: full
    locator: '''Block Billing''; ''Invoicing'''
  - ref: BLOOMBERGLAW-ACC-2025
    title: AI Does Little to Reduce Law Firm Billable Hours, Survey Shows (ACC-Everlaw survey)
    publisher: Bloomberg Law
    type: press
    url: https://news.bgov.com/business-and-practice/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows
    date: '2025-10-14'
    access: full
    locator: Paragraph quoting Gartner's Weston Wicks
  - ref: TRI-BILLING-2026
    title: How one law firm is challenging a broken status quo around billing (Kopka Law)
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing
    date: '2026-04-30'
    access: full
    locator: Section 'The administrative-industrial complex'
  - ref: LEGALFUTURES-PERLIN-2025
    title: GenAI could 'reinforce rather than disrupt' the billable hour (report on the Perlin article)
    publisher: Legal Futures
    type: press
    url: https://www.legalfutures.co.uk/latest-news/genai-could-reinforce-rather-than-disrupt-the-billable-hour
    date: '2025-11-14'
    access: full
    locator: Paragraphs on write-offs
  last_reviewed: '2026-10-19'
  notes: in-house. Vendor claim; no named customer in the sources read. A Wolters Kluwer 2026 CLM Alliance study summary seen only in search results says insurers using AI-driven bill review report better processing speed and billing compliance, with some reporting up to a 10% cut in legal costs; the page returned 403 and is not used as an outcome (WK-CLM-2026, search-only).
- id: professional-services-billing-collections-07
  title: Automated detection and follow-up of overdue invoices, with human collectors for escalation
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - transaction-processing
  - client-interaction
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: CollBox's co-founder, citing Clio data, said it takes law firms an average of 97 days to get paid and that no one owns the accounts receivable process inside firms (ABAJ-TECHSHOW-2026). Wells Fargo Legal Specialty Group data for the first half of 2026 show firm inventories up 17.7% and collection cycles slowing by 5% (LAWFUEL-WF-2026, secondary report).
  solution: CollBox, winner of ABA Techshow 2026's Startup Alley, integrates with practice management systems, automatically detects unpaid bills and chases them with email reminders and calls from trained accounts-receivable specialists. The ABA Journal headline calls it AI-powered; the pitch as reported describes detection and reminders plus human collectors (ABAJ-TECHSHOW-2026).
  outcomes:
  - lever: risk
    description: Revenue recovered for law firms by CollBox
    figure: more than $100 million in the past year
    measures: company-reported, at a three-minute pitch, as 'recovered more than $100 million for law firms in the past year'; number of firms, period definition and basis are not stated.
    provenance: vendor-published
    source_ref: ABAJ-TECHSHOW-2026
  prerequisites:
  - Integration with the practice management system so unpaid bills are detected (ABAJ-TECHSHOW-2026).
  - A client-relationship rule for who may chase which client (not covered by the sources).
  risks_and_guardrails:
  - 'Some post-work discounting protects client relationships; firms that push for full post-work realization risk damaging them (TRI-RATES-2026, p.11, ''Stage 3: Combustion'').'
  - 'Collection performance feeds back into the next cycle''s rate increases: weak collections undermine the ability to push rates higher (TRI-RATES-2026, p.12, ''Stage 4: Exhaust'').'
  - No bar guidance on automated payment reminders or third-party collectors was found in the sources read.
  human_checkpoints:
  - Trained collectors make calls and handle escalations (ABAJ-TECHSHOW-2026).
  role_evolution: The pitch says no lawyer joined a firm to be a bill collector; collection moves to a service or to billing staff (ABAJ-TECHSHOW-2026, quote of the co-founder).
  evidence_grade: C
  sources:
  - ref: ABAJ-TECHSHOW-2026
    title: AI-powered bill collector program takes top spot at ABA Techshow's Startup Alley
    publisher: ABA Journal
    type: conference
    url: https://www.abajournal.com/web/article/tool-that-gets-lawyers-paid-takes-top-spot-at-techshows-startup-alley
    date: '2026-03-26'
    access: full
    locator: Section on CollBox (26 Mar 2026)
  - ref: LAWFUEL-WF-2026
    title: US Law Firm Revenue Jumps 12.4% in First Half of 2026 as AI Work Drives Demand (reports Wells Fargo Legal Specialty Group figures)
    publisher: LawFuel
    type: press
    url: https://www.lawfuel.com/?p=194355
    date: '2026-08-26'
    access: full
    locator: Paragraphs on inventories and collection cycles
  - ref: TRI-RATES-2026
    title: Law Firm Rates Report 2026
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2025/10/Law-Firm-Rates-Report-2026.pdf
    date: 2025-10
    access: full
    locator: p.11 Stage 3; p.12 Stage 4
  last_reviewed: '2026-10-19'
  notes: Vendor claim from a startup pitch competition; grade C. The 97-day figure is relayed by the vendor from Clio and was not checked at source (Clio's Legal Trends pages returned 403). The Wells Fargo figures are in a secondary report of a Reuters story and the unit of 'collection cycles slowed by 5%' is not defined there. Other 'AI collections agent' material surfaced in search was vendor marketing and is not used.
- id: professional-services-billing-collections-08
  title: Matter-level statement of what AI changed in hours and cost, produced for the invoice and the client conversation
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  - client-interaction
  pattern: other
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: Clients ask what was used, how, and how it saved money; firms often answer 'we're still gathering the data' (TRI-LEGALWEEK-2026). A general counsel said it is very hard to tell whether clients see the benefit or just increased partner rates offsetting AI efficiencies (TRI-STANDOUT-2026). TRI warns that premium billing tied to AI adoption is sustainable only when clients clearly see added value (TRI-SOTLM-2026).
  solution: Time records that show where AI was used, with usage data from the AI platform, feed a per-matter view of effort and savings. Laurel and Legora say their second phase will jointly develop measures of how Legora is used and the value it brings, to be decided with customers; Laurel also markets 'Signal' for project profitability and AI ROI tied to hours (LEGORA-LAUREL-2026; LAURELSITE-2026). Firm-wide AI ROI measurement is routed to firm-finance.
  outcomes:
  - lever: experience
    description: Phase two measures are to be developed; no figure published
    figure: none published
    measures: 'n/a: no figure published'
    provenance: vendor-published
    source_ref: LEGORA-LAUREL-2026
  prerequisites:
  - Time entries that identify AI-assisted work (use case 09) and usage data from the AI platform (LEGORA-LAUREL-2026).
  - A baseline of how long the task took before AI; no source says where it comes from.
  risks_and_guardrails:
  - 'Under hourly billing the client benefits from time saved: the lawyer may bill only time actually spent (DCBAR-OP388-2024, section E; TXETHICS-OP705-2025, ''Fees''). A statement of savings should not turn into billing for time not worked.'
  - A Virginia Lawyer article advises disclosing efficiency-enhancing tools without itemising tool usage in a way that confuses value with minutes spent (VALAWYER-2026).
  - 'Stanford and USC researchers note that AI augmentation lowers input-cost observability: identical deliverables can be produced with widely varying human time and compute, which clients cannot see (STANFORD-DEL-2026, Section 1).'
  human_checkpoints:
  - Billing partner decides what is shown to the client.
  role_evolution: Greenberg Traurig has a Chief Pricing and Innovation Officer and DLA Piper a senior managing director of AI innovation; both spoke on client AI value at Legalweek (TRI-LEGALWEEK-2026).
  evidence_grade: C
  sources:
  - ref: LEGORA-LAUREL-2026
    title: Legora and Laurel partner to capture the time lawyers spend in Legora as they work
    publisher: Legora
    type: vendor
    url: https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work
    date: '2026-10-13'
    access: full
    locator: Phase two paragraph
  - ref: LAURELSITE-2026
    title: 'Laurel home page: AI Timekeeping and Work Intelligence Platform (read 19 Oct 2026)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai
    date: '2026-10-19'
    access: full
    locator: 'Signal tile: ''Project profitability and AI ROI, tied to the hours behind it'''
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: '''Proving AI''s path to saving clients money''; ''The billing conversation'''
  - ref: TRI-STANDOUT-2026
    title: Turning law firm AI strategies into practice (2026 Stand-out Lawyers Survey)
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice
    date: '2026-08-06'
    access: full
    locator: General counsel quote on partner rates
  - ref: TRI-SOTLM-2026
    title: '2026 State of the US Legal Market: AI value vs AI bubble analysis'
    publisher: Thomson Reuters Institute with Georgetown Law Center on Ethics and the Legal Profession
    type: survey
    url: https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble
    date: '2026-01-14'
    access: full
    locator: Analysis of premium billing tied to AI adoption
  - ref: DCBAR-OP388-2024
    title: Ethics Opinion 388 (generative AI in client matters)
    publisher: District of Columbia Bar
    type: professional-body
    url: https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388
    date: 2024-04
    access: full
    locator: Section E
  - ref: TXETHICS-OP705-2025
    title: Opinion 705 (generative AI)
    publisher: Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics
    type: professional-body
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Section 'Fees'
  - ref: VALAWYER-2026
    title: 'Using AI in the Face of Rule 1.5: Reasonableness and Client Communication (Genevieve Leah Sankar), Virginia Lawyer, February 2026 issue'
    publisher: Virginia State Bar (Virginia Lawyer magazine)
    type: professional-body
    url: https://virginialawyer.vsb.org/articles/using-ai-in-the-face-of-rule-1-5-reasonableness-and-client-communication
    date: '2026-01-21'
    access: full
    locator: '''Construction lawyers'' paragraph on explaining flat fees'
  - ref: STANFORD-DEL-2026
    title: 'Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives'
    publisher: Stanford Digital Economy Lab (Brynjolfsson) and USC Marshall (Petropoulos)
    type: academic
    url: https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf
    date: '2026-08-23'
    access: full
    locator: Section 1
  last_reviewed: '2026-10-19'
  notes: Announced as phase two of a partnership; no customer deployment. SPI's 2026 study says 84.8% of 245 firms say AI saves them time against a locked figure for those saying it generates revenue ('the leak') (SPI-AI-2026); this is routed to firm-finance.
- id: professional-services-billing-collections-09
  title: Tagging AI-assisted tasks in time entries and invoice lines to meet client AI terms (idea)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - transaction-processing
  - review-assurance
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: Client terms already ask for this. Zscaler's guidelines say a timekeeper who uses generative AI for a discrete task should note it in the time entry and that AI time and cost shall not be passed on (ZSCALER-OCG-2025). At Legalweek 2026 Ropes & Gray's Sergey Polak said clients are starting to ask whether AI was used on a task and how much time or money it saved; DLA Piper's Barclay Blair said other clients issue guidelines stating they will not pay for certain services if performed by AI (TRI-LEGALWEEK-2026). California says lawyers must follow client instructions or guidelines that restrict AI (CALBAR-GENAI-2026, p.7).
  solution: 'Idea: the timekeeping tool records, or the AI platform reports, which tasks were AI-assisted, and billing applies the client''s rule (write off, discount, disclose or report). No source describes a deployed tool for this; the requirement is documented, the tooling is not.'
  outcomes:
  - lever: risk
    description: none published
    figure: none published
    measures: 'n/a: no figure published'
    provenance: self-reported
    source_ref: ZSCALER-OCG-2025
  prerequisites:
  - Per-client AI terms held as rules (use case 03).
  - A way to identify AI-assisted tasks, for example usage data from the AI platform (use case 02).
  risks_and_guardrails:
  - The Australian regulators' statement says solicitors should record and disclose when and how AI was used and how it is reflected in costs if the client requests (AUSLEG-AISTATEMENT-2024, p.2).
  - The Law Society of England and Wales page says the SRA does not currently have specific generative AI guidance on use or disclosure for client care (LAWSOC-GENAI-2026, section on client care); SRA pages could not be opened.
  - Layer3 reports that some clients require disclosure of AI use and pass-through of efficiency savings, and that charging full hours for AI-accelerated work leads to write-offs (LAYER3-AIOCG-2026, 'Clause 4').
  human_checkpoints:
  - Timekeeper confirms the AI tag; billing partner applies the client rule.
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: ZSCALER-OCG-2025
    title: Outside Counsel Billing Guidelines (revised April 7, 2025); a client (in-house) primary document
    publisher: Zscaler, Inc.
    type: firm
    url: https://www.zscaler.com/legal/outside-counsel-billing-guidelines
    date: '2025-04-07'
    access: full
    locator: Section 'Artificial Intelligence (AI)'
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: '''The billing conversation'' paragraphs'
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.7, Rules 1.2 and 1.4 row
  - ref: AUSLEG-AISTATEMENT-2024
    title: Statement on the Use of Artificial Intelligence in Australian Legal Practice
    publisher: Law Society of New South Wales, Legal Practice Board of Western Australia, Victorian Legal Services Board + Commissioner
    type: regulator
    url: https://www.lawsociety.com.au/sites/default/files/2024-12/LS4590_PSP_Statement_AI_LawSocietyVersion.pdf
    date: 2024-12
    access: full
    locator: p.2
  - ref: LAWSOC-GENAI-2026
    title: Generative AI - the essentials (page is undated; latest event it cites is April 2026)
    publisher: Law Society of England and Wales
    type: professional-body
    url: https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials
    date: 2026-04
    access: full
    locator: Section on client care
  - ref: LAYER3-AIOCG-2026
    title: 'AI Provisions in Outside Counsel Guidelines: A Compliance Guide for Law Firms (updated 7 Sep 2026)'
    publisher: Layer3 Labs
    type: vendor
    url: https://www.layer3labs.io/guides/ai-provisions-outside-counsel-guidelines
    date: '2026-09-07'
    access: full
    locator: '''Clause 4: Billing Rules for AI-assisted Work'''
  last_reviewed: '2026-10-19'
  notes: 'Idea: the client demand is documented (Zscaler, Legalweek), but no deployed tagging tool was found. Grade D.'
- id: professional-services-billing-collections-10
  title: Summarised 'services rendered' invoice in place of itemised time when AI compresses tasks (idea)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - document-production
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: At Legalweek 2026 Zarwin Baum's Mitchell Kaplan said that when AI compresses hours into minutes, an itemised hourly bill undersells the value delivered (TRI-LEGALWEEK-2026). Kopka Law's founder calls the billable hour 'a gigantic waste of time for everyone involved' and the firm's COO describes the overhead of managing it on both the firm and client side (TRI-BILLING-2026).
  solution: 'Idea: replace itemised time entries with a single ''services rendered'' line, which Kaplan noted predates the billable hour, and asked whether clients would accept it. Kopka Law says it is moving to monthly-retainer or portfolio-based billing tied to KPIs such as cycle time, case disposition and indemnity outcomes (TRI-BILLING-2026). The sources do not describe an AI tool that writes the summary.'
  outcomes:
  - lever: cost
    description: none published
    figure: none published
    measures: 'n/a: no figure published'
    provenance: self-reported
    source_ref: TRI-LEGALWEEK-2026
  prerequisites:
  - Client agreement to a non-itemised format; clients with guidelines requiring one task per line cannot accept it (ZSCALER-OCG-2025, 'Block Billing').
  risks_and_guardrails:
  - Where fees are time-based, billing must reflect time actually spent, so a summarised bill still needs underlying records (CALBAR-GENAI-2026, p.8).
  - Virginia's opinion requires the fee basis to be adequately explained, particularly where AI reduces time (VACOURTS-LEO1901-2025, pp.3-4; VALAWYER-2026).
  - Perlin argues AFAs have mostly supplemented rather than replaced hourly billing and that firms still use hours to measure internal productivity (LEGALFUTURES-PERLIN-2025).
  human_checkpoints:
  - Billing partner agrees the format with the client.
  role_evolution: Rapoport and Tiano predict firms will move from input-based billing towards outputs and that the pyramid will be pressured (WJLTA-RAPOPORT-2025, abstract).
  evidence_grade: D
  sources:
  - ref: TRI-LEGALWEEK-2026
    title: 'Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide'
    publisher: Thomson Reuters Institute
    type: conference
    url: https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide
    date: '2026-03-13'
    access: full
    locator: Kaplan paragraph in 'The billing conversation'
  - ref: TRI-BILLING-2026
    title: How one law firm is challenging a broken status quo around billing (Kopka Law)
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing
    date: '2026-04-30'
    access: full
    locator: Sections on KPIs and billing model
  - ref: ZSCALER-OCG-2025
    title: Outside Counsel Billing Guidelines (revised April 7, 2025); a client (in-house) primary document
    publisher: Zscaler, Inc.
    type: firm
    url: https://www.zscaler.com/legal/outside-counsel-billing-guidelines
    date: '2025-04-07'
    access: full
    locator: '''Block Billing'''
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.8
  - ref: VACOURTS-LEO1901-2025
    title: Order approving Legal Ethics Opinion 1901 (full opinion text)
    publisher: Supreme Court of Virginia
    type: regulator
    url: https://www.vacourts.gov/static/courts/scv/amendments/leo_1901.pdf
    date: '2025-11-24'
    access: full
    locator: Rule 1.5(b) analysis
  - ref: VALAWYER-2026
    title: 'Using AI in the Face of Rule 1.5: Reasonableness and Client Communication (Genevieve Leah Sankar), Virginia Lawyer, February 2026 issue'
    publisher: Virginia State Bar (Virginia Lawyer magazine)
    type: professional-body
    url: https://virginialawyer.vsb.org/articles/using-ai-in-the-face-of-rule-1-5-reasonableness-and-client-communication
    date: '2026-01-21'
    access: full
    locator: Takeaways
  - ref: LEGALFUTURES-PERLIN-2025
    title: GenAI could 'reinforce rather than disrupt' the billable hour (report on the Perlin article)
    publisher: Legal Futures
    type: press
    url: https://www.legalfutures.co.uk/latest-news/genai-could-reinforce-rather-than-disrupt-the-billable-hour
    date: '2025-11-14'
    access: full
    locator: Paragraphs on AFAs
  - ref: WJLTA-RAPOPORT-2025
    title: 'Fighting the Hypothetical: Why Law Firms Should Rethink the Billable Hour in the Generative AI Era (Rapoport and Tiano), 20 Wash. J. L. Tech. & Arts 41'
    publisher: University of Washington School of Law, Washington Journal of Law, Technology & Arts
    type: academic
    url: https://digitalcommons.law.uw.edu/wjlta/vol20/iss2/2
    date: '2025'
    access: full
    locator: Abstract
  last_reviewed: '2026-10-19'
  notes: Idea discussed at a conference; Kopka Law's retainer model is a real, non-AI-specific alternative billing arrangement and is routed to scoping-pricing.
- id: professional-services-billing-collections-11
  title: Matter-level metering of AI tool costs for expense pass-through or overhead treatment (idea)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  - transaction-processing
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: workflow-automation
  maturity: emerging
  problem: The treatment of AI costs depends on whether they are overhead or matter-specific. California says general-purpose AI subscriptions are overhead, but per-use fees and custom builds for a matter may be charged if the fee agreement discloses it, the charge reflects actual cost, and no markup is added without informed written consent (CALBAR-GENAI-2026, p.8). Texas says per-use fees can be recovered only at the amount actually paid (TXETHICS-OP705-2025, 'Fees'). At ILTACON 2026 the shift from seat-based to consumption-based AI pricing was a hallway topic (EDISCOVERYTODAY-ILTACON-2026).
  solution: 'Idea: usage metering by matter so that consumption-priced AI costs can be allocated, disclosed and, where permitted, billed at cost. No source describes a deployed tool. Many insurance clients are said to refuse to pay for software or AI costs while expecting the savings (TRI-BILLING-2026).'
  outcomes:
  - lever: cost
    description: none published
    figure: none published
    measures: 'n/a: no figure published'
    provenance: self-reported
    source_ref: CALBAR-GENAI-2026
  prerequisites:
  - Fee agreement language on AI costs (CALBAR-GENAI-2026, p.8).
  - Usage data per matter from the AI vendor, which consumption pricing would supply.
  risks_and_guardrails:
  - North Carolina allows AI expenses to be billed if accurate, not clearly excessive and consented to, preferably in writing; it describes them as AI use specifically tied to the client's services or a general administrative fee for generic expenses, including general technology such as AI (NCBAR-FEO1-2024, Opinion 6).
  - Lawyers may not bill learning time for a general tool; the cost of GenAI may be overhead or a per-use charge if fully explained in advance and the client consents (ABA-BLT-2024, Fees).
  - DC says any out-of-pocket AI expense to be billed should be communicated under Rule 1.5 (DCBAR-OP388-2024, section E).
  human_checkpoints:
  - Billing partner confirms that the client agreed to pass-through before the expense is billed.
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.8
  - ref: TXETHICS-OP705-2025
    title: Opinion 705 (generative AI)
    publisher: Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics
    type: professional-body
    url: https://www.legalethicstexas.com/resources/opinions/opinion-705/
    date: 2025-02
    access: full
    locator: Section 'Fees'
  - ref: NCBAR-FEO1-2024
    title: 2024 Formal Ethics Opinion 1 (use of artificial intelligence in a law practice)
    publisher: North Carolina State Bar
    type: professional-body
    url: https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/
    date: '2024-11-01'
    access: full
    locator: Inquiries on billing AI expenses and administrative fees
  - ref: ABA-BLT-2024
    title: ABA Ethics Opinion on Generative AI Offers Useful Framework (summary of Formal Opinion 512, issued 29 July 2024)
    publisher: American Bar Association, Business Law Today
    type: professional-body
    url: https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-october/aba-ethics-opinion-generative-ai-offers-useful-framework/
    date: 2024-10
    access: full
    locator: Summary, Fees
  - ref: DCBAR-OP388-2024
    title: Ethics Opinion 388 (generative AI in client matters)
    publisher: District of Columbia Bar
    type: professional-body
    url: https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388
    date: 2024-04
    access: full
    locator: Section E
  - ref: EDISCOVERYTODAY-ILTACON-2026
    title: My Five ILTACON 2026 Takeaways (Doug Austin)
    publisher: eDiscovery Today
    type: conference
    url: https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/
    date: '2026-09-04'
    access: full
    locator: Section 'Is tokengeddon looming for AI pricing?'
  - ref: TRI-BILLING-2026
    title: How one law firm is challenging a broken status quo around billing (Kopka Law)
    publisher: Thomson Reuters Institute
    type: press
    url: https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing
    date: '2026-04-30'
    access: full
    locator: '''Why the billable hour hates AI'''
  last_reviewed: '2026-10-19'
  notes: 'Idea: regulators set the conditions and a conference writer reports the pricing shift; no metering-to-billing tool was found.'
- id: professional-services-billing-collections-12
  title: Pre-bill write-down risk scoring by matter, client and timekeeper (idea)
  archetype: professional-services
  module: billing-collections
  function: finance-accounting
  work_types:
  - data-reporting
  - expert-judgment
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: Write-downs happen late and unevenly. Thomson Reuters Institute data for January to June 2025 show associate rates are discounted less before billing (91.5% worked against standard), and the report says firm leaders expect associate work to be written off more often later; litigation sees far more write-offs than transactional practices such as real estate and M&A (TRI-RATES-2026, pp.10-11). Realization has declined since 2021 (TRI-RATES-2026, p.6).
  solution: 'Idea: use historical realization, client guidelines and AI-assisted bill analysis to flag entries and matters likely to be reduced before the bill is issued, so partners adjust or explain them first. Perlin argues GenAI could help firms predict the cost of tasks and matters in advance and reduce the ''granted reductions'' that clients impose (LEGALFUTURES-PERLIN-2025). Laurel''s guideline-based flagging (use case 04) is the nearest product.'
  outcomes:
  - lever: cost
    description: none published
    figure: none published
    measures: 'n/a: no figure published'
    provenance: independent
    source_ref: GEORGETOWN-PERLIN-2025
  prerequisites:
  - Several periods of realization data by timekeeper, client and matter type (TRI-RATES-2026 shows such data exist at firm level).
  risks_and_guardrails:
  - Some discounting acts as a protective buffer for client relationships (TRI-RATES-2026, p.11); predicting write-downs should not push partners to bill at levels clients will not accept.
  - Billing must stay accurate and reasonable whatever the prediction (CALBAR-GENAI-2026, p.8).
  human_checkpoints:
  - Billing partner decides adjustments (existing step).
  role_evolution: Not described.
  evidence_grade: D
  sources:
  - ref: GEORGETOWN-PERLIN-2025
    title: How The Billable Hour Can Survive Generative AI (Jonah Perlin), Stetson Business Law Review 5(1) 42-86
    publisher: Georgetown Law (Scholarship @ Georgetown Law)
    type: academic
    url: https://scholarship.law.georgetown.edu/facpub/2694
    date: '2025'
    access: full
    locator: 'Abstract (CHRGE equation: Compensation = Hours x Rate - Granted Reductions - Expenses)'
  - ref: LEGALFUTURES-PERLIN-2025
    title: GenAI could 'reinforce rather than disrupt' the billable hour (report on the Perlin article)
    publisher: Legal Futures
    type: press
    url: https://www.legalfutures.co.uk/latest-news/genai-could-reinforce-rather-than-disrupt-the-billable-hour
    date: '2025-11-14'
    access: full
    locator: Paragraphs on write-offs
  - ref: TRI-RATES-2026
    title: Law Firm Rates Report 2026
    publisher: Thomson Reuters Institute
    type: survey
    url: https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2025/10/Law-Firm-Rates-Report-2026.pdf
    date: 2025-10
    access: full
    locator: p.6; pp.10-11, Figures 7-8
  - ref: LAUREL-BILLING-2026
    title: 'Coming Soon: Laurel Billing - Defend every bill before it goes out (Nick Bazley)'
    publisher: Laurel
    type: vendor
    url: https://www.laurel.ai/blog/coming-soon-laurel-billing
    date: '2026-08-19'
    access: full
    locator: Compliance agent description
  - ref: CALBAR-GENAI-2026
    title: Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision)
    publisher: State Bar of California, Standing Committee on Professional Responsibility and Conduct
    type: regulator
    url: https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf
    date: '2026-05-14'
    access: full
    locator: p.8
  last_reviewed: '2026-10-19'
  notes: 'Idea: scholarly argument and descriptive benchmark data, no deployment found. Realization analytics at firm level are routed to firm-finance.'
```

## 3. Module notes

### Processes and key steps (work types)

1. Time capture and entry: activity recorded, matched to client and matter, narrative written (transaction-processing, data-reporting).
2. Task coding and guideline check at entry: UTBMS codes, block-billing and staffing rules, AI-use notes (review-assurance, document-production).
3. Pre-bill review and partner adjustment: write-ups, write-downs, discounts (review-assurance, expert-judgment).
4. Invoice assembly and e-billing submission in LEDES format (transaction-processing).
5. Client review: guideline checks, rejections, reductions, appeals and resubmission (review-assurance; in-house).
6. Fee explanation and AI-value conversation with the client (client-interaction).
7. Collections: aging, reminders, escalation (transaction-processing, client-interaction).
8. Realization and leakage analysis from standard rate to collected cash (data-reporting; much of this is routed to firm-finance).

### Common pain points

- Entries reconstructed from memory at day end; accounting staff required to submit daily time by 9:00 a.m. (LAUREL-WARRENAVERETT-2026).
- Guidelines that run 15 to 100 pages per client, bills assembled by hand, and partners spending hours on pre-bills (LAUREL-BILLING-2026, vendor anecdotes).
- Under hourly billing, finishing a task faster cuts the firm's own revenue; the College of Law calls this the 'productivity paradox' (COLLAW-BILLING-2025; TRI-BILLING-2026).
- Firms cannot show matter-level AI savings: 'We're still gathering the data' (TRI-LEGALWEEK-2026).
- Clients send opposite instructions on AI: demand savings and also require permission before use (TRI-LEGALWEEK-2026, DLA Piper panel).
- Insurers and other clients run large invoice-audit operations, and defence firms build payment and appeals teams in response (TRI-BILLING-2026).
- Slower collection: inventories up 17.7% and collection cycles up 5% in H1 2026 at the Wells Fargo panel (LAWFUEL-WF-2026, secondary).

### Metrics and benchmarks (what each measures)

- **Realization by pricing posture.** Firms with disciplined pricing committees and limited pre-matter discounting maintain worked realization as high as 95%; firms using aggressive alternative fee arrangements and volume discounts can fall to 75% to 80%. Worked realization means the share of standard rates realized after negotiation (TRI-RATES-2026, p.10, Thomson Reuters Institute data, YTD June 2025).
- **Realization by title.** Associates' average worked realization against standard rates was 91.5%, above the figures for partners, which the report says are below 90% (TRI-RATES-2026, p.10, Figure 7).
- **Realization trend.** The report says firms have seen a long-term decline in realization consistent since 2021, and an unseasonal drop in collections realization in Q2 2025; worked rates started 2025 at +7.1% and reached +7.4% by end of Q2, an acceleration it says the realization drop effectively neutralized (TRI-RATES-2026, p.6).
- **Same dollars per hour.** Despite different strategies, almost all firms ended up collecting roughly the same amount per hour (TRI-RATES-2026, p.2).
- **Rates and index.** Am Law 100 worked-rate growth near 10% and demand growth of 2.7% in Q1 2026 while the Law Firm Financial Index sat flat at 55, its long-run average (TRI-LFFI-Q1-2026). None of it is attributed to AI or to billing practice.
- **Wells Fargo Legal Specialty Group, H1 2026 (secondary report).** More than 140 firms including 69 of the 100 highest-grossing: revenue +12.4%; demand, measured by lawyer hours worked, +4.8%; inventories +17.7%; collection cycles slowed by 5%; expenses +9.6%; productivity +1.8% (LAWFUEL-WF-2026). The source does not define the unit for the collection-cycle change.
- **Client-perceived savings (in-house).** Nearly 60% of about 650 in-house counsel and legal operations staff (ACC-Everlaw, fielded 18 June to 18 July 2025) saw 'no noticeable savings yet' from outside counsel's generative AI use; among those who saw a positive result, 13% pointed to fewer billable hours and 20% to better turnaround; 64% expect to bring more work in-house (BLOOMBERGLAW-ACC-2025).
- **Strategy and ROI.** A Thomson Reuters speaker said firms with a GenAI strategy are 3.9 times more likely to achieve ROI and 22% of firms have one (TRI-LEGALWEEK-2026, speaker statement).
- **Days to get paid.** An average of 97 days for law firms, cited by CollBox's co-founder from Clio data (ABAJ-TECHSHOW-2026, secondhand; not checked at Clio).
- **Accounting-firm survey (vendor).** Among firms in Uku's survey (dozens of firms in 8 countries, fielded May to June 2026), 26% would hand 'draft and send invoices' to an autonomous agent, 15% named slow or inaccurate billing as their single most-cited operational headache, 62% said trust depends on a human approving before anything is sent, and zero said they already fully trust AI (UKU-AIACCOUNTING-2026).
- **AI use and the revenue gap.** 43.6% of projects now use AI, up from 23.1% in 2025, and 84.8% of 245 organisations say AI saves them time against a locked figure for those saying it generates revenue (SPI-AI-2026, landing page).
- **Vendor customer figures.** See use case 01 (Tonkon Torp, Lerners) and Laurel's home-page claims with no denominators (LAURELSITE-2026). Brightflag says hundreds of legal departments use its AI invoice review (BRIGHTFLAG-AIINVOICE-2025). LeanLaw argues AI does not raise realization by itself and under hourly billing can lower it (LEANLAW-REALIZATION-2026, vendor commentary, no figures used).
- **Quality evidence.** None for this module's AI uses. The adjacent evidence is a US court rejecting a law firm's use of ChatGPT output to support its billing rates in a fee application (J.G. v. New York City Department of Education, S.D.N.Y., 22 Feb 2024, as described in DCBAR-OP388-2024) and the Deloitte Australia partial refund after AI-generated errors (CTV-DELOITTE-2025).

### Guardrails and regulatory points

- **Hourly = actual time.** California: hourly billing must reflect time actually spent, recognising AI may reduce time (CALBAR-GENAI-2026, p.8). DC: a lawyer may bill only the time actually spent even if AI reduces it, and cannot charge for the perceived value of the AI's work absent a prior agreement (DCBAR-OP388-2024, summary and section E). Texas: actual time using the tool may be billed, not time 'saved' (TXETHICS-OP705-2025, 'Fees'). North Carolina: a lawyer who now spends one hour instead of three may not bill three (NCBAR-FEO1-2024, Opinion 6). Australia: billed time must accurately represent the work done and AI must not unnecessarily increase costs, for example through checking time (AUSLEG-AISTATEMENT-2024, p.1).
- **ABA Formal Opinion 512 (29 Jul 2024).** Lawyers may not charge for time spent learning a general technology; GenAI cost may be overhead or charged per use if explained in advance with informed consent (ABA-BLT-2024, Fees). The opinion's hourly and flat-fee language is quoted in TRI-ABA512-2025; the opinion itself was blocked and was not read.
- **Fixed and value fees.** North Carolina: flat fee allowed if not clearly excessive and the client consents (NCBAR-FEO1-2024, Opinion 6). Virginia: value-based fees can reflect efficiency and skill, and the fee must be explained under Rule 1.5(b) (VACOURTS-LEO1901-2025, pp.2-4; VALAWYER-2026). California: fee agreements should say how fees are calculated and how far AI factors into rates (CALBAR-GENAI-2026, p.8).
- **AI costs.** California: general subscriptions are overhead; matter-specific per-use costs may be billed if disclosed in the fee agreement, at actual cost, with no markup without informed written consent (CALBAR-GENAI-2026, p.8). Texas: recover no more than actually paid (TXETHICS-OP705-2025, 'Fees').
- **Client instructions.** California says a lawyer must follow client instructions or guidelines that restrict AI (CALBAR-GENAI-2026, p.7). Zscaler's guidelines say AI work product must be reviewed by a human attorney, AI time and cost are not passed on, and discrete AI tasks should be noted in the time entry (ZSCALER-OCG-2025). The Australian statement adds that solicitors should record and disclose, if the client requests, how AI use is reflected in costs (AUSLEG-AISTATEMENT-2024, p.2).
- **Accounting.** The AICPA Code bars contingent fees for audit, review and certain other engagements, and for preparing a tax return for any client; a member's fees may vary with the complexity of services (AICPA-CODE-2026, 1.510.001, paragraphs .01 and .04). Outcome-linked billing therefore cannot be copied from consulting into those services.
- **Government contracting (T&M).** FAR 52.232-7 requires vouchers to be substantiated by individual daily job timekeeping records or other approved substantiation (FAR-52.232-7, paragraph (a)). Public-sector buyers also add AI terms: the Australian Public Service AI plan will require panel suppliers to advise planned AI use when quoting and adds clauses that contractors stay fully responsible regardless of AI use (CANBERRATIMES-APSAI-2025). Deloitte Australia agreed to a partial refund of a AU$440,000 payment after a report contained apparent AI-generated errors (CTV-DELOITTE-2025), and Canada's federal government defended a separate contract with Deloitte while a provincial premier demanded accountability (BNN-DELOITTE-2025).
- **Worker monitoring and AI Act.** The ICO has guidance on monitoring workers, marked under review (ICO-MONITORING-2026). The EU AI Act applies from 2 August 2026, with Annex III high-risk obligations extended to 2 December 2027 (EC-AIACT-2026); Annex III point 4(b) covers AI intended to monitor and evaluate worker performance and behaviour (EU-AIACT-ANNEX3-2024). Whether a time-capture tool is in scope depends on its intended use and was not tested in any source.
- **Standards.** UTBMS code sets are maintained by bodies including the ABA and the LEDES Oversight Committee; the index read lists no AI-specific code set and the LEDES site shows no proposed standards open for comment (LEDES-UTBMS-2026).
- **England and Wales.** The Law Society page says the SRA does not currently have specific generative AI guidance on use or disclosure for client care (LAWSOC-GENAI-2026). SRA pages were blocked.

### Frontier signals (dated)

- 2025-04-07: Zscaler's outside counsel billing guidelines, as revised on this date, include an AI section (ZSCALER-OCG-2025).
- 2025-10-07: Deloitte Australia to repay part of a AU$440,000 payment (CTV-DELOITTE-2025).
- 2025-11-13: Australian Public Service AI plan adds AI-use declaration and responsibility clauses for consulting suppliers (CANBERRATIMES-APSAI-2025).
- 2025-11-24: Virginia Supreme Court approves LEO 1901, disagreeing with parts of ABA 512 and North Carolina's opinion on flat fees (VACOURTS-LEO1901-2025; VALAWYER-2026).
- 2026-03-13: Legalweek 2026 panels: clients seek line-item AI transparency; some refuse to pay for AI-done work (TRI-LEGALWEEK-2026).
- 2026-03-26: CollBox wins ABA Techshow Startup Alley with an overdue-invoice recovery service (ABAJ-TECHSHOW-2026).
- 2026-05-14: California's Board of Trustees approves the revised guidance, which addresses agentic AI (CALBAR-ETHICSHUB-2026); the guidance text also sets the billing rules (CALBAR-GENAI-2026, p.8).
- 2026-08-19: Laurel announces Laurel Billing, with Compliance and Scope agents, as coming soon (LAUREL-BILLING-2026).
- 2026-08-26: Wells Fargo H1 2026 data reported: inventories up 17.7%, collection cycles slower (LAWFUEL-WF-2026).
- 2026-09-04: Seat-to-consumption AI pricing discussed at ILTACON 2026 (EDISCOVERYTODAY-ILTACON-2026).
- 2026-10-13: Legora and Laurel announce time capture from Legora and a second phase to measure AI value (LEGORA-LAUREL-2026).
- 2027-12-02 (scheduled): EU AI Act Annex III high-risk obligations apply, as extended (EC-AIACT-2026).

### Workforce and role effects

- Billers and coordinators move from re-keying partner mark-ups to approving flagged fixes; billing partners approve decisions rather than entries (LAUREL-BILLING-2026; LAUREL-BILLINGPAGE-2026, vendor description).
- Lawyers' end-of-day docketing shrinks in the Lerners account (about five minutes against 30 to 45) (LAUREL-LERNERS-2026, quote).
- Kopka Law's COO says talent is leaving defence practice partly because of the tedium of time capture (TRI-BILLING-2026, quote).
- Greenberg Traurig's Chief Pricing and Innovation Officer and DLA Piper's AI innovation lead spoke on client AI value at Legalweek; such roles exist at these firms (TRI-LEGALWEEK-2026).
- Rapoport and Tiano interviewed law firm leaders and argue the pyramid is threatened as routine work moves to technology, (WJLTA-RAPOPORT-2025, abstract).
- Partners are the commercial transmission mechanism for billing strategy; gaps between partners' views hamper firm policy (TRI-STANDOUT-2026).

### Objections and concerns practitioners raise

- The hourly model punishes efficiency; some argue to leave it (TRI-BILLING-2026; COLLAW-BILLING-2025; WJLTA-RAPOPORT-2025).
- The opposite academic view: AI may leave total billable hours largely intact, and firms still use hours to measure productivity inside alternative fee arrangements (GEORGETOWN-PERLIN-2025; LEGALFUTURES-PERLIN-2025).
- ABA 512's flat-fee test is criticised for treating time taken as the benchmark of value and inviting buyers' remorse (William Josten, TRI-ABA512-2025); Virginia criticises the same line (VACOURTS-LEO1901-2025).
- Clients are not seeing savings (ACC-Everlaw) and suspect rate increases offset them; one general counsel asked whether savings are offset by higher partner rates (BLOOMBERGLAW-ACC-2025; TRI-STANDOUT-2026).
- Using AI mainly to justify higher billing exposes firms if clients tighten budgets (TRI-SOTLM-2026).
- Trust: accounting firms in a vendor survey want a human to approve before anything is sent (UKU-AIACCOUNTING-2026).
- Verification time: the Australian regulators say AI should not unnecessarily raise costs above traditional methods, for example through time spent checking its output (AUSLEG-AISTATEMENT-2024, p.1).
- Consumption-based AI pricing could turn AI into a variable matter cost; vendors were reluctant to discuss it (EDISCOVERYTODAY-ILTACON-2026).

### Interview probes for an advisor

1. When AI shortens a task, how does your time entry show who did what and for how long, and who certifies the entry before it is released?
2. Which client guidelines on AI (disclosure, no pass-through, approved tools, savings expected) do you hold today, and how do they reach the people who write time entries and assemble bills?
3. Last year, which bills were reduced, rejected or written down, by which rule, and could a pre-bill check have caught them? Can you see write-down rates by client, practice and timekeeper?
4. If a tool captured time from email, documents and calls, what would your data protection officer, employee representatives and clients say, and who decides?
5. How many days pass from work done to cash at each stage (capture, pre-bill, issue, client approval, payment), and which stage would you measure first?

## 4. Routed to other modules

- **scoping-pricing:** conversion of hourly work to flat, value or retainer fees and the state-by-state rule differences (CALBAR-GENAI-2026; NCBAR-FEO1-2024; VACOURTS-LEO1901-2025; TRI-ABA512-2025); Kopka Law's KPI-based retainer billing (TRI-BILLING-2026); the AICPA contingent-fee rule and pricing models for consulting (AICPA-CODE-2026; STANFORD-DEL-2026); fee-agreement wording on AI use.
- **firm-finance:** realization and leakage analytics from standard rate to collected cash (TRI-RATES-2026); Wells Fargo and Thomson Reuters Institute market data (LAWFUEL-WF-2026; TRI-LFFI-Q1-2026); firm-level AI ROI measurement and the SPI 'leak' (SPI-AI-2026; LAURELSITE-2026, Signal); consumption-priced AI as a variable cost (EDISCOVERYTODAY-ILTACON-2026); the argument that rate rises justified by AI create exposure (TRI-SOTLM-2026).
- **quality-review:** the court's rejection of ChatGPT as support for billing rates and the Deloitte Australia refund (DCBAR-OP388-2024; CTV-DELOITTE-2025); verification duties (CALBAR-GENAI-2026).
- **acceptance-risk:** AI-use declarations and responsibility clauses in public-sector supplier terms (CANBERRATIMES-APSAI-2025); client-approved tool lists in guidelines (LAYER3-AIOCG-2026).
- **talent-learning:** the pyramid and junior leverage under AI (WJLTA-RAPOPORT-2025); talent loss tied to time capture (TRI-BILLING-2026); non-billable learning time for tools (ABA-BLT-2024).
- **client-development:** partners not discussing AI with clients and the general counsel's question on partner rates (TRI-STANDOUT-2026).
- **Assurance and tax archetypes:** the contingent-fee rule for audit, review and tax-return work is recorded here only as a billing constraint (AICPA-CODE-2026).

## 5. Sources

Access is `full` unless stated (opened and read; the Brightflag post was read through a text mirror because the site blocked curl). One source, WK-CLM-2026, was seen only in a search result and is used in notes only. Dates are publication or event dates from page metadata or bylines unless noted; the Laurel customer-story pages all show 21 Aug 2026; LAWSOC-GENAI-2026 carries no date (April 2026 is the latest event it cites); TRI-RATES-2026 is dated from its October 2025 PDF metadata; ICO-MONITORING-2026 and EC-AIACT-2026 are live pages read in October 2026. ZSCALER-OCG-2025 is typed `firm` because it is a client's own primary document and no closer type exists.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ABA-BLT-2024 | ABA Ethics Opinion on Generative AI Offers Useful Framework (summary of Formal Opinion 512, issued 29 July 2024) | American Bar Association, Business Law Today | professional-body | https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-october/aba-ethics-opinion-generative-ai-offers-useful-framework/ | 2024-10 | full |
| ABAJ-TECHSHOW-2026 | AI-powered bill collector program takes top spot at ABA Techshow's Startup Alley | ABA Journal | conference | https://www.abajournal.com/web/article/tool-that-gets-lawyers-paid-takes-top-spot-at-techshows-startup-alley | 2026-03-26 | full |
| AICPA-CODE-2026 | AICPA Code of Professional Conduct (edition updated through July 2026) | AICPA | standard-setter | https://mn.gov/boa/assets/AICPA%20Code%20of%20Professional%20Conduct_tcm1233-764395.pdf | 2026-07 | full |
| AUSLEG-AISTATEMENT-2024 | Statement on the Use of Artificial Intelligence in Australian Legal Practice | Law Society of New South Wales, Legal Practice Board of Western Australia, Victorian Legal Services Board + Commissioner | regulator | https://www.lawsociety.com.au/sites/default/files/2024-12/LS4590_PSP_Statement_AI_LawSocietyVersion.pdf | 2024-12 | full |
| BLOOMBERGLAW-ACC-2025 | AI Does Little to Reduce Law Firm Billable Hours, Survey Shows (ACC-Everlaw survey) | Bloomberg Law | press | https://news.bgov.com/business-and-practice/ai-does-little-to-reduce-law-firm-billable-hours-survey-shows | 2025-10-14 | full |
| BNN-DELOITTE-2025 | Feds defend $1.1-million Deloitte contract for AI advice after firm admitted mistakes (Canadian Press) | BNN Bloomberg | press | https://www.bnnbloomberg.ca/business/company-news/2025/12/18/feds-defend-11-million-deloitte-contract-for-ai-advice-after-firm-admitted-mistakes/ | 2025-12-18 | full |
| BRIGHTFLAG-AIINVOICE-2025 | Legal AI Invoice Review Explained (Sinead Kenny; updated 24 Jul 2025) | Brightflag | vendor | https://brightflag.com/resources/ai-invoice-review-how-it-works/ | 2025-07-22 | full |
| CALBAR-ETHICSHUB-2026 | Ethics and technology resources (notes Board of Trustees approval of the revised guidance on 14 May 2026) | State Bar of California | regulator | https://www.calbar.ca.gov/Attorneys/Conduct-Discipline/Ethics/Ethics-Technology-Resources | 2026-05-14 | full |
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative Artificial Intelligence in the Practice of Law (2026 revision) | State Bar of California, Standing Committee on Professional Responsibility and Conduct | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05-14 | full |
| CANBERRATIMES-APSAI-2025 | What the public service's new AI plan means for external contractors (Brittney Levinson) | The Canberra Times | press | https://www.canberratimes.com.au/story/9110516/new-ai-plan-for-the-aps-sets-out-expectations-for-contractors/ | 2025-11-13 | full |
| COLLAW-BILLING-2025 | A guide to balancing AI-era billing with the Australian Solicitor's Conduct Rules (ASCR) | College of Law (Australia) | press | https://www.collaw.edu.au/community/news/a-guide-to-balancing-ai-era-billing-with-the-legal-professional-conduct-rules/ | 2025-12-02 | full |
| CTV-DELOITTE-2025 | Deloitte to partially refund Australian government for report with apparent AI-generated errors (Associated Press) | CTV News | press | https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ | 2025-10-07 | full |
| DCBAR-OP388-2024 | Ethics Opinion 388 (generative AI in client matters) | District of Columbia Bar | professional-body | https://www.dcbar.org/for-lawyers/legal-ethics/ethics-opinions-210-present/ethics-opinion-388 | 2024-04 | full |
| EC-AIACT-2026 | AI Act: regulatory framework for AI (application timeline) | European Commission | regulator | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-10 | full |
| EDISCOVERYTODAY-ILTACON-2026 | My Five ILTACON 2026 Takeaways (Doug Austin) | eDiscovery Today | conference | https://ediscoverytoday.com/2026/09/04/my-five-iltacon-2026-takeaways-legal-technology-trends/ | 2026-09-04 | full |
| EU-AIACT-ANNEX3-2024 | Annex III: High-risk AI systems referred to in Article 6(2) (online text of Regulation (EU) 2024/1689) | artificialintelligenceact.eu | regulator | https://artificialintelligenceact.eu/annex/3/ | 2024-08 | full |
| FAR-52.232-7 | FAR 52.232-7 Payments under Time-and-Materials and Labor-Hour Contracts (Nov 2021 clause text) | Acquisition.gov (US federal government) | regulator | https://www.acquisition.gov/far/52.232-7 | 2021-11 | full |
| GEORGETOWN-PERLIN-2025 | How The Billable Hour Can Survive Generative AI (Jonah Perlin), Stetson Business Law Review 5(1) 42-86 | Georgetown Law (Scholarship @ Georgetown Law) | academic | https://scholarship.law.georgetown.edu/facpub/2694 | 2025 | full |
| ICO-MONITORING-2026 | Employment practices and data protection: monitoring workers (page marked under review) | UK Information Commissioner's Office | regulator | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/ | 2026-10 | full |
| LAUREL-BILLING-2026 | Coming Soon: Laurel Billing - Defend every bill before it goes out (Nick Bazley) | Laurel | vendor | https://www.laurel.ai/blog/coming-soon-laurel-billing | 2026-08-19 | full |
| LAUREL-BILLINGPAGE-2026 | Laurel Billing product page ('Billing - coming soon'; read 19 Oct 2026) | Laurel | vendor | https://www.laurel.ai/platform/billing | 2026-10-19 | full |
| LAUREL-LERNERS-2026 | How Lerners repaired client service issues, netting out to zero billing disputes (customer story) | Laurel | vendor | https://www.laurel.ai/customer-stories/lerners | 2026-08-21 | full |
| LAUREL-TONKON-2026 | Tonkon Torp LLP embraces Laurel for superior client service and timekeeper happiness (customer story; page date shown as Aug 21, 2026, the same date as the other customer stories) | Laurel | vendor | https://www.laurel.ai/customer-stories/tonkon-torp | 2026-08-21 | full |
| LAUREL-WARRENAVERETT-2026 | How Warren Averett turned time entry into a competitive advantage (customer story) | Laurel | vendor | https://www.laurel.ai/customer-stories/warren-averett | 2026-08-21 | full |
| LAURELSITE-2026 | Laurel home page: AI Timekeeping and Work Intelligence Platform (read 19 Oct 2026) | Laurel | vendor | https://www.laurel.ai | 2026-10-19 | full |
| LAWFUEL-WF-2026 | US Law Firm Revenue Jumps 12.4% in First Half of 2026 as AI Work Drives Demand (reports Wells Fargo Legal Specialty Group figures) | LawFuel | press | https://www.lawfuel.com/?p=194355 | 2026-08-26 | full |
| LAWSOC-GENAI-2026 | Generative AI - the essentials (page is undated; latest event it cites is April 2026) | Law Society of England and Wales | professional-body | https://www.lawsociety.org.uk/topics/ai-and-lawtech/generative-ai-the-essentials | 2026-04 | full |
| LAYER3-AIOCG-2026 | AI Provisions in Outside Counsel Guidelines: A Compliance Guide for Law Firms (updated 7 Sep 2026) | Layer3 Labs | vendor | https://www.layer3labs.io/guides/ai-provisions-outside-counsel-guidelines | 2026-09-07 | full |
| LAYER3-OCG-2026 | Outside Counsel Billing Guidelines: plain-language guide (reviewed, updated 7 Jul 2026) | Layer3 Labs | vendor | https://www.layer3labs.io/guides/outside-counsel-billing-guidelines | 2026-07-07 | full |
| LEANLAW-REALIZATION-2026 | How AI Changes Your Law Firm's Realization Rate | LeanLaw | vendor | https://www.leanlaw.co/blog/how-ai-changes-your-law-firms-realization-rate/ | 2026-07-08 | full |
| LEDES-UTBMS-2026 | LEDES Oversight Committee site (ledes.org) and UTBMS.com code-set index, read 19 Oct 2026 | LEDES Oversight Committee | standard-setter | https://ledes.org/ ; https://www.utbms.com/ | 2026-10 | full |
| LEGALFUTURES-PERLIN-2025 | GenAI could 'reinforce rather than disrupt' the billable hour (report on the Perlin article) | Legal Futures | press | https://www.legalfutures.co.uk/latest-news/genai-could-reinforce-rather-than-disrupt-the-billable-hour | 2025-11-14 | full |
| LEGORA-LAUREL-2026 | Legora and Laurel partner to capture the time lawyers spend in Legora as they work | Legora | vendor | https://legora.com/newsroom/legora-and-laurel-partner-to-capture-the-time-lawyers-spend-in-legora-as-they-work | 2026-10-13 | full |
| NCBAR-FEO1-2024 | 2024 Formal Ethics Opinion 1 (use of artificial intelligence in a law practice) | North Carolina State Bar | professional-body | https://www.ncbar.gov/for-lawyers/ethics/adopted-opinions/2024-formal-ethics-opinion-1/ | 2024-11-01 | full |
| SPI-AI-2026 | 2026 Impact of AI on Professional Services (report landing page) | SPI Research | survey | https://spiresearch.com/reports/2026-ai-professional-services-survey/ | 2026-10 | full |
| STANFORD-DEL-2026 | Pricing Consulting Services in the Age of Agentic AI: A Strategy Map for Executives | Stanford Digital Economy Lab (Brynjolfsson) and USC Marshall (Petropoulos) | academic | https://digitaleconomy.stanford.edu/app/uploads/2026/08/AI_Agents_and_Consulting_Service_Pricing.pdf | 2026-08-23 | full |
| TRI-ABA512-2025 | Is ABA Formal Opinion 512 off the mark? And if so, what can law firms and GCs do about it? (William Josten; quotes the opinion) | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/aba-formal-opinion-512 | 2025-04-02 | full |
| TRI-BILLING-2026 | How one law firm is challenging a broken status quo around billing (Kopka Law) | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/institute/articles/broken-status-quo-around-billing | 2026-04-30 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: Firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-LFFI-Q1-2026 | Q1 2026 LFFI: Strong inputs, average output - and the first drops of rain | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/articles/lffi-q1-2026-strong-inputs-average-output | 2026-05-13 | full |
| TRI-RATES-2026 | Law Firm Rates Report 2026 | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2025/10/Law-Firm-Rates-Report-2026.pdf | 2025-10 | full |
| TRI-SOTLM-2026 | 2026 State of the US Legal Market: AI value vs AI bubble analysis | Thomson Reuters Institute with Georgetown Law Center on Ethics and the Legal Profession | survey | https://www.thomsonreuters.com/en/institute/articles/legal-market-report-2026-analysis-ai-bubble | 2026-01-14 | full |
| TRI-STANDOUT-2026 | Turning law firm AI strategies into practice (2026 Stand-out Lawyers Survey) | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/turning-law-firm-ai-strategies-into-practice | 2026-08-06 | full |
| TXETHICS-OP705-2025 | Opinion 705 (generative AI) | Professional Ethics Committee for the State Bar of Texas, via Texas Center for Legal Ethics | professional-body | https://www.legalethicstexas.com/resources/opinions/opinion-705/ | 2025-02 | full |
| UKU-AIACCOUNTING-2026 | AI in Accounting 2026: What Real Firms Actually Think (Uku report landing page) | Uku | survey | https://getuku.com/ai-in-accounting-report/ | 2026-06 | full |
| VACOURTS-LEO1901-2025 | Order approving Legal Ethics Opinion 1901 (full opinion text) | Supreme Court of Virginia | regulator | https://www.vacourts.gov/static/courts/scv/amendments/leo_1901.pdf | 2025-11-24 | full |
| VALAWYER-2026 | Using AI in the Face of Rule 1.5: Reasonableness and Client Communication (Genevieve Leah Sankar), Virginia Lawyer, February 2026 issue | Virginia State Bar (Virginia Lawyer magazine) | professional-body | https://virginialawyer.vsb.org/articles/using-ai-in-the-face-of-rule-1-5-reasonableness-and-client-communication | 2026-01-21 | full |
| VSB-LEO1901-2025 | Adopted: Legal Ethics Opinion 1901, Reasonable Fees and the Use of Generative Artificial Intelligence (page with comment and petition history) | Virginia State Bar | regulator | https://vsb.org/Site/news/rules-news/20250327-prop-1901-fees-ai.aspx | 2025-11-25 | full |
| WJLTA-RAPOPORT-2025 | Fighting the Hypothetical: Why Law Firms Should Rethink the Billable Hour in the Generative AI Era (Rapoport and Tiano), 20 Wash. J. L. Tech. & Arts 41 | University of Washington School of Law, Washington Journal of Law, Technology & Arts | academic | https://digitalcommons.law.uw.edu/wjlta/vol20/iss2/2 | 2025 | full |
| WK-CLM-2026 | 2026 CLM Alliance Litigation Management Study (seen in a search result; page returned 403) | Wolters Kluwer | survey | https://www.wolterskluwer.com/en/expert-insights/report-2026-clm-alliance-litigation-management-study | 2026-07-06 | search-only |
| ZSCALER-OCG-2025 | Outside Counsel Billing Guidelines (revised April 7, 2025); a client (in-house) primary document | Zscaler, Inc. | firm | https://www.zscaler.com/legal/outside-counsel-billing-guidelines | 2025-04-07 | full |

## 6. Gaps

- **Blocked or not reachable:** ABA Formal Opinion 512 text (americanbar.org returned a bot challenge; read through TRI-ABA512-2025 and ABA-BLT-2024), SRA pages (Cloudflare challenge), DCAA guidance (403), Clio Legal Trends reports (403), the ACC sample AI guidelines for outside counsel (403, members-only; its billing wording is unconfirmed), the Wolters Kluwer CLM Alliance study and CFO guide (403), Florida Bar Opinion 24-1 (page had no body text), NYC Bar Formal Opinion 2024-5 (page had no body text), Brightflag's main site (blocked; one post read through a mirror).
- **Not found:** any published error, override, false-flag or parallel-run rate for AI time capture, narrative drafting, pre-bill review or collection agents; any independent (non-vendor) measurement of recovered time; any bar or court statement on AI-drafted time entries as such; any UTBMS or LEDES AI task code or open proposal; any court decision cutting a fee petition because of AI-assisted time (a search found none); regulator or standard-setter guidance on AI collection reminders; named customers for Brightflag or CollBox; consulting-firm billing practices; AICPA, MCA or ICAEW guidance on AI and billing.
- **Not read:** Pennsylvania, Michigan, Oregon and other state opinions beyond the five texts above; the Citi Hildebrandt and primary Wells Fargo surveys; Gartner and Forrester reports; Thomson Reuters Institute's full Law Firm Rates Report sample description (sample size not confirmed in the PDF); the full SPI 2026 report (paywalled); older vendor surveys on lost billable time (seen only in search snippets).
- **Sector skew:** most governance material is US and Australian legal ethics. Accounting is one code edition, one vendor survey and one customer story; consulting is public-sector procurement and two press items; architecture and engineering is one vendor product line. In-house evidence is one public client guideline, one survey and vendor material.
- **Provenance cautions:** Laurel customer stories are vendor pages with undefined baselines and the same page date; the Tonkon Torp story gives 20 and 21 minutes in different places and 20% in two forms. The 97-day figure and the Wells Fargo figures are secondhand. CollBox's description in the ABA Journal headline (AI-powered) is broader than the pitch text. Zscaler's guidelines show one client's terms and cannot be generalised.
- **Search budget:** eleven web searches were used (rates and realization, guidelines and e-billing, court fee awards, DCAA timekeeping, time-capture studies, academic papers, UK guidance, legal spend management, accounting billing, the ACC sample, collections automation).
