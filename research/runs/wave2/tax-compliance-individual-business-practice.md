# Tax / compliance-individual-business: practice angle

- **Archetype:** tax
- **Module:** compliance-individual-business (1040, 1041, 1065, 1120-S and UK self-assessment by CPA firms and preparers)
- **Angle:** practice (what firms and vendors actually deploy)
- **Prepared:** 2026-10-17 (wave 2)
- **Method:** Sources were opened with `curl`, with the `r.jina.ai` text mirror where a site blocked `curl`. The brief's source leads came from `landscape-tax.md`. Each source is marked `access: full` (opened and read) or `access: search-only`. All web searches in this run were used up. The last use-case sources were found by following links from pages already read.

---

## 1. Summary

- **Vendors announced many agentic preparers in the 2025-26 season.** The named products are Thomson Reuters Ready to Review, Black Ore Tax Autopilot, Basis, Accrual, TaxGPT, Juno, CCH Axcess Scan, Canopy Smart Intake and Perplexity Computer for Taxes. Most outcome figures are vendor-published testimonials or vendor claims. No independent measurement of error rates, override rates or parallel runs for any commercial preparer was found.
- **The one independent test is old and covers a different task.** TaxCalcBench (July 2025) tested frontier models on calculating federal returns with no tax engine. It is not a test of agent-plus-engine products (COLUMN-TAXCALCBENCH-2025).
- **The best practitioner evidence is a candid buyer's evaluation.** WCG CPAs & Advisors (about 4,500 1040s in 2026, K-1-heavy) tested five AI preparation vendors and declined to commit for the 2026 season (WCG-NOTREADY-2026, 2026-07-24).
  - Its objections: no vendor completes a return inside the tax software the firm already uses; K-1 and consolidated-1099 coverage is missing or on a roadmap; proprietary platforms risk a restart when the AI cannot finish; and per-return pricing is high against a SurePrep baseline.
  - WCG plans an "AI Tax Prep Pod" from November 2026 and is using AI now for narratives, quoting and plan comparisons.
- **The strongest production use found is retail preparation at H&R Block.** On its 11 Aug 2026 call, H&R Block described AI for manual data entry, automated prior-year review ("Second Look") and the "Sidekick" preparer assistant. It gave no productivity figures for these (HRB-Q4CALL-2026).
- **The work is changing from preparing returns to reviewing prepared returns.**
  - Vendors describe "start at review" workflows.
  - PwC describes one reviewer replacing three people who previously huddled on K-1 footnotes. Reviewers see a confidence level and give a reason when they override (PWC-MEGNA-2025).
  - No source publishes override rates.
  - CPA Trendlines teaser research in April 2026 reported fewer tax returns produced, rising salaries and flat-to-down headcount. That is a counter-signal to claimed efficiency (CPATL-SEASON-2026, gated).
- **Governance is "existing duties apply".** The IRS Office of Professional Responsibility alert 2026-19 (24 Jun 2026) ties AI use to Circular 230 §§10.22, 10.27(a), 10.35, 10.36 and 10.37 and to IRC §§6713 and 7216 (IRS-OPR-2026). The UK PCRT bodies (19 Jan 2026) and the Australian TPB (22 Jul 2026) say the same. No source read gives AI-specific §7216 guidance.
- **Counts:** 17 use cases (A: 1, B: 9, C: 7, D: 0) and 53 sources. The A entry rests on one named-firm testimonial and is not independent.

---

## 2. Use cases

