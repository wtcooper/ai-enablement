# Professional services: acceptance-risk (combined deep dive)

Prepared 2026-10-19. Archetype: professional-services. Module: acceptance-risk (client and engagement acceptance and risk: conflicts checks, client due diligence and KYC, engagement risk assessment, ethics and independence-style checks, engagement letters and client AI terms). Angle: combined (practice, discourse, governance and evidence). Public sources only. Quotations are under 25 words. Pages that carry no date are dated by access (2026-10-19) and say so in `notes`.

## 1. Summary

**Public evidence for this module is thin and mostly vendor-published.** I opened 47 sources (3 more were seen only in search results). Nearly every named deployment comes from a vendor's own case study or press release, mainly Intapp. No independent measurement of AI in conflicts, KYC or acceptance exists in what I could reach. There is no error rate, override rate, false-positive rate from a named organisation, parallel run or inspection finding on AI used for acceptance.

- **Conflicts and intake are the most developed use.** Intapp made its agentic assistant Celeste generally available on 15 Jul 2026. It builds the search strategy, triages hits for expert review and drafts clearance summaries (INTAPP-CONFLICTS-2026; INTAPP-CELESTEGA-2026). BakerHostetler is named as an early adopter, but its CIO's quote is forward-looking ("believe ... can have a very positive impact"). The "10 times the matters" line is a conditional vendor statement, not a result.
- **The measured gains are from workflow digitisation, not AI.** BDO Canada, Sandberg Phoenix and Loeb & Loeb report throughput or cycle-time gains after replacing manual acceptance workflows. Those case studies do not isolate any AI feature, so the grade is capped at B (INTAPP-BDOCA-2025; INTAPP-SANDBERG-2025; INTAPP-LOEB-2021).
- **KYC and client due diligence is where AI is most concrete.** Pinsent Masons co-developed a Xapien LLM-based AML due-diligence report with risk-tiered routing. Grant Thornton UK selected Fenergo to unify KYC, due diligence and engagement acceptance. Both are described in future or expectation terms, by the vendors (XAPIEN-PINSENT-2026; FENERGO-GT-2026). UK practitioners in a Jan 2026 roundtable say AI is used for triage and efficiency, while risk assessment and acceptance decisions stay human-led (VINCI-AML-2026).
- **The tacit-knowledge failure mode is the field's main worry.** A Thomson Reuters Institute "premortem" scenario (hypothetical, not a real case) shows an agent clearing a conflict that only a long-serving colleague would have flagged (TRI-PREMORTEM-2026).
- **Client AI terms are the live new thread.** A conference roundtable, a vendor guide and a regulator-level duty all point the same way: clients are putting AI rules into outside counsel guidelines (OCGs) and engagement letters (JENNER-SANDPIPER-2026; LAYER3-OCG-2026; CALBAR-GENAI-2026). The ILTA 2026 survey shows 8% to 38% of firms, by size band, require client approval for generative AI use (ILTA-TECHSURVEY-2026). I found no firm that tracks client AI restrictions as structured data. That use case is graded D (idea).
- **Ethical walls now have to extend to AI tools.** ABA Opinion 512 and the California guidance both raise cross-matter exposure and ethical-wall bypass (ABA-OP512-2024; CALBAR-GENAI-2026). Intapp and Harvey announced in Feb 2026 a plan to enforce walls inside Harvey (INTAPP-HARVEY-2026).
- **Independence-style checks have almost no AI deployment evidence.** The live discussion is the reverse: when does licensing an AI audit tool become an independence threat for the firm (CIBA-INDEP-2026; IESBA-SNAPSHOT-2026).

**Use cases: 17** (A 0, B 6, C 8, D 3; see the YAML).

## 2. Use cases

