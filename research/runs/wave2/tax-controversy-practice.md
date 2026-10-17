# Tax controversy: practice angle (wave 2 deep dive)

- **Archetype:** tax
- **Module:** controversy (audits, notices, appeals and disputes from the taxpayer and practitioner side, plus tax-authority AI)
- **Angle:** practice (what firms, in-house teams and tax authorities actually do)
- **Prepared:** 2026-10-17
- **Method note:** Sources were opened with `curl` (HTML via a local text extractor, `pdftotext` for PDFs) and, for bot-walled hosts, the `r.jina.ai` text mirror (Axios, GAO, ATO, ANAO, Wolters Kluwer, Bloomberg Tax commentary, Stanford, HMRC). Web search was used for about ten directions and then ran out of budget; no job-posting search could be run after that point. Every source in section 5 was opened unless marked `search-only` (none are). Source keys follow the landscape file where the same document appears there.

## 1. Summary

- **The evidence is lopsided.** The best-measured AI in controversy sits on the tax-authority side (IRS return selection, assessed by TIGTA; ATO model governance, assessed by ANAO; IRS amended-return processing, reported by the IRS CIO). On the taxpayer and practitioner side, nearly everything is vendor description or a firm survey. No firm or in-house team has published an error rate, an override rate, a parallel-run result or a time saving for notice response, IDR handling or Appeals work.
- **Practitioner-side practice is concentrated in a few steps:** reading and summarising notices, drafting client explanations and agency replies, checking returns against third-party data before filing, and (for large multinationals) consistency checks on documentation. Wolters Kluwer (CCH AnswerConnect Document Analysis, CCH Expert AI) and Thomson Reuters (CoCounsel Tax) describe notice analysis as shipped features. EY's 2025 survey of 1,934 senior tax executives is the only sizeable measure: 39% say they have built at least one controversy-focused pilot or tool and 30% more are integrating GenAI into other processes. It is a self-reported survey by a firm that sells the services.
- **The visible failures are in written advocacy.** *Clinco v. Commissioner* (T.C. Memo. 2026-16) found that three of four cases cited were apparently hallucinated. Judge Holmes told Bloomberg he had seen fewer than a dozen such instances and issued no sanctions yet. In *Khoja v. Commissioner* a Tax Court judge questioned an IRS attorney about a non-existent citation in an IRS motion. IRS OPR Alert 2026-19 (24 Jun 2026) applies existing Circular 230 duties, including §10.27 on fees, to AI use.
- **Tax authorities are scaling AI while shrinking.** GAO counted 126 active IRS AI use cases at June 2025 (10 in August 2022), with 61% still in development. TIGTA found the IRS has no process to show AI selection models beat prior methods. The IRS CEO announced an "AI-first IRS" on 30 Sep 2026 with headcount flat at about 74,000. ATO's own CDO describes an AI assistant that orders substantiation documents for auditors, while ANAO found 74% of ATO production models had no completed data ethics assessment.
- **Roles are shifting, but the sources are thin.** The most concrete role signals are an IRS Chief Counsel attorney saying staff must adopt AI or leave, an IRS statement that AI "is not designed to eliminate jobs", a TEI poll in which two of more than 50 hands said tax owns AI implementation, and EY's finding that securing talent is the top barrier (44%).
- **Counts:** 20 candidate use cases (1 grade A, 8 grade B, 10 grade C, 1 grade D). 12 use cases are practitioner or in-house side (01 to 08 and 20, plus related checks inside 05) and 11 are tax-authority side; see the module notes for the split.

## 2. Use cases

