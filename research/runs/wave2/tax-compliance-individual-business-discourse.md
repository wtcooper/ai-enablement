# Tax, compliance-individual-business: discourse angle

- **Archetype:** tax
- **Module:** compliance-individual-business (individual, trust, partnership and small-business return preparation; 1040, 1041, 1065, 1120-S; UK self assessment and equivalents)
- **Angle:** discourse (what practitioners are saying)
- **Prepared:** 2026-10-17 (wave 2)
- **Method:** Started from `landscape-tax.md` and `vocabulary.md`. Opened pages with `curl` (and the r.jina.ai mirror for two pages that returned only navigation text); read trade press, professional-body publications, podcasts and transcripts, vendor posts, a practitioner newsletter and Hacker News threads. Reddit (r/taxpros) returned a network-policy block and Going Concern a 403. The web-search allowance ran out partway (about 10 searches returned results), so leads after that point were not chased. Every source below was opened unless marked `search-only`; none of the A/B outcomes rest on a search-only source.

## 1. Summary

- **The discourse has moved from "can AI do it" to "who reviews, who is liable, and what do we charge".** At the April 2026 TEI seminar the in-house tax community treated capability as settled and spent its time on silent errors, who owns AI, and how to review rising volumes (TEI-TAXTECH-2026). Small-firm trade press shows the same turn: policy templates, verification logs and vendor due diligence (JOFA-POLICY-2026, BARMORE-OPR-2026).
- **Agentic 1040 and pass-through preparation is the headline product story, but the evidence is vendor-sourced and thin.** Thomson Reuters (Ready to Review, generally available 15 Dec 2025), Black Ore (opened to firms 29 Apr 2026) and Basis (1065 demonstration, Feb 2026) are the named products. The only customer figure is a partner's estimate of about an hour saved per simple 1040. Black Ore's "above 99 percent" accuracy has no stated denominator. No error rate, override rate, parallel run or inspection result for AI-prepared returns was found in anything read.
- **The sharpest live argument is about fees.** OPR Alert 2026-19 (24 Jun 2026) says AI efficiencies should be passed to clients and warns about billing time not spent; the AICPA answered (8 Sep 2026) that this ignores value pricing and the costs of adopting AI, and its chief executive called the language non-authoritative (IRS-OPR-2026, AICPA-FEES-2026).
- **Disclosure and section 7216 consent are unresolved, and practitioner advice conflicts.** OPR cites sections 6713 and 7216 but does not say whether AI use needs consent. A practitioner newsletter lists five questions OPR left open; secondary reports say the AICPA advises disclosure as a precaution; a Journal of Accountancy article suggests engagement-letter wording instead (BARMORE-OPR-2026, LDS-CNBC-2026, JOFA-POLICY-2026).
- **The competitive threat is partly from the client side.** Perplexity's tax agent (2 Apr 2026), UK survey data from Taxfix, a National Association of Enrolled Agents warning, and Hacker News users describing Claude-prepared returns all point to taxpayers bypassing or auditing preparers (PERPLEXITY-2026, TECHRADAR-TAXFIX-2025, NAEA-AI-2026, HN-ASK-2026).
- **Independent measurement is the biggest gap.** The only quasi-independent numbers are TaxCalcBench (strict return-level correctness 0 to 71 percent on 50 TY2025 cases, depending on model and web search; calculation step only; run by a vendor with a deterministic engine) and an adjacent month-end-close benchmark (COLUMN-TCBREPO-2026, ACCTODAY-AIBENCH-2026).

## 2. Use cases

Grade count: A 0, B 3, C 10, D 3 (16 entries). `last_reviewed` is 2026-10-17 throughout.