```yaml
- id: professional-services-acceptance-risk-01
  title: Agentic conflicts search, hit triage and clearance-summary drafting
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Conflicts analysts build searches, read long hit lists and write up each clearance decision. Volume rises with lateral hiring and
    growth, and the history of a client relationship often sits outside the conflicts database.
  solution: >-
    Intapp says its Celeste assistant builds the search strategy, triages high-risk hits for expert review, drafts a clearance
    summary for each analysis and keeps monitoring integrated data sources for new issues. Checks can be started from the intake
    or CRM system. Experts review the hits and decide.
  outcomes:
    - lever: speed
      description: >-
        Vendor says Celeste surfaces relevant matters, partner experience and prior pitch materials for an urgent client request
        "in minutes rather than hours". No measured study was published.
      figure: "minutes rather than hours"
      measures: >-
        Vendor description of the time to surface relevant matters, partner experience and prior pitch materials for an urgent
        client request; not a measured result and not specific to conflict clearance time.
      provenance: vendor-published
      source_ref: INTAPP-CELESTEGA-2026
    - lever: capacity
      description: >-
        Intapp's chief product officer says that when a conflicts team can clear 10 times the matters, that is a new business model.
        The statement is conditional ("When a conflicts team can ..."), not a reported result.
      figure: "none published (conditional 10x statement)"
      measures: "Conditional vendor-executive statement about matters cleared by a conflicts team; no baseline or sample given."
      provenance: vendor-published
      source_ref: INTAPP-CELESTEGA-2026
  prerequisites:
    - A firm system of record for clients, matters, parties and relationships that the agent can search (Intapp positions Celeste as natively integrated with the firm's systems of record).
    - Documented conflicts methods and playbooks the agent can follow. The Thomson Reuters Institute premortem scenario shows the agent failing where informal rules were never written down.
    - Ethical-wall and need-to-know rules applied to the agent as they apply to people (INTAPP-CELESTEGA-2026).
  risks_and_guardrails:
    - A hypothetical premortem describes an agent clearing a conflict that depended on undocumented history; the scenario is illustrative and not a real incident (TRI-PREMORTEM-2026).
    - California's 2026 guidance says lawyers must not let agentic systems make substantive legal determinations without meaningful lawyer supervision, and that agent access to client files must be scoped and monitored (CALBAR-GENAI-2026).
    - Vendor material reports no accuracy benchmark or independent evaluation (INTAPP-CELESTEGA-2026 reports none; LAWSITES-CELESTE-2026 gives none).
  human_checkpoints:
    - Expert review of triaged hits before clearance.
    - Partner or risk-counsel decision on waivers and screens.
  role_evolution: >-
    BakerHostetler's CIO says the firm has onboarded many clients and complex engagements through lateral growth and believes Celeste can help it evaluate conflicts faster (INTAPP-CELESTEGA-2026). The one conflicts-analyst posting opened lists search, contextual analysis and intake management and requires Intapp, iManage and Aderant experience, with no AI duty visible in the public summary (VIRTUALVOCATIONS-2026).
  evidence_grade: B
  sources:
    - { ref: INTAPP-CELESTEGA-2026, title: "Intapp announces general availability of Celeste, the expert AI coworker for professional firms", publisher: Intapp, type: vendor, url: "https://www.intapp.com/news/general-availability-celeste/", date: 2026-07-15, access: full, locator: "paragraphs 3-7 and supporting quotes (Lowry, Jampol)" }
    - { ref: LAWSITES-CELESTE-2026, title: "Intapp makes Celeste generally available, calling it an AI coworker to run the business side of law firms", publisher: LawSites (LawNext), type: press, url: "https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html", date: 2026-07-16, access: full, locator: "paragraphs on BakerHostetler and playbooks" }
    - { ref: INTAPP-CONFLICTS-2026, title: "AI-powered conflicts management (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/conflicts/", date: 2026-10-19, access: full, locator: "section 'Agentic conflicts clearance'" }
    - { ref: TRI-PREMORTEM-2026, title: "Premortem: Your 2028 agentic AI pilot program failed", publisher: Thomson Reuters Institute, type: press, url: "https://www.thomsonreuters.com/en/insights/articles/premortem-your-2028-agentic-ai-pilot-program-failed", date: 2026-02-18, access: full, locator: "Premortem No. 1, paragraphs on the conflicts check" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Executive Summary p. 2; Duty of Confidentiality pp. 5-6" }
    - { ref: VIRTUALVOCATIONS-2026, title: "Conflicts Analyst (remote job posting)", publisher: Virtual Vocations, type: job-posting, url: "https://www.virtualvocations.com/job/conflicts-analyst-3264522-i.html", date: 2026-09-22, access: full, locator: "Job Summary and Required Qualifications" }
  last_reviewed: 2026-10-19
  notes: >-
    Celeste was previewed in Feb 2026 and made generally available 15 Jul 2026. The BakerHostetler quote is a belief about future impact, so maturity is "piloting", not "in-production". The Legal Technology article that reports conflicts and intake as the use case BakerHostetler took up first was seen in search results only (LEGALTECH-CELESTE-2026, search-only) and is not used for the grade. The product page is undated; the date is the access date.

- id: professional-services-acceptance-risk-02
  title: AI-prepopulated intake requests with role-based risk summaries for reviewers
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [transaction-processing, document-production]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Fee earners must re-key client and matter details into acceptance forms. Reviewers then read long requests to find the conflicts,
    anti-money-laundering (AML) and jurisdiction issues that matter to them.
  solution: >-
    Intapp says Celeste pulls details from emails and files and prepopulates the request in Outlook, validates entries before
    submission, and generates role-based summaries that highlight conflicts, AML risks, jurisdictional risk and strategic fit.
  outcomes:
    - lever: speed
      description: "none published for the AI features. The vendor describes the features only."
      figure: none published
      measures: "not applicable: no figure for AI-prepopulation or summaries was found"
      provenance: vendor-published
      source_ref: INTAPP-INTAKE-2026
  prerequisites:
    - A configured acceptance workflow and form set to prepopulate (see professional-services-acceptance-risk-03).
    - Email and document access for the agent, scoped under the firm's confidentiality rules.
  risks_and_guardrails:
    - California's guidance warns that agents with persistent access to email, document management and client files can expose confidential information across matters if poorly scoped (CALBAR-GENAI-2026).
    - Reviewers who rely on a generated summary may miss what it omits; no omission rate has been published (gap).
  human_checkpoints:
    - Requester confirms prepopulated fields before submission.
    - Reviewers approve or escalate the request.
  role_evolution: >-
    Intapp positions the feature as reducing partner burden on data capture (INTAPP-INTAKE-2026). No firm account of changed roles was found.
  evidence_grade: C
  sources:
    - { ref: INTAPP-INTAKE-2026, title: "AI-driven client onboarding for regulated professional firms (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/intake/", date: 2026-10-19, access: full, locator: "section 'AI-driven intake requests'" }
    - { ref: INTAPP-ACCT-ACCEPT-2026, title: "Business acceptance and continuance solution for accounting firms (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/accounting/client-onboarding-continuance/", date: 2026-10-19, access: full, locator: "section 'Accelerate onboarding...' (AI request summaries)" }
  last_reviewed: 2026-10-19
  notes: "Product pages are undated; the date is the access date. No named customer is tied to these specific AI features."

- id: professional-services-acceptance-risk-03
  title: Risk-based acceptance workflow with scoring, routing, audit trail and generated engagement documents
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [transaction-processing, review-assurance]
  pattern: end-to-end-case-agent
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Acceptance run on email chains, paper and legacy systems takes days to weeks, gives partners no status visibility and tempts
    lawyers to bypass the process.
  solution: >-
    A configured acceptance platform replaces the manual routing. Approval paths follow risk score, jurisdiction, service line and
    counterparty. Conflicts, independence, AML and terms checks are connected, and an audit trail is kept. Approved intake data
    can produce engagement letters. This is the workflow base on which the AI features in use cases 01, 02 and 04 sit. The case
    studies below do not isolate any AI feature.
  outcomes:
    - lever: capacity
      description: "BDO Canada reports more than 5,000 acceptances a month on average since go-live in January 2025, a 38% improvement on what the same resources could process before."
      figure: "38%; more than 5,000 acceptances per month"
      measures: "average acceptances processed per month since go-live in January 2025, compared with what the firm could process before the system with the same resources (source wording)"
      provenance: vendor-published
      source_ref: INTAPP-BDOCA-2025
    - lever: capacity
      description: "Sandberg Phoenix says it can open three times as many matters, with significantly fewer errors."
      figure: "3x (three times more matters)"
      measures: "number of matters the firm opens, compared with its volume before Intapp Conflicts and Intake (source wording; no error figure given)"
      provenance: vendor-published
      source_ref: INTAPP-SANDBERG-2025
    - lever: speed
      description: "Loeb & Loeb says new business that took weeks (never less than a few days) is usually complete in a few hours. Its conflicts team went from about 200 requests a month to sometimes 800."
      figure: "weeks or days to hours; about 200 to sometimes 800 requests per month"
      measures: "time to complete new business intake, as stated by the firm's Systems Integration Manager; requests processed per month by the conflicts team. The case study says firm growth accounts for some of the increase."
      provenance: vendor-published
      source_ref: INTAPP-LOEB-2021
  prerequisites:
    - Integrations to the firm's financial, HR and CRM systems (BDO Canada cited Microsoft Dynamics and Workday as pain points before the change).
    - A firm-wide standard acceptance policy, so the workflow can enforce required fields and approvals (Loeb & Loeb).
    - A cleaned conflicts dataset; BDO Australia moved to a single searchable source across eight offices (INTAPP-BDOAU-2024).
  risks_and_guardrails:
    - The figures describe workflow platforms, not AI, and are reported in vendor-hosted case studies (grade capped at B).
    - Partners keep ultimate responsibility for conflicts clearance (BDO Australia's risk and ethics director, INTAPP-BDOAU-2024).
  human_checkpoints:
    - Partner and risk-team approvals along the configured path.
    - Conflicts reviewers resolve hits.
  role_evolution: >-
    Loeb & Loeb says the project made its "human workflow engine" obsolete (its earlier paper workflow needed a team of four on data entry) and that engagement letters could no longer be overlooked or delayed (INTAPP-LOEB-2021). Sandberg Phoenix says it needed a dedicated intake department and a more sophisticated system as it grew (INTAPP-SANDBERG-2025).
  evidence_grade: B
  sources:
    - { ref: INTAPP-BDOCA-2025, title: "How BDO Canada increased efficiency by 38% during client and engagement acceptance", publisher: Intapp, type: vendor, url: "https://www.intapp.com/case-study/bdo-canada-acceptance-intapp-intake/", date: 2025-08-14, access: full, locator: "Results and 'Enhanced efficiency and accuracy' sections" }
    - { ref: INTAPP-SANDBERG-2025, title: "How Sandberg Phoenix improved efficiency and client service with Intapp Conflicts and Intapp Intake", publisher: Intapp, type: vendor, url: "https://www.intapp.com/case-study/sandberg-phoenix-growth-productivity/", date: 2025-08-13, access: full, locator: "Executive summary; 'Faster, easier intake processes'" }
    - { ref: INTAPP-LOEB-2021, title: "How Loeb & Loeb transformed new business onboarding with Intapp products", publisher: Intapp, type: vendor, url: "https://www.intapp.com/case-study/loeb-and-loeb/", date: 2021-08-16, access: full, locator: "'Business impact of automated intake'" }
    - { ref: INTAPP-BDOAU-2024, title: "How BDO Australia implemented an automated end-to-end conflicts clearance process", publisher: Intapp, type: vendor, url: "https://www.intapp.com/case-study/bdo-australia-implements-automated-conflicts-clearance-process-intapp-conflicts/", date: 2024-01-18, access: full, locator: "'Modernizing a manual clearance process'; 'Reaping the rewards'" }
    - { ref: INTAPP-INTAKE-2026, title: "AI-driven client onboarding for regulated professional firms (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/intake/", date: 2026-10-19, access: full, locator: "section 'Onboarding workflow orchestration'" }
    - { ref: INTAPP-PRACTUS-2026, title: "Practus LLP deploys Intapp's agentic AI solutions to power innovation and growth", publisher: Intapp, type: vendor, url: "https://www.intapp.com/news/practus-auxana-intapp/", date: 2026-09-01, access: full, locator: "paragraph 'Delivering elevated legal services'" }
  last_reviewed: 2026-10-19
  notes: >-
    Practus LLP and Auxana have used Intapp Conflicts and Walls for two years and have now added Intake (vendor announcement, 1 Sep 2026; no figures). Grade capped at B: the measurements are from non-AI workflow platforms in an adjacent form of the same process, and are vendor-published. BDO Australia implemented its system in 2017; the case study was published in 2024. The Loeb & Loeb study is from 2021, outside the 12-18 month window, kept as the clearest before-and-after account. Intapp claims its Conflicts and Intake products are used by more than 10 of the top 25 accounting firms (vendor claim, product pages).

- id: professional-services-acceptance-risk-04
  title: Continuous monitoring and re-screening of client relationships after acceptance
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, data-reporting]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Risk checks happen at onboarding, then clients change owners, face sanctions or litigation, or move into new jurisdictions.
    A UK regulator-data summary suggests re-screening lags: 92% of firms screen new clients against sanctions lists but 79% re-check existing ones.
  solution: >-
    Intapp says its intake platform alerts when client ownership, sanctions status, litigation exposure or jurisdictional risk
    shifts, and triggers strategic reviews when AML, independence or risk-score thresholds are crossed. Celeste is described as
    continuously monitoring integrated data sources for conflicts.
  outcomes:
    - lever: risk
      description: "none published for the monitoring features"
      figure: none published
      measures: "not applicable: no figure for monitoring alerts was found"
      provenance: vendor-published
      source_ref: INTAPP-INTAKE-2026
  prerequisites:
    - Third-party data feeds (Intapp lists sanctions screening, corporate hierarchies and beneficial ownership data) and entity matching between the firm's records and those feeds.
    - Configured thresholds for escalation by risk type.
  risks_and_guardrails:
    - A UK practitioner roundtable says AI and screening tools work when calibrated and governed, but over-reliance without tuning causes alert fatigue (VINCI-AML-2026).
    - Alert volumes and false-positive rates for these features are unpublished (gap).
  human_checkpoints:
    - Risk team triages alerts and decides on strategic review or exit.
  role_evolution: "No firm account found."
  evidence_grade: C
  sources:
    - { ref: INTAPP-INTAKE-2026, title: "AI-driven client onboarding for regulated professional firms (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/intake/", date: 2026-10-19, access: full, locator: "section 'Continuous monitoring and policy enforcement'" }
    - { ref: INTAPP-CONFLICTS-2026, title: "AI-powered conflicts management (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/conflicts/", date: 2026-10-19, access: full, locator: "'Catch conflicts automatically'" }
    - { ref: VINCI-SRA-2025, title: "The SRA releases its 2025 AML annual report. What does it mean for your firm?", publisher: VinciWorks, type: community, url: "https://vinciworks.com/blog/the-sra-releases-its-2025-aml-annual-report-what-does-it-mean-for-your-firm/", date: 2025-11-03, access: full, locator: "list of report findings (sanctions screening of new versus existing clients)" }
    - { ref: VINCI-AML-2026, title: "AML compliance in 2026: What UK law firms are asking now", publisher: VinciWorks, type: community, url: "https://vinciworks.com/blog/aml-compliance-in-2026-what-uk-law-firms-are-asking-now/", date: 2026-01-28, access: full, locator: "Q&A on technology and false positives" }
  last_reviewed: 2026-10-19
  notes: >-
    The 92% and 79% figures are the Solicitors Regulation Authority (SRA) findings as summarised by VinciWorks; the SRA page itself was blocked (Cloudflare), so they are secondary. They describe current practice, not AI. Measures: share of firms reviewed that screen new clients against sanctions lists, and share that re-check existing clients (source wording).

- id: professional-services-acceptance-risk-05
  title: LLM-generated sourced due-diligence report with risk-tiered routing at client onboarding
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [research-synthesis, review-assurance]
  pattern: research-brief
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    Every new client needs AML and bribery screening, so analysts spend hours on low-risk clients while the few risky ones wait
    in the same queue. Xapien describes partners spending up to three hours per client and analysts screening false positives.
  solution: >-
    Pinsent Masons co-developed with Xapien what Xapien calls the legal market's first LLM-powered AML due-diligence tool. The
    tool generates a sourced report on AML, anti-bribery and corruption, and ESG risks and flags risky connections. Low-risk
    reports pass with minimal oversight, medium-risk ones go to the AML team, and high-risk ones need further verification or
    partner consultation.
  outcomes:
    - lever: speed
      description: "Pinsent Masons expects low-risk clients to be cleared in hours rather than days, and a report in around 15 minutes. Both are stated as expectations (future tense)."
      figure: "hours rather than days; around 15 minutes per report"
      measures: "expected time to clear low-risk clients, and expected time for the tool to generate a report (vendor case-study wording: 'expects', 'will generate'); not a measured result"
      provenance: vendor-published
      source_ref: XAPIEN-PINSENT-2026
    - lever: risk
      description: "Xapien's Nov 2025 ebook summary says Pinsent Masons' General Counsel found fee earners losing 2.4 million hours to opening new matters and partners spending up to three hours per client. It describes the problem and does not report a result."
      figure: "2.4 million hours; up to three hours per client (problem statement)"
      measures: "hours fee earners were losing to opening new matters, and partner time per client, as stated in the ebook summary; the period and scope are not given in the text opened"
      provenance: vendor-published
      source_ref: XAPIEN-PINSENT-EBOOK-2025
  prerequisites:
    - Defined risk bands and routing rules (low, medium, high) agreed with the MLRO or equivalent.
    - Disambiguation of entities (Xapien's pitch is fewer false positives from name collisions).
  risks_and_guardrails:
    - UK firms in a Jan 2026 roundtable say AI is used for triage and efficiency, not decision-making; acceptance decisions stay human-led and defensible (VINCI-AML-2026).
    - Roundtable view: electronic checks are strong on scale and consistency but weaker on context, judgment and complex structures (VINCI-AML-2026).
    - The title of the Xapien ebook claims 90% automation and a 16 million pound saving. The body opened does not show how either was calculated, so neither is used as an outcome.
  human_checkpoints:
    - AML team evaluates medium-risk reports; analysts and partners handle high-risk cases.
  role_evolution: >-
    Xapien says analysts can allocate effort to higher-risk cases and apply controls proportionate to each client's risk (XAPIEN-PINSENT-2026).
  evidence_grade: B
  sources:
    - { ref: XAPIEN-PINSENT-2026, title: "Pinsent Masons case study", publisher: Xapien, type: vendor, url: "https://xapien.com/case-studies/pinsent-masons/", date: 2026-10-19, access: full, locator: "sections 'Before Xapien' and 'With Xapien'" }
    - { ref: XAPIEN-PINSENT-EBOOK-2025, title: "How Pinsent Masons automates 90% of client onboarding to save £16m (ebook summary)", publisher: Xapien, type: vendor, url: "https://xapien.com/ebook/how-pinsent-masons-automates-90-of-client-onboarding-to-save-16m/", date: 2025-11-06, access: full, locator: "eBook summary paragraph" }
    - { ref: XAPIEN-IDD-2024, title: "How a law firm merged initial due diligence into client onboarding", publisher: Xapien, type: vendor, url: "https://xapien.com/how-a-law-firm-merged-initial-due-diligence-into-client-onboarding/", date: 2024-02-01, access: full, locator: "paragraphs 'Get a flavour of risk' and 'How one law firm uses Xapien'" }
    - { ref: VINCI-AML-2026, title: "AML compliance in 2026: What UK law firms are asking now", publisher: VinciWorks, type: community, url: "https://vinciworks.com/blog/aml-compliance-in-2026-what-uk-law-firms-are-asking-now/", date: 2026-01-28, access: full, locator: "Q&A on AI providers for background checks and on technology strengths and limits" }
  last_reviewed: 2026-10-19
  notes: >-
    Graded B because Pinsent Masons is a named co-development partner, but the case study is in future tense and publishes no measurement, so maturity is "piloting". The case-study page is undated (access date used). A search summary (not opened) attributed to a Xapien interview figures of 26 days average onboarding before, a 58% cut in AML analysis hours and projected savings; those are search-only and are not used as outcomes. A second Xapien case study (Al Tamimi and Company) was seen in search results only and has no quantified result in the snippet. The 2024 Xapien post is outside the 12-18 month window and describes an unnamed law firm.

- id: professional-services-acceptance-risk-06
  title: Unified KYC, client due diligence and engagement acceptance on an AI-enabled client lifecycle platform
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [transaction-processing, review-assurance]
  pattern: end-to-end-case-agent
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Onboarding, due diligence and engagement acceptance run as separate steps with manual effort, slowing clients' start.
  solution: >-
    Grant Thornton UK selected Fenergo's AI-powered client lifecycle management platform to bring KYC, client due diligence and
    engagement acceptance into one process. Fenergo says this centralises onboarding and supports regulatory compliance.
  outcomes:
    - lever: capacity
      description: "Fenergo says the firm expects to remove thousands of hours of manual effort and onboard clients faster. This is an expectation at selection, not a result."
      figure: "thousands of hours (expected)"
      measures: "manual effort the firm expects to remove through the new onboarding process (source wording: 'expects to remove thousands of hours'); no baseline or period given"
      provenance: vendor-published
      source_ref: FENERGO-GT-2026
  prerequisites:
    - Mapping of the firm's acceptance policy into the platform's workflow.
  risks_and_guardrails:
    - Announcement of selection; implementation status and results were not stated.
  human_checkpoints:
    - Not described in the source.
  role_evolution: "Fenergo says teams are freed to focus on higher-value work (vendor wording)."
  evidence_grade: C
  sources:
    - { ref: FENERGO-GT-2026, title: "Grant Thornton UK selects Fenergo to streamline client onboarding and drive efficiency", publisher: Fenergo, type: vendor, url: "https://resources.fenergo.com/newsroom/grant-thornton-uk-selects-fenergo-to-streamline-client-onboarding-and-drive-efficiency", date: 2026-03-03, access: full, locator: "key takeaways and paragraphs 1-3" }
    - { ref: INTAPP-Q4-2026, title: "Intapp announces fourth quarter and fiscal year 2026 financial results", publisher: Intapp, type: vendor, url: "https://s206.q4cdn.com/284424942/files/doc_earnings/2026/q4/earnings-result/Q4-26-Press-Release.pdf", date: 2026-08-04, access: full, locator: "fiscal 2026 highlights (new clients list)" }
  last_reviewed: 2026-10-19
  notes: >-
    The press release's own date line reads 4 March 2026 while the page shows 3 March 2026; the page date is used. Intapp's Aug 2026 results release also lists Grant Thornton UK among new Intapp clients, without saying for which product; the two are not linked here.

- id: professional-services-acceptance-risk-07
  title: Agentic adverse-media screening of prospective clients (research prototype)
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [research-synthesis, review-assurance]
  pattern: research-brief
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: emerging
  problem: >-
    Keyword-based adverse-media screening produces many false positives and hybrid systems need extensive manual review.
  solution: >-
    Idea: an LLM agent searches the web, retrieves documents and computes an adverse-media score with a written justification, for
    an analyst to review. A 2025 research paper presents an open-source version aimed at financial institutions' AML compliance.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: "not applicable: idea; the abstract opened reports no evaluation metrics"
      provenance: independent
      source_ref: ORBILU-ADVERSE-2025
  prerequisites:
    - Search access, a scoring rubric tied to recognised risk categories, and analyst review.
  risks_and_guardrails:
    - No precision or recall against analysts has been published for professional-services use.
  human_checkpoints:
    - Analyst reviews the score and justification.
  role_evolution: "No source."
  evidence_grade: D
  sources:
    - { ref: ORBILU-ADVERSE-2025, title: "An Agentic LLM Framework for Adverse Media Screening in AML Compliance", publisher: University of Luxembourg (ORBilu repository), type: academic, url: "https://orbilu.uni.lu/handle/10993/67145", date: 2025-12-29, access: full, locator: "abstract" }
  last_reviewed: 2026-10-19
  notes: "Idea. Adjacent field: the paper targets financial institutions, not professional-services firms. Date is the repository listing date; only the abstract was read."

- id: professional-services-acceptance-risk-08
  title: AI extraction and categorisation of client outside counsel guidelines and terms, with enforcement at intake, conflicts and time entry
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [document-production, review-assurance]
  pattern: document-to-decision
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    Each client sends its own guidelines. Managing them on paper or in documents is slow and risky, and teams cannot quickly
    answer questions such as payment or security terms across clients.
  solution: >-
    Fredrikson & Byron's risk counsel says the AI takes a first pass at categorising each obligation in a new client's
    guidelines and she reviews and confirms it. Staff can ask a generative AI feature questions about client terms in Microsoft
    Teams. Intapp says captured terms are surfaced in intake, conflicts and time entry.
  outcomes:
    - lever: speed
      description: "Fredrikson & Byron's risk counsel says she can pull terms across clients much faster than before. No figure is given."
      figure: none published
      measures: "not applicable: qualitative statement ('much faster than before'); no time or volume figure"
      provenance: vendor-published
      source_ref: INTAPP-TERMS-2026
  prerequisites:
    - A central repository of client guidelines tied to the client record.
    - A named owner (risk counsel) to confirm the AI categorisation.
  risks_and_guardrails:
    - The risk counsel reviews every categorisation (INTAPP-FREDRIKSON-2024).
    - Dickinson Wright's risk manager calls the system an AI-assisted solution that speeds review and helps manage ongoing compliance (INTAPP-TERMS-2026); no error rate is published.
  human_checkpoints:
    - Risk counsel confirms categorised obligations before they are enforced.
  role_evolution: >-
    Staff ask the assistant instead of searching the repository or contacting the risk counsel (INTAPP-FREDRIKSON-2024).
  evidence_grade: B
  sources:
    - { ref: INTAPP-FREDRIKSON-2024, title: "How U.S. law firm Fredrikson & Byron centralized and improved management of outside counsel guidelines with Intapp Terms", publisher: Intapp, type: vendor, url: "https://www.intapp.com/case-study/fredrikson-ocgs-intapp-terms/", date: 2024-12-02, access: full, locator: "'Intapp Terms accelerates OCG review'; 'Intapp Assist for Terms offers firm professionals immediate answers'" }
    - { ref: INTAPP-TERMS-2026, title: "Intapp Terms: enforce client obligations everywhere (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/terms/", date: 2026-10-19, access: full, locator: "'Agentic obligation capture' and 'Embedded compliance across workflows'; customer quotes" }
  last_reviewed: 2026-10-19
  notes: >-
    The case study is Dec 2024, older than the 12-18 month window, but it is the only named account of AI in client-terms handling. Product page is undated (access date).

- id: professional-services-acceptance-risk-09
  title: Structured register of client AI restrictions, consents and disclosures applied at matter opening
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, client-interaction]
  pattern: grounded-knowledge-assistant
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: emerging
  problem: >-
    Clients are adding AI rules to outside counsel guidelines and engagement letters (disclosure or consent, approved tools, no
    client data in public models, billing for AI-driven savings). Firms must follow them, and tools differ by client.
  solution: >-
    Idea discussed by practitioners: capture each client's AI terms as structured obligations at intake, check each AI tool against
    the client's list before work starts, and keep a record of which tool touched which matter. Intapp announced a Celeste plug-in
    for ChatGPT Enterprise that lets professionals check captured work against the firm's outside counsel guidelines.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "not applicable: idea; no firm reporting a client-AI-terms register was found"
      provenance: vendor-published
      source_ref: LAYER3-OCG-2026
  prerequisites:
    - Use case 08 (guidelines captured as structured terms).
    - An inventory of the AI tools actually in use; ACCA notes that real use may not match the list of products a firm believes it has authorised (ACCA-ENGLETTERS-2026).
  risks_and_guardrails:
    - California's guidance says a lawyer must follow client instructions or guidelines that restrict AI use (CALBAR-GENAI-2026, Communication row, p. 7).
    - ABA Opinion 512 says lawyers must disclose AI use if the engagement terms or OCGs require it, and that boilerplate engagement-letter wording is not enough for informed consent to input client information into a self-learning tool (ABA-OP512-2024).
    - ACCA says inserting an AI clause will not make an unsafe process safe; policies, training and what happens on the file must support it (ACCA-ENGLETTERS-2026).
  human_checkpoints:
    - Partner or risk counsel agrees any client restriction and how compliance will be monitored (ACCA-ENGLETTERS-2026).
  role_evolution: >-
    A Sandpiper roundtable listed the role of firm general counsel in managing compliance with AI-related guidelines as a session topic (JENNER-SANDPIPER-2026).
  evidence_grade: D
  sources:
    - { ref: JENNER-SANDPIPER-2026, title: "Partner John Storino to speak at Sandpiper Partners' AI and Outside Counsel Guidelines Roundtable", publisher: Jenner & Block, type: conference, url: "https://www.jenner.com/print/v2/content/103115/partner-john-storino-to-speak-at-sandpiper-partners-ai-and-outside-counsel-guidelines-roundtable.pdf", date: 2026-10-08, access: full, locator: "paragraph 2" }
    - { ref: LAYER3-OCG-2026, title: "AI Provisions in Outside Counsel Guidelines: A Compliance Guide for Law Firms", publisher: Layer3 Labs, type: vendor, url: "https://www.layer3labs.io/guides/ai-provisions-outside-counsel-guidelines", date: "2026-09", access: full, locator: "intro and Clauses 1-5" }
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: American Bar Association, type: professional-body, url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: 2024-07-29, access: full, locator: "pp. 7-8" }
    - { ref: ACCA-ENGLETTERS-2026, title: "Engagement letters, AI and PCRT", publisher: ACCA, type: professional-body, url: "https://www.accaglobal.com/gb/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/september/Engagement-letters-AI-and-PCRT.html", date: "2026-09", access: full, locator: "'Contractual risks' and 'Operational and process risks'" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Communication Regarding Generative AI Use, p. 7" }
    - { ref: INTAPP-OPENAI-2026, title: "Intapp collaborates with OpenAI to bring frontier AI to the business of law", publisher: Intapp, type: vendor, url: "https://www.intapp.com/news/intapp-celeste-for-openai-for-law/", date: 2026-09-17, access: full, locator: "section 'Entitled access, wherever lawyers work'" }
    - { ref: ILTA-TECHSURVEY-2026, title: "ILTA Technology Survey 2026 Executive Summary", publisher: ILTA, type: survey, url: "https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf", date: "2026-06", access: full, locator: "Q3.18, p. 5" }
    - { ref: TRI-LEGALWEEK-2026, title: "Couples counseling at Legalweek 2026: firms and clients confront the AI value divide", publisher: Thomson Reuters Institute, type: conference, url: "https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide", date: 2026-03-13, access: full, locator: "paragraphs on line-item transparency and client guidelines" }
  last_reviewed: 2026-10-19
  notes: >-
    Idea, graded D. The Sandpiper entry is an event description (the roundtable was held 8 Oct 2026), so it supports the discussion, not any outcome. The Layer3 guide is vendor content: its claim that the Association of Corporate Counsel publishes sample AI guidelines for outside counsel was not checked at the source (ACC document seen in search only, access blocked). Layer3 date is the page's "updated Sep 7, 2026" line; the page's structured date is 2026-07-07.

- id: professional-services-acceptance-risk-10
  title: Ethical-wall and information-barrier enforcement extended to AI assistants and agents
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, software-systems]
  pattern: monitor-diagnose-act
  ladder: automate
  change_scope: process
  runtime_class: workflow-automation
  maturity: in-production
  problem: >-
    AI assistants that search firm content can reach matters that a person behind an ethical wall may not see, and wall policies
    have historically not extended into AI tools.
  solution: >-
    Nelson Mullins' applications manager says that with Intapp Walls she can point Microsoft Copilot where the firm wants and it
    pulls only from matters the user can access. Intapp and Harvey announced plans to sync wall policies with Harvey's access and
    sharing controls.
  outcomes:
    - lever: risk
      description: "Nelson Mullins' applications manager says she can point Microsoft Copilot where she wants and it will pull only from matters the user is permitted to access. No test result or incident count is published."
      figure: none published
      measures: "not applicable: qualitative customer statement on the Intapp Walls product page; page undated"
      provenance: vendor-published
      source_ref: INTAPP-WALLS-2026
  prerequisites:
    - Matter-level permission data kept current in the wall system.
    - Integrations between the wall system and each AI tool; Intapp lists Harvey, Microsoft Copilot and Celeste.
  risks_and_guardrails:
    - ABA Opinion 512 notes a self-learning tool may disclose information to people in the firm who are barred by an ethical wall, and quotes a Pennsylvania opinion warning that some AI models lack safeguards like ethical walls (ABA-OP512-2024).
    - California's guidance warns that agentic systems may unintentionally disclose confidential information across matters (CALBAR-GENAI-2026).
    - The Harvey-Intapp item is a plan ("announced their plans"), with no named adopting firm or availability date in the release (INTAPP-HARVEY-2026).
  human_checkpoints:
    - Risk or IT teams monitor access reports and blocked attempts (INTAPP-WALLS-2026 describes the reports).
  role_evolution: "No source."
  evidence_grade: B
  sources:
    - { ref: INTAPP-WALLS-2026, title: "Intapp Walls: information barriers for AI in professional firms (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/walls/", date: 2026-10-19, access: full, locator: "section 'Define and manage policies in one place' (Nelson Mullins quote); 'Expand AI securely across your firm'" }
    - { ref: INTAPP-HARVEY-2026, title: "Intapp to partner with Harvey bringing ethical wall enforcement directly into the platform", publisher: Intapp, type: vendor, url: "https://www.intapp.com/news/intapp-harvey-partner/", date: 2026-02-23, access: full, locator: "paragraphs 2-6" }
    - { ref: ABA-OP512-2024, title: "Formal Opinion 512: Generative Artificial Intelligence Tools", publisher: American Bar Association, type: professional-body, url: "https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf", date: 2024-07-29, access: full, locator: "footnote 4 (p. 2) and Confidentiality section (p. 7)" }
    - { ref: CALBAR-GENAI-2026, title: "Practical Guidance for the Use of Generative AI in the Practice of Law", publisher: State Bar of California, COPRAC, type: regulator, url: "https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf", date: "2026-05", access: full, locator: "Duty of Confidentiality, p. 6" }
  last_reviewed: 2026-10-19
  notes: >-
    Graded B on the named Nelson Mullins use of Walls with Copilot; the quote is undated and unmeasured. Intapp claims its walls product is used by more than 70 Am Law 100 firms (vendor claim, product page).

- id: professional-services-acceptance-risk-11
  title: Engagement letters generated from approved intake data and routed for signature
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [document-production]
  pattern: bulk-transformation
  ladder: automate
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Engagement letters get delayed or missed when intake is manual; scope, terms and client-specific AI wording vary.
  solution: >-
    Intapp says the intake platform converts approved intake data into engagement letters and routes them for review and
    signature, enforcing firm policy through automated creation and collection of letters (accounting page).
  outcomes:
    - lever: quality
      description: "none published. Loeb & Loeb says engagement letters 'could no longer be overlooked or delayed' once intake fields were mandatory (workflow, not AI)."
      figure: none published
      measures: "not applicable: qualitative statement in the Loeb & Loeb case study, about a non-AI workflow"
      provenance: vendor-published
      source_ref: INTAPP-LOEB-2021
  prerequisites:
    - Approved clause library, including AI disclosure and consent wording the firm is willing to offer.
  risks_and_guardrails:
    - ABA Opinion 512 says boilerplate engagement-letter wording does not suffice for informed consent to put client information into a self-learning AI tool (ABA-OP512-2024, p. 7).
    - ACCA (UK): disclosure that AI is used belongs in the engagement letter, and where AI is fundamental to the work the client should be told beforehand (ACCA-ENGLETTERS-2026).
  human_checkpoints:
    - Review and signature routing (INTAPP-INTAKE-2026).
  role_evolution: "No source."
  evidence_grade: C
  sources:
    - { ref: INTAPP-INTAKE-2026, title: "AI-driven client onboarding for regulated professional firms (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/intake/", date: 2026-10-19, access: full, locator: "'Generate engagement documentation automatically'" }
    - { ref: INTAPP-ACCT-ACCEPT-2026, title: "Business acceptance and continuance solution for accounting firms (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/accounting/client-onboarding-continuance/", date: 2026-10-19, access: full, locator: "'Engagement letter generation'" }
    - { ref: INTAPP-LOEB-2021, title: "How Loeb & Loeb transformed new business onboarding with Intapp products", publisher: Intapp, type: vendor, url: "https://www.intapp.com/case-study/loeb-and-loeb/", date: 2021-08-16, access: full, locator: "'Business impact of automated intake'" }
  last_reviewed: 2026-10-19
  notes: "I did not find 2026 announcements from accounting practice-management vendors (Karbon, Canopy, TaxDome, Financial Cents) or Clio on AI-drafted engagement letters (search returned none)."

- id: professional-services-acceptance-risk-12
  title: Independence, conflicts and reputational risk signals combined into one acceptance decision
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, expert-judgment]
  pattern: document-to-decision
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Accounting firms must weigh independence, ethics, quality and risk checks for each client and engagement, often from
    spreadsheets and separate systems.
  solution: >-
    Kingland says its acceptance solution pulls relevant data automatically, aggregates independence, conflicts and reputational
    risk signals in one workflow, routes to reviewers for sign-off, and uses configurable rules and automated assessments.
    Its AI platform description mentions confidence scoring and human-in-the-loop oversight. Intapp describes independence tracking
    for audit clients in its accounting intake.
  outcomes:
    - lever: quality
      description: none published
      figure: none published
      measures: "not applicable: product page with no outcome figure"
      provenance: vendor-published
      source_ref: KINGLAND-CEA-2026
  prerequisites:
    - Client and entity data in the firm's systems; a defined independence rule set.
  risks_and_guardrails:
    - IESBA (June 2026) says the Code's principles apply regardless of technology, that accountants must assess fitness for purpose and bias of technology outputs, and names automation bias as a threat to objectivity (IESBA-SNAPSHOT-2026).
    - PCAOB's QC 1000 (a firm quality-control standard) is scheduled to take effect on 15 Dec 2026 after a one-year postponement announced in Aug 2025; the interim standards stay in force until then (PCAOB-QC1000-2025). I did not read QC 1000's text on acceptance and continuance.
  human_checkpoints:
    - Reviewers sign off in routed workflow (KINGLAND-CEA-2026).
  role_evolution: "No source."
  evidence_grade: C
  sources:
    - { ref: KINGLAND-CEA-2026, title: "Client & Engagement Acceptance (product page)", publisher: Kingland, type: vendor, url: "https://www.kingland.com/client-engagement-acceptance", date: 2026-10-19, access: full, locator: "intro paragraphs; 'Value for your Firm'; 'AI Ecosystem'" }
    - { ref: INTAPP-ACCT-ACCEPT-2026, title: "Business acceptance and continuance solution for accounting firms (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/accounting/client-onboarding-continuance/", date: 2026-10-19, access: full, locator: "'Independence tracking'" }
    - { ref: IESBA-SNAPSHOT-2026, title: "IESBA Snapshot: Ethics and Independence Approach to the Use of Technology", publisher: IESBA, type: standard-setter, url: "https://www.ethicsboard.org/news-events/2026-06/iesba-snapshot-ethics-and-independence-approach-use-technology", date: "2026-06", access: full, locator: "Q2, Q4 (automation bias, independence)" }
    - { ref: PCAOB-QC1000-2025, title: "PCAOB postpones effective date of QC 1000 and related standards, rules, and forms", publisher: PCAOB, type: regulator, url: "https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-postpones-effective-date-of-qc-1000-and-related-standards--rules--and-forms", date: "2025-08", access: full, locator: "paragraphs 1 and 'Standards, Rules, and Forms Affected'" }
  last_reviewed: 2026-10-19
  notes: >-
    The PCAOB release was published in Aug 2025 (28 Aug per trade coverage; the day was not confirmed from the release text). As of 19 Oct 2026, QC 1000 is scheduled, not yet in force. Kingland page is undated (access date).

- id: professional-services-acceptance-risk-13
  title: Independence and objectivity assessment of AI tools and AI vendors used on client work
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [expert-judgment, review-assurance]
  pattern: other
  ladder: assist
  change_scope: step
  runtime_class: personal-assistant
  maturity: emerging
  problem: >-
    When a firm licenses an AI audit or review tool, it is unclear when that becomes an independence conflict, for example if the
    same vendor serves the audit client, or trains on the firm's client data.
  solution: >-
    Idea discussed by practitioners: add AI tools to the acceptance and independence assessment. For every tool that touches client
    work, record who owns the vendor, whether it serves the client, what is paid and whether payment depends on volume or
    referrals, and whether the vendor can train on client data.
  outcomes:
    - lever: risk
      description: none published
      figure: none published
      measures: "not applicable: idea"
      provenance: independent
      source_ref: CIBA-INDEP-2026
  prerequisites:
    - An inventory of AI tools and vendors in use.
  risks_and_guardrails:
    - The article says no standard has settled the question; IESBA's technology revisions name automation bias and accountability for outputs, but not the vendor relationship (CIBA-INDEP-2026).
    - IESBA says the independence standards were reinforced for self-review threats, assuming management responsibility and commercial dependencies in technology-enabled services (IESBA-SNAPSHOT-2026, Q4).
  human_checkpoints:
    - Partner judgment using the reasonable and informed third-party test; written disclosure to the client if something uncomfortable is found (CIBA-INDEP-2026).
  role_evolution: "No source."
  evidence_grade: D
  sources:
    - { ref: CIBA-INDEP-2026, title: "AI Audit Tools and the Independence Gap Nobody Fixed", publisher: "Accounting Weekly (author: CIBA quality-assurance manager)", type: professional-body, url: "https://www.accountingweekly.com/trending-news/ai-audit-tools-and-the-independence-gap-nobody-fixed", date: 2026-09-01, access: full, locator: "sections 'Can licensing an AI tool become an independence issue?' and 'What to do about it'" }
    - { ref: IESBA-SNAPSHOT-2026, title: "IESBA Snapshot: Ethics and Independence Approach to the Use of Technology", publisher: IESBA, type: standard-setter, url: "https://www.ethicsboard.org/news-events/2026-06/iesba-snapshot-ethics-and-independence-approach-use-technology", date: "2026-06", access: full, locator: "Q4, Q6, Q7" }
  last_reviewed: 2026-10-19
  notes: >-
    Idea. The article reports that a former PCAOB board member argued in a comment letter on an AICPA independence proposal that the position is unclear, and cites 81 comment letters; I could not confirm the letter count or the proposal's status from other sources. IESBA plans two non-authoritative guidance documents (technology, planned Q3 2026; AI-specific, planned Q4 2026) per the snapshot; neither was found published.

- id: professional-services-acceptance-risk-14
  title: Lateral-hire conflicts pre-screening and clearance preparation by an agent
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, transaction-processing]
  pattern: end-to-end-case-agent
  ladder: delegate
  change_scope: process
  runtime_class: background-agent
  maturity: announced
  problem: >-
    Lateral hires bring client relationships that must be checked for conflicts before the hire is made, and confidential
    information has to be handled carefully.
  solution: >-
    Intapp says Celeste can run an end-to-end lateral hire lifecycle: candidate research, conflicts pre-screening, clearance
    preparation and onboarding. Intapp's intake product also offers lateral candidates a secure portal to share confidential
    details. A blog on law-firm mergers frames merger conflicts clearance as an immediate crisis (title only).
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: "not applicable: announced capability; no result"
      provenance: vendor-published
      source_ref: INTAPP-CELESTEGA-2026
  prerequisites:
    - Conflicts and HR data connected; candidate confidentiality handled through a secure portal.
  risks_and_guardrails:
    - Intapp says ethical walls and need-to-know rules apply to Celeste exactly as to people (INTAPP-CELESTEGA-2026).
  human_checkpoints:
    - Not described.
  role_evolution: "No source."
  evidence_grade: C
  sources:
    - { ref: INTAPP-CELESTEGA-2026, title: "Intapp announces general availability of Celeste, the expert AI coworker for professional firms", publisher: Intapp, type: vendor, url: "https://www.intapp.com/news/general-availability-celeste/", date: 2026-07-15, access: full, locator: "paragraph 'In legal, it surfaces ... lateral hire lifecycle'" }
    - { ref: LAWSITES-CELESTE-2026, title: "Intapp makes Celeste generally available, calling it an AI coworker to run the business side of law firms", publisher: LawSites (LawNext), type: press, url: "https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html", date: 2026-07-16, access: full, locator: "paragraph on lateral hiring" }
    - { ref: INTAPP-INTAKE-2026, title: "AI-driven client onboarding for regulated professional firms (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/intake/", date: 2026-10-19, access: full, locator: "'Protect confidential information'" }
  last_reviewed: 2026-10-19
  notes: "Lateral hiring itself is a talent-learning topic; only the conflicts pre-screen belongs here."

- id: professional-services-acceptance-risk-15
  title: In-house legal front door that routes, completes and logs business requests (in-house)
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [transaction-processing, client-interaction]
  pattern: service-agent-escalation
  ladder: augment
  change_scope: process
  runtime_class: workflow-automation
  maturity: piloting
  problem: >-
    In-house teams get a stream of incomplete requests (a contract to check, a supplier to approve). Business teams stall or proceed
    without legal input and take on risk legal never sees.
  solution: >-
    In-house, vendor-described. Legora's Intake (available in Slack) has an agent read each request, ask for missing details,
    route it to the right team as a tracked task, and prepare a first draft from the team's playbooks; the default is that a lawyer
    reviews every piece of work. Routine, pre-approved requests such as a standard NDA can be completed and returned without
    review. Harvey's Intake routes requests from email, Jira, Slack and others to approved agents or lawyers and keeps an audit trail.
  outcomes:
    - lever: capacity
      description: "none published. Legora cites the ACC 2026 benchmark median of 367 employees per in-house lawyer as the problem, not as a result."
      figure: none published
      measures: "not applicable: product launch; the 367 figure (employees per in-house lawyer, ACC 2026 benchmark, as cited by Legora) is context, not an outcome"
      provenance: vendor-published
      source_ref: LEGORA-INTAKE-2026
  prerequisites:
    - Team playbooks and request types defined; per-type rules for review versus auto-completion.
  risks_and_guardrails:
    - Legora's general counsel says she needed to know who owns the answer before letting an agent answer the business, and that in Intake a lawyer always does (LEGORA-INTAKE-2026).
    - Harvey lets teams set routing, access and review rules, with a clear owner and status on each request (HARVEY-INTAKE-2026).
  human_checkpoints:
    - Lawyer reviews each piece of work by default; routine pre-approved types can bypass review.
  role_evolution: >-
    Legora says routine work such as security questionnaires stops landing on the most senior people (LEGORA-INTAKE-2026).
  evidence_grade: B
  sources:
    - { ref: LEGORA-INTAKE-2026, title: "Legora launches Intake: an agentic front door for in-house legal teams", publisher: Legora, type: vendor, url: "https://legora.com/newsroom/legora-launches-intake-an-agentic-front-door-for-in-house-legal-teams", date: "2026-10", access: full, locator: "paragraphs 1-8" }
    - { ref: HARVEY-INTAKE-2026, title: "Intake: move every request toward resolution (product page)", publisher: Harvey, type: vendor, url: "https://www.harvey.ai/platform/intake", date: 2026-10-19, access: full, locator: "sections 'Give Your Team a Head Start', 'Stay in Control of Every Request'; Carvana quote" }
  last_reviewed: 2026-10-19
  notes: >-
    In-house. This is a client-side request front door, adjacent to firm client acceptance; it may belong to a legal-operations extension. B rests on Carvana's senior corporate counsel appearing as a named Harvey design partner and on Legora's own general counsel partnering on the design; no results are published. Legora's release is dated within 12-19 Oct 2026 per the newsroom listing (exact day not confirmed); Harvey's page is undated (access date).

- id: professional-services-acceptance-risk-16
  title: Early opportunity screening against conflicts before a pitch or proposal advances
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [review-assurance]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: workflow-automation
  maturity: announced
  problem: >-
    Pitching for work that later fails conflicts wastes pursuit effort and embarrasses the firm.
  solution: >-
    Intapp says its conflicts product can screen opportunities before they advance to formal review. For ChatGPT Enterprise users
    the Celeste plug-in is described as sourcing opportunities on work the firm has already cleared for conflicts.
  outcomes:
    - lever: speed
      description: none published
      figure: none published
      measures: "not applicable: announced capability"
      provenance: vendor-published
      source_ref: INTAPP-CONFLICTS-2026
  prerequisites:
    - Conflicts data connected to CRM and pipeline.
  risks_and_guardrails:
    - Early screens use thinner information than a formal intake; no false-negative rate is published.
  human_checkpoints:
    - Formal review follows before acceptance.
  role_evolution: "No source."
  evidence_grade: C
  sources:
    - { ref: INTAPP-CONFLICTS-2026, title: "AI-powered conflicts management (product page)", publisher: Intapp, type: vendor, url: "https://www.intapp.com/conflicts/", date: 2026-10-19, access: full, locator: "'Spot conflicts early'" }
    - { ref: INTAPP-OPENAI-2026, title: "Intapp collaborates with OpenAI to bring frontier AI to the business of law", publisher: Intapp, type: vendor, url: "https://www.intapp.com/news/intapp-celeste-for-openai-for-law/", date: 2026-09-17, access: full, locator: "bullet list under 'Entitled access'" }
  last_reviewed: 2026-10-19
  notes: "Overlaps with pursuit-proposals; the conflicts screen itself belongs here."

- id: professional-services-acceptance-risk-17
  title: Small-firm conflicts-check agent with corporate-family mapping and fuzzy matching
  archetype: professional-services
  module: acceptance-risk
  function: risk-compliance-legal
  work_types: [review-assurance, research-synthesis]
  pattern: intake-triage
  ladder: augment
  change_scope: step
  runtime_class: background-agent
  maturity: piloting
  problem: >-
    A small firm clears conflicts with a spreadsheet and partner memory, missing relationships hidden behind different entity names
    or corporate parents.
  solution: >-
    The writer describes a four-stage agent: it ingests new-matter details, maps corporate hierarchies from a state registry and
    firm records, runs fuzzy and opposing-party searches across the client database, and scores each potential match by risk.
  outcomes:
    - lever: speed
      description: "The write-up says conflicts-check time fell from 2-3 hours per new matter to 8 minutes. The firm is unnamed (a 14-attorney Nashville firm) and the page is a builder's own account."
      figure: "2-3 hours to 8 minutes per new matter"
      measures: "time per new-matter conflicts check, as stated by the author for one unnamed firm; no sample size or method"
      provenance: vendor-published
      source_ref: ADAI-CONFLICT-2026
  prerequisites:
    - Client history digitised with related entities; a registry data source.
  risks_and_guardrails:
    - The author says the first version flagged too aggressively (common surnames, generic names, registered agents), so the managing partner spent more time dismissing false positives than on the manual checks; thresholds were tuned over three weeks.
  human_checkpoints:
    - The managing partner decides on flagged matches.
  role_evolution: "Managing partner no longer runs the manual search (author's account)."
  evidence_grade: C
  sources:
    - { ref: ADAI-CONFLICT-2026, title: "The Conflict Check Agent", publisher: AdAI (newsletter), type: vendor, url: "https://www.adai.news/p/ai-conflict-check-agent-law-firm-case-study", date: 2026-02-23, access: full, locator: "TL;DR; 'What We Built'; the section on false positives" }
  last_reviewed: 2026-10-19
  notes: "Unnamed organisation, self-published by the builder, no independent check: usable as a signal about false-positive tuning only. Not counted as a named deployment."
```