```yaml
- id: tax-compliance-individual-business-01
  title: Agent drafts a simple 1040 from source documents and the prior-year return for CPA review
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, document-production]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Preparing even simple 1040s means sorting source documents, keying data and building the return by hand, which crowds out higher-value work in busy season."
  solution: "Thomson Reuters' Ready to Review (built on the CoCounsel Tax, Audit and Accounting platform) uses agents to process source documents and prior-year returns, extract and categorise data and generate returns ready for professional review. The product page says the draft includes verification links back to source documents and diagnostics; the client portal, e-file and signature steps stay as before."
  outcomes:
    - lever: speed
      description: "A partner at CLH CPAs and Consultants (Indiana), which tried the product, said it reduces return preparation time on each simple 1040 by about an hour."
      figure: "approximately 1 hour per simple 1040"
      measures: "reduction in return preparation time on each simple 1040, per the CLH partner quoted in the vendor release; no method, sample or baseline published"
      provenance: vendor-published
      source_ref: TR-COCOUNSEL-2025
  prerequisites:
    - "Source documents and the prior-year return uploaded to CoCounsel Tax; document intake process defined by the firm"
    - "A client portal for review and signature, and the firm's usual e-file process"
  risks_and_guardrails:
    - "WCG reported that at its 2026 evaluation Ready to Review did not handle K-1s or consolidated 1099 brokerage statements, and said both were on the vendor's roadmap for November 2026 (WCG's account, not confirmed by Thomson Reuters)."
    - "WCG noted the product works inside Thomson Reuters' own environment, which it saw as a structural problem for firms on other tax engines."
    - "The scope in the product FAQ is a simple 1040 draft."
  human_checkpoints:
    - "Professional review of the agent-prepared draft, diagnostics and source links before delivery"
  role_evolution: "The vendor positions staff time shifting from data entry and document sorting to review and advisory work. No firm-reported role changes were found."
  evidence_grade: B
  sources:
    - { ref: TR-COCOUNSEL-2025, title: "Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows", publisher: Thomson Reuters, type: vendor, url: "https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows", date: 2025-11-05, access: full, locator: "section 'Transforming Tax Preparation with Agentic AI' (CLH quote); availability list (early adopter program; general availability 'in December 2025')" }
    - { ref: TR-RTR-2026, title: "Complete tax returns faster with Ready to Review (product page and FAQ)", publisher: Thomson Reuters, type: vendor, url: "https://tax.thomsonreuters.com/en/products/ready-to-review", date: 2026-10-17, access: full, locator: "FAQ answers on workflow, verification and diagnostics (page is undated; date is retrieval date)" }
    - { ref: WCG-NOTREADY-2026, title: "AI Tax Prep in 2026: Not Quite There Yet", publisher: WCG CPAs & Advisors, type: firm, url: "https://wcginc.com/blog/ai-tax-prep-in-2026-not-quite-there-yet/", date: 2026-07-24, access: full, locator: "section 'Thomson Reuters Ready to Review'" }
  last_reviewed: 2026-10-17
  notes: "General availability was announced for December 2025 in the release (future tense). No source confirms the actual general-availability date, so maturity stays piloting. The CLH figure is a partner's estimate in a vendor release."

- id: tax-compliance-individual-business-02
  title: End-to-end agent prepares complex, K-1-heavy returns with workpapers for CPA sign-off
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Complex returns (many K-1s, brokerage statements, multi-state) take days of preparer and reviewer time; firms are short of staff in busy season."
  solution: "Black Ore's Tax Autopilot ingests W-2s, 1099s, K-1s and brokerage statements, classifies and extracts the data, applies federal and state logic, builds workpapers and routes the return into the firm's tax software for human sign-off. Basis describes agents that gather client data, build workpapers and run quality controls so that 'staff investigate exceptions, managers review'. Accrual describes complex individual, trust and partnership returns 'prepared end to end'."
  outcomes:
    - lever: capacity
      description: "A partner at Boulay says returns with 60 or 70-plus K-1s that could take more than 100 preparation hours are now down to maybe 15 or 20 hours (Basis tax page testimonial; attribution to Kevin Elli, Partner, Boulay, from the page's structured data on the Basis home page)."
      figure: "from more than 100 hours to about 15-20 hours per return with 60-70+ K-1s"
      measures: "preparation hours on returns with 60 or 70-plus K-1s, as stated by the Boulay partner; no method, sample size or return form stated"
      provenance: vendor-published
      source_ref: BASIS-TAX-2026
    - lever: speed
      description: "Black Ore says Tax Autopilot achieved accuracy above 99 percent across tens of thousands of returns during a two-year pilot and time savings of up to 98 percent on complex filings."
      figure: ">99% accuracy; up to 98% time savings"
      measures: "vendor-stated accuracy 'across tens of thousands of returns' in the pilot and time savings 'on complex filings'; definition of accuracy and baseline not published"
      provenance: vendor-published
      source_ref: BLACKORE-2026
    - lever: speed
      description: "Kyle Parks of Maxwell Locke & Ritter is quoted saying a high-net-worth return could take several days to prepare and is now ready for review in minutes."
      figure: "from several days to minutes (one high-net-worth return type)"
      measures: "time to a review-ready high-net-worth return, per a customer quote in trade coverage of the launch; no sample or method"
      provenance: vendor-published
      source_ref: MYCPE-BLACKORE-2026
  prerequisites:
    - "Firm tax software integration (Black Ore routes into the firm's software; Accrual currently integrates with CCH Axcess; WCG says Black Ore exports mapped inputs into Lacerte)"
    - "Per-return or per-page pricing accepted: WCG reports Black Ore's pricing as $100 to $150 per return on average, built on $1 per scanned page and $3 per K-1 page, and estimated $200 to $250 for its own mix (WCG's account)"
    - "Firm complexity matrix and review model (Accrual says it asks firms for a complexity matrix and prices on engagement fees)"
  risks_and_guardrails:
    - "WCG found that the host tax software still re-runs its own calculations and diagnostics, so pre-preparation work is rechecked and the firm still handles diagnostics, e-file setup, Form 8879 and delivery (WCG's assessment of Black Ore)."
    - "Black Ore told Accounting Today that complex returns are about 98% touchless and that a CPA must attest to the return and resolve edge cases. Some firm leaders worried that returns prepared at a higher level of abstraction might differ from prior-year returns and create audit risk in the transition year."
    - "No independent audit of the accuracy or time claims was found."
    - "Black Ore states SOC 2 Type II certification; Basis states it does not train models on client data and keeps client data on US infrastructure (vendor statements)."
  human_checkpoints:
    - "CPA review and sign-off before the return goes to the client and the IRS"
    - "CPA answers questions the system cannot resolve from documents (for example partnership ambiguities)"
  role_evolution: "Black Ore says the platform is designed to compress the functions of admin, junior staff, senior staff and reviewers into one agentic workflow, and it added seniors' tie-outs, downloadable binders and manager reviewer workflows over time. Basis positions staff at exception investigation and managers at review. WCG says Black Ore 'replaces the first-level preparer, not the last mile'."
  evidence_grade: A
  sources:
    - { ref: BASIS-TAX-2026, title: "Basis for tax (solutions page)", publisher: Basis, type: vendor, url: "https://www.getbasis.ai/solutions/tax", date: 2026-10-17, access: full, locator: "section 'Automate the first pass on tax compliance' and customer quotes (page is undated; date is retrieval date)" }
    - { ref: BASIS-HOME-2026, title: "Basis home page (customer reviews in structured data)", publisher: Basis, type: vendor, url: "https://www.getbasis.ai/", date: 2026-10-17, access: full, locator: "JSON-LD Review objects (author Kevin Elli, Partner, Boulay)" }
    - { ref: BLACKORE-2026, title: "AI Tax Startup Black Ore Opens Platform to CPA Firms", publisher: Sovereign Magazine, type: press, url: "https://www.sovereignmagazine.com/article/ai-tax-startup-black-ore-opens-platform-to-cpa-firms", date: 2026-04-29, access: full, locator: "paragraphs 2-4 (pilot size, product description, accuracy and time-saving claims)" }
    - { ref: ACCTODAY-BLACKORE-2026, title: "Black Ore's Tax Autopilot now generally available", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/black-ores-tax-autopilot-now-generally-available", date: 2026-04-29, access: full, locator: "CEO statements on touchless rates and CPA attestation; paragraph on compressing preparer functions and prior-year delta concern" }
    - { ref: WCG-NOTREADY-2026, title: "AI Tax Prep in 2026: Not Quite There Yet", publisher: WCG CPAs & Advisors, type: firm, url: "https://wcginc.com/blog/ai-tax-prep-in-2026-not-quite-there-yet/", date: 2026-07-24, access: full, locator: "Black Ore section (Lacerte handoff, pricing)" }
    - { ref: MYCPE-BLACKORE-2026, title: "Can Black Ore's Tax Autopilot Fix the CPA Labor Shortage?", publisher: my-cpe, type: press, url: "https://my-cpe.com/insights/news-and-insights/technology/can-black-ore-tax-autopilot-fix-the-cpa-labor-shortage", date: 2026-05-04, access: full, locator: "section on early-user numbers (cost reduction up to 80%) and the Maxwell Locke & Ritter quote" }
    - { ref: ACCRUAL-HOME-2026, title: "Accrual home page", publisher: Accrual, type: vendor, url: "https://www.accrual.com/", date: 2026-10-17, access: full, locator: "'Complex individual, trust, and partnership returns, prepared end to end' (page undated)" }
    - { ref: ACCRUAL-LAUNCH-2026, title: "Tax platform Accrual launches with AI automation support for all forms", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/tax-platform-accrual-launches-with-ai-automation-support-for-all-forms", date: 2026-02-05, access: full, locator: "paragraphs on complexity-matrix pricing and CCH Axcess integration" }
  last_reviewed: 2026-10-17
  notes: "Graded A on the strength of one named-firm, quantified, before-and-after statement (Boulay). It is a vendor-published testimonial, not an independent measurement, and the return form is not stated. Black Ore's pilot lists 75 firms including 40% of the 20 largest CPA firms by revenue (company claim). Maxwell Locke & Ritter is named as a customer in the launch coverage. Black Ore's own site claims review time cut by over 50% (BLACKORE-SITE-2026, vendor claim). Aiwyn, a practice-management vendor, was reported to be recruiting 100 firms for a 1040 pilot in the 2026 season (BLACKORE-2026)."

- id: tax-compliance-individual-business-03
  title: Source-document classification, extraction and K-1 mapping with exception-only review
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing]
  pattern: intake-triage
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "K-1 packages, supplemental statements and multi-tier partnerships defeat template OCR and manual keying, and mapping footnote items to tax treatments used to need group review."
  solution: "CCH Axcess Scan (Wolters Kluwer) classifies and extracts W-2s, 1099s, brokerage statements and K-1s and 'surfaces only exceptions for review'. PwC says agents trained on how to treat K-1 footnote items assess each item, state a confidence level and flag it for a reviewer, who gives a reason when overriding so the agent can learn. Intuit's ProConnect describes AI data import with side-by-side confirmation of each figure against the source."
  outcomes:
    - lever: speed
      description: "A named ProConnect user firm (Kulangy CPA, LLC) says the SmartReturn import-and-review workflow lets it complete returns in half the time."
      figure: "returns completed in half the time"
      measures: "relative time to complete returns, per a customer quote on the vendor page; baseline and sample not given"
      provenance: vendor-published
      source_ref: INTUIT-PROCONNECTAI-2026
    - lever: quality
      description: "Wolters Kluwer says K-1 extraction delivers on average 97.5% overall accuracy."
      figure: "97.5% average overall accuracy"
      measures: "vendor statement of average overall accuracy of automated K-1 extraction; test set, unit (field or document) and method not stated"
      provenance: vendor-published
      source_ref: WK-AXCESSSCAN-2026
    - lever: capacity
      description: "PwC says one person now reviews where three people used to gather to decide how to treat an unfamiliar K-1 footnote. No rates or counts are published."
      figure: "none published"
      measures: "qualitative interview statement: one reviewer instead of three people gathering to decide"
      provenance: self-reported
      source_ref: PWC-MEGNA-2025
  prerequisites:
    - "Historical treatment data and guides to train the agents (PwC trained agents on historical data and keeps retraining on new data)"
    - "A tool-management layer for agents (PwC's Agent OS) and reviewers who record override reasons"
    - "For Scan: the CCH Axcess platform (pushes extracted data into CCH Axcess Tax)"
  risks_and_guardrails:
    - "PwC says confidence rarely reaches 100% and reviewers remain in the loop; 'it's not a complete handoff'."
    - "For simpler diagnostics PwC says fewer review layers may be needed; complex outputs such as tax calculations keep multi-eye review."
    - "WCG's evaluation judged that K-1 and consolidated-1099 coverage is a minimum bar for any vendor serving complex individual returns."
  human_checkpoints:
    - "Reviewer inspects flagged items and overrides low-confidence mappings with a recorded reason"
    - "Upstream validation of K-1 data before it flows to the return (K-1 Manager)"
  role_evolution: "Preparers and staff move from keying and interpreting footnotes to exception review. PwC says its reviewers' override explanations train the agents."
  evidence_grade: B
  sources:
    - { ref: PWC-MEGNA-2025, title: "How PwC's tax team is using agentic AI", publisher: CFO Dive (Informa TechTarget), type: press, url: "https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/", date: 2025-06-06, access: full, locator: "answer to first question (K-1 mapping, confidence and override loop); answers on Agent OS and review layers" }
    - { ref: WK-AXCESSSCAN-2026, title: "CCH Axcess Scan", publisher: Wolters Kluwer, type: vendor, url: "https://www.wolterskluwer.com/en/solutions/cch-axcess/scan", date: 2026-10-17, access: full, locator: "sections on complex K-1 extraction ('97.5% overall accuracy') and FAQ (page undated; read via r.jina.ai mirror)" }
    - { ref: INTUIT-PROCONNECTAI-2026, title: "AI-Powered Tax Prep Tools (ProConnect)", publisher: Intuit, type: vendor, url: "https://accountants.intuit.com/tax-software/tax-online/ai-features/", date: 2026-10-17, access: full, locator: "SmartReturn and 'Intelligent data import' blocks with customer quotes (page undated)" }
  last_reviewed: 2026-10-17
  notes: "PwC's K-1 example is in its asset and wealth management work, so it is an adjacent setting to individual and small-business returns; the grade is capped at B for that reason. The Intuit and Wolters Kluwer figures are undated vendor-page claims."

- id: tax-compliance-individual-business-04
  title: AI-prefilled client organizers, tailored document-request lists and automated chasing
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [client-interaction, coordination-scheduling]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Collecting information and documents from clients means repeated emails, missed files and late-arriving documents that disrupt preparation."
  solution: "Canopy's Smart Intake offers AI-prefilled questionnaires and organizers that clients confirm or change, custom document request lists, and AI renaming and classification of files. Basis says its agents read the prior-year return, organise documents, surface data gaps and contact clients to resolve them. ApariPro (UK) describes automated client requests and reminders."
  outcomes:
    - lever: speed
      description: "Canopy says that in tax preparation scenarios firms can save as much as 20 minutes per client."
      figure: "as much as 20 minutes per client"
      measures: "vendor-stated maximum time saved per client in tax preparation scenarios; method not stated"
      provenance: vendor-published
      source_ref: CANOPY-SMARTINTAKE-2025
  prerequisites:
    - "Client data already stored in the practice-management system (Canopy's prefill draws on it)"
    - "Firm-defined naming conventions for classification"
  risks_and_guardrails:
    - "Prefilled answers need client confirmation; Canopy's design has the client confirm or change AI suggestions."
    - "Client data goes to a vendor platform, so §7216 and firm confidentiality policies apply (see module notes)."
  human_checkpoints:
    - "Client confirms or edits prefilled answers"
    - "Staff review request lists and open items"
  role_evolution: "Admin and preparer time on chasing clients and sorting files falls; no firm-reported role changes were found."
  evidence_grade: C
  sources:
    - { ref: CANOPY-SMARTINTAKE-2025, title: "Canopy Unveils Native AI Powered Smart Intake Capability to Eliminate Client Friction", publisher: Canopy (press release via Silicon UK), type: vendor, url: "https://www.silicon.co.uk/press-release/canopy-unveils-native-ai-powered-smart-intake-capability-to-eliminate-client-friction", date: 2025-07-22, access: full, locator: "quote from the VP of Product; 'Key capabilities available now' list" }
    - { ref: BASIS-TAX-2026, title: "Basis for tax (solutions page)", publisher: Basis, type: vendor, url: "https://www.getbasis.ai/solutions/tax", date: 2026-10-17, access: full, locator: "feature list: agents read prior-year return, surface data gaps, reach out to clients" }
    - { ref: APARIPRO-2026, title: "ApariPro: AI powered tax preparation for accountancy firms", publisher: ApariPro, type: vendor, url: "https://www.aparipro.com/", date: 2026-06-17, access: full, locator: "comparison table 'Traditional workflow' vs 'With ApariPro' (date is the page's modified time)" }
  last_reviewed: 2026-10-17
  notes: "No named customer using Smart Intake was found. WCG uses Canopy as its workflow software (WCG-7216-2026) but does not say it uses Smart Intake. Further Canopy releases (Sep and Oct 2025, AI document requests and engagements) were seen only as search-result titles and were not opened (BusinessWire returned 403)."

- id: tax-compliance-individual-business-05
  title: Retail preparer office replaces manual data entry with AI
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing]
  pattern: bulk-transformation
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: "Preparers in assisted-tax offices spend much of an appointment collecting and entering information, leaving less time for advice."
  solution: "H&R Block management said the company is 'transforming how work gets done inside our offices by automating away the mechanical aspects of tax prep', from using AI to eliminate manual data entry to automating the initial review of prior-year returns. This supports an advice-focused office model that was run in pilot offices and will expand to a full designated market area for tax season 27."
  outcomes:
    - lever: experience
      description: "For the advice-focused pilot-office model (which management says technology enables), H&R Block reported higher client satisfaction, stronger belief in its expertise and value, and more engagement beyond tax season. No figures were given for these pilot results."
      figure: "none published"
      measures: "qualitative management statement about pilot offices; no counts or rates"
      provenance: self-reported
      source_ref: HRB-Q4CALL-2026
  prerequisites:
    - "Technology, talent and workflows to be refined in the larger market test (management says this is the purpose of the tax season 27 expansion)"
  risks_and_guardrails:
    - "Management says AI alone is not sufficient for complex clients who seek confidence, judgment and accountability."
  human_checkpoints:
    - "Tax pros remain responsible for the returns and the client guidance"
  role_evolution: "Management says tax pros spend less time collecting and entering information and more on guidance, planning and advice; field leadership is also being reshaped toward year-round development of associates."
  evidence_grade: B
  sources:
    - { ref: HRB-Q4CALL-2026, title: "H&R Block Q4 fiscal 2026 earnings call transcript", publisher: H&R Block (transcript via earningswhispers.com, read via r.jina.ai mirror), type: firm, url: "https://earningswhispers.com/transcript/HRB/Q42026", date: 2026-08-11, access: full, locator: "management prepared remarks on pilot offices and 'automating away the mechanical aspects'" }
  last_reviewed: 2026-10-17
  notes: "The transcript is a third-party copy of the company call dated 11 Aug 2026. H&R Block's fiscal year ends 30 June. Management also reported a 200 basis point conversion improvement and a 190 basis point retention gain in the season but did not attribute them to this AI change."

- id: tax-compliance-individual-business-06
  title: Automated look-back review of prior-year returns for missed opportunities ("Second Look")
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [review-assurance, client-interaction]
  pattern: full-population-testing
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Second Look, a service for new clients that reviews their last three years of returns for missed opportunities, was manual, so tax pros rarely offered it to new clients."
  solution: "In an analyst Q&A answer, management said that over about 18 months H&R Block automated Second Look using newer AI capabilities, so a much higher share of new assisted clients opt in. The stated goal is for every new assisted client to get it."
  outcomes:
    - lever: growth
      description: "New clients who received Second Look returned at a rate more than 600 basis points higher than those that did not. The comparison is for the Second Look service, not for the AI automation alone, and is not a controlled comparison."
      figure: "more than 600 basis points higher return rate"
      measures: "return rate (retention) of new clients who received Second Look versus new clients who did not, in the 2026 season, per management"
      provenance: self-reported
      source_ref: HRB-Q4CALL-2026
  prerequisites:
    - "Access to the client's prior three years of returns"
    - "Newer AI capabilities (not named in the transcript)"
  risks_and_guardrails:
    - "Management declined to give opt-in figures; the share of new clients receiving Second Look is only described as close to the goal."
  human_checkpoints:
    - "Tax pros focus on the returns with the greatest opportunity (management's wording about the expanded Second Look)"
  role_evolution: "Tax pros no longer carry the manual work of look-back reviews and can concentrate on the highest-opportunity returns."
  evidence_grade: B
  sources:
    - { ref: HRB-Q4CALL-2026, title: "H&R Block Q4 fiscal 2026 earnings call transcript", publisher: H&R Block (transcript via earningswhispers.com), type: firm, url: "https://earningswhispers.com/transcript/HRB/Q42026", date: 2026-08-11, access: full, locator: "prepared remarks on Second Look retention; analyst Q&A answer on automating Second Look" }
  last_reviewed: 2026-10-17
  notes: "The 600 basis point figure measures an existing service's retention link and is shown for context. The AI automation's own effect is not measured in any published figure."

- id: tax-compliance-individual-business-07
  title: Preparer-facing AI assistant for complex client questions and code changes
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [expert-judgment, research-synthesis]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Retail tax pros must stay current on tax code changes and answer unusual client questions during appointments."
  solution: "In April 2025 H&R Block and OpenAI said they were developing a generative AI tool for H&R Block tax pros, powered by vetted data from the Tax Institute, with an initial phase later in 2025 and large-scale deployment ahead of the 2026 season. On the August 2026 call management described 'Sidekick, our AI TaxPro assistant' as having strong adoption across offices."
  outcomes:
    - lever: quality
      description: "Management said Sidekick 'marched across our offices and saw strong adoption throughout the season' and also said it helped navigate complex tax questions more efficiently. No usage counts or accuracy figures were published."
      figure: "none published"
      measures: "qualitative adoption statement; no counts"
      provenance: self-reported
      source_ref: HRB-Q4CALL-2026
  prerequisites:
    - "A curated expert content base (H&R Block's Tax Institute)"
  risks_and_guardrails:
    - "OpenAI's chief economist said AI works best as a force multiplier for human expertise rather than a replacement (CNBC, 2025)."
  human_checkpoints:
    - "The tax pro decides how to answer the client; the assistant supports the pro"
  role_evolution: "Intended to let tax pros answer harder questions faster; management frames the tax pro's value as judgment and advice."
  evidence_grade: B
  sources:
    - { ref: CNBC-HRB-2025, title: "ChatGPT for taxes? OpenAI and H&R Block have a plan for tax pros", publisher: CNBC via NBC 7 San Diego, type: press, url: "https://www.nbcsandiego.com/news/business/money-report/chatgpt-for-taxes-openai-and-hr-block-have-a-plan-for-tax-pros/3804532/?amp=1", date: 2025-04-15, access: full, locator: "paragraphs on the project, the Tax Institute data and the 2026 season timing" }
    - { ref: HRB-Q4CALL-2026, title: "H&R Block Q4 fiscal 2026 earnings call transcript", publisher: H&R Block (transcript via earningswhispers.com), type: firm, url: "https://earningswhispers.com/transcript/HRB/Q42026", date: 2026-08-11, access: full, locator: "CEO prepared remarks: 'Sidekick, our AI TaxPro assistant'" }
  last_reviewed: 2026-10-17
  notes: "The transcript read does not say that Sidekick is the tool built with OpenAI. A search summary of H&R Block earnings commentary said so, but that item was not opened, so the link is unconfirmed. The research-assistant side of this belongs to the research-advisory module."

- id: tax-compliance-individual-business-08
  title: AI-assisted return review with source tie-out, diagnostics and prior-year variance lists
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [review-assurance]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: "Reviewers must check figures against source documents and prior years, which takes senior time."
  solution: "Intuit's ProConnect runs an AI assistant against thousands of diagnostics. Basis ties every number in a draft return to its source, builds the prior-year variance list and flags exceptions. Accrual shows prepared values, open issues, changes and supporting work together, with every figure traced to its source. Thomson Reuters says agents verify inputs against source documents and provide two-year comparisons and categorised diagnostics."
  outcomes:
    - lever: quality
      description: "Seed Money Consulting says knowing the AI is checking its work against thousands of diagnostics gives it confidence. No error counts are published."
      figure: "none published"
      measures: "qualitative customer quote on the vendor page; no counts of errors caught"
      provenance: vendor-published
      source_ref: INTUIT-PROCONNECTAI-2026
  prerequisites:
    - "Source documents linked to the return so figures can be traced"
    - "Prior-year return data for variance analysis"
  risks_and_guardrails:
    - "WCG notes the host tax software repeats its own diagnostics, so pre-checks upstream may be duplicated (WCG's assessment of one vendor architecture)."
    - "OPR Alert 2026-19 says practitioners must carefully review everything AI produces; AI review does not replace the practitioner's own §10.22 due diligence."
  human_checkpoints:
    - "Reviewer inspects flagged exceptions and decides on treatments"
    - "Preparer or reviewer signs the return"
  role_evolution: "Reviewers start from a prepared draft with open issues surfaced, rather than from scratch. Accrual testimonials describe reviewing a workbook rather than building one."
  evidence_grade: B
  sources:
    - { ref: INTUIT-PROCONNECTAI-2026, title: "AI-Powered Tax Prep Tools (ProConnect)", publisher: Intuit, type: vendor, url: "https://accountants.intuit.com/tax-software/tax-online/ai-features/", date: 2026-10-17, access: full, locator: "'Diagnostics' block with Seed Money Consulting quote" }
    - { ref: BASIS-SMALL-2026, title: "Basis for small firms", publisher: Basis, type: vendor, url: "https://www.getbasis.ai/solutions/small-firms", date: 2026-10-17, access: full, locator: "example exchange: 'Upload the draft return and the supporting docs'" }
    - { ref: ACCRUAL-INDIV-2026, title: "Accrual: individual (1040, 1041) tax preparation", publisher: Accrual, type: vendor, url: "https://www.accrual.com/tax/individuals", date: 2026-10-17, access: full, locator: "'Start with the work that needs your judgment' and 'Every figure traced to its source'" }
    - { ref: TR-RTR-2026, title: "Ready to Review (product page and FAQ)", publisher: Thomson Reuters, type: vendor, url: "https://tax.thomsonreuters.com/en/products/ready-to-review", date: 2026-10-17, access: full, locator: "FAQ answer on verification, two-year comparisons and diagnostics" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "opening section; 'Section 10.22 - Due Diligence'" }
  last_reviewed: 2026-10-17
  notes: "Seed Money Consulting is the named firm on the Intuit diagnostics quote. Only qualitative statements exist; no source reports false-positive or miss rates for AI review."

- id: tax-compliance-individual-business-09
  title: Agent prepares partnership (1065) and trust (1041) returns, including K-1 allocations, for review
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, document-production]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Partnership and trust returns need trial-balance import, partner capital and allocations, depreciation, §199A and §163(j) calculations, basis tracking and K-1 tie-out, much of it built in spreadsheets."
  solution: "Accrual describes preparing 1041 work from the governing instrument through to each beneficiary's K-1, and partnership returns from trial balance import to partner K-1s, computing depreciation, §199A, §163(j), allocations and capital accounts deterministically and syncing workpapers to the firm's tax engine. Armanino is its named customer. Basis demonstrated an agent that autonomously completed a 1065 return."
  outcomes:
    - lever: speed
      description: "Quotes on Accrual's partnership page, presented under 'How Armanino prepares partnership returns on Accrual' but unattributed by person, say a workpaper that takes about three hours to prepare could potentially be set up in 10 or 15 minutes, and that the saving for an average preparer and reviewer could be four or five hours."
      figure: "about 3 hours down to a potential 10-15 minutes for workpaper setup; potential 4-5 hours saved"
      measures: "estimated preparation time for a partnership workpaper, in anonymous quotes using 'could potentially'; these are estimates, not measurements"
      provenance: vendor-published
      source_ref: ACCRUAL-PARTNER-2026
  prerequisites:
    - "Prior-year data, trial balance, fixed-asset records and partnership agreement in the engagement"
    - "An existing tax engine that stays authoritative (Accrual syncs approved work to it)"
  risks_and_guardrails:
    - "WCG says business-entity returns (S corporations, partnerships, C corporations) involve book-to-tax adjustments, allocations and depreciation decisions that still belong in experienced human hands, and begins AI preparation with individual 1040s."
    - "Accrual's CEO said the product does not automate 100% of the work."
  human_checkpoints:
    - "Review of the draft with open items and treatment decisions surfaced before anything commits"
    - "Approval of agent changes (Accrual shows and asks approval before applying changes)"
  role_evolution: "Accrual describes the shift as 'from building workpapers to reviewing them'; one quote says the preparer's role for a simple return would largely be dropping information into the system."
  evidence_grade: B
  sources:
    - { ref: ACCRUAL-PARTNER-2026, title: "Accrual: partnership returns", publisher: Accrual, type: vendor, url: "https://www.accrual.com/tax/partnerships", date: 2026-10-17, access: full, locator: "sections 'From trial balance to partner K-1s' and 'From building workpapers to reviewing them'" }
    - { ref: ACCRUAL-INDIV-2026, title: "Accrual: individual (1040, 1041) tax preparation", publisher: Accrual, type: vendor, url: "https://www.accrual.com/tax/individuals", date: 2026-10-17, access: full, locator: "section 'From governing instrument to beneficiary K-1'; 'From pilot to production in months' (Armanino)" }
    - { ref: BASIS-2026, title: "Basis raises $100M Series B (BuiltIn NYC)", publisher: Built In NYC, type: press, url: "https://www.builtinnyc.com/articles/basis-raises-100m-series-b-20260226", date: 2026-02-26, access: full, locator: "sentence on the agent that autonomously completed a 1065" }
    - { ref: WCG-PLAYBOOK-2026, title: "AI Tax Preparation and Automation: What It Means for You", publisher: WCG CPAs & Advisors, type: firm, url: "https://wcginc.com/blog/ai-tax-preparation-and-automation-what-it-means-for-you/", date: 2026-07-05, access: full, locator: "Key Takeaways: 'Business entity returns still require human judgment'" }
    - { ref: ACCRUAL-LAUNCH-2026, title: "Tax platform Accrual launches with AI automation support for all forms", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/tax-platform-accrual-launches-with-ai-automation-support-for-all-forms", date: 2026-02-05, access: full, locator: "paragraphs on K-1 focus, 'not 100%' automation and plans beyond individual returns" }
  last_reviewed: 2026-10-17
  notes: "Armanino's role is shown on Accrual's own pages (a partnership announcement dated 2026-02-18 is listed on Accrual's press page, but the release returned 403 and was not read). The Basis 1065 item is a demonstration, not a customer deployment. Accrual's CEO told Accounting Today that its AI is 100% accurate (his claim), which sits against WCG's view that no vendor is yet end-to-end."

- id: tax-compliance-individual-business-10
  title: Trial balance to tax workpapers for pass-through entity returns (account mapping, M-1 adjustments, fixed assets)
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, data-reporting]
  pattern: bulk-transformation
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: "Business returns (1120-S, 1065) start with mapping the client's trial balance to return lines and building book-to-tax and fixed-asset workpapers by hand."
  solution: "Basis's small-firm page shows agents mapping client accounts to the firm's chart with tax-return line references and flagging new or unmapped accounts, then drafting M-1 adjustment, fixed-asset roll-forward and tax trial balance workpapers with every figure cited to its source."
  outcomes:
    - lever: speed
      description: "A managing partner at Whitcomb & Sheridan LLP says the tool has probably saved 10 to 20 hours in a week and that a task taking two to three hours takes about 30 minutes. The quote is general and does not name this step."
      figure: "10-20 hours in a week; 2-3 hours down to about 30 minutes"
      measures: "managing partner's estimate of hours saved in one week and for one task, not specific to trial balance mapping"
      provenance: vendor-published
      source_ref: BASIS-SMALL-2026
  prerequisites:
    - "Trial balance and prior-year mapping uploaded; source documents attached"
    - "Firm chart of accounts and workpaper standards"
  risks_and_guardrails:
    - "WCG states business-entity work still needs experienced human judgment (see use case 09)."
  human_checkpoints:
    - "Staff review mapping exceptions and workpaper drafts"
  role_evolution: "Staff review mapped output instead of building mappings; no firm-reported role changes were found."
  evidence_grade: C
  sources:
    - { ref: BASIS-SMALL-2026, title: "Basis for small firms", publisher: Basis, type: vendor, url: "https://www.getbasis.ai/solutions/small-firms", date: 2026-10-17, access: full, locator: "example exchanges under 'Tax, client accounting, and everything in between'; Whitcomb & Sheridan quote" }
    - { ref: WCG-PLAYBOOK-2026, title: "AI Tax Preparation and Automation: What It Means for You", publisher: WCG CPAs & Advisors, type: firm, url: "https://wcginc.com/blog/ai-tax-preparation-and-automation-what-it-means-for-you/", date: 2026-07-05, access: full, locator: "Key Takeaways" }
  last_reviewed: 2026-10-17
  notes: "The workflow is shown as illustrative product examples; no named customer is tied to this specific step."

- id: tax-compliance-individual-business-11
  title: Agent operates inside the firm's existing tax software through the user interface
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "Pre-preparation tools push data into the tax engine, which then recalculates and runs its own diagnostics, so the firm still does the final steps by hand. WCG's stated target is an AI that works inside Lacerte, Axcess or UltraTax the way a human preparer does."
  solution: "TaxGPT's product page says each return can be assigned to a dedicated AI agent that logs into the firm's existing tax software (it names Axcess, UltraTax, Drake and ProConnect), documents every action with source citations, and leaves the firm's own software as the system of record. A trade-press summary describes the agent reading documents, logging details into tax software and running diagnostics."
  outcomes:
    - lever: speed
      description: "TaxGPT says firms see a 90% reduction in first-pass preparation time within 60 days, and that a 25-person firm preparing 5,000 returns per season unlocked 28% more capacity without hiring."
      figure: "90% reduction in first-pass prep time; 28% more capacity"
      measures: "vendor statement of 'first pass prep time' reduction and capacity gain for a 25-person firm preparing 5,000 returns; the firm is not named, and the baseline and method are not stated"
      provenance: vendor-published
      source_ref: TAXGPT-SITE-2026
  prerequisites:
    - "Credentials and permissions for the agent in the firm's tax software"
    - "Zero data retention or equivalent controls and a vendor security review"
  risks_and_guardrails:
    - "WCG tried a browser-based approach from one of the five vendors it evaluated (not named in the text retrieved) and found it not production-ready: it tied up the laptop and did not integrate with desktop email. WCG says UltraTax's integration capabilities make an agent manipulating it like a human unlikely."
    - "The trade-press summary notes the approach raises questions about reliability and the CPA's responsibility."
  human_checkpoints:
    - "CPA review and sign-off; the firm remains system of record"
  role_evolution: "The firm's preparers become reviewers of completed engine files; the agent is assigned work per return."
  evidence_grade: C
  sources:
    - { ref: TAXGPT-SITE-2026, title: "AI tax preparation (TaxGPT product page)", publisher: TaxGPT, type: vendor, url: "https://www.taxgpt.com/ai-tax-preparation", date: 2026-10-17, access: full, locator: "sections on dedicated AI agents, 'Lives behind your workflow' and the results panel (page undated)" }
    - { ref: MYCPE-TAXGPT-2026, title: "TaxGPT Launches Autonomous Tax Agent for Busy Season", publisher: my-cpe, type: press, url: "https://my-cpe.com/insights/news-and-insights/technology/taxgpt-launches-autonomous-tax-agent-for-busy-season", date: 2026-03-25, access: full, locator: "summary paragraph (article body is paywalled; only the summary was read)" }
    - { ref: WCG-NOTREADY-2026, title: "AI Tax Prep in 2026: Not Quite There Yet", publisher: WCG CPAs & Advisors, type: firm, url: "https://wcginc.com/blog/ai-tax-prep-in-2026-not-quite-there-yet/", date: 2026-07-24, access: full, locator: "sections on browser-based vendor, 'What WCG Actually Wants' and the UltraTax sidebar" }
  last_reviewed: 2026-10-17
  notes: "No TaxGPT customer is named in the sources read. The WCG post does not name TaxGPT; do not read WCG's criticism as aimed at TaxGPT."

- id: tax-compliance-individual-business-12
  title: Return-derived client narratives, engagement quotes and tax-plan comparisons in a zero-data-retention sandbox
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [document-production, client-interaction]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Firms want to use filed or prior-year returns for advisory work, but cannot paste client data into public AI tools."
  solution: "WCG says it will use a PII/SOC 2-compliant, zero-data-retention sandbox from a vendor to upload tax returns for client-facing narratives, engagement quoting, tax-plan comparisons, strategy recommendations and internal training. It bought a block of 500 returns at $44 each to get access. Intuit lists an AI Client Briefing for ProConnect users."
  outcomes:
    - lever: growth
      description: "none published. WCG describes this as a legitimate, high-value use at the current capability level and says its move toward advisory work is the goal."
      figure: "none published"
      measures: "none published"
      provenance: self-reported
      source_ref: WCG-NOTREADY-2026
  prerequisites:
    - "A sandbox with SOC 2 compliance and zero data retention"
    - "Prior-year returns available to upload"
  risks_and_guardrails:
    - "OPR Alert 2026-19 warns against uploading sensitive data to unsecured or public systems and says only secure, enterprise-approved AI should be used with client data."
    - "WCG notes AI spend raises its technology stack cost by about 25% (WCG-PLAYBOOK-2026)."
  human_checkpoints:
    - "Staff review narratives and recommendations before they reach clients"
  role_evolution: "WCG says it wants to move off compliance work and toward advisory, with fewer CPAs and tax professionals coming out of school."
  evidence_grade: C
  sources:
    - { ref: WCG-NOTREADY-2026, title: "AI Tax Prep in 2026: Not Quite There Yet", publisher: WCG CPAs & Advisors, type: firm, url: "https://wcginc.com/blog/ai-tax-prep-in-2026-not-quite-there-yet/", date: 2026-07-24, access: full, locator: "sections 'What WCG Actually Is Doing' and Juno" }
    - { ref: WCG-PLAYBOOK-2026, title: "AI Tax Preparation and Automation: What It Means for You", publisher: WCG CPAs & Advisors, type: firm, url: "https://wcginc.com/blog/ai-tax-preparation-and-automation-what-it-means-for-you/", date: 2026-07-05, access: full, locator: "section 'Let's Be Direct About What This Is'" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "item 6, IRC sections 6713 and 7216(a)" }
    - { ref: INTUIT-PROCONNECTAI-2026, title: "AI-Powered Tax Prep Tools (ProConnect)", publisher: Intuit, type: vendor, url: "https://accountants.intuit.com/tax-software/tax-online/ai-features/", date: 2026-10-17, access: full, locator: "resource list entry 'AI Client Briefing' (title only; page undated)" }
  last_reviewed: 2026-10-17
  notes: "Graded C rather than B because the WCG description is a stated plan with no results, and the sandbox vendor is identified only as the source of the Juno sandbox the post names. This is a first-person firm description."

- id: tax-compliance-individual-business-13
  title: AI-native roll-up acquires small tax practices and runs them on in-house AI
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, expert-judgment]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: managed-agent-runtime
  maturity: in-production
  problem: "Small tax practices carry high manual workloads and thin margins; venture-backed firms are betting the same AI can be applied to acquired practices."
  solution: "Multiplier (founded 2022) acquired Citrine International Tax, a 12-person boutique providing cross-border tax accounting, and applied AI tools it built to it; it aims to buy high-recurring-revenue service firms and expand beyond personal tax compliance to compete with the Big Four. Its investor says small firms are more open to changing processes than a firm with 200 accountants."
  outcomes:
    - lever: cost
      description: "TechCrunch reports that Multiplier's AI tools helped Citrine more than double its profit margins."
      figure: "profit margins more than doubled"
      measures: "profit margins of one acquired 12-person tax accounting boutique; the period, baseline and method are not given"
      provenance: self-reported
      source_ref: MULTIPLIER-2025
  prerequisites:
    - "Capital to acquire practices and AI tools built in-house"
    - "Leaders of the acquired firm willing to integrate and customise AI"
  risks_and_guardrails:
    - "One acquired boutique is the only data point; the figure is a margin claim reported by the press."
  human_checkpoints:
    - "Not described in the source"
  role_evolution: "The model removes manual work inside acquired practices; roles in acquired firms are not described."
  evidence_grade: B
  sources:
    - { ref: MULTIPLIER-2025, title: "Multiplier, founded by ex-Stripe exec, nabs $27.5M to fuel AI-powered accounting roll-ups", publisher: TechCrunch, type: press, url: "https://techcrunch.com/2025/06/18/multiplier-founded-by-ex-stripe-exec-nabs-27-5m-to-fuel-ai-powered-accounting-roll-up", date: 2025-06-18, access: full, locator: "paragraphs 3-4 and the Lightspeed partner quotes" }
  last_reviewed: 2026-10-17
  notes: "Capped at B: Citrine is a cross-border tax accounting boutique, which is adjacent to 1040 and small-business compliance, and the margin claim is unaudited. Other AI-native roll-ups (Accrual, Gelt, Skalar, Limetax) listed in the landscape file were not verified here."

- id: tax-compliance-individual-business-14
  title: Dedicated AI team, champion network or pod to design and govern AI-assisted preparation
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [coordination-scheduling, software-systems]
  pattern: other
  ladder: assist
  change_scope: model
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Tools are changing faster than firm processes; someone must test vendors, document practice and train staff, and governance must cover agents as well as chat tools."
  solution: "PwC reports a governance committee over how it builds and uses AI systems in tax, an Agent OS to manage which tools agents use, more than 3,200 AI champions across the firm (many in tax) and a My AI training programme. WCG says its AI Tax Prep Pod launches in November 2026 to design the workflow, test tools, document best practices and shape how AI-assisted preparation is used across the firm. Vendors hire accountants into product roles: Basis lists a 'Member of Accounting Staff' role (4-10 years in audit and tax at a top firm) that builds the product with engineers and a 'Deployed Intelligence' customer role."
  outcomes:
    - lever: capacity
      description: "PwC reports more than 350,000 training hours in the US firm and about 80% of its people having taken some AI training. These are enablement measures for the firm, not tax work outcomes."
      figure: ">3,200 AI champions; >350,000 training hours; about 80% trained"
      measures: "firm-wide counts reported in an interview: AI champions identified across the firm, training hours in the US firm, and share of people who took some AI training; the denominator for 80% is not stated beyond 'our people'"
      provenance: self-reported
      source_ref: PWC-MEGNA-2025
  prerequisites:
    - "Executive sponsorship, protected training time and a vendor-testing process"
    - "Governance: explainability, traceability and auditability principles (PwC's responsible AI toolkit)"
  risks_and_guardrails:
    - "OPR Alert 2026-19 ties Circular 230 §10.36 to firm procedures for AI: staff training, secure data handling, AI accuracy monitoring and vetting of third-party tools, all documented."
    - "Thomson Reuters' 2026 report article says more than one third of professionals admit to using unauthorised AI tools."
  human_checkpoints:
    - "Governance committee oversight; approved outputs are locked and changes controlled (PwC)"
  role_evolution: "New roles appear: AI champions, agent managers, accounting-trained product and deployment staff. CPA Trendlines (gated teaser) reports public accounting firms adding 3,930 accountant and auditor positions since 2021 against 12,250 sales representatives, 11,140 financial managers and 8,130 computer and information systems managers."
  evidence_grade: B
  sources:
    - { ref: PWC-MEGNA-2025, title: "How PwC's tax team is using agentic AI", publisher: CFO Dive (Informa TechTarget), type: press, url: "https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/", date: 2025-06-06, access: full, locator: "answers on governance, 'AI champions' and 'My AI' training" }
    - { ref: WCG-PLAYBOOK-2026, title: "AI Tax Preparation and Automation: What It Means for You", publisher: WCG CPAs & Advisors, type: firm, url: "https://wcginc.com/blog/ai-tax-preparation-and-automation-what-it-means-for-you/", date: 2026-07-05, access: full, locator: "Key Takeaways: AI Tax Prep Pod" }
    - { ref: BASIS-CAREERS-2026, title: "Careers at Basis: Member of Accounting Staff; Deployed Intelligence Strategist", publisher: Basis, type: job-posting, url: "https://www.getbasis.ai/careers/member-of-accounting-staff-bf7e34d6", date: 2026-10-17, access: full, locator: "'About the Team', 'What you'll bring'; second posting https://www.getbasis.ai/careers/deployed-intelligence-strategist-1a01e77c (postings undated; retrieval date shown)" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "item 4, Section 10.36" }
    - { ref: TR-FOP-2026, title: "What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now", publisher: Thomson Reuters Institute, type: survey, url: "https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026", date: 2026-07-21, access: full, locator: "'Universal priorities for firm leaders': govern the tools" }
    - { ref: CPATL-WORKFORCE-2026, title: "CPAs Not Wanted: Firms Build a New Workforce - without Accountants", publisher: CPA Trendlines, type: press, url: "https://cpatrendlines.com/2026/05/29/cpas-not-wanted-firms-build-a-new-workforce-without-accountants", date: 2026-05-29, access: full, locator: "opening paragraphs (the rest is behind a membership wall)" }
  last_reviewed: 2026-10-17
  notes: "Pattern is other: this is organisational enablement (team, champions, governance), not a work pattern. The PwC counts are firm-wide, not tax-specific, and come from a June 2025 interview. The WCG pod is a stated plan (launches November 2026). Graded B on the PwC interview and the WCG announcement together."

- id: tax-compliance-individual-business-15
  title: Taxpayer-facing general-purpose agent reviews uploaded documents and drafts a federal return
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, client-interaction]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: model
  runtime_class: personal-assistant
  maturity: announced
  problem: "Self-filers face forms and uncertainty; the same capability could compete with low-end preparers."
  solution: "Perplexity's Computer for Taxes reviews uploaded financial documents, asks follow-up questions, maps inputs to IRS forms and drafts a federal return. Tax knowledge is packaged as loadable modules updated independently of the model. It also says it can review a professionally prepared return and help filers form questions for their provider."
  outcomes:
    - lever: cost
      description: "none published for accuracy. Access requires a $17 per month Pro subscription."
      figure: "none published"
      measures: "none published"
      provenance: vendor-published
      source_ref: PERPLEXITY-2026
  prerequisites:
    - "A Pro subscription; uploaded documents"
  risks_and_guardrails:
    - "A TaxSlayer test of four AI chatbots reported by the New York Times, as repeated by PYMNTS, found the tools miscalculated the refund or amount owed by an average of more than $2,000 across eight fictional tax scenarios (secondary report; chatbots rather than this product)."
    - "TaxCalcBench found frontier models computed fewer than a third of simplified federal returns correctly without a tax engine (see module notes)."
  human_checkpoints:
    - "The filer reviews and files; no preparer sign-off in the described flow"
  role_evolution: "Not described. The product is aimed at filers, and the source frames it as a way to reduce the burden of self-filing."
  evidence_grade: C
  sources:
    - { ref: PERPLEXITY-2026, title: "Perplexity Launches AI Agent That Drafts Tax Returns", publisher: PYMNTS, type: press, url: "https://www.pymnts.com/taxes/2026/perplexity-launches-ai-agent-that-drafts-tax-returns/", date: 2026-04-06, access: full, locator: "paragraphs 2-5 and the paragraph on the TaxSlayer test" }
  last_reviewed: 2026-10-17
  notes: "Announced by Perplexity on 2 Apr 2026. Included because it affects the low-end preparer market that the module serves. The accuracy claims come from the company's own announcement, and no customer outcome was found."

- id: tax-compliance-individual-business-16
  title: UK self-assessment (SA100) and Making Tax Digital preparation with AI document processing
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [transaction-processing, client-interaction]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "UK firms chase clients for information, review documents manually and re-key data into tax software for SA100 and quarterly Making Tax Digital submissions."
  solution: "ApariPro says it automates client information collection, AI document processing (P60s and others), return population and submission, integrating with Wolters Kluwer's CCH iFirm so the team reviews rather than prepares. The vendor says the team stays in control of reviewing and approving all information before submission."
  outcomes:
    - lever: capacity
      description: "none published as figures. Anonymous testimonials say manual data entry and administrative effort fell; a savings calculator is offered on the site."
      figure: "none published"
      measures: "none published"
      provenance: vendor-published
      source_ref: APARIPRO-2026
  prerequisites:
    - "Integration with the firm's tax software (CCH iFirm is named)"
  risks_and_guardrails:
    - "The PCRT AI guidance (19 Jan 2026) says members remain responsible for work produced with AI, and says entering client data into a publicly available AI model without consent is likely to breach confidentiality."
  human_checkpoints:
    - "Team review and approval before submission"
  role_evolution: "Vendor positions staff at review and advisory ('Stop preparing tax returns. Start reviewing them')."
  evidence_grade: C
  sources:
    - { ref: APARIPRO-2026, title: "ApariPro: AI powered tax preparation for accountancy firms", publisher: ApariPro, type: vendor, url: "https://www.aparipro.com/", date: 2026-06-17, access: full, locator: "hero, workflow comparison table, FAQ" }
    - { ref: PCRT-AI-2026, title: "Professional bodies issue AI advice to members", publisher: Association of Taxation Technicians, type: professional-body, url: "https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members", date: 2026-01-19, access: full, locator: "announcement text on PCRT topical guidance" }
    - { ref: ICAEW-PCRT-2026, title: "Professional Conduct in Relation to Taxation bodies publish guidance on using AI in tax", publisher: ICAEW, type: professional-body, url: "https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax", date: 2026-01, access: full, locator: "summary of the 'Confidentiality' principle and 'responsible for any work they produce'" }
  last_reviewed: 2026-10-17
  notes: "The ApariPro page is undated; the date is the page's modified time. A search summary also referred to an IRIS UK anomaly-checking tool for personal tax returns; that was not opened and is not used here. The Wolters Kluwer partnership with ApariPro is shown on ApariPro's page only."

- id: tax-compliance-individual-business-17
  title: Teach-once practice routines run by a general agent (open-issue resolution, recurring notice sweeps)
  archetype: tax
  module: compliance-individual-business
  function: service-delivery
  work_types: [coordination-scheduling, transaction-processing]
  pattern: other
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: "Multi-source follow-up on a return (call notes, open issues, binders, signature requests) is done by hand across systems."
  solution: "Accrual's Arc (unveiled 9 Sep 2026) takes an objective, drafts a plan, asks clarifying questions, and after approval executes across the firm's systems. In the demo it read a Teams transcript to propose changes to a partnership return's open items, asked for approval, and updated the workpaper with an audit trail. Routines the practitioner teaches can be saved as replayable agents."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "none published"
      provenance: vendor-published
      source_ref: ACCRUAL-ARC-2026
  prerequisites:
    - "Connected firm systems and permissioned access to meeting transcripts and the engagement binder"
  risks_and_guardrails:
    - "In the demo the agent proposed changes and waited for approval before updating the workpaper; the vendor reports an audit trail of sources, tools and actions."
  human_checkpoints:
    - "Practitioner approves the plan and each proposed change"
  role_evolution: "The presenter describes moving from clicking buttons to reviewing the agent's work."
  evidence_grade: C
  sources:
    - { ref: ACCRUAL-ARC-2026, title: "Accrual launches Arc AI for accounting workflows", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/accrual-launches-arc-ai-can-learn-from-and-replicate-accounting-workflows", date: 2026-09-22, access: full, locator: "paragraphs on the three task types and the Clarity Partners PPC demonstration" }
  last_reviewed: 2026-10-17
  notes: "Pattern is other: a general agent harness that plans, asks for approval and executes multi-system tasks. The notice-sweep part belongs to the controversy module (see Routed). The demonstration used a theoretical client."
```