```yaml
- id: tax-controversy-01
  title: AI reads and triages incoming IRS and state tax notices
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [transaction-processing]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "A notice is written in technical language. Before anything can be drafted, someone has to work out what changed, what the agency asks for and how to respond, and that first read often takes longer than expected. Handling also varies from practitioner to practitioner."
  solution: "An uploaded notice is analysed to pull out the response deadline, amount due and underlying issue (a CP2000 may flag omitted income or a third-party mismatch), then possible response paths such as dispute or penalty abatement are listed with when each may fit. EY describes notice tracking and key-element extraction as early use cases. Wolters Kluwer names CCH AnswerConnect Document Analysis and CCH Expert AI; Thomson Reuters lists IRS notices among documents CoCounsel Tax analyses."
  outcomes:
    - lever: speed
      description: "Vendor says summarising the notice and listing options shortens the time from receipt to action. No figure published."
      figure: "none published"
      measures: "no measure given"
      provenance: vendor-published
      source_ref: WK-NOTICE-2026
    - lever: quality
      description: "Vendor says every notice is evaluated with the same framework, which reduces variation in response time, communication and documentation. No figure published."
      figure: "none published"
      measures: "no measure given"
      provenance: vendor-published
      source_ref: WK-NOTICE-2026
  prerequisites:
    - "Notices reach the firm quickly (AccountingToday advises filing a Power of Attorney right away and keeping a structured notice workflow)."
    - "An approved AI tool with confidentiality protections; the OPR alert says to use only secure, enterprise-approved AI for client data."
  risks_and_guardrails:
    - "Return information shared with an unsecured tool can engage IRC §§6713 and 7216 and Circular 230 §10.51(a)(15) (IRS-OPR-2026, Regulatory Framework item 6)."
    - "A practitioner-written workflow says to check every number and the response deadline against the notice itself (FINDSKILL-2026, 'Minutes 13-15')."
    - "EY's Americas Tax Innovation Leader describes most pilots as classification, summarisation and key-element extraction, that is, early-stage (EY-TAXRISK-2025)."
  human_checkpoints:
    - "The reviewer chooses the course of action; the vendor page states that the reviewer 'still determines' it (WK-NOTICE-2026)."
  role_evolution: "Wolters Kluwer describes reviewers starting from a structured summary and a consistent baseline rather than reading each notice from scratch (WK-NOTICE-2026, 'Turning a notice into a clear summary')."
  evidence_grade: C
  sources:
    - { ref: WK-NOTICE-2026, title: "How to respond to IRS notices with a clear, structured workflow", publisher: Wolters Kluwer Tax and Accounting, type: vendor, url: "https://www.wolterskluwer.com/en/expert-insights/how-to-respond-to-irs-notices-with-a-clear-structured-workflow", date: 2026-07-06, access: full, locator: "sections 'Turning a notice into a clear summary', 'Clarifying response options', 'Creating a more consistent approach to notice handling'" }
    - { ref: WK-DOCAN-2026, title: "5 ways CCH AnswerConnect Document Analysis helps make tax work faster", publisher: Wolters Kluwer Tax and Accounting, type: vendor, url: "https://www.wolterskluwer.com/en/expert-insights/5-ways-cch-answerconnect-document-analysis-helps-make-tax-work-faster", date: 2026-07-06, access: full, locator: "section 'Turn IRS notices into clear action plans'" }
    - { ref: TR-COCOUNSEL-2026, title: "Meet CoCounsel Tax (on-demand demo page)", publisher: Thomson Reuters, type: vendor, url: "https://taxprof.thomsonreuters.com/meet-cocounsel-tax-26", date: 2026, access: full, locator: "bullet list 'In this demo, you'll learn how to' (page is undated; year from URL suffix)" }
    - { ref: EY-TAXRISK-2025, title: "2025 EY Tax Risk and Controversy survey", publisher: EY, type: survey, url: "https://www.ey.com/en_gl/insights/tax/tax-risk-and-controversy-survey", date: 2025-12-11, access: full, locator: "section 'GenAI tools focused on tax controversy', Daren Campbell quote" }
    - { ref: BTAX-EY-2025, title: "AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way", publisher: Bloomberg Tax (authors from EY), type: press, url: "https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way", date: 2025-11-21, access: full, locator: "section 'Enterprise Tax Functions', 'Tax notices' bullet" }
    - { ref: TEI-MIDYEAR-2026, title: "TEI Midyear Conference 2026 At a Glance agenda", publisher: Tax Executives Institute, type: conference, url: "https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf", date: 2026-03-17, access: full, locator: "Tuesday 17 Mar 2026, 1:30-2:30 PM breakouts: 'TEI Tax Lab: Managing Tax Notices with AI' (title only)" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework item 6; Best Practices" }
    - { ref: FINDSKILL-2026, title: "Tax Preparers: Turn a CP2000 Into a Client Answer in 15 Min", publisher: FindSkill.ai, type: vendor, url: "https://findskill.ai/blog/tax-preparers-cp2000-ai-workflow/", date: 2026-08-01, access: full, locator: "'The 15-minute workflow', 'What it can't do'" }
  last_reviewed: 2026-10-17
  notes: "No named customer, no accuracy figure and no time measurement for any vendor notice tool was found. The TEI lab is a title on an agenda; no content was read. Maturity is 'piloting' on the strength of EY's description of early pilots; the vendors describe the features as available."

- id: tax-controversy-02
  title: AI drafts client explanations and formal replies to notices (CP2000 responses, penalty abatement requests)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [document-production, client-interaction]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: piloting
  problem: "After a notice is understood, the firm must explain it to the client in plain language and prepare a formal response, often under a short response window. Both are drafted from scratch each time."
  solution: "The tool generates a client-ready explanation and a draft agency response such as a penalty abatement request, structured so it can be completed with client-specific facts. Drafts can become templates for similar notices. A practitioner write-up shows the same pattern with a general chatbot on de-identified numbers: explainer, response skeleton, then manual verification."
  outcomes:
    - lever: speed
      description: "Vendor says drafts shorten the path from identifying the issue to resolving it and keep a consistent format across engagements. No figure published."
      figure: "none published"
      measures: "no measure given"
      provenance: vendor-published
      source_ref: WK-NOTICE-2026
    - lever: quality
      description: "A survey finding: respondents report using GenAI to generate supporting evidence and documents in real time and to automate or partly automate responses to tax authority enquiries ('significant proportions', share not stated in the page text)."
      figure: "none published"
      measures: "EY survey of 1,934 senior tax executives; share using GenAI for these tasks not stated in the text read"
      provenance: vendor-published
      source_ref: EY-TAXRISK-2025
  prerequisites:
    - "De-identification or an enterprise AI tool with a signed data-processing agreement (FINDSKILL-2026, 'Step 0')."
    - "The practitioner decides the position (agree, disagree, partial agree, reasonable cause) before any drafting."
  risks_and_guardrails:
    - "Models can get tax law wrong; the practitioner workflow says to use AI for structure and explanation, not citation, and to check every authority (FINDSKILL-2026, 'What it can't do')."
    - "Billing: OPR says billing for manual time not actually spent may violate Circular 230 §10.27, depending on the facts (IRS-OPR-2026, item 2)."
    - "Circular 230 §10.22 due diligence applies to documents sent to the IRS (IRS-OPR-2026, item 1)."
  human_checkpoints:
    - "Practitioner verifies numbers, deadline and substantiation, re-inserts identifiers locally and signs as the professional who owns the position (FINDSKILL-2026, 'Minutes 13-15')."
  role_evolution: "The reviewer 'does not need to pause the workflow to write an explanation from scratch' (WK-NOTICE-2026). OPR says savings should be passed to clients openly and efficiency reflected in billing (IRS-OPR-2026, item 2)."
  evidence_grade: C
  sources:
    - { ref: WK-NOTICE-2026, title: "How to respond to IRS notices with a clear, structured workflow", publisher: Wolters Kluwer Tax and Accounting, type: vendor, url: "https://www.wolterskluwer.com/en/expert-insights/how-to-respond-to-irs-notices-with-a-clear-structured-workflow", date: 2026-07-06, access: full, locator: "sections 'Translating technical issues into client-ready communication', 'Generating formal responses for the agency'" }
    - { ref: TR-COCOUNSEL-2026, title: "Meet CoCounsel Tax (on-demand demo page)", publisher: Thomson Reuters, type: vendor, url: "https://taxprof.thomsonreuters.com/meet-cocounsel-tax-26", date: 2026, access: full, locator: "demo bullets: draft client letters and responses; reusable templates; 'IRS notice responses' example" }
    - { ref: FINDSKILL-2026, title: "Tax Preparers: Turn a CP2000 Into a Client Answer in 15 Min", publisher: FindSkill.ai, type: vendor, url: "https://findskill.ai/blog/tax-preparers-cp2000-ai-workflow/", date: 2026-08-01, access: full, locator: "'Step 0: De-identify'; 'The 15-minute workflow'" }
    - { ref: EY-TAXRISK-2025, title: "2025 EY Tax Risk and Controversy survey", publisher: EY, type: survey, url: "https://www.ey.com/en_gl/insights/tax/tax-risk-and-controversy-survey", date: 2025-12-11, access: full, locator: "section 'How GenAI is changing tax controversy'" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "Regulatory Framework items 1, 2 and 6" }
  last_reviewed: 2026-10-17
  notes: "The FindSkill article is a training-course vendor blog; its '45-minute call becomes a 5-minute email' line is an illustration, not a measurement, and is not used as a figure."

- id: tax-controversy-03
  title: Weekly IRS transcript monitoring to pre-empt CP2000 underreporter notices
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "The IRS Automated Underreporter flag is visible on account transcripts before the CP2000 letter is sent, but few practitioners check transcripts regularly, so the client is surprised and penalties and interest accrue."
  solution: "A practitioner obtains authorisations (Form 8821), pulls account transcripts for about 700 clients weekly with third-party software, and has the software highlight transcripts carrying the underreporting flag. The practitioner then compares the return to the IRS wage and income data, amends if needed and can tell the AUR unit the error was self-discovered."
  outcomes:
    - lever: risk
      description: "The practitioner says knowing in advance lets him fix the return and bypass the associated penalties and interest. The notice is still sent. No before/after figure."
      figure: "700 clients monitored weekly; practitioner cites over 6 million CP2000-type notices a year"
      measures: "700 = clients whose transcripts the practitioner pulls once a week (his statement); 6 million = IRS notices sent annually (his statement, 2019, not independently checked)"
      provenance: self-reported
      source_ref: ACCTODAY-2019
  prerequisites:
    - "Form 8821 on every client, with the box checked for IRS correspondence copies, and e-Services transcript access."
    - "The IRS requires disclosure that third-party software is used to pull transcripts (his statement)."
  risks_and_guardrails:
    - "The IRS does not check transcripts before the CP2000 is sent, so the letter still arrives (ACCTODAY-2019)."
    - "Client authorisations and disclosure are conditions of access (ACCTODAY-2019)."
  human_checkpoints:
    - "The professional reviews the flagged return and decides whether to amend."
  role_evolution: "Moves the practitioner from reacting to a notice to acting on a data signal (ACCTODAY-2019)."
  evidence_grade: B
  sources:
    - { ref: ACCTODAY-2019, title: "Using AI to get ahead of the IRS", publisher: Accounting Today, type: press, url: "https://www.accountingtoday.com/news/using-ai-to-get-ahead-of-the-irs", date: 2019-10-22, access: full, locator: "paragraphs 2-9 (Bill Nemeth, Atlanta practitioner)" }
  last_reviewed: 2026-10-17
  notes: "Older than the 12-18 month window; kept as the only named practitioner deployment found. The 'AI' label is the article's; the software analyses transcripts for a flag code. No 2025-2026 follow-up was found."

- id: tax-controversy-04
  title: Pre-filing audit-risk review that reconciles returns to third-party reporting and flags audit-sensitive items
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Practitioners say IRS data matching now flags mismatches between filed returns and third-party reports (1099-K, 1099-NEC, brokerage and K-1 data), so a technically correct return can still draw a notice if the numbers do not visibly reconcile."
  solution: "Before sign-off, AI reviews an uploaded return 'as though it were a partner-level signer' (Wolters Kluwer's words), lists major risk areas and a 'must-fix' list, and points to places in the return. Practitioner commentary recommends a reconciliation checklist and a documented review trail, and a basis reconciliation for digital-asset clients."
  outcomes:
    - lever: risk
      description: "No outcome published for any tool. A vendor page describes prioritised risks and 'must-fix' items for the reviewer."
      figure: "none published"
      measures: "no measure given"
      provenance: vendor-published
      source_ref: WK-DOCAN-2026
  prerequisites:
    - "Client records and third-party forms available in digital form before filing."
    - "A firm checklist or workflow that makes reconciliation sign-off a condition of return completion (TSCPA-2026 describes this as a practice some firms are adopting)."
  risks_and_guardrails:
    - "The IRS does not publish its selection criteria; the Accounting Today piece says practitioners cannot see what triggers scrutiny. That piece also states GAO found IRS lacks documentation and validation controls, which is not in the GAO highlights page read (see module notes)."
    - "Pre-filing checklists built from published GAO and TIGTA findings do not replicate IRS models; TSCPA says no publicly available software replicates IRS audit selection."
  human_checkpoints:
    - "Reviewer investigates each flagged item and signs the return."
  role_evolution: "Preparers are described as responsible for making returns consistent with third-party data, not only technically correct (TSCPA-2026, Conclusion)."
  evidence_grade: C
  sources:
    - { ref: WK-DOCAN-2026, title: "5 ways CCH AnswerConnect Document Analysis helps make tax work faster", publisher: Wolters Kluwer Tax and Accounting, type: vendor, url: "https://www.wolterskluwer.com/en/expert-insights/5-ways-cch-answerconnect-document-analysis-helps-make-tax-work-faster", date: 2026-07-06, access: full, locator: "section 'Review returns for red flags before sign-off'" }
    - { ref: TSCPA-2026, title: "AI at the IRS - What It Means for Practitioners", publisher: Tennessee Society of CPAs, type: professional-body, url: "https://tscpa.com/ai-at-the-irs-what-it-means-for-practitioners/", date: 2026, access: full, locator: "section 'What This Means for Tax Preparers' (page undated; written after the March 2026 GAO report)" }
    - { ref: ACCTODAY-2026, title: "What does an AI-driven IRS mean for small accounting firms?", publisher: Accounting Today (author at Ledger Labs), type: press, url: "https://www.accountingtoday.com/opinion/what-does-the-new-ai-driven-irs-mean-for-small-accounting-firms", date: 2026-07-02, access: full, locator: "'How small firms should respond: 5 practical steps', steps 2 and 3" }
  last_reviewed: 2026-10-17
  notes: "TaxGPT's Agent Andrew (return-review agent that 'surfaces audit-sensitive items', 24 Mar 2026) is the compliance module's; see section 4. The author of ACCTODAY-2026 works at a vendor (Ledger Labs) and several claims in it could not be traced."

- id: tax-controversy-05
  title: Transfer pricing documentation checked against public data to anticipate authority challenge
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [review-assurance, document-production]
  pattern: reconcile-exceptions
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: announced
  problem: "Authorities now use technology to review documentation. EY's global TP controversy leader puts it as 'documentation prepared today will be reviewed by the technology of tomorrow'. Inconsistencies between files and public data can invite challenge."
  solution: "EY describes TP Doc Insights, a GenAI tool that identifies discrepancies between existing TP documentation and publicly available data so teams can address areas likely to draw attention. KPMG says GenAI can help in TP controversy by reviewing historical documents and formulating responses."
  outcomes:
    - lever: risk
      description: "No outcome published. EY frames the tool as moving from reactive to defence-ready compliance."
      figure: "none published"
      measures: "no measure given"
      provenance: vendor-published
      source_ref: EY-TAXRISK-2025
  prerequisites:
    - "Documentation and supporting data in a form the tool can read."
    - "Public data sources for comparison."
  risks_and_guardrails:
    - "IRS LB&I official: AI can support but not replace legal, economic and factual judgment; expert witnesses should explain inputs, assumptions, methods and AI tools; the IRS wants to see the formulas (IRS-LBI-TP-2026)."
  human_checkpoints:
    - "TP professionals review flagged discrepancies; the IRS expects human judgment to remain (IRS-LBI-TP-2026)."
  role_evolution: "No role change is described in the sources."
  evidence_grade: C
  sources:
    - { ref: EY-TAXRISK-2025, title: "2025 EY Tax Risk and Controversy survey", publisher: EY, type: survey, url: "https://www.ey.com/en_gl/insights/tax/tax-risk-and-controversy-survey", date: 2025-12-11, access: full, locator: "box 'Case study: How GenAI can make transfer pricing files consistent'" }
    - { ref: KPMG-TP-2025, title: "GenAI Revolutionizes Transfer Pricing and Valuation", publisher: KPMG US, type: firm, url: "https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html", date: 2025, access: full, locator: "opening paragraph (date from URL path; page metadata shows 2026-10-12, probably a later update)" }
    - { ref: IRS-LBI-TP-2026, title: "Report on recent US international tax developments, 31 July 2026", publisher: EY Tax News, type: firm, url: "https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026", date: 2026-07-31, access: full, locator: "paragraphs 1-2 (remarks of the LB&I director of treaty and transfer pricing operations, 29 Jul 2026)" }
  last_reviewed: 2026-10-17
  notes: "Primarily a transfer-pricing item; kept here because it is framed as audit and controversy defence. Exactera's documentation reviewer is routed to transfer-pricing (section 4). The same EY page says 49% of respondents expect to tailor TP documentation to individual tax authorities; this is a survey expectation, not a deployment."

- id: tax-controversy-06
  title: In-house tax functions summarise legislation and dispute files and check consistency of data shared with authorities
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [research-synthesis, review-assurance]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: piloting
  problem: "Controversy teams hold large volumes of internal opinions, memos and meeting minutes and must track proposed external legislation, while data given to authorities has to be consistent."
  solution: "EY's survey says respondents use or expect to use GenAI for three main purposes: analysing and summarising external tax information (especially new and proposed legislation), analysing and summarising internally generated tax information (opinions, memos, meeting minutes), and enhancing the consistency of data shared with tax authorities."
  outcomes:
    - lever: capacity
      description: "Adoption of controversy-focused GenAI by respondents."
      figure: "39% built at least one tax risk or controversy-focused pilot or tool; 30% more have begun integrating GenAI into other key processes"
      measures: "share of the 1,934 senior tax executives surveyed (12 industries, 48 jurisdictions), as stated in the EY page"
      provenance: vendor-published
      source_ref: EY-TAXRISK-2025
    - lever: experience
      description: "Satisfaction with controversy management is higher among GenAI users. EY reads this as a benefit; it is a correlation in a self-selected sample."
      figure: "46% 'very satisfied' among those integrating GenAI in tax controversy vs 31% of those not"
      measures: "share of respondents in each group saying they are very satisfied with their controversy management approach (EY page); the press release words the comparison as 'AI users' vs 'non-AI users'"
      provenance: vendor-published
      source_ref: EY-TAXRISK-2025
  prerequisites:
    - "Data management: EY says GenAI is 'only showcasing' that collecting, cleansing, reporting and analysing data is key."
    - "Talent: securing people who can work with the technology is the biggest barrier, cited by 44% of respondents."
  risks_and_guardrails:
    - "EY says GenAI 'does not replace governance, it raises expectations of it': accountability, documented decision trails and control frameworks (EY-PAPERJAM-2026)."
    - "Survey is by a firm that sells controversy services and answers are self-reported."
  human_checkpoints:
    - "EY says agentic outputs 'should be reviewed by humans'."
  role_evolution: "EY says talent is the leading barrier; no role redesign is described."
  evidence_grade: C
  sources:
    - { ref: EY-TAXRISK-2025, title: "2025 EY Tax Risk and Controversy survey", publisher: EY, type: survey, url: "https://www.ey.com/en_gl/insights/tax/tax-risk-and-controversy-survey", date: 2025-12-11, access: full, locator: "sections 'How GenAI is changing tax controversy' and 'GenAI tools focused on tax controversy'; 44% barrier in the paragraph after the TP case study" }
    - { ref: EY-TAXRISKPR-2025, title: "EY 2025 Tax Risk and Controversy Survey: Tax leaders turn to AI to strengthen tax management as new risks loom", publisher: EY Global newsroom, type: firm, url: "https://www.ey.com/en_gl/newsroom/2025/12/ey-2025-tax-risk-and-controversy-survey-tax-leaders-turn-to-ai-to-strengthen-tax-management-as-new-risks-loom", date: 2025-12-11, access: full, locator: "opening bullets and section 'GenAI is reshaping how businesses manage tax disputes'" }
    - { ref: EY-TAXNEWS-2025, title: "Why AI is poised to make managing tax risk and controversy easier", publisher: EY Tax News Update, type: firm, url: "https://taxnews.ey.com/news/2025-2478-why-ai-is-poised-to-make-managing-tax-risk-and-controversy-easier", date: 2025-12-11, access: full, locator: "paragraph 1" }
    - { ref: EY-PAPERJAM-2026, title: "Tax controversy in a GenAI world", publisher: Paperjam (EY Luxembourg, promotional), type: firm, url: "https://en.paperjam.lu/article/tax-controversy-in-a-genai-world", date: 2026-03-06, access: full, locator: "sections 'Key figures', 'A new approach to tax governance'" }
  last_reviewed: 2026-10-17
  notes: "The press release states 70% have implemented or are integrating at least one GenAI tool for controversy management; the survey page states 'nearly seven in 10' and splits it 39% plus 30%, where the 30% is 'other key processes' rather than a controversy tool. The page text read does not give the share for each of the three purposes. The EY survey PDF was not opened."

- id: tax-controversy-07
  title: Agent drafts responses to audit queries and tracks information requests during an examination
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [document-production, coordination-scheduling]
  pattern: draft-review-loop
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: "During an examination the taxpayer must answer a stream of document and information requests under deadlines, often drawing on the same facts and files used for compliance."
  solution: "EY authors say tax agents can 'draft responses to audit queries' alongside monitoring rule changes and routing exceptions; EY's survey says respondents automate or partly automate responses to tax authority enquiries. A Miller & Chevalier CLE (25 Jun 2025) covered private use of AI in tax controversy and product demonstrations, with no detail published."
  outcomes:
    - lever: speed
      description: "none published"
      figure: "none published"
      measures: "no measure given"
      provenance: vendor-published
      source_ref: BTAX-EY-2025
  prerequisites:
    - "Integration, data lineage traceability and human judgment; the EY authors say sophistication raises the bar on all three."
  risks_and_guardrails:
    - "Privilege: a McDermott Tax Controversy 360 post (seen only in search snippets, not opened) is reported as cautioning about which AI platforms to use and what is shared; not relied on here."
    - "Court and OPR rules on verified submissions apply to anything filed (see 08)."
  human_checkpoints:
    - "EY authors: 'AI should be used to improve the human's review, not to remove the need for the review.'"
  role_evolution: "EY authors: tax departments shift from assembling information to applying judgment and conducting high-quality reviews."
  evidence_grade: C
  sources:
    - { ref: BTAX-EY-2025, title: "AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way", publisher: Bloomberg Tax (authors from EY), type: press, url: "https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way", date: 2025-11-21, access: full, locator: "paragraph 5 (agents 'draft responses to audit queries'); sections 'People, Skills, Culture' and 'Questions for 2026'" }
    - { ref: EY-TAXRISK-2025, title: "2025 EY Tax Risk and Controversy survey", publisher: EY, type: survey, url: "https://www.ey.com/en_gl/insights/tax/tax-risk-and-controversy-survey", date: 2025-12-11, access: full, locator: "section 'How GenAI is changing tax controversy', paragraph after the three purposes" }
    - { ref: MILLER-CLE-2025, title: "Leveraging AI, Big Data, IRS Online Services & Emerging Technology for Tax Controversy Professionals", publisher: Miller & Chevalier, type: conference, url: "https://www.millerchevalier.com/event/leveraging-ai-big-data-irs-online-services-emerging-technology-tax-controversy-professionals", date: 2025-06-25, access: full, locator: "event description" }
  last_reviewed: 2026-10-17
  notes: "A vendor page for an IDR-tracking agent (Cassidy, 'AI tax controversy validation agent') and a vendor case study claiming a 28% fall in audit adjustments at a 78-attorney firm (CleverX) appeared only in search results; the Cassidy URL now returns 404 and the CleverX page returned no readable content, so neither is used."

- id: tax-controversy-08
  title: LLM-assisted research and drafting for Tax Court and IRS submissions, with citation verification as the control
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [research-synthesis, document-production]
  pattern: draft-review-loop
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "Counsel and pro se taxpayers under time and cost pressure use general models to find authorities and draft briefs; models can invent plausible citations."
  solution: "Use is documented mainly through failures. In Clinco, taxpayer's counsel cited four cases for a wet-signature argument and the court described three as likely hallucinations; the court then upheld the IRS determinations. Firms are advised to adopt written AI policies, citation verification logs, second-reviewer cross-checks and training."
  outcomes:
    - lever: risk
      description: "Frequency of hallucinated authorities in Tax Court filings, as seen by one judge."
      figure: "fewer than a dozen instances seen; no sanctions issued by that judge as of 20 Mar 2026"
      measures: "Judge Holmes's recollection in a Bloomberg interview of instances of hallucinatory cases cited before him; not a systematic count"
      provenance: independent
      source_ref: BBG-TAXCT-2026
    - lever: quality
      description: "Share of authorities cited by counsel on one issue in Clinco that the court found apparently hallucinated."
      figure: "3 of 4"
      measures: "cases cited for the wet-signature argument that the court described as likely generated by a large language model (JofA summary of the opinion)"
      provenance: independent
      source_ref: TAXCT-CLINCO-2026
  prerequisites:
    - "Written firm AI policy, training, vetted tools and documented verification (IRS-OPR-2026, item 4 and Best Practices)."
  risks_and_guardrails:
    - "Circular 230 §§10.22, 10.35, 10.36, 10.37 and AICPA SSTS 1.4 place responsibility for accuracy on the practitioner (IRS-OPR-2026; TAXCT-CLINCO-2026)."
    - "Tax Court has no Rule 11 equivalent, but counsel are bound by ABA Model Rules under Tax Court Rule 201(a); IRC §6673 allows penalties up to $25,000 for frivolous or groundless positions (TAXCT-CLINCO-2026; BBG-TAXCT-2026)."
    - "Judge Holmes said a rule requiring certification that AI was not used might not make sense because there are legitimate uses, and the court is 'feeling our way in the dark' (BBG-TAXCT-2026, 'Feeling Our Way')."
    - "The IRS side is not immune: in Khoja v. Commissioner a judge held a 11 March 2026 hearing on an IRS motion that cited a non-existent case and questioned the signing IRS attorney about AI use and safeguards (BBG-TAXCT-2026, 'Protecting Taxpayers')."
  human_checkpoints:
    - "Independent verification of every cited authority against authoritative sources before filing."
  role_evolution: "Responsibility stays with the practitioner; firms add supervisory review and documentation (TAXCT-CLINCO-2026, 'Practical risk management')."
  evidence_grade: C
  sources:
    - { ref: TAXCT-CLINCO-2026, title: "A recipe for sanctions: AI-hallucinated citations in tax", publisher: Journal of Accountancy (AICPA), type: professional-body, url: "https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/", date: 2026-09-01, access: full, locator: "sections 'The apparitions in the briefing', 'A recipe for sanctions', 'Practical risk management', 'Firm policies for responsible AI use in tax practice'" }
    - { ref: BBG-TAXCT-2026, title: "Tax Court Navigates AI Misuse Rules for Self-Represented Filers", publisher: Bloomberg Tax, type: press, url: "https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers", date: 2026-03-20, access: full, locator: "paragraphs 1-3; sections 'Arrow in Quiver', 'Feeling Our Way', 'Protecting Taxpayers'" }
    - { ref: IRS-OPR-2026, title: "Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19)", publisher: IRS Office of Professional Responsibility, type: regulator, url: "https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70", date: 2026-06-24, access: full, locator: "'Real-World Consequences of Improper AI Use'; Regulatory Framework items 1-5" }
  last_reviewed: 2026-10-17
  notes: "Graded C because the filers' organisations are not named in the sources read and the documented outcome is a failure, not a deployment. JofA says Clinco appears to be the first Tax Court case to address potential hallucinations. The Clinco determinations upheld by the court rested on a bank-deposit analysis, not on the citation failure."

- id: tax-controversy-09
  title: Tax authority selects returns and issues for examination with machine-learning models (IRS)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: full-population-testing
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Selection by the older Discriminant Index Function produced a high share of examinations closing with no change, burdening compliant taxpayers and wasting examiner time. Large partnerships are hard to trace through tiers."
  solution: "The IRS integrated statistical and machine-learning techniques into return and issue selection and trained models on current return data rather than historical exam results. SB/SE has a Form 1040 return classification model and a selection model; LB&I has a Line Anomaly Recommender (corporate returns) and a Large Partnership Compliance model."
  outcomes:
    - lever: quality
      description: "SB/SE pilot of the Form 1040 selection model: higher assessment per examination hour, but also higher no-change rates. No deployment decision had been made. Figures are redacted in the public report."
      figure: "not published (redacted)"
      measures: "pilot test results: dollar tax assessment per examination hour and no-change rate (TIGTA, pp. 7-8)"
      provenance: independent
      source_ref: TIGTA-2025
    - lever: risk
      description: "TIGTA found the IRS has not established processes to evaluate whether AI model performance beats prior methods, and LB&I has no data to evaluate the LAR and LPC models' examination results."
      figure: "none published"
      measures: "TIGTA audit finding on the Large Business and International and Small Business/Self-Employed models"
      provenance: independent
      source_ref: TIGTA-2025
    - lever: cost
      description: "Contract spend on the LAR model."
      figure: "$3.9 million between September 2018 and September 2021"
      measures: "amount the IRS spent on two contracts to develop and manage the LAR model (TIGTA, p. 8)"
      provenance: independent
      source_ref: TIGTA-2025
  prerequisites:
    - "Examination results fed back into model training; TIGTA recommended this and a measurement plan to detect model drift, and the IRS agreed subject to staffing and Treasury guidance."
    - "Skills: GAO found staffing cuts left too few skilled employees and no workforce plan (GAO-2026)."
  risks_and_guardrails:
    - "GAO: 126 active use cases at June 2025 (10 in Aug 2022), 65 withheld as sensitive or exempt R&D, 61% (77 of 126) in development, over 25% without benefit information, and no entity responsible for managing AI investments across the agency (GAO-2026)."
    - "Academic work with IRS data (2010-14 audits) found flexible ML selection shifts audit burden from high- to middle-income taxpayers, and fairness corrections cost performance (STANFORD-AUDIT-2022)."
    - "Selection criteria are not published, so practitioners cannot see why a return was chosen."
  human_checkpoints:
    - "TSCPA says humans review AI outputs and make final decisions on audits to pursue (TSCPA-2026); TIGTA did not test this."
  role_evolution: "Examiners receive pre-scored inventory; EisnerAmper says revenue agents are beginning to get generative AI for drafting IDRs and exam reports (secondary, EISNER-IRSAI-2026)."
  evidence_grade: A
  sources:
    - { ref: TIGTA-2025, title: "The IRS Could Leverage Examination Results in AI Examination Case Selection Models and Improve Processes to Evaluate Performance (2025-308-022)", publisher: Treasury Inspector General for Tax Administration, type: regulator, url: "https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf", date: 2025-05-19, access: full, locator: "Highlights; pp. 3 (no-change rates), 7-8 (SB/SE pilot; LAR and LPC), 13-14 (Recommendation 3)" }
    - { ref: GAO-2026, title: "Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522)", publisher: U.S. Government Accountability Office, type: regulator, url: "https://www.gao.gov/products/gao-26-107522", date: 2026-03-24, access: full, locator: "Fast Facts; Highlights 'What GAO Found' paragraphs 1-4; Recommendations 1-8" }
    - { ref: STANFORD-AUDIT-2022, title: "Algorithmic Fairness and Vertical Equity: Income Fairness with IRS Tax Audit Models", publisher: Stanford Law School / FAccT 2022, type: academic, url: "https://law.stanford.edu/publications/algorithmic-fairness-and-vertical-equity-income-fairness-with-irs-tax-audit-models", date: 2022-06-20, access: full, locator: "Abstract" }
    - { ref: EISNER-IRSAI-2026, title: "AI at the IRS: Transforming Tax Enforcement and the Future of Taxpayer Services", publisher: EisnerAmper, type: firm, url: "https://eisneramper.com/insights/tax/ai-irs-transforming-0126", date: 2026-01-27, access: full, locator: "sections 'AI in Audits', 'Concerns with the Expanded Use of AI'" }
    - { ref: TSCPA-2026, title: "AI at the IRS - What It Means for Practitioners", publisher: Tennessee Society of CPAs, type: professional-body, url: "https://tscpa.com/ai-at-the-irs-what-it-means-for-practitioners/", date: 2026, access: full, locator: "section 'AI is Already Influencing Enforcement'" }
  last_reviewed: 2026-10-17
  notes: "Grade A rests on TIGTA's independent assessment of named IRS models; it measures the models' pilot behaviour, not outcomes for taxpayers. TIGTA's report predates the 2025 staffing cuts discussed in GAO-2026. The TIGTA background cites a tax gap of $688 billion for TY2021, $542 billion (79%) from underreporting. The Accounting Today July 2026 piece claims early pilots show the new models outperform prior methods 'by a meaningful margin'; the TIGTA report does not say this (it reports higher no-change rates in the SB/SE pilot)."

- id: tax-controversy-10
  title: AI agents summarise cases and search files in IRS Chief Counsel, Appeals and the Taxpayer Advocate Service
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [research-synthesis, transaction-processing]
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: step
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Disputes and advocacy cases in understaffed units take long to progress; staff spend time finding and summarising case material."
  solution: "Salesforce said Agentforce would be used across the Office of Chief Counsel, Taxpayer Advocate Service and the Office of Appeals for tasks like case summarisation and search. The vendor executive said the agents are built with guardrails and are not allowed to make final decisions or disburse funds."
  outcomes:
    - lever: speed
      description: "Stated aim is to complete cases more quickly. No figure published."
      figure: "none published"
      measures: "no measure given"
      provenance: vendor-published
      source_ref: IRS-AGENTFORCE-2025
  prerequisites:
    - "Platform modernisation: the vendor had worked with the IRS for a few years on basic platform technology in these units."
  risks_and_guardrails:
    - "Agents may not make final decisions or disburse funds (vendor executive, IRS-AGENTFORCE-2025)."
    - "Axios notes the rollout came as the IRS workforce fell by about 25% in 2025."
  human_checkpoints:
    - "Vendor says it does not advocate unreviewed AI processing; humans review and supplement."
  role_evolution: "A senior IRS Chief Counsel technology attorney said it would be 'negligence' not to start using AI tools to go 'head-to-head with some of the law firms' and that staff must adopt change or leave (IRS-AGENTFORCE-2025, 'Driving the news', 'The bottom line')."
  evidence_grade: C
  sources:
    - { ref: IRS-AGENTFORCE-2025, title: "Exclusive: IRS deploys AI agents", publisher: Axios, type: press, url: "https://www.axios.com/2025/11/21/irs-deploys-ai-agents", date: 2025-11-21, access: full, locator: "'Driving the news', 'What they're saying', 'The bottom line' (opened via text mirror)" }
    - { ref: EISNER-IRSAI-2026, title: "AI at the IRS: Transforming Tax Enforcement and the Future of Taxpayer Services", publisher: EisnerAmper, type: firm, url: "https://eisneramper.com/insights/tax/ai-irs-transforming-0126", date: 2026-01-27, access: full, locator: "section 'AI in Taxpayer Services' (secondary, repeats the rollout)" }
  last_reviewed: 2026-10-17
  notes: "Single-source: an exclusive announcement shared with Axios via the vendor, plus one IRS attorney. Whether it is live in Appeals was not confirmed, and no IRS document describing it was found. Appeals outcomes (cycle time, settlement rates) are not published."

- id: tax-controversy-11
  title: AI research assistant for IRS customer-service representatives (Archie)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [research-synthesis, client-interaction]
  pattern: grounded-knowledge-assistant
  ladder: assist
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Customer-service representatives must find answers in the Internal Revenue Manual while on a call; wrong or slow answers feed later notices and disputes."
  solution: "'Archie' is an AI-enabled tool that helps representatives research the Internal Revenue Manual. The National Taxpayer Advocate reports it as part of the Taxpayer 360 project."
  outcomes:
    - lever: capacity
      description: "Availability of the tool; no performance data."
      figure: "available to about 12,000 CSRs"
      measures: "number of customer-service representatives with access, as reported by the National Taxpayer Advocate"
      provenance: independent
      source_ref: NTA-OBJ-2026
  prerequisites:
    - "Taxpayer 360 programme; the NTA says it had not achieved a single integrated taxpayer view by the 2026 filing season."
  risks_and_guardrails:
    - "NTA calls the tools 'promising steps' but Taxpayer 360 'a work in progress'. No accuracy or usage data reported."
  human_checkpoints:
    - "The representative answers the taxpayer; the tool is for research."
  role_evolution: "No role change is described."
  evidence_grade: B
  sources:
    - { ref: NTA-OBJ-2026, title: "National Taxpayer Advocate Fiscal Year 2027 Objectives Report to Congress (Review of the 2026 Filing Season)", publisher: Taxpayer Advocate Service, type: regulator, url: "https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/06/JRC27_FullReport.pdf", date: 2026-06, access: full, locator: "Filing-season review, p. 16, text above 'Online Accounts Provide Valuable Self-Service Options' (only AI mentions read in this long report)" }
  last_reviewed: 2026-10-17
  notes: "Only the AI passages of a report of more than 5,000 lines were read. Archie is a service tool; its link to controversy is indirect (notice and examination questions)."

- id: tax-controversy-12
  title: AI and automation to speed IRS amended-return processing
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [transaction-processing]
  pattern: other
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: "The IRS receives about 5 million amended returns a year; a large backlog built up and individual amended returns could take 12 to 16 weeks."
  solution: "The IRS CIO told staff the IRS is using AI to speed processing of 'hundreds of thousands' of amended returns. The pattern is not described in the source; pattern 'other' (document-heavy transaction processing with AI assistance)."
  outcomes:
    - lever: speed
      description: "Processing time for an amended individual return, before and after AI and automation."
      figure: "from an average of 12, 14 or 16 weeks to under three days"
      measures: "average time to process an amended individual return, per the IRS CIO at an all-staff meeting; the number of returns this applies to is 'hundreds of thousands' of about 5 million received a year"
      provenance: self-reported
      source_ref: IRS-AIFIRST-2026
  prerequisites:
    - "Not stated. Nextgov reports 1,500 IT and HR staff were put on involuntary details to frontline service in February 2026, including to the amended-return backlog."
  risks_and_guardrails:
    - "No error or quality data given. GAO and TIGTA do not cover this tool."
  human_checkpoints:
    - "Not described."
  role_evolution: "IRS CEO: AI 'is not designed to eliminate jobs'; headcount 74,000 at the start and end of the year, after over 4,000 hires (IRS-AIFIRST-2026)."
  evidence_grade: B
  sources:
    - { ref: IRS-AIFIRST-2026, title: "Tax chief pushes 'AI-first IRS' to get more out of agency's workforce", publisher: Nextgov/FCW, type: press, url: "https://www.nextgov.com/artificial-intelligence/2026/10/tax-chief-pushes-ai-first-irs-get-more-out-agencys-workforce/416389/", date: 2026-10-02, access: full, locator: "paragraphs 2-4 and the final eight paragraphs (Pandya and Kweskin statements)" }
  last_reviewed: 2026-10-17
  notes: "Graded B, not A, although it has a before/after figure: amended-return processing is adjacent to controversy, the figure is an executive's oral statement reported by a trade outlet, and no document or independent check was found. The all-staff meeting was Wednesday 30 Sep 2026; the article is dated 2 Oct 2026."

- id: tax-controversy-13
  title: Multi-model confidence flagging of possible fraud, with human review (IRS)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "Fraud screening needs signals from several models and a way to avoid acting on a single model's output."
  solution: "Treasury's AI use case inventory lists a confidence threshold tool that assesses the output of multiple machine-learning models to flag possible fraud, which a human then reviews, and a synthetic data engine to test processing systems and simulate fraud cases. A separate 'Zero Paper AI Routing' agentic tool for mail is pre-deployment."
  outcomes:
    - lever: risk
      description: "No outcome published."
      figure: "none published"
      measures: "no measure given"
      provenance: independent
      source_ref: TREAS-AIINV-2026
  prerequisites:
    - "IT capacity: at least 16 IRS AI use cases involve IT staff, a classification that has shrunk 16% since the start of the administration (per a TIGTA memo cited by FedScoop)."
  risks_and_guardrails:
    - "FedScoop notes the 2024 inventory listed a 'collections chatbot', and a search of the new inventory for 'collections' and 'enforcement' returned no results."
  human_checkpoints:
    - "A person reviews each flagged case."
  role_evolution: "None described."
  evidence_grade: B
  sources:
    - { ref: TREAS-AIINV-2026, title: "IRS ramps up AI use amid staff cuts, Treasury inventory shows", publisher: FedScoop, type: press, url: "https://fedscoop.com/treasury-irs-ai-use-case-inventory/", date: 2026-01-29, access: full, locator: "paragraphs 1-6 and 10-12" }
  last_reviewed: 2026-10-17
  notes: "Inventory counts differ by scope: Treasury inventory reports 61 IRS use cases (49 a year earlier) and 129 Treasury-wide (54 earlier); GAO counted 126 active IRS use cases at June 2025 including 65 sensitive or exempt. The one high-impact IRS use case, 'IRS IaaP Accelerator', is pre-deployment IT tooling and is routed to tax-data-technology."

- id: tax-controversy-14
  title: AI orders substantiation documents for auditors assessing deduction claims (ATO)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: in-production
  problem: "Auditors verifying work-expense claims must sort through large volumes of receipts, invoices and other unstructured documents supplied as substantiation."
  solution: "The ATO's Chief Data Officer says the ATO built AI that reads receipts and invoices, suggests which documents relate to which deduction claim, and puts them in a likely best order for auditors to consider. It asks for feedback and learns from it. Auditors still decide validity."
  outcomes:
    - lever: speed
      description: "Described as saving time and making claims easier to assess. No figure published."
      figure: "none published"
      measures: "no measure given"
      provenance: self-reported
      source_ref: ATO-SPEECH-2026
    - lever: risk
      description: "ANAO assessment of ATO AI governance covering all production models (not this tool specifically)."
      figure: "32 of 43 production AI models (74%) had no completed data ethics assessment"
      measures: "ATO-built AI models in production as of 14 May 2024 without a finalised data ethics assessment as of August 2024 (ANAO para 2.87)"
      provenance: independent
      source_ref: ANAO-ATO-2025
  prerequisites:
    - "Data quality and lineage; the CDO says 'AI doesn't fail, the data does' and that controls are not optional extras."
    - "Approved tools for approved use cases and mandatory human oversight (ATO AI policy as described in the speech)."
  risks_and_guardrails:
    - "ANAO (audit of governance, data from 2024) concluded the ATO had 'partly effective' arrangements and lacked effective arrangements for design, development, deployment and monitoring of AI models; the ATO accepted the recommendations (ANAO-ATO-2025; recommendation count as reported by ONENEWS-2026)."
    - "ATO states adverse decisions affecting taxpayers' rights are made by a human and taxpayers keep a right of review (ATO-AI-2026, 'AI governance')."
  human_checkpoints:
    - "Auditors determine the validity of deduction claims."
  role_evolution: "Staff receive an AI assistant in place of a 'randomly organised digital shoebox' (ATO-SPEECH-2026). Microsoft Copilot was made available to all ATO staff during 2025."
  evidence_grade: B
  sources:
    - { ref: ATO-SPEECH-2026, title: "Speech to Australian Government Data Summit (Andrew Watson, Deputy Commissioner and Chief Data Officer)", publisher: Australian Taxation Office, type: regulator, url: "https://www.ato.gov.au/media-centre/speech-to-australian-government-data-summit", date: 2026-04-22, access: full, locator: "section 'What changed with Generative AI - and what didn't'" }
    - { ref: ANAO-ATO-2025, title: "Governance of Artificial Intelligence at the Australian Taxation Office", publisher: Australian National Audit Office, type: regulator, url: "https://www.anao.gov.au/work/performance-audit/governance-of-artificial-intelligence-the-australian-taxation-office", date: 2025-02, access: full, locator: "Conclusion paras 8-11; para 15; para 2.87 (report date from ONENEWS-2026; the page copy read shows no tabling date)" }
    - { ref: ATO-AI-2026, title: "ATO AI transparency statement", publisher: Australian Taxation Office, type: regulator, url: "https://www.ato.gov.au/about-ato/commitments-and-reporting/information-and-privacy/ato-ai-transparency-statement", date: 2026-07-27, access: full, locator: "sections 'How we use AI in the ATO', 'AI governance'" }
    - { ref: ONENEWS-2026, title: "ATO using AI to scan tax returns: what it knows", publisher: OneNews Australia, type: press, url: "https://www.onenewsaustralia.com/ato-ai-tax-return", date: 2026-08-10, access: full, locator: "sections on the Watson speech and the auditor general" }
  last_reviewed: 2026-10-17
  notes: "The ATO transparency statement date of 27 July 2026 is as reported by ONENEWS-2026; the mirrored copy read shows no update date, and the landscape recorded 27 Feb 2026 from a search snippet. The ANAO's 43 models and the 74% refer to all ATO-built production models in 2024, not to the document-ordering tool described in 2026."

- id: tax-controversy-15
  title: Real-time prompts at lodgment that ask taxpayers to check unusual entries (ATO myTax nudges)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [review-assurance, client-interaction]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: process
  runtime_class: background-agent
  maturity: in-production
  problem: "Errors found after lodgment lead to notices, amendments and disputes."
  solution: "ATO AI models prompt individuals completing their return in myTax to check amounts that do not match what is expected from other taxpayers with similar attributes or earlier years, so mistakes can be fixed before lodging. The ATO also says it may adjust pre-filled data back if a taxpayer changes it and the ATO has high confidence in its information."
  outcomes:
    - lever: quality
      description: "Aim is to help taxpayers get their tax right from the start. No outcome figure in the ATO source."
      figure: "none published"
      measures: "no measure given"
      provenance: self-reported
      source_ref: ATO-AI-2026
  prerequisites:
    - "Third-party reporting of over 600 million transactions a year and more than 100 million prefilled items (ONENEWS-2026 citing ATO pages)."
  risks_and_guardrails:
    - "Pre-fill override and opaque comparison groups create a practitioner issue: records are needed to justify changes (ONENEWS-2026)."
    - "ANAO governance findings apply (see 14)."
  human_checkpoints:
    - "Taxpayer reviews and decides; adverse decisions are made by a human (ATO-AI-2026)."
  role_evolution: "Preparers face a data-matched baseline when changing pre-filled figures (ONENEWS-2026)."
  evidence_grade: B
  sources:
    - { ref: ATO-AI-2026, title: "ATO AI transparency statement", publisher: Australian Taxation Office, type: regulator, url: "https://www.ato.gov.au/about-ato/commitments-and-reporting/information-and-privacy/ato-ai-transparency-statement", date: 2026-07-27, access: full, locator: "'Examples of how we use AI: Tax time nudging'" }
    - { ref: ONENEWS-2026, title: "ATO using AI to scan tax returns: what it knows", publisher: OneNews Australia, type: press, url: "https://www.onenewsaustralia.com/ato-ai-tax-return", date: 2026-08-10, access: full, locator: "sections 'Your bank, your employer and your crypto exchange all report in' and 'Andrew Watson says an AI assistant sorts the receipts'" }
    - { ref: GT-IE-OECD-2025, title: "Governing with AI: The new face of tax authorities", publisher: Grant Thornton Ireland, type: firm, url: "https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/", date: 2025-09-19, access: full, locator: "section 'Detecting tax fraud with algorithms'" }
  last_reviewed: 2026-10-17
  notes: "Grant Thornton Ireland, summarising the OECD, says ATO used real-time analytics to flag anomalies across more than 600,000 taxpayer interactions that generated close to AUD 80 million in revenue in one year. This is a secondary summary of an OECD report that was not opened, so the figure is not used as an outcome."

- id: tax-controversy-16
  title: ATO prioritises enterprise AI for case profiling, triage of taxpayer requests and drafting position papers
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [research-synthesis, document-production, transaction-processing]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "Isolated experiments ('a thousand flowers blooming') risk duplication and weak assurance; case work is information-heavy."
  solution: "The ATO executive prioritised seven enterprise AI use cases, including case profiling assistants that assemble facts and map them to legislation and policy, triage of unstructured taxpayer requests, drafting of position papers and structured correspondence, and assistants that assemble evidence against policy criteria. The CDO says the decision remains with a person and calls agentic AI 'the next frontier'."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "no measure given"
      provenance: self-reported
      source_ref: ATO-SPEECH-2026
  prerequisites:
    - "Reusable platforms, assurance and ethics checks, business-led ownership and change management (ATO-SPEECH-2026, 'From experimentation to industrialisation')."
  risks_and_guardrails:
    - "ATO test: 'if we can't explain it, defend it, or audit it - we shouldn't deploy it'. Human oversight is mandatory and accountability sits with people."
    - "ANAO found gaps in assurance, approval and monitoring of ATO AI models (see 14)."
  human_checkpoints:
    - "Decisions remain with people; drafts stay subject to human review."
  role_evolution: "AI 'is not about replacing people'; staff judgment and empathy stay at the core (ATO-SPEECH-2026, Closing)."
  evidence_grade: C
  sources:
    - { ref: ATO-SPEECH-2026, title: "Speech to Australian Government Data Summit (Andrew Watson, Deputy Commissioner and Chief Data Officer)", publisher: Australian Taxation Office, type: regulator, url: "https://www.ato.gov.au/media-centre/speech-to-australian-government-data-summit", date: 2026-04-22, access: full, locator: "section 'From experimentation to industrialisation: 7 priority use cases'" }
  last_reviewed: 2026-10-17
  notes: "Announced priorities, not deployments. ATO's own statement (ATO-AI-2026) says it is expanding enterprise generative AI use."

- id: tax-controversy-17
  title: HMRC plans AI for caseworkers, risk targeting and agentic case management
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [review-assurance, research-synthesis]
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: managed-agent-runtime
  maturity: announced
  problem: "HMRC needs to close the tax gap while moving most customer contact online."
  solution: "HMRC's Transformation Roadmap (as summarised by ICAS) lists new risk-targeting capabilities using AI, collaboration with the private sector to test AI, and giving caseworkers generative AI to summarise case documents and answer queries. It names agentic AI for case management and process automation."
  outcomes:
    - lever: capacity
      description: "Target digital share of customer interactions (not an AI outcome)."
      figure: "at least 90% digital by 2030; about 76% at the time of the roadmap"
      measures: "share of HMRC customer interactions that happen online (roadmap, via ICAS)"
      provenance: self-reported
      source_ref: ICAS-HMRCAI-2025
  prerequisites:
    - "Responsible AI commitments aligned with government AI frameworks and HMRC's Charter standards."
  risks_and_guardrails:
    - "An R&D adviser's FOI request led HMRC to say its R&D compliance team did not use generative AI for claims and that it was 'not approved for use in generating taxpayer letters'; the Financial Times, as reported by ICAS, also reported suggestions that some caseworkers may have used AI without authorisation. ICAS says the case shows the need for transparency and controls."
  human_checkpoints:
    - "Caseworkers make decisions with AI-generated summaries (roadmap, via ICAS)."
  role_evolution: "HMRC is introducing AI tools for telephony advisers to cut administrative time (ICAS)."
  evidence_grade: C
  sources:
    - { ref: ICAS-HMRCAI-2025, title: "HMRC's plans for AI", publisher: ICAS, type: professional-body, url: "https://www.icas.com/news-insights-events/news/tax/hmrc-s-plans-for-ai", date: 2025-10-29, access: full, locator: "sections 'The strategic approach', 'Specific examples from the roadmap', 'Potential pitfalls'" }
    - { ref: HMRC-ROADMAP-2025, title: "HMRC's Transformation Roadmap", publisher: HMRC (GOV.UK), type: regulator, url: "https://www.gov.uk/government/publications/hmrc-transformation-roadmap", date: 2025-07-21, access: full, locator: "publication landing page only; roadmap text not read" }
  last_reviewed: 2026-10-17
  notes: "A reported Quantexa contract for HMRC appeared only on mirrored copies of one article on unrelated domains and could not be traced to HMRC, so it is not used. The Financial Times article behind the FOI case was not opened."

- id: tax-controversy-18
  title: Generative AI drafts answers for state tax agency customer-service agents (California CDTFA)
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [client-interaction, research-synthesis]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: step
  runtime_class: shared-team-skills
  maturity: in-production
  problem: "Taxpayer queries need accurate, timely answers; wrong advice can lead to penalties and disputes."
  solution: "CDTFA launched a generative AI tool on 22 August 2025 that drafts answers from department reference materials (publications, law guides, website content); a customer service agent decides when a response is appropriate. Agents had begun logging in and had already used it in taxpayer interactions."
  outcomes:
    - lever: quality
      description: "No accuracy or usage figure published."
      figure: "none published"
      measures: "no measure given"
      provenance: self-reported
      source_ref: CDTFA-2025
  prerequisites:
    - "Curated agency reference content."
  risks_and_guardrails:
    - "Experts asked whether taxpayers would be penalised for relying on bad AI-generated advice; CDTFA responses suggest taxpayers can challenge incorrect advice only if given in writing. A civil-liberties advocate called it an 'extremely high-risk use case' (CDTFA-2025)."
    - "The Werfel risk register lists over-trust and unauthorised reliance, with a scenario where a chatbot says a taxpayer qualifies and the deduction is later disallowed on audit, creating possible estoppel claims (AICPA-WERFEL-2026, Appendix A, risk 4)."
  human_checkpoints:
    - "Customer service agent decides when to use the response."
  role_evolution: "Agents become reviewers of drafted answers."
  evidence_grade: B
  sources:
    - { ref: CDTFA-2025, title: "Experts Urge Caution as State Tax Agencies Deploy Generative AI", publisher: Tax Notes (copy hosted by American University Kogod), type: press, url: "https://kogod.american.edu/hubfs/experts_urge_caution_as_state_tax_agencies_deploy_generative_ai_20250826-161144.pdf", date: 2025-08-26, access: full, locator: "pp. 1-2" }
    - { ref: AICPA-WERFEL-2026, title: "A Risk Framework for the Use of AI in Tax Administration and Preparation, Appendix A: AI Risk Register for Tax Authorities", publisher: The Tax Adviser (AICPA), type: professional-body, url: "https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf", date: 2026-08-31, access: full, locator: "Appendix A, risk 4 'Over-Trust / Unauthorized Reliance' (article dated 31 Aug 2026; appendix PDF uploaded under a June 2026 path)" }
    - { ref: GT-IE-OECD-2025, title: "Governing with AI: The new face of tax authorities", publisher: Grant Thornton Ireland, type: firm, url: "https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/", date: 2025-09-19, access: full, locator: "sections 'Personalised and proactive taxpayer services', 'The trust factor' (secondary, OECD summary)" }
  last_reviewed: 2026-10-17
  notes: "The same Grant Thornton summary of the OECD report says France uses natural-language AI to triage taxpayer emails and draft replies that staff validate, and South Korea routes sensitive chatbot queries to humans. These are secondary and not graded here. The CDTFA is a state agency; no federal IRS equivalent with published controls was found."

- id: tax-controversy-19
  title: AI-assisted drafting of Taxpayer Advocate reports with staff verification
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [document-production]
  pattern: draft-review-loop
  ladder: augment
  change_scope: step
  runtime_class: personal-assistant
  maturity: in-production
  problem: "The advocacy office produces long reports to Congress with limited staff."
  solution: "The National Taxpayer Advocate's FY2027 Objectives Report discloses that portions were developed with the assistance of AI and that all AI-assisted content was reviewed, verified and approved by TAS staff."
  outcomes:
    - lever: capacity
      description: "none published"
      figure: "none published"
      measures: "no measure given"
      provenance: self-reported
      source_ref: NTA-OBJ-2026
  prerequisites:
    - "Staff review process."
  risks_and_guardrails:
    - "Disclosure statement and staff verification are the stated controls."
  human_checkpoints:
    - "TAS staff review, verify and approve all AI-assisted content."
  role_evolution: "None described."
  evidence_grade: B
  sources:
    - { ref: NTA-OBJ-2026, title: "National Taxpayer Advocate Fiscal Year 2027 Objectives Report to Congress", publisher: Taxpayer Advocate Service, type: regulator, url: "https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/06/JRC27_FullReport.pdf", date: 2026-06, access: full, locator: "front matter, AI assistance statement after the table of contents" }
  last_reviewed: 2026-10-17
  notes: "A tax-authority-adjacent office; included as a named, disclosed example of AI drafting in dispute-advocacy documents."

- id: tax-controversy-20
  title: "Idea: preventive controls and real-time data exchange with tax authorities instead of after-the-fact audit defence"
  archetype: tax
  module: controversy
  function: service-delivery
  work_types: [data-reporting, review-assurance]
  pattern: monitor-diagnose-act
  ladder: augment
  change_scope: model
  runtime_class: background-agent
  maturity: emerging
  problem: "As authorities move to real-time, data-driven models (Deloitte's 'Tax Administration 3.0'), more frequent granular data requests and anomaly detection can lead to more audits, and detective controls and reactive issue management 'would become unsustainable'."
  solution: "Deloitte's scenario framework says companies would need upstream data quality and preventive controls embedded in business processes, and links the scenario to authority AI progress. EY says the days of defending old positions in audits are giving way to real-time interactions and that this may reduce flash points. Labelled idea: both are discussion pieces, not reported deployments."
  outcomes:
    - lever: risk
      description: "none published"
      figure: "none published"
      measures: "no measure given"
      provenance: vendor-published
      source_ref: DELOITTE-TTT-2026
  prerequisites:
    - "Upstream data quality, integration between tax, finance and operations, and AI validation capability (DELOITTE-TTT-2026, scenarios 3 and 4)."
  risks_and_guardrails:
    - "Scenario framework, not a forecast; explainability and audit trails are listed as requirements."
  human_checkpoints:
    - "Human judgment remains instrumental; experts validate AI outputs."
  role_evolution: "Talent shifts toward data analytics, technology integration and project management (scenario 3); tax professionals move from preparation to oversight, interpretation, policy interaction and dispute resolution (scenario 4)."
  evidence_grade: D
  sources:
    - { ref: DELOITTE-TTT-2026, title: "Riding the wave: A framework to plan for AI (Tax Transformation Trends, AI report part three)", publisher: Deloitte Global, type: firm, url: "https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf", date: 2026-07, access: full, locator: "pp. 6-7, scenarios 3 and 4 (date from PDF metadata, 2 Jul 2026)" }
    - { ref: EY-TAXRISK-2025, title: "2025 EY Tax Risk and Controversy survey", publisher: EY, type: survey, url: "https://www.ey.com/en_gl/insights/tax/tax-risk-and-controversy-survey", date: 2025-12-11, access: full, locator: "introduction, paragraph on real-time interactions" }
  last_reviewed: 2026-10-17
  notes: "Idea label: discussed by firms; no deployment found."
```