## 3. Module notes

### Processes and key steps (with work types)

- **Opportunity pre-screen** against conflicts before a pitch advances (review-assurance). Use case 16.
- **New business intake request**: fee earner enters client, matter, parties; reviewers get the request (transaction-processing, document-production). Use cases 02, 03.
- **Conflicts search and clearance**: build search, read hits, resolve, record, decide waivers and screens (review-assurance, research-synthesis, expert-judgment). Use cases 01, 17.
- **Client due diligence, KYC and AML**: identity, beneficial ownership, sanctions and PEPs, adverse media, source of funds; risk rating and routing (research-synthesis, review-assurance). Use cases 05, 06, 07.
- **Engagement risk assessment and approval**: risk scoring, independence and ethics checks, partner and risk-team sign-off (expert-judgment, review-assurance). Use cases 03, 12.
- **Engagement letter, terms and client guidelines**: draft letters, capture and apply outside counsel guidelines (document-production, transaction-processing). Use cases 08, 11.
- **Ethical walls and information barriers** (review-assurance, software-systems). Use case 10.
- **Continuance and monitoring** after acceptance (data-reporting, review-assurance). Use case 04.
- **Client AI terms and disclosure** (client-interaction, review-assurance). Use case 09.
- **Lateral-hire conflicts** (review-assurance). Use case 14.