---

## 3. Module notes

### Processes and key steps (with work types)

1. Engagement setup: engagement letter, §7216 consent, client onboarding (`coordination-scheduling`, `document-production`).
2. Client organiser and document request (`client-interaction`; use case 04).
3. Document intake, classification and extraction of W-2s, 1099s, brokerage statements and K-1s (`transaction-processing`; use cases 03, 05).
4. Mapping and data entry into the tax engine (`transaction-processing`; use cases 01, 02, 11).
5. Preparation: workpapers, depreciation, basis, allocations, state returns (`transaction-processing`, `expert-judgment` for positions; use cases 02, 09, 10).
6. Diagnostics and layered review (`review-assurance`; use case 08).
7. Client delivery, Form 8879 e-file authorisation and e-filing (`transaction-processing`, `client-interaction`). WCG says these final steps still sit in the tax software (WCG-NOTREADY-2026).
8. Planning and advisory conversation built on the prepared return (`expert-judgment`, `client-interaction`; use case 12).
9. Notices after filing: routed (see section 4).

### Common pain points

- Busy-season volume and talent supply: The Sovereign article attributes about 300,000 net departures from the profession to the Bureau of Labor Statistics and a 17-year-low CPA exam candidate count to the AICPA; a 125-million-hour annual shortfall in US tax services is Black Ore's own figure, unattributed (BLACKORE-2026). WCG says the pipeline is thinning while the workload is not.
- K-1 complexity: WCG says K-1s and consolidated 1099s are central to complex individual returns; one product that did not handle them was "disqualifying" for WCG (WCG-NOTREADY-2026).
- Baseline before LLM agents: scan-and-push extraction into the tax engine (SurePrep with UltraTax CS) is the established workflow; a Thomson Reuters-hosted case study quotes a small firm saying there were not enough hours in the day in busy season (TR-MADSEN-2026, older tool generation, not LLM-based). WCG still uses SurePrep at about 4,500 1040s.
- Tool handoffs: extraction and pre-preparation tools push data into an engine that recalculates and re-runs diagnostics, so upstream checks are repeated (WCG-NOTREADY-2026).
- Client chasing and late documents: an Accrual customer quote says document collection was the biggest win (ACCRUAL-INDIV-2026, anonymous).
- Cost: WCG says AI raises its technology stack cost by about 25% (WCG-PLAYBOOK-2026).