## 3. Module notes

**Processes, key steps and work types**
- Return and issue selection by the authority (review-assurance, data-reporting): scoring, classification, ranking. Practitioner side has no view into it.
- Notice intake and triage (transaction-processing): read notice, tie to return, identify issue, deadline and amount; open power of attorney; route.
- Notice response (document-production, expert-judgment): choose agree, partial agree or disagree, penalty abatement or reasonable cause; draft client explanation and agency letter; assemble substantiation.
- Examination (coordination-scheduling, document-production, review-assurance): track and answer information document requests, support interviews and workpapers, test proposed adjustments.
- Appeals and protest (document-production, expert-judgment): written protest, settlement and alternative dispute resolution. No AI practice evidence for Appeals on the taxpayer side was found. On the IRS side, Appeals is named in the Agentforce announcement.
- Litigation (research-synthesis, document-production): research and briefs. This is the step with the most public AI incidents.
- Pre-filing risk review (review-assurance): reconcile to third-party data, document support, flag audit-sensitive items.
- Authority service and advocacy (client-interaction): chatbots, agent-assist tools, advocacy reports.

**Common pain points**
- Notices are issued by computers while human capacity to resolve them has fallen. The IRS lost over a quarter of its workforce in 2025; headcount is now flat at about 74,000 (IRS-AIFIRST-2026). A practitioner article says resolution takes longer while notices arrive faster; it is opinion, not measurement (ACCTODAY-2026).
- First read of a notice is slow and inconsistent between practitioners (WK-NOTICE-2026).
- Authority AI is opaque: selection criteria are not published (ACCTODAY-2026, TSCPA-2026).
- Data: EY finds data management is central; talent is the top barrier (44%) (EY-TAXRISK-2025).
- Silent failure: TEI attendees described AI that 'fails quietly and even politely' and said the tax function rarely owns AI implementation (TEI-TAXTECH-2026).