### Common pain points

- Acceptance run on email chains and paper took days to weeks; lawyers bypassed it (Loeb & Loeb, INTAPP-LOEB-2021). Partners lacked visibility into acceptance status (BDO Canada, INTAPP-BDOCA-2025).
- Conflict decisions depend on tacit history that is not in any database (hypothetical but representative, TRI-PREMORTEM-2026).
- Re-keying data and long requests for reviewers (INTAPP-INTAKE-2026).
- Weak client and matter risk assessment on files: SRA supervision found 39% of client and matter risk assessments ineffective or incomplete (VINCI-SRA-2025, secondary).
- Clients' AI rules differ, and firms need to know which tool may be used where (LAYER3-OCG-2026; JENNER-SANDPIPER-2026).

### Metrics and benchmarks

All of these are workflow or regulator figures. None measures AI quality in this module.

- BDO Canada: more than 5,000 acceptances a month on average since January 2025; described as a 38% improvement versus before with the same resources (vendor-published, INTAPP-BDOCA-2025).
- Sandberg Phoenix: three times as many matters opened, "significantly" fewer errors (vendor-published, INTAPP-SANDBERG-2025).
- Loeb & Loeb: conflicts team from about 200 to sometimes 800 requests a month; weeks to hours for new business intake; growth explains part (vendor-published, INTAPP-LOEB-2021, 2021).
- SRA 2025 AML report as summarised by VinciWorks: 935 supervisory engagements; 270 firms (32%) found non-compliant; 39% of client and matter risk assessments ineffective or incomplete; 92% of firms screen new clients against sanctions lists versus 79% re-checking existing clients (independent regulator data, secondary summary, VINCI-SRA-2025). The same article gives two different source-of-funds shortfall figures (18% and 25%), so neither is used.
- ILTA 2026 survey (Q3.18): share of firms whose policies include "Must obtain client approval" for generative AI rises from 8% (under 50 lawyers) to 20%, 24%, 38% and 34% across larger bands (50-149, 150-349, 350-699, over 700) (survey, ILTA-TECHSURVEY-2026, p. 5). Measure: percent of responding firms in each size band selecting that description of their official generative AI policy.
- ACC/Everlaw 2025 survey of 657 in-house professionals: 61% plan to push for change in how outside counsel services are delivered and priced; 59% report no GenAI savings from law firms yet (survey, ACC-EVERLAW-2025). This is the client pressure behind AI terms, not an acceptance metric.
- Intapp (vendor claims): Conflicts and Intake used by more than 10 of the top 25 accounting firms; Walls used by over 70 Am Law 100 firms (INTAPP-CONFLICTS-2026; INTAPP-WALLS-2026).
- **Quality evidence on AI is absent.** No error rate, override rate, parallel-run result, inspection finding or independent benchmark was found for AI in conflicts, KYC or acceptance. The only false-positive evidence is one builder's unverified account (ADAI-CONFLICT-2026) and a practitioner remark about alert fatigue (VINCI-AML-2026).

