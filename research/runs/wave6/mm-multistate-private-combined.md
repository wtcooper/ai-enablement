# Multistate tax for growing private companies (tax archetype, mid-market extension): combined deep dive

Researched 2026-10-21. Module `multistate-private`. Angles: practice, discourse, governance and evidence, in one pass because public evidence on this module is thin. Working files were kept in a private temp folder. Source refs reuse the archetype's refs where the same document is already cited (for example `SCPOST-AUDIT-2026`, `TAXNOTES-UNWATCHED-2026`, `NTT-BIAS-2026`, `CDTFA-2025`, `KTS-OPR-2026`, `BYRON-2026`, `VALS-TAXAGENT-2026`); `MTC-ANNUAL-2026`, `WITHUM-SEATA-2026` and `SALESTAX-AIAUDIT-2026` follow the landscape file.

## 1. Summary

- **The evidence is almost entirely about the counterparty.** The best public material on this module describes what state tax agencies do with AI (South Carolina, California's Franchise Tax Board, New York), not what accounting firms or in-house teams do. For the firm and in-house side, no named mid-market firm, no measured result, and no error, override or parallel-run figure was found. Every firm-side entry here is a vendor claim (C) or an idea (D).
- **No firm-side SALT AI deployment is documented.** Baker Tilly's sales and use tax page (opened) mentions technology but not AI and its income and franchise tax page (opened) has no AI mention; search summaries of Citrin Cooperman, Aprio and Frazier & Deeter SALT pages and job listings showed nexus, apportionment and voluntary disclosure services described without AI (Citrin's own page returned 403). The one firm-side thread that is concrete is Moss Adams (now part of Baker Tilly) publishing SALT guidance for AI companies as clients (demand created by AI, not AI used in the work).
- **State agency AI is real but patchy and hard to see.** A Tax Notes survey of 49 state and jurisdictional agencies in 2025 got 36 replies: 22 said they use no AI, 7 said they use some, 6 said they were interested [TAXNOTES-UNWATCHED-2026]. The FTA's chief operating officer says most agencies have used older machine learning for years for return processing and fraud detection [TAXNOTES-UNWATCHED-2026]. New York's tax department says its case selection system is not AI [NTT-BIAS-2026]. Counting "AI use" is therefore unreliable.
- **Specific, named state deployments found:** South Carolina DOR's FAST Enterprises audit-selection contract (starting with business filings, sales and use tax first) [SCPOST-AUDIT-2026]; California FTB machine-learning models in service since 2021 [NTT-BIAS-2026]; New York's CISS (disputed as AI) [NTT-BIAS-2026]; California CDTFA's call-centre generative AI (routed to controversy) [CDTFA-PR-2025].
- **Volume baseline for voluntary disclosure.** The Multistate Tax Commission's National Nexus Program reports 464 executed agreements and $28.3 million collected in FY2026, mostly sales tax economic nexus [MTC-NEXUSDIR-2026]. Neither MTC program report mentions AI.
- **Quality evidence.** None for a commercial multistate AI tool. One adjacent independent item: the Vals Tax Agent Bench includes SALT questions inside a mostly federal corporate set and traces 18 models on one New York versus California pass-through entity tax question; scores varied from 76.5% to 91% for the models named, and one model passed all 18 checks [VALS-TAXAGENT-2026]. No SALT-only score is published.
- **Counts.** 13 use cases: 0 grade A, 1 grade B, 8 grade C, 4 grade D (labelled ideas). 40 sources across 8 source types (section 5).

## 2. Use cases