**Metrics and benchmarks (with sources)**
- EY 2025 survey, 1,934 senior tax executives, 12 industries, 48 jurisdictions: 87% expect GenAI to improve controversy management; 39% built at least one controversy-focused pilot or tool; 30% more integrating GenAI into other processes; 46% vs 31% 'very satisfied'; 91% of AI users somewhat or very satisfied (EY-TAXRISK-2025). Self-reported, firm-published.
- IRS AI inventory: 126 active use cases at June 2025 (10 in Aug 2022); 61% in development; over 25% lacked benefit information (GAO-2026). Treasury inventory: IRS 61 use cases, up from 49; Treasury 129, up from 54 (TREAS-AIINV-2026).
- IRS amended returns: average 12 to 16 weeks down to under three days; 'hundreds of thousands' of about 5 million a year (IRS-AIFIRST-2026, self-reported).
- IRS compliance rate: about 85% now; CEO envisions mid-90s in five years (IRS-AIFIRST-2026).
- ATO: 43 AI models in production in 2024; 74% without a completed data ethics assessment (ANAO-ATO-2025).
- OECD Forum on Tax Administration: 70% of 54 members using AI tools, 80% with a digital transformation strategy; most common use is detecting evasion and fraud (OECD-DIGIT-2025, 2024 data, via Bloomberg Tax).
- Tax Court: three-quarters of cases pro se; fewer than a dozen hallucinated-citation instances seen by one judge (BBG-TAXCT-2026).
- No published error rates, override rates, parallel-run results or time measurements for practitioner-side notice, IDR or Appeals tools. TIGTA's no-change-rate metric is the one outcome measure used by an authority (TIGTA-2025, p. 3).