### Guardrails and regulatory points

- **California (2026)** says lawyers must not let agentic systems make substantive legal determinations without meaningful lawyer supervision; it names "autonomously facilitating client intake" as an agentic example; it warns about cross-matter disclosure from agents with persistent access; and it says lawyers must follow client guidelines that restrict AI. It also notes AI use in screening clients or candidates may carry bias risk (CALBAR-GENAI-2026, pp. 2, 5-7, 9).
- **ABA Opinion 512 (2024-07-29)**: informed consent is needed before inputting client information into many self-learning tools; boilerplate in engagement letters is not enough; disclosure is required when engagement terms or OCGs require it; the opinion also flags ethical-wall bypass (ABA-OP512-2024, pp. 7-8).
- **IESBA (June 2026 snapshot)**: technology revisions to the Code, approved in 2023 and effective December 2024, require understanding technology outputs, name automation bias, extend confidentiality to the data lifecycle (client data for AI training needs authorisation), and reinforce independence provisions. A technology guidance note is planned for Q3 2026 and an AI-specific one for Q4 2026 (IESBA-SNAPSHOT-2026).
- **ACCA / UK tax (Sept 2026)**: the January 2026 PCRT update recommends disclosing AI use in the engagement letter and, where AI is fundamental, telling the client first (ACCA-ENGLETTERS-2026).
- **PCAOB QC 1000**: effective date postponed to 15 Dec 2026 (PCAOB-QC1000-2025). I did not read its acceptance and continuance provisions.
- **UK AML**: practitioners expect the move from SRA to FCA supervision and tougher evidence standards; they keep acceptance decisions human-led (VINCI-AML-2026). The SRA page itself was blocked.