```yaml
- id: tax-multistate-private-01
  title: State tax agencies score returns and select audits with machine-learning models inside their core tax systems
  archetype: tax
  module: multistate-private
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    State agencies cannot manually review the millions of returns they receive. South Carolina's deputy director
    cites 5 to 6 million returns (SCPOST-AUDIT-2026). For a private multistate company this is the counterparty's side:
    selection criteria are not published, and taxpayers have few tools to challenge being selected (TAXNOTES-UNWATCHED-2026).
    Overlaps tax-controversy-15, which covers tax-authority risk targeting in general; this entry adds state detail
    for multistate taxpayers.
  solution: >-
    South Carolina's DOR signed a $3.5 million, five-year contract in December with FAST Enterprises for audit services
    that work with its GenTax system. The deputy director says it applies the department's existing methodology faster.
    It starts with business filings, sales and use tax first and then corporate returns; it could later extend to
    individual returns and look back up to three years where problems are flagged. The system suggests where audits
    should happen rather than conducting them (SCPOST-AUDIT-2026). Tax Notes reporters say California's Franchise Tax
    Board began using machine-learning models in 2021 to help decide which returns to pursue, with flagged items going
    to other automated systems or to staff (NTT-BIAS-2026). New York says its Case Identification and Selection System
    (built under an IBM contract) uses business rules and analytics, not AI; a researcher the reporters spoke to
    disagreed (NTT-BIAS-2026).
  outcomes:
    - {lever: risk, description: "Share of responding state tax agencies that reported using AI in tax operations", figure: "7 of 36 responding agencies", measures: "agencies that said they used AI programs, from chatbots to machine learning, among 36 that replied to Tax Notes' 2025 survey of 49 state and jurisdictional agencies; 22 said none, 6 were interested (some overlapping with the 22), 3 did not disclose", provenance: independent, source_ref: TAXNOTES-UNWATCHED-2026}
    - {lever: risk, description: "California agencies that reported a high-risk automated decision system in the 2025 AB 302 inventory", figure: "0 agencies", measures: "agencies reporting a high-risk system to the California Department of Technology, as described by Tax Notes reporters; experts told them this was not credible given the FTB models", provenance: independent, source_ref: NTT-BIAS-2026}
    - {lever: quality, description: "No audit-yield, no-change-rate or false-positive figure was published by South Carolina, California or New York in the sources read", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: SCPOST-AUDIT-2026}
  prerequisites:
    - "A core tax system holding the data and a vendor audit module that works with it; South Carolina's process is closed-loop between GenTax and the audit review system, with data held by the vendor already (SCPOST-AUDIT-2026)"
    - "Years of vendor vetting; the SC deputy director says the department vetted vendors for three or four years (SCPOST-AUDIT-2026)"
  risks_and_guardrails:
    - "Selection criteria are not public. Tax Notes reporters found no outside audit or legislative report of California's FTB models, though the FTB runs internal checks for over-selection from certain groups (NTT-BIAS-2026)"
    - "Whether a system counts as AI is contested, which affects which oversight laws apply (New York CISS); Tax Notes reports internal confusion about what is and is not AI (NTT-BIAS-2026; TAXNOTES-UNWATCHED-2026)"
    - "Experts quoted in the South Carolina story stress human oversight at every step and warn of opaque algorithms and unintended discriminatory results (SCPOST-AUDIT-2026; KOGOD-SC-2026)"
    - "Taxpayers face an asymmetry: faster agency outreach, but no matching upgrade to the channel for disputing it (NTT-BIAS-2026)"
  human_checkpoints:
    - "South Carolina: the system suggests audits; auditors conduct them (SCPOST-AUDIT-2026)"
    - "California: flagged items go to staff or to further automated processing (NTT-BIAS-2026)"
  role_evolution: >-
    The FTA's chief operating officer expects training to be the main workforce need and says the tools are unlikely to
    take jobs soon (TAXNOTESTALK-2025). South Carolina's deputy director says it is unclear whether the system will
    lead to more audits; the aim is a better hit rate and fewer audits ending in no change (SCPOST-AUDIT-2026).
  evidence_grade: B
  sources:
    - {ref: SCPOST-AUDIT-2026, title: "SCDOR to use AI to help decide which tax returns to audit", publisher: "Post and Courier", type: press, url: "https://www.postandcourier.com/news/sc-taxes-artificial-intelligence-audits-fast-scdor/article_54662d56-ae30-4130-845a-366547409477.html", date: "2026-04-12", access: full, locator: "article text, paragraphs on the FAST contract, scope and lookback"}
    - {ref: NTT-BIAS-2026, title: "How AI Bias Affects State Audit Selection", publisher: "Tax Notes Talk (Tax Analysts)", type: podcast, url: "https://taxnotestalk.taxnotes.com/124942/episodes/19216367-how-ai-bias-affects-state-audit-selection", date: "2026-05-22", access: full, locator: "transcript: California FTB and New York CISS case studies; AB 302 discussion"}
    - {ref: TAXNOTES-UNWATCHED-2026, title: "Tax Notes Investigates States' Use of AI in Audit Selection (excerpting Tax Notes, 14 Apr 2026)", publisher: "TaxProf Blog", type: press, url: "https://taxprofblog.aals.org/?p=134442", date: "2026-05-02", access: full, locator: "excerpt: survey results and Minnick quote"}
    - {ref: KOGOD-SC-2026, title: "Artificial Intelligence Being Used by SC Department of Revenue to Determine Who to Audit this Year", publisher: "Kogod Tax Policy Center, American University", type: academic, url: "https://kogod.american.edu/news/artificial-intelligence-being-used-by-sc-department-of-revenue-to-determine-who-to-audit-this-year", date: "2026-04-29", access: full, locator: "summary of the Post and Courier story"}
    - {ref: TAXNOTESTALK-2025, title: "Artificial Intelligence and State Tax Agencies", publisher: "Tax Notes Talk (Tax Analysts)", type: podcast, url: "https://taxnotestalk.taxnotes.com/124942/episodes/17439828-artificial-intelligence-and-state-tax-agencies", date: "2025-07-04", access: full, locator: "Minnick interview on training and workforce"}
  last_reviewed: "2026-10-21"
  notes: >-
    Kogod's summary calls the SC tool machine-learning models inside GenTax; the Post and Courier article says AI and
    describes scoring against what is typical for a business type. Tax Notes' NTT transcript says one estimate in 2012
    credited the New York system with helping collect more than $2 billion; the source is a reporter's recollection and
    the system is not confirmed as AI, so it is not used as an outcome. A search-snippet-only item (Route Fifty, 2026-07)
    says Vermont has identified AI tools for tax-fraud risk detection and Michigan has proposed funding for AI analytics
    in Treasury; that piece is a vendor executive's commentary and is not used for grading.

- id: tax-multistate-private-02
  title: States match third-party data with filings to find unregistered businesses, non-filers and remote sellers
  archetype: tax
  module: multistate-private
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    A growing company can create state tax obligations (income or franchise, withholding, sales) in states where it is
    not registered. Practitioner and vendor commentary says states are getting better at spotting this by connecting
    filing, marketplace, payment and payroll data (STI-AIAUDITS-2026; SALESTAX-AIAUDIT-2026).
  solution: >-
    The Sales Tax Institute's webinar listing says AI is already used to improve audit selection, detect fraud,
    identify non-filers and uncover unregistered remote sellers by linking previously siloed data, while saying state
    authorities are earlier in their AI journey than the IRS (STI-AIAUDITS-2026). A consultancy blog lists signals it
    says state systems weigh: payment processor totals against reported sales, marketplace reports, nexus thresholds,
    exemption certificate gaps and filing pattern changes (SALESTAX-AIAUDIT-2026). An Avalara report summarised in the
    trade press says states facing staffing shortfalls are looking to AI to multiply audit teams (AVALARA-TRENDS-2025).
    Withum's recap of the 2026 SEATA meeting says commissioners and revenue agents from eight Southeastern states
    described AI and analytics for risk identification, audit selection and fraud detection; the recap's state-by-state
    "why it matters" lines are Withum's own reading (WITHUM-SEATA-2026).
  outcomes:
    - {lever: risk, description: "No state publishes detection yield for this data matching in the sources read", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: STI-AIAUDITS-2026}
  prerequisites:
    - "State access to third-party data (marketplace, payment, federal data-sharing); the consultancy blog names these but does not document each state's access (SALESTAX-AIAUDIT-2026)"
  risks_and_guardrails:
    - "The strongest claims come from sales-tax consultancies and a training provider that sell compliance help; the consultancy blog is advocacy in tone and names no state document (SALESTAX-AIAUDIT-2026)"
    - "Counter-evidence: 22 of 36 responding agencies said they use no AI in tax operations (TAXNOTES-UNWATCHED-2026)"
    - "Mostly a sales tax story; the sales tax side is covered in indirect-tax (see section 4)"
  human_checkpoints:
    - "None described; the sources discuss detection and do not describe how agency staff review flags"
  role_evolution: >-
    Withum's recap advises documentation, accurate reporting and periodic tax health checks as states identify issues
    earlier (WITHUM-SEATA-2026).
  evidence_grade: C
  sources:
    - {ref: STI-AIAUDITS-2026, title: "AI in State Tax: New Tools, Familiar Risks (live webinar listing)", publisher: "Sales Tax Institute", type: vendor, url: "https://www.salestaxinstitute.com/sales-tax-education/ai-in-state-tax-audits", date: "2026-06-25", access: full, locator: "course description, first two paragraphs"}
    - {ref: SALESTAX-AIAUDIT-2026, title: "Are You Using AI to Find Businesses That Aren't Paying Sales Tax? Here's What That Means for You", publisher: "The Sales Tax People", type: firm, url: "https://sales.tax/sales-tax-updates/states-ai-sales-tax-audits-enforcement-2026/", date: "2026-05-18", access: full, locator: "section on what the scoring looks for"}
    - {ref: AVALARA-TRENDS-2025, title: "Avalara Report Shows Sales Tax Simplification Efforts, States Eyeing AI to Shore Up Audit Teams, and E-Invoicing Growth in 2025", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2025/01/21/avalara-report-shows-sales-tax-simplification-efforts-states-eyeing-ai-to-shore-up-audit-teams-and-e-invoicing-growth-in-2025/154946/", date: "2025-01-21", access: full, locator: "section 'States look to AI to boost audit efforts'"}
    - {ref: WITHUM-SEATA-2026, title: "Key Takeaways From the 2026 SEATA Conference", publisher: "Withum", type: firm, url: "https://www.withum.com/resources/key-takeaways-from-the-2026-seata-conference/", date: "2026-07-14", access: full, locator: "intro and 'The Bottom Line' (read via mirror)"}
    - {ref: TAXNOTES-UNWATCHED-2026, title: "Tax Notes Investigates States' Use of AI in Audit Selection (excerpting Tax Notes, 14 Apr 2026)", publisher: "TaxProf Blog", type: press, url: "https://taxprofblog.aals.org/?p=134442", date: "2026-05-02", access: full, locator: "excerpt: survey results"}
  last_reviewed: "2026-10-21"
  notes: >-
    The STI listing was last modified 2026-09-25 and, per a search result, the live session was set for 24 Sep 2026; the
    page text read does not show the date, so the session is cited only as a listing. Withum's recap also reports
    Alabama working to automate collections and lien processes and Arkansas using analytics for fraud identification;
    neither is described as AI.

- id: tax-multistate-private-03
  title: Residency and remote-worker income tax audits use analytics and mass letters (New York example)
  archetype: tax
  module: multistate-private
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Employees who work from a low-tax state for a high-tax-state employer, and individuals who say they moved, are an
    income tax and withholding exposure for owners and employers of growing private companies. New York's convenience
    of the employer rule is still being litigated (MTC-NEXUSUPD-2026).
  solution: >-
    A 2024 report summarised by Yahoo from CNBC says New York has been sending hundreds of thousands of AI-generated
    letters, mostly to wealthy people who say they have changed residency, and that a SALT lawyer says tax departments
    use human auditors and AI to examine cellphone records to see where people spend time (YAHOO-NYAI-2024). New York's
    department says its selection system is not AI (NTT-BIAS-2026), so the AI label is disputed.
  outcomes:
    - {lever: capacity, description: "Audits and auditors in New York in 2022, as reported", figure: "771,000 audits (up 56% on 2021); auditors down 5% to under 200", measures: "audits per a New York Department of Taxation and Finance report cited by CNBC and repeated by Yahoo; what counts as an audit and the AI share are not stated", provenance: self-reported, source_ref: YAHOO-NYAI-2024}
  prerequisites:
    - "Access to third-party location and asset data; the lawyer quoted says cellphone records are used (YAHOO-NYAI-2024); not otherwise documented"
  risks_and_guardrails:
    - "The AI claim is secondhand and the department denies its selection system is AI (NTT-BIAS-2026)"
    - "Source is from April 2024, older than the 12 to 18 month window; kept as a foundation for the remote-worker thread"
  human_checkpoints:
    - "None described in the source"
  role_evolution: >-
    The report ties higher audit volume to fewer auditors (YAHOO-NYAI-2024).
  evidence_grade: C
  sources:
    - {ref: YAHOO-NYAI-2024, title: "New York and other states are using AI to hunt down wealthy remote workers and demand more tax", publisher: "Yahoo (summarising CNBC)", type: press, url: "https://news.yahoo.com/tech/york-other-states-using-ai-112406645.html", date: "2024-04-16", access: full, locator: "paragraphs 2-9"}
    - {ref: NTT-BIAS-2026, title: "How AI Bias Affects State Audit Selection", publisher: "Tax Notes Talk (Tax Analysts)", type: podcast, url: "https://taxnotestalk.taxnotes.com/124942/episodes/19216367-how-ai-bias-affects-state-audit-selection", date: "2026-05-22", access: full, locator: "New York CISS segment"}
    - {ref: MTC-NEXUSUPD-2026, title: "Nexus Program Director's Update on Nexus Law Developments Since April 22, 2026 (for the 27 Jul 2026 meeting)", publisher: "Multistate Tax Commission", type: regulator, url: "https://www.mtc.gov/wp-content/uploads/2026/07/Nexus-Directors-Update-7-27-26r1.pdf", date: "2026-07-27", access: full, locator: "Cases: New York, In re Zelinsky"}
  last_reviewed: "2026-10-21"
  notes: >-
    The original CNBC report was not opened. Avalara's executive is quoted in trade press saying states have long used
    tools to select and run audits and AI is a natural fit (AVALARA-TRENDS-2025, section 'States look to AI'), which
    repeats the same New York claim.

- id: tax-multistate-private-04
  title: AI-assisted multistate nexus study across income, franchise, sales and payroll taxes, with state-by-state verification
  archetype: tax
  module: multistate-private
  function: service-delivery
  work_types: [research-synthesis, expert-judgment, document-production]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    A nexus study asks, state by state and tax by tax, whether sales, property, payroll or people create a filing
    duty, using thresholds that keep changing. In 2026 alone Kentucky dropped its 200-transaction sales tax test and New
    Jersey issued bright-line corporation business tax nexus guidance (MTC-NEXUSUPD-2026).
  solution: >-
    Kintsugi and Truss advertise a webinar that says it will show live examples of AI agents answering nexus questions
    across a client portfolio and state filing thresholds (TRUSS-KINTSUGI-2026). A law-firm article on the IRS Office of
    Professional Responsibility's AI alert uses a nexus study for state income and sales tax as its example of AI-assisted
    work, saying the practitioner must independently verify sales thresholds, transaction thresholds, tax rates and
    effective dates state by state (KTS-OPR-2026). Mercor's posting seeks SALT experts to evaluate and correct AI answers
    on nexus (economic, physical, factor-presence and remote employee) (MERCOR-SALT-2026).
  outcomes:
    - {lever: speed, description: "none published", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: TRUSS-KINTSUGI-2026}
  prerequisites:
    - "Client data by state (sales, payroll, property, employee locations); implied by the verification list in KTS-OPR-2026, not stated as a prerequisite"
  risks_and_guardrails:
    - "KTS says AI output is a draft; the practitioner verifies thresholds, rates and dates, and uses only firm-approved systems for client information (KTS-OPR-2026)"
    - "The OPR alert covers federal practice under Circular 230; KTS applies it to a state example (KTS-OPR-2026), and the indirect-tax module notes the alert does not address state filings"
    - "The webinar is a sales-tax-focused vendor listing; no income tax nexus tool or customer was found"
  human_checkpoints:
    - "Practitioner verification of every factor in the study (KTS-OPR-2026)"
  role_evolution: >-
    KTS says the practitioner remains responsible for the final work whatever the AI did (KTS-OPR-2026). Mercor's posting
    shows AI developers recruiting experienced SALT specialists to grade model answers (MERCOR-SALT-2026).
  evidence_grade: C
  sources:
    - {ref: TRUSS-KINTSUGI-2026, title: "What's Changing in Sales and Business Tax - And How AI Can Help (webinar listing)", publisher: "Truss with Kintsugi", type: vendor, url: "https://gettruss.io/events/sales-business-tax-ai", date: "2026-09-17", access: full, locator: "About Event and Learning Objectives"}
    - {ref: KTS-OPR-2026, title: "Using AI in Tax Practice: What Practitioners Need to Know Before Filing Season", publisher: "Kilpatrick Townsend & Stockton", type: firm, url: "https://ktslaw.com/blog/kilpatricks-state-and-local-tax-blog/2026/9/using-ai-in-tax-practice-what-practitioners-need-to-know-before-filing-season", date: "2026-09-29", access: full, locator: "paragraph beginning 'For example, if a client asks a practitioner to prepare a nexus study'"}
    - {ref: MERCOR-SALT-2026, title: "SALT (State and Local Taxation) Experts (job listing)", publisher: "Mercor (via AlignList)", type: job-posting, url: "https://alignlist.com/jobs/mercor-salt-state-and-local-taxation-experts-list-aaabnrlzswees5emkwdpflcl", date: "2026-06-12", access: full, locator: "responsibilities and topic list"}
    - {ref: MTC-NEXUSUPD-2026, title: "Nexus Program Director's Update on Nexus Law Developments Since April 22, 2026 (for the 27 Jul 2026 meeting)", publisher: "Multistate Tax Commission", type: regulator, url: "https://www.mtc.gov/wp-content/uploads/2026/07/Nexus-Directors-Update-7-27-26r1.pdf", date: "2026-07-27", access: full, locator: "Legislation: Kentucky; Rulings: New Jersey TB-108(R)"}
  last_reviewed: "2026-10-21"
  notes: >-
    The Truss listing date (2026-09-17) follows the indirect-tax file's citation of the same page; the listing text does
    not state the session date. Sales tax nexus monitoring and registration agents are in tax-indirect-tax-13.

- id: tax-multistate-private-05
  title: A remote hire's work location triggers state withholding, unemployment and foreign-qualification registration, handled by a platform or agent
  archetype: tax
  module: multistate-private
  function: risk-compliance-legal
  work_types: [transaction-processing, coordination-scheduling]
  pattern: end-to-end-case-agent
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    One employee working in a new state can require a foreign qualification, a state withholding account, an
    unemployment insurance registration and other agency accounts before the first paycheck; Gusto says an employee in a
    new state can also trigger corporate and franchise tax and sales tax obligations that may not show up in existing
    tools (GUSTO-MOSEY-2026). A payroll vendor's guide says withholding registration is required in 41 states and
    unemployment insurance in all 50 (WARP-REG-2026).
  solution: >-
    Gusto announced it acquired Mosey, which it describes as an AI-powered platform that automates state and local
    registrations, filings and renewals; Gusto Business Compliance is expected to launch later in 2026 and to surface
    requirements as a business grows, with AI agents doing the work behind the scenes (GUSTO-MOSEY-2026;
    FINTECHGLOBAL-GUSTO-2026). Warp says its payroll platform opens state tax accounts and files the registration
    paperwork when a customer hires in a new state (WARP-REG-2026). Skyvern, a browser-automation vendor, says its AI
    works through state registration portals in parallel and copes with portal changes (SKYVERN-REG-2026).
  outcomes:
    - {lever: speed, description: "Skyvern's manual baseline for one state registration filing", figure: "15-30 minutes per state (manual baseline)", measures: "time to complete registration forms by hand per state filing, as stated in the vendor's blog; no sample, customer or method given", provenance: vendor-published, source_ref: SKYVERN-REG-2026}
    - {lever: risk, description: "none published for Gusto/Mosey or Warp (no registration accuracy or penalty figures)", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: GUSTO-MOSEY-2026}
  prerequisites:
    - "Employee work location data from the HR or payroll system (payroll nexus follows where work is done, per GUSTO-MOSEY-2026)"
    - "An EIN and, in most states, foreign qualification before payroll registration (WARP-REG-2026)"
  risks_and_guardrails:
    - "Vendor claims only; no independent test of registration accuracy was found"
    - "Registration does not settle the income or franchise tax questions a new state raises; those need a nexus review (GUSTO-MOSEY-2026 lists them as separate triggers)"
    - "Gusto's target is small business (over 400,000 or 500,000 customers, depending on page); fit with middle-market payrolls is not shown"
  human_checkpoints:
    - "Not described for registrations; Gusto says no compliance expert is needed by the user (GUSTO-MOSEY-2026)"
  role_evolution: >-
    Gusto positions the work as moving from the owner or a lawyer to the platform (GUSTO-MOSEY-2026).
  evidence_grade: C
  sources:
    - {ref: GUSTO-MOSEY-2026, title: "Gusto Welcomes Mosey to Close the Compliance Gap for Small Businesses", publisher: "Gusto", type: vendor, url: "https://www.gusto.com/resources/company-news/gusto-mosey-acquisition", date: "2026-04-13", access: full, locator: "sections on compliance inflation and how Gusto is closing the gap (read via mirror; date from the FINTECHGLOBAL-GUSTO-2026 coverage)"}
    - {ref: FINTECHGLOBAL-GUSTO-2026, title: "Gusto and Mosey unite to tackle small business compliance", publisher: "Fintech Global", type: press, url: "https://fintech.global/2026/04/13/gusto-and-mosey-unite-to-tackle-small-business-compliance/", date: "2026-04-13", access: full, locator: "paragraphs 1-8"}
    - {ref: WARP-REG-2026, title: "How to register for state payroll taxes", publisher: "Warp", type: vendor, url: "https://www.warp.co/blog/how-to-register-for-state-payroll-taxes", date: "2026-02-19", access: full, locator: "intro and state-count paragraphs"}
    - {ref: SKYVERN-REG-2026, title: "Automating Payroll Registration Across All 50 States", publisher: "Skyvern", type: vendor, url: "https://www.skyvern.com/blog/automating-payroll-registration-50-states/", date: "2026-03-27", access: full, locator: "key takeaways and multi-portal burden section"}
  last_reviewed: "2026-10-21"
  notes: >-
    A search result described a Middesk automated payroll registration product; its page returned 404, so it is not used.
    Mosey's customers, and any Gusto customer outcome, were not found. Payroll withholding for remote workers had no
    other AI evidence; this is the whole public record found for payroll nexus.

- id: tax-multistate-private-06
  title: Apportionment factors computed from reconciled ledgers by rules, validated against prior periods, with optional AI commentary
  archetype: tax
  module: multistate-private
  function: finance-accounting
  work_types: [data-reporting, transaction-processing]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Sales, payroll and property factors are often computed separately by entity, which creates reconciliation work and
    error risk when state returns are prepared (ALTERYX-APPORT-2026). MTC held a 2026 panel on whether states should
    allow alternative apportionment (MTC-ANNUAL-2026), which shows the rules themselves are in flux.
  solution: >-
    Alteryx's starter kit reconciles factor inputs from source systems, applies jurisdiction rules, checks factors across
    jurisdictions and against prior periods, and builds an audit trail from each filed factor to its source; the kit
    adds guidance on feeding the structured output to a language model for commentary (ALTERYX-APPORT-2026). The core
    calculation is rules-based. Rules-based apportionment suites are older: CCH announced its Apportionment Suite in 2014
    (WK-APPORT-2014).
  outcomes:
    - {lever: quality, description: "none published (no customer, accuracy or time-saving figure)", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: ALTERYX-APPORT-2026}
  prerequisites:
    - "Reconciled property, payroll and sales data across entities and source systems (ALTERYX-APPORT-2026)"
  risks_and_guardrails:
    - "The AI step is optional commentary after a deterministic calculation; the vendor does not claim AI computes the factors (ALTERYX-APPORT-2026)"
    - "Agent-prepared business returns that include state apportionment (Byron) are tracked in tax-compliance-corporate-06; the >97% extraction accuracy there is the company's claim (BYRON-2026)"
  human_checkpoints:
    - "Prior-period anomalies are surfaced for explanation before filing (ALTERYX-APPORT-2026)"
  role_evolution: >-
    Not stated in the sources.
  evidence_grade: C
  sources:
    - {ref: ALTERYX-APPORT-2026, title: "Tax Apportionment Factor Computation Starter Kit", publisher: "Alteryx", type: vendor, url: "https://www.alteryx.com/starter-kit/tax-apportionment-factor-computation", date: "2026-07-16", access: full, locator: "Overview, What's included, Extending your workflow with AI (read via mirror)"}
    - {ref: WK-APPORT-2014, title: "Wolters Kluwer, CCH Launches Apportionment Suite", publisher: "Accounting Today", type: press, url: "https://www.accountingtoday.com/news/wolters-kluwer-cch-launches-apportionment-suite", date: "2014-09-29", access: full, locator: "article text"}
    - {ref: MTC-ANNUAL-2026, title: "59th Annual Meetings (schedule)", publisher: "Multistate Tax Commission", type: conference, url: "https://www.mtc.gov/events-training/59th-annual-meetings/", date: "2026-07-29", access: full, locator: "Day Three, 10:15 session 'Alternative Apportionment Reconsidered' (read via mirror)"}
    - {ref: BYRON-2026, title: "Byron Launches with AI Agents for Business Tax Preparation Workflows", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/2026/05/27/byron-launches-with-ai-agents-for-business-tax-preparation-workflows/184034/", date: "2026-05-27", access: full, locator: "paragraphs on specialised agents and accuracy claim"}
  last_reviewed: "2026-10-21"
  notes: >-
    A search listing also shows Thomson Reuters ONESOURCE State Apportionment as a rules-based tool; that page was not
    opened and is not used. No source describes AI computing apportionment for a mid-market firm.

- id: tax-multistate-private-07
  title: AI research assistants for multi-jurisdiction state tax questions (nexus, pass-through entity tax, sourcing), with authorities checked
  archetype: tax
  module: multistate-private
  function: service-delivery
  work_types: [research-synthesis, expert-judgment]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: announced
  problem: >-
    State answers differ by state and year (for example, New York's pass-through entity tax credit is refundable and
    California's is not, for tax year 2025, per a model answer in the Vals benchmark), so a wrong or stale citation
    changes the advice (VALS-TAXAGENT-2026).
  solution: >-
    Thomson Reuters says its Checkpoint Catalyst state topics integrate into CoCounsel Tax (TRFORD-SALT-2026). COST's
    March 2026 SALT workshop scheduled demonstrations of embedded research tools named as Bloomberg AI and Checkpoint
    CoCounsel, alongside Copilot Studio and Amazon Quick Suite agent building, presented by staff from Amazon, AT&T, EY,
    PwC and Reed Smith (COST-TECH-2026). Fintech Global reports that Blue J's platform supports federal, state and local tax research (BLUEJ-RAISE-2025).
  outcomes:
    - {lever: quality, description: "Vals public question P-004 (SALT: New York versus California pass-through entity tax credit), 18 models traced", figure: "overall leader scored 91%; three models scored 76.5%; one model passed all 18 checks", measures: "weighted rubric score on one public State & Local Tax question; the leader cleared every must-pass check and missed two lower-weight points; one question only, not a SALT-wide score", provenance: independent, source_ref: VALS-TAXAGENT-2026}
    - {lever: quality, description: "Vals Tax Agent Bench headline (adjacent: mostly federal corporate research)", figure: "best model 49.19%", measures: "average score across 193 private test questions, roughly 60% federal corporate income tax and the rest partnership, SALT, transfer pricing and employment tax; SALT-only score not published", provenance: independent, source_ref: VALS-TAXAGENT-2026}
  prerequisites:
    - "Approved enterprise tools and current state content; COST's workshop notes privacy and ethics among its topics (COST-TECH-2026)"
  risks_and_guardrails:
    - "The benchmark is adjacent evidence (research questions given to models), not a tool in firm practice; Vals is a commercial evaluator and the archetype files list it as vendor-type"
    - "The independent figures cap this entry's evidence at adjacent; no firm reported a measured SALT research time saving"
    - "KTS: treat AI text as a draft and verify authorities (KTS-OPR-2026)"
  human_checkpoints:
    - "Practitioner verifies authorities and effective dates (KTS-OPR-2026)"
  role_evolution: >-
    Not measured. The COST agenda frames AI as a tool for accelerating research and improving accuracy for technical
    tax work (COST-TECH-2026).
  evidence_grade: C
  sources:
    - {ref: VALS-TAXAGENT-2026, title: "Tax Agent Bench: Agentic US corporate tax research (leaderboard and methodology)", publisher: "Vals AI", type: vendor, url: "https://www.vals.ai/benchmarks/tax_agent_bench", date: "2026-10-20", access: full, locator: "Overview paragraph on question mix; Tool Use section on P-004 (read via mirror; the archetype cites an update of 2026-10-16)"}
    - {ref: COST-TECH-2026, title: "2026 SALT in a Digital World Workshop agenda (version dated 02/26/26)", publisher: "Council On State Taxation", type: conference, url: "https://www.cost.org/globalassets/cost/cost-events/2026tech-agenda-260226-revised.pdf", date: "2026-02-26", access: full, locator: "Monday March 2, Parts 1-4"}
    - {ref: TRFORD-SALT-2026, title: "Multistate Tax Trends: A Q&A with SALT Expert Niki Ford on Nexus, Marketplaces, AI, and the Future", publisher: "Thomson Reuters Tax & Accounting (Checkpoint News)", type: vendor, url: "https://tax.thomsonreuters.com/news/multistate-tax-trends-a-qa-with-salt-expert-niki-ford-on-nexus-marketplaces-ai-and-the-future/", date: "2026-04-09", access: full, locator: "series introduction and closing product references"}
    - {ref: BLUEJ-RAISE-2025, title: "Blue J raises $122m to scale AI-powered tax research", publisher: "Fintech Global", type: press, url: "https://fintech.global/?p=210135", date: "2025-08-05", access: full, locator: "paragraph 2"}
    - {ref: KTS-OPR-2026, title: "Using AI in Tax Practice: What Practitioners Need to Know Before Filing Season", publisher: "Kilpatrick Townsend & Stockton", type: firm, url: "https://ktslaw.com/blog/kilpatricks-state-and-local-tax-blog/2026/9/using-ai-in-tax-practice-what-practitioners-need-to-know-before-filing-season", date: "2026-09-29", access: full, locator: "paragraphs on due diligence and verification"}
  last_reviewed: "2026-10-21"
  notes: >-
    General cited research assistants are graded in tax-research-advisory-01 to -08; this entry keeps only the multistate
    angle. COST's list names tools as demonstrated in a workshop; it does not say any speaker's employer deployed them.

- id: tax-multistate-private-08
  title: "Idea: an in-house SALT team uses AI for quarterly state updates, comparing legislative versions and reviewing appeal arguments"
  archetype: tax
  module: multistate-private
  function: finance-accounting
  work_types: [research-synthesis, document-production]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    SALT teams track many state bills, rulings and cases and write periodic updates. Law moves fast: one MTC director's
    update for a single quarter lists amnesties, nexus rule changes, new taxes and court decisions across a dozen states
    (MTC-NEXUSUPD-2026).
  solution: >-
    COST's workshop agenda listed demonstrations of AI drafting quarterly SALT updates, comparing versions of
    legislative proposals and reviewing appeal arguments, presented by staff from AT&T, EY, Reed Smith and others
    (COST-TECH-2026). Nothing shows a team doing this in production.
  outcomes:
    - {lever: speed, description: "none published", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: COST-TECH-2026}
  prerequisites:
    - "An approved AI tool and a source set of current bills and rulings (inferred; not stated)"
  risks_and_guardrails:
    - "COST included an ethics session on AI-driven decision-making and digital audit tools in the same programme (COST-TECH-2026)"
  human_checkpoints:
    - "Not described"
  role_evolution: >-
    Not described.
  evidence_grade: D
  sources:
    - {ref: COST-TECH-2026, title: "2026 SALT in a Digital World Workshop agenda (version dated 02/26/26)", publisher: "Council On State Taxation", type: conference, url: "https://www.cost.org/globalassets/cost/cost-events/2026tech-agenda-260226-revised.pdf", date: "2026-02-26", access: full, locator: "Monday March 2, Part 3"}
    - {ref: MTC-NEXUSUPD-2026, title: "Nexus Program Director's Update on Nexus Law Developments Since April 22, 2026 (for the 27 Jul 2026 meeting)", publisher: "Multistate Tax Commission", type: regulator, url: "https://www.mtc.gov/wp-content/uploads/2026/07/Nexus-Directors-Update-7-27-26r1.pdf", date: "2026-07-27", access: full, locator: "whole document (7 pages)"}
  last_reviewed: "2026-10-21"
  notes: >-
    Idea. The agenda is for a workshop held 2-4 March 2026; the agenda version read is dated 26 Feb 2026. Law-change
    monitoring in general is tax-compliance-corporate-12 and tax-research-advisory-23.

- id: tax-multistate-private-09
  title: "Idea: a company scans its own data for the same signals states match on (registrations, thresholds, processor and marketplace totals) before a notice arrives"
  archetype: tax
  module: multistate-private
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    If states link filing, marketplace and payment data to find unregistered businesses (tax-multistate-private-02),
    companies that have never reconciled their own footprint have exposure they cannot see.
  solution: >-
    The Sales Tax Institute says its webinar will cover responding when nexus is triggered, addressing historical
    exposure before it becomes an audit issue, and strengthening data quality controls (STI-AIAUDITS-2026). A consultancy
    suggests reviewing nexus footprint, exemption certificates, classifications and under-collected periods, and checking
    for payroll registrations with no matching sales tax account (SALESTAX-AIAUDIT-2026). Withum advises periodic tax
    health checks (WITHUM-SEATA-2026). None of the three describes a deployed AI scan.
  outcomes:
    - {lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: vendor-published, source_ref: STI-AIAUDITS-2026}
  prerequisites:
    - "Company data by state: sales, payroll registrations, marketplace and processor totals (SALESTAX-AIAUDIT-2026)"
  risks_and_guardrails:
    - "A scan that finds exposure can affect voluntary disclosure eligibility if it leads to contact with a state; eligibility rules vary by state (SALESTAX-AIAUDIT-2026 discusses disclosure before a state opens an audit)"
  human_checkpoints:
    - "A professional decides on registration and disclosure (SALESTAX-AIAUDIT-2026 lists what AI cannot do: register, fix past periods, make judgment calls)"
  role_evolution: >-
    Not described.
  evidence_grade: D
  sources:
    - {ref: STI-AIAUDITS-2026, title: "AI in State Tax: New Tools, Familiar Risks (live webinar listing)", publisher: "Sales Tax Institute", type: vendor, url: "https://www.salestaxinstitute.com/sales-tax-education/ai-in-state-tax-audits", date: "2026-06-25", access: full, locator: "learning outcomes paragraph"}
    - {ref: SALESTAX-AIAUDIT-2026, title: "Are You Using AI to Find Businesses That Aren't Paying Sales Tax? Here's What That Means for You", publisher: "The Sales Tax People", type: firm, url: "https://sales.tax/sales-tax-updates/states-ai-sales-tax-audits-enforcement-2026/", date: "2026-05-18", access: full, locator: "sections on what to do and what AI cannot do"}
    - {ref: WITHUM-SEATA-2026, title: "Key Takeaways From the 2026 SEATA Conference", publisher: "Withum", type: firm, url: "https://www.withum.com/resources/key-takeaways-from-the-2026-seata-conference/", date: "2026-07-14", access: full, locator: "'The Bottom Line'"}
  last_reviewed: "2026-10-21"
  notes: >-
    Idea. The sources recommend reviews; the AI-driven version of the scan is the research team's reading of where
    commentators point, not something a source states. Kept as D.

- id: tax-multistate-private-10
  title: "Idea: defending AI-informed state assessments with data analytics, transparent documentation and human judgment"
  archetype: tax
  module: multistate-private
  function: service-delivery
  work_types: [expert-judgment, document-production]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    If an assessment starts from an opaque model score, the taxpayer must answer it without knowing what triggered it
    (NTT-BIAS-2026).
  solution: >-
    Akerman announced that a partner would present at COST's 57th Annual Meeting on state tax departments' increased use
    of AI in audits and practical approaches to defending AI-driven assessments, combining data analytics, transparent
    documentation and human judgment (AKERMAN-COST-2026). The announcement describes the session, not a method used
    on a case.
  outcomes:
    - {lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: AKERMAN-COST-2026}
  prerequisites:
    - "Not stated"
  risks_and_guardrails:
    - "The announcement is dated 23 Sep 2026 (the page's publication date); session content was not seen"
  human_checkpoints:
    - "Human judgment is one of the three named elements (AKERMAN-COST-2026)"
  role_evolution: >-
    Not described.
  evidence_grade: D
  sources:
    - {ref: AKERMAN-COST-2026, title: "Stefi George to Speak on Defending AI-Driven Tax Audits at COST's 57th Annual Meeting", publisher: "Akerman LLP", type: firm, url: "https://www.akerman.com/en/perspectives/stefi-george-to-speak-on-defending-ai-driven-tax-audits-at-costs-57th-annual-meeting.html", date: "2026-09-23", access: full, locator: "announcement text"}
    - {ref: NTT-BIAS-2026, title: "How AI Bias Affects State Audit Selection", publisher: "Tax Notes Talk (Tax Analysts)", type: podcast, url: "https://taxnotestalk.taxnotes.com/124942/episodes/19216367-how-ai-bias-affects-state-audit-selection", date: "2026-05-22", access: full, locator: "discussion of taxpayer-side asymmetry"}
  last_reviewed: "2026-10-21"
  notes: >-
    Idea. A talk abstract can support only an idea grade. A search result gave COST's meeting as 22-25 Sep 2026 in San
    Antonio; the Akerman page names the Hyatt Regency San Antonio Riverwalk and 23 Sep 2026.

- id: tax-multistate-private-11
  title: Exposure review and voluntary disclosure remediation marketed on the back of state AI enforcement
  archetype: tax
  module: multistate-private
  function: service-delivery
  work_types: [expert-judgment, client-interaction, document-production]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Companies with unregistered states need to decide between voluntary disclosure (lookback relief, usually requires no
    prior contact), amnesty (limited-time) or waiting.
  solution: >-
    A sales-tax consultancy argues that disclosing before a state's AI flags the business is cheaper than an audit after
    it, and says at least four states offer amnesty or disclosure programs in 2026 (SALESTAX-AIAUDIT-2026). The service
    is human; the AI link is the argument that detection is getting cheaper. The MTC's Multistate Voluntary Disclosure
    Program results give a baseline for demand. No source describes AI used inside the disclosure work.
  outcomes:
    - {lever: growth, description: "MTC Multistate Voluntary Disclosure Program, fiscal year 2026 (1 Jul 2025 to 30 Jun 2026)", figure: "464 executed agreements; $28,308,873 collected; average $61,010 per agreement", measures: "agreements executed by participating states, amounts paid by taxpayers directly to states and reported to the Commission, and average contract value; fiscal year 2025 was 498 agreements and $29,083,242", provenance: independent, source_ref: MTC-NEXUSDIR-2026}
    - {lever: growth, description: "Applications to the program", figure: "190 taxpayers in calendar 2025; 95 as of 30 Jun 2026", measures: "taxpayers that submitted applications to the Commission, most based on sales tax economic nexus", provenance: independent, source_ref: MTC-NEXUSDIR-2026}
  prerequisites:
    - "A quantified exposure by state, tax type and period before approaching a state (practice norm; the MTC report does not state it)"
  risks_and_guardrails:
    - "The sources do not show that state AI has increased disclosure volume: MTC agreements fell from 498 to 464 and collections from $29.1 million to $28.3 million year on year (MTC-NEXUSDIR-2026)"
    - "The consultancy sells these services; its claim is advocacy (SALESTAX-AIAUDIT-2026)"
  human_checkpoints:
    - "Professional-led negotiation; no AI step is described"
  role_evolution: >-
    Staffing at the MTC audit programme saw an unusually high number of changes in FY2026, with retirements in both the
    income tax and sales tax teams (MTC-AUDITDIR-2026).
  evidence_grade: C
  sources:
    - {ref: SALESTAX-AIAUDIT-2026, title: "Are You Using AI to Find Businesses That Aren't Paying Sales Tax? Here's What That Means for You", publisher: "The Sales Tax People", type: firm, url: "https://sales.tax/sales-tax-updates/states-ai-sales-tax-audits-enforcement-2026/", date: "2026-05-18", access: full, locator: "section on voluntary disclosure"}
    - {ref: MTC-NEXUSDIR-2026, title: "National Nexus Program Director's Report for FY 2026 (for the 27 Jul 2026 meeting)", publisher: "Multistate Tax Commission", type: regulator, url: "https://www.mtc.gov/wp-content/uploads/2026/07/Nexus-Directors-FY-26-report-7-27-26r1.pdf", date: "2026-07-27", access: full, locator: "page 1, Multistate Voluntary Disclosure Program"}
    - {ref: MTC-NEXUSUPD-2026, title: "Nexus Program Director's Update on Nexus Law Developments Since April 22, 2026 (for the 27 Jul 2026 meeting)", publisher: "Multistate Tax Commission", type: regulator, url: "https://www.mtc.gov/wp-content/uploads/2026/07/Nexus-Directors-Update-7-27-26r1.pdf", date: "2026-07-27", access: full, locator: "Rulings: Illinois, Indiana, Washington programs"}
    - {ref: MTC-AUDITDIR-2026, title: "Audit Director's Report FY 2026 Annual Report (for the 27 Jul 2026 meeting)", publisher: "Multistate Tax Commission", type: regulator, url: "https://www.mtc.gov/wp-content/uploads/2026/07/7-Audit-Directors-report-2026-summer-meeting1.pdf", date: "2026-07-27", access: full, locator: "section 2, Staffing"}
  last_reviewed: "2026-10-21"
  notes: >-
    The MTC figures are a demand baseline, not a measure of AI. In 2026 the MTC update lists the Illinois remote retailers
    amnesty (1 Aug to 31 Oct 2026), Indiana amnesty (15 Jul to 9 Sep 2026) and a Washington international remote seller
    voluntary disclosure programme (1 Feb to 31 May 2026). Voluntary disclosure and amnesty mechanics are not AI-specific
    and were not otherwise verified.

- id: tax-multistate-private-12
  title: "Idea: outside review, inventories and bias testing of state audit-selection models"
  archetype: tax
  module: multistate-private
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Agency selection systems get only internal review in the cases Tax Notes examined, and oversight laws miss them when
    agencies do not classify the systems as AI or high risk (NTT-BIAS-2026).
  solution: >-
    Experts quoted by Tax Notes say agencies should have outside oversight (lawmakers, another agency or a state auditor)
    and that a Stanford researcher wants clear goals so systems do not disproportionately select lower-income taxpayers;
    the same researcher sees machine learning as a potentially good tool against human bias (NTT-BIAS-2026). A vendor
    executive's commentary urges continuous testing, logging of model inputs and outputs and documented decision rules
    for revenue-agency AI pilots (ROUTEFIFTY-REV-2026). The New York Comptroller's 2025 audit of state AI governance found
    no statewide inventory of AI systems and inadequate central guidance, in four non-tax agencies (NYOSC-AIAUDIT-2025).
  outcomes:
    - {lever: risk, description: "none published", figure: "none published", measures: "not applicable", provenance: independent, source_ref: NTT-BIAS-2026}
  prerequisites:
    - "Agency willingness to classify selection models as in scope of AI oversight laws (NTT-BIAS-2026)"
  risks_and_guardrails:
    - "Tax Notes' experts note an institutional bias against finding problems in a system the agency has invested in (NTT-BIAS-2026)"
  human_checkpoints:
    - "Lawmakers, a state auditor or another agency as outside reviewers (NTT-BIAS-2026)"
  role_evolution: >-
    Not described.
  evidence_grade: D
  sources:
    - {ref: NTT-BIAS-2026, title: "How AI Bias Affects State Audit Selection", publisher: "Tax Notes Talk (Tax Analysts)", type: podcast, url: "https://taxnotestalk.taxnotes.com/124942/episodes/19216367-how-ai-bias-affects-state-audit-selection", date: "2026-05-22", access: full, locator: "closing takeaways and legislation discussion"}
    - {ref: NYOSC-AIAUDIT-2025, title: "DiNapoli: Improved Guidance Needed for State Agencies Using AI To Avoid Risks (Report 2023-S-50)", publisher: "Office of the New York State Comptroller", type: regulator, url: "https://www.osc.ny.gov/press/releases/2025/04/dinapoli-improved-guidance-needed-state-agencies-using-ai-avoid-risks", date: "2025-04-03", access: full, locator: "press release paragraphs 1-4; audit report pp. 1-3"}
    - {ref: ROUTEFIFTY-REV-2026, title: "From pilot to proof: How revenue agencies can launch AI responsibly", publisher: "Route Fifty (commentary by a Tricentis executive)", type: press, url: "https://www.route-fifty.com/artificial-intelligence/2026/07/pilot-proof-how-revenue-agencies-can-launch-ai-responsibly/415141/", date: "2026-07-31", access: full, locator: "sections on continuous validation and explainability"}
  last_reviewed: "2026-10-21"
  notes: >-
    Idea. Agency-side and policy-led; relevant to an assurance or governance engagement for a state or a vendor, less to a
    private company. NY's audit sampled four agencies (Aging, Corrections, Motor Vehicles, Transportation), not the tax
    department. California bills SB 420 and SB 1248 and a New York reporting law (2025) are mentioned by the Tax Notes
    reporters; their status was not checked.

- id: tax-multistate-private-13
  title: AI companies as a new SALT client segment for mid-market firms (digital product classification, nexus for cloud operations, remote employees, sourcing)
  archetype: tax
  module: multistate-private
  function: product-service-development
  work_types: [expert-judgment, document-production]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Fast-growing AI companies sell into many states, hire remotely and sell products that states classify differently.
    Moss Adams says these companies can trigger sales and use, income, franchise and gross receipts tax obligations and
    payroll issues from remote employees (MOSSADAMS-AISALT-2025).
  solution: >-
    Moss Adams (now part of Baker Tilly) published SALT guidance for AI companies in April 2025 and held a webcast in
    August 2025 on state and local tax challenges for AI companies across jurisdictions (MOSSADAMS-AISALT-2025;
    MOSSADAMS-AIWEBCAST-2025). Checkpoint's SALT Q&A says Maryland, Texas and Washington extended sales taxes to various
    automated services and that states will struggle to classify generative and agentic AI (TRFORD-SALT-2026). Eide Bailly's
    April 2026 roundup frames AI as a tax policy issue (EIDE-SALT-2026). This is demand created by AI, not AI used in the
    tax work.
  outcomes:
    - {lever: growth, description: "none published (no client count, revenue or engagement figure)", figure: "none published", measures: "not applicable", provenance: self-reported, source_ref: MOSSADAMS-AISALT-2025}
  prerequisites:
    - "SALT specialists with digital product and sourcing knowledge (inferred from the topic list in MOSSADAMS-AISALT-2025)"
  risks_and_guardrails:
    - "Taxability of AI products varies by state and is changing, which the sources say complicates nexus and sourcing (MOSSADAMS-AISALT-2025; TRFORD-SALT-2026)"
  human_checkpoints:
    - "Not applicable; the service is professional advice"
  role_evolution: >-
    Not described.
  evidence_grade: C
  sources:
    - {ref: MOSSADAMS-AISALT-2025, title: "Boost compliance and help reduce exposure by understanding AI SALT impacts", publisher: "Moss Adams", type: firm, url: "https://www.mossadams.com/articles/2025/04/ai-state-and-local-tax-considerations", date: "2025-04-11", access: full, locator: "opening paragraphs and nexus section"}
    - {ref: MOSSADAMS-AIWEBCAST-2025, title: "State and Local Tax Implications for AI Companies (webcast)", publisher: "Moss Adams", type: firm, url: "https://www.mossadams.com/events/2025/08/navigating-state-and-local-tax-for-ai-companies", date: "2025-08", access: full, locator: "event description"}
    - {ref: TRFORD-SALT-2026, title: "Multistate Tax Trends: A Q&A with SALT Expert Niki Ford on Nexus, Marketplaces, AI, and the Future", publisher: "Thomson Reuters Tax & Accounting (Checkpoint News)", type: vendor, url: "https://tax.thomsonreuters.com/news/multistate-tax-trends-a-qa-with-salt-expert-niki-ford-on-nexus-marketplaces-ai-and-the-future/", date: "2026-04-09", access: full, locator: "answer on AI and state taxes"}
    - {ref: EIDE-SALT-2026, title: "State & Local Tax Meets AI: How Technology Is Reshaping Taxability, Nexus, and State Enforcement", publisher: "Eide Bailly", type: firm, url: "https://www.eidebailly.com/insights/blogs/2026/4/salt20260430", date: "2026-04-30", access: full, locator: "key takeaways (the body is mainly a weekly state tax roundup)"}
  last_reviewed: "2026-10-21"
  notes: >-
    The webcast date is given as 2025-08 from the URL path; the page text read does not show the day. Taxability of AI
    products themselves belongs to indirect-tax (section 4).
```