**Guardrails and regulatory points**
- IRS OPR Alert 2026-19 applies Circular 230 §§10.22 (due diligence), 10.27(a) (fees), 10.35 (competence), 10.36 (firm procedures), 10.37 (written advice) and IRC §§6713 and 7216 to AI; cites ABA Formal Opinion 512; recommends documenting AI use and treating AI text as drafts (IRS-OPR-2026).
- AICPA SSTS Section 1.4 (reliance on tools) keeps responsibility with the member (TAXCT-CLINCO-2026).
- Tax Court: Rule 201(a) binds counsel to ABA Model Rules; IRC §6673 penalty up to $25,000; no AI certification rule adopted (BBG-TAXCT-2026).
- IRS LB&I (29 Jul 2026): expert witnesses should explain inputs, assumptions, methods and AI tools; the IRS wants to see formulas (IRS-LBI-TP-2026).
- Authority governance: GAO's eight recommendations, all accepted by IRS (GAO-2026); TIGTA's three (TIGTA-2025); ANAO's findings for ATO (ANAO-ATO-2025); ATO commits that adverse decisions are made by a human (ATO-AI-2026); Werfel's risk register for authorities, including chatbot over-trust and estoppel (AICPA-WERFEL-2026).
- EU AI Act: no dedicated category for tax administration systems, so whether they are high-risk is unclear (HADWICK-EUAIACT, 2024 paper on the proposal; EU Digital Omnibus delay proposals not verified).
- Australia: Privacy Act automated-decision disclosure changes from 10 Dec 2026 (ONENEWS-2026; secondary, not checked against the legislation).