### Frontier signals (dated, sourced)

- 2026-02-23: Intapp and Harvey announce plans to enforce ethical walls inside Harvey (INTAPP-HARVEY-2026). 2026-03-02: Intapp's COO says speed needs checks and safeguards (INTAPP-GLP-2026).
- 2026-05: California issues agentic-AI guidance covering intake and confidentiality (CALBAR-GENAI-2026).
- 2026-06: IESBA says it is not changing the Code further and plans guidance notes (IESBA-SNAPSHOT-2026).
- 2026-07-15: Celeste generally available, with conflicts, intake, pricing and lateral-hiring playbooks (INTAPP-CELESTEGA-2026).
- 2026-08-04: Intapp reports it is expanding its Moody's partnership to bring credit risk, entity screening and ownership data into Celeste (company-reported, INTAPP-Q4-2026).
- 2026-09-01: A CIBA article argues the independence rules do not cover AI-tool vendors (CIBA-INDEP-2026).
- 2026-09-17: Celeste plug-in for ChatGPT Enterprise announced, including checking captured work against client outside counsel guidelines (INTAPP-OPENAI-2026).
- 2026-10: Legora and Harvey launch in-house Intake products (LEGORA-INTAKE-2026; HARVEY-INTAKE-2026). 2026-10-08: roundtable on AI reshaping OCGs and engagement letters (JENNER-SANDPIPER-2026).