### Metrics and benchmarks (provenance in brackets)

- Boulay: returns with 60-70+ K-1s from more than 100 hours to about 15-20 hours (vendor-published testimonial; BASIS-TAX-2026).
- CLH CPAs: about one hour saved per simple 1040 (vendor-published; TR-COCOUNSEL-2025).
- Black Ore pilot: 75 firms; more than 99% accuracy across tens of thousands of returns; time savings up to 98%; cost per return down by up to 80%; review time cut by over 50% (vendor claims; BLACKORE-2026, MYCPE-BLACKORE-2026, BLACKORE-SITE-2026). Pricing reported by WCG as $100-150 per return on average (WCG's account).
- CCH Axcess Scan: 97.5% average overall accuracy on K-1 extraction (vendor claim; WK-AXCESSSCAN-2026).
- Canopy: up to 20 minutes saved per client (vendor claim; CANOPY-SMARTINTAKE-2025).
- TaxGPT: 90% reduction in first-pass preparation time (vendor claim; TAXGPT-SITE-2026).
- H&R Block: AI TaxAssist (paid DIY filers) supported 4.2 million client interactions; new clients getting Second Look returned at a rate more than 600 basis points higher (self-reported; HRB-Q4CALL-2026).
- TaxCalcBench (independent academic, by an author team from Column Tax, which sells a deterministic engine): 51 federal-only tax year 2024 test cases; the best model (Gemini 2.5 Pro) was fully correct on 32.35% of returns under the strict metric and 51.96% under a lenient ±$5 metric (COLUMN-TAXCALCBENCH-2025, results table). It tests unaided model calculation, not agents using a tax engine.
- TR 2026 Future of Professionals: 81% of tax and audit professionals use AI regularly; more than one third admit using unauthorised tools (vendor-owned survey; TR-FOP-2026).
- **Quality evidence: none independent.** No error rates, override rates, parallel-run results or inspection findings were found for any commercial preparer. PwC describes confidence flags and override reasons but publishes no rates. Black Ore says firms worried about differences from prior-year returns in the transition year (ACCTODAY-BLACKORE-2026). CPA Trendlines' April 2026 teaser says firms were producing fewer returns than a year earlier while salaries rose (CPATL-SEASON-2026; body gated, so figures and method unknown).

### Guardrails and regulatory points

- **Circular 230 (OPR Alert 2026-19, 24 Jun 2026):** §10.22 due diligence (verify facts, citations and calculations AI produces); §10.27(a) fees (billing manual time not spent, or double billing, may violate the rule depending on the facts; pass savings on openly and disclose AI use as needed); §10.35 competence (understand the technology's mechanics, limits and risks); §10.36 procedures (training, data-handling protocols, accuracy monitoring, vetting outside providers, all documented); §10.37 written advice (do not rely unreasonably on opaque logic); §10.51(a)(15) (willful unauthorised disclosure of return information) (IRS-OPR-2026).
- **IRC §7216 and §6713:** civil and criminal preparer penalties for unauthorised use or disclosure of tax return information (IRS-OPR-2026, item 6). Treas. Reg. §301.7216-3 requires taxpayer consent for uses and disclosures outside the listed exceptions, and §301.7216-3(b)(4) bars a US preparer from obtaining consent to disclose an individual filer's SSN to a preparer outside the US unless an adequate data protection safeguard defined by Treasury is used (ECFR-7216-3-2026). Under §301.7216-2(d) a US preparer may disclose return information to another US preparer for preparation or auxiliary services that are not substantive determinations (ECFR-7216-2-2026). None of the sources read says how these rules apply to AI vendors, and I found no AI-specific IRS §7216 guidance; treat that as an open question for counsel. WCG's August 2026 post shows a practical consent-first approach for its offshore team: consent requested before the engagement letter (WCG-7216-2026), but it concerns offshore staffing, not AI.
- **Vendor-side controls firms look for:** SOC 2 attestation, US data residency, no training on client data and zero data retention (stated by Black Ore, Basis, Juno and TaxGPT; WCG paid for a zero-data-retention sandbox).
- **UK and Australia:** PCRT topical guidance (19 Jan 2026): responsibility stays with the member; entering client data into a public AI model without consent is likely to breach confidentiality (PCRT-AI-2026, ICAEW-PCRT-2026). TPB Guidance Statement (22 Jul 2026): competence, reasonable care, confidentiality, record-keeping, professional judgment and supervision (TPB-AI-2026).
- **Disclosure:** the OPR alert says to disclose AI activities "in general or specific terms as needed"; no source shows how firms word this in engagement letters (gap).

### Frontier signals (dated)

- 2026-02-05: Accrual launches with $75M and "all forms" support, starting with complex K-1 work and the top 50 firms (ACCRUAL-LAUNCH-2026).
- 2026-04-29: Black Ore opens Tax Autopilot after a two-year pilot; about 3,700 firms on its waiting list (BLACKORE-2026).
- 2025-06-16 (older anchor): RSM launched myRSM Tax, built on a $1 billion technology and AI investment, to automate manual tasks and integrate workflows across entities and individuals; no outcome figures were published (RSM-MYRSM-2025, dated 2025-06-16).
- Basis announced an End-to-End Tax Platform that deploys agents from client intake through preparation and review; the blog post is undated and says leading firms are already building practices around agents doing the first pass (BASIS-E2E-2026).
- CPA Trendlines (gated) framed 2026 as a tipping point for agentic AI in tax and accounting firms (CPATL-OUTLOOK-2026, 2026-01-10, teaser only).
- 2026-09-22: Accrual's Arc agent, where a practitioner gives an objective, approves the plan and reviews the result (ACCRUAL-ARC-2026).
- 2026-07-24: WCG says no vendor yet completes a return inside commercial tax software and that it may revisit in November 2026. It reports Ready to Review's K-1 support is on a November 2026 roadmap (WCG-NOTREADY-2026).
- 2026-08-11: H&R Block will expand its AI-supported appointment model to a full designated market area for tax season 27 (HRB-Q4CALL-2026).
- Vendors compete on pricing models: per page or per return (Black Ore, per WCG) versus fees linked to a firm's engagement fees by complexity tier (Accrual) (ACCRUAL-LAUNCH-2026).
- TaxBench (Columbia, in development) targets 500+ rules and 50+ scenarios for tax year 2025 and field-by-field scoring including whether agents ask for missing information (COLUMBIA-TAXBENCH-2026).

### Workforce and role effects

- Reviewers start from a prepared draft; staff investigate exceptions (Basis); one reviewer replaces three people on K-1 footnote decisions (PwC); preparers become reviewers (anonymous Juno testimonial: "I'm reviewing, and that's a completely different job"; JUNO-SITE-2026).
- Retail: H&R Block says tax pros move from collecting and entering information to guidance and planning (HRB-Q4CALL-2026).
- Early-career development: Thomson Reuters' article says firms must ensure junior staff still build professional judgment as tasks automate (TR-FOP-2026). Black Ore's CEO said engineering needs "less and less" human engineers and he expects fewer people in other functions (ACCTODAY-BLACKORE-2026).
- Hiring mix: CPA Trendlines reports public accounting firms adding few accountants but many sales, finance, systems and data roles since 2021 (CPATL-WORKFORCE-2026, gated).
- Vendors hire accountants as product and deployment staff: the Basis accounting-staff posting asks for 4-10 years in audit or tax at a top firm and says the person will not do client accounting but shapes agent behaviour with engineers and prompt work (BASIS-CAREERS-2026).

### Objections and concerns practitioners raise

- "End to end" claims versus partial tools (WCG-NOTREADY-2026).
- Proprietary preparation platforms leave a firm stranded if the AI cannot finish a return, with prior-year history locked in (WCG).
- Price versus a working scan-and-push baseline: SurePrep at about $25 per return in WCG's own estimate (WCG).
- Accuracy claims with no independent test (this run).
- Reliability and the CPA's responsibility when automation prepares the return (MYCPE-TAXGPT-2026 summary).
- Year-one differences from prior-year returns (ACCTODAY-BLACKORE-2026).

### Interview probes for an advisor

1. Which step of your 1040 or 1065 workflow do you trust AI to do unreviewed, and what evidence (parallel runs, error counts, override rates) did you collect before deciding?
2. Where does the AI's work end and your tax software's work begin, and how many times is each return calculated or diagnosed?
3. Walk me through your §7216 consent, engagement letter and AI-use log. Which vendors see return information, and what did you check (SOC 2, retention, training on data)?
4. How have review roles and junior-staff development changed since you adopted AI preparation, and how do you price the savings (OPR §10.27(a))?
5. Who in the firm owns AI in tax (a pod, a champion network, a partner), and what would make you move from "evaluating" to "committed" for the next season?

---

## 4. Routed to other modules

- **tax / compliance (corporate and in-house direct tax):** KPMG's Digital Gateway with Claude, announced 2026-05-20, initial focus on tax clients and private equity, 276,000 KPMG people (KPMG-ANTHROPIC-2026); EY and PwC agent platforms for large clients (PWC-MEGNA-2025 Agent OS); in-house automation with Savant and Oxford Industries (SAVANT-2026, session on 28 Apr 2026).
- **tax / controversy:** notice intake and response-letter drafting in Accrual Arc (ACCRUAL-ARC-2026); the powers-of-attorney step in the same demo.
- **tax / research-advisory:** CoCounsel Tax and other research assistants; H&R Block's assistant as a knowledge tool (use case 07 note).
- **Accounting (client accounting services) archetype:** Baker Tilly's collaboration with Basis for managed accounting and finance services (BAKERTILLY-BASIS-2026, 2026-04-28); Wiss (Basis in client accounting services; WISS-BASIS-2024); Sikich (Basis in month-end close; SIKICH-BASIS-2026). None of these is tax return preparation. Baker Tilly also announced HubSync for tax workflow management (BAKERTILLY-HUBSYNC-2026, 2026-04-01; a short aggregator summary, workflow rather than preparation).
- **Governance and evidence angle:** TaxCalcBench and TaxBench (COLUMN-TAXCALCBENCH-2025, COLUMBIA-TAXBENCH-2026); OPR, PCRT and TPB guidance; the United States v. Heppner privilege discussion in a vendor blog (JUPID-7216-2026) was not verified against a primary source and is not used here.
- **Accounting archetype (close and categorisation):** Accounting Today (2026-10-16) reported two studies comparing human accountants with AI on month-end close and categorisation. I read only the first study's description; it concerns accounting, not tax.

---

## 5. Sources

Date is the publication date except where marked "retrieval date" (undated vendor page; read 2026-10-17) or "modified" (page metadata). Access `full` means the page was opened and read. Where a page was gated or truncated, the locator says so.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| TR-COCOUNSEL-2025 | Thomson Reuters Launches Agentic AI Solutions to Transform Tax, Audit and Accounting Workflows | Thomson Reuters | vendor | https://www.thomsonreuters.com/en/press-releases/2025/november/thomson-reuters-launches-agentic-ai-solutions-to-transform-tax-audit-and-accounting-workflows | 2025-11-05 | full |
| TR-RTR-2026 | Ready to Review (product page and FAQ) | Thomson Reuters | vendor | https://tax.thomsonreuters.com/en/products/ready-to-review | 2026-10-17 (retrieval) | full |
| TR-MADSEN-2026 | CPA firm automation case study: How one practice simplified 1040 tax prep (SurePrep/UltraTax; baseline) | Thomson Reuters Community | vendor | https://community.thomsonreuters.com/tax-accounting/f/tax-research-guidance/35077/cpa-firm-automation-case-study-how-one-practice-simplified-1040-tax-prep | 2026-03-17 | full |
| TR-FOP-2026 | What the 2026 Future of Professionals Report says tax & audit firm leaders should be prioritizing now | Thomson Reuters Institute | survey | https://www.thomsonreuters.com/en/institute/reports/future-of-professionals-tax-audit-firms-paper-2026 | 2026-07-21 | full |
| BLACKORE-2026 | AI Tax Startup Black Ore Opens Platform to CPA Firms | Sovereign Magazine | press | https://www.sovereignmagazine.com/article/ai-tax-startup-black-ore-opens-platform-to-cpa-firms | 2026-04-29 | full |
| ACCTODAY-BLACKORE-2026 | Black Ore's Tax Autopilot now generally available | Accounting Today | press | https://www.accountingtoday.com/news/black-ores-tax-autopilot-now-generally-available | 2026-04-29 | full |
| MYCPE-BLACKORE-2026 | Can Black Ore's Tax Autopilot Fix the CPA Labor Shortage? | my-cpe | press | https://my-cpe.com/insights/news-and-insights/technology/can-black-ore-tax-autopilot-fix-the-cpa-labor-shortage | 2026-05-04 | full |
| BLACKORE-SITE-2026 | Black Ore home page (Tax Autopilot claims) | Black Ore | vendor | https://www.blackore.ai/ | 2026-10-17 (retrieval) | full |
| BASIS-2026 | Basis raises $100M Series B | Built In NYC | press | https://www.builtinnyc.com/articles/basis-raises-100m-series-b-20260226 | 2026-02-26 | full |
| BASIS-HOME-2026 | Basis home page | Basis | vendor | https://www.getbasis.ai/ | 2026-10-17 (retrieval) | full |
| BASIS-TAX-2026 | Basis for tax | Basis | vendor | https://www.getbasis.ai/solutions/tax | 2026-10-17 (retrieval) | full |
| BASIS-SMALL-2026 | Basis for small firms | Basis | vendor | https://www.getbasis.ai/solutions/small-firms | 2026-10-17 (retrieval) | full |
| BASIS-E2E-2026 | The future of tax is end-to-end intelligence | Basis | vendor | https://www.getbasis.ai/blogs/the-future-of-tax-is-end-to-end-intelligence | 2026-10-17 (retrieval; page undated) | full |
| BASIS-CAREERS-2026 | Careers at Basis (Member of Accounting Staff; Deployed Intelligence Strategist; open roles list) | Basis | job-posting | https://www.getbasis.ai/careers | 2026-10-17 (retrieval) | full |
| ACCRUAL-LAUNCH-2026 | Tax platform Accrual launches with AI automation support for all forms | Accounting Today | press | https://www.accountingtoday.com/news/tax-platform-accrual-launches-with-ai-automation-support-for-all-forms | 2026-02-05 | full |
| ACCRUAL-ARC-2026 | Accrual launches Arc AI for accounting workflows | Accounting Today | press | https://www.accountingtoday.com/news/accrual-launches-arc-ai-can-learn-from-and-replicate-accounting-workflows | 2026-09-22 | full |
| ACCRUAL-HOME-2026 | Accrual home page | Accrual | vendor | https://www.accrual.com/ | 2026-10-17 (retrieval) | full |
| ACCRUAL-INDIV-2026 | Accrual: individual (1040, 1041) tax preparation | Accrual | vendor | https://www.accrual.com/tax/individuals | 2026-10-17 (retrieval) | full |
| ACCRUAL-PARTNER-2026 | Accrual: partnership returns | Accrual | vendor | https://www.accrual.com/tax/partnerships | 2026-10-17 (retrieval) | full |
| JUNO-SITE-2026 | Juno: tax prep automation (customer quotes) | Juno | vendor | https://www.juno.tax/ | 2026-10-17 (retrieval) | full |
| TAXGPT-SITE-2026 | AI tax preparation (product page) | TaxGPT | vendor | https://www.taxgpt.com/ai-tax-preparation | 2026-10-17 (retrieval) | full |
| MYCPE-TAXGPT-2026 | TaxGPT Launches Autonomous Tax Agent for Busy Season | my-cpe | press | https://my-cpe.com/insights/news-and-insights/technology/taxgpt-launches-autonomous-tax-agent-for-busy-season | 2026-03-25 | full (summary only; body paywalled) |
| WK-AXCESSSCAN-2026 | CCH Axcess Scan | Wolters Kluwer | vendor | https://www.wolterskluwer.com/en/solutions/cch-axcess/scan | 2026-10-17 (retrieval) | full (via r.jina.ai mirror) |
| INTUIT-PROCONNECTAI-2026 | AI-Powered Tax Prep Tools (ProConnect) | Intuit | vendor | https://accountants.intuit.com/tax-software/tax-online/ai-features/ | 2026-10-17 (retrieval) | full |
| CANOPY-SMARTINTAKE-2025 | Canopy Unveils Native AI Powered Smart Intake Capability | Canopy (via Silicon UK) | vendor | https://www.silicon.co.uk/press-release/canopy-unveils-native-ai-powered-smart-intake-capability-to-eliminate-client-friction | 2025-07-22 | full |
| APARIPRO-2026 | ApariPro: AI powered tax preparation for accountancy firms | ApariPro | vendor | https://www.aparipro.com/ | 2026-06-17 (modified) | full |
| SAVANT-2026 | Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Technology Seminar 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 | full |
| PERPLEXITY-2026 | Perplexity Launches AI Agent That Drafts Tax Returns | PYMNTS | press | https://www.pymnts.com/taxes/2026/perplexity-launches-ai-agent-that-drafts-tax-returns/ | 2026-04-06 | full |
| JUPID-7216-2026 | Can Accountants Use ChatGPT? IRS §7216, Client Confidentiality, and What Changed in 2026 | Jupid | vendor | https://jupid.com/blog/can-accountants-use-chatgpt | 2026-06-29 | full (skimmed; not relied on) |
| WCG-NOTREADY-2026 | AI Tax Prep in 2026: Not Quite There Yet | WCG CPAs & Advisors | firm | https://wcginc.com/blog/ai-tax-prep-in-2026-not-quite-there-yet/ | 2026-07-24 | full |
| WCG-PLAYBOOK-2026 | AI Tax Preparation and Automation: What It Means for You | WCG CPAs & Advisors | firm | https://wcginc.com/blog/ai-tax-preparation-and-automation-what-it-means-for-you/ | 2026-07-05 | full |
| WCG-7216-2026 | One Team, One Heartbeat: WCG Engagements Requires A 7216 Consent | WCG CPAs & Advisors | firm | https://wcginc.com/blog/one-team-one-heartbeat-7216-consent/ | 2026-08-28 | full |
| HRB-Q4CALL-2026 | H&R Block Q4 fiscal 2026 earnings call transcript | H&R Block (via earningswhispers.com) | firm | https://earningswhispers.com/transcript/HRB/Q42026 | 2026-08-11 | full (via r.jina.ai mirror) |
| CNBC-HRB-2025 | ChatGPT for taxes? OpenAI and H&R Block have a plan for tax pros | CNBC via NBC 7 San Diego | press | https://www.nbcsandiego.com/news/business/money-report/chatgpt-for-taxes-openai-and-hr-block-have-a-plan-for-tax-pros/3804532/?amp=1 | 2025-04-15 | full |
| RSM-MYRSM-2025 | RSM Expands AI Commitment with Launch of myRSM Tax | RSM US | firm | https://rsmus.com/newsroom/2025/rsm-expands-ai-commitment-with-launch-of-myrsm-tax.html | 2025-06-16 | full |
| PWC-MEGNA-2025 | How PwC's tax team is using agentic AI | CFO Dive (Informa TechTarget) | press | https://www.cfo.com/news/how-pwcs-dom-megna-tax-team-is-using-agentic-ai-agent-os-cpa-cfo-/750062/ | 2025-06-06 | full |
| MULTIPLIER-2025 | Multiplier nabs $27.5M to fuel AI-powered accounting roll-ups | TechCrunch | press | https://techcrunch.com/2025/06/18/multiplier-founded-by-ex-stripe-exec-nabs-27-5m-to-fuel-ai-powered-accounting-roll-up | 2025-06-18 | full |
| KPMG-ANTHROPIC-2026 | KPMG Partners with Anthropic for Digital Gateway Powered by Claude | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/05/20/kpmg-partners-with-anthropic-for-digital-gateway-powered-by-claude/183743/ | 2026-05-20 | full |
| BAKERTILLY-BASIS-2026 | Baker Tilly collaborates with Basis (managed services) | Baker Tilly | firm | https://www.bakertilly.com/news/baker-tilly-collaborates-with-basis | 2026-04-28 | full |
| BAKERTILLY-HUBSYNC-2026 | Baker Tilly Collaborates With HubSync to Modernize Tax Service Delivery | BiOnTX industry news (aggregator) | press | https://business.biontx.org/industry-news/Details/baker-tilly-collaborates-with-hubsync-to-modernize-tax-service-delivery-through-ai-enabled-workflows-333358 | 2026-04-01 | full (short summary) |
| WISS-BASIS-2024 | Wiss Announces Strategic Partnership with Accounting AI Platform Basis | Wiss | firm | https://wiss.com/wiss-announces-strategic-partnership-with-accounting-ai-platform-basis/ | 2024-09-16 | full (via r.jina.ai mirror) |
| SIKICH-BASIS-2026 | Sikich partners with Basis to advance AI-enabled accounting services | Sikich | firm | https://www.sikich.com/insight/sikich-partners-with-basis-to-advance-ai-enabled-accounting-services/ | 2026-07-01 | full |
| CPATL-OUTLOOK-2026 | Outlook 2026: Agentic AI Reaches the Tipping Point in Tax and Accounting Firms | CPA Trendlines | press | https://cpatrendlines.com/2026/01/10/outlook-2026-agentic-ai-reaches-the-tipping-point-in-tax-and-accounting-firms | 2026-01-10 | full (teaser; body gated) |
| CPATL-SEASON-2026 | Inside Tax Season's Hidden Shift: Same Work, Fewer People, Higher Cost | CPA Trendlines | press | https://cpatrendlines.com/2026/04/05/inside-tax-seasons-hidden-shift-same-work-fewer-people-higher-cost | 2026-04-05 | full (teaser; body gated) |
| CPATL-WORKFORCE-2026 | CPAs Not Wanted: Firms Build a New Workforce - without Accountants | CPA Trendlines | press | https://cpatrendlines.com/2026/05/29/cpas-not-wanted-firms-build-a-new-workforce-without-accountants | 2026-05-29 | full (teaser; body gated) |
| COLUMN-TAXCALCBENCH-2025 | TaxCalcBench: Evaluating Frontier Models on the Tax Calculation Task | Column Tax authors, arXiv 2507.16126 | academic | https://arxiv.org/abs/2507.16126 | 2025-07-22 | full (abstract and PDF) |
| COLUMBIA-TAXBENCH-2026 | TaxBench (in development) | Columbia DAP Lab | academic | https://daplab.cs.columbia.edu/benchmarks/taxbench/ | 2026-10-17 (retrieval) | full |
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (OPR Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| ECFR-7216-2-2026 | 26 CFR 301.7216-2 (permissible disclosures or uses without consent) | Legal Information Institute (e-CFR text) | regulator | https://www.law.cornell.edu/cfr/text/26/301.7216-2 | 2026-10-17 (retrieval) | full |
| ECFR-7216-3-2026 | 26 CFR 301.7216-3 (disclosure or use only with the taxpayer's consent) | Legal Information Institute (e-CFR text) | regulator | https://www.law.cornell.edu/cfr/text/26/301.7216-3 | 2026-10-17 (retrieval) | full |
| TPB-AI-2026 | TPB releases guidance on responsible AI use for tax practitioners | Tax Practitioners Board (Australia) | regulator | https://www.tpb.gov.au/tpb-releases-guidance-responsible-ai-use-tax-practitioners | 2026-07-22 | full (via r.jina.ai mirror) |
| PCRT-AI-2026 | Professional bodies issue AI advice to members | Association of Taxation Technicians (PCRT bodies) | professional-body | https://www.att.org.uk/technical/news/professional-bodies-issue-ai-advice-members | 2026-01-19 | full |
| ICAEW-PCRT-2026 | PCRT bodies publish guidance on using AI in tax | ICAEW | professional-body | https://www.icaew.com/insights/tax-news/2026/jan-2026/professional-conduct-in-relation-to-taxation-bodies-publish-guidance-on-using-ai-in-tax | 2026-01 | full |

Source counts: 53 distinct sources, all opened (several only as gated teasers or short summaries, noted in the table): vendor 19, press 16, firm 8, regulator 4, academic 2, professional-body 2, survey 1, job-posting 1.

---

## 6. Gaps

- **Independent quality evidence is absent.** No error rates, override rates, parallel-run results, regulator inspection findings or third-party measurement for Ready to Review, Black Ore, Basis, Accrual, Juno or TaxGPT. TaxCalcBench is an LLM-only calculation test from 2025 with 2025-vintage models.
- **Named customers and outcomes are thin.** Only Boulay, CLH, Maxwell Locke & Ritter, Armanino, Kulangy CPA, Whitcomb & Sheridan, Seed Money Consulting and H&R Block are named; all outcome statements are testimonials or management remarks. Armanino's partnership release (2026-02-18, BusinessWire) returned 403.
- **Blocked or unread:** Wolters Kluwer news pages (CCH Axcess Expert AI releases, 403 even through the mirror), BusinessWire releases for Canopy (Sep and Oct 2025) and Accrual (Sep 2026), the AICPA small-firm generative AI policy template (no content returned), the AICPA 2026 tax software survey AI results (page summary only), the Thomson Reuters 2026 State of Tax Professionals report and the Blue J/CPA.com outlook (landing pages only), Reddit r/taxpros (blocked by network policy), TaxDome and Karbon AI pages (no usable text), the full TaxGPT trade article (paywalled), and CPA Trendlines bodies (membership-gated).
- **Job postings:** only Basis role pages were read. A search result pointed to a Utah firm's tax manager posting that mentions drafting, research and review with AI tools, but the page returned no text and the posting has no confirmed date, so it is not used. No Big Four, mid-tier or H&R Block postings were reached.
- **UK and other markets:** only ApariPro and the PCRT guidance were read. An IRIS (UK) anomaly-check tool and the CCH iFirm collaboration were seen only in a search summary or on ApariPro's own page. Nothing on Germany, Canada, Australia (beyond the TPB statement) or India.
- **Trusts and estates (1041)** appear only on Accrual's pages. No practitioner source on AI use for fiduciary returns was found.
- **Engagement letters:** no source shows actual engagement-letter language on AI, AI-use logs or client disclosure; the OPR alert gives the expectation only.
- **§7216 and AI vendors:** no AI-specific IRS guidance was found in the sources read; the IRS §7216 FAQ page is marked archival.
- **Search budget:** web search was exhausted partway through the run. Candidate leads not followed: Gelt (the gelt.com page is an unrelated cashback site), Skalar and Limetax, Drake and UltraTax AI features, IRIS, the AICPA small-firm AI policy template, and the Intuit ELEVATE 2026 session list.
- **Conflicts noted:** Black Ore's waiting list is about 3,700 firms in the Sovereign article and close to 4,000 in a search summary; the former is used. Black Ore says "above 99 percent" accuracy while WCG calls no vendor end-to-end; these are different claims about different things (accuracy of extraction versus completion in the firm's own software).