**Frontier signals (dated)**
- 2025-07-21: HMRC roadmap names agentic AI for case management (ICAS-HMRCAI-2025).
- 2025-11-21: IRS announces Agentforce for Chief Counsel, TAS and Appeals (IRS-AGENTFORCE-2025).
- 2025-12-11: EY survey says days of defending old positions are giving way to real-time interactions (EY-TAXRISK-2025).
- 2026-01-29: Treasury inventory lists agentic IRS tools, both pre-deployment (TREAS-AIINV-2026).
- 2026-03-20: Tax Court starting to weigh guardrails (BBG-TAXCT-2026).
- 2026-04-22: ATO CDO says agentic AI is the next frontier (ATO-SPEECH-2026).
- 2026-06-24: OPR guidance (IRS-OPR-2026).
- 2026-07: Deloitte's four-scenario planning that pairs company AI adoption with authority AI progress (DELOITTE-TTT-2026).
- 2026-10-02: IRS 'AI-first' message (IRS-AIFIRST-2026).

**Workforce and role effects**
- IRS: AI 'is not designed to eliminate jobs' (CEO); headcount flat; GAO found staff cuts removed AI skills (63 employees lost from one analytics group) and there is no AI workforce plan (GAO-2026; IRS-AIFIRST-2026).
- IRS Chief Counsel attorney: adopt change and produce more work, or leave (IRS-AGENTFORCE-2025).
- Practitioners: shift from assembling information to review and judgment (BTAX-EY-2025); OPR expects firms to train staff and supervise (IRS-OPR-2026); pricing pressure noted as OPR warns against billing for time not spent.
- AI governance ownership: in a TEI poll, two hands of more than 50 said the tax function owns AI implementation at their company (TEI-TAXTECH-2026, TR Institute recap).
- AI team structure: no public org charts for controversy AI teams were found. ATO describes AI as business-led and technologist-enabled, with a Chief Data Officer as accountable official (ATO-SPEECH-2026, ATO-AI-2026). IRS has multiple entities overseeing individual use cases but none managing AI investment across the agency (GAO-2026).