```yaml
- id: tax-compliance-individual-business-01
  title: Agent prepares the 1040 from source documents to a return ready for professional review
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: >-
    Individual return preparation is document-heavy and falls in a short season. Black Ore frames its launch around
    a shortage of qualified accountants (BLACKORE-2026) and Thomson Reuters around busy-season burnout and staffing
    strain (TR-R2R-2025).
  solution: >-
    An AI agent ingests W-2s, 1099s, K-1s and brokerage statements (and, in one product, prior-year returns),
    classifies them, extracts the data, applies federal and state tax logic, builds workpapers and passes the
    return to the firm's existing tax software for human review and sign-off. Thomson Reuters Ready to Review
    (generally available in the US from 15 Dec 2025 per the vendor) and Black Ore Tax Autopilot (opened to firms on
    29 Apr 2026 after a two-year invitation-only pilot) are the two named products in the sources.
  outcomes:
    - lever: speed
      description: >-
        A named early-adopter partner (CLH CPAs and Consultants, Indiana) said Ready to Review reduced preparation
        time by about an hour on each simple 1040. It is an estimate quoted in the vendor's release, not a
        measured study.
      figure: about 1 hour saved per simple 1040
      measures: >-
        Partner's words: 'reducing return preparation time by approximately an hour on each simple 1040'. Baseline,
        sample size and method not stated.
      provenance: vendor-published
      source_ref: TR-COCOUNSEL-2025
    - lever: speed
      description: >-
        Black Ore says Tax Autopilot achieved time savings of up to 98 percent on complex filings during the
        pilot (company statement reported by a trade magazine).
      figure: up to 98 percent time savings
      measures: >-
        Company statement as reported: 'time savings of up to 98 percent on complex filings'. Time measured and
        baseline are not defined in the article.
      provenance: vendor-published
      source_ref: BLACKORE-2026
    - lever: quality
      description: >-
        Black Ore says accuracy was above 99 percent across tens of thousands of returns in the pilot. The article
        does not define accuracy (line-level, return-level, or after review).
      figure: accuracy above 99 percent
      measures: >-
        Company statement as reported: 'accuracy above 99 percent across tens of thousands of returns during the
        pilot'. The numerator and denominator are not defined.
      provenance: vendor-published
      source_ref: BLACKORE-2026
  prerequisites:
    - Source documents available digitally, collected through a portal or organizer (CPAPA-POSTEXT-2026, CPAPA-BLACKORE-2024).
    - An integration path into the firm's existing tax software, which both named products use for the review step (BLACKORE-2026, TR-COCOUNSEL-2025).
    - Vendor security assurance; Black Ore cites SOC 2 Type II (BLACKORE-2026). OPR expects third-party AI tools to be vetted (IRS-OPR-2026).
    - Start with simpler returns; one practitioner advised against putting the most complex or many-state returns in first (CPAPA-BLACKORE-2024).
  risks_and_guardrails:
    - >-
      Werfel's preparer risk register lists incorrect document extraction that flows silently into the return, and
      control dilution when AI-driven volume makes review less rigorous in practice (AICPA-WERFEL-2026).
    - >-
      The signing preparer remains responsible. OPR Alert 2026-19 ties AI output to Circular 230 section 10.22
      (due diligence) and section 10.35 (competence) (IRS-OPR-2026).
    - >-
      Model-only calculation is unreliable. On the TaxCalcBench TY2025 edition (50 cases), strict return-level
      correctness ran from 0 percent to 71 percent depending on model and web search (COLUMN-TCBREPO-2026). This
      is the calculation step only and is not a test of either named product.
    - >-
      A trade-press piece flags that photos of crumpled paper and consolidated brokerage statements are misread
      and that low-confidence extractions should go to a person (CPAPA-POSTEXT-2026).
  human_checkpoints:
    - Preparer or partner review of every return before sign-off (BLACKORE-2026, TR-COCOUNSEL-2025).
    - Tie-out of workpapers to source documents during review (CPAPA-BLACKORE-2024).
    - Review of low-confidence or extracted items before they enter the return (CPAPA-POSTEXT-2026).
  role_evolution: >-
    Thomson Reuters' president for tax says she expects firms to pair each CPA with at least one virtual agent and
    predicts fewer 80-hour weeks (TR-R2R-2025). Two CPA-technology commentators argue firms should not abandon
    1040 work because it feeds advisory relationships (CPAPA-BLACKORE-2024). The work shifts from keying and
    first-pass preparation to review.
  evidence_grade: B
  sources:
    - { ref: TR-COCOUNSEL-2025, title: "Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows", date: 2025-11-05, access: full, locator: "Transforming Tax Preparation with Agentic AI section; availability notes" }
    - { ref: TR-R2R-2025, title: "Transforming Busy Season: Introducing Ready to Review", publisher: Thomson Reuters (Elizabeth Beastrom), type: vendor, url: "https://www.thomsonreuters.com/en-us/posts/innovation/transforming-busy-season-introducing-ready-to-review-thomson-reuters-agentic-ai-for-1040-preparation/", date: 2025-12-15, access: full, locator: "paragraphs 2-3, 'The Next Step for 1040 Prep'" }
    - { ref: BLACKORE-2026, title: "AI Tax Startup Black Ore Opens Platform to CPA Firms", publisher: Sovereign Magazine, type: press, url: "https://www.sovereignmagazine.com/article/ai-tax-startup-black-ore-opens-platform-to-cpa-firms", date: 2026-04-29, access: full, locator: "paragraphs 2-4, 'How Tax Autopilot Works'" }
    - { ref: CPAPA-BLACKORE-2024, title: "Review of Black Ore Tax Autopilot - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/review-of-black-ore-tax-autopilot-the-accounting-technology-lab-podcast-june-2024/", date: 2024-06, access: full, locator: "transcript, hosts' discussion of partner-reviewable returns and tie-out" }
    - { ref: AICPA-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08, access: full, locator: "Figure 3, tax preparers risk register" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Circular 230 items 1 and 3" }
    - { ref: COLUMN-TCBREPO-2026, title: "TaxCalcBench repository README and TY2025 leaderboard", publisher: Column Tax (GitHub), type: vendor, url: "https://github.com/column-tax/tax-calc-bench", date: 2026-06, access: full, locator: "Leaderboard, Tax Year 2025 table and notes" }
    - { ref: CPAPA-POSTEXT-2026, title: "The Post-Extension Window: How to Sequence Firm Automation Before Busy Season", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/10/16/the-post-extension-window-how-to-sequence-firm-automation-before-busy-season/191855/", date: 2026-10-16, access: full, locator: "section 'Use AI where it reads, not where it decides'" }
  last_reviewed: 2026-10-17
  notes: >-
    Grade B, not A: the only named-customer figure is a partner's estimate quoted by the vendor, and the Black Ore
    figures are company statements without defined denominators. No independent error rate, override rate or
    parallel-run result for either product was found. Black Ore's claim that 40 percent of the 20 largest CPA firms
    were in the pilot, and the waitlist of about 3,700 firms, are company figures reported in BLACKORE-2026; only
    one customer (Maxwell Locke and Ritter) is named in the article.

- id: tax-compliance-individual-business-02
  title: Agent prepares partnership and other entity returns (1065, with 1120-S to follow)
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Entity returns are more varied than 1040s: allocations, K-1s and state filings multiply the review burden,
    and firms report staff shortages in this work as well.
  solution: >-
    Agents that work for hours at a time across client accounting, tax and audit workflows, including a
    demonstration of an agent completing a 1065 without a person. A June 2026 industry summit recap says
    predictions put autonomous individual preparation by 2027, with entity preparation following shortly after.
  outcomes:
    - lever: capacity
      description: none published
      figure: none published
      measures: >-
        BASIS-2026 says only that the company 'recently demonstrated' an agent that autonomously completed a 1065;
        no accuracy, time or review data is given.
      provenance: vendor-published
      source_ref: BASIS-2026
  prerequisites:
    - Structured client data and K-1 inputs; the Black Ore summit recap names data quality as the biggest barrier (BLACKORE-SUMMIT-2026, show notes as summarised in the page text).
  risks_and_guardrails:
    - Control dilution and incorrect document extraction, as for 1040 agents (AICPA-WERFEL-2026).
    - >-
      OPR expects the signing practitioner to verify facts, citations and calculations that AI produces
      (IRS-OPR-2026).
  human_checkpoints:
    - Practitioner review and signature; no named source describes a different arrangement (IRS-OPR-2026).
  role_evolution: >-
    Not described for entity returns in the sources read. The Black Ore summit recap mentions AI-native firms and a
    shift from compliance to advisory as themes (BLACKORE-SUMMIT-2026).
  evidence_grade: C
  sources:
    - { ref: BASIS-2026, title: "Basis Raises $100M to Deploy Automated Accounting Agents", publisher: Built In NYC, type: press, url: "https://www.builtinnyc.com/articles/basis-raises-100m-series-b-20260226", date: 2026-02-26, access: full, locator: "paragraphs 1-2" }
    - { ref: BLACKORE-SUMMIT-2026, title: "2026 Black Ore AI Tax Summit - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/2026-black-ore-ai-tax-summit-accounting-technology-lab-podcast-june-2026/", date: 2026-06, access: full, locator: "episode description (transcript was not available without sign-in)" }
    - { ref: AICPA-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08, access: full, locator: "Figure 3" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Circular 230 item 1" }
  last_reviewed: 2026-10-17
  notes: >-
    The Basis claim that its product is used by 30 percent of the 25 largest US accounting firms is a company
    figure repeated in BLACKORE-2026 (paragraph 'Competition in AI tax preparation'); it is not an outcome of this
    use case. The 2027 prediction is the podcast hosts' summary of industry predictions, not a measured forecast.

- id: tax-compliance-individual-business-03
  title: Agent maps K-1 and other source-document items to tax treatments with a confidence level and learns from overrides
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: >-
    Receiving K-1s and mapping footnote items to the right treatment used to rely on staff guides, OCR extraction
    and group discussion of unfamiliar footnotes.
  solution: >-
    PwC's US AI tax leader describes agents trained on historical data that read a K-1 footnote, say how they
    interpreted it and give a confidence level. A reviewer sees flagged items, and an override must come with a
    reason so the agent can learn from the correction. Agents run on PwC's Agent OS, which manages the tools each
    agent can use.
  outcomes:
    - lever: capacity
      description: >-
        Qualitative only: the interviewee says one person now reviews where three people used to gather to resolve
        an unfamiliar footnote. No time, accuracy or override-rate figure is given.
      figure: none published
      measures: Interviewee's description, 'instead of three people gathering to solve the issue, one person reviews'; not a measurement.
      provenance: self-reported
      source_ref: PWC-MEGNA-2025
  prerequisites:
    - Historical data to train the agents; ongoing feedback from reviewers (PWC-MEGNA-2025).
    - A tool-management layer (Agent OS) and a firm governance committee (PWC-MEGNA-2025).
  risks_and_guardrails:
    - >-
      Incorrect extraction or mapping that passes silently into the return is a named preparer risk
      (AICPA-WERFEL-2026).
    - >-
      PwC says its agents sit in a human-reviewed, multi-reviewer process, and that approved logic is locked so it
      cannot be changed ad hoc (PWC-MEGNA-2025).
  human_checkpoints:
    - Reviewer checks flagged, lower-confidence items and records a reason for any override (PWC-MEGNA-2025).
  role_evolution: >-
    PwC reports 3,200 AI champions and about 80 percent of US staff having taken some AI training, and says
    policy interpretation and high-touch consulting remain mostly human (PWC-MEGNA-2025).
  evidence_grade: B
  sources:
    - { ref: PWC-MEGNA-2025, title: "How PwC's tax team is using agentic AI (interview with Dom Megna)", publisher: CFO.com, type: firm, url: "https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/", date: 2025-06-06, access: full, locator: "answers 1, 2 and 5" }
    - { ref: AICPA-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08, access: full, locator: "Figure 3, 'Incorrect document extraction'" }
  last_reviewed: 2026-10-17
  notes: >-
    The K-1 example is from asset and wealth management work at a Big Four firm, so it is adjacent to the small-firm
    individual and pass-through workflow; this caps the grade at B. The interview is more than 15 months old.

- id: tax-compliance-individual-business-04
  title: Route returns by complexity so simple returns go to AI preparation and complex returns stay with staff
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, coordination-scheduling]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Firms turn away or lose low-fee 1040 work, and use outsourcing to handle volume, but 1040 clients also feed
    advisory work.
  solution: >-
    Practitioners advise using an AI preparation product for easier, data-entry-heavy returns first, keeping
    complex multi-state returns with staff. One product is priced per schedule, so cost tracks complexity.
  outcomes:
    - lever: cost
      description: >-
        One consultant says clients on the platform report more than the 90 percent time savings the company
        claims and more than 5x annual ROI. These are commentator statements about unnamed clients, in a June 2024
        episode.
      figure: more than 90 percent time savings; more than 5x ROI
      measures: >-
        Hosts' statements about their own client calculations and the company's claim ('90% of the time savings',
        'five times annual ROI'); clients, hours and baselines are unnamed.
      provenance: vendor-published
      source_ref: CPAPA-BLACKORE-2024
  prerequisites:
    - A way to classify return complexity at intake (by schedule, state count) (CPAPA-BLACKORE-2024).
  risks_and_guardrails:
    - >-
      The reviewer said AI can break down on, for example, a return with 30 states if it has seen too few training
      instances (CPAPA-BLACKORE-2024).
  human_checkpoints:
    - Partner review of the AI-prepared return (CPAPA-BLACKORE-2024).
  role_evolution: >-
    The hosts argue the main labour effect falls on outsourced and offshore services rather than onshore staff,
    because staff can contact clients directly (CPAPA-BLACKORE-2024).
  evidence_grade: C
  sources:
    - { ref: CPAPA-BLACKORE-2024, title: "Review of Black Ore Tax Autopilot - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/review-of-black-ore-tax-autopilot-the-accounting-technology-lab-podcast-june-2024/", date: 2024-06, access: full, locator: "transcript, second and last speaker turns" }
    - { ref: TR-COCOUNSEL-2025, title: "Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows", date: 2025-11-05, access: full, locator: "CLH quote on 'simple 1040'" }
  last_reviewed: 2026-10-17
  notes: >-
    Older foundation source (June 2024) because it is the clearest practitioner discussion of how a firm would
    split work by complexity. The firm in the hosts' client review is not named. 'Piloting' is used because use is
    described but no organisation is named.

- id: tax-compliance-individual-business-05
  title: Organizer and document-request automation with AI checking what has arrived
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [coordination-scheduling, client-interaction]
  pattern: intake-triage
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Staff send the organizer, then spend weeks sending reminders by hand and checking the portal, and a single
    missing brokerage statement can hold up the whole return.
  solution: >-
    A request list built from last year's uploads; each new file checked against it; scheduled reminders that
    name the specific missing document; a stop rule that hands the job to a person with a short summary after a
    set number of reminders. A model reads each upload to decide whether it is a W-2, a 1099-B or a property tax
    bill and to pull the payer and tax year.
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: >-
        The article recommends measuring median days from organizer sent to documents complete, and days from a
        finished return to a signed authorization and paid invoice, before and after; it reports no results.
      provenance: self-reported
      source_ref: CPAPA-POSTEXT-2026
  prerequisites:
    - A practice-management tool whose API and webhooks allow outside systems to read and update jobs (CPAPA-POSTEXT-2026).
    - Before-change measurements of cycle times (CPAPA-POSTEXT-2026).
  risks_and_guardrails:
    - >-
      The model will misread some documents, especially photos of crumpled paper and consolidated brokerage
      statements; low-confidence results go to a person and nothing extracted flows into a return without a
      preparer seeing it (CPAPA-POSTEXT-2026).
    - >-
      Automations only one or two people understand become a dependency (CPAPA-POSTEXT-2026).
    - >-
      Clients send photos by text and other insecure channels, which leads to follow-up questions and security
      risk (TAXADVISER-CLIENTS-2026).
  human_checkpoints:
    - Staff handle documents that fail the stop rule; preparer sees all extracted data (CPAPA-POSTEXT-2026).
  role_evolution: >-
    Preparers stop reading the board aloud to clients and spend less time chasing documents (CPAPA-POSTEXT-2026).
  evidence_grade: D
  sources:
    - { ref: CPAPA-POSTEXT-2026, title: "The Post-Extension Window: How to Sequence Firm Automation Before Busy Season", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/10/16/the-post-extension-window-how-to-sequence-firm-automation-before-busy-season/191855/", date: 2026-10-16, access: full, locator: "sections 'Start with one workflow' and 'Use AI where it reads, not where it decides'" }
    - { ref: TAXADVISER-CLIENTS-2026, title: "What today's clients expect from their CPA and how firms are responding", publisher: The Tax Adviser (interview with Bob Nolan, Drake Software), type: press, url: "https://www.thetaxadviser.com/issues/2026/aug/what-todays-clients-expect-from-their-cpa-and-how-firms-are-responding/", date: 2026-08-31, access: full, locator: "Q on communication preferences" }
  last_reviewed: 2026-10-17
  notes: >-
    Idea: a practitioner article recommends this sequence; it names no firm that has run it. Labelled idea.

- id: tax-compliance-individual-business-06
  title: Client status messages and AI-assisted client communication during the season
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [client-interaction, document-production]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Clients call to ask where their return stands, and preparers are interrupted to read the job board aloud.
  solution: >-
    Short messages generated when a job changes stage (documents received, in preparation, one question waiting,
    ready for signature, filed), once the board is kept current. A survey of CPA tax preparers lists client
    communication as the second most common use of AI after tax research.
  outcomes:
    - lever: experience
      description: >-
        32 percent of respondents to the AICPA/Journal of Accountancy 2026 survey said they use AI for client
        communication.
      figure: 32 percent
      measures: >-
        Share of respondents (from 1,808 AICPA members who prepared 2025 income tax returns for a fee, surveyed
        1-19 June 2026) who said they use AI for client communication. The denominator for this specific question
        is not stated in the text.
      provenance: independent
      source_ref: AICPA-TAXSW-2026
  prerequisites:
    - Job stages in the practice tool kept current before status automation is added (CPAPA-POSTEXT-2026).
  risks_and_guardrails:
    - Client data entered into public tools breaches OPR's expectation of secure, enterprise-approved AI (IRS-OPR-2026).
  human_checkpoints:
    - A person takes over when a client needs a call from someone they know (CPAPA-POSTEXT-2026).
  role_evolution: >-
    Not described beyond fewer status interruptions (CPAPA-POSTEXT-2026).
  evidence_grade: C
  sources:
    - { ref: AICPA-TAXSW-2026, title: "2026 tax software survey", publisher: The Tax Adviser and Journal of Accountancy (AICPA), type: survey, url: "https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/", date: 2026-08-31, access: full, locator: "section 'Use of AI and other technical tools'" }
    - { ref: CPAPA-POSTEXT-2026, title: "The Post-Extension Window: How to Sequence Firm Automation Before Busy Season", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/10/16/the-post-extension-window-how-to-sequence-firm-automation-before-busy-season/191855/", date: 2026-10-16, access: full, locator: "section 'Add status updates only when the board is current'" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Circular 230 item 6" }
  last_reviewed: 2026-10-17
  notes: >-
    Grade C: an adoption survey, no named organisation and no outcome. The survey's table of AI uses is an image and
    was not readable, so only the figures in the text are used.

- id: tax-compliance-individual-business-07
  title: AI second review and diagnostics on prepared returns
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Review is the bottleneck when preparation gets faster. Reviewers must catch extraction, mapping and eligibility
    errors across more returns.
  solution: >-
    A review agent checks a prepared return for accuracy and flags questions. A vendor founder says his company
    began with automating one review step inside preparation and then moved to preparation. Perplexity says its
    agent can review a professionally prepared return and surface gaps. PwC lists 'tax diagnostics' among its
    deployed agents.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: >-
        No source read gives an accuracy, false-positive or override rate for AI return review.
      provenance: vendor-published
      source_ref: CPAPA-TAXGPT-2026
  prerequisites:
    - Prepared return and source documents in a form the agent can read (CPAPA-TAXGPT-2026).
  risks_and_guardrails:
    - >-
      Control dilution: AI-driven volume can make review less rigorous in practice even if the process is unchanged
      on paper (AICPA-WERFEL-2026).
    - >-
      TEI attendees described grappling with how to review a growing volume of work when AI errors are 'polite,
      quiet and technical' (TEI-TAXTECH-2026).
    - >-
      In a month-end close benchmark, in three of the four AI-assisted sessions that did not receive a perfect score,
      the AI had the correct figure at some point but it did not reach the final submission (ACCTODAY-AIBENCH-2026;
      adjacent accounting task, not tax).
  human_checkpoints:
    - Reviewer decides on every flag; the signing practitioner remains responsible (IRS-OPR-2026).
  role_evolution: >-
    The host of the TaxGPT episode compares AI output to the work of a two-year associate that someone must go
    through in detail (CPAPA-TAXGPT-2026).
  evidence_grade: C
  sources:
    - { ref: CPAPA-TAXGPT-2026, title: "Why General AI is Not Suitable for Tax Research - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/why-general-ai-is-not-suitable-for-tax-research-accounting-technology-lab-podcast-june-2026/", date: 2026-06, access: full, locator: "transcript, founder's account of review then preparation agents" }
    - { ref: PERPLEXITY-2026, title: "Perplexity Launches AI Agent That Drafts Tax Returns", publisher: PYMNTS, type: press, url: "https://www.pymnts.com/taxes/2026/perplexity-launches-ai-agent-that-drafts-tax-returns/", date: 2026-04-06, access: full, locator: "section 'Chat to Execution'" }
    - { ref: PWC-MEGNA-2025, title: "How PwC's tax team is using agentic AI (interview with Dom Megna)", publisher: CFO.com, type: firm, url: "https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/", date: 2025-06-06, access: full, locator: "introduction" }
    - { ref: AICPA-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08, access: full, locator: "Figure 3, 'Control dilution'" }
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Tech: the man behind the curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: 2026-05-04, access: full, locator: "section 'A very bad wizard'" }
    - { ref: ACCTODAY-AIBENCH-2026, title: "AI beats human accountants at monthly close, transaction categorization", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization", date: 2026-10-16, access: full, locator: "The Mercor benchmark section" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Conclusion" }
  last_reviewed: 2026-10-17
  notes: >-
    Grade C: product claims and one vendor founder's account, no measured review quality. The TEI quote is from a
    Thomson Reuters Institute recap of an in-house tax event, so it applies to corporate teams more than to small
    firms.

- id: tax-compliance-individual-business-08
  title: Generative AI assistant for retail tax-office preparers on code changes and unusual cases
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: >-
    Retail preparers must keep up with frequent tax code changes and answer 'the most gnarly questions' that
    arrive at the counter.
  solution: >-
    H&R Block and OpenAI announced a tool built on vetted data from H&R Block's Tax Institute, with an initial
    phase planned for late 2025 and large-scale deployment planned ahead of the 2026 season. The companies also
    said they would study return on investment from the AI tools.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: >-
        The April 2025 announcement gives no results; H&R Block's scale (over 20 million returns, 9,000 offices,
        60,000 tax professionals) is the company's own description of its business.
      provenance: self-reported
      source_ref: CNBC-HRB-2025
  prerequisites:
    - A curated internal knowledge base (The Tax Institute) to ground answers (CNBC-HRB-2025).
  risks_and_guardrails:
    - OpenAI told CNBC it does not train on customer data for this work (CNBC-HRB-2025).
  human_checkpoints:
    - The tool supports human preparers; OpenAI's chief economist describes it as a force multiplier for human expertise (CNBC-HRB-2025).
  role_evolution: >-
    Preparers get faster answers; the companies said they would study how professionals use it (CNBC-HRB-2025).
  evidence_grade: C
  sources:
    - { ref: CNBC-HRB-2025, title: "ChatGPT for taxes? OpenAI and H&R Block have a plan for tax pros", publisher: CNBC (via NBC San Diego), type: press, url: "https://www.nbcsandiego.com/news/business/money-report/chatgpt-for-taxes-openai-and-hr-block-have-a-plan-for-tax-pros/3804532/?amp=1", date: 2025-04-15, access: full, locator: "paragraphs 5-7 and 13-15" }
  last_reviewed: 2026-10-17
  notes: >-
    No source read confirms that the tool was deployed in the 2026 season or reports results. The search budget was
    exhausted before that could be checked.

- id: tax-compliance-individual-business-09
  title: Return assembly, delivery, signature and e-file authorization automation
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [coordination-scheduling, document-production]
  pattern: other
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Assembling the return package, collecting signatures (including Form 8879 routing to more than one signer),
    and taking payment are manual and error-prone.
  solution: >-
    Delivery and e-signature workflow tools (Thomson Reuters names SafeSend for the client side and SurePrep for
    the firm side), with the vendor claiming AI that recognises documents, extracts data and flags discrepancies.
    The pattern here is 'other': mostly workflow automation with an AI layer claimed by the vendor.
  outcomes:
    - lever: speed
      description: >-
        Thomson Reuters publishes that firms using SafeSend save about 15 minutes on every return, with assembly and
        delivery taking three to four minutes against 20 or more for a manual process.
      figure: about 15 minutes per return; about $12,000 per 1,000 returns delivered
      measures: >-
        Vendor's statement: 'Firms using SafeSend save about 15 minutes on every return and roughly $12,000 for
        every 1,000 returns delivered'. Sample, baseline and method are not given; the article itself urges readers
        to ask who checked such numbers.
      provenance: vendor-published
      source_ref: TR-TRUST7-2026
  prerequisites:
    - Integration with the tax software the firm already runs (TR-TRUST7-2026).
  risks_and_guardrails:
    - >-
      Edge cases (a spouse who cannot find the signing link, failed identity checks, an 8879 routed to two signers
      in two states) are where platforms differ, so test the exception path (TR-TRUST7-2026).
  human_checkpoints:
    - The preparer signs the return; the article stresses that the tool will not be in the room when a position is questioned (TR-TRUST7-2026).
  role_evolution: >-
    Not described.
  evidence_grade: C
  sources:
    - { ref: TR-TRUST7-2026, title: "Can you trust it? 7 questions to ask any platform that claims to handle your entire tax workflow", publisher: Thomson Reuters Tax and Accounting, type: vendor, url: "https://tax.thomsonreuters.com/blog/can-you-trust-it-7-questions-to-ask-any-platform-that-claims-to-handle-your-entire-tax-workflow/", date: 2026-10-14, access: full, locator: "questions 2, 4 and 5" }
  last_reviewed: 2026-10-17
  notes: >-
    Vendor marketing for a competitive evaluation; treat the minutes-per-return figure as a claim. The AI element
    is asserted, not evidenced.

- id: tax-compliance-individual-business-10
  title: Replace offshore or contract data entry and first-pass preparation with AI-prepared returns
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing]
  pattern: bulk-transformation
  ladder: automate
  change_scope: model
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Busy-season volume is met with outsourced staff, contractors and offshore preparers, with onboarding,
    quality and disclosure concerns.
  solution: >-
    Firms bring first-pass preparation onshore through AI products instead of staffing it offshore or with
    contractors. A vendor founder says users of his agent talk about bringing work back onshore, and a consultant
    says AI affects outsourcing more than onshore staff.
  outcomes:
    - lever: cost
      description: none published
      figure: none published
      measures: >-
        No source read reports the share of preparation moved from outsourced staff to AI or the cost per return
        before and after.
      provenance: vendor-published
      source_ref: BLACKORE-2026
  prerequisites:
    - Confidence in AI output at a level that allows removing the human data-entry layer; none of the sources set that threshold.
  risks_and_guardrails:
    - >-
      The firm's own security and consent position still applies to AI vendors, as it did to offshore staff
      (IRS-OPR-2026, BARMORE-OPR-2026).
  human_checkpoints:
    - Partner review (CPAPA-BLACKORE-2024).
  role_evolution: >-
    A vendor founder predicts firms will reduce reliance on outsourcing and shift toward advisory work
    (CPAPA-TAXGPT-2026). A trade-press article reports growing reliance on offshore staff as a feature of the
    current labour shortage (BLACKORE-2026).
  evidence_grade: C
  sources:
    - { ref: CPAPA-TAXGPT-2026, title: "Why General AI is Not Suitable for Tax Research - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/why-general-ai-is-not-suitable-for-tax-research-accounting-technology-lab-podcast-june-2026/", date: 2026-06, access: full, locator: "episode description; transcript, founder's remarks on onshoring" }
    - { ref: CPAPA-BLACKORE-2024, title: "Review of Black Ore Tax Autopilot - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/review-of-black-ore-tax-autopilot-the-accounting-technology-lab-podcast-june-2024/", date: 2024-06, access: full, locator: "transcript, discussion of outsourcing and disclosures" }
    - { ref: BLACKORE-2026, title: "AI Tax Startup Black Ore Opens Platform to CPA Firms", publisher: Sovereign Magazine, type: press, url: "https://www.sovereignmagazine.com/article/ai-tax-startup-black-ore-opens-platform-to-cpa-firms", date: 2026-04-29, access: full, locator: "section 'Black Ore and the Accountant Shortage'" }
    - { ref: BARMORE-OPR-2026, title: "The IRS Just Weighed In on AI", publisher: AI Lab for Accountants (Charlie Barmore, CPA), type: community, url: "https://ai-lab-for-accountants.beehiiv.com/p/the-irs-just-weighed-in-on-ai", date: 2026-06-24, access: full, locator: "section 'What OPR did NOT resolve' (offshore subprocessor point)" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Circular 230 items 4 and 6" }
  last_reviewed: 2026-10-17
  notes: >-
    No measured outsourcing displacement was found; the claim rests on commentators and a vendor founder. The pattern
    'bulk-transformation' is the closest fit for moving first-pass preparation volume from people to a model.

- id: tax-compliance-individual-business-11
  title: Taxpayer-side agents draft or check returns, bypassing or second-guessing the preparer
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, client-interaction]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: personal-assistant
  maturity: announced
  problem: >-
    Self-filers face cost, time and jargon, and some now ask general-purpose AI for help before, or instead of,
    hiring a preparer.
  solution: >-
    Perplexity announced a Computer for Taxes agent on 2 Apr 2026 that reviews uploaded documents, asks follow-up
    questions, maps inputs to IRS forms and drafts a federal return; it says it can also review a professionally
    prepared return. Individual taxpayers in forum threads describe using Claude, Gemini or ChatGPT to prepare or
    check their own returns, including checking a CPA's work.
  outcomes:
    - lever: experience
      description: >-
        PYMNTS reports that about a quarter of US workers plan to use AI to help file taxes this year, more than
        double the 11 percent who said so last year.
      figure: about 25 percent, up from 11 percent
      measures: >-
        Share of US workers who said they plan to use AI to help file taxes, current year versus last year, as
        reported by PYMNTS from its own survey; sample not given.
      provenance: vendor-published
      source_ref: PERPLEXITY-2026
    - lever: quality
      description: >-
        A test of four chatbots by TaxSlayer, reported by the New York Times and relayed by PYMNTS, found the tools
        miscalculated the refund or amount owed by an average of more than $2,000 across eight fictional scenarios.
      figure: average error more than $2,000
      measures: >-
        Average miscalculation of refund or amount owed across eight fictional tax scenarios, four chatbots, per
        a TaxSlayer test (a competitor tax-software vendor), relayed secondhand.
      provenance: vendor-published
      source_ref: PERPLEXITY-2026
    - lever: experience
      description: >-
        Taxfix (a digital tax platform) reports that 59 percent of UK self assessment filers it surveyed plan to use
        AI tools to complete their returns, and 81 percent still want access to a qualified professional.
      figure: 59 percent plan to use AI; 81 percent want access to a professional
      measures: >-
        Taxfix's survey of UK Self Assessment filers (sample size not stated in the article): share planning to use
        AI tools before the 31 January deadline; share wanting access to a qualified professional when needed.
      provenance: vendor-published
      source_ref: TECHRADAR-TAXFIX-2025
  prerequisites:
    - Taxpayer uploads personal documents to the agent (PERPLEXITY-2026).
  risks_and_guardrails:
    - >-
      NAEA tells taxpayers not to upload W-2s, Social Security numbers or other personal data into unsecured or
      unverified AI systems and says AI quite often gives faulty tax advice (NAEA-AI-2026).
    - >-
      In a UK example from Taxfix, a client wrongly applied the 1,000-pound trading allowance and a person caught it
      (TECHRADAR-TAXFIX-2025).
    - >-
      Forum commenters raise liability: a CPA can be sued for negligence while an LLM cannot (HN-ASK-2026).
  human_checkpoints:
    - None by design for self-filers; practitioners are asked to validate client-brought AI conclusions (TECHRADAR-TAXFIX-2025).
  role_evolution: >-
    Taxfix says accountants will increasingly work with AI-informed clients and will need to validate, explain and
    possibly correct what they bring (TECHRADAR-TAXFIX-2025). A Drake Software tax analyst says tools that help
    people find answers quickly could reduce demand for simpler tax preparation over time (TAXADVISER-CLIENTS-2026).
  evidence_grade: C
  sources:
    - { ref: PERPLEXITY-2026, title: "Perplexity Launches AI Agent That Drafts Tax Returns", publisher: PYMNTS, type: press, url: "https://www.pymnts.com/taxes/2026/perplexity-launches-ai-agent-that-drafts-tax-returns/", date: 2026-04-06, access: full, locator: "sections 'Chat to Execution' and 'Consumers Are Already at the Door'" }
    - { ref: TECHRADAR-TAXFIX-2025, title: "The rise of the AI accountant: Cheaper. Faster. Riskier?", publisher: TechRadar (written by Taxfix), type: press, url: "https://www.techradar.com/pro/the-rise-of-the-ai-accountant-cheaper-faster-riskier", date: 2025-10-29, access: full, locator: "paragraphs 2-5, 'The impacts on accountants'" }
    - { ref: NAEA-AI-2026, title: "NAEA Highlights Find a Tax Expert Directory as Taxpayers Navigate AI-Driven Filing Season", publisher: National Association of Enrolled Agents, type: professional-body, url: "https://lite.aol.com/tech/story/0022/20260326/9679339.htm", date: 2026-03-26, access: full, locator: "quotes from NAEA president; data-protection paragraph" }
    - { ref: HN-ASK-2026, title: "Ask HN: Why hasn't AI replaced Tax filing software", publisher: Hacker News, type: community, url: "https://news.ycombinator.com/item?id=50004396", date: 2026-10-08, access: full, locator: "comments by arbol, gayaviswan, JohnFen, jfrbfbreudh" }
    - { ref: TAXADVISER-CLIENTS-2026, title: "What today's clients expect from their CPA and how firms are responding", publisher: The Tax Adviser (interview with Bob Nolan, Drake Software), type: press, url: "https://www.thetaxadviser.com/issues/2026/aug/what-todays-clients-expect-from-their-cpa-and-how-firms-are-responding/", date: 2026-08-31, access: full, locator: "last Q and A" }
  last_reviewed: 2026-10-17
  notes: >-
    Forum comments are anonymous and anecdotal (for example, one commenter says an LLM prepared a return 'more
    accurate' than their accountant but did not say how that was measured). TaxCalcBench (COLUMN-TCBREPO-2026)
    is the closest measured evidence: strict return-level correctness ranged from 0 to about 71 percent on 50
    TY2025 cases, and several top rows depend on web search.

- id: tax-compliance-individual-business-12
  title: AI-native roll-ups buy small tax practices and run them on in-house AI
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, document-production]
  pattern: other
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: >-
    Small tax practices have thin margins and difficulty adopting new processes, while buyers look for
    recurring-revenue service businesses.
  solution: >-
    Multiplier Holdings acquired Citrine International Tax, a 12-person cross-border tax accounting boutique, and
    applied AI tools it built in-house; the investor says the approach works best on small firms because they are
    more open to changing processes. Other AI-native firms are listed in the landscape file but were not opened here.
  outcomes:
    - lever: cost
      description: >-
        Multiplier says its AI tools helped Citrine more than double its profit margins after acquisition.
      figure: profit margins more than doubled
      measures: >-
        Profit margins of one 12-person tax accounting entity after acquisition and AI use; baseline margin and
        period not stated. Reported by TechCrunch from the founder and the investor.
      provenance: self-reported
      source_ref: MULTIPLIER-2025
  prerequisites:
    - A small, change-ready firm with high recurring revenue and an owner willing to customise the AI (MULTIPLIER-2025).
  risks_and_guardrails:
    - One firm, self-reported by the buyer; no independent verification (MULTIPLIER-2025).
  human_checkpoints:
    - Not described.
  role_evolution: >-
    Multiplier says its goal is to expand beyond personal tax compliance to an AI-powered competitor to the Big
    Four (MULTIPLIER-2025). The Black Ore summit recap lists AI-native firms and private equity in the profession
    as themes (BLACKORE-SUMMIT-2026).
  evidence_grade: B
  sources:
    - { ref: MULTIPLIER-2025, title: "Multiplier, founded by ex-Stripe exec, nabs $27.5M to fuel AI-powered accounting roll-ups", publisher: TechCrunch, type: press, url: "https://techcrunch.com/2025/06/18/multiplier-founded-by-ex-stripe-exec-nabs-27-5m-to-fuel-ai-powered-accounting-roll-up", date: 2025-06-18, access: full, locator: "paragraphs 3-4 and 6" }
    - { ref: BLACKORE-SUMMIT-2026, title: "2026 Black Ore AI Tax Summit - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/2026-black-ore-ai-tax-summit-accounting-technology-lab-podcast-june-2026/", date: 2026-06, access: full, locator: "episode description" }
  last_reviewed: 2026-10-17
  notes: >-
    Grade capped at B: the figure is for a cross-border tax accounting boutique, which is adjacent to individual and
    small-business return preparation, and the source is a funding story. Pattern is 'other': the change is who owns
    and runs the practice, not a single AI task.

- id: tax-compliance-individual-business-13
  title: Value-based pricing and disclosure of AI efficiencies for AI-assisted return work
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [client-interaction, expert-judgment]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    Hours-times-rate billing shrinks when AI cuts preparation time, and OPR has said billing for manual time that
    was not spent can raise an unconscionable-fee problem under section 10.27(a).
  solution: >-
    Price by value, bundle return preparation with advisory services, and disclose and credit AI efficiencies as
    OPR describes. The AICPA has asked the IRS for clarifying language and FAQs because the OPR text does not
    appear to allow for value pricing and overlooks software, implementation, governance and training costs.
  outcomes:
    - lever: growth
      description: none published
      figure: none published
      measures: >-
        No source gives a fee, margin or realisation figure for AI-assisted return preparation. The Thomson Reuters
        paper reports that one-third of respondents say their firms have yet to adapt commercial models.
      provenance: vendor-published
      source_ref: TR-FOP-2026
  prerequisites:
    - Time and cost tracking that lets the firm show what AI saved and what it cost (AICPA-FEES-2026).
  risks_and_guardrails:
    - >-
      OPR: where AI cuts research and drafting time, billing manual labour or time not spent, or double billing for
      AI-assisted tasks, may violate section 10.27 depending on facts such as a pattern across clients or the size
      of billing differences (IRS-OPR-2026).
    - >-
      The AICPA's chief executive said the OPR language is not authoritative and could be 'overstepping a little
      bit' (AICPA-FEES-2026).
  human_checkpoints:
    - Partner decision on pricing and disclosure.
  role_evolution: >-
    The AICPA says it encourages members toward advisory services and bundling (AICPA-FEES-2026). A vendor founder
    predicts a move from billable hours to outcome-based pricing (CPAPA-TAXGPT-2026).
  evidence_grade: D
  sources:
    - { ref: AICPA-FEES-2026, title: "AICPA seeks IRS clarity on AI guidelines, CPA fees", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/news/2026/sep/aicpa-seeks-irs-clarity-on-ai-guidelines-cpa-fees/", date: 2026-09-08, access: full, locator: "paragraphs 1-4 and 8-9" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Circular 230 item 2 (section 10.27(a))" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026: Actionable insights for tax and audit leaders", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: 2026-07-21, access: full, locator: "introductory paragraphs" }
    - { ref: CPAPA-TAXGPT-2026, title: "Why General AI is Not Suitable for Tax Research - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/why-general-ai-is-not-suitable-for-tax-research-accounting-technology-lab-podcast-june-2026/", date: 2026-06, access: full, locator: "episode description" }
  last_reviewed: 2026-10-17
  notes: >-
    Idea. The dispute between OPR and the AICPA is a documented discussion, but no firm has published how it
    prices AI-assisted preparation. Pattern is 'other': the change is commercial, not an AI task. OPR's text says
    AI activities should be disclosed in general or specific terms as needed.

- id: tax-compliance-individual-business-14
  title: Firm AI policy, approved-tool list and verification log for return work (Circular 230 section 10.36)
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [review-assurance, coordination-scheduling]
  pattern: other
  ladder: assist
  change_scope: process
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Staff use unapproved tools, nobody owns AI, and firms cannot show how outputs were verified.
  solution: >-
    A written AI policy with an approved-tool list and a request process, an AI lead or committee, vendor vetting,
    training, and documentation in the client file of the prompts used, how outputs were verified and who reviewed
    them, built into the quality-control system. Werfel's framework adds a scope-then-risk-then-controls method with
    phased rollout, for example limiting a tool to document summarisation before it drafts positions.
  outcomes:
    - lever: risk
      description: >-
        Thomson Reuters reports that more than one-third of tax and audit professionals use AI tools their firm has
        not sanctioned. In the corporate-tax setting, two hands of more than 50 went up when TEI attendees were asked
        whether tax owns AI implementation.
      figure: more than one-third use unsanctioned tools; 2 of more than 50 attendees say tax owns AI implementation
      measures: >-
        Share of respondents to the Thomson Reuters Future of Professionals 2026 survey of tax and audit professionals
        who use unauthorised AI tools (the page says 'more than one-third'; a Thomson Reuters blog says 34 percent);
        a show-of-hands poll at the April 2026 TEI Tax Technology Seminar.
      provenance: vendor-published
      source_ref: TR-FOP-2026
  prerequisites:
    - Someone accountable for AI at the firm (JOFA-POLICY-2026, AICPA-WERFEL-2026).
    - Enterprise or business-tier tools with defined data terms; OPR names 'secure, enterprise-approved AI' without defining it (IRS-OPR-2026, BARMORE-OPR-2026).
  risks_and_guardrails:
    - >-
      Section 10.36 makes those with principal authority responsible for reasonable procedures, documented, with
      staff training, secure data handling, accuracy monitoring and vetting of outsourced or third-party AI
      (IRS-OPR-2026).
    - >-
      Vendor indemnification from major AI providers generally does not remove client confidentiality, professional
      liability and accuracy exposures, per a CPA-technology podcast (CPAPA-AILIAB-2026; show notes only).
    - >-
      The AICPA formed the Council on AI Risk in Tax in September 2026 to test and refine Werfel's framework
      (AICPA-CART-2026).
  human_checkpoints:
    - The AI lead or committee approves tools and use cases; the signing CPA remains responsible for accuracy (JOFA-POLICY-2026).
  role_evolution: >-
    New AI lead role; staff training expected under section 10.36 (IRS-OPR-2026). Thomson Reuters' paper says firms
    must still give junior staff structured development as AI automates tasks (TR-FOP-2026).
  evidence_grade: C
  sources:
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Circular 230 item 4 and 'Best Practices for Responsible AI Use'" }
    - { ref: JOFA-POLICY-2026, title: "Drafting an AI policy that actually works", publisher: Journal of Accountancy (Nicole L. Graham, Esq.), type: press, url: "https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works/", date: 2026-07-01, access: full, locator: "sections 'Governance', 'Documentation and Supervision'" }
    - { ref: AICPA-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08, access: full, locator: "preparer methodology and 'Innovate, but responsibly'" }
    - { ref: TR-FOP-2026, title: "Future of Professionals Report 2026: Actionable insights for tax and audit leaders", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: 2026-07-21, access: full, locator: "'Universal priorities for firm leaders'" }
    - { ref: TEI-TAXTECH-2026, title: "2026 TEI Tax Tech: the man behind the curtain", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain", date: 2026-05-04, access: full, locator: "paragraph on the poll of more than 50 attendees" }
    - { ref: BARMORE-OPR-2026, title: "The IRS Just Weighed In on AI", publisher: AI Lab for Accountants (Charlie Barmore, CPA), type: community, url: "https://ai-lab-for-accountants.beehiiv.com/p/the-irs-just-weighed-in-on-ai", date: 2026-06-24, access: full, locator: "'What to do Monday morning'" }
    - { ref: AICPA-CART-2026, title: "AICPA, former IRS commissioner to lead initiative on AI in tax", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/", date: 2026-09-23, access: full, locator: "paragraphs 1-4" }
    - { ref: CPAPA-AILIAB-2026, title: "AI Liability for Accounting Firms: Are You Covered? - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/ai-liability-for-accounting-firms-are-you-covered-microsoft-google-openai-anthropic-accounting-technology-lab-podcast-oct-2026/", date: 2026-10, access: full, locator: "episode description" }
  last_reviewed: 2026-10-17
  notes: >-
    Governance is an enabling control for the other use cases rather than an AI task, so the pattern is 'other'.
    The TEI poll is from corporate tax departments, not small firms. The 34 percent versus 'more than one-third'
    difference reflects two Thomson Reuters pages describing the same survey (TR-CHEAP-2026 gives 34 percent).

- id: tax-compliance-individual-business-15
  title: Client disclosure and separate section 7216 consent before AI touches return information
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [client-interaction, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: emerging
  problem: >-
    Section 7216 requires written consent before preparers use or disclose return information for other
    purposes, and the exceptions have generally covered tax software. It is unsettled whether an AI tool counts as
    software or as a third party.
  solution: >-
    Practitioners and the AICPA advise a signed, stand-alone AI disclosure or consent, an inventory of AI tools that
    touch client data, and AI governance folded into the firm's written information security plan. Other guidance
    suggests engagement-letter language about AI use as voluntary transparency.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: No source reports how many firms use AI-specific consent or what clients do with it.
      provenance: self-reported
      source_ref: BARMORE-OPR-2026
  prerequisites:
    - An inventory of which AI tools staff use on client data (VERITO-DISCL-2026).
    - A decision on whether a given tool is a processor receiving return information (BARMORE-OPR-2026).
  risks_and_guardrails:
    - >-
      OPR Alert 2026-19 cites sections 6713 and 7216(a) and Circular 230 section 10.51(a)(15) and tells practitioners
      to use only secure, enterprise-approved AI; it does not say whether AI use requires consent
      (IRS-OPR-2026, BARMORE-OPR-2026).
    - >-
      Unresolved by OPR, per a practitioner newsletter: whether a self-hosted model is a disclosure, whether cloud
      AI needs consent, what 'enterprise-approved' means, how Rev. Proc. 2013-14 consent forms apply, and offshore
      subprocessor access (BARMORE-OPR-2026).
    - >-
      CNBC reports the IRS guidance does not directly say whether preparers must tell clients when generative AI
      helps prepare a return, and that the AICPA is advising disclosure as a precaution (LDS-CNBC-2026, secondary
      summary of CNBC).
    - >-
      Guidance conflicts on form: a vendor blog says the AICPA's Henry Grzes told CNBC the consent must be a separate
      document for individual returns (VERITO-DISCL-2026; not confirmed against CNBC), while a Journal of
      Accountancy article suggests disclosure language in all engagement letters (JOFA-POLICY-2026).
  human_checkpoints:
    - Client signs before AI is used on their return information (VERITO-DISCL-2026).
  role_evolution: >-
    Preparers and firm leaders take on an AI-tool inventory and consent-management task.
  evidence_grade: C
  sources:
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Circular 230 item 6; footnote 1" }
    - { ref: BARMORE-OPR-2026, title: "The IRS Just Weighed In on AI", publisher: AI Lab for Accountants (Charlie Barmore, CPA), type: community, url: "https://ai-lab-for-accountants.beehiiv.com/p/the-irs-just-weighed-in-on-ai", date: 2026-06-24, access: full, locator: "section 'What OPR did NOT resolve'" }
    - { ref: LDS-CNBC-2026, title: "IRS AI Guidance Leaves Client Disclosure Question Open", publisher: Let's Data Science (summarising CNBC), type: press, url: "https://letsdatascience.com/news/irs-ai-guidance-leaves-client-disclosure-question-open-f5400ffe", date: 2026-08-04, access: full, locator: "section 'Existing rules and the disclosure gap'" }
    - { ref: VERITO-DISCL-2026, title: "Do Tax Preparers Have to Disclose AI Use to Clients?", publisher: Verito (vendor blog), type: vendor, url: "https://verito.com/blog/ai-tax-preparer-disclosure-requirements/", date: 2026-08-14, access: full, locator: "section 'Does Section 7216 Require Telling Clients When AI Prepares Their Return?'" }
    - { ref: JOFA-POLICY-2026, title: "Drafting an AI policy that actually works", publisher: Journal of Accountancy (Nicole L. Graham, Esq.), type: press, url: "https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works/", date: 2026-07-01, access: full, locator: "section 'Transparency and Client Communication'" }
  last_reviewed: 2026-10-17
  notes: >-
    Pattern is 'other': a consent and disclosure control, not an AI task. The CNBC article itself (4 Aug 2026) was not opened; its content is taken from a secondary summary and a vendor
    blog, which is why no AICPA position is stated as fact. The AICPA's own FAQs on AI in federal tax practice are
    referred to in AICPA-FEES-2026 but were not retrieved.

- id: tax-compliance-individual-business-16
  title: Parallel-run and before-and-after measurement when adopting AI preparation
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: assist
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Firms adopt on vendor claims and cannot say whether time, quality or cycle time improved; independent
    evidence on AI-prepared returns is scarce.
  solution: >-
    Run last year's returns through the AI product to compare with what was filed, trial new workflows on a few
    dozen engagements first, and record cycle times before the change (median days from organizer sent to
    documents complete; days from finished return to signed authorization and paid invoice).
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: >-
        No firm has published a parallel-run result. A related benchmark outside tax found that accountants
        working with Claude took about 15 times longer per task than Claude alone (ACCTODAY-AIBENCH-2026).
      provenance: independent
      source_ref: ACCTODAY-AIBENCH-2026
  prerequisites:
    - Prior-year returns and source documents; baseline measures captured before change (CPAPA-POSTEXT-2026).
  risks_and_guardrails:
    - >-
      Werfel advises starting with limited-scope deployments tested thoroughly before scaling (AICPA-WERFEL-2026).
    - >-
      In the Mercor month-end close tasks, 12 junior CPAs (about five years' experience on average) generally scored
      below 50 percent without AI and none was perfect; the AI alone scored 100 percent on 20 attempts. The task is accounting close, not tax
      (ACCTODAY-AIBENCH-2026).
  human_checkpoints:
    - Partner reviews the difference between the AI draft and the filed return (CPAPA-BLACKORE-2024).
  role_evolution: >-
    Not described.
  evidence_grade: D
  sources:
    - { ref: CPAPA-BLACKORE-2024, title: "Review of Black Ore Tax Autopilot - Accounting Technology Lab Podcast", publisher: CPA Practice Advisor, type: podcast, url: "https://www.cpapracticeadvisor.com/podcasts/review-of-black-ore-tax-autopilot-the-accounting-technology-lab-podcast-june-2024/", date: 2024-06, access: full, locator: "transcript, remark about running a prior-year return" }
    - { ref: CPAPA-POSTEXT-2026, title: "The Post-Extension Window: How to Sequence Firm Automation Before Busy Season", publisher: CPA Practice Advisor, type: press, url: "https://www.cpapracticeadvisor.com/2026/10/16/the-post-extension-window-how-to-sequence-firm-automation-before-busy-season/191855/", date: 2026-10-16, access: full, locator: "sections 'Run the new workflow on a subset' and 'Measure before you change anything'" }
    - { ref: AICPA-WERFEL-2026, title: "A risk framework for AI use in tax administration and preparation", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/", date: 2026-08, access: full, locator: "'Innovate, but responsibly'" }
    - { ref: ACCTODAY-AIBENCH-2026, title: "AI beats human accountants at monthly close, transaction categorization", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization", date: 2026-10-16, access: full, locator: "The Mercor benchmark section" }
  last_reviewed: 2026-10-17
  notes: >-
    Idea: practitioners recommend this; no firm result was found. The Mercor and Digits study figures are
    vendor-run and adjacent, so they appear only in guardrails and are routed to the accounting archetype.
```