## 3. Module notes

**Processes and key steps (with work types)**
- Nexus identification and monitoring across income and franchise tax, sales, payroll and property: data-reporting, expert-judgment. Pain: thresholds and tests keep changing (2026 examples in the MTC update: Kentucky removed the 200-transaction alternative from 1 Aug 2026; New Jersey bright-line corporation business tax nexus guidance; Massachusetts and New York P.L. 86-272 cases) [MTC-NEXUSUPD-2026].
- Registration and foreign qualification (Secretary of State, withholding, unemployment insurance, other accounts): transaction-processing. Pain: portal-by-portal manual work; a payroll vendor says withholding registration is required in 41 states and unemployment insurance in all 50 [WARP-REG-2026].
- Apportionment and sourcing: data-reporting, expert-judgment. Pain: factors computed separately by entity and system [ALTERYX-APPORT-2026]. MTC debated alternative apportionment on 29 Jul 2026 [MTC-ANNUAL-2026].
- State return preparation (corporate, pass-through entity tax, composite and nonresident withholding): transaction-processing, document-production. Routed to compliance modules.
- Exposure quantification and voluntary disclosure: expert-judgment, document-production, client-interaction.
- Audit, notice and controversy: review-assurance, document-production. Routed to controversy.
- Law-change tracking: research-synthesis.