**Objections and concerns practitioners raise**
- Hallucinated authorities and the cost of a failed filing (TAXCT-CLINCO-2026).
- Confidentiality and §7216 when client data goes into AI tools (IRS-OPR-2026; FINDSKILL-2026).
- Fee ethics when drafting time falls (IRS-OPR-2026).
- Opacity and bias of authority models; a Stanford study with IRS data found cost to performance when fairness constraints are added (STANFORD-AUDIT-2022); EisnerAmper cites GAO on possible algorithmic bias in audit selection (EISNER-IRSAI-2026).
- Reliance on authority chatbots and whether taxpayers can contest wrong AI advice (CDTFA-2025).
- Discrepancies in secondary commentary: ACCTODAY-2026 attributes to GAO a finding that the IRS lacks controls to document and validate models and says it cites an IRM 10.24.1 on AI in audit selection (10 Feb 2026). Neither appears in the GAO page read, and the IRS IRM URL tried returned 404. Treat both as unverified.

**Interview probes for an advisor**
1. Walk me through the last IRS or state notice that came in: who read it, in what system, how long from receipt to first client contact, and which part could a model summarise without a person re-reading the notice?
2. Where does AI-generated text or a cited authority enter anything you send to the IRS, Appeals or a court, who checks each citation, and is that check logged?
3. Which clients' filings would reconcile differently to third-party reporting (1099-K, 1099-DA, K-1) than to your preparation, and do you reconcile before filing or after the CP2000?
4. How do you price and bill notice and exam work as drafting time falls, and what do your engagement letters say about AI use?
5. Who owns AI in your tax function (tax, IT, legal), and what would you tell an examiner or expert witness about the tools you used?

## 4. Routed to other modules

- **compliance:** TaxGPT Tax Prep Agent and return-review 'Agent Andrew' that surfaces audit-sensitive items, launched 24 Mar 2026, with vendor claims of 45 minutes saved per 1040 and a 90% cut in first-pass prep time (TAXGPT-2026; vendor claims, free portion of the page only).
- **indirect-tax:** Thomson Reuters ONESOURCE Sales and Use Tax AI, 15 Jan 2026, claiming up to 65% less routine reporting time and early customers reporting up to 75% lower audit exposure (TR-ONESOURCE-2026; vendor claims).
- **transfer-pricing:** Exactera ExactMatch and ExactReport, which it says reviews documentation against country requirements (EXACTERA-2025; sponsored); IRS LB&I remarks on AI and expert witnesses (IRS-LBI-TP-2026, also used in 05); KPMG's TP GenAI claims (KPMG-TP-2025).
- **tax-data-technology:** Oxford Industries and Savant co-presentation at TEI Tax Technology Seminar, 28 Apr 2026 (SAVANT-TEI-2026; announcement with no outcome); IRS 'IaaP Accelerator' agentic tool for cloud code compliance (TREAS-AIINV-2026); TEI recap themes of silent hallucination, training failures and token costs (TEI-TAXTECH-2026).
- **research-advisory:** Accuracy of AI research tools and hallucinated authorities (Clinco is about research citations as well as advocacy).
- **international-pillar-two:** EY finding that 92% of respondents expect a global minimum tax to increase disputes (EY-PAPERJAM-2026, 'Key figures').
- **professional responsibility (cross-cutting):** OPR Alert 2026-19 and AICPA SSTS Section 1.4 apply to every module.

## 5. Sources