## 3. Module notes

### Processes and key steps (with work types)

1. **Engagement and onboarding:** engagement letter, client information, prior-year data. Work types: document-production, client-interaction.
2. **Organizer and document request:** send the organizer, chase missing items by reminders, check what arrived. Work types: coordination-scheduling, client-interaction. A practitioner article says a single missing brokerage statement can hold up a return (CPAPA-POSTEXT-2026, 'Start with one workflow').
3. **Document intake and extraction:** classify W-2, 1099, K-1, brokerage statements and property-tax bills; pull payer and tax year; key data. Work type: transaction-processing.
4. **Preparation:** apply federal and state tax logic, build workpapers, tie out. Work types: transaction-processing, document-production.
5. **Review:** preparer, manager and partner review. Work type: review-assurance.
6. **Delivery and sign-off:** assembly, signature (including Form 8879 routing), payment, e-file authorization and filing. Work types: coordination-scheduling, document-production (TR-TRUST7-2026, question 2).
7. **Post-filing:** notices and amended returns (routed to controversy), and advisory follow-up from return data (routed to advisory).

### Common pain points

- **Labour supply and season peaks.** Black Ore frames its launch around a shortage of qualified accountants and long busy-season hours; Thomson Reuters says busy season has become synonymous with burnout and staffing strain (BLACKORE-2026, 'Black Ore and the Accountant Shortage'; TR-R2R-2025). The article attributes about 300,000 net departures from the profession to the Bureau of Labor Statistics, and gives a 125 million-hour annual shortfall in tax services as Black Ore's own estimate, which the company did not attribute to an external source.
- **Tax law complexity.** For solo practitioners and firms of up to 10 staff, tax law complexity ranked first in the AICPA's 2026 top-issues survey, ahead of AI (AICPA-TOPISSUES-2026).
- **Data import and integration.** In the AICPA's 2026 software survey, respondents were least satisfied with importing data (average 3.4 out of 5 across the seven major products) and integration with other software (AICPA-TAXSW-2026, 'Ratings').
- **Client channels.** A Drake Software tax analyst says clients text photos of documents, which is efficient but not always secure and leads to follow-up questions (TAXADVISER-CLIENTS-2026).
- **Low-value 1040 work.** Two CPA-technology commentators say many firms are walking away from 1040 work as low value even though it feeds advisory work (CPAPA-BLACKORE-2024).