**Metrics and benchmarks**
- State agency AI adoption: 7 of 36 responding agencies use AI; 22 none; 6 interested [TAXNOTES-UNWATCHED-2026] (independent, survey by Tax Notes in 2025, response rate 36 of 49).
- MTC Multistate Voluntary Disclosure Program FY2026: 464 executed agreements, $28,308,873 collected, average $61,010; 190 applications in calendar 2025 and 95 to 30 Jun 2026; 40 participating states including DC [MTC-NEXUSDIR-2026].
- MTC Joint Audit Program FY2026: proposed net assessments of $80,563,369 (income tax) and $3,179,204 (sales tax); 13 income tax and 22 sales tax audits in progress [MTC-AUDITDIR-2026].
- Vals Tax Agent Bench: best model 49.19% on 193 private questions (mostly federal corporate); one SALT question traced across 18 models [VALS-TAXAGENT-2026] (adjacent).
- New York audits in 2022: 771,000, up 56%; auditors down 5% to under 200 (secondhand, 2024) [YAHOO-NYAI-2024].
- No error rate, override rate, parallel-run result or time-saving figure exists for any AI tool in this module in the sources read.

**Guardrails and regulatory points**
- IRS OPR Alert 2026-19 (released 24 Jun 2026) applies existing Circular 230 duties to AI; KTS applies it to a nexus-study example and reminds firms of §§6713 and 7216 for client data and §10.36 firm procedures [KTS-OPR-2026]. It is federal; no state board of accountancy or state revenue department guidance on AI-assisted state tax work was found.
- AI used by state agencies: California's AB 302 inventory (2025) reported zero high-risk systems even though the FTB runs selection models [NTT-BIAS-2026]; New York's AI governance had no statewide inventory in April 2025 [NYOSC-AIAUDIT-2025]. New York's tax department says its selection system is not AI [NTT-BIAS-2026].
- CDTFA: written advice protections do not extend to verbal advice, so a taxpayer relying on an agent's AI-assisted oral answer may not be protected [CDTFA-2025].
- Voluntary disclosure normally needs no prior contact with the state; a company that registers or is contacted first can lose eligibility (practice rule stated by consultancies; not verified against state programme rules) [SALESTAX-AIAUDIT-2026].

