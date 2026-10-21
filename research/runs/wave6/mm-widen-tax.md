# Widen tax for private, owner-managed clients: pass-through, owner-level and entity-choice work

Researched 2026-10-21. Archetype: tax (mid-market extension). Module: widen-tax, extending `compliance-individual-business` (S corporation and partnership returns, K-1 flow to owners, basis, reasonable compensation, owner estimates) and `research-advisory` (entity choice, owner planning). One short section on trusts, estates and gifts. Angle: combined (practice, discourse, governance and evidence). Read first: the mid-market landscape, the vocabulary, the tax `ARCHETYPE.md`, both module files and both use-case files. Entries below add to those files; where a source supports an existing entry it is listed under "Routed to other modules".

## 1. Summary

- **Evidence is thin and almost entirely vendor-published.** I read 46 distinct sources (section 5). Thirteen use cases: none reaches grade A, two are grade B (a named firm's account, no published measurement), ten are grade C (vendor claims or product pages) and one is grade D (a practitioner-recommended control, labelled "idea"). No independent error rate, override rate or parallel-run result was found for any AI work on S corporation returns, partnership returns, basis, reasonable compensation, entity choice or fiduciary returns.
- **The existing module files already cover agent-prepared 1065, 1120-S and 1041 returns, K-1 extraction and trial-balance workpapers.** What they lack, and what this pass adds: reasonable-compensation studies, basis and distribution-limit tracking, multi-entity client workspaces, owner estimates, entity-return review, replacement of the tax engine with AI-native e-file, return-derived owner planning, S-election and pass-through entity tax (PTET) calculators, owner-exit structuring, and estate and gift tooling.
- **Most new material comes from AI-native vendors and small firms, not mid-market firms.** Instead, Filed and Gelt publish pages that name basis, AAA, reasonable compensation, shareholder estimates and S-election or PTET estimates as automated steps, and WageProof sells reasonable-compensation reports. None names a mid-market customer for those steps. The named mid-market firms in this field (Maxwell Locke & Ritter, a top-100 firm; WCG, a regional firm; Armanino and Boulay in the existing files) appear in connection with K-1-heavy individual and partnership preparation, which the existing files already hold. Firm kinds for the other named examples: One Stop CPA is a seven-person digital firm, Paramount Tax and JCG Tax are small firms, and Aardvark Tax Advisors is the practice arm of a venture-backed small-business platform. In the Thomson Reuters survey, "large" means 30 or more professionals and "midsize" 4 to 29, so its size splits describe smaller firms than this project's mid-market [TR-SOTP-2026].
- **The best discourse is about trust and review cost, not capability.** A sponsored summit recap reports a firm leader saying preparers re-checked everything AI produced, so firms paid for both tokens and labour [OLIVER-BOSUMMIT-2026]. A regional firm (WCG) says K-1 handling is the minimum bar and a vendor that cannot do it is not ready [WCG-NOTREADY-2026].
- **Governance is mostly existing Circular 230 and section 7216 duty applied to AI.** IRS OPR Alert 2026-19 ties AI use to due diligence, competence, firm procedures and fees [IRS-OPR-2026]. The open question is whether sending return data to an AI tool needs section 7216 consent, and the IRS has not said [CPAPA-7216-2026]. On the IRS side, TIGTA reports that the IRS's large-partnership programme is starting to use AI for risk selection, with early results that are not yet convincing [JOFA-TIGTA-2026].
- **Trusts, estates and gifts:** the AI that reaches firms is advisor-side planning software and attorney-side practice guidance, not fiduciary return preparation. Instead lists 1041 as live and 706 and 709 as coming (vendor roadmap). No firm-level evidence was found.

## 2. Use cases

Ids use the existing module's id plus a placeholder number (`-new-NN`). Dates for undated vendor pages are the access date (2026-10-21), and each entry says so in its locator. Figures are copied with what they measure.

```yaml
- id: tax-compliance-individual-business-new-01
  title: Reasonable-compensation study for S corporation owners, built duty by duty from wage data with a dated record
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Owners who work in their S corporation must pay themselves wages that are reasonable, and the IRS says there are no specific
    guidelines in the Code or regulations, only factors courts have used [IRS-FS200825-2008]. Many owners rely on a fixed ratio
    or a figure from a chatbot, and a practitioner-vendor writes that a custom study has been a one-off engagement costing
    thousands of dollars [NATP-RCOMP-2026].
  solution: >-
    Instead lists "Reasonable compensation analysis" as a ready-to-run agent workflow and as part of its S corporation tax plan
    [INSTEAD-SCORP-2026]. WageProof, whose page does not describe its method as AI, writes a study for each S corporation client
    that prices the owner's duties with Bureau of Labor Statistics wage data for the client's area and names the source of every
    wage figure; the client fills in a questionnaire or the firm does [WAGEPROOF-2026]. An earlier product, RCReports (2023), offers
    cost and market approaches over a proprietary wage database and a client questionnaire [RCREPORTS-IA-2023]. Against this, the
    NATP post by WageProof's founder says that in his testing the wage citations a chatbot gave often did not check out [NATP-RCOMP-2026].
  outcomes:
    - lever: quality
      description: >-
        The WageProof founder reports that when he pulled the BLS series a chatbot named, the figures were frequently not there and
        some cited sources did not exist. No counts or rates are given.
      figure: none published
      measures: qualitative description of the author's own testing of chatbot wage citations; no numerator or denominator
      provenance: vendor-published
      source_ref: NATP-RCOMP-2026
    - lever: cost
      description: >-
        WageProof lists a single report at $199, and firm plans at as low as $25 per report; its own page gives annual plans from
        $499 for 10 reports to $1,499 for 60.
      figure: "$199 single report; as low as $25 per report on firm plans"
      measures: list prices for one reasonable-compensation report, as stated by the vendor
      provenance: vendor-published
      source_ref: NATP-RCOMP-2026
    - lever: speed
      description: The WageProof page says creating a client report takes about 15 minutes.
      figure: about 15 minutes
      measures: vendor statement of the time to create one client report; sample and baseline not given
      provenance: vendor-published
      source_ref: WAGEPROOF-2026
  prerequisites:
    - A specific description of what the owner does and how much time each duty takes
    - Wage data from a recognised source, with the year, geography and percentile choices stated
    - A dated analysis, and a resolution adopting the salary, written in the year the salary is set (per the NATP post)
  risks_and_guardrails:
    - >-
      The IRS fact sheet lists factors courts have used, such as training and experience, duties and time devoted, and says there
      are no specific guidelines in the Code or regulations [IRS-FS200825-2008]
    - >-
      The NATP post says a salary set too low invites reclassification of distributions as wages, with back employment taxes,
      interest and a possible accuracy-related penalty under section 6662, and that the preparer can face a section 6694 penalty
      [NATP-RCOMP-2026]
    - >-
      A practitioner who tested ChatGPT in August 2024 judged it often adequate for a starting number but said the model does
      not do tax accounting or tax law well; the post is older than 18 months [EVERGREEN-CHATGPT-2024]
    - OPR Alert 2026-19 says due diligence requires verifying facts, citations and calculations that AI produces [IRS-OPR-2026]
    - Both authors of the vendor-side sources sell reasonable-compensation tools; there is no independent test
  human_checkpoints:
    - Preparer confirms the duty descriptions and the match of each duty to an occupation
    - Reviewer checks that every wage figure traces to a source an examiner could look up
    - Annual refresh when duties, the business or wage data change
  role_evolution: >-
    NATP's 2026 Taxposium programme included a one-CPE session titled "Advisory Opportunities with Reasonable Compensation"
    [NATP-TAXPOSIUMAG-2026]. The vendor pitch is that a branded study becomes a firm-delivered service rather than something the
    owner searches for free [NATP-RCOMP-2026].
  evidence_grade: C
  sources:
    - { ref: INSTEAD-SCORP-2026, title: "Instead for S Corporations (1120-S): AI Tax Agent", publisher: "Instead", type: vendor, url: "https://webflow.instead.com/products/s-corporation", date: "2026-10-21", access: full, locator: "page undated, date is access date; feature list and 'Ready to run' workflows" }
    - { ref: WAGEPROOF-2026, title: "Reasonable Compensation Software for CPAs & EAs", publisher: "WageProof", type: vendor, url: "https://www.wageproof.com/for-cpas", date: "2026-10-21", access: full, locator: "page undated, date is access date; hero text, 'Create a client report', pricing line" }
    - { ref: NATP-RCOMP-2026, title: "Four reasonable compensation mistakes S-corp clients make", publisher: "National Association of Tax Professionals (sponsored content by WageProof's founder, Josh Green)", type: vendor, url: "https://www.natptax.com/news-insights/blog/four-reasonable-compensation-mistakes-s-corp-clients-make/", date: "2026-09-16", access: full, locator: "Mistake 3; 'Why owners skip a proper study'; 'How WageProof approaches this'; read through the r.jina.ai mirror (direct curl 403)" }
    - { ref: IRS-FS200825-2008, title: "Wage Compensation for S Corporation Officers (FS-2008-25)", publisher: "Internal Revenue Service", type: regulator, url: "https://www.irs.gov/pub/irs-news/fs-08-25.pdf", date: "2008-08", access: full, locator: "'What's a Reasonable Salary?'" }
    - { ref: RCREPORTS-IA-2023, title: "Insightful Accountant & Tax Practice News First Look on RCReports", publisher: "Insightful Accountant", type: press, url: "https://insightfulaccountant.com/accounting-tech/vendor-news/insightful-accountant-tax-practice-news-first-look-on-rcre", date: "2023-02-24", access: full, locator: "'Evaluating Reasonable Compensation'; the article says it is based on information the developer submitted" }
    - { ref: EVERGREEN-CHATGPT-2024, title: "Using ChatGPT to Determine S Corporation Reasonable Compensation", publisher: "Evergreen Small Business (CPA practitioner blog)", type: press, url: "https://evergreensmallbusiness.com/using-chatgpt-to-determine-s-corporation-reasonable-compensation/", date: "2024-09-09", access: full, locator: "opening paragraphs and the August 2024 prompt example" }
    - { ref: NATP-TAXPOSIUMAG-2026, title: "Taxposium 2026 agenda", publisher: "National Association of Tax Professionals", type: conference, url: "https://taxposium.natptax.com/agenda", date: "2026-07", access: full, locator: "session list, Day 2: title and speaker (Nancy McClelland, CPA) only; no abstract" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Circular 230 section 10.22" }
  last_reviewed: "2026-10-21"
  notes: >-
    No named firm, mid-market or otherwise, was found using AI for this step. The product that most closely fits (WageProof) is not
    described as AI, so the AI contribution is the agent workflow at Instead and the questionnaire-to-report step. Taxposium dates
    are 13-15 July 2026 (past); only the title was read.

- id: tax-compliance-individual-business-new-02
  title: Shareholder and partner basis, AAA and distribution-limit schedules computed from the return, with alerts on negative basis
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [data-reporting, transaction-processing]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Reviewers of 1120-S and 1065 returns are expected to confirm shareholder basis schedules, the choice between the default
    basis method and the section 1367 election, partnership capital accounts under section 704(b) and the effect of debt, and
    these are among the topics a state-society course names for return reviewers [NYSSCPA-1120S1065-2025]. The IRS has a form
    for S corporation shareholders to figure stock and debt basis limitations (Form 7203) [IRS-F7203-2026].
  solution: >-
    Instead says its S corporation agent includes shareholder basis calculations, AAA and OAA tracking and K-1 generation for
    every shareholder, populated from workpapers [INSTEAD-SCORP-2026]. Intuit Tax Advisor (2024) shows stock and debt basis from
    the imported return, tracks the effect of strategies added to a projection, and alerts when distributions and changes
    produce negative basis [INTUIT-BASIS-2024]. Thomson Reuters says CoCounsel Tax can work through passive activity limits and
    at-risk basis with a source behind every answer [TR-COCOUNSELTAX-2026].
  outcomes:
    - lever: quality
      description: none published; the sources describe features only
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: INSTEAD-SCORP-2026
  prerequisites:
    - Prior-year returns and, where the history is incomplete, a reconstruction of opening basis
    - Complete entity financials and shareholder or partner agreements, including loans and contributions
    - Return software or an agent that stores the schedule year to year
  risks_and_guardrails:
    - >-
      Intuit's page says its tracking works from the imported return and does not require simulating future years; it does not
      claim to rebuild missing history [INTUIT-BASIS-2024]
    - No independent test of any AI-computed basis schedule was found
    - OPR Alert 2026-19 requires verification of facts, citations and calculations the AI produces [IRS-OPR-2026]
  human_checkpoints:
    - Preparer agrees opening basis and each year's contributions, loans and distributions to source records
    - Reviewer signs off any schedule where the tool reports negative or restored basis
  role_evolution: >-
    Not described in the sources. The course description shows the check is currently a reviewer skill learned by
    checklist [NYSSCPA-1120S1065-2025].
  evidence_grade: C
  sources:
    - { ref: INSTEAD-SCORP-2026, title: "Instead for S Corporations (1120-S): AI Tax Agent", publisher: "Instead", type: vendor, url: "https://webflow.instead.com/products/s-corporation", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'The S Corporation return' list and 'Tax return preparation'" }
    - { ref: INTUIT-BASIS-2024, title: "S corporation basis tracking in Intuit Tax Advisor", publisher: "Intuit", type: vendor, url: "https://accountants.intuit.com/taxprocenter/practice-management/s-corporation-basis-tracking-in-intuit-tax-advisor", date: "2024-07-03", access: full, locator: "opening paragraphs" }
    - { ref: TR-COCOUNSELTAX-2026, title: "CoCounsel Tax (firm product page)", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/products/cocounsel-tax", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Faster research with trusted sources'" }
    - { ref: IRS-F7203-2026, title: "About Form 7203, S Corporation Shareholder Stock and Debt Basis Limitations", publisher: "Internal Revenue Service", type: regulator, url: "https://www.irs.gov/forms-pubs/about-form-7203", date: "2026-06-27", access: full, locator: "opening sentence; date is the page's last-reviewed date" }
    - { ref: NYSSCPA-1120S1065-2025, title: "Forms 1120-S and 1065 Return Review Boot Camp for New and Experienced Reviewers (webcast)", publisher: "NYSSCPA", type: conference, url: "https://nysscpa.org/catalog/events/1016910-forms-1120-s-and-1065-return-review-boot-camp-for-new-and-experienced-reviewers-webcast-2025-18-11", date: "2025-11-18", access: full, locator: "learning objectives, Form 1120-S and Form 1065 bullets" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Circular 230 section 10.22" }
  last_reviewed: "2026-10-21"
  notes: >-
    The brief asked for basis-tracking evidence; none beyond product pages exists. The Intuit page is older than 18 months but is
    the only one that describes the negative-basis alert. Intuit's feature is not described as AI on that page; the Intuit Assist
    page of 2024-06-19 is the generative layer (see research-advisory-new-02).

- id: tax-compliance-individual-business-new-03
  title: One agent per client holds every entity they own (1040, 1120-S, 1065, 1041) and its filing history
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [data-reporting, coordination-scheduling]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    Owner-managed clients usually have a personal return, one or more operating entities and sometimes a trust, but returns are
    prepared and reviewed one at a time. Instead says most CPA firm clients have more than one entity [INSTEAD-CPA-2026].
  solution: >-
    Instead assigns each client an entity agent that indexes every uploaded document (W-2s, K-1s, prior returns, bank
    statements), holds the full filing history, carryforwards, elections and estimated payments, and flags year-over-year
    changes; a firm agent works across all clients [INSTEAD-ENTITY-2026]. The firm page says the agent understands how a
    client's 1040, 1120-S and 1065 interact [INSTEAD-CPA-2026].
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: INSTEAD-ENTITY-2026
  prerequisites:
    - Documents for every related entity in one workspace, with ownership percentages
    - Prior-year returns imported for carryforwards and elections
  risks_and_guardrails:
    - >-
      OPR Alert 2026-19 names cross-client leakage, where data from one client's file is reused to answer a question about
      another, as a privacy risk; a multi-entity workspace must keep ownership groups apart [IRS-OPR-2026]
    - The sources describe a design, not any measured check that entity-to-owner figures agree
  human_checkpoints:
    - Preparer confirms the ownership map and that each K-1 received ties to the entity return that issued it
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
    - { ref: INSTEAD-ENTITY-2026, title: "Instead Entity Agent: AI Tax Agent Per Client Entity", publisher: "Instead", type: vendor, url: "https://instead.com/products/entity-agent", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Upload once', 'Full filing history', 'An agent for every entity type'" }
    - { ref: INSTEAD-CPA-2026, title: "CPA Firms | Instead", publisher: "Instead", type: vendor, url: "https://instead.com/solutions/cpa-firms", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'One client, multiple entities, one conversation'" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "paragraph on repurposed client data" }
  last_reviewed: "2026-10-21"
  notes: >-
    Single-vendor evidence. Instead's own description of customers on the firm pages gives no names.

- id: tax-compliance-individual-business-new-04
  title: Quarterly estimated-tax projections for owners with safe-harbor analysis and flow-through impact
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [data-reporting, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Owners of S corporations and partnerships pay estimated tax on income that flows through from entities whose results are
    known only after the books close, so projections are rebuilt by hand and often late.
  solution: >-
    Instead lists quarterly estimated-tax calculations for shareholders, federal and state, including safe-harbor analysis and
    flow-through impact, and a ready-to-run workflow called "Build shareholder tax estimates (TY26)" [INSTEAD-SCORP-2026].
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: INSTEAD-SCORP-2026
  prerequisites:
    - Current-year entity financials and year-to-date owner payments
    - Prior-year return for the safe-harbor test
  risks_and_guardrails:
    - >-
      A search summary notes that 2026 law changes can make a prior-year safe harbor underpay when 2025 deductions do not
      repeat; thresholds were not verified against IRS Publication 505 (not opened)
    - OPR Alert 2026-19 requires verification of calculations AI produces [IRS-OPR-2026]
  human_checkpoints:
    - Preparer reviews the projection assumptions before the owner is told what to pay
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
    - { ref: INSTEAD-SCORP-2026, title: "Instead for S Corporations (1120-S): AI Tax Agent", publisher: "Instead", type: vendor, url: "https://webflow.instead.com/products/s-corporation", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Tax estimates' and 'Ready to run' workflows" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Circular 230 section 10.22" }
  last_reviewed: "2026-10-21"
  notes: >-
    Thinnest entry in the set: one vendor page. Kept because owner estimates were named in the brief and nothing else in the
    existing files covers them.

- id: tax-compliance-individual-business-new-05
  title: AI first-level review of entity returns - K-1 ties, source tie-out, wage and QBI allocation - before partner review
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Reviewers of 1120-S and 1065 returns work from long checklists covering M-1, M-2, basis schedules and capital accounts, and a
    state-society course describes staff-prepared entity returns as error-prone [NYSSCPA-1120S1065-2025].
  solution: >-
    Filed says its review product cross-checks every figure against the source document and surfaces transposed numbers,
    missing K-1 entries and dropped schedules before the reviewer opens the file; its sample planning report (an illustrative
    client, not a real one) shows the tool finding K-1 Statement A wages mapped to the wrong line, which cut a qualified
    business income (QBI) deduction on Form 8995-A [FILED-HOME-2026]. Instead lists AI return review that runs compliance
    checks against source documents, workpapers and current law, and "three-way review" in its preparation workflow
    [INSTEAD-SCORP-2026; INSTEAD-CPA-2026].
  outcomes:
    - lever: quality
      description: >-
        Filed's sample report claims correcting the wage mapping restores a $54,861 QBI deduction and saves an estimated $20,299
        of federal income tax for an illustrative client.
      figure: "$54,861 QBI deduction restored; $20,299 estimated federal tax saving (illustrative client)"
      measures: dollar impact in one vendor-authored sample planning report for a fictional client; not a measured result
      provenance: vendor-published
      source_ref: FILED-HOME-2026
    - lever: capacity
      description: >-
        A small-firm owner (Paramount Tax) says the tool turned people from preparers into reviewers themselves; a second firm
        (JCG Tax) says the team asked whether enough returns were coming in. The quotes do not name entity returns.
      figure: none published
      measures: two customer testimonials on the vendor's home page; no counts
      provenance: vendor-published
      source_ref: FILED-HOME-2026
  prerequisites:
    - Source documents attached to every figure in the return
    - Firm review checklist the tool can be held to
  risks_and_guardrails:
    - >-
      A summit speaker reported that when firms put AI in front of preparers, the preparers re-checked everything, so firms
      paid for tokens and labour (sponsored recap) [OLIVER-BOSUMMIT-2026]
    - OPR Alert 2026-19 requires verification of calculations AI produces [IRS-OPR-2026]
  human_checkpoints:
    - Reviewer works from the tool's flagged items but samples unflagged items against source
    - Partner signs the return
  role_evolution: >-
    Filed's customers describe a move from preparing to reviewing [FILED-HOME-2026].
  evidence_grade: C
  sources:
    - { ref: FILED-HOME-2026, title: "AI Tax Preparation & Review Software | Filed", publisher: "Filed", type: vendor, url: "https://www.filed.com", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Review', sample 'Tax planning report' Strategy 1, 'Real firms. Real results.'" }
    - { ref: INSTEAD-CPA-2026, title: "CPA Firms | Instead", publisher: "Instead", type: vendor, url: "https://instead.com/solutions/cpa-firms", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Tax preparation' and 'Return review' workflow tiles" }
    - { ref: INSTEAD-SCORP-2026, title: "Instead for S Corporations (1120-S): AI Tax Agent", publisher: "Instead", type: vendor, url: "https://webflow.instead.com/products/s-corporation", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Tax return review'" }
    - { ref: NYSSCPA-1120S1065-2025, title: "Forms 1120-S and 1065 Return Review Boot Camp for New and Experienced Reviewers (webcast)", publisher: "NYSSCPA", type: conference, url: "https://nysscpa.org/catalog/events/1016910-forms-1120-s-and-1065-return-review-boot-camp-for-new-and-experienced-reviewers-webcast-2025-18-11", date: "2025-11-18", access: full, locator: "course description and learning objectives" }
    - { ref: OLIVER-BOSUMMIT-2026, title: "40 Hours of Work Done in 5 Minutes: My Takeaways from Black Ore's AI Tax Summit", publisher: "Blake Oliver (post sponsored by Black Ore)", type: press, url: "https://www.blakeoliver.com/blog/black-ore-ai-tax-summit", date: "2026-06-04", access: full, locator: "section 'From 15 years to 15 months' (Sean McLean)" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "Circular 230 section 10.22" }
  last_reviewed: "2026-10-21"
  notes: >-
    Complements tax-compliance-individual-business-12 (general AI return review); this entry is specific to entity-return
    checks. Filed's customers are small firms and its sample is illustrative.

- id: tax-compliance-individual-business-new-06
  title: AI-native platform replaces the firm's tax engine for entity returns and e-files them (1120-S, 1065, 1041)
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, software-systems]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    A reason firms keep AI tools at arm's length is the "last mile": an AI that prepares a return in its own system cannot hand
    a half-finished return to the firm's tax software, so the work restarts when AI hits its ceiling [WCG-NOTREADY-2026].
  solution: >-
    On 2026-05-08 Instead announced that it completed government testing to e-file and print returns across federal, state and
    local jurisdictions for 1040, 1041, 1120, 1120-S and 1065, and says a firm can use it as a complete replacement for legacy
    tax software [INSTEAD-EFILE-2026]. Its CPA page lists CCH Axcess Tax, UltraTax, Lacerte and others as engines it replaces
    [INSTEAD-CPA-2026].
  outcomes:
    - lever: speed
      description: >-
        Instead says it reduces complex return preparation from 4-6 hours to under 60 minutes and automates a workflow it says
        consumes 60-80% of a firm's staff time.
      figure: "4-6 hours to under 60 minutes; 60-80% of staff time"
      measures: vendor statement about complex return preparation time and the share of staff time spent on preparation workflow; no sample or method
      provenance: vendor-published
      source_ref: INSTEAD-EFILE-2026
  prerequisites:
    - Willingness to move prior-year history and carryforwards into a new system
    - Firm tolerance for single-vendor dependence for filing
  risks_and_guardrails:
    - >-
      WCG warns that a proprietary system can trap prior-year history, make comparison and review harder and force a restart when
      a return needs a human decision [WCG-NOTREADY-2026]
    - >-
      The e-file approval is the company's statement; I found no IRS statement confirming it (a search summary reported none)
  human_checkpoints:
    - CPA signs; reviewer works from the tool's workpapers
  role_evolution: >-
    Instead's CPA page says its target user is one person handling hundreds of returns and rejects offshore and contractor
    preparation [INSTEAD-CPA-2026].
  evidence_grade: C
  sources:
    - { ref: INSTEAD-EFILE-2026, title: "Instead becomes the first new tax platform in decades to pass 100% government testing across all U.S. jurisdictions", publisher: "Instead", type: vendor, url: "https://instead.com/news/instead-first-new-tax-platform-100-percent-us-efile-approvals-all-jurisdictions", date: "2026-05-08", access: full, locator: "paragraphs 1-3" }
    - { ref: INSTEAD-CPA-2026, title: "CPA Firms | Instead", publisher: "Instead", type: vendor, url: "https://instead.com/solutions/cpa-firms", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Cancel your tax software'" }
    - { ref: WCG-NOTREADY-2026, title: "AI Tax Prep in 2026: Not Quite There Yet", publisher: "WCG CPAs & Advisors", type: firm, url: "https://wcginc.com/blog/ai-tax-prep-in-2026-not-quite-there-yet/", date: "2026-07-24", access: full, locator: "vendor evaluation: proprietary-software 'last mile' paragraphs" }
  last_reviewed: "2026-10-21"
  notes: >-
    A product announcement, not a deployment. Overlaps tax-compliance-individual-business-08 (agent inside the firm's software);
    this entry is the opposite design choice (replace the engine).

- id: tax-compliance-individual-business-new-07
  title: Estate, gift and fiduciary returns (706, 709, 1041) prepared by agents from governing documents
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [document-production, transaction-processing]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: >-
    Fiduciary, estate and gift returns are low-volume and document-heavy, and mid-market firms do them for owner families. In
    the 2026 AICPA tax software survey, 20% of respondents said they are expanding the services they offer, and 42% of those
    named estate, trust and gift financial planning [AICPA-TAXSW-2026].
  solution: >-
    Instead lists 1041 (fiduciary returns, beneficiary distributions) among the entity types its agent covers and lists 706
    and 709 as "Coming 2026" for tax year 2026 [INSTEAD-ENTITY-2026]. Thomson Reuters' fiduciary page describes fiduciary
    accounting software and a calendar for 1040, 1041, 706 and 709 deadlines; the descriptions I read did not describe an AI
    function [TR-FIDUCIARY-2026].
  outcomes:
    - lever: capacity
      description: none published
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: INSTEAD-ENTITY-2026
  prerequisites:
    - Trust instruments, wills and valuations in readable form
  risks_and_guardrails:
    - 706 and 709 are announced for a future tax year, not available
    - No independent test of AI on fiduciary or estate returns was found
  human_checkpoints:
    - Preparer reads the governing instrument against the draft allocation to beneficiaries
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
    - { ref: INSTEAD-ENTITY-2026, title: "Instead Entity Agent: AI Tax Agent Per Client Entity", publisher: "Instead", type: vendor, url: "https://instead.com/products/entity-agent", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'An agent for every entity type' (1041; 'Coming 2026' list)" }
    - { ref: AICPA-TAXSW-2026, title: "2026 tax software survey (1,808 AICPA members; AI adoption questions)", publisher: "The Tax Adviser (AICPA)", type: survey, url: "https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/", date: "2026-08-31", access: full, locator: "section 'Use of AI and other technical tools', last paragraphs on service expansion" }
    - { ref: TR-FIDUCIARY-2026, title: "Fiduciary tax solutions (ONESOURCE)", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/corporation-solutions/fiduciary-tax-solutions", date: "2026-10-21", access: full, locator: "page undated, date is access date; product tiles for ONESOURCE Fiduciary Accounting and Fiduciary Calendar" }
  last_reviewed: "2026-10-21"
  notes: >-
    tax-compliance-individual-business-06 already covers 1041 through K-1s (Accrual). The addition here is estate and gift
    returns. Search-only items not used as evidence: Datagrid and Digiqt vendor blogs on trust tax agents (not opened).

- id: tax-compliance-individual-business-new-08
  title: AI-native practice for owner-managed businesses where managers review AI-assisted entity returns and own planning
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [expert-judgment, review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: model
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Small and mid-sized practices serving owners are short of experienced reviewers, and a Black Ore executive puts the
    profession's shortfall at 125 million hours a year (sponsored recap; a vendor figure) [OLIVER-BOSUMMIT-2026].
  solution: >-
    Aardvark Tax Advisors, the accounting practice of Cynch AI, describes itself as an AI-native tax, accounting and advisory
    firm for small businesses and entrepreneurs, growing organically and by acquisition [AARDVARK-STM-2026]. Its Senior Tax
    Manager posting says the practice is integrating AI-enabled tools into tax delivery and expects the manager to review
    AI-assisted output, judge whether work is ready for a client, lead preparation and review of corporate, partnership,
    individual, trust and estate returns, and deliver planning beyond compliance [AARDVARK-STM-2026].
  outcomes:
    - lever: capacity
      description: none published; the posting states duties and requirements only
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: AARDVARK-STM-2026
  prerequisites:
    - Managers with ten or more years of entity and planning experience who can review AI-assisted work
    - Proprietary AI tooling (per the posting)
  risks_and_guardrails:
    - The posting says tools support the work and people remain accountable for the outcome [AARDVARK-STM-2026]
    - A summit panelist said a small firm can implement a tool in two to four weeks, a large firm in 18 to 24 months; both are statements, not measurements (sponsored recap) [OLIVER-BOSUMMIT-2026]
  human_checkpoints:
    - Manager reviews every return before it leaves the practice
  role_evolution: >-
    The role is defined as reviewer, planner and team lead rather than preparer: a manager who can tell client-ready from
    not-ready AI-assisted work [AARDVARK-STM-2026].
  evidence_grade: B
  sources:
    - { ref: AARDVARK-STM-2026, title: "Senior Tax Manager (Aardvark Tax Advisors, Cynch AI)", publisher: "Cynch AI (posting copies at jobs.auditfriendly.co and startup.jobs)", type: job-posting, url: "https://jobs.auditfriendly.co/jobs/senior-tax-manager-cynch-ai-f487bd54921b", date: "2026-09", access: full, locator: "'About the role' and 'What You'll Do'; the copy says the posting closed on 2026-09-09; posting date not captured; the 'strategic acquisitions' line appears on the startup.jobs copy (https://startup.jobs/senior-tax-manager-cynch-ai-9806576); both read through the r.jina.ai mirror" }
    - { ref: OLIVER-BOSUMMIT-2026, title: "40 Hours of Work Done in 5 Minutes: My Takeaways from Black Ore's AI Tax Summit", publisher: "Blake Oliver (post sponsored by Black Ore)", type: press, url: "https://www.blakeoliver.com/blog/black-ore-ai-tax-summit", date: "2026-06-04", access: full, locator: "sections 'The talent shortage' and 'From 15 years to 15 months'" }
  last_reviewed: "2026-10-21"
  notes: >-
    Grade B rests on one job posting that says AI tools are being integrated; it names no result. The firm is a venture-linked
    small-business practice, not a mid-market firm. Overlaps tax-compliance-individual-business-24 (AI-native roll-ups).

- id: tax-research-advisory-new-01
  title: S-election and state pass-through entity tax (PTET) calculators and break-even plans, offered to owners and run by firms
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [expert-judgment, data-reporting]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Owners hear that an S election or a PTET election "saves tax" and want to know whether it is worth it for their business;
    generic calculators handle W-2 cases only [GELT-CALC-2025].
  solution: >-
    Gelt, an AI-native tax firm, launched a hub of AI-powered calculators on 2025-12-29, with an S Corp calculator for
    self-employment tax and a PTET calculator, and says owners can move from estimate to expert execution with the firm
    [GELT-CALC-2025]. Instead lists "Build an S Corporation tax plan (TY26)" as a workflow with reasonable compensation and
    distribution strategy [INSTEAD-SCORP-2026]. Filed's sample planning report shows a Maryland PTET election with an estimated
    $22,222 per year of savings for an illustrative client [FILED-HOME-2026]. Thomson Reuters says CoCounsel Tax can evaluate S
    corporation conversions and partnership structures against Checkpoint content, with citations [TR-COCOUNSELCORP-2026].
  outcomes:
    - lever: growth
      description: >-
        The calculators are lead generation: Gelt says they let owners estimate the dollar value of a strategy before engaging
        the firm. No conversion figure is published.
      figure: none published
      measures: not applicable
      provenance: vendor-published
      source_ref: GELT-CALC-2025
  prerequisites:
    - Owner income, wages and state data
    - A reasonable-compensation figure (see compliance new-01)
  risks_and_guardrails:
    - >-
      OPR Alert 2026-19 lists Circular 230 section 10.37 (written advice must rest on reasonable factual and legal assumptions
      and reasonable consideration of all relevant facts) among the duties that apply [IRS-OPR-2026]
    - Estimated savings in the sources are vendor or illustrative figures
  human_checkpoints:
    - Adviser confirms facts, state treatment and the assumptions behind any savings figure before it reaches the owner
  role_evolution: >-
    Calculators move the first estimate to the owner; the firm's work shifts to checking the assumptions and implementing
    [GELT-CALC-2025].
  evidence_grade: C
  sources:
    - { ref: GELT-CALC-2025, title: "Gelt Launches Tax Calculator Hub to Help Business Owners Quantify Advanced Tax Strategies", publisher: "Gelt", type: vendor, url: "https://www.joingelt.com/blog/ai-tax-calculators-business-owners", date: "2025-12-29", access: full, locator: "overview bullets and 'Turning Complex Tax Strategies Into Clear Dollar Estimates'" }
    - { ref: INSTEAD-SCORP-2026, title: "Instead for S Corporations (1120-S): AI Tax Agent", publisher: "Instead", type: vendor, url: "https://webflow.instead.com/products/s-corporation", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Ready to run' workflows" }
    - { ref: FILED-HOME-2026, title: "AI Tax Preparation & Review Software | Filed", publisher: "Filed", type: vendor, url: "https://www.filed.com", date: "2026-10-21", access: full, locator: "page undated, date is access date; sample report Strategy 3" }
    - { ref: TR-COCOUNSELCORP-2026, title: "CoCounsel Tax: The AI tax assistant for in-house teams", publisher: "Thomson Reuters", type: vendor, url: "https://tax.thomsonreuters.com/en/products/cocounsel-tax/corp", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Analyze transactions and restructuring scenarios'" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "item 5, section 10.37" }
  last_reviewed: "2026-10-21"
  notes: >-
    The firm-side version, with a measured-by-the-firm estimate of project time, is tax-research-advisory-09 (Accordance, Finney
    Neill). State PTET mechanics belong to multistate-private (see section 4).

- id: tax-research-advisory-new-02
  title: Planning opportunities mined from filed owner returns and client data across the book, with dollar estimates
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [data-reporting, expert-judgment]
  pattern: bulk-transformation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    In the 2026 AICPA tax software survey, 93% of respondents said they use no tool to review returns for planning
    opportunities [AICPA-TAXSW-2026]. In the Thomson Reuters 2026 survey, 74% of respondents said clients strongly want
    additional financial advice, yet advisory margins are 20-24% against 28% for individual return preparation [TR-SOTP-2026].
  solution: >-
    Intuit Tax Advisor generates strategies automatically from ProConnect or Lacerte returns, and Intuit Assist (generative AI)
    answers questions and completes custom plans from the firm's goals; Intuit says the tool's existing strategies keep it from
    inventing recommendations [INTUIT-ASSIST-2024]. Wolters Kluwer describes CCH Axcess Advisor as surfacing opportunities
    hidden in client data, identifying which clients a given provision (for example, the 2025 tax law changes) affects, and
    drafting outreach with Expert AI [WK-WHATSNEW-2025]. Filed's Tax Planner builds an evidence-based plan from the return
    [FILED-HOME-2026]. A regional firm, WCG, says secure environments can already support tax plan comparisons and strategy
    recommendations [WCG-NOTREADY-2026].
  outcomes:
    - lever: growth
      description: >-
        In the AICPA survey, 93% of respondents did not use any other technology tool or application to review tax returns for
        planning opportunities; Holistiplan was used by 2%, and 5% used some other tool.
      figure: "93% did not use a planning-review tool; 2% used Holistiplan"
      measures: >-
        share of 1,808 AICPA members who prepared 2025 returns for a fee, answering whether they use other technology tools to
        review tax returns to highlight planning opportunities; the survey is not AI-specific
      provenance: independent
      source_ref: AICPA-TAXSW-2026
    - lever: growth
      description: >-
        In the Thomson Reuters survey, 28% of respondent firms plan to start offering tax strategy in the next 12 months and 37%
        are considering it.
      figure: "28% planning; 37% considering"
      measures: share of respondents saying their firm plans or is considering to start offering tax strategy services in the next 12 months
      provenance: independent
      source_ref: TR-SOTP-2026
  prerequisites:
    - Return data in the tool's format (ProConnect or Lacerte for Intuit; CCH Axcess for Advisor)
    - Pricing for advisory work; the Thomson Reuters survey reports advisory margins below compliance margins
  risks_and_guardrails:
    - >-
      Advisory impact in Intuit's tool is "estimated and not guaranteed" per the page's own footnote [INTUIT-ASSIST-2024]
    - Written advice must meet Circular 230 section 10.37 [IRS-OPR-2026]
    - Product pages are vendor claims; no accuracy or uptake data for the AI layers was found
  human_checkpoints:
    - Adviser confirms eligibility and substance before any strategy is proposed to the owner
  role_evolution: >-
    Thomson Reuters reports that among firms that reallocated tasks, 39% did so to free professionals for advisory work
    [TR-SOTP-2026].
  evidence_grade: C
  sources:
    - { ref: AICPA-TAXSW-2026, title: "2026 tax software survey (1,808 AICPA members; AI adoption questions)", publisher: "The Tax Adviser (AICPA)", type: survey, url: "https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/", date: "2026-08-31", access: full, locator: "section 'Use of AI and other technical tools', paragraph on planning-opportunity tools" }
    - { ref: TR-SOTP-2026, title: "2026 State of Tax Professionals Report", publisher: "Thomson Reuters Institute", type: survey, url: "https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2026/06/2026-State-of-Tax-Professionals-Report.pdf", date: "2026-06", access: full, locator: "executive summary p.4 (74%, margins); Figure 14 p.19; Figure 19 task reallocation" }
    - { ref: INTUIT-ASSIST-2024, title: "New! Intuit Assist for Intuit Tax Advisor", publisher: "Intuit", type: vendor, url: "https://accountants.intuit.com/taxprocenter/advisory-services/intuit-assist-for-intuit-tax-advisor/", date: "2024-06-19", access: full, locator: "opening paragraphs and footnote" }
    - { ref: WK-WHATSNEW-2025, title: "What's new with CCH Axcess Tax", publisher: "Wolters Kluwer", type: vendor, url: "https://wolterskluwer.com/en/expert-insights/whats-new-with-cch-axcess-tax", date: "2025-12-08", access: full, locator: "CCH Axcess Advisor bullets; read through the r.jina.ai mirror (direct curl 403)" }
    - { ref: FILED-HOME-2026, title: "AI Tax Preparation & Review Software | Filed", publisher: "Filed", type: vendor, url: "https://www.filed.com", date: "2026-10-21", access: full, locator: "page undated, date is access date; 'Tax Planner' and sample report" }
    - { ref: WCG-NOTREADY-2026, title: "AI Tax Prep in 2026: Not Quite There Yet", publisher: "WCG CPAs & Advisors", type: firm, url: "https://wcginc.com/blog/ai-tax-prep-in-2026-not-quite-there-yet/", date: "2026-07-24", access: full, locator: "'Key Takeaways' paragraph on what AI does well today" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: "IRS Office of Professional Responsibility", type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: "2026-06-24", access: full, locator: "item 5, section 10.37" }
  last_reviewed: "2026-10-21"
  notes: >-
    Maturity is piloting, not in-production, because the survey's 2% and 5% figures count planning-review tools, which are not
    all AI. CCH Axcess Advisor's general-availability date (13 May 2026) appeared only in a search summary and is not used.
    Related: tax-research-advisory-23 (law-change monitoring) and -09 (blueprints).

- id: tax-research-advisory-new-03
  title: Owner-exit and deal-structure research with authority-based tools, then a client-ready memo (small digital firm)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: >-
    Owners of real estate, professional and entrepreneurial businesses bring layered transactions across several entities and
    states, and the firm has to research structure and state tax before advising [JOFA-SMALLFIRMS-2026].
  solution: >-
    One Stop CPA, a digital firm with four accountants and three non-accountants, uses Blue J for authority-based tax research
    and enterprise ChatGPT to organise findings, structure follow-up questions, summarise and draft client-facing explanations;
    the CEO says the technical analysis comes before the draft [JOFA-SMALLFIRMS-2026]. In the example, a client considering a
    sale and moving to another state received an answer on state tax treatment and payout strategy within two hours
    [JOFA-SMALLFIRMS-2026].
  outcomes:
    - lever: speed
      description: >-
        The firm's CEO says an answer on the deal's tax treatment and the residency move took under two hours, much less than
        before. No baseline hours are given.
      figure: within two hours
      measures: time for one client's deal and relocation question, as stated by the firm's CEO to the Journal of Accountancy; no sample, baseline or method
      provenance: self-reported
      source_ref: JOFA-SMALLFIRMS-2026
  prerequisites:
    - Enterprise tiers only, so client data does not train the model (per the firm)
    - A saved library of prompts and templates for repeatable workflows
  risks_and_guardrails:
    - The article says the firms keep client information out of public AI platforms and have a human review the work [JOFA-SMALLFIRMS-2026]
    - One firm, one example; no error rate
  human_checkpoints:
    - CPA analyses the strategy before the AI organises it, and customises the output before it goes to the client
  role_evolution: >-
    The firm closes engagements with the deliverable and offers implementation or compliance add-ons at the same time
    [JOFA-SMALLFIRMS-2026].
  evidence_grade: B
  sources:
    - { ref: JOFA-SMALLFIRMS-2026, title: "Real-life ways small firms use AI", publisher: "Journal of Accountancy (AICPA)", type: press, url: "https://www.journalofaccountancy.com/news/2026/aug/real-life-ways-small-firms-use-ai.html", date: "2026-08-01", access: full, locator: "section 'Performing complex tax planning and research' (One Stop CPA)" }
  last_reviewed: "2026-10-21"
  notes: >-
    Small firm, not mid-market; kept because it is the only named firm account of deal and structure research for owner
    clients. Related: tax-research-advisory-21 and -22 are buy-side diligence.

- id: tax-research-advisory-new-04
  title: Estate documents read into a deterministic planning engine for advisors (Wealth.com Ester)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [document-production, data-reporting]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Estate planning for owner families has to combine assets, entities, family structures and tax considerations, which means
    reading long trust and will documents and recalculating distributions by hand [WEALTHCOM-2026].
  solution: >-
    Wealth.com's Ester Intelligence is described as an engine built for estate and tax planning that produces deterministic,
    auditable outputs and can be embedded in the platform or in a firm's own AI infrastructure; the company added tax planning in
    2026 [WEALTHCOM-2026].
  outcomes:
    - lever: capacity
      description: >-
        The company says the engine processed over 100,000 estate documents in 2025 and executed more than 1,000 deterministic
        calculations per estate distribution.
      figure: "100,000+ documents in 2025; 1,000+ calculations per estate distribution"
      measures: vendor counts of estate documents processed during 2025 and deterministic calculations executed for each estate distribution
      provenance: vendor-published
      source_ref: WEALTHCOM-2026
  prerequisites:
    - Trust and estate documents in digital form
    - An advisor platform contract (the company's customers are wealth-management firms)
  risks_and_guardrails:
    - >-
      ACTEC Fellows say too many attorneys use AI results, especially in research, without confirming them, and that human
      oversight and verification remain essential [ACTEC-AIVIDEO-2026]
    - The sources are a funding article and a vendor statement; no named customer or error rate
  human_checkpoints:
    - Advisor or attorney checks extracted terms against the instrument before illustrating outcomes
  role_evolution: Not described in the sources.
  evidence_grade: C
  sources:
    - { ref: WEALTHCOM-2026, title: "Wealth.com raises $65m Series B for AI wealth planning", publisher: "Fintech Global", type: press, url: "https://fintech.global/2026/04/16/wealth-com-raises-65m-series-b-for-ai-wealth-planning/", date: "2026-04-16", access: full, locator: "paragraphs 3-5" }
    - { ref: ACTEC-AIVIDEO-2026, title: "How Artificial Intelligence Affects Estate Planning in 2026", publisher: "ACTEC Foundation", type: professional-body, url: "https://actecfoundation.org/videos/how-artificial-intelligence-affects-estate-planning-in-2026/", date: "2026-02-05", access: full, locator: "transcript: 'Key AI Developments Since Our Last Update'" }
  last_reviewed: "2026-10-21"
  notes: >-
    Advisor-side wealth management, not a CPA-firm deployment; it shows what reaches firms through advisor partnerships. The
    AICPA survey reports only 2% of tax preparers using Holistiplan, a related planning tool (see research-advisory-new-02).

- id: tax-research-advisory-new-05
  title: Informed consent and verification rules for AI in estate planning (idea)
  archetype: tax
  module: research-advisory
  function: service-delivery
  work_types: [review-assurance, client-interaction]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Estate-planning professionals are adopting AI for research, drafting and summaries, and ACTEC Fellows say hundreds of
    attorneys and judges have been caught citing fabricated authority [ACTEC-AIVIDEO-2026].
  solution: >-
    Idea: tell clients the firm uses AI and how, obtain separate informed consent, verify every output against source, and
    build competence before adopting the tool. ACTEC Fellow Gerry Beyer says the American Bar Association and many local bars
    require telling clients and getting informed consent, and recommends a separately signed provision [ACTEC-AIVIDEO-2026]. A
    practitioner newsletter argues that competence must precede adoption, so a professional can do the task without the tool
    [SOE-COMPETENCE-2025]. The same author later wrote that AI will be best used to amplify bespoke services, not to replace them
    [SOE-STRATEGIC-2025].
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: not applicable
      provenance: self-reported
      source_ref: ACTEC-AIVIDEO-2026
  prerequisites:
    - Engagement terms with a separate AI-use consent clause
    - A section 7216 position for return information (see CPAPA-7216-2026)
  risks_and_guardrails:
    - The IRS has not said whether sending return information to an AI tool is a disclosure needing consent [CPAPA-7216-2026]
    - >-
      Consent cannot be a condition of service without making it involuntary under the regulations, so the firm needs a
      non-AI path for clients who decline [CPAPA-7216-2026]
  human_checkpoints:
    - Attorney or adviser verifies every AI output; consent is obtained before AI touches client data
  role_evolution: >-
    The newsletter author argues the firm of the future is distinguished by bespoke tools and by work outside the documents
    [SOE-STRATEGIC-2025].
  evidence_grade: D
  sources:
    - { ref: ACTEC-AIVIDEO-2026, title: "How Artificial Intelligence Affects Estate Planning in 2026", publisher: "ACTEC Foundation", type: professional-body, url: "https://actecfoundation.org/videos/how-artificial-intelligence-affects-estate-planning-in-2026/", date: "2026-02-05", access: full, locator: "transcript: 'Why AI Results Must Always Be Verified'; 'Client Consent and Attorney Obligations When Using AI'" }
    - { ref: SOE-COMPETENCE-2025, title: "AI in Estate Planning: Duties of Competence?", publisher: "State of Estates (Griffin Bridgers)", type: community, url: "https://griffinbridgers.substack.com/p/ai-in-estate-planning-duties-of-competence", date: "2025-01-21", access: full, locator: "free preview section (paid article); older than 12 months" }
    - { ref: SOE-STRATEGIC-2025, title: "AI in Estate Planning: Strategic Planning", publisher: "State of Estates (Griffin Bridgers)", type: community, url: "https://griffinbridgers.substack.com/p/ai-in-estate-planning-strategic-planning", date: "2025-11-13", access: full, locator: "'Opinion and Context'" }
    - { ref: CPAPA-7216-2026, title: "What to Settle Before Client Tax Data Touches AI", publisher: "CPA Practice Advisor", type: press, url: "https://www.cpapracticeadvisor.com/?p=191491", date: "2026-10-12", access: full, locator: "section 'The consent question has no clean answer yet'" }
  last_reviewed: "2026-10-21"
  notes: >-
    Idea: a control practitioners recommend, not a deployment. The ABA position is stated by the ACTEC Fellow; the ABA source
    itself was not reachable (403).
```

## 3. Module notes

### Processes and key steps (with work types)

| Process | Key steps | Work types |
|---|---|---|
| S corporation return (1120-S) for an owner-managed company | Trial balance to workpapers; book-to-tax (M-1, M-2, AAA); officer wages versus distributions; shareholder basis and Form 7203; K-1 per shareholder; review; e-file | transaction-processing, data-reporting, review-assurance |
| Partnership return (1065) | Trial balance; allocations and capital accounts (section 704(b)); debt and basis; K-1 and footnotes; review; e-file | transaction-processing, expert-judgment |
| K-1 flow to owners | K-1 issued by entity; received by owner; keyed or extracted into the 1040; basis and loss limitation at owner level | transaction-processing, data-reporting |
| Reasonable compensation | Duty interview; wage data; documented method and dated record; payroll set-up | research-synthesis, document-production |
| Owner estimates | Project entity income to owners; safe-harbor test; quarterly payments | data-reporting |
| Entity choice and owner planning | S-election break-even; PTET election; owner compensation and retirement design; exit and structure research; written advice | expert-judgment, research-synthesis |
| Trusts, estates, gifts | Fiduciary accounting and 1041; 706 and 709 preparation; estate plan documents | document-production, expert-judgment |

### Common pain points

- Weeks of review time on K-1-heavy owner returns; manual entry of one K-1 takes 10-15 minutes, per Wolters Kluwer (a vendor statement) [WK-SCANGA-2026].
- K-1 and consolidated-1099 coverage is the first screen for a tool; WCG, a regional firm preparing about 4,500 1040s, says Thomson Reuters' Ready to Review did not handle K-1s and listed them on a November 2026 roadmap [WCG-NOTREADY-2026]. Thomson Reuters' own blog (2025-12-19) says the tool covers 1040s and "will soon be expanding to business returns" [TR-R2RBLOG-2025].
- Basis and capital-account schedules are reviewer skills learned by checklist [NYSSCPA-1120S1065-2025].
- Defensible reasonable-compensation figures need method and record; custom studies have been costly [NATP-RCOMP-2026].
- Tax data wrangling takes 40% to 70% of tax professionals' time, per a Big Four panel at the Black Ore summit (sponsored recap) [OLIVER-BOSUMMIT-2026].
- Advisory work is underpriced: margins of 20-24% against 28% for individual preparation [TR-SOTP-2026].

### Metrics and benchmarks (with sources)

| Measure | Figure | What it counts | Provenance | Source |
|---|---|---|---|---|
| AI as top investment priority | 57% (47% in 2025, 35% two years earlier) | share of 600 respondents (56% midsize with 4-29 professionals, 23% small with 1-3, 21% large with 30+) | independent survey | [TR-SOTP-2026] |
| Proactive or optimized tech stage | 63% large firms (30+ professionals); 35% smaller firms | share of respondents in each size group | independent survey | [TR-SOTP-2026] |
| Firms using AI in tax research | 65%; 32% for client communication; 16% no plans (24.3% a year earlier) | share of 1,808 AICPA members who prepared 2025 returns for a fee | independent survey | [AICPA-TAXSW-2026] |
| No planning-review tool | 93%; Holistiplan 2% | same survey | independent survey | [AICPA-TAXSW-2026] |
| Expanding services | 20% expanding; 75% of those tax advisory; 42% estate, trust and gift planning | same survey | independent survey | [AICPA-TAXSW-2026] |
| K-1 extraction time | 10-15 minutes per K-1 manual; up to 60-80% reduction; 30-70% efficiency for early users | vendor statements | vendor-published | [WK-SCANGA-2026] |
| Black Ore early-access results | over 99% accuracy across tens of thousands of returns; over 98% autonomy rate; up to 98% time savings | company statement; method not stated | vendor-published | [BLACKORE-2026] |
| Instead complex return prep | 4-6 hours to under 60 minutes | company statement | vendor-published | [INSTEAD-EFILE-2026] |
| TIGTA soft-letter campaign | 483 partnerships written to; 163 no response, 182 responses rejected, 138 accepted | IRS Letter 6585 campaign on balance-sheet discrepancies | independent | [JOFA-TIGTA-2026] |
| TIGTA large-partnership exams | 82 partnerships selected; 36 closed, 92% of closed no-change | preliminary; 43 still open | independent | [JOFA-TIGTA-2026] |
| Tax Agent Bench top accuracy | 49.19% on 19 Oct 2026 | share of 193 research-grade US corporate tax questions answered fully correct, adjusted for citation quality; partnership tax is part of the remainder | independent (adjacent: corporate research, not entity returns; caps at B) | [VALS-TAXAGENT-2026] |
| TaxCalcBench | models "succeed in calculating less than a third" of federal returns on a simplified sample | 1040 calculation, not entity returns | vendor-authored benchmark (adjacent) | [COLUMN-TAXCALCBENCH-2025] |

Quality evidence is absent for this module. No source reports an error, override or parallel-run rate for AI work on S corporation, partnership, basis, reasonable-compensation, entity-choice or fiduciary work. The Vals and Column benchmarks test models on corporate research and 1040 calculation.

### Guardrails and regulatory points

- **OPR Alert 2026-19 (2026-06-24):** applies Circular 230 section 10.22 (due diligence: verify facts, citations, calculations), 10.27 (fees: do not bill for manual time not spent), 10.35 (competence), 10.36 (firm procedures, training, vetting of outside AI tools) and 10.37 (written advice) [IRS-OPR-2026].
- **Section 7216:** the IRS has not said whether sending return data to an AI tool is a disclosure needing consent; a cautious approach is a separate signed consent and a non-AI path for clients who decline [CPAPA-7216-2026]. Whether the 1040 consent format (Rev. Proc. 2013-14) applies to business-entity returns was not checked.
- **Reasonable compensation:** the IRS fact sheet says there are no specific guidelines in the Code or regulations and lists court factors [IRS-FS200825-2008]. Section 6662 and 6694 exposure is as stated by NATP [NATP-RCOMP-2026].
- **Basis:** Form 7203 is the IRS form for shareholder stock and debt basis limitations [IRS-F7203-2026].
- **Estate practice:** ACTEC Fellows describe informed consent to AI use as required by the ABA and many local bars [ACTEC-AIVIDEO-2026] (stated by the speaker; ABA text not read).
- **Counterparty:** TIGTA says the IRS's large-partnership programme is "attempting to enhance" compliance by using AI and tax experts, still in its initial stages, and that closed exams so far are 92% no-change [JOFA-TIGTA-2026].

### Frontier signals (dated, sourced)

- **2026-02-24:** Basis said it recently demonstrated what it calls the first AI agent to autonomously complete an end-to-end 1065; the press release names no firm or accuracy figure. A "Top 25 firm" setting appears only in a secondary blog [BASIS-B-2026].
- **2026-03-03:** The Accounting Podcast (episode 477) and a blog post by its host discuss whether AI can prepare a partnership return; the host guesses the IRS will not accept "AI prepared it" as a defense [ACCTGPOD-477-2026; OLIVER-PARTNERSHIP-2026].
- **2026-05-08:** Instead announces e-file approvals for 1040, 1041, 1120, 1120-S and 1065 (company statement) [INSTEAD-EFILE-2026].
- **2026-06-04 and 2026-06-17:** Black Ore summit recaps: hosts discuss predictions that fully autonomous individual preparation may arrive by 2027, with autonomous entity preparation shortly after [ATL-BOSUMMIT-2026]; a speaker predicts accountants will no longer prepare tax returns by 2030 [OLIVER-BOSUMMIT-2026] (sponsored).
- **2026-06-29:** Wolters Kluwer makes AI document intelligence in CCH Axcess Scan generally available for K-1s and supporting statements, built with Microsoft Azure Content Understanding [WK-SCANGA-2026].
- **2026-07-29:** a state-society webcast by two co-founders of an AI tax-preparation vendor (Byron) lists agentic preparation, the CPA talent shortage and the growing volume of K-1s as its themes, showing vendor-led CPE as a main channel for entity-return AI [NYSSCPA-AIPREP-2026].
- **2026-08-05:** Basis announces an End-to-End Tax Platform that takes the first pass from intake to review [BASIS-E2E-2026].
- **Roadmap items (not delivered):** Thomson Reuters Ready to Review K-1 support listed for November 2026 by WCG [WCG-NOTREADY-2026]; Instead 706 and 709 "Coming 2026" [INSTEAD-ENTITY-2026].
- **2026-03-25:** TIGTA report on partnership compliance programmes [JOFA-TIGTA-2026].

### Workforce and role effects

- Roles shift from preparing to reviewing: Filed customers [FILED-HOME-2026]; Aardvark's manager role [AARDVARK-STM-2026].
- Review cost can offset savings if reviewers re-check everything (Elevate CPA's Sean McLean, reported in a sponsored recap) [OLIVER-BOSUMMIT-2026].
- Among firms that reallocated tasks, 39% did so to free professionals for advisory work; 33% for busy-season capacity [TR-SOTP-2026].
- An EisnerAmper executive's four-tier leverage model (no AI 1x; tools only 1.2-1.5x; AI-first 5-10x; AI-native 20-50x; 7% of firms AI-first, 1% AI-native) is a speaker's estimate [OLIVER-BOSUMMIT-2026].

### Objections and concerns practitioners raise

- "Trust, not technology": preparers re-check AI output, so costs double (Elevate CPA) [OLIVER-BOSUMMIT-2026].
- Liability: the signer carries the penalty regardless of the tool [OLIVER-PARTNERSHIP-2026; NATP-RCOMP-2026].
- Last-mile and data lock-in with proprietary systems; vendors that cannot read K-1s [WCG-NOTREADY-2026].
- Chatbot numbers for salary and entity choice look authoritative but lack method [NATP-RCOMP-2026].
- Competence before adoption; fatigue with AI marketing (estate practitioners) [SOE-COMPETENCE-2025; SOE-STRATEGIC-2025].
- Partners, not staff, are the biggest obstacle to adoption (Big Four panel, sponsored recap) [OLIVER-BOSUMMIT-2026].

### Trusts, estates and gifts: what reaches mid-market firms (short section)

- **Planning side:** advisor platforms such as Wealth.com (estate and tax planning agents; raised $65 million in April 2026) serve wealth-management firms, and the AICPA survey shows CPA interest: 42% of the 20% of respondents expanding services chose estate, trust and gift planning [WEALTHCOM-2026; AICPA-TAXSW-2026].
- **Return side:** Instead lists 1041 as live and 706 and 709 as coming for TY26 (vendor) [INSTEAD-ENTITY-2026]; Thomson Reuters' fiduciary pages describe conventional software without an AI function I could read [TR-FIDUCIARY-2026].
- **Professional guidance:** ACTEC Foundation 2026 video on verification, security and informed consent [ACTEC-AIVIDEO-2026]; practitioner commentary on competence [SOE-COMPETENCE-2025].
- **Evidence:** no firm-level case, error rate or independent test. Treat this area as risk awareness, not proof points.

### Interview probes for an advisor

1. "Which owner clients have an S corporation salary backed by a dated, duty-based study, who produced it, and has any owner brought you a chatbot's number?" (reasonable compensation; new-01)
2. "Where do you track each shareholder's and partner's basis, who reconciles it to the K-1 each year, and what would you let a tool compute without a reviewer?" (basis; new-02)
3. "For a client with a 1040, an S corporation and a partnership, where does one person see all three, and how do you tie each K-1 received to the issuing return?" (multi-entity; new-03)
4. "When an AI-prepared entity return reaches your reviewer, what do they re-check, how long does that take, and what do you track: overrides, errors found, review hours?" (review cost; new-05)
5. "Who builds the S-election or PTET break-even for an owner, what written-advice standard do you apply, and are owners bringing their own calculators?" (entity choice; research-advisory new-01)

## 4. Routed to other modules

- **controversy:** the IRS's use of AI to select large partnerships for review, the soft-letter campaign and 92% no-change rate [JOFA-TIGTA-2026; LW-IRSAI-2024]. The Latham article (May-June 2024) describes the IRS announcing AI to identify partnership compliance issues and a new partnership examination group. Instead's S-election and late-filing resolution workflow [INSTEAD-SCORP-2026] (vendor).
- **multistate-private:** state PTET election mechanics and modelling (Gelt PTET calculator, Filed's Maryland sample) [GELT-CALC-2025; FILED-HOME-2026].
- **compliance-individual-business (existing entries):**
  - `#02` (K-1 extraction): CCH Axcess Scan general availability on 2026-06-29, with Wolters Kluwer's figures of 10-15 minutes per manual K-1 and an up to 60-80% reduction [WK-SCANGA-2026].
  - `#05` (end-to-end preparation): Maxwell Locke & Ritter's partner says a high-net-worth return with dozens of K-1s took several days and is now ready for review in minutes (a qualitative customer quote on the vendor release) [BLACKORE-2026].
  - `#06` (1065, 1120-S, 1041 agents): Basis's 1065 demonstration claim and the unverified "Top 25 firm" detail [BASIS-B-2026]; Accrual's launch article says the company is currently focused on individual returns, including complex K-1s [ACCRUAL-2026].
  - `#18` (phased adoption): the "preparers re-checked everything" account [OLIVER-BOSUMMIT-2026].
  - `#19` and `#21` (policy, consent): CPA Practice Advisor's 7216 advice [CPAPA-7216-2026].
  - `#24` (roll-ups): Aardvark's acquisition-led growth statement [AARDVARK-STM-2026].
- **research-advisory (existing entries):** `#09` Accordance blueprint (the firm-side S-election project) pairs with new-01; `#13` document analysis (TR CoCounsel Tax uploads for passive, at-risk basis and QBI errors [TR-COCOUNSELCORP-2026]); `#25` pricing (TR survey: 78% hourly, advisory margins 20-24% [TR-SOTP-2026]).
- **Future accounting and client advisory archetype (no module today):** Wiss's partnership with Basis began in the client accounting practice (September 2024, per a search summary; not opened).
- **data-technology:** tax engines versus AI-native replacement (new-06); data foundation as the first fix named by a Big Four panel [OLIVER-BOSUMMIT-2026].

## 5. Sources

Forty-six distinct documents were opened and read (`access: full`). By type: vendor 16, press 12, regulator 3, conference 3, firm 2, survey 2, academic 2, podcast 2, community 2, professional-body 1, job-posting 1.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| BASIS-B-2026 | Basis Raises $100 Million to Deploy AI Agents for Accounting Firms | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/24/basis-raises-100-million-to-deploy-ai-agents-for-accounting-firms/178759/ | 2026-02-24 | full |
| BASIS-E2E-2026 | The future of tax is end-to-end intelligence | Basis | vendor | https://www.getbasis.ai/blogs/the-future-of-tax-is-end-to-end-intelligence | 2026-08-05 | full |
| BLACKORE-2026 | Black Ore Launches Tax Autopilot for Broad Availability | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/04/29/black-ore-launches-tax-autopilot-for-broad-availability/182311/ | 2026-04-29 | full |
| ACCRUAL-2026 | Startup Accrual officially launches with $75M in funding | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/02/05/startup-accrual-officially-launches-with-75m-in-funding-to-bring-ai-native-automation-to-accounting/177600/ | 2026-02-05 | full |
| WK-SCANGA-2026 | Expanded CCH Axcess Expert AI to Deliver AI-Powered Scan and K-1 Automation | CPA Practice Advisor (Wolters Kluwer release) | press | https://www.cpapracticeadvisor.com/?p=185870 | 2026-06-29 | full |
| WK-WHATSNEW-2025 | What's new with CCH Axcess Tax | Wolters Kluwer | vendor | https://wolterskluwer.com/en/expert-insights/whats-new-with-cch-axcess-tax | 2025-12-08 | full (mirror) |
| TR-R2RBLOG-2025 | AI tax return preparation: how Ready to Review transforms the workflow | Thomson Reuters | vendor | https://tax.thomsonreuters.com/blog/ai-tax-return-preparation-how-ready-to-review-transforms-the-workflow/ | 2025-12-19 | full |
| WCG-NOTREADY-2026 | AI Tax Prep in 2026: Not Quite There Yet | WCG CPAs & Advisors | firm | https://wcginc.com/blog/ai-tax-prep-in-2026-not-quite-there-yet/ | 2026-07-24 | full |
| TR-COCOUNSELTAX-2026 | CoCounsel Tax (firm product page) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/products/cocounsel-tax | 2026-10-21 (access date) | full |
| TR-COCOUNSELCORP-2026 | CoCounsel Tax: The AI tax assistant for in-house teams | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/products/cocounsel-tax/corp | 2026-10-21 (access date) | full |
| TR-FIDUCIARY-2026 | Fiduciary tax solutions (ONESOURCE) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/corporation-solutions/fiduciary-tax-solutions | 2026-10-21 (access date) | full |
| INSTEAD-SCORP-2026 | Instead for S Corporations (1120-S): AI Tax Agent | Instead | vendor | https://webflow.instead.com/products/s-corporation | 2026-10-21 (access date) | full |
| INSTEAD-CPA-2026 | CPA Firms | Instead | vendor | https://instead.com/solutions/cpa-firms | 2026-10-21 (access date) | full |
| INSTEAD-ENTITY-2026 | Instead Entity Agent | Instead | vendor | https://instead.com/products/entity-agent | 2026-10-21 (access date) | full |
| INSTEAD-EFILE-2026 | Instead becomes the first new tax platform in decades to pass 100% government testing across all U.S. jurisdictions | Instead | vendor | https://instead.com/news/instead-first-new-tax-platform-100-percent-us-efile-approvals-all-jurisdictions | 2026-05-08 | full |
| FILED-HOME-2026 | AI Tax Preparation & Review Software | Filed | vendor | https://www.filed.com | 2026-10-21 (access date) | full |
| INTUIT-BASIS-2024 | S corporation basis tracking in Intuit Tax Advisor | Intuit | vendor | https://accountants.intuit.com/taxprocenter/practice-management/s-corporation-basis-tracking-in-intuit-tax-advisor | 2024-07-03 | full |
| INTUIT-ASSIST-2024 | New! Intuit Assist for Intuit Tax Advisor | Intuit | vendor | https://accountants.intuit.com/taxprocenter/advisory-services/intuit-assist-for-intuit-tax-advisor/ | 2024-06-19 | full |
| GELT-CALC-2025 | Gelt Launches Tax Calculator Hub to Help Business Owners Quantify Advanced Tax Strategies | Gelt | vendor | https://www.joingelt.com/blog/ai-tax-calculators-business-owners | 2025-12-29 | full |
| NATP-RCOMP-2026 | Four reasonable compensation mistakes S-corp clients make | NATP (sponsored; WageProof founder) | vendor | https://www.natptax.com/news-insights/blog/four-reasonable-compensation-mistakes-s-corp-clients-make/ | 2026-09-16 | full (mirror) |
| WAGEPROOF-2026 | Reasonable Compensation Software for CPAs & EAs | WageProof | vendor | https://www.wageproof.com/for-cpas | 2026-10-21 (access date) | full |
| RCREPORTS-IA-2023 | Insightful Accountant & Tax Practice News First Look on RCReports | Insightful Accountant | press | https://insightfulaccountant.com/accounting-tech/vendor-news/insightful-accountant-tax-practice-news-first-look-on-rcre | 2023-02-24 | full |
| EVERGREEN-CHATGPT-2024 | Using ChatGPT to Determine S Corporation Reasonable Compensation | Evergreen Small Business | press | https://evergreensmallbusiness.com/using-chatgpt-to-determine-s-corporation-reasonable-compensation/ | 2024-09-09 | full |
| IRS-FS200825-2008 | Wage Compensation for S Corporation Officers (FS-2008-25) | Internal Revenue Service | regulator | https://www.irs.gov/pub/irs-news/fs-08-25.pdf | 2008-08 | full |
| IRS-F7203-2026 | About Form 7203, S Corporation Shareholder Stock and Debt Basis Limitations | Internal Revenue Service | regulator | https://www.irs.gov/forms-pubs/about-form-7203 | 2026-06-27 (last reviewed) | full |
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| CPAPA-7216-2026 | What to Settle Before Client Tax Data Touches AI | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/?p=191491 | 2026-10-12 | full |
| JOFA-TIGTA-2026 | IRS watchdog cites resource limits, duplication in partnership audits | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/mar/irs-watchdog-cites-resource-limits-duplication-in-partnership-audits.html | 2026-03-25 | full |
| LW-IRSAI-2024 | New IRS Unit Leverages AI to Step Up Partnership Audits; Hundreds of New Inquiries Expected | Latham & Watkins, in Robotics, Artificial Intelligence & Law | firm | https://www.lw.com/people/admin/upload/SiteAttachments/New-IRS-Unit-Leverages-AI.pdf | 2024-05 | full |
| TR-SOTP-2026 | 2026 State of Tax Professionals Report | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en-us/posts/wp-content/uploads/sites/20/2026/06/2026-State-of-Tax-Professionals-Report.pdf | 2026-06 | full |
| AICPA-TAXSW-2026 | 2026 tax software survey | The Tax Adviser (AICPA) | survey | https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/ | 2026-08-31 | full |
| VALS-TAXAGENT-2026 | Tax Agent Bench | Vals AI | academic | https://vals.ai/benchmarks/tax_agent_bench | 2026-10-19 (updated) | full |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126) | arXiv (Bock, Molisee, Ozer, Shah; Column Tax) | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full |
| OLIVER-PARTNERSHIP-2026 | When AI Can Prepare a Partnership Return, What Happens to the Business Model? | Blake Oliver | press | https://www.blakeoliver.com/blog/when-ai-can-prepare-a-partnership-return | 2026-03-03 | full |
| ACCTGPOD-477-2026 | The AI Agent That Can Do A Partnership Tax Return (episode 477, show notes) | The Accounting Podcast (via CastFox) | podcast | https://www.castfox.net/podcast/the-accounting-podcast-930492/episode/the-ai-agent-that-can-do-a-partnership-tax-return-140333 | 2026-03-03 | full (show notes only) |
| OLIVER-BOSUMMIT-2026 | 40 Hours of Work Done in 5 Minutes: My Takeaways from Black Ore's AI Tax Summit | Blake Oliver (sponsored by Black Ore) | press | https://www.blakeoliver.com/blog/black-ore-ai-tax-summit | 2026-06-04 | full |
| ATL-BOSUMMIT-2026 | 2026 Black Ore AI Tax Summit - Accounting Technology Lab Podcast - June 2026 | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/2026-black-ore-ai-tax-summit-accounting-technology-lab-podcast-june-2026/ | 2026-06-17 | full (show notes only) |
| NATP-TAXPOSIUMAG-2026 | Taxposium 2026 agenda (13-15 July 2026, Cleveland) | National Association of Tax Professionals | conference | https://taxposium.natptax.com/agenda | 2026-07 | full (titles only) |
| NYSSCPA-AIPREP-2026 | AI in Tax Preparation: A Practical Guide (webcast) | NYSSCPA | conference | https://nysscpa.org/catalog/events/7297321-ai-in-tax-preparation-a-practical-guide-2026-29-07 | 2026-07-29 | full |
| NYSSCPA-1120S1065-2025 | Forms 1120-S and 1065 Return Review Boot Camp for New and Experienced Reviewers (webcast) | NYSSCPA | conference | https://nysscpa.org/catalog/events/1016910-forms-1120-s-and-1065-return-review-boot-camp-for-new-and-experienced-reviewers-webcast-2025-18-11 | 2025-11-18 | full |
| JOFA-SMALLFIRMS-2026 | Real-life ways small firms use AI | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/aug/real-life-ways-small-firms-use-ai.html | 2026-08-01 | full |
| ACTEC-AIVIDEO-2026 | How Artificial Intelligence Affects Estate Planning in 2026 | ACTEC Foundation | professional-body | https://actecfoundation.org/videos/how-artificial-intelligence-affects-estate-planning-in-2026/ | 2026-02-05 | full |
| SOE-COMPETENCE-2025 | AI in Estate Planning: Duties of Competence? | State of Estates (Griffin Bridgers) | community | https://griffinbridgers.substack.com/p/ai-in-estate-planning-duties-of-competence | 2025-01-21 | full (free preview of a paid article) |
| SOE-STRATEGIC-2025 | AI in Estate Planning: Strategic Planning | State of Estates (Griffin Bridgers) | community | https://griffinbridgers.substack.com/p/ai-in-estate-planning-strategic-planning | 2025-11-13 | full |
| WEALTHCOM-2026 | Wealth.com raises $65m Series B for AI wealth planning | Fintech Global | press | https://fintech.global/2026/04/16/wealth-com-raises-65m-series-b-for-ai-wealth-planning/ | 2026-04-16 | full |
| AARDVARK-STM-2026 | Senior Tax Manager (Aardvark Tax Advisors, Cynch AI) | Cynch AI (posting copies) | job-posting | https://jobs.auditfriendly.co/jobs/senior-tax-manager-cynch-ai-f487bd54921b | 2026-09 (closed 2026-09-09) | full (mirror) |

## 6. Gaps

- **No quality evidence.** No error rate, override rate, parallel-run result, inspection finding or independent measure for AI on S corporation or partnership returns, basis, reasonable compensation, entity choice or fiduciary returns. The Vals and Column benchmarks test corporate research and 1040 calculation, not entity returns.
- **No named mid-market firm** for reasonable compensation, basis tracking, owner estimates, entity-return review or PTET modelling. Named firms are small digital or AI-native practices (One Stop CPA, Aardvark, Paramount Tax, JCG Tax) or sit in existing entries (Maxwell Locke & Ritter, Armanino, Boulay).
- **Tax Adviser and Journal of Accountancy:** no 2026 article on AI and pass-through practice, entity choice or basis was found; a Tax Adviser S corporation developments item (2026-07-31) was seen only as a listing.
- **Search-only or blocked, not used as evidence:** CCH Axcess Advisor general availability (13 May 2026; Wolters Kluwer's page returned 403); Berkowitz Pollack Brant's note on the IRS pass-through unit (Cloudflare block); Datagrid and Digiqt trust-tax agent blogs; TaxGPT's business-returns roadmap; Perplexity's tax product; Wiss and Basis (2024, client accounting, not tax); a search-summary claim of a 20% loss of IRS pass-through program staff (not confirmed against TIGTA); the ABA's 2024 AI ethics opinion (403); an Inman article on AI and "should" questions; Holistiplan and Mili scope (403).
- **Reddit, TaxProTalk and other practitioner forums:** not reached; the community voice here comes from two newsletters and sponsored blogs.
- **Taxposium 2026:** only session titles read; no recap of the reasonable-compensation or "When One Entity Just Won't Do" sessions. No NSA or CCH Connections 2026 content found.
- **Section 7216 for entity returns:** the consent format and its application to 1065 and 1120-S were not checked.
- **IRS Publication 505** safe-harbor figures and the full TIGTA report (report number and date) were not opened; the TIGTA figures come from the Journal of Accountancy article.
- **Date gaps:** the Instead, Filed, WageProof and Thomson Reuters product pages are undated; their date is the access date. The Aardvark posting date was not captured.
- **Vendor concentration:** 16 of the 46 source rows are vendor pages. Two sponsored pieces (NATP post by the WageProof founder; the Black Ore summit recap) are marked as such.