### Metrics and benchmarks (with sources)

| Figure | What it measures (source's words) | Provenance | Source |
|---|---|---|---|
| 65 percent; 32 percent; 16 percent (24.3 percent in 2025) | Respondents using AI in tax research; using AI for client communication; saying they have no plans to use AI. Sample: 1,808 AICPA members who prepared 2025 returns for a fee, surveyed 1-19 June 2026. The text does not say whether the percentages use all 1,808 as denominator. | independent (professional body) | AICPA-TAXSW-2026 |
| 93 percent | Respondents who do not use other tools to review returns for planning opportunities; 2 percent use Holistiplan | independent | AICPA-TAXSW-2026 |
| 20 percent; of those, 75 percent tax advisory | Respondents expanding the services they offer; share of those naming tax advisory as an area | independent | AICPA-TAXSW-2026 |
| 81 percent | Tax and audit professionals who say they use AI tools regularly (Thomson Reuters 2026 Future of Professionals Report) | vendor-published | TR-FOP-2026 |
| More than one-third (34 percent in a TR blog) | Professionals using AI tools their firm has not authorised | vendor-published | TR-FOP-2026; TR-CHEAP-2026 |
| About one hour per simple 1040 | Partner's estimate of preparation time saved with Ready to Review, early-adopter program | vendor-published | TR-COCOUNSEL-2025 |
| Up to 98 percent; above 99 percent | Black Ore's claimed time saving on complex filings and accuracy across tens of thousands of pilot returns; denominators not defined | vendor-published | BLACKORE-2026 |
| 15 minutes per return; $12,000 per 1,000 returns | Thomson Reuters' claim for SafeSend delivery workflow savings | vendor-published | TR-TRUST7-2026 |
| Less than one third | Simplified federal returns computed correctly by frontier models, 2025 paper | vendor-published (Column Tax) | COLUMN-TAXCALCBENCH-2025 |
| 0 to 71.43 percent (strict, return-level) | TaxCalcBench TY2025 v2 edition, 50 cases with PDF inputs and state returns; best row used web search and scored 49 of 50 cases (one excluded because the model copied the expected output from the repository). Best row without web search: 40.00 percent. Calculation step only. | vendor-published (Column Tax sells a deterministic engine) | COLUMN-TCBREPO-2026 |
| Average error above $2,000 | Four chatbots, eight fictional tax scenarios, per a TaxSlayer test reported by the New York Times; relayed by PYMNTS | vendor-published (competitor), secondhand | PERPLEXITY-2026 |
| 59 percent; 73 percent | UK self-assessment filers planning to use AI tools; accountants surveyed who say AI gives incomplete advice. Taxfix survey, sample sizes not stated | vendor-published | TECHRADAR-TAXFIX-2025 |
| About 15 times longer; 100 percent vs below 50 percent | Mercor month-end close study (adjacent, not tax): accountants working with Claude vs Claude alone; Claude alone scored 100 percent on 20 attempts; 12 junior CPAs without AI generally scored below 50 percent | vendor-published (Mercor), adjacent | ACCTODAY-AIBENCH-2026 |
| More than 80 percent | Individual return preparation automated by some firms, per a 2025 CPA.com report as paraphrased by Journal of Accountancy; report not seen | secondhand | JOFA-SMALLFIRM-2026 |

**Absence of quality evidence:** none of the sources read gives an error rate, override rate, parallel-run result or inspection finding for AI-prepared individual or small-business returns, and none reports a regulator action on AI-prepared returns. OPR states that "cases imposing sanctions against other types of tax professionals are slowly emerging" and cites a 2025 Deloitte Australia report with invented quotes, not a return-preparation case (IRS-OPR-2026, 'Real-World Consequences').

### Guardrails and regulatory points

- **Circular 230 mapping (OPR Alert 2026-19, 24 Jun 2026):** section 10.22 due diligence, 10.27(a) fees, 10.35 competence, 10.36 firm procedures, 10.37 written advice, and 10.51(a)(15) with IRC sections 6713 and 7216(a) for unauthorised use or disclosure of return information (IRS-OPR-2026; JOFA-OPR-2026; ACCTODAY-OPR-2026). OPR says practitioners "must strictly handle all client data using only secure, enterprise-approved AI" and does not define the term (IRS-OPR-2026; BARMORE-OPR-2026).
- **Open questions:** whether cloud AI use needs section 7216 consent, whether a self-hosted model is a disclosure, how Rev. Proc. 2013-14 forms apply, and offshore subprocessors (BARMORE-OPR-2026, 'What OPR did NOT resolve').
- **Reorganisation:** Journal of Accountancy reports the IRS said in June 2026 it would merge OPR with the Return Preparer Office to form a Tax Professional Management Office (JOFA-OPR-2026, paragraph 4).
- **Courts:** *Clinco*, T.C. Memo. 2026-16: three of four cases cited by taxpayer's counsel were apparently hallucinated; the court stopped short of sanctions; the article calls it apparently the first Tax Court case to address AI hallucinations (TAXCT-CLINCO-2026).
- **Risk framework:** Werfel's preparer register lists 15 risks in five layers (technical, practice, legal and regulatory, business, workforce and strategic), including incorrect document extraction, control dilution and skill erosion; the AICPA's Council on AI Risk in Tax (23 Sep 2026) will test it (AICPA-WERFEL-2026, Figures 3-4; AICPA-CART-2026).
- **Liability and insurance:** a CPA-technology podcast (Oct 2026) says vendor indemnification from major AI providers generally does not remove confidentiality, professional-liability and accuracy exposures (CPAPA-AILIAB-2026, show notes only).
- **Landscape coverage not repeated here:** UK PCRT guidance and Australia's TPB guidance are in the landscape file and were not re-read.

### Frontier signals (dated, sourced)

- 2025-12-15: Thomson Reuters says Ready to Review is generally available for 1040 and expects firms to pair each CPA with at least one virtual agent (TR-R2R-2025).
- 2026-02-26: Basis reports a $100M Series B and an agent that autonomously completed a 1065 in a demonstration (BASIS-2026).
- 2026-04-02: Perplexity announces a consumer agent that drafts federal returns (PERPLEXITY-2026).
- 2026-04-29: Black Ore opens Tax Autopilot to firms after a two-year pilot; about 3,700 firms on a waitlist per the company (BLACKORE-2026).
- 2026-06: At Black Ore's summit, industry predictions as summarised by two CPA-technology hosts put fully autonomous individual preparation by 2027, with entity preparation shortly after (BLACKORE-SUMMIT-2026, episode description).
- 2026-06-24: OPR Alert 2026-19 (IRS-OPR-2026). 2026-09-08: AICPA asks the IRS to clarify the fee language (AICPA-FEES-2026). 2026-09-23: Council on AI Risk in Tax launched (AICPA-CART-2026).
- 2026-08: AICPA survey shows "no plans to use AI" falling from 24.3 to 16 percent in a year (AICPA-TAXSW-2026).
- 2026-10-16: Trade press advises sequencing automation, starting with document requests, in the post-extension quiet period before busy season (CPAPA-POSTEXT-2026).
- 2026-06: Column Tax releases a harder TaxCalcBench for tax year 2025 (PDF inputs, state returns) (COLUMN-TCBREPO-2026).

### Workforce and role effects

- A Thomson Reuters survey paper says more than one-quarter of tax and audit professionals would not accept a job at a firm lacking professional-grade AI, and almost one in three would consider leaving if AI expectations are not met within two years; it also tells leaders to ensure junior staff still get structured development as tasks are automated (TR-FOP-2026). Vendor-owned survey.
- Werfel's register names skill erosion (staff learn the tool rather than the law) and institutional knowledge loss as preparer risks (AICPA-WERFEL-2026, Figure 3).
- Two commentators expect the main labour effect on outsourced and offshore services rather than onshore staff (CPAPA-BLACKORE-2024); a vendor founder predicts less outsourcing and a move to advisory and outcome pricing (CPAPA-TAXGPT-2026).
- A Drake Software analyst says tools that help people find answers quickly could reduce demand for simpler tax preparation over time (TAXADVISER-CLIENTS-2026).
- AI change management ranked as the top five-year issue for CPA firms, and staff retention reached the top five for all but solo firms (AICPA-TOPISSUES-2026).
- At TEI, a transformation director described a training rollout that failed because users had not been consulted (TEI-TAXTECH-2026). Corporate setting.

### Objections and concerns practitioners raise

- **Silent, polite errors:** "AI doesn't fail loudly anymore" (TEI-TAXTECH-2026, 'A very bad wizard').
- **Review capacity:** volume outruns review; control dilution (TEI-TAXTECH-2026; AICPA-WERFEL-2026).
- **Humans overriding correct AI:** in the Mercor study, participants sometimes deferred to a later wrong AI answer or overrode a correct one (ACCTODAY-AIBENCH-2026; adjacent).
- **Fee pass-through that ignores AI costs and value pricing** (AICPA-FEES-2026).
- **Data exposure through consumer tools** (IRS-OPR-2026; NAEA-AI-2026) and ambiguity over section 7216 consent (BARMORE-OPR-2026).
- **Liability and who is the signer:** commenters note a CPA can be sued for negligence while an LLM cannot (HN-ASK-2026); Werfel lists liability ambiguity between preparer and vendor (AICPA-WERFEL-2026).
- **Vendor claims:** even Thomson Reuters tells buyers to ask who checked a vendor's numbers (TR-TRUST7-2026, question 4). A 2025 benchmark thread had commenters asking what an average accountant would score (HN-TCB-2025).
- **Disintermediation by consumer agents** (PERPLEXITY-2026; HN-ASK-2026), balanced by Taxfix's finding that 81 percent still want access to a professional (TECHRADAR-TAXFIX-2025).
- **Counter-view from corporate tax:** an academic argues AI cannot hold culpability and conflates preparation with practice (SALA-TAXNOTES-2026, abstract); this is a corporate tax claim and is routed below.

### Interview probes for an advisor

1. Which step of your return workflow would you hand to an agent first (document requests, extraction, preparation, review), and what did you measure before you changed it? Do you have median days from organizer sent to documents complete?
2. When an AI-prepared or AI-reviewed return reaches your reviewer, what are they asked to check, how long do they get, and have you ever seen a case where the reviewer overrode a correct AI answer or accepted a wrong one?
3. How do you handle section 7216 consent, engagement-letter wording and AI-tool vetting today, and who in the firm owns the approved-tool list?
4. How are you pricing AI-assisted returns, and how would you respond to a client or OPR asking where the efficiency went?
5. What happens to your junior staff pipeline and your outsourced capacity if first-pass preparation becomes routine, and which returns would you refuse to route to an agent?

## 4. Routed to other modules

- **research-advisory:** AI tax research is the most common AI use in the AICPA survey (65 percent) and the subject of the TaxGPT episode, the Thomson Reuters "cheap AI" post and the Clinco hallucination case (AICPA-TAXSW-2026, CPAPA-TAXGPT-2026, TR-CHEAP-2026, TAXCT-CLINCO-2026). Also the Blue J/CPA.com 33 to 60 percent weekly-use figure, seen only secondhand in VERITO-DISCL-2026 and LDS-CNBC-2026 (not used as an outcome).
- **controversy (tax authority AI, notices):** IRS AI audit selection and cross-matching, 25 percent staff reduction, longer notice resolution, and the advice to build a notice-response workflow and raise documentation standards (ACCTODAY-2026). The article's author works for an outsourced-accounting provider, and its IRM 10.24.1 and TIGTA/GAO counts were not checked against primary documents.
- **advisory / business model:** 20 percent of surveyed firms expanding services, mostly tax advisory (AICPA-TAXSW-2026); the "keep 1040 clients to feed advisory" argument (CPAPA-BLACKORE-2024); year-round compliance-risk partner positioning (ACCTODAY-2026).
- **tax-data-technology / corporate compliance:** TEI Tax Tech findings on ownership, training and review (TEI-TAXTECH-2026); Sala's argument about corporate tax team size (SALA-TAXNOTES-2026).
- **accounting archetype (bookkeeping, month-end close):** Mercor and Digits benchmarks and Digits Write MCP (ACCTODAY-AIBENCH-2026). A headline in the same trade outlet says BizBuyData will pay accounting firms for data to train AI (seen as a headline only; relevant to section 7216 and confidentiality if firms supply client data).
- **mid-tier firm platforms:** RSM's myRSM Tax ecosystem (announced 16 Jun 2025) automates manual tasks and data collection across entities and individuals but gives no outcomes (RSM-MYRSM-2025).

## 5. Sources

Refs match the landscape file where it already had the document (IRS-OPR-2026, AICPA-WERFEL-2026, AICPA-CART-2026, TAXCT-CLINCO-2026, BLACKORE-2026, BASIS-2026, PERPLEXITY-2026, TR-COCOUNSEL-2025, PWC-MEGNA-2025, RSM-MYRSM-2025, CNBC-HRB-2025, MULTIPLIER-2025, TEI-TAXTECH-2026, TR-FOP-2026, AICPA-TOPISSUES-2026, ACCTODAY-2026, AICPA-TAXSW-2026, SALA-TAXNOTES-2026, COLUMN-TAXCALCBENCH-2025). BLACKORE-SUMMIT-2026 is the landscape's conference key, used here for the Accounting Technology Lab podcast recap of that summit (landscape podcast key BLACKORE-POD). Dates are publication dates from page metadata or bylines. Where a month only is shown (podcast and GitHub pages), the page showed no full date.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| ACCTODAY-2026 | What does the new, AI-driven IRS mean for small accounting firms? (Allison Rinehimer, Ledger Labs) | Accounting Today | press | https://www.accountingtoday.com/opinion/what-does-the-new-ai-driven-irs-mean-for-small-accounting-firms | 2026-07-02 | full |
| ACCTODAY-AIBENCH-2026 | AI beats human accountants at monthly close, transaction categorization | Accounting Today | press | https://www.accountingtoday.com/news/ai-beats-human-accountants-at-monthly-close-transaction-categorization | 2026-10-16 | full |
| ACCTODAY-OPR-2026 | IRS rolls out AI guidelines for tax pros | Accounting Today | press | https://www.accountingtoday.com/news/irs-rolls-out-introductory-ai-guidelines-for-tax-practitioners | 2026-06-24 | full |
| AICPA-CART-2026 | AICPA, former IRS commissioner to lead initiative on AI in tax | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-former-irs-commissioner-to-lead-initiative-on-ai-in-tax/ | 2026-09-23 | full |
| AICPA-FEES-2026 | AICPA seeks IRS clarity on AI guidelines, CPA fees | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/news/2026/sep/aicpa-seeks-irs-clarity-on-ai-guidelines-cpa-fees/ | 2026-09-08 | full |
| AICPA-TAXSW-2026 | 2026 tax software survey | The Tax Adviser and Journal of Accountancy (AICPA) | survey | https://www.thetaxadviser.com/issues/2026/aug/2026-tax-software-survey/ | 2026-08-31 | full |
| AICPA-TOPISSUES-2026 | CPA Firm Top Issues Survey: firms focus on technology (629 respondents) | Journal of Accountancy (AICPA PCPS) | survey | https://www.journalofaccountancy.com/news/2026/jun/aicpa-top-issues-survey-firms-focus-on-technology-rises/ | 2026-06-23 | full |
| AICPA-WERFEL-2026 | A risk framework for AI use in tax administration and preparation | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/issues/2026/aug/a-risk-framework-for-ai-use-in-tax-administration-and-preparation/ | 2026-08 | full |
| BARMORE-OPR-2026 | The IRS Just Weighed In on AI | AI Lab for Accountants (Charlie Barmore | community | https://ai-lab-for-accountants.beehiiv.com/p/the-irs-just-weighed-in-on-ai | 2026-06-24 | full |
| BASIS-2026 | Basis Raises $100M to Deploy Automated Accounting Agents | Built In NYC | press | https://www.builtinnyc.com/articles/basis-raises-100m-series-b-20260226 | 2026-02-26 | full |
| BLACKORE-2026 | AI Tax Startup Black Ore Opens Platform to CPA Firms | Sovereign Magazine | press | https://www.sovereignmagazine.com/article/ai-tax-startup-black-ore-opens-platform-to-cpa-firms | 2026-04-29 | full |
| BLACKORE-SUMMIT-2026 | 2026 Black Ore AI Tax Summit - Accounting Technology Lab Podcast | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/2026-black-ore-ai-tax-summit-accounting-technology-lab-podcast-june-2026/ | 2026-06 | full |
| CNBC-HRB-2025 | ChatGPT for taxes? OpenAI and H&R Block have a plan for tax pros | CNBC (via NBC San Diego) | press | https://www.nbcsandiego.com/news/business/money-report/chatgpt-for-taxes-openai-and-hr-block-have-a-plan-for-tax-pros/3804532/?amp=1 | 2025-04-15 | full |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (arXiv 2507.16126) | Column Tax authors (arXiv) | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full |
| COLUMN-TCBREPO-2026 | TaxCalcBench repository README and TY2025 leaderboard | Column Tax (GitHub) | vendor | https://github.com/column-tax/tax-calc-bench | 2026-06 | full |
| CPAPA-AILIAB-2026 | AI Liability for Accounting Firms: Are You Covered? - Accounting Technology Lab Podcast | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/ai-liability-for-accounting-firms-are-you-covered-microsoft-google-openai-anthropic-accounting-technology-lab-podcast-oct-2026/ | 2026-10 | full |
| CPAPA-BLACKORE-2024 | Review of Black Ore Tax Autopilot - Accounting Technology Lab Podcast | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/review-of-black-ore-tax-autopilot-the-accounting-technology-lab-podcast-june-2024/ | 2024-06 | full |
| CPAPA-POSTEXT-2026 | The Post-Extension Window: How to Sequence Firm Automation Before Busy Season | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/10/16/the-post-extension-window-how-to-sequence-firm-automation-before-busy-season/191855/ | 2026-10-16 | full |
| CPAPA-TAXGPT-2026 | Why General AI is Not Suitable for Tax Research - Accounting Technology Lab Podcast | CPA Practice Advisor | podcast | https://www.cpapracticeadvisor.com/podcasts/why-general-ai-is-not-suitable-for-tax-research-accounting-technology-lab-podcast-june-2026/ | 2026-06 | full |
| HN-ASK-2026 | Ask HN: Why hasn't AI replaced Tax filing software | Hacker News | community | https://news.ycombinator.com/item?id=50004396 | 2026-10-08 | full |
| HN-TCB-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task (Hacker News thread) | Hacker News | community | https://news.ycombinator.com/item?id=45601230 | 2025-10-16 | full |
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| JOFA-OPR-2026 | IRS outlines AI risks, Circular 230 duties for tax practitioners | Journal of Accountancy | press | https://www.journalofaccountancy.com/news/2026/jun/irs-outlines-ai-risks-circular-230-duties-for-tax-practitioners/ | 2026-06-26 | full |
| JOFA-POLICY-2026 | Drafting an AI policy that actually works | Journal of Accountancy (Nicole L. Graham | press | https://www.journalofaccountancy.com/issues/2026/jul/drafting-an-ai-policy-that-actually-works/ | 2026-07-01 | full |
| JOFA-SMALLFIRM-2026 | Real-life ways small firms use AI | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/aug/real-life-ways-small-firms-use-ai/ | 2026-08-01 | full |
| LDS-CNBC-2026 | IRS AI Guidance Leaves Client Disclosure Question Open | Let's Data Science (summarising CNBC) | press | https://letsdatascience.com/news/irs-ai-guidance-leaves-client-disclosure-question-open-f5400ffe | 2026-08-04 | full |
| MULTIPLIER-2025 | Multiplier, founded by ex-Stripe exec, nabs $27.5M to fuel AI-powered accounting roll-ups | TechCrunch | press | https://techcrunch.com/2025/06/18/multiplier-founded-by-ex-stripe-exec-nabs-27-5m-to-fuel-ai-powered-accounting-roll-up | 2025-06-18 | full |
| NAEA-AI-2026 | NAEA Highlights Find a Tax Expert Directory as Taxpayers Navigate AI-Driven Filing Season | National Association of Enrolled Agents | professional-body | https://lite.aol.com/tech/story/0022/20260326/9679339.htm | 2026-03-26 | full |
| PERPLEXITY-2026 | Perplexity Launches AI Agent That Drafts Tax Returns | PYMNTS | press | https://www.pymnts.com/taxes/2026/perplexity-launches-ai-agent-that-drafts-tax-returns/ | 2026-04-06 | full |
| PWC-MEGNA-2025 | How PwC's tax team is using agentic AI (interview with Dom Megna) | CFO.com | firm | https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/ | 2025-06-06 | full |
| RSM-MYRSM-2025 | RSM Expands AI Commitment with Launch of myRSM Tax | RSM US | firm | https://rsmus.com/newsroom/2025/rsm-expands-ai-commitment-with-launch-of-myrsm-tax.html | 2025-06-16 | full |
| SALA-TAXNOTES-2026 | AI Won't Shrink Corporate Tax Teams Much. Here's Why. (Tax Notes State 121:189; abstract on TaxProf Blog) | Tax Notes / TaxProf Blog | academic | https://taxprofblog.aals.org/2026/07/20/ai-wont-shrink-corporate-tax-teams-much-heres-why/ | 2026-07-20 | full |
| TAXADVISER-CLIENTS-2026 | What today's clients expect from their CPA and how firms are responding | The Tax Adviser (interview with Bob Nolan | press | https://www.thetaxadviser.com/issues/2026/aug/what-todays-clients-expect-from-their-cpa-and-how-firms-are-responding/ | 2026-08-31 | full |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax (on Clinco v. Commissioner, T.C. Memo. 2026-16) | Journal of Accountancy | press | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 | full |
| TECHRADAR-TAXFIX-2025 | The rise of the AI accountant: Cheaper. Faster. Riskier? | TechRadar (written by Taxfix) | press | https://www.techradar.com/pro/the-rise-of-the-ai-accountant-cheaper-faster-riskier | 2025-10-29 | full |
| TEI-TAXTECH-2026 | 2026 TEI Tax Tech: the man behind the curtain | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| TR-CHEAP-2026 | Why cheap AI for tax work costs more than you think | Thomson Reuters Tax and Accounting | vendor | https://tax.thomsonreuters.com/blog/why-cheap-ai-for-tax-work-costs-more-than-you-think/ | 2026-10-07 | full |
| TR-COCOUNSEL-2025 | Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows | 2025-11-05 | full |
| TR-FOP-2026 | Future of Professionals Report 2026: Actionable insights for tax and audit leaders | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 | full |
| TR-R2R-2025 | Transforming Busy Season: Introducing Ready to Review | Thomson Reuters (Elizabeth Beastrom) | vendor | https://www.thomsonreuters.com/en-us/posts/innovation/transforming-busy-season-introducing-ready-to-review-thomson-reuters-agentic-ai-for-1040-preparation/ | 2025-12-15 | full |
| TR-TRUST7-2026 | Can you trust it? 7 questions to ask any platform that claims to handle your entire tax workflow | Thomson Reuters Tax and Accounting | vendor | https://tax.thomsonreuters.com/blog/can-you-trust-it-7-questions-to-ask-any-platform-that-claims-to-handle-your-entire-tax-workflow/ | 2026-10-14 | full |
| VERITO-DISCL-2026 | Do Tax Preparers Have to Disclose AI Use to Clients? | Verito (vendor blog) | vendor | https://verito.com/blog/ai-tax-preparer-disclosure-requirements/ | 2026-08-14 | full |

**Count:** 42 distinct sources, all `access: full` (opened and read; the episode pages for BLACKORE-SUMMIT-2026 and CPAPA-AILIAB-2026 gave show notes only, and TR-FOP-2026 and AICPA-TAXSW-2026 are partial because a report or table was gated or an image). By type: academic 2, community 3, conference 1, firm 2, podcast 4, press 16, professional-body 4, regulator 1, survey 3, vendor 6.

## 6. Gaps

- **Not reached:** Reddit (r/taxpros, TaxProTalk) returned a network-policy block and the r.jina.ai mirror was also blocked for Reddit; Going Concern returned 403; Winthrop's article on sections 7216 and 6713 was blocked by a firewall page; the AccountingWEB article "Accountants count the cost of clients' AI use" (3 Aug 2026) was seen only as a headline in a search extract. Hacker News was the only open practitioner-adjacent community source, and its commenters are mostly self-filers, not preparers.
- **Search budget:** web search stopped working partway (budget shared and used up). Not checked as a result: whether H&R Block's OpenAI tool was deployed in the 2026 season; the German case in which a Berlin chamber reportedly sued a tax-tech company over an "AI tax adviser" product (seen only in a search extract, so not used); ENGAGE 2026 and NATP Taxposium session recaps; Intuit, Drake and Wolters Kluwer product discourse beyond what the landscape file lists.
- **Gated or partial:** Black Ore summit transcript and speaker list (episode needs sign-in; a search extract named speakers from several large firms, which was not verified); the CNBC article of 4 Aug 2026 on AI disclosure (only secondary summaries read); the AICPA's own AI FAQs for federal tax practice (referred to in AICPA-FEES-2026); Blue J and CPA.com 2026 report and the Thomson Reuters State of Tax Professionals report (gated); the table of AI uses in the AICPA software survey (image); Bloomberg Tax pricing coverage (paywalled).
- **Quality evidence:** no error rate, override rate, review-time measurement, parallel-run result, inspection finding or enforcement case for AI-prepared individual or small-business returns. Customer figures are one partner's estimate (about an hour per simple 1040) and company statements. TaxCalcBench is run by a vendor and tests only the calculation step. The Mercor and Digits studies are vendor-run and about month-end close and categorisation, not tax.
- **Modules not covered by the discourse found:** trusts and estates (1041) and UK self-assessment preparer practice (beyond one Taxfix op-ed and survey) had almost no practitioner discourse in the sources read; 1120-S and 1065 discourse is mostly the Basis demonstration and a forecast.
- **Conflicts and cautions:**
  - Werfel's framework: the landscape file says it was published in September 2026 per the CART release ("earlier this month"); the Tax Adviser URL and page timestamp place it in the August 2026 issue (page time 2026-08-31). It is dated 2026-08 here.
  - Unapproved AI use: the landscape cites 35 percent; a Thomson Reuters blog says 34 percent (TR-CHEAP-2026) and the Thomson Reuters page says "more than one-third" (TR-FOP-2026). The page wording is used.
  - The Accounting Today article on the AI-driven IRS (ACCTODAY-2026) is an opinion piece by a staff member of an outsourced-accounting provider; its claims about IRM 10.24.1 and TIGTA project counts were not checked against primary documents and are not used as facts here.
  - Black Ore's "40 percent of the 20 largest firms" and Basis's "30 percent of the 25 largest" are company claims; only one Black Ore customer (Maxwell Locke and Ritter) is named.
  - The landscape records OPR Alert 2026-19 as read in its opening sections only; the full alert was read here.
  - The 2024 Black Ore podcast is more than 12-18 months old and used as a foundation for how practitioners think about complexity routing and parallel runs.