**Frontier signals (dated, sourced)**
- 2025-12: South Carolina DOR signs a $3.5 million, five-year audit contract; starts with sales and use tax, then corporate; may extend to individuals with up to three years of lookback [SCPOST-AUDIT-2026, article 2026-04-12].
- 2026-03-02: COST SALT in a Digital World workshop opens with a half-day of AI sessions, including building a basic agent [COST-TECH-2026].
- 2026-04-13: Gusto announces its Mosey acquisition; integrated compliance product expected later in 2026 [FINTECHGLOBAL-GUSTO-2026].
- 2026-06-23: FTA podcast recorded at its 2026 annual meeting with revenue officials from Wisconsin, Georgia, Tennessee and Nevada on AI and innovation (description only) [FTA-TAXBREAKS-2026].
- 2026-07-29: MTC panel on the impact of AI on administration and practice of state tax (FTA, Pennsylvania DOR, Blue J) [MTC-ANNUAL-2026]. Neither the Nexus nor the Audit committee agendas or director reports mention AI.
- 2026-09-23: Akerman announces a COST session on defending AI-driven assessments [AKERMAN-COST-2026].
- 2026-07-31: A vendor executive says states introduced more than 1,000 AI-related bills in 2025 and that Vermont and Michigan have AI plans for tax-fraud detection and Treasury analytics (commentary; not independently checked) [ROUTEFIFTY-REV-2026].