Types: regulator 8, professional-body 5, firm 10, vendor 8, press 11, academic 2, conference 3, survey 1, job-posting 1 (49 listed below counting distinct documents; 25 or more opened across at least nine source types).

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| IRS-OPR-2026 | Introductory Guidelines for Responsible AI Use in Federal Tax Practice (Alert 2026-19) | IRS Office of Professional Responsibility | regulator | https://content.govdelivery.com/accounts/USIRS/bulletins/41d6e70 | 2026-06-24 | full |
| TAXCT-CLINCO-2026 | A recipe for sanctions: AI-hallucinated citations in tax | Journal of Accountancy (AICPA) | professional-body | https://www.journalofaccountancy.com/issues/2026/sep/a-recipe-for-sanctions-ai-hallucinated-citations-in-tax/ | 2026-09-01 | full |
| BBG-TAXCT-2026 | Tax Court Navigates AI Misuse Rules for Self-Represented Filers | Bloomberg Tax | press | https://news.bloomberglaw.com/daily-tax-report/tax-court-navigates-ai-misuse-rules-for-self-represented-filers | 2026-03-20 | full |
| GAO-2026 | Artificial Intelligence: IRS Actions Needed to Address Skills Gaps, Information Quality, and Strategic Management (GAO-26-107522) | GAO | regulator | https://www.gao.gov/products/gao-26-107522 | 2026-03-24 | full |
| TIGTA-2025 | The IRS Could Leverage Examination Results in AI Examination Case Selection Models (2025-308-022) | TIGTA | regulator | https://www.tigta.gov/sites/default/files/reports/2025-08/2025308022fr.pdf | 2025-05-19 | full |
| TREAS-AIINV-2026 | IRS ramps up AI use amid staff cuts, Treasury inventory shows | FedScoop | press | https://fedscoop.com/treasury-irs-ai-use-case-inventory/ | 2026-01-29 | full |
| IRS-AIFIRST-2026 | Tax chief pushes 'AI-first IRS' | Nextgov/FCW | press | https://www.nextgov.com/artificial-intelligence/2026/10/tax-chief-pushes-ai-first-irs-get-more-out-agencys-workforce/416389/ | 2026-10-02 | full |
| IRS-AGENTFORCE-2025 | Exclusive: IRS deploys AI agents | Axios | press | https://www.axios.com/2025/11/21/irs-deploys-ai-agents | 2025-11-21 | full |
| NTA-OBJ-2026 | National Taxpayer Advocate FY2027 Objectives Report to Congress | Taxpayer Advocate Service | regulator | https://www.taxpayeradvocate.irs.gov/wp-content/uploads/2026/06/JRC27_FullReport.pdf | 2026-06 | full (AI passages only) |
| EISNER-IRSAI-2026 | AI at the IRS: Transforming Tax Enforcement and the Future of Taxpayer Services | EisnerAmper | firm | https://eisneramper.com/insights/tax/ai-irs-transforming-0126 | 2026-01-27 | full |
| ACCTODAY-2026 | What does an AI-driven IRS mean for small accounting firms? | Accounting Today | press | https://www.accountingtoday.com/opinion/what-does-the-new-ai-driven-irs-mean-for-small-accounting-firms | 2026-07-02 | full |
| ACCTODAY-2019 | Using AI to get ahead of the IRS | Accounting Today | press | https://www.accountingtoday.com/news/using-ai-to-get-ahead-of-the-irs | 2019-10-22 | full |
| TSCPA-2026 | AI at the IRS - What It Means for Practitioners | Tennessee Society of CPAs | professional-body | https://tscpa.com/ai-at-the-irs-what-it-means-for-practitioners/ | 2026 | full |
| MILLER-CLE-2025 | Leveraging AI, Big Data, IRS Online Services & Emerging Technology for Tax Controversy Professionals | Miller & Chevalier | conference | https://www.millerchevalier.com/event/leveraging-ai-big-data-irs-online-services-emerging-technology-tax-controversy-professionals | 2025-06-25 | full |
| TEI-MIDYEAR-2026 | TEI Midyear Conference 2026 At a Glance agenda | Tax Executives Institute | conference | https://www.tei.org/sites/default/files/MY%202026%20At%20a%20Glance%20Agenda_rev3.2_0.pdf | 2026-03-17 | full |
| TEI-TAXTECH-2026 | 2026 TEI Tax Technology Seminar: All eyes on the Man Behind the Curtain | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/2026-tei-tax-tech-man-behind-the-curtain | 2026-05-04 | full |
| SAVANT-TEI-2026 | Savant Brings Audit-Ready AI to Tax Leaders at TEI Tax Tech Seminar 2026 | Savant Labs | vendor | https://savantlabs.io/press/tei-tax-tech-2026-ai-tax-automation/ | 2026-04-16 | full |
| WK-NOTICE-2026 | How to respond to IRS notices with a clear, structured workflow | Wolters Kluwer Tax and Accounting | vendor | https://www.wolterskluwer.com/en/expert-insights/how-to-respond-to-irs-notices-with-a-clear-structured-workflow | 2026-07-06 | full |
| WK-DOCAN-2026 | 5 ways CCH AnswerConnect Document Analysis helps make tax work faster | Wolters Kluwer Tax and Accounting | vendor | https://www.wolterskluwer.com/en/expert-insights/5-ways-cch-answerconnect-document-analysis-helps-make-tax-work-faster | 2026-07-06 | full |
| TR-COCOUNSEL-2026 | Meet CoCounsel Tax (demo page) | Thomson Reuters | vendor | https://taxprof.thomsonreuters.com/meet-cocounsel-tax-26 | 2026 | full |
| TR-ONESOURCE-2026 | Thomson Reuters Launches AI Tax Compliance Solution (ONESOURCE Sales and Use Tax AI) | Thomson Reuters | vendor | https://thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk | 2026-01-15 | full |
| TAXGPT-2026 | TaxGPT Releases Autonomous Tax Workflow Agent | CPA Practice Advisor | press | https://www.cpapracticeadvisor.com/2026/03/24/taxgpt-releases-autonomous-tax-workflow-agent/180159/ | 2026-03-24 | full (free portion) |
| FINDSKILL-2026 | Tax Preparers: Turn a CP2000 Into a Client Answer in 15 Min | FindSkill.ai | vendor | https://findskill.ai/blog/tax-preparers-cp2000-ai-workflow/ | 2026-08-01 | full |
| EY-TAXRISK-2025 | 2025 EY Tax Risk and Controversy survey | EY | survey | https://www.ey.com/en_gl/insights/tax/tax-risk-and-controversy-survey | 2025-12-11 | full |
| EY-TAXRISKPR-2025 | EY 2025 Tax Risk and Controversy Survey: Tax leaders turn to AI | EY Global newsroom | firm | https://www.ey.com/en_gl/newsroom/2025/12/ey-2025-tax-risk-and-controversy-survey-tax-leaders-turn-to-ai-to-strengthen-tax-management-as-new-risks-loom | 2025-12-11 | full |
| EY-TAXNEWS-2025 | Why AI is poised to make managing tax risk and controversy easier | EY Tax News Update | firm | https://taxnews.ey.com/news/2025-2478-why-ai-is-poised-to-make-managing-tax-risk-and-controversy-easier | 2025-12-11 | full |
| EY-PAPERJAM-2026 | Tax controversy in a GenAI world | Paperjam (EY Luxembourg) | firm | https://en.paperjam.lu/article/tax-controversy-in-a-genai-world | 2026-03-06 | full |
| BTAX-EY-2025 | AI Is Gaining Grip on Tax Compliance. Tax Pros Must Lead the Way | Bloomberg Tax (EY authors) | press | https://news.bloombergtax.com/tax-insights-and-commentary/ai-is-gaining-grip-on-tax-compliance-tax-pros-must-lead-the-way | 2025-11-21 | full |
| AICPA-WERFEL-2026 | A Risk Framework for the Use of AI in Tax Administration and Preparation (Appendix A) | The Tax Adviser (AICPA) | professional-body | https://www.thetaxadviser.com/wp-content/uploads/sites/2/2026/06/appendices-ai-tax-risk-framework.pdf | 2026-08-31 | full (appendix only) |
| DELOITTE-TTT-2026 | Riding the wave: A framework to plan for AI | Deloitte Global | firm | https://www.deloitte.com/content/dam/assets-shared/docs/services/tax/2026/dttl-deloitte-tax-transformation-trends-ai-report-2025-part-three.pdf | 2026-07 | full |
| KPMG-TP-2025 | GenAI Revolutionizes Transfer Pricing and Valuation | KPMG US | firm | https://kpmg.com/us/en/articles/2025/genai-revolutionizes-transfer-pricing-valuation.html | 2025 | full |
| EXACTERA-2025 | AI is transforming transfer pricing (sponsored) | The Tax Adviser (Exactera) | vendor | https://www.thetaxadviser.com/issues/2025/sep/ai-is-transforming-transfer-pricing/ | 2025-08-31 | full |
| IRS-LBI-TP-2026 | Report on recent US international tax developments, 31 July 2026 | EY Tax News | firm | https://taxnews.ey.com/news/2026-1658-report-on-recent-us-international-tax-developments-31-july-2026 | 2026-07-31 | full |
| ATO-AI-2026 | ATO AI transparency statement | Australian Taxation Office | regulator | https://www.ato.gov.au/about-ato/commitments-and-reporting/information-and-privacy/ato-ai-transparency-statement | 2026-07-27 (per ONENEWS-2026) | full |
| ATO-SPEECH-2026 | Speech to Australian Government Data Summit | Australian Taxation Office | regulator | https://www.ato.gov.au/media-centre/speech-to-australian-government-data-summit | 2026-04-22 | full |
| ANAO-ATO-2025 | Governance of Artificial Intelligence at the Australian Taxation Office | Australian National Audit Office | regulator | https://www.anao.gov.au/work/performance-audit/governance-of-artificial-intelligence-the-australian-taxation-office | 2025-02 (per ONENEWS-2026) | full |
| ONENEWS-2026 | ATO using AI to scan tax returns: what it knows | OneNews Australia | press | https://www.onenewsaustralia.com/ato-ai-tax-return | 2026-08-10 | full |
| HMRC-ROADMAP-2025 | HMRC's Transformation Roadmap | HMRC (GOV.UK) | regulator | https://www.gov.uk/government/publications/hmrc-transformation-roadmap | 2025-07-21 | full (landing page only) |
| ICAS-HMRCAI-2025 | HMRC's plans for AI | ICAS | professional-body | https://www.icas.com/news-insights-events/news/tax/hmrc-s-plans-for-ai | 2025-10-29 | full |
| CDTFA-2025 | Experts Urge Caution as State Tax Agencies Deploy Generative AI | Tax Notes (via Kogod) | press | https://kogod.american.edu/hubfs/experts_urge_caution_as_state_tax_agencies_deploy_generative_ai_20250826-161144.pdf | 2025-08-26 | full |
| GT-IE-OECD-2025 | Governing with AI: The new face of tax authorities | Grant Thornton Ireland | firm | https://www.grantthornton.ie/insights/factsheets/governing-ai-tax-authorities/ | 2025-09-19 | full |
| OECD-DIGIT-2025 | Tax Authorities Increasingly Use AI in Audits, OECD Report Finds | Bloomberg Tax | press | https://news.bloombergtax.com/daily-tax-report/tax-authorities-increasingly-use-ai-in-audits-oecd-report-finds | 2025-06-17 | full |
| HADWICK-EUAIACT | Slipping Through the Cracks, the Carve-outs for AI Tax Enforcement Systems in the EU AI Act | European Papers | academic | https://www.europeanpapers.eu/e-journal/slipping-through-cracks-carve-outs-ai-tax-enforcement-systems-eu-ai-act | 2024-12-30 | full |
| STANFORD-AUDIT-2022 | Algorithmic Fairness and Vertical Equity: Income Fairness with IRS Tax Audit Models | Stanford Law School / FAccT 2022 | academic | https://law.stanford.edu/publications/algorithmic-fairness-and-vertical-equity-income-fairness-with-irs-tax-audit-models | 2022-06-20 | full |
| MERCOR-JOB-2026 | Tax Controversy Specialist / Legal Expert (J.D.) talent network | Mercor | job-posting | https://work.mercor.com/jobs/list_AAABnEvLz6Hhzqkiv5NOcJiJ/tax-controversy-specialist | undated | full |

Notes on a few sources: the MERCOR listing, as fetched, is a standing legal-expert AI evaluation network listing, not a tax-specific role or evidence of firm adoption, and is not used in any use case. SAVANT-TEI-2026, TR-ONESOURCE-2026 and TAXGPT-2026 are used only in section 4. OECD-DIGIT-2025 appears in the module notes only.

## 6. Gaps

- **No named firm or in-house controversy case with metrics.** No published error rate, override rate, parallel-run result, hours saved or fee impact for notice response, IDR handling, Appeals protest drafting or examination support. EY's survey is the only sizeable measure and it is self-reported.
- **Web search budget ran out** before job postings and several firm-specific directions could be searched. No controversy-specific job posting was found; the Mercor page is generic. The AI team structure (who owns controversy AI, reporting lines) is therefore documented only for tax authorities (ATO, IRS) and by a TEI poll, not for firms.
- **Big Four and large-law-firm controversy tools.** Only EY (survey, TP Doc Insights, notice-extraction pilots) and KPMG (one paragraph) were found. PwC, Deloitte and law-firm controversy AI were not reached. The KPMG, Deloitte and PwC controversy pages may be bot-walled.
- **Vendor products unreachable or unverified:** the Cassidy 'AI tax controversy validation agent' page returns 404; the CleverX case study (78-attorney firm, 28% fewer audit adjustments) returned no content; Canopy, TaxDome, Karbon and Drake notice features could not be confirmed; no state or sales-tax audit-defence AI product launch was found.
- **IRS primary documents.** No IRS document on generative AI for revenue agents (EisnerAmper is the only source and is secondary), on IRM treatment of AI (an IRM 10.24.1 reference in ACCTODAY-2026 could not be confirmed), or on Appeals use of Agentforce. TIGTA's FY2026 management challenges report and the Tax Notes Talk episodes on audit-selection bias and the Tax Court Chief Judge were not opened.
- **OECD, IMF and Stanford No. 124 primary pages** were blocked or not reached; OECD figures come from Bloomberg Tax and Grant Thornton summaries.
- **HMRC:** the roadmap text itself, the FT article on the R&D FOI case and the reported Quantexa contract were not reached or could not be traced to a primary source.
- **Dispute outcomes.** No data on whether AI-selected examinations or AI-generated notices produce more or fewer disputes, or on notice error rates (for example the share of CP2000s resolved in the taxpayer's favour).
- **Closed communities** (r/taxpros, TaxProTalk, TEI member sessions) were not reachable; the TEI Midyear 'Managing Tax Notices with AI' lab content was not available beyond its title.
- **Date uncertainty:** ANAO report date (taken from press), ATO transparency statement update date (taken from press), KPMG TP article (URL says 2025, page metadata says 2026-10-12), TSCPA and the TR demo page (undated).