### Workforce and role effects

- Reviewer role shifts from doing the search to confirming AI categorisations (Fredrikson & Byron's risk counsel, INTAPP-FREDRIKSON-2024).
- Firms with growth through lateral hiring expect the conflicts and intake teams to cope with volume (BakerHostetler, INTAPP-CELESTEGA-2026).
- Public hiring signals show no AI duty yet: one conflicts-analyst posting (Sept 2026) asks for Intapp, iManage and Aderant experience and three years of law-firm conflicts work (VIRTUALVOCATIONS-2026). Three other 2026 postings (Bond Schoeneck & King, Alston & Bird, DLA Piper) were described in search results only and could not be opened; a search summary says none mentions AI.
- Professional-liability risk management is a stated concern: Swiss Re Corporate Solutions and Wickard announced AI risk education for law firms (27 Aug 2026), covering supervision, confidentiality and internal AI approval processes (SWISSRE-WICKARD-2026).

### Objections and concerns practitioners raise

- Undocumented, tacit knowledge makes conflicts a poor first target for agents; human review can become theatre (TRI-PREMORTEM-2026, scenario).
- Alert fatigue and false positives when screening is not tuned (VINCI-AML-2026; ADAI-CONFLICT-2026).
- Electronic checks are weak on context and complex structures (VINCI-AML-2026).
- A clause in the engagement letter is not a control (ACCA-ENGLETTERS-2026; ABA-OP512-2024).
- Clients use AI adoption as leverage on fees, and some guidelines say they will not pay for work AI performed (TRI-LEGALWEEK-2026).
- Whether disclosing every AI use is practical; "a ghost around every corner" (Bloomberg Law Nov 2023, EY tax innovation leader, BLOOMBERGLAW-DISCLOSURE-2023; older than the window).
- AI vendors as an independence question (CIBA-INDEP-2026).

### Interview probes for an advisor

1. Think of the last conflict that was missed or nearly missed. Where did the deciding knowledge live: the database, documents, or one person's head? Could a new analyst find it?
2. Who signs the acceptance decision, and what would they need to see in a generated summary or risk report to trust it? Do you measure how often reviewers change or reject a hit triage, a risk rating or a summary?
3. How do client AI restrictions (guidelines, engagement letters, consent) reach the matter team and the tools they use? Who confirms that a tool is on the client's list?
4. How do your ethical walls apply to AI assistants and agents? Can an assistant see across matters?
5. For KYC and independence, what share of alerts or hits are false positives today, who tunes thresholds, and what is the cost of a miss compared with a false flag?

## 4. Routed to other modules

- **quality-review**: the Deloitte Australia AI-error refund and disclosure case is already in the landscape (CTV-DELOITTE-2025). Engagement risk when the firm's own AI-assisted deliverable is the exposure belongs there. PCAOB QC 1000 as a quality-management standard also belongs there.
- **client-development**: CalBar's example of "autonomously facilitating client intake" at the website lead stage, Intapp DealCloud relationship intelligence (Wotton Kearney, Forvis Mazars Capital Advisors, Sept and July 2026 releases) and opportunity sourcing. I read the Forvis Mazars and Wotton Kearney releases; both are about relationship and deal workflows, not acceptance.
- **scoping-pricing**: client demands that AI savings be shared in fees, AI line items on invoices and "will not pay for AI-done work" guidelines (TRI-LEGALWEEK-2026; LAYER3-OCG-2026 billing clause; CALBAR-GENAI-2026 billing row).
- **billing-collections** (landscape module; merged into firm-finance in the new ids): Intapp Time and Billstream surfacing client billing guidelines at time entry (INTAPP-TERMS-2026).
- **talent-learning**: lateral-hire onboarding as a people process; role effects on junior conflicts and intake staff.
- **knowledge-management**: Celeste's retrieval of relevant matters, partner experience and pitch materials (INTAPP-CELESTEGA-2026).
- **firm-finance**: Intapp's FY26 results (cloud ARR, new clients) as vendor business signals (INTAPP-Q4-2026).
- **In-house / legal operations**: Harvey and Legora Intake (use case 15) could move to a legal-operations extension.

## 5. Sources

Format: ref | title | publisher | type | URL | date | access. All were opened ("full") unless marked search-only.

| Ref | Title | Publisher | Type | URL | Date | Access |
|---|---|---|---|---|---|---|
| CALBAR-GENAI-2026 | Practical Guidance for the Use of Generative AI in the Practice of Law | State Bar of California, COPRAC | regulator | https://www.calbar.ca.gov/sites/default/files/portals/0/documents/ethics/Generative-AI-Practical-Guidance.pdf | 2026-05 | full |
| ABA-OP512-2024 | Formal Opinion 512: Generative Artificial Intelligence Tools | American Bar Association | professional-body | https://www.lawnext.com/wp-content/uploads/2024/07/aba-formal-opinion-512.pdf | 2024-07-29 | full |
| IESBA-SNAPSHOT-2026 | IESBA Snapshot: Ethics and Independence Approach to the Use of Technology | IESBA | standard-setter | https://www.ethicsboard.org/news-events/2026-06/iesba-snapshot-ethics-and-independence-approach-use-technology | 2026-06 | full |
| IESBA-TECHPAGE-2026 | Technology: Ethics and Independence Considerations (focus area page) | IESBA | standard-setter | https://www.ethicsboard.org/focus-areas/technology-ethics-independence-considerations | 2026-10-19 | full |
| PCAOB-QC1000-2025 | PCAOB postpones effective date of QC 1000 and related standards, rules, and forms | PCAOB | regulator | https://pcaobus.org/news-events/news-releases/news-release-detail/pcaob-postpones-effective-date-of-qc-1000-and-related-standards--rules--and-forms | 2025-08 | full (via text mirror) |
| ACCA-ENGLETTERS-2026 | Engagement letters, AI and PCRT | ACCA | professional-body | https://www.accaglobal.com/gb/en/technical-activities/uk-tech/in-practice-ezine-archive/In-Practice-archive-2026/september/Engagement-letters-AI-and-PCRT.html | 2026-09 | full |
| CIBA-INDEP-2026 | AI Audit Tools and the Independence Gap Nobody Fixed | Accounting Weekly (CIBA author) | professional-body | https://www.accountingweekly.com/trending-news/ai-audit-tools-and-the-independence-gap-nobody-fixed | 2026-09-01 | full |
| ILTA-TECHSURVEY-2026 | ILTA Technology Survey 2026 Executive Summary | ILTA | survey | https://higherlogicdownload.s3.amazonaws.com/ILTANET/ce7f3e74-fb70-402e-a1b3-5dc0abe72260/UploadedImages/Misc%20PDFs/2606_ILTA_Executive_Summary_FINAL__1_.pdf | 2026-06 | full |
| ACC-EVERLAW-2025 | ACC/Everlaw GenAI Strategic Value for Corporate Law Departments (press release) | Everlaw and ACC | survey | https://blog.everlaw.com/press/release/acc-report-2025 | 2025-10-14 | full |
| TRI-LEGALWEEK-2026 | Couples counseling at Legalweek 2026: firms and clients confront the AI value divide | Thomson Reuters Institute | conference | https://www.thomsonreuters.com/en/institute/articles/legalweek-2026-firm-client-divide | 2026-03-13 | full |
| TRI-PREMORTEM-2026 | Premortem: Your 2028 agentic AI pilot program failed | Thomson Reuters Institute | press | https://www.thomsonreuters.com/en/insights/articles/premortem-your-2028-agentic-ai-pilot-program-failed | 2026-02-18 | full |
| JENNER-SANDPIPER-2026 | Partner John Storino to speak at Sandpiper Partners' AI and Outside Counsel Guidelines Roundtable | Jenner & Block | conference | https://www.jenner.com/print/v2/content/103115/partner-john-storino-to-speak-at-sandpiper-partners-ai-and-outside-counsel-guidelines-roundtable.pdf | 2026-10-08 | full |
| SWISSRE-WICKARD-2026 | Swiss Re Corporate Solutions and Wickard announce offering focused on AI risk management and education for law firms | National Law Review (press release) | press | https://natlawreview.com/press-releases/swiss-re-corporate-solutions-and-wickard-announce-offering-focused-ai-risk | 2026-08-27 | full |
| MORGANLEWIS-WEBINAR-2025 | When Your Law Firms Use GenAI: In-House Counsel's Survival Guide to Avoid Scary Surprises (webinar listing) | Morgan Lewis | firm | https://www.morganlewis.com/events/2025/10/when-your-law-firms-use-genai-in-house-counsels-survival-guide-to-avoid-scary-surprises | 2025-10-30 | full (listing only; no session content) |
| BLOOMBERGLAW-DISCLOSURE-2023 | Law firms wrestle with how much to tell clients about AI use | Bloomberg Law | press | https://news.bloomberglaw.com/legal-ethics/law-firms-wrestle-with-how-much-to-tell-clients-about-ai-use | 2023-11-29 | full (older than window; foundation) |
| LAYER3-OCG-2026 | AI Provisions in Outside Counsel Guidelines: A Compliance Guide for Law Firms | Layer3 Labs | vendor | https://www.layer3labs.io/guides/ai-provisions-outside-counsel-guidelines | 2026-09 | full |
| VINCI-AML-2026 | AML compliance in 2026: What UK law firms are asking now | VinciWorks | community | https://vinciworks.com/blog/aml-compliance-in-2026-what-uk-law-firms-are-asking-now/ | 2026-01-28 | full |
| VINCI-SRA-2025 | The SRA releases its 2025 AML annual report. What does it mean for your firm? | VinciWorks | community | https://vinciworks.com/blog/the-sra-releases-its-2025-aml-annual-report-what-does-it-mean-for-your-firm/ | 2025-11-03 | full (secondary; SRA page blocked) |
| INTAPP-CONFLICTS-2026 | AI-powered conflicts management (product page) | Intapp | vendor | https://www.intapp.com/conflicts/ | 2026-10-19 | full (via text mirror; page undated) |
| INTAPP-INTAKE-2026 | AI-driven client onboarding for regulated professional firms (product page) | Intapp | vendor | https://www.intapp.com/intake/ | 2026-10-19 | full (via text mirror; page undated) |
| INTAPP-TERMS-2026 | Intapp Terms (product page) | Intapp | vendor | https://www.intapp.com/terms/ | 2026-10-19 | full (via text mirror; page undated) |
| INTAPP-WALLS-2026 | Intapp Walls: information barriers for AI (product page) | Intapp | vendor | https://www.intapp.com/walls/ | 2026-10-19 | full (via text mirror; page undated) |
| INTAPP-ACCT-ACCEPT-2026 | Business acceptance and continuance solution for accounting firms | Intapp | vendor | https://www.intapp.com/accounting/client-onboarding-continuance/ | 2026-10-19 | full (via text mirror; page undated) |
| INTAPP-EMPCOMP-2026 | Intapp Employee Compliance (product page) | Intapp | vendor | https://www.intapp.com/employee-compliance/ | 2026-10-19 | full (via text mirror; not AI-specific) |
| INTAPP-BDOCA-2025 | How BDO Canada increased efficiency by 38% during client and engagement acceptance | Intapp | vendor | https://www.intapp.com/case-study/bdo-canada-acceptance-intapp-intake/ | 2025-08-14 | full |
| INTAPP-SANDBERG-2025 | How Sandberg Phoenix improved efficiency and client service | Intapp | vendor | https://www.intapp.com/case-study/sandberg-phoenix-growth-productivity/ | 2025-08-13 | full |
| INTAPP-LOEB-2021 | How Loeb & Loeb transformed new business onboarding | Intapp | vendor | https://www.intapp.com/case-study/loeb-and-loeb/ | 2021-08-16 | full |
| INTAPP-BDOAU-2024 | How BDO Australia implemented an automated end-to-end conflicts clearance process | Intapp | vendor | https://www.intapp.com/case-study/bdo-australia-implements-automated-conflicts-clearance-process-intapp-conflicts/ | 2024-01-18 | full |
| INTAPP-FREDRIKSON-2024 | How Fredrikson & Byron centralized and improved management of outside counsel guidelines with Intapp Terms | Intapp | vendor | https://www.intapp.com/case-study/fredrikson-ocgs-intapp-terms/ | 2024-12-02 | full |
| INTAPP-BAKERBOTTS-2024 | How Baker Botts prioritizes security and agility using Intapp products | Intapp | vendor | https://www.intapp.com/case-study/baker-botts/ | 2024-01-02 | full (cloud migration of intake and conflicts; no AI; not used as evidence) |
| INTAPP-CELESTEGA-2026 | Intapp announces general availability of Celeste | Intapp | vendor | https://www.intapp.com/news/general-availability-celeste/ | 2026-07-15 | full |
| LAWSITES-CELESTE-2026 | Intapp makes Celeste generally available... | LawSites (LawNext) | press | https://www.lawnext.com/2026/07/intapp-makes-celeste-generally-available-calling-it-an-ai-coworker-to-run-the-business-side-of-law-firms.html | 2026-07-16 | full |
| INTAPP-HARVEY-2026 | Intapp to partner with Harvey bringing ethical wall enforcement directly into the platform | Intapp | vendor | https://www.intapp.com/news/intapp-harvey-partner/ | 2026-02-23 | full |
| INTAPP-GLP-2026 | Global Legal Post: Intapp strikes deals with Anthropic and Harvey (excerpt on Intapp site) | Intapp | press | https://www.intapp.com/news/global-legal-post-intapp-anthropic-harvey/ | 2026-03-02 | full (excerpt only) |
| INTAPP-OPENAI-2026 | Intapp collaborates with OpenAI to bring frontier AI to the business of law | Intapp | vendor | https://www.intapp.com/news/intapp-celeste-for-openai-for-law/ | 2026-09-17 | full |
| INTAPP-PRACTUS-2026 | Practus LLP deploys Intapp's agentic AI solutions | Intapp | vendor | https://www.intapp.com/news/practus-auxana-intapp/ | 2026-09-01 | full (Conflicts used two years; Intake added; no figures) |
| INTAPP-Q4-2026 | Intapp announces fourth quarter and fiscal year 2026 financial results | Intapp | vendor | https://s206.q4cdn.com/284424942/files/doc_earnings/2026/q4/earnings-result/Q4-26-Press-Release.pdf | 2026-08-04 | full |
| FENERGO-GT-2026 | Grant Thornton UK selects Fenergo to streamline client onboarding and drive efficiency | Fenergo | vendor | https://resources.fenergo.com/newsroom/grant-thornton-uk-selects-fenergo-to-streamline-client-onboarding-and-drive-efficiency | 2026-03-03 | full |
| XAPIEN-PINSENT-2026 | Pinsent Masons case study | Xapien | vendor | https://xapien.com/case-studies/pinsent-masons/ | 2026-10-19 | full (via text mirror; page undated) |
| XAPIEN-PINSENT-EBOOK-2025 | How Pinsent Masons automates 90% of client onboarding to save £16m (ebook summary) | Xapien | vendor | https://xapien.com/ebook/how-pinsent-masons-automates-90-of-client-onboarding-to-save-16m/ | 2025-11-06 | full (summary only) |
| XAPIEN-IDD-2024 | How a law firm merged initial due diligence into client onboarding | Xapien | vendor | https://xapien.com/how-a-law-firm-merged-initial-due-diligence-into-client-onboarding/ | 2024-02-01 | full |
| LEGORA-INTAKE-2026 | Legora launches Intake: an agentic front door for in-house legal teams | Legora | vendor | https://legora.com/newsroom/legora-launches-intake-an-agentic-front-door-for-in-house-legal-teams | 2026-10 | full (via text mirror) |
| HARVEY-INTAKE-2026 | Intake: move every request toward resolution | Harvey | vendor | https://www.harvey.ai/platform/intake | 2026-10-19 | full (page undated) |
| KINGLAND-CEA-2026 | Client & Engagement Acceptance (product page) | Kingland | vendor | https://www.kingland.com/client-engagement-acceptance | 2026-10-19 | full (page undated) |
| ORBILU-ADVERSE-2025 | An Agentic LLM Framework for Adverse Media Screening in AML Compliance | University of Luxembourg (ORBilu) | academic | https://orbilu.uni.lu/handle/10993/67145 | 2025-12-29 | full (abstract only; via text mirror) |
| ADAI-CONFLICT-2026 | The Conflict Check Agent | AdAI newsletter | vendor | https://www.adai.news/p/ai-conflict-check-agent-law-firm-case-study | 2026-02-23 | full |
| VIRTUALVOCATIONS-2026 | Conflicts Analyst (remote job posting) | Virtual Vocations (employer not shown) | job-posting | https://www.virtualvocations.com/job/conflicts-analyst-3264522-i.html | 2026-09-22 | full (summary; full description behind membership) |
| LEGALTECH-CELESTE-2026 | Intapp bets on 'firm AI' with general release of Celeste | Legal Technology | press | https://legaltechnology.com/intapp-bets-on-firm-ai-with-general-release-of-celeste/ | 2026-07 | search-only (page blocked) |
| ACC-AIGUIDE-2026 | Ethical Use of AI in Litigation (ACC slides prepared by Alston & Bird) | Association of Corporate Counsel | professional-body | https://www.acc.com/sites/default/files/2026-01/Ethical-Use-of-AI-in-Litigation.pdf | 2026-01 | search-only (403) |
| JOBS-OTHER-2026 | Conflicts and new business intake postings at Bond Schoeneck & King, Alston & Bird, DLA Piper | Employer sites and job aggregators | job-posting | https://www.bsk.com/career-opportunities/new-business-intake-manager | 2026-03 | search-only (pages gone or blocked) |

## 6. Gaps

- **No quality evidence for AI in this module.** No named organisation reports error, override or false-positive rates for AI in conflicts, KYC or acceptance, and I found no inspection findings, parallel runs or independent benchmarks. The only false-positive account is an unnamed firm's own write-up (ADAI-CONFLICT-2026).
- **Big Four and consulting acceptance.** A search for AI in Big Four acceptance, continuance or independence found no announcement and no firm primary document. No AI independence-check tool was found; the live discussion is about AI vendors as an independence threat. McKinsey, BCG, Deloitte, EY, KPMG and PwC primary pages were not reached.
- **Engagement letters.** No 2026 announcement from accounting practice-management vendors or Clio on AI-drafted engagement letters was found. The Sept 2026 ACCA article gives guidance but no deployment.
- **Client AI terms.** I found no primary text of a client's outside counsel guidelines with AI clauses, and no survey counting how many OCGs or engagement letters carry AI terms. The ACC sample guidelines and slides were seen in search only (403).
- **SRA.** The SRA AML annual report and AI pages were blocked (Cloudflare), so SRA figures come through a VinciWorks summary. The claim that the SRA plans AI analytics in 2026 was in that summary only and is not used.
- **Primary text of some regulator items.** PCAOB QC 1000's acceptance and continuance provisions and the AICPA independence proposal (including the "81 comment letters" claim) were not checked at source.
- **Conference and podcast content.** I found no recorded session, podcast or proceedings on AI in conflicts or acceptance. Event listings (Sandpiper roundtable, Swiss Re webinar, Morgan Lewis webinar) give agendas, not content. A podcast search returned no relevant 2026 episode.
- **Dates.** Several vendor product pages are undated (access date used). Legora's Intake release day and Harvey's Intake launch date were not confirmed. The Fenergo, Xapien case-study and Pinsent Masons deployment status was not confirmed by the firms.
- **Job postings.** Only one posting could be opened (employer not named; full description behind membership). The other three were search-only and were not available.
- **Not reached.** Legl, Thirdfort and other law-firm KYC vendor customer data; Thomson Reuters CLEAR and LexisNexis screening documentation; ABA primary page (a mirror copy of Opinion 512 was used); Legal Technology and Law360 articles (blocked).