**Workforce and role effects**
- FTA expects training to be the main need and does not expect job loss soon [TAXNOTESTALK-2025].
- An academic argues AI agents will not shrink corporate tax teams much because AI cannot bear culpability (abstract only; Tax Notes State) [SALA-TAXNOTES-2026].
- AI developers are recruiting SALT specialists with five or more years' experience, with Big 4, national firm, law firm, state revenue department or corporate tax backgrounds preferred, to grade model answers on nexus, nonresident withholding and composite filing [MERCOR-SALT-2026]. This is a new, outside-the-firm use of SALT expertise.
- The MTC joint audit programme reports unusually high staff turnover in FY2026 (retirements) [MTC-AUDITDIR-2026]; no link to AI is stated.

**Objections and concerns practitioners raise**
- Opacity and asymmetry: faster agency outreach with no matching channel for taxpayers to dispute selection [NTT-BIAS-2026].
- Definition games: whether a system "is AI" decides whether oversight laws apply [NTT-BIAS-2026; TAXNOTES-UNWATCHED-2026].
- Reliance on oral AI-assisted agency advice is unprotected [CDTFA-2025].
- AI cannot carry culpability, so teams will not shrink much [SALA-TAXNOTES-2026].
- Vendor and consultancy claims about state enforcement are marketing-tinged [SALESTAX-AIAUDIT-2026; STI-AIAUDITS-2026].
- Counter-signal: 22 of 36 responding agencies say they use no AI [TAXNOTES-UNWATCHED-2026].

**Interview probes for an advisor**
1. Where are your people actually working today, who tracks it (HR, payroll or tax), and when did anyone last compare that list with your state withholding and unemployment accounts?
2. When was the last nexus review that covered income and franchise tax and not only sales tax, and what data fed it?
3. If a state notice arrived tomorrow citing third-party data, how long would it take to assemble your apportionment support, and from which systems?
4. Do you have states you suspect you should be registered in? What has stopped you from going to voluntary disclosure, and does your firm or provider scan for it?
5. If you or your adviser used AI on a state nexus or apportionment conclusion, who verifies thresholds, rates and effective dates state by state, and where is that recorded?

## 4. Routed to other modules

- **indirect-tax:** sales and use tax nexus monitoring and registration agents (tax-indirect-tax-13), Avalara Aviator agent hub (product page, Sep 2026: agents for calculation, returns, research and registration/certificate verification) [AVALARA-AVIATOR-2026], Kintsugi, Vertex and Sovos claims; taxation of AI products and automated services (Maryland, Texas, Washington, Indiana, Illinois) [TRFORD-SALT-2026]; Streamlined Sales Tax multistate voluntary disclosure proposal presented to the MTC Nexus Committee (agenda item, 27 Jul 2026) [MTC-ANNUAL-2026].
- **controversy:** state agency generative AI in call centres (CDTFA with SymSoft; Missouri's chatbot features) [CDTFA-PR-2025; CDTFA-2025] already at tax-controversy-20; general state risk targeting (tax-controversy-15, which overlaps use case 01 here); state notice triage (tax-controversy-01).
- **compliance-corporate:** agent-prepared business returns that include state apportionment [BYRON-2026] (tax-compliance-corporate-06); law-change and calendar tracking (tax-compliance-corporate-12).
- **compliance-individual-business:** Basis and commentary on agent-prepared partnership returns [OLIVER-1065-2026]; composite and pass-through entity tax preparation for owners.
- **research-advisory:** general AI tax research tools and benchmarks (tax-research-advisory-01 to -08, -23) [VALS-TAXAGENT-2026]; Blue J.
- **transfer-pricing:** Withum notes states are devoting more resources to related-party transactions, royalties and management fees [WITHUM-SEATA-2026].
- **provision-pillar-two:** state tax disclosure under the new income tax rate reconciliation (the MTC seminar covered ITEP analysis of public companies' state taxes paid) [MTC-ANNUAL-2026].
- **guardrails (archetype level):** OPR Alert 2026-19 [KTS-OPR-2026].

## 5. Sources

| Ref | Title | Publisher | Type | URL | Date |
|---|---|---|---|---|---|
| SCPOST-AUDIT-2026 | SCDOR to use AI to help decide which tax returns to audit | Post and Courier | press | https://www.postandcourier.com/news/sc-taxes-artificial-intelligence-audits-fast-scdor/article_54662d56-ae30-4130-845a-366547409477.html | 2026-04-12 |
| KOGOD-SC-2026 | Artificial Intelligence Being Used by SC Department of Revenue to Determine Who to Audit this Year | Kogod Tax Policy Center (American University) | academic | https://kogod.american.edu/news/artificial-intelligence-being-used-by-sc-department-of-revenue-to-determine-who-to-audit-this-year | 2026-04-29 |
| TAXNOTES-UNWATCHED-2026 | Tax Notes Investigates States' Use of AI in Audit Selection | TaxProf Blog (excerpting Tax Notes) | press | https://taxprofblog.aals.org/?p=134442 | 2026-05-02 |
| NTT-BIAS-2026 | How AI Bias Affects State Audit Selection | Tax Notes Talk | podcast | https://taxnotestalk.taxnotes.com/124942/episodes/19216367-how-ai-bias-affects-state-audit-selection | 2026-05-22 |
| TAXNOTESTALK-2025 | Artificial Intelligence and State Tax Agencies | Tax Notes Talk | podcast | https://taxnotestalk.taxnotes.com/124942/episodes/17439828-artificial-intelligence-and-state-tax-agencies | 2025-07-04 |
| CDTFA-2025 | Experts Urge Caution as State Tax Agencies Deploy Generative AI | Tax Notes (copy hosted by Kogod) | press | https://kogod.american.edu/hubfs/experts_urge_caution_as_state_tax_agencies_deploy_generative_ai_20250826-161144.pdf | 2025-08-26 |
| CDTFA-PR-2025 | California Moving Forward with Generative Artificial Intelligence in State Call Center | California Department of Tax and Fee Administration | regulator | https://cdtfa.ca.gov/news/25-04.htm | 2025-05-05 |
| NYOSC-AIAUDIT-2025 | DiNapoli: Improved Guidance Needed for State Agencies Using AI To Avoid Risks (Report 2023-S-50) | Office of the New York State Comptroller | regulator | https://www.osc.ny.gov/press/releases/2025/04/dinapoli-improved-guidance-needed-state-agencies-using-ai-avoid-risks | 2025-04-03 |
| MTC-ANNUAL-2026 | 59th Annual Meetings (schedule and committee agendas) | Multistate Tax Commission | conference | https://www.mtc.gov/events-training/59th-annual-meetings/ | 2026-07-29 |
| MTC-NEXUSDIR-2026 | National Nexus Program Director's Report for FY 2026 | Multistate Tax Commission | regulator | https://www.mtc.gov/wp-content/uploads/2026/07/Nexus-Directors-FY-26-report-7-27-26r1.pdf | 2026-07-27 |
| MTC-NEXUSUPD-2026 | Nexus Program Director's Update on Nexus Law Developments | Multistate Tax Commission | regulator | https://www.mtc.gov/wp-content/uploads/2026/07/Nexus-Directors-Update-7-27-26r1.pdf | 2026-07-27 |
| MTC-AUDITDIR-2026 | Audit Director's Report FY 2026 | Multistate Tax Commission | regulator | https://www.mtc.gov/wp-content/uploads/2026/07/7-Audit-Directors-report-2026-summer-meeting1.pdf | 2026-07-27 |
| FTA-TAXBREAKS-2026 | Tax Breaks LIVE: A Million Ideas, One Question: Where Do You Start? (episode description) | Federation of Tax Administrators | podcast | https://rss.com/es/podcasts/taxbreaks/ | 2026-06-23 |
| WITHUM-SEATA-2026 | Key Takeaways From the 2026 SEATA Conference | Withum | firm | https://www.withum.com/resources/key-takeaways-from-the-2026-seata-conference/ | 2026-07-14 |
| COST-TECH-2026 | 2026 SALT in a Digital World Workshop agenda | Council On State Taxation | conference | https://www.cost.org/globalassets/cost/cost-events/2026tech-agenda-260226-revised.pdf | 2026-02-26 |
| AKERMAN-COST-2026 | Stefi George to Speak on Defending AI-Driven Tax Audits at COST's 57th Annual Meeting | Akerman LLP | firm | https://www.akerman.com/en/perspectives/stefi-george-to-speak-on-defending-ai-driven-tax-audits-at-costs-57th-annual-meeting.html | 2026-09-23 |
| STI-AIAUDITS-2026 | AI in State Tax: New Tools, Familiar Risks (webinar listing) | Sales Tax Institute | vendor | https://www.salestaxinstitute.com/sales-tax-education/ai-in-state-tax-audits | 2026-06-25 |
| SALESTAX-AIAUDIT-2026 | Are You Using AI to Find Businesses That Aren't Paying Sales Tax? | The Sales Tax People | firm | https://sales.tax/sales-tax-updates/states-ai-sales-tax-audits-enforcement-2026/ | 2026-05-18 |
| AVALARA-TRENDS-2025 | Avalara Report Shows ... States Eyeing AI to Shore Up Audit Teams ... | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2025/01/21/avalara-report-shows-sales-tax-simplification-efforts-states-eyeing-ai-to-shore-up-audit-teams-and-e-invoicing-growth-in-2025/154946/ | 2025-01-21 |
| YAHOO-NYAI-2024 | New York and other states are using AI to hunt down wealthy remote workers and demand more tax | Yahoo (summarising CNBC) | press | https://news.yahoo.com/tech/york-other-states-using-ai-112406645.html | 2024-04-16 |
| ROUTEFIFTY-REV-2026 | From pilot to proof: How revenue agencies can launch AI responsibly | Route Fifty | press | https://www.route-fifty.com/artificial-intelligence/2026/07/pilot-proof-how-revenue-agencies-can-launch-ai-responsibly/415141/ | 2026-07-31 |
| KTS-OPR-2026 | Using AI in Tax Practice: What Practitioners Need to Know Before Filing Season | Kilpatrick Townsend & Stockton | firm | https://ktslaw.com/blog/kilpatricks-state-and-local-tax-blog/2026/9/using-ai-in-tax-practice-what-practitioners-need-to-know-before-filing-season | 2026-09-29 |
| SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. (abstract) | TaxProf Blog / Tax Notes State | academic | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 |
| TRFORD-SALT-2026 | Multistate Tax Trends: A Q&A with SALT Expert Niki Ford | Thomson Reuters Tax & Accounting | vendor | https://tax.thomsonreuters.com/news/multistate-tax-trends-a-qa-with-salt-expert-niki-ford-on-nexus-marketplaces-ai-and-the-future/ | 2026-04-09 |
| EIDE-SALT-2026 | State & Local Tax Meets AI: How Technology Is Reshaping Taxability, Nexus, and State Enforcement | Eide Bailly | firm | https://www.eidebailly.com/insights/blogs/2026/4/salt20260430 | 2026-04-30 |
| MOSSADAMS-AISALT-2025 | Boost compliance and help reduce exposure by understanding AI SALT impacts | Moss Adams | firm | https://www.mossadams.com/articles/2025/04/ai-state-and-local-tax-considerations | 2025-04-11 |
| MOSSADAMS-AIWEBCAST-2025 | State and Local Tax Implications for AI Companies (webcast) | Moss Adams | firm | https://www.mossadams.com/events/2025/08/navigating-state-and-local-tax-for-ai-companies | 2025-08 |
| TRUSS-KINTSUGI-2026 | What's Changing in Sales and Business Tax - And How AI Can Help (webinar listing) | Truss with Kintsugi | vendor | https://gettruss.io/events/sales-business-tax-ai | 2026-09-17 |
| GUSTO-MOSEY-2026 | Gusto Welcomes Mosey to Close the Compliance Gap for Small Businesses | Gusto | vendor | https://www.gusto.com/resources/company-news/gusto-mosey-acquisition | 2026-04-13 |
| FINTECHGLOBAL-GUSTO-2026 | Gusto and Mosey unite to tackle small business compliance | Fintech Global | press | https://fintech.global/2026/04/13/gusto-and-mosey-unite-to-tackle-small-business-compliance/ | 2026-04-13 |
| WARP-REG-2026 | How to register for state payroll taxes | Warp | vendor | https://www.warp.co/blog/how-to-register-for-state-payroll-taxes | 2026-02-19 |
| SKYVERN-REG-2026 | Automating Payroll Registration Across All 50 States | Skyvern | vendor | https://www.skyvern.com/blog/automating-payroll-registration-50-states/ | 2026-03-27 |
| ALTERYX-APPORT-2026 | Tax Apportionment Factor Computation Starter Kit | Alteryx | vendor | https://www.alteryx.com/starter-kit/tax-apportionment-factor-computation | 2026-07-16 |
| WK-APPORT-2014 | Wolters Kluwer, CCH Launches Apportionment Suite | Accounting Today | press | https://www.accountingtoday.com/news/wolters-kluwer-cch-launches-apportionment-suite | 2014-09-29 |
| BYRON-2026 | Byron Launches with AI Agents for Business Tax Preparation Workflows | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/05/27/byron-launches-with-ai-agents-for-business-tax-preparation-workflows/184034/ | 2026-05-27 |
| VALS-TAXAGENT-2026 | Tax Agent Bench: Agentic US corporate tax research | Vals AI | vendor | https://www.vals.ai/benchmarks/tax_agent_bench | 2026-10-20 |
| BLUEJ-RAISE-2025 | Blue J raises $122m to scale AI-powered tax research | Fintech Global | press | https://fintech.global/?p=210135 | 2025-08-05 |
| MERCOR-SALT-2026 | SALT (State and Local Taxation) Experts (job listing) | Mercor via AlignList | job-posting | https://alignlist.com/jobs/mercor-salt-state-and-local-taxation-experts-list-aaabnrlzswees5emkwdpflcl | 2026-06-12 |
| AVALARA-AVIATOR-2026 | Avalara Aviator: AI Tax and Compliance Agent Hub | Avalara | vendor | https://www.avalara.com/gb/en-gb/products/aviator.html | 2026-09-25 |
| OLIVER-1065-2026 | When AI Can Prepare a Partnership Return, What Happens to the Business Model? | Blake Oliver (blog) | press | https://www.blakeoliver.com/blog/when-ai-can-prepare-a-partnership-return | 2026-03-03 |

**Counts by type (40 sources):** press 11, vendor 9, firm 7, regulator 5, podcast 3, academic 2, conference 2, job-posting 1. Six of the 40 (CDTFA-2025, CDTFA-PR-2025, SALA-TAXNOTES-2026, FTA-TAXBREAKS-2026, AVALARA-AVIATOR-2026, OLIVER-1065-2026) are cited only in the notes or in section 4, not in a use-case entry.

All 40 sources were opened and read (`access: full`); the FTA episode and the Sala article were read as descriptions or abstracts only, and several pages were read through the r.jina.ai mirror (MTC pages and reports, Withum, Alteryx, Vals, Gusto). Search-only items are described under Gaps.

## 6. Gaps

- **No firm-side practice evidence.** No named mid-market or top-100 firm, and no PE-backed platform, was found describing AI in multistate income and franchise tax, apportionment, nexus studies or voluntary disclosure. Firm SALT service pages found (Baker Tilly, Aprio, Frazier & Deeter via search summaries; Citrin Cooperman blocked, 403) describe nexus and apportionment work without AI. This is an absence in public sources, not proof of non-use.
- **No quality evidence.** No error, override or parallel-run result for any multistate AI use. The only independent measure is the Vals benchmark, adjacent and mostly federal.
- **Practitioner communities not reached:** r/taxpros and similar (blocked per the landscape file). Bloomberg Tax pages and Law360 are paywalled or returned 404; Bloomberg Tax's 2026 AI guide was not opened.
- **Conference material:** COST annual meeting agenda PDFs returned 404; the "Audit-Tron" session title seen in a search summary could not be verified (only the Akerman announcement was read). AICPA SALT technical resource panel materials were not found. The FTA generative AI white paper (expected Aug 2025) and the FTA 2024 agency survey were not located. The FTA Annual Meeting 2026 episode was read by description only.
- **Agency primary sources:** South Carolina's contract, the FAST audit module documentation, the California FTB's models and New York's CISS contract were not available; the reporters' accounts are the only source. Washington, Texas, Pennsylvania, Georgia, Virginia and other individual state AI programmes were not found beyond the items cited.
- **Original CNBC report** (New York AI letters, Apr 2024) was not opened; Yahoo's summary is used.
- **Payroll nexus:** vendor material only (Gusto/Mosey, Warp, Skyvern); a Middesk page returned 404. No evidence of a middle-market payroll or HRIS vendor shipping a remote-worker nexus agent; no customer outcomes.
- **Search-only observations (not used for grading):** a search result placed COST's 57th Annual Meeting at 22 to 25 September 2026; a Sales Tax Institute listing was shown with a 24 Sep 2026 session date; the Alteryx and TaxGPT items were seen first in search summaries (Alteryx was then read via mirror; a TaxGPT SALT job posting was not readable, so it is not used).
- **State conformity, pass-through entity tax elections and state tax credits:** no AI-specific evidence found beyond the single Vals PTET question.
